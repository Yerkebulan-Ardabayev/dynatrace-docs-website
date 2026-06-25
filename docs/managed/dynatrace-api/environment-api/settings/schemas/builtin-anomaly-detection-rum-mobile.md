---
title: Settings API - Anomaly detection for mobile applications schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-anomaly-detection-rum-mobile
scraped: 2026-05-12T11:41:53.444385
---

# Settings API - Anomaly detection for mobile applications schema table

# Settings API - Anomaly detection for mobile applications schema table

* Published Dec 05, 2023

### Anomaly detection for mobile applications (`builtin:anomaly-detection.rum-mobile)`

Dynatrace automatically detects application-related performance anomalies such as response time degradations and traffic spikes. Use these settings to configure detection sensitivity, set alert thresholds, or disable alerting for certain applications.

To avoid false-positive problem notifications, [automated anomaly detectionï»¿](https://dt-url.net/op03t6j "Visit Dynatrace support center") is only available for applications and services that have run for at least 20% of a week (7 days).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:anomaly-detection.rum-mobile` | * `group:anomaly-detection` | `DEVICE_APPLICATION_METHOD` - Mobile app key user action  `MOBILE_APPLICATION` - Mobile App  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.rum-mobile` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:anomaly-detection.rum-mobile` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.rum-mobile` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Error rate increase `errorRateIncrease` | [ErrorRateIncrease](#ErrorRateIncrease) | - | Required |
| Slow user actions `slowUserActions` | [SlowUserActions](#SlowUserActions) | - | Required |
| Unexpected low load `unexpectedLowLoad` | [UnexpectedLowLoad](#UnexpectedLowLoad) | - | Required |
| Unexpected high load `unexpectedHighLoad` | [UnexpectedHighLoad](#UnexpectedHighLoad) | - | Required |

##### The `ErrorRateIncrease` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect reported error rate increase `enabled` | boolean | - | Required |
| Detection strategy for error rate increases `detectionMode` | enum | The element has these enums * `auto` * `fixed` | Required |
| `errorRateIncreaseAuto` | [ErrorRateIncreaseAuto](#ErrorRateIncreaseAuto) | Alert if the percentage of user actions affected by reported errors exceeds **both** the absolute threshold and the relative threshold | Required |
| `errorRateIncreaseFixed` | [ErrorRateIncreaseFixed](#ErrorRateIncreaseFixed) | Alert if the custom reported error rate threshold is exceeded during any 5-minute period | Required |

##### The `SlowUserActions` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect slow user actions `enabled` | boolean | - | Required |
| Detection strategy for slow user actions `detectionMode` | enum | The element has these enums * `auto` * `fixed` | Required |
| `slowUserActionsAuto` | [SlowUserActionsAuto](#SlowUserActionsAuto) | - | Required |
| `slowUserActionsFixed` | [SlowUserActionsFixed](#SlowUserActionsFixed) | - | Required |

##### The `UnexpectedLowLoad` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect unexpected low load `enabled` | boolean | - | Required |
| Alert if the observed traffic drops below this threshold `thresholdPercentage` | float | Dynatrace learns your typical application traffic over an observation period of one week. Depending on this expected value Dynatrace detects abnormal traffic drops within your application. | Required |

##### The `UnexpectedHighLoad` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect unexpected high load `enabled` | boolean | - | Required |
| Alert if the observed traffic exceeds this threshold `thresholdPercentage` | float | Dynatrace learns your typical application traffic over an observation period of one week. Depending on this expected value Dynatrace detects abnormal traffic spikes within your application. | Required |

##### The `ErrorRateIncreaseAuto` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Absolute threshold `thresholdAbsolute` | float | - | Required |
| Relative threshold `thresholdRelative` | float | - | Required |

##### The `ErrorRateIncreaseFixed` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Absolute threshold `thresholdAbsolute` | float | - | Required |
| Detection sensitivity `sensitivity` | enum | The element has these enums * `low` * `medium` * `high` | Required |

##### The `SlowUserActionsAuto` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| All user actions `durationThresholdAll` | [SlowUserActionsAutoAll](#SlowUserActionsAutoAll) | Alert if the action duration of all user actions degrades beyond **both** the absolute and relative threshold: | Required |
| Slowest 10% `durationThresholdSlowest` | [SlowUserActionsAutoSlowest](#SlowUserActionsAutoSlowest) | Alert if the action duration of the slowest 10% of user actions degrades beyond **both** the absolute and relative threshold: | Required |
| Avoid over-alerting `durationAvoidOveralerting` | [SlowUserActionsAvoidOveralerting](#SlowUserActionsAvoidOveralerting) | To avoid over-alerting do not alert for low traffic applications with less than | Required |

##### The `SlowUserActionsFixed` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| All user actions `durationThresholdAllFixed` | [SlowUserActionsManualAll](#SlowUserActionsManualAll) | Alert if the action duration of all user actions degrades beyond the absolute threshold: | Required |
| Slowest 10% `durationThresholdSlowest` | [SlowUserActionsManualSlowest](#SlowUserActionsManualSlowest) | Alert if the action duration of the slowest 10% of user actions degrades beyond the absolute threshold: | Required |
| Avoid over-alerting `durationAvoidOveralerting` | [SlowUserActionsAvoidOveralerting](#SlowUserActionsAvoidOveralerting) | To avoid over-alerting do not alert for low traffic applications with less than | Required |
| Detection sensitivity `sensitivity` | enum | The element has these enums * `low` * `medium` * `high` | Required |

##### The `SlowUserActionsAutoAll` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Absolute threshold `durationThreshold` | float | - | Required |
| Relative threshold `slowdownPercentage` | float | - | Required |

##### The `SlowUserActionsAutoSlowest` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Absolute threshold `durationThreshold` | float | - | Required |
| Relative threshold `slowdownPercentage` | float | - | Required |

##### The `SlowUserActionsAvoidOveralerting` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `minActionRate` | integer | - | Required |

##### The `SlowUserActionsManualAll` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Absolute threshold `durationThreshold` | float | - | Required |

##### The `SlowUserActionsManualSlowest` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Absolute threshold `durationThreshold` | float | - | Required |