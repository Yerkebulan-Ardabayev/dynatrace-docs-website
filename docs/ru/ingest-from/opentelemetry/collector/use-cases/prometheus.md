---
title: Scrape Promethus metrics with the OpenTelemetry Collector
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/use-cases/prometheus
scraped: 2026-03-01T21:20:55.520832
---

# Scrape Promethus metrics with the OpenTelemetry Collector

# Scrape Promethus metrics with the OpenTelemetry Collector

* Latest Dynatrace
* How-to guide
* 2-min read
* Updated on Dec 09, 2025

The following configuration example shows how you configure a Collector instance to scrape data from an existing Prometheus setup and import it as OTLP request into Dynatrace.

## Prerequisites

* A Prometheus instance running on port 8888
* One of the following Collector distributions with the [Prometheus receiverï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/receiver/prometheusreceiver), the [metric start time processorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/metricstarttimeprocessor), and the [cumulative-to-delta processorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/cumulativetodeltaprocessor):

  + The [Dynatrace Collector](/docs/ingest-from/opentelemetry/collector#dt-collector-dist "Learn about the Dynatrace OTel Collector.")
  + OpenTelemetry [Contrib](/docs/ingest-from/opentelemetry/collector#collector-contrib "Learn about the Dynatrace OTel Collector.")
  + A [custom Builder version](/docs/ingest-from/opentelemetry/collector#collector-builder "Learn about the Dynatrace OTel Collector.")
* The [Dynatrace API endpoint URL](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") to which the data should be exported
* An [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") with the relevant access scope (only required for SaaS and ActiveGate)

See [Collector Deployment](/docs/ingest-from/opentelemetry/collector/deployment "How to deploy Dynatrace OTel Collector.") and [Collector Configuration](/docs/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.") on how to set up your Collector with the configuration below.

## Demo configuration

Dynatrace Collector v0.41.0+

The example pipeline below uses the [`metricstarttime` processorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/metricstarttimeprocessor), which is required to convert the metrics to delta temporality.

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



metricstarttime:



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



processors: [metricstarttime, cumulativetodelta]



exporters: [otlp_http]
```

Dynatrace Collector v0.40.0 or earlier

In **v0.40.0** of the Dynatrace Collector, you must run the Collector
with the following flag in order to keep adjusting start times in the
Prometheus receiver:

```
--feature-gates=-receiver.prometheusreceiver.RemoveStartTimeAdjustment
```

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



processors: [cumulativetodelta]



exporters: [otlp_http]
```

Configuration validation

[Validate your settings](/docs/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector.") to avoid any configuration issues.

Cumulativetodelta processor recommendation

It is recommended to set the `max_staleness` parameter of the [cumulativetodelta processorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/cumulativetodeltaprocessor) to a value higher than how often the collector receives metrics (e.g., how often metrics via OTLP are received, or how long the Prometheus scrape interval is). This ensures that no references to abandoned metric streams accumulate in memory over time.

## Components

For our configuration, we configure the following components.

### Receivers

Under `receivers`, we specify the `prometheus` receiver as active receiver component for our Collector instance. We configure the receiver with the two jobs `node-exporter` and `opentelemetry-collector` under `scrape_configs`, to fetch data from the specified hosts once a minute (`scrape_interval: 60s`).

For a full list of configuration parameters, see the [Prometheus documentationï»¿](https://github.com/prometheus/prometheus/blob/v2.28.1/docs/configuration/configuration.md).

### Processors

Under `processors`, we specify the [`cumulativetodelta` processorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/cumulativetodeltaprocessor) to convert the metrics emitted by the Prometheus receiver to their [delta aggregation format](/docs/ingest-from/opentelemetry/collector/configuration#delta-metrics "How to configure the OpenTelemetry Collector.").

In Dynatrace Collector v0.41.0+, we specify the
[`metricstarttime`
processorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/metricstarttimeprocessor)
to add start timestamps to the metrics. This is required to properly convert the metrics to delta temporality.

### Exporters

Under `exporters`, we specify the default [`otlp_http` exporterï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/exporter/otlphttpexporter) and configure it with our Dynatrace API URL and the required authentication token.

For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `Authorization`.

* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` contains the [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Service pipeline

Under `service`, we assemble our receiver, processor, and exporter objects into a metrics pipeline, which will execute the Prometheus jobs, convert their metrics to delta values, and ingest the data into Dynatrace.

## Limits and limitations

Metrics are ingested using the OpenTelemetry protocol (OTLP) via the [Dynatrace OTLP API](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") and are subject to the API's limits and restrictions.
For more information see:

* [OpenTelemetry metrics limitations](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Dynatrace metrics mapping](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")

To avoid data duplication, make sure that only one OpenTelemetry Collector scrapes a given target (for example, Kafka broker or Prometheus endpoint).

If you run multiple collector replicas, configure each one with a different target. This prevents duplicate metrics and unnecessary ingest costs.

The [Target Allocatorï»¿](https://opentelemetry.io/docs/platforms/kubernetes/operator/target-allocator/) automatically distributes the Prometheus targets among a pool of Collectors.

## Related topics

* [Enrich ingested data with Dynatrace-specific fields](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.")
* [Enrich OTLP requests with Kubernetes data](/docs/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.")