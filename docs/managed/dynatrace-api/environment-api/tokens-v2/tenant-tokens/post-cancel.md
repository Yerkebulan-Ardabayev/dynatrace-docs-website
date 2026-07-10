---
title: Tenant tokens API - POST cancel rotation
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/tokens-v2/tenant-tokens/post-cancel
---

# Tenant tokens API - POST cancel rotation

# Tenant tokens API - POST cancel rotation

* Reference
* Published Feb 23, 2021

Cancels the rotation of the tenant token. The new token is discarded and the old token remains valid. If you [configured](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token "Learn what a tenant token is and how to change it.") any OneAgents and ActiveGates to use the new token, you must restore the old configuration.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/tenantTokenRotation/cancel` |
| POST | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/tenantTokenRotation/cancel` |

## Authentication

To execute this request, you need an access token with `tenantTokenRotation.write` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [TenantTokenConfig](#openapi-definition-TenantTokenConfig) | Success. Rotation process has been cancelled. The current tenant token remains valid. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. There is no ongoing rotation process. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `TenantTokenConfig` object

Configuration of a [tenant token﻿](https://dt-url.net/b403ss9?dt=m).

| Element | Type | Description |
| --- | --- | --- |
| active | [TenantToken](#openapi-definition-TenantToken) | Tenant token |
| old | [TenantToken](#openapi-definition-TenantToken) | Tenant token |

#### The `TenantToken` object

Tenant token

| Element | Type | Description |
| --- | --- | --- |
| value | string | The secret of the tenant token. |

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



"active": {



"value": "string"



},



"old": {}



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

In this example, the request cancels the rotation process started in [start request example](/managed/dynatrace-api/environment-api/tokens-v2/tenant-tokens/post-start#example "Initiate Dynatrace tenant token rotation.").

The response code of **200** indicates a successful request. The old token **1234567890qrstuvwxyz** remains valid; the new token is discarded.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/v2/tenantTokenRotation/finish \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Accept: application/json'
```

#### Response body

```
{



"active": {



"value": "1234567890qrstuvwxyz"



},



"old": {



"value": null



}



}
```

#### Response code

200

## Related topics

* [Tenant token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token "Learn what a tenant token is and how to change it.")