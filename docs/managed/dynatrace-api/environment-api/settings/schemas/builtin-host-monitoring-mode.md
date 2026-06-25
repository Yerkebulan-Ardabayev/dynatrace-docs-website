---
title: Settings API - Monitoring Mode schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-host-monitoring-mode
scraped: 2026-05-12T11:41:32.545520
---

# Settings API - Monitoring Mode schema table

# Settings API - Monitoring Mode schema table

* Published Dec 05, 2023

### Monitoring Mode (`builtin:host.monitoring.mode)`

OneAgent monitoring mode can only be switched while the agent is connected.

Note that for this schema only, the [GET objectsï»¿](https://docs.dynatrace.com/docs/dynatrace-api/environment-api/settings/objects/get-objects) api will usually not return any objects as these settings are stored on the agents - please use the [GET effective valuesï»¿](https://docs.dynatrace.com/docs/dynatrace-api/environment-api/settings/objects/get-effective-values) api instead.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:host.monitoring.mode` | * `group:host-monitoring` | `HOST` - Host |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:host.monitoring.mode` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:host.monitoring.mode` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:host.monitoring.mode` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Monitoring mode `monitoringMode` | enum | Dynatrace OneAgent allows you to monitor every aspect of your environment, including all processes, services, and applications detected on your hosts.  OneAgent monitoring modes give you flexibility to adjust which capabilities of OneAgent are enabled for your host. Each successive mode increases the enabled capabilities, but also increases license consumption. To learn more, visit [Monitoring consumptionï»¿](https://www.dynatrace.com/support/help/shortlink/monitoring-consumption).  Monitoring mode will be applied to a process after its restart.  The OneAgent's monitoring mode will automatically overwrite this setting whenever it is changed with [oneagentctlï»¿](https://dt-url.net/oneagentctl) or the OneAgent comes online. The element has these enums * `DISCOVERY` * `INFRA_ONLY` * `FULL_STACK` | Required |