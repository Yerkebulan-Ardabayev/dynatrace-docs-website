---
title: Plugins API - GET a plugin's endpoint
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/plugins-api/get-an-endpoint
scraped: 2026-05-12T11:20:55.857720
---

# Plugins API - GET a plugin's endpoint

# Plugins API - GET a plugin's endpoint

* Reference
* Published Jun 07, 2019

Lists properties of the specified endpoint of the ActiveGate plugin.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/plugins/{id}/endpoints/{endpointId}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/plugins/{id}/endpoints/{endpointId}` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the required plugin. | path | Required |
| endpointId | string | The ID of the required endpoint. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [RemotePluginEndpoint](#openapi-definition-RemotePluginEndpoint) | Success |

### Response body objects

#### The `RemotePluginEndpoint` object

Configuration of a plugin endpoint.

| Element | Type | Description |
| --- | --- | --- |
| activeGatePluginModule | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | The short representation of a Dynatrace entity. |
| enabled | boolean | The endpoint is enabled (`true`) or disabled (`false`). |
| id | string | The ID of the endpoint. |
| name | string | The name of the endpoint, displayed in Dynatrace. |
| pluginId | string | The ID of the plugin to which the endpoint belongs. |
| properties | object | The list of endpoint parameters.  Each parameter is a property-value pair. |

#### The `EntityShortRepresentation` object

The short representation of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the Dynatrace entity. |
| id | string | The ID of the Dynatrace entity. |
| name | string | The name of the Dynatrace entity. |

### Response body JSON models

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

## Example

In this example, the request inquires for the parameter of the **SAPacceptance** endpoint, which has the ID of **5677163660730843402**. The endpoint belongs to the SAP plugin that has the ID of **custom.remote.python.sap**.

The API token is passed in the **Authorization** header.

The endpoint has the following parameters:

![Plugin endpoint - expanded](https://dt-cdn.net/images/plugin-endpoint-992-b29bf1b9d1.png)

Plugin endpoint - expanded

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/plugins/custom.remote.python.sap/endpoints/5677163660730843402 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/plugins/custom.remote.python.sap/endpoints/5677163660730843402
```

#### Response body

```
{



"id": "5677163660730843402",



"pluginId": "custom.remote.python.sap",



"name": "SAPacceptance",



"enabled": true,



"properties": {



"clientno": "001",



"serverIp": "192.168.1.0",



"password": "",



"instance": "00",



"username": "DYNATRACE"



},



"activeGatePluginModule": {



"id": "1768386982494938781",



"name": "GDNDYNSYNVSG03"



}



}
```

#### Response code

200