#!/usr/bin/python
from pyspark import *
import sys
from pyspark.sql import SparkSession
from pyspark.sql.types import NullType

spark = SparkSession.builder \
        .appName("Decision Pelicula") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()

spark.sparkContext.setLogLevel('ERROR')

df=spark.read.csv("ml-20m/movies.csv",header=True)

if (len(sys.argv) == 2):
    movie = sys.argv[1]
    id = df.select(df["movieId"]).where(df["title"].contains(movie)).first()[0]
    if id is None:
        imdb = spark.read.csv("title.akas.tsv",header=True)
        id = df.select(df["titleId"]).where(df["title"].contains(movie)).first()[0]
        ratings=spark.read.csv("title.ratings.tsv",header=True)
        score = ratings.select(ratings["averageRating"]).where(ratings["tconst"] == id).first()[0]
        if (float(score) >=7.5):
            print("It's worth watching. Amazing movie!")
        else:
            print("Not really")

    else:
        ratings=spark.read.csv("ml-20m/ratings.csv",header=True)
        score = ratings.select(ratings["rating"]).where(ratings["movieId"] == id).first()[0]
        if (float(score) >= 3.75):
            print("It's worth watching. Amazing movie!")
        else:
            print("Not really")

else:
    print("Invalid arguments: The user must provide a movie")
