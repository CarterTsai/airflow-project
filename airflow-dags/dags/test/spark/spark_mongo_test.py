from pyspark.sql import SparkSession
from pyspark.sql.functions import col, struct, explode, lit, collect_list, max, when
from pyspark.sql.window import Window
import os

mongodb_uri = "mongodb://test:test@172.27.48.1:27017/test.cart"

spark = SparkSession \
    .builder \
    .appName("myApp") \
    .config("spark.mongodb.input.uri", mongodb_uri) \
    .config("spark.mongodb.output.uri", mongodb_uri) \
    .getOrCreate()


spark = SparkSession \
    .builder \
    .appName("myApp") \
    .config("spark.mongodb.input.uri", mongodb_uri) \
    .config("spark.mongodb.output.uri", mongodb_uri) \
    .getOrCreate()

df = spark.read \
    .format("mongodb") \
    .option("spark.mongodb.read.database", "test") \
    .option("spark.mongodb.read.collection", "cart") \
    .option("spark.mongodb.read.connection.uri", "mongodb://test:test@172.27.48.1:27017/test.cart") \
    .load()

print(df)