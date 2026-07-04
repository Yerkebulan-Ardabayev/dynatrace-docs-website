---
title: Мониторинг Kong Gateway
source: https://docs.dynatrace.com/managed/ingest-from/technology-support/application-software/nginx/kong-gateway
scraped: 2026-05-12T11:23:25.123310
---

# Kong Gateway monitoring

# Kong Gateway monitoring

* Чтение: 4 мин
* Обновлено 04 сентября 2024 г.

Для включения мониторинга Kong в Dynatrace доступны следующие варианты.

* Рекомендуется: включить OneAgent для журналов шлюза, трассировок и мониторинга процессов. Этот вариант следует сочетать со сбором метрик Prometheus в Dynatrace для мониторинга метрик Kong Gateway.
* Мониторинг Kong с использованием OpenTelemetry для трассировок и Prometheus для метрик Kong Gateway.

OneAgent

OpenTelemetry

## Процесс и журналы Kong Gateway

OneAgent автоматически отслеживает процесс Kong Gateway и его журналы.

### Предварительные требования

* Kong Gateway версии 2.8+
* OneAgent или Dynatrace Operator установлен и доступен для мониторинга Kong Gateway.

Необходимый способ установки зависит от приложения:

| Если приложение выполняется | Инструкция |
| --- | --- |
| на виртуальной машине или физическом сервере | [OneAgent](/managed/ingest-from/dynatrace-oneagent/installation-and-operation "Установка OneAgent на сервер в первый раз.") |
| как рабочая нагрузка в Kubernetes или OpenShift | [Dynatrace Operator](/managed/ingest-from/setup-on-k8s/deployment "Развёртывание Dynatrace Operator в Kubernetes") |

## Трассировки приложения

Помимо процесса и журналов, OneAgent также предоставляет трассировки приложения Kong Gateway. См. [Инструментирование во время выполнения](/managed/ingest-from/technology-support/application-software/nginx/manual-runtime-instrumentation "Узнайте, как принудительно инструментировать пропатченные/нестандартные двоичные файлы NGINX во время выполнения.") для NGINX.

## Шаг 1. Настройка Kong Gateway

### Предварительные требования

* Kong Gateway версии 3.8+

Kong Gateway требует настройки двух параметров.

* `tracing_instrumentations = all`
* `tracing_sampling_rate = 1.0`

