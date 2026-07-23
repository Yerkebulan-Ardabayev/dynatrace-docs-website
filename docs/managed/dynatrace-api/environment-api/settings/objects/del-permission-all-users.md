---
title: Settings API - DELETE all-users permission
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/objects/del-permission-all-users
---

# Settings API - DELETE all-users permission

# Settings API - DELETE all-users permission

* Reference
* Published Jul 09, 2026

Removes permissions for the all-users accessor on the specified settings object. Deletion cannot be undone!

This endpoint applies only to objects on schemas with owner-based access control enabled (`ownerBasedAccessControl: true`). To identify such schemas, include `ownerBasedAccessControl` in the `add-fields` parameter when calling [List schemas](/managed/dynatrace-api/environment-api/settings/schemas/get-all "View all settings schemas of your monitoring environment via the Dynatrace API.").

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/v2/settings/objects/{objectId}/permissions/all-users` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/v2/settings/objects/{objectId}/permissions/all-users` |

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| objectId | string | The ID of the required settings object. | path | Required |
| adminAccess | boolean | If set to true and user has settings:objects:admin permission, the endpoint will act as if the user is the owner of all objects | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | No object available for the given objectId or the all-users accessor doesn't have any permissions on this object. |
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