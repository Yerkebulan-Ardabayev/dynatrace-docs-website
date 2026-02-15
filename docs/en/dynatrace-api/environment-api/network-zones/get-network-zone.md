---
title: Network zones API - GET a network zone
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/network-zones/get-network-zone
scraped: 2026-02-15T21:19:37.945357
---

# Network zones API - GET a network zone

# Network zones API - GET a network zone

* Reference
* Published Mar 05, 2020

Gets information about the specified network zone.

The request produces an `application/json` payload.

GET

* SaaS https://{your-environment-id}.live.dynatrace.com/api/v2/networkZones/{id}

## Authentication

To execute this request, you need the **Read network zones** (`networkZones.read`) permission assigned to your API token. To learn how to obtain and use it, see [Authentication](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the required network zone. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [NetworkZone](#openapi-definition-NetworkZone) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

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
| numOfOneAgentsFromOtherZones | integer | The number of OneAgents from other network zones that are using ActiveGates in the network zone.  This is a fraction ofÂ **numOfOneAgentsUsing**.  One possible reason for switching to another zone is that a firewall is preventing a OneAgent from connecting to any ActiveGate in the preferred network zone. |
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

* [Network zones](/docs/manage/network-zones "Find out how network zones work in Dynatrace.")