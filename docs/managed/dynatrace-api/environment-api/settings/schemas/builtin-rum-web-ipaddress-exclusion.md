---
title: Settings API - Exclude IP addresses from monitoring schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-ipaddress-exclusion
---

# Settings API - Exclude IP addresses from monitoring schema table

# Settings API - Exclude IP addresses from monitoring schema table

* Published Dec 05, 2023

### Exclude IP addresses from monitoring (`builtin:rum.web.ipaddress-exclusion)`

Enable the switch below if the IP addresses are to be included. Disable the switch if they are to be excluded.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.ipaddress-exclusion` | * `group:capturing` * `group:capturing.exclusions` | `APPLICATION` - Web application |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.ipaddress-exclusion` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.ipaddress-exclusion` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.ipaddress-exclusion` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| IP addresses exclusion list `ipExclusionList` | [IpAddressExclusionRule](#IpAddressExclusionRule)[] | **Examples:**  * 84.112.10.5 * fe80::10a1:c6b2:5f68:785d | Required |
| These are the only IP addresses that should be monitored `ipAddressExclusionInclude` | boolean | - | Required |

##### The `IpAddressExclusionRule` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Single IP or IP range start address `ip` | text | - | Required |
| IP range end `ipTo` | text | - | Optional |