---
title: Events API v2 - POST an event
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/events-v2/post-event
scraped: 2026-02-15T21:24:54.169784
---

# Events API v2 - POST an event

# Events API v2 - POST an event

* Reference
* Published Nov 05, 2021

Ingests a custom event to Dynatrace.

The request consumes an `application/json` payload.

The ingestion of custom events consumes [Davis Data Units (DDUs)](/docs/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).") from the events pool.

|  |  |  |
| --- | --- | --- |
| POST | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/events/ingest` |
| POST | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/events/ingest` |

## Authentication

To execute this request, you need an access token with `events.ingest` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [EventIngest](#openapi-definition-EventIngest) | The JSON body of the request. Contains properties of the new event. | body | Optional |

### Request body objects

#### The `EventIngest` object

The configuration of an event to be ingested.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| endTime | integer | The end time of the event, in UTC milliseconds.  If not set, the start time plus timeout is used. | Optional |
| entitySelector | string | The [entity selectorï»¿](https://dt-url.net/apientityselector), defining a set of Dynatrace entities to be associated with the event.  Only entities that have been active within the last 24 hours can be selected. Note that the `entityId` filter bypasses this time constraint, allowing events to be ingested for entities that have been inactive for more than 24 hours.  If not set, the event is associated with the environment (`dt.entity.environment`) entity. | Optional |
| eventType | string | The type of the event. The element can hold these values * `AVAILABILITY_EVENT` * `CUSTOM_ALERT` * `CUSTOM_ANNOTATION` * `CUSTOM_CONFIGURATION` * `CUSTOM_DEPLOYMENT` * `CUSTOM_INFO` * `ERROR_EVENT` * `MARKED_FOR_TERMINATION` * `PERFORMANCE_EVENT` * `RESOURCE_CONTENTION_EVENT` * `WARNING` | Required |
| properties | object | A map of event properties.  * To set event properties with predefined behavior, use classic `dt.event.*` and `dt.davis.*` properties. To check which properties belong to classic API, see [Events API v2 - GET all event propertiesï»¿](https://dt-url.net/9622g1w). * To attach entity information to an event, use `dt.entity.*` keys. * To provide additional info, you can use any key outside of the `dt.*` namespace.  Values of event properties with predefined behavior must fulfill the requirements of the respective property.  A maximum of 100 properties can be specified. A property key is allowed to contain up to 100 characters. A property value is allowed to contain up to 4096 characters. | Optional |
| startTime | integer | The start time of the event, in UTC milliseconds.  If not set, the current timestamp is used.  Depending on the event type, the start time must not lie in the past more than 6 hours for problem-opening events and 30 days for info events.  Depending on the event type, the start time must not lie in the future more than 5 minutes for problem-opening events and 7 days for info events.  Events that can be sent up to 7 days in the future:  * `CUSTOM_ANNOTATION` * `CUSTOM_CONFIGURATION` * `CUSTOM_DEPLOYMENT` * `CUSTOM_INFO` * `MARKED_FOR_TERMINATION` | Optional |
| timeout | integer | The timeout of the event, in minutes.  If not set, 15 is used.  The timeout will automatically be capped to a maximum of 360 minutes (6 hours).  Problem-opening events can be refreshed and therefore kept open by sending the same payload again. | Optional |
| title | string | The title of the event. | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"endTime": 1,



"entitySelector": "string",



"eventType": "AVAILABILITY_EVENT",



"properties": {},



"startTime": 1,



"timeout": 1,



"title": "string"



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [EventIngestResults](#openapi-definition-EventIngestResults) | The event ingest request was received by the server. The response body indicates for each event whether its creation was successful. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `EventIngestResults` object

The results of an event ingest.

| Element | Type | Description |
| --- | --- | --- |
| eventIngestResults | [EventIngestResult[]](#openapi-definition-EventIngestResult) | The result of each created event report. |
| reportCount | integer | The number of created event reports. |

#### The `EventIngestResult` object

The result of a created event report.

| Element | Type | Description |
| --- | --- | --- |
| correlationId | string | The correlation ID of the created event. |
| status | string | The status of the ingestion. The element can hold these values * `INVALID_ENTITY_TYPE` * `INVALID_METADATA` * `INVALID_TIMESTAMPS` * `OK` |

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



"eventIngestResults": [



{



"correlationId": "string",



"status": "INVALID_ENTITY_TYPE"



}



],



"reportCount": 1



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

## Examples

Example 1

Example 2

Example 3

Use case

An operations team wants to push a **Marked for termination** event to all the hosts that are planned to be removed. They also want to include the purpose for the deletion and a job identifier. The hosts to be removed are gathered in a designated host group.

In this example, the request sends a **Marked for termination** event to hosts that are planned to be removed. Such hosts are identified by the **cloud-burst-hosts** host group. The event automatically applies to all hosts that are part of the group. The purpose for termination and automation job number are provided as additional information.

The API token is passed in the **Authorization** header.

#### Curl

```
curl --request POST \



--url https://mySampleEnv.live.dynatrace.com/api/v2/events/ingest \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



--header 'Content-Type: application/json' \



--data '{



"eventType": "MARKED_FOR_TERMINATION",



"title": "Planned host downscale",



"entitySelector": "type(HOST),fromRelationship.isInstanceOf(type(HOST_GROUP),entityName(cloud-burst-hosts))",



"properties": {



"job.number": "21234346"



}



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/events/ingest
```

#### Request body

```
{



"eventType": "MARKED_FOR_TERMINATION",



"title": "Planned host downscale",



"entitySelector": "type(HOST),fromRelationship.isInstanceOf(type(HOST_GROUP),entityName(cloud-burst-hosts))",



"properties": {



"job.number": "21234346"



}



}
```

#### Response body

```
{



"reportCount": 2,



"eventIngestResults": [



{



"correlationId": "41f5d263011a6c9a",



"status": "OK"



},



{



"correlationId": "80eae4d163cc5760",



"status": "OK"



}



]



}
```

#### Response code

201

Use case

A DevOps team wants to connect their load test tool with Dynatrace to annotate a service that is currently undergoing a load test. Later, when Dynatrace raises a problem caused by the load test, the problem details will include this information, simplifying the triage process.

In this example, the request sends a **Custom info** event to the **BookingService** service, marking it as a target of a load test.

The API token is passed in the **Authorization** header.

#### Curl

```
curl --request POST \



--url https://mySampleEnv.live.dynatrace.com/api/v2/events/ingest \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



--header 'Content-Type: application/json' \



--data '{



"eventType": "CUSTOM_INFO",



"title": "Loadtest start",



"timeout": 30,



"entitySelector": "type(SERVICE),entityName.equals(BookingService)",



"properties": {



"Tool": "MyLoadTool",



"Load per minute": "100",



"Load pattern": "production"



}



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/events/ingest
```

#### Request body

```
{



"eventType": "CUSTOM_INFO",



"title": "Loadtest start",



"timeout": 30,



"entitySelector": "type(SERVICE),entityName.equals(BookingService)",



"properties": {



"Tool": "MyLoadTool",



"Load per minute": "100",



"Load pattern": "production"



}



}
```

#### Response body

```
{



"reportCount": 1,



"eventIngestResults": [



{



"correlationId": "eba82f647696e485",



"status": "OK"



}



]



}
```

#### Response code

201

Use case

The operations team of a large retailer wants to trigger an alert in Dynatrace whenever their catalog update batch process fails. They want to create an event and alert in Dynatrace, but they donât want Dynatrace Intelligence to merge this externally created event with any larger incident.

In this example, the request sends an **Error** event to the **BookingService** service, indicating a failed update. The **dt.event.allow\_davis\_merge** property is set to `false`, preventing Dynatrace Intelligence from merging this event with any other event.

The API token is passed in the **Authorization** header.

#### Curl

```
curl --request POST \



--url https://mySampleEnv.live.dynatrace.com/api/v2/events/ingest \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



--header 'Content-Type: application/json' \



--data '{



"eventType": "ERROR_EVENT",



"title": "Product catalog update failed",



"timeout": 30,



"entitySelector": "type(SERVICE),entityName.equals(BookingService)",



"properties": {



"dt.event.allow_davis_merge": "false",



"Catalog": "APAC travels",



"Batch processor": "travel-catalog"



}



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/events/ingest
```

#### Request body

```
{



"eventType": "ERROR_EVENT",



"title": "Product catalog update failed",



"timeout": 30,



"entitySelector": "type(SERVICE),entityName.equals(BookingService)",



"properties": {



"dt.event.allow_davis_merge": "false",



"Catalog": "APAC travels",



"Batch processor": "travel-catalog"



}



}
```

#### Response body

```
{



"reportCount": 1,



"eventIngestResults": [



{



"correlationId": "cefb7ae03ac720b6",



"status": "OK"



}



]



}
```

#### Response code

201

## Related topics

* [Event categories](/docs/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories "Learn about different categories of events and supported event types, along with their severity levels, and the logic behind raising them.")
* [Event analysis and correlation](/docs/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation "Gain an understanding of the Events section on each host, process, and service overview page.")