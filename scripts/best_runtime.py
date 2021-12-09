from pyspark import *
import sys
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StringType, IntegerType, DoubleType, BooleanType
from pyspark.sql.functions import col

spark = SparkSession.builder \
        .master("local") \
        .appName("best_runtime") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

df1_drop_cols = ("attributes", "language", "isOriginalTitle", "region")
df1 = spark.read.option('header', 'true').csv("title.akas.tsv", sep=r'\t')
df1 = df1.withColumn("titleId", col("titleId").cast(StringType()))\
         .withColumn("ordering", col("ordering").cast(IntegerType()))\
         .withColumn("title", col("title").cast(StringType()))
df1 = df1.drop(*df1_drop_cols).filter(col("ordering") == 1) #Other way to distinct by just taking the 1 in the order. So we don't have a couple of diffrent titles

df2_drop_cols = ("numVotes")
df2 = spark.read.option('header','true').csv("title.ratings.tsv", sep=r'\t')
df2 = df2.withColumn("tconst",col("tconst").cast(StringType()))\
        .withColumn("averageRating", col("averageRating").cast(DoubleType()))
df2 = df2.drop(*df2_drop_cols)

df3_drop_cols = ("startYear", "endYear", "isAdult", "primaryTitle", "originalTitle", "titleType")
df3 = spark.read.option('header','true').csv("title.basics.tsv", sep=r'\t') 
df3 = df3.withColumn("tconst",col("tconst").cast(StringType()))\
         .withColumn("runtimeMinutes",col("runtimeMinutes").cast(IntegerType()))\
         .withColumn("genres",col("genres").cast(StringType()))
df3 = df3.drop(*df3_drop_cols)

joined_df = df1.join(df2, df1.titleId == df2.tconst, "left")
df1.unpersist(), df2.unpersist()
joined_df = joined_df.join(df3, joined_df.titleId == df3.tconst, "left").orderBy("titleId")
df3.unpersist()
DF = joined_df.drop("tconst", "ordering", "titleID")

rating_level = float(0.0)
if len(sys.argv) == 4 or len(sys.argv) == 1:
        rating_level = ""
        runtime_min = ""
        runtime_max  = ""
        try:
                rating_level = float(sys.argv[1])
                runtime_min = float(sys.argv[2])
                runtime_max = float(sys.argv[3])
        except:
                print("No or wronge Input, default will be assumend")
                rating_level = float(0.0)
                runtime_min = float(1)
                runtime_max = float(10000)
        finally:
                #Best movies in a given min./max. time 
                Best_movie_runtime = DF.filter(DF.runtimeMinutes <= runtime_max)\
                                        .filter(DF.runtimeMinutes >= runtime_min)\
                                        .filter(DF.averageRating >= rating_level)\
                                        .orderBy(DF.averageRating.desc(), DF.runtimeMinutes.desc())
                #Check the output format
                Best_movie_runtime.show()

#This is more for getting insides of the diffrent categories
elif (len(sys.argv) == 5):
        rating_level = ""
        runtime_min = ""
        runtime_max  = ""
        args = ""
        try:
            rating_level = float(sys.argv[1])
            runtime_min = float(sys.argv[2])
            runtime_max = float(sys.argv[3])
            args = sys.argv[4]
        except:
                print("No or wronge Input, default will be assumend")
                rating_level = float(0.0)
                runtime_min = float(1)
                runtime_max = float(10000)
                args = "-avg"
        finally:
                #Agg's of rungtime 
                if runtime_min != 0 or runtime_max != 0:
                        DF_agg = DF.filter(DF.runtimeMinutes <= runtime_max)\
                                        .filter(DF.runtimeMinutes >= runtime_min)\
                                        .filter(DF.averageRating >= rating_level)
                elif runtime_min == 0 and runtime_max == 0 and rating_level == 0:
                        DF_agg = DF
                elif runtime_min == 0 and runtime_max == 0 and rating_level != 0:
                        DF_agg = DF.filter(DF.averageRating >= rating_level)
                else: DF_agg = DF

                if args == "-avg":
                        DF_agg = DF_agg.groupBy("genres")\
                                       .agg(F.avg(DF.runtimeMinutes))\
                                       .orderBy(col("avg(runtimeMinutes)").desc())
                elif args == "-max":
                         DF_agg = DF_agg.groupBy("genres")\
                                        .agg(F.max(DF.runtimeMinutes))
                         DF_agg = DF_agg.orderBy(col("max(runtimeMinutes)").desc())
                elif args == "-min":
                        DF_agg = DF_agg.groupBy("genres")\
                                       .agg(F.min(DF.runtimeMinutes))\
                                       .orderBy(col("min(runtimeMinutes)").asc())                
                elif args == "-sum":
                        DF_agg = DF_agg.groupBy("genres")\
                                       .agg(F.sum(DF.runtimeMinutes))\
                                       .orderBy(col("sum(runtimeMinutes)").desc())
                else: 
                        print("\n\nYou did not select a correct command!\nPossible: \n-avg \n-sum \n-min \n-max \n")
                        exit()
                DF_agg.printSchema()
                #Check the output format
                DF_agg.show()
