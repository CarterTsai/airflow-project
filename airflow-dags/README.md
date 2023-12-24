Dags on Docker Image
====================

https://www.projectpro.io/recipes/use-sparksubmitoperator-airflow-dag

### registry

local的docker registry 需要設定ip，請看docker-compose

```bash
docker pull registry:2
```

編輯或創建 Docker 的守護程序配置文件。這通常位於 /etc/docker/daemon.json。

在該文件中，添加或修改 insecure-registries 属性以包含你的 Docker Registry 的 IP 和連接埠：

```json
{
  "insecure-registries" : ["172.27.48.1:5000"]
}
```

```bash
docker run -d -p 5000:5000 --restart always --name registry registry:2
```


### Create Image

```bash
docker build -t airflow-dags:0.0.4 . 
```

### Push Image

```bash
$ docker tag airflow-dags:0.0.4 localhost:5000/airflow-dags:0.0.4
$ docker push localhost:5000/airflow-dags:0.0.4
```

$ docker tag airflow-dags:0.0.4 cartertsai/dags-test:0.0.4
$ docker push cartertsai/dags-test:0.0.4

### Sync Dags
# 將本地目錄同步到 Pod 的儲存卷
oc rsync ./local/dir/ POD_NAME:/path/in/pod
oc rsync ./dags airflow-7956cb87b7-m8f44:/opt/bitnami/airflow/


oc rsync . airflow-c97487fb8-4w79q:/spark/dags
oc rsync . airflow-c97487fb8-4w79q:/opt/bitnami/airflow/dags/

# 從 Pod 的儲存卷同步資料到本地目錄
oc rsync POD_NAME:/path/in/pod /local/dir/

oc rsync .\airflow-dags\dags\ airflow-6645596c5-74lbf:/opt/bitnami/airflow/dags/

oc rsync .\share\ aiflow-service-spark-master-0:/opt/share

oc port-forward svc/aiflow-service-spark-master-svc 7077:7077


###　Spark Test

oc port-forward svc/spark-worker-svc 8086:8080
oc port-forward svc/aiflow-service-spark-master-svc 7077:7077
oc port-forward svc/aiflow-service-spark-master-svc 8080:80

https://github.com/bitnami/charts/tree/main/bitnami/spark/

spark-submit --deploy-mode cluster \
--conf spark.kubernetes.driverEnv.SPARK_MASTER_URL=spark://aiflow-service-spark-master-0.aiflow-service-spark-headless.test-airflow.svc.cluster.local:7077 \
--master k8s://https://aiflow-service-spark-master-0.aiflow-service-spark-headless.test-airflow.svc.cluster.local:7077
 test.py


kind: Service
apiVersion: v1
metadata:
  name: spark-worker-svc
  namespace: test-airflow
  uid: b2b41961-69b7-46b2-9100-e4d76bf3c6eb
  resourceVersion: '1942182'
  creationTimestamp: '2023-09-06T20:29:38Z'
  labels:
    app: spark
    app.kubernetes.io/managed-by: Helm
  annotations:
    meta.helm.sh/release-name: spark-worker
    meta.helm.sh/release-namespace: spark-worker
  managedFields:
    - manager: Mozilla
      operation: Update
      apiVersion: v1
      time: '2023-09-06T20:32:07Z'
      fieldsType: FieldsV1
      fieldsV1:
        'f:metadata':
          'f:annotations':
            .: {}
            'f:meta.helm.sh/release-name': {}
            'f:meta.helm.sh/release-namespace': {}
          'f:labels':
            .: {}
            'f:app': {}
            'f:app.kubernetes.io/managed-by': {}
        'f:spec':
          'f:externalTrafficPolicy': {}
          'f:internalTrafficPolicy': {}
          'f:ports':
            .: {}
            'k:{"port":8080,"protocol":"TCP"}':
              .: {}
              'f:port': {}
              'f:protocol': {}
              'f:targetPort': {}
          'f:selector': {}
          'f:sessionAffinity': {}
          'f:type': {}
spec:
  clusterIP: 10.217.4.86
  externalTrafficPolicy: Cluster
  ipFamilies:
    - IPv4
  ports:
    - protocol: TCP
      port: 8080
      targetPort: 8080
      nodePort: 31724
  internalTrafficPolicy: Cluster
  clusterIPs:
    - 10.217.4.86
  type: NodePort
  ipFamilyPolicy: SingleStack
  sessionAffinity: None
  selector:
    app.kubernetes.io/component: worker
    app.kubernetes.io/name: spark
status:
  loadBalancer: {}
