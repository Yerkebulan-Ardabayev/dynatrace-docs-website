---
title: Transform OTLP gRPC to HTTP with the OpenTelemetry Collector
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/use-cases/grpc
scraped: 2026-03-03T21:32:35.758185
---

# Transform OTLP gRPC to HTTP with the OpenTelemetry Collector


* Latest Dynatrace
* How-to guide
* 1-min read
* Published Oct 11, 2023

The following configuration example shows how you would configure a Collector instance to transform a gRPC OTLP request to its HTTP counterpart.

## Prerequisites

* One of the following Collector distributions:

  + The [Dynatrace Collector](../../collector.md#dt-collector-dist "Learn about the Dynatrace OTel Collector.")
  + OpenTelemetry [Core](../../collector.md#collector-core "Learn about the Dynatrace OTel Collector.") or [Contrib](../../collector.md#collector-contrib "Learn about the Dynatrace OTel Collector.")
  + A [custom Builder version](../../collector.md#collector-builder "Learn about the Dynatrace OTel Collector.")
* The Dynatrace API endpoint URL to which the data should be exported
* An [API token](../../otlp-api.md#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") with the relevant access scope (only required for SaaS and ActiveGate)

See Collector Deployment and Collector Configuration on how to set up your Collector with the configuration below.

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

[Validate your settings](../configuration.md#validate "How to configure the OpenTelemetry Collector.") to avoid any configuration issues.

## Components

For our configuration, we configure the following components.

### Receivers

Under `receivers`, we specify the gRPC [`otlp` receiverï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/receiver/otlpreceiver) as active receiver component for our Collector instance.

### Exporters

Under `exporters`, we specify the default [`otlp_http` exporterï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/exporter/otlphttpexporter) and configure it with our Dynatrace API URL and the required authentication token.

For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `Authorization`.

* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](../../otlp-api.md#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` contains the [API token](../../otlp-api.md#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Service pipelines

Under `service`, we eventually assemble our receiver and exporter objects into pipelines, which explictly accept gRPC requests and forward them on HTTP to Dynatrace.

## Limits and limitations

Data is ingested using the OpenTelemetry protocol (OTLP) via the Dynatrace OTLP APIs and is subject to the API's limits and restrictions.
For more information see:

* OpenTelemetry metrics limitations
* [Dynatrace metrics mapping](../../otlp-api/ingest-otlp-metrics/about-metrics-ingest.md#dynatrace-mapping "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* Ingest OpenTelemetry logs

## Related topics

* Enrich ingested data with Dynatrace-specific fields
* Enrich OTLP requests with Kubernetes data