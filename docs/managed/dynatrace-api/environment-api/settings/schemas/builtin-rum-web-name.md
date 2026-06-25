---
title: Settings API - Application name schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-name
scraped: 2026-05-12T11:39:19.266529
---

# Settings API - Application name schema table

# Settings API - Application name schema table

* Published Dec 05, 2023

### Application name (`builtin:rum.web.name)`

This name is used to refer to your application throughout this Dynatrace environment. Be sure that your application has a meaningful name.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.name` | * `group:rum-settings` | `APPLICATION` - Web application |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.name` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.name` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.name` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Update application name `applicationName` | text | - | Required |