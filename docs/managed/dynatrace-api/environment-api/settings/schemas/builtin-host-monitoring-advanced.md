---
title: Settings API - Advanced Settings schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-host-monitoring-advanced
---

# Settings API - Advanced Settings schema table

# Settings API - Advanced Settings schema table

* Published Dec 05, 2023

### Advanced Settings (`builtin:host.monitoring.advanced)`

You can switch off the injection of the ProcessAgent and of CodeModules.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:host.monitoring.advanced` | * `group:host-monitoring` | `HOST` - Host |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:host.monitoring.advanced` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:host.monitoring.advanced` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:host.monitoring.advanced` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| ProcessAgent injection `processAgentInjection` | boolean | Disabling this setting disables many deep process visibility features, for example: tracing, profiling, technology-specific metrics (e.g. heap usage), JMX/PMI metrics collection, runtime vulnerability analytics, live debugging, etc. For Fullstack or Infrastructure modes, we only recommend disabling this setting for troubleshooting purposes.  Disabling automatic injection via [oneagentctl﻿](https://dt-url.net/oneagentctl) takes precedence over this setting being enabled and cannot be changed from the Dynatrace web UI. | Required |
| CodeModule injection `codeModuleInjection` | boolean | Inject CodeModules in Discovery mode. | Required |