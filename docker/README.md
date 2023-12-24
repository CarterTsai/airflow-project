### Build Image
```bash
$ docker-compose.exe build
```

### Push Image

```bash
$ docker tag airflow-test-all:1.0.6 cartertsai/airflow-test-all:1.0.6
$ docker push cartertsai/airflow-test-all:1.0.6
$ docker run aquasec/trivy image cartertsai/airflow-test-all:1.0.6
```

### TEST
$ docker-compose.exe up


### Push Image Spark

```bash
$ docker tag spark-all:0.0.1 cartertsai/spark-all:0.0.1
$ docker push cartertsai/spark-all:0.0.1
```