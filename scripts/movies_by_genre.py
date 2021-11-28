from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import sys
import re

conf = SparkConf().setAppName('Movies_by_genre')
sc = SparkContext(conf=conf)
spark = SparkSession.builder.master('local').appName('SparkSQL').getOrCreate()

df1 = spark.read.option('header','true').csv('ratings.csv')
df2 = spark.read.option('header','true').csv('movies.csv')

df3 = df1.join(df2,'movieId','rightouter') \
	.withColumn('genre',explode(split(col('genres'),'\\|'))) \
	.withColumn('rating', df1['rating'].cast('float')) \
	.select('movieId', 'rating', 'title', 'genre') \
	.filter(col('genre')=='Action') \
	.groupBy('movieId','title').avg('rating').alias('avg_rating') \
	.show()
