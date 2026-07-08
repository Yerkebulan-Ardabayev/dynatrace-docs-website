---
title: Settings API - Cost & Carbon Optimization schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-biz-carbon-cost-and-carbon-settings
---

# Settings API - Cost & Carbon Optimization schema table

# Settings API - Cost & Carbon Optimization schema table

* Published Mar 17, 2025

### Cost & Carbon Optimization (`app:dynatrace.biz.carbon:cost-and-carbon-settings)`

Settings for the Cost & Carbon Optimization AppEngine application.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.biz.carbon:cost-and-carbon-settings` | - | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.biz.carbon:cost-and-carbon-settings` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.biz.carbon:cost-and-carbon-settings` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.biz.carbon:cost-and-carbon-settings` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Workflow ID `workflowId` | text | - | Optional |
| GCP API key `gcpApiKey` | secret | - | Optional |
| Should collect costs `isCostCollected` | boolean | - | Optional |
| Idling optimization `idlingThresholds` | [TThreshold](#TThreshold) | - | Optional |
| Sizing optimization `sizingThresholds` | [TThreshold](#TThreshold) | - | Optional |
| Data center overrides `customDatacenterOverrides` | [TDataCenterValueOverrides](#TDataCenterValueOverrides)[] | - | Required |
| Business health performance indicator `businessHealth` | [TBusinessHealth](#TBusinessHealth) | - | Optional |

##### The `TThreshold` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Network Receiving `networkReceiving` | [TNetworkThreshold](#TNetworkThreshold) | - | Required |
| Network Transmitting `networkTransmitting` | [TNetworkThreshold](#TNetworkThreshold) | - | Required |
| Cpu `cpu` | [TCpuThreshold](#TCpuThreshold) | - | Required |
| Memory `memory` | [TCpuThreshold](#TCpuThreshold) | - | Required |

##### The `TDataCenterValueOverrides` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Data Center Id `dataCenterId` | text | - | Optional |
| Id `pue` | float | - | Optional |
| Carbon Intensity `ci` | float | - | Optional |
| PUE last update `pueLastUpdate` | zoned\_date\_time | - | Optional |
| Carbon Intensity last update `ciLastUpdate` | zoned\_date\_time | - | Optional |

##### The `TBusinessHealth` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Event `event` | [TBusinessEvent](#TBusinessEvent) | - | Required |

##### The `TNetworkThreshold` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Value `value` | integer | - | Required |
| Unit `unit` | enum | The element has these enums * `bytes/s` * `kilobytes/s` * `megabytes/s` * `gigabytes/s` | Required |

##### The `TCpuThreshold` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| CPU threshold [%] `value` | integer | - | Required |
| Unit `unit` | enum | The element has these enums * `%` | Required |

##### The `TBusinessEvent` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Select event `id` | [TBusinessEventId](#TBusinessEventId) | - | Optional |
| Select KPI `attribute` | text | - | Optional |
| KPI unit `unit` | text | - | Optional |

##### The `TBusinessEventId` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Provider `provider` | text | - | Required |
| Name `name` | text | - | Required |