FROM bitnami/airflow-scheduler:2-debian-11 as build

LABEL maintainer="Carter Tsai <Carter.Tsai@ibm.com" \
      com.project.image.base.name="docker.io/apache/airflow:2.6.3-python3.9" \
      com.project.image.created="2023-08-07T16:48:17Z" \
      com.project.image.description="airflow image" \
      com.project.image.licenses="Apache-2.0" \
      com.project.image.ref.name="" \
      com.project.image.title="airflow" \
      com.project.image.vendor="." \
      com.project.image.version="0.0.1"

USER root

RUN apt-get autoremove -yqq --purge && apt-get clean && \
      apt-get update && apt-get -y upgrade
# 	apt-get -y install 


RUN pip install pymongo==4.4.1
RUN pip install dnspython==2.4.2
RUN pip install apache-airflow-providers-common-sql>=1.3.1
RUN pip install psycopg2-binary>=2.8.0
RUN pip install apache-airflow-providers-mongo==3.2.1
RUN pip install apache-airflow-providers-postgres==5.6.0

USER 1001


COPY --chown=airflow:root dags /opt/bitnami/airflow/dags