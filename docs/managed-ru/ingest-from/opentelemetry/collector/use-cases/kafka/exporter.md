---
title: Пересылка данных OpenTelemetry с помощью exporter Kafka
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/kafka/exporter
scraped: 2026-05-12T12:15:10.036789
---

# Пересылка данных OpenTelemetry с помощью exporter Kafka

# Пересылка данных OpenTelemetry с помощью exporter Kafka

* Практическое руководство
* Чтение: 3 мин
* Опубликовано 05 ноября 2025 г.

В следующем примере конфигурации показано, как настроить экземпляр Collector для экспорта данных OTLP в Kafka.

## Предварительные требования

* Развёрнутый и настроенный дистрибутив Collector, будь то:

  + [Dynatrace Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [OpenTelemetry Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [пользовательская версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
* Компонент [`kafkaexporter`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/exporter/kafkaexporter).
* Развёрнутый сервер Kafka с доступным `BROKER_ADDRESS`.
  Дополнительные сведения см. в [руководстве по быстрому старту Apache Kafka](https://kafka.apache.org/quickstart).

## Демонстрационная конфигурация

Ниже приведён пример YAML-файла для базовой конфигурации Collector, который можно использовать для экспорта трассировок, метрик и логов OpenTelemetry в Kafka.

```
processors:



memory_limiter:



check_interval: 1s



limit_percentage: 100



batch:



send_batch_size: 500



timeout: 30s



receivers:



otlp:



protocols:



grpc:



endpoint: 0.0.0.0:4317



exporters:



kafka:



brokers: ["${env:BROKER_ADDRESS}"]



tls:



insecure: true # Only necessary if your Kafka server does not provide a certificate that's trusted by the OTel Collector.



traces:



metrics:



logs:



service:



pipelines:



traces:



receivers: [otlp]



processors: [memory_limiter, batch]



exporters: [kafka]



metrics:



receivers: [otlp]



processors: [memory_limiter, batch]



exporters: [kafka]



logs:



receivers: [otlp]



processors: [memory_limiter, batch]



exporters: [kafka]
```

Чтобы эта конфигурация работала, необходимо задать переменную окружения `BROKER_ADDRESS`.
Значение зависит от вашего сервера Kafka.

Проверка конфигурации

[Проверьте ваши настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "Как настроить OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

Для нашей конфигурации мы настраиваем определённые компоненты, как описано в разделах ниже.

### Receivers

В разделе `receivers` мы указываем [`otlp`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/receiver/otlpreceiver) в качестве активного компонента receiver для нашего развёртывания.
Это необходимо для приёма данных OTLP.

### Processors

В разделе `processors` мы указываем:

* [processor `memory_limiter`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/processor/memorylimiterprocessor).
* [processor `batch`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/processor/batchprocessor) согласно [рекомендации для exporter kafka](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/exporter/kafkaexporter#readme).

### Exporters

В разделе `exporters` мы указываем [exporter `kafka`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/exporter/kafkaexporter) для пересылки данных на сервер Kafka.

### Сервисный конвейер

В разделе `service` мы собираем наши объекты receiver, processor и exporter в сервисные конвейеры, которые выполняют следующие шаги:

1. Принимают запросы OTLP на настроенных портах.
2. Используют processor `memory_limit`, чтобы у Collector не закончилась память.
3. Группируют данные с помощью processor `batch`.
4. Экспортируют данные на сервер Kafka.

## Связанные темы

* [OTel Collector для приёма телеметрии в Dynatrace](/managed/ingest-from/opentelemetry/collector "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
* [Буферизация данных через Kafka с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/kafka "Как настроить OpenTelemetry Collector для буферизации данных через Kafka.")
* [Приём данных OpenTelemetry с помощью receiver Kafka](/managed/ingest-from/opentelemetry/collector/use-cases/kafka/receiver "Как настроить receiver Kafka в OpenTelemetry Collector для приёма OpenTelemetry из Kafka.")
* [Развёртывание Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector/deployment "Как развернуть Dynatrace OpenTelemetry Collector.")
* [Настройка OTel Collector](/managed/ingest-from/opentelemetry/collector/configuration "Как настроить OpenTelemetry Collector.")