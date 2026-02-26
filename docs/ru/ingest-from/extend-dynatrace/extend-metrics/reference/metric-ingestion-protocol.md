---
title: Metric ingestion protocol
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol
scraped: 2026-02-26T21:28:07.076552
---

# Metric ingestion protocol

# Metric ingestion protocol

* Latest Dynatrace
* 6-min read
* Updated on Jul 08, 2025

This page describes the protocol for metric ingestion in Dynatrace.

## Syntax

The general syntax of metric ingestion is the following:

```
metric.key,dimensions payload
```

### Metric key Required

The key of the metric you're submitting. It consists of sections, separated by dots, for example `first.second.third`.

Allowed characters are lowercase and uppercase letters, numbers, hyphens (`-`), and underscores (`_`). The following restrictions apply:

* Non-latin letters (like `Ã¶`) are not allowed.
* Metric keys cannot start with a number or a hyphen (`-`).
* Sections cannot start with a hyphen (`-`).
* The length of the key must be in range from 3 to 255 characters.

The metric key ends either at the first comma (if you're specifying dimensions) or at the first whitespace (if you omit dimensions).

Your provided key may be suffixed automatically depending on the payload. For details, see [Payload](#payload).

Avoid sections with non-alphabetical characters. You will need to escape these characters in the [metric selector](/docs/dynatrace-api/environment-api/metric-v2/metric-selector "Configure the metric selector for the Metric v2 API.") when you [query your metric](/docs/dynatrace-api/environment-api/metric-v2/get-data-points "Read data points of one or multiple metrics via Metrics v2 API.").

### Dimension Optional

If you want to omit dimensions, provide the payload right after the metric key, separated by a whitespace.

Dimensions are specified as `key="value"` pairs. You can specify up to 50 dimensions, separated by commas (`,`).

Allowed characters for the key are lowercase letters, numbers, hyphens (`-`), periods (`.`), colons (`:`) and underscores (`_`). Special letters (like `Ã¶`) are not allowed. The key can be in the `key.key-section` format.

Pass the dimension value as a quoted string. If you want to pass quotes (`"`) and/or backslashes (`\`) in a dimension value, make sure you escape them with a backslash (`\`). For example:

```
workHours,team="devops\\bugfixing",project="\"product\"_improvement" 1000
```

Currently we support only one dimension value per dimension key. If the same dimension key is specified multiple times in a single payload (for example, `ipaddress="192.168.100.1",ipaddress="10.0.0.1"`) the payload is valid, but only one value is accepted.

#### Dynatrace reserved dimensions

The `dt.entity.<entity_type>` key is a Dynatrace reserved dimension key that relates the metric to the monitored entity provided as dimension value (for example, the `dt.entity.host=HOST-06F288EE2A930951` dimension maps the data points to the host with the ID of **HOST-06F288EE2A930951**).

### Payload Required

The general format of the payload is the following:

```
format,dataPoint timestamp
```

#### Format Optional

You can specify a payload in two formats: gauge (`gauge`) or count value (`count`). Specify the format before you specify data points and separate it from data points with a comma (for example `gauge,80.6`).

A metric key can only refer to one payload type with Classic metrics. Thus, your provided metric key is automatically suffixed with `.count` for the payload type `count` unless the key already ends with `.count`. Vice versa, if the key of a metric with type gauge ends with `.count`, it is suffixed with `.gauge`.

Grail metrics do not apply the `.count` and `.gauge` suffixes.

gauge

count

For the gauge format, you can specify the following statistic summaries:

* `min`
* `max`
* `sum`
* `count`âthe number of measurements included in the data point.

You can omit the format if you're using a single value gauge payload. In that case, the provided value is used for all summaries and the count is set to `1`.

For example, a payload of `80.6` equals `gauge,min=80.6,max=80.6,sum=80.6,count=1`.

Usage of the count format will automatically create a new metric with the `your-metric-key.count` key. To specify the count value, you must provide the delta field: `count,delta=500`.

Data points of the `count` type are **deltas** between the previous and current data points. For example, if the initial data point has the value of `500` and the second data point has the value of `1,000`, the actual stored value at the timestamp of the second data point is `1,500`.

#### Data point Required

A data point might include one or, in the case of the gauge format, several measures. For several measures, provide them with statistic summaries. You must specify all the summaries.

A data point of the `count` type is the **delta** between the previous and current data points.

#### Timestamp Optional

The format of the timestamp is UTC milliseconds. The allowed range is between **1 hour** into the past and **10 minutes** into the future from now. Data points with timestamps outside of this range are rejected.

If no timestamp is provided, **the current timestamp of the server** is used.

### Metadata Optional

You can provide custom metric metadata via the ingestion protocol. The ingestion protocol supports only creation of metadata. If metadata for the same metric is specified several times in the payload, only the first occurrence is used. To view or update metadata, use either [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser.") or the Settings API (to learn how to compose an API payload, see [Set metric metadata](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/custom-metric-metadata#create "Provide metadata for your custom metric.")).

```
#metric.key <payload-format> dt.meta.<property>="<value>"
```

Set either `gauge` or `count` in place of `<payload-format>`. Usage of the count format will automatically create a new metric with the `metric-key.count` key.

The following properties are available. To specify several properties, separate them with a comma (`,`).

## Examples

The general syntax of metric ingestion is the following:

```
metric.key,dimensions payload



#metric.key <payload-format> dt.meta.<property1>="<value>", dt.meta.<property2>="<value>"
```

### Dimensions

Here's an example of a metric using multiple dimensions, `team` and `businessapp` that describe the reported datapoints.

```
mymetric,team=teamA,businessapp=hr 1000
```

Here's the same example with the timestamp of the data point.

```
mymetric,team=teamA,businessapp=hr 1000 1609459200000
```

### GAUGE metric

Gauge is the default data, so you can keep the data type optional in case you want to send gauge values:

```
cpu.temperature,hostname=hostA,cpu=1 55



cpu.temperature,hostname=hostA,cpu=2 45
```

Here's an example with the `gauge` data type used nonetheless.

```
cpu.temperature,hostname=hostA,cpu=1 gauge,45
```

You can also provide consolidated information about multiple datapoints recorded on the client side before sending it to Dynatrace. In the example below, 2 datapoints are summarized and the minimum, maximum, sum value and number of datapoints are sent in a single line.

```
cpu.temperature,hostname=hostA,cpu=1 gauge,min=17.1,max=17.3,sum=34.4,count=2
```

You can also relate measurements to existing host entities by making use of the `dt.entity.host` reserved dimension key.

```
cpu.temperature,dt.entity.host=HOST-4587AE40F95AD90D,cpu=1 gauge,min=17.1,max=17.3,sum=34.4,count=2
```

You don't need to specify the `dt.entity.host` dimension when using local ingestion methods via OneAgent, that is [dynatrace\_ingest](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-pipe "Learn how to ingest metrics using local scripting integration.") and [local API](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api "Use the Dynatrace API to retrieve the metrics of monitored entities."), because for this ingestion methods, the host context is added automatically.

### COUNT metric

For a count type of metric, the delta is calculated and provided by the client that sends the metric to Dynatrace, which in the case below represents new users reported by region.

```
new_user_count,region=EAST count,delta=50



new_user_count,region=WEST count,delta=150
```

### Create metadata

Here's an example of providing metadata for a `cpu.temperature` metric.

```
#cpu.temperature gauge dt.meta.unit=count,dt.meta.description="The temperature of the CPU",dt.meta.displayname="CPU temperature"
```

### API call

See [POST ingest data points](/docs/dynatrace-api/environment-api/metric-v2/post-ingest-metrics#example "Ingest custom metrics to Dynatrace via Metrics v2 API.") for an example API call.

## Related topics

* [Metrics API - POST ingest data points](/docs/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Ingest custom metrics to Dynatrace via Metrics v2 API.")