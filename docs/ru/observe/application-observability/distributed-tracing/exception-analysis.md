---
title: Exception analysis
source: https://www.dynatrace.com/docs/observe/application-observability/distributed-tracing/exception-analysis
scraped: 2026-02-18T21:16:01.013808
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