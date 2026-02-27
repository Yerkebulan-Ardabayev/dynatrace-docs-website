---
title: Ingest Zipkin data with the OpenTelemetry Collector
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/use-cases/zipkin
scraped: 2026-02-27T21:26:12.315016
---

# Ingest Zipkin data with the OpenTelemetry Collector

# Ingest Zipkin data with the OpenTelemetry Collector

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Oct 11, 2023

The following configuration example shows how you configure a Collector instance to accept Zipkin data, transform it to OTLP, and send it to the Dynatrace backend.

## Limitations

### B3 requirements

Pay attention to the B3 requirements, to avoid having spans being dropped because of shared and duplicated span identifiers. See the [propagator specificationï»¿](https://opentelemetry.io/docs/specs/otel/context/api-propagators/#b3-requirements) for more details.

For example, if you are using [Spring Code Sleuthï»¿](https://cloud.spring.io/spring-cloud-sleuth/2.1.x/multi/multi__propagation.html#_extracting_a_propagated_context), you can use the following configuration setting to disable span sharing:

```
spring:



sleuth:



supports-join: false
```

### Single Collector routing

Make sure to route all related Zipkin/B3 spans via the same Collector instance, to guarantee full ingestion. If you ingest some spans using OneAgent alone, they may not be properly linked and not show up as connected to your Zipkin spans.

## Prerequisites

* One of the following Collector distributions with the [Zipkin receiverï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/receiver/zipkinreceiver):

  + The [Dynatrace Collector](/docs/ingest-from/opentelemetry/collector#dt-collector-dist "Learn about the Dynatrace OTel Collector.")
  + OpenTelemetry [Contrib](/docs/ingest-from/opentelemetry/collector#collector-contrib "Learn about the Dynatrace OTel Collector.")
  + A [custom Builder version](/docs/ingest-from/opentelemetry/collector#collector-builder "Learn about the Dynatrace OTel Collector.")
* The [Dynatrace API endpoint URL](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") to which the data should be exported
* An [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") with the relevant access scope (only required for SaaS and ActiveGate)

See [Collector Deployment](/docs/ingest-from/opentelemetry/collector/deployment "How to deploy Dynatrace OTel Collector.") and [Collector Configuration](/docs/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.") on how to set up your Collector with the configuration below.

## Demo configuration

```
receivers:



zipkin:



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



traces:



receivers: [zipkin]



processors: []



exporters: [otlp_http]
```

Configuration validation

[Validate your settings](/docs/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector.") to avoid any configuration issues.

## Components

For our configuration, we configure the following components.

### Receivers

Under `receivers`, we specify the `zipkin` receiver as active receiver component for our Collector instance.

The Zipkin receiver can be customized with [a few more attributesï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/receiver/zipkinreceiver), which we leave with their default values in our example.

### Exporters

Under `exporters`, we specify the default [`otlp_http` exporterï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/exporter/otlphttpexporter) and configure it with our Dynatrace API URL and the required authentication token.

For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `Authorization`.

* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` contains the [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Service pipelines

Under `service`, we eventually assemble our receiver and exporter objects into a traces pipeline, which will handle our Zipkin transformation to OTLP.

## Related topics

* [Enrich ingested data with Dynatrace-specific fields](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.")
* [Enrich OTLP requests with Kubernetes data](/docs/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.")