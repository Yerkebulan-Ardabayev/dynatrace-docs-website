---
title: Service-level objectives API - GET all SLOs
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/service-level-objectives-classic/get-all
---

# Service-level objectives API - GET all SLOs

# Service-level objectives API - GET all SLOs

* Reference
* Updated on Jan 07, 2025

Lists all service-level objectives and their calculated values.

By default the values are calculated for the SLO's own timeframe. You can use a custom timeframe:

1. Set the **timeFrame** parameter to `GTF`.
2. Provide the timeframe in **from** and **to** parameters.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/slo` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/slo` |

## Authentication

To execute this request, you need an access token with `slo.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| nextPageKey | string | The cursor for the next page of results. You can find it in the **nextPageKey** field of the previous response.  The first page is always returned if you don't specify the **nextPageKey** query parameter.  When the **nextPageKey** is set to obtain subsequent pages, you must omit all other query parameters. | query | Optional |
| pageSize | integer | The amount of SLOs in a single response payload.  The maximal allowed page size is 10000.  If not set, 10 is used. | query | Optional |
| from | string | The start of the requested timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the relative timeframe of two weeks is used (`now-2w`). | query | Optional |
| to | string | The end of the requested timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the current timestamp is used. | query | Optional |
| sloSelector | string | The scope of the query. Only SLOs matching the provided criteria are included in the response.  You can add one or several of the criteria listed below.  * SLO ID: `id("id-1","id-2")`. * Name: `name("name")`. Filters for an SLO with the given name. The filter is case-sensitive. * Health state: `healthState("HEALTHY")` or `healthState("UNHEALTHY")`. Filters for SLOs that have no related open problems (`HEALTHY`) or SLOs that have related open problems (`UNHEALTHY`). You can specify only one health state. * Text: `text("value")`. Filters for all SLOs that contain the given value in their name or description. The filter is case-insensitive. * Problem: `problemDisplayName("value")`. Filters for all SLOs that are related to a given problem display name (e.g. P-12345). * Management zone name: `managementZone("MZ-A")`. Filters for all SLOs that are related to the given management zone name. Returned SLOs are evaluated against the given management zone. * Management zone ID: `managementZoneID("123")`. Filters for all SLOs that are related to the given management zone ID. Returned SLOs are evaluated against the given management zone.  To set several criteria, separate them with comma (`,`). Only SLOs matching all criteria are included in the response. Examples:  * .../api/v2/slo?sloSelector=name("Service Availability") * .../api/v2/slo?sloSelector=id("id") * .../api/v2/slo?sloSelector=text("Description"),healthState("HEALTHY").  The special characters `~` and `"` need to be escaped using a `~` (e.g. double quote search `text("~"")`). | query | Optional |
| sort | string | The sorting of SLO entries:  * `name`: Names in ascending order. * `-name`: Names in descending order.  If not set, the ascending order is used. | query | Optional |
| timeFrame | string | The timeframe to calculate the SLO values:  * `CURRENT`: SLO's own timeframe. * `GTF`: timeframe specified by **from** and **to** parameters.  If not set, the `CURRENT` value is used. The element can hold these values * `CURRENT` * `GTF` | query | Optional |
| demo | boolean | Get your SLOs (`false`) or a set of demo SLOs (`true`). | query | Optional |
| evaluate | string | Get your SLOs without them being evaluated (`false`) or with evaluations (`true`) with maximum `pageSize` of 25. The element can hold these values * `true` * `false` | query | Optional |
| enabledSlos | string | Get your enabled SLOs (`true`), disabled ones (`false`) or both enabled and disabled ones (`all`). The element can hold these values * `true` * `false` * `all` | query | Optional |
| showGlobalSlos | boolean | Get your global SLOs (`true`) regardless of the selected filter or filter them out (`false`). | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [SLOs](#openapi-definition-SLOs) | Success. The response contains the parameters and calculated values of the requested SLO. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `SLOs` object

Contains SLOs and paging information.

| Element | Type | Description |
| --- | --- | --- |
| nextPageKey | string | The cursor for the next page of results. Has the value of `null` on the last page.  Use it in the **nextPageKey** query parameter to obtain subsequent pages of the result. |
| pageSize | integer | The number of entries per page. |
| slo | [SLO](#openapi-definition-SLO)[] | The list of SLOs. |
| totalCount | integer | The total number of entries in the result. |

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



"nextPageKey": "AQAAABQBAAAABQ==",



"pageSize": 1,



"slo": [



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



],



"totalCount": 1



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