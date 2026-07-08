---
title: Services anomaly detection API - PUT configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-services/put-config
---

# Services anomaly detection API - PUT configuration

# Services anomaly detection API - PUT configuration

* Reference
* Published Aug 29, 2019

Updates the configuration of anomaly detection for services.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/services` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/services` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [ServiceAnomalyDetectionConfig](#openapi-definition-ServiceAnomalyDetectionConfig) | The JSON body of the request. Contains parameters of the service anomaly detection configuration. | body | Optional |

### Request body objects

#### The `ServiceAnomalyDetectionConfig` object

Dynatrace automatically detects service-related performance anomalies such as response time degradations and failure rate increases. Use these settings to configure detection sensitivity, set alert thresholds, or disable alerting for certain services.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| failureRateIncrease | [FailureRateIncreaseDetectionConfig](#openapi-definition-FailureRateIncreaseDetectionConfig) | Configuration of failure rate increase detection. | Required |
| loadDrop | [LoadDropDetectionConfig](#openapi-definition-LoadDropDetectionConfig) | The configuration of load drops detection. | Optional |
| loadSpike | [LoadSpikeDetectionConfig](#openapi-definition-LoadSpikeDetectionConfig) | The configuration of load spikes detection. | Optional |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging | Optional |
| responseTimeDegradation | [ResponseTimeDegradationDetectionConfig](#openapi-definition-ResponseTimeDegradationDetectionConfig) | Configuration of response time degradation detection. | Required |

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

#### The `LoadDropDetectionConfig` object

The configuration of load drops detection.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). | Required |
| loadDropPercent | integer | Alert if the observed load is less than *X* % of the expected value. | Optional |
| minAbnormalStateDurationInMinutes | integer | Alert if the service stays in abnormal state for at least *X* minutes. | Optional |

#### The `LoadSpikeDetectionConfig` object

The configuration of load spikes detection.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). | Required |
| loadSpikePercent | integer | Alert if the observed load is more than *X* % of the expected value. | Optional |
| minAbnormalStateDurationInMinutes | integer | Alert if the service stays in abnormal state for at least *X* minutes. | Optional |

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



"loadDrop": {



"enabled": true,



"loadDropPercent": 40,



"minAbnormalStateDurationInMinutes": 5



},



"loadSpike": {



"enabled": false



},



"metadata": {



"clusterVersion": "Mock version",



"configurationVersions": [



4,



2



]



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
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/services/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/services/validator` |

### Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Response

#### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Validated. The submitted configuration is valid. Response doesn't have a body. |
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

In this example, the request updates the configuration of anomaly detection for services from the [GET request](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-services/get-config#example "Read the configuration of anomaly detection for services via the Dynatrace API.") example. It changes the **Detect increase in failure rate** mode to **used fixed thresholds** and sets the following threshold with **high** sensitivity:

* Alert if **3**% of custom failure rate threshold is exceeded during any 5-minute period.

The API token is passed in the **Authorization** header.

You can download or copy the example request body to try it out on your own. Be sure to create a backup copy of your current configuration with the [GET services anomaly detection configuration](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-services/get-config "Read the configuration of anomaly detection for services via the Dynatrace API.") call.

#### Curl

```
curl -X PUT \



https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/services \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"responseTimeDegradation": {



"detectionMode": "DETECT_AUTOMATICALLY",



"automaticDetection": {



"responseTimeDegradationMilliseconds": 100,



"responseTimeDegradationPercent": 50,



"slowestResponseTimeDegradationMilliseconds": 100,



"slowestResponseTimeDegradationPercent": 100,



"loadThreshold": "TEN_REQUESTS_PER_MINUTE"



}



},



"failureRateIncrease": {



"detectionMode": "DETECT_USING_FIXED_THRESHOLDS",



"thresholds": {



"threshold": 3,



"sensitivity": "HIGH"



}



}



}



'
```

#### Request URL

```
PUT https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/services
```

#### Request body

```
{



"responseTimeDegradation": {



"detectionMode": "DETECT_AUTOMATICALLY",



"automaticDetection": {



"responseTimeDegradationMilliseconds": 100,



"responseTimeDegradationPercent": 50,



"slowestResponseTimeDegradationMilliseconds": 100,



"slowestResponseTimeDegradationPercent": 100,



"loadThreshold": "TEN_REQUESTS_PER_MINUTE"



}



},



"failureRateIncrease": {



"detectionMode": "DETECT_USING_FIXED_THRESHOLDS",



"thresholds": {



"threshold": 3,



"sensitivity": "HIGH"



}



}



}
```

#### Response code

204

#### Result

The updated configuration has the following parameters:

![Anomaly detection config - services - updated](https://dt-cdn.net/images/anomaly-detectoin-services-upd-899-c192035fcf.png)

Anomaly detection config - services - updated

## Related topics

* [Adjust the sensitivity of anomaly detection for services](/managed/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-services "Learn how to adapt the sensitivity of problem detection for services.")
* [Davis® AI](/managed/dynatrace-intelligence "Learn how Davis® AI detects performance anomalies, identifies root causes, and uses AI models for adaptive thresholds across your environment.")
* [Services](/managed/observe/application-observability/services "Learn how to monitor and analyze your services, define and use request attributes, and more.")