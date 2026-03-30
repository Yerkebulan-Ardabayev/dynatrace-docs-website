---
title: Мониторинг Kong Gateway
source: https://www.dynatrace.com/docs/ingest-from/technology-support/application-software/nginx/kong-gateway
scraped: 2026-03-05T21:26:34.967295
---

* Latest Dynatrace
* 4-min read

Для включения наблюдаемости Kong в Dynatrace доступны следующие варианты.

* Рекомендуемый вариант: включите OneAgent для журналов, трассировок и мониторинга процессов шлюза. Это следует сочетать со сбором метрик Dynatrace Prometheus для мониторинга метрик Kong Gateway.
* Мониторинг Kong с использованием комбинации OpenTelemetry для трассировок и Prometheus для метрик Kong Gateway.

OneAgent

OpenTelemetry

## Процесс и журналы Kong Gateway

OneAgent автоматически отслеживает процесс и журналы Kong Gateway.

### Предварительные требования

* Kong Gateway версии 2.8+
* OneAgent или Dynatrace Operator установлен и доступен для мониторинга вашего Kong Gateway.

Необходимая установка зависит от вашего приложения:

| Если ваше приложение работает | См. инструкцию для |
| --- | --- |
| на виртуальной машине или bare-metal | OneAgent |
| как рабочая нагрузка в Kubernetes или OpenShift | Dynatrace Operator |

## Трассировки приложений

Помимо процесса и журналов, OneAgent также предоставляет трассировки приложений Kong Gateway. См. Ручная инструментация времени выполнения для NGINX.

## Шаг 1. Настройка Kong Gateway

### Предварительные требования

* Kong Gateway версии 3.8+

Kong Gateway требует настройки двух параметров.

* `tracing_instrumentations = all`
* `tracing_sampling_rate = 1.0`

Для получения дополнительной информации и параметров см. [документацию Kong Gateway](https://dt-url.net/2m03q66).

## Шаг 2. Настройка плагина OpenTelemetry

1. Оцените поддержку логирования и трассировки в соответствии с [версией плагина OpenTelemetry](https://dt-url.net/1423wjw), установленной в вашей среде.
2. Отправьте следующий POST-запрос (пример предполагает Kong Gateway 3.8+), заменив `{HOST}`, `{PLUGIN-INSTANCE_NAME}` и `{OPENTELEMETRY_COLLECTOR}` соответствующими значениями:

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

Настройте OpenTelemetry Collector для отправки данных в вашу среду Dynatrace. Пример ниже показывает, как экспортировать трассировки и журналы.

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

## Шаг 3. Экспорт метрик спанов приложений

Чтобы включить метрики спанов для трассировок приложений, настройте раздел экспортеров коллектора в конфигурации OpenTelemetry Collector.

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

Плагин Prometheus для Kong -- это удобный способ сбора метрик Kong Gateway. Dynatrace может собирать эти метрики напрямую с шлюза, генерируемые плагином Kong. Порт и эндпоинт по умолчанию -- `8001/metrics`.

Для получения дополнительной информации и списка доступных метрик см. [документацию плагина Kong Prometheus](https://dt-url.net/gp23qq7).

## Шаг 1. Включение плагина Kong Prometheus

### Базовая конфигурация

Чтобы включить базовую конфигурацию плагина Kong Prometheus, отправьте POST-запрос, заменив `{HOST}` значением имени хоста.

```
curl -s -X POST http://{HOST}:8001/plugins \


-H 'Content-Type: application/json' \


-d '{


"name": "prometheus"


}'
```

### Дополнительные метрики плагина

Чтобы включить дополнительные метрики, создаваемые плагином Kong Gateway Prometheus, отправьте POST-запрос, заменив `{HOST}` и `{PLUGIN-INSTANCE_NAME}` соответствующими значениями:

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

После настройки [плагина Prometheus для Kong Gateway](https://dt-url.net/gp23qq7) метрики могут быть собраны с использованием Dynatrace ActiveGate (рекомендуется) или OpenTelemetry Collector.

ActiveGate

OpenTelemetry Collector

### Сбор метрик с использованием ActiveGate

В Kubernetes Dynatrace поддерживает сбор данных с эндпоинтов Prometheus с использованием специальных аннотаций.

Чтобы узнать, как собирать метрики Prometheus в Kubernetes, см. Мониторинг метрик Prometheus.

### Сбор метрик с использованием OpenTelemetry Collector

Вы также можете использовать приемник Prometheus в OpenTelemetry Collector для сбора метрик с Kong Gateway. Чтобы узнать, как собирать данные Prometheus с помощью OpenTelemetry Collector, см. Сбор метрик Prometheus с помощью OpenTelemetry Collector.

Если вы работаете в Kubernetes, вы можете обогащать трассировки, метрики и журналы с помощью процессора атрибутов Kubernetes в Collector. Это позволяет Dynatrace сопоставлять данные телеметрии с правильной топологией. Чтобы узнать, как включить обогащение в OpenTelemetry Collector, см. Обогащение OTLP-запросов данными Kubernetes.
