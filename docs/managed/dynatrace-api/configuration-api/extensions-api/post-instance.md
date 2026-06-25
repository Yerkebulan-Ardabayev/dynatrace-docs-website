---
title: Extensions API - POST a new extension's instance
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/extensions-api/post-instance
scraped: 2026-05-12T11:20:04.982355
---

# Extensions API - POST a new extension's instance

# Extensions API - POST a new extension's instance

* Reference
* Published Mar 06, 2020

Creates a new instance for the specified extension.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/extensions/{id}/instances` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/extensions/{id}/instances` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the extension | path | Required |
| body | [ExtensionConfigurationDto](#openapi-definition-ExtensionConfigurationDto) | The JSON body of the request. Contains new configuration of the extension. | body | Optional |

### Request body objects

#### The `ExtensionConfigurationDto` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| activeGate | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | The short representation of a Dynatrace entity. | Optional |
| enabled | boolean | The extension is enabled (`true`) or disabled (`false`). | Required |
| endpointId | string | The ID of the endpoint. | Optional |
| endpointName | string | The name of the endpoint, displayed in Dynatrace. | Optional |
| extensionId | string | The ID of the extension. | Optional |
| hostId | string | The ID of the host on which the extension runs. | Optional |
| properties | object | The list of extension parameters.  Each parameter is a key-value pair. | Optional |
| useGlobal | boolean | Allows to skip current configuration and use global one. | Required |

#### The `EntityShortRepresentation` object

The short representation of a Dynatrace entity.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| description | string | A short description of the Dynatrace entity. | Optional |
| id | string | The ID of the Dynatrace entity. | Required |
| name | string | The name of the Dynatrace entity. | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"activeGate": {



"id": "7835970235169136995",



"name": "ActiveGate Host Name"



},



"enabled": true,



"hostId": "HOST-01A7DEFA5340A86D",



"id": "custom.remote.python.demo",



"properties": {



"dropdownProperty": "three",



"password": "",



"serverIp": "127.0.0.1",



"username": "dynatrace"



},



"useGlobal": false



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Success. The extension configuration has been created. Response contains the ID of the new configuration. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid |

### Response body objects

#### The `EntityShortRepresentation` object

The short representation of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the Dynatrace entity. |
| id | string | The ID of the Dynatrace entity. |
| name | string | The name of the Dynatrace entity. |

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



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



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
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/extensions/{id}/instances/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/extensions/{id}/instances/validator` |

### Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Response

#### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Validated. The submitted configuration is valid. Response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid |

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

## Related topics

* [Develop your own Extensions](/managed/ingest-from/extensions/develop-your-extensions "Develop your own Extensions in Dynatrace.")