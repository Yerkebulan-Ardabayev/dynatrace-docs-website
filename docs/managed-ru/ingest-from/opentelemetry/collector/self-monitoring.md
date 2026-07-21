---
title: Самостоятельный мониторинг OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/self-monitoring
---

# Самостоятельный мониторинг OTel Collector

# Самостоятельный мониторинг OTel Collector

* Объяснение
* Чтение: 8 мин
* Обновлено 09 июня 2026 г.

OTel Collector предоставляет обширную внутреннюю телеметрию, которая помогает отслеживать его работу и устранять неполадки.

Ключевые возможности:

* **Время работы процесса и затраченное с момента старта процессорное время:** отслеживание того, сколько времени работает процесс, и сколько процессорного времени затрачено.
* **Использование памяти процессом и кучи:** отслеживание потребления памяти и использования кучи для обеспечения оптимальной производительности.
* **Receivers:** просмотр принятых и отклонённых элементов с разбивкой по типу данных.
* **Processors:** мониторинг входящих и исходящих элементов для понимания потока данных.
* **Exporters:** отслеживание отправленных элементов, элементов, которые не удалось поставить в очередь, и элементов, которые не удалось отправить, с разбивкой по типу данных. Также мониторинг размера и ёмкости очереди.
* **Запросы и ответы HTTP/gRPC:** количество, длительность и размер запросов и ответов для анализа эффективности взаимодействия.

## Отправка внутренней телеметрии (данных самостоятельного мониторинга) в Dynatrace

У каждого Collector есть возможности самостоятельного мониторинга, но их нужно активировать.

Данные самостоятельного мониторинга можно экспортировать из Collector по протоколу OTLP.

* Конфигурация ниже предполагает, что заданы переменные окружения `DT_ENDPOINT` и `DT_API_TOKEN`.
* Для отправки данных в Dynatrace через OTLP нужно указать endpoint Dynatrace и ingest-токен с областью действия `metrics.ingest`. Подробнее см. в [документации по OTLP Export](/managed/ingest-from/opentelemetry/otlp-api "Узнайте о OTLP-эндпоинтах API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace.").
* Переменная окружения `DT_ENDPOINT` должна содержать базовый URL и базовый путь `/api/v2/otlp`.

  Пример: `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`

Для отправки данных самостоятельного мониторинга в Dynatrace используй следующую конфигурацию:

```
service:



# turn on self-monitoring



telemetry:



metrics:



# metrics verbosity level. Higher verbosity means more metrics.



# The dashboard relies on metrics at level detailed.



level: detailed



# set up OTLP exporter



readers:



- periodic:



interval: 60000



exporter:



otlp:



protocol: http/protobuf



temporality_preference: delta



endpoint: "${env:DT_ENDPOINT}/v1/metrics"



headers:



- name: Authorization



value: "Api-Token ${env:DT_API_TOKEN}"
```

Обрати внимание: Collector умеет автоматически объединять конфигурационные файлы. Если предположить, что конфигурация выше сохранена в файле `selfmon-config.yaml`, Collector можно запустить так:

```
./dynatrace-otel-collector --config=your-already-existing-config.yaml --config=selfmon-config.yaml
```

Разумеется, конфигурацию можно добавить напрямую в существующую конфигурацию Collector.

Dynatrace принимает данные метрик с delta-темпоральностью по OTLP/HTTP.

* Collector и Collector Contrib версий 0.107.0 и выше, а также Dynatrace OTel Collector версий 0.12.0 и выше, поддерживают экспорт данных метрик в этом формате.
* Более ранние версии игнорируют флаг `temporality_preference`, и поэтому потребуют дополнительной обработки (конвертации из cumulative в delta) перед приёмом данных. Такую конвертацию можно выполнить с помощью экземпляра Collector, но это усложнит настройку, поэтому в данном документе она изначально не рассматривается.

## Обогащение данных самостоятельного мониторинга Collector атрибутами Kubernetes

По умолчанию Collector добавляет `service.instance.id` ко всем экспортируемым метрикам. Это позволяет различать экземпляры Collector.

Однако `service.instance.id`, это произвольно сгенерированный UUID, поэтому его не очень удобно интерпретировать. Экспортируемые данные можно обогатить дополнительными атрибутами, например атрибутами Kubernetes, которые проще интерпретировать человеку.

Есть два основных способа добавления атрибутов Kubernetes в данные телеметрии Collector:

