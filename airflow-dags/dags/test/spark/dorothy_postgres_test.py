from pyspark.sql import SparkSession
import os

# dirname = os.path.dirname(__file__)
# print(dirname)
jar_path = '/usr/local/bin/postgresql-42.5.1.jar'
spark = SparkSession.builder\
        .appName('test')\
        .config("spark.jars", jar_path)\
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

POSTGRESQL_USER = 'ap_user'
POSTGRESQL_PASSWORD = 'gszmHNMM'
postgres_db = 'edp'
database_url = f"jdbc:postgresql://emi-pgbouncer:5432/{postgres_db}"
jdbc_driver = "org.postgresql.Driver"
ans = read_table_query('select * from vw_ds_order')

print(ans)