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
df=spark.read.csv("Datasets/ml-20m/movies.csv",header=True)

if (len(sys.argv) == 2):
    movie = sys.argv[1]
    genres = df.select(df["genres"]).where(df["title"].contains(movie))
    if genres is None:
        imdb = spark.read.csv("Datasets/title.akas.tsv/data.tsv",header=True)
        id = df.select(df["titleId"]).where(df["title"].contains(movie))
        ratings=spark.read.csv("Datasets/title.ratings.tsv/data.tsv",header=True)
        score = ratings.select(ratings["averageRating"]).where(ratings["tconst"] == id)
        if (score >=7.5):
            print("It's worth watching. Amazing movie!")
        else:
            print("Not really")

    else:
        id = df.select(df["movieId"]).where(df["title"].contains(movie))
        ratings=spark.read.csv("Datasets/ml-20m/ratings.csv",header=True)
        score = ratings.select(ratings["rating"]).where(ratings["movieId"] == id)
        if (score >=3.75):
            print("It's worth watching. Amazing movie!")
        else:
            print("Not really")

else:
    print("Invalid arguments: The user must provide a movie")