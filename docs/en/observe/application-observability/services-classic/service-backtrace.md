---
title: Service backtrace
source: https://www.dynatrace.com/docs/observe/application-observability/services-classic/service-backtrace
scraped: 2026-02-06T16:22:45.694439
---

# Service backtrace

# Service backtrace

* Latest Dynatrace
* How-to guide
* 4-min read
* Published Jul 19, 2017

More than just knowing which service directly calls one of your services, it's helpful to know the sequence of service calls that leads up to each requestâall the way back up to the browser click that triggered the sequence of calls. Dynatrace **Service-level backtrace** can show you such call sequences.

Say for example that youâre analyzing a SQL database service and you want to understand the sequence of preceding service requests that ultimately triggered the incoming requests to the SQL service. With service-level backtrace you might learn that, for example, the SQL database service is called by `Service1`, while `Service1` is called by `Service2`, which in turn was triggered by a click on a login button.

To view service-level backtrace

1. Go to **Services** (previous Dynatrace) or ![Services Classic](https://dt-cdn.net/images/services-classic-f58502bd22.svg "Services Classic") **Services Classic**.
2. Select the service you want analyze.
3. On the service overview page, in the **Understand dependencies section**, select **Analyze backtrace** to view the service-level backtrace of requests to this service.

Notice in this example that the majority of calls come from a web application, `easyTravel`, and that the calls come via a specific chain of services (`EasyTravelWebServer` calls `easyTravel Customer Frontend` that calls `CouchDB_ET`). Select any element of the chain to see the names of individual requests. In the image below, all requests to `CouchDB_ET` originating from the `easytravel.com` application come from a detailed list of user actions.

![User actions in service-level backtrace](https://dt-cdn.net/images/user-actions-service-level-backtrace-1606-34253e59f0.png)

When a service or an application in a backtrace hierarchy is selected, you can access further analysis regarding this service or application in two separate sections.

![Service-level backtrace](https://dt-cdn.net/images/service-level-backtrace-1598-04ecfb12fc.png)

In the first section, in the case of an application, you can view the list of [user actions](/docs/observe/digital-experience/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.") of this specific application that occurred within the [selected timeframe](/docs/analyze-explore-automate/dashboards-classic/dashboards/dashboard-timeframe "Learn about Dynatrace dashboard timeframe and management zone settings."). In the case of services, you can view the types of requests that were made by that particular service to the next service in the backtrace flow.

The next section includes analysis data regarding the number of requests and any failures that may have occurred. Further information can be accessed by selecting the tabs:

* **Reasons for failed requests**  
  Lists the reasons that specific requests failed.
* **Stacktrace**  
  Shows in which part of the code a request was executed.
* **Referring pages**  
  Shows the HTTP referrers that contributed to the specific backtrace flow.
* **Proxies**  
  Provides information about the proxies or load balancers that a request was sent through.
* **Analyze**  
  Offers various analysis options for both the selected service (in the left-hand column) and the service examined in the backtrace (right-hand column).

  + [View service flow](/docs/observe/application-observability/services-classic/service-flow "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment.")
  + [View details of failure](/docs/observe/application-observability/services-classic/response-time-distribution-and-outlier-analysis#correlate-errors-with-response-times "Gain insights into the distribution of response times across all requests, including those that are either unusually high or unusually low.")
  + [View distributed traces](/docs/observe/application-observability/distributed-traces/use-cases/segment-request "Enhance your distributed system performance by segmenting requests with slow response time via Service flow and analyzing their distributed traces.")
  + [View response time](/docs/observe/application-observability/services-classic/service-response-time-hotspots "Identify the activities that consume the most response time for each service.")
  + [View outliers](/docs/observe/application-observability/services-classic/response-time-distribution-and-outlier-analysis "Gain insights into the distribution of response times across all requests, including those that are either unusually high or unusually low.")
  + [View method hotspots](/docs/observe/application-observability/services-classic/service-response-time-hotspots#code-level-visibility "Identify the activities that consume the most response time for each service.")
  + [View web requests](/docs/observe/application-observability/multidimensional-analysis/top-web-requests "Learn how to analyze all web requests across all of your services using Dynatrace.")

Additionally, you have the option of showing only those transactions that contain the current call chain. Just select [Filter service backtrace](/docs/observe/application-observability/services-classic/service-flow/service-flow-filtering "Understand how service filtering works and how it can be exploited.").

![Filter service-level backtrace chain](https://dt-cdn.net/images/filter-service-level-backtrace-chain-1589-94fc599a8b.png)

If a clustered service is selected in the backtrace, open the **Instances** tab to view the same analysis for every [service instances](/docs/observe/application-observability/services-classic/analyze-individual-service-instances "Find out how you can perform a service-instance analysis.") (see image above).

## Backtrace analysis examples

Here are some examples of how to use backtrace analysis:

Analyze the impact of errors

The backtrace feature becomes even more useful when it comes to analyzing errors. See the example below. It shows a `100%` **Failure rate** for the `AdsForBlog` request.

![Backtrace 6](https://dt-cdn.net/images/backtrace06-1354-edc72085b5.png)

To learn the root causes of detected failures, select **Analyze failure rate degradation**. You'll then see the message and the stacktrace (see image below). To see how significant the failures were and if they impacted your users, select **Analyze backtrace**.

![Backtrace 7](https://dt-cdn.net/images/backtrace07-1587-9980999988.png)

Dynatrace shows you how this failed request impacted your other services and your users. You can see that all requests came from a single user action, the loading of the blog. You can also see that the `/blog` request on the web server wasnât impacted by the failed `Ads request`. Not a single `/blogs` request failedâso the error was handled gracefully.

![Backtrace 8](https://dt-cdn.net/images/backtrace08-1328-23bee447bd.png)

![Backtrace 9](https://dt-cdn.net/images/backtrace09-1335-4bd4238f06.png)

In contrast, have a look at the service analysis page below. You can see immediately that the failure of the `Credit Card Verification` service had some impact on users. The `BookingService` requests failed and users could no longer purchase items. This shows clearly that this error is of high importance and should be addressed immediately to avoid future occurrences.

![Backtrace 10](https://dt-cdn.net/images/backtrace10-1309-ea97c0aa1e.png)

![Backtrace 12](https://dt-cdn.net/images/backtrace12-1333-ebb2bae108.png)

Understand third-party impact

Dynatrace enables you to see which services call which third-party services, in addition to the browser clicks that initiate such call sequences. In the image below, note that all requests to `fedex.com` are failing. The service backtrace tells you which services and which user clicks led up to this third-party call.

![Backtrace 13](https://dt-cdn.net/images/backtrace13-1259-8ef8c816f6.png)

![Backtrace 14](https://dt-cdn.net/images/backtrace14-1266-2325a9cae8.png)