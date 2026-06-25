---
title: Network zones API - PUT a network zone
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/network-zones/put-network-zone
scraped: 2026-05-12T11:52:21.058866
---

# Network zones API - PUT a network zone

# Network zones API - PUT a network zone

* Reference
* Published Apr 08, 2020

Updates the specified network zone. If the network zone with the specified ID doesn't exist, a new network zone is created.

The request produces and consumes an `application/json` payload.

|  |  |
| --- | --- |
| PUT | * Managed - Environment https://{your-environment-id}.live.dynatrace.com/api/v2/networkZones/{id} * Managed - Cluster Use the `PUT //networkZones/{id}` endpoint of the [Cluster API](/managed/dynatrace-api/cluster-api/cluster-api-v2 "Find out about managing environments, network zones, Synthetic locations, nodes, and tokens in Dynatrace Managed using the Cluster API v2."). |

## Authentication

To execute this request, you need the **Write network zones** (`networkZones.write`) permission assigned to your API token. To learn how to obtain and use it, see [Authentication](/managed/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the network zone to be updated.  If you set the ID in the body as well, it must match this ID.  The ID is not case sensitive. Dynatrace stores the ID in lowercase. | path | Required |
| body | [NetworkZone](#openapi-definition-NetworkZone) | The JSON body of the request. Contains parameters of the network zone. | body | Required |

### Request body objects

#### The `NetworkZone` object

Configuration of a network zone.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| alternativeZones | string[] | A list of alternative network zones. | Optional |
| description | string | A short description of the network zone. | Optional |
| fallbackMode | string | The fallback mode of the network zone. The element can hold these values * `ANY_ACTIVE_GATE` * `NONE` * `ONLY_DEFAULT_ZONE` | Optional |
| id | string | The ID of the network zone. | Optional |
| numOfConfiguredActiveGates | integer | The number of ActiveGates in the network zone. | Optional |
| numOfConfiguredOneAgents | integer | The number of OneAgents that are configured to use the network zone as primary. | Optional |
| numOfOneAgentsFromOtherZones | integer | The number of OneAgents from other network zones that are using ActiveGates in the network zone.  This is a fraction ofÂ **numOfOneAgentsUsing**.  One possible reason for switching to another zone is that a firewall is preventing a OneAgent from connecting to any ActiveGate in the preferred network zone. | Optional |
| numOfOneAgentsUsing | integer | The number of OneAgents that are using ActiveGates in the network zone. | Optional |
| overridesGlobal | boolean | Indicates if a global network zone is overridden (managed only). | Optional |
| scope | string | Specifies the scope of the network zone (managed only). | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
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
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Success. The new network zone has been created. The response body contains the ID of the new network zone. |
| **204** | - | Success. The network zone has been updated. Response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

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

## Related topics

* [Network zones](/managed/manage/network-zones "Find out how network zones work in Dynatrace.")