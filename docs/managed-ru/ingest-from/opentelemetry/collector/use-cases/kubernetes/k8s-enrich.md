---
title: Обогащение запросов OTLP данными Kubernetes
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich
scraped: 2026-05-12T12:04:40.123172
---

# Обогащение запросов OTLP данными Kubernetes

# Обогащение запросов OTLP данными Kubernetes

* Практическое руководство
* Чтение: 3 мин
* Обновлено 24 сентября 2025 г.

В следующем примере конфигурации показано, как настроить экземпляр Collector для обогащения данных телеметрии OTLP дополнительными метаданными Kubernetes. Это включает, например, сведения о поде, развёртывании и кластере, что позволяет Dynatrace корректно сопоставлять предоставленные данные телеметрии с соответствующими сущностями в Dynatrace.

Dynatrace рекомендует использовать ActiveGate для расширения мониторинга состояния и производительности вашего кластера Kubernetes.
Развёртывание ActiveGate позволяет приложению Dynatrace Kubernetes визуализировать данные Kubernetes и OpenTelemetry и сопоставлять их с соответствующими сущностями Kubernetes.

## Предварительные требования

* Развёрнутый ActiveGate для мониторинга Kubernetes API (необязательно)
* Один из следующих дистрибутивов Collector с processor [Kubernetes Attributes](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/k8sattributesprocessor) и [Transform](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/transformprocessor):

  + [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [OpenTelemetry Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [пользовательская версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
* OTel Collector, развёрнутый в [режиме агента](/managed/ingest-from/opentelemetry/collector/deployment#dynatrace-docs--agent "Как развернуть Dynatrace OpenTelemetry Collector.")
* [URL API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") вашей среды Dynatrace
* [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с соответствующей областью доступа
* [Kubernetes настроен](#kubernetes-configuration) для необходимого управления доступом на основе ролей

См. [Развёртывание Collector](/managed/ingest-from/opentelemetry/collector/deployment "Как развернуть Dynatrace OpenTelemetry Collector.") и [Настройку Collector](/managed/ingest-from/opentelemetry/collector/configuration "Как настроить OpenTelemetry Collector."), чтобы узнать, как настроить ваш Collector с приведённой ниже конфигурацией.

## Демонстрационная конфигурация

Service account

Помимо конфигурации Collector, необходимо также обновить конфигурацию Kubernetes, чтобы она соответствовала имени сервисного аккаунта, используемому в [файле RBAC](#kubernetes-configuration) (см. записи для [Helm](https://github.com/open-telemetry/opentelemetry-helm-charts/blob/opentelemetry-collector-0.100.0/charts/opentelemetry-collector/values.yaml#L184-L191), [Operator](https://github.com/open-telemetry/opentelemetry-operator/blob/v0.150.0/docs/api/opentelemetrycollectors.md#opentelemetrycollectorspec)).

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

[Проверьте ваши настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "Как настроить OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Конфигурация Kubernetes

Настройте следующий файл `rbac.yaml` в вашем экземпляре Kubernetes, чтобы разрешить OTel Collector использовать Kubernetes API с типом аутентификации через сервисный аккаунт.

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

Для нашей конфигурации мы настраиваем следующие компоненты.

### Receivers

В разделе `receivers` мы указываем стандартный receiver `otlp` в качестве активного компонента receiver для нашего экземпляра Collector.

Это сделано в основном в демонстрационных целях. Здесь можно указать любой другой допустимый receiver (например, `zipkin`).

### Processors

В разделе `processors` мы указываем [processor `k8sattributes`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/k8sattributesprocessor) со следующими параметрами:

* `extract`: задаёт, какие сведения следует извлекать.
* `pod_association`: задаёт, как информация о поде связывается с атрибутами.

Обратите внимание: атрибут `k8s.container.name` будет извлечён только в том случае, если под, из которого поступает
входящий сигнал, содержит только один контейнер, либо если принятый сигнал содержит атрибут ресурса `k8s.container.id`.
В противном случае processor k8sattributes не сможет корректно сопоставить нужный контейнер.

Dynatrace Operator обогащает данные OpenTelemetry из подов Kubernetes аннотациями `metadata.dynatrace.com`. При наличии этих аннотаций processor `k8sattributes` извлекает их.

Мы также настраиваем [processor `transform`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/transformprocessor) для автоматического добавления информации о кластере Kubernetes в качестве атрибутов ресурса для всех сигналов телеметрии.

### Exporters

В разделе `exporters` мы указываем стандартный [exporter `otlp_http`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/exporter/otlphttpexporter) и настраиваем его с помощью URL нашего Dynatrace API и необходимого токена аутентификации.

Для этого мы задаём следующие две переменные окружения и ссылаемся на них в значениях конфигурации `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.")

### Сервисные конвейеры

В разделе `service` мы собираем наши объекты receiver, processor и exporter в конвейеры для трассировок, метрик и логов. Эти конвейеры позволяют отправлять сигналы OpenTelemetry через экземпляр Collector с их автоматическим обогащением дополнительными сведениями, специфичными для Kubernetes.

## Пределы и ограничения

Данные принимаются с помощью протокола OpenTelemetry (OTLP) через [Dynatrace OTLP API](/managed/ingest-from/opentelemetry/otlp-api "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") и подчиняются ограничениям и лимитам этого API.
Дополнительные сведения см.:

* [Ограничения метрик OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения применяются.")
* [Сопоставление метрик Dynatrace](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения применяются.")
* [Приём логов OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs "Узнайте, как Dynatrace принимает записи логов OpenTelemetry и какие ограничения применяются.")

## Связанные темы

* [Обогащение принимаемых данных полями, специфичными для Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace.")