---
title: Settings API - Monitor name schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-synthetic-http-name
scraped: 2026-05-12T11:39:26.602996
---

# Settings API - Monitor name schema table

# Settings API - Monitor name schema table

* Published Dec 05, 2023

### Monitor name (`builtin:synthetic.http.name)`

Define the display name of your http monitor

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:synthetic.http.name` | * `group:synthetic.http` | `HTTP_CHECK` - HTTP monitor |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.http.name` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:synthetic.http.name` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.http.name` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Monitor name `name` | text | - | Required |
| Monitor description `description` | text | - | Optional |