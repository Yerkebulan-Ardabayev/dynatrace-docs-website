---
title: Сценарии использования OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases
scraped: 2026-05-12T12:00:53.786681
---

# Сценарии использования OTel Collector

# Сценарии использования OTel Collector

* Практическое руководство
* Чтение: 2 мин
* Обновлено 12 марта 2026 г.

## Рекомендуемые конфигурации

При использовании OTel Collector мы рекомендуем применять в базовой конфигурации следующие функции в дополнение к компонентам, специфичным для вашего сценария использования.

* [Группирование](/managed/ingest-from/opentelemetry/collector/use-cases/batch "Настройте OpenTelemetry Collector для отправки данных группами в бэкенд Dynatrace.") для повышения производительности и пропускной способности сети
* [Ограничение памяти](/managed/ingest-from/opentelemetry/collector/use-cases/memory "Настройте OpenTelemetry Collector для соблюдения ограничений памяти и предотвращения чрезмерного использования системных ресурсов.") во избежание проблем, связанных с выделением памяти
* [Обогащение данными Kubernetes](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Настройте OpenTelemetry Collector для обогащения запросов OTLP данными Kubernetes.") для включения специфичной для Kubernetes информации в ваши запросы и поддержки корреляции данных в бэкенде Dynatrace

## Сценарии использования

[### Группирование

Настройте Collector для отправки данных группами в бэкенд Dynatrace.](/managed/ingest-from/opentelemetry/collector/use-cases/batch "Настройте OpenTelemetry Collector для отправки данных группами в бэкенд Dynatrace.")[### Обогащение с помощью OneAgent

Настройте Collector для обогащения данных с помощью OneAgent.](/managed/ingest-from/opentelemetry/collector/use-cases/enrich "Настройте OpenTelemetry Collector для обогащения запросов OTLP данными хоста OneAgent.")[![FluentD](https://dt-cdn.net/images/untitled-300-c72685245e.png "FluentD")

### FluentD

Настройте Collector для приёма данных из FluentD.](/managed/ingest-from/opentelemetry/collector/use-cases/fluentd "Настройте OpenTelemetry Collector для приёма данных FluentD.")[### gRPC в HTTP

Настройте Collector для преобразования запроса gRPC OTLP в HTTP.](/managed/ingest-from/opentelemetry/collector/use-cases/grpc "Настройте OpenTelemetry Collector для преобразования запроса gRPC OTLP в HTTP.")[### Сводки гистограмм

Настройте Collector для вычисления сводок по интервалам для метрик-гистограмм.](/managed/ingest-from/opentelemetry/collector/use-cases/histograms "Настройте OpenTelemetry Collector для вычисления сводок гистограмм.")[![Infrastructure observability](https://cdn.bfldr.com/B686QPH3/at/5kh38tq37h2w4qtnmbp5m889/DT0434.svg?auto=webp&width=72&height=72 "Infrastructure observability")

### Мониторинг хостов

Отслеживайте ваши хосты, которые отправляют данные OpenTelemetry в Dynatrace.](/managed/ingest-from/opentelemetry/collector/use-cases/host-monitoring "Как отслеживать ваши хосты, которые используют Collector для отправки данных OpenTelemetry в Dynatrace.")[![Jaeger](https://dt-cdn.net/images/jaeger-300-3d21c8cbd4-300-2d7104a994.png "Jaeger")

### Jaeger

Настройте Collector для приёма и преобразования данных Jaeger в Dynatrace.](/managed/ingest-from/opentelemetry/collector/use-cases/jaeger "Настройте OpenTelemetry Collector для приёма и преобразования данных Jaeger в Dynatrace.")[![Infrastructure observability](https://cdn.bfldr.com/B686QPH3/at/5kh38tq37h2w4qtnmbp5m889/DT0434.svg?auto=webp&width=72&height=72 "Infrastructure observability")

### Journald

Настройте Collector для приёма логов журнала systemd в Dynatrace.](/managed/ingest-from/opentelemetry/collector/use-cases/journald "Настройте OpenTelemetry Collector для приёма логов журнала systemd с хостов Linux в Dynatrace.")[### Kafka

Настройте Collector для интеграции с Apache Kafka.](/managed/ingest-from/opentelemetry/collector/use-cases/kafka "Как настроить OpenTelemetry Collector для буферизации данных через Kafka.")[### Kubernetes

Настройте Collector для обогащения запросов OTLP данными Kubernetes, мониторинга кластеров или приёма логов подов.](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes "Настройте OpenTelemetry Collector для приёма данных Kubernetes в Dynatrace.")[### Файлы логов

Настройте Collector для приёма файлов логов.](/managed/ingest-from/opentelemetry/collector/use-cases/filelog "Настройте OpenTelemetry Collector для приёма данных логов в Dynatrace.")[### Маскирование конфиденциальных данных

Настройте Collector для маскирования конфиденциальных данных перед пересылкой в Dynatrace.](/managed/ingest-from/opentelemetry/collector/use-cases/redact "Настройте OpenTelemetry Collector для маскирования конфиденциальных данных перед пересылкой в Dynatrace.")[### Ограничения памяти

Настройте Collector для соблюдения ограничений памяти и предотвращения чрезмерного использования системных ресурсов.](/managed/ingest-from/opentelemetry/collector/use-cases/memory "Настройте OpenTelemetry Collector для соблюдения ограничений памяти и предотвращения чрезмерного использования системных ресурсов.")[### Несколько бэкендов

Настройте Collector для экспорта в несколько бэкендов.](/managed/ingest-from/opentelemetry/collector/use-cases/multi-export "Настройте OpenTelemetry Collector для отправки данных более чем в один бэкенд.")[### NetFlow

Настройте Collector для приёма пакетов NetFlow.](/managed/ingest-from/opentelemetry/collector/use-cases/netflow "Настройте OpenTelemetry Collector для приёма данных NetFlow.")[![Prometheus](https://dt-cdn.net/images/prometheus-logo-grey-e85840f462-8e7b2967a6.svg "Prometheus")

### Prometheus

Настройте Collector для сбора ваших данных Prometheus.](/managed/ingest-from/opentelemetry/collector/use-cases/prometheus "Настройте OpenTelemetry Collector для сбора ваших данных Prometheus.")[### Сэмплирование

Настройте Collector для сэмплирования распределённых трассировок.](/managed/ingest-from/opentelemetry/collector/use-cases/sampling "Настройте OpenTelemetry Collector для сэмплирования данных с помощью processor `tail_sampling`.")[### StatsD

Настройте Collector для приёма данных StatsD.](/managed/ingest-from/opentelemetry/collector/use-cases/statsd "Настройте OpenTelemetry Collector для приёма данных StatsD.")[### Syslog

Настройте Collector для приёма данных syslog.](/managed/ingest-from/opentelemetry/collector/use-cases/syslog "Настройте OpenTelemetry Collector для приёма данных syslog в Dynatrace.")[### Преобразование и фильтрация

Настройте Collector для добавления, преобразования и отбрасывания данных OpenTelemetry.](/managed/ingest-from/opentelemetry/collector/use-cases/transform "Настройте OpenTelemetry Collector для добавления, преобразования и отбрасывания данных OpenTelemetry.")[![Zipkin](https://dt-cdn.net/images/zipkin-gray-300-7e572e6589.png "Zipkin")

### Zipkin

Настройте Collector для приёма и преобразования данных Zipkin в Dynatrace.](/managed/ingest-from/opentelemetry/collector/use-cases/zipkin "Настройте OpenTelemetry Collector для приёма и преобразования данных Zipkin в Dynatrace.")