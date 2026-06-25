---
title: Settings API - Anomaly detectors schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-davis-anomaly-detectors
scraped: 2026-05-12T11:47:29.201959
---

# Settings API - Anomaly detectors schema table

# Settings API - Anomaly detectors schema table

* Published May 20, 2024

### Anomaly detectors (`builtin:davis.anomaly-detectors)`

Anomaly detectors are used to automatically detect anomalies in timeseries by using thresholds or baselines.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:davis.anomaly-detectors` | * `group:anomaly-detection` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:davis.anomaly-detectors` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:davis.anomaly-detectors` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:davis.anomaly-detectors` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | When enabled, the anomaly detector will be active and running. | Required |
| Title `title` | text | The title of the anomaly detector | Required |
| Description `description` | text | The description of the anomaly detector | Required |
| Source `source` | text | The source which created the anomaly detector | Required |
| Execution settings `executionSettings` | [ExecutionSettings](#ExecutionSettings) | Defines the configuration parameters that influence how and under what context a query or evaluation is executed. | Required |
| Analyzer input `analyzer` | [AnalyzerInput](#AnalyzerInput) | Analyzer input to initialize the analyzer | Required |
| Event template `eventTemplate` | [DavisEventTemplate](#DavisEventTemplate) | Defines additional fields on the davis events triggered by the anomaly detector | Required |

##### The `ExecutionSettings` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Actor `actor` | text | UUID of a service user. Queries will be executed on behalf of the service user. | Required |
| Query offset `queryOffset` | integer | Minute offset of sliding evaluation window for metrics with latency | Optional |
| Execution delay `delay` | integer | Fixed delay between executions (in seconds) | Optional |

##### The `AnalyzerInput` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Name `name` | text | Fully qualified name of the analyzer | Required |
| Input fields `input` | Set<[AnalyzerInputField](#AnalyzerInputField)> | Input fields for the specified analyzer | Required |

##### The `DavisEventTemplate` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Event properties `properties` | [EventProperty](#EventProperty)[] | Set of additional key-value properties to be attached to the triggered event. | Required |

##### The `AnalyzerInputField` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Key `key` | text | Analyzer input field key | Required |
| Value `value` | text | Analyzer input field value | Required |

##### The `EventProperty` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Key `key` | text | Property key | Required |
| Value `value` | text | Property value. Supports substitution of placeholders placed in curly braces {}. | Required |