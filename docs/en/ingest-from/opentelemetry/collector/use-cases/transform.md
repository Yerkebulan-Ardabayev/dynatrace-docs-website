---
title: Transform and filter data with the OpenTelemetry Collector
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/use-cases/transform
scraped: 2026-02-26T21:26:11.722421
---

# Transform and filter data with the OpenTelemetry Collector

# Transform and filter data with the OpenTelemetry Collector

* Latest Dynatrace
* How-to guide
* 4-min read
* Published Aug 19, 2024

The following configuration example shows how to configure a Collector instance to transform and manipulate OTLP requests, before forwarding them to Dynatrace.

Using the processors shown in this example (`filter` and `transform`), it is possible to streamline requests before sending them to Dynatrace and omit data possibly irrelevant to your use case, and to reduce billing costs.

## Prerequisites

* One of the following Collector distributions with the [transformï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/transformprocessor) and [filterï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/filterprocessor) processors

  + The [Dynatrace Collector](/docs/ingest-from/opentelemetry/collector#dt-collector-dist "Learn about the Dynatrace OTel Collector.")
  + OpenTelemetry [Contrib](/docs/ingest-from/opentelemetry/collector#collector-contrib "Learn about the Dynatrace OTel Collector.")
  + A [custom Builder version](/docs/ingest-from/opentelemetry/collector#collector-builder "Learn about the Dynatrace OTel Collector.")
* The [API URL](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") of your Dynatrace environment
* An [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") with the relevant access scope

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



transform:



trace_statements:



- context: resource



statements:



# Only keep a certain set of resource attributes



- keep_matching_keys(attributes, "^(aaa|bbb|ccc).*")



- context: span



statements:



# Only keep a certain set of span attributes



- keep_matching_keys(attributes, "(^xyz.pqr$)|(^(aaa|bbb|ccc).*)")



# Set a static key



- set(attributes["svc.marker"], "purchasing")



# Delete a specific key



- delete_key(attributes, "message")



# Rewrite a key



- set(attributes["purchase.id"], ConvertCase(attributes["purchase.id"], "upper"))



# Apply regex replacement



- replace_pattern(name, "^.*(DataSubmission-\d+).*$", "$$1")



metric_statements:



- context: metric



statements:



# Rename all metrics containing '_bad' suffix in their name with `_invalid`



- replace_pattern(name, "(.*)_bad$", "$${1}_invalid")



filter:



error_mode: ignore



traces:



span:



# Filter spans with resource attributes matching the provided regular expression



- IsMatch(resource.attributes["k8s.pod.name"], "^my-pod-name.*")



metrics:



metric:



# Filter metrics which contain at least one data point with a "bad.metric" attribute



- 'HasAttrKeyOnDatapoint("bad.metric")'



logs:



log_record:



# Filter logs with resource attributes matching the configured names



- resource.attributes["service.name"] == "service1"



- resource.attributes["service.name"] == "service2"



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



traces:



receivers: [otlp]



processors: [filter,transform]



exporters: [otlp_http]



metrics:



receivers: [otlp]



processors: [filter]



exporters: [otlp_http]



logs:



receivers: [otlp]



processors: [filter]



exporters: [otlp_http]
```

Configuration validation

[Validate your settings](/docs/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector.") to avoid any configuration issues.

## Components

For our configuration, we configure the following components.

### Receiver

Under `receivers`, we specify the standard `otlp` receiver as active receiver component for our Collector instance.

This is for demonstration purposes. You can specify any other valid receiver here (for example, `zipkin`).

### Processor

#### Transform

Under `processors`, we specify the [`transform` processorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/transformprocessor) with a set of different attribute modification statements. `context` indicates the scope to which the statements should apply (here, `resource` for resource attributes, `span` for span attributes, and `metric` for metrics).

See the [OpenTelemetry documentation of the transform processorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/processor/transformprocessor/README.md) for more details on the individual configuration options.

The sample configuration above uses the following statements:

#### Filter

In addition, we also configure an instance of the [`filter` processorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/filterprocessor), to filter signal based on the following criteria:

See the [OpenTelemetry documentation of the filter processorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/processor/filterprocessor/README.md) for more details on the individual configuration options.

### Exporter

Under `exporters`, we specify the default [`otlp_http` exporterï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/exporter/otlphttpexporter) and configure it with our Dynatrace API URL and the required authentication token.

For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `Authorization`.

* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` contains the [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Service pipeline

Under `service`, we assemble our receiver, processor, and exporter objects into a traces pipeline, which accepts OTLP traces on the configured endpoints and transforms trace attributes according to the configured rules, before forwarding everything to Dynatrace using the exporter.

## Limits and limitations

Data is ingested using the OpenTelemetry protocol (OTLP) via the [Dynatrace OTLP APIs](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") and is subject to the API's limits and restrictions.
For more information see:

* [OpenTelemetry metrics limitations](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Dynatrace metrics mapping](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Ingest OpenTelemetry logs](/docs/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.")

## Related topics

* [Enrich ingested data with Dynatrace-specific fields](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.")