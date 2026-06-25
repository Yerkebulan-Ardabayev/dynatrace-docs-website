---
title: Settings API - Limit outbound connections schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-dt-javascript-runtime-allowed-outbound-connections
scraped: 2026-05-12T11:43:19.870451
---

# Settings API - Limit outbound connections schema table

# Settings API - Limit outbound connections schema table

* Published Dec 05, 2023

### Limit outbound connections (`builtin:dt-javascript-runtime.allowed-outbound-connections)`

You can limit the accessibility of public endpoints from functions running in the Dynatrace JavaScript Runtime, for example, the backends of apps and functions written in the Dashboards, Notebooks and Automations app.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:dt-javascript-runtime.allowed-outbound-connections` | * `group:dt-javascript-runtime` * `group:preferences` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:dt-javascript-runtime.allowed-outbound-connections` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:dt-javascript-runtime.allowed-outbound-connections` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:dt-javascript-runtime.allowed-outbound-connections` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `allowedOutboundConnections` | [AllowedHostsList](#AllowedHostsList) | - | Required |

##### The `AllowedHostsList` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Limit outbound connections to endpoints in the allowlist `enforced` | boolean | If enabled, the Dynatrace JavaScript Runtime will only be able to connect to the specified hosts. | Required |
| Allowlist `hostList` | set | A host that app backends should be able to connect to. | Required |