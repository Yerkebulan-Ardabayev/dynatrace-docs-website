---
title: Settings API - Sensitive data masking schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-logmonitoring-sensitive-data-masking-settings
---

# Settings API - Sensitive data masking schema table

# Settings API - Sensitive data masking schema table

* Published Dec 05, 2023

### Sensitive data masking (`builtin:logmonitoring.sensitive-data-masking-settings)`

Create rules to mask any information you consider to be sensitive. Masking is done on OneAgent, and no personal data is sent or stored on Dynatrace server.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:logmonitoring.sensitive-data-masking-settings` | * `group:log-monitoring` * `group:log-monitoring.ingest-and-processing` | `HOST` - Host  `KUBERNETES_CLUSTER` - Kubernetes cluster  `HOST_GROUP` - Host Group  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.sensitive-data-masking-settings` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:logmonitoring.sensitive-data-masking-settings` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.sensitive-data-masking-settings` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Active `enabled` | boolean | - | Required |
| Name `config-item-title` | text | - | Required |
| `masking` | [Masking](#Masking) | - | Required |
| `matchers` | Set<[Matcher](#Matcher)> | - | Required |

##### The `Masking` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Search expression `expression` | text | Maximum one capture group is allowed. If none was given, the whole expression will be treated as a capture group. | Required |
| Masking type `type` | enum | The element has these enums * `STRING` * `SHA1` * `SHA256` | Required |
| Replacement `replacement` | text | - | Required |

##### The `Matcher` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Attribute `attribute` | enum | The element has these enums * `dt.entity.process_group` * `log.source` * `log.source.origin` * `host.tag` * `k8s.container.name` * `k8s.namespace.name` * `k8s.deployment.name` * `k8s.pod.annotation` * `k8s.pod.label` * `k8s.workload.name` * `k8s.workload.kind` * `container.name` * `dt.entity.container_group` * `process.technology` | Required |
| Operator `operator` | enum | The element has these enums * `MATCHES` | Required |
| `values` | set | - | Required |