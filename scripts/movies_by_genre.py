from pyspark import SparkConf, SparkContext
import sys

conf = SparkConf().setAppName('Movies_by_genre')
sc = SparkContext(conf=conf)
