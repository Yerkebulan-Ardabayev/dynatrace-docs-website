---
title: Configure the OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/configuration
---

# Configure the OTel Collector

# Configure the OTel Collector

* How-to guide
* 4-min read
* Updated on Apr 16, 2026

To successfully configure your OTel Collector instance, you need to configure each component (receiver, optional processor, and exporter) individually in the Collector YAML configuration file and enable them via additional pipeline objects.

Dynatrace OTel Collector

As part of a Dynatrace OTel Collector setup, note that you can only configure the components shipped with Dynatrace OTel Collector.

For a complete list of components that the Dynatrace OTel Collector supports, see [OTel Collector for ingesting telemetry into Dynatrace](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.").

## Configuration example

Here is an example YAML file for a very basic Collector configuration that can be used to export OpenTelemetry traces, metrics, and logs to Dynatrace.

```
receivers:



otlp:



protocols:



grpc:



endpoint: 0.0.0.0:4317



http:



endpoint: 0.0.0.0:4318



processors:



cumulativetodelta:



max_staleness: 25h



exporters:



otlp_http:



endpoint: "${env:DT_ENDPOINT}"



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



processors: [cumulativetodelta]



exporters: [otlp_http]



logs:



receivers: [otlp]



processors: []



exporters: [otlp_http]
```

Cumulativetodelta processor recommendation

It is recommended to set the `max_staleness` parameter of the [cumulativetodelta processor﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/cumulativetodeltaprocessor) to a value higher than how often the Collector receives metrics (e.g., how often metrics via OTLP are received, or how long the Prometheus scrape interval is). This ensures that no references to abandoned metric streams accumulate in memory over time.

In this YAML file, we configure the following components:

* An OTLP receiver (`otlp`) that can receive data via gRPC and HTTP.
* A processor to convert any metrics with cumulative temporality to delta temporality (see [Delta metrics](#delta-metrics) for more details).
* An OTLP HTTP exporter (`otlp_http`) configured with:

  + The Dynatrace endpoint, see [Base URLs](/managed/ingest-from/opentelemetry/otlp-api#base-url "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")
  + An API token, see [Authentication](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.").

As part of the `otlp_http` exporter configuration, you can also set the `logs_endpoint` to control how Dynatrace processes structured log data: keep the original nested structure (raw), or flatten it into key paths (flattened).
For more information, see [Configure structured logs processing](#structured-logs).

In the example configuration above, the Dynatrace token needs to have the **Ingest OpenTelemetry traces** (`openTelemetryTrace.ingest`), the **Ingest metrics** (`metrics.ingest`), and the **Ingest logs** (`logs.ingest`) permissions.

Within the service section, you define each component separately.

* Extensions can be enabled in their own section, while receivers, processors, and exporters are grouped under a pipeline section.
* Pipelines can be of type traces, metrics, or logs.
* Each receiver/processor/exporter can be used in more than one pipeline. For processors referenced in multiple pipelines, each pipeline gets a separate instance of the processors. This contrasts with receivers/exporters referenced in multiple pipelines, where only one instance of a receiver/exporter is used for all pipelines. Also, note that the order of processors dictates the order in which data is processed.
* You can also define the same components more than once. For example, you can have two different receivers or even two or more distinct parts of the pipeline.
* Even if a component is properly configured in its section, it will not be enabled unless it's also defined in the service section.

## Validate the configuration

It is important to ensure the used Collector configuration is syntactically and semantically correct. For example, YAML uses spaces (not tabs) for indentation, to define the document hierarchy, and it is necessary to use the right level of indentation for each section and component. The Collector provides the built-in `validate` command to verify the configuration and its components and services are properly configured.

```
dynatrace-otel-collector validate --config=[PATH_TO_YOUR_CONFIGURATION_FILE]
```

If you run a container instance of the Collector, you can also use the following Docker command to run the validation directly from your container.

```
docker run -v $(pwd):$(pwd) -w $(pwd) ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector:0.52.0 validate --config=[YOUR_CONFIGURATION_FILE]
```

## Delta metrics

Dynatrace requires metrics data to be [sent with delta temporality](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#aggregation-temporality "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.") and **not** cumulative temporality.

If your application doesn't allow you to configure delta temporality, you can use the [`cumulativetodelta` processor﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/cumulativetodeltaprocessor) to have your Collector instance adjust cumulative values to delta values. The [configuration example](#configuration-example) above shows how to configure and reference the processor in your Collector configuration.

## Chained and load-balanced Collectors

When you use more than one Collector instance, it's important to maintain stable value propagation across all instances.

This is particularly important when you send OTLP requests across different Collector instances (for example, load balancing), as each Collector instance keeps track of its own delta offset, which may break the data reported to the Dynatrace backend.

In such scenarios, we recommend routing your OTLP requests through a single, outbound Collector instance that forwards the data to the Dynatrace backend and takes care of the delta conversion. The other Collector instances should use a cumulative aggregation, to ensure stable and consistent value propagation.

## Configure structured logs processing

When you export structured logs to Dynatrace, Dynatrace processes the log data in one of two ways.
It either:

* Keeps the original nested structure from your logs source ("raw").
* Flattens it so all log attribute values are accessible via key paths ("flattened").

To configure this behavior, use the `logs_endpoint` setting as shown in the example below:

```
exporters:



otlp_http:



endpoint: "${env:DT_ENDPOINT}"



logs_endpoint: "${env:DT_ENDPOINT}/v1/logs?structure=raw"



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"
```

Make sure to include the complete API endpoint path including `/v1/logs` (environment variables are allowed), followed by the desired behavior.

* To keep the original nested structure, use `structure=raw`.
* To flatten the log data, use `structure=flattened`.

For more information, see [Log ingestion API processing](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs#otlp-structured-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.").

If this configuration option is not specified, the default behavior depends on when your environment was created.

* For Dynatrace version 1.331+ and environments created after February 1, 2026: Raw.
* For environments created before February 1, 2026: Flattened.