---
title: Extend metric observability
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-metrics
scraped: 2026-02-18T05:52:17.859280
---

# Extend metric observability

# Extend metric observability

* Latest Dynatrace
* 4-min read
* Published Feb 04, 2022

You can extend the data collected out of the box with data provided by the following frameworks and standards:

[![OpenTelemetry](https://dt-cdn.net/images/techn-icon-opentelemetry-345d0f8b0e.svg "OpenTelemetry")

### OpenTelemetry

Send OpenTelemetry metrics to Dynatrace](/docs/ingest-from/opentelemetry "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace.")[![Micrometer](https://dt-cdn.net/images/mircrometer-d91d5ac640.svg "Micrometer")

### Micrometer

Collect Micrometer metrics from JVM applications](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/micrometer "Learn how to send Micrometer metrics to Dynatrace.")[![Prometheus](https://dt-cdn.net/images/prometheus-b1fab729ac.svg "Prometheus")

### Prometheus

Send Prometheus metrics to Dynatrace](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/prometheus "Learn how to extend observability in Dynatrace with Prometheus metrics.")[![StatsD](https://dt-cdn.net/images/statsd-icon-bigger-800-72b34b3823.png "StatsD")

### StatsD

Send StatsD metrics to Dynatrace](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/statsd "Ingest metrics into Dynatrace using OneAgent and the ActiveGate StatsD client.")[![Telegraf](https://dt-cdn.net/images/techn-icon-telegraf-ba9e70e8d6.svg "Telegraf")

### Telegraf

Send Telegraf metrics to Dynatrace](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/telegraf "Ingest Telegraf metrics into Dynatrace.")[### Oracle Database

Extend your application observability into data acquired directly from your Oracle Database layer.](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/oraclesql "Learn how to extend observability in Dynatrace with declarative metrics ingested from Oracle Database.")[![Microsoft SQL Server](https://dt-cdn.net/images/techn-icon-microsoft-sqlserver-60740bd3fa.svg "Microsoft SQL Server")

### Microsoft SQL Server Database

Extend your application observability into data acquired directly from your Microsoft SQL Server layer.](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/microsoft-sql "Extend observability in Dynatrace with declarative metrics ingested from Microsoft SQL Server.")[![SNMP](https://dt-cdn.net/images/techn-icon-snmp-43de4f1139.svg "SNMP")

### SNMP

Learn how to monitor your network devices using SNMP.](/docs/ingest-from/extensions/supported-extensions/data-sources/snmp "Learn how to extend observability in Dynatrace with declarative SNMP metrics and event ingestion.")[![WMI](https://dt-cdn.net/images/techn-icon-microsoft-e15d516aaf.svg "WMI")

### WMI

Learn how to monitor your devices exposing Windows Management Instrumentation using WMI.](/docs/ingest-from/extensions/supported-extensions/data-sources/wmi "Learn how to extend observability in Dynatrace with declarative WMI metrics ingestion.")[![JMX](https://dt-cdn.net/images/techn-icon-java-3016283f6a.svg "JMX")

### JMX

Extend observability of your Java applications with JMX metrics.](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/jmx-extensions "Learn how to extend Dynatrace monitoring to include applications you've instrumented with JMX.")[### Scripting integration

Extend metric observability via Dynatrace' scripting integration.](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-pipe "Learn how to ingest metrics using local scripting integration.")[### Metric ingestion API

Extend metric observability via Dynatrace's open Metric APIs.](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api "Use the Dynatrace API to retrieve the metrics of monitored entities.")

## Access ingested metrics

You can access your ingested metrics via the Metric API v2 and in Data Explorer for custom charting.

### Metrics API

Use the [GET metric data points](/docs/dynatrace-api/environment-api/metric-v2/get-data-points "Read data points of one or multiple metrics via Metrics v2 API.") call of the Metrics API v2 to retrieve ingested data points.

### Data Explorer

Select **Create custom chart** and then select **Try it out** in the top banner. For more information, see [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.").

You can search the metric keys of all available metrics, select the metrics you want to chart, define how youâd like to analyze and chart them, and then pin your charts to a dashboard.

## Events

The custom metric ingest channel allows for ingestion of all types of metric measurements, regardless of the number of entities they relate to. The way an event is raised depends on whether there's no entity, a single entity, or multiple entities assigned to a custom metric. For more information, see [Topology awareness](/docs/dynatrace-intelligence/anomaly-detection/metric-events#topology "Learn about metric events in Dynatrace").

## Metric alerts

You can also create custom alerts based on the ingested metrics. Go to **Settings** > **Anomaly detection** > **Metric events** and select **Add metric event**. In the **Add metric event** page, search for a metric using its key and define your alert. For more information, see [Metric events for alerting](/docs/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace").

## Custom metric ingestion affects your DDU consumption

Only limited custom metric ingestion and analysis is included in out-of-the-box Dynatrace technology support. Custom metrics typically consume Davis data units, but custom metrics from OneAgent-monitored hosts are first deducted from your quota of [included metrics per host unit](/docs/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation#metrics-per-host-unit "Understand how to calculate Davis data unit consumption and costs related to monitored metrics."), so they won't necessarily consume DDUs. This applies to metrics that are assigned to a host either automatically or by adding the `dt.entity.host` dimension.

For details, see [DDUs for custom metrics](/docs/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.").

* Each ingested metric that is subject to DDU consumption (in other words, not assigned to a host) generates one or more **metric data points**. These data points consume DDUs with a weight of 0.001. Therefore, a simple metric reported once each minute for a full year will consume 526 DDUs (`525,600 minutes Ã 0.001 â 526 DDUs`).
* To check the DDU consumption of an environment, go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/) > **License** / **Subscription** > **Overview**.

### Metric dimensions also affect DDU Consumption

There are two additional factors to consider in determining which ingested metrics will consume DDUs and when:

* **Tuples**: Unique combinations of metric-dimension pairs (see examples below).

  + Metrics classic
    Each environment can support a maximum of 50,000,000 unique tuples monthly.

  + Metrics powered by Grail
    Each tuple counts toward your environment's [cardinality limit](/docs/analyze-explore-automate/metrics/limits "Reference of metrics powered by Grail").
* **Timeframe**: When the same metric is ingested with unique dimension tuples **within a 1-minute timeframe, each additional tuple results in the consumption of another metric data point.**

#### Examples

For the following examples, assume that all metrics are ingested once per minute.

* In this first example, the same distinct dimension tuple is reported twice within a one-minute interval. Therefore, only one (aggregated) data point is consumed (`1 data point Ã 0.001 DDUs`).

  ```
  cpu.temp,cpu=cpu1,cpu_type="INTEL" 55



  cpu.temp,cpu=cpu1,cpu_type="INTEL" 75
  ```
* Here two distinct dimension pairs are reported within a 1-minute interval. Therefore two data points are consumed (`2 Ã 0.001 DDUs`). From a consumption perspective, this is effectively two different metrics. A two-dimension tuple like this consumes `526 Ã 2 = 1,052` DDUs per year.

  ```
  cpu.temp,cpu=cpu1,cpu_type="INTEL" 55



  cpu.temp,cpu=cpu2,cpu_type="INTEL" 75
  ```
* Here, four distinct dimension pairs are reported within a 1-minute interval. Therefore, four data points are consumed (`4 Ã 0.001 DDUs`). From a consumption perspective, this is effectively four different metrics. A four-dimension tuple like this consumes `526 Ã 4 = 2,104` DDUs per year.

  ```
  cpu.temp,cpu=cpu1,cpu_type="INTEL" 55



  cpu.temp,cpu=cpu2,cpu_type="INTEL" 75



  cpu.temp,cpu=cpu3,cpu_type="INTEL" 55



  cpu.temp,cpu=cpu4,cpu_type="INTEL" 75
  ```

Each dimensional value (in this example, each network card) generates an individual time series within the chart. Therefore, for purposes of [calculating custom-metric consumption](/docs/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics."), each dimensional value is counted as a separate custom metric.

## Limits



The following limits apply to metric ingestion using a common ingestion channel. For API ingested metrics, if any limit is exceeded, the API call returns the **400** response code, with details in the response body.

| Entity | Limit | Description |
| --- | --- | --- |
| Metric key length, characters | 250 | The total length of the metric key, including the prefix. |
| Dimension key length, characters | 100 | The total length of the dimension key. |
| Dimension value length, characters | 250 | The total length of the dimension value. |
| Number of dimensions per line | 50 | The number of dimensions in a single line of the payload. |
| Total number of possible metric keys per environment | 100,000 | The maximum number of metric keys that can be registered in Dynatrace. |
| Number of tuples per month per metric | 1,000,000 | The maximum number of tuples (unique metric-dimension key-dimension value-payload type combinations) for each metric key for the last 30 days. |
| Number of tuples per month for all custom metrics | 50,000,000 | The maximum number of tuples (unique metric-dimension key-dimension value-payload type combinations) for all custom metrics for the last 30 days. |
| Length of line, characters | 50,000 | The maximum length of a single line of the payload. |

There's also a limit to the number of metrics that Dynatrace can ingest.

Channel

Limit

[OneAgent metric API](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api "Use the Dynatrace API to retrieve the metrics of monitored entities.")

Per minute per OneAgent instance:

OneAgent version 1.213 and earlier 1,000  
OneAgent version 1.215+ 100,000

[Metrics API v2](/docs/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Ingest custom metrics to Dynatrace via Metrics v2 API.")

There's no limit to the metric number, but [API throttling](/docs/dynatrace-api/basics/access-limit#throttling "Find out about payload limits and request throttling that may affect your use of the Dynatrace API.") applies.