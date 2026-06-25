---
title: Settings API - Timestamp/Splitting patterns schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-logmonitoring-timestamp-configuration
scraped: 2026-05-12T11:46:28.572535
---

# Settings API - Timestamp/Splitting patterns schema table

# Settings API - Timestamp/Splitting patterns schema table

* Published Dec 05, 2023

### Timestamp/Splitting patterns (`builtin:logmonitoring.timestamp-configuration)`

Dynatrace OneAgent detects number of timestamp formats in your log records. In case of custom timestamps included in log record define them below. This will assure data quality for analysis.
Timestamp detection also influence proper log splitting. If no timestamp is detected or log format prevents auto-timestamping, adjacent lines can be merged into single log record (also indentations are considered).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:logmonitoring.timestamp-configuration` | * `group:log-monitoring` * `group:log-monitoring.ingest-and-processing` | `HOST` - Host  `KUBERNETES_CLUSTER` - Kubernetes cluster  `HOST_GROUP` - Host Group  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.timestamp-configuration` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:logmonitoring.timestamp-configuration` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.timestamp-configuration` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Active `enabled` | boolean | - | Required |
| Name `config-item-title` | text | - | Required |
| Date-time pattern `date-time-pattern` | text | - | Required |
| Timezone `timezone` | text | - | Required |
| Timestamp search limit `date-search-limit` | integer | Defines the number of characters in every log line (starting from the first character in the line) where the timestamp is searched. | Optional |
| Skip indented lines `skip-indented-lines` | boolean | Don't parse timestamps in lines starting with white character | Optional |
| `matchers` | Set<[Matcher](#Matcher)> | - | Required |
| Entry boundary pattern `entry-boundary` | [EntryBoundary](#EntryBoundary) | Optional field. Enter a fragment of the line text that starts the entry. No support for wildcards - the text is treated literally. | Optional |
| Detect JSON format `json-configuration` | [JSONConfiguration](#JSONConfiguration) | - | Optional |

##### The `Matcher` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Attribute `attribute` | enum | The element has these enums * `dt.entity.process_group` * `log.source` * `log.source.origin` * `host.tag` * `k8s.container.name` * `k8s.namespace.name` * `k8s.deployment.name` * `k8s.pod.annotation` * `k8s.pod.label` * `k8s.workload.name` * `k8s.workload.kind` * `container.name` * `dt.entity.container_group` * `process.technology` | Required |
| Operator `operator` | enum | The element has these enums * `MATCHES` | Required |
| `values` | set | - | Required |

##### The `EntryBoundary` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `pattern` | text | - | Optional |

##### The `JSONConfiguration` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `formatDetection` | boolean | - | Optional |