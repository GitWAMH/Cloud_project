#!/usr/bin/python
from pyspark import *
import sys
from pyspark.sql import SparkSession
from pyspark.sql.types import NullType

spark = SparkSession.builder \
        .master("local") \
        .appName("Decision Pelicula") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()

df1 = spark.read.option('header', 'true').csv("/home/lukas/CLO/title.akas.tsv")
df2 = spark.read.option('header','true').csv("/home/lukas/CLO/title.ratings.tsv") 

df1.printSchema()
df2.printSchema()
joined_df = df1.join(df2, df1.titleId == df2.tconst, "left_semi")
##print(joined_df.collect())