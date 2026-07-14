---
title: Monitor Kafka with OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/kafka/kafkametrics
---

# Monitor Kafka with OTel Collector

# Monitor Kafka with OTel Collector

* How-to guide
* 3-min read
* Published Nov 26, 2025

The following configuration example shows how to configure an OTel Collector instance to scrape Kafka metrics via the `kafka_metrics` receiver component and ingest them as OTLP requests into Dynatrace.

## Prerequisites

To set up this configuration, ensure you have the following:

* One of the following Collector distributions with the [kafka\_metrics receiver﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/kafkametricsreceiver) and [cumulativetodelta processor﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/cumulativetodeltaprocessor)

  + [Dynatrace Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + [OpenTelemetry Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + [Custom Builder version](/managed/ingest-from/opentelemetry/collector#collector-builder "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
* A Kafka server deployed with a reachable `BROKER_ADDRESS`.
  For more information, see the [Kafka Apache quickstart guide﻿](https://kafka.apache.org/quickstart).
* The [Dynatrace API endpoint URL](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") to which the data should be exported.
* An [API token](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") with the relevant access scope (only required for SaaS and ActiveGate).

See [Collector Deployment](/managed/ingest-from/opentelemetry/collector/deployment "How to deploy the Dynatrace OpenTelemetry Collector.") and [Collector Configuration](/managed/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.") on how to set up your Collector with the configuration below.

## Demo configuration

```
receivers:



kafka_metrics:



brokers: ["${env:BROKER_ADDRESS}"]



scrapers:



- brokers



- topics



- consumers



processors:



cumulativetodelta:



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



metrics:



receivers: [kafka_metrics]



processors: [cumulativetodelta]



exporters: [otlp_http]
```

## Components

For our configuration, we configure the following components.

### Receivers

Under `receivers`, we specify the `kafka_metrics` receiver.
We configure it to scrape metrics from the Kafka broker specified in the `BROKER_ADDRESS` environment variable.
The receiver is set to collect metrics on brokers, topics, and consumers.

### Processors

The `cumulativetodelta` processor is required to convert cumulative metrics (as reported by Kafka) into [delta aggregation format](/managed/ingest-from/opentelemetry/collector/configuration#delta-metrics "How to configure the OpenTelemetry Collector."), for compatibility with the Dynatrace metrics ingestion API.

### Exporters

Under `exporters`, we specify the default [`otlp_http` exporter﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/exporter/otlphttpexporter) and configure it with our Dynatrace API URL and the required authentication token.

For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `Authorization`.

* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`).
* `DT_API_TOKEN` contains the [API token](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.").

### Services

Under `service`, we assemble our receiver, processor, and exporter components into a `metrics` pipeline. This pipeline:

1. Scrapes metrics from Kafka.
2. Converts cumulative metrics to delta metrics.
3. Exports the data to Dynatrace.

## Limits and limitations

### Avoid data duplication

To avoid data duplication, make sure that only one OTel Collector scrapes a given target (for example, Kafka broker or Prometheus endpoint).

If you run multiple OTel Collector replicas, configure each one with a different target. This prevents duplicate metrics and unnecessary ingest costs.

The [Target Allocator](/managed/ingest-from/opentelemetry/collector/use-cases/prometheus/standard#architecture-overview "Deploy a tiered Target Allocator, Scraper, and Gateway architecture for production-grade Prometheus scraping with the OpenTelemetry Collector.") automatically distributes the Prometheus targets among a pool of OTel Collectors.

### Use of the `cumulativetodelta` processor

Many OpenTelemetry receivers, including the `kafka_metrics` receiver, report cumulative metrics by default. Dynatrace requires delta metrics for proper visualization and analysis.

To convert cumulative metrics to delta metrics, include the `cumulativetodelta` processor in your metrics pipeline.
We recommend using this processor even if you expect some of the metrics to already have delta temporality, as those will be forwarded without any extra processing.

Statefulness

The cumulativetodelta processor calculates delta by remembering the previous value of a metric. For this reason, the calculation is only accurate if the metric is continuously sent to the same instance of the OTel Collector.
As a result, the cumulativetodelta processor may not work as expected if used in a deployment of multiple OTel Collectors. When using this processor, it's best for the data source to send data to a single OTel Collector.
If you need to scale your OTel Collectors while preserving processor state, use [stateful scaling](/managed/ingest-from/opentelemetry/collector/scaling#scaling-stateful-processing-using-non-pooled-collectors "How to scale the OpenTelemetry Collector.")

## Related topics

* [OTel Collector for ingesting telemetry into Dynatrace](/managed/ingest-from/opentelemetry/collector "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
* [Deploy the Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector/deployment "How to deploy the Dynatrace OpenTelemetry Collector.")
* [Configure the OTel Collector](/managed/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.")
* [Receive OpenTelemetry data with the Kafka receiver](/managed/ingest-from/opentelemetry/collector/use-cases/kafka/receiver "How to configure the OpenTelemetry Collector's Kafka receiver to ingest OpenTelemetry from Kafka.")
* [Forward OpenTelemetry data with the Kafka exporter](/managed/ingest-from/opentelemetry/collector/use-cases/kafka/exporter "How to configure the OpenTelemetry Collector to forward OpenTelemetry data with the Kafka exporter.")