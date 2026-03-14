---
title: Варианты использования OpenTelemetry Collector
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/use-cases
scraped: 2026-03-06T21:32:50.601348
---

# Сценарии использования OpenTelemetry Collector


* Latest Dynatrace
* How-to guide
* 2-min read
* Updated on Mar 06, 2026

## Рекомендуемые конфигурации

При использовании Collector мы рекомендуем использовать следующие функции в базовой конфигурации, в дополнение к компонентам, специфичным для вашего сценария использования.

* [Пакетная обработка](use-cases/batch.md "Настройте OpenTelemetry Collector для отправки данных пакетами в бэкенд Dynatrace.") -- для улучшения сетевой производительности и пропускной способности
* [Ограничение памяти](use-cases/memory.md "Настройте OpenTelemetry Collector для соблюдения ограничений памяти и предотвращения чрезмерного использования системных ресурсов.") -- для предотвращения проблем, связанных с выделением памяти
* [Обогащение Kubernetes](use-cases/kubernetes/k8s-enrich.md "Настройте OpenTelemetry Collector для обогащения запросов OTLP данными Kubernetes.") -- для включения специфичной для Kubernetes информации в ваши запросы и поддержки корреляции данных в бэкенде Dynatrace

## Сценарии использования

[### Пакетная обработка

Настройте OpenTelemetry Collector для отправки данных пакетами в бэкенд Dynatrace.](use-cases/batch.md "Настройте OpenTelemetry Collector для отправки данных пакетами в бэкенд Dynatrace.")[### Обогащение данными OneAgent

Настройте OpenTelemetry Collector для обогащения данных с помощью OneAgent.](use-cases/enrich.md "Настройте OpenTelemetry Collector для обогащения запросов OTLP данными хоста OneAgent.")[![FluentD](https://dt-cdn.net/images/untitled-300-c72685245e.png "FluentD")

### FluentD

Настройте OpenTelemetry Collector для приёма данных из FluentD.](use-cases/fluentd.md "Настройте OpenTelemetry Collector для приёма данных FluentD.")[### gRPC в HTTP

Настройте OpenTelemetry Collector для преобразования gRPC OTLP-запроса в HTTP.](use-cases/grpc.md "Настройте OpenTelemetry Collector для преобразования gRPC OTLP-запроса в HTTP.")[### Сводки гистограмм

Настройте OpenTelemetry Collector для вычисления сводок по бакетам метрик гистограмм.](use-cases/histograms.md "Настройте OpenTelemetry Collector для вычисления сводок гистограмм.")[![Infrastructure observability](https://cdn.bfldr.com/B686QPH3/at/5kh38tq37h2w4qtnmbp5m889/DT0434.svg?auto=webp&width=72&height=72 "Infrastructure observability")

### Расширение Host Monitoring

Мониторинг хостов, отправляющих данные OpenTelemetry в Dynatrace.](use-cases/host-monitoring.md "Как мониторить ваши хосты, использующие Collector для отправки данных OpenTelemetry в Dynatrace.")[![Jaeger](https://dt-cdn.net/images/jaeger-300-3d21c8cbd4-300-2d7104a994.png "Jaeger")

### Jaeger

Настройте OpenTelemetry Collector для приёма и преобразования данных Jaeger в Dynatrace.](use-cases/jaeger.md "Настройте OpenTelemetry Collector для приёма и преобразования данных Jaeger в Dynatrace.")[### Kafka

Настройте OpenTelemetry Collector для интеграции с Apache Kafka.](use-cases/kafka.md "Как настроить OpenTelemetry Collector для буферизации данных через Kafka.")[### Обогащение Kubernetes

Настройте OpenTelemetry Collector для обогащения запросов OTLP данными Kubernetes.](use-cases/kubernetes.md "Настройте OpenTelemetry Collector для приёма данных Kubernetes в Dynatrace.")[### Файлы логов

Настройте OpenTelemetry Collector для приёма файлов логов.](use-cases/filelog.md "Настройте OpenTelemetry Collector для приёма данных логов в Dynatrace.")[### Маскирование конфиденциальных данных

Настройте OpenTelemetry Collector для маскирования конфиденциальных данных перед пересылкой в Dynatrace.](use-cases/redact.md "Настройте OpenTelemetry Collector для маскирования конфиденциальных данных перед пересылкой в Dynatrace.")[### Ограничение памяти

Настройте OpenTelemetry Collector для соблюдения ограничений памяти и предотвращения чрезмерного использования системных ресурсов.](use-cases/memory.md "Настройте OpenTelemetry Collector для соблюдения ограничений памяти и предотвращения чрезмерного использования системных ресурсов.")[### Несколько бэкендов

Настройте OpenTelemetry Collector для экспорта в несколько бэкендов.](use-cases/multi-export.md "Настройте OpenTelemetry Collector для отправки данных более чем в один бэкенд.")[### NetFlow

Настройте OpenTelemetry Collector для приёма пакетов NetFlow.](use-cases/netflow.md "Настройте OpenTelemetry Collector для приёма данных NetFlow.")[![Prometheus](https://dt-cdn.net/images/prometheus-logo-grey-e85840f462-8e7b2967a6.svg "Prometheus")

### Prometheus

Настройте OpenTelemetry Collector для сбора ваших данных Prometheus.](use-cases/prometheus.md "Настройте OpenTelemetry Collector для сбора ваших данных Prometheus.")[### Сэмплирование

Настройте OpenTelemetry Collector для сэмплирования распределённых трассировок.](use-cases/sampling.md "Настройте OpenTelemetry Collector для сэмплирования данных с использованием процессора `tail_sampling`.")[### StatsD

Настройте OpenTelemetry Collector для приёма данных StatsD.](use-cases/statsd.md "Настройте OpenTelemetry Collector для приёма данных StatsD.")[### Syslog

Настройте OpenTelemetry Collector для приёма данных syslog.](use-cases/syslog.md "Настройте OpenTelemetry Collector для приёма данных syslog в Dynatrace.")[### Преобразование и фильтрация

Настройте OpenTelemetry Collector для добавления, преобразования и удаления данных OpenTelemetry.](use-cases/transform.md "Настройте OpenTelemetry Collector для добавления, преобразования и удаления данных OpenTelemetry.")[![Zipkin](https://dt-cdn.net/images/zipkin-gray-300-7e572e6589.png "Zipkin")

### Zipkin

Настройте OpenTelemetry Collector для приёма и преобразования данных Zipkin в Dynatrace.](use-cases/zipkin.md "Настройте OpenTelemetry Collector для приёма и преобразования данных Zipkin в Dynatrace.")
