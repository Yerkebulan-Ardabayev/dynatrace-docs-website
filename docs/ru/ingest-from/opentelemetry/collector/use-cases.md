---
title: OpenTelemetry Collector use cases
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/use-cases
scraped: 2026-03-06T21:32:50.601348
---

# Сценарии использования OpenTelemetry Collector

# Сценарии использования OpenTelemetry Collector

* Latest Dynatrace
* How-to guide
* 2-min read
* Updated on Mar 06, 2026

## Рекомендуемые конфигурации

При использовании Collector мы рекомендуем использовать следующие функции в базовой конфигурации, в дополнение к компонентам, специфичным для вашего сценария использования.

* [Пакетная обработка](/docs/ingest-from/opentelemetry/collector/use-cases/batch "Настройте OpenTelemetry Collector для отправки данных пакетами в бэкенд Dynatrace.") -- для улучшения сетевой производительности и пропускной способности
* [Ограничение памяти](/docs/ingest-from/opentelemetry/collector/use-cases/memory "Настройте OpenTelemetry Collector для соблюдения ограничений памяти и предотвращения чрезмерного использования системных ресурсов.") -- для предотвращения проблем, связанных с выделением памяти
* [Обогащение Kubernetes](/docs/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Настройте OpenTelemetry Collector для обогащения запросов OTLP данными Kubernetes.") -- для включения специфичной для Kubernetes информации в ваши запросы и поддержки корреляции данных в бэкенде Dynatrace

## Сценарии использования

[### Пакетная обработка

Настройте OpenTelemetry Collector для отправки данных пакетами в бэкенд Dynatrace.](/docs/ingest-from/opentelemetry/collector/use-cases/batch "Настройте OpenTelemetry Collector для отправки данных пакетами в бэкенд Dynatrace.")[### Обогащение данными OneAgent

Настройте OpenTelemetry Collector для обогащения данных с помощью OneAgent.](/docs/ingest-from/opentelemetry/collector/use-cases/enrich "Настройте OpenTelemetry Collector для обогащения запросов OTLP данными хоста OneAgent.")[![FluentD](https://dt-cdn.net/images/untitled-300-c72685245e.png "FluentD")

### FluentD

Настройте OpenTelemetry Collector для приёма данных из FluentD.](/docs/ingest-from/opentelemetry/collector/use-cases/fluentd "Настройте OpenTelemetry Collector для приёма данных FluentD.")[### gRPC в HTTP

Настройте OpenTelemetry Collector для преобразования gRPC OTLP-запроса в HTTP.](/docs/ingest-from/opentelemetry/collector/use-cases/grpc "Настройте OpenTelemetry Collector для преобразования gRPC OTLP-запроса в HTTP.")[### Сводки гистограмм

Настройте OpenTelemetry Collector для вычисления сводок по бакетам метрик гистограмм.](/docs/ingest-from/opentelemetry/collector/use-cases/histograms "Настройте OpenTelemetry Collector для вычисления сводок гистограмм.")[![Infrastructure observability](https://cdn.bfldr.com/B686QPH3/at/5kh38tq37h2w4qtnmbp5m889/DT0434.svg?auto=webp&width=72&height=72 "Infrastructure observability")

### Расширение Host Monitoring

Мониторинг хостов, отправляющих данные OpenTelemetry в Dynatrace.](/docs/ingest-from/opentelemetry/collector/use-cases/host-monitoring "Как мониторить ваши хосты, использующие Collector для отправки данных OpenTelemetry в Dynatrace.")[![Jaeger](https://dt-cdn.net/images/jaeger-300-3d21c8cbd4-300-2d7104a994.png "Jaeger")

### Jaeger

Настройте OpenTelemetry Collector для приёма и преобразования данных Jaeger в Dynatrace.](/docs/ingest-from/opentelemetry/collector/use-cases/jaeger "Настройте OpenTelemetry Collector для приёма и преобразования данных Jaeger в Dynatrace.")[### Kafka

Настройте OpenTelemetry Collector для интеграции с Apache Kafka.](/docs/ingest-from/opentelemetry/collector/use-cases/kafka "Как настроить OpenTelemetry Collector для буферизации данных через Kafka.")[### Обогащение Kubernetes

Настройте OpenTelemetry Collector для обогащения запросов OTLP данными Kubernetes.](/docs/ingest-from/opentelemetry/collector/use-cases/kubernetes "Настройте OpenTelemetry Collector для приёма данных Kubernetes в Dynatrace.")[### Файлы логов

Настройте OpenTelemetry Collector для приёма файлов логов.](/docs/ingest-from/opentelemetry/collector/use-cases/filelog "Настройте OpenTelemetry Collector для приёма данных логов в Dynatrace.")[### Маскирование конфиденциальных данных

Настройте OpenTelemetry Collector для маскирования конфиденциальных данных перед пересылкой в Dynatrace.](/docs/ingest-from/opentelemetry/collector/use-cases/redact "Настройте OpenTelemetry Collector для маскирования конфиденциальных данных перед пересылкой в Dynatrace.")[### Ограничение памяти

Настройте OpenTelemetry Collector для соблюдения ограничений памяти и предотвращения чрезмерного использования системных ресурсов.](/docs/ingest-from/opentelemetry/collector/use-cases/memory "Настройте OpenTelemetry Collector для соблюдения ограничений памяти и предотвращения чрезмерного использования системных ресурсов.")[### Несколько бэкендов

Настройте OpenTelemetry Collector для экспорта в несколько бэкендов.](/docs/ingest-from/opentelemetry/collector/use-cases/multi-export "Настройте OpenTelemetry Collector для отправки данных более чем в один бэкенд.")[### NetFlow

Настройте OpenTelemetry Collector для приёма пакетов NetFlow.](/docs/ingest-from/opentelemetry/collector/use-cases/netflow "Настройте OpenTelemetry Collector для приёма данных NetFlow.")[![Prometheus](https://dt-cdn.net/images/prometheus-logo-grey-e85840f462-8e7b2967a6.svg "Prometheus")

### Prometheus

Настройте OpenTelemetry Collector для сбора ваших данных Prometheus.](/docs/ingest-from/opentelemetry/collector/use-cases/prometheus "Настройте OpenTelemetry Collector для сбора ваших данных Prometheus.")[### Сэмплирование

Настройте OpenTelemetry Collector для сэмплирования распределённых трассировок.](/docs/ingest-from/opentelemetry/collector/use-cases/sampling "Настройте OpenTelemetry Collector для сэмплирования данных с использованием процессора `tail_sampling`.")[### StatsD

Настройте OpenTelemetry Collector для приёма данных StatsD.](/docs/ingest-from/opentelemetry/collector/use-cases/statsd "Настройте OpenTelemetry Collector для приёма данных StatsD.")[### Syslog

Настройте OpenTelemetry Collector для приёма данных syslog.](/docs/ingest-from/opentelemetry/collector/use-cases/syslog "Настройте OpenTelemetry Collector для приёма данных syslog в Dynatrace.")[### Преобразование и фильтрация

Настройте OpenTelemetry Collector для добавления, преобразования и удаления данных OpenTelemetry.](/docs/ingest-from/opentelemetry/collector/use-cases/transform "Настройте OpenTelemetry Collector для добавления, преобразования и удаления данных OpenTelemetry.")[![Zipkin](https://dt-cdn.net/images/zipkin-gray-300-7e572e6589.png "Zipkin")

### Zipkin

Настройте OpenTelemetry Collector для приёма и преобразования данных Zipkin в Dynatrace.](/docs/ingest-from/opentelemetry/collector/use-cases/zipkin "Настройте OpenTelemetry Collector для приёма и преобразования данных Zipkin в Dynatrace.")
