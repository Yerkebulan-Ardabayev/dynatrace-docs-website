---
title: Enrich OTLP with OneAgent data (non-containerized)
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/use-cases/enrich
scraped: 2026-02-21T21:23:39.527199
---

# Enrich OTLP with OneAgent data (non-containerized)

# Enrich OTLP with OneAgent data (non-containerized)

* Latest Dynatrace
* How-to guide
* 2-min read
* Updated on Dec 17, 2025

The following configuration example shows how you configure a Collector instance to enrich OpenTelemetry data with OneAgent host entities.

Enrichment is used for linking OpenTelemetry data to its OneAgent host and properly associating it within the topology model. For example, when ingesting logs from different hosts, tying the host entity to the respective log data allows you to run host-based log analytics tasks.

Container environments

Enrichment is specific to non-container OneAgent environments. Configuring a containerized Collector enrichment setup may lead to incorrect host and topology associations.

## Prerequisites

* One of the following Collector distributions with the [Resource Detection processorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/processor/resourcedetectionprocessor):

  + The [Dynatrace Collector](/docs/ingest-from/opentelemetry/collector#dt-collector-dist "Learn about the Dynatrace OTel Collector.")
  + OpenTelemetry [Contrib](/docs/ingest-from/opentelemetry/collector#collector-contrib "Learn about the Dynatrace OTel Collector.")
  + A [custom Builder version](/docs/ingest-from/opentelemetry/collector#collector-builder "Learn about the Dynatrace OTel Collector.")
* A OneAgent running on the same host as the Collector, where the OneAgent monitors in either Full-Stack, Infrastructure, or Foundation & Discovery mode.
* The [Dynatrace API endpoint URL](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") to which the data should be exported, configured as system environment variable
* An [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") with the relevant access scope (only required for SaaS and ActiveGate), configured as system environment variable

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



resourcedetection/dynatrace:



detectors: [dynatrace]



override: false



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



traces:



receivers: [otlp]



processors: [resourcedetection/dynatrace]



exporters: [otlp_http]



metrics:



receivers: [otlp]



processors: [resourcedetection/dynatrace]



exporters: [otlp_http]



logs:



receivers: [otlp]



processors: [resourcedetection/dynatrace]



exporters: [otlp_http]
```

Configuration validation

[Validate your settings](/docs/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector.") to avoid any configuration issues.

## Components

For our configuration, we configure the following components.

### Receivers

Under `receivers`, we specify the standard `otlp` receiver as active receiver component for our Collector instance.

This is mainly for demonstration purposes. You can specify any other valid receiver here (for example, `zipkin`).

### Processors

Under `processors`, we specify the [`resourcedetection` processorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/processor/resourcedetectionprocessor) and configure it with the [Dynatrace-specific detector `dynatrace`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/processor/resourcedetectionprocessor/README.md#dynatrace).

With this configuration, the resource detector processor will attempt to load the following three attributes from the [OneAgent enrichment file](/docs/ingest-from/extend-dynatrace/extend-data#dynatrace-oneagent "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions."):

* `dt.entity.host`
* `host.name`
* `dt.smartscape.host`

If the resource detector could load these values successfully, it will add them as resource attributes to the OTLP request. No additional processor configuration is necessary.

### Exporters

Under `exporters`, we specify the default [`otlp_http` exporterï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/exporter/otlphttpexporter) and configure it with our Dynatrace API URL and the required authentication token.

For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `headers`.

* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` contains the [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Service pipeline

Under `service`, we assemble our receiver, processor, and exporter objects into service pipelines, which will perform these steps:

* accept OTLP requests on the configured ports
* enrich them with the Dynatrace-relevant host data, using the resource detector processor
* and export the enriched data to Dynatrace