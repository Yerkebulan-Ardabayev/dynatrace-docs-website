---
title: "Events API v2 - GET all event properties"
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/events-v2/get-event-properties
updated: 2026-02-09
---

# Events API v2 - GET all event properties

# Events API v2 - GET all event properties

* Reference
* Published Oct 07, 2021

Lists all event properties that Dynatrace provides.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/eventProperties` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/eventProperties` |

## Authentication

To execute this request, you need an access token with `events.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| nextPageKey | string | The cursor for the next page of results. You can find it in the **nextPageKey** field of the previous response.  The first page is always returned if you don't specify the **nextPageKey** query parameter.  When the **nextPageKey** is set to obtain subsequent pages, you must omit all other query parameters. | query | Optional |
| pageSize | integer | The amount of event properties in a single response payload.  The maximal allowed page size is 500.  If not set, 100 is used. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [EventPropertiesList](#openapi-definition-EventPropertiesList) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `EventPropertiesList` object

A list of event properties.

| Element | Type | Description |
| --- | --- | --- |
| eventProperties | [EventPropertyDetails[]](#openapi-definition-EventPropertyDetails) | A list of event properties. |
| nextPageKey | string | The cursor for the next page of results. Has the value of `null` on the last page.  Use it in the **nextPageKey** query parameter to obtain subsequent pages of the result. |
| pageSize | integer | The number of entries per page. |
| totalCount | integer | The total number of entries in the result. |

#### The `EventPropertyDetails` object

Configuration of an event property.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the event property. |
| displayName | string | The display name of the event property. |
| filterable | boolean | The property can (`true`) or cannot (`false`) be used for filtering in the event selector. Usage in event selector: `property.<key>("value-1", "value-2")` |
| key | string | The key of the event property. |
| writable | boolean | The property can (`true`) or cannot (`false`) be set during event ingestion. |

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



"eventProperties": [



{



"description": "string",



"displayName": "Custom description",



"filterable": true,



"key": "dt.event.description",



"writable": true



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

In this example, the request lists all available event properties that are available in the **mySampleEnv** environment. The result is truncated to three entries

The API token is passed in the **Authorization** header.

#### Curl

```
curl --request GET \



--url 'https://mySampleEnv.live.dynatrace.com/api/v2/eventProperties?pageSize=3' \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/eventProperties?pageSize=3
```

#### Response body

```
{



"totalCount": 23,



"pageSize": 3,



"nextPageKey": "AQAAAAMBAAAAAw==",



"eventProperties": [



{



"key": "dt.event.allow_davis_merge",



"displayName": "Allow Davis merge",



"description": "Allow Davis AI to merge this event into existing problems (true) or force creating a new problem (false)",



"writable": true



},



{



"key": "dt.event.baseline.service_method",



"displayName": "Baseline affected service method",



"description": "Lists affected service methods of the triggered service event",



"writable": false



},



{



"key": "dt.event.baseline.total_load",



"displayName": "Baseline total load",



"description": "The load (calls per minute) of the entire service or application for triggered event",



"writable": false



}



]



}
```

#### Response code

200

## Related topics

* [Event analysis and correlation](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation "Gain an understanding of the Events section on each host, process, and service overview page.")
