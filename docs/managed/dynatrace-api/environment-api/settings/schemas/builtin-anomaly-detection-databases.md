---
title: Settings API - Anomaly detection for databases schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-anomaly-detection-databases
scraped: 2026-05-12T11:40:35.881643
---

# Settings API - Anomaly detection for databases schema table

# Settings API - Anomaly detection for databases schema table

* Published Dec 05, 2023

### Anomaly detection for databases (`builtin:anomaly-detection.databases)`

Dynatrace automatically detects database-service related performance anomalies such as response time degradations and failure rate increases.

Use these settings to configure detection sensitivity, set alert thresholds, or disable alerting for certain services. Read more about [Automated multi-dimensional baseliningï»¿](https://dt-url.net/5r5p0pnz/ "Visit Dynatrace support center").

To avoid false-positive problem notifications, [automated anomaly detectionï»¿](https://dt-url.net/5r5p0pnz/ "Visit Dynatrace support center") is only available for applications and services that have run for at least 20% of a week (7 days).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:anomaly-detection.databases` | * `group:anomaly-detection` | `SERVICE_METHOD` - Request  `SERVICE` - Service  `HOST_GROUP` - Host Group  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.databases` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:anomaly-detection.databases` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.databases` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Response time `responseTime` | [responseTime](#responseTime) | - | Required |
| Failure rate `failureRate` | [failureRate](#failureRate) | - | Required |
| Service load drops `loadDrops` | [loadDrops](#loadDrops) | Alert if the observed load is lower than the expected load by a specified margin for a specified amount of time.  Dynatrace learns your typical service load over an observation period of one week. | Required |
| Service load spikes `loadSpikes` | [loadSpikes](#loadSpikes) | Alert if the observed load exceeds the expected load by a specified margin for a specified amount of time.  Dynatrace learns your typical service load over an observation period of one week. | Required |
| Database failed connects `databaseConnections` | [databaseConnections](#databaseConnections) | Alert if the number of failed database connects within the specified time exceeds the specified absolute threshold: | Required |

##### The `responseTime` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect response time degradations `enabled` | boolean | - | Required |
| Detection mode for response time degradations `detectionMode` | enum | The element has these enums * `auto` * `fixed` | Required |
| `autoDetection` | [responseTimeAuto](#responseTimeAuto) | - | Required |
| `fixedDetection` | [responseTimeFixed](#responseTimeFixed) | - | Required |

##### The `failureRate` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect increases in failure rate `enabled` | boolean | - | Required |
| Detection mode for increases in failure rate `detectionMode` | enum | The element has these enums * `auto` * `fixed` | Required |
| `autoDetection` | [failureRateAuto](#failureRateAuto) | Alert if the percentage of failing service calls increases by **both** the absolute and relative thresholds: | Required |
| `fixedDetection` | [failureRateFixed](#failureRateFixed) | Alert if a given failure rate is exceeded during any 5-minute-period | Required |

##### The `loadDrops` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect service load drops `enabled` | boolean | - | Required |
| Alert if the observed load is less than this percentage of the expected value `loadDropPercent` | float | - | Required |
| Time span `minutesAbnormalState` | integer | - | Required |

##### The `loadSpikes` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect service load spikes `enabled` | boolean | - | Required |
| Alert if the observed load is more than this percentage of the expected value `loadSpikePercent` | float | - | Required |
| Time span `minutesAbnormalState` | integer | - | Required |

##### The `databaseConnections` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect failed database connects `enabled` | boolean | - | Required |
| Threshold `maxFailedConnects` | integer | - | Required |
| Time span `timePeriod` | integer | - | Required |

##### The `responseTimeAuto` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| All requests `responseTimeAll` | [responseTimeAutoAll](#responseTimeAutoAll) | Alert if the median response time of all requests degrades beyond **both** the absolute and relative thresholds: | Required |
| Slowest 10% `responseTimeSlowest` | [responseTimeAutoSlowest](#responseTimeAutoSlowest) | Alert if the response time of the slowest 10% of requests degrades beyond **both** the absolute and relative thresholds: | Required |
| Avoid over-alerting `overAlertingProtection` | [overAlertingProtection](#overAlertingProtection) | - | Required |

##### The `responseTimeFixed` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| All requests `responseTimeAll` | [responseTimeFixedAll](#responseTimeFixedAll) | Alert if the median response time of all requests degrades beyond this threshold within an observation period of 5 minutes: | Required |
| Slowest 10% `responseTimeSlowest` | [responseTimeFixedSlowest](#responseTimeFixedSlowest) | Alert if the response time of the slowest 10% of requests degrades beyond this threshold within an observation period of 5 minutes: | Required |
| Avoid over-alerting `overAlertingProtection` | [overAlertingProtection](#overAlertingProtection) | - | Required |
| Sensitivity `sensitivity` | enum | The element has these enums * `low` * `medium` * `high` | Required |

##### The `failureRateAuto` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Absolute threshold `absoluteIncrease` | float | - | Required |
| Relative threshold `relativeIncrease` | float | - | Required |
| Avoid over-alerting `overAlertingProtection` | [overAlertingProtection](#overAlertingProtection) | - | Required |

##### The `failureRateFixed` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Threshold `threshold` | float | - | Required |
| Avoid over-alerting `overAlertingProtection` | [overAlertingProtection](#overAlertingProtection) | - | Required |
| Sensitivity `sensitivity` | enum | The element has these enums * `low` * `medium` * `high` | Required |

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

##### The `overAlertingProtection` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Only alert if there are at least `requestsPerMinute` | float | - | Required |
| Only alert if the abnormal state remains for at least `minutesAbnormalState` | integer | - | Required |

##### The `responseTimeFixedAll` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Threshold `degradationMilliseconds` | float | - | Required |

##### The `responseTimeFixedSlowest` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Threshold `slowestDegradationMilliseconds` | float | - | Required |