---
title: Settings API - Exclude network traffic schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-exclude-network-traffic
---

# Settings API - Exclude network traffic schema table

# Settings API - Exclude network traffic schema table

* Published Dec 05, 2023

### Exclude network traffic (`builtin:exclude.network.traffic)`

OneAgent automatically detects and monitors all of your network traffic, but you can exclude traffic on specific network interfaces or hosts from monitoring.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:exclude.network.traffic` | * `group:monitoring` | `HOST` - Host |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:exclude.network.traffic` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:exclude.network.traffic` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:exclude.network.traffic` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Exclude NIC `excludeNic` | [NicForm](#NicForm)[] | Selecting a network interface, you will exclude all network traffic on that interface from being monitored. You can select from the list below what to not monitor, or input it manually using the "other one" option. | Required |
| Exclude IP `excludeIp` | [IpAddressForm](#IpAddressForm)[] | Providing a host IP address, you will exclude network traffic only in calculating connectivity (other metrics will still be calculated). | Required |

##### The `NicForm` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Operating system `os` | enum | The element has these enums * `OS_TYPE_UNKNOWN` * `OS_TYPE_AIX` * `OS_TYPE_DARWIN` * `OS_TYPE_HPUX` * `OS_TYPE_LINUX` * `OS_TYPE_SOLARIS` * `OS_TYPE_WINDOWS` * `OS_TYPE_ZOS` | Required |
| Network interface `interface` | text | - | Required |

##### The `IpAddressForm` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| IP address `ipAddress` | text | - | Required |