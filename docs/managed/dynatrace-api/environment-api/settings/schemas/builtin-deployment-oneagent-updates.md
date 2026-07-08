---
title: Settings API - OneAgent updates schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-deployment-oneagent-updates
---

# Settings API - OneAgent updates schema table

# Settings API - OneAgent updates schema table

* Published Dec 05, 2023

### OneAgent updates (`builtin:deployment.oneagent.updates)`

Select the OneAgent target version and configure update behavior. The selected version is also used for the [Deployment API﻿](https://dt-url.net/hh03wzk) and OneAgent deployment pages. For more about the OneAgent target version, see [OneAgent update﻿](https://dt-url.net/9901p5j). To learn more about the latest updates, see the [OneAgent release notes﻿](https://dt-url.net/release-notes-oneagent). To configure RUM JavaScript update behavior, see RUM JavaScript updates (`<your-dynatrace-url>//ui/settings/builtin:rum.web.rum-javascript-updates`).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:deployment.oneagent.updates` | * `group:updates` | `HOST` - Host  `HOST_GROUP` - Host Group  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:deployment.oneagent.updates` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:deployment.oneagent.updates` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:deployment.oneagent.updates` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Target version `targetVersion` | text | - | Required |
| Revision `revision` | text | - | Required |
| Update mode `updateMode` | enum | The element has these enums * `AUTOMATIC` * `AUTOMATIC_DURING_MW` * `MANUAL` | Required |
| Update windows `maintenanceWindows` | Set<[maintenanceWindow](#maintenanceWindow)> | - | Required |

##### The `maintenanceWindow` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Update window `maintenanceWindow` | setting | Select an update window for OneAgent updates (`<your-dynatrace-url>//ui/settings/builtin:deployment.management.update-windows`) | Required |