---
title: Settings API - Custom log sources schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-logmonitoring-custom-log-source-settings
scraped: 2026-05-12T11:49:40.248333
---

# Settings API - Custom log sources schema table

# Settings API - Custom log sources schema table

* Published Dec 05, 2023

### Custom log sources (`builtin:logmonitoring.custom-log-source-settings)`

Add custom log sources before creating log ingest rule in case of:

* process is not important (this mean that log source is not automatically discovered by OneAgent)
* logs from Windows event logs (other than Windows system log, Windows security log, or Windows Application log)
* AIX logs
* allowing binary content
* unsupported rotation pattern

OneAgent automatically discovers new log files for important processes on supported platforms. Auto-detected logs are listed on the Process Group Instance or Host screen.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:logmonitoring.custom-log-source-settings` | * `group:log-monitoring` * `group:log-monitoring.ingest-and-processing` | `HOST` - Host  `KUBERNETES_CLUSTER` - Kubernetes cluster  `HOST_GROUP` - Host Group  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.custom-log-source-settings` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:logmonitoring.custom-log-source-settings` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.custom-log-source-settings` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Active `enabled` | boolean | - | Required |
| Name `config-item-title` | text | - | Required |
| `custom-log-source` | [CustomLogSource](#CustomLogSource) | - | Required |
| Log Source context `context` | Set<[Context](#Context)> | Define Custom Log Source only within context if provided | Required |

##### The `CustomLogSource` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Log Source type `type` | enum | The element has these enums * `LOG_PATH_PATTERN` * `WINDOWS_EVENT_LOG` | Required |
| Accept binary content `accept-binary` | boolean | - | Optional |
| Encoding `encoding` | text | - | Optional |
| Log source `values-and-enrichment` | Set<[CustomLogSourceWithEnrichment](#CustomLogSourceWithEnrichment)> | It might be either an absolute path to log(s) with optional wildcards or Windows Event Log name. | Required |

##### The `Context` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Attribute `attribute` | enum | The element has these enums * `dt.entity.process_group` | Required |
| `values` | set | - | Required |

##### The `CustomLogSourceWithEnrichment` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Values `path` | text | - | Required |
| Enrichments `enrichment` | Set<[Enrichment](#Enrichment)> | Optional field that allows to define attributes that will enrich logs  ${N} can be used in attribute value to expand the value matched by wildcards where N denotes the number of the wildcard the expand | Required |

##### The `Enrichment` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| type `type` | enum | The element has these enums * `attribute` | Required |
| key `key` | text | - | Optional |
| value `value` | text | - | Optional |