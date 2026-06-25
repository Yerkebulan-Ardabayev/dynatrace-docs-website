---
title: Settings API - Crash rate increase settings for custom applications schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-anomaly-detection-rum-custom-crash-rate-increase
scraped: 2026-05-12T11:49:45.658502
---

# Settings API - Crash rate increase settings for custom applications schema table

# Settings API - Crash rate increase settings for custom applications schema table

* Published Dec 05, 2023

### Crash rate increase settings for custom applications (`builtin:anomaly-detection.rum-custom-crash-rate-increase)`

Dynatrace automatically detects application-related performance anomalies such as failure rate increases. Use these settings to configure detection sensitivity, set alert thresholds, or disable alerting for certain applications.

To avoid false-positive problem notifications, [automated anomaly detectionï»¿](https://dt-url.net/op03t6j "Visit Dynatrace support center") is only available for applications and services that have run for at least 20% of a week (7 days).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:anomaly-detection.rum-custom-crash-rate-increase` | * `group:anomaly-detection` | `CUSTOM_APPLICATION` - Custom Application  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.rum-custom-crash-rate-increase` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:anomaly-detection.rum-custom-crash-rate-increase` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.rum-custom-crash-rate-increase` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Crash rate increase `crashRateIncrease` | [CrashRateIncrease](#CrashRateIncrease) | - | Required |

##### The `CrashRateIncrease` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect crash rate increase `enabled` | boolean | - | Required |
| Detection strategy for crash rate increases `detectionMode` | enum | The element has these enums * `auto` * `fixed` | Required |
| `crashRateIncreaseAuto` | [CrashRateIncreaseAuto](#CrashRateIncreaseAuto) | Alert to crash rate increases when the auto-detected baseline is exceeded and the application has a minimum number of active, non-distinctive users. | Required |
| `crashRateIncreaseFixed` | [CrashRateIncreaseFixed](#CrashRateIncreaseFixed) | Alert to crash rate increases when the defined threshold is exceeded and the application has a minimum number of active, non-distinctive users. | Required |

##### The `CrashRateIncreaseAuto` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Relative threshold `baselineViolationPercentage` | float | Dynatrace learns the typical crash rate for all app versions and will create an alert if the baseline is violated by more than a specified threshold. Analysis happens based on a sliding window of 10 minutes. | Required |
| Minimum number of active, non-distinctive users `concurrentUsers` | float | - | Required |
| Detection sensitivity `sensitivity` | enum | The element has these enums * `low` * `medium` * `high` | Required |

##### The `CrashRateIncreaseFixed` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Absolute threshold `absoluteCrashRate` | float | - | Required |
| Minimum number of active, non-distinctive users `concurrentUsers` | integer | - | Required |