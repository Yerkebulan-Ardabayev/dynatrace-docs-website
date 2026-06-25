---
title: Settings API - Hub Requests schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-hub-manage-permissions
scraped: 2026-05-12T11:49:48.005356
---

# Settings API - Hub Requests schema table

# Settings API - Hub Requests schema table

* Published Jul 31, 2024

### Hub Requests (`app:dynatrace.hub:manage.permissions)`

Please add at least one admin with all necessary permissions to fulfill the requests.

You can either enter team or individual email addresses to receive request notifications.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.hub:manage.permissions` | - | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.hub:manage.permissions` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.hub:manage.permissions` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.hub:manage.permissions` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Contact Email `email` | text | - | Required |
| Name `description` | text | - | Required |