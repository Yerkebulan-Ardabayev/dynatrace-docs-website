---
title: Leverage log enrichment for traces to resolve problems
source: https://www.dynatrace.com/docs/observe/application-observability/distributed-traces/use-cases/problems-logs-traces
scraped: 2026-02-15T08:58:08.494451
---

# Leverage log enrichment for traces to resolve problems

# Leverage log enrichment for traces to resolve problems

* Tutorial
* 8-min read
* Published Jan 10, 2022

Logs are a crucial component for understanding the behavior of your environment. By combining logs with distributed traces, you can check log records in the full context of a transaction. Automatic contextualization of log data works out of the box for popular languages like Java, .NET, Node.js, Go, and PHP, as well as for NGINX and Apache web servers.

## Before you begin

Connect log data to traces for [Logs](/docs/analyze-explore-automate/logs/lma-log-enrichment "Connect your incoming log data to traces for more precise Dynatrace analysis.") or [Logs Classic](/docs/analyze-explore-automate/log-monitoring/log-monitoring-configuration/log-enrichment "Learn how you can connect your incoming log data to traces for more precise Dynatrace analysis."),

* Automatically via OneAgent features, for supported logging frameworks.
* Manually via open standards corresponding context information, for technologies that are not monitored by OneAgent or not supported out of the box yet.

## Use cases

Understand and fix multiple problems via logs and traces

### Scenario

The problem affects multiple services and combines a failure rate increase with response time degradation.

