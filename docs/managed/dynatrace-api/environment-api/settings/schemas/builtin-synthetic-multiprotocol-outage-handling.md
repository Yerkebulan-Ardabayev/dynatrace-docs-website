---
title: Settings API - Outage handling schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-synthetic-multiprotocol-outage-handling
scraped: 2026-05-12T11:45:56.012075
---

# Settings API - Outage handling schema table

# Settings API - Outage handling schema table

* Published Jul 31, 2024

### Outage handling (`builtin:synthetic.multiprotocol.outage-handling)`

Dynatrace can generate problems for both global outages and/or local outages based on the availability of either all configured locations or only individual locations over consecutive runs.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:synthetic.multiprotocol.outage-handling` | * `group:web-and-mobile-monitoring` * `group:synthetic.multiprotocol` * `group:web-and-mobile-monitoring.multiprotocol-monitor-default-settings` | `MULTIPROTOCOL_MONITOR` - Network availability monitor  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.multiprotocol.outage-handling` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:synthetic.multiprotocol.outage-handling` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.multiprotocol.outage-handling` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Generate a problem and send an alert when the monitor is unavailable at all configured locations. `globalOutages` | boolean | - | Required |
| Alert if all locations are unable to access my target address `globalConsecutiveOutageCountThreshold` | integer | - | Required |
| Generate a problem and send an alert when the monitor is unavailable for one or more consecutive runs at any location. `localOutages` | boolean | - | Required |
| Alert if at least `localLocationOutageCountThreshold` | integer | - | Required |
| are unable to access my target address `localConsecutiveOutageCountThreshold` | integer | - | Required |