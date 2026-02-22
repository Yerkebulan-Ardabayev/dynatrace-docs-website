---
title: Applications API - POST tags
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/applications-api/post-tags
scraped: 2026-02-22T21:15:35.656990
---

# Applications API - POST tags

# Applications API - POST tags

* Reference
* Updated on Mar 22, 2023
* Deprecated

Assigns [custom tags](/docs/manage/tags-and-metadata "Learn how to define tags and metadata. Understand how to use tags and metadata to organize your environment.") to the specified application. You only need to provide a tag value. The `CONTEXTLESS` context will be assigned automatically.

The usage of this API is limited to value-only tags. To assign key:value tags, use the [Custom tags API](/docs/dynatrace-api/environment-api/custom-tags/post-tags "Assign custom tags to monitored entities via Dynatrace API.").

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/applications/{meIdentifier}` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/applications/{meIdentifier}` |

## Authentication

To execute this request, you need an access token with `DataExport` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| meIdentifier | string | The Dynatrace entity ID of the application you want to update. | path | Required |
| body | [UpdateEntity](#openapi-definition-UpdateEntity) | A list of tags to be assigned to a Dynatrace entity. | body | Optional |

### Request body objects

#### The `UpdateEntity` object

A list of tags to be assigned to a Dynatrace entity.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| tags | string[] | A list of tags to be assigned to a Dynatrace entity. | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"tags": [



"office-linz",



"office-klagenfurt"



]



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. The parameters of the application have been updated. |
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

## Example

In this example, the request assigns the tags **iOS app** and **Android app** to the **easyTravel Demo** application, which has the ID **MOBILE\_APPLICATION-752C288D59734C79**.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/v1/entity/applications/MOBILE_APPLICATION-752C288D59734C79 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"tags": [



"iOS app",



"Android app"



]



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/applications/MOBILE_APPLICATION-752C288D59734C79
```

#### Request body

```
{



"tags": [



"iOS app",



"Android app"



]



}
```

#### Response code

204

## Related topics

* [Real User Monitoring](/docs/observe/digital-experience/rum-concepts/rum-overview "Learn about Real User Monitoring, key performance metrics, mobile app monitoring, and more.")