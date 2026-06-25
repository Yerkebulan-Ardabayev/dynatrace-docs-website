---
title: Сбор метрик Prometheus с помощью OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/prometheus
scraped: 2026-05-12T11:50:02.827907
---

# Сбор метрик Prometheus с помощью OTel Collector

# Сбор метрик Prometheus с помощью OTel Collector

* Практическое руководство
* Чтение: 2 мин
* Обновлено 04 мая 2026 г.

В следующем примере конфигурации показано, как настроить экземпляр Collector для сбора данных из существующей установки Prometheus и их импорта в виде запроса OTLP в Dynatrace.

## Предварительные требования

* Экземпляр Prometheus, работающий на порту 8888
* Один из следующих дистрибутивов Collector с [receiver Prometheus](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/prometheusreceiver), [processor metric start time](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/metricstarttimeprocessor) и [processor cumulative-to-delta](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/cumulativetodeltaprocessor):

  + [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + OpenTelemetry [Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [пользовательская версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
* [URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."), на который должны экспортироваться данные
* [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") с соответствующей областью доступа (требуется только для SaaS и ActiveGate)

См. [Развёртывание Collector](/managed/ingest-from/opentelemetry/collector/deployment "Как развернуть Dynatrace OpenTelemetry Collector.") и [Настройку Collector](/managed/ingest-from/opentelemetry/collector/configuration "Как настроить OpenTelemetry Collector."), чтобы узнать, как настроить ваш Collector с приведённой ниже конфигурацией.

## Демонстрационная конфигурация

Dynatrace Collector v0.41.0+

В приведённом ниже конвейере используется [processor `metricstarttime`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/metricstarttimeprocessor), который добавляет к метрикам начальные метки времени, и [processor `cumulativetodelta`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/cumulativetodeltaprocessor), который преобразует метрики в дельта-темпоральность.

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

Dynatrace OTel Collector v0.40.0 или ранее

Чтобы продолжить корректировать начальные значения времени в receiver Prometheus, запустите Collector со следующим флагом:

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

Проверка конфигурации

[Проверьте ваши настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "Как настроить OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

Рекомендация по processor cumulativetodelta

Рекомендуется задавать параметру `max_staleness` [processor cumulativetodelta](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/cumulativetodeltaprocessor) значение, превышающее частоту получения метрик Collector (например, частоту получения метрик через OTLP или длительность интервала сбора Prometheus). Это гарантирует, что со временем в памяти не накапливаются ссылки на заброшенные потоки метрик.

## Компоненты

Для нашей конфигурации мы настраиваем следующие компоненты.

### Receivers

В разделе `receivers` мы указываем receiver `prometheus` в качестве активного компонента receiver для нашего экземпляра Collector. Мы настраиваем receiver двумя заданиями `node-exporter` и `opentelemetry-collector` в разделе `scrape_configs`, чтобы получать данные с указанных хостов раз в минуту (`scrape_interval: 60s`).

Полный список параметров конфигурации см. в [документации Prometheus](https://github.com/prometheus/prometheus/blob/v2.28.1/docs/configuration/configuration.md).

### Processors

В разделе `processors` мы указываем [processor `cumulativetodelta`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/cumulativetodeltaprocessor), чтобы преобразовать метрики, выдаваемые receiver Prometheus, в их [формат дельта-агрегации](/managed/ingest-from/opentelemetry/collector/configuration#delta-metrics "Как настроить OpenTelemetry Collector.").

В Dynatrace Collector v0.41.0+ мы указываем
[processor `metricstarttime`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/metricstarttimeprocessor),
чтобы
добавить к метрикам начальные метки времени. Это необходимо для корректного преобразования метрик в дельта-темпоральность.

### Exporters

В разделе `exporters` мы указываем стандартный [exporter `otlp_http`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/exporter/otlphttpexporter) и настраиваем его с помощью URL нашего Dynatrace API и необходимого токена аутентификации.

Для этого мы задаём следующие две переменные окружения и ссылаемся на них в значениях конфигурации `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.")

### Сервисный конвейер

В разделе `service` мы собираем наши объекты receiver, processor и exporter в конвейер метрик, который выполняет задания Prometheus, преобразует их метрики в дельта-значения и принимает данные в Dynatrace.

## Пределы и ограничения

Метрики принимаются с помощью протокола OpenTelemetry (OTLP) через [Dynatrace OTLP API](/managed/ingest-from/opentelemetry/otlp-api "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") и подчиняются ограничениям и лимитам этого API.
Дополнительные сведения см.:

* [Ограничения метрик OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения применяются.")
* [Сопоставление метрик Dynatrace](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения применяются.")

Во избежание дублирования данных убедитесь, что заданную цель собирает только один OTel Collector (например, брокер Kafka или эндпоинт Prometheus).

Если вы запускаете несколько реплик OTel Collector, настройте каждую из них на свою цель. Это предотвращает дублирование метрик и лишние затраты на приём данных.

[Target Allocator](https://opentelemetry.io/docs/platforms/kubernetes/operator/target-allocator/) автоматически распределяет цели Prometheus между пулом OTel Collector.

## Связанные темы

* [Обогащение принимаемых данных полями, специфичными для Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace.")
* [Обогащение запросов OTLP данными Kubernetes](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Настройте OpenTelemetry Collector для обогащения запросов OTLP данными Kubernetes.")
* [Источник данных Prometheus](/managed/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions "Узнайте, как создать расширение Prometheus с помощью фреймворка Extensions.")