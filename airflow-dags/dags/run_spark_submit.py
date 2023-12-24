# 引入所需的函式庫和類別
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from spark_submit import SparkJob
import os


def get_directory():
    directory = "/opt/bitnami/airflow/dags/spark"
    files = os.listdir(directory)
    # 印出檔案列表
    for file in files:
        print(file)

    return files

def run_spark_submit():
    app = SparkJob('/opt/bitnami/airflow/dags/spark/test.py', master='spark://aiflow-service-spark-master-0.aiflow-service-spark-headless.test-airflow.svc.cluster.local:7077', name='simple-test')
    app.submit()

    while not app.concluded:
        # do other stuff...
        print(app.get_state()) # 'RUNNING'

    print(app.get_output())
    print(app.get_state()) # 'FINISHED'

    return app.get_output()

# 定義 DAG 參數
default_args = {
    'owner': 'me',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# 建立 DAG 實例
dag = DAG(
    'run_spark_submit',              # DAG 名稱
    default_args=default_args,  # 使用先前定義的參數
    description='An spark DAG example',  # DAG 描述
    schedule_interval=timedelta(days=1),  # 設定執行頻率，例如每天執行一次
    start_date=datetime(2023, 8, 10),     # DAG 開始日期
    catchup=False,             # 是否執行過去的排程
)

# 這裡你可以加入任務（tasks）, 但目前是空的 DAG

get_directory_operator = PythonOperator(
    task_id='get_directory',
    python_callable=get_directory,
    dag=dag,
)


run_spark_submit_operator = PythonOperator(
    task_id='run_spark_submit',
    python_callable=run_spark_submit,
    dag=dag,
)

get_directory_operator >> run_spark_submit_operator