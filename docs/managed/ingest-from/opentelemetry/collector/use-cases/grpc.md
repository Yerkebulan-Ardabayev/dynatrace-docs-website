---
title: Transform OTLP gRPC to HTTP with the OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/grpc
scraped: 2026-05-12T12:00:57.575460
---

# Transform OTLP gRPC to HTTP with the OTel Collector

# Transform OTLP gRPC to HTTP with the OTel Collector

* How-to guide
* 1-min read
* Published Oct 11, 2023

The following configuration example shows how you would configure a Collector instance to transform a gRPC OTLP request to its HTTP counterpart.

## Prerequisites

* One of the following Collector distributions:

  + The [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + OpenTelemetry [Core](/managed/ingest-from/opentelemetry/collector#collector-core "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.") or [Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + A [custom Builder version](/managed/ingest-from/opentelemetry/collector#collector-builder "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
* The [Dynatrace API endpoint URL](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") to which the data should be exported
* An [API token](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") with the relevant access scope (only required for SaaS and ActiveGate)

See [Collector Deployment](/managed/ingest-from/opentelemetry/collector/deployment "How to deploy the Dynatrace OpenTelemetry Collector.") and [Collector Configuration](/managed/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.") on how to set up your Collector with the configuration below.

## Demo configuration

```
receivers:



otlp:



protocols:



grpc:



endpoint: 0.0.0.0:4317



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



traces:



receivers: [otlp]



processors: []



exporters: [otlp_http]



metrics:



receivers: [otlp]



processors: []



exporters: [otlp_http]



logs:



receivers: [otlp]



processors: []



exporters: [otlp_http]
```

Configuration validation

[Validate your settings](/managed/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector.") to avoid any configuration issues.

## Components

For our configuration, we configure the following components.

### Receivers

Under `receivers`, we specify the gRPC [`otlp` receiverï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/receiver/otlpreceiver) as active receiver component for our Collector instance.

### Exporters

Under `exporters`, we specify the default [`otlp_http` exporterï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/exporter/otlphttpexporter) and configure it with our Dynatrace API URL and the required authentication token.

For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `Authorization`.

* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` contains the [API token](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Service pipelines

Under `service`, we eventually assemble our receiver and exporter objects into pipelines, which explicitly accept gRPC requests and forward them on HTTP to Dynatrace.

## Limits and limitations

Data is ingested using the OpenTelemetry protocol (OTLP) via the [Dynatrace OTLP APIs](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") and is subject to the API's limits and restrictions.
For more information see:

* [OpenTelemetry metrics limitations](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Dynatrace metrics mapping](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Ingest OpenTelemetry logs](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.")

## Related topics

* [Enrich ingested data with Dynatrace-specific fields](/managed/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.")
* [Enrich OTLP requests with Kubernetes data](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.")