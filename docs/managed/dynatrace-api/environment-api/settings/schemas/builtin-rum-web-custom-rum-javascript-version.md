---
title: Settings API - Custom RUM JavaScript version schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-custom-rum-javascript-version
scraped: 2026-05-12T11:43:29.550516
---

# Settings API - Custom RUM JavaScript version schema table

# Settings API - Custom RUM JavaScript version schema table

* Published Dec 05, 2023

### Custom RUM JavaScript version (`builtin:rum.web.custom-rum-javascript-version)`

Define a custom RUM JavaScript version to be added to the pool of versions for web applications to choose from.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.custom-rum-javascript-version` | * `group:web-and-mobile-monitoring.web-applications` * `group:web-and-mobile-monitoring` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.custom-rum-javascript-version` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.custom-rum-javascript-version` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.custom-rum-javascript-version` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Choose custom version `customJavaScriptVersion` | text | - | Optional |