* Внедрение соответствующих атрибутов в окружение контейнера, их чтение в Collector и добавление к телеметрическим данным, генерируемым на Collector.
* Отправка данных самостоятельного мониторинга Collector в его собственный receiver `otlp` и их обогащение с помощью процессора `k8sattributesprocessor` перед отправкой в Dynatrace через exporter `otlp_http`.

![Схема архитектуры самостоятельного мониторинга OTel Collector](https://cdn.bfldr.com/B686QPH3/as/89btfj36tbj3rs3z5ph89z97/Enriching_OpenTelemetry_Collector_self-monitoring_data_with_Kubernetes_attributes-Light_Mode?auto=webp&format=png&position=1)

Схема архитектуры самостоятельного мониторинга OTel Collector

### Чтение атрибутов из окружения контейнера

Нисходящий API Kubernetes позволяет внедрять информацию об окружении Kubernetes, в котором работает конкретный под.

Информацию о поде и контейнере можно передать в Collector через переменные окружения. В [документации Kubernetes﻿](https://kubernetes.io/docs/tasks/inject-data-application/environment-variable-expose-pod-information/#use-pod-fields-as-values-for-environment-variables) объясняется, как задавать такие данные, как имя узла, пространство имён или имя пода, в виде переменных окружения. Затем эти переменные становятся доступны для чтения внутри контейнера.

В следующем примере спецификации пода значения в `<>` являются заполнителями для фактических данных спецификации пода.

```
apiVersion: v1



kind: Pod



metadata:



name: <your-pod-name>



spec:



containers:



- name: <your-container>



image: <your-image>



env:



- name: MY_NODE_NAME



valueFrom:



fieldRef:



fieldPath: spec.nodeName



- name: MY_POD_NAME



valueFrom:



fieldRef:



fieldPath: metadata.name



- name: MY_POD_NAMESPACE



valueFrom:



fieldRef:



fieldPath: metadata.namespace
```

Конфигурация Collector для данных самостоятельного мониторинга позволяет добавлять атрибуты на основе переменных окружения.

Конфигурация ниже предполагает, что переменные окружения `MY_NODE_NAME`, `MY_POD_NAME` и `MY_POD_NAMESPACE` внедрены в контейнер Collector, и добавляет эти атрибуты к экспортируемым данным телеметрии. Для обогащения телеметрии «на лету» дополнительный экземпляр Collector не требуется.

```
service:



telemetry:



resource:



# This section reads the previously injected environment variables



# and attaches them to the telemetry the Collector generates about itself.



k8s.namespace.name: "${env:MY_POD_NAMESPACE}"



k8s.pod.name: "${env:MY_POD_NAME}"



k8s.node.name: "${env:MY_NODE_NAME}"



# the rest of the configuration did not change compared to above.



metrics:



level: detailed



readers:



- periodic:



exporter:



otlp:



endpoint: <...>
```

### Обогащение данных с помощью процессора k8sattributes

При таком подходе экземпляры Collector настраиваются на отправку своих внутренних данных телеметрии самим себе через receiver `otlp`, чтобы обогатить входящую телеметрию атрибутами Kubernetes с помощью процессора `k8sattributesprocessor`. Он получает эти данные из API Kuberenetes и прикрепляет их к проходящим через него данным телеметрии.

Для этого варианта в конфигурации Collector нужно настроить конвейер для обогащения данных самостоятельного мониторинга процессором `k8sattributesprocessor`:

```
receivers:



otlp:



protocols:



grpc:



endpoint: ${env:MY_POD_IP}:4317



http:



cors:



allowed_origins:



- http://*



- https://*



endpoint: ${env:MY_POD_IP}:4318



processors:



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



memory_limiter:



check_interval: 5s



limit_percentage: 80



spike_limit_percentage: 25



transform:



error_mode: ignore



metric_statements:



- context: resource



statements:



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

exporters:

otlp_http/dynatrace:

endpoint: ${env:DT_ENDPOINT}

headers:

Authorization: "Api-Token ${env:DT_API_TOKEN}"

sending_queue:

batch:

# Рекомендуемые значения по умолчанию для метрик

min_size: 3000

max_size: 3000

flush_timeout: 60s

service:

pipelines:

metrics:

receivers:

- otlp

processors:

- k8sattributes

- transform

- memory_limiter

- batch

exporters:

- otlp_http/dynatrace

# включить самомониторинг

telemetry:

metrics:

# уровень детализации метрик. Чем выше детализация, тем больше метрик.

# Дашборд использует метрики уровня detailed.

level: detailed

readers:

- periodic:

interval: 10000

timeout: 5000

exporter:

otlp:

protocol: http/protobuf

temporality_preference: delta

endpoint: ${env:MY_POD_IP}:4318
```