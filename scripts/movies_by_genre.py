#from pyspark import SparkConf, SparkContext
#from pyspark.sql import SparkSession
#from pyspark.sql.functions import *

#Scripts to recommend the N best rated movies by a user-passed genre
from pyspark import *
from pyspark.sql import *
from pyspark.sql.functions import *
import sys
import re

conf = SparkConf().setAppName('Movies_by_genre')
sc = SparkContext(conf=conf)

spark = SparkSession.builder.appName('SparkSQL').getOrCreate()
spark.sparkContext.setLogLevel('ERROR')

#Obtains the genre and the number of movies to show by arguments. If the number of movies is not given by the user, 5 is chosen by default
mode = sys.argv[1]
genre = sys.argv[2]
movies_to_show = 5 if len(sys.argv)<4 else int(sys.argv[3])
# When the user wants to use the MovieLens datasets
if mode == '-m': 
#Obtains the dataframes from the datasets ratings.csv and movies.csv
	df1 = spark.read.option('header','true').csv('ml-20m/ratings.csv')
	df2 = spark.read.option('header','true').csv('ml-20m/movies.csv')

	list_movies = df1.join(df2,'movieId','rightouter') \
		.withColumn('genre',explode(split(col('genres'),'\\,'))) \
		.withColumn('rating', df1['rating'].cast('float')) \
		.select('movieId', 'rating', 'title', 'genre') \
		.filter(lower(col('genre'))==genre.lower()) \
		.groupBy('movieId','title').avg('rating') \
		.orderBy(col('avg(rating)').desc(),col('title').asc()) \
		.limit(movies_to_show) \
		.rdd \
		.map(lambda row: (row[1],row[2])) \
		.collect()

	print(list_movies)
#When the user wants to use th IMDb datasets
elif mode == '-i':
	df1 = spark.read.csv('title.basics.tsv',sep=r'\t',header=True)
	df2 = spark.read.csv('title.ratings.tsv',sep=r'\t',header=True)

	list_movies = df1.join(df2,'tconst','rightouter') \
		.withColumn('genre',explode(split(col('genres'),'\\|'))) \
		.withColumn('rating', col('averageRating').cast('float')) \
		.select('tconst', 'averageRating', 'originalTitle', 'genre') \
		.filter(lower(col('genre'))==genre.lower()) \
		.orderBy(col('averageRating').desc(),col('originalTitle').asc()) \
		.limit(movies_to_show) \
		.rdd \
		.map(lambda row: (row[2],row[1])) \
		.collect()

	print(list_movies)
else:
	print('Error with the mode selection. Select -m to use the MovieLens datasets or -i to use the IMDb datasets\n')