Подробнее о параметрах см. в [документации Kong Gateway](https://dt-url.net/2m03q66).

## Шаг 2. Настройка плагина OpenTelemetry

1. Оцените поддержку ведения журналов и трассировки согласно [версии плагина OpenTelemetry](https://dt-url.net/1423wjw), установленной в вашей среде.
2. Отправьте следующий POST-запрос (пример рассчитан на Kong Gateway 3.8+), заменив `{HOST}`, `{PLUGIN-INSTANCE_NAME}` и `{OPENTELEMETRY_COLLECTOR}` нужными значениями:

```
curl -X POST http://{HOST}:8001/plugins \



-H 'Content-Type: application/json' \



-d '{



"name": "opentelemetry",



"instance_name": "{PLUGIN-INSTANCE_NAME}",



"config": {



"traces_endpoint": "http://{OPENTELEMETRY_COLLECTOR}:4318/v1/traces",



"logs_endpoint": "http://{OPENTELEMETRY_COLLECTOR}:4318/v1/logs",



"resource_attributes": {



"service.name": "kong-dev"



}



}



}'
```

## Шаг 3. Настройка OpenTelemetry Collector

Настройте OpenTelemetry Collector для отправки данных в среду Dynatrace. Пример ниже демонстрирует экспорт трассировок и журналов.

```
receivers:



otlp:



protocols:



http:



endpoint: 0.0.0.0:4318



exporters:



otlp_http:



endpoint: "${env:DT_BASEURL}/api/v2/otlp"



headers:



"Authorization": "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



traces:



receivers: [otlp]



processors: []



exporters: [otlp_http]



logs:



receivers: [otlp]



processors: []



exporters: [otlp_http]
```

## Шаг 3. Экспорт метрик спанов приложения

Чтобы включить метрики спанов для трассировок приложения, настройте раздел exporters коллектора в конфигурации OpenTelemetry Collector.

```
connectors:



spanmetrics:



dimensions:



- name: http.method



default: GET



- name: http.status_code



- name: http.route



exclude_dimensions:



- status.code



metrics_flush_interval: 15s



histogram:



disable: false



service:



pipelines:



traces:



receivers: [otlp]



processors: []



exporters: [spanmetrics]



metrics:



receivers: [spanmetrics]



processors: []



exporters: [otlp_http]
```

## Метрики

Плагин Prometheus для Kong является удобным способом сбора метрик Kong Gateway. Dynatrace может получать эти метрики непосредственно с шлюза через плагин Kong. Порт и эндпоинт по умолчанию: `8001/metrics`.

Подробнее и со списком доступных метрик см. в [документации плагина Kong Prometheus](https://dt-url.net/gp23qq7).

## Шаг 1. Включение плагина Kong Prometheus

### Базовая конфигурация

Чтобы включить базовую конфигурацию плагина Kong Prometheus, отправьте POST-запрос, заменив `{HOST}` именем хоста.

```
curl -s -X POST http://{HOST}:8001/plugins \



-H 'Content-Type: application/json' \



-d '{



"name": "prometheus"



}'
```

### Дополнительные метрики плагина

Чтобы включить дополнительные метрики плагина Kong Gateway Prometheus, отправьте POST-запрос, заменив `{HOST}` и `{PLUGIN-INSTANCE_NAME}` нужными значениями:

```
curl -s -X POST http://{HOST}:8001/plugins \



-H 'Content-Type: application/json' \



-d '{



"name": "prometheus",



"instance_name": "{PLUGIN-INSTANCE_NAME}",



"config": {



"per_consumer": true,



"status_code_metrics": true,



"latency_metrics": true,



"bandwidth_metrics": true,



"upstream_health_metrics": true



}



}'
```

Чтобы проверить доступные метрики Kong, выполните запрос к эндпоинту `/metrics`:

```
curl -i http://{HOST}:8001/metrics
```

## Шаг 2. Сбор метрик Prometheus

После настройки [плагина Prometheus для Kong Gateway](https://dt-url.net/gp23qq7) метрики можно собирать с помощью Dynatrace ActiveGate (рекомендуется) или OpenTelemetry Collector.

ActiveGate

OpenTelemetry Collector

### Сбор метрик с помощью ActiveGate

В Kubernetes Dynatrace поддерживает сбор данных с эндпоинтов Prometheus с помощью специальных аннотаций.

Подробнее о сборе метрик Prometheus в Kubernetes см. в разделе [Мониторинг метрик Prometheus](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-prometheus-metrics "Приём метрик с эндпоинтов Prometheus в Kubernetes, алерты на метрики и потребление мониторинга.").

### Сбор метрик с помощью OpenTelemetry Collector

Также можно использовать receiver Prometheus в OpenTelemetry Collector для сбора метрик Kong Gateway. Подробнее о сборе данных Prometheus с помощью OpenTelemetry Collector см. в разделе [Сбор метрик Prometheus с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/prometheus "Настройка OpenTelemetry Collector для сбора данных Prometheus.").

При работе в Kubernetes можно обогащать трассировки, метрики и журналы с помощью процессора атрибутов Kubernetes в коллекторе. Это позволяет Dynatrace сопоставлять данные телеметрии с правильной топологией. Подробнее о включении обогащения в OpenTelemetry Collector см. в разделе [Обогащение OTLP-запросов данными Kubernetes](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Настройка OpenTelemetry Collector для обогащения OTLP-запросов данными Kubernetes.").