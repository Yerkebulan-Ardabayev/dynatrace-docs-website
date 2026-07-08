---
title: Settings API - Beacon endpoint settings schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-mobile-beacon-endpoint
---

# Settings API - Beacon endpoint settings schema table

# Settings API - Beacon endpoint settings schema table

* Published Dec 05, 2023

### Beacon endpoint settings (`builtin:rum.mobile.beacon-endpoint)`

Define where OneAgent is to send your iOS and Android monitoring data.  
**Note:** To use an Environment ActiveGate as beacon endpoint, beacon forwarding must be enabled in the ActiveGate config first. Learn more about how to configure an [Environment ActiveGate﻿](https://dt-url.net/90r039v) or how to use [OneAgent as a beacon endpoint﻿](https://dt-url.net/hr4e0ijr).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.mobile.beacon-endpoint` | * `group:rum-general` | `MOBILE_APPLICATION` - Mobile App  `CUSTOM_APPLICATION` - Custom Application |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.mobile.beacon-endpoint` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.mobile.beacon-endpoint` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.mobile.beacon-endpoint` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Type `type` | enum | The element has these enums * `CLUSTER_ACTIVEGATE` * `ENVIRONMENT_ACTIVEGATE` * `INSTRUMENTED_WEBSERVER` | Required |
| URL `url` | text | This must be a valid beacon endpoint URL.  The URL must start with 'http://' or 'https://'. Environment ActiveGate URL must end with '/mbeacon/{{environment-id}}', Instrumented Web Server URL must end with '/dtmb'. | Required |