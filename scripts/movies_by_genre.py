from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import sys
import re

conf = SparkConf().setAppName('Movies_by_genre')
sc = SparkContext(conf=conf)
spark = SparkSession.builder.master('local').appName('SparkSQL').getOrCreate()

genre = sys.argv[1]
movies_to_show = 5 if len(sys.argv)<3 else int(sys.argv[2])

df1 = spark.read.option('header','true').csv('ratings.csv')
df2 = spark.read.option('header','true').csv('movies.csv')

list_movies = df1.join(df2,'movieId','rightouter') \
	.withColumn('genre',explode(split(col('genres'),'\\|'))) \
	.withColumn('rating', df1['rating'].cast('float')) \
	.select('movieId', 'rating', 'title', 'genre') \
	.filter(col('genre')==genre) \
	.groupBy('movieId','title').avg('rating') \
	.orderBy(col('avg(rating)').desc()) \
	.limit(movies_to_show) \
	.rdd \
	.map(lambda row: (row[1],row[2])) \
	.collect()

print(list_movies)
