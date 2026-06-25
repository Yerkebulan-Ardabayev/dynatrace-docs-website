---
title: Application anomaly detection API - GET configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-applications/get-config
scraped: 2026-05-12T11:21:27.272677
---

# Application anomaly detection API - GET configuration

# Application anomaly detection API - GET configuration

* Reference
* Published Jan 23, 2019

Gets the configuration of anomaly detection for applications.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/applications` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/applications` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ApplicationAnomalyDetectionConfig](#openapi-definition-ApplicationAnomalyDetectionConfig) | Success |

### Response body objects

#### The `ApplicationAnomalyDetectionConfig` object

The configuration of anomaly detection for applications.

| Element | Type | Description |
| --- | --- | --- |
| failureRateIncrease | [FailureRateIncreaseDetectionConfig](#openapi-definition-FailureRateIncreaseDetectionConfig) | Configuration of failure rate increase detection. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging |
| responseTimeDegradation | [ResponseTimeDegradationDetectionConfig](#openapi-definition-ResponseTimeDegradationDetectionConfig) | Configuration of response time degradation detection. |
| trafficDrop | [TrafficDropDetectionConfig](#openapi-definition-TrafficDropDetectionConfig) | The configuration of traffic drops detection. |
| trafficSpike | [TrafficSpikeDetectionConfig](#openapi-definition-TrafficSpikeDetectionConfig) | The configuration of traffic spikes detection. |

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

#### The `TrafficDropDetectionConfig` object

The configuration of traffic drops detection.

| Element | Type | Description |
| --- | --- | --- |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). |
| trafficDropPercent | integer | Alert if the observed traffic is less than *X* % of the expected value. |

#### The `TrafficSpikeDetectionConfig` object

The configuration of traffic spikes detection.

| Element | Type | Description |
| --- | --- | --- |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). |
| trafficSpikePercent | integer | Alert if the observed traffic is more than *X* % of the expected value. |

### Response body JSON models

```
{



"failureRateIncrease": {



"detectionMode": "DETECT_USING_FIXED_THRESHOLDS",



"thresholds": {



"sensitivity": "LOW",



"threshold": 10



}



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



},



"trafficDrop": {



"enabled": true,



"trafficDropPercent": 95



},



"trafficSpike": {



"enabled": false



}



}
```

## Example

In this example, the request lists the current configuration of anomaly detection for applications.

The API token is passed in the **Authorization** header.

The configuration has the following settings:

![Anomaly detection config - apps](https://dt-cdn.net/images/anomaly-detectoin-apps-971-b365c7a5c0.png)

Anomaly detection config - apps

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/applications \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/applications
```

#### Response body

```
{



"metadata": {



"clusterVersion": "1.163.0.20190130-210004",



"configurationVersions": [



2



]



},



"responseTimeDegradation": {



"detectionMode": "DETECT_AUTOMATICALLY",



"automaticDetection": {



"responseTimeDegradationMilliseconds": 100,



"responseTimeDegradationPercent": 50,



"slowestResponseTimeDegradationMilliseconds": 1000,



"slowestResponseTimeDegradationPercent": 10,



"loadThreshold": "TEN_REQUESTS_PER_MINUTE"



}



},



"trafficDrop": {



"enabled": true,



"trafficDropPercent": 50



},



"trafficSpike": {



"enabled": false



},



"failureRateIncrease": {



"detectionMode": "DETECT_AUTOMATICALLY",



"automaticDetection": {



"failingServiceCallPercentageIncreaseAbsolute": 5,



"failingServiceCallPercentageIncreaseRelative": 50



}



}



}
```

#### Response code

200

## Related topics

* [Adjust the sensitivity of anomaly detection for applications](/managed/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-applications "Learn how to adapt the sensitivity of problem detection for applications.")
* [DavisÂ® AI](/managed/dynatrace-intelligence "Get familiar with the capabilities of Davis AI.")