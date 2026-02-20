---
title: Services app
source: https://www.dynatrace.com/docs/observe/application-observability/services/services-app
scraped: 2026-02-20T21:06:59.534419
---

# Services app

# Services app

* Latest Dynatrace
* App
* 5-min read
* Updated on Feb 18, 2026

![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** delivers comprehensive visibility into your distributed services, enabling teams to quickly identify, investigate, and resolve issues across complex microservice architectures. This unified interface consolidates critical health signals and performance metrics to accelerate troubleshooting and optimize service reliability.

![View the real-time performance of all your services. Locate specific services using powerful filters.](https://cdn.hub.central.dynatrace.com/hub/1_DI39YNS_hQ7gBgG.png)![Analyze database queries executed by your services to discover which operations consume the most resources.](https://cdn.hub.central.dynatrace.com/hub/2_previously_5_7LmaiBa.png)![Use Dynatrace Intelligence's automated root cause analysis to quickly surface and pinpoint the source of issues in your application services, accelerating analysis.](https://cdn.hub.central.dynatrace.com/hub/3_lHZzEjb_zyT76Yj.png)![Failure analysis comparing timeframes.](https://cdn.hub.central.dynatrace.com/hub/failure-analysis-1990-6b9d85e513_38quxQP.png)

1 of 4View the real-time performance of all your services. Locate specific services using powerful filters.

## Prerequisites

* Your users should have the necessary permission to use ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**.
* ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** is installed in your environment.
* Dynatrace collects data on your services through [OneAgent or OpenTelemetry](/docs/observe/application-observability/services#add "Learn how to monitor and analyze your services, define and use request attributes, and more.").

## Get started

### Service health overview

![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** provides an intelligent health dashboard that surfaces issues demanding immediate attention. You can filter alerts by severity and drill into specific services experiencing degradation. When a service enters a critical state, the app highlights failure rates and provides context around what triggered the alertâwhether it's increased errors, latency spikes, or infrastructure problems.

![Health alert investigations](https://dt-cdn.net/images/health-alert-investigation-critical-filtering-1248-f719905bfe.png)

### Failure analysis and time-based comparisons

Overlay current failure patterns against baseline periods to immediately identify regressions. The visualization distinguishes between different failure types and severities, helping teams prioritize based on user impact.

Also, refer to the [Failure Analysis](/docs/observe/application-observability/services/failure-analysis "Failure Analysis helps you quickly detect, investigate, and resolve service failures in Dynatrace.") use case.

![Failure analysis comparing timeframes](https://dt-cdn.net/images/failure-analysis-comparing-timeframes-1174-f966ba23d7.png)

[![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems**](/docs/dynatrace-intelligence/davis-problems-app "Use the Problems app to quickly get to the root cause of incidents in your environment.") maps the entire impact chain from an initial failure through dependent services, infrastructure, and affected users.

Navigating from ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** to ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** Failure Analysis takes a single click, allowing for seamless investigation from high-level problem detection to granular service-specific error details, including timeframe comparisons and logs.

![Problem app flow to failure view in services app](https://dt-cdn.net/images/problem-app-flow-to-failures-1763-1f0cd27274.png)

### Advanced filtering and release analysis

Filter service views across releases and dozens of facets, including Kubernetes namespaces and deployment dimensions. Compare behavior across staging and production to identify configuration drift or isolate environment-specific issues.

![Filtering by release and namespace](https://dt-cdn.net/images/filtering-by-release-and-k8s-namespace-1451-c6b95eae9d.png)

### Response time analysis and comparison

Track response time to understand typical behavior versus worst-case scenarios. Analyze performance trends across different periods to identify exactly when a degradation began and what was the reason for it. Correlate latency changes with deployment events or traffic pattern shifts to quickly pinpoint the cause of performance regressions.

For details, see [Response time analysis](/docs/observe/application-observability/services/response-time-analysis "Response time analysis helps you quickly the key contributors to slow service performance in Dynatrace.").

![Response time analysis comparisons](https://dt-cdn.net/images/response-time-analysis-comparisons-with-p-50-p-90-1062-916cc69f80.png)

### Message processing

Track message publish rates, receive rates, and processing throughput across your service topology. Identify bottlenecks in asynchronous workflows that traditional request-response monitoring misses.

Visualize processing failure rates to pinpoint services struggling with message consumption or transformation logic. Maintain visibility into batch jobs, event processors, and queue-based integrations operating outside critical user-facing paths.

![Message queue interaction by service](https://dt-cdn.net/images/message-processing-per-service-publish-receive-process-1678-1e1552955c.png)

### Database query performance analysis

With the **Database queries** view, ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** provides detailed visibility into database queries executed by your services.

You can access the **Database queries** view in two different ways:

* Select  **Database queries** on the left side of ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** to see all queries executed across your services.
* Select the required service, and go to the **Database queries** tab to view the queries made by this particular service.

Both options provide query performance information, with a default view that shows the top queries ranked by cumulative duration.

![Database queries - Services app](https://dt-cdn.net/images/database-query-list-1783-1cedf6af87.png)

Redis statements often include unique identifiers or values, which results in thousands of distinct entries shown in the **Database queries** view. For tips on how to reduce cardinality for such database statements, refer to [Database queries: Normalize Redis commands](/docs/platform/openpipeline/use-cases/reduce-span-metric-cardinality#database-queries "Leverage three different views in the Services app to normalize span and metric data, ensuring aggregations and analysis remain reliable and usable.").

#### Use cases

* Discover which operations consume the most resources and where indexing or caching could improve performance.
* Eliminate blind spots by integrating infrastructure-layer database observability with service-level metrics.

#### Understand the query list

The **Database queries** view displays metrics about your most resource-intensive queries, sorted by cumulative duration.

The following information is available for each database query:

* **Query**: Full SQL or database operation.
* **System**: Database type, for example, PostgreSQL or Redis.
* **Errors**: Failed execution count.
* **Query count**: Total executions in the timeframe.
* **Average duration**: Average execution time per query.
* **Cumulative duration**: Total time your service spent on this query.

Select  (**Expand row**) on the left of the query to display its time-series charts. These three time-series charts visualize the performance trends:

* **Queries per minute**: Shows execution frequency patterns and spikes.
* **Query duration**: Tracks average response time changes over time.
* **Error rate**: Displays query failure percentage.

#### Find performance bottlenecks

Sort the database query list by one of the following parameters:

* **Cumulative duration** to immediately see which queries are consuming the most total time in your service.
* **Average duration** to find your slowest queries.
* **Query count** to identify high-frequency operations that might benefit from caching or indexing.

Remember that a query executing thousands of times with a modest duration can impact performance just as much as a slow query with fewer executions. By seeing both frequency and duration together, you can prioritize optimization efforts where they'll have the greatest impact.

### Outbound calls



![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** captures and analyzes outbound calls made by your services, and then presents the most frequently called and slowest external dependencies ranked by request rate and duration. The **Outbound calls** view displays request rate, error rate, average duration, and cumulative duration for each outbound call. Discover which external calls consume the most resources and where performance bottlenecks exist in your service dependencies. By integrating outbound call observability with service-level metrics, you can eliminate blind spots and quickly determine if issues originate within your service or downstream.

![Outbound calls tab](https://dt-cdn.net/images/scr-20260204-oxkt-1998-bc116aaf86.png)

URLs with variables in the path name still result in unusable data aggregations. For guidance on reducing cardinality in outbound calls, refer to the processing examples in [Reduce span-based and metric-based cardinality](/docs/platform/openpipeline/use-cases/reduce-span-metric-cardinality "Leverage three different views in the Services app to normalize span and metric data, ensuring aggregations and analysis remain reliable and usable.").

## Concepts

Service-related concepts, including distributed traces and spans, are central concepts in Dynatrace observability. Understanding these concepts enables effective monitoring and analysis of distributed systems. See [Service-related concepts](/docs/observe/application-observability/services/services-concepts "Understand application observability, services, and distributed tracing concepts.").

## Tutorials

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Maintain centralized control over service health, performance, and resources.](https://www.dynatrace.com/hub/detail/services-1/?query=services&filter=all)[![Dynatrace Signet](https://dt-cdn.net/images/dt-logo-color-vertical-0a89040753.svg "Dynatrace Signet")

### Try in Dynatrace Playground

Get a hands-on experience with ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** in our public sandbox environment, interacting with sample data without installing software.](https://wkf10640.apps.dynatrace.com/ui/apps/dynatrace.services/home)

## Related topics

* [Services](/docs/observe/application-observability/services "Learn how to monitor and analyze your services, define and use request attributes, and more.")
* [Distributed Tracing](/docs/observe/application-observability/distributed-tracing "Trace and analyze in real time highly distributed systems with Grail.")
* [Failure Analysis](/docs/observe/application-observability/services/failure-analysis "Failure Analysis helps you quickly detect, investigate, and resolve service failures in Dynatrace.")