from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import platform
import subprocess
import sys

def print_python_path():
    print(f"Python Executable Path: {sys.executable}")

def get_python():
    # 獲取 Python 版本
    python_version = platform.python_version()
    print(f"Python 版本：{python_version}")

def get_pip_packages():
    # 列出 pip 安裝的套件
    installed_packages = subprocess.getoutput("pip freeze")
    print("\n已安裝的 pip 套件：")
    print(installed_packages)

# 定義 DAG 參數
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# 初始化 DAG
dag = DAG(
    'get_python_and_pip_info',
    default_args=default_args,
    description='A simple DAG to get Python and pip package information',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 8, 28),
    catchup=False,
)

# 添加 PythonOperator 到 DAG
get_python_info_task = PythonOperator(
    task_id='get_python',
    python_callable=get_python,
    dag=dag,
)

get_install_info_task = PythonOperator(
    task_id='get_pip_info',
    python_callable=get_pip_packages,
    dag=dag,
)

get_python_path = PythonOperator(
    task_id='print_python_path',
    python_callable=print_python_path,
    dag=dag,
)

get_python_info_task >> get_install_info_task >> get_python_path