---
title: Metrics API v2
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/metric-v2
scraped: 2026-03-06T21:21:35.889227
---

# Metrics API v2


* Reference
* Updated on Jan 22, 2026

[### Get all

Get an overview of all metrics available in your environment.](metric-v2/get-all-metrics.md "List all metrics available in your monitoring environment via Metrics v2 API.")[### Get description

Get the full descriptor of a metric.](metric-v2/get-descriptor.md "View the descriptor of a metric via Metrics v2 API.")[### Read data points

Get data points from metrics you need.

For each metric you can get either one aggregated data point of a list of data points.](metric-v2/get-data-points.md "Read data points of one or multiple metrics via Metrics v2 API.")

[### Select the data you need

The Metrics API is a flexible instrument for obtaining data. Learn how to use metric selector transformations to fine-tune the scope of data you're reading.](metric-v2/metric-selector.md "Configure the metric selector for the Metric v2 API.")[### Modify data on read

In addition to transforming your metric, you can perform simple arithmetic operations right in your query. Learn how to use metric expressions to modify the data you're reading.](metric-v2/metric-expressions.md "Use metric expressions to apply arithmetic operations in a data points query via the Metrics API v2.")

[### Ingest custom metrics

Push custom data points to Dynatrace.](metric-v2/post-ingest-metrics.md "Ingest custom metrics to Dynatrace via Metrics v2 API.")[### Delete a metric

Delete a metric you no longer need.](metric-v2/delete-metric.md "Delete a metric ingested via Metrics v2 API.")[### Delete metrics

Delete metrics older than the specified number of days.](metric-v2/delete-metrics.md "Delete metrics ingested via Metrics v2 API.")

## Related topics

* [Built-in classic metrics](../../analyze-explore-automate/metrics-classic/built-in-metrics.md "Explore the complete list of built-in Dynatrace metrics.")
* [Extend metric observability](../../ingest-from/extend-dynatrace/extend-metrics.md "Learn how to extend metric observability in Dynatrace.")
* [Metric units API](metrics-units.md "Learn about units that Dynatrace metrics use via the Dynatrace API.")