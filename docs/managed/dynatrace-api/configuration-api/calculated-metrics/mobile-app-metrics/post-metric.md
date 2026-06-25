---
title: Mobile app metrics API - POST a metric
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/calculated-metrics/mobile-app-metrics/post-metric
scraped: 2026-05-12T11:17:33.916529
---

# Mobile app metrics API - POST a metric

# Mobile app metrics API - POST a metric

* Reference
* Published Apr 16, 2020

Creates a new calculated mobile app metric.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/mobile` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/mobile` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [CalculatedMobileMetric](#openapi-definition-CalculatedMobileMetric) | The JSON body of the request. Contains the definition of the new calculated metric for mobile or custom app. | body | Optional |

### Request body objects

#### The `CalculatedMobileMetric` object

Definition of the calculated metric for mobile or custom app.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| applicationIdentifier | string | The Dynatrace entity ID of the application to which the metric belongs. | Required |
| dimensions | [CalculatedMobileMetricDimension[]](#openapi-definition-CalculatedMobileMetricDimension) | A list of metric dimensions. | Optional |
| enabled | boolean | The metric is enabled (`true`) or disabled (`false`). | Required |
| metricKey | string | The unique key of the metric.  The key must have the `calc:apps` prefix. | Required |
| metricType | string | The type of the metric. The element can hold these values * `REPORTED_ERROR_COUNT` * `USER_ACTION_DURATION` * `WEB_REQUEST_COUNT` * `WEB_REQUEST_ERROR_COUNT` | Required |
| name | string | The name of the metric, displayed in the UI. | Required |
| userActionFilter | [CalculatedMobileMetricUserActionFilter](#openapi-definition-CalculatedMobileMetricUserActionFilter) | User actions filter of the calculated metric for mobile or custom app. | Optional |

#### The `CalculatedMobileMetricDimension` object

Dimension of the calculated mobile metric.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| dimension | string | The dimension of the metric. The element can hold these values * `APP_VERSION` * `DEVICE` * `ERROR_CONTEXT` * `GEOLOCATION` * `MANUFACTURER` * `OS` | Required |
| topX | integer | The number of top values to be calculated. | Required |

#### The `CalculatedMobileMetricUserActionFilter` object

User actions filter of the calculated metric for mobile or custom app.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| actionDurationFromMilliseconds | integer | Only actions with a duration more than or equal to this value (in milliseconds) are included in the metric calculation. | Optional |
| actionDurationToMilliseconds | integer | Only actions with a duration less than or equal to this value (in milliseconds) are included in the metric calculation. | Optional |
| apdex | string | Only actions with the specified Apdex score are included in the metric calculation. The element can hold these values * `Frustrated` * `Satisfied` * `Tolerating` * `Unknown` | Optional |
| appVersion | string | Only actions coming from this app version are included in the metric calculation.  The EQUALS operator applies. | Optional |
| carrier | string | Only actions coming from this carrier type are included in the metric calculation. | Optional |
| city | string | Only actions of users from this city are included in the metric calculation.  Specify geolocation ID here. | Optional |
| connectionType | string | Only actions coming from this connection type are included in the metric calculation. The element can hold these values * `LAN` * `MOBILE` * `OFFLINE` * `UNKNOWN` * `WIFI` | Optional |
| continent | string | Only actions of users from this continent are included in the metric calculation.  Specify geolocation ID here. | Optional |
| country | string | Only actions of users from this country are included in the metric calculation.  Specify geolocation ID here. | Optional |
| device | string | Only actions coming from this app version are included in the metric calculation.  The EQUALS operator applies. | Optional |
| hasHttpError | boolean | The HTTP error status of the actions to be included in the metric calculation:  * `true`: Only actions with HTTP errors are included. * `false`: All actions are included. | Optional |
| hasReportedError | boolean | The error status of the actions to be included in the metric calculation:  * `true`: Only actions with reported errors are included. * `false`: All actions are included. | Optional |
| isp | string | Only actions coming from this internet service provider are included in the metric calculation.  The EQUALS operator applies. | Optional |
| manufacturer | string | Only actions coming from devices of this manufacturer are included in the metric calculation.  The EQUALS operator applies. | Optional |
| networkTechnology | string | Filter by network technology | Optional |
| orientation | string | Only actions coming from devices with this display orientation are included in the metric calculation. The element can hold these values * `LANDSCAPE` * `PORTRAIT` * `UNKNOWN` | Optional |
| osFamily | string | Only actions coming from this OS family are included in the metric calculation.  Specify the OS ID here. | Optional |
| osVersion | string | Only actions coming from this OS version are included in the metric calculation.  Specify the OS ID here. | Optional |
| region | string | Only actions of users from this region are included in the metric calculation.  Specify geolocation ID here. | Optional |
| resolution | string | Only actions coming from devices with this display resolution are included in the metric calculation. The element can hold these values * `CGA` * `DCI2K` * `DCI4K` * `DVGA` * `FHD` * `FWVGA` * `FWXGA` * `GHDPlus` * `HD` * `HQVGA` * `HQVGA2` * `HSXGA` * `HUXGA` * `HVGA` * `HXGA` * `NTSC` * `PAL` * `QHD` * `QQVGA` * `QSXGA` * `QUXGA` * `QVGA` * `QWXGA` * `QXGA` * `SVGA` * `SXGA` * `SXGAMinus` * `SXGAPlus` * `UGA` * `UHD16K` * `UHD4K` * `UHD8K` * `UHDPlus` * `UNKNOWN` * `UWQHD` * `UXGA` * `VGA` * `WHSXGA` * `WHUXGA` * `WHXGA` * `WQSXGA` * `WQUXGA` * `WQVGA` * `WQVGA2` * `WQVGA3` * `WQXGA` * `WQXGA2` * `WSVGA` * `WSVGA2` * `WSXGA` * `WSXGAPlus` * `WUXGA` * `WVGA` * `WVGA2` * `WXGA` * `WXGA2` * `WXGA3` * `WXGAPlus` * `XGA` * `XGAPLUS` * `_1280x854` * `nHD` * `qHD` | Optional |
| userActionName | string | Only actions with this name are included in the metric calculation.  The EQUALS operator applies. | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"applicationIdentifier": "MOBILE_APPLICATION-1234",



"dimensions": [



{



"dimension": "GEOLOCATION",



"topX": 20



}



],



"enabled": true,



"metricKey": "calc:apps.mobile.mymetric",



"metricType": "USER_ACTION_DURATION",



"name": "MyMetric",



"userActionFilter": {



"country": "GEOLOCATION-1234",



"hasHttpError": true,



"osVersion": "OS-1234"



}



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Success. The calculated mobile metric has been created. Response contains its key and name. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid |

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

## Validate payload

We recommend that you validate the payload before submitting it with an actual request. A response code of **204** indicates a valid payload.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/mobile/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/mobile/validator` |

### Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Response

#### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Validated. The submitted metric is valid. The response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |

#### Response body objects

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

#### Response body JSON models

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

* [Create calculated metrics for mobile applications](/managed/observe/digital-experience/mobile-applications/additional-configuration/rum-calculated-metrics-mobile "Create calculated metrics as well as custom charts based on calculated metrics for your mobile applications.")
* [Create calculated metrics for custom applications](/managed/observe/digital-experience/custom-applications/additional-configuration/rum-calculated-metrics-custom "Create calculated metrics as well as custom charts based on calculated metrics for your custom applications.")