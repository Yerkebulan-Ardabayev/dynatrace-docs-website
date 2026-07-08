---
title: Service-level objectives API - PUT an SLO
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/service-level-objectives-classic/put-slo
---

# Service-level objectives API - PUT an SLO

# Service-level objectives API - PUT an SLO

* Reference
* Published Sep 07, 2022

Updates service-level objective (SLO) parameters.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/slo/{id}` |
| PUT | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/slo/{id}` |

## Authentication

To execute this request, you need an access token with `slo.write` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the required SLO. | path | Required |
| body | [SloConfigItemDtoImpl](#openapi-definition-SloConfigItemDtoImpl) | The JSON body of the request. Contains the updated parameters of the SLO. | body | Required |

### Request body objects

#### The `SloConfigItemDtoImpl` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| description | string | The description of the SLO. | Optional |
| enabled | boolean | The SLO is enabled (`true`) or disabled (`false`).  If not defined, the SLO is disabled by default. | Optional |
| errorBudgetBurnRate | [SloBurnRateConfig](#openapi-definition-SloBurnRateConfig) | Error budget burn rate configuration of a service-level objective (SLO). | Optional |
| evaluationType | string | The evaluation type of the SLO. The element can hold these values * `AGGREGATE` | Required |
| filter | string | The entity filter for the SLO evaluation. The total length of the entitySelector string in SLOs is limited to 1,000 characters. Use the [syntax of entity selector﻿](https://dt-url.net/entityselector). | Optional |
| ~~metricDenominator~~ | string | DEPRECATED  The total count metric (the denominator in rate calculation).  Required when the **useRateMetric** is set to `false`. | Optional |
| metricExpression | string | The percentage-based metric expression for the calculation of the SLO. | Optional |
| metricName | string | The name that is used to create SLO func metrics keys. Once created, metric name cannot be changed. | Optional |
| ~~metricNumerator~~ | string | DEPRECATED  The metric for the count of successes (the numerator in rate calculation).  Required when the **useRateMetric** is set to `false`. | Optional |
| ~~metricRate~~ | string | DEPRECATED  The percentage-based metric for the calculation of the SLO.  Required when the **useRateMetric** is set to `true`. | Optional |
| name | string | The name of the SLO. | Required |
| target | number | The target value of the SLO. | Required |
| timeframe | string | The timeframe for the SLO evaluation. Use the syntax of the global timeframe selector. | Required |
| ~~useRateMetric~~ | boolean | DEPRECATED  The type of the metric to use for SLO calculation:  * `true`: An existing percentage-based metric. * `false`: A ratio of two metrics.  For a list of available metrics, see [Built-in metric page﻿](https://dt-url.net/be03kow) or try the [GET metrics﻿](https://dt-url.net/8e43kxf) API call. | Optional |
| warning | number | The warning value of the SLO.  At warning state the SLO is still fulfilled but is getting close to failure. | Required |

#### The `SloBurnRateConfig` object

Error budget burn rate configuration of a service-level objective (SLO).

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| burnRateVisualizationEnabled | boolean | The error budget burn rate calculation is enabled (`true`) or disabled (`false`).  In case of `false`, no calculated values will be present here.  If not defined, the error budget burn rate calculation is disabled by default. | Optional |
| fastBurnThreshold | number | The threshold between a slow and a fast burn rate. | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"description": "Rate of successful payments per week",



"enabled": true,



"errorBudgetBurnRate": {



"burnRateVisualizationEnabled": true,



"fastBurnThreshold": 1.5



},



"evaluationType": "AGGREGATE",



"filter": "type(\"SERVICE\")",



"metricDenominator": "builtin:service.requestCount.server",



"metricExpression": "(100)*(builtin:service.errors.server.successCount:splitBy())/(builtin:service.requestCount.server:splitBy())",



"metricName": "payment_service_availability",



"metricNumerator": "builtin:service.errors.server.successCount",



"metricRate": "builtin:service.successes.server.rate",



"name": "Payment service availability",



"target": 95,



"timeframe": "-1d",



"useRateMetric": true,



"warning": 97.5



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | - | Success |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **404** | - | Failed. The requested resource doesn't exist. |
| **500** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Internal server error. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

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

* [Service-Level Objectives](/managed/deliver/service-level-objectives-classic "Monitor and alert on service-level objectives with Dynatrace in Service-Level Objectives Classic.")