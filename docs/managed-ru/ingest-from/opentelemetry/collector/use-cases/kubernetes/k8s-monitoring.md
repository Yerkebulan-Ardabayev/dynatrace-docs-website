---
title: Мониторинг кластеров Kubernetes с помощью Dynatrace Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-monitoring
---

# Мониторинг кластеров Kubernetes с помощью Dynatrace Collector

# Мониторинг кластеров Kubernetes с помощью Dynatrace Collector

* Практическое руководство
* Чтение: 5 мин
* Обновлено 20 нояб. 2025 г.

Dynatrace Collector обеспечивает широкую поддержку мониторинга кластера и рабочих нагрузок Kubernetes. Он поддерживает различные приёмники для сбора ключевых метрик о кластере, узлах и объектах Kubernetes.

В этом разделе описано, как настроить Collector для получения полной видимости кластеров Kubernetes через [**Data Explorer**](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") или пользовательские дашборды в Dashboards Classic.

Оператор Dynatrace

Dynatrace рекомендует использовать [Оператор Dynatrace для мониторинга Kubernetes](/managed/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes").
Однако этот сценарий предназначен специально для пользователей OpenTelemetry, которые предпочитают не разворачивать Оператор Dynatrace.
Настройка Collector, как описано ниже, сделает данные мониторинга Kubernetes доступными для использования в [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") и [Dashboards](/managed/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.").

## Предварительные требования

* Один из следующих дистрибутивов Collector с приёмниками [Kubernetes Cluster﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/k8sclusterreceiver), [Kubernetes Events﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/k8seventsreceiver) и [Kubelet Stats﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/kubeletstatsreceiver):

  + [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + [OTel Collector Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + [Собственная сборка OTel Collector](/managed/ingest-from/opentelemetry/collector#collector-builder "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
* Развёртывание Collector в [режиме агента](/managed/ingest-from/opentelemetry/collector/deployment#dynatrace-docs--agent "How to deploy the Dynatrace OpenTelemetry Collector.") для телеметрии на уровне узлов и кластера
* [API URL](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") среды Dynatrace
* [Токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") с соответствующей областью доступа
* [Настроенный Kubernetes](#kubernetes-configuration) для необходимого управления доступом на основе ролей

О том, как это настроить с помощью приведённых ниже конфигураций, см. в разделах [Развёртывание Collector](/managed/ingest-from/opentelemetry/collector/deployment "How to deploy the Dynatrace OpenTelemetry Collector.") и [Конфигурация Collector](/managed/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.").

## Демонстрационные конфигурации

### Конфигурация RBAC

Настройте следующий файл `rbac.yaml` для своего экземпляра Kubernetes, чтобы разрешить Collector использовать API Kubernetes с типом аутентификации service-account.

```
apiVersion: v1



kind: ServiceAccount



metadata:



labels:



app: otelcol-dt



name: otelcol-dt



---



apiVersion: rbac.authorization.k8s.io/v1



kind: ClusterRole



metadata:



name: otelcol-dt



labels:



app: otelcol-dt



rules:



- apiGroups:



- ""



resources:



- events



- namespaces



- namespaces/status



- nodes



- nodes/spec



- nodes/stats



- nodes/proxy



- persistentvolumes



- persistentvolumeclaims



- pods



- pods/status



- replicationcontrollers



- replicationcontrollers/status



- resourcequotas



- services



verbs:



- get



- list



- watch



- apiGroups:



- apps



resources:



- daemonsets



- deployments



- replicasets



- statefulsets



verbs:



- get



- list



- watch



- apiGroups:



- batch



resources:



- jobs



- cronjobs



verbs:



- get



- list



- watch



- apiGroups:



- autoscaling



resources:



- horizontalpodautoscalers



verbs:



- get



- list



- watch



- apiGroups:



- coordination.k8s.io



resources:



- leases



verbs:



- get



- list



- watch



- create



- update



- patch



- delete



---



apiVersion: rbac.authorization.k8s.io/v1



kind: ClusterRoleBinding



metadata:



name: otelcol-dt



labels:



app: otelcol-dt



roleRef:



apiGroup: rbac.authorization.k8s.io



kind: ClusterRole



name: otelcol-dt



subjects:



- kind: ServiceAccount



name: otelcol-dt



namespace: default
```

### Конфигурация коллектора

Учётная запись службы

Помимо конфигурации коллектора, важно также обновить конфигурацию Kubernetes в соответствии с именем service account, используемым в [файле RBAC](#kubernetes-configuration)
(см. записи для [Helm﻿](https://github.com/open-telemetry/opentelemetry-helm-charts/blob/opentelemetry-collector-0.127.2/charts/opentelemetry-collector/values.yaml#L245-L252) и [Operator﻿](https://github.com/open-telemetry/opentelemetry-operator/blob/v0.156.0/docs/api/opentelemetrycollectors.md#opentelemetrycollectorspec)).

```
extensions:



health_check:



endpoint: 0.0.0.0:13133



k8s_leader_elector:



auth_type: "serviceAccount"



lease_name: k8smonitoring



lease_namespace: ${env:POD_NAMESPACE}



receivers:



otlp:



protocols:



grpc:



endpoint: 0.0.0.0:4317



k8s_events:



auth_type: "serviceAccount"



k8s_leader_elector: k8s_leader_elector



kubelet_stats:



auth_type: "serviceAccount"



collection_interval: 10s



node: '${env:K8S_NODE_NAME}'



extra_metadata_labels:



- k8s.volume.type



k8s_api_config:



auth_type: "serviceAccount"



endpoint: "https://${env:K8S_NODE_NAME}:10250"



insecure_skip_verify: true



metric_groups:



- node



- pod



- container



- volume



k8s_cluster:



auth_type: "serviceAccount"



collection_interval: 10s



k8s_leader_elector: k8s_leader_elector



allocatable_types_to_report:



- cpu



- memory



- pods



node_conditions_to_report:



- Ready



- MemoryPressure



- PIDPressure



- DiskPressure



- NetworkUnavailable



metrics:



k8s.node.condition:



enabled: true



k8s.pod.status_reason:



enabled: true



processors:



cumulativetodelta:



max_staleness: 25h



filter:



error_mode: ignore



metrics:



metric:



- 'IsMatch(name, "k8s.volume.*") and resource.attributes["k8s.volume.type"] == nil'



- 'resource.attributes["k8s.volume.type"] == "configMap"'



- 'resource.attributes["k8s.volume.type"] == "emptyDir"'



- 'resource.attributes["k8s.volume.type"] == "secret"'



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



- k8s_leader_elector



pipelines:



metrics/node:



receivers:



- kubelet_stats



processors:



- filter



- k8sattributes



- transform



- cumulativetodelta



exporters:



- otlp_http



metrics:



receivers:



- k8s_cluster



processors:



- k8sattributes



- transform



- cumulativetodelta



exporters:



- otlp_http



logs:



receivers:



- k8s_events



processors:



- transform



exporters:



- otlp_http



traces:



receivers:



- otlp



processors:



- k8sattributes



- transform



exporters:



- otlp_http
```

Проверка конфигурации

[Проверьте свои настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

Рекомендация по процессору cumulativetodelta

Параметр `max_staleness` [процессора cumulativetodelta﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/cumulativetodeltaprocessor) рекомендуется устанавливать выше, чем частота получения метрик коллектором (например, как часто поступают метрики через OTLP или какой интервал сбора данных Prometheus). Это гарантирует, что ссылки на заброшенные потоки метрик не будут со временем накапливаться в памяти.

## Компоненты

Для нашей конфигурации мы настроили следующие компоненты:

#### Приёмники (Receivers)

В разделе `receivers` мы указываем следующие приёмники в качестве активных компонентов-приёмников для нашего развёртывания:

* [`otlp`﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/receiver/otlpreceiver): для приёма трейсов OTLP.
* [`k8sevents`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/k8seventsreceiver): для получения событий Kubernetes с сервера Kubernetes API. [1](#fn-1-1-def)
* [`k8s_cluster`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/k8sclusterreceiver): для получения метрик уровня кластера и событий сущностей с сервера Kubernetes API.
* [`kubelet_stats`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/kubeletstatsreceiver): для получения метрик уровня узла. Этому приёмнику требуется, чтобы переменная окружения `K8S_NODE_NAME` была установлена в `spec.nodeName` с помощью [Kubernetes Downward API﻿](https://kubernetes.io/docs/concepts/workloads/pods/downward-api/) (см. [пример﻿](https://kubernetes.io/docs/tasks/inject-data-application/environment-variable-expose-pod-information/)).

1

Приёмник `k8sevents` в настоящее время находится на стадии alpha и может претерпеть значительные изменения. Несмотря на раннюю стадию зрелости, он включён в дистрибутив Dynatrace Collector для поддержки раннего внедрения и экспериментов. На этой стадии стабильность, производительность и полнота функциональности не гарантируются.

#### Процессоры

В разделе `processors` мы указываем следующие процессоры:

* [`filter`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/filterprocessor): для фильтрации атрибутов Kubernetes.
* [`k8sattributes`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/k8sattributesprocessor): для извлечения и предоставления данных о подах.
* [`transform`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/transformprocessor): для преобразования метрик Kubernetes. Для этого требуется, чтобы переменная окружения `CLUSTER_NAME` была установлена в имя кластера. Укажите в качестве значения переменной произвольное имя, под которым кластер должен отображаться в Dynatrace.
* [`cumulativetodelta`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/cumulativetodeltaprocessor): для включения преобразования накопительных (cumulative) метрик.

#### Экспортёры

В разделе `exporters` мы указываем [экспортёр `otlp_http`﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/exporter/otlphttpexporter) и настраиваем его с URL нашего Dynatrace API и необходимым токеном аутентификации.

Для этого мы задаём две следующие переменные окружения и ссылаемся на них в значениях конфигурации `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL эндпойнта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте об эндпойнтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпойнтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.")

#### Extensions

В разделе `extensions` мы указываем [расширение `k8sleaderelector`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/extension/k8sleaderelector) для выбора лидера среди реплик агента, который будет собирать и экспортировать телеметрию уровня кластера.
Это гарантирует, что данные в любой момент собирает только один экземпляр коллектора, что позволяет избежать дублирования телеметрии.

#### Пайплайны сервиса

В разделе `service` мы собираем объекты приёмников, процессоров и экспортёров в пайплайны для трейсов, метрик и логов. Эти пайплайны позволяют отправлять сигналы OpenTelemetry через экземпляр коллектора и автоматически обогащать их дополнительными деталями, специфичными для Kubernetes.

## Использование Data Explorer

Data Explorer значительно расширяет возможности по запросу и визуализации метрик.
Подробнее см. в [Data Explorer](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразуйте результаты, чтобы получить нужные инсайты.").

## Использование пользовательских дашбордов

О настройке пользовательских дашбордов см. в [Dashboards](/managed/analyze-explore-automate/dashboards-classic "Узнайте, как создавать, управлять и использовать Dynatrace Dashboards Classic.").

## Ограничения

Данные принимаются по протоколу OpenTelemetry (OTLP) через [Dynatrace OTLP APIы](/managed/ingest-from/opentelemetry/otlp-api "Узнайте об эндпойнтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") и подчиняются лимитам и ограничениям API.
Подробнее см.:

* [Ограничения метрик OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения применяются.")
* [Сопоставление метрик Dynatrace](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения применяются.")
* [Приём логов OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs "Узнайте, как Dynatrace принимает записи логов OpenTelemetry и какие ограничения применяются.")