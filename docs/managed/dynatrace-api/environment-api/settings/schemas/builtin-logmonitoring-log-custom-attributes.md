---
title: Settings API - Log custom attributes schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-logmonitoring-log-custom-attributes
scraped: 2026-05-12T11:41:28.629265
---

# Settings API - Log custom attributes schema table

# Settings API - Log custom attributes schema table

* Published Dec 05, 2023

### Log custom attributes (`builtin:logmonitoring.log-custom-attributes)`

Dynatrace log monitoring gives you the ability to define custom attributes for ingested logs.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:logmonitoring.log-custom-attributes` | * `group:log-monitoring.analysis` * `group:log-monitoring` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.log-custom-attributes` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:logmonitoring.log-custom-attributes` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.log-custom-attributes` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Key `key` | text | The attribute key is case sensitive in log data ingestion. | Required |
| Show attribute values in side bar `aggregableAttribute` | boolean | In the case of Log Monitoring Classic, the change applies to newly ingested log events. This attribute won't search any log events ingested before this option was toggled on. In Logs on Grail's case, the switch's state is ignored. | Required |