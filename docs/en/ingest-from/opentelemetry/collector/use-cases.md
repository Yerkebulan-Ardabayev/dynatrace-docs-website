---
title: Collector use cases
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/use-cases
scraped: 2026-02-15T21:29:24.034118
---

# Collector use cases

# Collector use cases

* Latest Dynatrace
* How-to guide
* 2-min read
* Updated on Dec 09, 2025

## Recommended configurations

When using the Collector, we recommend using the following features in the basic configuration, in addition to components specific to your use case.

* [Batching](/docs/ingest-from/opentelemetry/collector/use-cases/batch "Configure the OpenTelemetry Collector to send data in batches to the Dynatrace backend.")âto improve network performance and throughput
* [Memory Limitation](/docs/ingest-from/opentelemetry/collector/use-cases/memory "Configure the OpenTelemetry Collector to respect memory limits and not use excessive system resources.")âto avoid memory allocation related issues
* [Kubernetes Enrichment](/docs/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.")âto include Kubernetes-specific information in your requests and support data correlation in the Dynatrace backend

## Use cases

[### Batching

Configure the OpenTelemetry Collector to send data in batches to the Dynatrace backend.](/docs/ingest-from/opentelemetry/collector/use-cases/batch "Configure the OpenTelemetry Collector to send data in batches to the Dynatrace backend.")[### Enrich with OneAgent

Configure the OpenTelemetry Collector to enrich data with OneAgent.](/docs/ingest-from/opentelemetry/collector/use-cases/enrich "Configure the OpenTelemetry Collector to enrich OTLP requests.")[![FluentD](https://dt-cdn.net/images/untitled-300-c72685245e.png "FluentD")

### FluentD

Configure the OpenTelemetry Collector to ingest data from FluentD.](/docs/ingest-from/opentelemetry/collector/use-cases/fluentd "Configure the OpenTelemetry Collector to ingest FluentD data.")[### gRPC to HTTP

Configure the OpenTelemetry Collector to transform a gRPC OTLP request to HTTP.](/docs/ingest-from/opentelemetry/collector/use-cases/grpc "Configure the OpenTelemetry Collector to transform a gRPC OTLP request to HTTP.")[### Histogram summaries

Configure the OpenTelemetry Collector to compute bucket summaries for histogram metrics.](/docs/ingest-from/opentelemetry/collector/use-cases/histograms "Configure the OpenTelemetry Collector to compute histogram summaries.")[![Jaeger](https://dt-cdn.net/images/jaeger-300-3d21c8cbd4-300-2d7104a994.png "Jaeger")

### Jaeger

Configure the OpenTelemetry Collector to ingest and transform Jaeger data into Dynatrace.](/docs/ingest-from/opentelemetry/collector/use-cases/jaeger "Configure the OpenTelemetry Collector to ingest and convert Jaeger data into Dynatrace.")[### Kafka

Configure the OpenTelemetry Collector to integrate with Apache Kafka.](/docs/ingest-from/opentelemetry/collector/use-cases/kafka "Configure the OpenTelemetry Collector to ingest data via Kafka into Dynatrace.")[### Kubernetes Enrichment

Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.](/docs/ingest-from/opentelemetry/collector/use-cases/kubernetes "Configure the OpenTelemetry Collector to ingest Kubernetes data into Dynatrace.")[### Log files

Configure the OpenTelemetry Collector to ingest log files.](/docs/ingest-from/opentelemetry/collector/use-cases/filelog "Configure the OpenTelemetry Collector to ingest log data into Dynatrace.")[### Mask sensitive data

Configure the OpenTelemetry Collector to mask sensitive data before forwarding to Dynatrace.](/docs/ingest-from/opentelemetry/collector/use-cases/redact "Configure the OpenTelemetry Collector to mask sensitive data before forwarding to Dynatrace.")[### Memory Limitation

Configure the OpenTelemetry Collector to respect memory limits and not use excessive system resources.](/docs/ingest-from/opentelemetry/collector/use-cases/memory "Configure the OpenTelemetry Collector to respect memory limits and not use excessive system resources.")[### Multiple backends

Configure the OpenTelemetry Collector to export to multiple backends.](/docs/ingest-from/opentelemetry/collector/use-cases/multi-export "Configure the OpenTelemetry Collector to send data to more than one backend.")[### NetFlow

Configure the OpenTelemetry Collector to ingest NetFlow packets.](/docs/ingest-from/opentelemetry/collector/use-cases/netflow "Configure the OpenTelemetry Collector to ingest NetFlow data.")[![Prometheus](https://dt-cdn.net/images/prometheus-logo-grey-e85840f462-8e7b2967a6.svg "Prometheus")

### Prometheus

Configure the OpenTelemetry Collector to scrape your Prometheus data.](/docs/ingest-from/opentelemetry/collector/use-cases/prometheus "Configure the OpenTelemetry Collector to scrape your Prometheus data.")[### Sampling

Configure the OpenTelemetry Collector to sample distributed traces.](/docs/ingest-from/opentelemetry/collector/use-cases/sampling "Configure the OpenTelemetry Collector to sample data using the `tail_sampling` processor.")[### StatsD

Configure the OpenTelemetry Collector to ingest StatsD data.](/docs/ingest-from/opentelemetry/collector/use-cases/statsd "Configure the OpenTelemetry Collector to ingest StatsD data.")[### Syslog

Configure the OpenTelemetry Collector to ingest syslog data.](/docs/ingest-from/opentelemetry/collector/use-cases/syslog "Configure the OpenTelemetry Collector to ingest syslog data into Dynatrace.")[### Transforming and filtering

Configure the OpenTelemetry Collector to add, transform, and drop OpenTelemetry data.](/docs/ingest-from/opentelemetry/collector/use-cases/transform "Configure the OpenTelemetry Collector to add, transform, and drop OpenTelemetry data.")[![Zipkin](https://dt-cdn.net/images/zipkin-gray-300-7e572e6589.png "Zipkin")

### Zipkin

Configure the OpenTelemetry Collector to ingest and transform Zipkin data into Dynatrace.](/docs/ingest-from/opentelemetry/collector/use-cases/zipkin "Configure the OpenTelemetry Collector to ingest and convert Zipkin data into Dynatrace.")