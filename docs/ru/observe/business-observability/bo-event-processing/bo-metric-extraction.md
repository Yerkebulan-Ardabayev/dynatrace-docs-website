---
title: Business event metric extraction via classic pipeline
source: https://www.dynatrace.com/docs/observe/business-observability/bo-event-processing/bo-metric-extraction
scraped: 2026-02-27T21:26:47.559472
---

# Business event metric extraction via classic pipeline

# Business event metric extraction via classic pipeline

* Latest Dynatrace
* How-to guide
* 3-min read
* Updated on Sep 06, 2023

With business event metric extraction via the classic pipeline, you can create your own business metrics. It enables you to:

* Create custom alerts, such as when a certain value surges or drops. Alerts can be based on attribute values or specific business event occurrences.
* Reduce your DDU consumption and lower your costs.

You need to create your business metrics before ingesting business event data.

## Configure metric extraction

To add a business event metric

1. Go to **Settings** > **Business Observability** > **Metric extraction**.
2. Select **Add business event metric** and name your metric by adding a metric **Key** starting with the `bizevents.` prefix (for example, `bizevents.EasyTrade.TradingVolume`).
3. Add a **Matcher** to your rule by pasting your [matcher-specific DQL query](/docs/analyze-explore-automate/logs/lma-classic-log-processing/lma-log-processing-matcher "Examine specific DQL functions and logical operators for log processing."). In the above example, to calculate your trading volume metric, you need to extract only buy transactions, so the matcher query is as follows.

   ```
   matchesValue(event.type, "com.easytrade.buy-assets")
   ```
4. Choose the **Measure** on which your metric will be based. There are two options.

   * **Occurrence of business events records**âa count of events that match your DQL query
   * **Attribute value**âa collection of measures for the attribute value of business events that match your DQL query

     Specify your attribute name in the **Attribute** field. Attribute name matching is not case sensitive. For example, if you choose `Trading_Volume`, the specified attribute name for metric extraction should be `trading_volume`. However, be sure to use the exact attribute name of your business event.
5. Select **Add dimension**. Adding dimensions allows you to split the business event occurrences by a specific business event attribute such as a hostname. If the attribute contains more than one value, the first attribute value acts as the metric dimension. The maximum number of dimensions is 50. Be sure to use the exact attribute name of your business event.
6. Select **Save changes**.

## Visualize metrics

You can extract and visualize your metrics to use them further in your analysis. You can also create metric-based alerts tailored to your needs.

### Display metrics in Data Explorer

To display business event metrics

1. Go to **Data Explorer**.
2. Find your metric in the search window, select **Run query**, and display the results.

   You can also:

   * Visualize your metric on a classic dashboard by selecting **Pin to dashboard**.
   * Export your data to a CSV file.
   * Share a link.
   * Copy the request.

See the example visualization below.

![Visualization of business events metric, bizevents.EasyTrade.TradingVolume](https://dt-cdn.net/images/business-event-metric-display-2806-d2f55d9cc7.png)

### Display metrics in Notebooks Notebooks

You can also explore custom metrics based on business events in Grail, for example, by using the DQL [`timeseries` command](/docs/platform/grail/dynatrace-query-language/commands/metric-commands#timeseries "DQL metric commands"). The following is an example DQL `timeseries` query against the `bizevents.easyTrade.TradingVolume` metric.

```
timeseries avg(bizevents.easyTrade.TradingVolume), alias:avgTradingVolume, interval:1d, from:now()-30d, to:now()
```

Run this query in [Notebooks](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") (**Query Grail** > **Run query**) and view results using the recommended **Line chart** visualization option.

![Query Business Observability custom metrics through DQL with timeseries in Notebooks](https://dt-cdn.net/images/ba-event-metric-query-notebooks-2122-6c3ead0aef.webp)

### Create alerts with metrics

To create alerts based on business event metrics

1. Go to **Settings** > **Anomaly detection** > **Metric events**.
2. Select **Add metric event** and create a custom event where **Type** is **Metric selector**. This is the [metric key defined earlier](#configure), for example, `bizevents.EasyTrade.TradingVolume`.

   Metric events based on business events are only supported with metric selector queries. See [Metric selector events](/docs/dynatrace-intelligence/anomaly-detection/metric-events/metric-selector-events#metricselectorevent "Learn about metric events based on a metric selector.") for more information.

### Unrecognized timestamp handling

If the event timestamp doesn't fall within the allowed [range](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#payload "Learn how the data ingestion protocol for Dynatrace Metrics API works."), your metric is replaced in Grail by a metric with the `.failed` suffix added to the metric key. This new metric will have a recent timestamp, `(now())` and the dimension that would have been attached to the metric you wanted to extract. You can also visualize this metric in [Data Explorer](#data-explorer) or [Notebooks](#notebooks).

## Related topics

* [Metric ingestion protocol](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol "Learn how the data ingestion protocol for Dynatrace Metrics API works.")