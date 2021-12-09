from pyspark import *
from pyspark.sql import SparkSession
from pyspark.sql.types import StringType, IntegerType, DoubleType, BooleanType
from pyspark.sql.functions import col
from pyspark.sql.functions import concat_ws
import sys

#Related to IMDb-Dataset
spark = SparkSession.builder \
        .master("local") \
        .appName("getRatingPerIMDbType") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

df1_drop_cols = ("attributes", "language", "isOriginalTitle", "region")
df1 = spark.read.option('header', 'true').csv("title.akas.tsv", sep=r'\t')
df1 = df1.withColumn("titleId", col("titleId").cast(StringType()))\
         .withColumn("ordering", col("ordering").cast(IntegerType()))\
         .withColumn("title", col("title").cast(StringType()))\
         .withColumn("types", col("types").cast(StringType()))
df1 = df1.drop(*df1_drop_cols).filter(col("ordering") == 1)
df_types = df1.select("types").distinct()
df_types = df_types.select(concat_ws('/t',df_types.types))
df_types = df_types.withColumnRenamed("concat_ws(/t, types)", "Selectable types")

df2_drop_cols = ("numVotes")
df2 = spark.read.option('header','true').csv("title.ratings.tsv", sep=r'\t')
df2 = df2.withColumn("tconst",col("tconst").cast(StringType()))\
        .withColumn("averageRating", col("averageRating").cast(DoubleType()))
df2 = df2.drop(*df2_drop_cols)

joined_df = df1.join(df2, df1.titleId == df2.tconst, "left")
df1.unpersist(), df2.unpersist()
joined_df = joined_df.drop("tconst", "ordering", "titleID")

try: 
        print("Number of args: " + str(len(sys.argv)))
        if len(sys.argv) == 1:
                #If just one arg is given the script does not do anything
                raise ValueError
        elif len(sys.argv) == 2:
                #If the userer does not not the types he can call help
                _help = sys.argv[1]
                _help = str(_help) 
                if  _help == "-help" or _help == "-h": 
                        print("You can choose from this types of movies:")
                        df_types.show()
                else: raise ValueError
        elif len(sys.argv) == 4:
                #if all args a correct he gets his number of recommandations of one type with a lower rating level
                print("Start processing:")
                selected_type = sys.argv[1]
                rating_level = sys.argv[2]
                count_of_recommandations = sys.argv[3]

                selected_type = str(selected_type)
                rating_level = float(rating_level)
                count_of_recommandations = int(count_of_recommandations)

                df = joined_df.filter(rating_level <= joined_df.averageRating)\
                                .filter(joined_df.types.contains(selected_type.lower()))\
                                .orderBy((joined_df.averageRating).desc())\
                                .limit(count_of_recommandations)\
                                .show(count_of_recommandations)
        else: raise ValueError
except Exception as ex:
        print("\n\nNot fitting args")
        print("Hint: Help will show you the possible types")
        print("The follwoing args have to be provided:")
        print("<IMDb-Type> <Rating_level | [double]> <count_of_recommandations | [int]>\n\n")
        print("For advancted users: ")
        print(type(ex))
