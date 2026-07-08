---
title: Settings API - ActiveGate updates schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-deployment-activegate-updates
---

# Settings API - ActiveGate updates schema table

# Settings API - ActiveGate updates schema table

* Published Dec 05, 2023

### ActiveGate updates (`builtin:deployment.activegate.updates)`

Configure ActiveGate update behavior. To learn more about the latest updates, visit [ActiveGate release notes﻿](https://dt-url.net/release-notes-activegate).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:deployment.activegate.updates` | * `group:updates` | `ENVIRONMENT_ACTIVE_GATE`  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:deployment.activegate.updates` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:deployment.activegate.updates` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:deployment.activegate.updates` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Automatic updates at earliest convenience `autoUpdate` | boolean | - | Required |