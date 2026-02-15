---
title: Histogram metrics
source: https://www.dynatrace.com/docs/analyze-explore-automate/metrics/histograms
scraped: 2026-02-15T09:07:01.567875
---

# Histogram metrics

# Histogram metrics

* Latest Dynatrace
* Explanation
* 7-min read
* Published Jul 09, 2025

Histogram metrics are a powerful way to capture the distribution of values for a given measurement, such as response times, request sizes, or durations. Compared to a counter that measures the overall total in a single value, a histogram counts the number of occurrences at different thresholds (called buckets). It is a multi-value counter, aggregating data into buckets, allowing you to analyze percentiles, averages, and the overall shape of your data.

## Histogram metrics use cases

* Measure response time distributions for services or endpoints
* Track request or payload sizes
* Analyze latency or duration metrics in distributed systems

For a deeper dive into histograms and their advantages, see the following series of the OpenTelemetry blog posts:

* [Why histograms?ï»¿](https://opentelemetry.io/blog/2023/why-histograms/)
* [Histograms vs. summariesï»¿](https://opentelemetry.io/blog/2023/histograms-vs-summaries/)
* [Exponential histogramsï»¿](https://opentelemetry.io/blog/2023/exponential-histograms/)

## Ingest histogram metrics

No special configuration is needed to ingest histograms from OpenTelemetry (OTLP ingest API) or Prometheus sources (Dynatrace Operator). Histogram metrics are sent automatically when your environment receives OpenTelemetry or Kubernetes data.

The OpenTelemetry Exponential Histogram is not supported as a histogram: the histogram's `min|max|sum|count` are ingested but the buckets aren't.

If any of below happens, the OpenTelemetry ingest API returns the `400` or `200 with partial success` responses.

* Cumulative histograms aren't ingested (similarly to cumulative counters).
* Histogram data points without `sum` aren't ingested. This happens when negative values are recorded.
* Histogram buckets are not sorted.
* Histogram bucket boundary values of `NaN` or `Infinite` are invalid.

## Query percentiles using DQL

Dynatrace Query Language (DQL) allows you to analyze histogram metrics using the percentile aggregation. It calculates the requested percentile across all the buckets for each time slot.

For example:

```
timeseries percentile(http_request_duration_seconds_bucket, 99)
```

The query calculates the 99th percentile of values based on the ingested histogram buckets.

Histograms represent data as a series of buckets, each containing the count of values that fall within a specific range. For example, `http_request_duration_seconds_bucket` contains counts of request durations grouped by predefined ranges (`le` dimension).

The `percentile` function uses the bucket data to estimate the requested percentile (for example, the 99th percentile). It interpolates the value at which 99% of the observed data points fall below, based on the cumulative counts in the histogram buckets.

This query is particularly useful for analyzing latency or performance metrics, as percentiles provide insights into the worst-case scenarios experienced by users.

## Visualization examples and important warnings

You can visualize histogram metrics in Dynatrace Notebooks or Dashboards using DQL queries. However, be aware of the following limitations:

* Dynatrace currently visualizes histogram metrics **as percentiles with line charts over time** (using the `timeseries` command). Visualizing the distribution of occurrences across buckets for a given period of time (typically using a bar chart visualization) is **NOT** supported at this time.

For more information, see [Edit visualizations for Notebooks and Dashboards](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations "Create, edit, and view visualizations on your Dynatrace dashboards and notebooks.").

## Licensing and billing

The [timeseries percentile](/docs/platform/grail/dynatrace-query-language/commands/metric-commands#timeseries_percentile "DQL metric commands") function, which is necessary to query histograms, is only available to DPS customers with the **Metrics powered by Grail** rate card. For more information, see [Metrics powered by Grail overview (DPS)](/docs/license/capabilities/metrics "Learn how Dynatrace Metrics powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.").