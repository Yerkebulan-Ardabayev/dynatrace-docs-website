---
title: Buffer data via Kafka with OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/kafka
scraped: 2026-05-12T12:10:52.144934
---

# Buffer data via Kafka with OTel Collector

# Buffer data via Kafka with OTel Collector

* Explanation
* 1-min read
* Updated on May 04, 2026

When you use Apache Kafka as the transport layer for OTLP, you add durability, scale, and flexibility to your observability pipelines.

Kafka decouples producers (OTel Collector agents) from consumers (Collector gateways).
This helps to:

* Absorb traffic spikes with persistent buffering.
* Survive network and backend failures.
* Enable fan-out to multiple downstream systems.

You can reliably perform the necessary enrichment on high-volume, bursty telemetryâall while keeping your data streams protected.

## Overview

You can configure Kafka exporter, Kafka receiver, and Kafka Metrics receiver components, as shown in the figure below.

* Exporter: Write OTLP data as Kafka messages on a per-signal basis (`otlp_logs`, `otlp_metrics`, `otlp_spans`).
* Receiver: Consume traces, metrics, and logs from Apache Kafka topics, and then forward these to backends such as Dynatrace.
* Kafka metrics receiver: Collect Kafkaâs own operational metrics (for example, `broker count`) via OTLP and export them to Dynatrace.

Note that running Kafka may introduce additional end-to-end latencies, operational overhead, and potential bottlenecks.

![Communication between OTel Collector and Kafka server](https://cdn.bfldr.com/B686QPH3/as/8zmzr8jx66vpjsjxqkhg8jw/OpenTelemetry_-_Configuring_Kafka_exporter_receiver_and_Metrics_receiver_components_-_Light_Mode?auto=webp&format=png&position=1)

Communication between OTel Collector and Kafka server

## Configuration

Configure your Collectors to start sending data to/from Kafka and the Dynatrace backend.

[### Exporter

Configure the Collector to export OTLP data to Kafka server.](/managed/ingest-from/opentelemetry/collector/use-cases/kafka/exporter "How to configure the OpenTelemetry Collector to forward OpenTelemetry data with the Kafka exporter.")[### Receiver

Configure the Collector to receive OTLP data from Kafka server.](/managed/ingest-from/opentelemetry/collector/use-cases/kafka/receiver "How to configure the OpenTelemetry Collector's Kafka receiver to ingest OpenTelemetry from Kafka.")[### Kafka Metrics Receiver

Configure the Collector to collect Kafka operational metrics and export them to Dynatrace.](/managed/ingest-from/opentelemetry/collector/use-cases/kafka/kafkametrics "How to configure the OpenTelemetry Collector to gather metrics from your Kafka server.")

## Related topics

* [OTel Collector for ingesting telemetry into Dynatrace](/managed/ingest-from/opentelemetry/collector "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
* [Forward OpenTelemetry data with the Kafka exporter](/managed/ingest-from/opentelemetry/collector/use-cases/kafka/exporter "How to configure the OpenTelemetry Collector to forward OpenTelemetry data with the Kafka exporter.")
* [Receive OpenTelemetry data with the Kafka receiver](/managed/ingest-from/opentelemetry/collector/use-cases/kafka/receiver "How to configure the OpenTelemetry Collector's Kafka receiver to ingest OpenTelemetry from Kafka.")
* [Monitor Kafka with OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/kafka/kafkametrics "How to configure the OpenTelemetry Collector to gather metrics from your Kafka server.")