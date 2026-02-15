---
title: Prometheus data source
source: https://www.dynatrace.com/docs/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions
scraped: 2026-02-15T21:22:35.725727
---

# Prometheus data source

# Prometheus data source

* Latest Dynatrace
* Reference
* 2-min read
* Updated on Sep 11, 2023

Dynatrace provides you with a framework that you can use to extend your application and services observability into data acquired directly from Prometheus. The Dynatrace extensions framework can pull Prometheus metrics from the `/metrics` endpoint, a Prometheus API endpoint, or a data exporter (Prometheus target).

Note that Dynatrace provides out-of-the-box support for ingesting metrics from [Prometheus exporters in Kubernetes](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-prometheus-metrics "Metric ingestion from Prometheus endpoints in Kubernetes, metrics alerts, and monitoring consumption.").

You can run Prometheus extensions right on the Prometheus host where you installed OneAgent, so your metrics are automatically enriched with host-specific dimensions. If, however, you can't install OneAgent on the Prometheus host, you can run extensions remotely and execute them on an ActiveGate group of your choice.

We assume the following:

* You possess sufficient [Prometheusï»¿](https://prometheus.io/) subject matter expertise to create an extension.
* You're familiar with [Extensions basic concepts](/docs/ingest-from/extensions/concepts "Learn more about the concept of Dynatrace Extensions.") and the general structure of the [extension YAML file](/docs/ingest-from/extensions/develop-your-extensions/extension-yaml "Learn how to create an extension YAML file using the Extensions framework.").

Be sure to review all prerequisites and limits.

## Supported Dynatrace versions

* Dynatrace version 1.225+
* Environment ActiveGate version 1.225+
* OneAgent version 1.225+ (local extensions)

## Limits

For limits applying to your extension, see [Extensions limits](/docs/ingest-from/extensions/extension-limits "Learn about extensions limits.") and the following Prometheus-specific limits:

* Maximum 1,000 `metrics` definitions
* Maximum 50 dimensions per metric

Volatile dimensions

Note that a large number of dimensions can exceed the limits and impact your Dynatrace environment performance beyond its capacity. Consider that:

* Prometheus labels automatically become Dynatrace dimensions.
* Certain metrics can be assigned to dimensions with a constantly increasing set of values, each of them becoming a new dimension.

See [Prometheus data source reference](/docs/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions/prometheus-schema-reference "Learn about Prometheus extensions in the Extensions framework.") to learn about the structure of the Prometheus extension YAML file and monitoring configuration format.