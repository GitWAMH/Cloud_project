#Scripts to recommend the N best rated movies by a user-passed genre
from pyspark import *
from pyspark.sql import *
from pyspark.sql.functions import *
import sys
import re

conf = SparkConf().setAppName('Movies_by_year')
sc = SparkContext(conf=conf)
spark = SparkSession.builder.master('local').appName('SparkSQL').getOrCreate()

#Obtains the genre and the number of movies to show by arguments. If the number of>mode = sys.argv[1]
mode = sys.argv[1]
year = sys.argv[2]
movies_to_show = 5 if len(sys.argv)<4 else int(sys.argv[3])
# When the user wants to use the MovieLens datasets
if mode == '-m':
#Obtains the dataframes from the datasets ratings.csv and movies.csv
        df1 = spark.read.option('header','true').csv('ratings.csv')
        df2 = spark.read.option('header','true').csv('movies.csv')

        list_movies = df1.join(df2,'movieId','rightouter') \
                .withColumn('rating', col('rating').cast('float')) \
		.withColumn('year', (1970 + (col('timestamp')/(60*60*24*365))).cast('int')) \
                .select('movieId', 'rating', 'title', 'year') \
                .filter(col('year')==year) \
                .groupBy('movieId','title').avg('rating') \
                .orderBy(col('avg(rating)').desc(),col('title').asc()) \
                .limit(movies_to_show) \
		.show()
                .rdd \
                .map(lambda row: (row[1],row[2])) \
                .collect()

        print(list_movies)
elif mode == '-i':
	df1 = spark.read.csv('title.basics.tsv',sep=r'\t',header=True)
        df2 = spark.read.csv('title.ratings.tsv',sep=r'\t',header=True)
	list_movies = df1.join(df2,'tconst','rightouter') \
		.select('tconst', 'averageRating', 'originalTitle', 'genre') \
		.filter(col('startYear')==genre) \
		.orderBy(col('averageRating').desc(),col('originalTitle').asc()) \
		.limit(movies_to_show) \                                                                                                .rdd \
		.map(lambda row: (row[2],row[1])) \
		.collect()

        print(list_movies)
else:
	print('Mode not selected\n');
