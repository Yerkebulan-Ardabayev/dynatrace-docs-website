---
title: Events API v2 - GET a event property
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/events-v2/get-event-property
scraped: 2026-05-12T12:01:03.699342
---

# Events API v2 - GET a event property

# Events API v2 - GET a event property

* Reference
* Published Oct 07, 2021

Gets the details about an event property.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/eventProperties/{propertyKey}` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/eventProperties/{propertyKey}` |

## Authentication

To execute this request, you need an access token with `events.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| propertyKey | string | The event property key you're inquiring. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [EventPropertyDetails](#openapi-definition-EventPropertyDetails) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

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



"description": "string",



"displayName": "Custom description",



"filterable": true,



"key": "dt.event.description",



"writable": true



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

In this example, the request queries the details of the **Custom source** event property.

The API token is passed in the **Authorization** header.

#### Curl

```
curl --request GET \



--url 'https://mySampleEnv.live.dynatrace.com/api/v2/eventProperties/dt.event.source' \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/eventProperties/dt.event.source
```

#### Response body

```
{



"key": "dt.event.source",



"displayName": "Custom source",



"description": "The name or ID of the external source of the event",



"writable": true



}
```

#### Response code

200

## Related topics

* [Event analysis and correlation](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation "Gain an understanding of the Events section on each host, process, and service overview page.")