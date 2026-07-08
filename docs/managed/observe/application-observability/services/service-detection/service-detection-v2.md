---
title: Service Detection v2
source: https://docs.dynatrace.com/managed/observe/application-observability/services/service-detection/service-detection-v2
---

# Service Detection v2

# Service Detection v2

* Overview
* 1-min read
* Updated on Jun 17, 2026

Cluster version 1.318+

Service Detection v2 (SDv2) operates according to a single set of rules that are based on attributes. This includes default rules, and you can additionally define your own custom rules. SDv2 rules apply only to OpenTelemetry services and the Adobe Experience Manager.

SDv2 provides:

* Service detection and naming based on resource attributes and conditions.
* Endpoint detection based on span and resource attributes.
* Service splitting based on resource attributes.
* Failure detection based on HTTP or gRPC codes or other span and resource attributes.

You can configure SDv2 via:

* Dynatrace web UI, as described in the pages within this section.
* [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.").

## Related topics

* [Service Detection v1](/managed/observe/application-observability/services/service-detection/service-detection-v1 "Find out how Dynatrace Service Detection v1 detects and names different types of services.")