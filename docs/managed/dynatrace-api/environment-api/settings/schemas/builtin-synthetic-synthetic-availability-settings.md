---
title: Settings API - Synthetic availability schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-synthetic-synthetic-availability-settings
scraped: 2026-05-12T11:43:04.947443
---

# Settings API - Synthetic availability schema table

# Settings API - Synthetic availability schema table

* Published Dec 05, 2023

### Synthetic availability (`builtin:synthetic.synthetic-availability-settings)`

Dynatrace offers the possibility to configure maintenance windows. By default maintenance windows only affect problem detection and alerting. You can change this behavior and calculate availability including/excluding maintenance window periods.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:synthetic.synthetic-availability-settings` | * `group:web-and-mobile-monitoring` * `group:web-and-mobile-monitoring.synthetic-monitors` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.synthetic-availability-settings` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:synthetic.synthetic-availability-settings` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.synthetic-availability-settings` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Exclude periods with maintenance windows from availability calculation `excludeMaintenanceWindows` | boolean | - | Required |