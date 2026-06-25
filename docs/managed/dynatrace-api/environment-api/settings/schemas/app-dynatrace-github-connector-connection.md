---
title: Settings API - GitHub Connections schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-github-connector-connection
scraped: 2026-05-12T11:46:12.955010
---

# Settings API - GitHub Connections schema table

# Settings API - GitHub Connections schema table

* Published Aug 26, 2024

### GitHub Connections (`app:dynatrace.github.connector:connection)`

GitHub authentication details

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.github.connector:connection` | - | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.github.connector:connection` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.github.connector:connection` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.github.connector:connection` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Connection name `name` | text | The name of the GitHub connection | Required |
| Type `type` | enum | Type of authentication method that should be used The element has these enums * `pat` | Required |
| Token `token` | secret | Token for the selected authentication type | Required |