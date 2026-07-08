---
title: Apply memory limits to the OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/memory
---

# Apply memory limits to the OTel Collector

# Apply memory limits to the OTel Collector

* How-to guide
* 2-min read
* Updated on Jan 08, 2026

The following configuration example shows how you configure a Collector instance and its native memory limiter processor to guarantee memory allocation keeps within the specified parameters.

Recommended configuration

For optimal memory usage with your Collector instance, we recommend that you
apply this configuration with most containerized setups. See the section on
[deployment considerations](#deployment-considerations) for more information.

## Prerequisites

* One of the following Collector distributions with the [memory limiter processor﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.155.0/processor/memorylimiterprocessor):

  + The [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + OpenTelemetry [Core](/managed/ingest-from/opentelemetry/collector#collector-core "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.") or [Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
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

[Validate your settings](/managed/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector.") to avoid any configuration issues.

## Components

For our configuration, we configure the following components.

### Receivers

Under `receivers`, we specify the standard `otlp` receiver as active receiver component for our Collector instance.

This is mainly for demonstration purposes. You can specify any other valid receiver here (for example, `zipkin`).

### Processors

Under `processors`, we specify the [`memory_limiter` processor﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.155.0/processor/memorylimiterprocessor) with the following parameters:

* `check_interval` configured to check the memory status every second
* `limit_percentage` configured to allow a maximum memory allocation of 90 percent
* `spike_limit_percentage` configured to allow a maximum spike memory usage of 20 percent

With this configuration, the OTel Collector checks the memory allocation every second
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
documentation﻿](https://pkg.go.dev/runtime#hdr-Environment_Variables) describing
how the environment variable works.

#### Deployment considerations

In containerized environments, or other places where the host environment sets
the Collector's maximum allowed memory, we recommend you use the
`limit_percentage` and `spike_limit_percentage` options.

For deployments on virtual machines or bare metal where the Collector is not
given an explicit memory quota, we instead recommend you use the `limit_mib` and
`spike_limit_mib` options.

### Exporters

Under `exporters`, we specify the default [`otlp_http` exporter﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.155.0/exporter/otlphttpexporter) and configure it with our Dynatrace API URL and the required authentication token.

For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `Authorization`.

* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` contains the [API token](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Service pipelines

Under `service`, we assemble our receiver and exporter objects into pipelines for traces, metrics, and logs and enable our memory limiter processor by referencing it under `processors` for each respective pipeline.

## Limits and limitations

Data is ingested using the OpenTelemetry protocol (OTLP) via the [Dynatrace OTLP APIs](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") and is subject to the API's limits and restrictions.
For more information see:

* [OpenTelemetry metrics limitations](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Dynatrace metrics mapping](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Ingest OpenTelemetry logs](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.")

## Related topics

* [Enrich ingested data with Dynatrace-specific fields](/managed/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.")
* [Enrich OTLP requests with Kubernetes data](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.")