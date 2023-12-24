from datetime import datetime, timedelta
from airflow import DAG
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 9, 10),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'postgresql_spark_submit_dag',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
)

spark_submit_task = SparkSubmitOperator(
    task_id='pg_spark_submit_job',
    conn_id='spark_default',  # 確保這個連接已在 Airflow 中設定好
    application='local:///opt/bitnami/airflow/spark/dags/spark/postgresql_test.py',  # 程式碼的路徑，需根據實際情況修改
    # kubernetes_master='https://api.crc.testing:6443',
    # deploy_mode='cluster',
    executor_cores=1,
    executor_memory='2g',
    driver_memory='1g',
    total_executor_cores=1,
    conf={
        'spark.kubernetes.namespace': 'test-airflow',
        'spark.kubernetes.file.upload.path': '/opt/bitnami/airflow/spark/dags/test_upload',
        'spark.kubernetes.authenticate.driver.serviceAccountName': 'task-pods-serviceaccount',
        'spark.kubernetes.authenticate.executor.serviceAccountName': 'task-pods-serviceaccount',
        'spark.kubernetes.driver.volumes.persistentVolumeClaim.spark-dags.options.claimName': 'spark-dags-pv-claim',
        'spark.kubernetes.driver.volumes.persistentVolumeClaim.spark-dags.mount.path': '/opt/bitnami/airflow/spark/dags',
        'spark.kubernetes.driver.pod.retained': 'false',
        'spark.kubernetes.container.image': 'cartertsai/spark-all:0.0.1'
    },
    verbose=True,
    dag=dag
)

spark_submit_task



