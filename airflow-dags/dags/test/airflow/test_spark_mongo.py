from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'test_spark_mongodb_submit_dag',
    default_args=default_args,
    description='An example DAG to submit Spark job',
    start_date=datetime(2023, 9, 10),
    catchup=False
)

spark_submit_cmd = """
/spark/bin/spark-submit \\
--master k8s://https://api.crc.testing:6443 \\
--name spark-py-driver \\
--deploy-mode cluster \\
--driver-memory 1g \\
--executor-memory 1g \\
--executor-cores 1 \\
--total-executor-cores 2 \\
--class my.main.Class \\
--verbose \\
--conf spark.kubernetes.namespace=test-airflow \\
--conf spark.kubernetes.authenticate.serviceAccountName='task-pods-serviceaccount' \\
--conf spark.kubernetes.authenticate.driver.serviceAccountName='task-pods-serviceaccount' \\
--conf spark.kubernetes.driver.volumes.persistentVolumeClaim.spark-dags.options.claimName='spark-dags-pv-claim' \\
--conf spark.kubernetes.driver.volumes.persistentVolumeClaim.spark-dags.mount.path='/spark/dags/' \\
--conf spark.kubernetes.container.image=cartertsai/train-spark:1.0.1 local:///spark/dags/spark_mongo_test.py 
"""

spark_submit_operator = BashOperator(
    task_id='check_spark_with_mongodb_submit_bash_dag',
    bash_command=spark_submit_cmd,
    dag=dag,
)

spark_submit_operator