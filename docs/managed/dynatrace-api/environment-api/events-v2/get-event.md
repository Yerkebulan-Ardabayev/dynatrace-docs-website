---
title: Events API v2 - GET an event
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/events-v2/get-event
---

# Events API v2 - GET an event

# Events API v2 - GET an event

* Reference
* Published Aug 06, 2021

Gets all properties of the specified event.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/events/{eventId}` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/events/{eventId}` |

## Authentication

To execute this request, you need an access token with `events.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| eventId | string | The ID of the required event. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [Event](#openapi-definition-Event) | Success. The response contains the configuration of the event. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `Event` object

Configuration of an event.

| Element | Type | Description |
| --- | --- | --- |
| correlationId | string | The correlation ID of the event. |
| endTime | integer | The timestamp when the event was closed, in UTC milliseconds.  Has the value of `null` if the event is still active. |
| entityId | [EntityStub](#openapi-definition-EntityStub) | A short representation of a monitored entity. |
| entityTags | [METag](#openapi-definition-METag)[] | A list of tags of the related entity. |
| eventId | string | The ID of the event. |
| eventType | string | The type of the event. |
| frequentEvent | boolean | If `true`, the event happens [frequently﻿](https://dt-url.net/4da3kdg?dt=m).  A frequent event doesn't raise a problem. |
| managementZones | [ManagementZone](#openapi-definition-ManagementZone)[] | A list of all management zones that the event belongs to. |
| properties | [EventProperty](#openapi-definition-EventProperty)[] | A list of event properties. |
| startTime | integer | The timestamp when the event was raised, in UTC milliseconds. |
| status | string | The status of the event. The element can hold these values * `CLOSED` * `OPEN` |
| suppressAlert | boolean | The alerting status during a [maintenance﻿](https://dt-url.net/b2123rg0?dt=m):  * `false`: Alerting works as usual. * `true`: Alerting is disabled. |
| suppressProblem | boolean | The problem detection status during a [maintenance﻿](https://dt-url.net/b2123rg0?dt=m):  * `false`: Problem detection works as usual. * `true`: Problem detection is disabled. |
| title | string | The title of the event. |
| underMaintenance | boolean | If `true`, the event happened while the monitored system was under maintenance. |

#### The `EntityStub` object

A short representation of a monitored entity.

| Element | Type | Description |
| --- | --- | --- |
| entityId | [EntityId](#openapi-definition-EntityId) | A short representation of a monitored entity. |
| name | string | The name of the entity.  Not included in the response in case no entity with the relevant ID was found. |

#### The `EntityId` object

A short representation of a monitored entity.

| Element | Type | Description |
| --- | --- | --- |
| id | string | The ID of the entity. |
| type | string | The type of the entity. |

#### The `METag` object

The tag of a monitored entity.

| Element | Type | Description |
| --- | --- | --- |
| context | string | The origin of the tag, such as AWS or Cloud Foundry.  Custom tags use the `CONTEXTLESS` value. |
| key | string | The key of the tag. |
| stringRepresentation | string | The string representation of the tag. |
| value | string | The value of the tag. |

#### The `ManagementZone` object

A short representation of a management zone.

| Element | Type | Description |
| --- | --- | --- |
| id | string | The ID of the management zone. |
| name | string | The name of the management zone. |

#### The `EventProperty` object

A property of an event.

| Element | Type | Description |
| --- | --- | --- |
| key | string | The key of the event property. |
| value | string | The value of the event property. |

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



"correlationId": "933613657e1c8fcf",



"endTime": 1564039524182,



"entityId": {



"entityId": {



"id": "string",



"type": "string"



},



"name": "string"



},



"entityTags": [



{



"context": "string",



"key": "string",



"stringRepresentation": "string",



"value": "string"



}



],



"eventId": "4293884258445543163_1564039524182",



"eventType": "LOW_DISK_SPACE",



"frequentEvent": true,



"managementZones": [



{



"id": "string",



"name": "string"



}



],



"properties": [



{



"key": "string",



"value": "string"



}



],



"startTime": 1564039524182,



"status": "OPEN",



"suppressAlert": true,



"suppressProblem": true,



"title": "High CPU load on host X",



"underMaintenance": true



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

In this example, the request queries the parameters of the event with the ID of **6375436663535938547\_1628496488654**.

This is the **SYNTHETIC\_GLOBAL\_OUTAGE** event, indicating global outage of browser monitors.

The API token is passed in the **Authorization** header.

#### Curl

```
curl --request GET \



--url https://mySampleEnv.live.dynatrace.com/api/v2/events/6375436663535938547_1628496488654 \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/events/6375436663535938547_1628496488654
```

#### Response body

```
{



"eventId": "6375436663535938547_1628496488654",



"startTime": 1628496488654,



"endTime": 1628503679796,



"eventType": "SYNTHETIC_GLOBAL_OUTAGE",



"title": "Browser monitor global outage",



"entityId": {



"entityId": {



"id": "SYNTHETIC_TEST-03ABB7F6446D1727",



"type": "SYNTHETIC_TEST"



},



"name": "Maintenance window test"



},



"properties": [



{



"key": "dt.event.group_label",



"value": "Browser monitor global outage"



},



{



"key": "dt.event.is_rootcause_relevant",



"value": "true"



}



],



"status": "CLOSED",



"correlationId": "aecd1653df38ef50",



"entityTags": [



{



"context": "CONTEXTLESS",



"key": "Synthetic",



"value": "Browser",



"stringRepresentation": "Synthetic:Browser"



}



],



"managementZones": [



{



"id": "-7832237287622819191",



"name": "Synthetic tests"



}



],



"underMaintenance": true,



"suppressAlert": false,



"suppressProblem": false,



"frequentEvent": false



}
```

#### Response code

200

## Related topics

* [Event categories](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories "Learn about different categories of events and supported event types, along with their severity levels, and the logic behind raising them.")
* [Event analysis and correlation](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation "Gain an understanding of the Events section on each host, process, and service overview page.")