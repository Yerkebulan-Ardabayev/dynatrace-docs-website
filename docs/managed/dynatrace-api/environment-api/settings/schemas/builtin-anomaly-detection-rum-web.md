---
title: Settings API - Anomaly detection for applications schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-anomaly-detection-rum-web
---

# Settings API - Anomaly detection for applications schema table

# Settings API - Anomaly detection for applications schema table

* Published Dec 05, 2023

### Anomaly detection for applications (`builtin:anomaly-detection.rum-web)`

Dynatrace automatically detects application-related performance anomalies such as response time degradations, failure rate increases, and traffic spikes. Use these settings to configure detection sensitivity, set alert thresholds, or disable alerting for certain applications.

To avoid false-positive problem notifications, [automated anomaly detection﻿](https://dt-url.net/op03t6j "Visit Dynatrace support center") is only available for applications and services that have run for at least 20% of a week (7 days).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:anomaly-detection.rum-web` | * `group:anomaly-detection` | `APPLICATION_METHOD` - User Action  `APPLICATION` - Web application  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.rum-web` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:anomaly-detection.rum-web` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.rum-web` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Response time `responseTime` | [responseTime](#responseTime) | - | Required |
| Error rate `errorRate` | [errorRate](#errorRate) | - | Required |
| Detect traffic drops `trafficDrops` | [appTrafficDrops](#appTrafficDrops) | - | Required |
| Detect traffic spikes `trafficSpikes` | [appTrafficSpikes](#appTrafficSpikes) | - | Required |

##### The `responseTime` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect key performance metric degradations `enabled` | boolean | - | Required |
| Detection strategy for key performance metric degradations `detectionMode` | enum | The element has these enums * `auto` * `fixed` | Required |
| `responseTimeAuto` | [responseTimeAuto](#responseTimeAuto) | - | Required |
| `responseTimeFixed` | [responseTimeFixed](#responseTimeFixed) | - | Required |

##### The `errorRate` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect increases in JavaScript errors `enabled` | boolean | - | Required |
| Detection strategy for increases in JavaScript errors `errorRateDetectionMode` | enum | The element has these enums * `auto` * `fixed` | Required |
| `errorRateAuto` | [errorRateAuto](#errorRateAuto) | Alert if the percentage of failing user actions increases by **both** the absolute and relative thresholds: | Required |
| `errorRateFixed` | [errorRateFixed](#errorRateFixed) | - | Required |

##### The `appTrafficDrops` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect traffic drops `enabled` | boolean | - | Required |
| `trafficDrops` | [trafficDrops](#trafficDrops) | Dynatrace learns your typical application traffic over an observation period of one week.  Depending on this expected value Dynatrace detects abnormal traffic drops within your application. | Required |

##### The `appTrafficSpikes` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect traffic spikes `enabled` | boolean | - | Required |
| `trafficSpikes` | [trafficSpikes](#trafficSpikes) | Dynatrace learns your typical application traffic over an observation period of one week.  Depending on this expected value Dynatrace detects abnormal traffic spikes within your application. | Required |

##### The `responseTimeAuto` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| All user actions `responseTimeAll` | [responseTimeAutoAll](#responseTimeAutoAll) | Alert if the median response time of all user actions degrades beyond **both** the absolute and relative thresholds: | Required |
| Slowest 10% `responseTimeSlowest` | [responseTimeAutoSlowest](#responseTimeAutoSlowest) | Alert if the response time of the slowest 10% of requests degrades beyond **both** the absolute and relative thresholds: | Required |
| Avoid over-alerting `overAlertingProtection` | [overAlertingProtectionAuto](#overAlertingProtectionAuto) | - | Required |

##### The `responseTimeFixed` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| All user actions `responseTimeAll` | [responseTimeFixedAll](#responseTimeFixedAll) | Alert if the key performance metric of all requests degrades beyond this threshold: | Required |
| Slowest 10% `responseTimeSlowest` | [responseTimeFixedSlowest](#responseTimeFixedSlowest) | Alert if the key performance metric of the slowest 10% of requests degrades beyond this threshold: | Required |
| Avoid over-alerting `overAlertingProtection` | [overAlertingProtectionAuto](#overAlertingProtectionAuto) | - | Required |
| Sensitivity `sensitivity` | enum | The element has these enums * `low` * `medium` * `high` | Required |

##### The `errorRateAuto` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Absolute threshold `absoluteIncrease` | float | - | Required |
| Relative threshold `relativeIncrease` | float | - | Required |
| Avoid over-alerting `overAlertingProtection` | [overAlertingProtectionAuto](#overAlertingProtectionAuto) | - | Required |

##### The `errorRateFixed` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Alert if this custom error rate threshold is exceeded during any 5-minute-period `maxFailureRateIncrease` | float | - | Required |
| Minimum number of actions per minute `errorRateReqPerMin` | float | To avoid over-alerting for low traffic applications | Required |
| Sensitivity `errorRateSensitivity` | enum | The element has these enums * `low` * `medium` * `high` | Required |
| Amount of minutes the observed traffic has to stay in abnormal state before alert `minutesAbnormalState` | float | - | Required |

##### The `trafficDrops` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Alert if the observed traffic is less than this percentage of the expected value `trafficDropPercentage` | float | - | Required |
| Minutes the observed traffic has to stay in abnormal state before alert `abnormalStateAbnormalState` | float | - | Required |

##### The `trafficSpikes` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Alert if the observed traffic is more than this percentage of the expected value `trafficSpikePercentage` | float | - | Required |
| Minutes an application has to stay in abnormal state before alert `minutesAbnormalState` | float | - | Required |

##### The `responseTimeAutoAll` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Absolute threshold `degradationMilliseconds` | float | - | Required |
| Relative threshold `degradationPercent` | float | - | Required |

##### The `responseTimeAutoSlowest` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Absolute threshold `slowestDegradationMilliseconds` | float | - | Required |
| Relative threshold `slowestDegradationPercent` | float | - | Required |

##### The `overAlertingProtectionAuto` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Minimum number of actions per minute `actionsPerMinute` | float | Only alert if there are at least | Required |
| Only alert if the abnormal state remains for at least `minutesAbnormalState` | float | - | Required |

##### The `responseTimeFixedAll` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Alert if the key performance metric degrades beyond this many ms within an observation period of 5 minutes `degradationMilliseconds` | float | - | Required |

##### The `responseTimeFixedSlowest` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Alert if the key performance metric of the slowest 10% degrades beyond this many ms within an observation period of 5 minutes `slowestDegradationMilliseconds` | float | - | Required |