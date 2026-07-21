---
title: Отправка данных OpenTelemetry с помощью экспортера Kafka
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/kafka/exporter
---

# Отправка данных OpenTelemetry с помощью экспортера Kafka

# Отправка данных OpenTelemetry с помощью экспортера Kafka

* Практическое руководство
* 3 мин на чтение
* Обновлено 11 мая 2026 г.

Следующий пример конфигурации показывает, как настроить экземпляр Collector для экспорта данных OTLP в Kafka.

## Предварительные требования

* Развёрнутый и настроенный дистрибутив Collector, будь то:

  + [Dynatrace Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + [OpenTelemetry Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + [пользовательская версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
* Компонент [`kafkaexporter`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/exporter/kafkaexporter).
* Развёрнутый сервер Kafka с доступным `BROKER_ADDRESS`.
  Подробнее см. в [руководстве по быстрому старту Kafka Apache﻿](https://kafka.apache.org/quickstart).

## Демонстрационная конфигурация

Ниже приведён пример файла YAML для базовой конфигурации Collector, которую можно использовать для экспорта трасс, метрик и логов OpenTelemetry в Kafka.

```
processors:



memory_limiter:



check_interval: 1s



limit_percentage: 100



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



sending_queue:



batch:



send_batch_size: 500



flush_timeout: 30s



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

Чтобы эта конфигурация заработала, нужно задать переменную окружения `BROKER_ADDRESS`.
Значение зависит от конкретного сервера Kafka.

Проверка конфигурации

[Проверьте свои настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

В этой конфигурации настраиваются определённые компоненты, описанные в разделах ниже.

### Receivers

В разделе `receivers` в качестве активного компонента receiver для нашего развёртывания указывается [`otlp`﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/receiver/otlpreceiver).
Это необходимо для приёма данных OTLP.

### Processors

В разделе `processors` указываются:

* процессор [`memory_limiter`﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/processor/memorylimiterprocessor);
* процессор [`batch`﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/processor/batchprocessor) в соответствии с [рекомендацией для экспортера kafka﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/exporter/kafkaexporter#readme).

### Exporters

В разделе `exporters` указывается [экспортер `kafka`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/exporter/kafkaexporter) для пересылки данных на сервер Kafka.

### Service pipeline

В разделе `service` объекты receiver, processors и exporter собираются в service pipeline, который выполняет следующие шаги:

1. Принимает запросы OTLP на настроенных портах.
2. Использует процессор `memory_limit`, чтобы Collector не исчерпал память.
3. Группирует данные с помощью процессора `batch`.
4. Экспортирует данные на сервер Kafka.

## Смежные темы

* [OTel Collector для приёма телеметрии в Dynatrace](/managed/ingest-from/opentelemetry/collector "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
* [Буферизация данных через Kafka с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/kafka "How to configure the OpenTelemetry Collector to buffer data via Kafka.")
* [Приём данных OpenTelemetry с помощью ресивера Kafka](/managed/ingest-from/opentelemetry/collector/use-cases/kafka/receiver "How to configure the OpenTelemetry Collector's Kafka receiver to ingest OpenTelemetry from Kafka.")
* [Развёртывание Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector/deployment "How to deploy the Dynatrace OpenTelemetry Collector.")
* [Настройка OTel Collector](/managed/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.")