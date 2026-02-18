---
title: Log metrics (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-metrics
scraped: 2026-02-18T21:30:10.161526
---

# Log metrics (Logs Classic)

# Log metrics (Logs Classic)

* Tutorial
* 7-min read
* Updated on Jan 18, 2023

Log Monitoring Classic

Dynatrace Log Monitoring gives you the ability not only to view and analyze logs, but also to create metrics based on log data and use them throughout Dynatrace like any other metric. You can add them to your dashboard, include them in an analysis, and even create custom alerts.

Log metric pricing is based on the Davis data units (DDUs) model. Check [DDUs for metrics](/docs/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.") to find out how you can estimate and track DDU consumption for log metrics.

Depending on the options you select during log metric creation, the new metric value can represent:

* **Occurrence of log records** (available in Dynatrace version 1.206+)  
  The metric value will represent a count of occurrences of log records that match the query.
* **Attribute value** (available in Dynatrace version 1.229+)  
  The metric value can represent one of the aggregations that you can specify in [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.").

When Dynatrace ingests log data, it applies the defined query to the log data and, based on your log metric **Measure** selection, the metric value will therefore represent either a count of the log records that match the query or one of the following values for the specified attribute: `Average`, `Count`, `Maximum`, `Minimum`, `Sum`, `Median`, `Percentile 10th`, `Percentile 75th`, or `Percentile 90th`. The specified attribute must be of numeric type. Dynatrace will attempt to convert string type attributes to numbers as long as they match the following pattern:  
`123`  
`123.`  
`123.456`  
`.456`  
`-.456`  
`+.456`  
`+123.456`  
`-123.456`  
`123.4e+5`  
`-123.4E-5`  
`1234e+5`  
`1234e5`

Attributes holding more than one value are not converted to attribute-based metrics.

## Creating log metric

All metrics based on a Log Monitoring matcher have a metric key with the `log.` prefix.

Log metric availability in Dynatrace

A created log metric is available only when new log data is ingested, and it matches the input from the **Matcher** field defined during log metric creation. Ensure that new log data has been ingested before utilizing the log metric in other areas of Dynatrace.

The range of a timestamp for accepting data that is used in metric creation is between **1 hour** in the past and **10 minutes** in the future. If no timestamp is provided, the current timestamp of the server is used.

There are two ways to create a metric based on log data:

### Create metric using settings

1. Go to **Settings** > **Log Monitoring** > **Metrics extraction** and select **Add log metric**.
2. In **Metric key**, append the metric name to the `log.` metric key.
3. In **Matcher**, enter the Log Monitoring query to filter the log data for your metric. For details, see [Log viewer](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer#query-syntax "Learn how to use Dynatrace log viewer to analyze log data.").

   I switched to Grail

   If you switched to [Dynatrace Grail](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more."), you may begin using the [DQL](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") functions in your Log Monitoring queries. For details, see [Log processing with classic pipeline](/docs/analyze-explore-automate/logs/lma-classic-log-processing#dql-functions "Utilize log processing rules to reshape incoming log data for better understanding, analysis, or further transformation.").
4. Select a **Measure**:

   * **Occurrence of log records**âa count of occurrences of log records that match the query.
   * **Attribute value**âthe collection of measures for the attribute value of log records that match the query. If you select this option, you need to also set **Attribute** to the attribute whose values will be gauged.
5. Optional Select **Add dimension** one or more times to add dimensions for your query result.  
   Adding dimensions allows you to split the log metric occurrences by a specific log data attribute. If the attribute contains more than one value, the first attribute value will act as the metric dimension. For details, see [Log viewer](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer#log-dimensions "Learn how to use Dynatrace log viewer to analyze log data.").
6. Select **Save changes** to create the log metric.

### Create metric using log viewer

1. Go to ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic**.
2. Create a log viewer query or use log viewer **Available attributes** to extract the log data that interests you. For details, see [Log viewer](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer#query-syntax "Learn how to use Dynatrace log viewer to analyze log data.").

Advanced query

In the advanced mode, you can specify more complex criteria for log events by using combinations of keywords, phrases, logical operators, and parentheses. If you use an advanced query and manually modify the query, select **Run query** to update the results table.

3. Select **Create metric**. Your log viewer query is now displayed on the **Log metrics** page.
4. Optionally, add dimensions for your query result.  
   Adding dimensions allows you to split the log metric occurrences according to specific log data attribute.
   For details, see [Log viewer](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer#log-dimensions "Learn how to use Dynatrace log viewer to analyze log data.").
5. Append the metric name to the metric key `log.` and save changes to create the log metric.

### Unique dimensions limits

If you create metrics with high cardinality (a lot of unique dimensions), you can reach your environment's [cardinality limit](/docs/analyze-explore-automate/metrics/limits "Reference of metrics powered by Grail"). To mitigate these limitations, you can:

* Narrow the query to decrease the number of logs in a metric.
* Lower the cardinality of your dimensions.
* Disable a metric that exceeds the limit.  
  It is recommended to add more filters to reduce the number of unique dimensions first.

## Create metrics from dropped logs

Logs often contain valuable metric data, but you may not want to store the original log data. To get the metric data from logs and discard the original log data, you can create a metric from dropped logs. For example, consider the following log content:

```
2023-06-15T13:02:56Z localhost haproxy[12528]: 10.10.10.10:48064 http-in~ local/local0 3605/0/0/61/3666 HTTP_STATUS 200 138 - - ---- 7416/7413/400/401/0 0/0 {574|||domain.com} {|} "POST /communication HTTP/1.1"
```

You may be interested only in the active session total time from HAPproxy and you would like to discard the rest of the log data.

To do that

1. Ingest the log data via OneAgent and API.

   * [Log ingestion via OneAgent](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa "Ingest log data to Dynatrace using OneAgent and have Dynatrace transform it into meaningful log messages.")
   * [Log ingestion API](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api "Stream log data to Dynatrace using API and have Dynatrace transform it into meaningful log messages.")
2. Extract the metric from the ingested log data.

   * [Log processing with classic pipeline](/docs/analyze-explore-automate/logs/lma-classic-log-processing "Utilize log processing rules to reshape incoming log data for better understanding, analysis, or further transformation.")
3. Create the log metric.

   * [Log metrics](/docs/analyze-explore-automate/logs/lma-log-processing/lma-log-metrics#log-metrics-create-rule "Create metrics based on log data and use them throughout Dynatrace like any other metric.")

## Editing log metric

To list, enable, disable, delete, or modify metrics created from log data, go to **Settings** > **Log Monitoring** > **Metrics extraction**.

Editing a metric key will generate a new metric. As a result, historical data will be accessible only with the old metric key.

## Example

In this example, we create and chart a log metric, save it to a dashboard, and create an alert.

1. Go to ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic** to display the log viewer.
2. Create a query that filters the data that you are interested in. For this example, to filter all log entries for `error`, enter this query: `status="error"`
3. Select **Create metric**.  
   The **Log metrics** page is displayed with **Matcher** set to your query.
4. Type in the metric key (a unique name for the metric). By default, each metric key begins with `log.` prefix. All log metrics based on logs must have a key starting with this prefix.  
   For this example, set key to: `log.error_PGI`
5. Select **Add dimension** and then select the `dt.entityprocess_group_instance` dimension from the list.

   If you saved the metric without adding a dimension, Dynatrace would count errors globally. But in this example, we want to see how the error status is distributed across process group instances. Adding the `dt.entityprocess_group_instance` dimension will make Dynatrace count the number of error statuses for each process group instance. This allows you to view precisely where the error status occurred and to create an alert for a particular dimension.
6. **Save changes**.

Now that you have defined the metric, you can chart it, pin it to a dashboard, and even create an alert based on it.

* **Chart:** Go to **Data Explorer**, set **Select metricâ¦** to `log.error_PGI`, and select **Run query**.
* **Dashboard:** After you create a chart, select **Pin to dashboard** to add the chart to one of your classic dashboards. For details, see [Pin tiles to your dashboard](/docs/analyze-explore-automate/dashboards-classic/charts-and-tiles/pin-tiles-to-your-dashboard "Learn to pin tiles to your dashboards.").
* **Alert:** Go to **Settings** > **Anomaly detection** > **Metric events**, select **Add metric event**, and create a custom event based on `log.error_PGI`.