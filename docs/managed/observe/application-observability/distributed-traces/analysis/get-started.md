---
title: Get started with Distributed Traces
source: https://docs.dynatrace.com/managed/observe/application-observability/distributed-traces/analysis/get-started
scraped: 2026-05-12T11:14:11.970352
---

# Get started with Distributed Traces

# Get started with Distributed Traces

* How-to guide
* 6-min read
* Updated on Aug 13, 2024

Distributed Traces Classic provides you with a combination of analysis tools to gain insight into your environment's transactions. It combines code-level visibility, topology information, and metadata with the highest level of data granularity and fidelity. In this article, you'll explore the Distributed Traces Classic functionalities and how to leverage them to analyze requests in your environment.

## Quick start

To get started with a distributed trace analysis

1. Go to **Distributed Traces**.
2. Optional Use the **Overview** chart to understand the request count and response time over the selected timeframe.
   Data retention

   The chart uses [trace and request data](/managed/observe/application-observability/multidimensional-analysis#data-source "Configure a multidimensional analysis view and save it as a calculated metric."), which has different data retention periods. For timeframes containing data older than 10 days, you can turn on the **Show data retention** toggle to better understand which data is available for which period directly from the chart.
3. Optional In the table, expand  the details of the trace you want to analyze for an overview of its topology, attributes, HTTP information, and timings.
4. Select the distributed trace name for in-depth trace analytics.
5. Select a time segment to expand the detail tabs.

## Get an overview

To configure a view of the distributed traces in your environment

1. Go to **Distributed Traces**.

   ![Distributed traces overview](https://dt-cdn.net/images/distributed-traces-overview-3552-8da636c2c1.png)

   Distributed traces overview
2. Configure a view by setting filters. To filter the distributed traces by

   * Ingestion method

     + Select **PurePaths** to view PurePathÂ® distributed traces captured by OneAgent.
     + Select **Ingested traces** to view distributed traces [instrumented with other libraries](/managed/ingest-from/extend-dynatrace/extend-tracing "Learn how to extend trace observability in Dynatrace.").
   * Service

     Go to **Filter requests** > **Service name** and enter the service name. Note that you can access this view also by going to **Services** > **More** (**â¦**) > **Distributed traces** for the service.

## Export overview data

You can export the distributed traces overview table data in a comma-separated values (CSV) file.

1. Go to **Distributed Traces**.
2. Optional Narrow down the table results by reconfiguring your view or via the search input field above the table.

   The table lists up to the **3,000** most recent traces that are captured during the selected timeframe and within the selected management zone. Depending on the timeframe and the configured view, the list highlights the most important node for the trace.

   Find a node

   To find a specific node of a trace

   1. Go to **Distributed Traces**.
   2. Filter the table by the trace ID.
   3. Select the trace name.
   4. In the **Trace** view, find the desired node.
3. In the lower-right corner of the page, select the **Show export** menu.

   ![Show export menu](https://dt-cdn.net/images/show-export-menu-107-2a8a76c9a2.png)

   Show export menu
4. Select one of the following options.

   | Option | Exported data | Fields | Number of entries |
   | --- | --- | --- | --- |
   | **Export visible data** | The currently displayed area of the table, taking into account applied filters | Only visible fields | Up to 50 traces |
   | **Export table data** | All table data, including traces that are not displayed on the current table page | All the available fields related to distributed traces | All 3,000 most recent traces |

## Analyze a single trace

The distributed trace analysis view provides an end-to-end waterfall visualization of the requests in a single trace.

To access the single trace view

1. Go to **Distributed Traces**.
2. From the table, select the distributed trace name.
3. Optional Go to the **Execution breakdown** to learn the trace time distribution.
4. Go to the waterfall chart to learn which services are traversed by the trace and in which order.
5. Select a request to visualize subsequent interactions.

   Use the colors and positions of the horizontal bars in the chart to see which requests were executed synchronously (in parallel). They indicate both the sequence and response time of each of the requests.

   ![Distributed traces - trace overview](https://dt-cdn.net/images/distributed-traces-trace-overview-1398-0bc0c909a4.png)

   Distributed traces - trace overview
6. Select a time segment to access in-depth trace analytics in detail tabs, down to code-level information.
7. Choose a detail tab to continue your analysis.

   Summary

   ![Distributed trace - summary tab](https://dt-cdn.net/images/purepath-distributed-trace-summary-tab-1578-9a1abde976.png)

   Distributed trace - summary tab

   |  |  |
   | --- | --- |
   | Availability | default |
   | Content | Includes details on metadata, request headers, request parameters, and information about the proxy through which the request was sent. |

   Values obscured with five asterisks (`*****`) imply [hidden confidential data](/managed/manage/data-privacy-and-security/data-privacy/personal-data-captured-by-dynatrace "Find out what types of end-user data may be captured during Dynatrace monitoring and the methods that are available for masking personal end-user data."), which can be unmasked by users with sufficient permissions. Three or fewer asterisks (`***`) are used for data aggregation purposes and can't be unmasked.

   Timings

   ![Distributed trace - timings](https://dt-cdn.net/images/purepath-distributed-trace-timings-1581-677870facf.png)

   Distributed trace - timings

   |  |  |
   | --- | --- |
   | Availability | default |
   | Content | Timing-specific details of services. Select **View method hotspots** for more details on timing contributions (for example, CPU, wait, sync, lock, and execution time). |
   | Example | The example above shows timing details for the `/orange.jsf` web service call. In this case, you see that the request lasts **57.7ms**. |

   Code level

   ![Distributed trace code-level insights](https://dt-cdn.net/images/purepath-distributed-trace-code-level-insights-1581-dca5962209.png)

   Distributed trace code-level insights

   |  |  |
   | --- | --- |
   | Availability | OneAgent required depends on data input [1](#fn-1-1-def) |
   | Content | Comprehensive code execution of each and every request, including the code-level method executions and their timings, in the exact sequence of events. |
   | Example | In the example above, Dynatrace tells you exactly which method in the `/orange.jsf` request on the `easyTravel Customer Frontend` service called the respective web services and which specific web-service methods were called. The timings displayed here are the timings as experienced by the `easyTravel Customer Frontend`, which, in the case of calls to services on remote tiers, represent the client time. |

   1

   The volume of code-level information varies depending on importance, timing, and estimated overhead. Typically, slower parts of a request contain more details.

   Logs

   |  |  |
   | --- | --- |
   | Availability | Log enrichment required depends on data input[1](#fn-2-1-def) |
   | Content | Log records in the full context of the transaction. All available span IDs are included by default.  * To filter by logs relevant to the selected waterfall node, turn on **Strict span filter**. * To see all the logs for a trace, select **View logs for this trace**. |
   | Example | [Leverage log enrichment for traces to resolve problems](/managed/observe/application-observability/distributed-traces/use-cases/problems-logs-traces "Use the log enrichment to view related log entries in the distributed traces view and enhance your analysis capabilities.") |

   1

   To get started, see [Log enrichment](/managed/analyze-explore-automate/log-monitoring/log-monitoring-configuration/log-enrichment "Learn how you can connect your incoming log data to traces for more precise Dynatrace analysis.").

   Errors

   |  |  |
   | --- | --- |
   | Availability | depends on data input |
   | Content | Occurring exceptions for failed requests. |
   | Example | [Drill-down to service failure causes](/managed/observe/application-observability/distributed-traces/use-cases/error-analysis "Resolve errors via distributed traces.") |

   Threads

   |  |  |
   | --- | --- |
   | Availability | OneAgent required depends on service type |

   Integrations

   |  |  |
   | --- | --- |
   | Availability | depends on service type |

## FAQ

What does `[declared unavailable by agent]` mean?

`[declared unavailable by agent]` is a placeholder value displayed in the trace view when metadata is not available for OneAgent to capture, due for example to a lack of data visibility or constraints in reporting it, for example, the technology is not supported by OneAgent. We recommend contacting a Dynatrace product specialist via live chat within your Dynatrace environment to understand your case.

## Related topics

* [Services](/managed/observe/application-observability/services-classic "Learn about Dynatrace's classic service monitoring")
* [Service flow](/managed/observe/application-observability/services-classic/service-flow "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment.")
* [Service analysis timings](/managed/observe/application-observability/services-classic/service-analysis-timing "Find out what each time in service analysis means.")