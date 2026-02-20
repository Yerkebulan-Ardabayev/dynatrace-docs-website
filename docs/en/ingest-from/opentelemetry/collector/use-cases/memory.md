---
title: Apply memory limits to the OpenTelemetry Collector
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/use-cases/memory
scraped: 2026-02-20T21:14:03.030160
---

# Apply memory limits to the OpenTelemetry Collector

# Apply memory limits to the OpenTelemetry Collector

* Latest Dynatrace
* How-to guide
* 2-min read
* Updated on Jan 08, 2026

The following configuration example shows how you configure a Collector instance and its native memory limiter processor to guarantee memory allocation keeps within the specified parameters.

Recommended configuration

For optimal memory usage with your Collector instance, we recommend that you
apply this configuration with most containerized setups. See the section on
[deployment considerations](#deployment-considerations) for more information.

## Prerequisites

* One of the following Collector distributions with the [memory limiter processorï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/processor/memorylimiterprocessor):

  + The [Dynatrace Collector](/docs/ingest-from/opentelemetry/collector#dt-collector-dist "Learn about the Dynatrace OTel Collector.")
  + OpenTelemetry [Core](/docs/ingest-from/opentelemetry/collector#collector-core "Learn about the Dynatrace OTel Collector.") or [Contrib](/docs/ingest-from/opentelemetry/collector#collector-contrib "Learn about the Dynatrace OTel Collector.")
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



memory_limiter:



check_interval: 1s



limit_percentage: 90



spike_limit_percentage: 20



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



traces:



receivers: [otlp]



processors: [memory_limiter]



exporters: [otlp_http]



metrics:



receivers: [otlp]



processors: [memory_limiter]



exporters: [otlp_http]



logs:



receivers: [otlp]



processors: [memory_limiter]



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

Under `processors`, we specify the [`memory_limiter` processorï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/processor/memorylimiterprocessor) with the following parameters:

* `check_interval` configured to check the memory status every second
* `limit_percentage` configured to allow a maximum memory allocation of 90 percent
* `spike_limit_percentage` configured to allow a maximum spike memory usage of 20 percent

With this configuration, the Collector checks the memory allocation every second
and starts to apply pressure using separate mechanisms after the following
limits are reached:

* Soft limit (`limit_percentage - spike_limit_percentage`): After this limit is
  reached, the processor rejects payloads until memory usage is under the limit.
  It is up to the receiver upstream of the processor to send the proper
  rejection messages.
* Hard limit: (`limit_percentage`): After this limit is reached, the processor
  will force garbage Collection until memory usage is under the limit. Data will
  continue to be rejected until usage is under the soft limit.

In addition to the memory limiter processor, we highly recommend you set the
`GOMEMLIMIT` environment variable to a value 80% of the hard limit. Note that
`GOMEMLIMIT` requires an absolute value in bytes to be set. For example, you
could set `GOMEMLIMIT=1024MiB` to start increasing the frequency of garbage
collection cycles once the Collector reaches 1024 MiB of memory used on the Go
VM heap. For more information, see the [Go package
documentationï»¿](https://pkg.go.dev/runtime#hdr-Environment_Variables) describing
how the environment variable works.

#### Deployment considerations

In containerized environments, or other places where the host environment sets
the Collector's maximum allowed memory, we recommend you use the
`limit_percentage` and `spike_limit_percentage` options.

For deployments on virtual machines or bare metal where the Collector is not
given an explicit memory quota, we instead recommend you use the `limit_mib` and
`spike_limit_mib` options.

### Exporters

Under `exporters`, we specify the default [`otlp_http` exporterï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/exporter/otlphttpexporter) and configure it with our Dynatrace API URL and the required authentication token.

For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `Authorization`.

* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` contains the [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Service pipelines

Under `service`, we assemble our receiver and exporter objects into pipelines for traces, metrics, and logs and enable our memory limiter processor by referencing it under `processors` for each respective pipeline.

## Limits and limitations

Data is ingested using the OpenTelemetry protocol (OTLP) via the [Dynatrace OTLP APIs](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") and is subject to the API's limits and restrictions.
For more information see:

* [OpenTelemetry metrics limitations](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Dynatrace metrics mapping](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Ingest OpenTelemetry logs](/docs/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.")

## Related topics

* [Enrich ingested data with Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.")
* [Enrich OTLP requests with Kubernetes data](/docs/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.")