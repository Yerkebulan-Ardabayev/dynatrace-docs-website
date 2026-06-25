---
title: Settings API - Allowed attributes schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-attribute-allow-list
scraped: 2026-05-12T11:47:32.791958
---

# Settings API - Allowed attributes schema table

# Settings API - Allowed attributes schema table

* Published Dec 05, 2023

### Allowed attributes (`builtin:attribute-allow-list)`

While Dynatrace automatically captures all OpenTelemetry attributes, to prevent the accidental storage of personal data, only the values of attributes for which a related key is specified in the allow-list below are persisted. This enables you to meet your privacy requirements while controlling the amount of monitoring data that's persisted. For further details on Dynatrace's privacy settings, visit the [Data privacy and securityï»¿](https://dt-url.net/bo210srx) documentation.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:attribute-allow-list` | * `group:service-monitoring` * `group:service-monitoring.spans` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:attribute-allow-list` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:attribute-allow-list` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:attribute-allow-list` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | If this is true, the value of the specified key is persisted. | Required |
| Attribute key `key` | text | Key of the attribute to persist | Required |