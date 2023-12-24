

# # 如果你有其他任務，你可以這樣設置依賴：
# # run_this >> spark_submit_task >> run_that



# # # 如果你有其他任務，你可以這樣設置依賴：
# # # run_this >> spark_submit_task >> run_that


# # # If you have other tasks, you can set dependencies like this:
# # # run_this >> spark_submit_task >> run_that


# # # # 引入所需的函式庫和類別
# from airflow import DAG
# from datetime import datetime, timedelta
# from airflow.operators.python_operator import PythonOperator
# from spark_submit import SparkJob
# from airflow.models import Variable
# import os


# # # def get_directory():
# # #     directory = "/opt/bitnami/airflow/dags/spark"
# # #     files = os.listdir(directory)
# # #     # 印出檔案列表
# # #     for file in files:
# # #         print(file)

# # #     return files

# def run_spark_submit():

#     spark_args = {
#         'master': 'k8s://https://api.crc.testing:6443',
#         'deploy_mode': 'cluster',
#         'name': 'spark-submit-app',
#         'class': 'my.main.Class',
#         'conf': [
#             "spark.kubernetes.namespace='test-airflow'",
#             "spark.kubernetes.file.upload.path='/opt/bitnami/airflow/spark/dags/test_upload'",
#             "spark.kubernetes.authenticate.driver.serviceAccountName=task-pods-serviceaccount",
#             "spark.kubernetes.driver.volumes.persistentVolumeClaim.spark-dags.options.claimName='spark-dags-pv-claim'",
#             "spark.kubernetes.driver.volumes.persistentVolumeClaim.spark-dags.mount.path='/opt/bitnami/airflow/spark/dags'",
#             "spark.kubernetes.container.image=apache/spark"
#         ],
#         'verbose': True,
#     }

#     app = SparkJob('/opt/bitnami/airflow/dags/spark/check_spark_job.py', **spark_args)

#     print(app.get_submit_cmd())


#     app.submit()

#     while not app.concluded:
#         # do other stuff...
#         print(app.get_state()) # 'RUNNING'

#     print(app.get_output())
#     print(app.get_state()) # 'FINISHED'

#     return app.get_output()

# # 定義 DAG 參數
# default_args = {
#     'owner': 'me',
#     'depends_on_past': False,
#     'email_on_failure': False,
#     'email_on_retry': False,
#     'retries': 1,
#     'retry_delay': timedelta(minutes=5),
# }

# # 建立 DAG 實例
# dag = DAG(
#     'check_spark_with_submit_dag',              # DAG 名稱
#     default_args=default_args,  # 使用先前定義的參數
#     description='An spark DAG example',  # DAG 描述
#     schedule_interval=timedelta(days=1),  # 設定執行頻率，例如每天執行一次
#     start_date=datetime(2023, 8, 10),     # DAG 開始日期
#     catchup=False,             # 是否執行過去的排程
# )

# # 這裡你可以加入任務（tasks）, 但目前是空的 DAG

# # get_directory_operator = PythonOperator(
# #     task_id='get_directory',
# #     python_callable=get_directory,
# #     dag=dag,
# # )


# run_spark_submit_operator = PythonOperator(
#     task_id='run_spark_submit',
#     python_callable=run_spark_submit,
#     dag=dag,
# )

# run_spark_submit_operator
# # # get_directory_operator >> run_spark_submit_operator



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
    'check_spark_with_submit_dag',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
)

spark_submit_task = SparkSubmitOperator(
    task_id='spark_submit_job',
    conn_id='spark_default',  # 確保這個連接已在 Airflow 中設定好
    application='local:///opt/bitnami/airflow/spark/dags/spark/check_spark_job.py',  # 程式碼的路徑，需根據實際情況修改
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
        'spark.kubernetes.container.image': 'apache/spark'
    },
    verbose=True,
    dag=dag
)

spark_submit_task



