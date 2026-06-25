---
title: ActiveGate tokens API - DELETE a token
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/tokens-v2/activegate-tokens/delete-activegate-token
scraped: 2026-05-12T12:09:59.984198
---

# ActiveGate tokens API - DELETE a token

# ActiveGate tokens API - DELETE a token

* Reference
* Published Dec 02, 2021

Deletes an ActiveGate token.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/activeGateTokens/{activeGateTokenIdentifier}` |
| DELETE | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/activeGateTokens/{activeGateTokenIdentifier}` |

## Authentication

To execute this request, you need an access token with `activeGateTokenManagement.write` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| activeGateTokenIdentifier | string | The ActiveGate token identifier, consisting of [prefix and public partï»¿](https://dt-url.net/rn00tjg) of the token to be deleted. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. Response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The requested resource doesn't exist. |
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

In this example, the request deletes the token with the ID of **dt0g02.xyz789**.

The API token is passed in the **Authorization** header.

#### Curl

```
curl --request DELETE \



--url https://mySampleEnv.live.dynatrace.com//api/v2/activeGateTokens/dt0g02.xyz789 \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com//api/v2/activeGateTokens/dt0g02.xyz789
```

#### Response code

204

## Related topics

* [Dynatrace ActiveGate](/managed/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.")