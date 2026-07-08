---
title: Events API v2 - GET an event type
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/events-v2/get-event-type
---

# Events API v2 - GET an event type

# Events API v2 - GET an event type

* Reference
* Published Aug 06, 2021

Gets the properties of an event type.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/eventTypes/{eventType}` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/eventTypes/{eventType}` |

## Authentication

To execute this request, you need an access token with `events.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| eventType | string | The event type you're inquiring. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [EventType](#openapi-definition-EventType) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `EventType` object

Configuration of an event type.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the event type. |
| displayName | string | The display name of the event type. |
| severityLevel | string | The severity level associated with the event type. The element can hold these values * `AVAILABILITY` * `CUSTOM_ALERT` * `ERROR` * `INFO` * `MONITORING_UNAVAILABLE` * `PERFORMANCE` * `RESOURCE_CONTENTION` |
| type | string | The event type. |

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



"description": "string",



"displayName": "High CPU",



"severityLevel": "PERFORMANCE",



"type": "OSI_HIGH_CPU"



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

In this example, the request queries the properties of the **APPLICATION\_SLOWDOWN** type.

The API token is passed in the **Authorization** header.

#### Curl

```
curl --request GET \



--url 'https://mySampleEnv.live.dynatrace.com/api/v2/eventTypes/APPLICATION_SLOWDOWN' \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/eventTypes/APPLICATION_SLOWDOWN
```

#### Response body

```
{



"type": "APPLICATION_SLOWDOWN",



"displayName": "Application slowdown",



"severityLevel": "PERFORMANCE",



"description": "User action duration degradation"



}
```

#### Response code

200

## Related topics

* [Event categories](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories "Learn about different categories of events and supported event types, along with their severity levels, and the logic behind raising them.")
* [Event analysis and correlation](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation "Gain an understanding of the Events section on each host, process, and service overview page.")