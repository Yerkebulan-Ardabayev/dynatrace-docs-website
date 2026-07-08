---
title: Process groups anomaly detection API - PUT configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-process-groups/put-config
---

# Process groups anomaly detection API - PUT configuration

# Process groups anomaly detection API - PUT configuration

* Reference
* Published Jun 03, 2020

Updates the configuration of anomaly detection for the specified process group.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/processGroups/{id}` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/processGroups/{id}` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The Dynatrace entity ID of the required process group. | path | Required |
| body | [AnomalyDetectionPG](#openapi-definition-AnomalyDetectionPG) | The JSON body of the request. Contains parameters of anomaly detection for a process group. | body | Optional |

### Request body objects

#### The `AnomalyDetectionPG` object

Configuration of anomaly detection for the process group.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| availabilityMonitoring | [AvailabilityMonitoringPG](#openapi-definition-AvailabilityMonitoringPG) | Configuration of the availability monitoring for the process group. | Optional |

#### The `AvailabilityMonitoringPG` object

Configuration of the availability monitoring for the process group.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| method | string | How to monitor the availability of the process group:  * `PROCESS_IMPACT`: Alert if any process of the group becomes unavailable. * `MINIMUM_THRESHOLD`: Alert if the number of active processes in the group falls below the specified threshold. * `OFF`: Availability monitoring is disabled. The element can hold these values * `MINIMUM_THRESHOLD` * `OFF` * `PROCESS_IMPACT` | Required |
| minimumThreshold | integer | Alert if the number of active processes in the group is lower than this value. | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"availabilityMonitoring": {



"method": "MINIMUM_THRESHOLD",



"minimumThreshold": 5



}



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. The configuration has been updated. Response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |

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
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/processGroups/{id}/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/processGroups/{id}/validator` |

### Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Response

#### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Validated. The submitted configuration is valid. Response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |

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

In this example, the request updates the configuration of anomaly detection for the process group with the ID of **PROCESS\_GROUP-52B42D0616D556F5** from the [GET request](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-process-groups/get-config#example "View the anomaly detection configuration for a process group via Dynatrace API.") example. It changes the method of detection to **PROCESS\_IMPACT**.

The API token is passed in the **Authorization** header.

You can download or copy the example request body to try it out on your own. First, be sure to create a backup copy of your current configuration with the **GET process group anomaly detection configuration** call.

#### Curl

```
curl -L -X PUT 'https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/processGroups/PROCESS_GROUP-52B42D0616D556F5' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



--data-raw '{



"availabilityMonitoring": {



"method": "PROCESS_IMPACT"



}



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/processGroups/PROCESS_GROUP-52B42D0616D556F5
```

#### Request body

```
{



"availabilityMonitoring": {



"method": "PROCESS_IMPACT"



}



}
```

#### Response code

204

#### Result

![PUT anomaly detection config - process group](https://dt-cdn.net/images/put-config-619-6a113b1650.png)

PUT anomaly detection config - process group

## Related topics

* [Davis® AI](/managed/dynatrace-intelligence "Learn how Davis® AI detects performance anomalies, identifies root causes, and uses AI models for adaptive thresholds across your environment.")
* [Process groups](/managed/observe/infrastructure-observability/process-groups "Analyze process groups and customize process group naming, detection, and monitoring.")