---
title: Settings API - Advanced correlation schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-resource-timing-origins
---

# Settings API - Advanced correlation schema table

# Settings API - Advanced correlation schema table

* Published Dec 05, 2023

### Advanced correlation (`builtin:rum.resource-timing-origins)`

OneAgent uses the `Server-Timing` response header to communicate RUM correlation data to the RUM JavaScript. For cross-origin requests, the RUM JavaScript can only access the `Server-Timing` header value if the `Timing-Allow-Origin` header permits the origin of the request. Therefore, OneAgent automatically adds the `Timing-Allow-Origin` header to your web application's response if it is not already set by your application. The `Timing-Allow-Origin` header controls access not only to the `Server-Timing` header value, but also to detailed resource timing data.

By default, access is granted to all origins. Add rules to restrict access to specified origins.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.resource-timing-origins` | * `group:web-and-mobile-monitoring.web-applications` * `group:web-and-mobile-monitoring` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.resource-timing-origins` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.resource-timing-origins` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.resource-timing-origins` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Matcher `matcher` | enum | The element has these enums * `EQUALS` * `STARTS_WITH` * `ENDS_WITH` * `CONTAINS` | Required |
| Pattern `pattern` | text | - | Required |