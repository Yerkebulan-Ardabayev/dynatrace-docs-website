---
title: Service Detection v2
source: https://www.dynatrace.com/docs/observe/application-observability/services/service-detection/service-detection-v2
scraped: 2026-02-15T21:15:41.950199
---

# Service Detection v2

# Service Detection v2

* Overview
* 1-min read
* Updated on Aug 18, 2025

Service Detection v2 (SDv2) operates according to a single set of rules that are based on attributes. This includes default rules, and you can additionally define your own custom rules.
SDv2 rules are available for OpenTelemetry services, and a public preview is available for services that are running in Kubernetes and monitored by OneAgent.

Public preview for SDv2 for Kubernetes

To join the public preview:

1. Navigate to your Kubernetes namespace or cluster.
2. Select **Settings** > **Service detection** > **Services Detection v2 for Kubernetes**.
3. Turn on the **Enable Service detection v2** toggle.

As part of the public preview, you can use the following attributes to further restrict where the new SDv2 rules should be applied.

* `dt.agent.module.type`
* `k8s.cluster.name`
* `k8s.namespace.name`
* `k8s.workload.name`
* `dt.host_group.id`

These are customized within your Kubernetes namespace or cluster settings.

Currently, Java is the only supported language, and you need to keep the default matching condition as `dt.agent.module.type == "java"`.
Support for additional languages is currently planned and will be announced via release notes.

SDv2 provides:

* Service detection and naming based on resource attributes and conditions.
* Endpoint detection based on span and resource and attributes.
* Service splitting based on resource attributes.
* Failure detection based on HTTP or gRPC codes or other span and resource attributes.

SDv2 behavior can be configured via:

* The Dynatrace web UI, as described in these pages.
* The [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.").

## Related topics

* [Service Detection v1](/docs/observe/application-observability/services/service-detection/service-detection-v1 "Find out how Dynatrace Service Detection v1 detects and names different types of services.")