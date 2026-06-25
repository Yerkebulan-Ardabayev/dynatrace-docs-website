---
title: Prometheus
source: https://docs.dynatrace.com/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/prometheus
scraped: 2026-05-12T11:10:18.691860
---

# Prometheus

# Prometheus

* 1-min read
* Published Feb 01, 2022

Prometheus — это open-source инструмент мониторинга и алертинга, популярный в Kubernetes-сообществе. Prometheus собирает метрики с большого числа HTTP(s) endpoint'ов, которые отдают метрики в формате OpenMetrics.

Dynatrace предоставляет фреймворк для удобного приёма данных от Prometheus в Dynatrace в большом масштабе и в контексте всех остальных данных.

Для начала проверьте [Dynatrace Hub](https://www.dynatrace.com/hub/) — возможно, ваша технология уже покрыта существующим расширением.

Если подходящего расширения нет, Dynatrace в данный момент предлагает три подхода к получению данных Prometheus в зависимости от среды.

* Prometheus в Kubernetes
* Prometheus вне Kubernetes
* Prometheus через OpenTelemetry Collector

Dynatrace принимает метрики gauge и counter от exporter'ов и серверов Prometheus. Эти метрики становятся доступны для построения графиков, алертинга и анализа в Dynatrace. Список доступных Prometheus exporters смотрите в [документации Prometheus](https://prometheus.io/docs/instrumenting/exporters/) или в [списке, который ведёт сообщество](https://github.com/prometheus/prometheus/wiki/Default-port-allocations).

## Prometheus в Kubernetes

В Kubernetes Dynatrace поддерживает сбор данных с любого HTTP(s) endpoint, отдающего метрики в формате OpenMetrics (например, Prometheus exporters). С помощью специфичных Dynatrace-аннотаций можно указать, какие pods или services сканировать.

* Как собирать [метрики Prometheus в Kubernetes](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-prometheus-metrics "Приём метрик с Prometheus endpoints в Kubernetes, алерты и потребление мониторинга.").

## Prometheus вне Kubernetes

Dynatrace предоставляет масштабируемый способ принимать метрики Prometheus напрямую с источника, без Kubernetes. Это работает полностью автоматически и лучше всего, если OneAgent установлен на машине, где формируются метрики Prometheus, но также возможно полностью agentless, когда OneAgent установить нельзя.

* Как собирать метрики Prometheus без Kubernetes через [Extensions 2.0 Prometheus data source](/managed/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions "Создание Prometheus-расширения через фреймворк Extensions.").

## Prometheus через OpenTelemetry Collector

Для сред, где нужна большая гибкость настройки, Dynatrace позволяет принимать метрики Prometheus через OpenTelemetry Collector. Чтобы начать, смотрите [Scrape data from Prometheus](/managed/ingest-from/opentelemetry/collector/use-cases/prometheus "Настройка OpenTelemetry Collector для сбора данных Prometheus.").