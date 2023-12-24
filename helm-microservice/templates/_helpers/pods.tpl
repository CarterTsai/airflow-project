{{/*
Define the image configs for airflow containers
*/}}

{{- define "airflow.image" }}
image: {{ .Values.airflow.image.repository }}:{{ .Values.airflow.image.tag }}
imagePullPolicy: {{ .Values.airflow.image.pullPolicy }}
securityContext:
  runAsUser: {{ .Values.airflow.image.uid }}
  runAsGroup: {{ .Values.airflow.image.gid }}
{{- end }}


{{- define "scheduler.image" }}
image: {{ .Values.scheduler.image.repository }}:{{ .Values.scheduler.image.tag }}
imagePullPolicy: {{ .Values.scheduler.image.pullPolicy }}
securityContext:
  runAsUser: {{ .Values.scheduler.image.uid }}
  runAsGroup: {{ .Values.scheduler.image.gid }}
{{- end }}


{{- define "postgres.image" }}
image: {{ .Values.postgres.image.repository }}:{{ .Values.postgres.image.tag }}
imagePullPolicy: {{ .Values.postgres.image.pullPolicy }}
securityContext:
  runAsUser: {{ .Values.postgres.image.uid }}
  runAsGroup: {{ .Values.postgres.image.gid }}
{{- end }}