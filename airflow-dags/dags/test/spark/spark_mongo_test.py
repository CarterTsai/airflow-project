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
    .format("mongo") \
    .option("spark.mongodb.input.database", "test") \
    .option("spark.mongodb.input.collection", "cart") \
    .option("spark.mongodb.input.connection.uri", "mongodb://test:test@172.27.48.1:27017/test.cart") \
    .load()

df.show()