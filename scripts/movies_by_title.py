from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
import sys

spark = SparkSession\
		.builder\
		.appName("Movies by title")\
		.getOrCreate()


if len(sys.argv) != 2:

	print('Usage: spark-submit movies_by_title.py [\'movie name\']\n*Remember to type your movie name between quotes (\'\')')
	
else:
	title = sys.argv[1]

	#Search in CSV
	df = spark.read.csv('movies.csv', header = 'true')

	matchedMovies = df.select('movieId', 'title')\
					.where(df['title'].contains(title))
	
	if not matchedMovies.rdd.isEmpty():
		for i in matchedMovies.collect():
			print(i[0] + ', ' + i [1])
	#if it's not found in movies.csv, we search in title.basics.tsv
	else:
		df2 = spark.read.csv('title.basics.tsv', sep = r'\t', header = True)
		matchedMovies = df2.select('tconst', 'primaryTitle', 'originalTitle')\
						.where(df2['primaryTitle'].contains(title) | df2['originalTitle'].contains(title))
		if not matchedMovies.rdd.isEmpty():
			for i in matchedMovies.collect():
				print(i[0] + ', ' + i [1] + ', ' + i[2])
		else:
			print('No results were found for the movie \'' + title + '\'')
		
