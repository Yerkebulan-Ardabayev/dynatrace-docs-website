---
title: Sampling with the OpenTelemetry Collector
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/use-cases/sampling
scraped: 2026-02-25T21:28:38.196731
---

# Sampling with the OpenTelemetry Collector

# Sampling with the OpenTelemetry Collector

* Latest Dynatrace
* How-to guide
* 5-min read
* Published May 28, 2024

A distributed application under heavy load may generate a massive amount of observability data. This data incurs generation, processing, transmission, and storage costs. However, it's often possible to use samplingâwhere you use only a relatively small portion of the observability data and drop the restâto reduce costs and still effectively monitor your application.

In OpenTelemetry, there are two main sampling methods:

* **Head sampling** is done within your application by the OpenTelemetry SDK, and typically involves saving a random sample of transactions.

  Head sampling is simple and effective, but it has important limitations. For example, because the sampling decision needs to be made at the start of the transaction, it can't be affected by anything that happens after that point.
* **Tail sampling** is used to make sampling decisions based on information unknown at the start of the transaction.

  In OpenTelemetry, tail sampling is typically done with the Collector by temporarily storing the full set of monitoring data until a transaction is completed. The Collector then decides to either save or drop the transaction data based on a set of sampling policies.

  Because tail sampling typically is not random, it's important to ensure that any calculated metrics are unbiased. This can be done by calculating metrics from the full set of transactions, as shown below, or from a separate, randomly sampled stream.

The following configuration example shows how to configure a Collector instance to sample trace data and import it as an OTLP request into Dynatrace. It uses the [`spanmetrics` connectorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/connector/spanmetricsconnector) to compute service metrics from traces before sampling in order to ensure their accuracy.

## Prerequisites

* One of the following Collector distributions with the [`transform`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/transformprocessor), [`filter`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/filterprocessor), and [`tail_sampling`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/tailsamplingprocessor) processors, and the [`spanmetrics`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/connector/spanmetricsconnector) connector:

  + The [Dynatrace Collector](/docs/ingest-from/opentelemetry/collector#dt-collector-dist "Learn about the Dynatrace OTel Collector.")
  + The OpenTelemetry [Contrib](/docs/ingest-from/opentelemetry/collector#collector-contrib "Learn about the Dynatrace OTel Collector.") distribution
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



tail_sampling:



# This configuration keeps errors, traces longer than 500ms, and 20% of all remaining traces.



# Adjust with policies of your choice.



policies:



- name: policy1-keep-errors



type: status_code



status_code: {status_codes: [ERROR, UNSET]}



- name: policy2-keep-slow-traces



type: latency



latency: {threshold_ms: 500}



- name: policy3-keep-random-sample



type: probabilistic



probabilistic: {sampling_percentage: 20}



decision_wait: 30s



connectors:



spanmetrics:



aggregation_temporality: "AGGREGATION_TEMPORALITY_DELTA"



namespace: "requests"



metrics_flush_interval: 15s



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: Api-Token ${env:DT_API_TOKEN}



service:



pipelines:



traces:



receivers: [otlp]



processors: [tail_sampling]



exporters: [otlp_http]



traces/spanmetrics:



receivers: [otlp]



processors: []



exporters: [spanmetrics]



metrics:



receivers: [spanmetrics]



processors: []



exporters: [otlp_http]
```

Configuration validation

[Validate your settings](/docs/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector.") to avoid any configuration issues.

## Components

For our configuration, we configure the following components.

### Receivers

Under `receivers`, we specify the standard `otlp` receiver as active receiver component for our Collector instance and configure it to accept OTLP requests on gRPC and HTTP.

### Processors

* [`tail_sampling`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/tailsamplingprocessor) to sample distributed traces based on properties of the trace.

### Connectors

Under `connectors`, we specify the [`spanmetrics` connectorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/connector/spanmetricsconnector) to compute service metrics from spans.

### Exporters

Under `exporters`, we specify the default [`otlp_http` exporterï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/exporter/otlphttpexporter) and configure it with our Dynatrace API URL and the required authentication token.

For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `Authorization`.

* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` contains the [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Service pipelines

Under `service`, we assemble three pipelines:

* `traces` assembles the OTLP receiver, tail sampling processor, and `otlp_http` exporter to send sampled spans to Dynatrace.
* `traces/spanmetrics` uses the same OTLP receiver and the `spanmetrics` connector to compute service metrics from received spans, without sampling, and forwards the computed metrics to `metrics`.
* `metrics` uses the `transform`, `filter`, and `transform/spanmetrics` processors to format metrics for Dynatrace metric ingest before sending metrics to Dynatrace using the `otlp_http` exporter.

## OpenTelemetry sampling considerations

### Mixed-mode sampling

OpenTelemetry and OneAgent use incompatible approaches to sampling that should not be mixed. If a distributed trace, which may include multiple applications and services, only partially utilizes either method, it's likely to result in inconsistent results and incomplete distributed traces. Each distributed trace should be sampled by only one of the methods to ensure it's captured in its entirety.

### Trace-derived service metrics

Dynatrace trace-derived metrics are calculated from trace data after it's ingested into Dynatrace.

If OpenTelemetry traces are sampled, the trace-derived metrics are calculated only from the sampled subset of trace data. This means that some trace-derived metrics might be biased or incorrect.

For example, a probabilistic sampler that saves 5% of traffic will result in a throughput metric that shows 5% of the actual throughput. If you use OpenTelemetry tail-based sampling to also capture 100% of slow or error traces, your service metrics will not only show incorrect throughput, but will also incorrectly bias error rates and response times.

To mitigate this, if you want to sample OpenTelemetry traces, you should calculate service metrics before sampling and use those metrics rather than the trace-derived metrics calculated by Dynatrace. If you're using the Collector for sampling, trace-derived metrics should be calculated by the Collector before applying sampling, or by the SDK. This can be done with the [`spanmetrics` connectorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/connector/spanmetricsconnector) as shown in the example above.

## Limits and limitations



Data is ingested using the OpenTelemetry protocol (OTLP) via the [Dynatrace OTLP APIs](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") and is subject to the API's limits and restrictions.
For more information see:

* [OpenTelemetry metrics limitations](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Dynatrace metrics mapping](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Ingest OpenTelemetry logs](/docs/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.")

## Related topics

* [Batch OTLP requests with the OpenTelemetry Collector](/docs/ingest-from/opentelemetry/collector/use-cases/batch "Configure the OpenTelemetry Collector to send data in batches to the Dynatrace backend.")
* [Compute histogram summaries with the OpenTelemetry Collector](/docs/ingest-from/opentelemetry/collector/use-cases/histograms "Configure the OpenTelemetry Collector to compute histogram summaries.")
* [Apply memory limits to the OpenTelemetry Collector](/docs/ingest-from/opentelemetry/collector/use-cases/memory "Configure the OpenTelemetry Collector to respect memory limits and not use excessive system resources.")
* [Send OpenTelemetry data to multiple backends](/docs/ingest-from/opentelemetry/collector/use-cases/multi-export "Configure the OpenTelemetry Collector to send data to more than one backend.")