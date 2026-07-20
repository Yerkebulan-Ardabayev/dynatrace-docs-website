---
title: Service detection
source: https://docs.dynatrace.com/managed/observe/application-observability/services/service-detection
---

# Service detection

# Service detection

* Explanation
* 1-min read
* Updated on Oct 25, 2025

A service in Dynatrace represents a logical grouping of workloads—typically, applications or microservices running in your environment. Service detection automatically identifies these services and encompasses endpoint detection, failure detection, and splitting.

Dynatrace offers two service detection approaches:

* Service Detection v2 (SDv2)
* Service Detection v1 (SDv1)

## Service Detection v2

[Service Detection v2](/managed/observe/application-observability/services/service-detection/service-detection-v2 "Find out how to detect, name, and split services from OpenTelemetry and OneAgent spans.") operates according to a single set of attribute-based rules—built-in and user-defined—evaluated against every span of a trace.

## Service Detection v1

[Service Detection v1](/managed/observe/application-observability/services/service-detection/service-detection-v1 "Find out how Dynatrace Service Detection v1 detects and names different types of services.") is the classic service detection for OneAgent-instrumented processes. It provides detection based on technology-specific service types.

## Comparison of Service Detection v2 and v1

![Diagram showing the differences between Service Detection v2 and Service Detection v1](https://dt-cdn.net/images/sdv2-sdv1-1383-eb18456698.png)

Diagram showing the differences between Service Detection v2 and Service Detection v1

As shown in the diagram above, Service Detection v2 detects services using rules that evaluate resource attributes (like `k8s.workload.name`) against spans. Service Detection v1 detects services based on technology-specific span content (for example, invoked Java classes such as `BillingController`).

[### Service Detection v2

Find out more about Service Detection v2.](/managed/observe/application-observability/services/service-detection/service-detection-v2 "Find out how to detect, name, and split services from OpenTelemetry and OneAgent spans.")[### Service Detection v1

Learn more about Service Detection v1.](/managed/observe/application-observability/services/service-detection/service-detection-v1 "Find out how Dynatrace Service Detection v1 detects and names different types of services.")