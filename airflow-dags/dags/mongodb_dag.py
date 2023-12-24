from datetime import datetime
from pymongo import MongoClient
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
}

def read_from_mongodb():
    # 建立 MongoDB 連接
    mongo_db_name = 'test'

    # Create the connection string
    # conn_str = f'mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/'
    # 設置 Airflow 變數：
    # 你可以通過 Airflow 的 Web UI 設置變數：

    # 打開 Airflow Web UI。
    # 在左側導航面板中，選擇 "Admin" -> "Variables"。
    # 點擊 "Create"，然後輸入 "Key"（例如 mongo_conn_str）和 "Val"（你的 MongoDB 連接字串）。
    # 或者，你可以使用 Airflow CLI 設置變數：
    # airflow variables --set mongo_conn_str 'mongodb://your_username:your_password@your_mongodb_host:27017/your_database_name'

    conn_str = Variable.get("mongodb_url")

    client = MongoClient(conn_str)
    db = client[mongo_db_name]
    collection = db['cart']
    
    # 讀取數據
    documents = collection.find()
    
    # 這只是一個示例，你可以基於需要進行其他操作
    for doc in documents:
        print(doc)

    client.close()

dag = DAG('mongodb_dag', default_args=default_args, description='A simple DAG to read from MongoDB', schedule_interval=None)

t1 = PythonOperator(
    task_id='read_mongo',
    python_callable=read_from_mongodb,
    dag=dag,
)

t1
