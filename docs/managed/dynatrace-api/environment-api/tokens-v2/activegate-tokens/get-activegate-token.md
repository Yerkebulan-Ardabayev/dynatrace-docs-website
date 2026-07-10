---
title: ActiveGate tokens API - GET a token
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/tokens-v2/activegate-tokens/get-activegate-token
---

# ActiveGate tokens API - GET a token

# ActiveGate tokens API - GET a token

* Reference
* Published Dec 02, 2021

Gets metadata of the ActiveGate token by its ID.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/activeGateTokens/{activeGateTokenIdentifier}` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/activeGateTokens/{activeGateTokenIdentifier}` |

## Authentication

To execute this request, you need an access token with `activeGateTokenManagement.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| activeGateTokenIdentifier | string | The ActiveGate token identifier, consisting of [prefix and public part﻿](https://dt-url.net/rn00tjg?dt=m) of the token. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ActiveGateToken](#openapi-definition-ActiveGateToken) | Success. The response contains the metadata of the tokens. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The requested resource doesn't exist. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

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



"activeGateType": "ENVIRONMENT",



"creationDate": "2020-11-22T08:15:30.144Z",



"expirationDate": "2020-11-24T08:15:30.144Z",



"id": "dt0g02.4KWZO5EF",



"lastUsedDate": "2020-11-23T08:15:30.144Z",



"name": "myToken",



"owner": "john.smith",



"seedToken": false



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

In this example, the request retrieves metadata for the token with the ID of **dt0g02.abc123**.

The API token is passed in the **Authorization** header.

#### Curl

```
curl --request GET \



--url https://mySampleEnv.live.dynatrace.com//api/v2/activeGateTokens/dt0g02.abc123 \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com//api/v2/activeGateTokens/dt0g02.abc123
```

#### Response body

```
{



"id": "dt0g02.abc123",



"name": "system:installer",



"owner": "max.mustermann@company.com",



"creationDate": "2021-11-22T11:39:29.797Z",



"seedToken": true,



"activeGateType": "ENVIRONMENT"



}
```

#### Response code

200

## Related topics

* [Dynatrace ActiveGate](/managed/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.")