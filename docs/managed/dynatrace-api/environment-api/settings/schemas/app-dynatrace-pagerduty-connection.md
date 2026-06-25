---
title: Settings API - PagerDuty Connections schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-pagerduty-connection
scraped: 2026-05-12T11:45:26.969248
---

# Settings API - PagerDuty Connections schema table

# Settings API - PagerDuty Connections schema table

* Published Dec 05, 2023

### PagerDuty Connections (`app:dynatrace.pagerduty:connection)`

Credentials for the PagerDuty App

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.pagerduty:connection` | - | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.pagerduty:connection` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.pagerduty:connection` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.pagerduty:connection` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Connection name `name` | text | The name of the PagerDuty connection | Required |
| PagerDuty API URL `url` | text | URL of the PagerDuty API endpoint | Required |
| API token `token` | secret | Token for the PagerDuty API endpoint | Required |