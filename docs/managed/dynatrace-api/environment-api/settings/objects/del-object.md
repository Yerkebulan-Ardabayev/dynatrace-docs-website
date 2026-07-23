---
title: Settings API - DELETE an object
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/objects/del-object
---

# Settings API - DELETE an object

# Settings API - DELETE an object

* Reference
* Updated on Jul 09, 2026

Deletes the specified settings object. Deletion cannot be undone!

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/objects/{objectId}` |
| DELETE | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/settings/objects/{objectId}` |

## Authentication

To execute this request, you need an access token with `settings.write` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| objectId | string | The ID of the required settings object. | path | Required |
| updateToken | string | The update token of the object. You can use it to detect simultaneous modifications by different users.  It is generated upon retrieval (GET requests). If set on update (PUT request) or deletion, the update/deletion will be allowed only if there wasn't any change between the retrieval and the update.  If omitted on update/deletion, the operation overrides the current value or deletes it without any checks. | query | Optional |
| adminAccess | boolean | If set to true and user has settings:objects:admin permission, the endpoint will act as if the user is the owner of all objects | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. Response doesn't have a body. |
| **400** | [SettingsObjectResponse](#openapi-definition-SettingsObjectResponse) | Failed. Schema validation failed. |
| **403** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. Forbidden. |
| **404** | [SettingsObjectResponse](#openapi-definition-SettingsObjectResponse) | Failed. The requested resource doesn't exist. |
| **409** | [SettingsObjectResponse](#openapi-definition-SettingsObjectResponse) | Failed. Conflicting resource. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `SettingsObjectResponse` object

The response to a creation- or update-request.

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code for the object. |
| error | [Error](#openapi-definition-Error) | - |
| invalidValue | [AnyValue](#openapi-definition-AnyValue) | The value of the setting.  It defines the actual values of settings' parameters.  The actual content depends on the object's schema. |
| objectId | string | For a successful request, the ID of the created or modified settings object. |

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

#### The `AnyValue` object

A schema representing an arbitrary value type.

### Response body JSON models

```
{



"code": 1,



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



},



"invalidValue": {



"autoMonitoring": true



},



"objectId": "Y2ktaGdyb3VwLTEyMythZjhjOThlOS0wN2I0LTMyMGEtOTQzNi02NTEyMmVlNWY4NGQ="



}
```