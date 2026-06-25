---
title: Settings API - Network zones settings schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-networkzones
scraped: 2026-05-12T11:47:57.743992
---

# Settings API - Network zones settings schema table

# Settings API - Network zones settings schema table

* Published Dec 05, 2023

### Network zones settings (`builtin:networkzones)`

In combination with ActiveGates, network zones save bandwidth and infrastructure costs by

* Compressing traffic
* Optimizing traffic routing
* Preventing unrelated traffic in between data centers and regions

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:networkzones` | * `group:preferences` | `environment`  `environment-default` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:networkzones` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:networkzones` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:networkzones` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enable network zones in this environment.  `enabled` | boolean | For details, see [Network zonesï»¿](https://www.dynatrace.com/support/help/shortlink/network-zones).  â  Warning: You may experience network imbalance if you suddenly disable network zones in an environment that has a high number of OneAgents with network zone configuration. To avoid this and to ensure smooth adoption of network zones, follow best practices for planning and proper naming, as explained in [Network zonesï»¿](https://www.dynatrace.com/support/help/shortlink/network-zones). | Required |