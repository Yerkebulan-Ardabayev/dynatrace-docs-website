---
title: Settings API - Slack schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-slack-connection
scraped: 2026-05-12T11:43:06.709745
---

# Settings API - Slack schema table

# Settings API - Slack schema table

* Published Dec 05, 2023

### Slack (`app:dynatrace.slack:connection)`

Authentication details for Slack API

(for more information read the [Slack api documentationï»¿](https://api.slack.com/authentication/basics/ "Visit Slack document"))

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.slack:connection` | - | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.slack:connection` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.slack:connection` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.slack:connection` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Connection name `name` | text | Provide a unique and clearly identifiable connection name to your Slack App. | Required |
| Bot token `token` | secret | The bot token obtained from the Slack App Management UI.  Bot token in the format `xoxb-******` | Required |