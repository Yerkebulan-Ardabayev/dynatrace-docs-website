---
title: Settings API - Geolocation settings schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-geo-settings
---

# Settings API - Geolocation settings schema table

# Settings API - Geolocation settings schema table

* Published Dec 05, 2023

### Geolocation settings (`builtin:geo-settings)`

Settings related to geolocations

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:geo-settings` | - | `environment`  `environment-default` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:geo-settings` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:geo-settings` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:geo-settings` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Display the world map `displayWorldmap` | boolean | - | Required |