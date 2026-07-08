---
title: Settings API - Launcher schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-launcher-home-launchpad
---

# Settings API - Launcher schema table

# Settings API - Launcher schema table

* Published May 05, 2025

### Launcher (`app:dynatrace.launcher:home.launchpad)`

Set up your teams home launchpads to streamline your workflow and enhance productivity. Configure up to 100 custom home launchpads in this environment to suit your specific needs.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.launcher:home.launchpad` | - | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.launcher:home.launchpad` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.launcher:home.launchpad` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.launcher:home.launchpad` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Home launchpad `groupLaunchpads` | [GroupLaunchpadItem](#GroupLaunchpadItem)[] | Set home launchpads for user groups. The highest ranked will be shown to the user of a group. | Required |

##### The `GroupLaunchpadItem` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Launchpad `launchpadId` | text | - | Required |
| User Group `userGroupId` | text | - | Required |
| State `isEnabled` | boolean | - | Required |