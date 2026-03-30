---
title: Сбор метрик Prometheus с помощью OpenTelemetry Collector
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/use-cases/prometheus
scraped: 2026-03-05T21:40:09.842786
---

Следующий пример конфигурации показывает, как настроить экземпляр Collector для сбора данных из существующей установки Prometheus и импорта их как OTLP-запрос в Dynatrace.

## Предварительные требования

* Экземпляр Prometheus, работающий на порту 8888
* Один из следующих дистрибутивов Collector с [Prometheus receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/receiver/prometheusreceiver), [metric start time processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/metricstarttimeprocessor) и [cumulative-to-delta processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/cumulativetodeltaprocessor):

  + [Dynatrace Collector](../../collector.md#dt-collector-dist "Узнайте о Dynatrace OTel Collector.")
  + OpenTelemetry [Contrib](../../collector.md#collector-contrib "Узнайте о Dynatrace OTel Collector.")
  + [Пользовательская версия Builder](../../collector.md#collector-builder "Узнайте о Dynatrace OTel Collector.")
* URL эндпоинта Dynatrace API, на который должны экспортироваться данные
* [API-токен](../../otlp-api.md#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с соответствующей областью доступа (требуется для ActiveGate)

См. Развёртывание Collector и Конфигурация Collector для информации о настройке вашего Collector с приведённой ниже конфигурацией.

## Демонстрационная конфигурация

Dynatrace Collector v0.41.0+

Приведённый ниже пример конвейера использует [`metricstarttime` processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/metricstarttimeprocessor), который необходим для преобразования метрик в дельта-темпоральность.

```
receivers:


prometheus:


config:


scrape_configs:


- job_name: 'node-exporter'


scrape_interval: 60s


static_configs:


- targets: ['prometheus-prometheus-node-exporter:9100']


- job_name: opentelemetry-collector


scrape_interval: 60s


static_configs:


- targets:


- 127.0.0.1:8888


processors:


metricstarttime:


cumulativetodelta:


max_staleness: 25h


exporters:


otlp_http:


endpoint: ${env:DT_ENDPOINT}


headers:


Authorization: "Api-Token ${env:DT_API_TOKEN}"


service:


pipelines:


metrics:


receivers: [prometheus]


processors: [metricstarttime, cumulativetodelta]


exporters: [otlp_http]
```

Dynatrace Collector v0.40.0 или более ранняя версия

В **v0.40.0** Dynatrace Collector необходимо запустить Collector
со следующим флагом, чтобы сохранить корректировку начального времени в
Prometheus receiver:

```
--feature-gates=-receiver.prometheusreceiver.RemoveStartTimeAdjustment
```

```
receivers:


prometheus:


config:


scrape_configs:


- job_name: 'node-exporter'


scrape_interval: 60s


static_configs:


- targets: ['prometheus-prometheus-node-exporter:9100']


- job_name: opentelemetry-collector


scrape_interval: 60s


static_configs:


- targets:


- 127.0.0.1:8888


processors:


cumulativetodelta:


max_staleness: 25h


exporters:


otlp_http:


endpoint: ${env:DT_ENDPOINT}


headers:


Authorization: "Api-Token ${env:DT_API_TOKEN}"


service:


pipelines:


metrics:


receivers: [prometheus]


processors: [cumulativetodelta]


exporters: [otlp_http]
```

Валидация конфигурации

[Проверьте ваши настройки](../configuration.md#validate "Как настроить OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

Рекомендация по cumulativetodelta processor

Рекомендуется установить параметр `max_staleness` процессора [cumulativetodelta](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/cumulativetodeltaprocessor) в значение, превышающее частоту получения метрик коллектором (например, частоту получения метрик через OTLP или длительность интервала скрейпинга Prometheus). Это гарантирует, что ссылки на заброшенные потоки метрик не будут накапливаться в памяти с течением времени.

## Компоненты

Для нашей конфигурации мы настраиваем следующие компоненты.

### Receivers

В секции `receivers` мы указываем receiver `prometheus` как активный компонент-приёмник для нашего экземпляра Collector. Мы настраиваем receiver с двумя заданиями `node-exporter` и `opentelemetry-collector` в секции `scrape_configs` для получения данных с указанных хостов раз в минуту (`scrape_interval: 60s`).

Полный список параметров конфигурации см. в [документации Prometheus](https://github.com/prometheus/prometheus/blob/v2.28.1/docs/configuration/configuration.md).

### Processors

В секции `processors` мы указываем процессор [`cumulativetodelta`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/cumulativetodeltaprocessor) для преобразования метрик, генерируемых Prometheus receiver, в их [дельта-формат агрегации](../configuration.md#delta-metrics "Как настроить OpenTelemetry Collector.").

В Dynatrace Collector v0.41.0+ мы указываем процессор
[`metricstarttime`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/metricstarttimeprocessor)
для добавления начальных временных меток к метрикам. Это необходимо для корректного преобразования метрик в дельта-темпоральность.

### Exporters

В секции `exporters` мы указываем стандартный экспортёр [`otlp_http`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/exporter/otlphttpexporter) и настраиваем его с URL Dynatrace API и необходимым токеном аутентификации.

Для этого мы устанавливаем следующие две переменные окружения и ссылаемся на них в значениях конфигурации для `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL эндпоинта Dynatrace API](../../otlp-api.md#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [API-токен](../../otlp-api.md#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.")

### Конвейер сервиса

В секции `service` мы собираем наши объекты receiver, processor и exporter в конвейер метрик, который будет выполнять задания Prometheus, преобразовывать их метрики в дельта-значения и принимать данные в Dynatrace.

## Ограничения

Метрики принимаются по протоколу OpenTelemetry (OTLP) через Dynatrace OTLP API и подчиняются ограничениям API.
Дополнительную информацию см. в:

* Ограничения метрик OpenTelemetry
* [Маппинг метрик Dynatrace](../../otlp-api/ingest-otlp-metrics/about-metrics-ingest.md#dynatrace-mapping "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения применяются.")

Чтобы избежать дублирования данных, убедитесь, что только один OpenTelemetry Collector собирает данные с заданного целевого объекта (например, брокера Kafka или эндпоинта Prometheus).

Если вы запускаете несколько реплик коллектора, настройте каждую из них с разными целевыми объектами. Это предотвращает дублирование метрик и ненужные затраты на приём.

[Target Allocator](https://opentelemetry.io/docs/platforms/kubernetes/operator/target-allocator/) автоматически распределяет целевые объекты Prometheus между пулом коллекторов.

## Связанные темы

* Обогащение принятых данных полями Dynatrace
* Обогащение OTLP-запросов данными Kubernetes
