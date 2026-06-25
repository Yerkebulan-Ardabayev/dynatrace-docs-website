---
title: Synthetic monitors API - DELETE a monitor
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic/synthetic-monitors/delete-a-monitor
scraped: 2026-05-12T11:59:50.000299
---

# Synthetic monitors API - DELETE a monitor

# Synthetic monitors API - DELETE a monitor

* Reference
* Published Jul 26, 2019

Deletes the specified monitor.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/synthetic/monitors/{monitorId}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/synthetic/monitors/{monitorId}` |

## Authentication

To execute this request, you need an access token with `ExternalSyntheticIntegration` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| monitorId | string | The ID of the synthetic monitor to be deleted. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. The synthetic monitor has been deleted. The response doesn't have a body |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

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

In this example, the request deletes the **restExample** monitor that has the ID of **SYNTHETIC\_TEST-00000000000254E2**.

#### Curl

```
curl -X DELETE \



https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/monitors/SYNTHETIC_TEST-00000000000254E2 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/monitors/SYNTHETIC_TEST-00000000000254E2
```

#### Response code

200

## Related topics

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.")