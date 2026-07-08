---
title: Span and trace context propagation in Distributed Traces Classic
source: https://docs.dynatrace.com/managed/observe/application-observability/distributed-traces/context-propagation
---

# Span and trace context propagation in Distributed Traces Classic

# Span and trace context propagation in Distributed Traces Classic

* Explanation
* 2-min read
* Updated on May 29, 2026

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

* **x-dynatrace**—for various communication protocols. This format is proprietary to Dynatrace.
* **traceparent** and **tracestate**—W3C standard format used by both OneAgent and OpenTelemetry.
* **dtdTraceTagInfo**—custom property for various messaging systems.

The exact implementation varies by technology: sometimes using HTTPS headers, SQS message properties, or AWS EventBridge payload injection.

## Mixed environments with OpenTelemetry

In mixed environments with both OneAgent and OpenTelemetry instrumentation, trace context propagation bridges the gap:

* Both OneAgent and OpenTelemetry use the W3C Trace Context format.
* The context must be propagated consistently across the communication channel.
* For HTTP, this is standardized in headers.
* For other protocols such as messaging and events, you need to be consistent with placement between OneAgent and OpenTelemetry.

## Turning on W3C trace context

There are several reasons to turn on W3C trace context in Dynatrace:

* Industry standard compatibility—it aligns with W3C specification.
* Vendor-agnostic tracing—it works in heterogeneous environments with multiple monitoring solutions.
* Future-proofing—it matches industry direction for distributed tracing.

### Considerations when using W3C trace context

* Interoperability challenges—despite being a standard, real-world implementation can vary.
* Browser and app behavior—some clients may send the same traceId repeatedly, affecting trace quality.
* Tool conflicts—multiple APM tools in the same process may overwrite each other's context.

### Set up W3C trace context

To turn W3C trace context on

1. Go to **Settings** > **Preferences** > **OneAgent features**.
2. Turn on **Send W3C Trace Context HTTP headers** and **Send W3C Trace Context gRPC headers**.

While the W3C standard formally specifies HTTP propagation, Dynatrace and the broader industry apply these concepts to other communication protocols.

## Supplementary custom headers

In addition to the main propagation mechanisms, the code modules for some technologies set additional custom HTTP request headers in the context of distributed tracing. Ensure that your infrastructure allows them to pass through unaltered.

| Header | Purpose |
| --- | --- |
| `X-dynaTrace-RequestState` | Used by the Apache, NGINX, and IIS code modules to track the depth of a subpath tree, preventing endless distributed traces. |
| `X-ruxit-Apache-ServerNamePorts` | Used by the Apache code module to synchronize service naming with the PHP code module. |
| `X-Ruxit-Forwarded-For` | Used by the NGINX code module to track proxy scenarios. |