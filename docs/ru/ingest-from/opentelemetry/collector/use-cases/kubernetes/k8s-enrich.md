---
title: Обогащение OTLP-запросов данными Kubernetes
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich
scraped: 2026-03-04T21:31:34.112149
---

* Latest Dynatrace

Следующий пример конфигурации демонстрирует, как настроить экземпляр Collector для обогащения телеметрических данных OTLP дополнительными метаданными Kubernetes. Сюда входят, например, сведения о подах, развёртываниях и кластерах, что позволяет Dynatrace корректно сопоставлять полученные телеметрические данные с соответствующими сущностями в Dynatrace.

Dynatrace рекомендует использовать ActiveGate для улучшения мониторинга состояния и производительности вашего кластера Kubernetes.
Развёртывание ActiveGate позволяет приложению Dynatrace Kubernetes визуализировать данные Kubernetes и OpenTelemetry и сопоставлять их с соответствующими сущностями Kubernetes.

## Предварительные требования

* Развёрнутый ActiveGate для мониторинга Kubernetes API (необязательно)
* Один из следующих дистрибутивов Collector с процессорами [Kubernetes Attributes](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/k8sattributesprocessor) и [Transform](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/transformprocessor):

  + [Dynatrace Collector](../../../collector.md#dt-collector-dist "Узнайте о Dynatrace OTel Collector.")
  + [OpenTelemetry Contrib](../../../collector.md#collector-contrib "Узнайте о Dynatrace OTel Collector.")
  + [Пользовательская сборка Builder](../../../collector.md#collector-builder "Узнайте о Dynatrace OTel Collector.")
* Collector, развёрнутый в [режиме агента](../../deployment.md#dynatrace-docs--agent "Как развернуть Dynatrace OTel Collector.")
* [URL API](../../../otlp-api.md#export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") вашей среды Dynatrace
* [API-токен](../../../otlp-api.md#authentication-export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с необходимой областью доступа
* [Kubernetes, настроенный](#kubernetes-configuration) для необходимого управления доступом на основе ролей

См. Развёртывание Collector и Настройка Collector для получения информации о настройке Collector с приведённой ниже конфигурацией.

## Демонстрационная конфигурация

Учётная запись службы

В дополнение к конфигурации Collector обязательно обновите конфигурацию Kubernetes, чтобы она соответствовала имени учётной записи службы, используемому в [файле RBAC](#kubernetes-configuration) (см. записи для [Helm](https://github.com/open-telemetry/opentelemetry-helm-charts/blob/opentelemetry-collector-0.100.0/charts/opentelemetry-collector/values.yaml#L184-L191), [Operator](https://github.com/open-telemetry/opentelemetry-operator/blob/v0.144.0/docs/api.md#opentelemetrycollectorspec)).

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

[Проверьте свои настройки](../../configuration.md#validate "Как настроить OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Конфигурация Kubernetes

Настройте следующий файл `rbac.yaml` в вашем экземпляре Kubernetes, чтобы разрешить Collector использовать Kubernetes API с типом аутентификации service-account.

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

### Приёмники

В разделе `receivers` мы указываем стандартный приёмник `otlp` как активный компонент-приёмник для нашего экземпляра Collector.

Это сделано в основном для демонстрационных целей. Здесь можно указать любой другой допустимый приёмник (например, `zipkin`).

### Процессоры

В разделе `processors` мы указываем [процессор `k8sattributes`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/k8sattributesprocessor) со следующими параметрами:

* `extract` — указывает, какую информацию следует извлечь.
* `pod_association` — указывает, как информация о поде связывается с атрибутами.

Обратите внимание, что атрибут `k8s.container.name` будет извлечён только если под, от которого получен входящий
сигнал, содержит только один контейнер, или если полученный сигнал содержит атрибут ресурса `k8s.container.id`.
В противном случае процессор k8sattributes не сможет корректно сопоставить нужный контейнер.

Dynatrace Operator обогащает данные OpenTelemetry от подов Kubernetes аннотациями `metadata.dynatrace.com`. При наличии этих аннотаций процессор `k8sattributes` извлекает их.

Мы также настраиваем [процессор `transform`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/transformprocessor), чтобы информация о кластере Kubernetes автоматически добавлялась как атрибуты ресурса для всех телеметрических сигналов.

### Экспортёры

В разделе `exporters` мы указываем стандартный [экспортёр `otlp_http`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/exporter/otlphttpexporter) и настраиваем его с URL Dynatrace API и необходимым токеном аутентификации.

Для этого мы задаём следующие две переменные окружения и ссылаемся на них в конфигурационных значениях `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL конечной точки Dynatrace API](../../../otlp-api.md#export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [API-токен](../../../otlp-api.md#authentication-export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.")

### Конвейеры сервиса

В разделе `service` мы объединяем наши объекты приёмников, процессоров и экспортёров в конвейеры для трассировок, метрик и логов. Эти конвейеры позволяют отправлять сигналы OpenTelemetry через экземпляр Collector и автоматически обогащать их дополнительными сведениями, специфичными для Kubernetes.

## Ограничения

Данные передаются по протоколу OpenTelemetry (OTLP) через Dynatrace OTLP API и подчиняются ограничениям и лимитам API.
Дополнительную информацию см.:

* Ограничения метрик OpenTelemetry
* [Сопоставление метрик Dynatrace](../../../otlp-api/ingest-otlp-metrics/about-metrics-ingest.md#dynatrace-mapping "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения действуют.")
* Приём логов OpenTelemetry

## Связанные темы

* Обогащение принятых данных полями, специфичными для Dynatrace
