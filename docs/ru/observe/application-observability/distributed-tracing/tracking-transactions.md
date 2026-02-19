---
title: Span and trace context propagation
source: https://www.dynatrace.com/docs/observe/application-observability/distributed-tracing/tracking-transactions
scraped: 2026-02-19T21:13:02.926457
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