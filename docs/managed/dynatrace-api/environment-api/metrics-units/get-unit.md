---
title: "Metric units API - GET a unit"
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/metrics-units/get-unit
updated: 2026-02-09
---

# Metric units API - GET a unit

# Metric units API - GET a unit

* Reference
* Published Feb 11, 2022

Gets properties of a metric unit.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/units/{unitId}` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/units/{unitId}` |

## Authentication

To execute this request, you need an access token with `metrics.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| unitId | string | The ID of the required unit. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [Unit](#openapi-definition-Unit) | Success |
| **404** | - | Not found. The requested resource is not found or the query is incorrect. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `Unit` object

The metadata of a unit.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the unit. |
| displayName | string | The display name of the unit. |
| displayNamePlural | string | The plural display name of the unit. |
| symbol | string | The symbol of the unit. |
| unitId | string | The ID of the unit. |

### Response body JSON models

```
{



"description": "The second is the base unit of time and defined as 1/86400 of a day.",



"displayName": "second",



"displayNamePlural": "seconds",



"symbol": "s",



"unitId": "Second"



}
```

## Example

In this example, the request retrieves metadata of the **Ratio** unit.

The API token is passed in the **Authorization** header.

#### Curl

```
curl --request GET \



--url https://mySampleEnv.live.dynatrace.com//api/v2/units/MebiByte \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com//api/v2/units/MebiByte
```

#### Response body

```
{



"unitId": "MebiByte",



"displayName": "mebibyte",



"symbol": "MiB",



"description": "1048576.0 byte"



}
```

#### Response code

200
