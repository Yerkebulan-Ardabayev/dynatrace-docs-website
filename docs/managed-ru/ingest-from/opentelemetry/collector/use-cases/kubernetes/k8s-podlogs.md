---
title: Приём логов подов Kubernetes через OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-podlogs
---

# Приём логов подов Kubernetes через OTel Collector

# Приём логов подов Kubernetes через OTel Collector

* Практическое руководство
* Чтение: 4 мин
* Обновлено 09 апр. 2026 г.

В примере конфигурации ниже показано, как настроить экземпляр Collector для получения логов со всех подов Kubernetes. Также показано, как обогатить логи метаданными Kubernetes, чтобы автоматически связать сервисы OpenTelemetry с подами и прикрепить логи к сервисам и подам Kubernetes.

## Предварительные требования

* Развёрнутый ActiveGate для мониторинга Kubernetes API
* Один из следующих дистрибутивов Collector с ресивером [Filelog﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.156.0/receiver/filelogreceiver) и процессором [Kubernetes Attributes﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/k8sattributesprocessor):

  + [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии от OpenTelemetry.")
  + [OpenTelemetry Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии от OpenTelemetry.")
  + [Пользовательская версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии от OpenTelemetry.")
* OTel Collector, развёрнутый на каждом узле
* [URL API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте про эндпоинты OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") вашей среды Dynatrace
* [Токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте про эндпоинты OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с необходимым уровнем доступа
* [Kubernetes настроен](#kubernetes-configuration) для требуемого управления доступом на основе ролей
* Kubernetes Secrets настроены так, как показано в [Развёртывание Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector/deployment "Как развернуть Dynatrace OpenTelemetry Collector.")

О том, как настроить Collector с указанной ниже конфигурацией, см. [Развёртывание Collector](/managed/ingest-from/opentelemetry/collector/deployment "Как развернуть Dynatrace OpenTelemetry Collector.") и [Конфигурация Collector](/managed/ingest-from/opentelemetry/collector/configuration "Как настроить OpenTelemetry Collector.").

## Демонстрационная конфигурация

Конфигурация Kubernetes

В этом примере конфигурации используется тот же подход обогащения Kubernetes, что и в сценарии [Обогащение запросов OTLP данными Kubernetes](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Настройка OpenTelemetry Collector для обогащения запросов OTLP данными Kubernetes.").

Помимо конфигурации Collector, обязательно также обновите конфигурацию Kubernetes для следующих компонентов:

* **Учётная запись службы**: укажите то же имя учётной записи службы, что используется в [файле RBAC](#kubernetes-configuration) (см. записи для [Helm﻿](https://github.com/open-telemetry/opentelemetry-helm-charts/blob/opentelemetry-collector-0.100.0/charts/opentelemetry-collector/values.yaml#L184-L191), [Operator﻿](https://github.com/open-telemetry/opentelemetry-operator/blob/v0.156.0/docs/api/opentelemetrycollectors.md#opentelemetrycollectorspec))
* **Смонтированные тома**: укажите тома файловой системы, в которых хост Kubernetes хранит соответствующие файлы логов (см. записи для [Helm﻿](https://github.com/open-telemetry/opentelemetry-helm-charts/blob/opentelemetry-collector-0.100.0/charts/opentelemetry-collector/values.yaml#L241), [Operator﻿](https://github.com/open-telemetry/opentelemetry-operator/blob/v0.156.0/docs/api/opentelemetrycollectors.md#opentelemetrycollectorspec))
* **Пути монтирования**: укажите пути файловой системы, по которым ранее настроенные тома должны монтироваться внутри контейнера (см. записи для [Helm﻿](https://github.com/open-telemetry/opentelemetry-helm-charts/blob/opentelemetry-collector-0.100.0/charts/opentelemetry-collector/values.yaml#L244), [Operator﻿](https://github.com/open-telemetry/opentelemetry-operator/blob/v0.156.0/docs/api/opentelemetrycollectors.md#opentelemetrycollectorspec))

```
receivers:



# configure the filelog receiver to access the pod logs



# from the mounted volumes



file_log:



include:



- /var/log/pods/*/*/*.log



include_file_name: false



include_file_path: true



start_at: end



operators:



- id: container-parser



type: container



processors:



transform:



error_mode: ignore



trace_statements: &dynatrace_transformations



# Set attributes taken from k8s metadata.



- context: resource



statements:



- set(attributes["k8s.cluster.name"], "${env:CLUSTER_NAME}")



- set(attributes["k8s.workload.kind"], "job") where IsString(attributes["k8s.job.name"])



- set(attributes["k8s.workload.name"], attributes["k8s.job.name"]) where IsString(attributes["k8s.job.name"])



- set(attributes["k8s.workload.kind"], "cronjob") where IsString(attributes["k8s.cronjob.name"])



- set(attributes["k8s.workload.name"], attributes["k8s.cronjob.name"]) where IsString(attributes["k8s.cronjob.name"])



- set(attributes["k8s.workload.kind"], "daemonset") where IsString(attributes["k8s.daemonset.name"])



- set(attributes["k8s.workload.name"], attributes["k8s.daemonset.name"]) where IsString(attributes["k8s.daemonset.name"])



- set(attributes["k8s.workload.kind"], "statefulset") where IsString(attributes["k8s.statefulset.name"])



- set(attributes["k8s.workload.name"], attributes["k8s.statefulset.name"]) where IsString(attributes["k8s.statefulset.name"])



- set(attributes["k8s.workload.kind"], "replicaset") where IsString(attributes["k8s.replicaset.name"])



- set(attributes["k8s.workload.name"], attributes["k8s.replicaset.name"]) where IsString(attributes["k8s.replicaset.name"])



- set(attributes["k8s.workload.kind"], "deployment") where IsString(attributes["k8s.deployment.name"])



- set(attributes["k8s.workload.name"], attributes["k8s.deployment.name"]) where IsString(attributes["k8s.deployment.name"])



# remove the delete statements if you want to preserve these attributes



- delete_key(attributes, "k8s.deployment.name")



- delete_key(attributes, "k8s.replicaset.name")



- delete_key(attributes, "k8s.statefulset.name")



- delete_key(attributes, "k8s.daemonset.name")



- delete_key(attributes, "k8s.cronjob.name")



- delete_key(attributes, "k8s.job.name")



# Set attributes from metadata specified in Dynatrace and set through the Dynatrace Operator.



# For more info: https://docs.dynatrace.com/docs/shortlink/k8s-metadata-telemetry-enrichment



- context: resource



statements:



- merge_maps(attributes, ParseJSON(attributes["metadata.dynatrace.com"]), "upsert") where IsMatch(attributes["metadata.dynatrace.com"], "^\\{")



- delete_key(attributes, "metadata.dynatrace.com")



metric_statements: *dynatrace_transformations



log_statements: *dynatrace_transformations



k8sattributes:



extract:



metadata:



- k8s.pod.name



- k8s.pod.uid



- k8s.pod.ip



- k8s.deployment.name



- k8s.replicaset.name



- k8s.statefulset.name



- k8s.daemonset.name



- k8s.job.name



- k8s.cronjob.name



- k8s.namespace.name



- k8s.node.name



- k8s.cluster.uid



- k8s.container.name



annotations:



- from: pod



key_regex: metadata.dynatrace.com/(.*)



tag_name: $$1



- from: pod



key: metadata.dynatrace.com



tag_name: metadata.dynatrace.com



pod_association:



- sources:



- from: resource_attribute



name: k8s.pod.name



- from: resource_attribute



name: k8s.namespace.name



- sources:



- from: resource_attribute



name: k8s.pod.ip



- sources:



- from: resource_attribute



name: k8s.pod.uid



- sources:



- from: connection



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



logs:



receivers: [file_log]



processors: [k8sattributes,transform]



exporters: [otlp_http]
```

Проверка конфигурации

[Проверьте свои настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "Как настроить OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Настройка Kubernetes

Настроить следующий файл `rbac.yaml` в инстансе Kubernetes, чтобы разрешить OTel Collector использовать Kubernetes API с типом аутентификации service-account.

```
apiVersion: v1



kind: ServiceAccount



metadata:



labels:



app: collector



name: collector



---



apiVersion: rbac.authorization.k8s.io/v1



kind: ClusterRole



metadata:



name: collector



labels:



app: collector



rules:



- apiGroups:



- ''



resources:



- 'pods'



- 'namespaces'



verbs:



- 'get'



- 'watch'



- 'list'



- apiGroups:



- 'apps'



resources:



- 'replicasets'



verbs:



- 'get'



- 'list'



- 'watch'



- apiGroups:



- 'extensions'



resources:



- 'replicasets'



verbs:



- 'get'



- 'list'



- 'watch'



---



apiVersion: rbac.authorization.k8s.io/v1



kind: ClusterRoleBinding



metadata:



name: collector



labels:



app: collector



roleRef:



apiGroup: rbac.authorization.k8s.io



kind: ClusterRole



name: collector



subjects:



- kind: ServiceAccount



name: collector



namespace: default
```

Настройка для GKE Autopilot или AWS EKS

Если Collector запускается на GKE Autopilot или AWS EKS, в конфигурации нужны следующие изменения:

* **Режим развёртывания**: Collector нужно развернуть как DaemonSet, чтобы обеспечить доступ к файлам логов подов на хосте. Подробности о развёртывании Collector как DaemonSet смотри в разделе [Инструкции по развёртыванию](/managed/ingest-from/opentelemetry/collector/deployment "Как развернуть Dynatrace OpenTelemetry Collector.").
* **Монтирование тома**: монтирование томов в `/var/log/pods` должно быть доступно только для чтения, иначе Collector не сможет получить доступ к файлам логов
  в этом каталоге.

Ниже приведён пример конфигурации для Collector DaemonSet с необходимыми монтированиями томов для сбора логов подов:

```
apiVersion: apps/v1



kind: DaemonSet



metadata:



name: dynatrace-otel-collector



spec:



selector:



matchLabels:



app.kubernetes.io/name: dynatrace-otel-collector



template:



metadata:



labels:



app.kubernetes.io/instance: dynatrace-otel-collector



app.kubernetes.io/name: dynatrace-otel-collector



spec:



serviceAccountName: collector



tolerations:



# these tolerations are to have the daemonset runnable on control plane nodes



# remove them if your control plane nodes should not run pods



- key: node-role.kubernetes.io/control-plane



operator: Exists



effect: NoSchedule



- key: node-role.kubernetes.io/master



operator: Exists



effect: NoSchedule



containers:



- args: ["--config", "/conf/otel-collector-config.yaml"]



env:



- name: MY_POD_IP



valueFrom:



fieldRef:



apiVersion: v1



fieldPath: status.podIP



image: ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector:0.52.0



name: otel-collector



resources:



limits:



memory: 512Mi



volumeMounts:



- name: dynatrace-otel-collector-config



mountPath: /conf



# read-only volumeMount for the directory containing the pod logs



- name: logs



mountPath: /var/log



readOnly: true



volumes:



- configMap:



name: dynatrace-otel-collector-config



items:



- key: otel-collector-config



path: otel-collector-config.yaml



name: dynatrace-otel-collector-config



# hostPath volume containing the pod logs of the respective node the Collector instance is running on



- hostPath:



path: /var/log



name: logs
```

## Компоненты

Для нашей конфигурации настроены следующие компоненты.

### Receivers

В разделе `receivers` указан receiver `filelog` как активный компонент-receiver для нашего инстанса Collector.

Filelog receiver поддерживает ряд [параметров конфигурации﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.156.0/receiver/filelogreceiver/README.md), позволяющих настраивать его поведение. В примере используются следующие:

* `include`, задаёт шаблон пути к файлам, которые нужно принимать.
* `start_at`, задаёт, должен ли receiver читать с начала файла или только самые последние записи, с конца.
* `operators`, настраивает оператор [`container`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.156.0/pkg/stanza/docs/operators/container.md), который автоматически парсит каждую запись лога.

### Processors

В разделе `processors` указан [processor `k8sattributes`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/k8sattributesprocessor) со следующими параметрами:

* `extract`, задаёт, какую информацию нужно извлекать.
* `pod_association`, задаёт, как информация о поде связывается с атрибутами.

### Exporters

В разделе `exporters` указан стандартный [exporter `otlp_http`﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/exporter/otlphttpexporter), настроенный с URL Dynatrace API и требуемым токеном аутентификации, как описано в разделе [Kubernetes Secrets](#kubernetes-secrets).

### Service pipelines

В разделе `service` receiver, processor и exporter объединяются в pipeline'ы для трейсов, метрик и логов. Эти pipeline'ы позволяют отправлять сигналы OpenTelemetry через инстанс Collector и автоматически обогащать их дополнительными деталями, специфичными для Kubernetes.

## Похожие темы

* [Обогащение OTLP-запросов данными Kubernetes](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Настройка OpenTelemetry Collector для обогащения OTLP-запросов данными Kubernetes.")
* [Приём логов из файлов с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/filelog "Настройка OpenTelemetry Collector для приёма данных логов в Dynatrace.")