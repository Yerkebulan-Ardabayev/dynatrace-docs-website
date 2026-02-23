---
title: Detect problems with Logs
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-use-cases/lma-detect-problems-with-logs
scraped: 2026-02-23T21:35:56.369823
---

# Detect problems with Logs

# Detect problems with Logs

* Latest Dynatrace
* Tutorial
* 8-min read
* Published Oct 08, 2024

Quickly detecting and solving the problems in your environment is crucial to retaining a stable revenue and ensuring the trust of your customers. However, manually analyzing older application or third-party applications where you don't have access to the source code can be time-consuming.

Resolving a problem with Dynatrace drastically accelerates your Mean-time-to-Identify (MTTI) for critical issues, and increases your speed in fixing them before impacting customer experience, thus minimizing impact to your business from outages. By having a single observability platform for all signals, you reduce the risk for human errors from manual correlation of problem details.

Using Dynatrace allows you to avoid looking through all the existing records by showing you only the log lines directly related to the detected problem. This method also allows you to quickly inspect the error details such as message, status, and line of code (LOC) where the error has occurred.

![Problem Detection with Logs use case explanation](https://dt-cdn.net/images/obslab-logalerting-animated-c4b8056092.gif)

## What you will learn

This tutorial will guide you through the process of extracting relevant information from logs through OpenPipeline and accessing logs through the Problems app. It'll show you how to use DQL queries to find information relevant to your problem and get a deeper, more contextual view on the issue with traces.

By the end, you'll know how to

* Enrich logs with additional context as they are collected via OneAgent or OpenTelemetry
* Configure OpenPipeline to extract relevant information from logs and convert it to an event
* Use the Problems app to access relevant log lines
* Find the root cause with the help of logs

The example used in this guideline is taken from [Dynatrace Observability Lab: Problem Detection with Logsï»¿](https://dt-url.net/0jdt0unq). For the full experience, you can follow this hands-on demo. It explains the process of problem creation and test environment setup.

## Before you begin

### Prerequisites

* Access to a Dynatrace SaaS environment
* Access to OpenTelemetry demo or OneAgent
* Installed [Problems app](/docs/dynatrace-intelligence/davis-problems-app "Use the Problems app to quickly get to the root cause of incidents in your environment.")
* [Set up OpenPipeline ingestion](/docs/platform/openpipeline/getting-started/how-to-ingestion "How to ingest data for a configuration scope in OpenPipeline.")
* [Configured OpenPipeline](/docs/platform/openpipeline/getting-started/tutorial-configure-processing "Configure ingest sources, routes, and processing for your data in OpenPipeline.")

## Steps

This tutorial assumes that you're already monitoring your environment with Dynatrace.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Create a new pipeline for data extraction**](/docs/analyze-explore-automate/logs/lma-use-cases/lma-detect-problems-with-logs#step-1 "Use the Problems app and Logs to quickly detect and analyze arising problems.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Add a dynamic route for the pipeline**](/docs/analyze-explore-automate/logs/lma-use-cases/lma-detect-problems-with-logs#step-2 "Use the Problems app and Logs to quickly detect and analyze arising problems.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Access problems through the Problems app**](/docs/analyze-explore-automate/logs/lma-use-cases/lma-detect-problems-with-logs#step-3 "Use the Problems app and Logs to quickly detect and analyze arising problems.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**View Logs through the problem records**](/docs/analyze-explore-automate/logs/lma-use-cases/lma-detect-problems-with-logs#step-4 "Use the Problems app and Logs to quickly detect and analyze arising problems.")[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

**View details in Distributed Traces**](/docs/analyze-explore-automate/logs/lma-use-cases/lma-detect-problems-with-logs#step-5 "Use the Problems app and Logs to quickly detect and analyze arising problems.")

### Step 1 Create a new pipeline for data extraction

OpenPipeline is the Dynatrace data handling solution for data processing and ingestion. You can configure OpenPipeline to extract specific information relevant for your case and convert it into an event that can be alerted on. For more information on OpenPipeline processing capabilities, see [Processing in OpenPipeline](/docs/platform/openpipeline/concepts/processing "Learn the core concepts of Dynatrace OpenPipeline processing.").

To create a new pipeline

1. In **Dynatrace**, select  or press `Ctrl+K` to find and select **OpenPipeline**.
2. Go to **Logs**, select the **Pipelines** tab, and select  **Pipeline**.
3. Select  and change the pipeline name to `Log Errors`.
4. Select  to save your changes.
5. On the **Data extraction** tab, select  **Processor** and choose **Davis event**. This creates a new processor.
6. Fill in the required fields. The result should be similar to the example that follows this procedure.

   * Set **Name** to any name you like
   * **Matching condition** should be set to `true`
   * Set **Event name** to the following:

     ```
     [{priority}][{deployment.release_stage}][{deployment.release_product}][{dt.owner}] {alertmessage}
     ```
   * Set **Event description** to `{supportInfo} - Log line: {content}`
7. Set the following **Event properties**:

   Event property

   Value

   **event.type**

   `ERROR_EVENT`

   **dt.owner**

   `{dt.owner}`

   **dt.cost.costcenter**

   `{dt.cost.costcenter}`

   **dt.cost.product**

   `{dt.cost.product}`

   **deployment.release\_product**

   `{deployment.release_product}`

   **deployment.release\_stage**

   `{deployment.release_stage}`
8. Select **Save** to save your pipeline.

An example of creating a new Log Error pipeline

![An example of creating a new Log Errors pipeline](https://dt-cdn.net/images/log-errors-pipeline-example-1916-afc5178aef.png)

### Step 2 Add a dynamic route for the pipeline

Ingested and extracted data needs to be directed to the pipeline before it's processed. Creating a route is necessary to make sure that your data is directed to the right pipeline, especially in cases where you have multiple pipelines. For more information, see [Routing](/docs/platform/openpipeline/concepts/data-flow#routing "Learn how data flows in Dynatrace Platform, from ingestion to storage, via Dynatrace OpenPipeline.").

To add new dynamic routing

1. Go to **Logs**, select the **Dynamic routing** tab, and select  **Dynamic route**.
2. Fill in the required fields:

   * Set **Name** to any name you like
   * **Matching condition** should be set to

     ```
     isNotNull(alertmessage) and



     isNotNull(priority) and



     priority == "1"
     ```
3. Select **Add** to create a new dynamic route.

An example of creating a new dynamic route for Log Errors pipeline

![An example of creating a new route for Log Errors pipeline](https://dt-cdn.net/images/log-errors-new-dynamic-route-1918-4ad0eb9a7e.png)

### Step 3 Access problems through the Problems app

Once the problem is detected and recorded in logs, you can check its status in the Problems app.

The Problems app is a tool designed to help operational and site reliability teams reduce the mean time to repair (MTTR) by presenting every aspect of the incident. For more information, see [Problems app](/docs/dynatrace-intelligence/davis-problems-app "Use the Problems app to quickly get to the root cause of incidents in your environment.").

To access the Problems app

1. In **Dynatrace**, select  or press `Ctrl+K` to find and select the **Problems** app.
2. Select the open problem ID to see the record. Open problems are listed with a **Status** of `Active`.

![Problems app Errors-only list](https://dt-cdn.net/images/problems-app-errors-1918-89ccc3de72.png)

### Step 4 View logs through the problem records



A problem record shows you the number of events, SLOs, affected users, and affected entities. By default, the record shows you the affected deployment and a chart illustrating the problem. You can switch between **Chart** and **Properties**, as well as display **Deployment**, **Events**, or **Logs** connected to the problem.

![Problem record view](https://dt-cdn.net/images/problems-app-record-1912-8f5daeb578.png)

1. Select **Logs** to access logs from the problem record. On the **Logs** tab, you will see a chart of ingested records and a list of recommended queries that will help you analyze the problem faster.
2. Select **Run query** for  `Show x errors` where `x` is the number of errors recorded for your problem.
3. Select a log entry you want to expand. An expanded entry provides you with useful metadata like

   * Timestamp of the log line
   * `host.name` corresponding to the container name
   * `loglevel` (for example, `ERROR`)
   * OpenTelemetry or OneAgent `span_id` and `trace_id`
   * `dt.owner`, the owner of the component
   * `dt.cost.product` and `dt.cost.costcenter` corresponding to the cost information

Expanded log entry example

![Expanded log entry containing metadata information](https://dt-cdn.net/images/problems-app-show-errors-1646-e64b66e6ee.png)

4. Select **Show surrounding logs** to see the logs connected to the problem.

Surrounding logs view example

![Surrounding logs based on traces that show events connected to the error with the same trace_id](https://dt-cdn.net/images/surrounding-logs-traces-1834-bfc676163f.png)

5. Choose a filter for surrounding logs:

   * **based on trace** (default): display all logs with the same `trace_id`.
   * **based on topology**: show the error in the context of all logs for the failing service at the time of the error.

Logs related to the error, such as info events, may contain additional information that will help you in locating the root cause. Examples of additional information include:

* `statuscode` contains the error status code. For example, `FailedPrecondition`.
* `detail` contains the error message and the line of code where the error has occurred.

Related event additional information example

![Related info log with additional information statuscode and detail](https://dt-cdn.net/images/log-problem-debugging-with-logs-1802-ac039df62f.png)

### Step 5 View details in Distributed Traces

Traces provide you with a deeper view and additional context for the information available in logs. To be able to access traces through logs, you need to connect log data to traces via OpenTelemetry or OneAgent. To learn more about enriching logs with traces, see [Understand and fix multiple problems via logs and traces](/docs/observe/application-observability/distributed-traces/use-cases/problems-logs-traces "Use the log enrichment to view related log entries in the distributed traces view and enhance your analysis capabilities.").

To access traces through logs

1. Select the `trace_id` while you're in the expanded log view.
2. Go to **Explore**, select **Open field with**, and select **Distributed Traces** in the pop-up window.

The Distributed Traces app displays a chronological list of called functions, which you can use to make a step-by-step analysis of the problem. The failing point will be marked by a red line.

Distributed Traces app view example

![Distributed traces app displaying called methods with failing point marked red](https://dt-cdn.net/images/distributed-traces-problem-debug-with-logs-1860-966aefdd42.png)

## Summary

If you followed all the steps, you have:

* Created a pipeline designed for detecting errors.
* Found the root cause with the help of the Problems app and logs.

If your developer has provided you with a runbook that you can use as a guide for resolving errors, you can follow it as your next step.

Otherwise, your next step should be to contact the team responsible for maintaining the service or feature that led to an error. If you're a part of that team, you can begin the process of debugging the issue.