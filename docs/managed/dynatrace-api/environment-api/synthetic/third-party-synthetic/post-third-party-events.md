---
title: Third-party synthetic API - POST third-party events to Dynatrace
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic/third-party-synthetic/post-third-party-events
scraped: 2026-05-12T11:54:36.809237
---

# Third-party synthetic API - POST third-party events to Dynatrace

# Third-party synthetic API - POST third-party events to Dynatrace

* Reference
* Published May 15, 2020

Pushes information about third-party synthetic events to Dynatrace.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/synthetic/ext/events` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/synthetic/ext/events` |

## Authentication

To execute this request, you need an access token with `ExternalSyntheticIntegration` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [3rdPartySyntheticEvents](#openapi-definition-3rdPartySyntheticEvents) | The JSON body of the request. Contains third-party synthetic events. | body | Required |

### Request body objects

#### The `3rdPartySyntheticEvents` object

The list of third-party synthetic events.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| open | [3rdPartyEventOpenNotification[]](#openapi-definition-3rdPartyEventOpenNotification) | The list of open third-party synthetic events. | Optional |
| resolved | [3rdPartyEventResolvedNotification[]](#openapi-definition-3rdPartyEventResolvedNotification) | The list of closed third-party synthetic events. | Optional |
| syntheticEngineName | string | The type of the third-party synthetic monitor. | Required |

#### The `3rdPartyEventOpenNotification` object

The open third-party synthetic event.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| eventId | string | The unique ID of the event. | Required |
| eventType | string | The type of the event. The element can hold these values * `testOutage` * `testSlowdown` | Required |
| locationIds | string[] | The list of IDs of third-party synthetic locations where the event happens. | Required |
| name | string | The name of the event. | Required |
| reason | string | The cause of the event. | Required |
| startTimestamp | integer | The start timestamp of the event, in UTC milliseconds. | Required |
| testId | string | The ID of the third-party synthetic monitor. | Required |

#### The `3rdPartyEventResolvedNotification` object

The closed third-party synthetic event.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| endTimestamp | integer | The end timestamp of the event, in UTC milliseconds. | Required |
| eventId | string | The unique ID of the event. | Required |
| testId | string | The ID of the third-party synthetic monitor. | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"open": [



{



"eventId": "string",



"eventType": "testOutage",



"locationIds": [



"string"



],



"name": "string",



"reason": "string",



"startTimestamp": 1,



"testId": "string"



}



],



"resolved": [



{



"endTimestamp": 1,



"eventId": "string",



"testId": "string"



}



],



"syntheticEngineName": "string"



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. The information is accepted and stored. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
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

## Update an existing third-party monitor

To update an existing third-party monitor, specify its engine in the **syntheticEngineName** field of the `3rdPartySyntheticTests` object and its ID in the **id** field of the `3rdPartySyntheticTest` object.

You have to submit **all** the parameters of the monitor. Do not change the values of parameters you don't want to change.

## Example

In this example, the request adds the **outage** event to the **example of synthetic monitor - 1** third-party synthetic monitor from the [**POST third-party monitors to Dynatrace** example](/managed/dynatrace-api/environment-api/synthetic/third-party-synthetic/post-third-party-monitors#example "Push third-party synthetic monitors to Dynatrace via Synthetic v1 API.").

The API token is passed in the **Authorization** header.

You can download the request body JSON to perform a sample request in your environment. Be sure to replace the timestamps with recent ones or the results will be too old.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/ext/events \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{<truncated - see the Request body section below>}



'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/ext/events
```

#### Request body

```
{



"syntheticEngineName": "My third-party synthetic",



"open": [



{



"testId": "3rdPartySyntheticMonitor1",



"eventId": "extOpenEvent1-1",



"name": "example of  event",



"reason": "sample outage",



"eventType": "testOutage",



"locationIds": ["Linz1"],



"startTimestamp": 1543582285957



}



],



"resolved": []



}
```

#### Response code

204

#### Result

The highlights show parameters submitted in the request.

![External synthetic event](https://dt-cdn.net/images/ext-monitor-event-1850-a94fba57bf.png)

External synthetic event