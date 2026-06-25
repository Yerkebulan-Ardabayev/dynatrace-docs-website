---
title: Process groups anomaly detection API - DELETE configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-process-groups/del-config
scraped: 2026-05-12T11:19:12.612818
---

# Process groups anomaly detection API - DELETE configuration

# Process groups anomaly detection API - DELETE configuration

* Reference
* Published Jun 03, 2020

Deletes the configuration of anomaly detection for the specified process group.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/processGroups/{id}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/processGroups/{id}` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The Dynatrace entity ID of the required process group. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. The configuration has been updated. Response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Process group doesn't exist |

### Response body objects

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

In this example, the request deletes the configuration of anomaly detection for the process group with the ID of **PROCESS\_GROUP-52B42D0616D556F5** from the [GET request](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-process-groups/get-config#example "View the anomaly detection configuration for a process group via Dynatrace API.") example.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -L -X DELETE 'https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/processGroups/PROCESS_GROUP-52B42D0616D556F5' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/processGroups/PROCESS_GROUP-52B42D0616D556F5
```

#### Response code

204

#### Result

![DEL anomaly detection config - process group](https://dt-cdn.net/images/del-config-603-da5d855f0e.png)

DEL anomaly detection config - process group

## Related topics

* [DavisÂ® AI](/managed/dynatrace-intelligence "Get familiar with the capabilities of Davis AI.")
* [Process groups](/managed/observe/infrastructure-observability/process-groups "Analyze process groups and customize process group naming, detection, and monitoring.")