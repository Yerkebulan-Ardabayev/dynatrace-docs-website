---
title: Process groups API - POST tags
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/process-groups-api/post-tags
scraped: 2026-02-17T04:50:52.529487
---

# Process groups API - POST tags

# Process groups API - POST tags

* Reference
* Updated on Mar 22, 2023
* Deprecated

Assigns [custom tags](/docs/manage/tags-and-metadata "Learn how to define tags and metadata. Understand how to use tags and metadata to organize your environment.") to the specified [process group](/docs/observe/infrastructure-observability/process-groups "Analyze process groups and customize process group naming, detection, and monitoring."). You need only provide a tag value. The `CONTEXTLESS` context will be assigned automatically.

The usage of this API is limited to value-only tags. To assign key:value tags, use the [Custom tags API](/docs/dynatrace-api/environment-api/custom-tags/post-tags "Assign custom tags to monitored entities via Dynatrace API.").

The request produces an `application/json`

|  |  |  |
| --- | --- | --- |
| POST | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/infrastructure/process-groups/{meIdentifier}` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/infrastructure/process-groups/{meIdentifier}` |

## Authentication

To execute this request, you need an access token with `DataExport` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| meIdentifier | string | The Dynatrace entity ID of the process group to be updated. | path | Required |
| body | [UpdateEntity](#openapi-definition-UpdateEntity) | The JSON body of the request. Contains tags to be added to the process group. | body | Optional |

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
| **204** | - | Success. The parameters of the process group have been updated. |
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

In this example, the request assigns the **PHP** tag to the **PHP-FPM** process group, which has the ID of **PROCESS\_GROUP-E5C3CC7EC1F80B5B**.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/process-groups/PROCESS_GROUP-E5C3CC7EC1F80B5B \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"tags": [



"PHP"



]



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/process-groups/PROCESS_GROUP-E5C3CC7EC1F80B5B
```

#### Request body

```
{



"tags": [



"PHP"



]



}
```

#### Response code

204

## Related topics

* [Process groups](/docs/observe/infrastructure-observability/process-groups "Analyze process groups and customize process group naming, detection, and monitoring.")