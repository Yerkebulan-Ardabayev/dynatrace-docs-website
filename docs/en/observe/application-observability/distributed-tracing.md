---
title: Distributed Tracing
source: https://www.dynatrace.com/docs/observe/application-observability/distributed-tracing
scraped: 2026-02-16T09:12:15.958524
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