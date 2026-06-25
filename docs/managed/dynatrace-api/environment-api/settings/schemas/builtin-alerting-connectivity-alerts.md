---
title: Settings API - Connectivity alerts schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-alerting-connectivity-alerts
scraped: 2026-05-12T11:41:43.753922
---

# Settings API - Connectivity alerts schema table

# Settings API - Connectivity alerts schema table

* Published Dec 05, 2023

### Connectivity alerts (`builtin:alerting.connectivity-alerts)`

Enable or disable TCP connectivity problems for processes of this process group.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:alerting.connectivity-alerts` | - | `PROCESS_GROUP` - Process Group |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:alerting.connectivity-alerts` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:alerting.connectivity-alerts` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:alerting.connectivity-alerts` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| TCP connectivity problems `connectivityAlerts` | boolean | - | Required |