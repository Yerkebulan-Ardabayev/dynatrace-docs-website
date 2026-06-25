---
title: Settings API - Container monitoring rules schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-container-monitoring-rule
scraped: 2026-05-12T11:43:56.451284
---

# Settings API - Container monitoring rules schema table

# Settings API - Container monitoring rules schema table

* Published Dec 05, 2023

### Container monitoring rules (`builtin:container.monitoring-rule)`

Within container environments, OneAgent automatically injects code modules into containerized processes to provide out of the box full-stack visibility into applications running within containers. Dynatrace provides complete control over automatic injection of code modules into the container technologies.

In Kubernetes, container monitoring rules are evaluated only in case of `classicFullStack` injection mode. The rules are ignored in case of `cloudNativeFullStack` or `applicationMonitoring`.

Please use the annotation-based configuration option as described [hereï»¿](https://dt-url.net/k8sdtoconfig).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:container.monitoring-rule` | * `group:processes-and-containers.containers` * `group:processes-and-containers` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:container.monitoring-rule` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:container.monitoring-rule` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:container.monitoring-rule` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | - | Required |
| Mode `mode` | enum | The element has these enums * `MONITORING_OFF` * `MONITORING_ON` | Required |
| Container property `property` | enum | The element has these enums * `CONTAINER_NAME` * `IMAGE_NAME` * `KUBERNETES_NAMESPACE` * `KUBERNETES_CONTAINERNAME` * `KUBERNETES_BASEPODNAME` * `KUBERNETES_FULLPODNAME` * `KUBERNETES_PODUID` | Required |
| Condition operator `operator` | enum | The element has these enums * `STARTS` * `NOT_STARTS` * `ENDS` * `NOT_ENDS` * `CONTAINS` * `NOT_CONTAINS` * `EQUALS` * `NOT_EQUALS` * `EXISTS` * `NOT_EXISTS` | Required |
| Condition value `value` | text | - | Required |