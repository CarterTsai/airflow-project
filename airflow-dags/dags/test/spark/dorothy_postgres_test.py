from pyspark.sql import SparkSession
import os

spark = SparkSession.builder\
        .appName('test')\
        .getOrCreate()

def read_table_query(sql_query):
    df = spark.read.format("jdbc") \
            .option("url", database_url) \
            .option("query", sql_query) \
            .option("user", POSTGRESQL_USER) \
            .option("password", POSTGRESQL_PASSWORD) \
            .option("driver", jdbc_driver) \
            .load()
    return df

POSTGRESQL_USER = 'postgre'
POSTGRESQL_PASSWORD = '1qaz2wsx'
postgres_db = 'airflow'
database_url = f"jdbc:postgresql://172.27.48.1:5432/{postgres_db}"
jdbc_driver = "org.postgresql.Driver"
ans = read_table_query('select * from public.ab_permission')

ans.show()