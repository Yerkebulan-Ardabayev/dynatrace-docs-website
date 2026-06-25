---
title: Settings API - Application name schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-mobile-name
scraped: 2026-05-12T11:49:18.491751
---

# Settings API - Application name schema table

# Settings API - Application name schema table

* Published Dec 05, 2023

### Application name (`builtin:rum.mobile.name)`

This name is used to refer to your mobile app throughout this Dynatrace environment. Be sure that your app has a meaningful name.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.mobile.name` | * `group:rum-general` | `MOBILE_APPLICATION` - Mobile App |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.mobile.name` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.mobile.name` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.mobile.name` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Update app name `applicationName` | text | - | Required |