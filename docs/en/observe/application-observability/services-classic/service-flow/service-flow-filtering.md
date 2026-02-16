---
title: Service flow filtering
source: https://www.dynatrace.com/docs/observe/application-observability/services-classic/service-flow/service-flow-filtering
scraped: 2026-02-16T21:13:11.316143
---

# Service flow filtering

# Service flow filtering

* 5-min read
* Published Jul 19, 2017

Modern web applications typically feature complex service architectures that can process millions of different types of requests. With each unique request behaving slightly differently and triggering a slightly varied service flow, it can be a real challenge to analyze the performance and behavior of individual requests.

The filtering features help you to navigate the complexity of your application's service architectureâenabling you to find the proverbial needle in the haystack. Dynatrace **Service flow** enables you to analyze subsets of requests triggered by a given service.

The general **Service flow** filtration procedure looks like this:

1. Go to ![Services Classic](https://dt-cdn.net/images/services-classic-f58502bd22.svg "Services Classic") **Services Classic**.
2. Select the service you want to analyze.
3. On the service overview page, under **Understand dependencies**, select **View service flow**.
4. Within **Service flow**, select a called service to define the sequence of services you want to analyze.  
   The [pane on the right](/docs/observe/application-observability/services-classic/service-flow/service-flow-metrics#side-pane "Learn about the service flow metrics that measure the performance of the service calls that are triggered by each service request in your environment.") directly opens to the **Passing transactions** tab.
5. To create a filter for the selected service sequence, do one of the following:

   * Select **Filter service flow** in the top tile.
   * Select **Filter** ![Filter](https://dt-cdn.net/images/filter-icon-41ddd02d66.svg "Filter") above the selected service.
6. Add more criteria to the filter:

   1. In the filter, select the service where you want to apply additional filtration.
   2. From the **Filtered by** list, select the criterion.
   3. Specify the threshold or matching rules for the criterion.
   4. Select **Apply**.
   5. If needed, add more criteria to the filter.
   6. When finished, select **Apply**.

See below for a more detailed explanation.

## Filter requests based on specific call sequences

Call sequence filters are available in most service analysis views, but theyâre most obvious in the **Service flow**. As you can see in the example below, only **5.9%** of the requests to the `easyTravel Customer Frontend` service also called the `JourneyService` service. Next, **99%** of them called the `easyTravel-Business` database service.

![Service flow - overview](https://dt-cdn.net/images/service-flow-overview-1779-2ec7d38f7d.png)

To focus **Service Flow** on these calls

1. Go to ![Services Classic](https://dt-cdn.net/images/services-classic-f58502bd22.svg "Services Classic") **Services Classic**.
2. Select the service you want to analyze.
3. On the service overview page, under **Understand dependencies**, select **View service flow**.
4. Within **Service flow**, select a called service to define the sequence of services you want to analyze. In our example, it's `easyTravel-Business`.  
   The **Passing transactions** tab appears on the right side of the page.
5. To create a filter for the selected service sequence, do one of the following:

   * Select **Filter service flow** in the top tile.
   * Select **Filter** ![Filter](https://dt-cdn.net/images/filter-icon-41ddd02d66.svg "Filter") above the selected service.

Let's go back to our example. A filter has been created to focus analysis only on those requests from the `easyTravel Customer Frontend` service that call the `JourneyService` service and subsequently call the `easyTravel-Business` database.

Notice that the number of requests analyzed on `easyTravel Customer Frontend` has been reduced to **8.73k** from **156k**, as only a subset of calls is now taken into account. Consequently, the average response time now represents only those `easyTravel Customer Frontend` requests that call `JourneyService`.

Now take a close look at the `JourneyService` node. Note that **35%** of the `easyTravel Customer Frontend` service's response time is taken up by `JourneyService`. **Service flow** also reveals something unexpectedâsome of the selected requests trigger the `RMI server`.

![Service flow - filter by called service](https://dt-cdn.net/images/service-flow-filter-1621-b66825047a.png)

## Multi-faceted filters

Each filter can contain multiple call sequences. This means that you can create complex, multi-faceted call-sequence filters based on your unique service-analysis needs. **Service Flow** will only focus on calls that fit all the criteria.

To add the new sequences to the existing filter

1. While your current filter is still active, select an additional call sequence in **Service flow**.
2. In the **Passing transactions** tab of the [pane on the right](/docs/observe/application-observability/services-classic/service-flow/service-flow-metrics#side-pane "Learn about the service flow metrics that measure the performance of the service calls that are triggered by each service request in your environment."), select **Filter service flow**.

In the example below, the filter criteria are extended with calls from the `easyTravel Customer Frontend` service that call the `RMI server` service and subsequently call the `easyTravel-Business` database. Now the number of requests analyzed on `easyTravel Customer Frontend` has been reduced to **528**. Also, the `JourneyService` service is now responsible for **39%** of the response time.

![ Service flow - applied filter](https://dt-cdn.net/images/service-flow-filtered-1622-125fbdca28.png)

## Extend your filters with additional criteria

After you've narrowed down the number of calls based on the involved services, you can add more criteria to the filter.

1. In the filter, select the service where you want to apply additional filtering.
2. From the **Filtered by** list, select the criterion.
3. Specify the threshold or matching rules for the criterion.

   ![Service flow filter 8](https://dt-cdn.net/images/service-filter-8-699-1e8e0e114f.png)
4. Select **Apply**.
5. If needed, add more criteria to the filter.
6. When finished, select **Apply**.

In our example, we applied the **Response time** threshold of **200 ms** to `JourneyService`. Now only calls with a response time longer than **200 ms** are shown, and there are just **6** of them. We're now very close to finding the needle in this haystack!

![ Service flow - results of filtering](https://dt-cdn.net/images/service-flow-use-filter-1624-3394932b09.png)

## Analyze call sequences from multiple angles

The true power of call-sequence filtering becomes apparent when you begin analysis of a problematic call sequence. In the example above, **Service flow** now shows us that **40%** of the `easyTravel Customer Frontend` service's response time is taken up by `JourneyService`.

The next logical step is to analyze the response time of the `JourneyService` service in the context of the selected call sequence. To do this, select `JourneyService` within `Service flow`. The right pane reveals all the analysis options that you can perform on the selected serviceâall within the context of the filtered call sequence. All the filters you created in **Service flow** will also be applied to the additional analysis.

Learn more about additional analysis options in topics listed below.

* [Distributed traces](/docs/observe/application-observability/distributed-traces/use-cases/segment-request#pp-analysis "Enhance your distributed system performance by segmenting requests with slow response time via Service flow and analyzing their distributed traces.")  
  Analyze the detailed method-level chain of calls.
* [Analyze backtrace](/docs/observe/application-observability/services-classic/service-backtrace "Trace the sequence of service calls all the way back up to the browser click that triggered the sequence of calls.")  
  Explore the sequence of service calls that led up to the specific service request.
* [View response time](/docs/observe/application-observability/services-classic/service-response-time-hotspots "Identify the activities that consume the most response time for each service.")  
  View how the response time is distributed along different functions of the service (for example, database usage and code execution)
* [Analyze outliers](/docs/observe/application-observability/services-classic/response-time-distribution-and-outlier-analysis "Gain insights into the distribution of response times across all requests, including those that are either unusually high or unusually low.")  
  View the response time distribution of requests to the service within a specific timeframe.

## Related topics

* [Advanced service flow filteringï»¿](https://www.youtube.com/watch?v=bbZdkuClx-E)