---
title: Network zones API - GET all network zones
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/network-zones/get-all
---

# Network zones API - GET all network zones

# Network zones API - GET all network zones

* Reference
* Published Mar 05, 2020

Lists all existing network zones.

The request produces an `application/json` payload.

|  |  |
| --- | --- |
| GET | * Managed - Environment https://{your-environment-id}.live.dynatrace.com/api/v2/networkZones * Managed - Cluster Use the `GET /networkZones` endpoint of the [Cluster API](/managed/dynatrace-api/cluster-api/cluster-api-v2 "Find out about managing environments, network zones, Synthetic locations, nodes, and tokens in Dynatrace Managed using the Cluster API v2."). |

## Authentication

To execute this request, you need the **Read network zones** (`networkZones.read`) permission assigned to your API token. To learn how to obtain and use it, see [Authentication](/managed/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [NetworkZoneList](#openapi-definition-NetworkZoneList) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `NetworkZoneList` object

A list of network zones.

| Element | Type | Description |
| --- | --- | --- |
| networkZones | [NetworkZone](#openapi-definition-NetworkZone)[] | A list of network zones. |

#### The `NetworkZone` object

Configuration of a network zone.

| Element | Type | Description |
| --- | --- | --- |
| alternativeZones | string[] | A list of alternative network zones. |
| description | string | A short description of the network zone. |
| fallbackMode | string | The fallback mode of the network zone. The element can hold these values * `ANY_ACTIVE_GATE` * `NONE` * `ONLY_DEFAULT_ZONE` |
| id | string | The ID of the network zone. |
| numOfConfiguredActiveGates | integer | The number of ActiveGates in the network zone. |
| numOfConfiguredOneAgents | integer | The number of OneAgents that are configured to use the network zone as primary. |
| numOfOneAgentsFromOtherZones | integer | The number of OneAgents from other network zones that are using ActiveGates in the network zone.  This is a fraction of **numOfOneAgentsUsing**.  One possible reason for switching to another zone is that a firewall is preventing a OneAgent from connecting to any ActiveGate in the preferred network zone. |
| numOfOneAgentsUsing | integer | The number of OneAgents that are using ActiveGates in the network zone. |
| overridesGlobal | boolean | Indicates if a global network zone is overridden (managed only). |
| scope | string | Specifies the scope of the network zone (managed only). |

#### The `ErrorEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

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

### Response body JSON models

```
{



"networkZones": [



{



"alternativeZones": [



"string"



],



"description": "string",



"fallbackMode": "ANY_ACTIVE_GATE",



"id": "string",



"numOfConfiguredActiveGates": 1,



"numOfConfiguredOneAgents": 1,



"numOfOneAgentsFromOtherZones": 1,



"numOfOneAgentsUsing": 1,



"overridesGlobal": true,



"scope": "string"



}



]



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

## Related topics

* [Network zones](/managed/manage/network-zones "Find out how network zones work in Dynatrace.")