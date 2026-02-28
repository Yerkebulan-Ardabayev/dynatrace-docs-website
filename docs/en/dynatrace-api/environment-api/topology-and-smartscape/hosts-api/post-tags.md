---
title: Hosts API - POST tags
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/hosts-api/post-tags
scraped: 2026-02-28T21:17:52.140709
---

# Hosts API - POST tags

# Hosts API - POST tags

* Reference
* Updated on Mar 22, 2023
* Deprecated

Assigns [custom tags](/docs/manage/tags-and-metadata "Use tags and metadata to organize data in your Dynatrace environment.") to the specified host. You only need to provide a tag value. The `CONTEXTLESS` context will be assigned automatically.

The usage of this API is limited to value-only tags. To assign key:value tags, use the [Custom tags API](/docs/dynatrace-api/environment-api/custom-tags/post-tags "Assign custom tags to monitored entities via Dynatrace API.").

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/infrastructure/hosts/{meIdentifier}` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/infrastructure/hosts/{meIdentifier}` |

## Authentication

To execute this request, you need an access token with `DataExport` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| meIdentifier | string | The Dynatrace entity ID of the host to be updated. | path | Required |
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
| **204** | - | Success. The parameters of the host have been updated. |
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

In this example, the request assigns the **Linux** and **Rack 123** tags to the **tag009** host, which has the ID of **HOST-B7A6F9EE9F366CB5**.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/hosts/HOST-B7A6F9EE9F366CB5 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"tags": [



"Linux",



"Rack 123"



]



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/hosts/HOST-B7A6F9EE9F366CB5
```

#### Request body

```
{



"tags": [



"iOS app",



"Adnroid app"



]



}
```

#### Response code

204

## Related topics

* [Hosts Classic](/docs/observe/infrastructure-observability/hosts "Learn how to get started with host monitoring, understand which measures contribute to host health, how to set up custom host names, and more.")