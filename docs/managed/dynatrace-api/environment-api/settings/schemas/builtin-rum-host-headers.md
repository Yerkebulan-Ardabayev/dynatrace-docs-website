---
title: Settings API - Identify host names schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-host-headers
scraped: 2026-05-12T11:39:12.521925
---

# Settings API - Identify host names schema table

# Settings API - Identify host names schema table

* Published Dec 05, 2023

### Identify host names (`builtin:rum.host-headers)`

Specify HTTP request headers OneAgent can use to identify your application's host names, whenever Dynatrace canât automatically identify them. Provided headers are processed sequentially, with the ones at the top of the list taking priority. Learn why it's important and when we can't identify them.

Dynatrace uses host names as part of the URL that is matched against your application detection rules, which control when OneAgent injects the RUM JavaScript tag. For instance, when your web server operates behind a firewall using a different host name your application detection rule wonât match and OneAgent wonât inject RUM into your application.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.host-headers` | * `group:web-and-mobile-monitoring.web-applications` * `group:web-and-mobile-monitoring` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.host-headers` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.host-headers` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.host-headers` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| HTTP header format `headerName` | text | - | Required |