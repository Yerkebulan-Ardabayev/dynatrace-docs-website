---
title: Settings API - Business flow schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-biz-flow-biz-flow-settings
---

# Settings API - Business flow schema table

# Settings API - Business flow schema table

* Published May 20, 2024

### Business flow (`app:dynatrace.biz.flow:biz-flow-settings)`

Settings for the Business flow AppEngine application.

Warning! If the following configurations are modified here, in the Settings 2.0 environment, it is likely that the Business Flow application will lose access to them or will have unexpected behaviour. It is strongly advised not to make any changes and to save them here. If you want to make changes, access Business Flow app.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.biz.flow:biz-flow-settings` | - | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.biz.flow:biz-flow-settings` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.biz.flow:biz-flow-settings` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.biz.flow:biz-flow-settings` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Name `name` | text | Configuration Name | Optional |
| Description `description` | text | Configuration description | Optional |
| Version `version` | integer | - | Optional |
| Configuration ID `id` | text | - | Optional |
| Steps `steps` | [TStepType](#TStepType)[] | Configuration Steps | Required |
| Connections `connections` | [TConnectionType](#TConnectionType)[] | - | Required |
| Correlation ID `correlationID` | text | Correlation ID | Optional |
| KPI Label `kpiLabel` | text | - | Required |
| KPI `kpi` | text | KPI | Optional |
| KPI Event `kpiEvent` | [TKpiEventType](#TKpiEventType) | - | Optional |
| KPI Unit `kpiUnit` | text | - | Optional |
| Calculation type `kpiCalculation` | enum | The element has these enums * `sum` * `firstEvent` * `lastEvent` | Optional |
| Analysis type `analysisType` | enum | The element has these enums * `fulfillment` * `conversion` * `other` | Required |
| Analysis custom label `analysisCustomLabel` | text | - | Required |
| Analysis Unit `analysisUnit` | text | - | Optional |
| Anomaly Detector IDs `anomalyDetectorIDs` | [TAnomalyDetectorIDsType](#TAnomalyDetectorIDsType) | - | Optional |
| Is Smartscape Topology Enabled `isSmartscapeTopologyEnabled` | boolean | - | Required |
| Smartscape Entity ID `smartscapeEntityId` | text | - | Optional |
| Priority `priority` | enum | The element has these enums * `high` * `medium` * `low` * `critical` | Optional |
| Monitoring timeframe in hours `monitoringTimeframeInHours` | integer | - | Optional |
| Monitoring frequency in hours `monitoringFrequencyInHours` | integer | - | Optional |
| Is default query limit ignored `isDefaultQueryLimitIgnored` | boolean | - | Required |

##### The `TStepType` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Name `name` | text | - | Required |
| ID `id` | text | - | Required |
| Is Root `isRoot` | boolean | - | Optional |
| Events `events` | [TEventType](#TEventType)[] | - | Required |

##### The `TConnectionType` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| ID `id` | text | - | Required |
| Source `source` | text | - | Required |
| Target `target` | text | - | Required |

##### The `TKpiEventType` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Name `name` | text | - | Required |
| Provider `provider` | text | - | Required |

##### The `TAnomalyDetectorIDsType` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Errors `errors` | text | - | Optional |
| Revenue `revenue` | text | - | Optional |
| Average duration `avgDuration` | text | - | Optional |
| Completed Flows `completedFlows` | text | - | Optional |

##### The `TEventType` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| ID `id` | text | - | Required |
| Correlation ID `correlationID` | text | - | Optional |
| Name `name` | text | - | Required |
| Provider `provider` | text | - | Required |
| Is Error `isError` | boolean | - | Required |
| Is Disabled `isDisabled` | boolean | - | Required |