---
title: Metric units API - GET convert units
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/metrics-units/get-unit-convert
scraped: 2026-02-27T21:25:31.673440
---

# Metric units API - GET convert units

# Metric units API - GET convert units

* Reference
* Published Mar 25, 2022

Converts a source unit into a target unit.

If no target unit is set, the request finds an appropriate target unit automatically, taking into account the preferred number format (if specified).

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/units/{unitId}/convert` |
| GET | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/units/{unitId}/convert` |

## Authentication

To execute this request, you need an access token with `metrics.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| unitId | string | The ID of the source unit. | path | Required |
| value | number | The value to be converted. | query | Required |
| targetUnit | string | The ID of the target unit.  If not set, the request finds an appropriate target unit automatically, based on the specified number format. | query | Optional |
| numberFormat | string | The preferred number format of the target value. You can specify the following formats:  * `binary` * `decimal`  `Only used if the target unit if not set. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [UnitConversionResult](#openapi-definition-UnitConversionResult) | Success |
| **404** | - | Not found. The requested resource is not found or the query is incorrect. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `UnitConversionResult` object

The result of a unit conversion.

| Element | Type | Description |
| --- | --- | --- |
| resultValue | number | The result of the unit conversion. |
| unitId | string | The ID of the unit of this conversion result. |

### Response body JSON models

```
{



"resultValue": 1,



"unitId": "string"



}
```