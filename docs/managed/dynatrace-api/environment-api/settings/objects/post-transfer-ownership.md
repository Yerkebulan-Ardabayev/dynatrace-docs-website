---
title: Settings API - POST transfer ownership
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/objects/post-transfer-ownership
---

# Settings API - POST transfer ownership

# Settings API - POST transfer ownership

* Reference
* Published Jul 09, 2026

Transfers ownership of the specified settings object. Only the current owner or a user with the `settings:objects:admin` permission (globally or for the relevant schema) can transfer ownership. The previous owner loses access after the transfer unless they are explicitly listed as an accessor on the object.

This endpoint applies only to objects on schemas with owner-based access control enabled (`ownerBasedAccessControl: true`). To identify such schemas, include `ownerBasedAccessControl` in the `add-fields` parameter when calling [List schemas](/managed/dynatrace-api/environment-api/settings/schemas/get-all "View all settings schemas of your monitoring environment via the Dynatrace API.").

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/v2/settings/objects/{objectId}:transfer-ownership` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/v2/settings/objects/{objectId}:transfer-ownership` |

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| objectId | string | The ID of the required settings object. | path | Required |
| adminAccess | boolean | If set to true and user has settings:objects:admin permission, the endpoint will act as if the user is the owner of all objects | query | Optional |
| body | [TransferOwnershipRequest](#openapi-definition-TransferOwnershipRequest) | The JSON body of the request. | body | Optional |

### Request body objects

#### The `TransferOwnershipRequest` object

The request to change ownership of an object.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| newOwner | [Identity](#openapi-definition-Identity) | An Identity describing either a user, a group, or the all-users group (applying to all users). | Optional |

#### The `Identity` object

An Identity describing either a user, a group, or the all-users group (applying to all users).

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| id | string | The user id or user group id if type is 'user' or 'group', missing if type is 'all-users'. | Optional |
| type | string | The type of the identity. The element can hold these values * `all-users` * `group` * `user` | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"newOwner": {



"id": "string",



"type": "user"



}



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. Response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **403** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. Forbidden. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | No object available for the given objectId. |
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