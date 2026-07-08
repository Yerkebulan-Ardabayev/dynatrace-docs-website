---
title: Settings API - Log ingest rules schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-logmonitoring-log-storage-settings
---

# Settings API - Log ingest rules schema table

# Settings API - Log ingest rules schema table

* Published Dec 05, 2023

### Log ingest rules (`builtin:logmonitoring.log-storage-settings)`

You can include and exclude specific log sources for analysis by Dynatrace Log Monitoring. The ingest of log records is based on below rules that use matchers like log path, log levels, process groups, k8s specific selectors and more.

To ingest logs, create a new ingest rule. Use suggestions or type in the log source. You can review available log sources on the Process Group Instance screens. You need to define a custom log source if the required log source is not listed.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:logmonitoring.log-storage-settings` | * `group:log-monitoring` * `group:log-monitoring.ingest-and-processing` | `HOST` - Host  `KUBERNETES_CLUSTER` - Kubernetes cluster  `HOST_GROUP` - Host Group  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.log-storage-settings` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:logmonitoring.log-storage-settings` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.log-storage-settings` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Active `enabled` | boolean | - | Required |
| Name `config-item-title` | text | - | Required |
| Send to storage `send-to-storage` | boolean | If `true` matching logs will be included in storage. If `false` matching logs will be excluded from storage. | Required |
| `matchers` | Set<[Matcher](#Matcher)> | - | Required |

##### The `Matcher` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Attribute `attribute` | enum | The element has these enums * `dt.entity.process_group` * `log.source` * `log.source.origin` * `log.content` * `loglevel` * `journald.unit` * `host.tag` * `k8s.container.name` * `k8s.namespace.name` * `k8s.deployment.name` * `k8s.pod.annotation` * `k8s.pod.label` * `k8s.workload.name` * `k8s.workload.kind` * `container.name` * `dt.entity.container_group` * `process.technology` * `winlog.eventid` * `winlog.provider` * `winlog.task` * `winlog.opcode` * `winlog.username` * `winlog.keywords` | Required |
| Operator `operator` | enum | The element has these enums * `MATCHES` | Required |
| `values` | set | - | Required |