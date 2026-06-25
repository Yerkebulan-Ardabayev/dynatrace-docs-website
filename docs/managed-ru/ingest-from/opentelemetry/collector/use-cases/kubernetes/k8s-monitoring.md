---
title: Мониторинг кластеров Kubernetes с помощью OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-monitoring
scraped: 2026-05-12T12:12:02.357698
---

# Мониторинг кластеров Kubernetes с помощью OTel Collector

# Мониторинг кластеров Kubernetes с помощью OTel Collector

* Практическое руководство
* Чтение: 5 мин
* Обновлено 20 ноября 2025 г.

OTel Collector обеспечивает широкую поддержку мониторинга кластеров Kubernetes и рабочих нагрузок. Он поддерживает различные компоненты receiver для сбора критически важных метрик о кластере Kubernetes, узлах и объектах.

Этот сценарий использования объясняет, как настроить ваш Collector для получения полной видимости в кластерах Kubernetes через [**Data Explorer**](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразовывайте результаты для получения нужных сведений.") или пользовательские панели мониторинга в Dashboards Classic.

Dynatrace Operator

Dynatrace рекомендует использовать [Dynatrace Operator для мониторинга Kubernetes](/managed/ingest-from/setup-on-k8s "Способы развёртывания и настройки Dynatrace в Kubernetes").
Однако этот сценарий использования предназначен специально для пользователей OpenTelemetry, которые предпочитают не развёртывать Dynatrace Operator.
Настройка Collector, описанная ниже, сделает данные мониторинга Kubernetes доступными для использования в [Data Explorer](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразовывайте результаты для получения нужных сведений.") и [Dashboards](/managed/analyze-explore-automate/dashboards-classic "Узнайте, как создавать, управлять и использовать Dynatrace Dashboards Classic.").

## Предварительные требования

* Один из следующих дистрибутивов Collector с receiver [Kubernetes Cluster](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/k8sclusterreceiver), [Kubernetes Events](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/k8seventsreceiver) и [Kubelet Stats](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/kubeletstatsreceiver):

  + [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [OTel Collector Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [специально собранный OTel Collector](/managed/ingest-from/opentelemetry/collector#collector-builder "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
* Развёртывание Collector в [режиме агента](/managed/ingest-from/opentelemetry/collector/deployment#dynatrace-docs--agent "Как развернуть Dynatrace OpenTelemetry Collector.") для телеметрии уровня узла и кластера
* [URL API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") вашей среды Dynatrace
* [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с соответствующей областью доступа
* [Kubernetes, настроенный](#kubernetes-configuration) для необходимого управления доступом на основе ролей

См. [Развёртывание Collector](/managed/ingest-from/opentelemetry/collector/deployment "Как развернуть Dynatrace OpenTelemetry Collector.") и [Настройку Collector](/managed/ingest-from/opentelemetry/collector/configuration "Как настроить OpenTelemetry Collector."), чтобы узнать, как настроить это с помощью приведённых ниже конфигураций.

## Демонстрационные конфигурации

### Конфигурация RBAC

Настройте следующий файл `rbac.yaml` для вашего экземпляра Kubernetes, чтобы разрешить Collector использовать Kubernetes API с типом аутентификации service-account.

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

### Конфигурация Collector

Service account

В дополнение к конфигурации Collector обязательно обновите конфигурацию Kubernetes, чтобы она соответствовала имени service account, указанному в [файле RBAC](#kubernetes-configuration)
(см. записи для [Helm](https://github.com/open-telemetry/opentelemetry-helm-charts/blob/opentelemetry-collector-0.127.2/charts/opentelemetry-collector/values.yaml#L245-L252) и [Operator](https://github.com/open-telemetry/opentelemetry-operator/blob/v0.150.0/docs/api/opentelemetrycollectors.md#opentelemetrycollectorspec)).

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



kubeletstats:



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



- kubeletstats



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

[Проверьте ваши настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "Как настроить OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

Рекомендация по processor cumulativetodelta

Рекомендуется устанавливать параметр `max_staleness` [processor cumulativetodelta](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/cumulativetodeltaprocessor) в значение, превышающее частоту получения Collector метрик (например, как часто метрики принимаются через OTLP или каков интервал сбора Prometheus). Это гарантирует, что ссылки на заброшенные потоки метрик не будут накапливаться в памяти с течением времени.

## Компоненты

Для нашей конфигурации мы настроили следующие компоненты:

#### Receivers

В разделе `receivers` мы указываем следующие компоненты receiver в качестве активных компонентов для нашего развёртывания:

* [`otlp`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/receiver/otlpreceiver): для приёма трассировок OTLP.
* [`k8sevents`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/k8seventsreceiver): для получения событий Kubernetes от сервера Kubernetes API. [1](#fn-1-1-def)
* [`k8s_cluster`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/k8sclusterreceiver): для получения метрик уровня кластера и событий сущностей от сервера Kubernetes API.
* [`kubeletstats`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/kubeletstatsreceiver): для получения метрик уровня узла. Для этого receiver необходимо задать переменную окружения `K8S_NODE_NAME` со значением `spec.nodeName` с помощью [Kubernetes Downward API](https://kubernetes.io/docs/concepts/workloads/pods/downward-api/) (см. [пример](https://kubernetes.io/docs/tasks/inject-data-application/environment-variable-expose-pod-information/)).

1

Receiver `k8sevents` в настоящее время находится на стадии альфа и может претерпевать значительные изменения. Несмотря на раннюю стадию зрелости, он включён в дистрибутив Dynatrace Collector для поддержки раннего освоения и экспериментирования. Следует учитывать, что стабильность, производительность и полнота функциональности на данном этапе не гарантированы.

#### Processors

В разделе `processors` мы указываем следующие компоненты processor:

* [`filter`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/filterprocessor): для фильтрации атрибутов Kubernetes.
* [`k8sattributes`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/k8sattributesprocessor): для извлечения и предоставления данных подов.
* [`transform`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/transformprocessor): для преобразования метрик Kubernetes. Для этого необходимо задать переменную окружения `CLUSTER_NAME` с именем кластера. Задайте произвольное имя, под которым кластер будет отображаться в Dynatrace.
* [`cumulativetodelta`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/cumulativetodeltaprocessor): для включения преобразования кумулятивных метрик.

#### Exporters

В разделе `exporters` мы указываем [exporter `otlp_http`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/exporter/otlphttpexporter) и настраиваем его с помощью URL нашего Dynatrace API и необходимого токена аутентификации.

Для этого мы задаём следующие две переменные окружения и ссылаемся на них в значениях конфигурации `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.")

#### Extensions

В разделе `extensions` мы указываем [extension `k8sleaderelector`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/extension/k8sleaderelector) для выбора ведущего среди реплик агентов, который будет собирать и экспортировать телеметрию уровня кластера.
Это гарантирует, что в каждый момент времени данные собирает только один экземпляр Collector, что позволяет избежать дублирования телеметрии.

#### Сервисные конвейеры

В разделе `service` мы собираем наши объекты receiver, processor и exporter в конвейеры для трассировок, метрик и логов. Эти конвейеры позволяют отправлять сигналы OpenTelemetry через экземпляр Collector с их автоматическим обогащением дополнительными сведениями, специфичными для Kubernetes.

## Использование Data Explorer

Data Explorer значительно расширяет возможности запроса и визуализации метрик.
Дополнительные сведения см. в разделе [Data Explorer](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразовывайте результаты для получения нужных сведений.").

## Использование пользовательских панелей мониторинга

Сведения о настройке пользовательских панелей мониторинга см. в разделе [Dashboards](/managed/analyze-explore-automate/dashboards-classic "Узнайте, как создавать, управлять и использовать Dynatrace Dashboards Classic.").

## Пределы и ограничения

Данные принимаются с помощью протокола OpenTelemetry (OTLP) через [Dynatrace OTLP API](/managed/ingest-from/opentelemetry/otlp-api "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") и подчиняются ограничениям и лимитам этого API.
Дополнительные сведения см.:

* [Ограничения метрик OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения применяются.")
* [Сопоставление метрик Dynatrace](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения применяются.")
* [Приём логов OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs "Узнайте, как Dynatrace принимает записи логов OpenTelemetry и какие ограничения применяются.")