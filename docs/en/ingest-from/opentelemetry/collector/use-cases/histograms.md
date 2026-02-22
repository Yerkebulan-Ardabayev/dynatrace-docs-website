---
title: Compute histogram summaries with the OpenTelemetry Collector
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/use-cases/histograms
scraped: 2026-02-22T21:22:38.846443
---

# Compute histogram summaries with the OpenTelemetry Collector

# Compute histogram summaries with the OpenTelemetry Collector

* Latest Dynatrace
* How-to guide
* 3-min read
* Published Apr 08, 2024

Ingest histograms directly

Starting with Dynatrace version 1.300, histogram ingestion is supported directly via OTLP ingest API. Consequently, it's not required to use Collector as a workaround. Dynatrace recommends ingesting histograms directly without additional data manipulation.

The following configuration example shows how to use the Collector to compute and ingest summaries of histogram buckets, such as the overall sum of all values in the bucket and their total count.

## Prerequisites

* One of the following Collector distributions with the [transformï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/transformprocessor) and [filterï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/filterprocessor) processors:

  + The [Dynatrace Collector](/docs/ingest-from/opentelemetry/collector#dt-collector-dist "Learn about the Dynatrace OTel Collector.")
  + OpenTelemetry [Contrib](/docs/ingest-from/opentelemetry/collector#collector-contrib "Learn about the Dynatrace OTel Collector.")
  + A [custom Builder version](/docs/ingest-from/opentelemetry/collector#collector-builder "Learn about the Dynatrace OTel Collector.")
* The [Dynatrace API endpoint URL](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") to which the data should be exported
* An [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") with the relevant access scope (only required for SaaS and ActiveGate)

See [Collector Deployment](/docs/ingest-from/opentelemetry/collector/deployment "How to deploy Dynatrace OTel Collector.") and [Collector Configuration](/docs/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.") on how to set up your Collector with the configuration below.

## Demo configuration

```
receivers:



otlp:



protocols:



grpc:



endpoint: 0.0.0.0:4317



http:



endpoint: 0.0.0.0:4318



processors:



transform:



metric_statements:



- context: metric



statements:



# Get count from the histogram. The new metric name will be <histogram_name>_count



- extract_count_metric(true) where type == METRIC_DATA_TYPE_HISTOGRAM



# Get sum from the histogram. The new metric name will be <histogram_name>_sum



- extract_sum_metric(true) where type == METRIC_DATA_TYPE_HISTOGRAM



# convert the <histogram_name>_sum metrics to gauges.



- convert_sum_to_gauge() where IsMatch(name, ".*_sum")



filter:



metrics:



metric:



# Drop metrics of type histogram. The _count and _sum metrics will still be exported.



- type == METRIC_DATA_TYPE_HISTOGRAM



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



metrics:



receivers: [otlp]



processors: [transform,filter]



exporters: [otlp_http]
```

Configuration validation

[Validate your settings](/docs/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector.") to avoid any configuration issues.

## Components

For our configuration, we configure the following components.

### Receivers

Under `receivers`, we specify the standard `otlp` receiver as active receiver component for our Collector instance and configure it to accept OTLP requests on gRPC and HTTP.

### Processors

Under `processors`, we configure the following two processor instances:

* [`transform`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/transformprocessor), to compute the desired sum and count values of the histograms:

  + We first use the function [`extract_count_metric`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/processor/transformprocessor/README.md#extract_count_metric) to compute the number of values in each histogram bucket.
  + Then, we use the function [`extract_sum_metric`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/processor/transformprocessor/README.md#extract_sum_metric) to compute the total sum of all of its values and convert it to a gauge using [`convert_sum_to_gauge`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/processor/transformprocessor/README.md#convert_sum_to_gauge).
* [`filter`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/filterprocessor), to drop the existing histogram buckets (based on `type`) and avoid histogram-related error messages.

With this configuration, the Collector drops histogram metrics and creates in their place two new metrics for the sum and item count of each respective histogram.

### Exporters

Under `exporters`, we specify the default [`otlp_http` exporterï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/exporter/otlphttpexporter) and configure it with our Dynatrace API URL and the required authentication token.

For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `Authorization`:

* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` contains the [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Service pipelines

Under `service`, we assemble our receiver and exporter objects into a metric pipeline and enable the two processors by referencing them under `processors`.

## Limits and limitations

Metrics are ingested using the OpenTelemetry protocol (OTLP) via the [Dynatrace OTLP API](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") and are subject to the API's limits and restrictions.
For more information see:

* [OpenTelemetry metrics limitations](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Dynatrace metrics mapping](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")

## Related topics

* [Enrich ingested data with Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.")