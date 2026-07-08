---
title: Settings API - Attack alerting profiles schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-appsec-notification-attack-alerting-profile
---

# Settings API - Attack alerting profiles schema table

# Settings API - Attack alerting profiles schema table

* Published Dec 05, 2023

### Attack alerting profiles (`builtin:appsec.notification-attack-alerting-profile)`

Attack alerting profiles enable you to set up alert-filtering rules that are based on the state of detected attacks. This allows you to control which conditions result in security notifications and which don't.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:appsec.notification-attack-alerting-profile` | * `group:alerting.appsec` * `group:alerting` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:appsec.notification-attack-alerting-profile` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:appsec.notification-attack-alerting-profile` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:appsec.notification-attack-alerting-profile` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | - | Required |
| Name `name` | text | - | Required |
| Attack State `enabledAttackMitigations` | Set<[AttackMitigation](#AttackMitigation)> | The element has these enums * `NONE_BLOCKING_DISABLED` * `BLOCKED_WITH_EXCEPTION` * `NONE_ALLOWLISTED` | Required |