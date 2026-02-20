# Документация Dynatrace: observe/application-observability
Язык: Русский (RU)
Сгенерировано: 2026-02-20
Файлов в разделе: 66
---

## observe/application-observability/distributed-traces/analysis/connect-environments.md

---
title: Set up cross-environment tracing
source: https://www.dynatrace.com/docs/observe/application-observability/distributed-traces/analysis/connect-environments
scraped: 2026-02-20T21:20:36.063591
---

# Set up cross-environment tracing

# Set up cross-environment tracing

* How-to guide
* 6-min read
* Updated on Jun 04, 2024

In multiple environment scenarios, data pools are separated. If a request affects services that are monitored in different Dynatrace environments, its traces aren't automatically correlated.

To correlate and follow such traces, you can configure a connection between the Dynatrace environments and enable the response header and coordinated sampling switches. The service flow then represents the connection between the connected environments, distributed traces link to the connected remote environment, and you can access DavisÂ® AI analysis capabilities.

## Configuration

### Before you begin

Limitations

* Cross-environment tracing is limited to traces of requests that can transfer information about response headers and trace context from the receiving environment, such as HTTP or synchronous requests.
* IBM z/OS (CICS, IMS, and Java) and AWS Lambda don't support cross-environment tracing.

Prerequisites

* Make sure that a direct network connection between the clusters can be established via HTTP/HTTPs.

API equivalents

The procedures that follow use the Dynatrace web UI. To carry out the equivalent tasks via API, see:

* [Access tokens API](/docs/dynatrace-api/environment-api/tokens-v2/api-tokens "Manage Dynatrace API authentication tokens.")âto create a token in the remote environment
* [Remote environments API](/docs/dynatrace-api/configuration-api/remote-environments "Manage configurations of remote Dynatrace environments via the Dynatrace configuration API.")âto create a link to the remote environment from the local environment

### Steps

1. Create an access token

With this procedure, you get an access token from the remote environment that you need in the other steps.

To create an access token in the remote Dynatrace environment

1. Sign in to the remote environment.

   * This is the environment from which you pull data.
   * If you can't sign in to the remote environment, someone with access to the remote environment can do this procedure for you.
2. Go to **Access Tokens**.
3. Select **Generate new token**.
4. Enter a token name.
5. Find and select the following scopes:

   * **Look up a single trace** (`traces.lookup`)
   * **Fetch data from a remote environment** (`RestRequestForwarding`)
6. Select **Generate token**.  
   This generates a token that gives your local environment permission to check the existence of a trace in a remote environment and to pull data from a remote environment.
7. Select **Copy** and then paste the token to a secure location.  
   It's a long string that you need to copy and paste back into Dynatrace later.

2. Add the remote environment

To add the remote Dynatrace environment to the list of available remote environments

1. Sign in to your local Dynatrace environment.
2. Go to **Settings**.
3. Select **Integration** > **Remote environments**.
4. Select **Connect environment**.
5. Define the remote environment from which your local environment pulls data, and then select **Save changes**.

   * **Name** is the name under which the remote environment will be listed in your current Dynatrace environment. This is freeform text. It doesn't affect the remote environment.
   * **Remote environment URI**

     + For Dynatrace SaaS, it needs to be in the following format:

       `https://<ENVIRONMENTID>.live.dynatrace.com/`

       Replace `<ENVIRONMENTID>` with your actual environment ID.
     + For Dynatrace Managed, any URI is allowed.
     + To connect a Dynatrace (SaaS deployment) environment to a Dynatrace Managed deployment via a URI that is outside the `dynatrace-managed.com` domain, contact a Dynatrace product expert via live chat within your Dynatrace environment.
   * **Network scope**

     + `External`: The remote environment is located in another network. Globally configured proxy settings are used if present. This is the default scope.
     + `Internal`: The remote environment is located in the same network. Globally configured proxy settings are not used.
     + `Cluster`: The remote environment is located in the same cluster. The request is made to `localhost`.

     Dynatrace SaaS can only use the `External` network scope.
   * **Token** is the token you generated in the previous procedure. It needs to include the **Look up a single trace** scope (`traces.lookup`).
   * **Test connection** checks the connection from your current environment to the remote environment.

     Be sure to get a `connection successfully established` message before continuing.

3. Enable the features

Enable the following features in each environment of the group that you want to connect:

* **Coordinated sampling**

  You can increase the consistency of cross-environment tracing with coordinated sampling. When you enable the switch, sampling is coordinated across environments with the help of the W3C trace ID.

  1. Go to **Settings** > **Preferences** > **OneAgent features**.
  2. Set W3C trace context propagation according to your preferences.  
     You can send W3C trace context HTTP headers or gRPC headers.
  3. Find and turn on **Cross-environment tracing - Coordinated sampling**.
* **Response headers**

  You can enable the identification and tracking of cross-environment calls, including the environment ID and the trace ID in HTTP response headers. If the calling environment receiving the response has the environment configured as a trusted remote environment, the call destination is linked.

  1. Go to **Settings** and select **Preferences** > **OneAgent features**.
  2. Find and turn on **Cross-environment tracing - Environment and transaction IDs in HTTP response headers**.

Now that you have connected your environments, you can analyze traces across cross-connected remote environments.

### Troubleshooting

[`Verification failed, please check your settings: Constraints violated.` message displayed when adding a remote environmentï»¿](https://dt-url.net/t903mr6)

## Analyze cross-connected remote environments

Once you configure a connection between environments, the following specific analysis options are available.

### Service overview

Dynatrace detects requests to connected Dynatrace environments and uses the available information to create an associated **Remote environment** web service or web request service.

![Remove environment service overview](https://dt-cdn.net/images/cross-environment-4-1608-af340752cb.jpeg)

* Outgoing calls to connected environments are represented in **Smartscape** and **Service flow**.

  ![Remote environment service in Smartscape topology](https://dt-cdn.net/images/cross-environment-1-1202-a48e0448d7.jpeg)
* All the services monitored by the remote environment and contributing to the request are listed on the **Remote environments** page. To open it, select **Open environment** on a **Remote environment** service page.

### Service flow

**Service flow** recognizes remote environment calls. Because the requests are monitored by another Dynatrace environment, a specific drill-down option is available when you select the remote environment call. In the side pane, select **Open environment** to access the **Remote environments** page.

![Remove environment in service flow analysis](https://dt-cdn.net/images/cross-environment-2-1531-85c4a673fc.jpeg)

### Distributed traces

* When a request goes to a connected remote environment, Dynatrace displays the remote environment name in the call tree.

  To follow the trace in the remote environment

  1. Select the remote environment request.
  2. In the **Summary** tab, select **Open environment**.
* If the environments' connection is configured correctly, Dynatrace automatically displays the call **Aggregated requests**. It aggregates all the data of detected requests on each respective connected remote environment.

  If you configured a connection to the remote environment but you can't see requests on it, you can trigger a manual search for the trace in configured environments. In the upper-right corner of the trace page, select **Find in remote environments**.

### Davis AI

Once Dynatrace creates the remote environment service, problems and events are correlated to the affected remote environment service.

You can use [Davis AI](/docs/dynatrace-intelligence "Get familiar with the capabilities of Dynatrace Intelligence.") capabilities to understand which requests are failing and discover the root cause of problems in the remote environment.

![ Davis AI problem analysis of remote environment service](https://dt-cdn.net/images/cross-environment-3-1600-8b1ae112a1.jpeg)

## Related topics

* [What is a monitoring environment?](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.")
* [Create remote/multi-environment Dynatrace dashboards](/docs/analyze-explore-automate/dashboards-classic/dashboards/dashboards-multi-environment "Create dashboards that display data from multiple Dynatrace environments.")
* [Remote environments API](/docs/dynatrace-api/configuration-api/remote-environments "Manage configurations of remote Dynatrace environments via the Dynatrace configuration API.")

---

## observe/application-observability/distributed-traces/analysis/diagnostic-messages.md

---
title: Treat diagnostic messages
source: https://www.dynatrace.com/docs/observe/application-observability/distributed-traces/analysis/diagnostic-messages
scraped: 2026-02-20T21:27:57.849044
---

# Treat diagnostic messages

# Treat diagnostic messages

* 4-min read
* Updated on Jun 10, 2023

Captured distributed traces are the main source of data for Dynatrace DavisÂ® causal AI. Because Davis relies on high data quality and fidelity, certain standards must be met to analyze the collected data; all services, methods, timings, properties, and so on must be correctly captured and transmitted. If this doesn't happen, you'll be informed of the issue via a diagnostic message for the affected traces.

* In case the correct service can be determined, distributed traces with diagnostic messages are listed on the service's **Distributed traces** page, along with all other distributed traces related to the service.

  ![Distributed traces diagnostic message - capture error](https://dt-cdn.net/images/distributed-traces-capture-error-3112-189ed8979d.png)
* In case a related service can't be determined, for example, because of a missing service name or type, distributed traces are listed as **Unexpected services** in the list of services of the process for which distributed traces have been captured.

  Unexpected services may be caused by network issues (data lost in transition) or by the abrupt termination of the process (restart or scaling).

## Troubleshoot diagnostic messages

Via the content of diagnostic messages, you can understand the possible causes of missing capture or transmission of data and to what extent DavisÂ® AI can rely on the collected data. Sometimes diagnostic messages are symptoms of a setup issue that requires investigation.

To maintain good data quality, we recommend that you

* Use network error patterns to identify the source of a problem.

  For example, if all requests of a specific service have network-related errors, the cause may be a short-living process that isn't sending data to Dynatrace.
* Reduce the number of [request attributes](/docs/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.") or change the definitions of [custom services](/docs/observe/application-observability/services/service-detection/service-detection-v1/service-types/custom-services "Define entry points (a method, class, or interface) for custom services that don't use standard protocols.") to reduce the number of requests.

## Truncation of trace data

A trace can be truncated because data isn't fully acquired, correlated, or visualized. This typically occurs when limits established to protect your environment's resources are exceeded. When trace data is truncated, you get a specific diagnostic message.

If you've configured [cross-environment tracing](/docs/observe/application-observability/distributed-traces/analysis/connect-environments "Analyze requests across environment boundaries."), data fetched from remote environments isn't truncated but aggregated.

While limits that protect your environment's resources can't usually be removed, you might influence truncation by intervening at the source of the problem. The following list includes some suggestions to help reduce the truncation of trace data.

* Reduce the number of nodes sent per trace, for example, by modifying custom services and OneAgent features active in your environment.

  OneAgent can send a limited number of nodes per trace. Once it runs into resource limitations, new nodes are no longer created. The trace is truncated at ingestion, and new incoming data isn't added to the trace. This can affect the correlation of entities and undermine your data quality.
* Investigate traces running for extended lengths of time.

  To protect your environment's resources, action is taken when traces run for extended lengths of time. For example, traces that are no longer active after running for 90 minutes are timed out, while traces for which the start time of the call is too far in the past are truncated. In both cases, new data isn't added to the trace. This can affect the correlation of entities and data quality.
* Investigate traces with limited or excessive amounts of data.

  + When trace data doesn't contain sufficient metadata on networks or not all nodes were received, correlating entities might be unsuccessful, leading to truncated traces.
  + When a call has too many in-progress dependencies or the trace has too many nodes, such a trace is truncated. We recommend investigating the related service and, in case of custom services, getting in touch with a Dynatrace product expert via live chat within your environment.
* Adapt the full-trace view to visualize the data you need.

  The full-trace view in Dynatrace is typically large enough to display the most important information for the entire trace. However, formatting can be modified to help you visualize all the data you need.

  Format element

  Initial setup

  Adaptation

  Time range

  For the current time range, select **More** (**â¦**) in the upper-right corner of the full-trace view and hover over **Refine analysis**.

  To increase the time range, select **Refine analysis**.

  Visible requests

  In the [**Code level** tab](/docs/observe/application-observability/distributed-traces/analysis/get-started#code-level-tab "Get started with distributed trace analysis in Dynatrace."), you can see service calls up to 100,000 nodes.

  To change this limit, contact a Dynatrace product expert via live chat within your Dynatrace environment.

---

## observe/application-observability/distributed-traces/concepts.md

---
title: Distributed traces concepts
source: https://www.dynatrace.com/docs/observe/application-observability/distributed-traces/concepts
scraped: 2026-02-19T21:17:42.544336
---

# Distributed traces concepts

# Distributed traces concepts

* Explanation
* 1-min read
* Published Mar 30, 2021

In this article, you will learn about the most important concepts and terminology for distributed tracing in Dynatrace.

![Relation between Services and Traces and Spans](https://dt-cdn.net/images/distributed-traces-obs-1280-3f571c7197.png)

### Distributed trace

A distributed trace is a sequence of spans, identified by a unique trace ID, that follows the path of a single request as it traverses through various services and components in a distributed system. In a modern microservice environment, it typically spans multiple services, providing a detailed view of the request's journey and performance. The trace contains semantically different attributes that make it possible to interpret and understand the collected data, helping identify bottlenecks, errors, and latency issues for efficient troubleshooting and optimization.

![Traces and services](https://dt-cdn.net/images/traces-services-1920-59a6506038.png)

#### Use cases

* Understand how requests propagate across distributed systems and microservices.
* Use high-quality data generated by distributed systems and microservices for request analysis.
* Quickly understand how each microservice is performing.
* Follow [Dynatrace Intelligence root cause analysis drill-downs](/docs/dynatrace-intelligence/root-cause-analysis/concepts "Get acquainted with root cause analysis concepts.") to identify cause-effect relationships between events.

### Span

A span represents a single operation within a distributed trace, capturing the details of the request's journey through multiple services. Each span includes attributes such as the name, the start timestamp, a list of span events (such as exceptions), the parent's span identifier, and the span kind. This informationâ**span context**â helps to put all spans and events in context with each other, so that you can trace and understand the performance and behavior of individual operations within the distributed system.

Within a trace, when the activityâ*parent span*âis completed, the next activity passes to its *child span*. A span without a parent span is called a trace *root span* and indicates the start of a trace.

The image below shows a trace traversing three services and producing a request for each service. Each request has a root span, one of which is also the root of the trace.

* A is both the first span of the trace and the first span of the request within the first service; additionally, A is a span without a parent. A is both the root of the trace and of the request.
* C is the first span of the request within the second service; additionally, C has a parent (B). C is the root of the second request.
* E is not the first span of the request within the third service. E's parent (D) is the root of the third request.

![Trace anatomy](https://dt-cdn.net/images/trace-anatomy-1920-6ba49e1863.png)

Learn more about [span semantic fields](/docs/semantic-dictionary/fields#span "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.").

The span context allows a child span to relate to the trace and its parent span. Therefore, the context needs to be propagated within a service (across different threads) but also across services and process boundaries. This typically happens via HTTP headers (like the [W3C trace contextï»¿](https://www.w3.org/TR/trace-context/)) or via unique IDs in messaging systems. To learn more about context propagation, see [Span and trace context propagation in Distributed Traces Classic](/docs/observe/application-observability/distributed-traces/context-propagation "Understand span and trace context propagation in Dynatrace and how to set them up.").

### Attribute

Attributes are key-value pairs that provide details about a span, request, or resource such as response codes, HTTP methods, and URLs. Via attributes, you can group, query, find, and analyze your traces and spans.

#### Use cases

Dynatrace uses attribute metadata to

* [Detect and name services](/docs/observe/application-observability/services/service-detection/service-detection-v1 "Find out how Dynatrace Service Detection v1 detects and names different types of services.").
* Gather data on the trace context and relationships with other entities for [Smartscape topology](/docs/analyze-explore-automate/smartscape-classic "Learn how Smartscape Classic visualizes all the entities and dependencies in your environment.").
* Connect log data to traces for [Logs](/docs/analyze-explore-automate/logs/lma-log-enrichment "Connect your incoming log data to traces for more precise Dynatrace analysis.") or [Logs Classic](/docs/analyze-explore-automate/log-monitoring/log-monitoring-configuration/log-enrichment "Learn how you can connect your incoming log data to traces for more precise Dynatrace analysis.").
* Understand how the duration of a span is affected by [service timings](/docs/observe/application-observability/services-classic/service-analysis-timing "Find out what each time in service analysis means.") (for example, CPU time, network time, or just waiting for other threads) and analyze which code was executed in the context of the span.

#### Best practices

If you collect trace data via

* OpenTelemetry, define [captured attribute settings](/docs/ingest-from/extend-dynatrace/extend-tracing/span-settings "Learn how to configure span settings for OpenTelemetry and OpenTracing.").
* OneAgent, define [requests attribute settings](/docs/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.").

Learn more about [request attributes](/docs/semantic-dictionary/fields#request-attributes "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.") and [captured attributes](/docs/semantic-dictionary/fields#captured-attributes "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.") semantic fields.

### Service

Services are traversed by distributed traces. On horizontally scaled services, specific **Service Instances** process each span. Services are determined and named based on available attributes or properties that are collected along with the spans.

#### Use cases

* [Segment requests to improve response time degradation](/docs/observe/application-observability/distributed-traces/use-cases/segment-request "Enhance your distributed system performance by segmenting requests with slow response time via Service flow and analyzing their distributed traces.").

### Data collection and context propagation

You can integrate OpenTelemetry and OneAgent to collect trace dataâlike request status, response time, versions, infrastructure information, and other relevant metadata as attributes. The trace context, including the unique trace ID, is then propagated across your apps and microservices.

#### Best practices

Before getting started with distributed tracing, understand how setup and trace data collection differs between OpenTelemetry and OneAgent. The following is an overview of the key differences.

OpenTelemetry

OneAgent

Set up

Automatic or manual

Automatic

Capturing

Automatic collection of allowed span attributes.

Automatic collection of several request attributes, including HTTP method, URL, response codes, topology data, and details about the underlying technologies.

Context

Automatically or manually contextualized log entries, depending on the instrumentation library.

Automatically contextualized

* Log entries produced by prominent log frameworks.
* Traces in Smartscape and Dynatrace Intelligence.

To get started see

* [Automatic setup with OneAgent](/docs/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.")
* [Instrumentation with OpenTelemetry](/docs/ingest-from/opentelemetry/getting-started "How to get your OpenTelemetry data into Dynatrace.")
* [Extend distributed tracing](/docs/ingest-from/extend-dynatrace/extend-tracing "Learn how to extend trace observability in Dynatrace.")

Use OpenTelemetry in combination with OneAgent to enhance your observability coverage, using the best of both.

### PurePathÂ® technology

Dynatrace patented PurePathÂ® technology for distributed tracing, since 2006. PurePathÂ® technology combines distributed tracing information with additional insights like user experience information, logs, metrics, topology information, metadata, and even code-level profiling information to provide the highest level of data fidelity and granularity.

#### Use cases

Analyze data down to code-level detail without ever losing the full context around your environment during drill down, with the highest level of data granularity and fidelity of monitored transactions.

---

## observe/application-observability/distributed-traces/context-propagation.md

---
title: Span and trace context propagation in Distributed Traces Classic
source: https://www.dynatrace.com/docs/observe/application-observability/distributed-traces/context-propagation
scraped: 2026-02-18T05:56:56.844487
---

# Span and trace context propagation in Distributed Traces Classic

# Span and trace context propagation in Distributed Traces Classic

* Explanation
* 2-min read
* Published Feb 02, 2026

## Trace context across services

Dynatrace provides continuous visibility into service flows by propagating trace context as transactions move between services and components. This propagation is essential for end-to-end monitoring of distributed applications.

## Automatic propagation with OneAgent

When you install OneAgent, it automatically:

* Injects trace context into outgoing requests.
* Reads trace context from incoming requests.
* Maintains transaction context across service boundaries.
* Uses various mechanisms to correlate distributed traces, allowing Dynatrace to show the complete transaction flow through your application.

## Propagation mechanisms

Dynatrace employs several mechanisms to maintain trace context:

* **x-dynatrace**âfor various communication protocols. This format is proprietary to Dynatrace.
* **traceparent** and **tracestate**âW3C standard format used by both OneAgent and OpenTelemetry.
* **dtdTraceTagInfo**âcustom property for various messaging systems.

The exact implementation varies by technology: sometimes using HTTPS headers, SQS message properties, or AWS EventBridge payload injection.

## Mixed environments with OpenTelemetry

In mixed environments with both OneAgent and OpenTelemetry instrumentation, trace context propagation bridges the gap:

* Both OneAgent and OpenTelemetry use the W3C Trace Context format.
* The context must be propagated consistently across the communication channel.
* For HTTP, this is standardized in headers.
* For other protocols such as messaging and events, you need to be consistent with placement between OneAgent and OpenTelemetry.

## Turning on W3C trace context

There are several reasons to turn on W3C trace context in Dynatrace:

* Industry standard compatibilityâit aligns with W3C specification.
* Vendor-agnostic tracingâit works in heterogeneous environments with multiple monitoring solutions.
* Future-proofingâit matches industry direction for distributed tracing.

### Considerations when using W3C trace context

* Interoperability challengesâdespite being a standard, real-world implementation can vary.
* Browser and app behaviorâsome clients may send the same traceId repeatedly, affecting trace quality.
* Tool conflictsâmultiple APM tools in the same process may overwrite each other's context.

### Set up W3C trace context

To turn W3C trace context on

**Latest Dynatrace**

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **General monitoring settings** > **OneAgent features**.
2. Turn on **Send W3C Trace Context HTTP headers** and **Send W3C Trace Context gRPC headers**.

**Dynatrace Classic**

1. Go to **Settings** > **Preferences** > **OneAgent features**.
2. Turn on **Send W3C Trace Context HTTP headers** and **Send W3C Trace Context gRPC headers**.

While the W3C standard formally specifies HTTP propagation, Dynatrace and the broader industry apply these concepts to other communication protocols.

---

## observe/application-observability/distributed-traces/use-cases/problems-logs-traces.md

---
title: Leverage log enrichment for traces to resolve problems
source: https://www.dynatrace.com/docs/observe/application-observability/distributed-traces/use-cases/problems-logs-traces
scraped: 2026-02-20T21:17:50.537773
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

---

## observe/application-observability/distributed-traces/use-cases/segment-request.md

---
title: Segment requests to improve response time degradation
source: https://www.dynatrace.com/docs/observe/application-observability/distributed-traces/use-cases/segment-request
scraped: 2026-02-20T21:08:03.818974
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

---

## observe/application-observability/distributed-traces.md

---
title: Distributed Traces Classic
source: https://www.dynatrace.com/docs/observe/application-observability/distributed-traces
scraped: 2026-02-20T21:18:14.774245
---

# Distributed Traces Classic

# Distributed Traces Classic

* Overview
* 1-min read
* Updated on May 17, 2024

Distributed tracing is an essential monitoring, debugging, and optimizing tool for distributed software architectures. By visualizing how different services are connected and how your requests travel through various tiers of an application, it helps teams to quickly understand the performance of each microservice.

[### Concepts

Learn the core concepts and terminology of distributed tracing in Dynatrace.](/docs/observe/application-observability/distributed-traces/concepts "Learn more about distributed tracing core concepts and terminology.")[### Context propagation

Understand span and trace context propagation in Dynatrace and how to set them up.](/docs/observe/application-observability/distributed-traces/context-propagation "Understand span and trace context propagation in Dynatrace and how to set them up.")[![Distributed Traces Classic](https://dt-cdn.net/images/distributed-traces-classic-7197cdacfb.svg "Distributed Traces Classic")

### Analyze

Analyze distributed traces.](/docs/observe/application-observability/distributed-traces/analysis/get-started "Get started with distributed trace analysis in Dynatrace.")[![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing")

### Distributed tracing powered by Grail

Latest Dynatrace

Upgrade Distributed Traces Classic ![Distributed Traces Classic](https://dt-cdn.net/images/distributed-traces-classic-7197cdacfb.svg "Distributed Traces Classic") to Distributed Tracing ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") app and discover distributed tracing powered by Grail.](/docs/observe/application-observability/distributed-tracing "Trace and analyze in real time highly distributed systems with Grail.")

## Related topics

* [Application Observability](/docs/observe/application-observability "Get familiar with application observability capabilities in Dynatrace.")

---

## observe/application-observability/distributed-tracing/advanced-tracing-analytics.md

---
title: Advanced Tracing Analytics powered by Grail
source: https://www.dynatrace.com/docs/observe/application-observability/distributed-tracing/advanced-tracing-analytics
scraped: 2026-02-20T21:08:23.762942
---

# Advanced Tracing Analytics powered by Grail

# Advanced Tracing Analytics powered by Grail

* Latest Dynatrace
* Tutorial
* 2-min read
* Updated on Aug 28, 2025
* Preview

Advanced Tracing Analytics powered by Grail is designed for experienced users who require advanced tracing analysis that can be consumed via [Dashboards](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time."), [Notebooks](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace."), [Workflows](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services."), and via the [Dynatrace API](/docs/dynatrace-api "Find out what you need to use the Dynatrace API.").

## Before you begin

Prerequisites

* Make sure your user has [permissions](/docs/observe/application-observability/distributed-tracing/permissions "Manage permissions for Distributed Tracing powered by Grail.") necessary to access trace data.
* [Traces powered by Grail overview (DPS)](/docs/license/capabilities/traces "Learn how Dynatrace Traces powered by Grail consumption is calculated using the Dynatrace Platform Subscription (DPS) model.").

Prior knowledge

* [Distributed Tracing concepts](/docs/observe/application-observability/distributed-tracing#main-content--concepts "Trace and analyze in real time highly distributed systems with Grail.")
* [Semantic model for Traces](/docs/semantic-dictionary/model/trace "Get to know the Semantic Dictionary models related to traces.")

## Access spans and span attributes via DQL

A span represents a logical unit of work within the trace and is described by span attributes. Span attributes are set by the instrumentation that creates the span and provides detailed information on the span, including the kind of operation it represents and context on its origin. The semantics of all the fields are documented in [Dynatrace Semantic Dictionary](/docs/semantic-dictionary "The Semantic Dictionary defines standardized field names used across monitoring data types like logs, events, spans, metrics, and entities."). With DQL you can

* Access every single span via the command `fetch spans`. Combine it with DQL functions to query any span attribute stored in Grail without additional configuration.
* Fully search any span attribute of type `string`, via [string function available in DQL](/docs/platform/grail/dynatrace-query-language/functions/string-functions "A list of DQL string functions."), such as `startsWith`, `endsWith`, `contains`, or `matchesPhrase`.

Example: DQL access to all spans

The following example query fetches spans with an HTTP request header and, for each span, shows the values of the endpoint name, the HTTP request header and method and the trace ID.

```
fetch spans



| filter isNotNull( http.request.header.host)



| fields endpoint.name, http.request.header.host, http.request.method, trace.id



| limit 5
```

Query result:

endpoint.name

http.request.header.host

http.request.method

trace.id

`/api/currency`

`astroshop.playground.demoability.dynatracelabs.com`

`GET`

`86b11c85e1bc1dc039252a95fd009d16`

Example: DQL access to all attributes

The following query fetches spans generated with an HTTP route from the server. To make sure all spans use the same field name for the HTTP request method field, it looks for two semantically different fields and stores the first result into a new field for consultation purposes. It then summarizes the results by HTTP request method and HTTP route, providing the number of spans, their average duration, and the value of their duration in the 50th percentiles.

```
fetch spans



| filter span.kind == "server" and isNotNull(http.route)



| fieldsAdd http.request.method = coalesce(http.request.method, http.method)



| summarize { count(), avg(duration), p50=percentile(duration, 50)}, by: { http.request.method, http.route }



| limit 3
```

Query result:

http.request.method

http.route

count()

avg(duration)

p50

`POST`

`/v1/orders/{id}/status`

`758`

`84.28 ms`

`78.11 ms`

Example: Full text search

The following example fetches spans with an HTTP route that contain `user` and don't end with `username` and summarizes the results, providing the number of spans by HTTP request method and HTTP route.

```
fetch spans



| filterOut isNull(http.route)



| filter contains(http.route, "v1/") and not endsWith(http.route, "/sell")



| summarize count(), by: { http.request.method, http.route }
```

Query result:

http.request.method

http.route

count()

`POST`

`v1/balance/{accountId:int}/deposit`

`458`

For more examples, see the [Introductionï»¿](https://wkf10640.apps.dynatrace.com/ui/document/v0/#share=404274dc-4f04-4dda-840d-47ba9bd17a9f) notebook in Dynatrace Playground.

## HTTP requests and networking



You can analyze your Web Requests via DQL and

* Get information on the duration of span data via the `summarize` function.
* Extract a timeseries from span raw data via the `makeTimeseries` command and filter results by any span attribute.
* Analyze requests.
* Aggregate results by request ID (OneAgent required).

Example: Summarize duration

In the following example, the query fetches spans that contain the HTTP route with a specific string value (`services`) and summarizes the results by duration. The duration is expressed in buckets of 100ms increments, ordered from lowest to highest value. Each bucket aggregates the response times of a number of spans, which are represented by a random trace picked among the aggregated values.

```
fetch spans



// filter for specific HTTP route



| filter contains(http.route, "services")



| summarize {



spans=count(),



trace=takeAny(record(start_time, trace.id)) // pick random trace from aggregation bucket



}, by: { bin(duration, 100ms) }



| fields `bin(duration, 100ms)`, spans, trace.id=trace[trace.id], start_time=trace[start_time]
```

Query result:

bin(duration, 100ms)

spans

trace.id

start\_time

`300.00ms`

`342`

`4e990942081eb61ac0e39399555ebb2a`

`2025-05-27T08:04:04.229120000+02:00`

Example: Extract timeseries

Via the `makeTimeseries` command, you can extract a timeseries from raw span data and use span attributes to filter, aggregate, or group the results. This on-the-fly approach supersedes the limitation of materialized timeseries (metrics) that require sets of dimensions defined up-front.

The following query fetches spans that contain a specific HTTP route and extracts a timeseries based on the results.

```
fetch spans



// filter for specific http route



| filter contains(http.route, "services") and http.request.method == "GET"



// extract timeseries



| makeTimeseries { avg=avg(duration) }



, by: { http.route }, bins:250
```

Example: Request analysis

A request is an incoming call identified in Dynatrace by the key-value pair `request.is_root_span: true`. You can analyze requests using the fields function to extract specific information or track issues such as failed requests by using `request.is_failed: true`. For example, you can query failed requests and display relevant details, including the associated endpoint, to pinpoint where issues occur.

Requests typically also contain the endpoint, a name that represents a specific path or resource within a service where requests are directed. It represents the entry point for interactions, such as an API routeâfor example, `/api/orders`âor a method.

The following query fetches failed requests and displays the values of the specified fields.

```
fetch spans



// filter only for request root spans



| filter request.is_root_span == true



| filter request.is_failed == true



| fields trace.id, span.id, start_time, response_time = duration, endpoint.name



| limit 100
```

Example: Request aggregation via request ID (OneAgent required)

In the following example, the goal is to gather information on the child spans of the requests. The `request.id` is leveraged to aggregate the results since all spans that belong to a single request carry its ID.

```
fetch spans



// request.id is pre-requisite for this query. not always present



| filter isNotNull(request.id)



| summarize {



spans = count(),



client_spans = countIf(span.kind == "client"),



span_events = sum(arraySize(span.events)),



// from all spans in the summarized group, select the one that is the request root



request_root = takeMin(record(



root_detection_helper = coalesce(if(request.is_root_span, 1), 2 /* INVALID */),



start_time, endpoint.name, duration



))



}, by: { trace.id, request.id }



// reset request_root to NULL if root_detection_helper is invalid



| fieldsAdd request_root=if(request_root[root_detection_helper] < 2, request_root)



| fieldsFlatten request_root | fieldsRemove request_root.root_detection_helper, request_root



| fields



start_time = request_root.start_time,



endpoint = request_root.endpoint.name,



response_time = request_root.duration,



spans,



client_spans, span_events,



trace.id



| limit 100
```

Example: Trace aggregations

A full trace consists of many spans. You usually want to identify a trace by the first request it started with; the "root request".

The following query finds the root request span and additionally does aggregations over the whole trace, based on an aggregation on the `trace.id`.

```
fetch spans



| summarize {



spans = count(),



client_spans = countIf(span.kind == "client"),



span_events = sum(arraySize(span.events)),



// endpoints involved in the trace



endpoints = toString(arrayRemoveNulls(collectDistinct(endpoint.name))),



// hosts involved in the trace



hosts = arrayRemoveNulls(collectDistinct(host.name)),



// from all spans in the summarized group, select the one that is the first request root in the trace



trace_root = takeMin(record(



root_detection_helper = coalesce(if(request.is_root_span, 1), if(isNull(span.parent_id), 2), 3),



start_time, endpoint.name, duration



))



}, by: { trace.id }



| fieldsFlatten trace_root | fieldsRemove trace_root.root_detection_helper, trace_root



| fields



start_time = trace_root.start_time,



endpoint = trace_root.endpoint.name,



response_time = trace_root.duration,



spans,



client_spans, span_events,



endpoints, hosts,



trace.id



| sort start_time



| limit 100
```

Example: Request attributes

Request attributes are represented as span attributes on the "request root span" (`request.is_root: true`) with the following key: `request_attribute.name of the <request attribute>`.

If the request attribute name contains special characters, you need to use backticks.

```
fetch spans



// no backticks required



| filter isNotNull(request_attribute.my_customer_id)



// backticks required



| filter isNotNull(`request_attribute.My Customer ID`)
```

The data type of `request_attribute.*` depends on the request attribute configuration. If the configuration is set to "All values", the data type is array.

If a request attribute is configured to be captured from method parameters, there are additional attributes on the span on which the attribute has been captured with the following `captured_attribute.<name of the request attribute>` key. The data type of `captured_attribute.*` is always an array because at capture time, it's unknown whether there is one or multiple values.

For more examples, see the [HTTP Requests and Networkingï»¿](https://wkf10640.apps.dynatrace.com/ui/document/v0/#share=b6b8711d-3b72-42e7-9ed2-527193709611) notebook in Dynatrace Playground.

## Databases



You can analyze your Databases with Traces DQL.

Example: Top 10 most frequent database queries

This query identifies the top 10 most frequently executed database queries from client spans, across your telemetry data, and groups them by database system, operation name, and query text.

```
fetch spans



| filter isNotNull(db.namespace) AND span.kind == "client"



| summarize by:{db.system, db.operation.name, db.query.text}, count = count()



| sort count desc



| limit 10
```

Example: Top database statements per service

This query identifies the top 10 database statements executed by each service, along with the total number of calls made to each statement. It takes into account sampling and aggregation to provide an accurate count of database calls.

```
fetch spans



// filter for database spans



| filter span.kind == "client" and isNotNull(db.namespace)



// add service name



| fieldsAdd entityName = dt.entity.service



// calculate multiplicity factor for every span, to for extrapolations



| fieldsAdd sampling.probability = (power(2, 56) - coalesce(sampling.threshold, 0)) * power(2, -56)



| fieldsAdd sampling.multiplicity = 1/sampling.probability



| fieldsAdd multiplicity = coalesce(sampling.multiplicity, 1)



* coalesce(aggregation.count, 1)



* dt.system.sampling_ratio



| summarize { db_calls = sum(multiplicity) }, by: { dt.entity.service.name, code.function, db.system, db.namespace, db.query.text }



// top 100



| sort db_calls desc



| limit 10
```

Example: Database calls per endpoint as timeseries

This query identifies the top 10 database calls made to each endpoint over time. It takes into account sampling and aggregation to provide an accurate count of database calls.

```
fetch spans



// calculate multiplicity factor for every span, to for extrapolations



| fieldsAdd sampling.probability = (power(2, 56) - coalesce(sampling.threshold, 0)) * power(2, -56)



| fieldsAdd sampling.multiplicity = 1/sampling.probability



| fieldsAdd multiplicity = coalesce(sampling.multiplicity, 1)



* coalesce(aggregation.count, 1)



* dt.system.sampling_ratio



| summarize {



spans = count(),



db_spans = countIf(span.kind == "client" and isNotNull(db.namespace)),



db_calls = sum(if(span.kind == "client" and isNotNull(db.namespace),   multiplicity, else: 0) ),



// from all spans in the summarized group, select the one that is the request root



request_root = takeMin(record(



root_detection_helper = coalesce(if(isNotNull(endpoint.name), 1), 2),



start_time, endpoint.name, duration



))



}, by: { trace.id, request.id }



| fields



start_time = request_root[start_time],



endpoint = request_root[endpoint.name],



respopnse_time = request_root[duration],



spans,



db_spans, db_calls,



trace.id



| makeTimeseries { avg(db_calls) }, by: { endpoint }



// only show top 10 timeseries



| sort arraySum(`avg(db_calls)`) desc



| limit 10
```

Example: Database errors

This query identifies the top 10 database errors occurring in client spans, and groups them by database system and query text.

```
fetch spans



// filter for database spans



| filter span.kind == "client"



| filter isNotNull(span.events)



| filter db.namespace != ""



| filter isNotNull(db.query.text)



| filter eventname == "exception"



// adds service name



| fieldsAdd entityName(dt.entity.service)



// adds the error message



| fieldsAdd exception = span.events[0][exception.message]



// adds span name



| fieldsAdd eventname = span.events[0][span_event.name]



| summarize {ExceptionMessage = collectDistinct(exception),



Errors = count()},



by:{Database = db.namespace, Query = db.query.text}



// only show top 10 errors



| sort Errors desc



| limit 10
```

Query result:

Database

Query

ExceptionMessage

Errors

TradeManagement

`SET IMPLICIT_TRANSACTIONS OFF; SET NOCOUNT ON; INSERT INTO [Trades] ([Id], [AccountId], [Direction], [EntryPrice], [InstrumentId], [Quantity], [Status], [TimestampClose], [TimestampOpen], [TradeClosed], [TransactionHappened]) VALUES (@p0, @p1, @p2, @p3, @p4, @p5, @p6, @p7, @p8, @p9, @p10);`

One or more errors occurred. (Cannot insert explicit value for identity column in table 'Trades' when IDENTITY\_INSERT is set to OFF.)

201

For more examples, see the [Databasesï»¿](https://wkf10640.apps.dynatrace.com/ui/document/v0/#share=1386b571-6998-445c-ae10-75510374d535) notebook in Dynatrace Playground.

## Exceptions

Exceptions that happen in the context of a distributed trace are stored within individual spans as a list of `span.events`. You can query for those exceptions with the `iAny` DQL command. You can also expand and flatten the span events, so that the exception attributes appear as top-level attributes. With this, it's easy to create timeseries or any other aggregation from exceptions.

Every attribute's value is of type `string`, making it searchable, which also applies to exception messages and stack traces. On top of that, you can apply the `parse` DQL command to extract structured information.

Example: Find exceptions and excluding specific ones

This query extracts spans that contain error events, specifically focusing on exceptions that aren't related to HTTP.

```
fetch spans



// only spans which contain a span event of type "exception"



| filter iAny(span.events[][span_event.name] == "error")



// exclude specific exception



| filter iAny(contains(span.events[][span_event.name], "http"))



// make exception attributes top level attributes



| expand span.events



| fields span.events



| fieldsFlatten span.events



| fieldsRemove span.events



| limit 1000
```

Example: Full-text search

This query performs a full-text search on the stack trace of spans to find specific error messages.

```
fetch spans



// full text search on stacktrace



| filter iAny(contains(span.events[][exception.stack_trace], "hang up"))



// make exception attributes top level attributes



| expand span.events



| fields span.events



| fieldsFlatten span.events



| limit 1000
```

Example: Exception count by type

This query counts the number of exceptions by their type.

```
fetch spans



// only spans which contain a span event of type "exception"



| filter iAny(span.events[][span_event.name] == "exception")



// make exception type top level attribute



| expand span.events



| fieldsFlatten span.events, fields: { exception.type }



| summarize count(), by: { exception.type }
```

Query result:

`exception.type`

count()

`*net.OpError`

1

`Error`

236

`Grpc.Core.RpcException`

57

PHP Deprecated

1626

`error`

311

`javax.servlet.http.HttpServletResponse.setStatus`

2

`null`

114

Example: Exception frequency as chart

This query creates a timeseries chart showing the frequency of exceptions by their type.

```
fetch spans



// only spans which contain a span event of type "exception"



| filter iAny(span.events[][span_event.name] == "exception")



// make exception type top level attribute



| expand span.events



| fieldsFlatten span.events, fields: { exception.type }



| makeTimeseries count(), by: { exception.type }
```

Query result:

![Exception frequency as chart](https://dt-cdn.net/images/exception-freq-chart-2204-52643bd7ab.png)

Example: Use the parse command to extract information

This query extracts structured information from exception messages using the `parse` command.

```
fetch spans



| filter iAny(contains(span.events[][exception.message], "Bio for user with id"))



// make exception attributes top level attributes



| expand span.events



| fields span.events



| fieldsFlatten span.events



| fieldsRemove span.events



// parse "user_id" number from the exception message



// Example message: "Bio for user with id '9146' not found"



| parse `span.events.exception.message`, "Bio for user with id \'INT:user_id\' not found"



| summarize count(), by: { user_id }



// show top 5



| sort `count()` desc



| limit 5
```

Query result:

`user_id`

count()

3

3

302

3

389

3

428

3

507

3

For more examples, see the [Exceptionsï»¿](https://wkf10640.apps.dynatrace.com/ui/document/v0/#share=e977e465-a4a8-4be7-a335-0f6eb5c420aa) notebook in Dynatrace Playground.

## Logs



Logs can be enriched with `trace_id` and `span_id`. OneAgent can even enrich such context into logs automatically. With this information, you can join spans and logs to, for example, find traces and spans that emit specific logs.

Example: Logs with trace context

This query fetches logs that are enriched with trace context information.

```
fetch logs



// only logs that have a trace context



| filterOut isNull(trace_id)



| limit 10
```

Example: Find spans containing a specific string

This query fetches spans that contain a specific string in their attributes.

```
fetch spans



| filter trace.id in [



fetch logs



// only logs that have a trace context



| filter isNotNull(trace_id)



// search for a particular string in logs content



| filter contains(content, "No carts for user")



// convert from string to UID type



| fields toUid(trace_id)



]



| limit 5
```

Example: From logs containing a specific string, show performance of spans in which the log was emitted

This query fetches spans that were active when a specific log message was emitted.

```
fetch spans



| filter span.id in [



fetch logs



// only logs that have a trace context



| filter isNotNull(span_id)



| filter contains(content, "No carts for user")



// convert from string to UID type



| fields toUid(span_id)



]



// pick either the span name or code namespace and function, depending on what's available



| fieldsAdd name = coalesce(span.name, concat(code.namespace, ".", code.function))



| summarize { count(), avg(duration), p99=percentile(duration, 99), trace.id=takeAny(trace.id) } , by: { k8s.pod.name, name }
```

Example: Join spans and logs

This query joins spans with logs based on the trace ID.

```
fetch spans



| fieldsAdd trace_id = toString(trace.id)



| join [ fetch logs ]



, on:{ left[trace_id] == right[trace_id] }



, fields: { content, loglevel }



| fields start_time, trace.id, span.id, code=concat(code.namespace, ".", code.function), loglevel, content



| limit 100
```

For more examples, see the [Logsï»¿](https://wkf10640.apps.dynatrace.com/ui/document/v0/#share=3701c262-0afd-4ad7-bdf0-154fe93333ca) notebook in Dynatrace Playground.

## Sampling, aggregation, and extrapolation

Sampling
:   * **Adaptive Traffic Management (ATM)** is a rate-limiting, head-based sampling mechanism that adaptively reacts to the rate of requests. The decision is made on the agent, at the beginning of a trace (thus "head-based").
    * **Adaptive Load Reduction (ALR)** is a server-side sampling mechanism that's aimed to protect the backend infrastructure from being overloaded.
    * **Read Sampling**
    * With read sampling, you can control how much data should be read in a query, via the parameter `samplingRatio`.
    * With a value greater than 1, only a sampled fraction of the data is read.
    * The following sampling rates are available: `1`, `10`, `100`, `1000`, `10000`, `100000`. Whereas `1` means 100% data, and `100` means 1% of data.
    * The actually applied read-sampling ratio can be used via `dt.system.sampling_ratio`. Even if `samplingRatio` is set to `samplingRatio: 17`, Grail may decide to fall back to an actual sampling rate of 10.
    * Read sampling is aware of traces. This means that within a specific sampling rate, you'll find either all spans of a trace, or none (based on common `trace.id`).

Aggregation
:   Certain types of operations of the same type can be aggregated into a single span to optimize and reduce the number of spans. One example is database spans. If there are many database operations with the same statement on the same database, OneAgent may choose to aggregate them. Such aggregated spans can be identified by the presence of the `aggregation.count` attribute.

Extrapolation
:   To take all of this into account, when counting operations, you need to extrapolate span counts to actual operation count by using the correct extrapolation-factor:

    ```
    // calculate multiplicity factor for every span, to for extrapolations



    | fieldsAdd sampling.probability = (power(2, 56) - coalesce(sampling.threshold, 0)) * power(2, -56)



    | fieldsAdd sampling.multiplicity = 1/sampling.probability



    | fieldsAdd multiplicity = coalesce(sampling.multiplicity, 1)



    * coalesce(aggregation.count, 1)



    * dt.system.sampling_ratio
    ```

    To use the extrapolation, for example, to count the number of requests, you need to use `sum()`:

    ```
    | summarize count = sum(multiplicity)
    ```

Example: Count requests with extrapolations

This query counts the number of requests with extrapolations applied.

```
fetch spans



// read only 1% of data for better read performance



, samplingRatio:100



// only request roots



| filter request.is_root_span == true



// calculate multiplicity factor for every span, to for extrapolations



| fieldsAdd sampling.probability = (power(2, 56) - coalesce(sampling.threshold, 0)) * power(2, -56)



| fieldsAdd sampling.multiplicity = 1/sampling.probability



| fieldsAdd multiplicity = coalesce(sampling.multiplicity, 1)



* coalesce(aggregation.count, 1)



* dt.system.sampling_ratio



| summarize span_count=count(), request_count_extrapolated = sum(multiplicity)
```

Query result:

`span_count`

`request_count_extrapolated`

479927

48460200

Example: Database call count and durations, extrapolated

This query counts the number of database calls with extrapolations applied.

```
fetch spans



// read only 1% of data for better read performance



, samplingRatio:100



// only database spans



| filter isNotNull(db.statement)



// calculate multiplicity factor for every span, to for extrapolations



| fieldsAdd sampling.probability = (power(2, 56) - coalesce(sampling.threshold, 0)) * power(2, -56)



| fieldsAdd sampling.multiplicity = 1/sampling.probability



| fieldsAdd multiplicity = coalesce(sampling.multiplicity, 1)



* coalesce(aggregation.count, 1)



* dt.system.sampling_ratio



| fieldsAdd aggregation.duration_avg = coalesce(aggregation.duration_sum / aggregation.count, duration)



| summarize {



operation_count_extrapolated = sum(multiplicity),



operation_duration_extrapolated = sum(aggregation.duration_avg * multiplicity) / sum(multiplicity)



}
```

Query result:

`operation_count_extrapolated`

`operation_duration_extrapolated`

11800

6.38ms

For more examples, see the [Sampling, aggregation, and extrapolationï»¿](https://wkf10640.apps.dynatrace.com/ui/document/v0/#share=4c3d3c0f-161a-4c0e-bc8a-623410d549c3) notebook in Dynatrace Playground.

## Trace query usage



Explore the Trace query usage from the billing perspective. Discover usage per apps, users, and query type.

Example: Query traces usage for Apps

This query analyzes billing usage data specifically related to trace queries, aiming to break down data consumption and query volume by application and user.

```
fetch dt.system.events



| filter event.kind == "BILLING_USAGE_EVENT"



| filter event.type == "Traces - Query"



| dedup event.id



| summarize {



data_read_GiB = sum(billed_bytes / 1024 / 1024 / 1024.0),



Query_count = count()



}, by: {



App_context = client.application_context, application_detail = client.source, User = user.email



}



| fieldsAdd split_by_user = record(data_read_GiB, App_context, application_detail, User, Query_count)



| summarize {



split_by_user = arraySort(collectArray(split_by_user), direction: "descending"),



data_read_GiB = sum(data_read_GiB),



Query_count = sum(Query_count)



}, by:{



App_context, application_detail



}



| fieldsAdd split_by_user = record(App_context = split_by_user[][App_context], application_detail = split_by_user[][application_detail], User = split_by_user[][User], data_read_GiB = split_by_user[][data_read_GiB], data_read_pct = (split_by_user[][data_read_GiB] / data_read_GiB * 100), Query_count = split_by_user[][Query_count])



| fieldsAdd split_by_user = if(arraySize(split_by_user) == 1, arrayFirst(split_by_user)[User], else: split_by_user)



| fieldsAdd application_details = record(data_read_GiB, App_context, application_detail, split_by_user, Query_count)



| summarize {



application_details = arraySort(collectArray(application_details), direction: "descending"),



data_read_GiB = sum(data_read_GiB),



Query_count = toLong(sum(Query_count))



}, by:{



App_context



}



| fieldsAdd application_details = record(App_context = application_details[][App_context], application_detail = application_details[][application_detail], split_by_user = application_details[][split_by_user], data_read_GiB = application_details[][data_read_GiB], data_read_pct = application_details[][data_read_GiB] / data_read_GiB * 100, Query_count = application_details[][Query_count])



| fieldsAdd key = 1



| fieldsAdd total = lookup([



fetch dt.system.events



| filter event.kind == "BILLING_USAGE_EVENT" and event.type == "Traces - Query"



| dedup event.id



| summarize total = sum(billed_bytes / 1024 / 1024 / 1024.0)



| fieldsAdd key = 1



], sourceField: key, lookupField:key)[total]



| fields App_context, application_details, data_read_GiB, data_read_pct = data_read_GiB / total * 100, Query_count



| sort data_read_GiB desc
```

Example: Query traces usage by users

This query provides a detailed breakdown of trace query billing usage by user, focusing on how much data each user consumes and through which application contexts.

```
fetch dt.system.events



| filter event.kind == "BILLING_USAGE_EVENT"



| filter event.type == "Traces - Query"



| dedup event.id



| summarize {



data_read_GiB = sum(billed_bytes / 1024 / 1024 / 1024.0),



Query_count = count()



}, by: {



App_context = client.application_context, application_detail = client.source, User = user.email



}



| fieldsAdd split_by_application_detail = record(data_read_GiB, App_context, application_detail, User, Query_count)



| summarize {



split_by_application_detail = arraySort(collectArray(split_by_application_detail), direction: "descending"),



data_read_GiB = sum(data_read_GiB),



Query_count = sum(Query_count)



}, by:{



User, App_context



}



| fieldsAdd split_by_application_detail = record(User = split_by_application_detail[][User], App_context = split_by_application_detail[][App_context], application_detail = split_by_application_detail[][application_detail], data_read_GiB = split_by_application_detail[][data_read_GiB], data_read_pct = (split_by_application_detail[][data_read_GiB] / data_read_GiB * 100), Query_count = split_by_application_detail[][Query_count])



| fieldsAdd split_by_application_detail = if(arraySize(split_by_application_detail) == 1, arrayFirst(split_by_application_detail)[application_detail], else: split_by_application_detail)



| fieldsAdd App_contexts = record(data_read_GiB, User, App_context, split_by_application_detail, Query_count)



| summarize {



App_contexts = arraySort(collectArray(App_contexts), direction: "descending"),



data_read_GiB = sum(data_read_GiB),



Query_count = toLong(sum(Query_count))



}, by:{



User



}



| fieldsAdd App_contexts = record(User = App_contexts[][User], App_context = App_contexts[][App_context], split_by_application_detail = App_contexts[][split_by_application_detail], data_read_GiB = App_contexts[][data_read_GiB], data_read_pct = App_contexts[][data_read_GiB] / data_read_GiB * 100, Query_count = App_contexts[][Query_count])



| fieldsAdd key = 1



| fieldsAdd total = lookup([



fetch dt.system.events



| filter event.kind == "BILLING_USAGE_EVENT" and event.type == "Traces - Query"



| dedup event.id



| summarize total = sum(billed_bytes / 1024 / 1024 / 1024.0)



| fieldsAdd key = 1



], sourceField: key, lookupField:key)[total]



| fields User, App_contexts, data_read_GiB, data_read_pct = data_read_GiB / total * 100, Query_count



| sort data_read_GiB desc
```

Example: Top 10 disks with the highest average usage

This query identifies the top 10 disks with the highest average usage across hosts. It calculates the average disk usage percentage for each disk-host pair, and then computes the overall average for each combination.

```
timeseries percent = avg(dt.host.disk.used.percent), by:{dt.entity.host, dt.entity.disk}



| fieldsAdd percent = arrayAvg(percent)



| fieldsAdd display = concat(entityName(dt.entity.host), " | ",  entityName(dt.entity.disk), " | " , round(percent, decimals:2), "%", if(percent>80, "â ï¸"))



| sort percent desc



| limit 10
```

Query result:

![Top 10 disks with the highest average usage](https://dt-cdn.net/images/screenshot-2025-08-27-at-12-58-07-2192-27582c6ee2.png)

For more examples, see the [Trace query usageï»¿](https://wkf10640.apps.dynatrace.com/ui/document/v0/#share=c34f9969-b1f7-4c7d-a183-4bed553118ec) notebook in Dynatrace Playground.

## Related topics

* [Distributed traces concepts](/docs/observe/application-observability/distributed-traces/concepts "Learn more about distributed tracing core concepts and terminology.")
* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")

---

## observe/application-observability/distributed-tracing/data-retention.md

---
title: Retain trace data for long periods
source: https://www.dynatrace.com/docs/observe/application-observability/distributed-tracing/data-retention
scraped: 2026-02-20T21:07:58.401673
---

# Retain trace data for long periods

# Retain trace data for long periods

* Latest Dynatrace
* Tutorial
* 3-min read
* Updated on Jun 23, 2025

Long-term data retention provides comprehensive trend analysis and performance monitoring over extended periods. For industries with regulatory requirements for auditing and compliance purposes, storing trace data for several years can be a requirement. Additionally, it supports teams in identifing recurring issues, troubleshooting processes that take longer than expected, and investigating and resolving issues that may not be immediately apparent, especially those that develop over time.

With distributed tracing powered by Grail, you can store trace data in Grail buckets with custom retention time, from 10 days up to 10 years, shaping trace data retention and storage according to team ownership or time requirements.

## Who is this for

This article is intended for SRE and architects who want to store trace data to compare the behavior of services over long periods of time for troubleshooting or compliance purposes.

## What you will learn

In this article you will learn how to create a custom bucket with a 5-year data retention period and assign production trace data of a Kubernetes namespace to it.

## Before you begin

Prerequisites

* Dynatrace SaaS environment powered by Grail and AppEngine.
* Dynatrace Platform Subscription (DPS) with [Traces powered by Grail overview (DPS)](/docs/license/capabilities/traces "Learn how Dynatrace Traces powered by Grail consumption is calculated using the Dynatrace Platform Subscription (DPS) model.") capabilities.
* `openpipeline:configurations:write` and `openpipeline:configurations:read` permissions. To learn how to set up the permissions, see [Permissions in Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.").

Prior knowledge

* [Organize data](/docs/platform/grail/organize-data "Insights on the Grail data model consisting of buckets, tables, and views.")
* [Data retention periods](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods "Check retention times for various data types.")

Key terms

Pipeline
:   Collection of processing instructions to structure, separate, and store data.

Stage
:   Phase in a pipeline sequence, focused on a task and defined by processors.

Processor
:   Pre-formatted processing instruction.

Routing
:   Assignation of data to a pipeline, based either on matching conditions (dynamic routing) or directly configured (static).

## Steps

1. Create a custom bucket

To create a custom bucket with a long retention period

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Storage management** > **Bucket storage management** >  **Bucket**.
2. Define the new bucket

   * Name: `long_term_spans`
   * Retention period (days): `1825`
   * Record type: **spans**
3. Select **Create** and then refresh the list (  ).

You created a new bucket to store trace data for 5 years. The bucket will remain empty until you assign records to it via ![OpenPipeline](https://dt-cdn.net/images/openpipeline-configurations-highresolution-1025-8c07f4c78c.webp "OpenPipeline") OpenPipeline.

2. Set the bucket as storage

To assign records from a production namespace to the `long_term_spans` bucket via ![OpenPipeline](https://dt-cdn.net/images/openpipeline-configurations-highresolution-1025-8c07f4c78c.webp "OpenPipeline") OpenPipeline

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Spans** > **Pipelines**.
2. Choose an existing pipeline or create a new one.
3. In the **Storage** stage, select  **Processor** > **Bucket assignement**.
4. Define the new processor

   * Name: `Store prod spans (5 years)`
   * Condition: `k8s.namespace.name==prod`
   * Bucket: **long\_term\_spans**
5. Select **Save**.

If an existing route points to the pipeline, the new processor will start assigning trace data from the production namespace to the `long_term_spans` bucket. If you created a new pipeline for the processor, make sure to route trace data to it.

3. Route data to the bucket

Make sure your pipeline is receiving records via a dynamic route.

1. Go to **Dynamic routing**.
2. Choose an existing dynamic route or create a new one.
3. Define the route by entering a route name, a matching condition (for example `true`), and the target pipeline name.
4. Select **Save**.

## Conclusion

You created a new bucket with a custom retention period of 5 years. The new bucket is the storage option for production-related spans. Spans are routed to the pipeline and assigned to the bucket according to matching condition.

## Related topics

* [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.")
* [Data retention periods](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods "Check retention times for various data types.")

---

## observe/application-observability/distributed-tracing/detect-performance-issues.md

---
title: Detect performance issues
source: https://www.dynatrace.com/docs/observe/application-observability/distributed-tracing/detect-performance-issues
scraped: 2026-02-20T21:08:25.067142
---

# Detect performance issues

# Detect performance issues

* Latest Dynatrace
* Tutorial
* 5-min read
* Published Oct 28, 2024

Understanding which requests are slow and why that happens can be challenging in modern, cloud-based, distributed systems. The [Distributed Tracing ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") appï»¿](https://dt-url.net/vc23u9n) is designed to help answer these questions quickly through an exploratory approach.

Test the app in a sandbox environment:

* [Playground environmentï»¿](https://dt-url.net/al43u2h)

## Target audience

This article is intended for SREs, developers, and performance architects who want to investigate performance issues by analyzing distributed traces within the Distributed Tracing app.

## What you will learn

In this tutorial, youâll learn how to use the Distributed Tracing app specifically to analyze and troubleshoot slow requests in a production Kubernetes namespace. You will learn to:

* Filter traces based on relevance  
  Use facets to narrow down the scope of traces, focusing on those that align with your responsibilities or areas of interest.
* Zoom in on specific timeframes  
  Pinpoint relevant time periods with the time series chart or timeframce selector to view performance over a selected duration.
* Identify performance outliers  
  Use histogram views to locate traces with extended response times.
* Analyze affected services and requests  
  Use the grouping feature to understand which services and requests are affected.
* Drill down into individual traces  
  Explore detailed trace data for specific requests to uncover root causes and pinpoint what occurred during slow response events.

## Prerequisites

* You're familiar with the [concepts of distributed tracing](/docs/observe/application-observability/distributed-traces/concepts "Learn more about distributed tracing core concepts and terminology.").
* You have Dynatrace Platform Subscription (DPS).
* You're ingesting trace data via [Dynatrace OneAgent](/docs/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.") or [OpenTelemetry](/docs/ingest-from/opentelemetry/getting-started "How to get your OpenTelemetry data into Dynatrace."). To get started ingesting trace data, go to the **Distributed Tracing** >  **Traces** > choose a source and follow the in-product guidance.
* Make sure that your traces are available in the [Distributed Tracing ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing")](/docs/observe/application-observability/distributed-tracing/distributed-tracing-app "Discover the functionalities of the new Distributed Tracing app.") app.

## Analyze and troubleshoot performance issues

1. Go to Distributed Tracing ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing").
2. In the upper-right corner, select the timeframe **Last 30 minutes** to see how the number of requests and their response time have evolved during that timeframe.
3. Use facets to filter traces by a specific namaspace. To analyze traces that traverse your Kubernetes **prod** namespace,

   1. In the facets list, go to **Kubernetes** > **Kubernetes namespace**.

      The namespaces that are detected more frequently in your traces are listed first.
   2. Select **prod**.

      The filter field query automatically changes. You can edit the filter query further before updating the results.
   3. Select  **Update** to update the results.
4. Observe the charts to quickly spot performance outliers.

   1. Go to the **Timeseries** chart to get an overview of the trends.

      ![Detect performance issues timeseries](https://dt-cdn.net/images/traces-example-00001-timeseries-3430-6a591decfd.png)

      The Kubernetes **prod** namespace shows several spikes for request count and a cluster of failed requests.
   2. To analyze data further, select **Histrogram**.

      ![Detect performance issues histogram](https://dt-cdn.net/images/traces-example-00002-3440-40b39e1573.png)

      The histogram summarizes the amount of requests to a specific response time bucket. There's a cluster of requests to the **prod** environment that take around 5s.
   3. Select the chart area containing the affected cluster to focus on the requests that fall into that response time bucket.

      The filter bar is updated to show traces for the selected response time area, and the list shows traces with similar services and endpoints.
5. Group the requests by service and endpoint to undestand which services and endpoints are affected.

   1. Go to the table and select  **Group by:**.
   2. Select the attributes **Service** and **Endpoint**.

      In the table view (:TableIcon:) you can see an aggregated list of the services and endpoints that fall into the selected response time for the **prod** namespace. The columns summarize average and highest duration, the request count, and how many of these requests failed, including the failure rate.
   3. To learn more about the top contributors to an aggregate in the table, select .

      Focusing on the **/cart/checkout** request, you'll see that it not only has a slow response time (**5.82 s**) but also a high failure rate (**28%**), indicating it may be a key bottleneck.

      ![distributed tracing cart/checkout request](https://dt-cdn.net/images/wkf10640-apps-dynatrace-com-ui-apps-dynatrace-distributedtracing-explorer-3840-e0a340e0bf.png)
   4. To focus on a request, select the request name (**/cart/checkout**) in the table and filter by the endpoint.

      The filter field query and the table results are automatically updated.
6. To identify the bottleneck for a request matching the selected filters, go to the  list view and select the timestamp for one of the requests.

The single trace perspective opens at the bottom half of the page. Now, you can analyze the full end-to-end trace. In our case, we see that the bottleneck is the **GetCart** endpoint on the **Cart** services, which leads to a slow response time.

## Conclusion

In this tutorial, you've learned how to effectively use the Distributed Tracing ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") app for analyzing and troubleshooting slow requests within a production Kubernetes namespace. You're now skilled at filtering traces based on relevance, zooming in on specific timeframes to identify anomalies, and analyzing impacted services and requests. These skills enabled you to diagnose and resolve performance issues within your Kubernetes environment efficiently.

We analyzed trace data and identified a cluster of slow and failing requests within the production Kubernetes namespace. By filtering, grouping, and examining trace data, we were able to pinpoint a bottleneck in the **GetCart** endpoint of the **Cart** service.

---

## observe/application-observability/distributed-tracing/distributed-tracing-app/facets.md

---
title: Manage facets
source: https://www.dynatrace.com/docs/observe/application-observability/distributed-tracing/distributed-tracing-app/facets
scraped: 2026-02-19T21:17:41.188841
---

# Manage facets

# Manage facets

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Jan 23, 2025

This article contains information on how to manage your facets to correspond to your preferred filtering in the Distributed tracing app.

## Before you begin

Prerequisites

* [Set up Grail permissions for Distributed Tracing](/docs/observe/application-observability/distributed-tracing/permissions "Manage permissions for Distributed Tracing powered by Grail.").

## Manage all facets

To manage which facets of your environment are displayed

1. Go to ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing** > **Explorer**.
2. Select **Show facets**.
3. Select or deselect items from the predefined categories.

   * Check the category box to select or deselect all facets in the category.
   * Select  to view the facets in a category and select or deselect them.
4. Select **Save**.

## Revert to default settings

If you have previously modified the facets, to revert to the default settings for facets in your environment

1. Go to ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing** > **Explorer**.
2. Select **Show facets**.
3. Select **Reset facet to default**.
4. Select  **Confirm reset?**

## Edit a facet

1. Go to ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing** > **Explorer**.
2. Expand a facet category and select the facet you want to edit.
3. Select  next to the facet's name and then  **Edit facet**.
4. Make the desired changes and select **Save**.

## Hide a facet

To hide a facet from the list

1. Go to ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing** > **Explorer**.
2. Expand a facet category and select the facet you want to hide.
3. Select  next to the facet's name and then  **Hide facet**.

## Group facets

To group your records by attributes

1. Go to ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing** > **Explorer**.
2. Expand a facet category and select the facet you want to use for grouping.
3. Select  next to the facet's name and then  **Group by**.

The table is updated with the selected attribute(s). To change the filter selection, select  **Group by:** field and add or remove any attribute from the list. If you remove all attributes, the table resorts to its default view.

---

## observe/application-observability/distributed-tracing/distributed-tracing-app.md

---
title: Distributed Tracing app
source: https://www.dynatrace.com/docs/observe/application-observability/distributed-tracing/distributed-tracing-app
scraped: 2026-02-20T21:08:20.660612
---

# Distributed Tracing app

# Distributed Tracing app

* Latest Dynatrace
* Explanation
* 6-min read
* Updated on Jan 12, 2026

![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing** enhances Dynatrace abilities to analyze and filter trace data at both the request and span levels. With advanced filtering options, such as facets and the grouping function, you can easily explore and pinpoint issues. In addition, your selection is preserved across interactions, enabling you to drill down to the single trace information, and to identify the root cause and prevent failures in your environments.

In Dynatrace, go to ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing** to access this app.

* In the **Distributed Tracing** welcome view, you can get started discovering the app and getting data into Dynatrace. Alternatevely, you can add trace data at any time by selecting  **Traces** and choosing a source. Follow the in-product guidance to continue the configuration for the selected source.
* The default view **Explorer** contains all the user-interface elements to analyze your trace data.

## Requests and spans

A distributed trace is a collection of spans representing a request's journey through a distributed system.

### Requests

The request is the call initiated by a user or system to perform a specific task. It interacts with various services and components within the distributed system.

To view trace data created in your environment in response to an external request, select **Requests** in the upper-left corner of ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**.

### Spans

Spans are individual operations representing each request interaction with the distributed system.

To view all trace data by single operations, select **Spans** in the upper-left corner of ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**.

## Filter field

By entering a query in the [filter field](/docs/discover-dynatrace/get-started/dynatrace-ui/ui-filter-field "The filter field is a powerful tool that allows you to quickly find relevant information or narrow down results within apps."), you can quickly build DQL-based filtering options.

```
"Kubernetes namespace" = prod AND Endpoint = /cart/* AND "Response time" >= 5s
```

You can narrow your results by timeframe or segments.

* To refresh the result for the selected timeframe, select  **Refresh**.
* To choose [segments](/docs/manage/segments "Segments logically structure monitoring data in Grail and function as convenient filters for data that users are allowed to access based on permissions."), select .

The filter field is automatically modified when you apply other filtering selections, such as [facets](#facets). To update the results after you change the filter field query, select  **Update**.

### Use cases

* Get results for any key-value pair.
* Visualize and edit your filtering selection.

## Charts

The charts allow you to view your trace data trends and distribution. You can also hide or show the chart card again at any time.

When you hover over the chart and select an area, the filter field and results are automatically updated to focus on the selected portion of the trace data.

Distributed Tracing charts

The following table compares the **Timeseries** and **Histogram** charts.

Timeseries

Histogram

X-axis

Time intervals [1](#fn-1-1-def)

Response time intervals

Y-axis

Frequency of data points (left-hand side) and response time (right-hand side)

Frequency of data points

Important statistical factors

The legend lists dedicated views for percentiles, averages, and successful and failed requests. Choose an option to view the related trends.

Percentiles and averages are marked with contrast-color vertical lines.

Use cases

Understand how trace data changes over time and identify trends and cyclic behaviors.

Visualize your data's distribution, identify patterns, and spot outliers.

1

Granularity depends on the selected timeframe.

## Facets

Facets are quick filters for trace data. They correspond to span attribute key-value pairs detected in your environment and are grouped by facet categories. The most important DQL field IDs are grouped by default in predefined categories. You can define new facet categories and new facets for attributes that are important to you. Each facet category displays the most frequently detected attributes for the current filtering selection.

For details how to manage your facets, see [Manage facets](/docs/observe/application-observability/distributed-tracing/distributed-tracing-app/facets "Manage your facets in the Distributed Tracing app.").

### Use cases

* Add new facets to better catalog your trace data.
* Select facets from the facet list to filter data by them. The filter field is automatically modified according to your selection. Make sure to select  **Update**.
* Quickly group by attributed keys.
* Quickly add attributes as columns to the table.

## Table results

The table lists the latest 1000 records for the selected timeframe that match the filtering options you applied. The table data is available as a list (  ) or grouped by attributes (  ). You can manage columns to display only the attributes you're interested in and exclude noise.

UI element

Scope

`<column value>`

Filter trace data by a column value.

Copy the DQL statement or the DQL API call.

Download the visible table data.

### Use cases

* Compare records and their different attribute values.
* Filter trace data by a result by selecting the table result. The filter field is automatically modified according to your selection. Make sure to select  **Update**.
* Reduce noise by hiding unnecessary columns from the table or deselecting an attribute.

## Group by

Analyze predetermined important dimensions, such as request count, failure, and percentile contribution, by combining up to 3 attributes that matter the most to you. To group your records by attributes

* Go to the table and select  **Group by:**. Then select/deselect the attribute you're interested in.
* Go to the facet list and select  > **Group by** for each attribute key.

## Single trace perspective

The single trace perspective offers a detailed view of the trace spans.

* The waterfall list on the left contains the trace spans, ordered by sequence. For each span you can see,

  + The corresponding duration bar.
  + The related service; spans associated with the same service are of the same color.
  + The span kind, represented by an icon.

    | Icon | Span kind |
    | --- | --- |
    |  | Web or RPC call (client or server) |
    | The database vendor or | Database call (client) |
    |  | Producer or consumer |
    | The service technology | Call (client or server), internal, or link |

  You can understand the sequence and correlation of spans by observing the size and position of the duration bar. Additionally, you can do the following:

  + Search by values (name, endpoint, service, or attribute).
  + View or hide all spans for the selected trace (  **Name**) or subsequent spans in the trace execution (  next to the span name).
  + View attributes for a span in the details panel by selecting the span name.
  + Explore logs related to the span or the trace (  **View logs**).
* On the right, you can explore and search for attributes for the selected span. Enter a value in the  **Search details** field to view only key or value results matching your search.

To access the single trace perspective, go to the table row of the trace you're interested in and select the trace start time. The single trace perspective opens in the bottom half of the page.

### Use cases

* Focus on the analysis of a single trace.
* Follow full end-to-end traces, across complex transaction flows, even when spanning different trace IDs.

## Exceptions

Use the **Exceptions** tab in ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing** to understand which exceptions occur across your traces and identify, analyze, and resolve issues related to exceptions.

Through visualizations, aggregated data, and contextual insights, the **Exceptions** tab can help you understand the root causes of exceptions and their impact on your service.

This feature is designed for SREs, developers, and DevOps teams who need fast, actionable insights into exception patterns and their impact on services.

Exception analysis provides:

* A clear view of why exceptions occur
* Advanced filtering by service, endpoint, exception type, and timeframe
* In-depth analysis and visual trends of exception occurrences
* Aggregated stack traces to identify root causes
* Contextual logs linked to exceptions
* Insights into requests containing exceptions, including sub-traces

### Integration with Dynatrace

* Embedded in [![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**](/docs/observe/application-observability/distributed-tracing/distributed-tracing-app "Discover the functionalities of the new Distributed Tracing app.") as a new **Exceptions** tab
* Integrated into the Dynatrace service-specific drill-down options
* Replaces the legacy Exceptions Analysis page for DPS customers

### Access and navigation



In addition to the **Exceptions** tab in [![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**](/docs/observe/application-observability/distributed-tracing/distributed-tracing-app "Discover the functionalities of the new Distributed Tracing app."), you can analyze exceptions in context through service-specific drill-downs.

To learn more about analyzing exceptions, see [Exception analysis](/docs/observe/application-observability/distributed-tracing/exception-analysis "Exception analysis helps you detect, investigate, and resolve exceptions more effectively in Dynatrace.").

---

## observe/application-observability/distributed-tracing/exception-analysis.md

---
title: Exception analysis
source: https://www.dynatrace.com/docs/observe/application-observability/distributed-tracing/exception-analysis
scraped: 2026-02-20T21:08:11.420996
---

# Exception analysis

# Exception analysis

* Latest Dynatrace
* Tutorial
* 4-min read
* Published Jan 12, 2026

Exception analysis in Dynatrace provides a comprehensive view of exceptions occurring along your traces. It enables you to identify, analyze, and resolve issues by offering:

* Visual trends of exception occurrences over time
* Advanced filtering by service, endpoint, exception type, and timeframe
* Aggregated stack traces to pinpoint root causes

With detailed contextual logs and insights into requests containing exceptions, including sub-traces, Dynatrace helps you understand the root causes of exceptions and their impact across your distributed traces, ensuring faster resolution and improved reliability.

## What is exception analysis?

In Dynatrace, an exception refers to an error or unexpected condition that occurs during code execution. Exceptions may result from programming errors, invalid inputs, resource issues, or external service failures.

Exceptions are captured during a span either by OneAgent or via OpenTelemetry. The new Exception analysis will leverage the semantics defined [Semantic Dictionary: Traces](/docs/semantic-dictionary/model/trace#exception "Get to know the Semantic Dictionary models related to traces."), which are based on [OpenTelemetry semantic conventionsï»¿](https://opentelemetry.io/docs/specs/semconv/exceptions/exceptions-spans/).

Exception analysis helps you detect, investigate, and resolve exceptions more effectively. It introduces a user-focused interface with advanced capabilities for both reactive and proactive troubleshooting.

To explore **Exceptions**

1. Go to [![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**](/docs/observe/application-observability/distributed-tracing/distributed-tracing-app "Discover the functionalities of the new Distributed Tracing app.").
2. Select the **Exceptions** tab.

This feature is designed for SREs, developers, and DevOps teams who need fast, actionable insights into exception patterns and their impact on services.

Exception analysis provides:

* A clear view of which exceptions occur
* Trends showing how exceptions evolve over time
* Advanced filtering by service, endpoint, exception type, and timeframe
* In-depth analysis and visual trends of exception occurrences
* Aggregated stack traces to identify root causes
* Contextual logs linked to exceptions
* Insights into requests containing exceptions

## Key capabilities

### Core capabilities

Capability

Description

**Advanced filtering**

Use Dynatrace filters to narrow down exceptions by attributes such as service, endpoint, failures, and more.

* Timeframe
* Segments
* Facets

**Exception trend chart**

Visualize the trend of exceptions over time.

* Select an exception in the table to highlight it in the trend chart for deeper analysis.

**Exceptions table**

View a detailed list of exceptions, including their type, frequency, and impact.

* Select an exception in the table to highlight it in the trend chart for deeper analysis.

**Aggregated stack traces**

Explore aggregated stack traces for each exception, allowing you to identify common code paths and pinpoint the root cause of issues.

**Related logs**

View logs related to each exception for additional context. This helps you correlate log events with the occurrence of exceptions.

**Requests containing exceptions**

Analyze requests that contained the selected exception, either directly or within a sub-trace. This feature helps you understand how exceptions are affecting specific transactions.

### Integration with Dynatrace

* Embedded in [![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**](/docs/observe/application-observability/distributed-tracing/distributed-tracing-app "Discover the functionalities of the new Distributed Tracing app.") as a new **Exceptions** tab
* Integrated into the Dynatrace services-specific drill-down options
* Replaces the legacy Exceptions Analysis page for DPS customers

## Access and navigation

Exception analysis is designed to support both contextual and exploratory workflows.

### Prerequisites

* DPS license
* SaaS environment with the latest Dynatrace platform enabled

### Direct access

To explore **Exceptions** directly

1. Go to [![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**](/docs/observe/application-observability/distributed-tracing/distributed-tracing-app "Discover the functionalities of the new Distributed Tracing app.").
2. Select the **Exceptions** tab.

### Contextual access

To analyze exceptions in context

1. Go to [![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**](/docs/observe/application-observability/services/services-app "Maintain centralized control over service health, performance, and resources with the Services app.").
2. Turn on **Analyze details**.
3. Select the **Exceptions** tab.

## Get started

To get started troubleshooting service exceptions

1. Go to [![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**](/docs/observe/application-observability/distributed-tracing/distributed-tracing-app "Discover the functionalities of the new Distributed Tracing app.") and select the **Exceptions** tab.
2. Apply filters for service, endpoint, and timeframe.
3. Select an exception from the table to highlight its trend in the chart and additional details for further analysis.
4. For the selected exception, the screen provides aggregated stack traces. These stack traces are grouped to show common execution paths with their contribution, making it easier to understand what they have in common and where they deviate from each other.
5. To examine logs happening on these spans containing the exception, select the **Logs** tab.
6. To see endpoints impacted by exceptions, select the **Requests** tab.

## Join the conversation

Weâd love to hear your feedback and questions about the new Exceptions Analysis experience.

Visit the [Feedback Channelï»¿](https://dt-url.net/i003111) in the Dynatrace Community.

---

## observe/application-observability/distributed-tracing/ingest-traces.md

---
title: Ingest traces
source: https://www.dynatrace.com/docs/observe/application-observability/distributed-tracing/ingest-traces
scraped: 2026-02-20T21:08:26.404916
---

# Ingest traces

# Ingest traces

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Feb 07, 2025

You can use OneAgent or OpenTelemetry integration to add traces to Dynatrace, including trace data from specific extensions for third-party systems, such as Serverless functions and Adobe Experience Manager (AEM) Cloud Service. This ensures, that you capture detailed trace data to analyze the behavior and performance of your applications.

* OneAgent

  Dynatrace OneAgent is the simplest way to capture trace data. By installing OneAgent on your hosts, you can automatically collect distributed traces from your applications.
* OpenTelemetry integration

  If you are using OpenTelemetry, you can configure it to send trace data to Dynatrace. This involves setting up the OpenTelemetry Collector and configuring it to export traces to Dynatrace.

Choose one of the following options to learn more about the configuration.

Cloud Workload

#### AWS

[AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration) [AWS Fargate](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate) [Amazon EC2](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-ec2) [Amazon ECS](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-ecs) [Amazon EKS](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-eks) [AWS App Runner](/docs/ingest-from/amazon-web-services/integrate-into-aws/app-runner) [AWS Elastic Beanstalk](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-beanstalk) [All AWS cloud services](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services) 

#### Microsoft Azure

[Azure Monitor metrics](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide) [Azure Logs](/docs/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure) [Azure Kubernetes Service (AKS)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-aks) [Azure App Service](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice) [Azure Functions](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions) [Azure Virtual Machines (VM)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-vm) [Azure Virtual Machine Scale Set (VMSS)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-vmss) [Azure Service Fabric](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-servicefabric) [Azure Spring Apps](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-spring) [All Azure cloud services](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics) 

#### Google Cloud

[![Google Cloud Run (managed)](https://cdn.bfldr.com/B686QPH3/at/7mr6q4h3nv5qjvgccbqm8x5/DT0184.svg?auto=webp&width=72&height=72 "Google Cloud Run (managed)")Google Cloud Run (managed)](/docs/ingest-from/google-cloud-platform/gcp-integrations/cloudrun) [![Google Cloud Functions](https://cdn.bfldr.com/B686QPH3/at/rc58vncw7jkjs8pf5m4wk8p/DT0172.svg?auto=webp&width=72&height=72 "Google Cloud Functions")Google Cloud Functions](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions) [![Google Cloud App Engine](https://cdn.bfldr.com/B686QPH3/at/cs4628s93tzgrqp5vbqvf2x/DT0059.svg?auto=webp&width=72&height=72 "Google Cloud App Engine")Google App Engine](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-app-engine) [![Google Compute Engine](https://cdn.bfldr.com/B686QPH3/at/9qpgp4rfnnc556gbwgc32fs4/DT0220.svg?auto=webp&width=72&height=72 "Google Compute Engine")Google Compute Engine](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-compute-engine) [![Google Kubernetes Engine](https://cdn.bfldr.com/B686QPH3/at/sz8sx4wfhjf3bsb5m6sbj4k/DT0166.svg?auto=webp&width=72&height=72 "Google Kubernetes Engine")Google Kubernetes Engine (GKE)](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-gke) [All Google Cloud services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new)

Kubernetes

[Kubernetes cluster](/docs/ingest-from/setup-on-k8s/deployment) [Envoy](/docs/ingest-from/opentelemetry/integrations/envoy) [Istio](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/istio-deployment)

Host-based

[AIX](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix) [Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux) [Solaris](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/solaris) [Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows) [zOS](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos) 

[Amazon EC2](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-ec2) [Azure Virtual Machines (VM)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-vm) [![Google Compute Engine](https://cdn.bfldr.com/B686QPH3/at/9qpgp4rfnnc556gbwgc32fs4/DT0220.svg?auto=webp&width=72&height=72 "Google Compute Engine")Google Compute Engine](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-compute-engine)

OpenTelemetry

[OpenTelemetry](/docs/ingest-from/opentelemetry)

Other setup options

[Graal VM Native Image](/docs/ingest-from/technology-support/application-software/java/graalvm-native-image) [GitOps](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/using-gitops) [Docker](/docs/ingest-from/setup-on-container-platforms/docker) [Heroku](/docs/ingest-from/setup-on-container-platforms/heroku) [Ingest data in Dynatrace](/docs/ingest-from)

## Related topics

* [Dynatrace OneAgent](/docs/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.")
* [Get started with OpenTelemetry and Dynatrace](/docs/ingest-from/opentelemetry/getting-started "How to get your OpenTelemetry data into Dynatrace.")
* [Extend distributed tracing](/docs/ingest-from/extend-dynatrace/extend-tracing "Learn how to extend trace observability in Dynatrace.")
* [Adaptive Traffic Management for distributed tracing](/docs/ingest-from/dynatrace-oneagent/adaptive-traffic-management "Dynatrace Adaptive Traffic Management provides dynamic sampling to ensure that the amount of capture traces stays within the Full-Stack Monitoring included trace volume.")

---

## observe/application-observability/distributed-tracing/permissions.md

---
title: Set up Grail permissions for Distributed Tracing
source: https://www.dynatrace.com/docs/observe/application-observability/distributed-tracing/permissions
scraped: 2026-02-20T21:08:30.364640
---

# Set up Grail permissions for Distributed Tracing

# Set up Grail permissions for Distributed Tracing

* Latest Dynatrace
* How-to guide
* 1-min read
* Updated on Nov 20, 2025

Dynatrace has a [permission model for Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail."). This applies to all telemetry data, such as metrics, events, spans, and logs.

We recommend setting up permissions along organizational lines and deployment scopes. Suitable concepts include host groups, Kubernetes clusters, and Kubernetes namespaces. These attributes are typically available for all telemetry data ingested via Dynatrace collection methods like OneAgent, OpenTelemetry, or Kubernetes operator. Hence, you can use these attributes to enable [record-level permissions](/docs/platform/grail/organize-data/assign-permissions-in-grail#grail-permissions-table-record "Find out how to assign permissions to buckets and tables in Grail.").

For Kubernetes-based deployments, make sure Dynatrace Operator has [metadata enrichment](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment "Metadata enrichment in the Dynatrace Operator adds context to Kubernetes pods by attaching relevant metadata to entities like pods, hosts, and processes for better observability.") enabled.

If you only require a basic permission concept, setting up bucket-level permissions is the best option. You can then route your data to the correct bucket in OpenPipeline by matching one of the mentioned deployment-relevant primary Grail fields.

For more control in Dynatrace, you can set up policy boundaries with more granular restrictions on a data level. By default, you can use the following attributes:

* `dt.host_group.id`
* `k8s.cluster.name`
* `k8s.namespace.name`
* Any other attribute listed in the [permission model](/docs/platform/grail/organize-data/assign-permissions-in-grail#grail-permissions-table-record "Find out how to assign permissions to buckets and tables in Grail.")

Dynatrace provides a comprehensive permission model for Grail that applies to all telemetry data-including metrics, logs, spans, and events.

## Set up the security context

If the permissions on deployment-level attributes or the bucket level are insufficient, Dynatrace allows you to set up fine-grained permissions by adding a `dt.security_context` attribute to your data. This context can represent your security architecture and could even be hierarchical by encoding this into a string such as: `department-A/department-AB/team-C`.

### Leverage existing tags at the source

You can define the security context at the source via [OneAgent](/docs/ingest-from/dynatrace-oneagent/oneagent-security-context "Learn how to set up Grail permissions for OneAgent."), [OpenTelemetry](/docs/ingest-from/opentelemetry/opentelemetry-security-context "Set up Grail permissions for OpenTelemetry."), or [Kubernetes labels or annotations](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment "Guides for telemetry enrichment on Kubernetes"). This allows you to use your existing labels and tags to facilitate permissions in Dynatrace.

## Set up the security context in OpenPipeline

Alternatively, you can define a security context based on existing resource attributes to your [span data within OpenPipeline](/docs/platform/openpipeline/concepts/processing "Learn the core concepts of Dynatrace OpenPipeline processing."):

1. Filter the records that should get the `dt.security_context` attribute added to them. To do so, open a new [notebook](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") and create a filtering DQL query, such as:

```
fetch spans



| filter matchesPhrase(deployment.release_stage, "prod-")
```

This query allows you to filter the span records to which you'll want to add the `dt.security_context` attribute. Once you're satisfied with the query result, copy the span processing function of the DQL query, in this case: `matchesPhrase(deployment.release_stage, "prod-")`.

2. Define the spans security context rule using the resulting function and specify the value of the `dt.security_context` attribute. The value of the `dt.security_context` attribute can be a literal value that you provide, or the name of another attribute; the value will be used as the value of `dt.security_context`.

## Recommendations for Distributed Tracing permissions

Permissions are typically configured for distributed tracing so users can see the complete end-to-end trace. Traces often span multiple services, hosts, or clusters, and cutting across traces with permission boundaries can result in incomplete or fragmented data. While service-level trace analytics will be less affected, and the distributed tracing app will work just fine, the potential lack of visibility impacts analytics and troubleshooting.

When setting up permissions for Distributed Tracing, consider these recommendations:

1. Avoid cutting through tracesâmake sure users can access all spans within a trace relevant to their role or deployment stage, while restricting access to sensitive services. Therefore, set graceful permissions and avoid boundaries restricting access to whole spans within a trace, as this can prevent a comprehensive analysis. For example, provide access to all spans in the relevant deployment stage (such as staging or production) or within organizational units (such as department or geographic region), and just restrict access to sensitive services (for example, the SSO).
2. Use field-level security for sensitive dataâinstead of restricting access to entire spans or traces, use field-level security to protect sensitive information.

   * Dynatrace automatically identifies selected span attributesâdefined in the [Global Field Reference](/docs/semantic-dictionary/fields "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.")âand requests [attributes marked as confidential](/docs/manage/data-privacy-and-security/configuration/configure-global-privacy-settings "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.").
   * Only users with the `builtin-sensitive-spans` and `builtin-request-attributes-spans` [field permissions](/docs/platform/grail/organize-data/assign-permissions-in-grail#field-permissions "Find out how to assign permissions to buckets and tables in Grail.") can see these sensitive fields.
   * Custom fieldsets can also be defined to specify sensitive attributes and the scope in which they apply. For example, see [Masking at display](/docs/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#masking-at-display "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.").
3. Leverage the security context to define permissions on individual span recordsâDynatrace allows you to tweak your ingested span data by adding a [`dt.security_context`](/docs/observe/business-observability/bo-event-processing/bo-security-context "Use Dynatrace powered by Grail and DQL to reshape incoming business events data for better understanding, analysis, or further processing.") attribute to specific span records. This allows you to set additional options, such as permissions for individual records. To create a security context to your ingested span data, you need to create a pipeline rule.

## User permissions for Distributed Tracing

When working with the ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**, make sure that you've read and set all the necessary permissions:

Policy scope

Table permission

Read buckets data

`storage:buckets:read`

Read span data

`storage:spans:read`

Read entities data

`storage:entities:read`

Read log data

`storage:logs:read`

Read filter-segments data

`storage:filter-segments:read`

View sensitive fields trace data [1](#fn-1-1-def) [2](#fn-1-2-def)

`storage:fieldsets:read WHERE storage:fieldset-name="builtin-sensitive-spans`

`storage:fieldsets:read WHERE storage:fieldset-name="builtin-request-attributes-spans`

Read user app states

`state:user-app-states:read`

Write user app states

`state:user-app-states:write`

Delete user app states

`state:user-app-states:delete`

1

Sensitive attributes for spans are tagged as `sensitive-spans` in [Global field reference](/docs/semantic-dictionary/fields "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.").

2

To learn more about restricted view access to personal data and confidential request attributes, see [Masking at display](/docs/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#masking-at-display "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.").

---

## observe/application-observability/distributed-tracing/storage.md

---
title: Configure data storage and retention for Distributed Tracing
source: https://www.dynatrace.com/docs/observe/application-observability/distributed-tracing/storage
scraped: 2026-02-20T21:08:29.055656
---

# Configure data storage and retention for Distributed Tracing

# Configure data storage and retention for Distributed Tracing

* Latest Dynatrace
* How-to guide
* 2-min read
* Updated on Jun 23, 2025

Distributed traces are stored in Grail buckets with a retention period from 10 days up to 10 years. By default, trace data is stored for 10 days in the `default_span` bucket.

* You can store trace data in a custom bucket for specific purposes or with a longer retention period.
* You can skip storage of trace data from a specific ingest source or based on matching conditions.

## Who is this for

This article contains information on how to configure trace data retention and storage for Distributed Tracing powered by Grail via [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline."). This article is intended for administrators controlling identity and access management.

## Prerequisites

* Dynatrace SaaS environment powered by Grail and AppEngine.
* Dynatrace Platform Subscription (DPS) with [Traces powered by Grail overview (DPS)](/docs/license/capabilities/traces "Learn how Dynatrace Traces powered by Grail consumption is calculated using the Dynatrace Platform Subscription (DPS) model.") capabilities.
* `openpipeline:configurations:write` and `openpipeline:configurations:read` permissions. To learn how to set up the permissions, see [Permissions in Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.").

## Store trace data in a custom bucket

Buckets can improve query performance by reducing query execution time and the scope of data read. With this procedure, you create a new bucket with a custom retention period for trace data. Spans that match the route and the pipeline conditions are stored according to the chosen bucket retention period.

1. Create a custom bucket

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Storage management** > **Bucket storage management** >  **Bucket**.
2. Define the new bucket

   1. Enter a bucket name and the custom retention period (days).
   2. Choose the **span** bucket table type.
3. Select **Create**.
4. Select  to refresh the bucket list.

2. Assign trace data to a bucket

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Spans** > **Pipelines** and choose an existing pipeline or create a new one.
2. In the **Storage** stage, select  **Processor** > **Bucket assignement** and define the new processor.

   1. Enter the processor name and the matching condition.
   2. Choose a bucket from the **Storage** dropdown list.
3. Select **Save**.
4. Make sure your pipeline is receiving records via a dynamic route.

   1. Go to **Dynamic routing**.
   2. Choose an existing dynamic route or create a new one.
   3. Define the route by entering a route name, a matching condition (for example `true`), and the target pipeline name.
   4. Select **Save**.

## Skip storage

With this procedure, you skip storage of spans that match the route and the pipeline conditions. Trace data is not retained.

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Spans** >**Pipelines** and choose an existing pipeline or create a new one.
2. In the **Storage** stage, select  **Processor** > **No storage assignment**.
3. Enter the processor name and matching condition.
4. Select **Save**.
5. Make sure your pipeline is receiving records via a dynamic route.

   1. Go to **Dynamic routing**.
   2. Choose an existing dynamic route or create a new one.
   3. Define the route by entering a route name, a matching condition (for example `true`), and the target pipeline name.
   4. Select **Save**.

## Related topics

* [Retain trace data for long periods](/docs/observe/application-observability/distributed-tracing/data-retention "Create and assign buckets with custom data retention for your trace data in Grail.")
* [Data retention periods](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods "Check retention times for various data types.")

---

## observe/application-observability/distributed-tracing/tracking-transactions.md

---
title: Span and trace context propagation
source: https://www.dynatrace.com/docs/observe/application-observability/distributed-tracing/tracking-transactions
scraped: 2026-02-20T21:08:07.420748
---

# Span and trace context propagation

# Span and trace context propagation

* Latest Dynatrace
* Reference
* 2-min read
* Published Jun 03, 2025

## Trace context across services

Dynatrace provides continuous visibility into service flows by propagating trace context as transactions move between services and components. This propagation is essential for end-to-end monitoring of distributed applications.

## Automatic propagation with OneAgent

When you install OneAgent, it automatically:

* Injects trace context into outgoing requests.
* Reads trace context from incoming requests.
* Maintains transaction context across service boundaries.
* Uses various mechanisms to correlate distributed traces, allowing Dynatrace to show the complete transaction flow through your application.

## Propagation mechanisms

Dynatrace employs several mechanisms to maintain trace context:

* **x-dynatrace**âfor various communication protocols. This format is proprietary to Dynatrace.
* **traceparent** and **tracestate**âW3C standard format used by both OneAgent and OpenTelemetry.
* **dtdTraceTagInfo**âcustom property for various messaging systems.

The exact implementation varies by technology: sometimes using HTTPS headers, SQS message properties, or AWS EventBridge payload injection.

## Mixed environments with OpenTelemetry

In mixed environments with both OneAgent and OpenTelemetry instrumentation, trace context propagation bridges the gap:

* Both OneAgent and OpenTelemetry use the W3C Trace Context format.
* The context must be propagated consistently across the communication channel.
* For HTTP, this is standardized in headers.
* For other protocols such as messaging and events, you need to be consistent with placement between OneAgent and OpenTelemetry.

## Turning on W3C trace context

There are several reasons to turn on W3C trace context in Dynatrace:

* Industry standard compatibilityâit aligns with W3C specification.
* Vendor-agnostic tracingâit works in heterogeneous environments with multiple monitoring solutions.
* Future-proofingâit matches industry direction for distributed tracing.

### Considerations when using W3C trace context

* Interoperability challengesâdespite being a standard, real-world implementation can vary.
* Browser and app behaviorâsome clients may send the same traceId repeatedly, affecting trace quality.
* Tool conflictsâmultiple APM tools in the same process may overwrite each other's context.

### Set up W3C trace context

To turn W3C trace context on

**Latest Dynatrace**

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **General monitoring settings** > **OneAgent features**.
2. Turn on **Send W3C Trace Context HTTP headers** and **Send W3C Trace Context gRPC headers**.

**Dynatrace Classic**

1. Go to **Settings** > **Preferences** > **OneAgent features**.
2. Turn on **Send W3C Trace Context HTTP headers** and **Send W3C Trace Context gRPC headers**.

While the W3C standard formally specifies HTTP propagation, Dynatrace and the broader industry apply these concepts to other communication protocols.

---

## observe/application-observability/distributed-tracing/use-traces-and-dql-to-spot-patterns.md

---
title: Use traces, DQL, and logs to spot patterns
source: https://www.dynatrace.com/docs/observe/application-observability/distributed-tracing/use-traces-and-dql-to-spot-patterns
scraped: 2026-02-20T21:08:05.234232
---

# Use traces, DQL, and logs to spot patterns

# Use traces, DQL, and logs to spot patterns

* Latest Dynatrace
* Tutorial
* 14-min read
* Published Nov 20, 2025

Identify abnormal patterns in traces and logs using [![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**](/docs/observe/application-observability/distributed-tracing/distributed-tracing-app "Discover the functionalities of the new Distributed Tracing app.") and [Dynatrace Query Language (DQL)](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.").

## Introduction

In this tutorial, you'll learn how to utilize traces, DQL, and logs to:

* Spot inefficient database queries.
* Understand workload patterns.
* Identify abnormalities in database usage.
* Do performance analysis.
* Understand the impact of individual database queries (for example, how much data they change).

For your ease of reference, the sections where we use ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing** are marked with this icon ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing"), while the sections where we utilize DQL are marked with . Also, for a detailed explanation of each DQL query, select **Explain this DQL query** above the DQL query code block.

## Target audience

Any user of latest Dynatrace who is eager to learn more about traces, logs, and DQL and understand how to use all these effectively.

## Learning outcome

After completing this tutorial, you'll learn how to write and efficiently utilize a variety of DQL queries, which can help you streamline troubleshooting, set up alerts, and automate workflows.

## Before you begin

### Prerequisites

All you need to complete this tutorial is access to latest Dynatrace in your environment.

Alternatively, use our [Dynatrace Playgroundï»¿](https://wkf10640.apps.dynatrace.com/) environment to follow the steps of this tutorial.

### Prior knowledge

* Familiarity with latest Dynatrace
* At least basic knowledge of DQL
* Understanding of what [Distributed Tracing](/docs/observe/application-observability/distributed-tracing "Trace and analyze in real time highly distributed systems with Grail.") is

  For an overview, check out [Unleash the Power of Distributed Tracingï»¿](https://youtu.be/8QuBqPsqZlg?si=RKrl7MW6kODQgFDA) on YouTube.

## Identify inefficient database query patterns

Whether a certain SQL statement is executed repeatedly, multiple different SQL statements are called within a trace, or one long-running query is involvedâeach scenario represents a potential performance issue we aim to detect.

### Distributed Tracing Spot query patterns with Distributed Tracing

Let's start with ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**. Thanks to this app, we can quickly identify inefficient or redundant database usage by leveraging a couple of filters, groupings, and views.

1. Go to ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**.
2. In the upper-left part of the page, under the app header, select **Spans** to view the analysis based on request spans.
3. In the **Search facets** text field, enter **Databases**, and select the **Databases** facet to reveal all related metadata.
4. Next to **Db query text**, select  (**More**) > **Group by** to instantly analyze all database queries across spans.

From this view, you can:

* Sort the data by different parameters in ascending or descending order.
* Group the data by multiple attributes.
* Narrow down the data by using various filters.

You can apply the techniques described below to exceptions, hosts, processes, remote procedure calls, and more.

![In Distributed Tracing, switch to "Spans" and group the data by "Db query text" and "Service" to reveal some database query patterns](https://dt-cdn.net/images/spot-database-query-patterns-with-distributed-tracing-3840-d081d5aa09.png)

#### Sort data

Select the table column headers to sort the data by different parameters and surface certain database query patterns.

* **Count**: Find the most frequent queries.
* **Average duration**: Spot the longest-running queries.
* **Failure rate**: View the database queries with the highest error occurrence.

#### Group data by multiple attributes

Slice your data by multiple attributes to refine your view.

1. Right above the table, expand the **Group by** dropdown list, and select **Services**. You should have the following grouping:  
   **Group by: Db query text | Service**.

   This way, you can see which database queries are shared across services.
2. Change the order of the grouping attributes. In the **Group by** dropdown list, clear **Db query text**, and then select this attribute again. You should have the following grouping:  
   **Group by: Service | Db query text**.

   In this case, you can see which database queries each service is executing.
3. Select  to the left of the currently active primary attribute to expand the attribute and view the requested analysis.

The order in which you put the grouping attributes directly influences the results you receive.

#### Narrow down data via filters

Apply filters to narrow down the data.

In the **Type to filter** text field, enter a query. For instance, enter `"Db query text" = *` to get rid of spans with empty database queries.

### Spot unusual patterns with DQL

After utilizing ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**, let's learn how to use DQL to reveal atypical patterns in your traces and logs. We recommend using [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") to run all the DQL query examples in this tutorial.

1. Go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.
2. Select  **Notebook** in the app header to create a new notebook.
3. Open the  **Add** menu, and select  **DQL**.

   You can add multiple DQL sections for all the DQL queries provided in the tutorial.
4. In the query section, enter a DQL query.
5. Select  **Run** to execute the DQL query.

![Use Notebooks to enter and run the DQL queries provided in this tutorial](https://dt-cdn.net/images/spot-unusual-patterns-with-dql-and-notebooks-3840-134c8bdd13.png)

### Discover top query types

Let's check how often a specific query type (for example, `INSERT`, `SELECT`, or `UPDATE`) shows up in your spans over time. Copy the following query to the notebook query section, and then select  **Run** to execute the DQL query.

Explain this DQL query

* `fetch spans`: Retrieve data from the `spans` table, which contains information about individual spans.
* `filter isNotNull(db.query.text)`: Include only those spans where the database query is present.
* `parse db.query.text, "string:type"`: Parse the `db.query.text` field and extract the `type` value to find out which query type we're looking at. This value is then stored in a new field called `type`.
* `makeTimeseries count(), by:{upper(type)}`: Count how many times each query type appears in our spans and create a time series for visualization.

```
fetch spans



| filter isNotNull(db.query.text)



| parse db.query.text, "string:type"



| makeTimeseries count(), by:{upper(type)}
```

Run in Playground

![Time series created with DQL that shows the count of spans with a non-null database query text, grouped by the uppercase version of the query type](https://dt-cdn.net/images/top-query-types-3008-99fd02b845.png)

Use this query to understand workload patterns or spot anomalies.

### Spot time-consuming queries

Now, let's run the query below to see how long your database queries are taking and locate the slowest queries.

Explain this DQL query

* `fetch spans`: Retrieve data from the `spans` table, which contains information about individual spans.
* `filter isNotNull(db.query.text)`: Include only those spans where the database query is present.
* `makeTimeseries sum(duration), by:{db.query.text}`: Create a time series that shows the sum of the duration of each query, sorted by query text.

```
fetch spans



| filter isNotNull(db.query.text)



| makeTimeseries sum(duration), by:{db.query.text}
```

Run in Playground

![Time series created with DQL that shows the total duration of spans grouped by database query text](https://dt-cdn.net/images/time-consuming-queries-3008-f36e14a02e.png)

This time series allows us to spot time-consuming database queries and is great for performance tuning. When a query takes too much time, there might be a more efficient query that achieves the same goal.

### Reveal high-impact queries



With this query, we can check how many rows of data are affectedâfor example, `SELECT`ed, `INSERT`ed, or `DELETE`dâby each database query.

Explain this DQL query

* `fetch spans`: Retrieve data from the `spans` table, which contains information about individual spans.
* `filter isNotNull(db.query.text)`: Include only those spans where the database query is present.
* `makeTimeseries sum(db.affected_item_count), by:{db.query.text}`: Create a time series summing up the number of the affected data rows, sorted by query text.

```
fetch spans



| filter isNotNull(db.query.text)



| makeTimeseries sum(db.affected_item_count), by:{db.query.text}
```

Run in Playground

![Time series created with DQL that shows the total number of affected items over time for each unique database query text](https://dt-cdn.net/images/high-impact-queries-3008-6e139ac96c.png)

This time series shows how many rows of data are affected by each query. If a particular query affects more data rows than others, such a query would be a great candidate for optimization.

## Spot exception patterns

In this section, let's use DQL to reveal certain exception patterns. We'll determine which exception types are most common and locate services with the most exceptions.

### Count exceptions per exception type

We focus on the number of exceptions that are coming in and learn how frequently each type of exception occurs.

Explain this DQL query

* `fetch spans`: Retrieve data from the `spans` table, which contains information about individual spans.
* `filter iAny(span.events[][span_event.name] == "exception")`: Include only those spans that have an exception.
* `expand span.events`: Flatten the `span.events` array to work with the individual span events instead of the entire array.
* `fieldsFlatten span.events, fields: {exception.type}`: Extract the `exception.type` field from each span event and flatten that into a column of its own that we can group and count.
* `makeTimeseries count(), by: {exception.type}, time:start_time`: Create a time series showing the count of exceptions, grouped by their type over time. This time series shows how frequently each type of exception occurs based on the start time of the span.

```
fetch spans



| filter iAny(span.events[][span_event.name] == "exception")



| expand span.events



| fieldsFlatten span.events, fields: {exception.type}



| makeTimeseries count(), by: {exception.type}, time:start_time
```

Run in Playground

![Time series created with DQL that shows the count of exceptions over time, grouped by their type](https://dt-cdn.net/images/exceptions-per-exception-type-3008-3a21c3be67.png)

Checking the number of exceptions per exception type can be useful for error monitoring and debugging. With this query, you can:

* Identify which types of exceptions are most common.
* Spot trends or spikes in specific exception types.
* Correlate exception frequency with deployments, traffic changes, or other system events.

### Spot services with most exceptions

With the next query, we get the list of services with the largest number of exceptions.

Explain this DQL query

* `fetch spans`: Retrieve data from the `spans` table, which contains information about individual spans.
* `filter iAny(span.events[][span_event.name] == "exception")`: Include only those spans that have an exception.
* `expand span.events`: Flatten the `span.events` array to work with the individual span events instead of the entire array.
* `fieldsFlatten span.events, fields: {exception.type, exception.message}`: Flatten the `exception.type` and `exception.message` fields.
* `summarize count(), by: {service.name, exception.message}`: Summarize these fields by count and group them by service name and exception message.

```
fetch spans



| filter iAny(span.events[][span_event.name] == "exception")



| expand span.events



| fieldsFlatten span.events, fields: {exception.type, exception.message}



| summarize count(), by: {service.name, exception.message}
```

Run in Playground

Spotting services with the highest number of exceptions can help you triage and prioritize your team's troubleshooting efforts. Moreover, knowing which exception messages are most common can help you detect recurring bugs or misconfigurations.

## Detect hotspot internal methods

When it comes to code optimization, you might first want to see what your hotspots methods are. In this case, we can analyze all spans that represent internal method calls and then group them by service and span name.

### Distributed Tracing Find long-running spans with Distributed Tracing

Here is how we achieve that in ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**.

1. Go to ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**.
2. In the upper-left part of the page, under the app header, select **Spans** to view the analysis based on request spans.
3. In the **Search facets** text field, enter **Span**, and then select **internal** under the **Span kind** facet.
4. Right above the table, expand the **Group by** dropdown list, and select **Services** and **Span name**. You should have the following grouping:  
   **Group by: Service | Span name**.
5. Select the **Average duration** table header.
6. Select  to the left of the currently active primary attribute to expand the attribute and view the requested analysis.

![In Distributed Tracing, switch to "Spans", filter for internal spans, and group the data by "Service" and "Span name" to identify long-running spans](https://dt-cdn.net/images/find-long-running-spans-with-distributed-tracing-3840-7b407b56ad.png)

You can instantly see which spans are consuming the most time.

### Identify top 10 slowest internal spans

Leveraging the next query, you get the list of slowest internal span nodes by average duration.

Explain this DQL query

* `fetch spans`: Retrieve data from the `spans` table, which contains information about individual spans.
* `` filter matchesValue(`span.kind`, "internal") ``: Focus on internal spans, thus excluding span types such as HTTP requests or messaging spans.
* `summarize {durationSum = sum(duration), callCount = count(), avgDuration = avg(duration)}, by: {service.name, span.name}`: Aggregate the span data by three verticals (their total duration, number of calls, and average duration) and group the data by service and span name to get metrics per method or operation within each service.
* `sort avgDuration desc`: Sort by average duration, starting with the longest (that is, slowest internal operations).
* `limit 10`: Restrict the output to the top 10 results.

```
fetch spans



| filter matchesValue(`span.kind`, "internal")



| summarize {durationSum = sum(duration), callCount = count(), avgDuration = avg(duration)}, by: {service.name, span.name}



| sort avgDuration desc



| limit 10
```

Run in Playground

Identifying a function in your code that consumes a significant amount of execution time or resources helps detect bottlenecks, understand runtime behavior, and streamline optimization efforts (such as reducing CPU usage, memory consumption, or response time).

## Identify log patterns: services with most logs

Now, let's unveil services that produce the largest number of logs. The query below offers us a simple way of identifying our top log producers within the context of a trace.

Explain this DQL query

* `fetch logs`: Load all available log data from the `logs` table.
* `filter isNotNull(trace_id)`: Include only those logs that are part of a trace.
* `summarize count = count(), by: {service.name}`: Sum the logs up and group them by service name, which means we count how many trace-linked logs each service has produced.
* `sort count desc`: Sort by number of logs, starting with the largest, thus services with the highest number of logs appear first.
* `limit 20`: Restrict the output to the top 20 results.

```
fetch logs



| filter isNotNull(trace_id)



| summarize count = count(), by: {service.name}



| sort count desc



| limit 20
```

Run in Playground

Such a DQL query comes in handy when you need to understand which services produce the largest number of logs. Knowing that, you can identify log-heavy services, which might be over-logging, and optimize log ingestion costs.

## Join logs and traces: count logs per service endpoint



Finally, let's find out how many logs are created per service endpoint.

By default, logs don't contain endpoint information. However, by [enriching logs with the trace ID](/docs/analyze-explore-automate/logs/lma-log-enrichment "Connect your incoming log data to traces for more precise Dynatrace analysis."), we can `join` logs and traces based on their common field.

Explain this DQL query

* `fetch spans`: Retrieve data from the `spans` table, which contains information about individual spans.
* `join [`: Perform a join operation with another dataset:

  + `fetch logs`: Load all available log data from the `logs` table.
  + `fieldsAdd trace.id = toUid(trace_id)`: Add a `trace.id` field by converting the `trace_id` field to a unique identifier (UID) using the `toUid` function.
  + `summarize logCount = count(), by: {trace.id}`: Summarize the logs data by `trace.id`, calculating the total number of logs for each trace.
  + `], on: {trace.id}`: Join the summarized logs data with the spans data on the `trace.id` field, combining the two datasets.
* `filter isNotNull(http.url)`: Include only those spans that contain a HTTP URL.
* `summarize {requestCount = count(), logCount = sum(right.logCount)}, by: {http.url}`: Sum up the request count and the log count per requested endpoint (`http.url` field).
* `fieldsAdd logPerRequest = logCount / requestCount`: Add a field where we calculate the ratio of logs per request.
* `sort logPerRequest desc`: Sort by descending order.

```
fetch spans



| join [



fetch logs



| fieldsAdd trace.id = toUid(trace_id)



| summarize logCount = count(), by: {trace.id}



], on: {trace.id}



| filter isNotNull(http.url)



| summarize {requestCount = count(), logCount = sum(right.logCount)}, by: {http.url}



| fieldsAdd logPerRequest = logCount / requestCount



| sort logPerRequest desc
```

Run in Playground

Running this query, we obtain a list sorted by endpoint that summarizes the number of requests and logs received for each endpoint, while we also calculate the ratio of logs per request. This is useful in identifying our heavy-hitting endpoints that might be producing excessive logs.

## Call to action

We hope this tutorial has given you some additional tips and tricks on how to become more efficient in analyzing traces and logs and spotting abnormalities in your environment. You can apply similar techniques to exceptions, hosts, processes, remote procedure calls, and more.

You learned how to use ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing** to detect database query patterns. Furthermore, you grasped numerous examples on how to utilize DQL to find services with the most exceptions, identify hotspot methods, and even join logs and traces to calculate the number of logs created per service endpoint.

If you believe that you need to have certain information at hand, [add the DQL query result to the dashboard](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks#edit-section-edit-controls "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace."). You might also consider [creating a metric](/docs/analyze-explore-automate/logs/lma-use-cases/lma-e2e-create-log-metric "Explore the Log Management and Analytics use case for creating a log metric.") that you can extract from the logs as they come into Dynatrace.

## Next steps

* Check out this [dedicated notebookï»¿](https://wkf10640.apps.dynatrace.com/ui/apps/dynatrace.notebooks/notebook/94d1e2b0-0d81-4803-8b5e-5b9614598d86) created in our Dynatrace Playground environment, where we share some of the tips and tricks on leveraging traces, logs, and DQL to highlight unusual patterns in your environment.
* Dive deeper into the world of DQL: visit [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") and [DQL best practices](/docs/platform/grail/dynatrace-query-language/dql-best-practices "Best practices for using Dynatrace Query Language.").
* Explore the following Dynatrace apps:

  + [![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**](/docs/observe/application-observability/distributed-tracing/distributed-tracing-app "Discover the functionalities of the new Distributed Tracing app.")
  + [![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**](/docs/analyze-explore-automate/logs/lma-logs-app "Search, filter, and analyze logs with Dynatrace Logs app to quickly investigate and share insights.")
  + [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.")
  + [![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.")

---

## observe/application-observability/distributed-tracing.md

---
title: Distributed Tracing
source: https://www.dynatrace.com/docs/observe/application-observability/distributed-tracing
scraped: 2026-02-20T21:07:02.314886
---

# Distributed Tracing

# Distributed Tracing

* Latest Dynatrace
* App
* 3-min read
* Published Jul 15, 2024

## Prerequisites

* [Dynatrace Platform Subscription (DPS)](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")

### Permissions

The following table describes the required permissions.

Permission

Description

storage:buckets:read

Read buckets data

storage:spans:read

Read span data

storage:entities:read

Read entities data

storage:logs:read

Read logs

state:user-app-states:read

Read user app state

state:user-app-states:write

Write user app state

state:user-app-states:delete

Delete user app state

storage:fieldsets:read

Read masked/sensitive fields

storage:filter-segments:read

Read filter-segments

storage:smartscape:read

Read smartscape nodes and edges

10

rows per page

Page

1

of 1

## Installation

Make sure the app is [installed in your environment](/docs/manage/hub#install "See the information about Dynatrace Hub.").

## Get started

Distributed Tracing powered by Grail helps you get the most out of your trace data in Dynatrace. It enables the ingestion and processing of petabytes of trace data, allowing you to monitor and troubleshoot errors and performance issues in complex distributed software systems at scale. Trace data follows the Dynatrace [trace-span data model](#distributed-tracing-concepts), so the analysis of all related information and attributes is intuitive and can be done via ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing** and Dynatrace Query Language (DQL). The trace data is stored in Grail, so you can leverage the power of Grail to analyze even unknown unknowns.

![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing** user-friendly interface is designed with engineers, SREs, and performance architects in mind, making it easy to visually analyze your trace data right away.

![Quickly understand response times and errors using dynamic visualization tools like histograms](https://cdn.hub.central.dynatrace.com/hub/1_LwL2KfK.png)![Dive into the details of a trace and explore related logs](https://cdn.hub.central.dynatrace.com/hub/2_WV8DuOY.png)![Easily track all exceptions within a span with clear relationships and exception chains showing root cause](https://cdn.hub.central.dynatrace.com/hub/3_5iXpQnz.png)![Surface and analyze exceptions across traces with readable stack traces, aggregated insights, and visual markers highlighting problematic spans](https://cdn.hub.central.dynatrace.com/hub/4_Qscx7Vl.png)

1 of 4Quickly understand response times and errors using dynamic visualization tools like histograms

## Learning modules

Go through the following process to learn using Distributed Tracing:

[01Exception analysis

* Tutorial
* Exception analysis helps you detect, investigate, and resolve exceptions more effectively in Dynatrace.](/docs/observe/application-observability/distributed-tracing/exception-analysis)[02Ingest traces

* How-to guide
* Instrument your applications with OneAgent or OpenTelemetry to start ingesting trace data into Dynatrace.](/docs/observe/application-observability/distributed-tracing/ingest-traces)[03Set up Grail permissions for Distributed Tracing

* How-to guide
* Manage permissions for Distributed Tracing powered by Grail.](/docs/observe/application-observability/distributed-tracing/permissions)[04Configure data storage and retention for Distributed Tracing

* How-to guide
* Manage data storage and retention for Distributed Tracing powered by Grail.](/docs/observe/application-observability/distributed-tracing/storage)[05Span and trace context propagation

* Reference
* Understand span and trace context propagation in Dynatrace and how to set them up.](/docs/observe/application-observability/distributed-tracing/tracking-transactions)[06Use traces, DQL, and logs to spot patterns

* Tutorial
* Utilize traces, logs, and DQL to visualize raw data and identify abnormal patterns.](/docs/observe/application-observability/distributed-tracing/use-traces-and-dql-to-spot-patterns)[07Distributed Tracing app

* Explanation
* Discover the functionalities of the new Distributed Tracing app.](/docs/observe/application-observability/distributed-tracing/distributed-tracing-app)[08Advanced Tracing Analytics powered by Grail

* Tutorial
* Explore advanced tracing analysis capabilities on Grail.](/docs/observe/application-observability/distributed-tracing/advanced-tracing-analytics)

## Concepts

### Distributed trace

A distributed trace is a sequence of spans, identified by a unique trace ID, that follows the path of a single request as it traverses through various services and components in a distributed system. In a modern microservice environment, it typically spans multiple services, providing a detailed view of the request's journey and performance. The trace contains semantically different attributes that make it possible to interpret and understand the collected data, helping identify bottlenecks, errors, and latency issues for efficient troubleshooting and optimization.

![Traces and services](https://dt-cdn.net/images/traces-services-1920-59a6506038.png)

#### Use cases

* Understand how requests propagate across distributed systems and microservices.
* Use high-quality data generated by distributed systems and microservices for request analysis.
* Quickly understand how each microservice is performing.
* Follow [Dynatrace Intelligence root cause analysis drill-downs](/docs/dynatrace-intelligence/root-cause-analysis/concepts "Get acquainted with root cause analysis concepts.") to identify cause-effect relationships between events.

### Span

A span represents a single operation within a distributed trace, capturing the details of the request's journey through multiple services. Each span includes attributes such as the name, the start timestamp, a list of span events (such as exceptions), the parent's span identifier, and the span kind. This informationâ**span context**â helps to put all spans and events in context with each other, so that you can trace and understand the performance and behavior of individual operations within the distributed system.

Within a trace, when the activityâ*parent span*âis completed, the next activity passes to its *child span*. A span without a parent span is called a trace *root span* and indicates the start of a trace.

The image below shows a trace traversing three services and producing a request for each service. Each request has a root span, one of which is also the root of the trace.

* A is both the first span of the trace and the first span of the request within the first service; additionally, A is a span without a parent. A is both the root of the trace and of the request.
* C is the first span of the request within the second service; additionally, C has a parent (B). C is the root of the second request.
* E is not the first span of the request within the third service. E's parent (D) is the root of the third request.

![Trace anatomy](https://dt-cdn.net/images/trace-anatomy-1920-6ba49e1863.png)

Learn more about [span semantic fields](/docs/semantic-dictionary/fields#span "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.").

The span context allows a child span to relate to the trace and its parent span. Therefore, the context needs to be propagated within a service (across different threads) but also across services and process boundaries. This typically happens via HTTP headers (like the [W3C trace contextï»¿](https://www.w3.org/TR/trace-context/)) or via unique IDs in messaging systems. To learn more about context propagation, see [Span and trace context propagation](/docs/observe/application-observability/distributed-tracing/tracking-transactions "Understand span and trace context propagation in Dynatrace and how to set them up.").

### Attribute



Attributes are key-value pairs that provide details about a span, request, or resource such as response codes, HTTP methods, and URLs. Via attributes, you can group, query, find, and analyze your traces and spans.

#### Use cases

Dynatrace uses attribute metadata to

* [Detect and name services](/docs/observe/application-observability/services/service-detection/service-detection-v1 "Find out how Dynatrace Service Detection v1 detects and names different types of services.").
* Gather data on the trace context and relationships with other entities for [Smartscape topology](/docs/analyze-explore-automate/smartscape-classic "Learn how Smartscape Classic visualizes all the entities and dependencies in your environment.").
* Connect log data to traces for [Logs](/docs/analyze-explore-automate/logs/lma-log-enrichment "Connect your incoming log data to traces for more precise Dynatrace analysis.") or [Logs Classic](/docs/analyze-explore-automate/log-monitoring/log-monitoring-configuration/log-enrichment "Learn how you can connect your incoming log data to traces for more precise Dynatrace analysis.").
* Understand how the duration of a span is affected by [service timings](/docs/observe/application-observability/services-classic/service-analysis-timing "Find out what each time in service analysis means.") (for example, CPU time, network time, or just waiting for other threads) and analyze which code was executed in the context of the span.

#### Best practices

If you collect trace data via

* OpenTelemetry, define [captured attribute settings](/docs/ingest-from/extend-dynatrace/extend-tracing/span-settings "Learn how to configure span settings for OpenTelemetry and OpenTracing.").
* OneAgent, define [requests attribute settings](/docs/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.").

Learn more about [request attributes](/docs/semantic-dictionary/fields#request-attributes "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.") and [captured attributes](/docs/semantic-dictionary/fields#captured-attributes "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.") semantic fields.

### Service

Services are traversed by distributed traces. On horizontally scaled services, specific **Service Instances** process each span. Services are determined and named based on available attributes or properties that are collected along with the spans.

#### Use cases

* [Segment requests to improve response time degradation](/docs/observe/application-observability/distributed-traces/use-cases/segment-request "Enhance your distributed system performance by segmenting requests with slow response time via Service flow and analyzing their distributed traces.").

### Data collection and context propagation

You can integrate OpenTelemetry and OneAgent to collect trace dataâlike request status, response time, versions, infrastructure information, and other relevant metadata as attributes. The trace context, including the unique trace ID, is then propagated across your apps and microservices.

#### Best practices

Before getting started with distributed tracing, understand how setup and trace data collection differs between OpenTelemetry and OneAgent. The following is an overview of the key differences.

OpenTelemetry

OneAgent

Set up

Automatic or manual

Automatic

Capturing

Automatic collection of allowed span attributes.

Automatic collection of several request attributes, including HTTP method, URL, response codes, topology data, and details about the underlying technologies.

Context

Automatically or manually contextualized log entries, depending on the instrumentation library.

Automatically contextualized

* Log entries produced by prominent log frameworks.
* Traces in Smartscape and Dynatrace Intelligence.

To get started see

* [Automatic setup with OneAgent](/docs/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.")
* [Instrumentation with OpenTelemetry](/docs/ingest-from/opentelemetry/getting-started "How to get your OpenTelemetry data into Dynatrace.")
* [Extend distributed tracing](/docs/ingest-from/extend-dynatrace/extend-tracing "Learn how to extend trace observability in Dynatrace.")

Use OpenTelemetry in combination with OneAgent to enhance your observability coverage, using the best of both.

## Use cases

Use ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing** for:

* Troubleshooting: Find out why requests fail and prevent future issues.
* Performance optimization: Understand [system performance](/docs/observe/application-observability/distributed-tracing/detect-performance-issues "Analyze your trace data and detected which requests are slow and why with the Distributed Tracing app.") and identify bottlenecks to improve reliability and user experience.
* Detailed analysis: Look into individual trace details for deeper insights.
* Exploratory analysis: Use free-form analysis to discover and explore unknown unknowns on the fly.
* Discovering unknown unknowns: Be prepared for the unknown by using free-form analysis to explore and dissect data on the fly.
* Synthesizing traces and monitoring signals: View trace data in context with other signal like logs, business events, or metrics.

## FAQ

Why do I see the message "The new tracing experience is coming to your environment soon!" when starting the Distributed Tracing app?

The new tracing experience is rolled out in stages to extend access to Dynatrace SaaS DPS customers until March 2025. The availability timing depends on the geographic region and the overall trace volume of your account. For more information, reach out to your Customer Success Manager.

Are traces in Distributed Traces Classic views still available?

Yes. Once you start analyzing traces in the Distributed Tracing app, you can continue to use Distributed Traces Classic side by side.

Which licensing package covers Distributed Tracing?

DPS FullStack and/or Custom Traces Classic. No additional costs apply when you're using the new Distributed Tracing app.

I modified facets. Can I reset them to the recommended way?

Yes. Go to ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing** and select **Show facets** > **Reset to default**.

How can I remove span.kind links with null duration?

Update to the latest version of OneAgent.

Not all traces available in Distributed Traces Classic are visible in the Distributed Tracing app.

* Make sure you have the latest version of OneAgent.
* Make sure the [OneAgent feature](/docs/ingest-from/dynatrace-oneagent/oneagent-features "Manage OneAgent features globally and per process group.") **Forward Tag 4 trace context extension** is on; this ensures OneAgent-captured traces are compatible with the W3C trace context standard.

I see incomplete end-to-end traces in the Distributed Tracing app that are shown complete in Distributed Traces Classic.

* Make sure you have the latest version of OneAgent.
* Make sure the [OneAgent feature](/docs/ingest-from/dynatrace-oneagent/oneagent-features "Manage OneAgent features globally and per process group.") **Forward Tag 4 trace context extension** is on; this ensures OneAgent-captured traces are compatible with the W3C trace context standard.

How can I filter for traces that are collected by OneAgent or ingested via OpenTelemetry?

1. Go to ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**.
2. In the facet list, enter `span source` and select the source you're interested in.

Does the new distributed tracing experience support cross-environment tracing?

Not yet.

![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Analyze and slice distributed traces by any attribute and from any source.

[Dynatrace Hubï»¿](https://www.dynatrace.com/hub/detail/distributed-tracing/?internal_source=doc&internal_medium=link&internal_campaign=cross)

## Related topics

* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [What is Dynatrace Grail?](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more.")
* [Span and trace context propagation](/docs/observe/application-observability/distributed-tracing/tracking-transactions "Understand span and trace context propagation in Dynatrace and how to set them up.")

---

## observe/application-observability/live-debugger/additional-settings.md

---
title: Configure additional settings for Live Debugging
source: https://www.dynatrace.com/docs/observe/application-observability/live-debugger/additional-settings
scraped: 2026-02-20T21:17:28.930244
---

# Configure additional settings for Live Debugging

# Configure additional settings for Live Debugging

* Latest Dynatrace
* How-to guide
* 3-min read
* Updated on Feb 19, 2026

## Manage Opt-in/Opt-out

Grants permission to control opt-in/opt-out code monitoring for the entire environment or by scope.

**Example policy**:

```
ALLOW settings:objects:read, settings:objects:write, settings:schemas:read WHERE settings:schemaId = "builtin:devobs.agent.optin";
```

## Manage breakpoints

Grants permission to manage Live Debugging breakpoints.

**Example policy**:

Allow managing breakpoints across the environment:

```
ALLOW dev-obs:breakpoints:manage;
```

## OneAgent setup

### Node

#### Transpiled code

If your application's code is being transpiled or bundled, you need to include the source maps, either in-line or as separate files.

* Webpack  
  Use either the `inline-source-map` or `source-map` values for the `devtool` option in the Webpack config file.
* Babel  
  Use either the `inline`, `both` or `true` values for the `sourceMaps` option in the Babel config file.
* TypeScript  
  Set either `inlineSourceMap` or `sourceMap` fields to `true` as well as `inlineSources` to `true` in the TypeScript config file.
* CoffeeScript  
  Pass either the `-M` (inline) or `-m` flags to the coffee CLI tool.
* Webpack + TypeScript  
  Add `sourceMap` as well as `inlineSources` to `true` (setting `inlineSourceMap` isnât enough in this case) in the TypeScript config file and use either the `inline-source-map` or `source-map` values for the `devtool` option in the Webpack config file.

#### Uglification/minification

![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger** works with uglified/minified code if it's provided with source maps. However, mangling (changing of variable names) should not be applied. Webpack may automatically mangle variable names when used in production.

```
const TerserPlugin = require("terser-webpack-plugin");



module.exports = {



// ...



optimization: {



minimizer: \[new TerserPlugin({



terserOptions: {



mangle: false,



},



})],



},



};
```

## Integrate with your version control

When debugging within a remote environment, you need to know exactly what source code it is executing.

![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger** integrates with your source control provider to fetch the correct source code for every environment.

Configure the following environment variables to enable automatic source code fetching:

* `DT_LIVEDEBUGGER_COMMIT` - String that indicates your git commit
* `DT_LIVEDEBUGGER_REMOTE_ORIGIN` - String that indicates your git remote origin

For multiple sources, use the environment variable `DT_LIVEDEBUGGER_SOURCES` to initialize the SDK with information about the sources used in your application.

`DT_LIVEDEBUGGER_SOURCES` is a semicolon-separated list of source control repository and revision information, joined by `#`. For example: `DT_LIVEDEBUGGER_SOURCES=https://github.com/myorg/MyRepo#abc123;https://github.com/otherorg/OtherRepo#xyz789`.

In JVM languages, you can also specify a path to JAR, which must contain the following attributes in its JAR manifest:

* `DT-LiveDebugger-Repository`
* `DT-LiveDebugger-Revision`

Then you can have a combination of URLs and paths to JARs.

Example: `DT_LIVEDEBUGGER_SOURCES=https://github.com/myorg/MyRepo#abc123;/path/to/lib.jar`.

## Apply data masking rules

![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger** offers data masking rules to let you control sensitive data, giving you the ability to specify which data it should not collect and display to users.

You can set the data masking rules through the Live Debugger settings page.

1. Go to **Settings** > **Observability for Developers** > **Sensitive data masking**.
2. Configure data masking by adding rules with a set of matchers that identify your sensitive data.
3. Select **Add rule** to start configuring your rule.
4. Set **Name** to the name to display for your configuration.
5. Select the rule type:

   * **Redact by variable name**  
     When masking by variable name, the entire value of any variable matching that name will be redacted. You can specify how the variable name should match:

     **Equals**: Match variables with names that are exactly the same as the input string (for example, `foo` matches only `foo`).
     **Contains**: Match variables with names that include the input string (for example, `foo` matches `myfoobar` or `foo123`).
     **Starts with**: Match variables with names that begin with the input string (for example, `foo` matches `foobar` or `foo123`).
     **Ends with**: Match variables with names that end with the input string (for example, `foo` matches `myfoo` or `barfoo`).
   * **Redact by regex**  
     When masking by regular expression, all variable values matches to that expression will be redacted.
     For example, adding a rule regarding the variable value `\[0-9]+` will replace `nameAndPassword:LordHelmet-12345` with `nameAndPassword:LordHelmet-\*\*\*\*`.

Defined rules can be reordered, and they are executed in the order in which they appear on the **Sensitive data masking** page.

The redacted data is replaced, by default, with the string `\*\*\*`.

You can choose a custom string for the rule, or replace it with an SHA-256 hash. For example, adding a rule for the variable name `secretKey` with a custom replacement of `REDACTED` replaces the output `secretKey:12345` with `secretKey:REDACTED`.

---

## observe/application-observability/live-debugger/breakpoints.md

---
title: Live Debugger breakpoints
source: https://www.dynatrace.com/docs/observe/application-observability/live-debugger/breakpoints
scraped: 2026-02-19T21:25:29.244873
---

# Live Debugger breakpoints

# Live Debugger breakpoints

* Latest Dynatrace
* Explanation
* 8-min read
* Published May 07, 2024

Dynatrace **non-breaking breakpoints** allow the OneAgent deployed in your application to fetch data from any place in your code, allowing you to observe the current state of your application and quickly find bugs in production without stopping your application.

## Add breakpoints

To add a breakpoint in ![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger**, select the gutter by the required code line number.

## Breakpoint status

Once you set a non-breaking breakpoint, it has a status associated with it (**Active**, **Pending**, **Disabled**, **Error**, or **Warning**). To view more information about the status, right-click the breakpoint and select **Status**.

For more information, you can select the Breakpoint status indicator or read more about it on this page.

Expand any of the following for a summary of a breakpoint status.

Active

`Active` status occurs when one of or more of your applications has applied the breakpoint and no errors have been reported.
In most cases, once the breakpoint has transitioned to active, you will see snapshots collected the next time the line is executed.
If you don't see any snapshots arriving, this may be due to any of the following reasons:

* **Incorrect Application**  
  You aren't invoking the correct line of code in the correct application instance.
* **Long Running Function**  
  You have placed a breakpoint on a long-running function. In this runtime, breakpoints are only applied for function calls performed after the breakpoint was created.

Pending

`Pending` status indicates that the breakpoint has not been applied to any of your applications. This could mean one of the following:

* **No Application instances**  
  The breakpoint couldn't be applied because no application instance matches the current filter. This could mean one of the following:

  + OneAgent has not been installed.
  + OneAgent has been installed, but the application can't connect to the Dynatrace service.
  + The application can connect to the Dynatrace service, but it is excluded by the current filter definition.
  + The application is currently not running and will be running in the future.
* **Wrong Source File**  
  The source file you used to set the breakpoint isn't loaded in any of the applications in the current filter.
* **No Code**  
  You have set the breakpoint on a line that has no executable code associated with it.
* **(JVM) No Debug Information**  
  You have compiled your classes without debug information. Select here for more information.
* **(Node) No Source Maps**  
  You are using a transpiled application without including source maps. Try using a minimal transpilation level, or make sure to add source maps to your deployed application. Check out the source code section for more information.
* **(Node) Code is in a Dependency**  
  You are debugging a package deployed as a dependency. This requires setting up your source repository accordingly.
* **(Node) Different File Layout**  
  File paths are changed between source repository and deployment. This requires setting up your source repository accordingly.

Disabled

`Disabled` status occurs when the breakpoint was disabled due to limits. These include limits applied by the user for that specific breakpoint (for example, time limit, hit limit).

* For more information on the reason why the breakpoint was disabled, right-click the breakpoint and select **Status**.
* To re-enable the breakpoint (by resetting the limit counter), right-click the breakpoint and select **Enable**.

Error

`Error` status occurs when one of or more of your applications has reported an error in processing, applying, or executing the breakpoint.

`Error` messages are documented within ![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger** or IDE, but examples include:

* **Source file has changed**  
  Dynatrace verifies that the source file you see in our IDE is the file you are deploying in your application. If the file version is wrong, the breakpoint will not be set. If you use source commit detection, you will see the correct git commit to use on the app instances page.
* **Breakpoint collection took too long**  
  Dynatrace employs a safeguard in case a single breakpoint takes too long to collect data from your application.
* **(Node) Running with a Debugger**  
  You are using ![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger** side-by-side with another debugger such as WebStorm Debugger.

Warning

`Warning` indicates some problems have occurred with the breakpoint, and Dynatrace is trying its best to deliver the data you've requested.

`Warning` messages are documented within ![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger** or IDE, but examples include:

* **Breakpoint collection is sampled due to rate-limiting**  
  Dynatrace employs a built-in rate-limiting mechanism to prevent breakpoints set in hot code paths from impacting application performance. This error indicates that the rate limit has been hit and the breakpoint has been rate-limited for the offending application instance. Collection is sampled to prevent performance impact on your application.
* **(JVM) Source file not found**  
  Dynatrace relies on source file hashing to ensure you are debugging the correct version of the files you are trying to debug. In most JVM based languages, include your source within your Jar/War/Ear archives.

## Data collection

The next time the code on which you set the breakpoint is invoked, Dynatrace will collect parts of the application state and send it to ![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger** or the IDE.

## Collection levels

There are several collection levels that you can set to a breakpoint. The collection levels set three different values:

* **Collection depth**: how deep to go in the collection.
* **String width**: how many characters to collect from a string.
* **Collection width**: how many elements to collect from vectors, arrays, lists, etc.

Three collection levels are available:

Level\Language

JVM

Node.js

Low

Collection depth: 2

String width: 128

Collection width: 10

Collection depth: 2

String width: 128

Collection width: 5

Medium

Collection depth: 5

String width: 512

Collection width: 15

Collection depth: 3

String width: 512

Collection width: 10

High

Collection depth: 8

String width: 4096

Collection width: 25

Collection depth: 5

String width: 4096

Collection width: 20

For example, if an object has a deeply nested field, we will stop when we reach the maximum collection depth (as in the following example). Note that `l5` has more fields, but they werenât collected because they were too deep.

![Example of an object with deeply nested fields](https://dt-cdn.net/images/2025-01-30-22-13-44-1200-5eed210010-640-cfbd29135d.jpg)

## Breakpoint limits

You can set limits on individual breakpoints to limit the amount of data that will be collected. When limits are reached, the breakpoint will be automatically disabled. Once disabled, it will not collect additional data. To re-enable a breakpoint, right-click it and select **Enable**.

The limits can be set based on:

* Time (for example, 1 Hour, 24 hours, a week)
* Hit count (the number of times the breakpoint is triggered)

Breakpoint default limit values:

* Breakpoint time limit: 7 days
* Breakpoint hit limit: 100
* Collection level: Medium

## Breakpoint conditions



Conditional breakpoints allow you to limit the data collected by OneAgent. You will only collect data when the defined expression evaluates as true. This makes it possible to debug specific scenarios and limit the number of messages you receive.
To set a condition, right-click a breakpoint and select **Edit**.

Condition types:

* Simple conditions  
  Using a simple condition, you can compare a variable with some value (or another variable).
* Advanced conditions  
  Using an advanced condition, you can define a more complex condition using logical parameters. Use `&&` for an AND statement, `||` for an OR statement, and `(` and `)` for encapsulation.

Advanced conditions support the following operators and functions:

Operator

Example

Description

`==`

`a==1`, `b=='bbb'`, `x==y`

If the values of two operands are equal, the condition is true.

`!=`

`a!=1`, `b!='bbb'`, `x!=y`

If values of two operands are not equal, the condition is true.

`>`

`a>1`, `x>y`

If the value of the left operand is greater than the value of the right operand, the condition is true.

`>=`

`a>=1`, `x>=y`

If the value of the left operand is greater than or equal to the value of the right operand, the condition is true.

`<`

`a<1`, `x<y`

If the value of left operand is less than the value of right operand, then condition becomes true.

`<=`

`a<=1`, `x<=y`

If the value of the left operand is less than or equal to the value of the right operand, the condition is true.

`in`

`'bbb' in a`

If the value of the left operand is included in the right operand, the condition is true.

`&&`

`a<=1 && b!='bbb'`

If both operands are true, the condition is true.

`||`

`a<=1 || b=='bbb'`

If any of the two operands are non-zero, the condition is true.

`()`

``` (a<=1``||``b=='bbb') && (x<y) ```

You can use parentheses to change the precedence when evaluating the condition.

`[]`

`arr[4]!=4`, `dict['a']!=4`

Set conditions regarding to a specific sequenceâs element - list, dict, etc.

`size`

`arr.size() >= 32`

Use size instead of len or length on any platform.

---

## observe/application-observability/live-debugger/ide-integration.md

---
title: Use Live Debugger with your IDE
source: https://www.dynatrace.com/docs/observe/application-observability/live-debugger/ide-integration
scraped: 2026-02-20T21:24:38.169197
---

# Use Live Debugger with your IDE

# Use Live Debugger with your IDE

* Latest Dynatrace
* How-to guide
* 4-min read
* Updated on Dec 08, 2025

You can use ![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger** directly from your own integrated development environment (IDE). Currently, Dynatrace supports Visual Studio Code and the JetBrains suite.

## Requirements

### Visual Studio Code

* Minimum supported version: 1.85.0+

### JetBrains IDEs

* Minimum supported version: 2024.1
* Recommended version: 2025.1+ for the best experience

JetBrains updates their platform versions frequently. We recommend keeping your IDE updated to the latest version to ensure compatibility with the Live Debugger plugin.

## Visual Studio Code extension

Follow the steps below to set up and use the **Observability for Developers by Dynatrace** extension in Visual Studio Code.

### 1. Set up the extension

1. In Visual Studio Code, install the [Observability for Developers by Dynatraceï»¿](https://dt-url.net/6v03quu) extension.
2. From the Primary Side Bar, select  (**Dynatrace Debugger**). The **Dynatrace Debugger** configuration panel opensânormally, on the left of your IDE.
3. Select **Log in** to sign in to Dynatrace.
4. Under **Environment**, select the environment you'd like to debug. The environment list opens above, displaying all Dynatrace environments where you have Live Debugging permissions. Select an environment from the list.
5. Select **Customize session filters** to configure your debug session. Only instances with Live Debugging enabled appear. Select filters for the instances you'd like to debug, and select **Set**.

### 2. Add a Live Debugging breakpoint

You need to add a Live Debugging [breakpoint](/docs/observe/application-observability/live-debugger/breakpoints "Learn how to add breakpoints, view available statuses, set breakpoint levels, and more.") in Visual Studio Code.

Right-click a code line number, and select **Add Live Debugging Breakpoint**. The breakpoint is applied to instances matching the filters and environment set in the previous steps.

### 3. View the data

When your breakpoints are triggered, the data streams into the **Dynatrace snapshots** panel in Visual Studio Code. Select **Open the Snapshot Panel** in the **Dynatrace Debugger** configuration panel, and then select a snapshot to see local variables, stack trace, process information, and tracing data.

### 4. Update debugging session configurationOptional

When required, you can access all session configuration options via the Primary Side Bar in Visual Studio Code. Select  (**Dynatrace Debugger**) to open the **Dynatrace Debugger** configuration panel.

### 5. Manage breakpointsOptional

* To add a breakpoint, right-click a code line number, and select **Add Live Debugging Breakpoint**.
* To open the breakpoint context menu, right-click the breakpoint icon. The following options are displayed:

  + **Breakpoint Status**
  + **Disable Breakpoint**
  + **Edit Breakpoint**
  + **Remove Breakpoint**
* To view the breakpoint list, select  (**Dynatrace Debugger**) from the Primary Side Bar in your IDE, and expand the **Live debugging breakpoints** section. Select a breakpoint in this list to view its status and editor.

## JetBrains plugin

Complete the steps below to configure and utilize the **Observability for Developers by Dynatrace** plugin in a JetBrains IDE.

### 1. Set up the plugin

1. Install the [Observability for Developers by Dynatraceï»¿](https://dt-url.net/pf23qui) plugin and restart your JetBrains IDE.
2. From the Tool window bar (usually located on the left), select  (**Observability for Developers**). The **Observability for Developers** panel opensânormally, at the bottom of the JetBrains IDE.
3. Select **Log in** to sign in to Dynatrace.
4. Expand the dropdown list in the panel header, and select the environment you want to debug. The environment list displays all Dynatrace environments where you have Live Debugging permissions.
5. Select **Filter Applications** in the panel header to configure your debug session.
   Only instances with Live Debugging enabled are displayed. Select filters for the instances you want to debug, and select **Set**.

### 2. Add a Live Debugging breakpoint

You need to add a Live Debugging [breakpoint](/docs/observe/application-observability/live-debugger/breakpoints "Learn how to add breakpoints, view available statuses, set breakpoint levels, and more.") in your JetBrains IDE.

Select the required code line number, and then select **Live Debugging Breakpoint**. The breakpoint is applied to instances matching the filters and environment set in the previous steps.

### 3. View the data

When your breakpoints are triggered, the data is streamed into the **Observability for Developers** panel. Select a snapshot to view local variables, stack trace, process information, and tracing data.

### 4. Update debugging session configurationOptional

When required, you can access all session configuration options via the header of the **Observability for Developers** panel in your JetBrains IDE. Open the panel and hover over the header to see the configuration options.

### 5. Manage breakpointsOptional

* To add a breakpoint, select the required code line number, and then select **Live Debugging Breakpoint** from the list.
* You can interact with your breakpoints directly from the code. Select the breakpoint icon to open the Breakpoint editor.
* Select **More** in the Breakpoint editor to access advanced editing options and view all breakpoints in this session.

---

## observe/application-observability/live-debugger/setup.md

---
title: Set up permissions for Live Debugging
source: https://www.dynatrace.com/docs/observe/application-observability/live-debugger/setup
scraped: 2026-02-20T21:11:55.362812
---

# Set up permissions for Live Debugging

# Set up permissions for Live Debugging

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Nov 22, 2025

## User permissions

All supported values for each IAM permission and condition are listed below. Use them to define access policies based on a fine-grained set of permissions and conditions that can be enforced per service. For more information, see [Working with policies](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies").

Permission

Description

state:user-app-states:read

Allows write required user settings

state:user-app-states:write

Allows write required user settings

settings:objects:read

Allows reading required client settings

app-settings:objects:read

Allows reading required settings, such as On-Prem Git servers

dev-obs:breakpoints:set

See Observability for Developers agents and place breakpoints.

dev-obs:breakpoints:manage

Manage Observability for Developers breakpoints.

10

rows per page

Page

1

of 1

## Set breakpoints

Grants permission to set user-level Live Debugging breakpoints.

**Conditions**:

* `dev-obs:k8s.namespace.name` - the name of the namespace that the pod is running in.

  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`
* `dev-obs:k8s.cluster.name` â the name of the cluster that the pod is running in.

  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`
* `dev-obs:dt.entity.process_group` - the process group your application is a part of.

  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`
* `dev-obs:dt.process_group.detected_name` â the detected name of the process group your application is a part of.

  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`
* `dev-obs:host.group` â the host group your application is a part of.

  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`
* `dev-obs:host.name` â the host name your application is a part of.

  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`

**Example policies**:

* Allow setting breakpoints for all instances:

  ```
  ALLOW dev-obs:breakpoints:set;
  ```
* Allow setting breakpoints for a particular host group:

  ```
  ALLOW dev-obs:breakpoints:set WHERE dev-obs:dt.process_group.detected_name = "my_process_group";
  ```

## Read snapshots

Grants permission to read user-level Live Debugging snapshots.

**Example policies**:

* Allow read snapshots:

  ```
  ALLOW storage:application.snapshots:read;



  ALLOW storage:buckets:read WHERE storage:table-name = "application.snapshots";
  ```

---

## observe/application-observability/live-debugger.md

---
title: Live Debugger
source: https://www.dynatrace.com/docs/observe/application-observability/live-debugger
scraped: 2026-02-20T21:15:02.034931
---

# Live Debugger

# Live Debugger

* Latest Dynatrace
* App
* 8-min read
* Updated on Dec 01, 2025

![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger** is a cloud native, live data collection app that gives you instant access to the code-level data you need to troubleshoot and debug quickly in any environment, from development to production.

* Access the necessary and relevant data without adding additional code, waiting for redeployment, or attempting to reproduce issues locally.
* Using non-breaking breakpoints, instantly see the complete state of your application, including stack trace, variable values, and more, all without stopping or breaking your running code.

## Prerequisites

* Dynatrace SaaS environment with a Dynatrace Platform Subscription (DPS) that includes [Code Monitoring](/docs/license/capabilities/container-monitoring#code-monitoring "Learn about the different container monitoring modes that are available with a Dynatrace Platform Subscription (DPS) license.")
* OneAgent version 1.309+ with **Java Live-Debugger** and **Node.js Live-Debugger** [OneAgent features](/docs/ingest-from/dynatrace-oneagent/oneagent-features "Manage OneAgent features globally and per process group.") enabled
* [Monitoring modes](/docs/platform/oneagent/monitoring-modes/monitoring-modes "Find out more about the available monitoring modes when using OneAgent."): Full-Stack, Infrastructure, or Discovery (with container code-module injection)
* [Code modules](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix#other-modules "Learn which capabilities are supported by OneAgent on different operating systems and platforms."): Java and Node.js

## Get started

![Real-time snapshot of debug data created once a non-breaking breakpoint has been triggered.](https://dt-cdn.net/hub/LiveDebugger_Ddll6iV.png)![Real-time snapshots with VS Code PlugIn](https://dt-cdn.net/hub/VSCode_2.png)![Real-time snapshots with JetBrains PlugIn](https://dt-cdn.net/hub/Jetbrains_1.png)

1 of 3Real-time snapshot of debug data created once a non-breaking breakpoint has been triggered.

### Activate the Live Debugger feature

To activate the Live Debugger feature

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **General monitoring settings** > **OneAgent features**.
2. Turn on **Java Live-Debugger**, **Node.js Live-Debugger**, or both, depending on your needs.
3. Restart any process that is affected.

### Enable Observability for Developers

To use ![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger**, you need to opt-in to Observability for Developers. You can enable it for specific process groups, Kubernetes namespaces, clusters, or the entire environment.

Environment level

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **Observability for Developers** > **Enable Observability for Developers**.
2. Turn on **Enable Observability for Developers**.

Process group level

1. Go to **Technologies & Processes Classic**.
2. Select the category and then the required process group.
3. On the process group overview page, select **Settings**.
4. Go to **Observability for Developers** > **Enable Observability for Developers**.
5. Turn on **Enable Observability for Developers**.

Kubernetes namespaces and clusters level

1. Go to ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**.
2. Select the required namespace or cluster.
3. In the upper-right corner, select  > **Connection settings** or, if not available, **Anomaly detection settings**.
4. Close the **Kubernetes namespace anomaly detection** or **Connection settings** overlay. You should see the namespace or cluster settings page.
5. Go to **Collect and capture** > **Observability for Developers** > **Enable Observability for Developers**.
6. Turn on **Enable Observability for Developers**.

### Enable Live Debugging in ActiveGate

ActiveGate version 1.311+

An ActiveGate isn't strictly required for ![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger** to work, but it significantly streamlines the process, especially in Kubernetes environments. It allows you to reduce your interaction with Dynatrace to one single point, which is available locally. Besides convenience, this solution optimizes traffic volume and reduces the complexity of the network and cost.

#### Host-based deployments

The Live Debugger module is enabled by default for host-based ActiveGate deployments starting from ActiveGate version 1.311.

#### Kubernetes Operator deployments

For Kubernetes Operator deployments, enable the Live Debugger module via the ActiveGate capabilities section in the DynaKube configuration.

To enable the Live Debugger module

1. Set `debugging` capability in the `DynaKube.yaml` file.

   ```
   activeGate:



   capabilities:



   - debugging
   ```

If you're using a proxy, configure it within the Environment ActiveGate as described in [Proxy for ActiveGate](/docs/ingest-from/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate "Learn how to configure ActiveGate properties to set up a proxy.").

### Start live debugging an application

To start a live debugging session

1. Go to ![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger**.
2. Select  (**Debug Configuration**) under the app header to open the **Customize your debug session** overlay.
3. Scope the instances you would like to debug.

   * Add one or more filters from the facets list.
   * Choose a filter within the application properties.

### Fetch source code

Each debug session must contain the application source code you're about to debug. ![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger** lets you quickly load sources from your local file system and various Git providers. When you integrate your source code into ![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger**, it remains between your code repository and your local browser.

There are two main ways to import your source code:

* Automatic fetching
* Manual fetching

#### Automatic fetching

![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger** can connect to a repository and automatically fetch the source code for the selected instance.

Your repository can be automatically fetched for the selected instance based on your Git permissions if your admin has already set it up.

To learn more about automatic fetching, see [Integrate with your version control](/docs/observe/application-observability/live-debugger/additional-settings#integrate-with-your-version-control "Manage breakpoint permissions, configure OneAgent-related settings, set up the version control integration, and apply data masking rules.").

#### Manual fetching

![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger** lets you easily load your relevant source code into the application. Select  under **Source Code** to open a list of the supported Git providers from which you can fetch sources.

##### Git on-premises integration

![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger** integrates directly with the cloud editions of the following Git providers, both on-premises and SaaS:

* GitHub
* Bitbucket
* GitLab
* Azure DevOps

To enable ![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger** to integrate with your on-premises or locally hosted Git provider

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Apps** > **Git On-Premise Servers**.
2. Select **Add item**.

   * **Git Provider**: Specify your Git provider.
   * **Server URL**: Provide your server's HTTP/HTTPS URL.
3. Select **Save and close**.

To use Bitbucket On-Premises, install the [Dynatrace Desktop app](#local-file-system).

##### Local file system

![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger** includes a desktop application (**Dynatrace Desktop app**) that can access source repositories from your local file system. This allows you to fetch source code from locally hosted Git providers.

**Windows**: Versions 7, 8, and 8.1 aren't supported.
**MacOS**: All versions are supported.

1. Under **Source Code**, select  > **Local Filesystem**.
2. Select **Download desktop app** to get the installation file for the Dynatrace Desktop app.
3. Install the app according to the instructions in your operating system.

### Place a non-breaking breakpoint



To get real-time code-level data

1. Select the service you want to debug.
2. Navigate to the file system.
3. Set a non-breaking breakpoint on the line of code you want to debug.

[Non-breaking breakpoints](/docs/observe/application-observability/live-debugger/breakpoints "Learn how to add breakpoints, view available statuses, set breakpoint levels, and more.") are reference breakpoints for the lines of code from which you want to collect debug data. These breakpoints don't stop your code from running. Instead, they carry the debug data collection request. Placing these breakpoints and receiving the derived snapshots don't affect your application or its users.

After placing a non-breaking breakpoint, ensure your code has been triggered so that the data is collected and appears immediately in ![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger**.

### See the debug data

Once the non-breaking breakpoint is triggered, the collected data is displayed in the Snapshots Pane at the bottom of ![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger**.

Select the required snapshot to view the following information:

* All local variables and their values.
* Process information.
* Complete stack trace leading to the breakpoint.
* Tracing information from the running application.

You can also debug code up the stack from the stack trace view, including third-party components.

## Concepts

Application Observability
:   The inability to access code-level data on demand is a challenge that most developers face when troubleshooting and debugging application issues. Instead, they have to go through long deployment cycles and investigation of logs to find the relevant data they need to understand what's going on in their running code.

Live Debugger
:   ![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger** is a cloud native debugging and live data collection solution that gives instant access to the code-level debug data you need to troubleshoot and understand complex, modern applications with no extra coding, redeployments, or restarts.

    You can use ![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger** in any environment, from development to production, and at any time, to instantly access the real-time data needed to get to the root cause of issues faster.

Dynamic logging
:   Developer teams often try to log as much as possible, as they're often not sure what data will be needed to debug an issue. This generates many unneeded logs and horrid signal-to-noise ratios.

    By shifting their logging mindset to Live Debugging, teams can reduce logging costs and, most importantly, the heavy effort required to support intense logging pipelines and cleanups.

Development collaboration
:   Collected debug data can be shared among team members when debugging application issues. This allows team members to have their own view of collected debug data and share that data with other team members for improved collaboration.

    As a result, ![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger** can become a single source of truth, the go-to place for developers to see reality as it is and collaborate on it.

On-demand trace inspection
:   ![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger** collects an object representation of traces used by your application. Developers can then correlate captured debug data with tracing data from your application.

Dev training and onboarding
:   Understanding new code can be challenging. It's twice as tricky when it's legacy code or, as often occurs, code written by someone else.

    ![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger** lets developers speed up their learning process by allowing them to observe unfamiliar code running in its native environment.

## Use cases

### Capture real-time debug data

* Instantly understand the state of your application using non-breaking breakpoints and get instant output, including your full stack trace, local and global variables, tracing data and context, and server metrics (CPU, memory, time measurements, and more).

### Troubleshoot faster

* Instantly debug the most complex flows.
* Fix bugs with zero friction, overhead, or risk.
* Get real-time data without stopping your app.
* Gain visibility into third-party dependencies and overcome debugging challenges from using open source components, external dependencies, or your legacy code.

### Dev-friendly debugging experience

* Empower your developers with on-demand access to code-level data.
* Get full visibility into your code with a simple and intuitive experience.
  Optimize R&D efficiency: Spend less time fixing bugs and more time developing value for your organization and customers.
* Never leave your comfort zone with the choice of either an IDE plugin or the Live Debugger web app.

### Test and optimize your code faster

* Instantly understand if specific line of code was reached at all with exploratory analytics

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub](https://www.dynatrace.com/hub/detail/live-debugger)

---

## observe/application-observability/multidimensional-analysis/top-database-statements.md

---
title: Top database statements
source: https://www.dynatrace.com/docs/observe/application-observability/multidimensional-analysis/top-database-statements
scraped: 2026-02-20T21:28:22.925982
---

# Top database statements

# Top database statements

* How-to guide
* 4-min read
* Updated on Sep 13, 2022

The **Top database statements** view enables you to understand the overall database activity rather than just the activity of a single database. This view can also be used to better analyze end-to-end database activities during specific timeframes.

To access the **Top database statements** page

1. Go to **Multidimensional Analysis** or ![Databases Services Classic](https://dt-cdn.net/images/databases-512-6aa6fff194.png "Databases Services Classic") **Database Services Classic**.
2. Select **Top database statements**.

## Analyze database statements

The **Top database statements** page displays a chart indicating the top SQL and NoSQL statements in your environment over time. The chart also highlights a few top statements based on execution count. The table following the chart lists the 100 **top dimensions**.

![Top database statements page](https://dt-cdn.net/images/top-database-statements-3564-3bd08ea1b1.png)

You can configure a view by adjusting **Metric** and the other parameters or by adding a filter.

* Different metrics, such as **Fetch count**, **Response time**, and **Row count**, result in different order of the statements. Depending on the time consumption per statement, the frequency of statement execution, or error rate, the page first lists statements that are executed more frequently or are more expensive from a resource perspective, from the highest value of the chosen metric to the lowest.
* You can use **Filter requests** to narrow down the list of database statements.

Filter request examples

The following example shows a view configured with the metric **Response time**, filtered by value range `â¥100ms`. The list shows all database statements which response took at least 100 ms.

![Response time filter in top database statement analysis](https://dt-cdn.net/images/response-time-filter-in-top-database-statement-analysis-3684-0962b8fba9.png)

The view in this example is configured with the metric **Fetch count** filtered by value range `â¥5`. The list shows database statement with at least 5 database fetches per execution.

![Fetch count in top database statements analysis](https://dt-cdn.net/images/fetch-count-in-top-database-statements-analysis-3548-bdb184cbd0.png)

* You can export the table data in a comma-separated values (CSV) file.

  1. In the lower-right corner of the page, select **Show export menu** ![More](https://dt-cdn.net/images/more-icon-01c8b008ca.svg "More").

     ![Show export menu](https://dt-cdn.net/images/show-export-menu-107-2a8a76c9a2.png)
  2. Select **Export visible data** or **Export table data**.

     Option

     Exported data

     Fields

     Number of entries

     **Export visible data**

     The currently displayed area of the table, taking into account applied filters

     Only visible data

     Up to 100 top dimensions

     **Export table data**

     All table data

     All the available data related to top dimensions

     Up to 100 top dimensions
* The chart uses [trace and request data](/docs/observe/application-observability/multidimensional-analysis#data-source "Configure a multidimensional analysis view and save it as a calculated metric."), which has different data retention periods. For timeframes containing data older than 10 days, you can turn on the **Show data retention** toggle to better understand which data is available for which period directly from the chart.

## Analyze individual SQL statements

To access several statement-specific analysis views, including **Service backtrace** and **Outliers** analysis, select **More** (**â¦**).

### Database statement details

You can directly access analysis for individual statements by selecting **Filter**. Alternatively, select **More** (**â¦**) > **Statement details**.

![Distributed traces of individual database statement](https://dt-cdn.net/images/distributed-traces-top-database-statements-1593-b6fb81c79e.png)

Select a statement to view all permutations of the selected query. Dynatrace aggregates the inserts, updates, and deletes on a per-table basis.

![Details of an individual database statement](https://dt-cdn.net/images/details-individual-statements-1564-56ba5e5697.png)

### Database service backtrace

To access backtrace analysis for the selected statement, select **Service backtrace** from the **Analyze** menu. The **Backtrace** page provides details on the user interaction that triggered the selected SQL statement permutation and the user interaction or service request that originated the statement. Select any of the incoming requests to view a visualization of the backtrace.

![Backtrace for top database statements](https://dt-cdn.net/images/backtrace-for-top-database-statements-1699-76085f0963.png)

### Response time distribution

To understand the response time distribution of the command, select **Outliers** from the **Analyze** menu. The **Response time distribution** page shows the number of requests that fell within various response time ranges. Select any column in the chart to analyze the specific requests that fell within that specific response time range.

![Response time distribution of requests of a service](https://dt-cdn.net/images/response-time-distribution-database-statements-1800-8ff28dc6c7.png)

### View single executions

To view the individual executions of each command, select **More** (**â¦**) > **Distributed traces** > **Trace**.

The **Fetches** column shows the number of database round trips per SQL execution. Because most database drivers page result sets, roundtrips are normally fetched in sets of **Rows returned** per fetch. Therefore, if a result set has 200 rows and you have a fetch size of 50 rows per fetch, it will take 4 fetches to get all the data. More fetches mean slower response time. However, having too large of a fetch size can also lead to poor memory usage and you typically wouldn't read an entire data set anyway.

Select any execution in the list to access its distributed trace.

![PurePathÂ® trace of an execution](https://dt-cdn.net/images/purepath-database-statements-1597-d6db847c88.png)

## Example: Understand SQL for Service flow

While SQL analysis is available at multiple locations in the service-analysis workflow, it has been added as the primary analysis view for databases in the [**Service flow**](/docs/observe/application-observability/services-classic/service-flow "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment.") view. The following example indicates a service flow that has already been filtered to focus on a particular chain of calls. You can see that, whenever the **Customer Frontend** service calls the **JourneyService**, **58%** of the **response time contribution** can be attributed to the **EasyTravel** SQL service.

![From service flow to database statement](https://dt-cdn.net/images/from-service-flow-to-database-statement-1748-bff9188259.png)

The default action has changed and now displays **View database statements**.

You can perform several types of analysis:

1. To see the database statements that were executed by the selected flow within the analysis timeframe, select **View database statements**. This can be tremendously valuable because it shows you why a database contributes a specified amount of time.
2. To reveal which statements have the highest overall response time, sort the **Top dimensions** list by **Count/min**.

![Example of SQL service multidimensional analysis](https://dt-cdn.net/images/example-of-sql-service-multidimensional-analysis-3574-7c039d0068.png)

3. Select **More** (**â¦**) and then:

* Select **Outliers** to see the distribution of response times.
* Select **Distributed traces** to understand the evolution of each individual SQL statement over time, along with the average **Rows returned** count.
* Select **Service backtrace** to see which user clicks led to the slowest executions of the statement.

---

## observe/application-observability/multidimensional-analysis/top-web-requests.md

---
title: Top web requests
source: https://www.dynatrace.com/docs/observe/application-observability/multidimensional-analysis/top-web-requests
scraped: 2026-02-19T21:22:32.200674
---

# Top web requests

# Top web requests

* How-to guide
* 4-min read
* Updated on Sep 13, 2022

The highly flexible **Top web requests** view enables you to analyze the top web requests across all your services and to look for requests that originate from or are destined to specific URLs. This view is easily configurable and serves as a convenient entry point for in-depth analysis of your services.

To access the **Top web requests** analysis page

1. Go to **Multidimensional Analysis**.
2. Click the **Top web requests** tile.

![Top web requests page](https://dt-cdn.net/images/top-web-requests-page-3518-5c4cc7fb02.png)

## Configure view

The **Top web requests** page lists all web requests that occurred during the selected timeframe and within the selected management zone. In **Configure view**, you can set up multiple filtering capabilities. The view updates automatically as you change the parameters.

Parameter

Description

Metric

The metric to be analyzedâset by default to **Request count**.

Aggregation

How the metric values are aggregatedâavailable aggregations depend on the selected metric.

Split mode

How dimensions specified in **Split by dimension** are treated.

* **Split by services**âeach dimension is displayed separately for each service.
* **Merge by services**âsame dimensions from different services are merged into one.

Split by dimension

A list of dimensions by which the requests are split. By default the request name (`{Request:Name}`) dimension is set.

You can specify several dimensions. Place your cursor in the input field to see the available options. The requests are split by dimension in the specified order.

Filter requests

Filter the requests to be included to the view. By default the following criteria are set:

* **Service type**: `Web service`
* **Service type**: `Web request service`

You can provide additional criteria. Place your cursor in the input field to see the available options.

Criteria of the same type are grouped by the OR logic. Criteria of different types are grouped by the AND logic.

Once the view is configured, you can save it for quick access in the future. Just select **Save view** and provide a name.

You can also save the configuration as a calculated service metric and use it as any other metric in Dynatrace (for example, for [alerting](/docs/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace")).

You can export the table data in a comma-separated values (CSV) file.

1. In the lower-right corner of the page, select **Show export menu** ![More](https://dt-cdn.net/images/more-icon-01c8b008ca.svg "More").

   ![Show export menu](https://dt-cdn.net/images/show-export-menu-107-2a8a76c9a2.png)
2. Select **Export visible data** or **Export table data**.

   Option

   Exported data

   Fields

   Number of entries

   **Export visible data**

   The currently displayed area of the table, taking into account applied filters

   Only visible data

   Up to 100 top dimensions

   **Export table data**

   All table data

   All the available data related to top dimensions

   Up to 100 top dimensions

## View

* The chart on the **Top web requests** page shows the top 15 dimensions (all other dimensions are aggregated into a single dimension), and the table beneath contains up to 85 more dimensions, bringing the total number of chartable dimensions to 100. The view instantly adapts to the changes you make in the **Configure view** pane.
* The chart uses [trace and request data](/docs/observe/application-observability/multidimensional-analysis#data-source "Configure a multidimensional analysis view and save it as a calculated metric."), which has different data retention periods. For timeframes containing data older than 10 days, you can turn on the **Show data retention** toggle to better understand which data is available for which period directly from the chart.
* In the **Actions** column of the table, you can select:

  + **Filter** ![Filter](https://dt-cdn.net/images/filter-icon-41ddd02d66.svg "Filter") to filter the view for the specified dimension.
  + **More** (**â¦**) to access further analysis options from the [**Analyze** menu](/docs/observe/application-observability/services-classic/context-specific-drill-down#analyze-menu "Learn about easy navigation and filtering for services analysis.").

## Example use cases

Here you can find some use cases for the **Top web requests** view.

### Find a particular URL

With **Top web request** view you can focus your analysis on requests that come from or are going to a particular URL.

1. Specify `{URL:Host}{Relative-URL}` in the **Split by dimension** field to split your requests based on URLs.
2. Now filter the requests to a particular URL. In the **Filter requests** field, select the `Web request URL` filter type and provide the pattern for the URL. Note that this filter uses the **CONTAINS** operator.

### Find requests with error response codes

You can easily narrow down your requests to those that returned an error response code (that is, any error code in the range **4xx**). After you configure the dimensions that you're interested in, place your cursor into the **Filter requests** field and select the **HTTP response code** filter type (you can start typing to narrow down the suggestions). Then select the **4xx** criteria and wait for data processing to complete.

### Find POST HTTP requests

You have two options for viewing your POST (or any other HTTP method) at a glance: (1) set the HTTP method dimension or (2) filter the request by HTTP method.

#### Dimension

In this case you'll see all your requests grouped by HTTP method and by any other dimension you provide. Just specify `{HTTP-Method}` in the **Split by dimension** field.

#### Filter

In this case, all non-POST requests are filtered out, so you can focus your analysis. Just specify the `HTTP method` and select `POST` value in the **Filter requests** field.

## Related topics

* [Service metrics API](/docs/dynatrace-api/configuration-api/calculated-metrics/service-metrics "Manage calculated service metrics via the Dynatrace configuration API.")

---

## observe/application-observability/multidimensional-analysis.md

---
title: Multidimensional analysis
source: https://www.dynatrace.com/docs/observe/application-observability/multidimensional-analysis
scraped: 2026-02-19T21:16:57.123946
---

# Multidimensional analysis

# Multidimensional analysis

* How-to guide
* 4-min read
* Updated on Sep 13, 2022

The **Multidimensional analysis** view enables you to analyze web requests of your services with fine-tuned filtering, so you can focus your analysis on the dimensions that matter most. This view is easily configurable and serves as a convenient entry point for in-depth analysis of your services.

With multidimensional analysis, you can investigate custom views: **Top web requests**, **Database statements**, and **Exception analysis**.

To access the **Multidimensional analysis** page

1. Go to **Multidimensional Analysis**.
2. Choose one of the analysis options that you want to investigate, or **Create analysis view**.

## Pre-defined views

[### Top web requests

Analyze the most frequent and most expensive web requests.](/docs/observe/application-observability/multidimensional-analysis/top-web-requests "Learn how to analyze all web requests across all of your services using Dynatrace.")[### Top database statements

Analyze the most frequent and most expensive database statements.](/docs/observe/application-observability/multidimensional-analysis/top-database-statements "Understand the database activity across your environment with Dynatrace.")[### Exception analysis

Understand and analyze all code-level exceptions.](/docs/observe/application-observability/multidimensional-analysis/exception-analysis "Learn how Dynatrace can help you see which exceptions occurred in your environment during a selected analysis timeframe.")

## Data source

Multidimensional analysis uses trace and request data as its data source, which includes information on [distributed traces](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods#traces-grail "Check retention times for various data types.") and [requests](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods#request-attributes "Check retention times for various data types.").

* For timeframes shorter than two hours, a higher resolution (below 1 minute) is used.
* For larger amounts of data, especially for longer timeframes or unfiltered analysis, sampling is applied: only a fraction of trace and request data is used.
* To view the information about the data used for analysis and suggestions on how to improve accuracy, hover over **Refine**.
* To include more data to the analysis, select **Refine**.

Multidimensional analysis vs charts

Unlike [Data Explorer](/docs/analyze-explore-automate/explorer#limitations "Query for metrics and transform results to gain desired insights."), multidimensional analysis uses trace and request data, not metric data, so values on multidimensional analysis charts might differ from values on custom charts.

## Configure view

In **Configure view**, you can set up multiple filtering capabilities. The view updates automatically as you change the parameters.

Parameter

Description

Metric

The metric to be analyzed.

Aggregation

How the metric values are aggregated. Available aggregations depend on the selected metric.

Split mode

How dimensions specified in **Split by dimension** are treated.

* **Split by services**âeach dimension is displayed separately for each service.
* **Merge by services**âsame dimensions from different services are merged into one.

Split by dimension

A list of dimensions by which the requests are split.

You can specify several dimensions. Place your cursor in the input field to see the available options. The requests are split by dimension in the specified order.

Filter requests

Filter the requests to be included to the view. Place your cursor in the input field to see the available options.

Criteria of the same type are grouped by **OR** logic. Criteria of different types are grouped by **AND** logic.

You can export the table data in a comma-separated values (CSV) file.

1. In the lower-right corner of the page, select **Show export menu** ![More](https://dt-cdn.net/images/more-icon-01c8b008ca.svg "More").

   ![Show export menu](https://dt-cdn.net/images/show-export-menu-107-2a8a76c9a2.png)
2. Select **Export visible data** or **Export table data**.

   Option

   Exported data

   Fields

   Number of entries

   **Export visible data**

   The currently displayed area of the table, taking into account applied filters

   Only visible data

   Up to 100 top dimensions

   **Export table data**

   All table data

   All the available data related to top dimensions

   Up to 100 top dimensions

## View

![Top database statements page](https://dt-cdn.net/images/top-database-statements-3564-3bd08ea1b1.png)

The chart shows the top 15 dimensions (all other dimensions are aggregated into a single dimension) and the table beneath contains up to 85 more dimensions, bringing the total number of chartable dimensions to 100. The view instantly adapts to the changes you make in the **Configure view** pane.

In the **Actions** column of the table, you can select:

* **Filter** ![Filter](https://dt-cdn.net/images/filter-icon-41ddd02d66.svg "Filter") to filter the view for the specified dimension.
* **More** (**â¦**) to access further analysis options from the [**Analyze** menu](/docs/observe/application-observability/services-classic/context-specific-drill-down#analyze-menu "Learn about easy navigation and filtering for services analysis.").

For timeframes containing data older than 10 days, you can turn on **Show data retention** to better understand which data is available for which period directly from the chart.

### Save view

Once the view is configured, you can save it for quick access in the future. Just select **Save** view and provide a name.

Dynatrace provides several views out of the box:

* [Exception analysis](/docs/observe/application-observability/multidimensional-analysis/exception-analysis "Learn how Dynatrace can help you see which exceptions occurred in your environment during a selected analysis timeframe.")
* [Top database statements](/docs/observe/application-observability/multidimensional-analysis/top-database-statements "Understand the database activity across your environment with Dynatrace.")
* [Top web requests](/docs/observe/application-observability/multidimensional-analysis/top-web-requests "Learn how to analyze all web requests across all of your services using Dynatrace.")

## Calculated service metric

You can save the configured view as a calculated service metric, which you can use just like any other Dynatrace metric, for example for [charting](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") or [data export via API](/docs/dynatrace-api/environment-api/metric-v2/get-data-points "Read data points of one or multiple metrics via Metrics v2 API.").

Only new data is written to calculated metrics; retrospective data is not included.

Limits

* Only new data is written to calculated metrics; retrospective data is not included.
* You can have up to 500 enabled calculated metrics per environment and up to 100 enabled calculated metrics per service.
* Classic calculated metrics support at most 100 dimension values. This is referred to as the "top X" rule, as you can select fewer depending on your configuration. However you choose the top 100 dimension values, the remaining dimensions are aggregated into a single timeseries and the dimension value is accessible through a special `remainder` dimension. The [remainder](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#remainder "Configure the metric selector for the Metric v2 API.") filter condition allowing you to filter on this `remainder` dimension.

* Grail calculated service metrics with cardinality higher than 2000 within any 5-minute window in the past 2 weeks or since the last metric change are automatically disabled in Grail. Enabling such metrics on Grail is not allowed. If the metric is already enabled on Grail, you are informed of the metric rejection via the [**Metric & Dimensions Usage + Rejections**](/docs/dynatrace-api/environment-api/metric-v2/best-practices#identify-high-cardinality-situations "Best practices for metrics.") ready-made dashboard. To enable a Classic metric on Grail and keep collecting incoming data on Grail, make sure cardinality stays below the limit.

To create a calculated service metric from a multidimensional analysis view

1. Go to **Multidimensional Analysis**.
2. Select **Create analysis view**.
3. Optional Select the management zone. The new metric will be restricted to data from this zone.
4. Configure the view. Find the description of available options in the [**Configure view**](#configure) section above.
5. In the **View** pane, select **Create metric**.

   ![Create calculated metric](https://dt-cdn.net/images/service-calculated-metric-create-328-e5859c1ea9.png)
6. Specify the name for the metric. The name is added to the metric key automatically.
7. Optional If needed, customize the metric key.

   Once a metric is created, you can't change its key.
8. Optional If you want to fine-tune your metric, select **Advanced options** to configure additional parameters of the metric. For details, see [Calculated metrics for services](/docs/observe/application-observability/services/calculated-service-metric "Learn how to create a calculated metric based on web requests.").
9. Select **Create metric**.

## Related topics

* [Service metrics API](/docs/dynatrace-api/configuration-api/calculated-metrics/service-metrics "Manage calculated service metrics via the Dynatrace configuration API.")
* [Calculated metrics for services](/docs/observe/application-observability/services/calculated-service-metric "Learn how to create a calculated metric based on web requests.")

---

## observe/application-observability/profiling-and-optimization/crash-analysis.md

---
title: Crash analysis
source: https://www.dynatrace.com/docs/observe/application-observability/profiling-and-optimization/crash-analysis
scraped: 2026-02-18T21:27:39.150599
---

# Crash analysis

# Crash analysis

* How-to guide
* 7-min read
* Published Jul 19, 2017

Processes crash for a multitude of reasons and itâs often difficult to understand the root causes that contribute to such crashes. When a monitored process crashes, youâll see a process crash entry in the **Events** section of each affected process and host page. The example process below has some availability problems (shown in red on the timeline). By selecting the affected timeframe in the timeline, the **Events** section shows you the number of process crashes that occurred during that timeframe (1 crash in this example).

![Event details](https://dt-cdn.net/images/event-details-3321-d2e1237b17.png)

Select **Process crash details** to view a detailed list of the crashes that occurred during the selected timeframe. Here youâll find all details related to why each process crashed.

![Process crash](https://dt-cdn.net/images/process-crash-1418-427d215ec4.png)

The provided crash details include the signal that killed the process (for example, `Segmentation fault` or `Abort`), the execution stack frame that crashed, and more. The crash typeâsuch as a native core dump, Java core dump, or abnormal program exit due to an exceptionâdetermines which crash details are available.

This functionality works for all processes on each monitored host.

## Analyze additional crash artifacts

Crash details often include a **Download** button that provides access to additional crash artifacts, such as `hs_err_pid` files for Java crashes, text files that provide analysis of Linux and Windows core dumps, or files containing the .NET, Java, or Node.js exceptions that were potentially responsible for the crashes. For example, the **Segmentation fault** crash report above resulted in a core dump. OneAgent analyzed the core dump automatically and then produced the following report as a log artifact:

```
dumpproc version 1.108.0.20161025-115919, installer version 1.108.0.20161025-121046



2016-11-09 18:00:44: Application 'CreditCardAutho', inner pid '15891', outer pid '0', signal: 'Segmentation fault' (11)



process group ID: 0x441b2cb89962033d



process group instance ID: 0xfe58bab23100f42c



process group Name: easytravel-*-x*



threadCount: 1



thread: 0 - stack range: 0x7ffeda572000-0x7ffeda594000, size: 136 kB



0x00007ffeda592be0 0x00007f4de477604d libpthread-2.15.so!<imagebase>+0xf04d



0x00007ffeda592bf0 0x00000000004038d8 CreditCardAuthorizationS64!main+0x1b8



0x00007ffeda592c60 0x00007f4de41c676d libc-2.15.so!__libc_start_main+0xed



0x00007ffeda592d20 0x000000000040329a CreditCardAuthorizationS64!<imagebase>+0x329a



mapped files:



0000000000400000-000000000041e000 0 /home/labuser/easytravel-2.0.0-x64/CreditCardAuthorizationS64 (MD5: da5992daf5ba3b76c633c853c7da5e87)



000000000051d000-000000000051e000 1d /home/labuser/easytravel-2.0.0-x64/CreditCardAuthorizationS64 (MD5: da5992daf5ba3b76c633c853c7da5e87)



00007f4de41a5000-00007f4de4359000 0 /lib/x86_64-linux-gnu/libc-2.15.so (GNU Build-Id: aa64a66ac46bff200848c0a0694011bd0140ab4e)



00007f4de4359000-00007f4de4558000 1b4 /lib/x86_64-linux-gnu/libc-2.15.so (GNU Build-Id: aa64a66ac46bff200848c0a0694011bd0140ab4e)



00007f4de4558000-00007f4de455c000 1b3 /lib/x86_64-linux-gnu/libc-2.15.so (GNU Build-Id: aa64a66ac46bff200848c0a0694011bd0140ab4e)



00007f4de455c000-00007f4de455e000 1b7 /lib/x86_64-linux-gnu/libc-2.15.so (GNU Build-Id: aa64a66ac46bff200848c0a0694011bd0140ab4e)



00007f4de4563000-00007f4de4565000 0 /lib/x86_64-linux-gnu/libdl-2.15.so (GNU Build-Id: d181af551dbbc43e9d55913d532635fde18e7c4e)



00007f4de4565000-00007f4de4765000 2 /lib/x86_64-linux-gnu/libdl-2.15.so (GNU Build-Id: d181af551dbbc43e9d55913d532635fde18e7c4e)



00007f4de4765000-00007f4de4766000 2 /lib/x86_64-linux-gnu/libdl-2.15.so (GNU Build-Id: d181af551dbbc43e9d55913d532635fde18e7c4e)



00007f4de4766000-00007f4de4767000 3 /lib/x86_64-linux-gnu/libdl-2.15.so (GNU Build-Id: d181af551dbbc43e9d55913d532635fde18e7c4e)



00007f4de4767000-00007f4de477f000 0 /lib/x86_64-linux-gnu/libpthread-2.15.so (GNU Build-Id: c340af9dee97c17c730f7d03693286c5194a46b8)



00007f4de477f000-00007f4de497e000 18 /lib/x86_64-linux-gnu/libpthread-2.15.so (GNU Build-Id: c340af9dee97c17c730f7d03693286c5194a46b8)



00007f4de497e000-00007f4de497f000 17 /lib/x86_64-linux-gnu/libpthread-2.15.so (GNU Build-Id: c340af9dee97c17c730f7d03693286c5194a46b8)



00007f4de497f000-00007f4de4980000 18 /lib/x86_64-linux-gnu/libpthread-2.15.so (GNU Build-Id: c340af9dee97c17c730f7d03693286c5194a46b8)



00007f4de4984000-00007f4de4a02000 0 /lib/x86_64-linux-gnu/liboneagentproc.so (1.108.0.20161025-115919)



00007f4de4a02000-00007f4de4c01000 7e /lib/x86_64-linux-gnu/liboneagentproc.so (1.108.0.20161025-115919)



00007f4de4c01000-00007f4de4c03000 7d /lib/x86_64-linux-gnu/liboneagentproc.so (1.108.0.20161025-115919)



00007f4de4c03000-00007f4de4c05000 7f /lib/x86_64-linux-gnu/liboneagentproc.so (1.108.0.20161025-115919)



00007f4de4cc0000-00007f4de4ce2000 0 /lib/x86_64-linux-gnu/ld-2.15.so (GNU Build-Id: e25ad1a11ccf57e734116b8ec9c69f643dca9f18)



00007f4de4ee2000-00007f4de4ee3000 22 /lib/x86_64-linux-gnu/ld-2.15.so (GNU Build-Id: e25ad1a11ccf57e734116b8ec9c69f643dca9f18)



00007f4de4ee3000-00007f4de4ee5000 23 /lib/x86_64-linux-gnu/ld-2.15.so (GNU Build-Id: e25ad1a11ccf57e734116b8ec9c69f643dca9f18)
```

## Protect sensitive user data

Crash reports might include sensitive personal information that should not be viewed by all users. For this reason, your Dynatrace administrator must enable the [**View logs** account-security option](/docs/manage/identity-access-management/permission-management/role-based-permissions#environment "Role-based permissions") and the [**View sensitive request data**](/docs/manage/identity-access-management/permission-management/role-based-permissions#environment "Role-based permissions") permissions in your user profile before you can view personal data. This option is disabled by default for all non-admin users and must be explicitly enabled before you can access log contents.

## Crash handling on Windows

In order for a generic Windows process crash (core dump) to be visible to Dynatrace, the crash must be detected by Windows Error Reporting. For this reason, the Windows Error Reporting service must be enabled.

![Process crashes 6](https://dt-cdn.net/images/process-crashes6-1142-db9303969a.png)

When a crash occurs on Windows, a dialog appears, asking if you want to debug or close the crashed application. This is not desirable for headless systems. You can disable this dialog by adding a value to the registry, as shown below:

`[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\Windows Error Reporting] "DontShowUI"=dword:00000001`

![Process crashes 8](https://dt-cdn.net/images/process-crashes8-880-1d0cfb52b5.png)

You can learn about other valuable settings related to Windows Error Reporting by visiting [Microsoft documentationï»¿](https://msdn.microsoft.com/en-us/library/windows/desktop/bb513638(v=vs.85).aspx).

## Linux core dump handling

In Linux, the way the kernel handles the core dump is set in `/proc/sys/kernel/core_pattern`. Beginning with kernel 2.6.19 (1), there are two methods of dealing with application crashes. The core dump might be written to a file pointed to by the `/proc/sys/kernel/core_pattern` entry or pushed to an applicationâthe entry must be prefixed with a vertical slash character (`|`) character.

Because Suse Linux uses the first method, the entry is similar to
`/proc/sys/kernel/core_pattern:core`. This means that a file with the name `core` is written in the current working directory of the crashed process.

Ubuntu and Red Hat generally rely on their own tools to report crash dumps, so the lines appear as follows:  
`|/usr/share/apport/apport %p %s %c %P`  
or  
`|/usr/libexec/abrt-hook-ccpp %s %c %p %u %g %t e`

In the last example, when a program crashes, the `coredump` output is pushed to `stdin` of the application given in the first parameter. Moreover, the kernel fills the values of any parameters formatted as `%[a-zA-Z]`. The `apport` reporting service overwrites the file `/proc/sys/kernel/core_pattern`. If `apport` is enabled (in `/etc/default/apport`), then the `/proc/sys/kernel/core_pattern` configuration setting is set when the `apport` crash reporting service starts on system boot.
[Read moreâ¦ï»¿](https://askubuntu.com/questions/420410/how-to-permanently-edit-the-core-pattern-file)

### Operating system changes



OneAgent installer performs the following changes to your system to handle core dumps.

#### Disabling ABRT and Apport

[ABRTï»¿](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/deployment_guide/ch-abrt) (Red Hat) and [Apportï»¿](https://launchpad.net/ubuntu/+source/apport) (Debian) services are stopped and disabled.

Both services are re-enabled during [OneAgent uninstallation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/uninstall-oneagent-on-linux "Learn how you can remove OneAgent from your Linux-based system.").

For more information, see [OneAgent security on Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/oneagent-security-linux#operating-system-changes "Learn about Dynatrace OneAgent security and modifications to your Linux-based system").

#### Core pattern handling

The OneAgent installer overwrites the core pattern with its own command but preserves the original pattern.

* The content of the original `/proc/sys/kernel/core_pattern` file is copied to:

  + OneAgent version 1.301 and earlier `/opt/dynatrace/oneagent/agent/conf/original_core_pattern`
  + OneAgent version 1.302+ `/var/lib/dynatrace/oneagent/agent/backup/original_core_pattern`

  When OneAgent is uninstalled, the original core pattern present in this file, is restored to `/proc/sys/kernel/core_pattern`.
* The content of the original `kernel.core_pattern` option of `/etc/sysctl.conf` is copied to:

  + OneAgent version 1.301 and earlier `/opt/dynatrace/oneagent/agent/conf/original.sysctl.corepattern`
  + OneAgent version 1.302+ `/var/lib/dynatrace/oneagent/agent/backup/original.sysctl.corepattern`

  When OneAgent is uninstalled, the original core pattern present in this file is restored to `kernel.core_pattern` in `/etc/sysctl.conf`. If `kernel.core_pattern` was not present in `/etc/sysctl.conf` before OneAgent installation, the backup file is not created.

Depending on the original entry in `core_pattern`, Dynatrace will write different patterns to `core_pattern`. The possible configurations and expected entries after installation are listed below:

| Original core\_pattern entry | core\_pattern after ruxitdumpproc installation | Comment |
| --- | --- | --- |
| core | /opt/dynatrace/oneagent/agent/rdp -p %p -e %e -s %s | Simple core dump without parameters. |
| core\_%s\_%e | /opt/dynatrace/oneagent/agent/rdp -p %p -e %e -s %s -kp %s,%e | Simple core dump with parameters in the filename. The `-kp` parameter is appended along with all kernel parameters needed for Dynatrace to substitute in the original filename. |
| /usr/share/apport/apport | /opt/dynatrace/oneagent/agent/rdp -p %p -e %e -s %s | Core dump next application without parameters. The `-a` argument is not appended to the output `core_pattern` entry if there are no parameters. |
| /usr/share/apport/apport %p %s %c %P | /opt/dynatrace/oneagent/agent/rdp -p %p -e %e -s %s -a %p %s %c %P | Core dump next application with parameters. The `-a` argument gets appended along with all of the parameters after the binary path to `apport`. |

### Core handling by OneAgent dumpproc

When a crash occurs:

1. `rdp` is called to dump the core to OneAgent folders. This core is used by the Crash Reporting functionality.
2. OneAgent reads `original_core_pattern` and generates a core dump based on its settings. Therefore, if the original configuration specified a particular location for writing the core dump file, this will continue even after OneAgent is installed.
3. The core dump is analyzed to check if Dynatrace could have been the root cause of the crash.

   * If OneAgent determines that Dynatrace could have been at fault:

     + A support alert is generated. This is reported to our DevOps team.
     + The core dump is zipped and retained in addition to all involved libraries. This is needed for later offline analysis.
   * If OneAgent determines that Dynatrace is not at fault:

     + A crash is reported via the Dynatrace web UI to the user.
     + If it has any impact on the customer's application, a problem is opened and an appropriate event is generated for the involved processes as described above.

## Cleanup

The log and support alert directories are cleaned up automatically.

* For support alerts, we process the `core dump`, then zip it and keep it in order to be sent to cluster.
* For crashes (non-instrumented processes or instrumented ones where we decide Dynatrace is not at fault), we process and then delete the copy of the `core dump`.

## Related topics

* [View crash reports for mobile applications](/docs/observe/digital-experience/mobile-applications/analyze-and-use/crash-reports-mobile "Check the latest crash reports for your mobile applications.")
* [View crash reports for custom applications](/docs/observe/digital-experience/custom-applications/analyze-and-use/crash-reports-custom "Check the latest crash reports for your custom applications.")
* [New: User session analysis](/docs/observe/digital-experience/session-segmentation/new-user-sessions "Learn about user session segmentation and filtering attributes.")

---

## observe/application-observability/profiling-and-optimization/memory-dump-analysis.md

---
title: Analyze memory dumps
source: https://www.dynatrace.com/docs/observe/application-observability/profiling-and-optimization/memory-dump-analysis
scraped: 2026-02-20T21:25:28.784573
---

# Analyze memory dumps

# Analyze memory dumps

* How-to guide
* 5-min read
* Updated on Jan 19, 2026

Dynatrace can store and analyze memory dumps for Java, .NET, and Node.js applications.

Memory dumps are stored by OneAgent locally for a limited time on the disk of the monitored application-server machine.

If an ActiveGate is configured, then OneAgent automatically uploads the memory dumps to the ActiveGate, which acts as a long-term storage center for memory dumps. This approach ensures that memory dumps are available only to users who have access to the network location of your ActiveGate. This precaution provides an additional security layer to ensure that no personal data leaves your data center unless you configure it that way.

![Memory dump page](https://dt-cdn.net/images/memory-dumps-1181-d3e7b9b87e.png)

## Before you begin

* To trigger memory dumps, you need the [**View sensitive request data**](/docs/manage/identity-access-management/permission-management/role-based-permissions#environment "Role-based permissions") user permission.
* To store memory dumps, your application server must have adequate space.
* To access persisted memory dumps via Dynatrace web UI, [configure an ActiveGate to store memory dumps in a centralized location](/docs/observe/application-observability/profiling-and-optimization/memory-dump-analysis/configure-an-activegate-for-memory-dump-storage "Learn how to enable storage of memory dumps on an ActiveGate."). To learn more about memory dump retention time, see [Data retention periods](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods#memory-dumps "Check retention times for various data types.").

## Trigger memory dumps

To trigger a memory dump

1. Navigate to the **Memory dumps** page:

   * On the page of the entity that you want to analyze, select **More** (**â¦**) > **Memory dump details**.
   * Go to ![Profiling & Optimization](https://dt-cdn.net/hub/logos/profiling-optimization.png "Profiling & Optimization") **Profiling & Optimization** > **Memory dumps**.
2. Select the process you want to analyze and select **Trigger new dump** to generate a new memory dump.  
   It takes a few minutes to generate a memory dump. The time required varies widely based on application type. Java applications that have multiple GBs of heap memory may take several minutes; smaller dumps are available almost immediately.

   Java

   Dynatrace uses the [JVM Tool Interface (JVM TI)ï»¿](https://docs.oracle.com/javase/8/docs/platform/jvmti/jvmti.html) to generate memory dumps. For this reason, your JVM may stall during memory-dump generation. Please restart your Java-based application following trigger of a memory dump.
3. After a few minutes, refresh the page. The newly created dump now appears in the list.

## Download and view memory dumps

To download memory dumps

1. Navigate to the **Memory dumps** page:

   * On the page of the entity that you want to analyze, select **More** (**â¦**) > **Memory dump details**.
   * Go to ![Profiling & Optimization](https://dt-cdn.net/hub/logos/profiling-optimization.png "Profiling & Optimization") **Profiling & Optimization** > **Memory dumps**.
2. Expand your memory dump record.
3. From the **Download link** list, select the ActiveGate from where you want to download the memory dump, and select **Download**.

   If you can't download the memory dump via UI, download the file manually at local path indicated in the web UI. Note that memory dumps that are stored by OneAgent locally are available for a limited time; when OneAgent periodically empties the directory, the file size could be 0 bytes.

In the case of Java applications, the download provides the memory dump in [hprofï»¿](https://dt-url.net/kh03s1r) format, which can be analyzed using a number of tools, including [Eclipse Memory analyzerï»¿](https://dt-url.net/uq23syk) and [VisualVMï»¿](https://dt-url.net/mz43sws). The IBM JVM doesn't support hprof, but its own format called IBM Portable Heap Dump (PHD). This can also be analyzed by the Eclipse Memory analyzer.

Node.js memory dumps can be opened in Google Chrome's integrated memory heap snapshot analysis tool.

.NET memory dumps can be opened in [PerfViewï»¿](https://dt-url.net/fb03syb) or Visual Studio.

## Limitations

* .NET memory dumps are not supported in Alpine Linux based containers.
* Memory dump uploads are not supported for both [Kubernetes Applicationâonly monitoring](/docs/ingest-from/setup-on-k8s/deployment/application-observability "Deploy Dynatrace Operator in application monitoring mode to Kubernetes") and [Kubernetes Cloud Native Full Stack monitoring](/docs/ingest-from/setup-on-k8s/deployment/full-stack-observability "Deploy Dynatrace Operator in cloud-native full-stack mode to Kubernetes").

  This is because OneAgent runs in a container with a readâonly filesystem (OneAgent binary directory `/opt/dynatrace/oneagent-paas` is mounted as readâonly), so Dynatrace cannot write the memory dump files it needs. At the same time, the `DATA_STORAGE` installer parameter used to override the dump directory is [not supported in containerâbased deployments](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). Therefore, it's not possible to change the dump location to a writable path. As a result, memory dump collection is not possible in Kubernetes environments monitored with Applicationâonly monitoring or Cloud Native Full Stack.

## FAQ

If I enable memory dump analysis on multiple ActiveGates, which ActiveGate will perform the memory dump?

ActiveGates have an automatically assigned priority. If more than one ActiveGate has the same priority, an endpoint is selected randomly.

What happens if a file transfer to an ActiveGate fails?

OneAgent attempts to send the dump list to all available endpoints until it finds one that works. This process is retried until it's successful or until the dumps are deleted by aging tasks (for example, if there are too many or if they are too old).

What happens if ActiveGate runs out of space for memory dumps?

ActiveGate first deletes outdated dumps. If there are no outdated dumps, ActiveGate deletes the oldest dumps first.

Can I configure where OneAgent stores memory dumps?

Yes. OneAgent stores memory dumps locally and ensures that dumps do not leave your local network. You can [customize the location of the memory dumps](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux#data-storage "Learn how to use the Linux installer with command line parameters.").

The end user can't access any of ActiveGate endpoints. Can I still provide access to the memory dump file?

Yes. Because from time to time an ActiveGate endpoint might not be accessible to the end user, ActiveGates can have multiple IP addresses, and so multiple endpoints. If all of the existing endpoints are not accessible to the end user at the same time, you can still provide access to the memory dump file.

* You can enable remote access to the ActiveGate by changing the public endpoints.  
  To learn how to configure a new endpoint, see:

  + [Enable the memory dump module](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#mem_dump_mod "Learn which ActiveGate properties you can configure based on your needs and requirements.")
  + [Configure ActiveGate for memory dump storage](/docs/observe/application-observability/profiling-and-optimization/memory-dump-analysis/configure-an-activegate-for-memory-dump-storage "Learn how to enable storage of memory dumps on an ActiveGate.")
* If remote access to the ActiveGate is not possible, you can download the memory dump file manually from the ActiveGate host.

  + To access the ActiveGate host, use a protocol that allows you to transfer files (such as sFTP or SSH).
  + To download the memory dump file, you need to [learn the location of the file](/docs/observe/application-observability/profiling-and-optimization/memory-dump-analysis/configure-an-activegate-for-memory-dump-storage#specify-dedicated-dump-directory "Learn how to enable storage of memory dumps on an ActiveGate.").
  + To be able to identify the memory dump, unzip its file via a protocol that includes a `summary.json` (such as sFTP or SSH).

## Related topics

* [Dynatrace ActiveGate](/docs/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.")
* [Role-based permissions](/docs/manage/identity-access-management/permission-management/role-based-permissions "Role-based permissions")

---

## observe/application-observability/profiling-and-optimization.md

---
title: Profiling and optimization
source: https://www.dynatrace.com/docs/observe/application-observability/profiling-and-optimization
scraped: 2026-02-18T21:23:33.275057
---

# Profiling and optimization

# Profiling and optimization

* Overview
* 1-min read
* Published Sep 25, 2018

Apart from automated problem detection, Dynatrace offers you a set of analysis tools that you can use to manually detect problems.

* **CPU profiling** highlights the biggest CPU consumers in your environment and allows you to drill down to the method level of a CPU problem.
* **Memory dump analysis** and **Process crashes** enable you to detect application crashes on Windows and Linux and analyze the core dumps of these crashes.

To access profiling and optimization options

1. Go to ![Profiling & Optimization](https://dt-cdn.net/hub/logos/profiling-optimization.png "Profiling & Optimization") **Profiling & Optimization**.
2. Select the analysis option you want to investigate among **CPU profiling**, **Memory dumps**, and **Process crashes**.

[### Memory dumps

Trigger and analyze Java, .NET, and Node.js memory dumps.](/docs/observe/application-observability/profiling-and-optimization/memory-dump-analysis "Learn how Dynatrace enables you to trigger, download and analyze memory dumps for Java and Node.js.")[### CPU profiling

Understand and analyze the CPU usage of your processes down to the code level.](/docs/observe/application-observability/profiling-and-optimization/cpu-profiling "Learn how you can use Dynatrace to perform enhanced code analysis.")[### Process crashes

Track all application crashes and enable analysis.](/docs/observe/application-observability/profiling-and-optimization/crash-analysis "Learn how Dynatrace can help you gain insight into process crashes.")

---

## observe/application-observability/services/calculated-service-metric.md

---
title: Calculated metrics for services
source: https://www.dynatrace.com/docs/observe/application-observability/services/calculated-service-metric
scraped: 2026-02-19T21:32:57.236405
---

# Calculated metrics for services

# Calculated metrics for services

* Latest Dynatrace
* How-to guide
* 5-min read
* Published Mar 30, 2021

Dynatrace automatically captures important metrics for services with no configuration required. You might need additional business or technical metrics that are specific to your application. These metrics can be calculated and derived based on a wide variety of available data within the captured distributed trace. You can also split these metrics by multiple dimensions, for example, a requests attribute or an HTTP method.

[OpenPipeline metric extraction](/docs/platform/openpipeline/use-cases/tutorial-system-events "Learn how to extract a metric to track system events with OpenPipeline.") now replaces calculated service metrics as the method to create additional service business or technical metrics. To read more about metric extraction, see [Extract metrics from spans and distributed traces](/docs/platform/openpipeline/use-cases/tutorial-extract-metrics-from-spans "Extract metrics directly from your spans and distributed traces via OpenPipeline.").
If you're an existing customer, you can still use them until we deprecate them. If you're a new customer, you won't be able to create calculated service metrics anymore.

## Why start using OpenPipeline instead of classic calculated service metrics?

* More flexible metric creation from spansâwith OpenPipeline, metrics are no longer limited to support at most 100 dimension values (âtop Xâ).

  + You can store full dimension cardinality
  + You can combine dimensions freely
  + Powerful ingestion, processing, and transformation capabilities are available via a unified solution (that works the same for other configuration scopes, such as logs and events).
* Better scale and performanceâplatform-scale ingest and stream processing built to go beyond petabytes; no more 500 calculated service metrics limit per tenant.
* Security, cost management, and data governanceâfilter and mask sensitive or unnecessary fields; assign cost center usage to specific metrics; route data to specific Grail buckets with controlled retention durations.

Limits

* Only new data is written to calculated metrics; retrospective data is not included.
* You can have up to 500 enabled calculated metrics per environment and up to 100 enabled calculated metrics per service.
* Classic calculated metrics support at most 100 dimension values. This is referred to as the "top X" rule, as you can select fewer depending on your configuration. However you choose the top 100 dimension values, the remaining dimensions are aggregated into a single timeseries and the dimension value is accessible through a special `remainder` dimension. The [remainder](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#remainder "Configure the metric selector for the Metric v2 API.") filter condition allowing you to filter on this `remainder` dimension.

* Grail calculated service metrics with cardinality higher than 2000 within any 5-minute window in the past 2 weeks or since the last metric change are automatically disabled in Grail. Enabling such metrics on Grail is not allowed. If the metric is already enabled on Grail, you are informed of the metric rejection via the [**Metric & Dimensions Usage + Rejections**](/docs/dynatrace-api/environment-api/metric-v2/best-practices#identify-high-cardinality-situations "Best practices for metrics.") ready-made dashboard. To enable a Classic metric on Grail and keep collecting incoming data on Grail, make sure cardinality stays below the limit.

## Create a calculated service metric

### Steps

1. Go to **Settings** > **Server-side service monitoring** > **Calculated service metrics** > **Create new metric**.
2. Enter the name for the metric.
   The name and the `calc:service.` prefix are added automatically to the metric key. Note that once a metric is [enabled in Grail](#grail) the prefix is automatically changed to `service.`
3. Choose the metric source from the **Metric source** list.

   * If the source is a request attribute, select the required unit.
   * Optional To exclude the data contribution of [muted requests](/docs/observe/application-observability/services/service-detection/service-detection-v1/service-monitoring-mute "Mute the monitoring of certain service requests so that you can focus on the performance of requests that affect your customers."), turn on **Ignore muted requests**.
4. Optional Select the management zone. The new metric will be restricted to data from this zone.
5. Provide conditions to define which requests are included in the calculation.

   If you provide several conditions, **all conditions must be fulfilled** to use the metric.

   1. Select **Add condition**.
   2. Select the attribute to be checked.
   3. Select the operator of the condition.
   4. If needed, specify the reference value.

      * Classic metric Preview shows the list of services to be included to the custom metric and the estimation of [DDU consumption](/docs/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.").

        Preview only considers management zone and conditions based on service attributes. These attributes are marked with `[Service property]` in the attribute list.

      * Grail metric While the DDUs estimation is only valid for the Classic metric, for the Grail metric expect enhanced precision and more comprehensive insights, as in Grail, the metrics' full dimension cardinality is stored (not just the Top X values). This may result in a greater number of data points compared to the classic metric, allowing for a more detailed analysis of your data.
6. Optional Add dimension to your new metric.

   1. Turn on **Split by dimension**.
   2. Choose the placeholders to define the dimension.

      * Select an available placeholder from **Dimension value pattern**.
      * Create a [custom placeholder](#placeholder).
   3. Enter a dimension name.
   4. Classic metric Define the top *X* value limit.

      The top *X* value limit applies to the Classic metric only, not to the Grail metric.

      1. In the **Number of top values** field, specify the amount of top *X* values to be calculated for the metric.
      2. From the **Value sorting** and **Value aggregation** lists, select the sorting and aggregation of the top *X* values.
7. Review the metric source and dimension names. They will be used in the UI and API. Once a metric is created, you can't change them.
8. Select **Save metric**.

## Create a custom placeholder

When a placeholder is not available, you can create a custom placeholder. All custom placeholders must be used in the dimension value pattern, alternatevely you can delete unused custom placeholders.

Prior knowledge

### Extraction method

You have two methods to extract the value for a placeholder:

* Delimiter-based. In this case, Dynatrace extracts the value by checking the value of the source against a reference value and specified delimiter kind and position.
* Regex-based. In this case, Dynatrace uses regular expression extraction. To learn how Dynatrace uses regular expressions, see [Regular expressions in Dynatrace](/docs/manage/tags-and-metadata/reference/regular-expressions-in-dynatrace "Learn how to use regular expressions in the context of Dynatrace.").

### Extraction method for request attributes

Placeholders that are based on request attributes provide three options for value extraction:

* **First**: The first occurrence of the attribute is used to extract the value.
* **Last**: The last occurrence of the attribute is used to extract the value.
* **Count**: The value equals the number of attribute occurrences.

### Steps

To create a custom placeholder

1. While creating or editing a calculated service metric, select **Add custom placeholder**.
2. Enter a name for your placeholder. The name will be used in the **Dimension value pattern** field.
3. Select the source for the dimension.
4. Choose the [extraction method](#prior).

   If the source is a request attribute,

   1. Optional Select **Use from downstream services** checkbox to use child calls as the value source.
   2. Optional Restrict the child calls to a particular management zone or service tag.
5. Select **Add**.
6. Required Use the newly created placeholder in the dimension value pattern.

## Enable a metric in Grail

Prerequisites

* Make sure each dimension cardinality is less than 2000 within any 5-minute window in the past 2 weeks or since the last metric change.
* Review the dimension for [unsupported placeholders](/docs/analyze-explore-automate/metrics/built-in-metrics-on-grail#unsupported-placeholders "Get to know the equivalents of the classic built-in metrics supported on Grail.") on Grail.

### Steps

To enable a metric in Grail, turn on **Enable on Grail**.

### Conclusion

The prefix is automatically modified from `calc:service.` to `service.`. The metric name and previosuly existing dimension are maintained. Supported placeholders are converted to additional dimensions and new dimensions are added for metrics derived by OneAgent.

For a complete list of available dimensions see [Built-in Metrics on Grail - Calculated service metrics](/docs/analyze-explore-automate/metrics/built-in-metrics-on-grail#calc-service "Get to know the equivalents of the classic built-in metrics supported on Grail.").

## Related topics



* [Service metrics API](/docs/dynatrace-api/configuration-api/calculated-metrics/service-metrics "Manage calculated service metrics via the Dynatrace configuration API.")
* [Multidimensional analysis](/docs/observe/application-observability/multidimensional-analysis "Configure a multidimensional analysis view and save it as a calculated metric.")

---

## observe/application-observability/services/customize-api-definitions.md

---
title: Custom API definitions
source: https://www.dynatrace.com/docs/observe/application-observability/services/customize-api-definitions
scraped: 2026-02-20T21:18:02.576896
---

# Custom API definitions

# Custom API definitions

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Nov 22, 2018

For some languages, like Node.js and Go, Dynatrace provides detection based on modules and packages. It uses a basic set of predefined APIs for Java and .NET. However, for others, Dynatrace allows you to create custom API definitions for the various frameworks in your environment. Custom API definitions are used to further segment the API breakdown and make it easier to quickly see which frameworks contain hotspots.

For example, by using a custom-created API definition called `easyTravel`, Dynatrace is able to identify all easyTravel-related method calls as part of the easyTravel-specific code.

To add a user-defined API detection rule:

1. Go to **Settings** > **Server-side service monitoring** > **API detection rules**.
2. Select **Create API detection rule**.
3. Type the name of the API.  
   The API name in this example is **easyTravel**.
4. Select **Add new condition**.
   The pattern to be used for identifying the API in this example is `com.dynatrace.easytravel`.
5. Select **Confirm** to save the new API detection rule.

![Add API detection rule](https://dt-cdn.net/images/add-api-detection-rule-1316-08acb766e6.png)

The user-defined **easyTravel** API is now included in the code-level analysis.

## Related topics

* [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.")

---

## observe/application-observability/services/enhanced-endpoints-sdv1.md

---
title: Leverage enhanced endpoints for SDv1
source: https://www.dynatrace.com/docs/observe/application-observability/services/enhanced-endpoints-sdv1
scraped: 2026-02-20T21:29:14.292522
---

# Leverage enhanced endpoints for SDv1

# Leverage enhanced endpoints for SDv1

* Latest Dynatrace
* How-to guide
* 7-min read
* Published Jan 19, 2026

With the **Enhanced endpoints for Service Detection v1 (SDv1)** feature, you can get full endpoint visibility for SDv1 services. When this feature is turned on, all endpoints are shown in [![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**](/docs/observe/application-observability/services/services-app "Maintain centralized control over service health, performance, and resources with the Services app.") without requiring you to configure [key requests](/docs/observe/application-observability/services/services-concepts#key-requests "Understand application observability, services, and distributed tracing concepts."). This is consistent with the behavior already in place for [SDv2](/docs/observe/application-observability/services/service-detection/service-detection-v2 "Find out how to detect, name, and split services from OpenTelemetry and OneAgent spans.") services.

The **Enhanced endpoints for SDv1** feature is turned on by default for the environments created in Dynatrace version 1.330+. For existing environments, the feature is available in Dynatrace version 1.333+.

No endpoints are created for [external services](/docs/discover-dynatrace/get-started/glossary#glossary-externalservice "Get acquainted with Dynatrace terminology.") and for the following SDv1 service types: [Background activity services](/docs/observe/application-observability/services/service-detection/service-detection-v1/service-types#background-activity-services "Understand the different types of services that can be detected and monitored in your environment."), [Queue listener services](/docs/observe/application-observability/services/service-detection/service-detection-v1/service-types#queue-listener-services "Understand the different types of services that can be detected and monitored in your environment."), and Key value store.

## Benefits

* **Complete endpoint visibility in ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services****: Gain a complete list of endpoints for SDv1 services in ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**.

  If you don't enable the **Enhanced endpoints for SDv1** feature, the **Endpoints** section in ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** either remains empty or only shows key requests.
* **Improved service insights**: The list of endpoints enhances visibility into the service's behavior, enabling quick identification and resolution of issues.
* **Dedicated metrics for endpoints**: Detected endpoints feature [dedicated metrics](#metrics), which you can add to [dashboards](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") and analyze for long-term endpoint history.

## Endpoint metrics

When the **Enhanced endpoints for SDv1** feature is turned on, Dynatrace starts collecting metrics for all detected endpoints of an SDv1 service in Grail.

The following metrics are collected for each endpoint:

* Failure rate
* Response time
* Throughput

These endpoint metrics are available not only in ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** but also in other Dynatrace apps, such as [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") or [![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.").

## Enable enhanced endpoints for SDv1

You can activate the **Enhanced endpoints for SDv1** feature for the entire environment or for a specific host group, Kubernetes namespace, and cluster.

Environment

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **Services**.
2. Under **Service detection v1**, select **Enhanced endpoints for SDv1**.
3. Turn on **Enable enhanced endpoints for SDv1**.

Host group

1. Go to ![Deployment Status](https://dt-cdn.net/images/deploy-status-512-c91e319ae5.png "Deployment Status") **Deployment Status** > **OneAgents**.
2. On the **OneAgent deployment** page, turn off **Show new OneAgent deployments**.
3. In the **Filter by** field, enter **Host group**, and then select the host group you want to configure from the dropdown list.

   The host list is now filtered by the selected host group. Each listed host has a **Host group:** `<group name>` link, where `<group name>` is the name of the host group that you want to configure.

   The **Host group** property is not displayed when the selected host doesn't belong to any host group.
4. Select the host group name in any row.

   As you have filtered by host group, all displayed hosts go to the same host group.

5. Close the overlay with the host group settings.
6. Go to **Process and contextualize** > **Services** > **Enhanced endpoints for SDv1**.
7. Turn on **Enable enhanced endpoints for SDv1**.

Kubernetes namespace or cluster

1. Go to ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**.
2. Select the required namespace or cluster.
3. In the upper-right corner of the namespace or cluster details pane, select  (**Actions menu**) > **Service detection settings**.
4. Go to **Process and contextualize** > **Services** > **Enhanced endpoints for SDv1**.
5. Turn on **Enable enhanced endpoints for SDv1**.

Endpoint names are changed

Enabling the **Enhanced endpoints for SDv1** feature changes some request names and their associated endpoint names. For this reason, your existing API metric queries, dashboards, and configured alerts for the changed endpoints might be impacted, so you should reconfigure them. See [Changes to endpoint names](#changes-to-endpoint-names) for the details.

## View service endpoints

Service endpoints as well as the [related metrics](#metrics) are displayed in ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**, in the **Endpoints** section.

1. Go to ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** > **Explorer**.
2. Find and select the service for which you want to explore the endpoints.
3. On the **Overview** tab, scroll down to the **Endpoints** section.

From there, you can view the service endpoints, check the related endpoint metrics, view traces for each endpoint, and more. Select  (**Actions menu**) for the endpoint to view the available options.

![Services app showing the Endpoints section with four different endpoints and their metrics](https://dt-cdn.net/images/service-app-endpoints-section-3840-6f62930eb6.png)

## Changes to endpoint names



Enabling the **Enhanced endpoints for SDv1** feature changes some request names and their associated endpoint names. Check the flowchart and textual description below for the details.

Pre-existing key requests and request naming rules remain in effect

For all service types, the already existing [key requests](/docs/observe/application-observability/services-classic/monitor-key-requests "Discover how to closely monitor requests that are critical to your business.") and [request naming rules](/docs/observe/application-observability/services/service-detection/service-detection-v1/set-up-request-naming "Adjust request naming and define the operations your services offer.") continue to apply.

If you have set up key requests, the associated endpoints have the same names as their key requests. If you have configured request naming rules, they are also applied to the related endpoint names.

![Diagram - Changes to endpoint names](https://dt-cdn.net/images/enhanced-endpoints-sdv1-changes-to-endpoint-names-6993-563d8740fc.png)

When the **Enhanced endpoints for SDv1** feature is on, some endpoint names for [web request services](/docs/observe/application-observability/services/service-detection/service-detection-v1/service-types#web-request-service "Understand the different types of services that can be detected and monitored in your environment.") and other service types are changed. This depends on whether there's an associated [request naming rule](/docs/observe/application-observability/services/service-detection/service-detection-v1/set-up-request-naming "Adjust request naming and define the operations your services offer.") and whether [volatile placeholder attributes](#volatile-placeholder-attributes) are used in these rules.

Endpoint names for web request services

Endpoint names for all other service types

**No request naming rule**

The following built-in rules are used for the endpoint names:[1](#fn-1-1-def)

1. `{http.request.method} {http.route}`
2. `{http.request.method} /*`

No change. The original request name is kept as the endpoint name.

**Request naming rule has no volatile placeholder attributes**

The placeholders are replaced with the corresponding values, and the template is fully applied.[2](#fn-1-2-def)

The placeholders are replaced with the corresponding values, and the template is fully applied.[2](#fn-1-2-def)

**Request naming rule contains volatile placeholder attributes**

The placeholder is not replaced, and the placeholder name is used in the endpoint name as is.[3](#fn-1-3-def)

The placeholder is not replaced, and the placeholder name is used in the endpoint name as is.[3](#fn-1-3-def)

1

For example, if the spans have no `{http.route}`, the endpoint name is `GET /*`.

2

For example, the `{HTTP-Method} - {Request:IsKeyRequest} - user authentication endpoint` template results in the `GET - yes - user authentication endpoint` endpoint name. Note that both `{HTTP-Method}` and `{Request:IsKeyRequest}` are replaced with their corresponding values (that is, `GET` and `yes`), as these are non-volatile placeholder attributes.

3

For example, the `{HTTP-Method} - {URL} - user authentication endpoint` template results in the `GET - {URL} - user authentication endpoint` endpoint name. Note that `{HTTP-Method}` (non-volatile placeholder attribute) is replaced with `GET` , while `{URL}` (volatile placeholder attribute) is not replaced and is used as is.

You can modify endpoint names by creating [custom naming rules](/docs/observe/application-observability/services/service-detection/service-detection-v1/set-up-request-naming#create-request-naming-rule "Adjust request naming and define the operations your services offer.").

### Volatile placeholder attributes

The volatile placeholder attributes are as follows:

* `{OneAgentAttribute:}` except `http.route`
* `{Relative-URL}`
* `{URL:Path}`
* `{URL:Query}`
* `{URL}`
* Customer-defined patterns based on one of the above-stated patterns

### Required actions

As some request names and their associated endpoint names change after you enable the **Enhanced endpoints for SDv1** feature, your existing API metric queries, dashboards, and configured alerts for the changed endpoints might be impacted. For this reason, you should reconfigure the affected entities.

## Static resource requests

Static resource requests include `Image`, `Binary`, `CSS`, and `JavaScript`.

When the **Enhanced endpoints for SDv1** feature is turned on, all static resource requests are unmuted and grouped into a single **Static resources** endpoint that has the same [metrics](#metrics) as other regular endpoints.

However, you can mute your static resource requests.

Whether the **Static resources** endpoint is muted or not, you can always go to [![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**](/docs/observe/application-observability/distributed-tracing/distributed-tracing-app "Discover the functionalities of the new Distributed Tracing app.") to view and analyze spans like CSS, images, or binary.

### Mute static resource requests

To mute static resource requests, follow the steps described in [Mute monitoring of service requests](/docs/observe/application-observability/services/service-detection/service-detection-v1/service-monitoring-mute "Mute the monitoring of certain service requests so that you can focus on the performance of requests that affect your customers.").

After you mute your static resource requests, the **Static resources** endpoint is not displayed in the endpoint list in ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**, and these requests don't count toward the overall service metrics.

### Manage resource request detection

You can add or edit filename extensions that count towards the **Static resources** endpoint. For details, see [Configure resource request detection](/docs/observe/application-observability/services/service-detection/service-detection-v1/set-up-request-naming#resource-request-detection "Adjust request naming and define the operations your services offer.").

Your existing configuration for resource request detection is still applicable, so if you have already added additional filename extensions, the corresponding requests should also become a part of the **Static resources** endpoint.

---

## observe/application-observability/services/failure-analysis.md

---
title: Failure Analysis
source: https://www.dynatrace.com/docs/observe/application-observability/services/failure-analysis
scraped: 2026-02-20T21:07:46.044501
---

# Failure Analysis

# Failure Analysis

* Latest Dynatrace
* Tutorial
* 4-min read
* Updated on Oct 23, 2025

Modern distributed systems generate complex failure patterns that require fast, reliable analysis.

**Failure Analysis** in Dynatrace addresses this need by offering a focused experience for investigating service failures, helping you uncover patterns and contributing factors across your environments.

## What is Failure Analysis?

In Dynatrace, a failure refers to any request or transaction that does not complete successfully. Failures may result from HTTP errors, unhandled exceptions, or custom-defined conditions that indicate unexpected behavior.

**Failure Analysis** helps you detect, investigate, and resolve service failures faster and more effectively. It modernizes the Dynatrace experience by introducing a user-focused interface and new capabilities that support both reactive and proactive troubleshooting.

You can access **Failure Analysis** directly from the problems-specific drill-down options when a failure rate increase is detected, or explore it manually from the **Failures** tab in ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**.

This feature is designed for SREs, developers, and DevOps teams who need fast, actionable insights into service health and failure patterns.

**Failure Analysis** provides:

* A clear view of why service requests are failing
* Advanced filtering by service, endpoint, failure type, and timeframe
* In-depth analysis and visual comparison of failure trends across time periods, including precise insights into how failure counts evolve and what causes them
* Contextual logs linked to failed requests
* Insights into related outgoing calls and database failures

## Key capabilities

### Core capabilities

* **Advanced filtering**  
  Use Dynatrace filters to narrow down failures by attributes such as service, endpoint, failure type, and more.
  Timeframe filters allow users to isolate failures within specific periods or compare across time ranges.
* **Comparison mode**  
  Visually compare failure rates across different timeframes to identify trends, assess the impact of changes, or validate fixes.
  Interactive annotationsâlabels displayed above the graph, provide additional context for specific timeframes when hovered over, highlighting key failure events for deeper insights.
* **Contextual log integration**  
  View logs directly associated with failed service calls (via trace/span IDs).
  This provides essential context for understanding the root cause.
* **Outgoing call analysis**  
  Investigate failures in downstream dependencies such as HTTP requests, gRPC calls, or third-party APIs.
  Dynatrace detects failed states based on HTTP/gRPC response codes, span status, and the presence of exceptions within traces.
* **Database failure insights**  
  Analyze failed database interactions, including query-level visibility for supported databases.
  This helps identify backend issues contributing to service instability.
* **Exploratory and contextual access**  
  Access the Failure Analysis page with or without predefined context. When accessed via the problems-specific drill-down options, filters are pre-applied.
  Users can also explore failures manually by adjusting filters.

### Integration with Dynatrace

* Embedded in the ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** application as a new **Failures** tab
* Integrated into the **Dynatrace problems-specific drill-down options** when failure rate increases are detected as [root causes](/docs/dynatrace-intelligence/davis-problems-app#streamline-problem-resolution-with-problems-specific-drill-down-options "Use the Problems app to quickly get to the root cause of incidents in your environment.")
* Replaces the legacy **Failure Analysis** page for DPS customers

## Access and navigation

The new **Failure Analysis** feature is available as a dedicated **Failures** tab in Dynatrace **Services**. It is designed to support both contextual and exploratory workflows.

### How to access

* **Contextual Access via problems-specific drill-down options**  
  When a failure rate increase is identified as the root cause of a problem, you are directed to the **Failure Analysis** page with pre-applied filters based on the affected service and endpoint.
* **Exploratory Access**  
  You can also navigate to the **Failures** tab manually and adjust filters to explore failures across services, endpoints, and timeframes.

### Prerequisites

* DPS license
* SaaS environment with the new Dynatrace platform enabled

## Get started

To get started troubleshooting a service failure

1. Go to ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** and select the **Failures** tab.
2. Apply filters for service, endpoint, and timeframe.
3. Use **compare to** (for example, select `Same timeframe last week`) to detect anomalies.
4. Open the log view to examine logs emitted during failed traces.
5. Check outgoing calls and database queries.

## Limitations

While the new **Failure Analysis** experience introduces significant improvements in usability and functionality, you may occasionally experience slower load times when accessing **Failure Analysis** in environments with high trace volumes or complex service architectures. Dynatrace is actively monitoring performance and continuously optimizing the experience.

## Related resources and next steps

To deepen your understanding of failure detection and troubleshooting in Dynatrace, explore the following resources:

* [Configure service failure detection](/docs/observe/application-observability/services/service-detection/service-detection-v1/configure-service-failure-detection "Discover which service error types Dynatrace automatically detects and learn how to adjust failure detection settings to meet your specific requirements.")
* [Root cause analysis concepts](/docs/dynatrace-intelligence/root-cause-analysis/concepts "Get acquainted with root cause analysis concepts.")
* [Triage and investigate incidents in the Problems app](/docs/dynatrace-intelligence/davis-problems-app "Use the Problems app to quickly get to the root cause of incidents in your environment.")

### Join the conversation

Weâd love to hear your feedback and questions about the new **Failure Analysis** experience.  
[Visit the Feedback Channel in the Dynatrace Communityï»¿](https://community.dynatrace.com/t5/Feedback-channel/Feedback-channel-for-the-new-Failure-Analysis-feature/td-p/282050)

---

## observe/application-observability/services/monitor-service-message-processing.md

---
title: Monitor service message processing
source: https://www.dynatrace.com/docs/observe/application-observability/services/monitor-service-message-processing
scraped: 2026-02-20T21:18:38.903751
---

# Monitor service message processing

# Monitor service message processing

* Latest Dynatrace
* Tutorial
* 3-min read
* Published Jan 15, 2026

Modern distributed systems rely heavily on asynchronous communication through message queues and streaming platforms. Understanding message flow, throughput, and processing failures is critical for maintaining system reliability.

Monitoring service message processing in Dynatrace addresses this need by providing comprehensive visibility into message-based transactions across your microservices architecture, helping you track throughput, identify bottlenecks, and resolve processing issues.

## What is service message processing monitoring?

In Dynatrace, message processing refers to any transaction involving message queues or streaming platforms like Kafka, RabbitMQ, ActiveMQ, and AWS SQS. This includes messages published to topics, received from queues, and processed by consuming services.

Service message processing monitoring helps you understand how messages flow through your distributed systems, detect processing bottlenecks, and identify failures in asynchronous communication patterns.

You can access service message processing directly from ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**, or through custom dashboards and alerts configured to monitor messaging metrics.

This feature is designed for SREs, developers, and platform engineers who need visibility into asynchronous communication patterns and message processing health.

Service message processing monitoring provides:

* Real-time visibility into message publish, receive, and process rates
* Identification of processing bottlenecks and queue lag
* Tracking of message flow between producing and consuming services
* Error rate monitoring for failed message processing
* Infrastructure dependency mapping for messaging platforms
* Integration with distributed traces for root cause analysis

## Metrics reference

Dynatrace provides four core metrics for monitoring message processing:

| Metric | Description | Unit |
| --- | --- | --- |
| `dt.service.messaging.publish.count` | Messages sent to queues/topics | count |
| `dt.service.messaging.receive.count` | Messages received from queues/topics | count |
| `dt.service.messaging.process.count` | Messages successfully processed | count |
| `dt.service.messaging.process.failure_count` | Messages that failed processing | count |

### Key dimensions

| Dimension | Description | Example values |
| --- | --- | --- |
| `messaging.destination.name` | Queue or topic name | `authorQueue`, `orderEvents` |
| `dt.entity.service` | Service identifier | `spring-kafka-producer` |
| `messaging.system` | Messaging platform | `kafka`, `rabbitmq`, `aws_sqs` |
| `aws.account.id` | AWS account identifier | `123456789012` |
| `aws.region` | AWS region | `us-east-1` |
| `k8s.cluster.name` | Kubernetes cluster name | `prod-cluster` |
| `k8s.namespace.name` | Kubernetes namespace | `payment-services` |

## Get started

To begin monitoring service message processing

1. Go to ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**, select the **Explorer** tab, and select **Message processing**.
2. Select the service and queue/topic you want to monitor.
3. View **Publish rate**, **Receive rate**, and **Process rate** in the time series charts.
4. Identify lag by comparing receive rates to process rates.
5. Drill down to distributed traces to investigate specific message failures.

## Query examples

Monitor service messaging throughput:

```
timeseries throughput = sum(dt.service.messaging.process.count),



by: {dt.smartscape.service}



| lookup [smartscapeNodes "SERVICE" | fields name,id],



sourceField:dt.smartscape.service, lookupField:id



| fieldsAdd `Service` = lookup.name, dt.smartscape.service



| summarize throughput = sum(throughput[]),



by: { timeframe, interval, `Service`, dt.smartscape.service }
```

Calculate service messaging failure rate:

```
timeseries { throughput = sum(dt.service.messaging.process.count),



failure_count = sum(dt.service.messaging.process.failure_count) },



by: {dt.smartscape.service}, nonempty:true, union:true



| lookup [ smartscapeNodes "SERVICE" | fields name, id],



sourceField:dt.smartscape.service, lookupField:id



| fieldsAdd `Service` = lookup.name, dt.smartscape.service



| summarize failure_rate = sum((failure_count[] / throughput[]) * 100),



by: { timeframe, interval, `Service`, dt.smartscape.service }
```

---

## observe/application-observability/services/request-attributes/capture-request-attributes-based-on-method-arguments.md

---
title: Capture request attributes based on method arguments
source: https://www.dynatrace.com/docs/observe/application-observability/services/request-attributes/capture-request-attributes-based-on-method-arguments
scraped: 2026-02-19T21:18:22.141664
---

# Capture request attributes based on method arguments

# Capture request attributes based on method arguments

* Latest Dynatrace
* 6-min read
* Published May 11, 2018

Dynatrace allows you to create request attributes based on method arguments.

## Create request attributes

To create a request attribute based on a method argument

1. Go to **Settings** > **Server-side service monitoring** > **Request attributes**.
2. Select **Define a new request attribute**.
3. Provide a unique **Request attribute name**. You can rename an attribute at any point in the future.
4. Select **Add new data source**.
5. Optional Define the scope of the request attribute.
6. From the **Request attribute source** list, select **Java method parameter(s)**, **.NET method parameter(s)**, or **PHP method parameter(s)**.
7. Select the **Select method sources** button to open the class wizard. Here you can select the class of the method upon whose argument you want to set an attribute.
8. Select the process group that contains the classes or interfaces youâre interested in and select **Continue**.
9. Search for the class that includes the method youâre interested in. Begin typing the class name and select **Search** button. The list may take a few seconds to populate.
10. Select a class from the displayed list. If the list doesnât contain the class youâre looking for, refine the search string.

    ![Request attributes .NET](https://dt-cdn.net/images/request-attributes-dotnet-1-1326-b3cbc95405.png)
11. Finally, select one or more methods that you want to capture parameters from and then select **Finish**.
12. The methods you selected are listed in the method argument capture rule (see below). For each method, from the list box under **Capture**, select the argument or return value of the method you want to capture.

    ![Request attributes .NET](https://dt-cdn.net/images/request-attributes-dotnet-2-1325-6354f7c2ab.png)
13. You can always extend the list or remove methods later. Once saved, restart the processes that this rule applies to.

### Notes

* In addition to arguments and return values of any method, you can also capture the number of occurrences. You should only use a single method rule when capturing occurrences. Dynatrace will count the number of calls of this method within a single request.
* You can [capture non-primitive and non-string objects](#numerical). This can, however, result in increased performance overhead. Some objects may inadvertently change their state based on the method called, so use this option with caution.
* Core Java classes (for example, `javax.` and `java.`) or .NET classes (for example, `System.`) produce the warning **Not instrumentable**. These classes can't be used, because instrumenting them would mean instrumenting a substantial part of your environment.

## What's next?

Once your services begin calling the respective methods, you should see the request attribute appear on the distributed traces page.

![Request attributes .NET](https://dt-cdn.net/images/request-attributes-net-1801-7073b46dd3.png)

The code-level tree view also contains these methods. This view tells you what the value was on each specific methodâin case the method is called multiple times with different values.

![Request attributes .NET - code level](https://dt-cdn.net/images/request-attributes-net-code-level-1804-839768da1d.png)

## Post processing

In most cases, a captured value will contain what it is youâre looking for. However, you may not want an entire value, or even every value. With post processing you can manipulate the captured value.

Expand the **Optionally restrict or process the captured parameter(s) further** option to see the processing steps. The steps are executed in the presented orderâeach step is applied to the result of the previous step.

You don't have to apply all the steps. Each step becomes active once you provide a value for it or select the option box.

![Post processing options for defining request attribute rule](https://dt-cdn.net/images/post5steps-1353-6e753964a1.png)

Step 1 enables you to extract something from the resulting string based on delimited characters.

Step 2 can split the captured value into several values based on a delimited character.

Step 3 removes whitespaces.

Step 4 enables you to filter out captured values that don't fit the provided criterion.

Step 5 enables you to extract something from the resulting string based a [regular expression](/docs/manage/tags-and-metadata/reference/regular-expressions-in-dynatrace "Learn how to use regular expressions in the context of Dynatrace.").

## Numerical values and aggregations

You might want to capture an argument of a method and the method is called multiple times. Sometimes youâre only interested in a specific value. In other cases, you may only want to count the executions or average the captured values. Within other values, the argument in question may be a complex object and youâre really only interested in one aspect of the object.

To tackle such situations, you can use the **Data type** and the **Aggregation on request** options when you define or configure a request attribute.

### Aggregations

Aggregation is applied not only within a single data source (for example, a method rule) but also across multiple data sources. The order is defined by:

* Order of the data source rules
* Order of the method rules within a method data source
* Order of the method executions in your application (when a method is executed multiple times)

#### Text attributes

For text attributes, you can choose between these options:

* First occurrence
* Last occurrence
* Set of distinct values

The **Set of distinct** values option enables you to use all distinct values found in a request for filtering. For example, if a request captures a request attribute called `Product` and two values are captured for this attribute, `Book` and `Video`. You can filter by either of these values to find the request in question.

#### Numeric attributes

For numeric values, you can use the following aggregations:

* Minimum of captured values
* Maximum of captured values
* Average of captured values
* Sum of captured values
* Count occurrences
* Count distinct

If you choose one of these options, the data type changes to integer automatically. These settings are useful when youâre counting something.

## Deep object access

A value that youâre interested in may not be available as a simple argument, but rather as part of a complex argument object or even a member variable of a class youâre looking at. Such values can still be accessed. You can access not only argument values and return values, but also an object itself. Whenever an item to be captured (be it an argument or an object) is a complex object, you have the ability to define a method (chain) that enables deep access into the object. The example below uses the method `getBookingCode`. You can even execute a chain, for example, `getBookingCode().getCustomerCode()`.

![Request attributes](https://dt-cdn.net/images/deep-object-access-1157-bad06a137b.png)

The deep object access feature introduces new code into your application that must be executed. As such, it may change the state of your application or introduce performance impact. Use this feature with caution.

### Limitations

The following limitations apply to deep object access:

* You can access only one field at a time. If you're accessing a field, it must be in the beginning of the chain.
* Method parameters are not allowed.
* You must use valid Java, .NET, or PHP notation.

---

## observe/application-observability/services/request-attributes/capture-request-attributes-based-on-web-request-data.md

---
title: Capture request attributes based on web request data
source: https://www.dynatrace.com/docs/observe/application-observability/services/request-attributes/capture-request-attributes-based-on-web-request-data
scraped: 2026-02-19T21:18:18.066616
---

# Capture request attributes based on web request data

# Capture request attributes based on web request data

* Latest Dynatrace
* 4-min read
* Updated on Jul 06, 2023

To define a request attribute based on web request data:

1. Go to **Settings** > **Server-side service monitoring** > **Request attributes**.
2. Select the **Create new request attribute** button.
3. Provide a unique **Request attribute name**. You can rename an attribute at any point in the future.
4. Indicate **Data type**.  
   You can't change **Data type** following request attribute setup.
5. If multiple values exist in a single request, specify what should be stored in the request attribute for every request, and choose how to normalize the text.
6. Check whether this rule should access unmasked data, and whether the request attribute contains [confidential data](/docs/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#restrict-view-access "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.").

   This will potentially access personal data.
7. Add a data source. You can define one or more rules to specify how your attribute should be fetched.  
   Each rule needs a source. Dynatrace needs to know where it can collect the request attribute. You can define the rule by first selecting where the rule should be applied (based on process group, host group, service technology, or group tag), and then indicating where the actual parameter can be found (**Request attribute source**).
8. Once you have added all the data sources, select **Save** to save your request attribute rule.

## Request attribute rules

Have a look at the example request attribute rule below. Note that the request attribute `destination` can obtain its value from two different sources, either an `HTTP Post` parameter (`iceform:destination`) or an `HTTP GET` parameter (`destination`). Rules are executed in order. If a request meets the criteria for both rules, its value will be taken from the first rule.

Each rule needs a source. In the example below, the request attribute source is a web request `HTTP GET` parameter (`destination`).

![Example of request attributes rule definition](https://dt-cdn.net/images/get-2018-10-30-14-26-29-1373-3d3ff74f1c.png)

This `GET` parameter will be captured on all monitored processes that support code-level insight and it will be reported on all requests that are monitored by Dynatrace.

While this is convenient, itâs not always whatâs needed. This is why you can restrict rules to a subset of process groups and services. To do this, select process group and service names from the four drop-lists above to reduce the number of process groups and services that the rule applies to.

You may not be interested in capturing every value. In other cases, a value may contain a prefix that you want to check against. To do this, specify that the designated parameter should only be used if its value matches a certain value. You can also opt to not use an entire value, but instead extract a portion of a value. The example below is set up to only consider `iceform:destination` `HTTP POST` parameters that begin with the string `Journey :`. This approach will extract everything that follows the string `Journey:` and store it in the request attribute.

![Example of request attributes POST rule definition](https://dt-cdn.net/images/post-2018-10-30-14-15-35-1379-6f82cbbf7c.png)

Requests can have as many attributes as you want.

## Request attribute sources for web requests

Request attribute data sources for web requests include

* Technology-independent sources, such as:

  + HTTP POST parameters
  + [Client IP addresses](/docs/observe/digital-experience/rum-concepts/detection-of-ip-addresses-locations-and-user-agents#ip-addresses "Dynatrace detects IP addresses and geolocations like a city, region, and country as well as browsers, devices, and operating systems.")  
    The value of the first matching header is reported.
  + HTTP request and response headers
  + Web request URL or one of its constituents, like the path or a query parameter

  In the last two cases, you can also choose the side of the web request on which to capture and store the attribute.

  OneAgent is always required at capture.

  Option

  Request type

  Capture side

  Store side

  **Capture on the client side of a web request service and store on the calling service**

  Full-service call[1](#fn-1-1-def)

  Client

  Server

  **Capture on server side of a web request service**

  Full-service call

  Server

  Server

  **Capture on the client side of a web request service**

  External service call[2](#fn-1-2-def)

  Client

  Client

  **Capture from both client and server side and store where found**

  Full-service call

  Server

  Server

  **Capture from both client and server side and store where found**

  External service call

  Client

  Client

  1

  Full-service call: request that is fully monitored by Dynatrace.

  2

  External service call: request that goes to external resources.
* Technology-specific sources.

  + The application can hold a complex object in an attribute, while OneAgent converts it to a string upon capture (for example, in [Java servlet session attributeï»¿](https://dt-url.net/q503soq) and [ASP.NET session-state variableï»¿](https://dt-url.net/qf23stx)). This might have side effects, so be careful with what you capture.
  + ASP.NET When multiple parameters have the same name, you will see only the first captured value.
  + Java servlet Java servlet request attributes and session attributes are captured only after the servlet or filter is entered.

## Post processing

In most cases, a captured value will contain what it is youâre looking for. However, you may not want an entire value, or even every value. With post processing you can manipulate the captured value.

Expand the **Optionally restrict or process the captured parameter(s) further** option to see the processing steps. The steps are executed in the presented orderâeach step is applied to the result of the previous step.

You don't have to apply all the steps. Each step becomes active once you provide a value for it or select the option box.

![Post processing options for defining request attribute rule](https://dt-cdn.net/images/post5steps-1353-6e753964a1.png)

Step 1 enables you to extract something from the resulting string based on delimited characters.

Step 2 can split the captured value into several values based on a delimited character.

Step 3 removes whitespaces.

Step 4 enables you to filter out captured values that don't fit the provided criterion.

Step 5 enables you to extract something from the resulting string based a [regular expression](/docs/manage/tags-and-metadata/reference/regular-expressions-in-dynatrace "Learn how to use regular expressions in the context of Dynatrace.").

---

## observe/application-observability/services/request-attributes/filter-monitoring-data-via-request-attributes.md

---
title: Filter monitoring data via request attributes
source: https://www.dynatrace.com/docs/observe/application-observability/services/request-attributes/filter-monitoring-data-via-request-attributes
scraped: 2026-02-19T21:18:25.524108
---

# Filter monitoring data via request attributes

# Filter monitoring data via request attributes

* Latest Dynatrace
* 2-min read
* Updated on Jul 28, 2023

Once youâve defined your request attributes, they're listed in the related service analysis and indicated as labels for the respective requests.

![Request attributes](https://dt-cdn.net/images/request-attribute-filter-1446-3c51f44605.png)

* To filter the entire page view down to only those requests that carry a specific attribute, select a request attribute from the **Request attribute** list.
* To check the values of a request attribute, expand its row.

  By selecting a value, you can filter the page down to requests that carry the specified value for the selected request attribute.
* The applied request attribute or request attribute value filter persists in further analysis options such as [**Service flow**](/docs/observe/application-observability/services-classic/service-flow "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment.") and [**Multidimensional analysis**](/docs/observe/application-observability/multidimensional-analysis "Configure a multidimensional analysis view and save it as a calculated metric.").

  Example

  To filter **BookingService** requests by request attribute value, we select **Request attributes** > **Booking** and choose the value **checkCreditCard**. The results reflect the current filter settings and show the same metrics as the request table.

  ![Request attributes' list](https://dt-cdn.net/images/request-attribute-filter-1-1439-2762e66325.png)

  + **Median response time** is the median response time of all requests that contain the request attribute.
  + **Total time consumption** is the sum of response times of all requests in the selected timeframe that have the selected request attribute.
  + You can also view the corresponding throughput metrics.

  We select **Create analysis view** to visualize a multidimensional analysis custom view filtered by the selected request attribute value.

  ![Multidimensional analysis filtered by request attribute value](https://dt-cdn.net/images/request-attribute-filter-2-1423-91835f8d9f.png)
* To filter [custom charts](/docs/analyze-explore-automate/dashboards-classic/dashboards-upgrade "Upgrade your Dynatrace custom charts to Data Explorer visualizations now.") by request attribute or request attribute value, create a [custom metric](/docs/observe/application-observability/services/calculated-service-metric "Learn how to create a calculated metric based on web requests.") based on these conditions.

  Without a custom metric, if a request attribute is detected for a service, all data points for the service metric are displayed in the custom charts.

## Related topics

* [Capture request attributes based on web request data](/docs/observe/application-observability/services/request-attributes/capture-request-attributes-based-on-web-request-data "Create request attributes based on web request data.")
* [Capture request attributes based on method arguments](/docs/observe/application-observability/services/request-attributes/capture-request-attributes-based-on-method-arguments "Learn how to create request attributes based on Java, .NET, or PHP method arguments and how to use them on the serviceâs overview page. Also find out how you can aggregate the captured values of request attributes as well as how you can access objects, in case the value to be captured is a complex object.")

---

## observe/application-observability/services/request-attributes.md

---
title: Request attributes
source: https://www.dynatrace.com/docs/observe/application-observability/services/request-attributes
scraped: 2026-02-20T21:08:19.279683
---

# Request attributes

# Request attributes

* Latest Dynatrace
* 3-min read
* Updated on Aug 02, 2024

Dynatrace tracks all requests, from end to end, and automatically monitors the services that underlie each transaction. The performance and attributes of each request can be analyzed in detail. You're not limited to just certain predefined attributes. You can also configure custom *request attributes* that you can use to improve filtering and analysis of web requests.

Request attributes are essentially key/value pairs that are associated with a particular service request. For example, if you have a travel website that tracks the destinations of each of your customersâ bookings, you can set up a destination attribute for each service request. The specific value of the destination attribute of each request is populated for you automatically on all calls that include a destination attribute (see the `destination` attribute example below). A single request might have multiple request attributes.

![Request attributes](https://dt-cdn.net/images/request-attributes-1575-7055953a5c.png)

Multiple requests within a single distributed trace might have the same attribute but with different values.

## Define request attributes

You can capture request attributes based on:

* [Web request data](/docs/observe/application-observability/services/request-attributes/capture-request-attributes-based-on-web-request-data "Create request attributes based on web request data.")
* [Java, .NET, and PHP method arguments](/docs/observe/application-observability/services/request-attributes/capture-request-attributes-based-on-method-arguments "Learn how to create request attributes based on Java, .NET, or PHP method arguments and how to use them on the serviceâs overview page. Also find out how you can aggregate the captured values of request attributes as well as how you can access objects, in case the value to be captured is a complex object.")
* Any data captured with the [OneAgent SDK](/docs/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk "The Dynatrace OneAgent SDK enables you to instrument your application manually to extend end-to-end visibility for frameworks and technologies for which there is no code module yet available.")

## Confidential request attributes

As request attributes may include confidential values, Dynatrace makes it possible to mark a request attribute as confidential. To do this

1. Go to **Settings** > **Server-side service monitoring** > **Request attributes**.
2. Select **Edit** for the relevant request attribute.
3. Select **Request attribute contains confidential data**.

With this setting enabled, Dynatrace users who don't have access to confidential data see only an obscured view of masked data. For example, while they can see all performance metrics related to the execution of a certain SQL statement, all sensitive values in the statement are represented with asterisks (`*****`), and so are hidden from unauthorized access.

## How to make use of request attributes

Here are some examples of how you can use request attributes:

* [Filter your monitoring data](/docs/observe/application-observability/services/request-attributes/filter-monitoring-data-via-request-attributes "Use request attributes to filter your monitoring data and narrow down service analysis scope.")
* [Define web-request naming rules](/docs/observe/application-observability/services/service-detection/service-detection-v1/set-up-request-naming "Adjust request naming and define the operations your services offer.")
* [Set up detection of business-logic related errors](/docs/observe/application-observability/services/service-detection/service-detection-v1/configure-service-failure-detection#detection-of-business-logic-related-errors-using-request-attributes "Discover which service error types Dynatrace automatically detects and learn how to adjust failure detection settings to meet your specific requirements.")
* [Enrich distributed traces analysis by adding metadata to distributed traces](/docs/observe/application-observability/distributed-traces/use-cases/segment-request "Enhance your distributed system performance by segmenting requests with slow response time via Service flow and analyzing their distributed traces.")
* [Create calculated metrics](/docs/dynatrace-api/configuration-api/calculated-metrics "Learn what the Dynatrace calculated metrics config API offers.")
* [Create custom queries, segmentation, and aggregation of session data with User Session Query Language](/docs/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Learn how you can access and query user session data based on keywords, syntax, functions, and more.")

## Limits

### Number of request attributes

The maximum number of request attributes per request is 100.

### Number of request attribute values

The maximum number of values of a request attribute per request is 10.

### Number of request attribute values in number calculations

For each request, the maximum number of request attribute values that are evaluated within a number calculation (such as `avg`, `sum`, `count`, or `max`) is 1,000.

### Number of captured request attributes per distributed trace

The maximum number of request attributes that can be captured by OneAgent for a distributed trace is 1,000. Request attributes that are captured multiple times within a distributed trace and request attributes that are captured on single requests contribute to this limit. Once the limit is reached, any subsequent request attribute is not captured.

## Related topics

* [Request attributes API](/docs/dynatrace-api/configuration-api/service-api/request-attributes-api "Learn what the Dynatrace request attribute config API offers.")
* [Service flow filtering](/docs/observe/application-observability/services-classic/service-flow/service-flow-filtering "Understand how service filtering works and how it can be exploited.")
* [Set up request naming](/docs/observe/application-observability/services/service-detection/service-detection-v1/set-up-request-naming "Adjust request naming and define the operations your services offer.")

---

## observe/application-observability/services/response-time-analysis.md

---
title: Response time analysis
source: https://www.dynatrace.com/docs/observe/application-observability/services/response-time-analysis
scraped: 2026-02-20T21:07:48.917304
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

**Capability**

**Description**

Root cause identification

Understand the main contributors to slow service requests, such as CPU heavy service execution, waiting for outbound calls, or heavy database queries.

Advanced filtering

Use filters to narrow down failures by attributes such as service, endpoint, and more. Timeframe filters allow users to isolate failures within specific periods or compare across time ranges.

Response time trend chart

Understand how the response time evolves over time or as a histogram distribution chart.

Timeframe comparison

Compare the response time between two timeframes to identify trends, assess the impact of changes, or validate fixes.

Outbound calls

Investigate the impact of downstream dependencies such as downstream services, or third-party APIs to the response time.

Infrastructure perspective

Gain insights into key metrics for related infrastructure components, helping to identify potential bottlenecks.

Exploratory and contextual access

Access response time analysis with or without predefined context. When accessed via the problems-specific drill-down options or from a specific service, filters are pre-applied. Users can also explore failures manually by adjusting filters.

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

---

## observe/application-observability/services/service-detection/service-detection-v1/configure-service-failure-detection.md

---
title: Configure service failure detection
source: https://www.dynatrace.com/docs/observe/application-observability/services/service-detection/service-detection-v1/configure-service-failure-detection
scraped: 2026-02-19T21:15:24.053378
---

# Configure service failure detection

# Configure service failure detection

* How-to guide
* 9-min read
* Updated on Oct 01, 2025

Dynatrace failure detection automatically detects the vast majority of error conditions in your environment, including the underlying [root causes](/docs/dynatrace-intelligence/root-cause-analysis/concepts "Get acquainted with root cause analysis concepts."). With this approach, Dynatrace is able to provide you with answers when problems occur or when your application performance drops.

When Dynatrace detects a service error, it doesn't necessarily mean that you want to label a request as failed. If the default service-error detection settings don't meet your needs, you can configure failure detection settings as explained in this page.

By default, Dynatrace detects:

* Programming exceptions (Java, .NET, Node.js, and PHP) as the reason for failed requests when exceptions result in the abort of service calls.
* Error pages provided by many web containers for the handled exceptions.
* HTTP `500`â`599` error codes for web requests interpreted as errors on the server side.
* HTTP `400`â`599` error codes for web requests interpreted as errors on the client side.

Why does client side include 5xx codes?

The detected error codes depend on the perspective:

* From the server perspective, only a `5xx` code is an error, because a `4xx` code means a client error.
* From the client perspective, a `5xx` still means there's an error even though it's not the client's fault.

## Failure detection settings

You can configure failure detection globally or on individual services.

* When you configure failure detection settings on the service level, they override the global setup.
* Failure detection rules are evaluated from top to bottom; the first matching rule applies. If multiple failure detection rules have the same conditions, only the first matching rule applies.

The following failure detection rules don't apply to the service types:

* Span service
* Unified service

  To learn more about unified service failure detection, see [Unified services](/docs/observe/application-observability/services/service-detection/service-detection-v1/service-types/unified-service "Define services on observability signals ingested via Trace ingest APIs.").

Global settings

Service-level settings

To configure service failure detection globally

1. Go to **Settings** and expand **Server-side service monitoring**.
2. To add a new failure detection rule, go to **Failure detection rules** > **Add failure detection rule**.

   Each rule can have multiple conditions, based on defined failure detection parameters. You can use existing failure detection parameters for failure detection rules or create new ones.

   * To add a new failure detection parameter, go to **Failure detection parameters** > **Add failure detection parameters**. To learn more, see [Parameters](#parameters), [HTTP parameters](#http), and [General parameters](#general) below.
   * Use the **Enabled** switch to turn a rule on or off.
   * Dynatrace recalculates global rule matching every 10 minutes.

To configure service failure for a specific service

1. Go to ![Services Classic](https://dt-cdn.net/images/services-classic-f58502bd22.svg "Services Classic") **Services Classic** and select the service for which you need to adapt failure detection.
2. Select **More** (**â¦**) > **Settings**.
3. Select **Failure detection** and then **HTTP parameters** or **General parameters**, depending on the parameters you want to configure.
4. Turn on **Override global failure detection settings** (see **1** in the graphic).  
   If a failure detection rule applies, from here you can access both the rule (see **3** in the graphic) and the parameters (see **2** in the graphic).

## Parameters

Parameters for failure detection include HTTP-specific parameters and general parameters (related to exceptions, custom errors, and span failure detection). While you can always access general parameters both globally and on the service level, you might not see HTTP failure detection parameters on the service level, as they are visible only on specific services, such as web requests and web services. You can set them up after enabling **Override global failure detection settings** (**1** in the graphic) and even if no global rule matches the service.

![Failure detection - HTTP parameters](https://dt-cdn.net/images/failure-detection-http-parameters-1791-26675df666.png)

### HTTP parameters

* **HTTP response codes**

  `HTTP-4XX` response codes usually indicate client-side errors, not server-side errors. You can specify which missing HTTP response codes should be treated as server-side errors and which as client-side errors. You can define multiple ranges separated by commas (for example, `400-402, 405-417`).

  Depending on your application, missing response codes might indicate a "fire and forget" call that didnât return a response at all, a timeout, or an error situation. Dynatrace considers missing response codes as special cases and doesnât report them as a default behavior. You can change this by enabling **Treat missing HTTP response code as server side errors** or **Treat missing HTTP response code as client side errors**.
* **HTTP 404 - broken link configuration**

  When a web server canât find a certain page, it returns an `HTTP 404` response code. Usually, this indicates a problem on the calling side. When the calling side belongs to the same website, this would be considered a broken link.

  Because most customers don't consider broken links to be a problem on their server, Dynatrace classifies broken links as client-side problems and not automatically as failures on the server side. However, you can enable the **Consider 404 HTTP response codes as failures** switch to classify broken links as server-side failures. After doing so, you can associate additional hosts at other domains to your application by adding the name of the host under **Add other application domain**.

### General parameters



* **Success forcing exceptions**

  These exceptions indicate that a service call should not be considered as failed, for example, because the client aborted the operation. Although they are technical errors, in principle they don't count as failed requests because they aren't caused by faults with the service. If a request encounters such an exception in the root call of the service, Dynatrace considers the request to be successful, regardless of the HTTP error code or any other information. You can select **Add exception** to add exception classes that indicate such situations.
* **Ignored exceptions**

  There are situations in which your code (or third-party code that you don't control) returns exceptions that indicate a certain response and not an error. For example, the Thrift client for Cassandra returns a `NotFoundException` response when a row isnât found. This isnât an error, but simply a response code.

  You can select **Add exception** to configure Dynatrace to not consider such exceptions as failed request indicators. Additionally, you can define a string that must be found within an exception message for the exception to be ignored. If the HTTP response code for the same call shows an error, Dynatrace considers the request as failed. To consider a request successful regardless of the HTTP error code or any other information, see **Success forcing exceptions**.
* **Custom handled exceptions**

  There are situations in which application code handles exceptions gracefully in a manner that isnât automatically detected by Dynatrace. When this happens, Dynatrace doesnât detect failed requests or alert you to errors.

  You can remedy such situations by specifying an exception class that should result in a failed request. Optionally, you can define a string that must be found in the exception message. If this string isn't found, the exception won't lead to a failed request.  
  If Dynatrace finds the defined exception (and the optionally-defined exception message) on a request, Dynatrace marks the request as failed.  
  Note that this doesn't work if you exclude the exception class from capture in [Deep process monitoring settings](/docs/observe/infrastructure-observability/process-groups/configuration/pg-monitoring#deep-monitoring "Ways to customize process-group monitoring").
* **Ignore all exceptions**

  When **Ignore all exceptions** is enabled, Dynatrace ignores **Success forcing exceptions**, **Ignored Exceptions** and **Custom handled exceptions** for the services to which the parameters applyâthe specific service if the switch is enabled on the service-level or the services that match the global rule.
  Because exceptions are still tracked, they appear in distributed traces, but you don't receive alerts for them and requests aren't labeled as failed.
* **Custom errors via request attributes**

  Custom error situations might be triggered by exceptions, but some are detectable only via a return value or other means. To support such cases, you can define a [request attribute](/docs/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.") that captures the required data. You can then define a custom error rule based on the request attribute that checks the value of the request attribute to determine if the request has failed or not.

  Example: Use request attributes to detect business logic-related errors

  Requests might fail for reasons related to business logic. These situations often arenât detectable via exceptions or HTTP response codes. Nevertheless, they are indicative of problems and might be even more important than situations detected via exceptions and response codes. For example, you might have a business function in your Java code that indicates an error via a return value or you might have your own error-handling functionality that, when called, indicates a functional business error.

  Such situations can be captured via [request attributes](/docs/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views."), which you can use as indicators for error situations.

  To create a custom error rule

  1. Go to ![Services Classic](https://dt-cdn.net/images/services-classic-f58502bd22.svg "Services Classic") **Services Classic**.
  2. Select the service for which you need to adapt failure detection.
  3. Select **More** (**â¦**) > **Settings**.
  4. Select **Failure detection** > **General parameters**
  5. Under **Custom error rules**, select **Add custom error rule**.
  6. Select a request attribute from the displayed list.
  7. Define a condition for the rule, such as **contains** and a value.

  In the example below, a value of `-1` in the `Amount of recommendations` attribute indicates an error. Following this rule, if Dynatrace detects such an error, it will mark the respective service request as failed and explain that the rule match is the reason for the failure.

  ![Custom error rule](https://dt-cdn.net/images/custom-error-rule-2908-978f284947.png)
* **Span failure**

  Span failure detection is specific to OpenTelemetry. Dynatrace by default detects span failures, but there are specific cases in which you might want to change these settings. To ignore span failure detection, turn on **Ignore span failure detection**.

## Schema info

On the service level, you can visualize the **Schema ID** by selecting **More** (**â¦**) > **Schema info** in the upper-right corner of the **HTTP parameters** or **General parameters** page.

## Related topics

* [Request attributes](/docs/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.")
* [Root cause analysis concepts](/docs/dynatrace-intelligence/root-cause-analysis/concepts "Get acquainted with root cause analysis concepts.")
* [Failure detection API](/docs/dynatrace-api/configuration-api/service-api/failure-detection "Learn what the Dynatrace failure detection config API offers.")

---

## observe/application-observability/services/service-detection/service-detection-v1/customize-service-detection.md

---
title: Service detection rules
source: https://www.dynatrace.com/docs/observe/application-observability/services/service-detection/service-detection-v1/customize-service-detection
scraped: 2026-02-20T21:16:43.851257
---

# Service detection rules

# Service detection rules

* How-to guide
* 15-min read
* Updated on Oct 21, 2025

When monitoring with OneAgent, your deployed applications and related microservices are automatically detected by Dynatrace, based on specific properties of your application deployment and configuration, such as the application identifier, part of the URL, or the server name.

Attributes used for detection are marked with an asterisk â± on the [service](/docs/observe/application-observability/services-classic/service-analysis-new "Learn about all the service monitoring details that Dynatrace can provide.") overview page, under **Properties and tags**.

In certain cases, the quality of data available to Dynatrace might be insufficient for high-precision service detection. To tailor out-of-the-box detection to your environment, you can create new rules or setup improvements.

## Manage rule-based service detection

You can use transformation rules, for example, to remedy the following use cases:

* If the web Application IDs contain the version or build date, you can define a rule that removes the build date/ID from the web application ID.
* When server names are not properly defined in the underlying deployment (for example, with Apache HTTP or Nginx in AWS environments), you can define a stable web server name and therefore a stable cluster service containing all instances.
* You can correct the misuse of the context root in the deployed application.

  A typical web server has a concept called the context root to separate services based on the URL. For some technologies, such as Node.js, the context root is not available or it's improperly defined. You can superimpose the context root, and create separate services for each of your applications, instead of a single service containing multiple applications.
* You can ignore the port for service detection. This is helpful when the port is used dynamically, for example, in Node.js applications.

Additionally, the rules can be exported and imported from one environment to another.

Detection rules are evaluated from top to bottom, and the first matching rule applies, so be sure to place your rule in the correct position on the list.

### Prerequisites

* Familiarize yourself with the notion of a [full and external (opaque) request](/docs/discover-dynatrace/get-started/glossary#request "Get acquainted with Dynatrace terminology.").
* API onlyRequired To be able to configure rule-based service detection via the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers."), you need an access token with **Read settings** (`settings.read`) and **Write settings** (`settings.write`) scopes. To learn how to obtain it, see [Create an access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.").

### Create a rule

When you define a new rule, depending on the configuration, the original services might get less traffic or no traffic at all. New monitoring data is then redirected according to the rule configuration, between the original and the newly detected services.

via web UI

via API

To define a new service detection rule via web UI

1. Go to **Settings**.
2. Expand **Service Detection** and select a request type (**Full web request rules** or **Full web service rules**, or **External web request rules** or **External web service rules**).
3. Select **Add item** and start configuring the parameters of the new rule.

   1. Type a **Rule name**.
   2. To change the service detection's behavior, enable at least one of the service identifier contributors, so that the rule's triggered.
   3. To target the rule application, in the **Conditions** section, configure restrictions related toâfor exampleâa management zone, specific conditions, or the port.
4. Select **Save changes**.

This procedure overwrites any existing configuration. If you want to modify an existing configuration, see the [**Modify a rule**](#api-update) section below.

To define a new service detection rule via API

1. Query the settings schema via the [GET a schema](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") callâit contains the information about parameters included in the settings object.

   The ID of schema depends on the request type, as summarized in the following table.

   Request type

   Schema ID

   Full web request

   [`builtin:service-detection.full-web-request`](/docs/dynatrace-api/environment-api/settings/schemas/builtin-service-detection-full-web-request "View builtin:service-detection.full-web-request settings schema table of your monitoring environment via the Dynatrace API.")

   Full web service

   [`builtin:service-detection.full-web-service`](/docs/dynatrace-api/environment-api/settings/schemas/builtin-service-detection-full-web-service "View builtin:service-detection.full-web-service settings schema table of your monitoring environment via the Dynatrace API.")

   External web request

   [`builtin:service-detection.external-web-request`](/docs/dynatrace-api/environment-api/settings/schemas/builtin-service-detection-external-web-request "View builtin:service-detection.external-web-request settings schema table of your monitoring environment via the Dynatrace API.")

   External web service

   [`builtin:service-detection.external-web-service`](/docs/dynatrace-api/environment-api/settings/schemas/builtin-service-detection-external-web-service "View builtin:service-detection.external-web-service settings schema table of your monitoring environment via the Dynatrace API.")
2. Create a JSON object for your settings.

   Example JSON for a full web request rule

   ```
   [



   {



   "schemaId":"builtin:service-detection.full-web-request",



   "scope":"environment",



   "value":{



   "enabled":true,



   "name":"Detect Application,Application-1 as the same",



   "description":"Example: merge services",



   "managementZones":["-8445121454707515572"],



   "idContributors":{



   "applicationId":{



   "enableIdContributor":true,



   "serviceIdContributor":{



   "contributionType":"TransformValue",



   "transformations": [



   {



   "transformationType":"REMOVE_NUMBERS",



   "minDigitCount":1,



   "includeHexNumbers":false



   }



   ]



   }



   },



   "contextRoot":{



   "enableIdContributor":false



   },



   "serverName":{



   "enableIdContributor":false



   }



   },



   "conditions": [



   {



   "attribute":"ApplicationId",



   "compareOperationType":"StringStartsWith",



   "textValues": ["application"],



   "ignoreCase":false



   }



   ]



   }



   }



   ]
   ```
3. Use the [POST an object](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") call to send your configuration.

### Modify a rule



When you modify a rule, some services might not be affected by it anymore. While historical data is available only for the previous service, all newly captured data is then associated with the new standalone service.

via web UI

via API

To edit an existing rule via the web UI

1. Go to **Settings**.
2. Expand **Service Detection** and select a request type (**Full web request rules** or **Full web service rules**, or **External web request rules** or **External web service rules**).
3. Expand ![Expand row](https://dt-cdn.net/images/expand-row-icon-9c4950fc2e.svg "Expand row") the row of the rule.
4. Edit the rule settings.
5. Select **Save changes**.

To update an existing rule via API

1. Query the settings schema via the [GET a schema](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") callâit contains the information about parameters included in the settings object.

   The ID of schema depends on the request type, as summarized in the following table.

   Request type

   Schema ID

   Full web request

   [`builtin:service-detection.full-web-request`](/docs/dynatrace-api/environment-api/settings/schemas/builtin-service-detection-full-web-request "View builtin:service-detection.full-web-request settings schema table of your monitoring environment via the Dynatrace API.")

   Full web service

   [`builtin:service-detection.full-web-service`](/docs/dynatrace-api/environment-api/settings/schemas/builtin-service-detection-full-web-service "View builtin:service-detection.full-web-service settings schema table of your monitoring environment via the Dynatrace API.")

   External web request

   [`builtin:service-detection.external-web-request`](/docs/dynatrace-api/environment-api/settings/schemas/builtin-service-detection-external-web-request "View builtin:service-detection.external-web-request settings schema table of your monitoring environment via the Dynatrace API.")

   External web service

   [`builtin:service-detection.external-web-service`](/docs/dynatrace-api/environment-api/settings/schemas/builtin-service-detection-external-web-service "View builtin:service-detection.external-web-service settings schema table of your monitoring environment via the Dynatrace API.")
2. Query the current configuration via the [GET objects](/docs/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API.") call.
3. Create a JSON object for your update. We recommend to use **updateToken** from previous objectâit ensures proper versioning of your settings.

   Example JSON for a full web request rule

   ```
   [



   {



   "updateToken":"vu9U3hXY3q0ATAAkOWFiNGI2ZDAtYWFhNC00M2IwLWEzZDYtNDQ2OTZkNzIyYzE5ACRmMTA1NTJlMC01M2Q5LTExZWQtODAwMS0wMTAwMDAwMDAwMDO-71TeFdjerQ",



   "value":{



   "enabled":true,



   "name":"Detect Application, Application-1 as the same",



   "description":"Example: merge services",



   "managementZones":["-8445121454707515572"],



   "idContributors":{



   "applicationId":{



   "enableIdContributor":true,



   "serviceIdContributor":{



   "contributionType":"TransformValue",



   "transformations":[



   {



   "transformationType":"REMOVE_NUMBERS",



   "minDigitCount":1,



   "includeHexNumbers":false



   }



   ]



   }



   },



   "contextRoot":{



   "enableIdContributor":false



   },



   "serverName":{



   "enableIdContributor":false



   }



   },



   "conditions":[



   {



   "attribute":"ApplicationId",



   "compareOperationType":"StringStartsWith",



   "textValues":["application"],



   ///Added condition to ignore case sensitivity for texts.



   "ignoreCase":true



   }



   ]



   }



   }



   ]
   ```
4. Use the [PUT an object](/docs/dynatrace-api/environment-api/settings/objects/put-object "Edit a settings object via the Dynatrace API.") call to send your configuration.

### Delete a rule

If you delete a rule, all individual services are split and once again treated as standalone services.

via web UI

via API

To delete a service detection rule

1. Go to **Settings**.
2. Expand **Service Detection** and select a request type (**Full web request rules** or **Full web service rules**, or **External web request rules** or **External web service rules**).
3. In the **Delete** column for the corresponding rule row, select **Delete row** ![Remove](https://dt-cdn.net/images/remove-icon-105c6a04c2.svg "Remove")

To delete a rule via API

1. Query the list of existing rules via the [GET objects](/docs/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API.") call. Specify the schema of your request type in the **schemaIds** query parameter.
   The ID of schema depends on the request type, as summarized in the following table.

   Request type

   Schema ID

   Full web request

   [`builtin:service-detection.full-web-request`](/docs/dynatrace-api/environment-api/settings/schemas/builtin-service-detection-full-web-request "View builtin:service-detection.full-web-request settings schema table of your monitoring environment via the Dynatrace API.")

   Full web service

   [`builtin:service-detection.full-web-service`](/docs/dynatrace-api/environment-api/settings/schemas/builtin-service-detection-full-web-service "View builtin:service-detection.full-web-service settings schema table of your monitoring environment via the Dynatrace API.")

   External web request

   [`builtin:service-detection.external-web-request`](/docs/dynatrace-api/environment-api/settings/schemas/builtin-service-detection-external-web-request "View builtin:service-detection.external-web-request settings schema table of your monitoring environment via the Dynatrace API.")

   External web service

   [`builtin:service-detection.external-web-service`](/docs/dynatrace-api/environment-api/settings/schemas/builtin-service-detection-external-web-service "View builtin:service-detection.external-web-service settings schema table of your monitoring environment via the Dynatrace API.")
2. Find the rule you want to delete, and copy its **objectId**.
3. Delete the rule via the [DELETE an object](/docs/dynatrace-api/environment-api/settings/objects/del-object "Delete a settings object via the Dynatrace API.") call. Use the object ID obtained in the previous step.

### Examples



#### Separate fully monitored web request services based on URL or superimposed context root

For some technologies monitored by Dynatrace, the context root is not supported. A single service per process group is detected by default. You can change service detection by imposing a context root on a fully monitored web request.

In this example, when the URL path of a full web request starts with specific wording (`blog/`), we want to detect a service, whose ID will be transformed to the first segment of the URL.

Rule set-up

via web UI

via API

1. Go to **Settings**.
2. Expand **Service Detection** and select **Full web request rules**.
3. In the full web request rules, select **Add item**.
4. Configure the parameters as follows

   1. Enter a **Rule name**.
   2. Optional Enter a **Description**.
   3. Go to **URL context root** and turn on **Transform this value before letting it contribute to the Service ID**.

      1. From the **Contribution type** list, select **Use transformed URL path**.
      2. In **Segments to copy from URL path**, enter the number of segments of the URL to be kept (`1`).
   4. Go to **Conditions** and select **Add item**.

      1. From the **Take the value of this attribute** list, select **URL path**.
      2. From the **Apply this operation** list, select **Starts with**.
      3. Go to **Values** and select **Add item**, then enter `blog/`.
5. Select **Save changes**.

```
[



{



"schemaId":"builtin:service-detection.full-web-request",



"scope":"environment",



"value":{



"enabled":true,



"name":"Dynatrace Blog",



"description":"Detect first segment of an URL path as service when it starts with blog/",



"managementZones":[],



"idContributors":{



"applicationId":{



"enableIdContributor":false



},



"contextRoot":{



"enableIdContributor":true,



"serviceIdContributor":{



"contributionType":"TransformURL",



"segmentCount":1,



"transformations":[]



}



},



"serverName":{



"enableIdContributor":false



}



},



"conditions":[



{



"attribute":"UrlPath",



"compareOperationType":"StringStartsWith",



"textValues":["blog/"],



"ignoreCase":false



}



]



}



}



]
```

#### Merge application data into a single service, based on the application ID value

When incoming data is volatile or not specific enough, you can use service detection rules to merge services, for example, Apache HTTP clusters in AWS without a proper virtual host or web application IDs containing the build date.

In this example, we want to merge in the same service all incoming data from applications whose ID starts with `application`.

Rule set-up

via web UI

via API

1. Go to **Settings**.
2. Expand **Service Detection** and select **Full web request rules**.
3. In the full web request rules, select **Add item**.
4. Configure the parameters as follows.

   1. Enter a **Rule name**.
   2. Optional Enter a **Description**.
   3. Select **Set a management zone** and choose the management zone for the list.
   4. Go to **Application identifier** and turn on **Transform this value before letting it contribute to the Service ID**.

      1. From the **Contribution type** list, select **Use transformed value**.
      2. Go to **Transformations** and select **Add item**.

         1. From the **Transformation type** list, select **remove numbers**.
         2. Enter a **min digit count** (`1`)
   5. Go to **Conditions** and select **Add item**.

      1. From the **Take the value of this attribute** list, select **Application identifier**.
      2. From the **Apply this operation** list, select **Starts with**.
      3. Go to **Values** and select **Add item**, then enter `application`.
5. Select **Save changes**.

See the following [example JSON](#eg_appId).

#### Separate services for âpublic network servicesâ based on URL

In this example, when the top-level domain of an external web request ends with a specific wording (`dynatrace.com`), we want to detect a service, whose ID will be transformed to the first segment of the URL.

Rule set-up

via web UI

via API

1. Go to **Settings**.
2. Expand **Service Detection** and select **External web request rules**.
3. In the external web request rules, select **Add item**.
4. Configure the parameters as follows.

   1. Enter a **Rule name**.
   2. Optional Enter a **Description**.
   3. Go to **URL context root** and turn on **Transform this value before letting it contribute to the Service ID**.

      1. From the **Contribution type** list, select **Use transformed URL path**.
      2. In **Segments to copy from URL path**, enter the number of segments of the URL to be kept (`1`).
   4. Go to **Public domain name** and turn off **Port**.
   5. Go to **Conditions** and select **Add item**.

      1. From the **Take the value of this attribute** list, select **Top level domain**.
      2. From the **Apply this operation** drowpdown list, select **Ends with**.
      3. Go to **Values** and select **Add item**, then enter `dynatrace.com`.
      4. To ignore case sensitivity, turn on **Ignore case**.
5. Select **Save changes**.

```
[



{



"schemaId":"builtin:service-detection.external-web-request",



"scope":"environment",



"value":{



"enabled":true,



"name":"Dynatrace.com - based on URL",



"description":"Blog example: Dynatrace.com based on URL",



"managementZones":[],



"idContributors":{



"applicationId":{



"enableIdContributor":false



},



"contextRoot":{



"enableIdContributor":true,



"serviceIdContributor":{



"contributionType":"TransformURL",



"segmentCount":1,



"transformations":[]



}



},



"publicDomainName":{



"enableIdContributor":false



},



"portForServiceId":false



},



"conditions":[



{



"attribute":"TopLevelDomain",



"compareOperationType":"StringEndsWith",



"textValues":["dynatrace.com"],



"ignoreCase":true



}



]



}



}



]
```

#### Separate services for âpublic network servicesâ based on subdomains

If different endpoints shouldnât be combined in the same service (for example, `support.dynatrace.com` and `blog.dynatrace.com`), you can instruct Dynatrace to detect multiple services from the same domain, based on the detected hostname instead of the request's domain name.

Rule set-up

via web UI

via API

1. Go to **Settings**.
2. Expand **Service Detection** and select **External web request rules**.
3. In the external web request rules, select **Add item**.
4. Configure the parameters as follows.

   1. Enter a **Rule name**.
   2. Optional Enter a **Description**.
   3. Go to **Public domain name** and turn on **Transform this value before letting it contribute to the Service ID**.

      1. From the **Contribution type** list, select **Use the original value**.
      2. Turn on **Copy from host name**.
      3. Turn off **Port**.
   4. Go to **Conditions** and select **Add item**.

      1. From the **Take the value of this attribute** list, select **Top level domain**.
      2. From the **Apply this operation** drowpdown list, select **Ends with**.
      3. Go to **Values** and select **Add item**, then enter `dynatrace.com`.
      4. To ignore case sensitivity, turn on **Ignore case**.
5. Select **Save changes**.

```
[



{



"schemaId":"builtin:service-detection.external-web-request",



"scope":"environment",



"value":{



"enabled":true,



"name":"Dynatrace.com - based on subdomains",



"description":"Blog example: Separate services for public network services based on subdomains ",



"managementZones":[],



"idContributors":{



"applicationId":{



"enableIdContributor":false



},



"contextRoot":{



"enableIdContributor":false



},



"publicDomainName":{



"enableIdContributor":true,



"serviceIdContributor":{



"contributionType":"OriginalValue",



"copyFromHostName":true



}



},



"portForServiceId":false



},



"conditions":[



{



"attribute":"TopLevelDomain",



"compareOperationType":"StringEndsWith",



"textValues":["dynatrace.com"],



"ignoreCase":true



}



]



}



}



]
```

## Improve service detection

### Web server naming issues

* In some cases, web servers don't have well-defined virtual hosts, server names, or sites. A web server might simply be named `localhost`. This can result in multiple similar services that contain multiple website instances. To remedy such issues, adjust [process-group detection settings](/docs/observe/infrastructure-observability/process-groups/configuration/pg-monitoring#rules "Ways to customize process-group monitoring").
* When there is no virtual host configured on an Apache HTTP server, the web server name defaults to the name of the physical host. In cloud environments, this leads to one virtual host for each physical host instance and thus one service instance. If the cloud environment starts and stops the hosts, these services will be temporary.

  To remedy such localhost scenarios, use an environment variable to define virtual host names: set `DT_LOCALTOVIRTUALHOSTNAME` for each web server process to any value. Dynatrace will pick up the names and use them in place of the existing localhost virtual host names. With this approach, you ensure that multiple physical hosts report the same virtual host and thus get one service with multiple instances, one instance per physical host.

### Define web application IDs

Some technologies don't provide unique application names. In such cases, you can define an environment variable called `DT_APPLICATIONID` to provide a unique name. This only impacts services of the respective process that don't already have application IDs. For Java applications, you can alternatively use the system property `dynatrace.application.id`.

### Rotating and anonymous ports



Dynatrace takes the listen port of each web request service into account when naming and detecting requests. In some cases, these ports are meaningless or random, changing with each restart. This is especially true if you're using a load balancer that dynamically assigns ports to application processes, as is the case in many Node.js scenarios.

To remedy this, set environment variable `DT_IGNOREDYNAMICPORT=true`. This removes the port from detection and replaces it with `*`.

## FAQ

If a service doesn't receive any new data after I create/edit/delete a rule, what happens to it?

When you create, edit, or delete a rule, data monitored after the change in service detection rules is aggregated and assigned to services, depending on the rule configuration. If a service stops receiving data, its historical data remains available (for example, for charting). You can still see the service and its traces in your environment.

## Related topics

* [Merged services](/docs/observe/application-observability/services/service-detection/service-detection-v1/service-types/merged-services "Consolidate multiple web-request services of the same process group into one service.")
* [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.")
* [Service detection API](/docs/dynatrace-api/configuration-api/service-api/detection-rules "Learn what the Dynatrace service detection rules config API offers.")
* [[Blog] New Dynatrace API enhances automatic service detection - with concrete examplesï»¿](https://www.dynatrace.com/news/blog/new-dynatrace-api-enhances-automatic-service-detection/#how-to-use-the-new-api)

---

## observe/application-observability/services/service-detection/service-detection-v1/customize-service-naming.md

---
title: Service naming rules
source: https://www.dynatrace.com/docs/observe/application-observability/services/service-detection/service-detection-v1/customize-service-naming
scraped: 2026-02-19T21:18:32.223054
---

# Service naming rules

# Service naming rules

* How-to guide
* 4-min read
* Published Oct 04, 2017

Dynatrace [automatically detects and names your applicationsâ server-side services](/docs/observe/application-observability/services/service-detection/service-detection-v1 "Find out how Dynatrace Service Detection v1 detects and names different types of services.") based on basic properties of your application deployment and configuration. Built-in rules define these names. These properties and the resulting service names should be intuitive to you because they reflect your service landscape. Still, you might want to customize these names. Custom service naming rules enable you to enhance automated service naming.

## Built-in rules

Built-in service naming rules define how the service naming works out of the box. Built-in rules are not configurable. You can still access them for documentation purposes. Go to **Settings** > **Server-side service monitoring** > **Service naming rules** and scroll to the **Built-in rules** section. Here you can expand every rule to see how is it configured.

## Custom rules

Custom service naming rules override built-in rules enabling you to create your own naming standards. To access custom rules, go to **Settings** > **Server-side service monitoring** > **Service naming rules**.

Custom rules are evaluated from top to bottom, and the first matching rule applies, so be sure to place your rule in the correct position on the list.

To define a custom service naming rule

1. Go to **Settings** > **Server-side service monitoring** > **Service naming rules**.
2. Select the **Add a new rule**.
3. Type a **Rule name**.
4. Define the **Service name format**, including any static text string to be included that describes the named service. You can use placeholders to make it easy to dynamically include specific service and process group properties in the automated service name.
5. Optional Consider restricting this naming rule to a specific process group, technology, or service type.  
   While this step is optional, it provides a quick means of reducing the number of services that a rule applies to. To reduce the list of applicable services even further, you can add **Conditions** to the new rule.

   If within the name format you reference a property that doesnât exist in a service that the rule applies to, the placeholder will be replaced with an empty string. You can ensure that the rule only applies to services where the property exists by adding an `exists` condition for the desired property.
6. Select **Save**.

## Service name format

Service name format enable you to build complex naming standards for the services in your environment. You can use placeholders to build a name based on service properties. Placeholders will be replaced with actual values in the service name. In case the provided value is missing, the placeholder will resolve to an empty string. Place your cursor in the **Service name format** input field to see the list of available placeholders.

You can use [regular expressions](/docs/manage/tags-and-metadata/reference/regular-expressions-in-dynatrace "Learn how to use regular expressions in the context of Dynatrace.") to extract portions of the service name, created by a built-in rule. Add the regex before the closing curly bracket `}` of the placeholder. For example, for `{ProcessGroup:DetectedName}` use `{ProcessGroup:DetectedName/REGEX}`.

## Related topics

* [Conditional naming API](/docs/dynatrace-api/configuration-api/conditional-naming "Learn what the Dynatrace configuration API for conditional naming offers.")

---

## observe/application-observability/services/service-detection/service-detection-v1/service-types/opaque-services.md

---
title: Opaque services
source: https://www.dynatrace.com/docs/observe/application-observability/services/service-detection/service-detection-v1/service-types/opaque-services
scraped: 2026-02-20T21:09:25.709011
---

# Opaque services

# Opaque services

* How-to guide
* 3-min read
* Published Oct 04, 2017

Opaque services are services that are detected on the calling side by Dynatrace for which code-level visibility isn't available. Dynatrace can detect requests to opaque services and identify which processes they are processed by, but Dynatrace can't monitor these services directly.

Code-level visibility isn't possible if:

* A service is of a technology type for which deep monitoring isn't supported.
* A service is of an unrecognized or unsupported technology.

## No deep monitoring support

Code-level visibility might not be available for some technologies, even though the technology is supported by Dynatrace.

Nevertheless, Dynatrace can detect all requests to such services that are sent by services with full visibility. Dynatrace calculates response times and failure rates and generates appropriate alerts.

Thanks to artificial intelligence, Dynatrace understands the impact that host and process performance problems can have on services. This is why Dynatrace correlates host and process issues with corresponding slow-downs in service requests. For example, if a service without code-level visibility crashes, Dynatrace will interpret the crash as the root cause of any increased failure rate in calls to this service.

## Unrecognized or unsupported technologies

When a service is of an unrecognized technology or a technology that is recognized but not currently supported by Dynatrace, the service is considered to be opaque.

Although deep monitoring isn't supported for such services, Dynatrace can still detect all requests to this service that are sent by fully visible services and, for example, calculate the relevant response times and failure rate.

Opaque services of unrecognized or unsupported technologies are included in Smartscape. This ensures a complete representation of your infrastructureâs topology, even when your environment includes opaque services.

The [OneAgent SDK](/docs/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk "The Dynatrace OneAgent SDK enables you to instrument your application manually to extend end-to-end visibility for frameworks and technologies for which there is no code module yet available.") enables you to instrument your application manually to extend end-to-end visibility for unrecognized or unsupported technologies.

## Other reasons services may be classified as opaque

There can be cases where a service is considered opaque even when the service is recognized and of a supported technology. This can occur for the multiple reasons, such as:

* A process is offline but a service still makes calls to it. These opaque services are used to visualize dependencies in the context of availability problems.
* A process never started processing a request (the calling service receives an error or timeout) and therefore Dynatrace can't track the request in the process.
* A process hasn't completely restarted following OneAgent installation. By the time the process restarts, it should no longer appear as opaque.
* The framework processing the request at the specific port is not currently supported by OneAgent. If this is important to you, please suggest a product idea for the specific framework and version in [Dynatrace Community product ideasï»¿](https://community.dynatrace.com/t5/Product-ideas/idb-p/DynatraceProductIdeas) (Community sign-in required).
* The framework is supported, but OneAgent has run into a technical problem. In such a case, please [submit a Support ticketï»¿](https://www.dynatrace.com/support/contact-support/). Describe the issue as best you can and include all details regarding your underlying framework, technologies, and versions.

---

## observe/application-observability/services/service-detection/service-detection-v1/service-types/unified-service.md

---
title: Unified services
source: https://www.dynatrace.com/docs/observe/application-observability/services/service-detection/service-detection-v1/service-types/unified-service
scraped: 2026-02-20T21:28:16.331683
---

# Unified services

# Unified services

* How-to guide
* 6-min read
* Updated on Oct 13, 2025

Dynatrace version 1.274

## Overview

The **Unified service** type represents services detected using Service Detection v2 (SDv2) rules based on resource attributes.
These services were first introduced for OpenTelemetry and are now being rolled out for OneAgent in public preview (fall 2025).

Services using SDv2 detection show **Unified service** as their service type in the web UI properties, indicating that SDv2 detection rules are being applied.

Key capabilities:

* Response time, throughput, and failure rate metrics
* Automatic endpoint detection and monitoring

The term "unified services" was introduced before SDv2 existed. The underlying service, endpoint, failure, and splitting detection rules were introduced at the same time, but were hardcoded. SDv2 now makes these rules configurable. While properties still display **Unified service**, SDv2 focuses on detection rules rather than service types.

The Grail metrics `dt.service.request.response_time`, `dt.service.request.failure_count`, and `dt.service.request.count` are billable. To learn more, see [Metrics powered by Grail (DPS)](/docs/license/capabilities/metrics "Learn how Dynatrace Metrics powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.").

For current detection rules and customization options, see the [Service Detection v2](/docs/observe/application-observability/services/service-detection/service-detection-v2 "Find out how to detect, name, and split services from OpenTelemetry and OneAgent spans.").

## Legacy span:service

Legacy **span:services** were automatically migrated to SDv2 (**Unified service**) by October 1, 2025.

This affects **span:services** (OTLP API ingested services) only, not **span (default) services** detected by OneAgent with the OpenTelemetry sensor, which will remain unchanged.

For details, see the [Service Detection V2 (SDv2) Overviewï»¿](https://dt-url.net/b4030ff) post in the Dynatrace Community.

---

## observe/application-observability/services/service-detection/service-detection-v1/set-up-request-naming.md

---
title: Set up request naming
source: https://www.dynatrace.com/docs/observe/application-observability/services/service-detection/service-detection-v1/set-up-request-naming
scraped: 2026-02-20T21:21:47.624537
---

# Set up request naming

# Set up request naming

* How-to guide
* 7-min read
* Updated on Jan 21, 2026

You can use request naming rules to adjust how your requests are tracked and to define service entry and endpoints in your customer-facing workflow. With such end-to-end tracing, you can easily recognize and monitor important business transactions that are critical to the success of your digital business.

By using request attributes in combination with naming rules, you can capture even more context around your requests and use these additional details to slice and dice your monitoring data.

Because request naming rules produce distinct service requests, each request is [independently baselined](/docs/dynatrace-intelligence/anomaly-detection/automated-multidimensional-baselining "Learn how Dynatrace AI automatically calculates baselines based on a multi-dimensional baselining scheme.") and monitored for performance anomalies. The performance metrics captured for these requests are also separately accessible via the [Timeseries API v1](/docs/dynatrace-api/environment-api/metric-v1 "Retrieve metric information via Timeseries v1 API.") endpoint.

## Before you start

* Request naming rules are supported for the following service types.

  + Web request (except **Requests to unmonitored hosts** and **Requests to public networks**)
  + Web
  + Method request
  + Messaging and queing (except [listener services](/docs/observe/infrastructure-observability/queues/queue-concepts#listener-service "Basic concepts of message queue monitoring in Dynatrace."))
  + RMI
  + CICS
  + IMS
  + Enterprise service bus
  + Remote call
* Key request detection is name based. If a request naming rule affects a key request and you want Dynatrace to keep detecting it as a key request, you need to add the new name to the [list of key request names](/docs/observe/application-observability/services-classic/monitor-key-requests#rename "Discover how to closely monitor requests that are critical to your business.").

## Create a request naming rule for a service

The first step in setting up clear naming for your service (web) requests is to create request naming rules with conditions that define how they appear in your environment.

1. Go to ![Services Classic](https://dt-cdn.net/images/services-classic-f58502bd22.svg "Services Classic") **Services Classic** and select the service you want to configure.
2. Select **More** (**â¦**) > **Settings**.
3. On the **Service settings** page, go to the **Request naming rules** (or **Web request naming rules**) and select **Add rule**.
4. Define a set of conditions that represent the criteria of your service operations.

   You can use anything from request headers to code-level method argument values to identify specific requests. All requests that match the specified criteria will be named based on the defined naming pattern.

   ![Request naming rule](https://dt-cdn.net/images/naming-rule-2010-1385de1a99.png)

   In the example above, three conditions are defined.

   * The URL path must contain the string `orange-booking-payment`.
   * The request must be an **HTTP method** of type **GET**.
   * The request must have the attribute `easyTravel destination`.

   All requests matching **all** the specified criteria will be named based on the defined naming pattern `PAYMENT`.

   ![Add request naming rule - example](https://dt-cdn.net/images/example-naming-rule-2006-1ef0fc7a46.png)
5. Select **Save**.

## Global request naming rules

[Service request naming API](/docs/dynatrace-api/configuration-api/service-api/request-naming-api "Learn what the Dynatrace request naming config API offers.") enables you to consolidate or refine requests across multiple services. Additionally, you can synchronize these rules across multiple Dynatrace environments. To learn how to create a global request naming rule via API, see [this use case](/docs/dynatrace-api/configuration-api/service-api/request-naming-api/create-a-new-request-naming-rule "Learn how to create a request naming rule via the Dynatrace API.").

## Configure resource request detection

Dynatrace automatically detects resource requests based on the file extension and tracks these requests in the following groups:

* Images
* CSS
* JavaScript
* Binaries

When the **Enhanced endpoints for SDv1** feature is turned on, all static resource requests are grouped into a single **Static resources** endpoint. See [Static resource requests](/docs/observe/application-observability/services/enhanced-endpoints-sdv1#resource-requests "Utilize the Enhanced endpoints for SDv1 feature to gain deeper insights into your application's performance and improve your ability to monitor and troubleshoot service interactions.") for more details.

If Dynatrace doesn't automatically detect one of your application's images or binaries, you can add the missing filename extensions. You can configure these settings for the entire environment or for a specific service.

Environment

1. Go to ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**.
2. Go to the **Explorer** tab and select any SDv1 service.
3. In the upper-right corner of the service details pane, select  (**Actions menu**) > **Settings**.
4. Under **Naming**, select **Web request naming**.
5. Scroll down to the **Resource requests** section, and follow the **settings** link in **Use global resource request detection settings**.
6. Under **Web resource requests**, enter the required filename extensions for image and binary resources.

Alternatively, use our API to modify [global request naming rules](#global-rules).

Service

1. Go to ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**.
2. Go to the **Explorer** tab, find the service for which you want to update the settings, and select it.
3. In the upper-right corner of the service details pane, select  (**Actions menu**) > **Settings**.
4. Under **Naming**, select **Web request naming**.
5. Scroll down to the **Resource requests** section, and turn off **Use global resource request detection settings**.
6. Enter the required filename extensions for image and binary resources.

## Additional elements for request naming

### Request attributes and placeholders

You can include the value of request attributes and placeholders in naming patterns.

* Use a **Request attribute** to create intuitive variant names for your request. The request creates a separate trackable request for each permutation of the respective request attribute.

Example: Request attributes in naming patterns

Using the request attribute `easyTravel destination` in the naming pattern, a variant request is created for each destination thatâs booked by customers of `easyTravel`. The result is that this rule no longer creates a single kind of request, it now creates a separate trackable request for each booked destination.

![Use request attributes to set up request naming rules](https://dt-cdn.net/images/request-attributes-2002-61662e499a.png)

Looking at the distributed traces, the URLs are all the same but each request name includes now a different destination-city attribute value.

![Naming pattern with request attributes](https://dt-cdn.net/images/request-attributes-example-2004-cfa8f5d39c.png)

* **Placeholder(s)** can extract values from request attributes or URLs.

Example: Custom placeholders

If the URL path contains the string `orange-booking`, the booking defined by the placeholder `stage` is extracted from the URL naming pattern and uppercased. The placeholder `stage` is defined as the text between `orange-booking-` and `.jsf` in the URL path.

![Extraction with placeholder](https://dt-cdn.net/images/extraction-placeholders-2000-0683e7a52f.png)

Using this placeholder, the resulting list of request names appears as follows:

![Results of request naming with placeholder in the service distributed trace list](https://dt-cdn.net/images/placeholders-request-naming-1130-60e819ce95.png)

By constructing your service entry and end points in this way for Dynatrace monitoring, you can track all of your organizationâs key operations, such as business transactions, at a highly granular level.

### Cleanup rules

Service-level rules and settings, including web request services clean URL rules, override global request naming rules.

* You can define global request naming rules through the API to clean up the URLs of one or more services at the time.
* Web request services have unique features to generate clean URLs via UI.

Accessing **Service settings** > **Web request naming**, you can:

* **Remove UUIDs, IP addresses and IBANs from URLs**.

  This action normalizes URL paths containing UUIDs, IP addresses, and IBANs by replacing specific values with content-related static strings, such as `UUID`, `IPv4`, and `IBAN`.

  This option is not available for environments where the [**Enhanced endpoints for SDv1** feature](/docs/observe/application-observability/services/enhanced-endpoints-sdv1 "Utilize the Enhanced endpoints for SDv1 feature to gain deeper insights into your application's performance and improve your ability to monitor and troubleshoot service interactions.") is enabled.
* **Create clean URL rule**.

  Define the [regular expressions](/docs/manage/tags-and-metadata/reference/regular-expressions-in-dynatrace "Learn how to use regular expressions in the context of Dynatrace.") to remove parts of a web request service URL path, such as IDs.

Custom service request names are never masked.

### Preview



You can modify a request naming rule or combine them to create even more fine-grained request names. **Preview Rule** shows the output of the new request naming rule.

![Modify and preview a request naming rule](https://dt-cdn.net/images/modify-naming-rule-2012-c9ae3151bf.png)

In the above example, a new rule, `Booking {RequestAttribute:easyTravel destination} - {stage}`, combines the previous two examples. It defines a request naming pattern that includes not only the booking stage (`{stage}`) but also the destination attribute (`{RequestAttribute:easyTravel destination}`). Now we get a separate request for each booking stage, plus further splits based on the destination attribute.

### Data masking

You can choose to display unmasked data for specific requests by selecting the checkbox **Access unmasked data**.

This will potentially expose [personal data](/docs/manage/data-privacy-and-security/data-privacy/personal-data-captured-by-dynatrace#service-request-monitoring "Find out what types of end-user data may be captured during Dynatrace monitoring and the methods that are available for masking personal end-user data.") before it is stored and displayed.

## Service analysis

The full value of setting up your business-critical requests in this way becomes apparent once you dig into the analysis thatâs available for each individual request on the service level.

Request attributes give you absolute flexibility in identifying and naming your requests based on your business requirements. Dynatrace tracks each request from end to end and tells you how all the requests are related.

Multi-tiered analysis

To illustrate multi-tiered analysis, letâs add another request naming rule that splits out the booking requests based on the attribute `Loyalty`.

![Multi-tiered service analysis](https://dt-cdn.net/images/multi-tiered-analysis-2002-c95686fde7.png)

This addition results in separate requests to this service based on loyalty status.

Now when we look at an individual trace, we can see how useful the two defined request attributes are. In this example, we see that `Booking Shizunai` was performed by a customer who has `PLATINUM` loyalty status. This was achieved by defining a request naming rule on the `easyTravel Customer Frontend` service that tracks bookings per destination and a separate request naming rule that tracks bookings on the backend `BookingServiceTom` based on loyalty status.

![Multi-tiered service analysis trace](https://dt-cdn.net/images/multi-tiered-analysis-trace-2024-0b4a266f8f.png)

Multidimensional analysis

Because request naming rules produce distinct service requests, you have even further filtering options based on the attributes of the new requests that have been defined. In the example below, the destination breakdown is combined with `PLATINUM` loyalty status.

![Resource attributes](https://dt-cdn.net/images/multidim-analysis-2036-7a8488d166.png)

![Request attributes in multidimensional analysis](https://dt-cdn.net/images/multidimen-analysis-request-attributes-2020-b78f22fb23.png)

You can also leverage this functionality in combination with [powerful hierarchical filtering](/docs/observe/application-observability/services-classic/service-flow/service-flow-filtering "Understand how service filtering works and how it can be exploited.").
In this example, we analyze booking requests that are in the `finish` stage, with a destination of `shizunai`, response time range 1s-2s, and Platinum loyalty status.

![Filter traces by request](https://dt-cdn.net/images/multidim-analysis-traces-2014-6fc5fb8941.png)

While this has been possible using request attributes alone, request naming makes this approach even more powerful.

## Limitations

[Atomic groups](/docs/manage/tags-and-metadata/reference/regular-expressions-in-dynatrace#capture-groups-are-not-allowed-for-simple-matches "Learn how to use regular expressions in the context of Dynatrace.") are not allowed in regular expressions for global request naming rules.

## Related topics

* [Capture request attributes based on web request data](/docs/observe/application-observability/services/request-attributes/capture-request-attributes-based-on-web-request-data "Create request attributes based on web request data.")
* [Capture request attributes based on method arguments](/docs/observe/application-observability/services/request-attributes/capture-request-attributes-based-on-method-arguments "Learn how to create request attributes based on Java, .NET, or PHP method arguments and how to use them on the serviceâs overview page. Also find out how you can aggregate the captured values of request attributes as well as how you can access objects, in case the value to be captured is a complex object.")
* [Request attributes API](/docs/dynatrace-api/configuration-api/service-api/request-attributes-api "Learn what the Dynatrace request attribute config API offers.")
* [Calculated metrics for services](/docs/observe/application-observability/services/calculated-service-metric "Learn how to create a calculated metric based on web requests.")
* [Monitor key requests](/docs/observe/application-observability/services-classic/monitor-key-requests "Discover how to closely monitor requests that are critical to your business.")

---

## observe/application-observability/services/service-detection/service-detection-v1.md

---
title: Service Detection v1
source: https://www.dynatrace.com/docs/observe/application-observability/services/service-detection/service-detection-v1
scraped: 2026-02-20T21:08:10.106508
---

# Service Detection v1

# Service Detection v1

* Overview
* 1-min read
* Updated on Aug 06, 2025

Service Detection v1 (SDv1) is a service detection mechanism for OneAgent-instrumented services in Dynatrace.

It provides detection capabilities based on technology-specific service types, each with their own detection rules and configuration options. These capabilities include:

* **Service type recognition**: Identify different service types.
* **Custom detection rules**: Fine-tunes how services are detected and grouped.
* **Request naming**: Tracks key business transactions.
* **Failure detection**: Identifies errors and problematic requests.

In addition to SDv1, you can also use [Service Detection v2](/docs/observe/application-observability/services/service-detection/service-detection-v2 "Find out how to detect, name, and split services from OpenTelemetry and OneAgent spans.") (SDv2), which provides unified service detection rules across OpenTelemetry and OneAgent data sources. SDv2 is available in general availability for OpenTelemetry and in public preview for OneAgent on Kubernetes.

## Service types

SDv1 can detect the following service types:

* **Web request services**: Applications deployed via web servers or web containers.
* **Web services**: As defined by WSDL.
* **Database services**: Applications that make database requests.
* **Messaging services**: Queue and topic listeners in applications.
* **Remoting services**: RMI and RPC communications.
* **Background activity services**: Threads running in the background.
* **Custom services**: User-defined instrumentation for non-standard technologies.

## Configuration options

With SDv1, you can configure the options described below.

### Service detection rules

* Merge applications into a single service.
* Separate services based on URL patterns.
* Create rules for unmonitored hosts.
* Fix web server naming issues.

For details, see [Service detection rules](/docs/observe/application-observability/services/service-detection/service-detection-v1/customize-service-detection "Use detection rules to customize and enhance the automated detection of your services.").

### Service naming

* Built-in rules define out-of-the-box naming.
* Custom service naming rules let you create your own naming standards.
* Service name formats with placeholders for consistent naming conventions.

For additional information, see [Service naming rules](/docs/observe/application-observability/services/service-detection/service-detection-v1/customize-service-naming "Use naming rules to customize and enhance the automated naming of your services.")

### Request naming

* Define how requests appear in your environment.
* Create intuitive names for business transactions.
* Track operations at a granular level.

Check out [Set up request naming](/docs/observe/application-observability/services/service-detection/service-detection-v1/set-up-request-naming "Adjust request naming and define the operations your services offer.") for details.

### Failure detection

* Configure error detection settings globally or for individual services.
* Define custom error rules.
* Handle HTTP errors and exceptions based on your needs.

See [Configure service failure detection](/docs/observe/application-observability/services/service-detection/service-detection-v1/configure-service-failure-detection "Discover which service error types Dynatrace automatically detects and learn how to adjust failure detection settings to meet your specific requirements.") for more information.

## Related topics

* [Service Detection v2](/docs/observe/application-observability/services/service-detection/service-detection-v2 "Find out how to detect, name, and split services from OpenTelemetry and OneAgent spans.")
* [Service detection API](/docs/dynatrace-api/configuration-api/service-api/detection-rules "Learn what the Dynatrace service detection rules config API offers.")
* [Process group detection](/docs/observe/infrastructure-observability/process-groups/configuration/pg-detection "Ways to customize process-group detection")

---

## observe/application-observability/services/service-detection/service-detection-v2/endpoint-detection-v2.md

---
title: Customize endpoint detection in Service Detection v2
source: https://www.dynatrace.com/docs/observe/application-observability/services/service-detection/service-detection-v2/endpoint-detection-v2
scraped: 2026-02-20T21:20:51.878049
---

# Customize endpoint detection in Service Detection v2

# Customize endpoint detection in Service Detection v2

* How-to guide
* 2-min read
* Updated on Feb 04, 2026

Service Detection v2 (SDv2) allows you to identify specific endpoints into your services.
You can use the default Dynatrace detection rules and also define your own custom rules.

If you have existing OpenTelemetry endpoints created before August 2025, you are currently using [hard-coded endpoint detection rules](#legacy-default-endpoint-rules). You can opt in to the [new improved rules](#default-endpoint-rules), which are now configurable and provide better service health monitoring via [settings](#new-default-endpoint-rules-opt-in), but this will cause breaking changes to your endpoints. See the [community postï»¿](https://dt-url.net/lv031sg) for comparison dashboards before opting in.

## Aim and context

This page describes endpoint detection for SDv2, how to use default detection rules, and how to create your own custom rules.

SDv2 treats the following span types as endpoints:

* Standard HTTP and gRPC endpoints (`span.kind == server`).
  These are treated as web-based entry points into a service and represent incoming HTTP or gRPC requests handled by the service.
* Message consumption endpoints (`span.kind == consumer`).
  These are treated as entry points into a service for messages from queue systems like RabbitMQ, ActiveMQ, and Kafka and represent messages consumed by the service.

## Endpoint detection rules

* Rules are evaluated in order, from top to bottom.
* Custom rules are always evaluated before default rules.
* Only the first matching rule is applied.

### New endpoint detection opt-in

Opting in will enable the creation of [custom rules](#create-new-rule) and the use of the new [default rule set](#default-endpoint-rules), but will break existing endpoints. See the [community postï»¿](https://dt-url.net/lv031sg) for comparison dashboards before opting in.

You can find the setting to opt in to the new way of endpoint detection in ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **Services** > **Enable endpoint detection**.

If this setting is not available, you are already using the new configurable endpoint detection rules. This can happen if we didn't find any SDv2-related data in your tenant during the update to Dynatrace version 1.321, or if your tenant was created using Dynatrace version 1.321 or later.

### Default rules

These rules focus on actual service health by considering only service entry points (server and consumer spans), excluding outbound calls to other services. This provides more accurate service health monitoring by distinguishing service problems from external dependency issues.

* The default endpoint detection rules can be activated or deactivated.
* You can add custom endpoint detection rules as described in [Create new rule](#create-new-rule).

Any tenant created with Dynatrace version 1.330+ uses these configurable rules. Older tenants can be opted in to the configurable rule set; see the [New endpoint detection opt-in](#new-default-endpoint-rules-opt-in) section.

Priority

Condition

Endpoint

1

`span.kind == "server"` + `rpc.service` + `rpc.method`

`{rpc.service}.{rpc.method}`

2

`span.kind == "server"` + `rpc.method`

`{rpc.method}`

3[1](#fn-1-1-def)

`span.kind == "server"` + `http.request.method` + `url.path.pattern`

`{http.request.method} {url.path.pattern}`

4

`span.kind == "server"` + `http.request.method` + `url.truncated_path`

`{http.request.method} {url.truncated_path}`

5

`span.kind == "server"` + `http.request.method` + `http.route`

`{http.request.method} {http.route}`

6

`span.kind == "server"` + `http.request.method`

`{http.request.method} /*`

7

`span.kind == "server"` + `span.name`

`{span.name}`

8

`span.kind == "consumer"` + `span.name`

`{span.name}`

1

Rule available with Dynatrace SaaS version 1.330+. See [Configure URL path pattern matching in Service Detection v2](/docs/observe/application-observability/services/service-detection/service-detection-v2/url-pattern-matching-v2 "Find out how to get better endpoint names for frameworks without route templates by setting up URL pattern matching rules.") for details.

### Legacy default rules

Legacy endpoint detection rules apply also to all trace root spans (span without a parent span)âwhether client, consumer, internal, or producer span. This broad approach captured comprehensive system activity but created noise in service health monitoring, since outbound call failures typically indicate problems with the called service rather than the calling service.
However, you can still add custom endpoint rules to the new endpoint detection to restore exactly this behavior.

Priority

Condition

Endpoint name

1

`service.name` starts with `istio-`

`/`

2

`rpc.service` + `rpc.method` + `span.kind` is `server`

`<rpc.method>.<rpc.service>` or `<rpc.method>`

3

`adobe.em.env_type` + `url.truncated_path` + `span.kind` is `server`

`<url.truncated_path>`

4

`adobe.em.env_type` + `url.path` is `/system/probes/health` OR `http.request.method` is `HEAD`

`Health Check`

5

`http.route` + `span.kind` is `server`

`<http.route>`

6

`http.method` + `span.kind` is `server` + `telemetry.sdk.language` is `apache`, `cpp`, or `nginx`

`/`

7

`faas.name`

`invoke`

8

`code.namespace` + `code.function`

`<code.namespace>.<code.function>` or `<code.function>` or `<code.namespace>`

9

`span.name`

`<span.name>`

## Steps

Endpoint detection is customized in ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **Services** > **Endpoint detection**.

### Create new rule

1. In **Endpoint detection**, select **Add rule**.
2. Fill in the following optional and required fields:

   * **Rule name**: Required A user-defined name for the rule.
   * **Description**: Optional A human-readable description of the rule.
   * **Matching condition**: Required A [DQL matcher](/docs/platform/openpipeline/reference/dql-matcher-in-openpipeline "Examine specific DQL functions and logical operators for log processing.").
     If the matching condition applies, the rule is evaluated.

     Keep in mind that the rules are applied on spans with span kind `span.kind == server` or `span.kind == consumer`, as well as on trace root spans (spans without a parent span) regardless of the span kind.

     To avoid unexpected behavior, we recommend adding the span kind explicitly to the condition. For example, `span.kind == server` for HTTP endpoints or `span.kind == consumer` for message consumption endpoints.

   * **If condition matches**: Required The action that will be taken.
     Options are either

     + **Detect request on endpoint**: The endpoint is detected and named.
     + **Suppress request**: The endpoint will not be detected by this or any subsequent rule.
   * **Endpoint name template**: The name that you want the endpoint to have.
     You can use plain text, or span and resource attributes surrounded by curly braces (`{}`).
     For the rule to be applied, the span must contain all the specified resource attributes.
3. Select **Save changes**.

### Edit custom rules

You can re-order custom rules to affect the order of precedence.

You can also edit a custom rule.

1. Navigate to the rule and select **Details** > .
2. Edit the field(s) as appropriate.
3. Select **Save changes**.

It's not possible to re-order or edit built-in rules.

### Delete custom rules

You can delete a custom rule.

1. Navigate to the rule and select **Delete** > .
2. Select **Save changes** to permanently delete the rule, or **Discard changes** to keep the rule.

It's not possible to delete built-in rules, however you can deactivate built-in rules.

## Best practices when creating new rules

* Keep the number of custom rules manageable to maintain performance.
  For many environments, the default rules will be enough.
* Start by creating endpoint rules for the most critical endpoints.
* Use consistent naming conventions for your endpoints.
* Regularly review your custom endpoint rules to ensure that they still match your application architecture.

## Related topics

* [Service Detection v2](/docs/observe/application-observability/services/service-detection/service-detection-v2 "Find out how to detect, name, and split services from OpenTelemetry and OneAgent spans.")

---

## observe/application-observability/services/service-detection/service-detection-v2/failure-detection-v2.md

---
title: Customize failure detection in Service Detection v2
source: https://www.dynatrace.com/docs/observe/application-observability/services/service-detection/service-detection-v2/failure-detection-v2
scraped: 2026-02-20T21:18:54.368956
---

# Customize failure detection in Service Detection v2

# Customize failure detection in Service Detection v2

* Latest Dynatrace
* How-to guide
* 3-min read
* Updated on Nov 24, 2025

Service Detection v2 (SDv2) allows you to detect failures based on the attributes of a span that is relevant to failure detection.
These relevant spans include, for example, [request](/docs/semantic-dictionary/fields#request "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.") root spans.
You can use the default Dynatrace detection rules and also define your own custom rules.

## Aim and context

This page describes failure detection for SDv2, how to use default detection rules, and how to create your own custom rules.

Failure detection consists of:

* The ruleset, which is a DQL matcher that specifies the overall span and resource attributes that are evaluated.
* Failure conditions under which the span will fail.
* Custom failure rules that use DQL matchers to specify additional conditions under which the span will fail.
* Ignored exceptions, where you can force the span to succeed even in if the defined exceptions occur.

### Failure detection rulesets and rules

* Rulesets and rules are evaluated in order, from top to bottom.
* Custom rulesets are always evaluated before default rulesets.
* The first matching ruleset is applied.
* Within the applied ruleset, all rules are evaluated.

### Default failure detection rulesets and rules

Dynatrace provides default failure detection rulesets and rules.
Additionally, you can add custom rulesets and rules as described in [Create new ruleset](/docs/observe/application-observability/services/service-detection/service-detection-v2/failure-detection-v2#create-new-ruleset "Find out how to detect failed requests within services.").

Condition

Failure reason

`span.status_code` is `ERROR`

Based on span status

`http.response.status_code` is `5xx` (server-side error)

The HTTP error status code

`rpc.grpc.status_code` is `2`, `4`, `12`, `13`, `14`, or `15` (that is, a server-side error code).

The gRPC error status code

Exited by exception

The exception itself

A request is considered successful if no failure detection rule matches.

## Steps

Failure detection is customized in ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **Services** > **Failure detection**.

To configure failure detection:

1. Create the ruleset.
2. Define the failure conditions.
3. Define the ignored exceptions. Optional
4. Define the rule(s). Optional
5. Define any HTTP or gRPC status code overrides. Optional

### Create the ruleset

1. In **Failure detection**, select **Add ruleset**.
2. Fill in the following optional and required fields:

   * **Ruleset name**: Required A user-defined name for the ruleset.
   * **Description**: Optional A human-readable description of the rule.
   * **Matching condition**: Required A [DQL matcher](/docs/platform/openpipeline/reference/dql-matcher-in-openpipeline "Examine specific DQL functions and logical operators for log processing."), which specifies the span and resource attributes that the ruleset applies to.
     If the matching condition applies, the ruleset is evaluated.
3. To save, select **Save changes**.

### Define the failure conditions

Within the ruleset, these parameters define conditions under which a span will fail.

* **HTTP status codes**: One or more HTTP status codes.
  If one of these codes is returned, the span will fail.
  By default this is set to `500-599`.
* **gRCP status codes**: One or more gRCP status codes.
  If one of these codes is returned, the span will fail.
  By default this is set to `2,4,12,13,14,15`.
* **Span status code**: If enabled: when the span's status code indicates a failure, the span will fail.
  By default, this is enabled.
* **Exceptions**: If enabled: when an unescaped exception occurs, the span will fail.
  By default, this is enabled.

### Add ignored exceptions

Optional

Within a ruleset, you can exclude specific exceptions.
If the span includes the defined exception type and message, this exception will not cause the span to fail.

Select **Add ignored exception** and enter values for both:

* **Exception type contains**.
* **Exception message contains**.

Example ignored exception

To ignore all NullPointerExceptions that contain the expected null value in their message, set the following values.

* Exception type contains: `NullPointerException`
* Exception message contains: `<Expected null value>`

### Define the custom failure rule(s)

Optional

Beyond the failure conditions that you already defined, you can define additional custom conditions under which a span will fail.
These conditions are called custom failure rules.
They are defined with any key/value pair using DQL matchers.

1. To define a rule, select **Add custom rule**.
2. Fill in the following required fields.

   * **Rule name**: A descriptive name.
   * **DQL condition**: A [DQL matcher](/docs/platform/openpipeline/reference/dql-matcher-in-openpipeline "Examine specific DQL functions and logical operators for log processing.") that consists of one or more DQL functions.
     If the matching condition applies, the rule is triggered.
     If the matching condition does not apply, the rule is not triggered.

     Whether or not the condition applies, the span is evaluated against subsequent rules.

When a rule is triggered, a corresponding entry in the [`dt.failure\_detection.results array](/docs/semantic-dictionary/model/trace#failure-detection-result "Get to know the Semantic Dictionary models related to traces.") is created.

Example custom rule

This is an example custom rule to detect business logic failures.

* Rule name: `Business Transaction Failure`
* DQL matching rule: `transaction.status == "FAILED"`

### Override failure detection

Optional

Sometimes, you want a span to succeed even if it contains error indicators.
Within a ruleset, you can define certain conditions that will force success.

To do this, select  > **Override failure detection with success forcing rules**.
Then, define one or more rules.

* **HTTP status codes**: The HTTP error code(s) that will force success on the server side.
* **gRPC error codes**: The gRPC error code(s) that will force success on the server side.
* **Span status code**: If the span's status code is `OK` it will succeed, regardless of any other error indicators.
* **Force success on specific exceptions**: Specific exceptions that should force success, see [Define ignored exceptions](#ignored-exceptions).
* **Custom success forcing rules**: Custom conditions that should force success, see [Define the rule(s)](#define-rules).

Example escaped exception

To force success on an example span that contains an escaped exception, set the following values.

* Evaluated expression: `Any(span.events[][span_event.name] == "exception" and span.events[][exception.escaped] != false)`
* Failure detection result: `reason="exception", verdict="success", exception_ids`

This is useful for applications that use exceptions as part of normal control flow rather than as error indicators.

Example custom success rule

To force success for an expected business condition, set the following values.

* Rule name: `Expected Cache Miss`
* DQL matching rule: `cache.result == "MISS" and operation.type == "READ"`

This is useful for business-specific scenarios where there are expected business conditions.

### Edit custom rulesets and rules

You can re-order custom rulesets and rules to affect the order of precedence.

You can also edit custom rulesets and rules.
To do so, navigate to the ruleset or rule and select **Details** > .
Edit the field(s) as appropriate and then select **Save changes**.

### Delete custom rulesets and rules

To delete a custom ruleset or rule, navigate to the ruleset or rule and select **Delete** > .
Select **Save changes** to permanently delete the ruleset or rule, or **Discard changes** to keep the rule.

You can delete only custom rulesets and rules, not the built-in ones.

## Related topics

* [Service Detection v2](/docs/observe/application-observability/services/service-detection/service-detection-v2 "Find out how to detect, name, and split services from OpenTelemetry and OneAgent spans.")

---

## observe/application-observability/services/service-detection/service-detection-v2/service-detection-v2.md

---
title: Customize service detection in Service Detection v2
source: https://www.dynatrace.com/docs/observe/application-observability/services/service-detection/service-detection-v2/service-detection-v2
scraped: 2026-02-20T21:24:08.022979
---

# Customize service detection in Service Detection v2

# Customize service detection in Service Detection v2

* How-to guide
* 2-min read
* Updated on Nov 24, 2025

Service Detection v2 (SDv2) allows you to define services based on span resource attributes.
You can use the default Dynatrace detection rules and also define your own custom rules.
The same rules are also applied to log and metric ingest which allows Dynatrace to link the input of all sources together.

## Aim and context

This page describes service detection for SDv2, how to use default detection rules, and how to create your own custom rules.

### Service detection rules

* Rules apply to spans, metrics, and logs.

* Rules are evaluated in order, from top to bottom.
* Custom rules are always evaluated before default rules.
* Only the first matching rule is applied.

### Default service detection rules

Dynatrace provides several default service detection rules.
Additionally, custom rules can be created as described in [Create new rule](/docs/observe/application-observability/services/service-detection/service-detection-v2/service-detection-v2#create-new-rule "Find out how to detect services based on OpenTelemetry resource attributes.").

Any future default rule changes will be opt-in: new rules will be shipped as disabled; you can choose whether to activate them.

Priority

Condition

Service name

1

`adobe.em.tier`, `adobe.em.env_type`, `adobe.em.program` attributes present

`aem-{adobe.em.tier}-{adobe.em.env_type}-{adobe.em.program}`

2

`k8s.workload.name` attribute present

`{k8s.workload.name}`

3

`dt.kubernetes.workload.name` attribute present

`{dt.kubernetes.workload.name}`

4

`istio.canonical_service` attribute present

`{istio.canonical_service}`

5

`service.name` attribute present

`{service.name}`

The service ID is a unique identifier, such as `SERVICE-649B4E44CBA804F4`, that is the result of hashing the attribute values that are used as part of the name pattern, additional service detection attributes, and [service splitting attributes](/docs/observe/application-observability/services/service-detection/service-detection-v2/service-splitting-v2 "Find out how to split detected services based on resource attributes."), when applicable.

## Steps

Detection rules are customized in ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **Services** > **Service detection**.

### Create new rule

1. In **Service detection**, select **Add rule**.
2. Fill in the following optional and required fields:

   * **Rule name**: Required

     A user-defined name for the rule.
   * **Description**: Optional

     A human-readable descriptor of the rule.
   * **Matching condition**: Required

     A [DQL matcher](/docs/platform/openpipeline/reference/dql-matcher-in-openpipeline "Examine specific DQL functions and logical operators for log processing.").
     If the matching condition applies, the rule is evaluated.
   * **Service name template**: Required

     The name that you want the service to have.
     You can use plain text, or resource attributes surrounded by curly braces (`{}`).
     For the rule to be applied, the span must contain all the specified resource attributes.
     Changing the static parts of the template or re-ordering the used attributes will not affect the service ID. Only completely removing an attribute or adding a new attribute will also change the service ID.
   * **Additional service detection attributes**: Optional

     Additional attributes used to detect and split services without affecting the generated name.
     Each attribute consists of a resource attribute specified without curly braces (for example, `service.name` or `k8s.workload.name`).
     Adding or removing attributes in this section will change the resulting service ID.

     Up to 10 additional service detection attributes can be applied.
3. Select **Save changes**.

### Edit custom rules

You can re-order custom rules.

You can also edit a custom rule.

1. Navigate to the rule and select **Details** > .
2. Edit the fields as appropriate.
3. Select **Save changes**.

### Delete custom rules

To delete a custom rule

1. Navigate to the rule and select **Delete** > .
2. Select **Save changes** to permanently delete the rule, or **Discard changes** to keep the rule.

You can delete only custom rules, not the built-in rules.

## FAQ

### How can I remove an attribute that was used as part of the service name without also changing the service ID?

To remove an attribute that was used as part of the service name without also changing the service ID

1. Remove the attribute from the **Service name template**.
2. Add the attribute to the **Additional service detection attributes** section.

This way, it will still contribute to the service ID, but it will no longer be part of the service name.

### My **Matching conditions** do match certain spans but still my rule is not applied. Why?

Verify that all the attributes used as parts of the **Service name template** and **Additional service detection attributes** also exist on the spans. The existence of those attributes is an implicit matching condition.

## Related topics

* [Service Detection v2](/docs/observe/application-observability/services/service-detection/service-detection-v2 "Find out how to detect, name, and split services from OpenTelemetry and OneAgent spans.")

---

## observe/application-observability/services/service-detection/service-detection-v2/service-splitting-v2.md

---
title: Customize service splitting in Service Detection v2
source: https://www.dynatrace.com/docs/observe/application-observability/services/service-detection/service-detection-v2/service-splitting-v2
scraped: 2026-02-19T21:27:56.357054
---

# Customize service splitting in Service Detection v2

# Customize service splitting in Service Detection v2

* How-to guide
* 2-min read
* Updated on Nov 24, 2025

Service Detection v2 (SDv2) lets you split your [detected services](/docs/observe/application-observability/services/service-detection/service-detection-v2/service-detection-v2 "Find out how to detect services based on OpenTelemetry resource attributes.") based on resource attributes.
You can use the default Dynatrace detection rules and also define your own custom rules.
These rules are applied globally to all detected services.

## Aim and context

This page describes service splitting for SDv2, how to use default splitting rules, and how to create your own custom rules.

Service splitting is particularly useful when:

* You need to compare the same service across different environments.
* You want to isolate performance issues to specific deployment regions.
* You need to track behavior differences between service versions.
* You're troubleshooting environment-specific issues.

### Service splitting rules

* Rules are evaluated in order, from top to bottom.
* Custom rules are always evaluated before default rules.
* Only the first matching rule is applied.

### Default splitting rules

Dynatrace provides default service splitting rules as described in the table below.
Additionally, custom rules can be created as described in [Create new rule](/docs/observe/application-observability/services/service-detection/service-detection-v2/service-splitting-v2#create-new-rule "Find out how to split detected services based on resource attributes.").

Priority

Rule name

Condition

Splitting attributes

Status

1

Split Adobe Experience Manager (AEM) services by process group

`adobe.em.tier` + `adobe.em.env_type` + `adobe.em.program`

`dt.entity.process_group`

Enabled

2

Split services by k8s cluster and namespace

None (applies to all)

`k8s.namespace.name` + `k8s.cluster.uid`

Enabled[1](#fn-1-1-def)

3

Split services by k8s namespace Deprecated

None (applies to all)

`k8s.namespace.name`

Disabled[2](#fn-1-2-def)

1

If you began using Dynatrace before Dynatrace version 1.317, this is disabled.

2

If you began using Dynatrace before Dynatrace version 1.317, this is enabled.

## Steps

Service splitting rules are customized in ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **Services** > **Service splitting**.

### Create new rule

1. In **Service splitting**, select **Add rule**.
2. Fill in the following optional and required fields:

   * **Rule name**: Required A user-defined name for the rule.
   * **Description**: Optional A human-readable description of the rule.
   * **Matching condition**: Required A[DQL matcher](/docs/platform/openpipeline/reference/dql-matcher-in-openpipeline "Examine specific DQL functions and logical operators for log processing.").
     If the matching condition applies, the rule is evaluated.
   * **Split service by resource attribute**: Optional Spans will be separated into services according to the resource attribute(s) defined here.
     Consists of one or more resource attributes specified without curly braces, e.g. `dt.entity.process_group` or `k8s.namespace.name`.

     To add a resource attribute, select **Add item** and enter the **Attribute key**.

     Up to 10 resource attributes can be configured.
3. To save, select **Save changes**.

### Edit custom rules

You can re-order custom rules to affect the order of precedence.

You can also edit a custom rule.

1. Navigate to the rule and select **Details** > .
2. Edit the field(s) as appropriate.
3. Select **Save changes**.

It's not possible to re-order or edit built-in rules.

### Delete custom rules

You can delete a custom rule.

1. Navigate to the rule and select **Delete** > .
2. Select **Save changes** to permanently delete the rule, or **Discard changes** to keep the rule.

It's not possible to delete built-in rules, however you can deactivate built-in rules.

## Best practices for splitting services

* Start with broader splitting rules before adding more specific ones.
* Don't over-split services as this can cause you to receive the same alert spread across many different services.
* Choose attributes that provide meaningful insights for your specific use case.
* Regularly review splitting rules as your application architecture evolves.

## Related topics

* [Service Detection v2](/docs/observe/application-observability/services/service-detection/service-detection-v2 "Find out how to detect, name, and split services from OpenTelemetry and OneAgent spans.")

---

## observe/application-observability/services/service-detection/service-detection-v2/url-pattern-matching-v2.md

---
title: Configure URL path pattern matching in Service Detection v2
source: https://www.dynatrace.com/docs/observe/application-observability/services/service-detection/service-detection-v2/url-pattern-matching-v2
scraped: 2026-02-20T21:29:07.779190
---

# Configure URL path pattern matching in Service Detection v2

# Configure URL path pattern matching in Service Detection v2

* Latest Dynatrace
* How-to guide
* 7-min read
* Published Jan 23, 2026

Dynatrace SaaS version 1.330+

With the **URL pattern matching** feature, Service Detection v2 (SDv2) can generate better endpoint names by extracting URL path patterns from raw URL paths.

Dynatrace can extract stable, lowâvolatility URL patterns from raw URL paths and write them to the `url.path.pattern` span attribute. The `url.path.pattern` attribute is derived beforehand and then used by [SDv2 endpoint detection](/docs/observe/application-observability/services/service-detection/service-detection-v2/endpoint-detection-v2 "Find out how to detect endpoints that are entry points into your service.") to name and group endpoints appropriately.

The **URL pattern matching** feature is designed for situations where frameworks or servers don't provide route templates (for example, reverse proxies or libraries without `http.route`), so endpoint names remain meaningful and consistent, preserving correct granularity for critical performance metrics.

## Aim and context

This page describes URL path pattern matching for SDv2 and how to create URL path pattern matching rules, specifically how to define URL path patterns correctly.

* SDv2 applies URL pattern matching to the `span.kind == server` and `span.kind == consumer` span types.
* Endpoint detection includes the **HTTP request method and URL path pattern** [built-in endpoint rule](/docs/observe/application-observability/services/service-detection/service-detection-v2/endpoint-detection-v2#default-endpoint-rules "Find out how to detect endpoints that are entry points into your service."). This rule uses `url.path.pattern` and takes precedence over the **HTTP request method and route** rule in determining endpoint names. This way, your extracted URL pattern takes precedence when both `url.path.pattern` and `http.route` are available.
* To benefit from the **URL pattern matching** feature, you need to [create URL path pattern matching rules](#create-rule), specifying the required URL path patterns according to the pattern syntax reference.
* A URL path pattern describes how a raw URL path (for example, `/order/12345`) is generalized into a stable template (for example, `/order/{id}`). It's leveraged to produce lowâvolatility values for the `url.path.pattern` span attribute.

## Pattern matching logic and precedence

* Only spans with `span.kind == server` and `span.kind == consumer` are processed.
* One URL path pattern matching rule may contain one or more URL path patterns.
* URL path pattern matching rules are evaluated in order from top to bottom. Only the first matching rule is applied. The first rule with a URL pattern that matches is applied to a span.
* URL path patterns within a matching rule are also evaluated in order from top to bottom. Only the first matching URL pattern is applied.

  The first matching URL path pattern defines the resulting value for the `url.path.pattern` attribute of a span. When the URL pattern matches, the `url.path.pattern` span attribute is based on this matching URL pattern.
* URL patterns operate on path segments; path segments are URL parts between a slash `/`.
* Leading slashes in URL paths are normalized before matching.

  Before URL patterns are evaluated, any number of leading slashes in the path is reduced to a single `/` to ensure consistent and reliable matching.
* Matching is case sensitive.

## URL pattern syntax reference

Use the information below to construct meaningful URL path patterns for your [URL path pattern matching rules](#create-rule).

The following characters or values are possible in the URL path patterns. Use them to replace highâcardinality parts of your URLs (IDs, version numbers, and deep internal URL paths) with placeholders or asterisks while keeping the overall structure of the endpoint recognizable.

* Literal segments
* Placeholders `{placeholder-name}`
* Variable segments `_`
* Catch-all `*`

### Literal segments

* Represented by a literal value of a path segment.
* Matches an exact path segment.
* Copied as-is to the output.
* Use for fixed path parts that never change.

URL pattern

URL path

Resulting endpoint

`/api/orders`

`/api/orders`

`/api/orders`

### Placeholder `{placeholder-name}`

* Represented by a placeholder name in curly braces, for example, `{id}` or `{date}`.
* Matches exactly one path segment.
* Replaced with a placeholder name in curly braces.
* Use to hide dynamic path values, for example, IDs, UUIDs, or timestamps.

URL pattern

URL path

Resulting endpoint

`/api/orders/{id}`

`/api/orders/1234`

`/api/orders/abcd`

`/api/orders/{id}`

`/api/orders/{id}`

### Variable segments `_`

* Represented by an underscore `_`.
* Matches exactly one path segment.
* Replaced with the original segment value.
* Use when the segment should remain visible, for example, for versioned APIs where the version should remain visible.

URL pattern

URL path

Resulting endpoint

`/api/_/orders`

`/api/v1/orders`

`/api/v2/orders`

`/api/v1/orders`

`/api/v2/orders`

### Catch-all `*`

* Represented by an asterisk `*`.
* Matches zero or more trailing segments. Must be the last token in the URL pattern.
* Replaced with `*`.
* Use when matching any remaining path segments.

URL pattern

URL path

Resulting endpoint

`/internal/*`

`/internal/service`

`/internal/service/operation/extra`

`/internal/*`

`/internal/*`

## Configure URL pattern matching

The sections below describe how to create and manage URL pattern matching rules.

### Create a URL pattern matching rule

To create a URL path pattern matching rule

1. Go to **Settings** (Dynatrace Classic) or **Settings Classic** > **Service detection** > **URL path pattern matching**.

When the **Settings Classic** option is not available for you, use the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") to create URL pattern matching rules.

2. Select **Add rule**.
3. Fill in the following optional and required fields.

   * **Rule name**: Required

     A user-defined name for the rule.
   * **Description**: Optional

     A human-readable descriptor of the rule.
   * **Matching condition**: Required

     A [DQL matcher](/docs/platform/openpipeline/reference/dql-matcher-in-openpipeline "Examine specific DQL functions and logical operators for log processing.").
     If the matching condition applies, the rule is evaluated.
4. Select **Add item** and specify a URL path pattern according to the [pattern syntax reference](#syntax-reference). Repeat if more path patterns should to be added.
5. If required, use ![Drag handle](https://dt-cdn.net/images/drag-handle-turquoise-600-1aa0e5ea00.svg "Drag handle") to re-order the added URL path patterns, considering that the first matching pattern is used to determine the `url.path.pattern` attribute value.
6. Select **Save changes**.

### Manage URL pattern matching rules

You can edit, disable, or delete your URL pattern matching rules.

1. Go to **Settings** (Dynatrace Classic) or **Settings Classic** > **Service detection** > **URL path pattern matching**.

When the **Settings Classic** option is not available for you, use the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") to create URL pattern matching rules.

2. Make the required changes to your URL path pattern matching rules:

   * ![Expand row](https://dt-cdn.net/images/expand-row-icon-9c4950fc2e.svg "Expand row") in the **Details** column to edit a rule.
   * ![Toggle icon](https://dt-cdn.net/images/icon-toggle-barista-701-35879d6adf.png "Toggle icon") in the **Enabled** column to disable or enable a rule.
   * ![Drag handle](https://dt-cdn.net/images/drag-handle-turquoise-600-1aa0e5ea00.svg "Drag handle") to re-order the rules.
   * ![Remove](https://dt-cdn.net/images/remove-icon-105c6a04c2.svg "Remove") in the **Delete** column to permanently delete a rule.
3. Select **Save changes** to apply the changes you've made.

## Use cases and examples

The **URL pattern matching** feature is particularly useful for the following use cases:

* Nginx reverse proxy routing
* Versioned APIs
* REST endpoints with IDs
* Internal APIs with deep paths
* Mixed depth paths

Use case

URL pattern

URL path

Resulting endpoint

Nginx reverse proxy routing

`/api/_/_/{id}`

`/api/v1/users/john`

`/api/v2/users/jack`

`/api/v1/users/{id}`

`/api/v2/users/{id}`

API versioning patterns

`/api/_/_/{id}`

`/api/v1/orders/123456789`

`/api/v2/orders/987654321`

`/api/v1/orders/{id}`

`/api/v2/orders/{id}`

Mixed depth paths

`/blog/_/_/*`

`/blog/2024/11/my-post.md`

`/blog/2024/12/my-holiday.md`

`/blog/2026/01/15/my-thoughts.md`

`/blog/2026/02/05/my-memories.md`

`/blog/2024/11/*`

`/blog/2024/12/*`

`/blog/2026/01/*`

`/blog/2026/02/*`

## Related topics

* [Customize endpoint detection in Service Detection v2](/docs/observe/application-observability/services/service-detection/service-detection-v2/endpoint-detection-v2 "Find out how to detect endpoints that are entry points into your service.")

---

## observe/application-observability/services/service-detection/service-detection-v2.md

---
title: Service Detection v2
source: https://www.dynatrace.com/docs/observe/application-observability/services/service-detection/service-detection-v2
scraped: 2026-02-19T21:18:36.664478
---

# Service Detection v2

# Service Detection v2

* Overview
* 1-min read
* Updated on Feb 04, 2026

Service Detection v2 (SDv2) operates according to a single set of rules that are based on attributes. This includes default rules, and you can additionally define your own custom rules. SDv2 rules are generally available for OpenTelemetry services; for services that are running in Kubernetes and monitored by OneAgent, SDv2 rules are available as a Preview release.

Preview release for OneAgent-instrumented Kubernetes services

SDv2 is available as a Preview release for services that are running in Kubernetes and monitored by OneAgent. You can join this Preview release via the **Service Detection v2 for OneAgent** settings page.

1. Go to ![Kubernetes](https://dt-cdn.net/images/kubernetes-512-90e7075764.png "Kubernetes") **Kubernetes Classic**.
2. Find and select your Kubernetes cluster. When required, also select the namespace.
3. In the upper-right corner of the cluster or namespace overview page, select **More** (**â¦**) > **Settings**.
4. Go to **Service detection** > **Service Detection v2 for OneAgent**.
5. Turn on **Enable Service detection v2 for Kubernetes workloads**.

As part of the Preview release, you can use the following attributes to further restrict where the new SDv2 rules should be applied.

* `dt.agent.module.type`
* `k8s.cluster.name`
* `k8s.namespace.name`
* `k8s.workload.name`
* `dt.host_group.id`

These are customized within your Kubernetes namespace or cluster settings.

Currently, Java is the only supported language, and you need to keep the default matching condition as `dt.agent.module.type == "java"`. Support for additional languages is currently planned and will be announced via release notes.

SDv2 provides:

* Service detection and naming based on resource attributes and conditions.
* Endpoint detection based on span and resource attributes.
* Service splitting based on resource attributes.
* Failure detection based on HTTP or gRPC codes or other span and resource attributes.

SDv2 behavior can be configured via:

* The Dynatrace web UI, as described in the pages within this section.
* The [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.").

## Related topics

* [Service Detection v1](/docs/observe/application-observability/services/service-detection/service-detection-v1 "Find out how Dynatrace Service Detection v1 detects and names different types of services.")

---

## observe/application-observability/services/services-app.md

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

---

## observe/application-observability/services/services-concepts.md

---
title: Service-related concepts
source: https://www.dynatrace.com/docs/observe/application-observability/services/services-concepts
scraped: 2026-02-20T21:07:51.553623
---

# Service-related concepts

# Service-related concepts

* Latest Dynatrace
* Explanation
* 3-min read
* Updated on Jan 28, 2026

Service-related concepts, including distributed traces and spans, are central concepts in Dynatrace observability. Understanding these concepts enables effective monitoring and analysis of distributed systems.

## Attributes

**Attributes** are key-value pairs that provide details about spans, requests, or resources (for example, a span name, response codes, HTTP methods, URLs, or failure detection results). They're used to group, query, find, and analyze traces and spans.

Dynatrace uses resource attributes to detect and name services, gather trace context data and entity relationships for Smartscape topology, connect log data to traces, understand span duration impacts from service timings, and analyze executed code. Attribute keys adhere to the [Dynatrace Semantic Dictionary](/docs/semantic-dictionary "The Semantic Dictionary defines standardized field names used across monitoring data types like logs, events, spans, metrics, and entities.").

## Spans and distributed traces

**Spans** are single units of work within a distributed trace. Each span consists of multiple attributes and includes information such as a span ID, span name, start time, duration, span events (for example, exceptions), span kind, and parent span identifier. Spans connect via the parent identifier to build a tree-like structure.

**Distributed traces** are sequences of spans with an identical trace ID that follow a single path through various services and components. They help you understand request propagation across distributed systems, analyze microservices data, assess microservice performance, and follow [Dynatrace Intelligence](/docs/dynatrace-intelligence "Get familiar with the capabilities of Dynatrace Intelligence.")
root cause analysis for cause-and-effect relationships.

## Services and service detection

**Services** are logical units that group together related spans within distributed traces, for example, all spans produced by the same Kubernetes workload.

**Service Detection v2 (SDv2)** operates according to a single set of attribute-based rules (built-in and user-defined) evaluated against every span of a trace. It's available for OpenTelemetry trace data and in public preview for traces produced by OneAgent (Java) in Kubernetes. Request metrics are only recorded for services with defined endpoints.

**Service Detection v1 (SDv1)** is the classic service detection for OneAgent-instrumented processes. It provides detection based on technology-specific service types with limited configurability compared to Service Detection v2.

## Endpoints and entry points

**Endpoints** represent the API entry point of a service. For Service Detection v2, endpoints are defined through rules matching span attributes. For Service Detection v1, endpoints are automatically derived and supersede the concept of [key requests](#key-requests)on SaaS. All endpoints generate associated metrics and are displayed in [![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**](/docs/observe/application-observability/services/services-app "Maintain centralized control over service health, performance, and resources with the Services app.") for both service detection versions.

**Entry points** (Service Detection v1) mark the first method or operation when a service is invoked. They serve as the starting point for tracing activity and are used in failure detection configuration, custom service definition, and service flow analysis.

## Requests

Requests have different definitions depending on the service detection version.

* **Service Detection v1**: A request encompasses all spans of a trace that belong to the same service and aren't interrupted by spans of a different service. All workload typesâweb, messaging, batch, and cron jobsâare treated as requests.
* **Service Detection v2**: Requests specifically track external calls into a monitored process, represented as endpoints (for example, web requests or RPC/RMI calls). Services without endpoints have no request metrics.

## Key requests

Key requests are requests requiring special attention (critical business measures or vital technical functionality). This legacy approach requires manual configuration with limits of 500 per environment and 100 per service.

Switch to Enhanced endpoints for SDv1

Instead of [defining key requests](/docs/observe/application-observability/services-classic/monitor-key-requests "Discover how to closely monitor requests that are critical to your business.") for SDv1 services, we strongly recommend enabling the [**Enhanced endpoints for SDv1** feature](/docs/observe/application-observability/services/enhanced-endpoints-sdv1 "Utilize the Enhanced endpoints for SDv1 feature to gain deeper insights into your application's performance and improve your ability to monitor and troubleshoot service interactions.") that allows showing all endpoints in ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**, not just key requests.

## Errors, exceptions, and failures

**Errors and exceptions** are captured as attributes on spans (for example, span events) within distributed traces. They provide details about request processing problems, including an error type, message, stack traces, timestamp, and associated span context. Errors and exceptions are automatically captured from OneAgent-monitored applications and OpenTelemetry instrumentation.

**Failures** are determined by failure detection, typically based on error and exception data. Note that the existence of errors doesn't necessarily mean the associated request is considered failed. Configuration differs between Service Detection v1 (global or per-service settings) and Service Detection v2 (rule sets based on span attributes).

---

## observe/application-observability/services-classic/monitor-key-requests.md

---
title: Monitor key requests
source: https://www.dynatrace.com/docs/observe/application-observability/services-classic/monitor-key-requests
scraped: 2026-02-20T21:20:39.938816
---

# Monitor key requests

# Monitor key requests

* How-to guide
* 5-min read
* Updated on Jan 21, 2026

Switch to Enhanced endpoints for SDv1

Setting up key requests is not available for environments created in Dynatrace version 1.330+.

Instead of defining key requests as described on this page, we strongly recommend enabling the [**Enhanced endpoints for SDv1** feature](/docs/observe/application-observability/services/enhanced-endpoints-sdv1 "Utilize the Enhanced endpoints for SDv1 feature to gain deeper insights into your application's performance and improve your ability to monitor and troubleshoot service interactions.") that allows showing all endpoints in [![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**](/docs/observe/application-observability/services/services-app "Maintain centralized control over service health, performance, and resources with the Services app."), not just key requests.

*Key requests* are requests that need special attention, either because they're a critical measure of the success of your business (for example, a login request or a shopping-cart checkout request) or because they provide vital technical functionality that your application relies on.

* Key requests feature [dedicated metrics](/docs/analyze-explore-automate/metrics-classic/built-in-metrics#key-requests "Explore the complete list of built-in Dynatrace metrics.") that you can manage via the web UI or [API](#manage-api). You can create dedicated dashboard tiles for charting key requests, with direct access from your dashboard, and analyze key request long-term metric history in [request charts](/docs/observe/application-observability/services-classic#request-charting "Learn about Dynatrace's classic service monitoring").
* Alerting is always enabled for key requests, even when they contribute less than 1% of throughput. They also provide custom thresholds.
* Data retention periods of key requests are maintained as follows:

  Data type

  Retention period

  [Detailed code-level data](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods#purepath "Check retention times for various data types.")

  10 days

  [Aggregated code-level data](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods#request-attributes "Check retention times for various data types.")

  35 days

  [Long-term metric history](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods#metrics-classic "Check retention times for various data types.")

  5 years

Key requests are highlighted in **Key requests/endpoints** of each service overview page. This visibility is particularly valuable for low-volume, high-importance requests that would otherwise appear at the bottom of **Top requests**.

The number of key requests is limited:

* 500 key requests per environment across all services.
* 100 key requests per service.

When you reach that limit, consider using [calculated service metrics](/docs/observe/application-observability/services/calculated-service-metric "Learn how to create a calculated metric based on web requests."), which offer you a more flexible approach.

## Create a key request (via web UI)

To mark a specific request as a key request

1. Go to ![Services Classic](https://dt-cdn.net/images/services-classic-f58502bd22.svg "Services Classic") **Services Classic**.
2. Select the relevant service from the list.
3. On the service overview page, select a **View** button (such as **View requests**, **View dynamic requests**, or **View resource requests**).
4. Scroll down to **Top requests** and select a request you want to mark as a key request.
5. On the request overview page, select **More** (**â¦**) > **Mark as key request** or **Pin to dashboard**.

   ![Set key request](https://dt-cdn.net/images/key-request-1000-c04070fc96.png)

After you manually identify a key request, its trend lines are retained perpetually.

## Show key requests on a dashboard

To create a dashboard tile for a specific request

1. Go to ![Services Classic](https://dt-cdn.net/images/services-classic-f58502bd22.svg "Services Classic") **Services Classic**.
2. Select the relevant service from the list.
3. On the service overview page, select **View** (**View requests**, **View dynamic requests**, or **View resource requests**).
4. Scroll down to **Key requests/endpoints** and select a request you want to show on a dashboard.
5. On the request overview page, select **More** (**â¦**) > **Pin to dashboard**.  
   A new request-specific tile that shows the most important metrics for that particular request is then added to your dashboard.

Dashboard tiles include only data collected after the request has been marked as key request.

## Rename key requests

Key request detection is name-based. When you apply a [request naming rule](/docs/observe/application-observability/services/service-detection/service-detection-v1/set-up-request-naming "Adjust request naming and define the operations your services offer."), it can affect key requests. If you want Dynatrace to continue detecting renamed requests as key requests, you need to add the new name to the list of key request names.

1. Go to ![Services Classic](https://dt-cdn.net/images/services-classic-f58502bd22.svg "Services Classic") **Services Classic** and select the service you want to configure.
2. Select **More** (**â¦**) > **Settings**.
3. On the **Service settings** page, go to the **Key requests** tab and select **Add item** to add the name to which the request naming rules apply.

## Anomaly detection with key requests

Dynatrace assumes that low-volume requests are of less importance than high-volume and key requests. This means that requests that contribute less than 1% to the overall load of a service won't raise alerts unless their impact is significant enough that the service's overall response time or failure rate is affected. Because this default treatment is not appropriate for all low-volume requests, you should manually tag any important low-volume requests as key requests to ensure that they have standard alerting thresholds.

### Request-specific alerting thresholds

Because certain requests may have specific response-time and failure-rate patterns, while others may have strict SLA thresholds, Dynatrace enables you to define custom alerting thresholds when anomalies are detected related to the performance of key requests. If set, key-request-level thresholds override service-level thresholds. To learn how to set request-level thresholds, see [**Thresholds for a specific web request**](/docs/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-services#key-request "Learn how to adapt the sensitivity of problem detection for services.").

## Calculated service metric

As an alternative way to focus on particular requests, you can create a [calculated service metric](/docs/observe/application-observability/services/calculated-service-metric "Learn how to create a calculated metric based on web requests."), based on the requests you need. This approach provides you more flexibility with alertingâyou can use the calculated metric just like any built-in metric provided by Dynatrace.

## Manage key requests via Settings API

You can manage key request configurations via the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.").

To be able to use the API you need an access token with **Read settings** (`settings.read`) and **Write settings** (`settings.write`) scopes. To learn how to obtain it, see [Create an access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.").

### Create key request configuration

Follow the steps below to create a new key request configuration. Note that this procedure overwrites any existing configuration. If you want to modify an existing configuration, see the [**Update key request configuration**](#update-api) section below.

1. To learn the format of the settings object, query its schema via the [GET a schema](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") call. The ID of key request schema is `builtin:settings.subscriptions.service`.
2. Create the JSON object for your settings.  
   Note that the scope of a key request is always a service. You must specify the service by its Dynatrace entity ID. To find out the entity ID of your service, use the [GET entities list](/docs/dynatrace-api/environment-api/entity-v2/get-entities-list "View a list of monitored entities via Dynatrace API.") request.
   Example JSON

   ```
   [



   {



   "schemaId": "builtin:settings.subscriptions.service",



   "scope": "SERVICE-123456789",



   "value": {



   "keyRequestNames": [



   "/cart/checkout"



   ]



   }



   }



   ]
   ```
3. Use the [POST an object](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") endpoint to send your configuration.

### Update key request configuration



1. To learn the format of the settings object, query its schema via the [GET a schema](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") call. The ID of key request schema is `builtin:settings.subscriptions.service`.  
   Note that the scope of a key request is always a service. You must specify the service by its Dynatrace entity ID. To find out the entity ID of your service, use the [GET entities list](/docs/dynatrace-api/environment-api/entity-v2/get-entities-list "View a list of monitored entities via Dynatrace API.") request.
2. Query the current configuration via the [GET objects](/docs/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API.") call.
3. Create the JSON for your update.

   1. Use the **updateToken** value from the previous step.
   2. Modify the list of requests in the **keyRequestNames** array as needed.
      Example JSON

      ```
      {



      "updateToken": "vu9U3hXY3q0ATAAkMG",



      "value": {



      "keyRequestNames": [



      "/cart/checkout",



      "/cart"



      ]



      }



      }
      ```
4. Use the [PUT an object](/docs/dynatrace-api/environment-api/settings/objects/put-object "Edit a settings object via the Dynatrace API.") endpoint to send your configuration.

## Related topics

* [Service analysis timings](/docs/observe/application-observability/services-classic/service-analysis-timing "Find out what each time in service analysis means.")
* [Calculated metrics for services](/docs/observe/application-observability/services/calculated-service-metric "Learn how to create a calculated metric based on web requests.")
* [Mute monitoring of service requests](/docs/observe/application-observability/services/service-detection/service-detection-v1/service-monitoring-mute "Mute the monitoring of certain service requests so that you can focus on the performance of requests that affect your customers.")

---

## observe/application-observability/services-classic/response-time-distribution-and-outlier-analysis.md

---
title: Response time distribution and outlier analysis
source: https://www.dynatrace.com/docs/observe/application-observability/services-classic/response-time-distribution-and-outlier-analysis
scraped: 2026-02-19T21:18:29.568443
---

# Response time distribution and outlier analysis

# Response time distribution and outlier analysis

* How-to guide
* 5-min read
* Published Jul 19, 2017

To evaluate the performance of your applications, it's crucial that you have the ability to track the response time of each request within each end-to-end transaction performed by your applications. Dynatrace provides such functionality in the form of response time distribution and outlier analysis. By understanding the distribution of the response times across all requests, you can focus on those requests that have the slowest response times. Outlier response times (those requests that have either unusually high or unusually low response times) greatly affect the overall response time of transactions.

## Response time distribution

To view the **Response time** chart for a service

1. Go to ![Services Classic](https://dt-cdn.net/images/services-classic-f58502bd22.svg "Services Classic") **Services Classic**.
2. Select the service you want to analyze.
3. On the service overview page, select a **View** button (such as **View requests**, **View dynamic requests**, or **View resource requests**).
4. Select the **Response time** tab.

The **Response time** chart illustrates how the response times of the requests triggered by this service were distributed during the [selected timeframe](/docs/analyze-explore-automate/dashboards-classic/dashboards/dashboard-timeframe "Learn about Dynatrace dashboard timeframe and management zone settings.") (see the example below). This chart also shows you the average number of requests over time as well as the minimum/maximum response time of each [service instance](/docs/observe/application-observability/services-classic/analyze-individual-service-instances "Find out how you can perform a service-instance analysis."). For response time analysis, you have the option of viewing the `Median`, `Slowest 10%`, or `Slowest 5%` percentiles.

![Outlier 1](https://dt-cdn.net/images/outlier01-1650-3919f9c0c9.png)

Hold your cursor over any time interval in the chart to display time-interval controls and the specific measurements for that interval, including number of **Requests**, **Response time**, **Min/max instance response time**, and date/time.

To adjust the time scale along the X-axis, select a different time interval from the drop list beneath the chart. Or use the **+/-** buttons to zoom in/out on a timeframe. The left/right arrows enable you to step forward and backward through time intervals. These buttons are visible if you move your cursor over the chart.

![Outlier 12](https://dt-cdn.net/images/outlier12-1603-50212f1c22.png)

## Outlier analysis

To gain a deeper understanding on how response times vary across requests during the selected period, select **Analyze outliers** to navigate to the **Response time distribution** page.

Select any distribution-percentile bar to view the number of requests that fall into that response time range. As you can see in the **Top web requests** section beneath the chart, the slowest requests (the longest response times) may take dramatically longer to execute than the fastest requests. Such outliers can have a big influence on the overall response time of a service.

![Outlier 2](https://dt-cdn.net/images/outlier02-1675-11a21ba4a2.png)

You can take a closer look at the requests within each selected response time range by selecting **Zoom in**.

![Outlier 3](https://dt-cdn.net/images/outlier03-1539-4d0ab0a038.png)

The example below shows that there are about 600 requests that have response times between `70.5 ms` and `439 ms` and that the `orange.jsf` web request contributes the most to the overall response time (491 requests during the analysis timeframe).

![Outlier 4](https://dt-cdn.net/images/outlier04-1539-ca5706f5dd.png)

With a bar selected in the chart, select **Analyze backtrace** or **View service flow** to see where these requests fit within the overall transaction sequence.

The **Service flow** example below shows that the requests initiated by the `Customer Frontend service` have response times between `70 ms` and `439 ms`. The `JourneyService` contributes the most to the response time in this example. In total, this service received `585` requests.

![Outlier 5](https://dt-cdn.net/images/outlier05-1186-a4a3eca5f3.png)

Select **View response time hotspots** to view in-depth detail related to the `easyTravel Customer Frontend` requests within this response time range. This gives you code-level visibility into this response-time range. Select the section **Service execution** of the infographic to see a breakdown of the underlying service execution times. In the **Breakdown of service execution time** section, select **Code execution** to view the related **Method hotspots contributing to code execution**.

![Outlier 6](https://dt-cdn.net/images/outlier06-1601-96dbd55349.png)

## Analyze slow requests

Returning to the **Response time distribution** page, you can see that there are a few requests that have response times higher than `3.4 s`. Selecting this column in the chart reveals further detail (see below). This last selection has revealed an important insightâthere is only a single request in this response time range, with a response time of `3.77 s` (visible below in the **Top web requests** section). This single outlier has skewed the overall response time of the service. Now it's time to dig a little deeper for the root cause of this issue.

![Outlier 7](https://dt-cdn.net/images/outlier07-1535-785f5bbe88.png)

Have a look at the response time hotspot for this single request. The reason for this outlier is an RMI lookup of the `JourneyBean`.

![Outlier 8](https://dt-cdn.net/images/outlier08-1598-8d6f327ff2.png)

You can additionally have a look at the **Service flow** for this request. **Service flow** shows this entire transaction from end-to-end. It reveals that this single request resulted in no less than 93 database calls!

![Outlier 9](https://dt-cdn.net/images/outlier09-1114-a47e90c7e8.png)

As you can see, with only a few clicks, Dynatrace enables you to shed light on the fine-grained details of each request, down to the code level.

## Correlate errors with response times

Another important aspect of response time distribution is the ability to correlate failure rate with response time. Failing requests often have particularly fast or slow response times (they either fail quickly or eventually time out). The example below shows that 38% of all requests faster than `27.6 ms` are failing. A closer look at the request table reveals that these are actually two specific types of requests that always fail in this response time range. You can analyze these requests by selecting **View details of failures**.

![Outlier 10](https://dt-cdn.net/images/outlier10-1548-9fbe76f395.png)

Failure analysis shows that the requests in question all fail due to an `HTTP 500` error in the `PHP on FPM pool www` service, which can be further analyzed by selecting **Details**.

![Outlier 11](https://dt-cdn.net/images/outlier11-1237-d52e611821.png)

As you can see, outlier analysis, enabled by Dynatrace response-time distribution analysis, reveals which types of requests have the largest impact on each serviceâs overall response time. Outlier analysis also helps you understand the correlation between specific errors and response times.

## Related topics

* [Service analysis timings](/docs/observe/application-observability/services-classic/service-analysis-timing "Find out what each time in service analysis means.")
* [[Blog] Better understand response time differences over time using compare modeï»¿](https://www.dynatrace.com/news/blog/better-understand-response-time-differences-over-time-using-compare-mode/)

---

## observe/application-observability/services-classic/service-analysis-new.md

---
title: Service analysis
source: https://www.dynatrace.com/docs/observe/application-observability/services-classic/service-analysis-new
scraped: 2026-02-20T21:24:48.896069
---

# Service analysis

# Service analysis

* How-to guide
* 6-min read
* Updated on Jun 13, 2025

This topic is about the ![Services Classic](https://dt-cdn.net/images/services-classic-f58502bd22.svg "Services Classic") **Services Classic** page and is a redesign of the classic page. Check out the [![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** app](/docs/observe/application-observability/services/services-app "Maintain centralized control over service health, performance, and resources with the Services app.") for the latest experience.

All services detected by Dynatrace in your environment are displayed on the ![Services Classic](https://dt-cdn.net/images/services-classic-f58502bd22.svg "Services Classic") **Services Classic** page. You can analyze each service and drill down to code-level information.

![Services list](https://dt-cdn.net/images/services-page-1504-133c9f1b72.png)

How to get there:

1. Go to ![Services Classic](https://dt-cdn.net/images/services-classic-f58502bd22.svg "Services Classic") **Services Classic**.
2. Select a service name in the list to go to that service's overview page.

![Service overview with Unified Analysis new design](https://dt-cdn.net/images/service-overview-new-design-1768-fe1ab99c85.png)

Each **Service** page lists the most important information for that service. All relevant service metrics are shown on a single page, which is divided into several logical sections. Other panes of the service overview page show service performance and serve as entry points to deeper analysis.

## Notifications bar

The service notifications bar gives you a quick overview of the service state. Select a notification item to display more information.

### Properties and tags

Select **Properties and tags** on the notifications bar to display the **Properties and tags** panel, which displays metadata about the selected service:

* **Tags** lists tags currently applied to the service.  
  Select **Add Tag** to add a tag to the service metadata.
* **Properties** lists various service properties, such as application name, service type, technologies, and management zones.

### Problems

* On the notifications bar, **Problems** indicates active and closed problems related to the selected service.
* Select **Problems** on the notifications bar to display the **Problems** panel, which lists the problems.

  + Select a problem to display details.
  + Select **Go to problems** to go to the [Problems](/docs/dynatrace-intelligence "Get familiar with the capabilities of Dynatrace Intelligence.") page filtered by the selected service.

### SLOs

* On the notifications bar, **SLOs** indicates the current number of [SLOs](/docs/deliver/service-level-objectives-classic "Monitor and alert on service-level objectives with Dynatrace in Service-Level Objectives Classic.") related to the selected service.
* Select **SLOs** on the notifications bar to display the **Service-level objectives** panel, which lists SLOs that are directly or indirectly connected to the service.

#### Directly connected SLOs

* An SLO is directly connected to a service when the [entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.") of an SLO meets the following criteria:

  + The entity type is set to `"SERVICE"`.
  + The entity ID is set to the service ID.
* To see only SLOs that are directly connected to the service, make sure that **Show only directly connected SLOs** is turned on.

#### Indirectly connected SLOs

* An SLO isn't directly connected to a service when, in the [entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.") of an SLO, no entity ID is provided.

  Example: When generic values, such as `type("SERVICE"),tag("slo")` are provided, the query results in all SLOs for all services, including the current service.
* To see SLOs that are not directly connected to the service, turn off **Show only directly connected SLOs**.

#### Options

* Expand **Details** to view a chart of the respective SLO metrics.
* In **Actions**, select

  + **View in Data Explorer** to [see SLO metrics in Data Explorer](/docs/deliver/service-level-objectives-classic/configure-and-monitor-slo#explorer "Create, configure, and monitor service-level objectives with Dynatrace.").
  + **Pin to Dashboard** to [pin the SLO to your dashboard](/docs/deliver/service-level-objectives-classic/configure-and-monitor-slo#dash "Create, configure, and monitor service-level objectives with Dynatrace.").
  + **SLO definition** to edit the SLO in **Service-level objective definitions**.
  + **Clone** to [clone the SLO](/docs/deliver/service-level-objectives-classic/configure-and-monitor-slo#clone "Create, configure, and monitor service-level objectives with Dynatrace.").
  + **Create alert** to [create an alert for the SLO](/docs/deliver/service-level-objectives-classic/configure-and-monitor-slo#alerts "Create, configure, and monitor service-level objectives with Dynatrace.").

#### No SLOs

If no SLOs are found, you can

* Select a different timeframe in the upper-right corner.

  ![Timeframe selector: menu bar](https://dt-cdn.net/images/timeframe-selector-menu-bar-264-8193110c8c.png)
* Select **Add SLO** to create an SLO in the [SLO wizard](/docs/deliver/service-level-objectives-classic/configure-and-monitor-slo#wizard "Create, configure, and monitor service-level objectives with Dynatrace.").

### Owners

Select **Owners** on the notifications bar to display the **Ownership** panel, which lists [owners](/docs/deliver/ownership "Map team ownership to monitored entities for better collaboration, task assignment, incident and vulnerability response, and service-level management.") of the selected service.

* Select  to learn more about a current ownership.
* To add an ownership, select **Add a new Ownership tag**.

## Performance

### Service overview

You can configure the **Service overview** card to focus on various metrics of the service performance.

* In the **Service overview**, you can

  + See the service in Smartscape by selecting **Smartscape view** .
  + Analyze **Response time hotspots**, **Details of failures**, and method hotspots.
  + Compare service request performance indicators, such us response time, failures, CPU, and load, based on different timeframes.
* For each metric, you can select **More** (**â¦**) and

  + Analyze the metric in Data Explorer.
  + Create a metric event.
  + Pin the metric to a classic dashboard. For details, see [Pin tiles to your dashboard](/docs/analyze-explore-automate/dashboards-classic/charts-and-tiles/pin-tiles-to-your-dashboard "Learn to pin tiles to your dashboards.").

### Endpoints

Unified service

The **Endpoints** card offers an overview of the monitored service endpoints.

* To analyze an endpoint metrics, in the **Details** column select .
* To analyze an endpoint distributed traces, in the **Actions** column select **More** (**â¦**) > **View distributed traces**.

Data availability depends on endpoint metrics, which consume DDUs. To get started on endpoint monitoring, see [Manage endpoint monitoring](/docs/observe/application-observability/services/service-detection/service-detection-v1/service-types/unified-service#endpoint-monitoring "Define services on observability signals ingested via Trace ingest APIs.").

### Service mesh metrics

Unified service

If a service mesh is detected in your application, service mesh metrics are displayed for the related service. [ISTIO logs and metrics](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-istio-metrics "Istio metric ingestion and topology detection") are enriched with service mesh ID, putting data into context. Note that service mesh metrics are created from ingested service mesh traces.

### Key requests

The **Key requests** card offers an overview of the key requests found for the service in the selected timeframe. You can quickly access analysis for other requests related to the services such as:

* [**View all requests**](/docs/observe/application-observability/services-classic#charts "Learn about Dynatrace's classic service monitoring")
* [**Top web requests**](/docs/observe/application-observability/multidimensional-analysis/top-web-requests "Learn how to analyze all web requests across all of your services using Dynatrace.")
* [**View outliers**](/docs/observe/application-observability/services-classic/response-time-distribution-and-outlier-analysis#outlier-analysis "Gain insights into the distribution of response times across all requests, including those that are either unusually high or unusually low.")

### Topology



In the **Topology** card, you can learn

* Which services are calling and which are called by the service.  
  Select **Related services** to understand the service relation. Expand **Details** to view a chart of the respective service metrics. You can quickly access further analysis options such as [**View backtrace**](/docs/observe/application-observability/services-classic/service-backtrace "Trace the sequence of service calls all the way back up to the browser click that triggered the sequence of calls.") and [**Service flow**](/docs/observe/application-observability/services-classic/service-flow "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment.").
* On which processes and hosts the service is running on.  
  Expand **Details** to view a chart of the respective process metrics. Select the name of the process to analyze it deeper.
* Which HTTP monitors and (mobile) applications are calling the service.  
  Select the name of a calling entity to analyze it deeper.

![Topology - Service overview](https://dt-cdn.net/images/topology-services-2886-fc9dda7f82.png)

### Distributed traces

The **Distributed traces** card provides an overview of the most recent traces, depending on the selected timeframe. Select **Full search** to directly access the [distributed traces overview for the service](/docs/observe/application-observability/distributed-traces/analysis/get-started "Get started with distributed trace analysis in Dynatrace.").

### Events

Contains a list of [events](/docs/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation "Gain an understanding of the Events section on each host, process, and service overview page.") that affect the service in the current timeframe.

### Related logs

Contains a list of [logs](/docs/analyze-explore-automate/logs "Log Management and Analytics provides a unified approach to controlling and studying your log data in Dynatrace.") related to the service in the current timeframe.

* To analyze all the logs for the related service, select **Go to logs** .
* To analyze a specific log, expand **Details**. If a trace or a user session is found for the log line, you can directly access it from this view.

## Related topics

* [Unified analysis pages](/docs/ingest-from/extend-dynatrace/extend-ui/unified-analysis "Extend the Dynatrace web UI using entity-tailored unified analysis pages.")

---

## observe/application-observability/services-classic/service-analysis-timing.md

---
title: Service analysis timings
source: https://www.dynatrace.com/docs/observe/application-observability/services-classic/service-analysis-timing
scraped: 2026-02-20T21:08:17.989711
---

# Service analysis timings

# Service analysis timings

* Reference
* 5-min read
* Updated on Jul 24, 2023

Service analysis operates with many different timings, describing the behavior of the service. The table below provides an overview of such timings. Timings vary in different analysis types:

* DT: [Distributed traces](/docs/observe/application-observability/distributed-traces/use-cases/segment-request#pp-code-level-tab "Enhance your distributed system performance by segmenting requests with slow response time via Service flow and analyzing their distributed traces.").
* RT: [Response time](/docs/observe/application-observability/services-classic/service-response-time-hotspots "Identify the activities that consume the most response time for each service.").
* SF: [Service flow](/docs/observe/application-observability/services-classic/service-flow "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment.").
* MH: [Method hotspots](/docs/observe/application-observability/services-classic/service-response-time-hotspots "Identify the activities that consume the most response time for each service.").

Regardless of which analysis you're running, it is not guaranteed that you'll see all of the timings listed here. The actual timings you see depend completely on how you're running your services. For example, if the distributed trace runs completely on one host without any networking involved, you won't see any network-related times.

Time

Appears in

Description

Response time

DT  
SF

The total execution time of the first node of a distributed trace.

* Server side The time between moments when the distributed trace is started on the server side and when the response is sent back to the client.
* Client side The time between moments when the client triggers the request and receives the response.

Response time

RT

The total execution time of the method.

* Server side The processing time of the method.
* Client side The time between moments when the client triggers the request and receives the response.

Processing time

DT  
RT

The duration of the distributed trace from start to end.

It is the *wall-clock time* (difference between start and end time), not the sum of all asynchronous executions.

Execution time

RT

The total time taken to execute the code.

It is the **sum of all asynchronous executions**, so it might be longer than the processing time.

Suspension

DT  
RT

The time during which any code execution is halted. It is usually caused by garbage collection.

Wait time

DT

The time during which the code actively waits for something (for example, `Object.wait()` or a similar functionality).

Lock wait

RT

The time during which the code is blocked. It usually caused by wait time prior to entry into a synchronized code block or by wait time to acquire a spinlock.

Active wait

RT

The time during which the code in *this node* is waiting for something. The wait caused by child calls is not included.

Lock time

DT

The time during which the code is blocked by waiting for a synchronous code block.

Network I/O

DT  
RT

The time during which the code is actively waiting for *native* network functions (for example, `java.net.SocketInputStream.socketRead0`).

For response time analysis, the wait caused by child calls is not included.

Disk I/O

DT  
RT

The time during which the code is actively reading from or writing to a disk or waiting for disk input/output.

For response time analysis, the wait caused by child calls is not included.

Total I/O

-

In a node, this is **the sum of Network I/O and Disk I/O**.

When these metrics aren't available, and if the node is the direct parent of a synchronously invoked child service that isn't a custom service, the node Total I/O can be estimated as **the node Duration minus the node CPU Self time**.

CPU time

DT  
RT

The time during which the CPU executes code related to the distributed trace. The measurement is provided by OneAgent.

Self time

DT  
RT

The processing time of a particular node in the distributed trace.

Other

DT

Any unclassified fraction of the self time.

Elapsed time

DT

The time between executions, from when the distributed trace is created to when the method enters.

Duration

DT

Timeframe that represents the duration of a node, including its synchronous children nodes, from its start time to its end time.

Code execution

MH

Percentage of measured samples in which the method code is actively executed.

Disk I/O

MH

Percentage of measured samples in which the method is actively reading from or writing to a disk or waiting for disk input/output.

Network I/O

MH

Percentage of measured samples in which the method is actively waiting for *native* network functions.

Waiting

MH

Percentage of measured samples in which the method is actively waiting for something (for example, `Object.wait()` or a similar functionality).

Locking

MH

Percentage of measured samples in which the method is blocked by waiting for a synchronous code block.

## Related topics

* [Distributed Traces Classic](/docs/observe/application-observability/distributed-traces "Gain observability into highly distributed, cloud-native architectures to effectively trace and analyze transactions in real time.")
* [Service flow](/docs/observe/application-observability/services-classic/service-flow "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment.")
* [Multidimensional analysis](/docs/observe/application-observability/multidimensional-analysis "Configure a multidimensional analysis view and save it as a calculated metric.")

---

## observe/application-observability/services-classic/service-backtrace.md

---
title: Service backtrace
source: https://www.dynatrace.com/docs/observe/application-observability/services-classic/service-backtrace
scraped: 2026-02-19T21:14:50.638230
---

# Service backtrace

# Service backtrace

* How-to guide
* 4-min read
* Published Jul 19, 2017

More than just knowing which service directly calls one of your services, it's helpful to know the sequence of service calls that leads up to each requestâall the way back up to the browser click that triggered the sequence of calls. Dynatrace **Service-level backtrace** can show you such call sequences.

Say for example that youâre analyzing a SQL database service and you want to understand the sequence of preceding service requests that ultimately triggered the incoming requests to the SQL service. With service-level backtrace you might learn that, for example, the SQL database service is called by `Service1`, while `Service1` is called by `Service2`, which in turn was triggered by a click on a login button.

To view service-level backtrace

1. Go to ![Services Classic](https://dt-cdn.net/images/services-classic-f58502bd22.svg "Services Classic") **Services Classic**.
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

---

## observe/application-observability/services-classic/service-flow/service-flow-filtering.md

---
title: Service flow filtering
source: https://www.dynatrace.com/docs/observe/application-observability/services-classic/service-flow/service-flow-filtering
scraped: 2026-02-19T21:18:20.777374
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

---

## observe/application-observability/services-classic/service-flow.md

---
title: Service flow
source: https://www.dynatrace.com/docs/observe/application-observability/services-classic/service-flow
scraped: 2026-02-19T21:15:04.470403
---

# Service flow

# Service flow

* How-to guide
* 2-min read
* Published Jul 19, 2017

Dynatrace understands your applicationsâ transactions from end to end. This transactional insight is visualized through **Service flow**, which illustrates the sequence of service calls that are triggered by each service request in your environment. Within a service flow, you see the flow of service calls from the perspective of a single service, request or their filtered subset. Along with the specific services that are triggered, you can also see how each component of a request contributes to the overall response time.

To view the service flow triggered by a specific service

1. Go to ![Services Classic](https://dt-cdn.net/images/services-classic-f58502bd22.svg "Services Classic") **Services Classic**.
2. Select the service you want to analyze.
3. On the service overview page, under **Understand dependencies**, select **View service flow**.

The image below shows the service flow triggered by the `EasyTravelWebServer` service, as well as how each initiated service contributes to the overall response time. The `EasyTravelWebServer` service calls a Tomcat service. The Tomcat service in turn calls two other services, which call two more services. What becomes immediately apparent is that the `Credit Card Verification` service contributes the most to overall response time, although its caller, `BookingService`, is only called by `27%` of the requests. This degree of analysis enables you to understand the larger complexities within your system.

![Serviceflow 1](https://dt-cdn.net/images/serviceflow1-1537-0535d3964f.png)

**Service flow** offers insights on the sequence of service-call chains across services. To understand the execution order of service calls relative to one another, use **Service backtrace** instead.

Service flows can become highly complex. For improved readability of service-flow data, Dynatrace aggregates services that contribute little to overall response time. Aggregated services have names like `2 services` and `4 instances`. Notice the aggregate named `4 services` in the middle column below. Select this to see which services are aggregated here. When you select one of the aggregated services, **Service flow** displays the requests path of the selected service.

Aggregations are calculated dynamically based on the size of your browser window. You can use your browser's zoom in/out feature to make more space available.

![Serviceflow 2](https://dt-cdn.net/images/serviceflow2-1910-d07d5c5e14.png)

As you can see in the example above, some of the services in the above service flow appear multiple times (`easyTravel Customer Frontend` and `EasyTravelWebserver`). This is because these services were called at multiple points during the flow of this transaction. Each call performs different actions and contributes different amounts to the overall response time. Dynatrace doesnât aggregate these varying circumstances into a single metric because individually they are significant and provide valuable insight into whatâs going on at a deep level in your environment.

---

## observe/application-observability/services-classic/service-response-time-hotspots.md

---
title: Service response time hotspots
source: https://www.dynatrace.com/docs/observe/application-observability/services-classic/service-response-time-hotspots
scraped: 2026-02-19T21:16:55.784384
---

# Service response time hotspots

# Service response time hotspots

* How-to guide
* 5-min read
* Published Jul 19, 2017

With deep process monitoring enabled, Dynatrace analyzes the response time of each service running within each process. This is applicable to Java, .NET, Node.js, PHP, Apache webserver, IIS, NGINX, and other technologies.

Response time hotspots indicate which activities consume the most time for a specific service. Each **Service** page offers an overview of related response-time hotspots under **Current hotspot** and includes:

* Top findings, such as requests with slow response time, high failure rate, or high CPU consumption.
* Requests with high consumption of request resources. The percentage shows the share of the request in the overall response time of the service. In the example below, `85%` of the response time of `JourneyService` is spent executing the `findJourneys` request.

![Hotspots 0](https://dt-cdn.net/images/hotspots0-1309-9b8dfdbea1.png)

To view the hotspot analysis

1. Go to ![Services Classic](https://dt-cdn.net/images/services-classic-f58502bd22.svg "Services Classic") **Services Classic**.
2. Select the service you want to analyze.
3. Do one of the following:

   * To analyze a hotspot top finding, select the finding in the **Current hotspots** to display the details of the service, filtered to the problematic request.
   * To analyze all response time hotspots of the service, on the service overview page, choose either the **View requests**, **View dynamic requests**, or **View resource requests**) option. Dynatrace will display the overall details of the service.
4. Select **View response time hotspots** to navigate to the **Response time analysis** page.

![Hotspots 1](https://dt-cdn.net/images/hotspots1-1309-752c2e2bd8.png)

On the **Response time analysis** page you see the average response time observed during the analyzed timeframe. On the left side of the infographic, under **Distribution**, you can see how much time is contributed by calls to other services, calls to databases, and code-level execution. On the right side, under **Top findings**, we list the biggest hotspots identified by Dynatrace. You can select any of these entries to view further details.

## Calls to other services

Select **Interaction with services and queues** to display details regarding how these calls contribute to the overall response time.

![Hotspots 2](https://dt-cdn.net/images/hotspots2-1889-e6dec0cd21.png)

On the left side you see how often the analyzed service calls other services and to what extent these calls contribute to the response time. On the right side, this information is broken down into more detail. In the example above, you see that most of the time is contributed by the `Easytravel Customer Frontend` service. Select the service name to view the next step in the hierarchy. Once you reach the lowest level (the request level) you see full response-time details for the selected request.

![Hotspots 3](https://dt-cdn.net/images/hotspots3-1887-d7ea5fdd55.png)

In the example above, we see that `EasytravelWebserver:8079` calls the URL `/orange.jsf` on `easytravel Customer Frontend` in only 7.46% of the overall requests it initiatesâexactly once each time. We see that the response time of `/orange.jsf` is `255 ms` on average. However, because this is called only rarely, it contributes only `19 ms` to the average response time of `EasytravelWebserver:8079`.

If you select the arrow button on the left boundary of the **Interaction with services and queues** section, you can again move upwards in the hierarchy.

## Database requests

Select the **Database usage** portion of the infographic to access details about the database requests of the analyzed service and to see how they contribute to the response time. The top section offers the same navigation and information offered by the **Interaction with services and queues** section. Beneath this you can view all database requests.

![Hotspots 4](https://dt-cdn.net/images/hotspots4-1252-be6d5ddef6.png)

By selecting the list box in the top right corner, you can sort database statements by **average execution time**, **percentage of calls**, **invocations**, and **contribution**. By default, the statements that contribute the most to response time are included at the top of the list. Select a SQL statement to view the values for these four attributes.

![Hotspots 5](https://dt-cdn.net/images/hotspots5-1228-0f1d8e37b5.png)

## Code-level visibility

Select **Service execution** to view how much time the service spent executing its own code.

![Service execution time](https://dt-cdn.net/images/service-execution-time-1445-780d85d724.png)

The lengths of the bars represent the amount of time spent in each particular area. The dark blue color represents CPU time. Select any row name that's rendered as a link to view the related method-level hotspots.

![Code-level visibility](https://dt-cdn.net/images/hotspots-1446-6c931f44ae.png)

Select the **View method hotspots** button and check all the classes and methods that were executed to run the service under the **Call tree** section. The **Stacktrace samples** column shows how many times the class/method was executed for the service during the selected timeframe. The **Contribution** column shows the share of consumption that the class/method contributes to the overall execution. This allows you to identify which class and/or method is consuming most of the execution time and subsequently optimize the code.

### Download code

Prerequisites

Ensure you have the **View sensitive request data** [permission](/docs/manage/identity-access-management/permission-management/role-based-permissions "Role-based permissions") in your environment.

Limitations

Downloading the code is supported for Java, .NET, and Node.js.

To download the code for an execution,

1. Go to **Actions** and select  > **Source code**.
2. Choose the process from which you want to download the code.
3. Select **Download** for the execution you're interested in.
4. Open the source code.

   Node.js

   Java

   .NET

   The source code is directly visible in Dynatrace.

   Required To convert the code into source code, use an external decompiler, such as [Bytecode Viewerï»¿](https://bytecodeviewer.com).

   Choose the decompiler most suited to the specific Java version youâre working with.

   Required To convert the code into source code, use an external decompiler, such as [dotPeakï»¿](https://www.jetbrains.com/decompiler/).

   Choose the decompiler most suited to the specific .NET version youâre working with.

## Automatic Hotspots

The **Top findings** section of the **Response time** analysis infographic lists the hotspots that are the key contributors to the analyzed request.

If a request is slow, you'll see the underlying cause listed under **Top findings**. Select a finding to view further details. In this example you can see that 226 ms out of 639 ms were spent in a call to `PaymentLogic.DoPay`!

![Hotspots 7](https://dt-cdn.net/images/hotspots7-1254-e581fe35b2.png)

## Response time distribution

Select the circular **Response time** portion of the infographic to open a chart that shows the response time distribution of all analyzed requests. This shows you if your service has a range of response times or if it performs uniformly.

![Hotspots 8](https://dt-cdn.net/images/hotspots8-1248-286099cfc1.png)

Typically, web-request services have a wide range of response times. Analyzing a single request often shows a more uniform picture.

## Related topics

* [Service analysis timings](/docs/observe/application-observability/services-classic/service-analysis-timing "Find out what each time in service analysis means.")

---

## observe/application-observability/services-classic.md

---
title: Services Classic
source: https://www.dynatrace.com/docs/observe/application-observability/services-classic
scraped: 2026-02-18T21:23:34.542425
---

# Services Classic

# Services Classic

* Overview
* 4-min read
* Updated on Jun 12, 2025

The **Services** page is an overview page displaying all services that Dynatrace has detected in your environment.

Use the guides and references below to gain more insight about monitoring and analyzing these services.

[#### Service analysis

Learn about all the service monitoring details that Dynatrace can provide.

* How-to guide

Read this guide](/docs/observe/application-observability/services-classic/service-analysis-new)[#### Context-specific drill-down

Learn about easy navigation and filtering for services analysis.

* Reference

Read this reference](/docs/observe/application-observability/services-classic/context-specific-drill-down)[#### Analyze individual service instances

Find out how you can perform a service-instance analysis.

* How-to guide

Read this guide](/docs/observe/application-observability/services-classic/analyze-individual-service-instances)[#### Service analysis timings

Find out what each time in service analysis means.

* Reference

Read this reference](/docs/observe/application-observability/services-classic/service-analysis-timing)[#### Response time distribution and outlier analysis

Gain insights into the distribution of response times across all requests, including those that are either unusually high or unusually low.

* How-to guide

Read this guide](/docs/observe/application-observability/services-classic/response-time-distribution-and-outlier-analysis)[#### Service response time hotspots

Identify the activities that consume the most response time for each service.

* How-to guide

Read this guide](/docs/observe/application-observability/services-classic/service-response-time-hotspots)[#### Service flow

Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment.

* How-to guide

Read this guide](/docs/observe/application-observability/services-classic/service-flow)[#### Monitor key requests

Discover how to closely monitor requests that are critical to your business.

* How-to guide

Read this guide](/docs/observe/application-observability/services-classic/monitor-key-requests)[#### Service backtrace

Trace the sequence of service calls all the way back up to the browser click that triggered the sequence of calls.

* How-to guide

Read this guide](/docs/observe/application-observability/services-classic/service-backtrace)

---

## observe/application-observability/services.md

---
title: Services
source: https://www.dynatrace.com/docs/observe/application-observability/services
scraped: 2026-02-20T21:07:50.245812
---

# Services

# Services

* Latest Dynatrace
* Overview
* 4-min read
* Updated on Oct 23, 2025

Services are an application's fundamental building blocks. From an observability standpoint, they provide application owners with critical metrics to monitor application health.

[![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**](/docs/observe/application-observability/services/services-app "Maintain centralized control over service health, performance, and resources with the Services app.") provides detailed insights into the performance and health of your services and includes useful features like [Service flow](/docs/observe/application-observability/services-classic/service-flow "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment.") and [Backtrace](/docs/observe/application-observability/services-classic/service-backtrace "Trace the sequence of service calls all the way back up to the browser click that triggered the sequence of calls.").

## Prerequisites

### Permissions

Check the minimal set of permissions required to run ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**.

Permission

Description

storage:events:read

Query events from GRAIL

storage:entities:read

Query entities from GRAIL

storage:logs:read

Query logs from GRAIL

storage:spans:read

Read span data

storage:metrics:read

Query metrics from GRAIL

storage:buckets:read

Read buckets

storage:smartscape:read

Read smartscape nodes and edges

hub:catalog:read

Read release details

storage:fieldsets:read

Read fieldsets from GRAIL

storage:filter-segments:read

Read filter-segments

10

rows per page

Page

1

of 1

### Installation

Make sure ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** is [installed in your environment](/docs/manage/hub#install "See the information about Dynatrace Hub.").

## Get started

![View the real-time performance of all your services. Locate specific services using powerful filters.](https://cdn.hub.central.dynatrace.com/hub/1_DI39YNS_hQ7gBgG.png)![Analyze database queries executed by your services to discover which operations consume the most resources.](https://cdn.hub.central.dynatrace.com/hub/2_previously_5_7LmaiBa.png)![Use Dynatrace Intelligence's automated root cause analysis to quickly surface and pinpoint the source of issues in your application services, accelerating analysis.](https://cdn.hub.central.dynatrace.com/hub/3_lHZzEjb_zyT76Yj.png)![Failure analysis comparing timeframes.](https://cdn.hub.central.dynatrace.com/hub/failure-analysis-1990-6b9d85e513_38quxQP.png)

1 of 4View the real-time performance of all your services. Locate specific services using powerful filters.

In Dynatrace, go to ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** to launch the app.

![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** provides detailed insights into the performance and health of your services. Use it to perform failure analysis, response times, query performance, and message processing. You can also utilize this app to filter by key attributes, for example, Kubernetes namespaces or HTTP endpoints, and examine relationships to Kubernetes, host, and cloud infrastructure. Moreover, you can view logs emitted by your services and jump directly to [![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**](/docs/observe/application-observability/distributed-tracing/distributed-tracing-app "Discover the functionalities of the new Distributed Tracing app.") for deeper analysis of specific transactions.

For more information, see [Services app](/docs/observe/application-observability/services/services-app "Maintain centralized control over service health, performance, and resources with the Services app.").

## Add services to Dynatrace

Add services to Dynatrace using OneAgent or OpenTelemetry integration.

Both options capture metrics, traces, and logs and include support for Serverless functions.

Choose one of the following options to learn more:

Cloud Workload

#### AWS

[AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration) [AWS Fargate](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate) [Amazon EC2](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-ec2) [Amazon ECS](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-ecs) [Amazon EKS](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-eks) [AWS App Runner](/docs/ingest-from/amazon-web-services/integrate-into-aws/app-runner) [AWS Elastic Beanstalk](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-beanstalk) [All AWS cloud services](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services) 

#### Microsoft Azure

[Azure Monitor metrics](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide) [Azure Logs](/docs/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure) [Azure Kubernetes Service (AKS)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-aks) [Azure App Service](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice) [Azure Functions](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions) [Azure Virtual Machines (VM)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-vm) [Azure Virtual Machine Scale Set (VMSS)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-vmss) [Azure Service Fabric](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-servicefabric) [Azure Spring Apps](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-spring) [All Azure cloud services](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics) 

#### Google Cloud

[![Google Cloud Run (managed)](https://cdn.bfldr.com/B686QPH3/at/7mr6q4h3nv5qjvgccbqm8x5/DT0184.svg?auto=webp&width=72&height=72 "Google Cloud Run (managed)")Google Cloud Run (managed)](/docs/ingest-from/google-cloud-platform/gcp-integrations/cloudrun) [![Google Cloud Functions](https://cdn.bfldr.com/B686QPH3/at/rc58vncw7jkjs8pf5m4wk8p/DT0172.svg?auto=webp&width=72&height=72 "Google Cloud Functions")Google Cloud Functions](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions) [![Google Cloud App Engine](https://cdn.bfldr.com/B686QPH3/at/cs4628s93tzgrqp5vbqvf2x/DT0059.svg?auto=webp&width=72&height=72 "Google Cloud App Engine")Google App Engine](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-app-engine) [![Google Compute Engine](https://cdn.bfldr.com/B686QPH3/at/9qpgp4rfnnc556gbwgc32fs4/DT0220.svg?auto=webp&width=72&height=72 "Google Compute Engine")Google Compute Engine](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-compute-engine) [![Google Kubernetes Engine](https://cdn.bfldr.com/B686QPH3/at/sz8sx4wfhjf3bsb5m6sbj4k/DT0166.svg?auto=webp&width=72&height=72 "Google Kubernetes Engine")Google Kubernetes Engine (GKE)](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-gke) [All Google Cloud services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new)

Kubernetes

[Kubernetes cluster](/docs/ingest-from/setup-on-k8s/deployment) [Envoy](/docs/ingest-from/opentelemetry/integrations/envoy) [Istio](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/istio-deployment)

Host-based

[AIX](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix) [Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux) [Solaris](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/solaris) [Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows) [zOS](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos) 

[Amazon EC2](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-ec2) [Azure Virtual Machines (VM)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-vm) [![Google Compute Engine](https://cdn.bfldr.com/B686QPH3/at/9qpgp4rfnnc556gbwgc32fs4/DT0220.svg?auto=webp&width=72&height=72 "Google Compute Engine")Google Compute Engine](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-compute-engine)

OpenTelemetry

[OpenTelemetry](/docs/ingest-from/opentelemetry)

Other setup options

[Graal VM Native Image](/docs/ingest-from/technology-support/application-software/java/graalvm-native-image) [GitOps](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/using-gitops) [Docker](/docs/ingest-from/setup-on-container-platforms/docker) [Heroku](/docs/ingest-from/setup-on-container-platforms/heroku) [Ingest data in Dynatrace](/docs/ingest-from)

[#### Service flow

Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment.

* How-to guide

Read this guide](/docs/observe/application-observability/services-classic/service-flow)[#### Service backtrace

Trace the sequence of service calls all the way back up to the browser click that triggered the sequence of calls.

* How-to guide

Read this guide](/docs/observe/application-observability/services-classic/service-backtrace)

## Related topics



* [Service flow](/docs/observe/application-observability/services-classic/service-flow "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment.")
* [Distributed Traces Classic](/docs/observe/application-observability/distributed-traces "Gain observability into highly distributed, cloud-native architectures to effectively trace and analyze transactions in real time.")

---

## observe/application-observability.md

---
title: Application Observability
source: https://www.dynatrace.com/docs/observe/application-observability
scraped: 2026-02-20T21:08:44.473989
---

# Application Observability

# Application Observability

* Latest Dynatrace
* Overview
* 1-min read
* Published Feb 06, 2023

[![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing")

#### Distributed Tracing

Trace and analyze in real time highly distributed systems with Grail.

* App

Explore this app](/docs/observe/application-observability/distributed-tracing)[![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger")

#### Live Debugger

Get familiar with the Live Debugger capabilities in Dynatrace.

* App

Explore this app](/docs/observe/application-observability/live-debugger)[![Services](https://dt-cdn.net/hub/logos/services.png "Services")

#### Services

Learn how to monitor and analyze your services, define and use request attributes, and more.

* Overview

See the overview](/docs/observe/application-observability/services)

## Classic

[#### Distributed Traces Classic

Gain observability into highly distributed, cloud-native architectures to effectively trace and analyze transactions in real time.

* Overview

See the overview](/docs/observe/application-observability/distributed-traces)[#### Multidimensional analysis

Configure a multidimensional analysis view and save it as a calculated metric.

* How-to guide

Read this guide](/docs/observe/application-observability/multidimensional-analysis)[#### Profiling and optimization

Learn how to use Dynatrace diagnostic tools for crash analysis, memory dump analysis, and more.

* Overview

See the overview](/docs/observe/application-observability/profiling-and-optimization)[#### Services Classic

Learn about Dynatrace's classic service monitoring

* Overview

See the overview](/docs/observe/application-observability/services-classic)

## See also

[![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs")

### Log Management and Analytics

Log Management and Analytics provides a unified approach to controlling and studying your log data in Dynatrace.](/docs/analyze-explore-automate/logs "Log Management and Analytics provides a unified approach to controlling and studying your log data in Dynatrace.")[![Digital Experience](https://cdn.bfldr.com/B686QPH3/at/24vb99tkw5wm7xrvxpshcbvr/Digital_Experience.svg?auto=webp&width=72&height=72 "Digital Experience")

### Digital Experience

Use RUM and Synthetic Monitoring for total Digital Experience Monitoring.](/docs/observe/digital-experience "Optimize end-user experience with Digital Experience Monitoring to ensure application performance and availability across all channels.")

---
