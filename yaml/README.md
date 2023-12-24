Airflow
============
###
```bash
$> oc get all -n test-airflow
```
```bash
$> helm install aiflow-service-pv ./yaml -n test-airflow
```
```bash
$> oc apply -f ./yaml/persistent_volume.yaml
$> oc apply -f ./yaml/airflow-role.yaml
$> oc apply -f ./yaml/airflow-rolebinding.yaml
```