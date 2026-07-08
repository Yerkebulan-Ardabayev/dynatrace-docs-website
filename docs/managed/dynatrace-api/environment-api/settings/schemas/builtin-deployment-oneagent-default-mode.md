---
title: Settings API - OneAgent default mode schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-deployment-oneagent-default-mode
---

# Settings API - OneAgent default mode schema table

# Settings API - OneAgent default mode schema table

* Published Aug 05, 2024

### OneAgent default mode (`builtin:deployment.oneagent.default-mode)`

You can configure which OneAgent [monitoring mode﻿](https://dt-url.net/8703q1z) will be used by default for OneAgent installation commands provided in the Dynatrace web UI. This does not affect OneAgent installer behavior. OneAgent installed without the monitoring mode parameter will run in Full-Stack Monitoring mode.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:deployment.oneagent.default-mode` | * `group:preferences` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:deployment.oneagent.default-mode` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:deployment.oneagent.default-mode` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:deployment.oneagent.default-mode` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| OneAgent default monitoring mode `defaultMode` | enum | The element has these enums * `FULL_STACK` * `INFRASTRUCTURE` * `DISCOVERY` | Required |