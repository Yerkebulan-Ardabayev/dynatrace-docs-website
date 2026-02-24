---
title: Response time analysis
source: https://www.dynatrace.com/docs/observe/application-observability/services/response-time-analysis
scraped: 2026-02-24T21:14:40.038085
---

# Response time analysis

# Response time analysis

* Latest Dynatrace
* Tutorial
* 3-min read
* Published Jan 12, 2026

Response time analysis in Dynatrace helps users quickly identify the key contributors to slow service performance. By analyzing outbound calls, database and queue interactions, and service internals, this feature provides a clear breakdown of where time is being spent. Additionally, it offers an infrastructure perspective, giving insights into key metrics for related infrastructure components.

This analysis is designed to be used both reactively, to investigate specific performance issues, and proactively, to explore potential bottlenecks. Users can also compare different timeframes to understand how the response time for services and their endpoints has changed over time.

## Key capabilities

## Access and navigation

The new response time analysis is available as a dedicated **Response Time** tab in [![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**](/docs/observe/application-observability/services/services-app "Maintain centralized control over service health, performance, and resources with the Services app."). It is designed to support both contextual and exploratory workflows.

### Service-specific response time analysis

When you're looking at the details of a specific service, select **Analyze response time** on top of the response time chart or on a specific endpoint of your service. This opens the **Response Time** tab with filters based on the selected service.

### Contextual access via problems-specific drill-down options

When a response time degradation is identified as the root cause of a problem, the **Response Time** tab opens with filters based on the affected service and endpoint.

### Exploratory access

To explore services and see which are slowest, go to the **Response Time** tab in [![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**](/docs/observe/application-observability/services/services-app "Maintain centralized control over service health, performance, and resources with the Services app.") manually.

* Adjust filters to explore failures across services, endpoints, and timeframes.
* Compare it to different timeframes.

## Get started

To find out what's slow

1. Go to [![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**](/docs/observe/application-observability/services/services-app "Maintain centralized control over service health, performance, and resources with the Services app.") and select the **Response Time** tab.
2. Apply [segments](/docs/manage/segments "Segments logically structure monitoring data in Grail and function as convenient filters for data that users are allowed to access based on permissions.") and filters to focus on relevant services/endpoints.

   For single service analysis, you also get a contribution breakdown that classifies the calls to:

   * Internal service execution
   * Outbound calls
   * Database usage
   * Message processing

To find out why it's slow

1. Turn on **Analyze details** above the table for additional details to help you understand what contributed most to the response time of the selected services and traces.
2. Response time analysis provides a detailed breakdown of where time is being spent during service requests. This includes:

   | Category | Description |
   | --- | --- |
   | **Outbound calls** | Shows the time spent waiting for downstream dependencies, such as API calls or frontend processing. |
   | **Database interactions** | Highlights the time spent on database queries and interactions. |
   | **Service internals** | Breaks down the time spent within the service itself, including code execution and internal processing. |
   | **Infrastructure metrics** | Displays key metrics for related infrastructure components, such as CPU usage, memory consumption, and network latency. |

## Use cases

### Investigate slow services

When a service is perceived as slow, use response time analysis to:

* Identify whether the issue is caused by service internals, downstream dependencies, database interactions, or infrastructure congestions.
* Drill down into specific areas to pinpoint the root cause of the slowness.
* View related infrastructure metrics to determine if hardware or network issues are contributing to the problem.

### Monitor performance proactively

Use response time analysis proactively to:

* Explore potential performance bottlenecks before they impact users.
* Monitor key metrics for critical services and infrastructure components.
* Gain a deeper understanding of how different factors contribute to overall response times.