---
title: Applications API - GET all apps
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/applications-api/get-all
scraped: 2026-02-28T21:17:44.835905
---

# Applications API - GET all apps

# Applications API - GET all apps

* Reference
* Updated on Mar 22, 2023
* Deprecated

This API is deprecated. Use the [Monitored entities API](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.") instead. You can find more information about switching to the new API in the [migration guide](/docs/dynatrace-api/basics/deprecation-migration-guides/topology-v1-to-entity-v2 "Migrate your automation to the Monitored entities API.").

Fetches the list of all [applications](/docs/discover-dynatrace/get-started/glossary#app "Get acquainted with Dynatrace terminology.") in your Dynatrace environment, along with their parameters.

The full list can be lengthy, so you can narrow it down by specifying filter parameters, like tags. See the **Parameters** section for more details.

You can additionally limit the output by using the pagination:

1. Specify the number of results per page in the **pageSize** query parameter.
2. Then use the cursor from the **Next-Page-Key** response header in the **nextPageKey** query parameter to obtain subsequent pages.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/applications` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/applications` |

## Authentication

To execute this request, you need an access token with `DataExport` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| startTimestamp | integer | The start timestamp of the requested timeframe, in milliseconds (UTC).  If not set, then 72 hours behind from now is used. | query | Optional |
| endTimestamp | integer | The end timestamp of the requested timeframe, in milliseconds (UTC).  If not set, then the current timestamp is used.  The timeframe must not exceed 3 days. | query | Optional |
| relativeTime | string | The relative timeframe, back from now. The element can hold these values * `min` * `5mins` * `10mins` * `15mins` * `30mins` * `hour` * `2hours` * `6hours` * `day` * `3days` | query | Optional |
| tag | string[] | Filters the resulting set of applications by the specified tag. You can specify several tags in the following format: `tag=tag1&tag=tag2`. The application has to match **all** the specified tags.  In case of key-value tags, such as imported AWS or CloudFoundry tags, use the following format: `tag=[context]key:value`. For custom key-value tags, omit the context: `tag=key:value`. | query | Optional |
| entity | string[] | Filters result to the specified applications only.  To specify several applications use the following format: `entity=ID1&entity=ID2`. | query | Optional |
| managementZone | integer | Only return applications that are part of the specified management zone. | query | Optional |
| includeDetails | boolean | Includes (`true`) or excludes (`false`) details which are queried from related entities.  Excluding details may make queries faster.  If not set, then `true` is used. | query | Optional |
| pageSize | integer | The number of applications per result page.  If not set, pagination is not used and the result contains all applications fitting the specified filtering criteria. | query | Optional |
| nextPageKey | string | The cursor for the next page of results. You can find it in the **Next-Page-Key** header of the previous response.  If you're using pagination, the first page is always returned without this cursor.  You must keep all other query parameters as they were in the first request to obtain subsequent pages. | query | Optional |

## Response headers

| Header | Type | Description |
| --- | --- | --- |
| Total-Count | integer | The estimated number of results. |
| Next-Page-Key | string | The cursor for the next page of results. Without it you'll get the first page again. |
| Page-Size | string | The maximum number of results per page. |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [Application[]](#openapi-definition-Application) | Success |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ResponseBody` object

#### The `Application` object

| Element | Type | Description |
| --- | --- | --- |
| applicationMatchTarget | string | -The element can hold these values * `DOMAIN` * `URL` |
| applicationType | string | -The element can hold these values * `AGENTLESS_MONITORING` * `AUTO_INJECTED` * `DEFAULT` * `SAAS_VENDOR` |
| customizedName | string | The customized name of the entity |
| discoveredName | string | The discovered name of the entity |
| displayName | string | The name of the Dynatrace entity as displayed in the UI. |
| entityId | string | The Dynatrace entity ID of the required entity. |
| firstSeenTimestamp | integer | The timestamp of when the entity was first detected, in UTC milliseconds |
| fromRelationships | object | The list of outgoing calls from the application. |
| lastSeenTimestamp | integer | The timestamp of when the entity was last detected, in UTC milliseconds |
| managementZones | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | The management zones that the entity is part of. |
| ruleAppliedMatchType | string | -The element can hold these values * `ALL_URLS_AND_DOMAINS` * `CONTAINS` * `ENDS` * `EQUALS` * `MATCHES` * `STARTS` |
| ruleAppliedPattern | string | - |
| tags | [TagInfo[]](#openapi-definition-TagInfo) | The list of entity tags. |
| toRelationships | object | The list of incoming calls to the application. |

#### The `EntityShortRepresentation` object

The short representation of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the Dynatrace entity. |
| id | string | The ID of the Dynatrace entity. |
| name | string | The name of the Dynatrace entity. |

#### The `TagInfo` object

Tag of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| context | string | The origin of the tag, such as AWS or Cloud Foundry.  Custom tags use the `CONTEXTLESS` value. The element can hold these values * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | The key of the tag.  Custom tags have the tag value here. |
| value | string | The value of the tag.  Not applicable to custom tags. |

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
[



{



"applicationMatchTarget": "DOMAIN",



"applicationType": "AGENTLESS_MONITORING",



"customizedName": "string",



"discoveredName": "string",



"displayName": "string",



"entityId": "string",



"firstSeenTimestamp": 1,



"fromRelationships": {



"calls": [



"string"



]



},



"lastSeenTimestamp": 1,



"managementZones": [



{



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



}



],



"ruleAppliedMatchType": "ALL_URLS_AND_DOMAINS",



"ruleAppliedPattern": "string",



"tags": [



{



"context": "AWS",



"key": "string",



"value": "string"



}



],



"toRelationships": {



"monitors": [



"string"



]



}



}



]
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

In this example, the request asks for a list all the applications in the environment.

The API token is passed in the **Authorization** header.

The result is truncated to three entries.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/entity/applications/ \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/applications
```

#### Response body

```
[



{



"entityId": "APPLICATION-EA7C4B59F27D43EB",



"displayName": "RUM Default Application",



"customizedName": "RUM Default Application",



"discoveredName": "RUM Default Application",



"firstSeenTimestamp": 1422282024216,



"lastSeenTimestamp": 1538579528065,



"tags": [



{



"context": "CONTEXTLESS",



"key": "Mytag"



},



{



"context": "CONTEXTLESS",



"key": "Test"



}



],



"fromRelationships": {



"calls": [



"SERVICE-FFE4B7A6D72F2CAC"



]



},



"toRelationships": {},



"applicationType": "DEFAULT",



"ruleAppliedPattern": "http",



"managementZones": [



{



"id": "-6239538939987181652",



"name": "allTypes"



},



{



"id": "-2519468841583898843",



"name": "app name exists"



},



{



"id": "4485554873951847460",



"name": "Applications except easyTravel"



}



]



},



{



"entityId": "APPLICATION-BBFA55551D507E2B",



"displayName": "easyTravel Ionic Web",



"discoveredName": "easyTravel Ionic Web",



"firstSeenTimestamp": 1528695861873,



"lastSeenTimestamp": 1538572321269,



"tags": [],



"fromRelationships": {



"calls": [



"SERVICE-ED0B103392AC86BF"



]



},



"toRelationships": {},



"applicationType": "RUMONLY",



"managementZones": [



{



"id": "-6239538939987181652",



"name": "allTypes"



},



{



"id": "-4085081632192243904",



"name": "easyTravel"



}



]



},



{



"entityId": "MOBILE_APPLICATION-752C288D59734C79",



"displayName": "easyTravel Demo",



"customizedName": "easyTravel Demo",



"discoveredName": "752c288d-5973-4c79-b7d1-3a49d4d42ea0",



"firstSeenTimestamp": 1469613941393,



"lastSeenTimestamp": 1538654940201,



"tags": [



{



"context": "CONTEXTLESS",



"key": "portal"



},



{



"context": "CONTEXTLESS",



"key": "easyTravel"



}



],



"fromRelationships": {



"calls": [



"SERVICE-ED0B103392AC86BF"



]



},



"toRelationships": {},



"mobileOsFamily": [



"ANDROID",



"IOS",



"WINDOWS"



],



"managementZones": [



{



"id": "-4085081632192243904",



"name": "easyTravel"



}



]



}



]
```

#### Response code

200

## Related topics

* [Real User Monitoring](/docs/observe/digital-experience/rum-concepts/rum-overview "Learn about Real User Monitoring, key performance metrics, mobile app monitoring, and more.")