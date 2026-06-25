---
title: Drill-down to service failure causes
source: https://docs.dynatrace.com/managed/observe/application-observability/distributed-traces/use-cases/error-analysis
scraped: 2026-05-12T12:01:22.078850
---

# Drill-down to service failure causes

# Drill-down to service failure causes

* Tutorial
* 1-min read
* Updated on May 17, 2024

Analyzing individual requests is a useful way of gaining a better understanding of detected errors. In this article, you will learn how to determine the error underlining an increasing service failure rate using distributed tracing.

## Scenario

In the image below, you can see that requests to `Redis` started to fail around the `10:45` mark on the timeline.

## Steps

1. To find the **Failure rate** tab, go to the serviceâs details page and select a **View** button (such as **View requests**, **View dynamic requests**, or **View resource requests**).

   ![Distributed trace 11](https://dt-cdn.net/images/purepath11-1574-ab48d3472e.png)

   Distributed trace 11
2. Select **Analyze backtrace** to see where these requests came from.

   The requests originate from the `weather-express` service and nearly all failed requests to `Redis` have the same exceptionâan `AbortError` caused by a closed connection.

   ![Distributed trace 12](https://dt-cdn.net/images/purepath12-1591-7acd7c6a02.png)

   Distributed trace 12
3. To analyze down to the affected `Node.js` traces, select **More** (**â¦**) > **Distributed traces**.

   By looking at the `Node.js` trace and its code-level execution tree below, you can see that a `Redis` request leads to an error. You can see where this error occurs in the flow of the `Node.js` code.

   ![Distributed trace 13](https://dt-cdn.net/images/purepath13-1017-a26a6a6140.png)

   Distributed trace 13
4. Select the **Errors** tab to analyze the exception.

   ![Distributed trace 14](https://dt-cdn.net/images/purepath14-1015-5ae03d05ff.png)

   Distributed trace 14

## Conclusion

Each distributed trace on the **Errors** tab shows a unique set of parameters leading up to the error. With this approach to analysis, the distributed traces view can be very useful in helping you understand why certain exceptions occurred.