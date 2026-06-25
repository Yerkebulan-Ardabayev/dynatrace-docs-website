---
title: Settings API - Enable endpoint detection schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-endpoint-detection-rules-opt-in
scraped: 2026-05-12T11:38:58.881074
---

# Settings API - Enable endpoint detection schema table

# Settings API - Enable endpoint detection schema table

* Published Aug 25, 2025

### Enable endpoint detection (`builtin:endpoint-detection-rules-opt-in)`

Enable SDv2 endpoint detection rules (`<your-dynatrace-url>/builtin:endpoint-detection-rules`) instead of the hard-coded ones. See [Service Detection v2 documentationï»¿](https://dt-url.net/lu030qq) and [community postï»¿](https://dt-url.net/r2230n9) for details.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:endpoint-detection-rules-opt-in` | * `group:service-detection` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:endpoint-detection-rules-opt-in` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:endpoint-detection-rules-opt-in` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:endpoint-detection-rules-opt-in` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enable Endpoint detection rules `enabled` | boolean | If enabled, the new endpoint detection rules will be active. | Required |