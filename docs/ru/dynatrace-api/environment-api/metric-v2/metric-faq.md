---
title: Metrics API - FAQ
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/metric-v2/metric-faq
scraped: 2026-02-25T21:26:23.394027
---

# Metrics API - FAQ

# Metrics API - FAQ

* Reference
* Updated on Nov 16, 2022

## Metric query

Why is the last timestamp of the result in the future?

In Dynatrace, metric data points are stored in time slots of different resolutions. The finest granularity of a time slot is one minute.
The timestamps returned by the metrics query endpoint are the *end times* of these time slots.

For example, if the current time is 09:24 a.m. and you query the last 6 hours at a 1-hour resolution, the timestamp of the last data point will be today at 10:00 a.m. For details, see [Timeframe note](/docs/dynatrace-api/environment-api/metric-v2/get-data-points#timeframe-note "Read data points of one or multiple metrics via Metrics v2 API.").

Why do the returned values grow larger for a larger timeframe?

The data points returned by the query endpoint are time-aggregated. Depending on the query timeframe, the resolution of the data points may be minutes, hours, days, or even years. If you query a larger timeframe, the resolution of your data is likely to be coarser, causing greater values for aggregations such as `sum` or `count`.

If you want to have comparable results for different resolutions, use the [**rate** transformation](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#rate "Configure the metric selector for the Metric v2 API."). For example, `:rate(1m)` provides you with the value per minute.

Why is the value of a percentage metric greater than 100% when a fold is used?

For example, the following query might return values higher than 100% even though the metric's unit is `Percent`.

```
builtin:host.availability:splitBy():avg:fold
```

The root cause of this problem is that, when you apply an [**aggregation** transformation](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#aggregation "Configure the metric selector for the Metric v2 API.") (by calling `:avg` in the example above), the semantics of the metric are lost and unavailable for transformations that occur later in the transformation chain. That is, when the [**fold** transformation](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#fold "Configure the metric selector for the Metric v2 API.") is called, the information that the values should be averaged is no longer available, and the aggregation `sum` is applied instead.

To prevent this issue, do not perform an aggregation before a fold transformation.

```
builtin:host.availability:splitBy():fold
```

Why is the value of a dimension null?

If a [top x](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#remainder "Configure the metric selector for the Metric v2 API.") is applied to a dimension of a metric, only *x* dimension values are retained. All other dimension values are booked into the `remainder` dimension, which has the value `null`.

How can I get pretty names for monitored entities?

By default, the query response only contains the IDs of the monitored entities (for example, `HOST-E1784F5E3F9987CD`).

If you want to have the entity name in the response as well, you need to use the [**names** transformation](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#names "Configure the metric selector for the Metric v2 API."). The pretty name is then available in the `dimensionMap` under the dimension key `dt.entity.<entityType>.name` for example, `dt.entity.host.name`).

Why is the result of my metric expression empty?

There are multiple reasons why a metric expression could yield an empty result:

* The dimension keys of the metrics used in the expression do not match.

  If you have metrics with different dimension keys, you need to align the dimensions of the metrics to make a calculation possible. You can use either the [**split by**](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#splitby "Configure the metric selector for the Metric v2 API.") or [**merge**](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#merge "Configure the metric selector for the Metric v2 API.") transformation for this purpose. Consider this query:

  ```
  builtin:host.cpu.iowait



  /



  builtin:host.disk.throughput.read
  ```

  It will produce the `Metric expression contains non-matching dimension-keys.` error, because the **builtin:host.cpu.iowait** metric has only one dimension (**dt.entity.host**), while **builtin:host.disk.throughput.read** has two (**dt.entity.host** and **dt.entity.disk**). To make the query work, you need to get rid of the disk dimension (for example, by using the **merge** transformation).

  ```
  builtin:host.cpu.iowait



  /



  builtin:host.disk.throughput.read:merge(dt.entity.disk)
  ```
* The dimension values do not match.

  For example, the following expression will deliver an empty result because different dimension values cannot be joined.

  ```
  builtin:host.cpu.iowait:filter(eq(dt.entity.host,HOST-001))



  /



  builtin:host.cpu.iowait:filter(eq(dt.entity.host,HOST-002))
  ```

  The solution in this case is to drop the dimensions completely using the [**splitBy** transformation](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#splitby "Configure the metric selector for the Metric v2 API.").

  ```
  builtin:host.cpu.iowait:filter(eq(dt.entity.host,HOST-001)):splitBy()



  /



  builtin:host.cpu.iowait:filter(eq(dt.entity.host,HOST-002)):splitBy()
  ```

  One more reason why there are no matching tuples: applying a [**limit** transformation](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#limit "Configure the metric selector for the Metric v2 API.") to an operand of the expression may cause matching dimensions to be filtered out. **Always** apply the **limit** transformation to the result of an expression and not to its operands.

  Consider the following query, which attempts to add top-10 CPU usage times to top-10 CPU idle times.

  ```
  builtin:host.cpu.usage:sort(value(avg,descending)):limit(10)



  +



  builtin:host.cpu.idle:sort(value(avg,descending)):limit(10)
  ```

  If you have a large environment with hundreds of hosts, it is unlikely that the 10 hosts with the highest CPU usage are among the 10 hosts with the highest CPU idle time. The operands won't have matching tuples, therefore the result of the expression will be empty. The solution is to apply the limit to the result of the expression instead:

  ```
  (



  builtin:host.cpu.usage



  +



  builtin:host.cpu.idle



  )



  :sort(value(auto,descending))



  :limit(10)
  ```
* There is no data for a metric.

  Consider this example of a ratio expression, where we calculate the error ratio for key user actions:

  ```
  builtin:apps.other.keyUserActions.reportedErrorCount.os



  /



  builtin:apps.other.keyUserActions.requestCount.os
  ```

  If there are many requests but not a single error in your timeframe, the result will be empty, though an error ratio of `0` would be more meaningful. You can achieve that with the `default(0)` transformation:

  ```
  builtin:apps.other.keyUserActions.reportedErrorCount.os:default(0)



  /



  builtin:apps.other.keyUserActions.requestCount.os
  ```

Why can I apply an aggregation that the metric does not support?

After performing a space aggregation using the [**split by**](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#splitby "Configure the metric selector for the Metric v2 API.") or [**merge**](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#merge "Configure the metric selector for the Metric v2 API.") transformation, you can apply arbitrary aggregations to the result.

For example, you can run the following query even though the metric does not natively support percentiles.

```
builtin:host.cpu.user:splitBy("dt.entity.host"):percentile(50)
```

However, because the metric has only one dimension (**dt.entity.host**), no values are in fact space-aggregated. Consequently, the `percentile(50)` aggregation will deliver the same result as `percentile(99)`, because the percentile estimation is based on only one data point in this case.

## Metric ingest



Why is my ingested data point unavailable?

There are multiple reasons why a data point could be unavailable. Try the following solutions.

* Make sure that you receive a response with the `202` HTTP status code for the ingest endpoint.
* It may take a couple of minutes until an ingested data point becomes available via the Metrics REST API and in [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."). The solution is to wait.
* Use the **Metric & Dimension Usage + Rejections** dashboard to check whether the data point was rejected at a later stage. A data point could be accepted by the ingestion endpoint, but later rejected because an invariant was broken.
* Check the filters you're using. The data point may be filtered out by a management zone or a timeframe filter.

Why are my metric keys suffixed with '.count' or '.gauge'?

Metrics with different [payload types](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#payload "Learn how the data ingestion protocol for Dynatrace Metrics API works.") cannot share the same key. Therefore:

* `count` metrics are automatically suffixed with `.count` unless their metric key already ends with `.count` or `_count`
* `gauge` metrics are automatically suffixed with `.gauge` if their key ends with `.count` or `_count`

Why is the metadata of my metric not updated?

You can write the metadata of a metric via the [ingestion protocol](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#metadata "Learn how the data ingestion protocol for Dynatrace Metrics API works.") only if *it has not been set before*. To update the metric metadata, you need to use the [metric browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser#metadata "Browse metrics with the Dynatrace metrics browser.").

Why is an ingested dimension missing?

If you ingest a dimension with an empty value, the whole dimension tuple is dropped at ingestion time. For instance, if you ingest `myMetric,dimEmpty="" 1`, the dimension `dimEmpty` is removed.