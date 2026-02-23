---
title: Distributed Tracing app
source: https://www.dynatrace.com/docs/observe/application-observability/distributed-tracing/distributed-tracing-app
scraped: 2026-02-23T21:20:31.534507
---

# Distributed Tracing app

# Distributed Tracing app

* Latest Dynatrace
* Explanation
* 6-min read
* Updated on Jan 12, 2026

![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing** enhances Dynatrace abilities to analyze and filter trace data at both the request and span levels. With advanced filtering options, such as facets and the grouping function, you can easily explore and pinpoint issues. In addition, your selection is preserved across interactions, enabling you to drill down to the single trace information, and to identify the root cause and prevent failures in your environments.

In Dynatrace, go to ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing** to access this app.

* In the **Distributed Tracing** welcome view, you can get started discovering the app and getting data into Dynatrace. Alternatevely, you can add trace data at any time by selecting  **Traces** and choosing a source. Follow the in-product guidance to continue the configuration for the selected source.
* The default view **Explorer** contains all the user-interface elements to analyze your trace data.

## Requests and spans

A distributed trace is a collection of spans representing a request's journey through a distributed system.

### Requests

The request is the call initiated by a user or system to perform a specific task. It interacts with various services and components within the distributed system.

To view trace data created in your environment in response to an external request, select **Requests** in the upper-left corner of ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**.

### Spans

Spans are individual operations representing each request interaction with the distributed system.

To view all trace data by single operations, select **Spans** in the upper-left corner of ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**.

## Filter field

By entering a query in the [filter field](/docs/discover-dynatrace/get-started/dynatrace-ui/ui-filter-field "The filter field is a powerful tool that allows you to quickly find relevant information or narrow down results within apps."), you can quickly build DQL-based filtering options.

```
"Kubernetes namespace" = prod AND Endpoint = /cart/* AND "Response time" >= 5s
```

You can narrow your results by timeframe or segments.

* To refresh the result for the selected timeframe, select  **Refresh**.
* To choose [segments](/docs/manage/segments "Segments logically structure monitoring data in Grail and function as convenient filters for data that users are allowed to access based on permissions."), select .

The filter field is automatically modified when you apply other filtering selections, such as [facets](#facets). To update the results after you change the filter field query, select  **Update**.

### Use cases

* Get results for any key-value pair.
* Visualize and edit your filtering selection.

## Charts

The charts allow you to view your trace data trends and distribution. You can also hide or show the chart card again at any time.

When you hover over the chart and select an area, the filter field and results are automatically updated to focus on the selected portion of the trace data.

Distributed Tracing charts

The following table compares the **Timeseries** and **Histogram** charts.

Timeseries

Histogram

X-axis

Time intervals [1](#fn-1-1-def)

Response time intervals

Y-axis

Frequency of data points (left-hand side) and response time (right-hand side)

Frequency of data points

Important statistical factors

The legend lists dedicated views for percentiles, averages, and successful and failed requests. Choose an option to view the related trends.

Percentiles and averages are marked with contrast-color vertical lines.

Use cases

Understand how trace data changes over time and identify trends and cyclic behaviors.

Visualize your data's distribution, identify patterns, and spot outliers.

1

Granularity depends on the selected timeframe.

## Facets

Facets are quick filters for trace data. They correspond to span attribute key-value pairs detected in your environment and are grouped by facet categories. The most important DQL field IDs are grouped by default in predefined categories. You can define new facet categories and new facets for attributes that are important to you. Each facet category displays the most frequently detected attributes for the current filtering selection.

For details how to manage your facets, see [Manage facets](/docs/observe/application-observability/distributed-tracing/distributed-tracing-app/facets "Manage your facets in the Distributed Tracing app.").

### Use cases

* Add new facets to better catalog your trace data.
* Select facets from the facet list to filter data by them. The filter field is automatically modified according to your selection. Make sure to select  **Update**.
* Quickly group by attributed keys.
* Quickly add attributes as columns to the table.

## Table results

The table lists the latest 1000 records for the selected timeframe that match the filtering options you applied. The table data is available as a list (  ) or grouped by attributes (  ). You can manage columns to display only the attributes you're interested in and exclude noise.

UI element

Scope

`<column value>`

Filter trace data by a column value.

Copy the DQL statement or the DQL API call.

Download the visible table data.

### Use cases

* Compare records and their different attribute values.
* Filter trace data by a result by selecting the table result. The filter field is automatically modified according to your selection. Make sure to select  **Update**.
* Reduce noise by hiding unnecessary columns from the table or deselecting an attribute.

## Group by

Analyze predetermined important dimensions, such as request count, failure, and percentile contribution, by combining up to 3 attributes that matter the most to you. To group your records by attributes

* Go to the table and select  **Group by:**. Then select/deselect the attribute you're interested in.
* Go to the facet list and select  > **Group by** for each attribute key.

## Single trace perspective

The single trace perspective offers a detailed view of the trace spans.

* The waterfall list on the left contains the trace spans, ordered by sequence. For each span you can see,

  + The corresponding duration bar.
  + The related service; spans associated with the same service are of the same color.
  + The span kind, represented by an icon.

    | Icon | Span kind |
    | --- | --- |
    |  | Web or RPC call (client or server) |
    | The database vendor or | Database call (client) |
    |  | Producer or consumer |
    | The service technology | Call (client or server), internal, or link |

  You can understand the sequence and correlation of spans by observing the size and position of the duration bar. Additionally, you can do the following:

  + Search by values (name, endpoint, service, or attribute).
  + View or hide all spans for the selected trace (  **Name**) or subsequent spans in the trace execution (  next to the span name).
  + View attributes for a span in the details panel by selecting the span name.
  + Explore logs related to the span or the trace (  **View logs**).
* On the right, you can explore and search for attributes for the selected span. Enter a value in the  **Search details** field to view only key or value results matching your search.

To access the single trace perspective, go to the table row of the trace you're interested in and select the trace start time. The single trace perspective opens in the bottom half of the page.

### Use cases

* Focus on the analysis of a single trace.
* Follow full end-to-end traces, across complex transaction flows, even when spanning different trace IDs.

## Exceptions

Use the **Exceptions** tab in ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing** to understand which exceptions occur across your traces and identify, analyze, and resolve issues related to exceptions.

Through visualizations, aggregated data, and contextual insights, the **Exceptions** tab can help you understand the root causes of exceptions and their impact on your service.

This feature is designed for SREs, developers, and DevOps teams who need fast, actionable insights into exception patterns and their impact on services.

Exception analysis provides:

* A clear view of why exceptions occur
* Advanced filtering by service, endpoint, exception type, and timeframe
* In-depth analysis and visual trends of exception occurrences
* Aggregated stack traces to identify root causes
* Contextual logs linked to exceptions
* Insights into requests containing exceptions, including sub-traces

### Integration with Dynatrace

* Embedded in [![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**](/docs/observe/application-observability/distributed-tracing/distributed-tracing-app "Discover the functionalities of the new Distributed Tracing app.") as a new **Exceptions** tab
* Integrated into the Dynatrace service-specific drill-down options
* Replaces the legacy Exceptions Analysis page for DPS customers

### Access and navigation



In addition to the **Exceptions** tab in [![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**](/docs/observe/application-observability/distributed-tracing/distributed-tracing-app "Discover the functionalities of the new Distributed Tracing app."), you can analyze exceptions in context through service-specific drill-downs.

To learn more about analyzing exceptions, see [Exception analysis](/docs/observe/application-observability/distributed-tracing/exception-analysis "Exception analysis helps you detect, investigate, and resolve exceptions more effectively in Dynatrace.").