---
title: Understand and manage your consumption of Infrastructure Monitoring (DPS)
source: https://docs.dynatrace.com/managed/license/capabilities/app-infra-observability/infrastructure-monitoring
---

# Understand and manage your consumption of Infrastructure Monitoring (DPS)

# Understand and manage your consumption of Infrastructure Monitoring (DPS)

* Explanation
* 1-min read
* Updated on Jun 09, 2026

Dynatrace OneAgent can be configured for Infrastructure Monitoring mode, which provides comprehensive host monitoring for physical and virtual hosts.

In addition to all features of [Foundation & Discovery](/managed/license/capabilities/app-infra-observability/foundation-and-discovery "Learn how your consumption of the Dynatrace Foundation & Discovery DPS capability is billed and charged."), Infrastructure Monitoring also includes detailed process performance metrics, disk performance metrics, process-to-process network analysis, and per process memory analysis.
Dynatrace Extensions can be enabled on hosts with Infrastructure Monitoring mode and may consume [custom metric data points](/managed/license/capabilities/app-infra-observability/infrastructure-monitoring#infra-metrics "Learn how your consumption of the Dynatrace Infrastructure Monitoring DPS capability is billed and charged.").

### Host hours

The unit of measure for calculating consumption of host monitoring in Infrastructure Monitoring mode is a host-hour.
Each instance of Dynatrace OneAgent installed and running on an operating system instance (deployed on, for example, a physical or virtual machine) with Infrastructure Monitoring mode enabled consumes host hours.
The longer that a host is monitored, the more host-hours you consume.
Consumption is independent from a host's memory size.

### Billing granularity for host-hour consumption

Dynatrace is built for dynamic cloud-native environments where hosts and services are rapidly spun up and destroyed.
Therefore, billing granularity for host-hour consumption is calculated in 15-minute intervals.
When a host is monitored for fewer than 15 minutes in an interval, host-hour consumption is rounded up to 15 minutes before consumption is calculated.

The figure below illustrates how host-hour consumption per host is calculated at 15-minute intervals.

![Infrastructure Monitoring consumption](https://cdn.bfldr.com/B686QPH3/as/4sqp5cxcncksmpsrtfr5njf9/Infrastructure_Monitoring_consumption-Light_Mode?auto=webp&format=png&position=1)

Infrastructure Monitoring consumption

### Metrics

This section assumes that you have followed the Dynatrace-recommended deployment options.
If you implement a custom deployment, the charging of included metrics may still work as described—but this is not guaranteed by Dynatrace.

Dynatrace Infrastructure Monitoring includes Infrastructure Monitoring metrics and [other built-in metrics](/managed/analyze-explore-automate/metrics-classic/built-in-metrics "Explore the complete list of built-in Dynatrace metrics.").
These metrics are included and never produce any charge.

Infrastructure Monitoring also includes a defined amount of custom metric data points.
Every host adds 1,500 custom metric data points in each 15-minute interval.
Included metric data points that are not consumed within the 15-minute interval in which they are granted do not roll over to subsequent intervals.
Your environment's included metric data points are applied automatically to metrics that originate at hosts that are monitored by OneAgent in Infrastructure Monitoring mode.
This applies to custom metrics as described in the table below.

Custom metric data points that exceed your included volume of metric data points are charged as [Custom Metrics Classic](/managed/license/capabilities/platform-extensions/custom-metrics-classic "Learn how your consumption of the Dynatrace Custom Metrics Classic DPS capability is billed and charged.").

| Origin | Examples (including but not limited to) |
| --- | --- |
| An Infrastructure-monitored host and sent via the [OneAgent metric API](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api "Use the Dynatrace API to retrieve the metrics of monitored entities.") | * OpenTelemetry metrics * Spring Micrometer * StatsD * JMX * Extensions run locally on the host by OneAgent * a host-local Telegraf |
| An Infrastructure-monitored Kubernetes node | * OpenTelemetry metrics * Spring Micrometer * JMX * [Prometheus metrics via ActiveGate](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-prometheus-metrics "Metric ingestion from Prometheus endpoints in Kubernetes, metrics alerts, and monitoring consumption.")  * This does not include Metrics sent via the Dynatrace Collector or OpenTelemetry Collector. |

Looking at Figure 2 above, the included custom metric data point volume for the four 15-minute intervals is shown below.

### Included custom metric data points calculation example

* First 15-minute interval: `1 (hosts monitored) × 1,500 (metric data points) = 1,500 Included custom metric data points`
* Second 15-minute interval: `2 (hosts monitored) × 1,500 (metric data points) = 3,000 Included custom metric data points`
* Third 15-minute interval: `1 (hosts monitored) × 1,500 (metric data points) = 1,500 Included custom metric data points`
* Fourth 15-minute interval: `1 (hosts monitored) × 1,500 (metric data points) = 1,500 Included custom metric data points`

### How custom metric data points are consumed in Infrastructure Monitoring mode

Custom metric data point consumption takes many forms.
An equal number of custom metric data points can be consumed:

* By a few high-resolution metrics or numerous low-resolution metrics.
* Equally across multiple 15-minute intervals or all at once in a single minute.
* By all Infrastructure-monitored hosts, a subset of all Infrastructure-monitored hosts, or a single infrastructure-monitored host.

## Consumption details: Infrastructure

Dynatrace provides built-in usage metrics that help you understand and analyze your organization's consumption of Infrastructure Monitoring.
To use these metrics, in ![Data Explorer](https://dt-cdn.net/images/data-explorer-512-743267b1fc.png "Data Explorer") **Data Explorer**, enter `DPS` in the **Search** field.
These metrics are also available via the Environment API and in Account Management (**Usage summary** > **Infrastructure Monitoring** > **Actions** > **View details**)
.

Here is the list of metrics you can use to monitor the consumption details for Infrastructure Monitoring.

(DPS) Infrastructure Monitoring billing usage
:   Key: `builtin:billing.infrastructure_monitoring.usage`

    Dimension: Count

    Resolution: 15 min

    Description: Total number of host hours consumed in Infrastructure Monitoring mode.

(DPS) Infrastructure Monitoring billing usage per host
:   Key: `builtin:billing.infrastructure_monitoring.usage_per_host`

    Dimension: Host (`dt.entity.host`)

    Resolution: 15 min

    Description: Consumed host hours in Infrastructure Monitoring mode per host.

(DPS) Total metric data points reported by Infrastructure hosts
:   Key: `builtin:billing.infrastructure_monitoring.metric_data_points.ingested`

    Dimension: Count

    Resolution: 15 min

    Description: Number of metric data points consumed by all Infrastructure-monitored hosts.

(DPS) Metric data points reported and split by Infrastructure hosts
:   Key: `builtin:billing.infrastructure_monitoring.metric_data_points.ingested_by_host`

    Dimension: Host (`dt.entity.host`)

    Resolution: 15 min

    Description: Number of metric data points, split by Infrastructure-monitored hosts.

(DPS) Available included metric data points for Infrastructure-monitored hosts
:   Key: `builtin:billing.infrastructure_monitoring.metric_data_points.included`

    Dimension: Count

    Resolution: 15 min

    Description: Total number of included metric data points deductible from the metric data points reported by all Infrastructure-monitored hosts.

(DPS) Consumed included metric data points for Infrastructure hosts
:   Key: `builtin:billing.infrastructure_monitoring.metric_data_points.included_used`

    Dimension: Count

    Resolution: 15 min

    Description: Number of consumed included metric data points for Infrastructure-monitored hosts.

(DPS) Total metric data points billed for Infrastructure hosts
:   Key: `builtin:billing.custom_metrics_classic.usage.infrastructure_hosts`

    Dimension: Count

    Resolution: 15 min

    Description: Number of metric data points billed for all Infrastructure-monitored hosts.

### Monitor host-hour consumption

You can monitor the total host-hour consumption for different intervals (15 min, hour, day, or week) for any selected timeframe using the "(DPS) Infrastructure Monitoring billing usage" metric.
The example below shows that 5 hosts were monitored, leading to total consumption of 5 host-hours for each hour.

![Infrastructure Monitoring (DPS)](https://dt-cdn.net/images/image011-1099-50bac22dd0.png)

Infrastructure Monitoring (DPS)

You can split the total host hour consumption using the metric "(DPS) Infrastructure Monitoring billing usage per host".
The example below shows the list of all hosts that reported consumption.

![Infrastructure Monitoring (DPS)](https://dt-cdn.net/images/image013-1099-cb1470f609.png)

Infrastructure Monitoring (DPS)

### Monitor metric consumption for Infrastructure monitored hosts

Use the metric "(DPS) Total metric data points billed for Infrastructure hosts" to monitor the number of metric data points that are billed for Infrastructure monitored hosts, as shown in the example below.

![Infrastructure Monitoring (DPS)](https://dt-cdn.net/images/image015-1101-5c4b7620a4.png)

Infrastructure Monitoring (DPS)

To manage your metrics budget, you can monitor the number of available included metric data points against the number of total consumed metrics data points using these two metrics: "(DPS) Available included metric data points for Infrastructure hosts" and "(DPS) Total metric data points reported by Infrastructure hosts".
The example below shows that more metric data points were consumed that were included with these Infrastructure monitored hosts.

![Infrastructure Monitoring (DPS)](https://dt-cdn.net/images/image017-1100-7b133be12d.png)

Infrastructure Monitoring (DPS)

You can use the metric "(DPS) Metric data points reported and split by Infrastructure hosts" to track the number of metric data points consumed per Infrastructure monitored host.
The split view helps in discovering the hosts that consume the most metric data points.
The example below shows that one of the Infrastructure monitored hosts reported significantly more metrics data points than the others.

![Infrastructure Monitoring (DPS)](https://dt-cdn.net/images/image019-1768-c4ed044b93.png)

Infrastructure Monitoring (DPS)

## Related topics

* [Dynatrace OneAgent](/managed/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.")
* [Application & Infrastructure Observability overview (DPS)](/managed/license/capabilities/app-infra-observability "Learn about the different Application & Infrastructure Observability options that are available with a Dynatrace Platform Subscription (DPS) license.")
* [Dynatrace pricing﻿](https://www.dynatrace.com/pricing/)