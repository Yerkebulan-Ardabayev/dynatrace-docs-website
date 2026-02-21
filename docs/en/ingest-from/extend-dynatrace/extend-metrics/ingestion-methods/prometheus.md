---
title: Prometheus
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/prometheus
scraped: 2026-02-21T21:15:56.650501
---

# Prometheus

# Prometheus

* Latest Dynatrace
* 1-min read
* Published Feb 01, 2022

Prometheus is an open-source monitoring and alerting toolkit that is popular in the Kubernetes community. Prometheus scrapes metrics from a number of HTTP(s) endpoints that expose metrics in the OpenMetrics format.

Dynatrace provides you with a framework to easily ingest data provided by Prometheus into Dynatrace at scale and in the context to all other data.

To get started, check [Dynatrace Hubï»¿](https://www.dynatrace.com/hub/) to see if your technology is already covered by an existing extension.

If there's no extension covering your needs, Dynatrace currently provides three approaches to acquiring Prometheus data, depending on the environment.

* Prometheus in Kubernetes
* Prometheus outside of Kubernetes
* Prometheus via OpenTelemetry Collector

Dynatrace integrates gauge and counter metrics from Prometheus exporters and servers. These metrics are then available for charting, alerting, and analysis within Dynatrace. See the list of available Prometheus exporters in the [Prometheus documentationï»¿](https://prometheus.io/docs/instrumenting/exporters/) or in the [list maintained by the communityï»¿](https://github.com/prometheus/prometheus/wiki/Default-port-allocations).

## Prometheus in Kubernetes

In Kubernetes, Dynatrace supports scraping of any HTTP(s) endpoint offering metrics in OpenMetrics format (for example, Prometheus exporters). Using Dynatrace-specific annotations, you can specify which pods or services to scrape.

* Learn how to collect [Prometheus metrics in Kubernetes](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-prometheus-metrics "Metric ingestion from Prometheus endpoints in Kubernetes, metrics alerts, and monitoring consumption.").

## Prometheus outside of Kubernetes

Dynatrace provides a scalable means to ingest Prometheus metrics directly from the source, without Kubernetes. This works fully automatically and works best if OneAgent is installed on the box where the Prometheus metrics originate, but it can also be done in a fully agentless manner when OneAgent can't be installed on the box.

* Learn how to collect Prometheus metrics without Kubernetes using [Extensions 2.0 Prometheus data source](/docs/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions "Learn how to create a Prometheus extension using the Extensions framework.").

## Prometheus via OpenTelemetry Collector

For environments that require greater customization, Dynatrace allows the ingestion of Prometheus metrics using the OpenTelemetry Collector. To get started, see [Scrape data from Prometheus](/docs/ingest-from/opentelemetry/collector/use-cases/prometheus "Configure the OpenTelemetry Collector to scrape your Prometheus data.").