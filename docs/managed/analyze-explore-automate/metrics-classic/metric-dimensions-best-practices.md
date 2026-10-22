---
title: Best practices for metric dimensions and cardinality
source: https://docs.dynatrace.com/managed/analyze-explore-automate/metrics-classic/metric-dimensions-best-practices
---

# Best practices for metric dimensions and cardinality

# Best practices for metric dimensions and cardinality

* Best practices
* 5-min read
* Updated on Oct 15, 2026

Use these practices to keep your metric dimensions useful and your environment within its cardinality limits. These practices apply to every metric you ingest, and following them keeps queries fast and prevents Dynatrace from rejecting data points.

[**Choose only the dimensions you need**](#think-about-the-dimensions-you-need)[**Avoid volatile dimensions**](#avoid-volatile-dimensions)[**Stay within cardinality limits**](#avoid-high-cardinality-limits)[**Monitor dimension usage**](#identify-high-cardinality-situations)[**Investigate high-cardinality metrics**](#investigate-high-cardinality-metrics)[**Block dimensions you don't need**](#metric-dimension-block-list)

## Choose only the dimensions you need

Add only the dimensions you need to filter and aggregate by at query time, because every distinct combination of dimension values counts against your cardinality limits. Dimensions enrich a metric with context, such as where the metric was measured. You can see your dimensions when using the [metric ingestion protocol](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol "Learn how the data ingestion protocol for Dynatrace Metrics API works.").

A combination of dimension values is called a **dimension tuple**.

The following example creates a metric with two dimensions, `host.name` and `owner`.

```
cpu.temperature, host.name="Alice's PC",           owner="Alice"  gauge,50 1699625420



cpu.temperature, host.name="Alice's Raspberry Pi", owner="Alice"  gauge,40 1699625420



cpu.temperature, host.name="Bob's PC",             owner="Bob"    gauge,60 1699625420
```

The data above creates the following dimension tuples.

```
(host.name="Alice's PC",           owner="Alice")



(host.name="Alice's Raspberry Pi", owner="Alice")



(host.name="Bob's PC",             owner="Bob")
```

## Avoid volatile dimensions

Avoid short-lived IDs and timestamps as dimension values, because volatile dimensions can produce unintended results, increase costs, and slow query performance. If a dimension value is a universally unique identifier, epoch timestamp, or numeric value, consider whether it's truly necessary for your use case.

The following example is a common misconfiguration using syntax from the metric ingestion protocol.

```
cpu.temperature, host.name="Alice's PC", measured_at="1699625420"  gauge,50 1699625420



cpu.temperature, host.name="Alice's PC", measured_at="1699625421"  gauge,50 1699625421



cpu.temperature, host.name="Alice's PC", measured_at="1699625422"  gauge,49 1699625422



cpu.temperature, host.name="Alice's PC", measured_at="1699625423"  gauge,49 1699625423
```

The dimension `measured_at` uses an epoch timestamp to track when the data was measured.

* The `measured_at` dimension is unnecessary, because each data point already carries its timestamp.
* Because `measured_at` creates a new dimension tuple with every data point, the metric reaches the per-metric limit after 1,000,000 seconds online, which is about 11 days.

## Stay within cardinality limits

Plan your dimensions around the cardinality limits, because once a limit is reached, data points with new, unseen dimension tuples are rejected. A cardinality limit is a limit on the number of dimension tuples you can ingest, and Dynatrace enforces these limits to mitigate the effects of volatile dimensions.

Metrics have the following dimension tuple limits:

| Limit | Value | Note |
| --- | --- | --- |
| Built-in metric pool dimension limit | 20 million | Shared dimension tuple space for all built-in metrics |
| Custom metric pool dimension limit | 50 million | Shared dimension tuple space for all custom metrics, such as Prometheus metrics |
| Per-metric dimension limit | 1,000,000 | Separate dimension tuple limit for each metric, built-in or custom |

The limits are applied against the dimension tuples of the last 30 days (a 30-day sliding window). The limits apply to the environment.

## Monitor dimension usage

Check your dimension tuple usage, because spotting a metric that approaches a limit lets you act before data points are rejected. Self-monitoring metrics show the current dimension tuple space usage. You can find them on the **Metric dimension usage and rejection self-monitoring** dashboard, which contains the following tiles:

* **Custom metric dimensions usage**

  The share of the 50 million custom metric dimension tuple limit used in the last 30 days. For example, `0.87%` is about 435,000 dimension tuples.
* **Builtin metric dimensions usage**

  The share of the 20 million built-in metric dimension tuple limit used. For example, `1.68%` is about 336,000 dimension tuples.
* **Highest metric dimensions usage**

  Individual metrics that use more than 50 percent of the per-metric limit.
* **High-cardinality dimensions**

  The dimensions with the highest cardinality for your metrics in the last 30 days. The tile includes only dimensions with a cardinality of 10 percent of the limit or more. If your custom metric reaches the dimension limit, consider removing or optimizing the most volatile dimensions.

## Investigate high-cardinality metrics

When you're close to reaching a cardinality limit, investigate the cause before removing data, because the root cause is often a resource you can fix at its source.

1. Check if the amount of data ingested is plausible.

   Is a test environment cronjob or another resource overloading the ingest? Perhaps the root cause is a long-running resource that was never turned off.
2. Analyze which metrics Dynatrace rejects.

   Is the metric still relevant, and does its dimensionality fit its use cases?
3. Consider the relative importance of the parts of your environment.

   You know your environment best. Not all parts of the environment are equally important. Again, does the metric's dimensionality fit its use cases?

## Block dimensions you don't need

Use the metric dimension block list when you can't change the data source, such as a third-party exporter or an SDK. Dynatrace drops blocked dimensions before it stores the metric, so they no longer count toward your cardinality limits.

The block list applies only to custom-ingested metrics, such as metrics ingested through the Metrics API v2, OpenTelemetry, or Prometheus. The block list has no effect on built-in metrics.

To block a dimension

1. Go to **Settings** > **Metrics** > **Metric dimension block list**.
2. Select **Add item**.
3. In **Dimension key**, enter the dimension to block.
4. In **Metric key**, enter the metric to block the dimension on.

   To match several metrics, end the metric key with `*`. For example, `my.metric*` or `my.*` matches all metric keys with that prefix.
5. Turn on **Enabled**.
6. Select **Save changes**.

The entry's summary reads `Block dimension <dimension key> on metric <metric key>`.

To automate the block list, use the `builtin:metric.dimensionblocklist` schema through the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.").