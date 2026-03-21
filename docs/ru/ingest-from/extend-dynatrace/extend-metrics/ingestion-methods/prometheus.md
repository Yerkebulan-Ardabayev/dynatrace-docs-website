---
title: Prometheus
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/prometheus
scraped: 2026-03-06T21:16:30.428379
---

* Latest Dynatrace
* 1-min read

Prometheus — это набор инструментов с открытым исходным кодом для мониторинга и оповещения, широко используемый в сообществе Kubernetes. Prometheus собирает метрики из ряда конечных точек HTTP(s), предоставляющих метрики в формате OpenMetrics.

Dynatrace предоставляет вам фреймворк для удобного приёма данных от Prometheus в Dynatrace в масштабе и в контексте всех остальных данных.

Для начала работы проверьте [Dynatrace Hub](https://www.dynatrace.com/hub/), чтобы узнать, охвачена ли ваша технология существующим расширением.

Если расширение, отвечающее вашим потребностям, отсутствует, Dynatrace в настоящее время предлагает три подхода к получению данных Prometheus в зависимости от среды.

* Prometheus в Kubernetes
* Prometheus вне Kubernetes
* Prometheus через OpenTelemetry Collector

Dynatrace интегрирует метрики gauge и counter из экспортёров и серверов Prometheus. Эти метрики затем доступны для построения графиков, оповещения и анализа в Dynatrace. Список доступных экспортёров Prometheus см. в [документации Prometheus](https://prometheus.io/docs/instrumenting/exporters/) или в [списке, поддерживаемом сообществом](https://github.com/prometheus/prometheus/wiki/Default-port-allocations).

## Prometheus в Kubernetes

В Kubernetes Dynatrace поддерживает сбор данных с любых конечных точек HTTP(s), предоставляющих метрики в формате OpenMetrics (например, экспортёры Prometheus). С помощью специальных аннотаций Dynatrace вы можете указать, с каких подов или сервисов выполнять сбор данных.

* Узнайте, как собирать [метрики Prometheus в Kubernetes](../../../../observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-prometheus-metrics.md "Metric ingestion from Prometheus endpoints in Kubernetes, metrics alerts, and monitoring consumption.").

## Prometheus вне Kubernetes

Dynatrace предоставляет масштабируемый способ приёма метрик Prometheus непосредственно из источника без Kubernetes. Это работает полностью автоматически и наиболее эффективно, если OneAgent установлен на хосте, где генерируются метрики Prometheus, но также может быть реализовано полностью без агента, если установить OneAgent на хосте невозможно.

* Узнайте, как собирать метрики Prometheus без Kubernetes с помощью [источника данных Prometheus для Extensions 2.0](../../../extensions/develop-your-extensions/data-sources/prometheus-extensions.md "Learn how to create a Prometheus extension using the Extensions framework.").

## Prometheus через OpenTelemetry Collector

Для сред, требующих большей гибкости настройки, Dynatrace позволяет принимать метрики Prometheus с помощью OpenTelemetry Collector. Для начала работы см. [Сбор данных из Prometheus](../../../opentelemetry/collector/use-cases/prometheus.md "Configure the OpenTelemetry Collector to scrape your Prometheus data.").
