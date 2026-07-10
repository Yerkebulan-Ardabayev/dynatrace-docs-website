---
title: Database anomaly detection API - GET configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-database/get-config
---

# Database anomaly detection API - GET configuration

# Database anomaly detection API - GET configuration

* Reference
* Published Aug 28, 2019

Gets the configuration of anomaly detection for database services.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/databaseServices` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/databaseServices` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [DatabaseAnomalyDetectionConfig](#openapi-definition-DatabaseAnomalyDetectionConfig) | Success |

### Response body objects

#### The `DatabaseAnomalyDetectionConfig` object

The configuration of the anomaly detection for database services.

| Element | Type | Description |
| --- | --- | --- |
| databaseConnectionFailureCount | [DatabaseConnectionFailureDetectionConfig](#openapi-definition-DatabaseConnectionFailureDetectionConfig) | Parameters of the failed database connections detection.  The alert is triggered when failed connections number exceeds **connectionFailsCount** during any **timePeriodMinutes** minutes period. |
| failureRateIncrease | [FailureRateIncreaseDetectionConfig](#openapi-definition-FailureRateIncreaseDetectionConfig) | Configuration of failure rate increase detection. |
| loadDrop | [LoadDropDetectionConfig](#openapi-definition-LoadDropDetectionConfig) | The configuration of load drops detection. |
| loadSpike | [LoadSpikeDetectionConfig](#openapi-definition-LoadSpikeDetectionConfig) | The configuration of load spikes detection. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging |
| responseTimeDegradation | [ResponseTimeDegradationDetectionConfig](#openapi-definition-ResponseTimeDegradationDetectionConfig) | Configuration of response time degradation detection. |

#### The `DatabaseConnectionFailureDetectionConfig` object

Parameters of the failed database connections detection.

The alert is triggered when failed connections number exceeds **connectionFailsCount** during any **timePeriodMinutes** minutes period.

| Element | Type | Description |
| --- | --- | --- |
| connectionFailsCount | integer | Number of failed database connections during any **timePeriodMinutes** minutes period to trigger an alert. |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). |
| timePeriodMinutes | integer | The *X* minutes time period during which the **connectionFailsCount** is evaluated. |

#### The `FailureRateIncreaseDetectionConfig` object

Configuration of failure rate increase detection.

| Element | Type | Description |
| --- | --- | --- |
| automaticDetection | [FailureRateIncreaseAutodetectionConfig](#openapi-definition-FailureRateIncreaseAutodetectionConfig) | Parameters of failure rate increase auto-detection. Required if **detectionMode** is `DETECT_AUTOMATICALLY`. Not applicable otherwise.  The absolute and relative thresholds **both** must exceed to trigger an alert.  Example: If the expected error rate is 1.5%, and you set an absolute increase of 1%, and a relative increase of 50%, the thresholds will be: Absolute: 1.5% + **1%** = 2.5% Relative: 1.5% + 1.5% \* **50%** = 2.25% |
| detectionMode | string | How to detect failure rate increase: automatically, or based on fixed thresholds, or do not detect. The element can hold these values * `DETECT_AUTOMATICALLY` * `DETECT_USING_FIXED_THRESHOLDS` * `DONT_DETECT` |
| thresholds | [FailureRateIncreaseThresholdConfig](#openapi-definition-FailureRateIncreaseThresholdConfig) | Fixed thresholds for failure rate increase detection.  Required if **detectionMode** is `DETECT_USING_FIXED_THRESHOLDS`. Not applicable otherwise. |

#### The `FailureRateIncreaseAutodetectionConfig` object

Parameters of failure rate increase auto-detection. Required if **detectionMode** is `DETECT_AUTOMATICALLY`. Not applicable otherwise.

The absolute and relative thresholds **both** must exceed to trigger an alert.

Example: If the expected error rate is 1.5%, and you set an absolute increase of 1%, and a relative increase of 50%, the thresholds will be:
Absolute: 1.5% + **1%** = 2.5%
Relative: 1.5% + 1.5% \* **50%** = 2.25%

| Element | Type | Description |
| --- | --- | --- |
| failingServiceCallPercentageIncreaseAbsolute | integer | Absolute increase of failing service calls to trigger an alert, %. |
| failingServiceCallPercentageIncreaseRelative | integer | Relative increase of failing service calls to trigger an alert, %. |

#### The `FailureRateIncreaseThresholdConfig` object

Fixed thresholds for failure rate increase detection.

Required if **detectionMode** is `DETECT_USING_FIXED_THRESHOLDS`. Not applicable otherwise.

| Element | Type | Description |
| --- | --- | --- |
| sensitivity | string | Sensitivity of the threshold.  With `low` sensitivity, high statistical confidence is used. Brief violations (for example, due to a surge in load) won't trigger alerts.  With `high` sensitivity, no statistical confidence is used. Each violation triggers alert. The element can hold these values * `HIGH` * `LOW` * `MEDIUM` |
| threshold | integer | Failure rate during any 5-minute period to trigger an alert, %. |

#### The `LoadDropDetectionConfig` object

The configuration of load drops detection.

| Element | Type | Description |
| --- | --- | --- |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). |
| loadDropPercent | integer | Alert if the observed load is less than *X* % of the expected value. |
| minAbnormalStateDurationInMinutes | integer | Alert if the service stays in abnormal state for at least *X* minutes. |

#### The `LoadSpikeDetectionConfig` object

The configuration of load spikes detection.

| Element | Type | Description |
| --- | --- | --- |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). |
| loadSpikePercent | integer | Alert if the observed load is more than *X* % of the expected value. |
| minAbnormalStateDurationInMinutes | integer | Alert if the service stays in abnormal state for at least *X* minutes. |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description |
| --- | --- | --- |
| clusterVersion | string | Dynatrace version. |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. |

#### The `ResponseTimeDegradationDetectionConfig` object

Configuration of response time degradation detection.

| Element | Type | Description |
| --- | --- | --- |
| automaticDetection | [ResponseTimeDegradationAutodetectionConfig](#openapi-definition-ResponseTimeDegradationAutodetectionConfig) | Parameters of the response time degradation auto-detection. Required if the **detectionMode** is `DETECT_AUTOMATICALLY`. Not applicable otherwise.  Violation of **any** criterion triggers an alert. |
| detectionMode | string | How to detect response time degradation: automatically, or based on fixed thresholds, or do not detect. The element can hold these values * `DETECT_AUTOMATICALLY` * `DETECT_USING_FIXED_THRESHOLDS` * `DONT_DETECT` |
| thresholds | [ResponseTimeDegradationThresholdConfig](#openapi-definition-ResponseTimeDegradationThresholdConfig) | Fixed thresholds for response time degradation detection.  Required if **detectionMode** is `DETECT_USING_FIXED_THRESHOLDS`. Not applicable otherwise. |

#### The `ResponseTimeDegradationAutodetectionConfig` object

Parameters of the response time degradation auto-detection. Required if the **detectionMode** is `DETECT_AUTOMATICALLY`. Not applicable otherwise.

Violation of **any** criterion triggers an alert.

| Element | Type | Description |
| --- | --- | --- |
| loadThreshold | string | Minimal service load to detect response time degradation.  Response time degradation of services with smaller load won't trigger alerts. The element can hold these values * `FIFTEEN_REQUESTS_PER_MINUTE` * `FIVE_REQUESTS_PER_MINUTE` * `ONE_REQUEST_PER_MINUTE` * `TEN_REQUESTS_PER_MINUTE` |
| responseTimeDegradationMilliseconds | integer | Alert if the response time degrades beyond *X* milliseconds. |
| responseTimeDegradationPercent | integer | Alert if the response time degrades beyond *X* %. |
| slowestResponseTimeDegradationMilliseconds | integer | Alert if the response time of the slowest 10% degrades beyond *X* milliseconds. |
| slowestResponseTimeDegradationPercent | integer | Alert if the response time of the slowest 10% degrades beyond *X* %. |

#### The `ResponseTimeDegradationThresholdConfig` object

Fixed thresholds for response time degradation detection.

Required if **detectionMode** is `DETECT_USING_FIXED_THRESHOLDS`. Not applicable otherwise.

| Element | Type | Description |
| --- | --- | --- |
| loadThreshold | string | Minimal service load to detect response time degradation.  Response time degradation of services with smaller load won't trigger alerts. The element can hold these values * `FIFTEEN_REQUESTS_PER_MINUTE` * `FIVE_REQUESTS_PER_MINUTE` * `ONE_REQUEST_PER_MINUTE` * `TEN_REQUESTS_PER_MINUTE` |
| responseTimeThresholdMilliseconds | integer | Response time during any 5-minute period to trigger an alert, in milliseconds. |
| sensitivity | string | Sensitivity of the threshold.  With `low` sensitivity, high statistical confidence is used. Brief violations (for example, due to a surge in load) won't trigger alerts.  With `high` sensitivity, no statistical confidence is used. Each violation triggers an alert. The element can hold these values * `HIGH` * `LOW` * `MEDIUM` |
| slowestResponseTimeThresholdMilliseconds | integer | Response time of the 10% slowest during any 5-minute period to trigger an alert, in milliseconds. |

### Response body JSON models

```
{



"databaseConnectionFailureCount": {



"connectionFailsCount": 5,



"enabled": "true",



"timePeriodMinutes": 5



},



"failureRateIncrease": {



"detectionMode": "DETECT_USING_FIXED_THRESHOLDS",



"thresholds": {



"sensitivity": "LOW",



"threshold": 10



}



},



"loadDrop": {



"enabled": true,



"loadDropPercent": 40,



"minAbnormalStateDurationInMinutes": 5



},



"loadSpike": {



"enabled": false



},



"responseTimeDegradation": {



"automaticDetection": {



"loadThreshold": "ONE_REQUEST_PER_MINUTE",



"responseTimeDegradationMilliseconds": 250,



"responseTimeDegradationPercent": 90,



"slowestResponseTimeDegradationMilliseconds": 500,



"slowestResponseTimeDegradationPercent": 200



},



"detectionMode": "DETECT_AUTOMATICALLY"



}



}
```

## Example

In this example, the request lists the current configuration of anomaly detection for database services.

The API token is passed in the **Authorization** header.

The configuration has the following settings:

![Anomaly detection config - database](https://dt-cdn.net/images/anomaly-detecion-database-760-a1cca17927.png)

Anomaly detection config - database

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/databaseServices \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/databaseServices
```

#### Response body

```
{



"metadata": {



"clusterVersion": "1.163.2.20190201-072431",



"configurationVersions": [



3



]



},



"responseTimeDegradation": {



"detectionMode": "DONT_DETECT"



},



"failureRateIncrease": {



"detectionMode": "DETECT_USING_FIXED_THRESHOLDS",



"thresholds": {



"threshold": 0,



"sensitivity": "LOW"



}



},



"databaseConnectionFailureCount": {



"enabled": true,



"connectionFailsCount": 5,



"timePeriodMinutes": 5



}



}
```

#### Response code

200

## Related topics

* [Adjust the sensitivity of anomaly detection for database services](/managed/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-services-database "Learn how to adapt the sensitivity of problem detection for database services.")
* [Unavailable in Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.")
* [Databases Services](/managed/observe/infrastructure-observability/databases "Learn how to automatically detect database services, how to analyze database services, and more.")