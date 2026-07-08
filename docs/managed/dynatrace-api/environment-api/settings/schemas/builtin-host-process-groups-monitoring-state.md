---
title: Settings API - Process group monitoring schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-host-process-groups-monitoring-state
---

# Settings API - Process group monitoring schema table

# Settings API - Process group monitoring schema table

* Published Dec 05, 2023

### Process group monitoring (`builtin:host.process-groups.monitoring-state)`

Enable or disable monitoring for certain process groups on this host

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:host.process-groups.monitoring-state` | - | `HOST` - Host |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:host.process-groups.monitoring-state` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:host.process-groups.monitoring-state` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:host.process-groups.monitoring-state` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Process group `ProcessGroup` | text | - | Required |
| Monitoring state `MonitoringState` | enum | The element has these enums * `MONITORING_OFF` * `MONITORING_ON` * `DEFAULT` | Required |