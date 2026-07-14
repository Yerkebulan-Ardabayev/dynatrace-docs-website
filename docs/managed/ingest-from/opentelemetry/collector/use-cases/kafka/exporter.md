---
title: Forward OpenTelemetry data with the Kafka exporter
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/kafka/exporter
---

# Forward OpenTelemetry data with the Kafka exporter

# Forward OpenTelemetry data with the Kafka exporter

* How-to guide
* 3-min read
* Updated on May 11, 2026

The following configuration example shows how you configure a Collector instance to export OTLP data to Kafka.

## Prerequisites

* A deployed and configured Collector distribution, whether:

  + [Dynatrace Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + [OpenTelemetry Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + [custom Builder version](/managed/ingest-from/opentelemetry/collector#collector-builder "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
* The [`kafkaexporter`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/exporter/kafkaexporter) component.
* A Kafka server deployed with a reachable `BROKER_ADDRESS`.
  For more information, see the [Kafka Apache quickstart guide﻿](https://kafka.apache.org/quickstart).

## Demo configuration

Here is an example YAML file for a basic Collector configuration that can be used to export OpenTelemetry traces, metrics, and logs to Kafka.

```
processors:



memory_limiter:



check_interval: 1s



limit_percentage: 100



receivers:



otlp:



protocols:



grpc:



endpoint: 0.0.0.0:4317



exporters:



kafka:



brokers: ["${env:BROKER_ADDRESS}"]



tls:



insecure: true # Only necessary if your Kafka server does not provide a certificate that's trusted by the OTel Collector.



traces:



metrics:



logs:



sending_queue:



batch:



send_batch_size: 500



flush_timeout: 30s



service:



pipelines:



traces:



receivers: [otlp]



processors: [memory_limiter, batch]



exporters: [kafka]



metrics:



receivers: [otlp]



processors: [memory_limiter, batch]



exporters: [kafka]



logs:



receivers: [otlp]



processors: [memory_limiter, batch]



exporters: [kafka]
```

For this configuration to work, you need to set the `BROKER_ADDRESS` environment variable.
The value is specific to your Kafka server.

Configuration validation

[Validate your settings](/managed/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector.") to avoid any configuration issues.

## Components

For our configuration, we configure certain components as described in the sections below.

### Receivers

Under `receivers`, we specify [`otlp`﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/receiver/otlpreceiver) as the active receiver component for our deployment.
This is required to accept OTLP data.

### Processors

Under `processors`, we specify:

* [`memory_limiter` processor﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/processor/memorylimiterprocessor).
* [`batch` processor﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/processor/batchprocessor) as per [recommendation for the kafka exporter﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/exporter/kafkaexporter#readme).

### Exporters

Under `exporters`, we specify the [`kafka` exporter﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/exporter/kafkaexporter) to forward data to the Kafka server.

### Service pipeline

Under `service`, we assemble our receiver, processors, and exporter objects into service pipelines, which will perform these steps:

1. Accept OTLP requests on the configured ports.
2. Use the `memory_limit` processor to make sure that the Collector doesn't run out of memory.
3. Batch data using the `batch` processor.
4. Export data to Kafka server.

## Related topics

* [OTel Collector for ingesting telemetry into Dynatrace](/managed/ingest-from/opentelemetry/collector "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
* [Buffer data via Kafka with OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/kafka "How to configure the OpenTelemetry Collector to buffer data via Kafka.")
* [Receive OpenTelemetry data with the Kafka receiver](/managed/ingest-from/opentelemetry/collector/use-cases/kafka/receiver "How to configure the OpenTelemetry Collector's Kafka receiver to ingest OpenTelemetry from Kafka.")
* [Deploy the Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector/deployment "How to deploy the Dynatrace OpenTelemetry Collector.")
* [Configure the OTel Collector](/managed/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.")