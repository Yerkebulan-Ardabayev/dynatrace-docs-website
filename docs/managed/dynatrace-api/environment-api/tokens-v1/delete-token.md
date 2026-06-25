---
title: Tokens API v1 - DELETE an existing token
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/tokens-v1/delete-token
scraped: 2026-05-12T12:11:11.376981
---

# Tokens API v1 - DELETE an existing token

# Tokens API v1 - DELETE an existing token

* Reference
* Updated on May 17, 2022

This API is deprecated. Use the [Access tokens API](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens "Manage Dynatrace API authentication tokens.") instead.

Updates the specified Dynatrace API authentication token.

This request enables you to delete any token, including tokens not owned by the user who owns the token used to authenticate the call.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/tokens/{id}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/tokens/{id}` |

## Authentication

To execute this request, you need an access token with `TenantTokenManagement` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the token to be deleted. Can either be the public identifier or the secret.  You can't delete the token you're using for authentication of the request. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. You can't delete the token you're using for authentication of the request. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The requested token has not been found. |
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

In this example, the request deletes the token with ID value **4e9f128e-04f9-4795-8b7c-3c14a5e885e4**. The response code of **204** indicates that the deletion was successful.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X DELETE \



https://mySampleEnv.live.dynatrace.com/api/v1/tokens/4e9f128e-04f9-4795-8b7c-3c14a5e885e4 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/tokens/4e9f128e-04f9-4795-8b7c-3c14a5e885e4
```

#### Response code

204