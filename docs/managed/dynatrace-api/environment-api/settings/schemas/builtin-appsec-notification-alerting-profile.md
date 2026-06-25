---
title: Settings API - Vulnerability alerting profiles schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-appsec-notification-alerting-profile
scraped: 2026-05-12T11:49:20.284438
---

# Settings API - Vulnerability alerting profiles schema table

# Settings API - Vulnerability alerting profiles schema table

* Published Dec 05, 2023

### Vulnerability alerting profiles (`builtin:appsec.notification-alerting-profile)`

Vulnerability alerting profiles enable you to set up alert-filtering rules that are based on the risk level of detected vulnerabilities. This allows you to control which conditions result in security notifications and which don't.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:appsec.notification-alerting-profile` | * `group:alerting.appsec` * `group:alerting` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:appsec.notification-alerting-profile` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:appsec.notification-alerting-profile` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:appsec.notification-alerting-profile` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | - | Required |
| Name `name` | text | - | Required |
| Alert for the following events: `enabledTriggerEvents` | Set<[TriggerEvent](#TriggerEvent)> | The element has these enums * `SECURITY_PROBLEM_OPENED` * `NEW_MANAGEMENT_ZONE_AFFECTED` | Required |
| Alert only if the following management zone is affected (optional) `managementZone` | setting | - | Optional |
| Risk Levels `enabledRiskLevels` | Set<[RiskLevel](#RiskLevel)> | The element has these enums * `CRITICAL` * `HIGH` * `MEDIUM` * `LOW` | Required |