from pyspark.sql import SparkSession
import psycopg2

def main():
    try:

        connection = psycopg2.connect(
            host='hippo-pgbouncer',
            database='dbo',
            user='sa',
            password='pT2@LZIL}M8jMvPi)|eOgqLA'
        )

        cursor = connection.cursor()
    
        # SQL 查詢命令
        query = "SELECT * FROM pg_catalog.pg_tables;"
        cursor.execute(query)

        # 獲取並印出結果
        records = cursor.fetchall()
        for record in records:
            print(record)

        # 關閉資源
        cursor.close()
        connection.close()

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