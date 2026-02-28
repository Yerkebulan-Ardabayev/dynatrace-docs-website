---
title: Speed up incident response with Dynatrace Investigations reference time
source: https://www.dynatrace.com/docs/secure/use-cases/speed-up-incident-response-with-reference-time
scraped: 2026-02-28T21:33:46.500677
---

# Speed up incident response with Dynatrace Investigations reference time

# Speed up incident response with Dynatrace Investigations reference time

* Latest Dynatrace
* Tutorial
* Published May 13, 2025

Effective incident response and root cause analysis rely on accurate timing and context. With ![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**'s [reference time](/docs/secure/investigations/concepts#reference "Key concepts for using Dynatrace Investigations across security, operations, and performance analysis."), you can enhance data-driven investigations by gaining deeper insight into the sequence of events.
This article explores how you can maximize the benefits of timestamp reference within [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.").

## Target audience

This article is intended for Security and Site Reliability Engineers who participate in incident response, root cause analysis, and threat-hunting endeavors that involve data-driven forensic investigations.

## Scenario

You get a notification that your production environment has a high load of HTTP 503 errors. You now have to quickly find out what has caused these errors. You log in to your Dynatrace environment and start the investigation. Fortunately, your colleagues have already started the investigation, and some initial steps have already been taken.

## Before you begin

1. Open the [read-only shared investigation in Dynatrace Playgroundï»¿](https://wkf10640.apps.dynatrace.com/ui/apps/dynatrace.security.investigator/share/484db0e6-d7fa-48ec-97ce-6612260e0854).
2. Duplicate the investigation to continue the investigation scenario and be able to execute queries. For instructions, see [Duplicate investigations](/docs/secure/investigations/case-sharing#duplicate "Share, duplicate, and control access to investigations across teams in Dynatrace Investigations.").

## Get started

The following steps guide you through the flow of a root cause analysis using the reference time as one of the tools in ![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**.

1. Analyze the response chart

Open the duplicated investigation and select the blue node to view the chart representation of the response code distribution over time.

You can see the response code 503 spike for a while before returning to a normal state.

![chart](https://dt-cdn.net/images/092f92179d3-3279-04ba0d498c.png)

2. Look for the first occurrence of the error

As written in [RFC7231ï»¿](https://datatracker.ietf.org/doc/html/rfc7231#section-6.6.4), the response code `503 (Service Unavailable)` indicates that the server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. In other words, a request that results in a response 503 is not the cause of the problem but only an indication that something has already broken the service.

To find out what caused the service problems, let's examine the events that occurred before the first request, which received a response of 503.

1. In the query input for the blue node, remove the last line containing the `makeTimeseries` command.
2. Add the following `filter` command to retrieve only requests resulting in the `503` response code:

   ```
   | filter response_code == 503
   ```
3. Add the following `summarize` command to take the minimum timestamp value from all results:

   ```
   | summarize min(timestamp)
   ```
4. Run the query.

   This creates a new node with a single value in the **timestamp** field.
5. Right-click on the timestamp in the results table and select **Set as reference time** to define it as a reference.

   You notice a reference time box on top of the page and a new virtual column called **timestamp\_diff** representing the offset between the timestamp value and your reference time. The reference time is `00:00:00.000` since the value in the **timestamp** field and the reference time are the same.

   ![reference-time](https://dt-cdn.net/images/2025-05-12-11-28-20-1423-b9a8d6eb0e.png)

   Multiple virtual offset fields can be in one result set; you can create a virtual field for any `timestamp` type.

3. Find a preceding error message

Using the reference time, let's look for the request that led to our service being unresponsive.

1. Navigate to the second (orange) node to see the Istio logs. You notice that the reference time offset field is present in this results table as well.
2. In the menu of the reference time box, select **Earlier than**. This [creates a timestamp filter](/docs/secure/investigations/filter-logs#reference "Narrow down data to relevant entries in Investigations.") to fetch logs written before the time of the reference timestamp value.

   ![timestamp filter](https://dt-cdn.net/images/2025-05-12-12-19-49-1920-3d859cdb64.png)
3. Rename `timestamp` to `start_time` in the timestamp filter command.

   **Reason**: When creating a reference time, the first timestamp field is used for filtering. In this case, the `timestamp` field is used. For Istio logs, we need to use the `start_time` field; this means you need to manually modify the filter and rename `timestamp` to `start_time` in the filter statement.
4. Add the `sort` command to sort results chronologically.

   Your DQL query should look similar to this:

   ```
   fetch logs, timeframe: "05:00:00Z/06:00:00Z"



   | filter k8s.cluster.name == "prod.cupid.cluster"



   | filter k8s.container.name == "istio-proxy"



   | parse content, "json{JSONTIMESTAMP:start_time, INT:response_code}(flat=true)"



   | filter start_time < toTimestamp("2025-05-12T05:32:01.000Z")



   | sort timestamp desc
   ```
5. Run the query.

   The first record in the results table contains an HTTP 500 response, which can indicate the request that might have caused the error in your system.

   ![response code 500](https://dt-cdn.net/images/2025-05-12-13-41-43-1920-26f19ab69f.png)
6. Right-click on the record's timestamp and select **Replace as reference time** to replace the current reference time with the value from the suspicious request.

4. Analyze application logs

You found the request that resulted in an HTTP 500 error in the Istio logs. However, to understand what happened to your application, you need to dig into the application logs.

1. Go to the first node of the query tree. Here, you can see all the containers and processes you have logs for.
2. In the query input, remove the `summarize` command.
3. Right-click on the `heartbeat-matcher-service` value in the `k8s.container.name` column, select **Filter**, and run the query.

   The results show all the application logs and their relative distance from when the error occurred (that is, the offset to our reference time).
4. In the reference time box menu, select `1 min` in the **Show surrounding logs** section, and then run the query.

   This allows you to look closely at the relevant events and filter to only those around your reference time.
5. In the timestamp column header, select **Sort ascending** to sort the results chronologically.

   When looking at the results, you can see all the requests and logged information about the incident time. Scrolling further down, you discover that a stack trace has been written to the logs at the exact moment of the reference time.

   ![stack trace](https://dt-cdn.net/images/2025-05-12-15-47-12-1920-0726580722.png)

## Conclusion

With reference time, you can efficiently navigate logs while maintaining the incident's time context. It helps you track the time offset between events youâre analyzing and when the incident occurred. This allows you to uncover relevant threads and evidenceâeven from logs and events that may initially seem unrelated.

Reference time integrates diverse information, ensuring a consistent incident context across all data points.