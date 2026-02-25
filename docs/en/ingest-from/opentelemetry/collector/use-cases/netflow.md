---
title: Ingest NetFlow with the OpenTelemetry Collector
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/use-cases/netflow
scraped: 2026-02-25T21:30:03.510519
---

# Ingest NetFlow with the OpenTelemetry Collector

# Ingest NetFlow with the OpenTelemetry Collector

* Latest Dynatrace
* How-to guide
* 1-min read
* Updated on Jan 27, 2026

The following configuration example shows how to configure a Collector instance to accept NetFlow packets and ingest them as OTLP requests into Dynatrace.

## Prerequisites

* One of the following Collector distributions with the [NetFlow receiverï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/receiver/netflowreceiver):

  + [The Dynatrace Collector](/docs/ingest-from/opentelemetry/collector#dt-collector-dist "Learn about the Dynatrace OTel Collector.")
  + [OpenTelemetry Contrib](/docs/ingest-from/opentelemetry/collector#collector-contrib "Learn about the Dynatrace OTel Collector.")
  + [A custom Builder version](/docs/ingest-from/opentelemetry/collector#collector-builder "Learn about the Dynatrace OTel Collector.")
* The [Dynatrace API endpoint URL](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") to which the data should be exported.
* An [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") with the Ingest logs (`logs.ingest`) scope.
* A NetFlow- or sFlow-capable device that can send NetFlow packets to the Collector instance.

See [Collector Deployment](/docs/ingest-from/opentelemetry/collector/deployment "How to deploy Dynatrace OTel Collector.") and [Collector Configuration](/docs/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.") on how to set up your Collector with the configuration below.

## Collector configuration

```
receivers:



netflow:



hostname: "0.0.0.0"



scheme: netflow



port: 2055



sockets: 2



workers: 4



processors:



batch:



send_batch_size: 30



timeout: 30s



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



logs:



receivers: [netflow]



processors: [batch]



exporters: [otlp_http]
```

Check the [NetFlow receiverï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/receiver/netflowreceiver#netflow-receiver) documentation for the available configuration options.

We recommend setting the `sockets` parameter to match the number of CPU cores available on the Collector instance, and the `workers` parameter to twice the number of sockets. This configuration allows the Collector to process multiple incoming NetFlow packets concurrently, which improves performance.

For extremely large volumes of data, you should parallelize the configuration among multiple Collector instances.

Configuration validation

[Validate your settings](/docs/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector.") to avoid any configuration issues.

## Components

For our configuration, we configure the following components.

### Receivers

Under `receivers`, we specify the `netflow` receiver as the active receiver component for our Collector instance and configure it to listen on specified ports.

### Processors

Under `processors`, we specify the `batch` processor, which batches the incoming NetFlow packets before sending them to Dynatrace. This is useful for optimizing performance and reducing the number of requests sent.

### Exporters

Under `exporters`, we specify the default [`otlp_http` exporterï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/exporter/otlphttpexporter) and configure it with our Dynatrace API URL and the required authentication token.

For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `Authorization`.

* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` contains the [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Service pipelines

Under `service`, we assemble our receiver and exporter objects into a logs pipeline, which will listen on the configured address for incoming NetFlow packets and forward them to Dynatrace using the exporter.

## Data visualization

The logs records will be available in Dynatrace with fields documented in the [receiver documentationï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/receiver/netflowreceiver#data-format).

### Example DQL queries

* Fetch all NetFlow logs and summarize the bytes and packets by source and destination addresses:

  ```
  fetch logs



  | filter otel.scope.name == "otelcol/netflowreceiver"



  | summarize {bytes=sum(toDouble(flow.io.bytes)), packets=sum(toDouble(flow.io.packets))}, by: {source = source.address, destination = destination.address}



  | fieldsAdd bytes_relative=bytes



  | fieldsAdd packets_relative=packets



  | sort bytes desc
  ```

  ![Sample NetFlow charts showing top sources, destination and conversations](https://dt-cdn.net/images/screenshot-2025-06-16-at-12-55-07-pm-1956-d01b596006.png)
* Fetch the most used ports:

  ```
  fetch logs



  | filter otel.scope.name == "otelcol/netflowreceiver"



  | summarize {bytes=sum(toDouble(flow.io.bytes))}, by: {port = destination.port}



  | sort bytes desc



  | limit 10
  ```

  ![A NetFlow chart showing the top used ports by bytes](https://dt-cdn.net/images/screenshot-2025-06-16-at-1-04-11-pm-734-9a3a884a16.png)

## Limits and limitations

Logs are ingested using the OpenTelemetry protocol (OTLP) via the [Dynatrace OTLP API](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") and are subject to the API's limits and restrictions.
For more information see:

* [Ingest OpenTelemetry logs](/docs/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.")

## Related topics

* [Ingest logs from files with the OpenTelemetry Collector](/docs/ingest-from/opentelemetry/collector/use-cases/filelog "Configure the OpenTelemetry Collector to ingest log data into Dynatrace.")