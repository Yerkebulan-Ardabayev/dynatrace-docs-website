---
title: Application anomaly detection API - PUT configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-applications/put-config
---

# Application anomaly detection API - PUT configuration

# Application anomaly detection API - PUT configuration

* Reference
* Published Jan 23, 2019

Updates the configuration of anomaly detection for applications.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/applications` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/applications` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [ApplicationAnomalyDetectionConfig](#openapi-definition-ApplicationAnomalyDetectionConfig) | The JSON body of the request, containing parameters of the application anomaly detection configuration. | body | Optional |

### Request body objects

#### The `ApplicationAnomalyDetectionConfig` object

The configuration of anomaly detection for applications.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| failureRateIncrease | [FailureRateIncreaseDetectionConfig](#openapi-definition-FailureRateIncreaseDetectionConfig) | Configuration of failure rate increase detection. | Required |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging | Optional |
| responseTimeDegradation | [ResponseTimeDegradationDetectionConfig](#openapi-definition-ResponseTimeDegradationDetectionConfig) | Configuration of response time degradation detection. | Required |
| trafficDrop | [TrafficDropDetectionConfig](#openapi-definition-TrafficDropDetectionConfig) | The configuration of traffic drops detection. | Required |
| trafficSpike | [TrafficSpikeDetectionConfig](#openapi-definition-TrafficSpikeDetectionConfig) | The configuration of traffic spikes detection. | Required |

#### The `FailureRateIncreaseDetectionConfig` object

Configuration of failure rate increase detection.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| automaticDetection | [FailureRateIncreaseAutodetectionConfig](#openapi-definition-FailureRateIncreaseAutodetectionConfig) | Parameters of failure rate increase auto-detection. Required if **detectionMode** is `DETECT_AUTOMATICALLY`. Not applicable otherwise.  The absolute and relative thresholds **both** must exceed to trigger an alert.  Example: If the expected error rate is 1.5%, and you set an absolute increase of 1%, and a relative increase of 50%, the thresholds will be: Absolute: 1.5% + **1%** = 2.5% Relative: 1.5% + 1.5% \* **50%** = 2.25% | Optional |
| detectionMode | string | How to detect failure rate increase: automatically, or based on fixed thresholds, or do not detect. The element can hold these values * `DETECT_AUTOMATICALLY` * `DETECT_USING_FIXED_THRESHOLDS` * `DONT_DETECT` | Required |
| thresholds | [FailureRateIncreaseThresholdConfig](#openapi-definition-FailureRateIncreaseThresholdConfig) | Fixed thresholds for failure rate increase detection.  Required if **detectionMode** is `DETECT_USING_FIXED_THRESHOLDS`. Not applicable otherwise. | Optional |

#### The `FailureRateIncreaseAutodetectionConfig` object

Parameters of failure rate increase auto-detection. Required if **detectionMode** is `DETECT_AUTOMATICALLY`. Not applicable otherwise.

The absolute and relative thresholds **both** must exceed to trigger an alert.

Example: If the expected error rate is 1.5%, and you set an absolute increase of 1%, and a relative increase of 50%, the thresholds will be:
Absolute: 1.5% + **1%** = 2.5%
Relative: 1.5% + 1.5% \* **50%** = 2.25%

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| failingServiceCallPercentageIncreaseAbsolute | integer | Absolute increase of failing service calls to trigger an alert, %. | Required |
| failingServiceCallPercentageIncreaseRelative | integer | Relative increase of failing service calls to trigger an alert, %. | Required |

#### The `FailureRateIncreaseThresholdConfig` object

Fixed thresholds for failure rate increase detection.

Required if **detectionMode** is `DETECT_USING_FIXED_THRESHOLDS`. Not applicable otherwise.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| sensitivity | string | Sensitivity of the threshold.  With `low` sensitivity, high statistical confidence is used. Brief violations (for example, due to a surge in load) won't trigger alerts.  With `high` sensitivity, no statistical confidence is used. Each violation triggers alert. The element can hold these values * `HIGH` * `LOW` * `MEDIUM` | Required |
| threshold | integer | Failure rate during any 5-minute period to trigger an alert, %. | Required |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| clusterVersion | string | Dynatrace version. | Optional |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. | Optional |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. | Optional |

#### The `ResponseTimeDegradationDetectionConfig` object

Configuration of response time degradation detection.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| automaticDetection | [ResponseTimeDegradationAutodetectionConfig](#openapi-definition-ResponseTimeDegradationAutodetectionConfig) | Parameters of the response time degradation auto-detection. Required if the **detectionMode** is `DETECT_AUTOMATICALLY`. Not applicable otherwise.  Violation of **any** criterion triggers an alert. | Optional |
| detectionMode | string | How to detect response time degradation: automatically, or based on fixed thresholds, or do not detect. The element can hold these values * `DETECT_AUTOMATICALLY` * `DETECT_USING_FIXED_THRESHOLDS` * `DONT_DETECT` | Required |
| thresholds | [ResponseTimeDegradationThresholdConfig](#openapi-definition-ResponseTimeDegradationThresholdConfig) | Fixed thresholds for response time degradation detection.  Required if **detectionMode** is `DETECT_USING_FIXED_THRESHOLDS`. Not applicable otherwise. | Optional |

#### The `ResponseTimeDegradationAutodetectionConfig` object

Parameters of the response time degradation auto-detection. Required if the **detectionMode** is `DETECT_AUTOMATICALLY`. Not applicable otherwise.

Violation of **any** criterion triggers an alert.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| loadThreshold | string | Minimal service load to detect response time degradation.  Response time degradation of services with smaller load won't trigger alerts. The element can hold these values * `FIFTEEN_REQUESTS_PER_MINUTE` * `FIVE_REQUESTS_PER_MINUTE` * `ONE_REQUEST_PER_MINUTE` * `TEN_REQUESTS_PER_MINUTE` | Required |
| responseTimeDegradationMilliseconds | integer | Alert if the response time degrades beyond *X* milliseconds. | Required |
| responseTimeDegradationPercent | integer | Alert if the response time degrades beyond *X* %. | Required |
| slowestResponseTimeDegradationMilliseconds | integer | Alert if the response time of the slowest 10% degrades beyond *X* milliseconds. | Required |
| slowestResponseTimeDegradationPercent | integer | Alert if the response time of the slowest 10% degrades beyond *X* %. | Required |

#### The `ResponseTimeDegradationThresholdConfig` object

Fixed thresholds for response time degradation detection.

Required if **detectionMode** is `DETECT_USING_FIXED_THRESHOLDS`. Not applicable otherwise.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| loadThreshold | string | Minimal service load to detect response time degradation.  Response time degradation of services with smaller load won't trigger alerts. The element can hold these values * `FIFTEEN_REQUESTS_PER_MINUTE` * `FIVE_REQUESTS_PER_MINUTE` * `ONE_REQUEST_PER_MINUTE` * `TEN_REQUESTS_PER_MINUTE` | Required |
| responseTimeThresholdMilliseconds | integer | Response time during any 5-minute period to trigger an alert, in milliseconds. | Required |
| sensitivity | string | Sensitivity of the threshold.  With `low` sensitivity, high statistical confidence is used. Brief violations (for example, due to a surge in load) won't trigger alerts.  With `high` sensitivity, no statistical confidence is used. Each violation triggers an alert. The element can hold these values * `HIGH` * `LOW` * `MEDIUM` | Required |
| slowestResponseTimeThresholdMilliseconds | integer | Response time of the 10% slowest during any 5-minute period to trigger an alert, in milliseconds. | Required |

#### The `TrafficDropDetectionConfig` object

The configuration of traffic drops detection.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). | Required |
| trafficDropPercent | integer | Alert if the observed traffic is less than *X* % of the expected value. | Optional |

#### The `TrafficSpikeDetectionConfig` object

The configuration of traffic spikes detection.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). | Required |
| trafficSpikePercent | integer | Alert if the observed traffic is more than *X* % of the expected value. | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

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

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. Configuration has been updated. Response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid |

### Response body objects

#### The `ErrorEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### The `Error` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | A list of constraint violations |
| message | string | The error message |

#### The `ConstraintViolation` object

A list of constraint violations

| Element | Type | Description |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -The element can hold these values * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Response body JSON models

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```

## Validate payload

We recommend that you validate the payload before submitting it with an actual request. A response code of **204** indicates a valid payload.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/applications/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/applications/validator` |

### Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Response

#### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Validated. The submitted configuration is valid. Response does not have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid |

#### Response body objects

#### The `ErrorEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### The `Error` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | A list of constraint violations |
| message | string | The error message |

#### The `ConstraintViolation` object

A list of constraint violations

| Element | Type | Description |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -The element can hold these values * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### Response body JSON models

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```

## Example

In this example, the request updates the configuration of anomaly detection for applications from the [GET request](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-applications/get-config#example "Read the configuration of anomaly detection for applications via the Dynatrace API.") example. It activates **traffic spikes detection** and sets the threshold of **200**%.

The API token is passed in the **Authorization** header.

You can download or copy the example request body to try it out on your own. Be sure to create a backup copy of your current configuration with the **GET application anomaly detection configuration** call.

#### Curl

```
curl -X PUT \



https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/applications \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



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



"enabled": true,



"trafficSpikePercent": 200



},



"failureRateIncrease": {



"detectionMode": "DETECT_AUTOMATICALLY",



"automaticDetection": {



"failingServiceCallPercentageIncreaseAbsolute": 5,



"failingServiceCallPercentageIncreaseRelative": 50



}



}



}



'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/applications
```

#### Request body

```
{



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



"enabled": true,



"trafficSpikePercent": 200



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

204

#### Result

The updated configuration has the following parameters:

![Anomaly detection config - apps - updated](https://dt-cdn.net/images/anomaly-detectoin-apps-upd-1004-b6691ad3d1.png)

Anomaly detection config - apps - updated

## Related topics

* [Adjust the sensitivity of anomaly detection for applications](/managed/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-applications "Learn how to adapt the sensitivity of problem detection for applications.")
* [Davis® AI](/managed/dynatrace-intelligence "Learn how Davis® AI detects performance anomalies, identifies root causes, and uses AI models for adaptive thresholds across your environment.")