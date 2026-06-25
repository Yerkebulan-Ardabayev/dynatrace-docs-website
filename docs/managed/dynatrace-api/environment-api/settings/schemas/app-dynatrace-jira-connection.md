---
title: Settings API - Jira Connections schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-jira-connection
scraped: 2026-05-12T11:49:01.133821
---

# Settings API - Jira Connections schema table

# Settings API - Jira Connections schema table

* Published Dec 05, 2023

### Jira Connections (`app:dynatrace.jira:connection)`

Credentials for the Jira App

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.jira:connection` | - | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.jira:connection` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.jira:connection` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.jira:connection` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Connection name `name` | text | The name of the Jira connection | Required |
| Jira URL `url` | text | URL of the Jira server | Required |
| Type `type` | enum | Type of authentication method that should be used The element has these enums * `basic` * `pat` * `cloud-token` | Required |
| User `user` | text | Username or E-Mail address | Required |
| Password `password` | secret | Password of the Jira user | Required |
| Token `token` | secret | Token for the selected authentication type | Required |