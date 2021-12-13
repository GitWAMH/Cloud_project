#!/usr/bin/python
from pyspark import *
import sys
from pyspark.sql import SparkSession
from pyspark.sql.types import NullType
spark = SparkSession.builder \
        .master("local") \
        .appName("Anio e idioma Pelicula") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()
spark.sparkContext.setLogLevel('ERROR')

if (len(sys.argv) > 1):
    data = sys.argv[1]
    if (data.isdigit()):
        year = data
        df=spark.read.csv("title.basics.tsv", sep=r'\t',header=True)
        movies = df.select(df["originalTitle"], df["tconst"]).where(df["startYear"] == year)
        ratings=spark.read.csv("title.ratings.tsv", sep=r'\t', header=True)
        # bestMovies = movies.select(movies["originalTitle"], movies["tconst"]).where(movies["tconst"] == ratings["tconst"]).orderBy(ratings["averageRating"])
        bestMovies = movies.join(ratings, movies["tconst"] == ratings["tconst"], "inner").orderBy(ratings["averageRating"], ascending=False)
        if len(sys.argv) == 3:
            num = sys.argv[2]
        # elif(len(sys.argv) == 4):
        #     num = sys.argv[3]
        else:
            num = 10
        bestMovies.show(num)

    else:
        region = data
        df=spark.read.csv("title.akas.tsv", sep=r'\t',header=True)
        movies = df.select(df["title"], df["titleId"]).where(df["region"] == region)
        if movies.count() == 0:
            rdd = df.select(df["region"]).distinct().rdd.map(lambda row: (row[0])).collect()
            print("Region not found. These are the regions available:\n")
            print(rdd)

        else:
            ratings=spark.read.csv("title.ratings.tsv", sep=r'\t', header=True)
            # bestMovies = movies.select(movies["originalTitle"], movies["tconst"]).where(movies["tconst"] == ratings["tconst"]).orderBy(ratings["averageRating"])
            bestMovies = movies.join(ratings, movies["titleId"] == ratings["tconst"], "inner").orderBy(ratings["averageRating"], ascending=False)
            if len(sys.argv) == 3:
                num = sys.argv[2]
            # elif(len(sys.argv) == 4):
            #     num = sys.argv[3]
            else:
                num = 10
            bestMovies.show(int(num))        

else:
    print("Invalid arguments: The user must provide a year or language to search")
