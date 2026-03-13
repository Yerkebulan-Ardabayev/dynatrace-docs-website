---
title: OpenTelemetry Collector use cases
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/use-cases
scraped: 2026-03-06T21:32:50.601348
---

# OpenTelemetry Collector use cases

# OpenTelemetry Collector use cases

* Latest Dynatrace
* How-to guide
* 2-min read
* Updated on Mar 06, 2026

## Recommended configurations

When using the Collector, we recommend using the following features in the basic configuration, in addition to components specific to your use case.

* [Batching](use-cases/batch.md "Configure the OpenTelemetry Collector to send data in batches to the Dynatrace backend.")âto improve network performance and throughput
* [Memory Limitation](use-cases/memory.md "Configure the OpenTelemetry Collector to respect memory limits and not use excessive system resources.")âto avoid memory allocation related issues
* [Kubernetes Enrichment](use-cases/kubernetes/k8s-enrich.md "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.")âto include Kubernetes-specific information in your requests and support data correlation in the Dynatrace backend

## Use cases

[### Batching

Configure the OpenTelemetry Collector to send data in batches to the Dynatrace backend.](use-cases/batch.md "Configure the OpenTelemetry Collector to send data in batches to the Dynatrace backend.")[### Enrich with OneAgent

Configure the OpenTelemetry Collector to enrich data with OneAgent.](use-cases/enrich.md "Configure the OpenTelemetry Collector to enrich OTLP requests with OneAgent host data.")[![FluentD](https://dt-cdn.net/images/untitled-300-c72685245e.png "FluentD")

### FluentD

Configure the OpenTelemetry Collector to ingest data from FluentD.](use-cases/fluentd.md "Configure the OpenTelemetry Collector to ingest FluentD data.")[### gRPC to HTTP

Configure the OpenTelemetry Collector to transform a gRPC OTLP request to HTTP.](use-cases/grpc.md "Configure the OpenTelemetry Collector to transform a gRPC OTLP request to HTTP.")[### Histogram summaries

Configure the OpenTelemetry Collector to compute bucket summaries for histogram metrics.](use-cases/histograms.md "Configure the OpenTelemetry Collector to compute histogram summaries.")[![Infrastructure observability](https://cdn.bfldr.com/B686QPH3/at/5kh38tq37h2w4qtnmbp5m889/DT0434.svg?auto=webp&width=72&height=72 "Infrastructure observability")

### Host Monitoring extension

Monitor your hosts that send OpenTelemetry data to Dynatrace.](use-cases/host-monitoring.md "How to monitor your hosts that use Collectors to send OpenTelemetry data to Dynatrace.")[![Jaeger](https://dt-cdn.net/images/jaeger-300-3d21c8cbd4-300-2d7104a994.png "Jaeger")

### Jaeger

Configure the OpenTelemetry Collector to ingest and transform Jaeger data into Dynatrace.](use-cases/jaeger.md "Configure the OpenTelemetry Collector to ingest and convert Jaeger data into Dynatrace.")[### Kafka

Configure the OpenTelemetry Collector to integrate with Apache Kafka.](use-cases/kafka.md "How to configure the OpenTelemetry Collector to buffer data via Kafka.")[### Kubernetes Enrichment

Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.](use-cases/kubernetes.md "Configure the OpenTelemetry Collector to ingest Kubernetes data into Dynatrace.")[### Log files

Configure the OpenTelemetry Collector to ingest log files.](use-cases/filelog.md "Configure the OpenTelemetry Collector to ingest log data into Dynatrace.")[### Mask sensitive data

Configure the OpenTelemetry Collector to mask sensitive data before forwarding to Dynatrace.](use-cases/redact.md "Configure the OpenTelemetry Collector to mask sensitive data before forwarding to Dynatrace.")[### Memory Limitation

Configure the OpenTelemetry Collector to respect memory limits and not use excessive system resources.](use-cases/memory.md "Configure the OpenTelemetry Collector to respect memory limits and not use excessive system resources.")[### Multiple backends

Configure the OpenTelemetry Collector to export to multiple backends.](use-cases/multi-export.md "Configure the OpenTelemetry Collector to send data to more than one backend.")[### NetFlow

Configure the OpenTelemetry Collector to ingest NetFlow packets.](use-cases/netflow.md "Configure the OpenTelemetry Collector to ingest NetFlow data.")[![Prometheus](https://dt-cdn.net/images/prometheus-logo-grey-e85840f462-8e7b2967a6.svg "Prometheus")

### Prometheus

Configure the OpenTelemetry Collector to scrape your Prometheus data.](use-cases/prometheus.md "Configure the OpenTelemetry Collector to scrape your Prometheus data.")[### Sampling

Configure the OpenTelemetry Collector to sample distributed traces.](use-cases/sampling.md "Configure the OpenTelemetry Collector to sample data using the `tail_sampling` processor.")[### StatsD

Configure the OpenTelemetry Collector to ingest StatsD data.](use-cases/statsd.md "Configure the OpenTelemetry Collector to ingest StatsD data.")[### Syslog

Configure the OpenTelemetry Collector to ingest syslog data.](use-cases/syslog.md "Configure the OpenTelemetry Collector to ingest syslog data into Dynatrace.")[### Transforming and filtering

Configure the OpenTelemetry Collector to add, transform, and drop OpenTelemetry data.](use-cases/transform.md "Configure the OpenTelemetry Collector to add, transform, and drop OpenTelemetry data.")[![Zipkin](https://dt-cdn.net/images/zipkin-gray-300-7e572e6589.png "Zipkin")

### Zipkin

Configure the OpenTelemetry Collector to ingest and transform Zipkin data into Dynatrace.](use-cases/zipkin.md "Configure the OpenTelemetry Collector to ingest and convert Zipkin data into Dynatrace.")