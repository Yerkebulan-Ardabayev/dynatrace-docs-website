---
title: Settings API - Anonymize End-User IP Addresses schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-preferences-ipaddressmasking
---

# Settings API - Anonymize End-User IP Addresses schema table

# Settings API - Anonymize End-User IP Addresses schema table

* Published Dec 05, 2023

### Anonymize End-User IP Addresses (`builtin:preferences.ipaddressmasking)`

Control what data Dynatrace is capturing. Dynatrace can capture IP addresses and GPS coordinates of end users to determine the location from which they access your application. IP Address Masking truncates IP addresses captured from your end users' web browsers and the data captured by OneAgent for effective de-identification.

To learn more, visit [Mask IPs and GPS coordinates﻿](https://dt-url.net/mask-end-users-ip-addresses). For further details on Dynatrace's privacy settings, visit [Data privacy and security﻿](https://dt-url.net/zn03sq4) documentation.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:preferences.ipaddressmasking` | * `group:rum-general` * `group:preferences` * `group:rum-settings` * `group:privacy-settings` | `MOBILE_APPLICATION` - Mobile App  `CUSTOM_APPLICATION` - Custom Application  `APPLICATION` - Web application  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:preferences.ipaddressmasking` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:preferences.ipaddressmasking` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:preferences.ipaddressmasking` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Mask end-user IP addresses and GPS coordinates `enabled` | boolean | - | Required |
| `type` | enum | The element has these enums * `all` * `public` | Required |