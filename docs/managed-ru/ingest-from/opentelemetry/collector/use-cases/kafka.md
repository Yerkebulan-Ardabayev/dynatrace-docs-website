---
title: Буферизация данных через Kafka с помощью OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/kafka
scraped: 2026-05-12T12:10:52.144934
---

# Буферизация данных через Kafka с помощью OTel Collector

# Буферизация данных через Kafka с помощью OTel Collector

* Пояснение
* Чтение: 1 мин
* Обновлено 04 мая 2026 г.

Когда вы используете Apache Kafka как транспортный слой для OTLP, вы повышаете надёжность, масштабируемость и гибкость своих конвейеров наблюдаемости.

Kafka разделяет производителей (агенты OTel Collector) и потребителей (шлюзы Collector).
Это помогает:

* Поглощать всплески трафика за счёт постоянной буферизации.
* Переживать сбои сети и бэкенда.
* Обеспечивать веерное распределение данных по нескольким нижестоящим системам.

Необходимое обогащение телеметрии большого объёма с резкими всплесками можно надёжно выполнять, сохраняя при этом защиту потоков данных.

## Обзор

Можно настроить компоненты Kafka exporter, Kafka receiver и Kafka Metrics receiver, как показано на рисунке ниже.

* Exporter: записывает данные OTLP в виде сообщений Kafka по каждому сигналу отдельно (`otlp_logs`, `otlp_metrics`, `otlp_spans`).
* Receiver: потребляет трассировки, метрики и логи из топиков Apache Kafka, а затем пересылает их в бэкенды, такие как Dynatrace.
* Kafka metrics receiver: собирает собственные операционные метрики Kafka (например, `broker count`) через OTLP и экспортирует их в Dynatrace.

Обратите внимание, что запуск Kafka может привнести дополнительные сквозные задержки, операционные накладные расходы и потенциальные узкие места.

![Communication between OTel Collector and Kafka server](https://cdn.bfldr.com/B686QPH3/as/8zmzr8jx66vpjsjxqkhg8jw/OpenTelemetry_-_Configuring_Kafka_exporter_receiver_and_Metrics_receiver_components_-_Light_Mode?auto=webp&format=png&position=1)

Обмен данными между OTel Collector и сервером Kafka

## Настройка

Настройте ваши экземпляры Collector, чтобы начать отправку данных в Kafka и из неё, а также в бэкенд Dynatrace.

[### Exporter

Настройте Collector для экспорта данных OTLP на сервер Kafka.](/managed/ingest-from/opentelemetry/collector/use-cases/kafka/exporter "Как настроить OpenTelemetry Collector для пересылки данных OpenTelemetry с помощью exporter Kafka.")[### Receiver

Настройте Collector для приёма данных OTLP с сервера Kafka.](/managed/ingest-from/opentelemetry/collector/use-cases/kafka/receiver "Как настроить receiver Kafka в OpenTelemetry Collector для приёма OpenTelemetry из Kafka.")[### Kafka Metrics Receiver

Настройте Collector для сбора операционных метрик Kafka и их экспорта в Dynatrace.](/managed/ingest-from/opentelemetry/collector/use-cases/kafka/kafkametrics "Как настроить OpenTelemetry Collector для сбора метрик с вашего сервера Kafka.")

## Связанные темы

* [OTel Collector для приёма телеметрии в Dynatrace](/managed/ingest-from/opentelemetry/collector "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
* [Пересылка данных OpenTelemetry с помощью exporter Kafka](/managed/ingest-from/opentelemetry/collector/use-cases/kafka/exporter "Как настроить OpenTelemetry Collector для пересылки данных OpenTelemetry с помощью exporter Kafka.")
* [Приём данных OpenTelemetry с помощью receiver Kafka](/managed/ingest-from/opentelemetry/collector/use-cases/kafka/receiver "Как настроить receiver Kafka в OpenTelemetry Collector для приёма OpenTelemetry из Kafka.")
* [Мониторинг Kafka с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/kafka/kafkametrics "Как настроить OpenTelemetry Collector для сбора метрик с вашего сервера Kafka.")