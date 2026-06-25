---
title: Mobile and custom app API - POST user session property
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/user-action-and-session-properties/post-property
scraped: 2026-05-12T11:15:26.476462
---

# Mobile and custom app API - POST user session property

# Mobile and custom app API - POST user session property

* Reference
* Published Nov 05, 2020

Creates a new user session property in the specified application.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{applicationId}/userActionAndSessionProperties` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{applicationId}/userActionAndSessionProperties` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| applicationId | string | The UUID of the required mobile or custom application. It can be found in the Instrumentation Wizard of your app. | path | Required |
| body | [MobileSessionUserActionProperty](#openapi-definition-MobileSessionUserActionProperty) | The JSON body of the request. Contains the configuration of the property. | body | Optional |

### Request body objects

#### The `MobileSessionUserActionProperty` object

Configuration of the mobile session or user action property.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| aggregation | string | The aggregation type of the property.  It defines how multiple values of the property are aggregated. The element can hold these values * `AVERAGE` * `FIRST` * `LAST` * `MAX` * `MIN` * `SUM` | Optional |
| cleanupRule | string | The cleanup rule of the property.  Defines how to extract the data you need from a string value. Specify the [regular expressionï»¿](https://dt-url.net/k9e0iaq) for the data you need there. | Optional |
| displayName | string | The display name of the property. | Optional |
| key | string | The unique key of the mobile session or user action property. | Required |
| name | string | The name of the reported value.  Only applicable when the **origin** is set to `API`. | Optional |
| origin | string | The origin of the property The element can hold these values * `API` * `SERVER_SIDE_REQUEST_ATTRIBUTE` | Required |
| serverSideRequestAttribute | string | The ID of the request attribute.  Only applicable when the **origin** is set to `SERVER_SIDE_REQUEST_ATTRIBUTE`. | Optional |
| storeAsSessionProperty | boolean | If `true`, the property is stored as a session property | Optional |
| storeAsUserActionProperty | boolean | If `true`, the property is stored as a user action property | Optional |
| type | string | The data type of the property. The element can hold these values * `DOUBLE` * `LONG` * `STRING` | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"aggregation": "AVERAGE",



"cleanupRule": "string",



"displayName": "string",



"key": "string",



"name": "string",



"origin": "API",



"serverSideRequestAttribute": "string",



"storeAsSessionProperty": true,



"storeAsUserActionProperty": true,



"type": "DOUBLE"



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [MobileSessionUserActionPropertyShort](#openapi-definition-MobileSessionUserActionPropertyShort) | Success. The property has been created. The response contains the ID of the new property. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |

### Response body objects

#### The `MobileSessionUserActionPropertyShort` object

A short representation of mobile session or user action property.

| Element | Type | Description |
| --- | --- | --- |
| displayName | string | The display name of the session or user action property. |
| key | string | The key of the session or user action property. |

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



"displayName": "string",



"key": "string"



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

## Validate payload

We recommend that you validate the payload before submitting it with an actual request. A response code of **204** indicates a valid payload.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{applicationId}/userActionAndSessionProperties/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{applicationId}/userActionAndSessionProperties/validator` |

### Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Response

#### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. The submitted configuration is valid. Response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |

#### Response body objects

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

#### Response body JSON models

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