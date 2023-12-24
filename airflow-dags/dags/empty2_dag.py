# 引入所需的函式庫和類別
from airflow import DAG
from datetime import datetime, timedelta
from airflow.sensors.external_task_sensor import ExternalTaskSensor


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
dags = DAG(
    'empty2_dag',              # DAG 名稱
    default_args=default_args,  # 使用先前定義的參數
    description='An empty DAG example',  # DAG 描述
    schedule_interval=timedelta(days=1),  # 設定執行頻率，例如每天執行一次
    start_date=datetime(2023, 8, 10),     # DAG 開始日期
    catchup=False,             # 是否執行過去的排程
) 
    
wait_for_dag1 = ExternalTaskSensor(
    task_id='wait_for_dag1',
    external_dag_id='empty1_dag',  # 換成你想等待的 DAG 的 ID
    external_task_id=None,     # 如果你想等待特定的任務，填寫這裡。否則，它將等待整個 DAG 完成。
    mode='poke',
)

# 這裡你可以加入任務（tasks）, 但目前是空的 DAG
