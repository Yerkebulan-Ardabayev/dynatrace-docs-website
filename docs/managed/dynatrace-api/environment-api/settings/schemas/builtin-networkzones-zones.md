---
title: Settings API - Network zone schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-networkzones-zones
---

# Settings API - Network zone schema table

# Settings API - Network zone schema table

* Published Oct 27, 2025

### Network zone (`builtin:networkzones.zones)`

Define rules to organize network structures and improve routing efficiency.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:networkzones.zones` | - | `environment`  `environment-default` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:networkzones.zones` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:networkzones.zones` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:networkzones.zones` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Identifier `id` | text | A lowercase string limited to 256 characters that can contain alphanumerics (0-9, a-z), hyphens (-), underscores (\_), and dots (.), but can not start with a dot. | Required |
| Description `description` | text | - | Optional |
| Alternative zones `alternativeZones` | set | Network zones that should be used when the primary zone is not available. | Required |
| Fallback mode `fallbackMode` | enum | Determines the network zone fallback behavior in case the primary and alternative zones are not available. The element has these enums * `ANY_ACTIVE_GATE` * `ONLY_DEFAULT_ZONE` * `NONE` | Required |