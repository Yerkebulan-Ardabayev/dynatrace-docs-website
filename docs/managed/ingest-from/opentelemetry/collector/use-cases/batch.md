---
title: Batch OTLP requests with the OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/batch
---

# Batch OTLP requests with the OTel Collector

# Batch OTLP requests with the OTel Collector

* How-to guide
* 3-min read
* Updated on May 11, 2026

The following configuration example shows how you configure a Collector instance and the `otlp_http` exporter to queue and batch OTLP requests and improve throughput performance.

Recommended configuration

For optimal performance of your Collector instance, we recommend you adjust the
batching configuration in all setups similar to what is below. The values in the
following configuration example have been found to work well for most data, but
you are encouraged to determine the best settings for your particular situation.

## Prerequisites

* A Collector distribution:

  + The [Dynatrace Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + The OpenTelemetry [Core](/managed/ingest-from/opentelemetry/collector#collector-core "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.") or [Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.") distribution
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



http:



endpoint: 0.0.0.0:4318



exporters:



otlp_http/traces:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



sending_queue:



batch:



min_size: 5000



max_size: 5000



flush_timeout: 60s



otlp_http/metrics:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



sending_queue:



batch:



min_size: 3000



max_size: 3000



flush_timeout: 60s



otlp_http/logs:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



sending_queue:



batch:



min_size: 1800



max_size: 2000



flush_timeout: 60s



service:



pipelines:



traces:



receivers: [otlp]



exporters: [otlp_http/traces]



metrics:



receivers: [otlp]



exporters: [otlp_http/metrics]



logs:



receivers: [otlp]



exporters: [otlp_http/logs]
```

Configuration validation

[Validate your settings](/managed/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector.") to avoid any configuration issues.

## Components

For our configuration, we configure the following components.

### Receivers

Under `receivers`, we specify the standard `otlp` receiver as active receiver component for our Collector instance.

This is for demonstration purposes. You can specify any other valid receiver here (for example, `zipkin`).

### Exporters

Under `exporters`, we specify an [`otlp_http` exporter﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/exporter/otlphttpexporter) for each signal and configure it with the appropriate batching settings as well as our Dynatrace API URL and the required authentication token.

For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `Authorization`.

* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` contains the [API token](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

Under the `sending_queue` section of the exporter's config, we specify a different [`batch` section﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/exporter/exporterhelper#sending-queue-batch-settings)
for each telemetry signal, with the following parameters:

* `min_size`: sets the minimum number of entries the processor will queue before sending the whole batch.
* `max_size`: sets the maximum number of entries a batch may contain. More entries will split a large batch into smaller ones.
* `timeout`: defines the duration after which the batch will be sent. A batch is sent after the `timeout` only when the `send_batch_size` condition is not reached.

With this configuration, the OTel Collector queues telemetry entries in batches, ensuring a good balance between the size and number of export requests
to the Dynatrace API.

Batch size values

Not only the number of individual telemetry entries will contribute to the eventual size
of a batch, but also the number of associated attributes and their size.

For example, attributes on spans/metrics/logs can make a batch size with the same amount of entries larger,
depending on how many/how large the attributes are.

Use the configuration values above as a starting point, but be sure to adapt them to fit your data volume
and comply with the Dynatrace API limits for each signal type ([traces](/managed/ingest-from/opentelemetry/otlp-api/ingest-traces#ingestion-limits "Learn how Dynatrace ingests OpenTelemetry traces and what limitations apply."),
[metrics](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#limits "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply."), [logs](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs#ingestion-limits "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.")) to avoid request rejections.

You can use the [ActiveGate self-monitoring metrics](/managed/ingest-from/dynatrace-activegate/activegate-sfm-metrics#rest "Explore ActiveGate self-monitoring  metrics.")
to troubleshoot rejected requests. For example, you can use: `dsfm:active_gate.rest.request_count` filtering for the `operation`
dimension (`POST /otlp/v1/<...>` for OTLP ingest) and split by `response_code`. Large requests are rejected with HTTP status code `413`.

Another alternative is checking the Collector logs for error messages such as: `HTTP Status Code 413, Message=Max Payload size of`.

### Service pipelines

Under `service`, we assemble our receiver and exporter objects into pipelines for traces, metrics, and logs.

## Limits and limitations

Data is ingested using the OpenTelemetry protocol (OTLP) via the [Dynatrace OTLP APIs](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") and is subject to the API's limits and restrictions.
For more information see:

* [OpenTelemetry metrics limitations](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Dynatrace metrics mapping](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Ingest OpenTelemetry logs](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.")

## Related topics

* [Enrich ingested data with Dynatrace-specific fields](/managed/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.")
* [Enrich OTLP requests with Kubernetes data](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.")