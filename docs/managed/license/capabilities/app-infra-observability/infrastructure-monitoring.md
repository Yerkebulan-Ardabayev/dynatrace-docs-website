---
title: Understand and manage Infrastructure Monitoring consumption (DPS)
source: https://docs.dynatrace.com/managed/license/capabilities/app-infra-observability/infrastructure-monitoring
---

# Understand and manage Infrastructure Monitoring consumption (DPS)

# Understand and manage Infrastructure Monitoring consumption (DPS)

* Explanation
* 1-min read
* Updated on Jun 01, 2026

Dynatrace Infrastructure Monitoring is a OneAgent monitoring mode that provides comprehensive host-level observability for physical and virtual machines. This page explains how Infrastructure Monitoring consumption is calculated, how to track and analyze your usage, and how to optimize your spend.

In addition to all features of [Foundation & Discovery](/managed/license/capabilities/app-infra-observability/foundation-and-discovery "Learn how your consumption of the Dynatrace Foundation & Discovery DPS capability is billed and charged."), Infrastructure Monitoring also includes detailed process performance metrics, disk performance metrics, process-to-process network analysis, and per process memory analysis.
Dynatrace Extensions can be enabled on hosts with Infrastructure Monitoring mode and may consume [custom metric data points](/managed/license/capabilities/app-infra-observability/infrastructure-monitoring#infra-metrics "Learn how Infrastructure Monitoring consumption is calculated, how to track and analyze your usage, and how to optimize your spend.").

## How consumption is calculated

Infrastructure Monitoring consumption is measured in **host hours**, using the **Infrastructure Monitoring** rate card item.

### Key terms

Host
:   An operating system instance (physical or virtual machine) on which Dynatrace OneAgent is installed and running.

Metric data point
:   A single measurement value stored in Dynatrace that belongs to a metric identified by a metric key and has a timestamp.

### Counting rules and exceptions

A host hour represents one hour of active monitoring for a single host.

Consumption is independent of the host's memory size. Each monitored host contributes one host hour per hour regardless of how much RAM it has.

### Billing granularity

Dynatrace is built for dynamic cloud-native environments where hosts and services are rapidly spun up and destroyed.
Therefore, billing granularity for host-hour consumption is calculated in 15-minute intervals.
When a host is monitored for fewer than 15 minutes in an interval, host-hour consumption is rounded up to 15 minutes before consumption is calculated.

The figure below illustrates how host-hour consumption per host is calculated at 15-minute intervals.

![Infrastructure Monitoring consumption example](https://dt-cdn.net/images/infrastructure-monitoring-consumption-light-mode-3840-23a7d10898.png)

Infrastructure Monitoring consumption example

### Bundled functionality

This section assumes that you have followed the Dynatrace-recommended deployment options.
If you implement a custom deployment, the charging of included metrics may still work as described—but this is not guaranteed by Dynatrace.

Use of Infrastructure Monitoring metrics and [other built-in metrics](/managed/analyze-explore-automate/metrics-classic/built-in-metrics "Explore the complete list of built-in Dynatrace metrics.") is included at no additional cost on Infrastructure Monitoring-enabled hosts.

Every host also includes 1,500 custom metric data points in each 15-minute interval. Unused custom metric data points don't roll over to subsequent intervals.

Included metric data points are applied automatically to metrics that originate at hosts that are monitored by OneAgent in Infrastructure Monitoring mode. This applies to custom metrics as described in the table below.

Custom metric data points that exceed your included volume of metric data points are charged as [Custom Metrics Classic](/managed/license/capabilities/platform-extensions/custom-metrics-classic "Learn how your consumption of the Dynatrace Custom Metrics Classic DPS capability is billed and charged.").

| Origin | Examples (including but not limited to) |
| --- | --- |
| An Infrastructure-monitored host and sent via the [OneAgent metric API](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api "Use the Dynatrace API to retrieve the metrics of monitored entities.") | * OpenTelemetry metrics * Spring Micrometer * StatsD * JMX * Extensions run locally on the host by OneAgent * a host-local Telegraf |
| An Infrastructure-monitored Kubernetes node | * OpenTelemetry metrics * Spring Micrometer * JMX * [Prometheus metrics via ActiveGate](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-prometheus-metrics "Metric ingestion from Prometheus endpoints in Kubernetes, metrics alerts, and monitoring consumption.")  * This doesn't include Metrics sent via the Dynatrace Collector or OpenTelemetry Collector. |

#### Included custom metric data points calculation example

* First 15-minute interval: `1 (hosts monitored) × 1,500 (metric data points) = 1,500 included custom metric data points`
* Second 15-minute interval: `2 (hosts monitored) × 1,500 (metric data points) = 3,000 included custom metric data points`
* Third 15-minute interval: `1 (hosts monitored) × 1,500 (metric data points) = 1,500 included custom metric data points`
* Fourth 15-minute interval: `1 (hosts monitored) × 1,500 (metric data points) = 1,500 included custom metric data points`

Custom metric data point consumption takes many forms.
An equal number of custom metric data points can be consumed:

* By a few high-resolution metrics or numerous low-resolution metrics.
* Equally across multiple 15-minute intervals or all at once in a single minute.
* By all Infrastructure-monitored hosts, a subset of all Infrastructure-monitored hosts, or a single infrastructure-monitored host.

## Track your consumption

Dynatrace provides various options to help you understand and analyze your organization's consumption of Infrastructure Monitoring.

### Insights via Account Management

License managers can view usage and costs in [**Account Management**﻿](https://myaccount.dynatrace.com/).

![Cost and usage details for Infrastructure Monitoring](https://dt-cdn.net/images/screenshot-2026-06-11-at-15-48-1822-293540e773.png)

Cost and usage details for Infrastructure Monitoring

1. Go to [**Account Management**﻿](https://myaccount.dynatrace.com/) > **Subscription** > **Overview** > **Cost and usage details** > **Usage summary**.
2. Select the **Infrastructure Monitoring** capability.
3. From this screen, you can also drill down into usage detail on the capability and environment level.

   * Capability level: Select **View Details** next to the capability you want to explore.
   * Environment level: In the **Environments** table, select **…** > **Open details with Notebooks**.

For more information, see [Overview (Dynatrace Platform Subscription)](/managed/manage/account-management/license-subscription/subscription-overview-dps "View your Dynatrace Platform Subscription (DPS) budget summary and cost analysis.").

## Optimize your consumption

### Configuration best practices

* Monitor your included custom metric budget. Each host includes 1,500 custom metric data points per 15-minute interval. If extensions or custom instrumentation regularly generate more, review whether all metrics are required and consider removing low-value metrics.
* Audit host inventory regularly. Look for decommissioned hosts, duplicate OneAgent instances, or hosts that are auto-scaled down and no longer active. Removing inactive hosts immediately stops consumption.

### Ongoing optimization

* Use the `builtin:billing.infrastructure_monitoring.metric_data_points.ingested_by_host` metric to identify high-consuming hosts and correlate with their business value.
* Disable OneAgent on idle non-production hosts (for example, staging environments outside working hours) to avoid paying for unused monitoring.
* Review Dynatrace Extensions running on Infrastructure Monitoring hosts. Each extension can generate custom metric data points. Disable extensions that no longer provide value.

### Automation

You can use Dynatrace to automate some of your optimization efforts:

* Anomaly alerts: Get notified of unexpected spikes in Infrastructure Monitoring host-hour consumption. To do this, set up [Cost Monitors](/managed/manage-your-costs/control/cost-monitors "Learn how to use the Cost Monitors feature to make forecasts and cost events.") in [**Account Management**﻿](https://myaccount.dynatrace.com/).
* Scheduled reports: Deliver automated consumption reports to stakeholders on a regular cadence. To do this, use ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** and ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**.
* Remediation workflows: Automatically respond to cost threshold events, such as disabling non-critical hosts when a budget limit is reached. To do this, use [AutomationEngine](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").

## FAQs

### Is Infrastructure Monitoring consumption affected by host memory size?

No. Host-hour consumption is independent of host memory size. Each monitored host contributes one host hour per hour of monitoring regardless of how much RAM it has. This is different from Full-Stack Monitoring, which scales with memory.

### How does Infrastructure Monitoring compare to Foundation & Discovery?

Both use host hours as the unit of measure, but Infrastructure Monitoring provides significantly deeper observability:

* Foundation & Discovery: Basic host health, OS service status, topology and process discovery. No custom metrics. Lower cost per host hour.
* Infrastructure Monitoring: Everything in Foundation & Discovery, plus detailed process performance metrics, disk performance, network traffic analysis, per-process memory analysis, and 1,500 included custom metric data points per host per 15 minutes.

### What happens if my custom metric data points exceed the included quota?

Data points beyond the 1,500 per host per 15-minute interval are billed as [Custom Metrics Classic](/managed/license/capabilities/platform-extensions/custom-metrics-classic "Learn how your consumption of the Dynatrace Custom Metrics Classic DPS capability is billed and charged.").

* Use `builtin:billing.infrastructure_monitoring.metric_data_points.included` and `builtin:billing.infrastructure_monitoring.metric_data_points.ingested` to stay within budget.
* Use `builtin:billing.infrastructure_monitoring.metric_data_points.ingested_by_host` to identify which hosts are the source of the overage.

### How does billing granularity work?

Consumption is calculated in 15-minute intervals. If a host is monitored for fewer than 15 minutes in a given interval, its consumption is rounded up to 15 minutes. This ensures short-lived cloud instances are billed accurately.

### Does Infrastructure Monitoring include log ingestion?

OneAgent automatically ingests logs in all monitoring modes, including Infrastructure Monitoring. However, log ingestion doesn't consume Infrastructure Monitoring host hours; it is billed separately as [Log Management and Analytics](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").

### Can I run Dynatrace Extensions with Infrastructure Monitoring?

Yes. Dynatrace Extensions can be enabled on Infrastructure Monitoring hosts. Extensions may generate custom metric data points, which are counted against the 1,500 included data points per host per 15-minute interval. Any excess is billed separately.

## Related topics

* [Dynatrace OneAgent](/managed/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.")
* [Application & Infrastructure Observability overview (DPS)](/managed/license/capabilities/app-infra-observability "Learn about the different Application & Infrastructure Observability options that are available with a Dynatrace Platform Subscription (DPS) license.")
* [Dynatrace pricing﻿](https://www.dynatrace.com/pricing/)