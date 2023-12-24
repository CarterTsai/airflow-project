from pyspark.sql import SparkSession
from pyspark.sql.functions import col, struct, explode, lit, collect_list, max, when
from pyspark.sql.window import Window
import os


# package file path
# java_path = '/home/jovyan/work/packages/mongo-jar/mongo-java-driver-3.12.14.jar'
# jar_path = '/home/jovyan/work/packages/mongo-jar/mongo-spark-connector_2.12-2.4.0.jar'
java_path = '/usr/local/bin/mongo-java-driver-3.12.14.jar'
jar_path = '/usr/local/bin/mongo-spark-connector_2.12-2.4.0.jar'

mongodb_uri = "mongodb://root:172.27.48.1:27017/?authSource=root" 


spark = SparkSession \
    .builder \
    .appName("myApp") \
    .config('spark.jars', jar_path)\
    .config('spark.driver.extraClassPath', java_path)\
    .config("spark.mongodb.input.uri", mongodb_uri) \
    .config("spark.mongodb.output.uri", mongodb_uri) \
    .getOrCreate()

df = spark.read \
    .format("com.mongodb.spark.sql.DefaultSource") \
    .option("spark.mongodb.input.database", "test") \
    .option("spark.mongodb.input.collection", "cart") \
    .load()

df.show()
