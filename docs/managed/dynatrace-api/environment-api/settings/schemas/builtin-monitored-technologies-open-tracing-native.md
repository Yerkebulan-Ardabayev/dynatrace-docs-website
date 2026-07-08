---
title: Settings API - Envoy schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-monitored-technologies-open-tracing-native
---

# Settings API - Envoy schema table

# Settings API - Envoy schema table

* Published Dec 05, 2023

### Envoy (`builtin:monitored-technologies.open-tracing-native)`

By default, Envoy monitoring is disabled on all hosts. If you want to enable Envoy monitoring on selected hosts, enable it on these hosts via their settings.

If you want to disable Envoy monitoring only on selected hosts, enable global Envoy monitoring and disable it on these hosts via their settings.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:monitored-technologies.open-tracing-native` | - | `HOST` - Host  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitored-technologies.open-tracing-native` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:monitored-technologies.open-tracing-native` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitored-technologies.open-tracing-native` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Monitor Envoy `enabled` | boolean | - | Required |