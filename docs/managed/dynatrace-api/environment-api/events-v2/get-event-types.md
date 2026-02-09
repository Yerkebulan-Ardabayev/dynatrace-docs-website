---
title: "Events API v2 - GET all event types"
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/events-v2/get-event-types
updated: 2026-02-09
---

# Events API v2 - GET all event types

# Events API v2 - GET all event types

* Reference
* Published Aug 06, 2021

Lists all types of events that might be raised in your environment.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/eventTypes` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/eventTypes` |

## Authentication

To execute this request, you need an access token with `events.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| nextPageKey | string | The cursor for the next page of results. You can find it in the **nextPageKey** field of the previous response.  The first page is always returned if you don't specify the **nextPageKey** query parameter.  When the **nextPageKey** is set to obtain subsequent pages, you must omit all other query parameters. | query | Optional |
| pageSize | integer | The amount of event types in a single response payload.  The maximal allowed page size is 500.  If not set, 100 is used. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [EventTypeList](#openapi-definition-EventTypeList) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `EventTypeList` object

A list of event types.

| Element | Type | Description |
| --- | --- | --- |
| eventTypeInfos | [EventType[]](#openapi-definition-EventType) | A list of event types. |
| nextPageKey | string | The cursor for the next page of results. Has the value of `null` on the last page.  Use it in the **nextPageKey** query parameter to obtain subsequent pages of the result. |
| pageSize | integer | The number of entries per page. |
| totalCount | integer | The total number of entries in the result. |

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



"eventTypeInfos": [



{



"description": "string",



"displayName": "High CPU",



"severityLevel": "PERFORMANCE",



"type": "OSI_HIGH_CPU"



}



],



"nextPageKey": "AQAAABQBAAAABQ==",



"pageSize": 1,



"totalCount": 1



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

In this example, the request lists all event types that can be created in the **mySampleEnv** environment. The result is truncated to three entries

The API token is passed in the **Authorization** header.

#### Curl

```
curl --request GET \



--url 'https://mySampleEnv.live.dynatrace.com/api/v2/eventTypes?pageSize=3' \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/eventTypes?pageSize=3
```

#### Response body

```
{



"totalCount": 144,



"pageSize": 3,



"nextPageKey": "AQAAAGQBAAAAZA==",



"eventTypeInfos": [



{



"type": "APPLICATION_UNEXPECTED_LOW_LOAD",



"displayName": "Application low traffic",



"severityLevel": "AVAILABILITY",



"description": "Unexpected low traffic"



},



{



"type": "MOBILE_APP_CRASH_RATE_INCREASED",



"displayName": "Mobile app crash rate increase",



"severityLevel": "ERROR"



},



{



"type": "APPLICATION_SLOWDOWN",



"displayName": "Application slowdown",



"severityLevel": "PERFORMANCE",



"description": "User action duration degradation"



}



]



}
```

#### Response code

200

## Related topics

* [Event categories](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories "Learn about different categories of events and supported event types, along with their severity levels, and the logic behind raising them.")
* [Event analysis and correlation](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation "Gain an understanding of the Events section on each host, process, and service overview page.")
