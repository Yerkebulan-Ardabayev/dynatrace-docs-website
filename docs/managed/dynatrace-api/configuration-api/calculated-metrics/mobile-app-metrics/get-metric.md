---
title: Mobile app metrics API - GET a metric
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/calculated-metrics/mobile-app-metrics/get-metric
---

# Mobile app metrics API - GET a metric

# Mobile app metrics API - GET a metric

* Reference
* Published Apr 16, 2020

Gets the descriptor of the specified calculated mobile app metric.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/mobile/{metricKey}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/mobile/{metricKey}` |

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
| **200** | [CalculatedMobileMetric](#openapi-definition-CalculatedMobileMetric) | Success |

### Response body objects

#### The `CalculatedMobileMetric` object

Definition of the calculated metric for mobile or custom app.

| Element | Type | Description |
| --- | --- | --- |
| applicationIdentifier | string | The Dynatrace entity ID of the application to which the metric belongs. |
| dimensions | [CalculatedMobileMetricDimension](#openapi-definition-CalculatedMobileMetricDimension)[] | A list of metric dimensions. |
| enabled | boolean | The metric is enabled (`true`) or disabled (`false`). |
| metricKey | string | The unique key of the metric.  The key must have the `calc:apps` prefix. |
| metricType | string | The type of the metric. The element can hold these values * `REPORTED_ERROR_COUNT` * `USER_ACTION_DURATION` * `WEB_REQUEST_COUNT` * `WEB_REQUEST_ERROR_COUNT` |
| name | string | The name of the metric, displayed in the UI. |
| userActionFilter | [CalculatedMobileMetricUserActionFilter](#openapi-definition-CalculatedMobileMetricUserActionFilter) | User actions filter of the calculated metric for mobile or custom app. |

#### The `CalculatedMobileMetricDimension` object

Dimension of the calculated mobile metric.

| Element | Type | Description |
| --- | --- | --- |
| dimension | string | The dimension of the metric. The element can hold these values * `APP_VERSION` * `DEVICE` * `ERROR_CONTEXT` * `GEOLOCATION` * `MANUFACTURER` * `OS` |
| topX | integer | The number of top values to be calculated. |

#### The `CalculatedMobileMetricUserActionFilter` object

User actions filter of the calculated metric for mobile or custom app.

| Element | Type | Description |
| --- | --- | --- |
| actionDurationFromMilliseconds | integer | Only actions with a duration more than or equal to this value (in milliseconds) are included in the metric calculation. |
| actionDurationToMilliseconds | integer | Only actions with a duration less than or equal to this value (in milliseconds) are included in the metric calculation. |
| apdex | string | Only actions with the specified Apdex score are included in the metric calculation. The element can hold these values * `Frustrated` * `Satisfied` * `Tolerating` * `Unknown` |
| appVersion | string | Only actions coming from this app version are included in the metric calculation.  The EQUALS operator applies. |
| carrier | string | Only actions coming from this carrier type are included in the metric calculation. |
| city | string | Only actions of users from this city are included in the metric calculation.  Specify geolocation ID here. |
| connectionType | string | Only actions coming from this connection type are included in the metric calculation. The element can hold these values * `LAN` * `MOBILE` * `OFFLINE` * `UNKNOWN` * `WIFI` |
| continent | string | Only actions of users from this continent are included in the metric calculation.  Specify geolocation ID here. |
| country | string | Only actions of users from this country are included in the metric calculation.  Specify geolocation ID here. |
| device | string | Only actions coming from this app version are included in the metric calculation.  The EQUALS operator applies. |
| hasHttpError | boolean | The HTTP error status of the actions to be included in the metric calculation:  * `true`: Only actions with HTTP errors are included. * `false`: All actions are included. |
| hasReportedError | boolean | The error status of the actions to be included in the metric calculation:  * `true`: Only actions with reported errors are included. * `false`: All actions are included. |
| isp | string | Only actions coming from this internet service provider are included in the metric calculation.  The EQUALS operator applies. |
| manufacturer | string | Only actions coming from devices of this manufacturer are included in the metric calculation.  The EQUALS operator applies. |
| networkTechnology | string | Filter by network technology |
| orientation | string | Only actions coming from devices with this display orientation are included in the metric calculation. The element can hold these values * `LANDSCAPE` * `PORTRAIT` * `UNKNOWN` |
| osFamily | string | Only actions coming from this OS family are included in the metric calculation.  Specify the OS ID here. |
| osVersion | string | Only actions coming from this OS version are included in the metric calculation.  Specify the OS ID here. |
| region | string | Only actions of users from this region are included in the metric calculation.  Specify geolocation ID here. |
| resolution | string | Only actions coming from devices with this display resolution are included in the metric calculation. The element can hold these values * `CGA` * `DCI2K` * `DCI4K` * `DVGA` * `FHD` * `FWVGA` * `FWXGA` * `GHDPlus` * `HD` * `HQVGA` * `HQVGA2` * `HSXGA` * `HUXGA` * `HVGA` * `HXGA` * `NTSC` * `PAL` * `QHD` * `QQVGA` * `QSXGA` * `QUXGA` * `QVGA` * `QWXGA` * `QXGA` * `SVGA` * `SXGA` * `SXGAMinus` * `SXGAPlus` * `UGA` * `UHD16K` * `UHD4K` * `UHD8K` * `UHDPlus` * `UNKNOWN` * `UWQHD` * `UXGA` * `VGA` * `WHSXGA` * `WHUXGA` * `WHXGA` * `WQSXGA` * `WQUXGA` * `WQVGA` * `WQVGA2` * `WQVGA3` * `WQXGA` * `WQXGA2` * `WSVGA` * `WSVGA2` * `WSXGA` * `WSXGAPlus` * `WUXGA` * `WVGA` * `WVGA2` * `WXGA` * `WXGA2` * `WXGA3` * `WXGAPlus` * `XGA` * `XGAPLUS` * `_1280x854` * `nHD` * `qHD` |
| userActionName | string | Only actions with this name are included in the metric calculation.  The EQUALS operator applies. |

### Response body JSON models

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

## Related topics

* [Create calculated metrics for mobile applications in RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/rum-calculated-metrics-mobile "Create calculated metrics as well as custom charts based on calculated metrics for your mobile applications.")
* [Create calculated metrics for custom applications in RUM Classic](/managed/observe/digital-experience/rum-classic/custom-applications/additional-configuration/rum-calculated-metrics-custom "Create calculated metrics as well as custom charts based on calculated metrics for your custom applications.")