---
title: Migrate from Problems API v1 to Problems API v2
source: https://www.dynatrace.com/docs/dynatrace-api/basics/deprecation-migration-guides/problems-v1-to-v2
scraped: 2026-02-17T21:33:48.205554
---

# Migrate from Problems API v1 to Problems API v2

# Migrate from Problems API v1 to Problems API v2

* Reference
* Published Nov 30, 2022

[Problems API v1](/docs/dynatrace-api/environment-api/problems "Find out what the Dynatrace Problems v1 API offers.") has been deprecated with [Dynatrace version 1.243](/docs/whats-new/dynatrace-api/sprint-243 "Changelog for Dynatrace API version 1.243"). Its replacement is [Problems API v2](/docs/dynatrace-api/environment-api/problems-v2 "Find out what the Dynatrace Problems v2 API offers."). We recommend that you migrate to the new API at your earliest convenience.

The migration affects endpoint URLs, query parameters, and response/request body parameters, as well as the scope of the token for request authentication.

## New features

Events API v2 offers you the following new features:

* The [entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.") helps you to filter problems in read requests.
* Improved problem filtering via a problem selector.
* Unified timeframe selector.

## Base URL

| new Problems v2 | old Problems v1 |
| --- | --- |
| `/api/v2/problems` | `/api/v1/problem` |

## Authentication token scope

| new Problems v2 | old Problems v1 |
| --- | --- |
| **Read problems** (`problems.read`) **Write problems** (`problems.write`) | **Access problem and event feed, metrics, and topology** (`DataExport`) |

## Parameters

To learn about new query/body parameters, see the documentation of individual requests in [Problems API v2](/docs/dynatrace-api/environment-api/problems-v2 "Find out what the Dynatrace Problems v2 API offers.").

## Example

In this example, we query a list of open problems on hosts that happened within the last two hours.

Problems v2

Problems v1

#### Request URL

```
GET https://mySampleEnv.live.dynatrace.com/api/v2/problems?from=now-2h&problemSelector=status("open")&entitySelector=type("HOST")
```

#### Response body

```
{



"totalCount": 2,



"pageSize": 50,



"problems": [



{



"problemId": "-6156404735398726308_1669823466223V2",



"displayId": "P-221194163",



"title": "Host or monitoring unavailable",



"impactLevel": "INFRASTRUCTURE",



"severityLevel": "AVAILABILITY",



"status": "OPEN",



"affectedEntities": [



{



"entityId": {



"id": "HOST-E371A974A078CC54",



"type": "HOST"



},



"name": "frontend-dev"



}



],



"impactedEntities": [



{



"entityId": {



"id": "HOST-E371A974A078CC54",



"type": "HOST"



},



"name": "frontend-dev"



}



],



"rootCauseEntity": null,



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



"problemFilters": [



{



"id": "ca786d1f-e6cf-4451-b9dc-9c27c5c339e1",



"name": "Infrastructure alerts"



},



{



"id": "d03022be-d0e3-4089-b02d-ebec9ae87da4",



"name": "Frontend alerts"



}



],



"startTime": 1669823466223,



"endTime": -1



},



{



"problemId": "7188776519218424524_1669820820000V2",



"displayId": "P-221194115",



"title": "High memory usage",



"impactLevel": "INFRASTRUCTURE",



"severityLevel": "CUSTOM_ALERT",



"status": "OPEN",



"affectedEntities": [



{



"entityId": {



"id": "HOST-0F5789A6850FA907",



"type": "HOST"



},



"name": "easyTravel.bookingService.Win.1"



}



],



"impactedEntities": [



{



"entityId": {



"id": "HOST-0F5789A6850FA907",



"type": "HOST"



},



"name": "easyTravel.bookingService.Win.dev.1"



}



],



"rootCauseEntity": null,



"managementZones": [



{



"id": "4067143719293196613",



"name": "dev"



},



{



"id": "7918335421727549830",



"name": "Infrastructure windows"



},



{



"id": "-6239538939987181652",



"name": "Booking service"



}



],



"entityTags": [



{



"context": "CONTEXTLESS",



"key": "stage",



"value": "dev",



"stringRepresentation": "stage:dev"



},



{



"context": "CONTEXTLESS",



"key": "bookingService",



"stringRepresentation": "bookingService"



}



],



"problemFilters": [



{



"id": "ca786d1f-e6cf-4451-b9dc-9c27c5c339e1",



"name": "Infrastructure alerts"



},



{



"id": "ff956dac-8709-3546-bf2b-d82195e7ef6a",



"name": "Booking service alerts"



}



],



"startTime": 1669821000000,



"endTime": -1



}



],



"warnings": []



}
```

In Events API v1, it is not possible to select multiple entities via the entity selector. You have to rely on tags. For illustration purposes, the example payload shows the same problems, but you would have to find them in the payload by external means.

#### Request URL

```
GET https://mySampleEnv.live.dynatrace.com/api/v1/problem/feed?relativeTime=2hours&status=OPEN&tag=stage:dev
```

#### Response body

```
{



"result": {



"problems": [



{



"id": "-6156404735398726308_1669823466223V2",



"startTime": 1669823466223,



"endTime": -1,



"displayName": "P-221194163",



"impactLevel": "INFRASTRUCTURE",



"status": "OPEN",



"severityLevel": "AVAILABILITY",



"commentCount": 0,



"tagsOfAffectedEntities": [



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



"rankedImpacts": [



{



"entityId": "HOST-E371A974A078CC54",



"entityName": "frontend-dev",



"severityLevel": "AVAILABILITY",



"impactLevel": "INFRASTRUCTURE",



"eventType": "CONNECTION_LOST"



}



],



"affectedCounts": {



"INFRASTRUCTURE": 1,



"SERVICE": 0,



"APPLICATION": 0,



"ENVIRONMENT": 0



},



"recoveredCounts": {



"INFRASTRUCTURE": 0,



"SERVICE": 0,



"APPLICATION": 0,



"ENVIRONMENT": 0



},



"hasRootCause": false



},



{



"id": "7188776519218424524_1669820820000V2",



"startTime": 1669821000000,



"endTime": -1,



"displayName": "P-221194115",



"impactLevel": "INFRASTRUCTURE",



"status": "OPEN",



"severityLevel": "CUSTOM_ALERT",



"commentCount": 0,



"tagsOfAffectedEntities": [



{



"context": "CONTEXTLESS",



"key": "stage",



"value": "dev"



},



{



"context": "CONTEXTLESS",



"key": "bookingService"



}



],



"rankedImpacts": [



{



"entityId": "HOST-0F5789A6850FA907",



"entityName": "easyTravel.bookingService.Win.1",



"severityLevel": "CUSTOM_ALERT",



"impactLevel": "INFRASTRUCTURE",



"eventType": "CUSTOM_ALERT"



}



],



"affectedCounts": {



"INFRASTRUCTURE": 1,



"SERVICE": 0,



"APPLICATION": 0,



"ENVIRONMENT": 0



},



"recoveredCounts": {



"INFRASTRUCTURE": 0,



"SERVICE": 0,



"APPLICATION": 0,



"ENVIRONMENT": 0



},



"hasRootCause": false



}



]



}



}
```

## Related topics

* [Problems API v2](/docs/dynatrace-api/environment-api/problems-v2 "Find out what the Dynatrace Problems v2 API offers.")
* [Problems API v1](/docs/dynatrace-api/environment-api/problems "Find out what the Dynatrace Problems v1 API offers.")