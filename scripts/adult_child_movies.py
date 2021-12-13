#Scripts to recommend the N best rated movies by a user-passed genre
from pyspark import *
from pyspark.sql import *
from pyspark.sql.functions import *
import sys
import re

conf = SparkConf().setAppName('Adult_child_movies')
sc = SparkContext(conf=conf)

spark = SparkSession.builder.appName('SparkSQL').getOrCreate()
spark.sparkContext.setLogLevel('ERROR')

#Obtains the genre and the number of movies to show by arguments.
adult = -1
if sys.argv[1]=='-a':
	adult = 1
elif sys.argv[1]=='-c':
	adult = 0

movies_to_show = 5 if len(sys.argv)<3 else int(sys.argv[2])

# When the user wants to use the MovieLens datasets
df1 = spark.read.csv('title.basics.tsv',sep=r'\t',header=True)
df2 = spark.read.csv('title.ratings.tsv',sep=r'\t',header=True)

if adult != -1:
	list_movies = df1.join(df2,'tconst','rightouter') \
		.select('tconst', 'originalTitle', 'isAdult','averageRating') \
		.filter(col('isAdult')==adult) \
		.orderBy(col('averageRating').desc(),col('originalTitle').asc()) \
		.limit(movies_to_show) \
		.rdd \
		.map(lambda row: (row[1],row[3])) \
		.collect()

	print(list_movies)
else:
	print('Option not selected\n')

