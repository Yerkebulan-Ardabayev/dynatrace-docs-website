---
title: Service flow metrics
source: https://docs.dynatrace.com/managed/observe/application-observability/services-classic/service-flow/service-flow-metrics
scraped: 2026-05-12T12:30:51.255865
---

# Service flow metrics

# Service flow metrics

* 4-min read
* Updated on Aug 18, 2022

When you select a service within a service flow, the path to the serviceâbeginning with the service that triggered the flowâis highlighted in blue (see image below). Additionally, the arrows constituting the path are enriched with metrics.

![Service flow overview - response time contribution](https://dt-cdn.net/images/service-flow-metrics-1523-dd66283508.png)

Service flow overview - response time contribution

Apart from response time contribution, you can also view the **Average response time** and the number of **Requests** initiated by each service included in the service flow. Just select a service to expand it. Once selected, you can view further details like **Avg. time spent in called services** and the number of **Failed requests** (see image above, bottom right).

Each service also shows the **Response time contribution**, which is calculated using the following formula:

![Response time contribution](https://dt-cdn.net/images/formula-656-40670a0f97.png)

Response time contribution

Value discrepancy

The displayed value for the response time contribution may differ from the actual mathematical result as the calculations are based on underlying data and then rounded off afterwards.

In the service flow example above these are marked as follows:

* 1âAverage response time service
* 2âCall percentage

  The percentage of requests calling the target service among all requests initiated by the service.
* 3âCall per request

  The average number of calls to the target service that were included in each request.
* 4âAverage response time overall

Let's assume that your service flow indicates these request values for your service:

* Average response time = `134ms`
* Call percentage = `6%`
* Calls per request = `1.7`

so:

* Response time contribution = (Average response time) Ã (Call percentage) Ã (Calls per request)
* Response time contribution = `134` Ã `0.06` Ã `1.7`

In this case, the response time contribution = `14%`

If you select **Filter service flow** on the service, the view will filter down to show only the requests that call that service. The call percentage will then rise to `100%`. This set of requests is a subset of what you examine and, because it contributes to every request in that new view, the contribution will be higher.

## Request details in the Service flow side pane

The right side of the **Service flow** page hosts a pane dedicated to the details of the service requests that triggered the service flow (`easyTravel Customer Frontend` in the image below), which includes:

* The **Passing transactions** tab.  
  This tab shows the throughput of the service and its performanceâresponse time, number of requests, and more. Select **Show more** to view [additional analysis options](#further-analysis). The analysis includes all the requests originating from the service.
* The **Infrastructure** tab.  
  This tab shows that `easyTravel Customer Frontend` runs on two hosts and how the throughput is distributed between them. Select **Apply as filter** to filter the service flowâonly calls originating from the selected host are shown.

![Service flow - side pane](https://dt-cdn.net/images/service-flow-side-panels-1745-766324477a.png)

Service flow - side pane

When you select a service within the service flow, a bottom tile hosts the details of the selected service (at the image below it's `easyTravel-Business`).

* The top tile then shows details in the context of the selected service.  
  The number of calls that originate from `easyTravel Customer Frontend` and subsequently call `easyTravel-Business` is **8,490** out of **127,000**. Select **Filter service flow** to show only calls originating from `easyTravel Customer Frontend` and subsequently hitting `easyTravel-Business`. [Additional analysis options](#further-analysis) also focus on these calls.
* In between tiles, you can see the list of all intermediate services and/or proxies between `easyTravel Customer Frontend` and `easyTravel-Business`. You can expand each section and view its details, by selecting it.
* The new tile at the bottom shows details of calls to `easyTravel-Business` that originated from `easyTravel Customer Frontend`. [Additional analysis options](#further-analysis) also focus on these calls.

![Service flow - side pane adapts to the selected service](https://dt-cdn.net/images/service-flow-service-side-panels-1293-3b4dfe84ec.png)

Service flow - side pane adapts to the selected service

### Service-specific analysis options

Depending on the type of service, the bottom tile of the side pane adapts to offer you quick access to specific analysis options.

* **Remote environments**  
  For requests to connected environments, you can go to the [**Remote environments**](/managed/observe/application-observability/distributed-traces/analysis/connect-environments#service-flow "Analyze requests across environment boundaries.") page in the respective remote environment by selecting **Open environment**.
* **Databases**  
  For requests from databases, select **View database statements** to leverage the [top database statements](/managed/observe/infrastructure-observability/databases/database-services-classic/analyze-database-services#service-flow-for-sql-analysis "Analyze your database services with Dynatrace (classic page).") analysis.

## Additional analysis options

* [Distributed traces](/managed/observe/application-observability/distributed-traces/use-cases/segment-request "Enhance your distributed system performance by segmenting requests with slow response time via Service flow and analyzing their distributed traces.")  
  Analyze the detailed method-level chain of calls.
* [Analyze backtrace](/managed/observe/application-observability/services-classic/service-backtrace "Trace the sequence of service calls all the way back up to the browser click that triggered the sequence of calls.")  
  Explore the sequence of service calls that led up to the specific service request.
* [View response time](/managed/observe/application-observability/services-classic/service-response-time-hotspots "Identify the activities that consume the most response time for each service.")  
  View how the response time is distributed along different functions of the service (for example, database usage, code execution, etc.)
* [Analyze outliers](/managed/observe/application-observability/services-classic/response-time-distribution-and-outlier-analysis "Gain insights into the distribution of response times across all requests, including those that are either unusually high or unusually low.")  
  View the response time distribution of requests to the service within a specific timeframe.

You can specify additional filtering options to narrow down the scope of the analysis. See [Service flow filtering](/managed/observe/application-observability/services-classic/service-flow/service-flow-filtering "Understand how service filtering works and how it can be exploited.") to learn how. All these filters will also be applied to further analysis.