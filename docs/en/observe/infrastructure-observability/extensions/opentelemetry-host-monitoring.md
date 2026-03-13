---
title: OpenTelemetry Host Monitoring extension
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/extensions/opentelemetry-host-monitoring
scraped: 2026-03-06T21:36:13.602335
---

# OpenTelemetry Host Monitoring extension

# OpenTelemetry Host Monitoring extension

* Latest Dynatrace
* Extension
* Updated on Mar 02, 2026

Generate topology and screens for your OpenTelemetry host data for quicker display and easier analysis of the data.

## Get started

### Overview

Monitor your hosts with OpenTelemetry using integrated metric visualizations, topology, and alerts. This extension automatically generates entities for hosts and their running processes, presenting telemetry data through intuitive interfaces designed for quick analysis. By correlating metrics, logs, and spans to host and process entities, you gain full context and a comprehensive view of your infrastructure.

### Use cases

* Track performance, health, and availability of OpenTelemetry-monitored infrastructure.
* Analyze trends and baselines for capacity planning.
* Raise alerts on resource saturation, network errors, and other infrastructure issues.
* Get a dedicated, pre-configured view for infrastructure monitoring.

### Requirements

This extension depends on telemetry data that is pushed to Dynatrace from OpenTelemetry via an [OpenTelemetry Collector](../../../ingest-from/opentelemetry/collector.md "Learn about the Dynatrace OTel Collector.").

## Activation and setup

1. Deploy the OpenTelemetry Collector.

   1. Follow the instructions on the [OpenTelemetry Collector](../../../ingest-from/opentelemetry/collector/deployment.md "How to deploy Dynatrace OTel Collector.") to deploy the Collector.
   2. Use the [reference configurationï»¿](https://github.com/Dynatrace/dynatrace-otel-collector/blob/main/config_examples/host-metrics.yaml).
   3. Ensure the Collector is running and telemetry data is reported to Dynatrace correctly.
2. Activate the OpenTelemetry Host Monitoring extension.

## Details

The [OpenTelemetry Collector](../../../ingest-from/opentelemetry/collector.md "Learn about the Dynatrace OTel Collector.") captures telemetry data from your infrastructure and pushes metrics to Dynatrace via the OTel API.

The extension displays telemetry data captured by the OpenTelemetry Collector and provides quick analysis and clear understanding of the data, adding Dynatrace-specific context to all signals (metrics, logs, and spans).

For information on how to use the extension within Dynatrace, see [Monitor hosts that send OpenTelemetry data to Dynatrace](../../../ingest-from/opentelemetry/collector/use-cases/host-monitoring.md "How to monitor your hosts that use Collectors to send OpenTelemetry data to Dynatrace.").

### Licensing and cost

All ingested OpenTelemetry data (logs, metrics, and spans) is charged according to your rate card, see [Dynatrace Platform Subscription](../../../license/capabilities.md "How different DPS capabilities work and how consumption is calculated and billed.") or [Dynatrace classic licensing](../../../license/monitoring-consumption-classic.md "Understand how Dynatrace monitoring consumption is calculated for classic licensing.").

The use of this extension does not itself incur any additional costs.

Based on our measurements using [the reference configurationï»¿](https://github.com/Dynatrace/dynatrace-otel-collector/blob/main/config_examples/host-metrics.yaml), we estimate the following metrics ingest volume:

* Approximately 4400 metric data points per host per hour.
* Approximately 400 datapoints per process per hour.

Both these numbers will vary depending on the available metrics. For more details, see [Limitations](#limitations).

### Limitations

* The metric `system.processes.created` is currently available only on Linux and BSD operating systems.
* The metric `process.disk.io` requires running the Collector with privileged access. Not doing so will prevent the metric from being captured.

## Feature sets

This extension does not include any feature sets. Users are in control of what data will be sent to Dynatrace based on the Collector configuration.

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Generate topology and screens for your OpenTelemetry host data for quicker display and easier analysis of the data.](https://www.dynatrace.com/hub/detail/opentelemetry-host-monitoring-extension/)