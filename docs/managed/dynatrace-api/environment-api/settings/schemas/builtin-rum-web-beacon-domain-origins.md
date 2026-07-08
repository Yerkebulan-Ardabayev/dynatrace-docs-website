---
title: Settings API - Beacon origins for CORS schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-beacon-domain-origins
---

# Settings API - Beacon origins for CORS schema table

# Settings API - Beacon origins for CORS schema table

* Published Dec 05, 2023

### Beacon origins for CORS (`builtin:rum.web.beacon-domain-origins)`

Specify the RUM beacon origins that must be accepted by OneAgent and ActiveGate. Dynatrace tries to match each of your defined rules against the `Origin` request header of your incoming beacons and copies the origin from the matched header to the `Access-Control-Allow-Origin` response header. Beacon origins that aren't part of the defined rule set will be rejected and the beacon response will return HTTP 403. If your rule set is empty, beacon origins will be accepted from any domain. Note that when you enable the first rule, applications that don't match the rule no longer collect RUM data.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.beacon-domain-origins` | * `group:web-and-mobile-monitoring.web-applications` * `group:web-and-mobile-monitoring` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.beacon-domain-origins` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.beacon-domain-origins` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.beacon-domain-origins` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Matcher `matcher` | enum | The element has these enums * `EQUALS` * `STARTS_WITH` * `ENDS_WITH` * `CONTAINS` | Required |
| Pattern `pattern` | text | - | Required |