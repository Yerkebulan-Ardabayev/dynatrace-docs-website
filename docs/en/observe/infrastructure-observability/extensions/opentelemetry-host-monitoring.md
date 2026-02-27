---
title: OpenTelemetry Host Monitoring extension
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/extensions/opentelemetry-host-monitoring
scraped: 2026-02-27T21:30:22.189457
---

# OpenTelemetry Host Monitoring extension

# OpenTelemetry Host Monitoring extension

* Latest Dynatrace
* Extension
* Updated on Feb 25, 2026

Generate topology and screens for your OpenTelemetry host data for quicker display and easier analysis of the data.

## Get started

### Overview

Monitor your hosts with OpenTelemetry using integrated metric visualizations, topology, and alerts. This extension automatically generates entities for hosts and their running processes, presenting telemetry data through intuitive interfaces designed for quick analysis. By correlating metrics, logs, and spans to host and process entities, you gain full context and a comprehensive view of your infrastructure.

### Requirements

This extension depends on the telemetry data that is pushed to Dynatrace from OpenTelemetry, using the [OpenTelemetry Collector](/docs/ingest-from/opentelemetry/collector "Learn about the Dynatrace OTel Collector.").

## Activation and setup

In order to use this extension, you need to:

* [Deploy the OpenTelemetry Collector](/docs/ingest-from/opentelemetry/collector/deployment "How to deploy Dynatrace OTel Collector."), following the instructions for the relevant deployment option.
* Activate this extension in Dynatrace environment to report on the metrics in context. This extension doesn't need an ActiveGate or a OneAgent.

### Use cases

* Track performance, health, and availability of OpenTelemetry-monitored infrastructure.
* Analyze trends and baselines for capacity planning.
* Raise alerts on resource saturation, network errors, and other infrastructure issues.
* Get a dedicated, pre-configured view for infrastructure monitoring.

This extension uses telemetry data collected by the OpenTelemetry Collector. To monitor the health of your Collectors, see [Collector self-monitoring](/docs/ingest-from/opentelemetry/collector/self-monitoring "How to monitor OpenTelemetry Collectors with Dynatrace dashboards.").

## Activation and setup

### Deploy the OpenTelemetry Collector

1. Follow the instructions on the [OpenTelemetry Collector](/docs/ingest-from/opentelemetry/collector/deployment "How to deploy Dynatrace OTel Collector.") to deploy the Collector.
2. Use the [reference configurationï»¿](https://github.com/Dynatrace/dynatrace-otel-collector/blob/main/config_examples/host-metrics.yaml).
3. Ensure the Collector is running and telemetry data is reported to Dynatrace correctly.

### Activate the OpenTelemetry Host Monitoring extension

Activate the OpenTelemetry Host Monitoring extension to enable [topology](#topology), [Unified Analysis screens](#screens), and [alert templates](#alert-templates).

## Details

The [OpenTelemetry Collector](/docs/ingest-from/opentelemetry/collector "Learn about the Dynatrace OTel Collector.") captures telemetry data from your infrastructure and pushes metrics to Dynatrace via the OTel API.

The extension displays telemetry data captured by the OpenTelemetry Collector and provides quick analysis and clear understanding of the data, adding Dynatrace-specific context to all signals (metrics, logs, and spans).

### Topology

This extension automatically generates topology for infrastructure monitored via the OpenTelemetry Collector. Specifically, it creates the following entity types based on metadata extracted from metrics, logs, and traces:

| Entity type | Entity ID |
| --- | --- |
| OpenTelemetry Host | dt.entity.otel:host |
| OpenTelemetry Process | dt.entity.otel:process |

These entities enable Dynatrace to correlate your metrics, logs, and spans and provide unified context across your monitored environment.

#### Enrich application telemetry

If you send your application telemetry to your local host OpenTelemetry Collector, it will automatically enrich the data with the required host attributes so that the signals are correctly attached to the OpenTelemetry Host entity.

To enrich application telemetry with the corresponding process entity, all signals (metrics, logs, and spans) need to have the `process.executable.name` resource attribute. For logs and spans to have this attribute, you need to initialize your OTel SDK with the [process resource detectorï»¿](https://opentelemetry.io/docs/languages/go/resources/).
If this is not implemented for your technology's OTel SDK, you can always set the `process.executable.name` attribute through the `OTEL_RESOURCE_ATTRIBUTES` [environment variableï»¿](https://opentelemetry.io/docs/specs/otel/configuration/sdk-environment-variables/#general-sdk-configuration).

### Screens

The extension provides screens and dashboards that display entity information, metrics, and more. The data is displayed in a smart and structured way for easier navigation and a clearer understanding of the insights.

To find a list of your OTel hosts and processes, go to ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations** > **Technologies**.

### Alert templates

This extension provides alert templates that you can use to create alerts based on the imported data. To use these templates and set up alerts:

1. Go to ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions** > **OpenTelemetry Host Monitoring** > **Extension content**.
2. Find any alert template you're interested in and select  **New Alert**.
3. Configure the alert according to the available options.

### Licensing and cost

All ingested OpenTelemetry data (logs, metrics, and spans) is charged according to your rate card, see [Dynatrace Platform Subscription](/docs/license/capabilities "How different DPS capabilities work and how consumption is calculated and billed.") or [Dynatrace classic licensing](/docs/license/monitoring-consumption-classic "Understand how Dynatrace monitoring consumption is calculated for classic licensing.").

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