---
title: Settings API - General settings schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-dashboards-general
---

# Settings API - General settings schema table

# Settings API - General settings schema table

* Published Dec 05, 2023

### General settings (`builtin:dashboards.general)`

Configure anonymous access and home dashboard settings.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:dashboards.general` | * `group:dashboards` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:dashboards.general` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:dashboards.general` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:dashboards.general` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Allow anonymous access `enablePublicSharing` | boolean | Allow users to grant anonymous access to dashboards. No sign-in will be required to view those dashboards read-only. | Required |
| Home dashboards `defaultDashboardList` | [UserGroups](#UserGroups)[] | Configure home dashboard for selected user group. The selected preset dashboard will be loaded as default landing page for this environment. | Required |

##### The `UserGroups` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| User group `UserGroup` | text | Show selected dashboard by default for this user group | Required |
| Home dashboard `Dashboard` | text | Preset dashboard to show as default landing page | Required |