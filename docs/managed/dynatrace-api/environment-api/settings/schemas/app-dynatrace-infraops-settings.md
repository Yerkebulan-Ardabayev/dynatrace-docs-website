---
title: Settings API - Infrastructure & Operations app settings schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-infraops-settings
---

# Settings API - Infrastructure & Operations app settings schema table

# Settings API - Infrastructure & Operations app settings schema table

* Published May 27, 2024

### Infrastructure & Operations app settings (`app:dynatrace.infraops:settings)`

Use these settings to customize the I&O App experience. Please note: You must reload the app for any changes to take effect.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.infraops:settings` | - | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.infraops:settings` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.infraops:settings` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.infraops:settings` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Show monitoring candidates `show.monitoring.candidates` | boolean | When set to true, the app will display monitoring candidates in the Hosts table | Required |
| Show app only hosts `show.standalone.hosts` | boolean | When set to true, the app will display app only hosts in the Hosts table | Required |
| Network interface saturation threshold `interface.saturation.threshold` | float | The threshold at which a network device interface is deemed to be saturated. | Required |
| Limit the number of entities in main inventories `invex.dql.query.limit` | integer | Limit the number of results returned from Grail for Host, Network device, and Extensions entities. | Required |