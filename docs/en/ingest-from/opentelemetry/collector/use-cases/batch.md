---
title: Batch OTLP requests with the OpenTelemetry Collector
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/use-cases/batch
scraped: 2026-02-17T05:07:06.562681
---

# Batch OTLP requests with the OpenTelemetry Collector

# Batch OTLP requests with the OpenTelemetry Collector

* Latest Dynatrace
* How-to guide
* 3-min read
* Published Oct 11, 2023

The following configuration example shows how you configure a Collector instance and its native batch processor to queue and batch OTLP requests and improve throughput performance.

Recommended configuration

For optimal performance of your Collector instance, we recommend that you apply this configuration with all setups.

If you use other processors, make sure the batch processor is configured last in your pipeline.

## Prerequisites

* One of the following Collector distributions with the [batch processorï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/processor/batchprocessor):

  + The [Dynatrace Collector](/docs/ingest-from/opentelemetry/collector#dt-collector-dist "Learn about the Dynatrace OTel Collector.")
  + The OpenTelemetry [Core](/docs/ingest-from/opentelemetry/collector#collector-core "Learn about the Dynatrace OTel Collector.") or [Contrib](/docs/ingest-from/opentelemetry/collector#collector-contrib "Learn about the Dynatrace OTel Collector.") distribution
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



batch/traces:



send_batch_size: 5000



send_batch_max_size: 5000



timeout: 60s



batch/metrics:



send_batch_size: 3000



send_batch_max_size: 3000



timeout: 60s



batch/logs:



send_batch_size: 1800



send_batch_max_size: 2000



timeout: 60s



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



traces:



receivers: [otlp]



processors: [batch/traces]



exporters: [otlp_http]



metrics:



receivers: [otlp]



processors: [batch/metrics]



exporters: [otlp_http]



logs:



receivers: [otlp]



processors: [batch/logs]



exporters: [otlp_http]
```

Configuration validation

[Validate your settings](/docs/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector.") to avoid any configuration issues.

## Components

For our configuration, we configure the following components.

### Receivers

Under `receivers`, we specify the standard `otlp` receiver as active receiver component for our Collector instance.

This is for demonstration purposes. You can specify any other valid receiver here (for example, `zipkin`).

### Processors

Under `processors`, we specify a different [`batch` processorï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/processor/batchprocessor)
for each telemetry signal, with the following parameters:

* `send_batch_size`: sets the minimum number of entries the processor will queue before sending the whole batch.
* `send_batch_max_size`: sets the maximum number of entries a batch may contain. More entries will split the batch into smaller ones.
* `timeout`: defines the duration after which the batch will be sent. A batch is sent after the `timeout` only when the `send_batch_size` condition is not reached.

With this configuration, the Collector queues telemetry entries in batches, ensuring a good balance between the size and number of export requests
to the Dynatrace API.

Batch size values

Not only the number of individual telemetry entries will contribute to the eventual size
of a batch, but also the number of associated attributes and their size.

For example, attributes on spans/metrics/logs can make a batch size with the same amount of entries larger,
depending on how many/how large the attributes are.

Use the configuration values above as a starting point, but be sure to adapt them to fit your data volume
and comply with the Dynatrace API limits for each signal type ([traces](/docs/ingest-from/opentelemetry/otlp-api/ingest-traces#ingestion-limits "Learn how Dynatrace ingests OpenTelemetry traces and what limitations apply."),
[metrics](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#limits "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply."), [logs](/docs/ingest-from/opentelemetry/otlp-api/ingest-logs#ingestion-limits "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.")) to avoid request rejections.

You can use the [ActiveGate self-monitoring metrics](/docs/ingest-from/dynatrace-activegate/activegate-sfm-metrics#rest "Explore ActiveGate self-monitoring  metrics.")
to troubleshoot rejected requests. For example, you can use: `dsfm:active_gate.rest.request_count` filtering for the `operation`
dimension (`POST /otlp/v1/<...>` for OTLP ingest) and split by `response_code`. Large requests are rejected with HTTP status code `413`.

Another alternative is checking the Collector logs for error messages such as: `HTTP Status Code 413, Message=Max Payload size of`.

### Exporters

Under `exporters`, we specify the default [`otlp_http` exporterï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/exporter/otlphttpexporter) and configure it with our Dynatrace API URL and the required authentication token.

For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `Authorization`.

* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` contains the [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Service pipelines

Under `service`, we assemble our receiver and exporter objects into pipelines for traces, metrics, and logs and enable our batch processor by referencing it under `processors` for each respective pipeline.

## Limits and limitations

Data is ingested using the OpenTelemetry protocol (OTLP) via the [Dynatrace OTLP APIs](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") and is subject to the API's limits and restrictions.
For more information see:

* [OpenTelemetry metrics limitations](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Dynatrace metrics mapping](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Ingest OpenTelemetry logs](/docs/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.")

## Related topics

* [Enrich ingested data with Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.")
* [Enrich OTLP requests with Kubernetes data](/docs/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.")