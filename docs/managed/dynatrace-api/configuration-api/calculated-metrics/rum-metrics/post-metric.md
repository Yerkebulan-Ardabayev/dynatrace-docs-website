---
title: Web application metrics API - POST a metric
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/calculated-metrics/rum-metrics/post-metric
scraped: 2026-05-12T11:17:56.258346
---

# Web application metrics API - POST a metric

# Web application metrics API - POST a metric

* Reference
* Published Feb 28, 2020

Creates a new calculated web application metric.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/rum` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/rum` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [WebApplicationMetric](#openapi-definition-WebApplicationMetric) | The JSON body of the request. Contains the descriptor of the new calculated web application metric. | body | Required |

### Request body objects

#### The `WebApplicationMetric` object

Descriptor of the calculated web application metric.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| applicationIdentifier | string | The Dynatrace entity ID of the application to which the metric belongs. | Required |
| dimensions | [WebApplicationDimensionDefinition[]](#openapi-definition-WebApplicationDimensionDefinition) | A list of metric dimensions. | Optional |
| enabled | boolean | The metric is enabled (`true`) or disabled (`false`). | Required |
| metricDefinition | [WebApplicationMetricDefinition](#openapi-definition-WebApplicationMetricDefinition) | Definition of the web application metric. | Required |
| metricKey | string | The unique key of the metric.  The key must have the `calc:apps` prefix. | Required |
| name | string | The displayed name of the metric. | Required |
| userActionFilter | [UserActionFilter](#openapi-definition-UserActionFilter) | User actions filter of the calculated web application metric.  Only user actions matching the provided criteria are used for metric calculation.  A user action must match **all** the criteria. | Optional |

#### The `WebApplicationDimensionDefinition` object

Dimension of the calculated web application metrics.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| dimension | string | The dimension of the metric. The element can hold these values * `ApdexType` * `Browser` * `ErrorContext` * `ErrorOrigin` * `ErrorType` * `GeoLocation` * `StringProperty` * `UserActionType` | Required |
| propertyKey | string | The key of the user action property.  Only applicable for the `StringProperty` dimension. | Optional |
| topX | integer | The number of top values to be calculated. | Required |

#### The `WebApplicationMetricDefinition` object

Definition of the web application metric.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| metric | string | The type of the web application metric. The element can hold these values * `Apdex` * `ApplicationCache` * `Callback` * `CumulativeLayoutShift` * `DNSLookup` * `DOMComplete` * `DOMContentLoaded` * `DOMInteractive` * `DoubleProperty` * `ErrorCount` * `FirstContentfulPaint` * `FirstInputDelay` * `FirstInputStart` * `FirstPaint` * `HTMLDownloaded` * `LargestContentfulPaint` * `LoadEventEnd` * `LoadEventStart` * `LongProperty` * `LongTasksTime` * `NavigationStart` * `OnDOMContentLoaded` * `OnLoad` * `Processing` * `RedirectTime` * `Request` * `RequestStart` * `Response` * `SecureConnect` * `SpeedIndex` * `TCPConnect` * `TimeToFirstByte` * `UserActionDuration` * `VisuallyComplete` | Required |
| propertyKey | string | The key of the user action property.  Only applicable for `DoubleProperty` and `LongProperty` metrics. | Optional |

#### The `UserActionFilter` object

User actions filter of the calculated web application metric.

Only user actions matching the provided criteria are used for metric calculation.

A user action must match **all** the criteria.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| actionDurationFromMilliseconds | integer | Only actions with a duration more than or equal to this value (in milliseconds) are included in the metric calculation. | Optional |
| actionDurationToMilliseconds | integer | Only actions with a duration less than or equal to this value (in milliseconds) are included in the metric calculation. | Optional |
| apdex | string | Only actions with the specified Apdex score are included in the metric calculation. The element can hold these values * `Frustrated` * `Satisfied` * `Tolerating` * `Unknown` | Optional |
| browserFamily | string | Only user actions coming from the specified browser family are included in the metric calculation.  The EQUALS operator applies. | Optional |
| browserType | string | Only user actions coming from the specified browser type are included in the metric calculation.  The EQUALS operator applies. | Optional |
| browserVersion | string | Only user actions coming from the specified browser version are included in the metric calculation.  The EQUALS operator applies. | Optional |
| city | string | Only actions of users from this city are included in the metric calculation.  Specify geolocation ID here. | Optional |
| continent | string | Only actions of users from this continent are included in the metric calculation.  Specify geolocation ID here. | Optional |
| country | string | Only actions of users from this country are included in the metric calculation.  Specify geolocation ID here. | Optional |
| customAction | boolean | The status of custom actions in the metric calculation:  * `true`: Custom actions are included. * `false`: All actions are included. | Optional |
| customErrorName | string | The custom error name of the actions to be included in the metric calculation. | Optional |
| customErrorType | string | The custom error type of the actions to be included in the metric calculation. | Optional |
| domain | string | Only user actions coming from the specified domain are included in the metric calculation.  The EQUALS operator applies. | Optional |
| hasAnyError | boolean | The error status of the actions to be included in the metric calculation:  * `true`: Only actions that have any errors are included. * `false`: All actions are included. | Optional |
| hasCustomErrors | boolean | The custom error status of the actions to be included in the metric calculation:  * `true`: Only actions with custom errors are included. * `false`: All actions are included. | Optional |
| hasHttpErrors | boolean | The request error status of the actions to be included in the metric calculation:  * `true`: Only actions with request errors (HTTP errors, failed images, CSP rule violations) are included. * `false`: All actions are included. | Optional |
| hasJavascriptErrors | boolean | The JavaScript error status of the actions to be included in the metric calculation:  * `true`: Only actions with JavaScript errors are included. * `false`: All actions are included. | Optional |
| httpErrorCode | integer | The HTTP error status code of the actions to be included in the metric calculation. | Optional |
| httpErrorCodeTo | integer | Can be used in combination with `httpErrorCode` to define a range of error codes that will be included in the metric calculation. | Optional |
| httpPath | string | The request path that has been determined to be the origin of an HTTP error of the actions to be included in the metric calculation. | Optional |
| ip | string | Only actions coming from this IP address are included in the metric calculation.  The EQUALS operator applies. | Optional |
| ipV6Traffic | boolean | The IPv6 status of the actions to be included in the metric calculation:  * `true`: Only actions coming from IPv6 are included. * `false`: All actions are included. | Optional |
| loadAction | boolean | The status of load actions in the metric calculation:  * `true`: Load actions are included. * `false`: All actions are included. | Optional |
| osFamily | string | Only actions coming from this OS family are included in the metric calculation.  Specify the OS ID here. | Optional |
| osVersion | string | Only actions coming from this OS version are included in the metric calculation.  Specify the OS ID here. | Optional |
| realUser | boolean | The status of actions coming from real users in the metric calculation:  * `true`: Only actions from real users are included. * `false`: All actions are included. | Optional |
| region | string | Only actions of users from this region are included in the metric calculation.  Specify geolocation ID here. | Optional |
| robot | boolean | The status of actions coming from robots in the metric calculation:  * `true`: Only actions from robots are included. * `false`: All actions are included. | Optional |
| synthetic | boolean | The status of actions coming from synthetic monitors in the metric calculation:  * `true`: Only actions from synthetic monitors are included. * `false`: All actions are included. | Optional |
| targetViewGroup | string | Only actions on the specified group of views are included in the metric calculation. | Optional |
| targetViewGroupNameMatchType | string | Specifies the match type of the view group filter, e.g. using `Contains` or `Equals`. Defaults to `Equals`. The element can hold these values * `Contains` * `Equals` | Optional |
| targetViewName | string | Only actions on the specified view are included in the metric calculation. | Optional |
| targetViewNameMatchType | string | Specifies the match type of the view name filter, e.g. using `Contains` or `Equals`. Defaults to `Equals`. The element can hold these values * `Contains` * `Equals` | Optional |
| userActionName | string | Only actions with this name are included in the metric calculation.  The EQUALS operator applies. | Optional |
| userActionProperties | [UserActionPropertyFilter[]](#openapi-definition-UserActionPropertyFilter) | Only actions with the specified properties are included in the metric calculation. | Optional |
| xhrAction | boolean | The status of XHR actions in the metric calculation:  * `true`: XHR actions are included. * `false`: All actions are included. | Optional |
| xhrRouteChangeAction | boolean | The status of route change actions in the metric calculation:  * `true`: Route change actions are included. * `false`: All actions are included. | Optional |

#### The `UserActionPropertyFilter` object

User action property filter.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| from | number | Only actions that have a value greater than or equal to this are included in the metric calculation.  Only applicable to numerical values. | Optional |
| key | string | The key of the action property we're checking. | Optional |
| matchType | string | Specifies the match type of a string filter, e.g. using `Contains` or `Equals`.  Only applicable to string values. The element can hold these values * `Contains` * `Equals` | Optional |
| to | number | Only actions that have a value less than or equal to this are included in the metric calculation.  Only applicable to numerical values. | Optional |
| value | string | Only actions that have this value in the specified property are included in the metric calculation.  Only applicable to string values. | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"applicationIdentifier": "APPLICATION-1234",



"dimensions": [



{



"dimension": "GeoLocation",



"topX": 20



}



],



"enabled": true,



"metricDefinition": {



"metric": "UserActionDuration"



},



"metricKey": "calc:apps.web.mymetric",



"name": "MyMetric",



"userActionFilter": {



"browserType": "BROWSER-1234",



"country": "GEOLOCATION-1234",



"loadAction": true



}



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Success. The metric has been created. Response contains its key and name. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |

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
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/rum/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/rum/validator` |

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

* [Create calculated metrics for web applications](/managed/observe/digital-experience/web-applications/additional-configuration/rum-calculated-metrics-web "Create calculated metrics as well as custom charts based on calculated metrics for your web applications.")