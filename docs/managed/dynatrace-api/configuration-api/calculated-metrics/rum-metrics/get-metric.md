---
title: Web application metrics API - GET a metric
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/calculated-metrics/rum-metrics/get-metric
scraped: 2026-05-12T11:17:54.466478
---

# Web application metrics API - GET a metric

# Web application metrics API - GET a metric

* Reference
* Published Feb 28, 2020

Gets the descriptor of the specified calculated web application metric.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/rum/{metricKey}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/rum/{metricKey}` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| metricKey | string | The key of the required metric. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [WebApplicationMetric](#openapi-definition-WebApplicationMetric) | Success |

### Response body objects

#### The `WebApplicationMetric` object

Descriptor of the calculated web application metric.

| Element | Type | Description |
| --- | --- | --- |
| applicationIdentifier | string | The Dynatrace entity ID of the application to which the metric belongs. |
| dimensions | [WebApplicationDimensionDefinition[]](#openapi-definition-WebApplicationDimensionDefinition) | A list of metric dimensions. |
| enabled | boolean | The metric is enabled (`true`) or disabled (`false`). |
| metricDefinition | [WebApplicationMetricDefinition](#openapi-definition-WebApplicationMetricDefinition) | Definition of the web application metric. |
| metricKey | string | The unique key of the metric.  The key must have the `calc:apps` prefix. |
| name | string | The displayed name of the metric. |
| userActionFilter | [UserActionFilter](#openapi-definition-UserActionFilter) | User actions filter of the calculated web application metric.  Only user actions matching the provided criteria are used for metric calculation.  A user action must match **all** the criteria. |

#### The `WebApplicationDimensionDefinition` object

Dimension of the calculated web application metrics.

| Element | Type | Description |
| --- | --- | --- |
| dimension | string | The dimension of the metric. The element can hold these values * `ApdexType` * `Browser` * `ErrorContext` * `ErrorOrigin` * `ErrorType` * `GeoLocation` * `StringProperty` * `UserActionType` |
| propertyKey | string | The key of the user action property.  Only applicable for the `StringProperty` dimension. |
| topX | integer | The number of top values to be calculated. |

#### The `WebApplicationMetricDefinition` object

Definition of the web application metric.

| Element | Type | Description |
| --- | --- | --- |
| metric | string | The type of the web application metric. The element can hold these values * `Apdex` * `ApplicationCache` * `Callback` * `CumulativeLayoutShift` * `DNSLookup` * `DOMComplete` * `DOMContentLoaded` * `DOMInteractive` * `DoubleProperty` * `ErrorCount` * `FirstContentfulPaint` * `FirstInputDelay` * `FirstInputStart` * `FirstPaint` * `HTMLDownloaded` * `LargestContentfulPaint` * `LoadEventEnd` * `LoadEventStart` * `LongProperty` * `LongTasksTime` * `NavigationStart` * `OnDOMContentLoaded` * `OnLoad` * `Processing` * `RedirectTime` * `Request` * `RequestStart` * `Response` * `SecureConnect` * `SpeedIndex` * `TCPConnect` * `TimeToFirstByte` * `UserActionDuration` * `VisuallyComplete` |
| propertyKey | string | The key of the user action property.  Only applicable for `DoubleProperty` and `LongProperty` metrics. |

#### The `UserActionFilter` object

User actions filter of the calculated web application metric.

Only user actions matching the provided criteria are used for metric calculation.

A user action must match **all** the criteria.

| Element | Type | Description |
| --- | --- | --- |
| actionDurationFromMilliseconds | integer | Only actions with a duration more than or equal to this value (in milliseconds) are included in the metric calculation. |
| actionDurationToMilliseconds | integer | Only actions with a duration less than or equal to this value (in milliseconds) are included in the metric calculation. |
| apdex | string | Only actions with the specified Apdex score are included in the metric calculation. The element can hold these values * `Frustrated` * `Satisfied` * `Tolerating` * `Unknown` |
| browserFamily | string | Only user actions coming from the specified browser family are included in the metric calculation.  The EQUALS operator applies. |
| browserType | string | Only user actions coming from the specified browser type are included in the metric calculation.  The EQUALS operator applies. |
| browserVersion | string | Only user actions coming from the specified browser version are included in the metric calculation.  The EQUALS operator applies. |
| city | string | Only actions of users from this city are included in the metric calculation.  Specify geolocation ID here. |
| continent | string | Only actions of users from this continent are included in the metric calculation.  Specify geolocation ID here. |
| country | string | Only actions of users from this country are included in the metric calculation.  Specify geolocation ID here. |
| customAction | boolean | The status of custom actions in the metric calculation:  * `true`: Custom actions are included. * `false`: All actions are included. |
| customErrorName | string | The custom error name of the actions to be included in the metric calculation. |
| customErrorType | string | The custom error type of the actions to be included in the metric calculation. |
| domain | string | Only user actions coming from the specified domain are included in the metric calculation.  The EQUALS operator applies. |
| hasAnyError | boolean | The error status of the actions to be included in the metric calculation:  * `true`: Only actions that have any errors are included. * `false`: All actions are included. |
| hasCustomErrors | boolean | The custom error status of the actions to be included in the metric calculation:  * `true`: Only actions with custom errors are included. * `false`: All actions are included. |
| hasHttpErrors | boolean | The request error status of the actions to be included in the metric calculation:  * `true`: Only actions with request errors (HTTP errors, failed images, CSP rule violations) are included. * `false`: All actions are included. |
| hasJavascriptErrors | boolean | The JavaScript error status of the actions to be included in the metric calculation:  * `true`: Only actions with JavaScript errors are included. * `false`: All actions are included. |
| httpErrorCode | integer | The HTTP error status code of the actions to be included in the metric calculation. |
| httpErrorCodeTo | integer | Can be used in combination with `httpErrorCode` to define a range of error codes that will be included in the metric calculation. |
| httpPath | string | The request path that has been determined to be the origin of an HTTP error of the actions to be included in the metric calculation. |
| ip | string | Only actions coming from this IP address are included in the metric calculation.  The EQUALS operator applies. |
| ipV6Traffic | boolean | The IPv6 status of the actions to be included in the metric calculation:  * `true`: Only actions coming from IPv6 are included. * `false`: All actions are included. |
| loadAction | boolean | The status of load actions in the metric calculation:  * `true`: Load actions are included. * `false`: All actions are included. |
| osFamily | string | Only actions coming from this OS family are included in the metric calculation.  Specify the OS ID here. |
| osVersion | string | Only actions coming from this OS version are included in the metric calculation.  Specify the OS ID here. |
| realUser | boolean | The status of actions coming from real users in the metric calculation:  * `true`: Only actions from real users are included. * `false`: All actions are included. |
| region | string | Only actions of users from this region are included in the metric calculation.  Specify geolocation ID here. |
| robot | boolean | The status of actions coming from robots in the metric calculation:  * `true`: Only actions from robots are included. * `false`: All actions are included. |
| synthetic | boolean | The status of actions coming from synthetic monitors in the metric calculation:  * `true`: Only actions from synthetic monitors are included. * `false`: All actions are included. |
| targetViewGroup | string | Only actions on the specified group of views are included in the metric calculation. |
| targetViewGroupNameMatchType | string | Specifies the match type of the view group filter, e.g. using `Contains` or `Equals`. Defaults to `Equals`. The element can hold these values * `Contains` * `Equals` |
| targetViewName | string | Only actions on the specified view are included in the metric calculation. |
| targetViewNameMatchType | string | Specifies the match type of the view name filter, e.g. using `Contains` or `Equals`. Defaults to `Equals`. The element can hold these values * `Contains` * `Equals` |
| userActionName | string | Only actions with this name are included in the metric calculation.  The EQUALS operator applies. |
| userActionProperties | [UserActionPropertyFilter[]](#openapi-definition-UserActionPropertyFilter) | Only actions with the specified properties are included in the metric calculation. |
| xhrAction | boolean | The status of XHR actions in the metric calculation:  * `true`: XHR actions are included. * `false`: All actions are included. |
| xhrRouteChangeAction | boolean | The status of route change actions in the metric calculation:  * `true`: Route change actions are included. * `false`: All actions are included. |

#### The `UserActionPropertyFilter` object

User action property filter.

| Element | Type | Description |
| --- | --- | --- |
| from | number | Only actions that have a value greater than or equal to this are included in the metric calculation.  Only applicable to numerical values. |
| key | string | The key of the action property we're checking. |
| matchType | string | Specifies the match type of a string filter, e.g. using `Contains` or `Equals`.  Only applicable to string values. The element can hold these values * `Contains` * `Equals` |
| to | number | Only actions that have a value less than or equal to this are included in the metric calculation.  Only applicable to numerical values. |
| value | string | Only actions that have this value in the specified property are included in the metric calculation.  Only applicable to string values. |

### Response body JSON models

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

## Related topics

* [Create calculated metrics for web applications](/managed/observe/digital-experience/web-applications/additional-configuration/rum-calculated-metrics-web "Create calculated metrics as well as custom charts based on calculated metrics for your web applications.")