---
title: OTel Collector use cases
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases
scraped: 2026-05-12T12:00:53.786681
---

# OTel Collector use cases

# OTel Collector use cases

* How-to guide
* 2-min read
* Updated on Mar 12, 2026

## Recommended configurations

When using the OTel Collector, we recommend using the following features in the basic configuration, in addition to components specific to your use case.

* [Batching](/managed/ingest-from/opentelemetry/collector/use-cases/batch "Configure the OpenTelemetry Collector to send data in batches to the Dynatrace backend.")âto improve network performance and throughput
* [Memory Limitation](/managed/ingest-from/opentelemetry/collector/use-cases/memory "Configure the OpenTelemetry Collector to respect memory limits and not use excessive system resources.")âto avoid memory allocation related issues
* [Kubernetes Enrichment](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.")âto include Kubernetes-specific information in your requests and support data correlation in the Dynatrace backend

## Use cases

[### Batching

Configure the Collector to send data in batches to the Dynatrace backend.](/managed/ingest-from/opentelemetry/collector/use-cases/batch "Configure the OpenTelemetry Collector to send data in batches to the Dynatrace backend.")[### Enrich with OneAgent

Configure the Collector to enrich data with OneAgent.](/managed/ingest-from/opentelemetry/collector/use-cases/enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with OneAgent host data.")[![FluentD](https://dt-cdn.net/images/untitled-300-c72685245e.png "FluentD")

### FluentD

Configure the Collector to ingest data from FluentD.](/managed/ingest-from/opentelemetry/collector/use-cases/fluentd "Configure the OpenTelemetry Collector to ingest FluentD data.")[### gRPC to HTTP

Configure the Collector to transform a gRPC OTLP request to HTTP.](/managed/ingest-from/opentelemetry/collector/use-cases/grpc "Configure the OpenTelemetry Collector to transform a gRPC OTLP request to HTTP.")[### Histogram summaries

Configure the Collector to compute bucket summaries for histogram metrics.](/managed/ingest-from/opentelemetry/collector/use-cases/histograms "Configure the OpenTelemetry Collector to compute histogram summaries.")[![Infrastructure observability](https://cdn.bfldr.com/B686QPH3/at/5kh38tq37h2w4qtnmbp5m889/DT0434.svg?auto=webp&width=72&height=72 "Infrastructure observability")

### Host monitoring

Monitor your hosts that send OpenTelemetry data to Dynatrace.](/managed/ingest-from/opentelemetry/collector/use-cases/host-monitoring "How to monitor your hosts that use Collectors to send OpenTelemetry data to Dynatrace.")[![Jaeger](https://dt-cdn.net/images/jaeger-300-3d21c8cbd4-300-2d7104a994.png "Jaeger")

### Jaeger

Configure the Collector to ingest and transform Jaeger data into Dynatrace.](/managed/ingest-from/opentelemetry/collector/use-cases/jaeger "Configure the OpenTelemetry Collector to ingest and convert Jaeger data into Dynatrace.")[![Infrastructure observability](https://cdn.bfldr.com/B686QPH3/at/5kh38tq37h2w4qtnmbp5m889/DT0434.svg?auto=webp&width=72&height=72 "Infrastructure observability")

### Journald

Configure the Collector to ingest systemd journal logs into Dynatrace.](/managed/ingest-from/opentelemetry/collector/use-cases/journald "Configure the OpenTelemetry Collector to ingest systemd journal logs from Linux hosts into Dynatrace.")[### Kafka

Configure the Collector to integrate with Apache Kafka.](/managed/ingest-from/opentelemetry/collector/use-cases/kafka "How to configure the OpenTelemetry Collector to buffer data via Kafka.")[### Kubernetes

Configure the Collector to enrich OTLP requests with Kubernetes data, monitor clusters, or to ingest pod logs.](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes "Configure the OpenTelemetry Collector to ingest Kubernetes data into Dynatrace.")[### Log files

Configure the Collector to ingest log files.](/managed/ingest-from/opentelemetry/collector/use-cases/filelog "Configure the OpenTelemetry Collector to ingest log data into Dynatrace.")[### Mask sensitive data

Configure the Collector to mask sensitive data before forwarding to Dynatrace.](/managed/ingest-from/opentelemetry/collector/use-cases/redact "Configure the OpenTelemetry Collector to mask sensitive data before forwarding to Dynatrace.")[### Memory limits

Configure the Collector to respect memory limits and not use excessive system resources.](/managed/ingest-from/opentelemetry/collector/use-cases/memory "Configure the OpenTelemetry Collector to respect memory limits and not use excessive system resources.")[### Multiple backends

Configure the Collector to export to multiple backends.](/managed/ingest-from/opentelemetry/collector/use-cases/multi-export "Configure the OpenTelemetry Collector to send data to more than one backend.")[### NetFlow

Configure the Collector to ingest NetFlow packets.](/managed/ingest-from/opentelemetry/collector/use-cases/netflow "Configure the OpenTelemetry Collector to ingest NetFlow data.")[![Prometheus](https://dt-cdn.net/images/prometheus-logo-grey-e85840f462-8e7b2967a6.svg "Prometheus")

### Prometheus

Configure the Collector to scrape your Prometheus data.](/managed/ingest-from/opentelemetry/collector/use-cases/prometheus "Configure the OpenTelemetry Collector to scrape your Prometheus data.")[### Sampling

Configure the Collector to sample distributed traces.](/managed/ingest-from/opentelemetry/collector/use-cases/sampling "Configure the OpenTelemetry Collector to sample data using the `tail_sampling` processor.")[### StatsD

Configure the Collector to ingest StatsD data.](/managed/ingest-from/opentelemetry/collector/use-cases/statsd "Configure the OpenTelemetry Collector to ingest StatsD data.")[### Syslog

Configure the Collector to ingest syslog data.](/managed/ingest-from/opentelemetry/collector/use-cases/syslog "Configure the OpenTelemetry Collector to ingest syslog data into Dynatrace.")[### Transform and filter

Configure the Collector to add, transform, and drop OpenTelemetry data.](/managed/ingest-from/opentelemetry/collector/use-cases/transform "Configure the OpenTelemetry Collector to add, transform, and drop OpenTelemetry data.")[![Zipkin](https://dt-cdn.net/images/zipkin-gray-300-7e572e6589.png "Zipkin")

### Zipkin

Configure the Collector to ingest and transform Zipkin data into Dynatrace.](/managed/ingest-from/opentelemetry/collector/use-cases/zipkin "Configure the OpenTelemetry Collector to ingest and convert Zipkin data into Dynatrace.")