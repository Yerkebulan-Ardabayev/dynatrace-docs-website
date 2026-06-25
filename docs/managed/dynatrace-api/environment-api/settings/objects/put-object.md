---
title: Settings API - PUT an object
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/objects/put-object
scraped: 2026-05-12T11:38:48.531723
---

# Settings API - PUT an object

# Settings API - PUT an object

* Reference
* Published Feb 24, 2021

Updates the specified settings object.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/objects/{objectId}` |
| PUT | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/settings/objects/{objectId}` |

## Authentication

To execute this request, you need an access token with `settings.write` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

**Note**: The `settings.read` scope is required as well.

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| objectId | string | The ID of the required settings object. | path | Required |
| validateOnly | boolean | If `true`, the request runs only validation of the submitted settings object, without saving it. | query | Optional |
| adminAccess | boolean | If set to true and user has settings:objects:admin permission, the endpoint will act as if the user is the owner of all objects | query | Optional |
| body | [SettingsObjectUpdate](#openapi-definition-SettingsObjectUpdate) | The JSON body of the request. Contains updated parameters of the settings object. | body | Optional |

### Request body objects

#### The `SettingsObjectUpdate` object

An update of a settings object.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| insertAfter | string | The position of the updated object. The new object will be moved behind the specified one.  **insertAfter** and **insertBefore** are evaluated together and only one of both can be set (and be non `null`).  If `null` (or unset) and **insertBefore** is `null` (or unset), the existing object keeps the current position.  If set to an empty string, the updated object will be placed in the first position.  Only applicable for objects based on schemas with ordered objects (schema's **ordered** parameter is set to `true`). | Optional |
| insertBefore | string | The position of the updated object. The new object will be moved in front of the specified one.  **insertAfter** and **insertBefore** are evaluated together and only one of both can be set (and be non `null`).  If `null` (or unset) and **insertAfter** is `null` (or unset), the existing object keeps the current position.  If set to an empty string, the updated object will be placed in the last position.  Only applicable for objects based on schemas with ordered objects (schema's **ordered** parameter is set to `true`). | Optional |
| schemaVersion | string | The version of the schema on which the object is based. | Optional |
| updateToken | string | The update token of the object. You can use it to detect simultaneous modifications by different users.  It is generated upon retrieval (GET requests). If set on update (PUT request) or deletion, the update/deletion will be allowed only if there wasn't any change between the retrieval and the update.  If omitted on update/deletion, the operation overrides the current value or deletes it without any checks. | Optional |
| value | string | The value of the setting.  It defines the actual values of settings' parameters.  The actual content depends on the object's schema. | Required |

#### The `AnyValue` object

A schema representing an arbitrary value type.

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"insertAfter": "Y2ktaGdyb3VwLTEyMythZjhjOThlOS0wN2I0LTMyMGEtOTQzNi02NTEyMmVlNWY4NGQ=",



"insertBefore": "Y2ktaGdyb3VwLTEyMythZjhjOThlOS0wN2I0LTMyMGEtOTQzNi02NTEyMmVlNWY4NGQ=",



"schemaVersion": "1.0.0",



"updateToken": "Y2ktaGdyb3VwLTEyMythZjhjOThlOS0wN2I0LTMyMGEtOTQzNi02NTEyMmVlNWY4NGQ=",



"value": "string"



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [SettingsObjectResponse](#openapi-definition-SettingsObjectResponse) | Success |
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
| invalidValue | string | The value of the setting.  It defines the actual values of settings' parameters.  The actual content depends on the object's schema. |
| objectId | string | For a successful request, the ID of the created or modified settings object. |

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

#### The `AnyValue` object

A schema representing an arbitrary value type.

#### The `SettingsObjectResponse` object

The response to a creation- or update-request.

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code for the object. |
| error | [Error](#openapi-definition-Error) | - |
| invalidValue | string | The value of the setting.  It defines the actual values of settings' parameters.  The actual content depends on the object's schema. |
| objectId | string | For a successful request, the ID of the created or modified settings object. |

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



"invalidValue": "string",



"objectId": "Y2ktaGdyb3VwLTEyMythZjhjOThlOS0wN2I0LTMyMGEtOTQzNi02NTEyMmVlNWY4NGQ="



}
```

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



"invalidValue": "string",



"objectId": "Y2ktaGdyb3VwLTEyMythZjhjOThlOS0wN2I0LTMyMGEtOTQzNi02NTEyMmVlNWY4NGQ="



}
```