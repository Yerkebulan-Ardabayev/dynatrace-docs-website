---
title: Settings API - ServiceNow Connections schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-servicenow-connection
---

# Settings API - ServiceNow Connections schema table

# Settings API - ServiceNow Connections schema table

* Published Feb 26, 2024

### ServiceNow Connections (`app:dynatrace.servicenow:connection)`

Connections allow you to integrate into ServiceNow.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.servicenow:connection` | - | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.servicenow:connection` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.servicenow:connection` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.servicenow:connection` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Connection name `name` | text | A unique and clearly identifiable connection name to your ServiceNow instance. | Required |
| ServiceNow instance URL `url` | text | URL of the ServiceNow instance. | Required |
| Type `type` | enum | Type of authentication method that should be used. The element has these enums * `basic` * `client-credentials` | Required |
| User `user` | text | Username or Email address. | Required |
| Password `password` | secret | Password of the ServiceNow user. | Required |
| Client ID `clientId` | text | Client ID of the ServiceNow OAuth server | Required |
| Client Secret `clientSecret` | secret | Client secret of the ServiceNow OAuth server | Required |