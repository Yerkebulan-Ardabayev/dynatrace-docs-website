---
title: Settings API - Monitoring schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-host-monitoring
---

# Settings API - Monitoring schema table

# Settings API - Monitoring schema table

* Published Dec 05, 2023

### Monitoring (`builtin:host.monitoring)`

OneAgent automatically monitors host, its processes, services and applications but you can switch off monitoring or disable auto-injection.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:host.monitoring` | * `group:host-monitoring` | `HOST` - Host |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:host.monitoring` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:host.monitoring` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:host.monitoring` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Monitor this host `enabled` | boolean | Turn on monitoring to gain visibility into this host, its processes, services, and applications. | Required |