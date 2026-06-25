---
title: Settings API - Preferences schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-attributes-preferences
scraped: 2026-05-12T11:40:33.794350
---

# Settings API - Preferences schema table

# Settings API - Preferences schema table

* Published Feb 26, 2024

### Preferences (`builtin:attributes-preferences)`

Define the default behavior of persisting OpenTelemetry attributes. You can either choose to store all attributes except certain blocked attributes or only store explicitly allowed attributes.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:attributes-preferences` | * `group:service-monitoring` * `group:service-monitoring.spans` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:attributes-preferences` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:attributes-preferences` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:attributes-preferences` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `persistenceMode` | enum | The element has these enums * `ALLOW_ALL_ATTRIBUTES` * `BLOCK_ALL_ATTRIBUTES` | Required |