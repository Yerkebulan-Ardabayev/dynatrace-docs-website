---
title: Settings API - Extensions Creator schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-custom-extensions-creator-custom-extensions-creator
scraped: 2026-05-12T11:42:53.781170
---

# Settings API - Extensions Creator schema table

# Settings API - Extensions Creator schema table

* Published Aug 26, 2024

### Extensions Creator (`app:dynatrace.custom.extensions.creator:custom-extensions-creator)`

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.custom.extensions.creator:custom-extensions-creator` | - | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.custom.extensions.creator:custom-extensions-creator` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.custom.extensions.creator:custom-extensions-creator` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.custom.extensions.creator:custom-extensions-creator` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Name `name` | text | A friendly name for this environment | Required |
| Environment URL `environmentUrl` | text | The environment URL to retrieve Custom DB Query V1 endpoints from  This is only used by the Custom DB Query migration feature of the app.  Do not forget to allow outbout connections to this URL in Dynatrace, under **Settings > Preferences > Limit outbound connections** | Required |
| API Token `apiToken` | secret | A token with **ReadConfig** scope  This allows the app to make GET calls to the Configuration V1 API | Required |