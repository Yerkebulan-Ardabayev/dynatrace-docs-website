---
title: Settings API - Log metrics schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-logmonitoring-schemaless-log-metric
scraped: 2026-05-12T11:39:51.853229
---

# Settings API - Log metrics schema table

# Settings API - Log metrics schema table

* Published Dec 05, 2023

### Log metrics (`builtin:logmonitoring.schemaless-log-metric)`

With log metrics, you can use queries to create metrics from logs data for dashboarding, analysis, and custom alerting. Log metrics consume [DavisÂ® data unitsï»¿](https://dt-url.net/vg43xi8).

Note that newly-defined log metrics are available only for log data ingested after metric creation.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:logmonitoring.schemaless-log-metric` | * `group:log-monitoring.analysis` * `group:log-monitoring` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.schemaless-log-metric` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:logmonitoring.schemaless-log-metric` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.schemaless-log-metric` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | - | Required |
| Metric key `key` | text | - | Required |
| Matcher `query` | text | - | Required |
| Metric measurement `measure` | enum | The element has these enums * `OCCURRENCE` * `ATTRIBUTE` | Required |
| Attribute `measureAttribute` | text | - | Required |
| Dimensions `dimensions` | set | To enable splitting on your metric, add desired dimensions.  You can select a dimension name from the list or set it to any value. To extract fields from logs, you can use log processing (`<your-dynatrace-url>/builtin:logmonitoring.log-dpp-rules`). | Required |