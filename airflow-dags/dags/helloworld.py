# 保存此文件為 hello_airflow.py 並放在你的 Airflow DAGs 文件夾裡面

# 引入必要的模組和類
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# 定義Python函數作為我們要執行的任務
def print_hello():
    return 'Hello, Airflow!'

# 定義DAG
default_args = {
    'owner': 'me',
    'depends_on_past': False,
    'email': ['hamming0324@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'hello_airflow',  # DAG的名稱
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval=timedelta(days=1),  # 定義執行間隔為每天一次
    start_date=datetime(2023, 8, 7),  # 定義起始執行日期
    catchup=False,
)

# 將Python函數封裝為Airflow PythonOperator
hello_operator = PythonOperator(
    task_id='print_hello',
    python_callable=print_hello,
    dag=dag,
)

# 設定任務執行順序 (在這裡只有一個任務，所以這步驟可選)
# hello_operator >> another_task (如果你有其他任務的話)

hello_operator