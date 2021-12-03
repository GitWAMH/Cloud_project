#!/usr/bin/python
from pyspark import *
import sys
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder \
        .master("local") \
        .appName("Decision Pelicula") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()
df1 = spark.read.option('header', 'true').csv("title.akas.tsv", sep=r'\t')
df2 = spark.read.option('header','true').csv("title.ratings.tsv", sep=r'\t') 
df3 = spark.read.option('header','true').csv("title.basics.tsv", sep=r'\t') 

df1.printSchema(), df2.printSchema(), df3.printSchema()
joined_df = df1.join(df2, df1.titleId == df2.tconst, "left_semi").join(df3, df1.titleId == df3.tconst, "left_semi")
#Insert drop for unneccasry columns 
#Insert a distinct
df1.unpersist(), df2.unpersist(), df3.unpersist()
#Transform the data in the correct types
DF = joined_df.withColumn("Open", joined_df["Open"].cast(DoubleType()))\
                .withColumn("Open", joined_df["Open"].cast(DoubleType()))\
                .withColumn("Open", joined_df["Open"].cast(DoubleType()))\
                .withColumn("Open", joined_df["Open"].cast(DoubleType()))\
                .withColumn("Open", joined_df["Open"].cast(DoubleType()))\
                .withColumn("Open", joined_df["Open"].cast(DoubleType()))\
                .withColumn("Open", joined_df["Open"].cast(DoubleType()))\
                .distinct()
print(joined_df.collect())
joined_df.unpersist()

rating_level = float(0.0)
if len(sys.argv) == 2 or len(sys.argv) == 0:
        try:
                rating_level = float(sys.argv[1])
                runtime_max = float(sys.argv[2])
        except:
                print("Input wasent a Number")
                rating_level = float(0.0)
                runtime_max = float(100000000000)
        finally:
                #AVG rungtime in a genre 
                DF_avg_runtime_genre = DF.groupBy("genres").agg(F.avg(DF.runtimeMinutes)).orderBy("F.avg(DF.runtimeMinutes)")
                DF_= DF.filter(DF.runtimeMinutes < runtime_max).groupBy("titleId").filter(DF.averageRating > rating_level)
elif (len(sys.argv) == 3):
        try:
            rating_level = float(sys.argv[1])
            runtime_max = float(sys.argv[2])
            if (sys.argv[3] == "yes"): genre = True 
            else: genre = False 
        except:
                print("Input wasent a Number")
                rating_level = float(0.0)
        finally:
                #AVG rungtime in a genre 
                DF_avg_runtime_genre = DF.groupBy("genres").agg(F.avg(DF.runtimeMinutes)).orderBy("F.avg(DF.runtimeMinutes)") 
