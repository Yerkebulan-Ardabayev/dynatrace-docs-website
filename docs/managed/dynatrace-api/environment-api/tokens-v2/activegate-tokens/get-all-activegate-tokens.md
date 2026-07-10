---
title: ActiveGate tokens API - GET all tokens
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/tokens-v2/activegate-tokens/get-all-activegate-tokens
---

# ActiveGate tokens API - GET all tokens

# ActiveGate tokens API - GET all tokens

* Reference
* Published Dec 02, 2021

Lists all ActiveGate tokens available for your environment.

You can limit the output by using the pagination:

1. Specify the number of results per page in the **pageSize** query parameter.
2. Then use the cursor from the **nextPageKey** field of the previous response in the **nextPageKey** query parameter to obtain subsequent pages.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/activeGateTokens` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/activeGateTokens` |

## Authentication

To execute this request, you need an access token with `activeGateTokenManagement.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| nextPageKey | string | The cursor for the next page of results. You can find it in the **nextPageKey** field of the previous response.  The first page is always returned if you don't specify the **nextPageKey** query parameter.  When the **nextPageKey** is set to obtain subsequent pages, you must omit all other query parameters. | query | Optional |
| pageSize | integer | The amount of ActiveGate tokens in a single response payload.  The maximal allowed page size is 3000 and the minimal size is 100.  If not set, 100 is used. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ActiveGateTokenList](#openapi-definition-ActiveGateTokenList) | Success. The response contains the list of ActiveGate tokens. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The requested resource doesn't exist. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ActiveGateTokenList` object

A list of ActiveGate tokens.

| Element | Type | Description |
| --- | --- | --- |
| activeGateTokens | [ActiveGateToken](#openapi-definition-ActiveGateToken)[] | A list of ActiveGate tokens. |
| nextPageKey | string | The cursor for the next page of results. Has the value of `null` on the last page.  Use it in the **nextPageKey** query parameter to obtain subsequent pages of the result. |
| pageSize | integer | The number of entries per page. |
| totalCount | integer | The total number of entries in the result. |

#### The `ActiveGateToken` object

Metadata of an ActiveGate token.

| Element | Type | Description |
| --- | --- | --- |
| activeGateType | string | The type of the ActiveGate for which the token is valid. The element can hold these values * `ENVIRONMENT` * `CLUSTER` |
| creationDate | string | The token creation date in ISO 8601 format (`yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`). |
| expirationDate | string | The token expiration date in ISO 8601 format (`yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`).  If not set, the token never expires. |
| id | string | The ActiveGate token identifier, consisting of [prefix and public part﻿](https://dt-url.net/rn00tjg?dt=m) of the token. |
| lastUsedDate | string | The token last used date in ISO 8601 format (`yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`). |
| name | string | The name of the token. |
| owner | string | The owner of the token. |
| seedToken | boolean | The token is a seed token (`true`) or an individual token (`false`). |

#### The `ErrorEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### The `Error` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | A list of constraint violations |
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



"activeGateTokens": {



"activeGateType": "ENVIRONMENT",



"creationDate": "2020-11-22T08:15:30.144Z",



"expirationDate": "2020-11-24T08:15:30.144Z",



"id": "dt0g02.4KWZO5EF",



"lastUsedDate": "2020-11-23T08:15:30.144Z",



"name": "myToken",



"owner": "john.smith",



"seedToken": "false"



},



"nextPageKey": "AAAAAAAAAAAAAABOAAAAAAAAAAAAAAA6ACQAEAAAABgACgAITFdXQk1BRzYAAAhtZXRhZGF0YQB___-bf___m3iIYxfF7xVQvY72rwblQkcAAwAAAAAAAADHAAAAZA==",



"pageSize": 100,



"totalCount": 1000



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

In this example, the request lists all ActiveGate tokens available for the **mySampleEnv** environment.

The API token is passed in the **Authorization** header.

The result is truncated to three entries.

#### Curl

```
curl --request GET \



--url https://mySampleEnv.live.dynatrace.com//api/v2/activeGateTokens \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com//api/v2/activeGateTokens
```

#### Response body

```
{



"totalCount": 3,



"pageSize": 3,



"activeGateTokens": [



{



"id": "dt0g02.abc123",



"name": "system:installer",



"owner": "max.mustermann@company.com",



"creationDate": "2021-11-22T11:39:29.797Z",



"seedToken": true,



"activeGateType": "ENVIRONMENT"



},



{



"id": "dt0g02.321cba",



"name": "system:installer",



"owner": "john.smith@company.com",



"creationDate": "2021-11-30T14:11:40.913Z",



"seedToken": true,



"activeGateType": "ENVIRONMENT"



},



{



"id": "dt0g02.123abc",



"name": "system:initial-setup",



"owner": "mary.brown@company.com",



"creationDate": "2021-10-22T13:48:00.135Z",



"lastUsedDate": "2021-12-02T11:52:17.201Z",



"seedToken": false,



"activeGateType": "ENVIRONMENT"



},



]



}
```

#### Response code

200

## Related topics

* [Dynatrace ActiveGate](/managed/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.")