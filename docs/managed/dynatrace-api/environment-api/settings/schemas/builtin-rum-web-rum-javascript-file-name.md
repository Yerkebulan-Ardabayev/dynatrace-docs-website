---
title: Settings API - RUM monitoring code filename schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-rum-javascript-file-name
---

# Settings API - RUM monitoring code filename schema table

# Settings API - RUM monitoring code filename schema table

* Published Jun 09, 2025

### RUM monitoring code filename (`builtin:rum.web.rum-javascript-file-name)`

Define a custom filename prefix that should be used instead of the default prefix in the RUM monitoring code filename, which is ruxitagentjs or ruxitagent, see [Configure the Real User Monitoring code source﻿](https://dt-url.net/wc03z4k) for details.

**Note:** Be aware that you may experience a temporary reduction in collected RUM data after changing the RUM monitoring code filename prefix. Therefore, this setting should not be changed frequently.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.rum-javascript-file-name` | * `group:web-and-mobile-monitoring.web-applications` * `group:web-and-mobile-monitoring` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.rum-javascript-file-name` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.rum-javascript-file-name` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.rum-javascript-file-name` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Custom filename prefix `filename` | text | - | Required |