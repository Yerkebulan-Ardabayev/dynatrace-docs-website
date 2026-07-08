---
title: Settings API - Vulnerability Analytics- Monitoring rules for third-party vulnerabilities schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-appsec-rule-settings
---

# Settings API - Vulnerability Analytics- Monitoring rules for third-party vulnerabilities schema table

# Settings API - Vulnerability Analytics- Monitoring rules for third-party vulnerabilities schema table

* Published Dec 05, 2023

### Vulnerability Analytics: Monitoring rules for third-party vulnerabilities (`builtin:appsec.rule-settings)`

The global third-party vulnerability detection control defines the default monitoring mode. To override the default, define custom monitoring rules here. Note that monitoring rules are ordered; the first matching rule applies.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:appsec.rule-settings` | * `group:appsec.vulnerability-analytics` * `group:appsec` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:appsec.rule-settings` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:appsec.rule-settings` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:appsec.rule-settings` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | - | Required |
| Control `mode` | enum | The element has these enums * `MONITORING_OFF` * `MONITORING_ON` | Required |
| Property `property` | enum | The element has these enums * `PROCESS_TAG` * `HOST_TAG` * `MANAGEMENT_ZONE` | Required |
| Condition operator `operator` | enum | The element has these enums * `EQUALS` * `NOT_EQUALS` | Required |
| Condition value `value` | text | - | Required |