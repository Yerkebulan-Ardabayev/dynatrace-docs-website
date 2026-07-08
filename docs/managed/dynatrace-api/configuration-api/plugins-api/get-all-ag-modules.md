---
title: Plugins API - GET all ActiveGate plugin modules
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/plugins-api/get-all-ag-modules
---

# Plugins API - GET all ActiveGate plugin modules

# Plugins API - GET all ActiveGate plugin modules

* Reference
* Published Jun 07, 2019

Every ActiveGate plugin runs on a certain ActiveGate instance. The part of the ActiveGate code that runs plugins is called an *ActiveGate plugin module*.

This request lists all ActiveGate plugin modules available in your Dynatrace environment.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/plugins/activeGatePluginModules` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/plugins/activeGatePluginModules` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [StubList](#openapi-definition-StubList) | Success. The response contains IDs of ActiveGate plugin modules. Use them to configure plugin endpoints. |

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

In this example, the request lists all the ActiveGate plugin modules available in the **mySampleEnv** environment.

The API token is passed in the **Authorization** header.

The result is truncated to three entries.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/plugins/activeGatePluginModules \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/plugins/activeGatePluginModules
```

#### Response body

```
{



"values": [



{



"id": "1768386982494938781",



"name": "GDNDYNSYNVSG03"



},



{



"id": "6121289130553435111",



"name": "l-009"



},



{



"id": "-7614291897790148410",



"name": "GDNDYNSYNDEMODEVAG01"



}



]



}
```

#### Response code

200