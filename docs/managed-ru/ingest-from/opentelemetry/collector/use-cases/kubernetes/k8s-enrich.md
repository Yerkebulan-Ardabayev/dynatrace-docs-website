---
title: Обогащение запросов OTLP данными Kubernetes
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich
---

# Обогащение запросов OTLP данными Kubernetes

# Обогащение запросов OTLP данными Kubernetes

* Практическое руководство
* 3 мин на чтение
* Обновлено 24 сентября 2025 г.

В приведённом ниже примере конфигурации показано, как настроить экземпляр Collector для обогащения телеметрических данных OTLP дополнительными метаданными Kubernetes. Это включает, например, сведения о pod, deployment и кластере и позволяет Dynatrace корректно сопоставлять предоставленные телеметрические данные с соответствующими сущностями в Dynatrace.

Dynatrace рекомендует использовать ActiveGate для улучшения мониторинга состояния и производительности кластера Kubernetes.
Развёртывание ActiveGate позволяет приложению Dynatrace Kubernetes визуализировать данные Kubernetes и OpenTelemetry и сопоставлять их с соответствующими сущностями Kubernetes.

## Предварительные требования

* Развёрнутый ActiveGate для мониторинга Kubernetes API, необязательно
* Один из следующих дистрибутивов Collector с процессорами [Kubernetes Attributes﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/k8sattributesprocessor) и [Transform﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/transformprocessor):

  + [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Узнать, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [OpenTelemetry Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Узнать, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [Пользовательская версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "Узнать, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
* OTel Collector, развёрнутый в [режиме agent](/managed/ingest-from/opentelemetry/collector/deployment#dynatrace-docs--agent "Как развернуть Dynatrace OpenTelemetry Collector.")
* [URL API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнать про конечные точки OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace.") среды Dynatrace
* [Токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнать про конечные точки OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с соответствующей областью доступа
* [Kubernetes настроен](#kubernetes-configuration) для требуемого контроля доступа на основе ролей

О настройке Collector с указанной ниже конфигурацией см. [Развёртывание Collector](/managed/ingest-from/opentelemetry/collector/deployment "Как развернуть Dynatrace OpenTelemetry Collector.") и [Настройка Collector](/managed/ingest-from/opentelemetry/collector/configuration "Как настроить OpenTelemetry Collector.").

## Демонстрационная конфигурация

Сервисная учётная запись

Помимо настройки Collector, обязательно нужно также обновить конфигурацию Kubernetes в соответствии с именем сервисной учётной записи, используемым в [файле RBAC](#kubernetes-configuration) (см. записи для [Helm﻿](https://github.com/open-telemetry/opentelemetry-helm-charts/blob/opentelemetry-collector-0.100.0/charts/opentelemetry-collector/values.yaml#L184-L191), [Operator﻿](https://github.com/open-telemetry/opentelemetry-operator/blob/v0.156.0/docs/api/opentelemetrycollectors.md#opentelemetrycollectorspec)).

```
extensions:



health_check:



endpoint: ${env:MY_POD_IP}:13133



receivers:



otlp:



protocols:



grpc:



endpoint: ${env:MY_POD_IP}:4317



http:



endpoint: ${env:MY_POD_IP}:4318



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



extensions:



- health_check



pipelines:



traces:



receivers: [otlp]



processors: [k8sattributes, transform]



exporters: [otlp_http]



metrics:



receivers: [otlp]



processors: [k8sattributes, transform]



exporters: [otlp_http]



logs:



receivers: [otlp]



processors: [k8sattributes, transform]



exporters: [otlp_http]
```

Проверка конфигурации

[Проверьте настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "Как настроить OpenTelemetry Collector.") во избежание проблем с конфигурацией.

## Настройка Kubernetes

Настройте следующий файл `rbac.yaml` в своём экземпляре Kubernetes, чтобы разрешить OTel Collector использовать Kubernetes API с типом аутентификации service-account.

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

## Компоненты

Для нашей конфигурации мы настроили следующие компоненты.

### Receivers

В разделе `receivers` указан стандартный receiver `otlp` в качестве активного компонента-приёмника для экземпляра Collector.

Это сделано в основном в демонстрационных целях. Здесь можно указать любой другой допустимый receiver (например, `zipkin`).

### Обработчики (Processors)

В разделе `processors` указывается [`k8sattributes` processor﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/k8sattributesprocessor) со следующими параметрами:

* `extract`, определяет, какая информация должна извлекаться.
* `pod_association`, определяет, как информация о поде связывается с атрибутами.

Учти, что атрибут `k8s.container.name` будет извлечён только в том случае, если под, от которого получен входящий сигнал, содержит только один контейнер, либо если полученный сигнал содержит ресурсный атрибут `k8s.container.id`. В противном случае процессор k8sattributes не сможет корректно сопоставить нужный контейнер.

Оператор Dynatrace обогащает данные OpenTelemetry от подов Kubernetes аннотациями `metadata.dynatrace.com`. При наличии таких аннотаций процессор `k8sattributes` их извлекает.

Также настраивается [`transform` processor﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/transformprocessor) для автоматического добавления информации о кластере Kubernetes в качестве ресурсных атрибутов для всех телеметрических сигналов.

### Экспортеры (Exporters)

В разделе `exporters` указывается стандартный [`otlp_http` exporter﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/exporter/otlphttpexporter), который настраивается с указанием URL Dynatrace API и необходимого токена аутентификации.

Для этого задаются следующие две переменные окружения, на которые даются ссылки в значениях конфигурации `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL конечной точки Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [API токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Конвейеры служб (Service pipelines)

В разделе `service` объекты receiver, processor и exporter собираются в конвейеры для трасс, метрик и логов. Эти конвейеры позволяют отправлять сигналы OpenTelemetry через экземпляр Collector и автоматически обогащать их дополнительными деталями, специфичными для Kubernetes.

## Лимиты и ограничения

Данные принимаются с использованием протокола OpenTelemetry (OTLP) через [OTLP APIы Dynatrace](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") и подчиняются лимитам и ограничениям API.
Подробнее см.:

* [Ограничения метрик OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Сопоставление метрик Dynatrace](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Приём логов OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.")

## Похожие темы

* [Обогащение принимаемых данных полями, специфичными для Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.")