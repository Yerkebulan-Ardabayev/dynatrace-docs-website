---
title: Scrape Prometheus metrics with the OTel Collector (simplified)
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/prometheus/simplified
---

# Scrape Prometheus metrics with the OTel Collector (simplified)

# Scrape Prometheus metrics with the OTel Collector (simplified)

* How-to guide
* 4-min read
* Updated on Jun 19, 2026

This page describes how to configure the OpenTelemetry Collector to scrape Prometheus endpoints and forward the resulting metrics to Dynatrace.
It focuses on a simplified setup where you have a static or simple set of endpoints and don't need auto-scaling or redundancy.

## When to use this approach

Use a single Collector when one or more of the following scenarios apply.

* You scrape a small or moderate number of endpoints (up to a few dozen).
* The list of targets is mostly static or driven by simple service discovery (`static_configs`, single Kubernetes namespace, file-based discovery).
* A single Collector instance has enough CPU and memory headroom for the expected load.

A single Collector eventually runs out of headroom.
If you don't yet need the standard architecture, you can run multiple independent simplified Collectors, each scraping a distinct set of targets (for example, one per namespace or team).
However you need to partition targets yourself, and there's no shared auto-scaling.

## When to move to the standard deployment

Move to the [standard deployment](/managed/ingest-from/opentelemetry/collector/use-cases/prometheus/standard "Deploy a tiered Target Allocator, Scraper, and Gateway architecture for production-grade Prometheus scraping with the OpenTelemetry Collector.") with the standard architecture using Target Allocator when you notice one or more of the following signals.

* Throughput ceiling: The Collector can't keep up with the volume of scraped data, even after you increase its CPU and memory.
* Scrape duration approaches the scrape interval: A scrape takes almost as long as the interval itself, so the Collector can't reliably finish one cycle before the next begins.
* `memory_limiter` trips or the pod is OOM-killed: The Collector repeatedly hits its memory limit and drops data or restarts.
* Target count outgrows manual partitioning: You have more targets than one Collector can handle, and splitting them across multiple independent Collectors has become a maintenance burden.
* You need auto-scaling or redundancy: A single Collector is a single point of failure and can't scale horizontally with load.

The standard deployment adds automatic target discovery through Prometheus Operator CRDs, horizontal auto-scaling, and redundancy across the scraper and gateway pools.

