---
title: Settings API - OneAgent features schema table
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/settings/schemas/builtin-oneagent-features
scraped: 2026-02-21T21:10:46.991090
---

# Settings API - OneAgent features schema table

# Settings API - OneAgent features schema table

* Published Dec 05, 2023

### OneAgent features (`builtin:oneagent.features)`

Dynatrace OneAgent follows a zero-configuration approach. Therefore, the set of default features apply when you roll out OneAgent the first time. When additional features become available with newer OneAgent versions, they can be activated here to make them available across your environment.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:oneagent.features` | * `group:preferences` | `PROCESS_GROUP_INSTANCE` - Process  `PROCESS_GROUP` - Process Group  `CLOUD_APPLICATION` - Kubernetes workload  `CLOUD_APPLICATION_NAMESPACE` - Kubernetes namespace  `KUBERNETES_CLUSTER` - Kubernetes cluster  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:oneagent.features` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:oneagent.features` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:oneagent.features` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | - | Required |
| Instrumentation enabled (change needs a process restart) `instrumentation` | boolean | - | Optional |
| Activate this feature also in OneAgents only fulfilling the minimum Opt-In version `forcible` | boolean | - | Optional |
| Feature `key` | text | - | Required |