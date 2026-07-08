---
title: Service-level Objectives API - GET an SLO
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/service-level-objectives-classic/get-slo
---

# Service-level Objectives API - GET an SLO

# Service-level Objectives API - GET an SLO

* Reference
* Updated on Jan 07, 2025

Gets the parameter of the specified service-level objective (SLO) classic.

If **from** and **to** parameters are provided, the SLO is calculated for that timeframe; otherwise the SLO's own timeframe is used.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/slo/{id}` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/slo/{id}` |

## Authentication

To execute this request, you need an access token with `slo.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| from | string | The start of the requested timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the relative timeframe of two weeks is used (`now-2w`). | query | Optional |
| to | string | The end of the requested timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the current timestamp is used. | query | Optional |
| id | string | The ID of the required SLO. | path | Required |
| timeFrame | string | The timeframe to calculate the SLO values:  * `CURRENT`: SLO's own timeframe. * `GTF`: timeframe specified by **from** and **to** parameters.  If not set, the `CURRENT` value is used. The element can hold these values * `CURRENT` * `GTF` | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [SLO](#openapi-definition-SLO) | Success. The response contains the parameters and calculated values of the requested SLO. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The requested resource doesn't exist. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `SLO` object

Parameters of a service-level objective (SLO).

| Element | Type | Description |
| --- | --- | --- |
| burnRateMetricKey | string | The key for the SLO's error budget burn rate func metric. |
| ~~denominatorValue~~ | number | DEPRECATED  The denominator value used to evaluate the SLO when **useRateMetric** is set to `false`. |
| description | string | A short description of the SLO. |
| enabled | boolean | The SLO is enabled (`true`) or disabled (`false`). |
| error | string | The error of the SLO calculation.  If the value differs from `NONE`, there is something wrong with the SLO calculation. |
| errorBudget | number | The error budget of the calculated SLO.  The error budget is the difference between the calculated and target values. A positive number means all is good; a negative number means trouble.  Has the value of the evaluated error budget or the value of `-1`:  * If there is an error with the SLO calculation; in that case check the value of the **error** property. * If the evaluate parameter has not been set to `true`; in that case the **error** property will contain no error. |
| errorBudgetBurnRate | [SloBurnRate](#openapi-definition-SloBurnRate) | Error budget burn rate evaluation of a service-level objective (SLO). |
| errorBudgetMetricKey | string | The key for the SLO's error budget func metric. |
| evaluatedPercentage | number | The calculated status value of the SLO. Has the value of the evaluated SLO status or the value of `-1`:  * If there is an error with the SLO calculation; in that case check the value of the **error** property. * If the evaluate parameter has not been set to `true`; in that case the **error** property will contain no error. |
| evaluationType | string | The evaluation type of the SLO. The element can hold these values * `AGGREGATE` |
| filter | string | The entity filter for the SLO evaluation. The total length of the entitySelector string in SLOs is limited to 1,000 characters. Use the [syntax of entity selector﻿](https://dt-url.net/entityselector). |
| id | string | The ID of the SLO |
| ~~metricDenominator~~ | string | DEPRECATED  The total count metric (the denominator in rate calculation).  Required when the **useRateMetric** is set to `false`. |
| metricExpression | string | The percentage-based metric expression for the calculation of the SLO. |
| metricKey | string | The key for the SLO's status func metric. |
| metricName | string | The name that is used to create SLO func metrics keys. Once created, metric name cannot be changed. |
| ~~metricNumerator~~ | string | DEPRECATED  The metric for the count of successes (the numerator in rate calculation).  Required when the **useRateMetric** is set to `false`. |
| ~~metricRate~~ | string | DEPRECATED  The percentage-based metric for the calculation of the SLO.  Required when the **useRateMetric** is set to `true`. |
| name | string | The name of the SLO. |
| normalizedErrorBudgetMetricKey | string | The key for the SLO's normalized error budget func metric. |
| ~~numeratorValue~~ | number | DEPRECATED  The numerator value used to evaluate the SLO when **useRateMetric** is set to `false`. |
| ~~problemFilters~~ | string[] | DEPRECATED  The entity filter for fetching the number of problems related to an SLO. Auto-generated in case no filter has been added to the SLO. |
| relatedOpenProblems | integer | Number of open problems related to the SLO.  Has the value of `-1` if there's an error with fetching SLO related problems. |
| relatedTotalProblems | integer | Total number of problems related to the SLO.  Has the value of `-1` if there's an error with fetching SLO related problems. |
| status | string | The status of the calculated SLO. The element can hold these values * `FAILURE` * `SUCCESS` * `WARNING` |
| target | number | The target value of the SLO. |
| timeframe | string | The timeframe for the SLO evaluation. Use the syntax of the global timeframe selector. |
| ~~useRateMetric~~ | boolean | DEPRECATED  The type of the metric to use for SLO calculation:  * `true`: An existing percentage-based metric. * `false`: A ratio of two metrics.  For a list of available metrics, see [Built-in metric page﻿](https://dt-url.net/be03kow) or try the [GET metrics﻿](https://dt-url.net/8e43kxf) API call. |
| warning | number | The warning value of the SLO.  At warning state the SLO is still fulfilled but is getting close to failure. |

#### The `SloBurnRate` object

Error budget burn rate evaluation of a service-level objective (SLO).

| Element | Type | Description |
| --- | --- | --- |
| burnRateType | string | The calculated burn rate type.  Has a value of 'FAST', 'SLOW' or 'NONE'. The element can hold these values * `FAST` * `NONE` * `SLOW` |
| burnRateValue | number | The burn rate of the SLO, calculated for the last hour. |
| burnRateVisualizationEnabled | boolean | The error budget burn rate calculation is enabled (`true`) or disabled (`false`).  In case of `false`, no calculated values will be present here. |
| estimatedTimeToConsumeErrorBudget | number | The estimated time left to consume the error budget in hours. |
| fastBurnThreshold | number | The threshold between a slow and a fast burn rate. |
| sloValue | number | The calculated value of the SLO for the timeframe chosen for the burn rate calculation. |

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



"burnRateMetricKey": "func:slo.errorBudgetBurnRate.payment_service_availability",



"denominatorValue": 90,



"description": "Rate of successful payments per week",



"enabled": true,



"error": "NONE",



"errorBudget": 1.25,



"errorBudgetBurnRate": {



"burnRateType": "SLOW",



"burnRateValue": 1.25,



"burnRateVisualizationEnabled": true,



"estimatedTimeToConsumeErrorBudget": 24,



"fastBurnThreshold": 1.5,



"sloValue": 95



},



"errorBudgetMetricKey": "func:slo.errorBudget.payment_service_availability",



"evaluatedPercentage": 96.25,



"evaluationType": "AGGREGATE",



"filter": "type(\"SERVICE\")",



"id": "123e4567-e89b-42d3-a456-556642440000",



"metricDenominator": "builtin:service.requestCount.server",



"metricExpression": "(100)*(builtin:service.errors.server.successCount:splitBy())/(builtin:service.requestCount.server:splitBy())",



"metricKey": "func:slo.payment_service_availability",



"metricName": "payment_service_availability",



"metricNumerator": "builtin:service.errors.server.successCount",



"metricRate": "builtin:service.successes.server.rate",



"name": "Payment service availability",



"normalizedErrorBudgetMetricKey": "func:slo.normalizedErrorBudget.payment_service_availability",



"numeratorValue": 80,



"problemFilters": "[type(\"SERVICE\")]",



"relatedOpenProblems": 1,



"relatedTotalProblems": 1,



"status": "WARNING",



"target": 95,



"timeframe": "-1d",



"useRateMetric": true,



"warning": 97.5



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

* [Service-Level Objectives](/managed/deliver/service-level-objectives-classic "Monitor and alert on service-level objectives with Dynatrace in Service-Level Objectives Classic.")