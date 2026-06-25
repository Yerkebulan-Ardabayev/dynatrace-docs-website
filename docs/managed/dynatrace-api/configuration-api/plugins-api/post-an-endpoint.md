---
title: Plugins API - POST a new plugin's endpoint
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/plugins-api/post-an-endpoint
scraped: 2026-05-12T11:21:07.509018
---

# Plugins API - POST a new plugin's endpoint

# Plugins API - POST a new plugin's endpoint

* Reference
* Published Jun 07, 2019

Creates a new endpoint for the specified ActiveGate plugin.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/plugins/{id}/endpoints` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/plugins/{id}/endpoints` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the plugin where you want to create an endpoint. | path | Required |
| body | [RemotePluginEndpoint](#openapi-definition-RemotePluginEndpoint) | The JSON body of the request. Contains parameters of the new plugin endpoint. | body | Optional |

### Request body objects

#### The `RemotePluginEndpoint` object

Configuration of a plugin endpoint.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| activeGatePluginModule | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | The short representation of a Dynatrace entity. | Required |
| enabled | boolean | The endpoint is enabled (`true`) or disabled (`false`). | Optional |
| id | string | The ID of the endpoint. | Optional |
| name | string | The name of the endpoint, displayed in Dynatrace. | Optional |
| pluginId | string | The ID of the plugin to which the endpoint belongs. | Optional |
| properties | object | The list of endpoint parameters.  Each parameter is a property-value pair. | Optional |

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



"activeGatePluginModule": {



"id": "-8844900174269363000"



},



"enabled": true,



"id": "-2183662974968812535",



"name": "Demo endpoint",



"pluginId": "custom.remote.python.demo",



"properties": {



"dropdownProperty": "two",



"password": "",



"serverIp": "127.0.0.1",



"username": "dynatrace"



}



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Success. The plugin endpoint has been created. Response contains the ID of the new endpoint. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |

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
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/plugins/{id}/endpoints/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/plugins/{id}/endpoints/validator` |

### Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Response

#### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Validated. The submitted configuration is valid. Response doesn't have a body. |
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

## Example

In this example, the request creates a new endpoint for the SAP plugin which has the ID of **custom.remote.python.sap**.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/config/v1/plugins/custom.remote.python.sap/endpoints \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"pluginId": "custom.remote.python.sap",



"name": "RESTtest",



"enabled": false,



"properties": {



"clientno": "001",



"serverIp": "127.0.0.1",



"password": "",



"instance": "00",



"username": "DT"



},



"activeGatePluginModule": {



"id": "1768386982494938781"



}



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/plugins/custom.remote.python.sap/endpoints
```

#### Request body

```
{



"pluginId": "custom.remote.python.sap",



"name": "RESTtest",



"enabled": false,



"properties": {



"clientno": "001",



"serverIp": "192.168.0.1",



"password": "",



"instance": "00",



"username": "DT"



},



"activeGatePluginModule": {



"id": "1768386982494938781"



}



}
```

#### Response body

```
{



"id": "8757307336635955682"



}
```

#### Response code

201

#### Result

The new endpoint looks like this in the UI:

![Plugin endpoint - new](https://dt-cdn.net/images/plugin-endpoint-new-993-64cfba7a9e.png)

Plugin endpoint - new