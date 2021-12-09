from pyspark.sql import SparkSession
from pyspark.sql.functions import lower
import sys

spark = SparkSession\
		.builder\
		.appName("Movies by title")\
		.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

if len(sys.argv) != 2:

	print('Usage: spark-submit movies_by_title.py [\'movie title\']\n*Remember to type your movie title between quotes (\'\')')
	
else:
	title = sys.argv[1]

	#Search in CSV
	moviesDF = spark.read.csv('ml-20m/movies.csv', header = True)
	ratingsDF = spark.read.csv('ml-20m/ratings.csv', header = True)
	matchedMovies = moviesDF.join(ratingsDF, 'movieId')\
			.withColumn('rating', ratingsDF.rating.cast('float'))\
			.where(lower(moviesDF.title).contains(title.lower()))\
			.groupBy('movieId', 'title').avg('rating')\
			.sort('avg(rating)', ascending = False)
	
	if not matchedMovies.rdd.isEmpty():
		matchedMovies.select('title', 'avg(rating)').show(truncate = False)
	#if it's not found in movies.csv, we search in title.basics.tsv
	else:
		moviesDF = spark.read.csv('title.basics.tsv', sep = r'\t', header = True)
		ratingsDF = spark.read.csv('title.ratings.tsv', sep = r'\t', header = True)
		matchedMovies = moviesDF.join(ratingsDF, 'tconst')\
				.withColumn('averageRating', ratingsDF.averageRating.cast('float'))\
				.select('tconst', 'primaryTitle', 'originalTitle', 'averageRating')\
				.where(lower(moviesDF.primaryTitle).contains(title.lower()) | lower(moviesDF.originalTitle).contains(title.lower()))\
				.sort('averageRating', ascending = False)
		
		if not matchedMovies.rdd.isEmpty():
			matchedMovies.select('primaryTitle', 'originalTitle', 'averageRating').show(truncate = False)
		else:
			print('No results were found for the movie \'' + title + '\'')
		
