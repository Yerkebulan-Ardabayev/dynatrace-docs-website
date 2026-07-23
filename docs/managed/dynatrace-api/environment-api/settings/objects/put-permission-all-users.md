---
title: Settings API - PUT all-users permission
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/objects/put-permission-all-users
---

# Settings API - PUT all-users permission

# Settings API - PUT all-users permission

* Reference
* Published Jul 09, 2026

Updates the permissions for the all-users accessor on the specified settings object. Any user with read and write permissions on the object can update permissions.

This endpoint applies only to objects on schemas with owner-based access control enabled (`ownerBasedAccessControl: true`). To identify such schemas, include `ownerBasedAccessControl` in the `add-fields` parameter when calling [List schemas](/managed/dynatrace-api/environment-api/settings/schemas/get-all "View all settings schemas of your monitoring environment via the Dynatrace API.").

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/v2/settings/objects/{objectId}/permissions/all-users` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/v2/settings/objects/{objectId}/permissions/all-users` |

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| objectId | string | The ID of the required settings object. | path | Required |
| adminAccess | boolean | If set to true and user has settings:objects:admin permission, the endpoint will act as if the user is the owner of all objects | query | Optional |
| body | [UpdatePermissionsRequest](#openapi-definition-UpdatePermissionsRequest) | The JSON body of the request. | body | Optional |

### Request body objects

#### The `UpdatePermissionsRequest` object

The request to update the permissions of a specific accessor.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| permissions | string[] | r = read, w = write The element can hold these values * `r` * `w` | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"permissions": [



"r"



]



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | - | Success |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | If permission list is empty, contains unsupported entries or unsupported combinations of entries. |
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