Airflow
============
https://github.com/bitnami/containers/tree/main/bitnami/airflow#how-to-use-this-image


###
```bash
$> oc get all -n test-airflow
```
### Helm
```bash
# $> helm install test-airflow ./helm
# $> helm upgrade test-airflow ./helm --dry-run --debug
# $> helm uninstall test-airflow
$> helm install aiflow-service ./helm-single -n test-airflow --debug
$> helm upgrade aiflow-service ./helm-single -n test-airflow
```

### Secret Config Encryption


### Airflow
```bash
$> oc apply -f ./airflow.yaml
$> oc expose svc airflow
```

### Service Account
```bash
$> oc apply -f ./serviceaccount.yaml 
```

### Airflow
```bash
$> oc apply -f ./airflow-scheduler.yaml
```

```bash
$> oc apply -f ./airflow-config.yaml
$> oc apply -f ./persistent_volume.yaml 
$> oc apply -f ./pod-template.yaml
$> oc apply -f ./serviceaccount.yaml
```

### Postgresql
```bash
$> oc apply -f ./postgresql.yaml.yaml
$> oc expose svc postgres 
$> oc port-forward svc/postgres 5432:5432
```

當你使用 oc expose svc postgres 命令來創建一個 route 時，這條命令會創建一個可以將流量導入到你的 PostgreSQL 服務的 route。

但是，如果你不能通過這個 route 連接到 PostgreSQL，這可能是由於以下原因：

PostgreSQL 通常運行在非 HTTP 端口上：PostgreSQL 通常運行在 5432 端口上，而路由 (route) 通常被設計用於導向 HTTP 或 HTTPS 流量。因此，即使你創建了一個 route，你可能也無法通過該 route 來使用 PostgreSQL 的原生協議連接到服務。

安全性問題：OpenShift 預設啟用了很多安全策略，這可能會阻止從外部連接到集群內部的服務。你需要確保你的 PostgreSQL 服務的安全性設置允許來自該 route 的連接。

網路問題：可能存在網路連接問題。你應確保你的集群和服務的網路設置都正確。

如果你想從集群外部訪問你的 PostgreSQL 服務，一個更常見的做法是使用 NodePort 或 LoadBalancer 服務。這兩種服務都允許你從集群外部連接到一個特定的端口，並將連接導向到你的 PostgreSQL 服務。

另外，你還可以考慮使用 OpenShift 的 port forwarding 功能，這可以讓你將本地的一個端口映射到集群中的一個服務。例如，以下命令將本地的 5432 端口映射到集群中名為 postgres 的服務的 5432 端口：


建立service account
```bash
oc apply -f .\serviceaccount.yaml 
```


```bash
oc port-forward svc/postgres 5432:5432
使用這條命令後，你可以像連接到本地的 PostgreSQL 服務一樣，使用 psql -h localhost -p 5432 -U postgres -d mydb 來連接到你的 PostgreSQL 服務。
```

### 

```bash
$> oc get pods
NAME                        READY   STATUS    RESTARTS      AGE
airflow-7c96898b44-5vnlr    1/1     Running   3 (76s ago)   23m
postgres-55567b6459-drvhs   1/1     Running   0             2m33s
$> oc exec -ti postgres-55567b6459-drvhs /bin/bash
$> psql -h localhost -U airflow -d airflow
```