When you switch, you need to convert your static `scrape_configs` into `ServiceMonitor` or `PodMonitor` CRDs; see [Migrate from a single Collector](/managed/ingest-from/opentelemetry/collector/use-cases/prometheus/standard#migrate "Deploy a tiered Target Allocator, Scraper, and Gateway architecture for production-grade Prometheus scraping with the OpenTelemetry Collector.").

## Prerequisites

This use case assumes that you have:

* A Prometheus scrape target exposing port `8888`.
* One of the following Collector distributions with the [Prometheus receiver﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.155.0/receiver/prometheusreceiver), the [metric start time processor﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.155.0/processor/metricstarttimeprocessor), and the [cumulative-to-delta processor﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.155.0/processor/cumulativetodeltaprocessor):

  + The [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + OpenTelemetry [Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + A [custom Builder version](/managed/ingest-from/opentelemetry/collector#collector-builder "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
* The [Dynatrace API endpoint URL](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") to which the data should be exported.
* An [API token](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") with the relevant access scope (only required for SaaS and ActiveGate).

See [Collector Deployment](/managed/ingest-from/opentelemetry/collector/deployment "How to deploy the Dynatrace OpenTelemetry Collector.") and [Collector Configuration](/managed/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.") on how to set up your Collector with the configuration below.

## Resource sizing

For Collectors deployed as pods in Kubernetes, we recommend the following resource limits for ingesting up to 1 million data points per minute (DPM). To ingest more data, consider using the [standard deployment model](/managed/ingest-from/opentelemetry/collector/use-cases/prometheus/standard "Deploy a tiered Target Allocator, Scraper, and Gateway architecture for production-grade Prometheus scraping with the OpenTelemetry Collector.").

* CPU: 2 cores
* Memory: 8 GiB

These values assume the Collector is configured according to the [demo configuration](/managed/ingest-from/opentelemetry/collector/use-cases/prometheus/simplified#demo-configuration "Configure a single OpenTelemetry Collector to scrape Prometheus endpoints for small and medium-scale workloads."), which includes the `prometheus` receiver, `metric_start_time` and `cumulativetodelta` processors, and `otlp_http` exporter.
Additional processors will increase these requirements.

## Demo configuration

This configuration requires Dynatrace Collector v0.41.0 or later. The example pipeline below uses the [`metric_start_time` processor﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.155.0/processor/metricstarttimeprocessor), which adds start timestamps to metrics, and the [`cumulativetodelta` processor﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.155.0/processor/cumulativetodeltaprocessor), which converts the metrics to delta temporality.

```
receivers:



prometheus:



config:



scrape_configs:



- job_name: 'node-exporter'



scrape_interval: 60s



static_configs:



- targets: ['prometheus-prometheus-node-exporter:9100']



- job_name: opentelemetry-collector



scrape_interval: 60s



static_configs:



- targets:



- 127.0.0.1:8888



processors:



metric_start_time:



cumulativetodelta:



max_staleness: 25h



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



metrics:



receivers: [prometheus]



processors: [metric_start_time, cumulativetodelta]



exporters: [otlp_http]
```

Configuration validation

[Validate your settings](/managed/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector.") to avoid any configuration issues.

Cumulativetodelta processor recommendation

It is recommended to set the `max_staleness` parameter of the [cumulativetodelta processor﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.155.0/processor/cumulativetodeltaprocessor) to a value higher than how often the Collector receives metrics (e.g., how often metrics via OTLP are received, or how long the Prometheus scrape interval is). This ensures that no references to abandoned metric streams accumulate in memory over time.

## Components

For our configuration, we configure the following components.

### Receivers

Under `receivers`, we specify the `prometheus` receiver as active receiver component for our Collector instance. We configure the receiver with the two jobs `node-exporter` and `opentelemetry-collector` under `scrape_configs`, to fetch data from the specified hosts once a minute (`scrape_interval: 60s`).

For a full list of configuration parameters, see the [Prometheus documentation﻿](https://github.com/prometheus/prometheus/blob/v2.28.1/docs/configuration/configuration.md).

### Processors

Under `processors`, we specify the [`cumulativetodelta` processor﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.155.0/processor/cumulativetodeltaprocessor) to convert the metrics emitted by the Prometheus receiver to their [delta aggregation format](/managed/ingest-from/opentelemetry/collector/configuration#delta-metrics "How to configure the OpenTelemetry Collector.").

In Dynatrace Collector v0.41.0+, we specify the
[`metric_start_time`
processor﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.155.0/processor/metricstarttimeprocessor)
to add start timestamps to the metrics. This is required to properly convert the metrics to delta temporality.

### Exporters

Under `exporters`, we specify the default [`otlp_http` exporter﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.155.0/exporter/otlphttpexporter) and configure it with our Dynatrace API URL and the required authentication token.

For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `Authorization`.

* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` contains the [API token](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Service pipeline

Under `service`, we assemble our receiver, processor, and exporter objects into a metrics pipeline, which will execute the Prometheus jobs, convert their metrics to delta values, and ingest the data into Dynatrace.

## Limits and limitations

Metrics are ingested using the OpenTelemetry protocol (OTLP) via the [Dynatrace OTLP API](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") and are subject to the API's limits and restrictions.
For more information see:

* [OpenTelemetry metrics limitations](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Dynatrace metrics mapping](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")

To avoid data duplication, make sure that only one OTel Collector scrapes a given target (for example, Kafka broker or Prometheus endpoint).

If you run multiple OTel Collector replicas, configure each one with a different target. This prevents duplicate metrics and unnecessary ingest costs.

The [Target Allocator](/managed/ingest-from/opentelemetry/collector/use-cases/prometheus/standard#architecture-overview "Deploy a tiered Target Allocator, Scraper, and Gateway architecture for production-grade Prometheus scraping with the OpenTelemetry Collector.") automatically distributes the Prometheus targets among a pool of OTel Collectors.

## Related topics

* [Scrape Prometheus metrics with the OTel Collector (standard)](/managed/ingest-from/opentelemetry/collector/use-cases/prometheus/standard "Deploy a tiered Target Allocator, Scraper, and Gateway architecture for production-grade Prometheus scraping with the OpenTelemetry Collector.")
* [Enrich ingested data with Dynatrace-specific fields](/managed/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.")
* [Enrich OTLP requests with Kubernetes data](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.")
* [Prometheus data source](/managed/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions "Learn how to create a Prometheus extension using the Extensions framework.")