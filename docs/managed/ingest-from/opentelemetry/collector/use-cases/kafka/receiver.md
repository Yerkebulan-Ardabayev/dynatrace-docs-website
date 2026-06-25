---
title: Receive OpenTelemetry data with the Kafka receiver
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/kafka/receiver
scraped: 2026-05-12T12:15:06.191704
---

# Receive OpenTelemetry data with the Kafka receiver

# Receive OpenTelemetry data with the Kafka receiver

* How-to guide
* 3-min read
* Published Nov 05, 2025

The following configuration example shows how you configure Kafka to read data from topics and relay this data via OTLP.

## Prerequisites

* A deployed and configured collector distribution, whether

  + [Dynatrace Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + [OpenTelemetry Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + [custom Builder version](/managed/ingest-from/opentelemetry/collector#collector-builder "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
* The [`kafkareceiver`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/kafkareceiver) component.
* A Kafka server deployed with a reachable `BROKER_ADDRESS`.
  For more information, see the [Kafka Apache quickstart guideï»¿](https://kafka.apache.org/quickstart).
* The [Dynatrace API endpoint URL](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") to which the data should be exported.
* An [API token](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") with the relevant access scope. (Only for exports to SaaS and ActiveGate.)

## Demo configuration

Here is an example YAML file for a basic Collector configuration that can be used to receive OpenTelemetry traces, metrics, and logs from Kafka.

```
receivers:



kafka:



tls:



insecure: true # Only necessary if your Kafka server does not provide a certificate that's trusted by the OTel Collector.



traces:



metrics:



logs:



brokers: ["${env:BROKER_ADDRESS}"]



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



traces:



receivers: [kafka]



exporters: [otlp_http]



metrics:



receivers: [kafka]



exporters: [otlp_http]



logs:



receivers: [kafka]



exporters: [otlp_http]
```

For this configuration to work, you need to set the following environment variables.

* `BROKER_ADDRESS`: Specific to your Kafka server.
* `DT_ENDPOINT`: The [base URL of the Dynatrace API endpoint](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`).
* `DT_API_TOKEN`: The [API token](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.").

Configuration validation

[Validate your settings](/managed/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector.") to avoid any configuration issues.

## Components

For our configuration, we configure certain components as described in the sections below.

### Receivers

Under `receivers`, we specify [`kafka`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/kafkareceiver) as the active receiver component for our deployment.
This is required to receive data from Kafka server.

### Exporters

Under `exporters`, we specify the [`otlp_http` exporterï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/exporter/otlphttpexporter) to forward data into Dynatrace.

For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `Authorization`.

* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`).
* `DT_API_TOKEN` contains the [API token](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.").

### Service pipeline

Under `service`, we assemble our receiver, and exporter objects into service pipelines, which will perform these steps:

1. Receive data from Kafka server.
2. Export the data to Dynatrace.

## Related topics

* [OTel Collector for ingesting telemetry into Dynatrace](/managed/ingest-from/opentelemetry/collector "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
* [Buffer data via Kafka with OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/kafka "How to configure the OpenTelemetry Collector to buffer data via Kafka.")
* [Forward OpenTelemetry data with the Kafka exporter](/managed/ingest-from/opentelemetry/collector/use-cases/kafka/exporter "How to configure the OpenTelemetry Collector to forward OpenTelemetry data with the Kafka exporter.")
* [Deploy the Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector/deployment "How to deploy the Dynatrace OpenTelemetry Collector.")
* [Configure the OTel Collector](/managed/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.")