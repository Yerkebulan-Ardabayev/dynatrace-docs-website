---
title: Settings API - POST an object
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/settings/objects/post-object
scraped: 2026-02-15T21:15:32.265311
---

# Settings API - POST an object

# Settings API - POST an object

* Reference
* Published Feb 24, 2021

Creates a new settings object or validates the provided settings object.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/objects` |
| POST | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/settings/objects` |

## Authentication

To execute this request, you need an access token with `settings.write` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| validateOnly | boolean | If `true`, the request runs only validation of the submitted settings objects, without saving them. | query | Optional |
| adminAccess | boolean | If set to true and user has settings:objects:admin permission, the endpoint will act as if the user is the owner of all objects | query | Optional |
| body | [SettingsObjectCreate[]](#openapi-definition-SettingsObjectCreate) | The JSON body of the request. Contains the settings objects. | body | Optional |

### Request body objects

#### The `RequestBody` object

#### The `SettingsObjectCreate` object

Configuration of a new settings object.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| externalId | string | External identifier for the object being created | Optional |
| insertAfter | string | The position of the new object. The new object will be added after the specified one.  If `null` (or unset), the new object will be placed in the last position.  If set to an empty string, the new object will be placed in the first position.  Only applicable for objects based on schemas with ordered objects (schema's `ordered` parameter is set to `true`). | Optional |
| objectId | string | The ID of the settings object that should be replaced.  Only applicable if an external identifier is provided. | Optional |
| schemaId | string | The schema on which the object is based. | Required |
| schemaVersion | string | The version of the schema on which the object is based. | Optional |
| scope | string | The scope that the object targets. For more details, please see [Dynatrace Documentationï»¿](https://dt-url.net/ky03459). | Required |
| value | string | The value of the setting.  It defines the actual values of settings' parameters.  The actual content depends on the object's schema. | Required |

#### The `AnyValue` object

A schema representing an arbitrary value type.

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
[



{



"externalId": "string",



"insertAfter": "Y2ktaGdyb3VwLTEyMythZjhjOThlOS0wN2I0LTMyMGEtOTQzNi02NTEyMmVlNWY4NGQ=",



"objectId": "Y2ktaGdyb3VwLTEyMythZjhjOThlOS0wN2I0LTMyMGEtOTQzNi02NTEyMmVlNWY4NGQ=",



"schemaId": "builtin:container.built-in-monitoring-rule",



"schemaVersion": "1.0.0",



"scope": "HOST-D3A3C5A146830A79",



"value": "string"



}



]
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [SettingsObjectResponse[]](#openapi-definition-SettingsObjectResponse) | Success |
| **207** | [SettingsObjectResponse[]](#openapi-definition-SettingsObjectResponse) | Multi-status: different objects in the payload resulted in different statuses. |
| **400** | [SettingsObjectResponse[]](#openapi-definition-SettingsObjectResponse) | Failed. Schema validation failed. |
| **403** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. Forbidden. |
| **404** | [SettingsObjectResponse[]](#openapi-definition-SettingsObjectResponse) | Failed. The requested resource doesn't exist. |
| **409** | [SettingsObjectResponse[]](#openapi-definition-SettingsObjectResponse) | Failed. Conflicting resource. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ResponseBody` object

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

#### The `ErrorResponseBody` object

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
[



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



]
```

```
[



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



]
```