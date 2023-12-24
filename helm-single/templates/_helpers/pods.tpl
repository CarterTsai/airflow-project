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


{{- define "metadata.image" }}
image: {{ .Values.metadata.image.repository }}:{{ .Values.metadata.image.tag }}
imagePullPolicy: {{ .Values.metadata.image.pullPolicy }}
securityContext:
  runAsUser: {{ .Values.metadata.image.uid }}
  runAsGroup: {{ .Values.metadata.image.gid }}
{{- end }}