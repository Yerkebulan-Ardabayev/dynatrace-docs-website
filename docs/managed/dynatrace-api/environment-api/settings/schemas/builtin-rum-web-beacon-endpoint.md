---
title: Settings API - Beacon endpoint settings schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-beacon-endpoint
---

# Settings API - Beacon endpoint settings schema table

# Settings API - Beacon endpoint settings schema table

* Published Apr 03, 2024

### Beacon endpoint settings (`builtin:rum.web.beacon-endpoint)`

Define where OneAgent is to send your web application monitoring data.
Learn more about how to [configure the beacon endpoint﻿](https://dt-url.net/yp036lb).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.beacon-endpoint` | * `group:rum-settings` | `APPLICATION` - Web application |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.beacon-endpoint` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.beacon-endpoint` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.beacon-endpoint` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Type `type` | enum | The element has these enums * `DEFAULT_CONFIG` * `ACTIVEGATE` * `ONEAGENT` | Required |
| URL `url` | text | You can specify either path segments or an absolute URL. | Required |
| Send beacon data via CORS `useCors` | boolean | Learn more about [sending beacon data via CORS﻿](https://dt-url.net/r7038sa) | Required |