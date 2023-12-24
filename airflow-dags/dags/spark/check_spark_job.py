from pyspark.sql import SparkSession

def main():
    try:
        spark = SparkSession.builder \
            .appName("TestSpark") \
            .getOrCreate()
        
        df = spark.createDataFrame([(1, 'foo'), (2, 'bar')], ['ID', 'Value'])
        df.show()
        
        print("Spark is working.")
    except Exception as e:
        print(f"Spark test failed: {e}")

if __name__ == "__main__":
    main()