---
title: Settings API - Cookies schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-synthetic-http-cookies
scraped: 2026-05-12T11:44:47.289010
---

# Settings API - Cookies schema table

# Settings API - Cookies schema table

* Published Dec 05, 2023

### Cookies (`builtin:synthetic.http.cookies)`

Set cookies to store state information or instruct the server not to send certain kinds of information.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:synthetic.http.cookies` | * `group:synthetic.http` | `HTTP_CHECK` - HTTP monitor |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.http.cookies` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:synthetic.http.cookies` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.http.cookies` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Set cookies `enabled` | boolean | - | Required |
| `cookies` | Set<[CookieEntry](#CookieEntry)> | - | Required |

##### The `CookieEntry` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Name `name` | text | Enclose placeholder values in brackets, for example {email} | Required |
| Value `value` | text | Enclose placeholder values in brackets, for example {email} | Required |
| Domain `domain` | text | Enclose placeholder values in brackets, for example {email} | Required |
| Path (optional) `path` | text | Enclose placeholder values in brackets, for example {email} | Optional |