![Log analysis distributed trace - 6](https://dt-cdn.net/images/pp-log-analysis-10-1748-d69dbc6248.png)

### Steps

We begin our analysis with the affected Go service and check its [dynamic requests](/docs/discover-dynatrace/get-started/glossary#request "Get acquainted with Dynatrace terminology.").

![Log analysis distributed trace - 7](https://dt-cdn.net/images/pp-log-analysis-11-1505-1fd6fd3e99.png)

To investigate the failure rate, we select the **Failure rate** tile. This takes us to the **Failure rate** tab of the **Details** page.

![Log analysis distributed trace - 8](https://dt-cdn.net/images/pp-log-analysis-12-1912-d76c441a51.png)

The chart highlights the time period over which the failure rate increase occurred. To find out more, we select **Analyze failure rate degradation**.

![Log analysis distributed trace - 9](https://dt-cdn.net/images/pp-log-analysis-13-1906-6b41b2c5a8.png)

We immediately see that a lot of requests are affected and that Dynatrace suggests some possible root causes. We select **Details** for the first one to inspect that possible root cause.

The first extension on the list is an issue with a credit card payment, which has a serious impact on users, so that matter requires investigation. You can find related logs at the bottom of the page. For now, let's select **View all logs in the log viewer** to check all possible logs.

![Log analysis distributed trace - 2](https://dt-cdn.net/images/pp-log-analysis-2-1447-b5b36536ec.png)

We can see right away that there's a problem with loading shipping holidays. Expand a log record to see more. Among additional attributes, we can find the **trace\_id** property, which links the log record to a distributed trace.

![Log analysis distributed trace - 3](https://dt-cdn.net/images/pp-log-analysis-3-1427-7226617f24.png)

Select the value of the property to navigate to the related distributed trace. It contains a detailed overview of application behavior and user experience for this particular transaction.

![Log analysis distributed trace - 4](https://dt-cdn.net/images/pp-log-analysis-4-1461-bcd3cbdc49.png)

We can see at a glance that two traces are in an erroneous state. If we went through them, we'd find an error log for the `/cart` trace.

![Log analysis distributed trace - 5](https://dt-cdn.net/images/pp-log-analysis-6-1461-d8c0d325b5.png)

The log shows an error while attempting to load shipping holidays, so we can check this trace for more information, as it contains an error as well, hinting that it might be the cause of response time degradation.

Looking at the distributed trace, we conclude that there's something wrong with the **GetCart** service, which contributes significantly to the overall response time. If we check its logs, we'll find the **slow request** entry.

Now that we have identified components contributing to the problem, we can contact responsible teams and ask them to investigate.

Let's go back and check logs for more errors. Because we have attended to the shipping holiday problem, we can filter out those logs with [**advanced query** mode](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer#search "Learn how to use Dynatrace log viewer to analyze log data.").

![Log analysis distributed trace - 10](https://dt-cdn.net/images/pp-log-analysis-14-1890-6ccd1ed6f9.png)

Remaining logs indicate a problem with an unsupported card type. Let's expand the log and navigate to the distributed trace.

![Log analysis distributed trace - 11](https://dt-cdn.net/images/pp-log-analysis-15-1902-d9e4833047.png)

By going through the distributed trace, we can see that the application is functioning normally and that the problems are caused by an unsupported card type.

Because this is not something we can fix in our application, we contact our payment handling provider to see how this issue can be resolved.

As a side-effect of this analysis, we notice that the card number appears in the log, so we might also contact the responsible team to change logging rules to prevent logging of sensitive information.

Analyze automatically detected problems when the root cause is service failure

### Scenario

In this example, we analyze an online boutique, `HipsterShop`. It's a cloud-native microservices demo application that allows users to browse items, add them to a shopping cart, and purchase them.

![Dashboard - Logs in root cause analysis](https://dt-cdn.net/images/service-failure-logs-root-cause-analysis3-2560-78d5bf5753.png)

In the **Dashboard**, we see that two problems have been reported within a 24-hour timeframe.

### Steps

When we select the **Problems** tile to investigate them, we discover that `HipsterShop` has been affected by a JavaScript error rate increase that had consequences for end users. To get more details, we open the `P-2205042` problem.

![Overview of problems - Logs in root cause analysis](https://dt-cdn.net/images/service-failure-logs-root-cause-analysis1-1495-c6b7028ccb.png)

On the problem page, contextualized data allows us to understand the end user impact, how many users have been affected, and details about the newly occurring JavaScript error. Under **Root cause**, we learn that the problem originates from a configuration change on the Kubernetes workload `AdService`, which enables the **Expanded Ads** functionality.

![Problem details - Logs in root cause analysis](https://dt-cdn.net/images/service-failure-logs-root-cause-analysis2-2560-5f3a5d2a88.png)

By selecting **Analyze Failure rate degradation**, we get an overview of all failed requests, highlighting:

* Which requests failed.  
  In this case, problems affected the `GetAds` request.
* Exception details related to the failed requests.  
  In this case, `NullPointerException` was thrown in the `AdService` where an object was expected.
* **Related errors logs** and warnings.

![Failure analysis - Logs in root cause analysis](https://dt-cdn.net/images/service-failure-logs-root-cause-analysis4-1599-e7b264e724.png)

Logs in proactive troubleshooting (Kubernetes)

### Scenario

From the dashboard, we want to investigate the `frontend` service, which is deployed as a Kubernetes workload. To get information on the workload, we select the **frontend** Kubernetes workload tile.

![Dashboard - Logs for Kubernetes](https://dt-cdn.net/images/service-failure-logs-root-cause-analysis3-2560-78d5bf5753.png)

The workload details page lists all critical health metrics for the workload, such as its CPU and memory usage and limits of the underlying pods, but also response time, failure rate, and throughput for the deployed services. When one of the services (in our case, `frontend`) is affected by an error, you can investigate it via the service page or, as in our case, check the **Logs** section.

![Workload analysis - Logs for Kubernetes](https://dt-cdn.net/images/kubernetes-workload-log-analysis-958-0090d7c91c.png)

The log table shows the **Status** info. The red bars indicate that some errors are logged here. We can investigate them by filtering the available logs by **status** `error`. We see that all of them are related to a failed order process due to invalid or wrong credit card information. Because each of these log entries happens in the context of a distributed trace, we can also take a look at the related trace for specific log entries by selecting **View trace**.

![Distributed traces - Logs for Kubernetes](https://dt-cdn.net/images/distributed-traces-logs-k8-2560-90a6930d6e.png)

This reveals that the selected log entry on the Go-based `frontend` microservice is just part of a more complex error pattern. We see that it calls the `PlaceOrder` method of the `hipstershop.CheckoutService` downstream. By selecting this service, we can see that OneAgent automatically collects additional helpful information, for example, the fact that it is a gRPC call. By selecting the **Logs** tab we can see that during this call two log entries have been created, including the error message. Selecting **Show related entry 'Code level' tab**, we can also understand in which part of their Go microservice the specific logline was generated.

By selecting the NGINX `frontend reverse proxy` row, we can see that the call returned a `500 â Internal Server Error` to the client, which doesn't seem to be the correct error code for wrong credit card information.

![Summary tab of frontend revers proxy](https://dt-cdn.net/images/summary-tab-2560-bc9484ed00.png)

It now makes sense to discuss this behavior with the developers and see whether the `HTTP 400` would be a better code and to double-check the frontend app to see if this case is properly handled in the web UI.

## Learn more

Integrating Logs and Traces

## FAQ

What kind of pricing and packaging do I need to start?

You need both log monitoring and trace pricing and packaging.

Your technology is monitored via OneAgent

Learn more about pricing and packaging

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

* For logs, see [Log Management and Analytics (Grail)](/docs/license/monitoring-consumption-classic/davis-data-units/log-management-and-analytics "Understand how the volume of DDUs consumption is calculated for Dynatrace Log Management and Analytics.") or [Log Monitoring Classic](/docs/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Understand how the volume of DDU consumption is calculated for Dynatrace Log Monitoring Classic.").
* For traces (Full-Stack Monitoring), see [Application and Infrastructure Monitoring (Host Units)](/docs/license/monitoring-consumption-classic/application-and-infrastructure-monitoring "Understand how Dynatrace application and infrastructure monitoring consumption is calculated based on host units.")

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

* For logs, see [Log Management and Analytics (Grail)](/docs/license/monitoring-consumption-classic/davis-data-units/log-management-and-analytics "Understand how the volume of DDUs consumption is calculated for Dynatrace Log Management and Analytics.") or [Log Monitoring Classic](/docs/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Understand how the volume of DDU consumption is calculated for Dynatrace Log Monitoring Classic.").
* For traces (open trace ingestion with OpenTelemetry), see [DDUs for serverless functions](/docs/license/monitoring-consumption-classic/davis-data-units/serverless-monitoring "Understand how serverless monitoring consumption is calculated.") and [DDUs for custom traces (Trace API)](/docs/license/monitoring-consumption-classic/davis-data-units/custom-traces "Understand how DDU consumption is calculated for spans ingested via the Trace API.")

Can I use this data for end user sessions?

Yes. To learn how, see [Connect your log data to user sessions and Session Replays](/docs/whats-new/saas/sprint-244#connect-your-log-data-to-user-sessions-and-session-replays "Release notes for Dynatrace SaaS, version 1.244").

## Related topics

* [Log viewer (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer "Learn how to use Dynatrace log viewer to analyze log data.")
* [Dynatrace Intelligence](/docs/dynatrace-intelligence "Get familiar with the capabilities of Dynatrace Intelligence.")
* [[Blog] Automatic connection of logs and traces accelerates AI-driven cloud analyticsï»¿](https://www.dynatrace.com/news/blog/automatic-connection-of-logs-and-traces-accelerates-ai-driven-cloud-analytics/)