---
title: ActiveGate tokens API - POST a token
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/tokens-v2/activegate-tokens/post-activegate-token
---

# ActiveGate tokens API - POST a token

# ActiveGate tokens API - POST a token

* Reference
* Published Dec 02, 2021

Creates a new ActiveGate token.

The token will be owned by the user who owns the token used to authenticate the call.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/activeGateTokens` |
| POST | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/activeGateTokens` |

## Authentication

To execute this request, you need an access token with one of the following scopes:

* `activeGateTokenManagement.create`
* `activeGateTokenManagement.write`

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [ActiveGateTokenCreate](#openapi-definition-ActiveGateTokenCreate) | The JSON body of the request. Contains parameters of the new ActiveGate token. | body | Required |

### Request body objects

#### The `ActiveGateTokenCreate` object

Parameters of a new ActiveGate token.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| activeGateType | string | The type of the ActiveGate for which the token is valid. The element can hold these values * `ENVIRONMENT` * `CLUSTER` | Required |
| expirationDate | string | The expiration date of the token.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the token never expires.  Ensure that it is not set in the past and does not exceed `2 years` from the moment of creation." | Optional |
| name | string | The name of the token. | Required |
| seedToken | boolean | The token is a seed token (`true`) or an individual token (`false`).  We recommend the individual token option (false). | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"activeGateType": "ENVIRONMENT",



"expirationDate": "now+6M",



"name": "myToken",



"seedToken": false



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [ActiveGateTokenCreated](#openapi-definition-ActiveGateTokenCreated) | Success. The token has been created. The body of the response contains the token secret. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ActiveGateTokenCreated` object

The newly created ActiveGate token.

| Element | Type | Description |
| --- | --- | --- |
| expirationDate | string | The token expiration date in ISO 8601 format (`yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`). |
| id | string | The ActiveGate token identifier, consisting of [prefix and public part﻿](https://dt-url.net/rn00tjg?dt=m) of the token. |
| token | string | The secret of the token. |

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



"expirationDate": "2020-11-24T08:15:30.144Z",



"id": "dt0g02.4KWZO5EF",



"token": "dt0g02.4KWZO5EF.XT47R5DRADJIZUFOX4UDNOKTSUSABGLN7XSMJG7UXHRXKNY4WLORH4OF4T75MG7E"



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

In this example, the request creates a new ActiveGate token for an environment ActiveGate. The token is valid for two weeks (14 days) from the moment of creation.

The API token is passed in the **Authorization** header.

#### Curl

```
curl --request GET \



--url https://mySampleEnv.live.dynatrace.com//api/v2/activeGateTokens \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



--header 'Content-Type: application/json' \



--data '{



"name": "REST test",



"expirationDate": "now+14d",



"seedToken": false,



"activeGateType": "ENVIRONMENT"



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com//api/v2/activeGateTokens
```

#### Request body

```
{



"name": "REST test",



"expirationDate": "now+14d",



"seedToken": false,



"activeGateType": "ENVIRONMENT"



}
```

#### Response body

```
{



"id": "dt0g02.xyz789",



"token": "dt0g02.xyz789.987654321zyxwvutsrq",



"expirationDate": "2021-12-14T13:42:31.148Z"



}
```

#### Response code

201

## Related topics

* [Dynatrace ActiveGate](/managed/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.")