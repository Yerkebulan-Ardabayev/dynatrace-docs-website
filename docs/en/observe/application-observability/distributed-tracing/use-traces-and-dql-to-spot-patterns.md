---
title: Use traces, DQL, and logs to spot patterns
source: https://www.dynatrace.com/docs/observe/application-observability/distributed-tracing/use-traces-and-dql-to-spot-patterns
scraped: 2026-02-23T21:20:41.475600
---

# Use traces, DQL, and logs to spot patterns

# Use traces, DQL, and logs to spot patterns

* Latest Dynatrace
* Tutorial
* 14-min read
* Published Nov 20, 2025

Identify abnormal patterns in traces and logs using [![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**](/docs/observe/application-observability/distributed-tracing/distributed-tracing-app "Discover the functionalities of the new Distributed Tracing app.") and [Dynatrace Query Language (DQL)](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.").

## Introduction

In this tutorial, you'll learn how to utilize traces, DQL, and logs to:

* Spot inefficient database queries.
* Understand workload patterns.
* Identify abnormalities in database usage.
* Do performance analysis.
* Understand the impact of individual database queries (for example, how much data they change).

For your ease of reference, the sections where we use ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing** are marked with this icon ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing"), while the sections where we utilize DQL are marked with . Also, for a detailed explanation of each DQL query, select **Explain this DQL query** above the DQL query code block.

## Target audience

Any user of latest Dynatrace who is eager to learn more about traces, logs, and DQL and understand how to use all these effectively.

## Learning outcome

After completing this tutorial, you'll learn how to write and efficiently utilize a variety of DQL queries, which can help you streamline troubleshooting, set up alerts, and automate workflows.

## Before you begin

### Prerequisites

All you need to complete this tutorial is access to latest Dynatrace in your environment.

Alternatively, use our [Dynatrace Playgroundï»¿](https://wkf10640.apps.dynatrace.com/) environment to follow the steps of this tutorial.

### Prior knowledge

* Familiarity with latest Dynatrace
* At least basic knowledge of DQL
* Understanding of what [Distributed Tracing](/docs/observe/application-observability/distributed-tracing "Trace and analyze in real time highly distributed systems with Grail.") is

  For an overview, check out [Unleash the Power of Distributed Tracingï»¿](https://youtu.be/8QuBqPsqZlg?si=RKrl7MW6kODQgFDA) on YouTube.

## Identify inefficient database query patterns

Whether a certain SQL statement is executed repeatedly, multiple different SQL statements are called within a trace, or one long-running query is involvedâeach scenario represents a potential performance issue we aim to detect.

### Distributed Tracing Spot query patterns with Distributed Tracing

Let's start with ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**. Thanks to this app, we can quickly identify inefficient or redundant database usage by leveraging a couple of filters, groupings, and views.

1. Go to ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**.
2. In the upper-left part of the page, under the app header, select **Spans** to view the analysis based on request spans.
3. In the **Search facets** text field, enter **Databases**, and select the **Databases** facet to reveal all related metadata.
4. Next to **Db query text**, select  (**More**) > **Group by** to instantly analyze all database queries across spans.

From this view, you can:

* Sort the data by different parameters in ascending or descending order.
* Group the data by multiple attributes.
* Narrow down the data by using various filters.

You can apply the techniques described below to exceptions, hosts, processes, remote procedure calls, and more.

![In Distributed Tracing, switch to "Spans" and group the data by "Db query text" and "Service" to reveal some database query patterns](https://dt-cdn.net/images/spot-database-query-patterns-with-distributed-tracing-3840-d081d5aa09.png)

#### Sort data

Select the table column headers to sort the data by different parameters and surface certain database query patterns.

* **Count**: Find the most frequent queries.
* **Average duration**: Spot the longest-running queries.
* **Failure rate**: View the database queries with the highest error occurrence.

#### Group data by multiple attributes

Slice your data by multiple attributes to refine your view.

1. Right above the table, expand the **Group by** dropdown list, and select **Services**. You should have the following grouping:  
   **Group by: Db query text | Service**.

   This way, you can see which database queries are shared across services.
2. Change the order of the grouping attributes. In the **Group by** dropdown list, clear **Db query text**, and then select this attribute again. You should have the following grouping:  
   **Group by: Service | Db query text**.

   In this case, you can see which database queries each service is executing.
3. Select  to the left of the currently active primary attribute to expand the attribute and view the requested analysis.

The order in which you put the grouping attributes directly influences the results you receive.

#### Narrow down data via filters

Apply filters to narrow down the data.

In the **Type to filter** text field, enter a query. For instance, enter `"Db query text" = *` to get rid of spans with empty database queries.

### Spot unusual patterns with DQL

After utilizing ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**, let's learn how to use DQL to reveal atypical patterns in your traces and logs. We recommend using [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") to run all the DQL query examples in this tutorial.

1. Go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.
2. Select  **Notebook** in the app header to create a new notebook.
3. Open the  **Add** menu, and select  **DQL**.

   You can add multiple DQL sections for all the DQL queries provided in the tutorial.
4. In the query section, enter a DQL query.
5. Select  **Run** to execute the DQL query.

![Use Notebooks to enter and run the DQL queries provided in this tutorial](https://dt-cdn.net/images/spot-unusual-patterns-with-dql-and-notebooks-3840-134c8bdd13.png)

### Discover top query types

Let's check how often a specific query type (for example, `INSERT`, `SELECT`, or `UPDATE`) shows up in your spans over time. Copy the following query to the notebook query section, and then select  **Run** to execute the DQL query.

Explain this DQL query

* `fetch spans`: Retrieve data from the `spans` table, which contains information about individual spans.
* `filter isNotNull(db.query.text)`: Include only those spans where the database query is present.
* `parse db.query.text, "string:type"`: Parse the `db.query.text` field and extract the `type` value to find out which query type we're looking at. This value is then stored in a new field called `type`.
* `makeTimeseries count(), by:{upper(type)}`: Count how many times each query type appears in our spans and create a time series for visualization.

```
fetch spans



| filter isNotNull(db.query.text)



| parse db.query.text, "string:type"



| makeTimeseries count(), by:{upper(type)}
```

Run in Playground

![Time series created with DQL that shows the count of spans with a non-null database query text, grouped by the uppercase version of the query type](https://dt-cdn.net/images/top-query-types-3008-99fd02b845.png)

Use this query to understand workload patterns or spot anomalies.

### Spot time-consuming queries

Now, let's run the query below to see how long your database queries are taking and locate the slowest queries.

Explain this DQL query

* `fetch spans`: Retrieve data from the `spans` table, which contains information about individual spans.
* `filter isNotNull(db.query.text)`: Include only those spans where the database query is present.
* `makeTimeseries sum(duration), by:{db.query.text}`: Create a time series that shows the sum of the duration of each query, sorted by query text.

```
fetch spans



| filter isNotNull(db.query.text)



| makeTimeseries sum(duration), by:{db.query.text}
```

Run in Playground

![Time series created with DQL that shows the total duration of spans grouped by database query text](https://dt-cdn.net/images/time-consuming-queries-3008-f36e14a02e.png)

This time series allows us to spot time-consuming database queries and is great for performance tuning. When a query takes too much time, there might be a more efficient query that achieves the same goal.

### Reveal high-impact queries

With this query, we can check how many rows of data are affectedâfor example, `SELECT`ed, `INSERT`ed, or `DELETE`dâby each database query.

Explain this DQL query

* `fetch spans`: Retrieve data from the `spans` table, which contains information about individual spans.
* `filter isNotNull(db.query.text)`: Include only those spans where the database query is present.
* `makeTimeseries sum(db.affected_item_count), by:{db.query.text}`: Create a time series summing up the number of the affected data rows, sorted by query text.

```
fetch spans



| filter isNotNull(db.query.text)



| makeTimeseries sum(db.affected_item_count), by:{db.query.text}
```

Run in Playground

![Time series created with DQL that shows the total number of affected items over time for each unique database query text](https://dt-cdn.net/images/high-impact-queries-3008-6e139ac96c.png)

This time series shows how many rows of data are affected by each query. If a particular query affects more data rows than others, such a query would be a great candidate for optimization.

## Spot exception patterns

In this section, let's use DQL to reveal certain exception patterns. We'll determine which exception types are most common and locate services with the most exceptions.

### Count exceptions per exception type

We focus on the number of exceptions that are coming in and learn how frequently each type of exception occurs.

Explain this DQL query

* `fetch spans`: Retrieve data from the `spans` table, which contains information about individual spans.
* `filter iAny(span.events[][span_event.name] == "exception")`: Include only those spans that have an exception.
* `expand span.events`: Flatten the `span.events` array to work with the individual span events instead of the entire array.
* `fieldsFlatten span.events, fields: {exception.type}`: Extract the `exception.type` field from each span event and flatten that into a column of its own that we can group and count.
* `makeTimeseries count(), by: {exception.type}, time:start_time`: Create a time series showing the count of exceptions, grouped by their type over time. This time series shows how frequently each type of exception occurs based on the start time of the span.

```
fetch spans



| filter iAny(span.events[][span_event.name] == "exception")



| expand span.events



| fieldsFlatten span.events, fields: {exception.type}



| makeTimeseries count(), by: {exception.type}, time:start_time
```

Run in Playground

![Time series created with DQL that shows the count of exceptions over time, grouped by their type](https://dt-cdn.net/images/exceptions-per-exception-type-3008-3a21c3be67.png)

Checking the number of exceptions per exception type can be useful for error monitoring and debugging. With this query, you can:

* Identify which types of exceptions are most common.
* Spot trends or spikes in specific exception types.
* Correlate exception frequency with deployments, traffic changes, or other system events.

### Spot services with most exceptions

With the next query, we get the list of services with the largest number of exceptions.

Explain this DQL query

* `fetch spans`: Retrieve data from the `spans` table, which contains information about individual spans.
* `filter iAny(span.events[][span_event.name] == "exception")`: Include only those spans that have an exception.
* `expand span.events`: Flatten the `span.events` array to work with the individual span events instead of the entire array.
* `fieldsFlatten span.events, fields: {exception.type, exception.message}`: Flatten the `exception.type` and `exception.message` fields.
* `summarize count(), by: {service.name, exception.message}`: Summarize these fields by count and group them by service name and exception message.

```
fetch spans



| filter iAny(span.events[][span_event.name] == "exception")



| expand span.events



| fieldsFlatten span.events, fields: {exception.type, exception.message}



| summarize count(), by: {service.name, exception.message}
```

Run in Playground

Spotting services with the highest number of exceptions can help you triage and prioritize your team's troubleshooting efforts. Moreover, knowing which exception messages are most common can help you detect recurring bugs or misconfigurations.

## Detect hotspot internal methods

When it comes to code optimization, you might first want to see what your hotspots methods are. In this case, we can analyze all spans that represent internal method calls and then group them by service and span name.

### Distributed Tracing Find long-running spans with Distributed Tracing

Here is how we achieve that in ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**.

1. Go to ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**.
2. In the upper-left part of the page, under the app header, select **Spans** to view the analysis based on request spans.
3. In the **Search facets** text field, enter **Span**, and then select **internal** under the **Span kind** facet.
4. Right above the table, expand the **Group by** dropdown list, and select **Services** and **Span name**. You should have the following grouping:  
   **Group by: Service | Span name**.
5. Select the **Average duration** table header.
6. Select  to the left of the currently active primary attribute to expand the attribute and view the requested analysis.

![In Distributed Tracing, switch to "Spans", filter for internal spans, and group the data by "Service" and "Span name" to identify long-running spans](https://dt-cdn.net/images/find-long-running-spans-with-distributed-tracing-3840-7b407b56ad.png)

You can instantly see which spans are consuming the most time.

### Identify top 10 slowest internal spans

Leveraging the next query, you get the list of slowest internal span nodes by average duration.

Explain this DQL query

* `fetch spans`: Retrieve data from the `spans` table, which contains information about individual spans.
* `` filter matchesValue(`span.kind`, "internal") ``: Focus on internal spans, thus excluding span types such as HTTP requests or messaging spans.
* `summarize {durationSum = sum(duration), callCount = count(), avgDuration = avg(duration)}, by: {service.name, span.name}`: Aggregate the span data by three verticals (their total duration, number of calls, and average duration) and group the data by service and span name to get metrics per method or operation within each service.
* `sort avgDuration desc`: Sort by average duration, starting with the longest (that is, slowest internal operations).
* `limit 10`: Restrict the output to the top 10 results.

```
fetch spans



| filter matchesValue(`span.kind`, "internal")



| summarize {durationSum = sum(duration), callCount = count(), avgDuration = avg(duration)}, by: {service.name, span.name}



| sort avgDuration desc



| limit 10
```

Run in Playground

Identifying a function in your code that consumes a significant amount of execution time or resources helps detect bottlenecks, understand runtime behavior, and streamline optimization efforts (such as reducing CPU usage, memory consumption, or response time).

## Identify log patterns: services with most logs

Now, let's unveil services that produce the largest number of logs. The query below offers us a simple way of identifying our top log producers within the context of a trace.

Explain this DQL query

* `fetch logs`: Load all available log data from the `logs` table.
* `filter isNotNull(trace_id)`: Include only those logs that are part of a trace.
* `summarize count = count(), by: {service.name}`: Sum the logs up and group them by service name, which means we count how many trace-linked logs each service has produced.
* `sort count desc`: Sort by number of logs, starting with the largest, thus services with the highest number of logs appear first.
* `limit 20`: Restrict the output to the top 20 results.

```
fetch logs



| filter isNotNull(trace_id)



| summarize count = count(), by: {service.name}



| sort count desc



| limit 20
```

Run in Playground

Such a DQL query comes in handy when you need to understand which services produce the largest number of logs. Knowing that, you can identify log-heavy services, which might be over-logging, and optimize log ingestion costs.

## Join logs and traces: count logs per service endpoint

Finally, let's find out how many logs are created per service endpoint.

By default, logs don't contain endpoint information. However, by [enriching logs with the trace ID](/docs/analyze-explore-automate/logs/lma-log-enrichment "Connect your incoming log data to traces for more precise Dynatrace analysis."), we can `join` logs and traces based on their common field.

Explain this DQL query

* `fetch spans`: Retrieve data from the `spans` table, which contains information about individual spans.
* `join [`: Perform a join operation with another dataset:

  + `fetch logs`: Load all available log data from the `logs` table.
  + `fieldsAdd trace.id = toUid(trace_id)`: Add a `trace.id` field by converting the `trace_id` field to a unique identifier (UID) using the `toUid` function.
  + `summarize logCount = count(), by: {trace.id}`: Summarize the logs data by `trace.id`, calculating the total number of logs for each trace.
  + `], on: {trace.id}`: Join the summarized logs data with the spans data on the `trace.id` field, combining the two datasets.
* `filter isNotNull(http.url)`: Include only those spans that contain a HTTP URL.
* `summarize {requestCount = count(), logCount = sum(right.logCount)}, by: {http.url}`: Sum up the request count and the log count per requested endpoint (`http.url` field).
* `fieldsAdd logPerRequest = logCount / requestCount`: Add a field where we calculate the ratio of logs per request.
* `sort logPerRequest desc`: Sort by descending order.

```
fetch spans



| join [



fetch logs



| fieldsAdd trace.id = toUid(trace_id)



| summarize logCount = count(), by: {trace.id}



], on: {trace.id}



| filter isNotNull(http.url)



| summarize {requestCount = count(), logCount = sum(right.logCount)}, by: {http.url}



| fieldsAdd logPerRequest = logCount / requestCount



| sort logPerRequest desc
```

Run in Playground

Running this query, we obtain a list sorted by endpoint that summarizes the number of requests and logs received for each endpoint, while we also calculate the ratio of logs per request. This is useful in identifying our heavy-hitting endpoints that might be producing excessive logs.

## Call to action

We hope this tutorial has given you some additional tips and tricks on how to become more efficient in analyzing traces and logs and spotting abnormalities in your environment. You can apply similar techniques to exceptions, hosts, processes, remote procedure calls, and more.

You learned how to use ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing** to detect database query patterns. Furthermore, you grasped numerous examples on how to utilize DQL to find services with the most exceptions, identify hotspot methods, and even join logs and traces to calculate the number of logs created per service endpoint.

If you believe that you need to have certain information at hand, [add the DQL query result to the dashboard](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks#edit-section-edit-controls "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace."). You might also consider [creating a metric](/docs/analyze-explore-automate/logs/lma-use-cases/lma-e2e-create-log-metric "Explore the Log Management and Analytics use case for creating a log metric.") that you can extract from the logs as they come into Dynatrace.

## Next steps

* Check out this [dedicated notebookï»¿](https://wkf10640.apps.dynatrace.com/ui/apps/dynatrace.notebooks/notebook/94d1e2b0-0d81-4803-8b5e-5b9614598d86) created in our Dynatrace Playground environment, where we share some of the tips and tricks on leveraging traces, logs, and DQL to highlight unusual patterns in your environment.
* Dive deeper into the world of DQL: visit [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") and [DQL best practices](/docs/platform/grail/dynatrace-query-language/dql-best-practices "Best practices for using Dynatrace Query Language.").
* Explore the following Dynatrace apps:

  + [![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**](/docs/observe/application-observability/distributed-tracing/distributed-tracing-app "Discover the functionalities of the new Distributed Tracing app.")
  + [![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**](/docs/analyze-explore-automate/logs/lma-logs-app "Search, filter, and analyze logs with Dynatrace Logs app to quickly investigate and share insights.")
  + [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.")
  + [![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.")