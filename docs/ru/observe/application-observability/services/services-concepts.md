---
title: Service-related concepts
source: https://www.dynatrace.com/docs/observe/application-observability/services/services-concepts
scraped: 2026-02-21T21:09:04.076634
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