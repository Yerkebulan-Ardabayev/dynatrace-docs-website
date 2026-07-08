---
title: Settings API - Outage handling schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-synthetic-browser-outage-handling
---

# Settings API - Outage handling schema table

# Settings API - Outage handling schema table

* Published Dec 05, 2023

### Outage handling (`builtin:synthetic.browser.outage-handling)`

Dynatrace can generate problems for both global outages and/or local outages based on the availability of either all configured locations or only individual locations over consecutive runs.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:synthetic.browser.outage-handling` | * `group:web-and-mobile-monitoring` * `group:web-and-mobile-monitoring.browser-monitor-default-settings` | `SYNTHETIC_TEST` - Synthetic monitor  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.browser.outage-handling` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:synthetic.browser.outage-handling` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.browser.outage-handling` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Generate a problem and send an alert when the monitor is unavailable at all configured locations. `globalOutages` | boolean | - | Required |
| Alert if all locations are unable to access my web application `globalConsecutiveOutageCountThreshold` | integer | - | Required |
| Generate a problem and send an alert when the monitor is unavailable for one or more consecutive runs at any location. `localOutages` | boolean | - | Required |
| Alert if at least `localLocationOutageCountThreshold` | integer | - | Required |
| are unable to access my web application `localConsecutiveOutageCountThreshold` | integer | - | Required |
| Automatic retry on error. `retryOnError` | boolean | When enabled, which is the default, failing monitor executions are retried immediately one time to avoid false positives and only the second result is used. When disabled, we use the first result right away. Requires ActiveGate version 1.207+ for private locations. | Required |