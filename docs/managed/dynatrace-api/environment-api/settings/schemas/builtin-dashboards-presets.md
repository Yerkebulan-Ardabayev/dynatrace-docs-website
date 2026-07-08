---
title: Settings API - Preset settings schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-dashboards-presets
---

# Settings API - Preset settings schema table

# Settings API - Preset settings schema table

* Published Dec 05, 2023

### Preset settings (`builtin:dashboards.presets)`

Configure dashboard preset settings.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:dashboards.presets` | * `group:dashboards` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:dashboards.presets` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:dashboards.presets` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:dashboards.presets` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enable presets `enableDashboardPresets` | boolean | Dashboard presets are visible to all users by default. For a pristine environment you may disable them entirely or opt to manually limit visibility to selected user groups. | Required |
| Limit preset visibility `dashboardPresetsList` | [DashboardPresets](#DashboardPresets)[] | Show selected preset to respective user group only. | Required |

##### The `DashboardPresets` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Dashboard preset `DashboardPreset` | text | Dashboard preset to limit visibility for | Required |
| User group `UserGroup` | text | User group to show selected dashboard preset to | Required |