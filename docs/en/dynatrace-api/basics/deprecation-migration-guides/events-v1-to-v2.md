---
title: Migrate from Events API v1 to Events API v2
source: https://www.dynatrace.com/docs/dynatrace-api/basics/deprecation-migration-guides/events-v1-to-v2
scraped: 2026-02-21T21:25:39.495004
---

# Migrate from Events API v1 to Events API v2

# Migrate from Events API v1 to Events API v2

* Reference
* Published Nov 25, 2022

[Events API v1](/docs/dynatrace-api/environment-api/events-v1 "Find out what you can do with the Dynatrace Events API.") has been deprecated with [Dynatrace version 1.243](/docs/whats-new/dynatrace-api/sprint-243 "Changelog for Dynatrace API version 1.243"). Its replacement is [Events API v2](/docs/dynatrace-api/environment-api/events-v2 "Find out what you can do with the Dynatrace Events API v2."). We recommend that you migrate to the new API at your earliest convenience.

The migration affects endpoint URLs, query parameters, and response/request body parameters, as well as the scope of the token for request authentication.

## New features

Events API v2 offers you the following new features:

* The [entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.") helps you to filter events in read requests and ingest events that affect multiple entities.
* Improved event filtering via an event selector.
* Unified timeframe selector.
* Event properties endpoints.
* Event types endpoints.

## Licensing

The [ingestion](/docs/dynatrace-api/environment-api/events-v2/post-event "Ingests an event via the Dynatrace API.") of custom events consumes [Davis Data Units (DDUs)](/docs/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).") from the events pool.

## Base URL

| new Events v2 | old Events v1 |
| --- | --- |
| `/api/v2/events` | `/api/v1/events` |

## Authentication token scope

| new Events v2 | old Events v1 |
| --- | --- |
| **Read events** (`events.read`) **Ingest events** (`events.ingest`) | **Access problem and event feed, metrics, and topology** (`DataExport`) |

## Parameters

To learn about new query/body parameters, see the documentation of individual requests in [Events API v2](/docs/dynatrace-api/environment-api/events-v2 "Find out what you can do with the Dynatrace Events API v2.").

## Examples

Here are some examples of differences in API usage.

### List events within a timeframe

In this example, we query a list of open availability events on hosts that happened within the last two hours.

Events v2

Events v1

#### Request URL

```
GET https://mySampleEnv.live.dynatrace.com/api/v2/events?eventSelector=eventType("AVAILABILITY_EVENT"),status("OPEN")&from=now-2h&entitySelector=type("HOST")
```

#### Response body

```
{



"totalCount": 28,



"pageSize": 2,



"nextPageKey": "AQANMTY2OTY0NDE2NjAwOQEADTE2Njk2NTEzNjYwMDkBADtTdHJpbmcoVDFCRlRnPT0pLUxvbmcoMTg0YmVlMjU1NjkpLUxvbmcoYTdjZjQ2NjZlNjIwZjMyMSktMgEAAAACAQAuZXZlbnRUeXBlKCJBVkFJTEFCSUxJVFlfRVZFTlQiKSxzdGF0dXMoIk9QRU4iKQEADHR5cGUoIkhPU1QiKQA=",



"events": [



{



"eventId": "-9195326388738983252_1669651221408",



"startTime": 1669651221408,



"endTime": -1,



"eventType": "AVAILABILITY_EVENT",



"title": "No process found for rule Oracle listener",



"entityId": {



"entityId": {



"id": "HOST-E371A974A078CC54",



"type": "HOST"



},



"name": "frontend-dev"



},



"properties": [



{



"key": "Event source",



"value": "Process availability"



},



{



"key": "Message",



"value": "Missing process matching rule named Oracle listener"



},



{



"key": "custom.message-process-av",



"value": "The {dt.event.title} is on deployment version: {dt.event.deployment.version}"



},



{



"key": "dt.event.group_label",



"value": "Availability event"



},



{



"key": "dt.event.impact_level",



"value": "Infrastructure"



},



{



"key": "dt.event.is_rootcause_relevant",



"value": "true"



},



{



"key": "dt.event.timeout",



"value": "4"



},



{



"key": "dt.event.title",



"value": "No process found for rule Oracle listener"



}



],



"status": "OPEN",



"correlationId": "458a73c38677f1ac",



"entityTags": [



{



"context": "CONTEXTLESS",



"key": "frontend",



"stringRepresentation": "frontend"



},



{



"context": "CONTEXTLESS",



"key": "stage",



"value": "dev",



"stringRepresentation": "stage:dev"



}



],



"managementZones": [



{



"id": "6143976176513989654",



"name": "Infrastructure Linux"



},



{



"id": "4067143719293196613",



"name": "dev"



},



{



"id": "-6114370715062110014",



"name": "frontent"



}



],



"underMaintenance": false,



"suppressAlert": false,



"suppressProblem": false,



"frequentEvent": false



},



{



"eventId": "-6354783141434952927_1669649814889",



"startTime": 1669649814889,



"endTime": -1,



"eventType": "AVAILABILITY_EVENT",



"title": "Host unavailable",



"entityId": {



"entityId": {



"id": "HOST-FD01FA52FB10B433",



"type": "HOST"



},



"name": "GDNVTUBU2004-1"



},



"properties": [



{



"key": "dt.event.group_label",



"value": "Availability event"



},



{



"key": "dt.event.impact_level",



"value": "Infrastructure"



},



{



"key": "dt.event.is_rootcause_relevant",



"value": "true"



},



{



"key": "dt.event.timeout",



"value": "5"



},



{



"key": "dt.event.title",



"value": "Host unavailable"



}



],



"status": "OPEN",



"correlationId": "360ad37a6f4de7d0",



"entityTags": [



{



"context": "CONTEXTLESS",



"key": "OS",



"value": "Linux",



"stringRepresentation": "OS:Linux"



}



],



"managementZones": [



{



"id": "6143976176513989654",



"name": "Linux"



},



{



"id": "4067143719293196613",



"name": "dev"



}



],



"underMaintenance": false,



"suppressAlert": false,



"suppressProblem": false,



"frequentEvent": false



}



],



"warnings": []



}
```

In Events API v1, it is not possible to filter the events feed by event status. Also, it is not possible to select multiple entities via the entity selector. You can only specify particular entities. For illustration purposes, the example payload shows the same events, but you would have to find them in the payload by external means.

#### Request URL

```
GET https://mySampleEnv.live.dynatrace.com/api/v1/events?relativeTime=2hours?eventType=AVAILABILITY_EVENT
```

#### Response body

```
{



"nextEventStartTms": 1669639936928,



"nextEventId": -3132566662524695739,



"nextCursor": "AgEAAAGEvd8xRAEAAAGEvk0ORAAAAQA8U3RyaW5nKFQxQkZUZz09KS1Mb25nKDE4NGJlNGI5YmEwKS1Mb25nKGQ0ODZlMzM3YWNmYzBiNDUpLTk2",



"from": 1669632831812,



"to": 1669640031812,



"totalEventCount": 25703,



"events": [



{



"eventId": -9195326388738983252,



"startTime": 1669651221408,



"endTime": 1669658492185,



"entityId": "HOST-E371A974A078CC54",



"entityName": "frontend-dev",



"severityLevel": "AVAILABILITY",



"impactLevel": "INFRASTRUCTURE",



"eventType": "AVAILABILITY_EVENT",



"eventStatus": "OPEN",



"tags": [



{



"context": "CONTEXTLESS",



"key": "frontend"



},



{



"context": "CONTEXTLESS",



"key": "stage",



"value": "dev"



}



],



"id": "-9195326388738983252_1669651221408",



"customProperties": {



"custom.message-process-av": "The {dt.event.title} is on deployment version: {dt.event.deployment.version}",



"Event source": "Process availability",



"Message": "Missing process matching rule named Oracle listener"



},



"correlationId": "458a73c38677f1ac",



"source": "builtin"



},



{



"eventId": -6354783141434952927,



"startTime": 1669649814889,



"endTime": 1669652093491,



"entityId": "HOST-FD01FA52FB10B433",



"entityName": "GDNVTUBU2004-1",



"severityLevel": "AVAILABILITY",



"impactLevel": "INFRASTRUCTURE",



"eventType": "AVAILABILITY_EVENT",



"eventStatus": "OPEN",



"tags": [



{



"context": "CONTEXTLESS",



"key": "OS",



"value": "Linux"



}



],



"id": "-6354783141434952927_1669649814889",



"correlationId": "360ad37a6f4de7d0",



"source": "builtin"



}



]



}
```

### Ingest a third-party event

In this example, we ingest a custom info event affecting all hosts whose hostname begins with `prod`.

Events v2

Events v1

#### Request URL

```
POST https://mySampleEnv.live.dynatrace.com/api/v2/events
```

#### Request body

```
{



"eventType": "AVAILABILITY_EVENT",



"title": "Critical service outage",



"timeout": 30,



"entitySelector": "type(HOST),entityName.startsWith(prod)",



"allowDavisMerge": false,



"properties": {



"custom property 1": "my property value 1",



"custom property 2": "my property value 2"



}



}
```

In the Events API v1, it is not possible to select multiple entities via the entity selector. You have to either specify each entity or rely on tags.

#### Request URL

```
POST https://mySampleEnv.live.dynatrace.com/api/v1/events
```

#### Request body

```
{



"eventType": "AVAILABILITY_EVENT",



"title": "Critical service outage",



"description": "REST example",



"timeoutMinutes": 30,



"attachRules": {



"tagRule": [



{



"meTypes": [



"HOST"



],



"tags": [



{



"context": "CONTEXTLESS",



"key": "stage",



"value": "production"



}



]



}



]



},



"source": "REST API"



}
```

## Related topics

* [Events API v2](/docs/dynatrace-api/environment-api/events-v2 "Find out what you can do with the Dynatrace Events API v2.")
* [Events API v1](/docs/dynatrace-api/environment-api/events-v1 "Find out what you can do with the Dynatrace Events API.")