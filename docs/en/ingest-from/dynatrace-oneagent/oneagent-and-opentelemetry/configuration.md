---
title: Enable the OpenTelemetry Span Sensor for OneAgent
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration
scraped: 2026-02-24T21:34:16.304175
---

# Enable the OpenTelemetry Span Sensor for OneAgent

# Enable the OpenTelemetry Span Sensor for OneAgent

* Latest Dynatrace
* How-to guide
* 5-min read
* Updated on Feb 09, 2026

In addition to the application-side configuration, several Dynatrace-specific settings let you control how OpenTelemetry data is used in Dynatrace.

To learn how to send OpenTelemetry data to a Dynatrace OneAgent, see [Use OneAgent with OpenTelemetry data](/docs/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/oneagent-otel "Learn how to send OpenTelemetry data to a Dynatrace OneAgent.").

## Prerequisites

Java

Go

Node.js

PHP

.NET and .NET Core

.NET Framework

Python

| Monitoring framework | Versions |
| --- | --- |
| [OpenTelemetryï»¿](https://github.com/open-telemetry/opentelemetry-java/) | 1.0 - 1.3[1](#fn-monitoring-framework-1-def), 1.4 - 1.54[1](#fn-monitoring-framework-1-def) |
| [OpenTracingï»¿](https://opentracing.io/guides/java/) | 0.33, 0.32, 0.31 |

1

Supported in [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options").

To enable OpenTelemetry Java

1. Go to the appropriate configuration page:

   * In Latest Dynatrace, go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **General monitoring settings** > **OneAgent features**.
   * In Dynatrace Classic, go to **Settings** > **Preferences** > **OneAgent network modules & integrations**

2. Find and enable **OpenTelemetry (Java)**.

Existing tracers are replaced and will no longer work after you enable OpenTelemetry Java.

| Monitoring framework | Versions |
| --- | --- |
| [OpenTelemetryï»¿](https://github.com/open-telemetry/opentelemetry-go/) | 1.0 - 1.7, 1.8 - 1.11.0, 1.11.1 - 1.27, 1.28 - 1.40 |

Opt-in

To enable OpenTelemetry Go

1. Go to the appropriate configuration page:

   * In Latest Dynatrace, go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **General monitoring settings** > **OneAgent features**.
   * In Dynatrace Classic, go to **Settings** > **Preferences** > **OneAgent network modules & integrations**

2. Find and enable **OpenTelemetry (Go) [Opt-In]**.

Existing tracers are not affected by OneAgent OpenTelemetry for Go support.

OneAgent version 1.217 and earlier The OpenTelemetry Go Sensor propagates Dynatrace context across processes only if **Send W3C Trace Context HTTP headers** is enabled:

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **General monitoring settings** > **OneAgent features**.
2. Turn on **Send W3C trace context HTTP headers**.

| Monitoring framework | Versions |
| --- | --- |
| [OpenTelemetryï»¿](https://www.npmjs.com/package/@opentelemetry/api) | 1[1](#fn-monitoring-framework-1-def) |

1

Supported in [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options")

Opt-in

To enable OpenTelemetry Node.js:

1. Go to the appropriate configuration page:

   * In Latest Dynatrace, go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **General monitoring settings** > **OneAgent features**.
   * In Dynatrace Classic, go to **Settings** > **Preferences** > **OneAgent network modules & integrations**

1. Find and enable **OpenTelemetry (Node.js) [Opt-In]**.

| Monitoring framework | Versions |
| --- | --- |
| [OpenTelemetryï»¿](https://github.com/open-telemetry/opentelemetry-php) | 1.0.0 |

Opt-in

To enable OpenTelemetry PHP:

1. Go to the appropriate configuration page:

   * In Latest Dynatrace, go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **General monitoring settings** > **OneAgent features**.
   * In Dynatrace Classic, go to **Settings** > **Preferences** > **OneAgent network modules & integrations**

2. Find and enable **OpenTelemetry (PHP) [Opt-In]**.

Existing tracers are not affected by OneAgent OpenTelemetry for PHP support.

| Monitoring framework | Versions |
| --- | --- |
| [OpenTelemetryï»¿](https://github.com/open-telemetry/opentelemetry-dotnet) | 1.0.1+, 1.1+ |

Opt-in

To enable OpenTelemetry .NET and .NET Core:

1. Go to the appropriate configuration page:

   * In Latest Dynatrace, go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **General monitoring settings** > **OneAgent features**.
   * In Dynatrace Classic, go to **Settings** > **Preferences** > **OneAgent network modules & integrations**

2. Find and enable **OpenTelemetry (.NET) [Opt-In]**.

Existing tracers are not affected by OneAgent OpenTelemetry for .NET support.

| Monitoring framework | Versions |
| --- | --- |
| [OpenTelemetryï»¿](https://github.com/open-telemetry/opentelemetry-dotnet) | 1.0.1+, 1.1+ |

Opt-in

To enable OpenTelemetry .NET Framework:

1. Go to the appropriate configuration page:

   * In Latest Dynatrace, go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **General monitoring settings** > **OneAgent features**.
   * In Dynatrace Classic, go to **Settings** > **Preferences** > **OneAgent network modules & integrations**

2. Find and enable **OpenTelemetry (.NET) [Opt-In]**.

Existing tracers are not affected by OneAgent OpenTelemetry for .NET support.

| Monitoring framework | Versions |
| --- | --- |
| [OpenTelemetryï»¿](https://github.com/open-telemetry/opentelemetry-python) | 1.1+ |

Opt-in

To enable OpenTelemetry Python:

1. Go to the appropriate configuration page:

   * In Latest Dynatrace, go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **General monitoring settings** > **OneAgent features**.
   * In Dynatrace Classic, go to **Settings** > **Preferences** > **OneAgent network modules & integrations**

2. Find and enable **OpenTelemetry (Python) [Opt-In]**.

Existing tracers are not affected by OneAgent OpenTelemetry for Python support.

## Attribute redaction

The OneAgent code module's OpenTelemetry Span Sensor automatically captures all OpenTelemetry attributes.
If you want to prevent the accidental storage of personal data, you can exclude specific attribute keys for which the values must not be persisted.
By omitting attributes containing personal data, you can meet your organization's privacy requirements and control the scope of stored monitoring data.

To configure attribute storage and masking settings for your environment

1. Go to the appropriate configuration page:

   * In Latest Dynatrace, go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **General monitoring settings** > **OneAgent features**.
   * In Dynatrace Classic, go to **Settings** > **Preferences** > **OneAgent network modules & integrations**

2. Select **Server-side service monitoring** > **Attribute capturing**.
3. optional To change the default OpenTelemetry attribute persistence, go to **Preferences**.

   * To store all attributes except the ones in the **Blocked attributes** list, select **Allow all attributes**
   * To block all attributes except the ones in the **Allowed attributes** list, select **Block all attributes**

   Only one setting preference is possible.
4. Add an attribute name to the attribute list.

   1. On the **Attribute capturing** page, select **Blocked attributes** or **Allowed attributes**.

      Allowed attributes list Dynatrace recommends a few basic attributes to generally be included, such as `service.name` or `service.version`. For ease of use, Dynatrace comes with a default configuration that can be adjusted.
   2. Select **Add item** to add a new key to the attribute list and enter the key.
   3. Select **Save changes**.
5. Perform the following actions to mask a stored attribute value.

   1. On the **Attribute capturing** page, select **Attribute data masking**.
   2. Select **Add item** to add a new key to the masked attributed list.
   3. Enter a stored value key and select an option from the **Masking** dropdown list. To learn more about masking options, see [OpenTelemetry traces](/docs/manage/data-privacy-and-security/data-privacy/personal-data-captured-by-dynatrace#otel-traces "Find out what types of end-user data may be captured during Dynatrace monitoring and the methods that are available for masking personal end-user data.").
   4. Select **Save changes**.

You can then find the attribute key on the **Distributed traces** page on the [**Summary** tab](/docs/observe/application-observability/distributed-traces/use-cases/segment-request#summary-tab "Enhance your distributed system performance by segmenting requests with slow response time via Service flow and analyzing their distributed traces.").

## Trace search limitations

### Resource attributes

Searching by resource attribute is limited to the service name: filter by `Service name` on the **Distributed traces** page.

### Span attributes

Searching by span attribute is limited to the span name: filter by `Request` on the **Distributed traces** page.

## How the Span Sensor works

For more information about the OneAgent code module's OpenTelemetry Span Sensor, see [Detect OpenTelemetry spans using the OneAgent code module's OpenTelemetry Span Sensor](/docs/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/oneagent-otel#oneagent-otel-span-sensor "Learn how to send OpenTelemetry data to a Dynatrace OneAgent.").

### Entry points

To avoid possible conflicts with existing PurePath distributed traces, OneAgent ingests by default only spans with a [span kindï»¿](https://opentelemetry.io/docs/concepts/signals/traces/#span-kind) of `Server` or `Consumer`. This usually is not an issue, as instrumentation libraries typically configure the appropriate span kind, however something to take into account if your application fully uses manual instrumentation.

This behavior can be customized with an [entry point rule](/docs/ingest-from/extend-dynatrace/extend-tracing/span-settings#span-entry-points "Learn how to configure span settings for OpenTelemetry and OpenTracing."). To do that, in Dynatrace go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **OpenTelemetry** > **Span entry points** and create a new rule with the appropriate action and matcher entry.

### Span hierarchy

Depending on your setup, you may experience "flat span enrichment". This is when spans are displayed in Dynatrace as a flat list instead of a tree hierarchy. While this generally is the default behavior with OneAgent ingestion of OpenTelemetry traces, the hierarchy may still reflect actual span relations as defined by the instrumentation, depending on the involved OneAgent code modules and their support for the instrumented technologies.

Leaf spans

When merging OpenTelemetry spans into OneAgent sensor traces, make sure that OpenTelemetry spans are leaf spans and not in-between OneAgent spans.

### Attribute capturing

As OneAgent ingests spans already [upon their creation](#point-of-ingestion), not all eventual attributes may be already present at the initial ingest. Any attributes added at a later point are highlighted in Dynatrace with an `initial value not set` note and cannot be used for span capture rules, as they were not yet available when the rules were being evaluated.

### Context propagation

When ingesting OpenTelemetry traces automatically with the OneAgent Span Sensor, there is a difference between the context propagation of OpenTelemetry traces and OneAgent traces.

While propagation of OpenTelemetry traces may be already handled properly by your application, it is also important to consolidate them with the OneAgent-specific trace. This can be achieved with a [context propagation rule](/docs/ingest-from/extend-dynatrace/extend-tracing/span-settings#span-context-propagation "Learn how to configure span settings for OpenTelemetry and OpenTracing."). To configure this, in Dynatrace go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **OpenTelemetry** > **Span context propagation** and create a context propagation rule with a `Propagate` action and a matcher entry for the span in question (for example, based on the span name or instrumentation library).

Try to avoid trace consolidation for technologies already covered natively by OneAgent sensors. Merging such OpenTelemetry spans into a OneAgent trace may lead to undefined states.

## Export to third-party backends while using OneAgent

While OpenTelemetry traces are always exported to other backends as is, a small data adjustment takes place when your OneAgent-instrumented application starts a fresh OpenTelemetry trace. This applies only to new traces and not when a trace is continued via context propagation.

In that case, OneAgent may have already created a new trace object when OpenTelemetry was initialized. If these two traces (with separate IDs) are not reconciled, telemetry data might be duplicated or fragmented. To mitigate this and still keep Dynatrace PurePath traces consistent, OneAgent uses the following approach:

* The OpenTelemetry trace ID takes precedence in exports to third parties
* On the Dynatrace backend, the PurePath trace ID is assigned instead

To enable correlation between these two IDs, Dynatrace creates additional [span linksï»¿](https://opentelemetry.io/docs/specs/otel/overview/#links-between-spans) for each span, linking to the OpenTelemetry trace.

The ID rewrite applies only to newly started traces (not context propagation) and to the OpenTelemetry SDKs for Go, Java, JavaScript, PHP, and Python but not to .NET.

## Limitations

### Java

* OneAgent version 1.294 and earlier OneAgent replaces installed global OpenTelemetry SDK components `TracerProvider`, `Propagator`, and `ContextManager`.
  Therefore, with OpenTelemetry Java enabled, traces are no longer seen by this SDK or exported to backends like Jaeger.
* OneAgent version 1.259+ To avoid duplicates, OneAgent [ignores spans from some automatic instrumentation libraries](#java-span-dropping).
* When OneAgent and OpenTelemetry sensors are both present for the same technology, you may experience additional overhead.

### Go

* OneAgent can only instrument Tracer implementation of the default OpenTelemetry SDK.
* When both OneAgent and OpenTelemetry sensors are present for the same technology, you may experience the following limitations:

  + Duplicate nodes in distributed traces
  + Additional overhead

### Node.js

* OneAgent version 1.331+ To avoid duplicates, OneAgent [ignores spans from some automatic instrumentation libraries](#nodejs-span-dropping).
* OneAgent version 1.329 and earlier When OneAgent and OpenTelemetry instrument the same module (such as HTTP or GRPC), you may experience the following limitations:

  + Duplicate nodes in distributed traces
  + Disconnected distributed traces
  + Additional overhead
* OneAgent version 1.261 and earlier OneAgent replaces installed global OpenTelemetry SDK components `TracerProvider`, `Propagator`, and `ContextManager`.
  Therefore, with OpenTelemetry Node.js enabled, traces are no longer seen by this SDK or exported to backends like Jaeger.

### PHP

* OneAgent version 1.313+ To avoid duplicates, OneAgent [ignores spans from some automatic instrumentation libraries](#php-span-dropping).

### Python

* When both OneAgent and OpenTelemetry sensors are present for the same technology, you may experience the following limitations:

  + Duplicate nodes in distributed traces
  + Disconnected distributed traces
  + Additional overhead

### All languages

* OneAgent captures OpenTelemetry resource attributes only if they are provided via the `OTEL_SERVICE_NAME` and `OTEL_RESOURCE_ATTRIBUTES` environment variables. When using the OpenTelemetry trace ingest API, this limitation doesn't apply.
* You can't create [request attributes](/docs/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.") (commonly used for trace searching and filtering) based on OpenTelemetry resource attributes.
* OneAgent truncates attribute values exceeding 4,096 characters.

## Prevention of span duplication in Java

OneAgent version 1.259+

To avoid possible span duplicates for areas covered by OpenTelemetry and OneAgent, OneAgent skips spans from the following automatic instrumentation Java libraries if OneAgent is configured to instrument your Java application and ingest OpenTelemetry spans.

Such spans are skipped only by OneAgent. Exports to third parties (for example, other backends or the Collector) remain unaffected.

## Prevention of span duplication in Node.js

OneAgent version 1.331+

To avoid possible span duplicates for areas covered by OpenTelemetry and OneAgent, OneAgent skips spans from the following automatic instrumentation Node.js libraries if OneAgent is configured to instrument your Node.js application and ingest OpenTelemetry spans.

Such spans are skipped only by OneAgent. Exports to third parties (for example, other backends or the Collector) remain unaffected.

## Prevention of span duplication in PHP

OneAgent version 1.313+

To avoid possible span duplicates for areas covered by OpenTelemetry and OneAgent, OneAgent skips spans from the following automatic instrumentation PHP libraries if OneAgent is configured to instrument your PHP application and ingest OpenTelemetry spans.

Such spans are skipped only by OneAgent. Exports to third parties (for example, other backends or the Collector) remain unaffected.