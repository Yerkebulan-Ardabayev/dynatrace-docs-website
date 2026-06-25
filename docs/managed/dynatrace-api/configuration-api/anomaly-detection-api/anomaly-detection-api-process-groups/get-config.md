---
title: Process groups anomaly detection API - GET configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-process-groups/get-config
scraped: 2026-05-12T11:19:14.058424
---

# Process groups anomaly detection API - GET configuration

# Process groups anomaly detection API - GET configuration

* Reference
* Published Jun 03, 2020

Gets the configuration of anomaly detection for the specified process group.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/processGroups/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/processGroups/{id}` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The Dynatrace entity ID of the required process group. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [AnomalyDetectionPG](#openapi-definition-AnomalyDetectionPG) | Success |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Process group doesn't exist |

### Response body objects

#### The `AnomalyDetectionPG` object

Configuration of anomaly detection for the process group.

| Element | Type | Description |
| --- | --- | --- |
| availabilityMonitoring | [AvailabilityMonitoringPG](#openapi-definition-AvailabilityMonitoringPG) | Configuration of the availability monitoring for the process group. |

#### The `AvailabilityMonitoringPG` object

Configuration of the availability monitoring for the process group.

| Element | Type | Description |
| --- | --- | --- |
| method | string | How to monitor the availability of the process group:  * `PROCESS_IMPACT`: Alert if any process of the group becomes unavailable. * `MINIMUM_THRESHOLD`: Alert if the number of active processes in the group falls below the specified threshold. * `OFF`: Availability monitoring is disabled. The element can hold these values * `MINIMUM_THRESHOLD` * `OFF` * `PROCESS_IMPACT` |
| minimumThreshold | integer | Alert if the number of active processes in the group is lower than this value. |

#### The `ErrorEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### The `Error` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | A list of constraint violations |
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



"availabilityMonitoring": {



"method": "MINIMUM_THRESHOLD",



"minimumThreshold": 5



}



}
```

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

In this example, the request gets the configuration of anomaly detection for the process group with the ID of **PROCESS\_GROUP-52B42D0616D556F5**.

The API token is passed in the **Authorization** header.

The configuration has the following settings:

![GET anomaly detection config - process group](https://dt-cdn.net/images/get-config-641-4141d73410.png)

GET anomaly detection config - process group

#### Curl

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/processGroups/PROCESS_GROUP-52B42D0616D556F5' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/processGroups/PROCESS_GROUP-52B42D0616D556F5
```

#### Response body

```
{



"availabilityMonitoring": {



"method": "MINIMUM_THRESHOLD",



"minimumThreshold": 10



}



}
```

#### Response code

200

## Related topics

* [DavisÂ® AI](/managed/dynatrace-intelligence "Get familiar with the capabilities of Davis AI.")
* [Process groups](/managed/observe/infrastructure-observability/process-groups "Analyze process groups and customize process group naming, detection, and monitoring.")