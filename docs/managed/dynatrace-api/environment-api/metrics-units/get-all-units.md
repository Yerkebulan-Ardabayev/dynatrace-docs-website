---
title: "Metric units API - GET all units"
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/metrics-units/get-all-units
updated: 2026-02-09
---

# Metric units API - GET all units

# Metric units API - GET all units

* Reference
* Published Feb 11, 2022

Lists all available metric units of your environment.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/units` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/units` |

## Authentication

To execute this request, you need an access token with `metrics.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| unitSelector | string | Selects units to be included to the response. Available criteria:  * Compatibility: `compatibleTo("unit","display-format")`. Returns units that can be converted to the specified unit. The optional display format (`binary` or `decimal`) argument is supported by bit- and byte-based units and returns only units for the specified format. | query | Optional |
| fields | string | Defines the list of properties to be included in the response. The ID of the unit is **always** included. The following additional properties are available:  * `displayName`: The display name of the unit. * `symbol`: The symbol of the unit. * `description`: A short description of the unit.  By default, the ID, the display name, and the symbol are included.  To add properties, list them with leading plus `+`. To exclude default properties, list them with leading minus `-`.  To specify several properties, join them with a comma (for example `fields=+description,-symbol`).  If you specify just one property, the response contains the unitId and the specified property. To return unit IDs only, specify `unitId` here. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [UnitList](#openapi-definition-UnitList) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `UnitList` object

A list of units along with their properties.

| Element | Type | Description |
| --- | --- | --- |
| totalCount | integer | The total number of units in the result. |
| units | [Unit[]](#openapi-definition-Unit) | A list of units. |

#### The `Unit` object

The metadata of a unit.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the unit. |
| displayName | string | The display name of the unit. |
| displayNamePlural | string | The plural display name of the unit. |
| symbol | string | The symbol of the unit. |
| unitId | string | The ID of the unit. |

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



"totalCount": 2,



"units": [



{



"description": "byte per second",



"displayName": "byte per second",



"displayNamePlural": "bytes per second",



"symbol": "B/s",



"unitId": "BytePerSecond"



},



{



"description": "byte per minute",



"displayName": "byte per minute",



"displayNamePlural": "bytes per minute",



"symbol": "B/min",



"unitId": "BytePerMinute"



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

## Example

In this example, the request lists all metric units available for the **mySampleEnv** environment.

The API token is passed in the **Authorization** header.

The result is truncated to three entries.

#### Curl

```
curl --request GET \



--url https://mySampleEnv.live.dynatrace.com/api/v2/units \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/units
```

#### Response body

```
{



"totalCount": 3,



"activeGateTokens": [



{



"unitId": "Second",



"displayName": "second",



"symbol": "s"



},



{



"unitId": "GigaBit",



"displayName": "gigabit",



"symbol": "Gbit"



},



{



"unitId": "KiloBytePerSecond",



"displayName": "kilobyte per second",



"symbol": "kB/s"



}



]



}
```

#### Response code

200
