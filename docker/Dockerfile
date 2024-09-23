FROM bitnami/airflow:2-debian-12 as build

LABEL maintainer="Carter Tsai <Carter.Tsai@ibm.com" \
      com.project.image.base.name="docker.io/apache/airflow:2.6.3-python3.9" \
      com.project.image.created="2023-08-07T16:48:17Z" \
      com.project.image.description="airflow image" \
      com.project.image.licenses="Apache-2.0" \
      com.project.image.ref.name="" \
      com.project.image.title="airflow" \
      com.project.image.vendor="." \
      com.project.image.version="1.0.6"

USER root

# 設置環境變數
ENV SPARK_VERSION=3.5.3
ENV HADOOP_VERSION=3
ENV JAVA_VERSION=17
ENV JAVA_HOME=/usr/lib/jvm/java-$JAVA_VERSION-openjdk-amd64

RUN apt-get autoremove -yqq --purge && apt-get clean && \
      apt-get update && apt-get -y upgrade

# 複製 requirements.txt 並安裝所有依賴項
COPY ./config/requirements.txt /opt/bitnami/airflow/venv
RUN apt install wget
# Spark
RUN apt-get install -y openjdk-$JAVA_VERSION-jdk

RUN wget https://downloads.apache.org/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz && \
    tar xzf spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz && \
    mv spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION /spark && \
    rm spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz


# RUN pip install --no-cache-dir -r /opt/bitnami/airflow/venv/requirements.txt
RUN /opt/bitnami/airflow/venv/bin/pip install --no-cache-dir -r /opt/bitnami/airflow/venv/requirements.txt

ENV PATH $PATH:/spark/bin
ENV SPARK_HOME=/spark

COPY ./config/run.sh /opt/bitnami/scripts/airflow/run.sh

RUN apt-get install curl vim netcat-openbsd tree -y

USER 1001

CMD ["/opt/bitnami/scripts/airflow/run.sh"]