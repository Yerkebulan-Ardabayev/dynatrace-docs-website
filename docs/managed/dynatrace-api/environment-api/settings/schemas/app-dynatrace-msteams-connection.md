---
title: Settings API - Microsoft Teams schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-msteams-connection
---

# Settings API - Microsoft Teams schema table

# Settings API - Microsoft Teams schema table

* Published Dec 05, 2023

### Microsoft Teams (`app:dynatrace.msteams:connection)`

Authentication details for the Microsoft Teams App

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.msteams:connection` | - | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.msteams:connection` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.msteams:connection` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.msteams:connection` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Connection name `name` | text | The name of the Microsoft Teams connection | Required |
| The targeted Microsoft Team `teamName` | text | Optional | Optional |
| The targeted Channel name `channelName` | text | Optional | Optional |
| Webhook URL `webhook` | secret | The Webhook URL that links to the channel  The URL is created using the `Incoming Webhook` app on Teams | Required |