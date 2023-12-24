from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
import psycopg2
from airflow.models import Variable
import json

def query_postgresql():
    conn_str_config = Variable.get("pg_connect")
    print(conn_str_config)
    print(type(conn_str_config))
    conn_str = json.loads(conn_str_config)
    print(conn_str)

    # 資料庫連接資訊
    connection = psycopg2.connect(
        host=conn_str['host'],
        database=conn_str['database'],
        user=conn_str['user'],
        password=conn_str['password']
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

# 定義 DAG 參數
default_args = {
    'owner': 'me',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    # 'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# 建立 DAG 實例
dag = DAG(
    'query_postgresql_example',              # DAG 名稱
    default_args=default_args,  # 使用先前定義的參數
    description='An empty DAG example',  # DAG 描述
    schedule=timedelta(days=1),  # 設定執行頻率，例如每天執行一次
    start_date=datetime(2023, 8, 10),     # DAG 開始日期
    catchup=False,             # 是否執行過去的排程
)

# 這裡你可以加入任務（tasks）, 但目前是空的 DAG

hello_operator = PythonOperator(
    task_id='query_postgresql',
    python_callable=query_postgresql,
    dag=dag,
)

hello_operator