---
title: Detect performance issues
source: https://www.dynatrace.com/docs/observe/application-observability/distributed-tracing/detect-performance-issues
scraped: 2026-02-19T21:12:45.408530
---

# Detect performance issues

# Detect performance issues

* Latest Dynatrace
* Tutorial
* 5-min read
* Published Oct 28, 2024

Understanding which requests are slow and why that happens can be challenging in modern, cloud-based, distributed systems. The [Distributed Tracing ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") appï»¿](https://dt-url.net/vc23u9n) is designed to help answer these questions quickly through an exploratory approach.

Test the app in a sandbox environment:

* [Playground environmentï»¿](https://dt-url.net/al43u2h)

## Target audience

This article is intended for SREs, developers, and performance architects who want to investigate performance issues by analyzing distributed traces within the Distributed Tracing app.

## What you will learn

In this tutorial, youâll learn how to use the Distributed Tracing app specifically to analyze and troubleshoot slow requests in a production Kubernetes namespace. You will learn to:

* Filter traces based on relevance  
  Use facets to narrow down the scope of traces, focusing on those that align with your responsibilities or areas of interest.
* Zoom in on specific timeframes  
  Pinpoint relevant time periods with the time series chart or timeframce selector to view performance over a selected duration.
* Identify performance outliers  
  Use histogram views to locate traces with extended response times.
* Analyze affected services and requests  
  Use the grouping feature to understand which services and requests are affected.
* Drill down into individual traces  
  Explore detailed trace data for specific requests to uncover root causes and pinpoint what occurred during slow response events.

## Prerequisites

* You're familiar with the [concepts of distributed tracing](/docs/observe/application-observability/distributed-traces/concepts "Learn more about distributed tracing core concepts and terminology.").
* You have Dynatrace Platform Subscription (DPS).
* You're ingesting trace data via [Dynatrace OneAgent](/docs/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.") or [OpenTelemetry](/docs/ingest-from/opentelemetry/getting-started "How to get your OpenTelemetry data into Dynatrace."). To get started ingesting trace data, go to the **Distributed Tracing** >  **Traces** > choose a source and follow the in-product guidance.
* Make sure that your traces are available in the [Distributed Tracing ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing")](/docs/observe/application-observability/distributed-tracing/distributed-tracing-app "Discover the functionalities of the new Distributed Tracing app.") app.

## Analyze and troubleshoot performance issues

1. Go to Distributed Tracing ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing").
2. In the upper-right corner, select the timeframe **Last 30 minutes** to see how the number of requests and their response time have evolved during that timeframe.
3. Use facets to filter traces by a specific namaspace. To analyze traces that traverse your Kubernetes **prod** namespace,

   1. In the facets list, go to **Kubernetes** > **Kubernetes namespace**.

      The namespaces that are detected more frequently in your traces are listed first.
   2. Select **prod**.

      The filter field query automatically changes. You can edit the filter query further before updating the results.
   3. Select  **Update** to update the results.
4. Observe the charts to quickly spot performance outliers.

   1. Go to the **Timeseries** chart to get an overview of the trends.

      ![Detect performance issues timeseries](https://dt-cdn.net/images/traces-example-00001-timeseries-3430-6a591decfd.png)

      The Kubernetes **prod** namespace shows several spikes for request count and a cluster of failed requests.
   2. To analyze data further, select **Histrogram**.

      ![Detect performance issues histogram](https://dt-cdn.net/images/traces-example-00002-3440-40b39e1573.png)

      The histogram summarizes the amount of requests to a specific response time bucket. There's a cluster of requests to the **prod** environment that take around 5s.
   3. Select the chart area containing the affected cluster to focus on the requests that fall into that response time bucket.

      The filter bar is updated to show traces for the selected response time area, and the list shows traces with similar services and endpoints.
5. Group the requests by service and endpoint to undestand which services and endpoints are affected.

   1. Go to the table and select  **Group by:**.
   2. Select the attributes **Service** and **Endpoint**.

      In the table view (:TableIcon:) you can see an aggregated list of the services and endpoints that fall into the selected response time for the **prod** namespace. The columns summarize average and highest duration, the request count, and how many of these requests failed, including the failure rate.
   3. To learn more about the top contributors to an aggregate in the table, select .

      Focusing on the **/cart/checkout** request, you'll see that it not only has a slow response time (**5.82 s**) but also a high failure rate (**28%**), indicating it may be a key bottleneck.

      ![distributed tracing cart/checkout request](https://dt-cdn.net/images/wkf10640-apps-dynatrace-com-ui-apps-dynatrace-distributedtracing-explorer-3840-e0a340e0bf.png)
   4. To focus on a request, select the request name (**/cart/checkout**) in the table and filter by the endpoint.

      The filter field query and the table results are automatically updated.
6. To identify the bottleneck for a request matching the selected filters, go to the  list view and select the timestamp for one of the requests.

The single trace perspective opens at the bottom half of the page. Now, you can analyze the full end-to-end trace. In our case, we see that the bottleneck is the **GetCart** endpoint on the **Cart** services, which leads to a slow response time.

## Conclusion

In this tutorial, you've learned how to effectively use the Distributed Tracing ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") app for analyzing and troubleshooting slow requests within a production Kubernetes namespace. You're now skilled at filtering traces based on relevance, zooming in on specific timeframes to identify anomalies, and analyzing impacted services and requests. These skills enabled you to diagnose and resolve performance issues within your Kubernetes environment efficiently.

We analyzed trace data and identified a cluster of slow and failing requests within the production Kubernetes namespace. By filtering, grouping, and examining trace data, we were able to pinpoint a bottleneck in the **GetCart** endpoint of the **Cart** service.