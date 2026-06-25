---
title: Plugins API - PUT an endpoint of a plugin
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/plugins-api/put-an-endpoint
scraped: 2026-05-12T11:21:00.315706
---

# Plugins API - PUT an endpoint of a plugin

# Plugins API - PUT an endpoint of a plugin

* Reference
* Published Jun 07, 2019

Updates properties of the specified endpoint of the ActiveGate plugin.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/plugins/{id}/endpoints/{endpointId}` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/plugins/{id}/endpoints/{endpointId}` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the plugin where you want to update an endpoint.  If you set the plugin ID in the body as well, it must match this ID. | path | Required |
| endpointId | string | The ID of the endpoint to be updated.  If you set the endpoint ID in the body as well, it must match this ID. | path | Required |
| body | [RemotePluginEndpoint](#openapi-definition-RemotePluginEndpoint) | The JSON body of the request. Contains updated parameters of the plugin endpoint. | body | Optional |

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
| **204** | - | Success. The endpoint has been updated. Response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |

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

In this example, the request updates the **RESTtest** endpoint of the SAP plugin which has the ID of **custom.remote.python.sap**. It makes the following changes to the endpoint:

* **name** to `RESTtest - updated`
* **serverIp** to `192.168.1.1`
* **activeGatePluginModule** to l-009 which has the ID of `6121289130553435111`

The API token is passed in the **Authorization** header.

You can download or copy the example request body to try it out on your own.

The original endpoint has the following parameters:

![Plugin endpoint - new](https://dt-cdn.net/images/plugin-endpoint-new-993-64cfba7a9e.png)

Plugin endpoint - new

#### Curl

```
curl -X PUT \



https://mySampleEnv.live.dynatrace.com/api/config/v1/plugins/custom.remote.python.sap/endpoints/8757307336635955682 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"name": "RESTtest - updated",



"enabled": false,



"properties": {



"clientno": "001",



"serverIp": "192.168.1.1",



"password": "",



"instance": "00",



"username": "DT"



},



"activeGatePluginModule": {



"id": "6121289130553435111"



}



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/plugins/custom.remote.python.sap/endpoints/8757307336635955682
```

#### Request body

```
{



"name": "RESTtest - updated",



"enabled": false,



"properties": {



"clientno": "001",



"serverIp": "192.168.1.1",



"password": "",



"instance": "00",



"username": "DT"



},



"activeGatePluginModule": {



"id": "6121289130553435111"



}



}
```

#### Response code

204

#### Result

The updated endpoint looks like this in the UI:

![Plugin endpoint - updated](https://dt-cdn.net/images/plugin-endpoint-upd-983-da2c6ef648.png)

Plugin endpoint - updated