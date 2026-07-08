---
title: OpenTelemetry Host Monitoring extension
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/extensions/opentelemetry-host-monitoring
---

# OpenTelemetry Host Monitoring extension

# OpenTelemetry Host Monitoring extension

* Extension
* Updated on Jun 15, 2026

Monitor OpenTelemetry-instrumented hosts with auto-generated entity topology, metric visualizations, and alerts for faster infrastructure analysis.

## Get started

### Overview

Monitor your hosts with OpenTelemetry using integrated metric visualizations, topology, and alerts. This extension automatically generates entities for hosts and their running processes, presenting telemetry data through intuitive interfaces designed for quick analysis. By correlating metrics, logs, and spans to host and process entities, you gain full context and a comprehensive view of your infrastructure.

### Use cases

* Track performance, health, and availability of OpenTelemetry-monitored infrastructure.
* Analyze trends and baselines for capacity planning.
* Raise alerts on resource saturation, network errors, and other infrastructure issues.
* Get a dedicated, pre-configured view for infrastructure monitoring.

### Requirements

This extension depends on telemetry data that is pushed to Dynatrace from OpenTelemetry via an [OpenTelemetry Collector](/managed/ingest-from/opentelemetry/collector "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.").

## Activation and setup

1. Deploy the OpenTelemetry Collector.

   * Follow the instructions on the [OpenTelemetry Collector](/managed/ingest-from/opentelemetry/collector/deployment "How to deploy the Dynatrace OpenTelemetry Collector.") to deploy the Collector.
   * Use the [reference configuration﻿](https://github.com/Dynatrace/dynatrace-otel-collector/blob/main/config_examples/host-metrics.yaml).
   * Ensure the Collector is running and telemetry data is reported to Dynatrace correctly.
2. Activate the OpenTelemetry Host Monitoring extension.

## Details

The [OpenTelemetry Collector](/managed/ingest-from/opentelemetry/collector "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.") captures telemetry data from your infrastructure and pushes metrics to Dynatrace via the OTel API.

The extension displays telemetry data captured by the OpenTelemetry Collector and adds Dynatrace-specific context to all signals (metrics, logs, and spans) for analysis and correlation.

For information on how to use the extension within Dynatrace, see [Monitor hosts that send OpenTelemetry data to Dynatrace](/managed/ingest-from/opentelemetry/collector/use-cases/host-monitoring "How to monitor your hosts that use Collectors to send OpenTelemetry data to Dynatrace.").

### Limitations

* The metric `system.processes.created` is currently available only on Linux and BSD operating systems.
* The metric `process.disk.io` requires running the Collector with privileged access. Not doing so will prevent the metric from being captured.

### Licensing and costs

All ingested OpenTelemetry data (logs, metrics, and spans) is charged according to your rate card, see [License Dynatrace](/managed/license "Dynatrace Platform Subscription, capability rate cards, hybrid licensing, and previous license models.") or [Dynatrace classic licensing](/managed/license/monitoring-consumption-classic "Understand how Dynatrace classic monitoring consumption is calculated, including host units, DDUs, DEM units, and Application Security units.").

The use of this extension does not itself incur any additional costs.

Based on our measurements using [the reference configuration﻿](https://github.com/Dynatrace/dynatrace-otel-collector/blob/main/config_examples/host-metrics.yaml), we estimate the following metrics ingest volume:

* Approximately 4400 metric data points per host per hour.
* Approximately 400 datapoints per process per hour.

Both these numbers will vary depending on the available metrics. For more details, see [Limitations](#limitations).

### Licensing and costs

There is no charge to use the extension. You are only charged for the data that the extension ingests.

The OpenTelemetry Host Monitoring extension ingests custom metrics, which consume [Davis Data Units (DDUs)](/managed/license/classic-licensing/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.").

Based on our measurements using [the reference configuration﻿](https://github.com/Dynatrace/dynatrace-otel-collector/blob/main/config_examples/host-metrics.yaml), we estimate the following metrics ingest volume:

* Approximately 4400 metric data points per host.
* Approximately 400 datapoints per process.

Both these numbers will vary depending on the available metrics. For more details, see [Limitations](#limitations).

Metric ingestion consumes [Davis Data Units (DDUs)](/managed/license/classic-licensing/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.") at the rate of .001 DDUs per metric data point. To calculate the approximate yearly consumption in DDUs, apply the following calculation: `<metric data points per minute> * 60 minutes * 24 hours * 365 days * 0.001`.

For logs, regular DDU consumption applies. See [DDU consumption for Log Management and Analytics](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") or [DDUs for Log Monitoring Classic](/managed/license/classic-licensing/davis-data-units/log-monitoring-consumption "Understand how the volume of DDU consumption is calculated for Dynatrace Log Monitoring Classic.").

The DDU cost above does not include any possible log events or custom events that are triggered by the extension. For more information, see [DDU events](/managed/license/classic-licensing/davis-data-units/ddu-events "Understand how to calculate Davis data unit consumption and costs related to custom-configured and custom-ingested events.").

## Feature sets

This extension does not include any feature sets. Users control what data the Collector sends to Dynatrace based on the Collector configuration.

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Monitor OpenTelemetry-instrumented hosts with auto-generated entity topology, metric visualizations, and alerts for faster infrastructure analysis.](https://www.dynatrace.com/hub/detail/opentelemetry-host-monitoring-extension/)