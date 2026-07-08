---
title: Plugins API - GET all plugins
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/plugins-api/get-all-plugins
---

# Plugins API - GET all plugins

# Plugins API - GET all plugins

* Reference
* Published Jun 07, 2019

Lists all plugins uploaded to your Dynatrace environment.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/plugins` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/plugins` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [StubList](#openapi-definition-StubList) | Success |

### Response body objects

#### The `StubList` object

An ordered list of short representations of Dynatrace entities.

| Element | Type | Description |
| --- | --- | --- |
| values | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation)[] | An ordered list of short representations of Dynatrace entities. |

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



"values": [



{



"description": "Dynatrace entity 1 for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity 1"



},



{



"id": "ee70f7d3-9a4e-4f5f-94d2-c9d6156f1618",



"name": "Dynatrace entity 2"



},



{



"id": "8cdabe77-9e1a-4be8-b3df-269dd6fa9d7f"



}



]



}
```

## Example

In this example, the request lists all the plugins uploaded to the **mySampleEnv** environment.

The API token is passed in the **Authorization** header.

The result is truncated to four entries. The request lists these plugins:

![Plugins - list](https://dt-cdn.net/images/plugin-list-2-1200-a346e1c0be.png)

Plugins - list

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/plugins \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/plugins
```

#### Response body

```
{



"values": [



{



"id": "custom.remote.python.sap",



"name": "SAP plugin",



"description": "ActiveGate plugin"



},



{



"id": "custom.remote.python.simple_math",



"name": "MathPlugin",



"description": "ActiveGate plugin"



},



{



"id": "custom.python.wavebuoyplugin",



"name": "WaveBuoy Plugin",



"description": "OneAgent plugin"



},



{



"id": "custom.jmx.creatorCreatedPlugin1506519805362",



"name": "Jetty2",



"description": "JMX plugin"



}



]



}
```

#### Response code

200