---
title: Settings API - Blocked attributes schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-attribute-block-list
scraped: 2026-05-12T11:40:57.640587
---

# Settings API - Blocked attributes schema table

# Settings API - Blocked attributes schema table

* Published Feb 26, 2024

### Blocked attributes (`builtin:attribute-block-list)`

While Dynatrace automatically captures all OpenTelemetry attributes, to prevent the accidental storage of personal data, you may exclude certain attribute keys for which the values must not be persisted. This enables you to meet your privacy requirements while controlling the amount of monitoring data that's persisted. For further details on Dynatrace's privacy settings, visit the [Data privacy and securityï»¿](https://dt-url.net/bo210srx) documentation.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:attribute-block-list` | * `group:service-monitoring` * `group:service-monitoring.spans` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:attribute-block-list` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:attribute-block-list` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:attribute-block-list` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | If this is true, the value of the specified key is not persisted. | Required |
| Attribute key `key` | text | Key of the attribute that should not be persisted | Required |