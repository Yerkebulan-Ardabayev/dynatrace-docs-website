---
title: Send Micrometer metrics to Dynatrace
source: https://docs.dynatrace.com/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/micrometer
---

# Send Micrometer metrics to Dynatrace

# Send Micrometer metrics to Dynatrace

* 2-min read
* Updated on Jul 23, 2026

[Micrometer﻿](https://dt-url.net/7u039ck) is an open source instrumentation framework for JVM-based application metrics. It's used by [Spring Boot﻿](https://dt-url.net/ba239ye) to record a wide range of metrics. You can ingest Micrometer and Spring Boot metrics and analyze them with Dynatrace Davis® AI end-to-end in the context of your trace, log, and diagnostics data. With Dynatrace, you get intelligent AI-based observability and automatic root cause analysis for Spring Boot, 15+ pre-instrumented JVM-based frameworks and servers, and custom metrics.

You can use Micrometer in Dynatrace to:

* Ingest pre-instrumented metrics from Spring Boot applications.
* Ingest pre-instrumented metrics from JVM-based frameworks, servers, and cache systems.
* Define and ingest custom metrics.

Metrics ingested from Micrometer consume [DDUs for custom metrics](/managed/license/classic-licensing/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.").

## Registry options

Micrometer uses the concept of a **registry** to export metrics to a monitoring system. There are two registries you can use to send Micrometer metrics to Dynatrace:

* **OTLP registry (recommended)**: Exports metrics over the OpenTelemetry Protocol (OTLP). Use this approach to standardize on OpenTelemetry across your applications or align your Micrometer metrics with other OpenTelemetry signals.
* **Dynatrace registry**: Exports metrics to the [Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.") using the [metric ingestion protocol](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol "Learn how the data ingestion protocol for Dynatrace Metrics API works."). Use this approach if your applications don't use OpenTelemetry yet.

[![OpenTelemetry](https://dt-cdn.net/images/techn-icon-opentelemetry-345d0f8b0e.svg "OpenTelemetry")

### OTLP registry (recommended)

Send Micrometer metrics using the OpenTelemetry (OTLP) registry.](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/micrometer/otlp-registry "Learn how to send Micrometer metrics to Dynatrace using the OpenTelemetry (OTLP) registry to align with the OpenTelemetry ecosystem.")[![Micrometer](https://dt-cdn.net/images/mircrometer-d91d5ac640.svg "Micrometer")

### Dynatrace registry

Send Micrometer metrics to the Dynatrace Metrics API.](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/micrometer/dynatrace-registry "Learn how to send Micrometer metrics to Dynatrace using the Dynatrace Micrometer registry.")