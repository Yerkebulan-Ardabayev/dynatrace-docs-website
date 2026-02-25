---
title: Segment requests to improve response time degradation
source: https://www.dynatrace.com/docs/observe/application-observability/distributed-traces/use-cases/segment-request
scraped: 2026-02-25T21:15:34.047126
---

# Segment requests to improve response time degradation

# Segment requests to improve response time degradation

* Tutorial
* 3-min read
* Updated on May 17, 2024

In your environment, there are many thousands of requests, each with their relationships and context. To identify the root cause of inefficiencies, it's therefore necessary to narrow down the analysis to just the relevant requests. You can segment your requests by [filtering the service flow](/docs/observe/application-observability/services-classic/service-flow/service-flow-filtering "Understand how service filtering works and how it can be exploited.") or via [outlier analysis](/docs/observe/application-observability/services-classic/response-time-distribution-and-outlier-analysis "Gain insights into the distribution of response times across all requests, including those that are either unusually high or unusually low.").

## Scenario

The service `easyTravel Customer Frontend` received 249,000 requests during the selected 2-hour timeframe. In this example, we want to identify requests with a slow response time for the service.

## Steps

1. Start by segmenting the requests via **Service flow**.

   1. To access the service flow

      1. Go to ![Services Classic](https://dt-cdn.net/images/services-classic-f58502bd22.svg "Services Classic") **Services Classic**.
      2. Select the service you want to analyze.
      3. On the service overview page, under **Understand dependencies**, select **View service flow**.

      We are interested specifically in the requests from `easyTravel Customer Frontend` that call first `AuthenticationService` and then `easyTravel-Business`. **94%** of the `easyTravel Customer Frontend` requests calling `AuthenticationService` also call `VerificationService`.
   2. To focus on a subset of requests

      1. Select a called service > **Apply filter** ![Filter](https://dt-cdn.net/images/filter-icon-41ddd02d66.svg "Filter").

         ![Segmentation of transactions via service flow](https://dt-cdn.net/images/transactions-manual-segmentation-1225-210c1e1ad2.png)
      2. To add a service as a second filter parameter, select the service you want to add.

         ![Refine chain of calls](https://dt-cdn.net/images/service-flow-chain-of-calls-1221-12f6c53a07.png)
2. To access the distributed traces list filtered by the set parameters, select the caller service (`easyTravel Customer Frontend`) > **Distributed traces** ![Distributed traces](https://dt-cdn.net/images/purepaths-icon-790bea38ba.svg "Distributed traces").

   The **Most recent traces** list features the requests initiated by `easyTravel Customer Frontend` that match the filter criteria. You can filter the list or sort it by **Start time**, **Name**, **Response time**, **Processing time**, **HTTP method**, or **Response code**.
3. To visualize only `easyTravel Customer Frontend` requests with response time slower than or equal to 80 ms

   1. Select the **easyTravel Customer Frontend** node.
   2. From the **Filter requests** list, select **Response time**.
   3. Select **greater than or equal to â¥**, type `80` in the input field, and select **Apply**.
   4. Select **Apply**.

   ![Filter distributed traces](https://dt-cdn.net/images/filter-distributd-traces-1621-2d6b34444e.png)

   Only **3** requests out of the initial 249,000 justify in-depth distributed trace analysis.

   ![Detection of slow requests](https://dt-cdn.net/images/slower-requests-detection-1589-e1fc1d5a66.png)
4. Select a trace from the refined list to proceed with its code-level analysis.

## Conclusion

By segmenting the requests in `easyTravel Customer Frontend` service flow and drilling down to only the ones that satisfy our criteria, we narrow down the necessary in-depth analysis from 249,000 to 3 requests for the selected 2-hour timeframe.

You can extend your analysis:

* To see where the request originated, select **More** (**â¦**) > [**Service backtrace**](/docs/observe/application-observability/services-classic/service-backtrace "Trace the sequence of service calls all the way back up to the browser click that triggered the sequence of calls.").
* To see the entire trace from the first fully monitored process group, select **Show full trace**.
  Each distributed trace tracks a request from start to finish. This means that the traces always start at the first fully monitored process group. With this option, you can change your perspective and focus only on a service.