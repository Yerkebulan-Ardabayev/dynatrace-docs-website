---
title: Service Detection v2
source: https://www.dynatrace.com/docs/observe/application-observability/services/service-detection/service-detection-v2
scraped: 2026-02-16T09:23:45.758097
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