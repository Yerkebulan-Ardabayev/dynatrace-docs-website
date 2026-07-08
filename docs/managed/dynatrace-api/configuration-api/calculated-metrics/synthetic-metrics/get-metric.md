---
title: Synthetic metrics API - GET a metric
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/calculated-metrics/synthetic-metrics/get-metric
---

# Synthetic metrics API - GET a metric

# Synthetic metrics API - GET a metric

* Reference
* Published Apr 16, 2020

Gets the descriptor of the specified calculated synthetic metric.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/synthetic/{metricKey}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/synthetic/{metricKey}` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| metricKey | string | The key of the required calculated synthetic metric. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [CalculatedSyntheticMetric](#openapi-definition-CalculatedSyntheticMetric) | Success |

### Response body objects

#### The `CalculatedSyntheticMetric` object

Definition of the calculated synthetic metric.

| Element | Type | Description |
| --- | --- | --- |
| dimensions | [SyntheticMetricDimension](#openapi-definition-SyntheticMetricDimension)[] | A list of metric dimensions. |
| enabled | boolean | The metric is enabled (`true`) or disabled (`false`). |
| filter | [SyntheticMetricFilter](#openapi-definition-SyntheticMetricFilter) | Filter of the calculated synthetic metric. |
| metric | string | The type of the synthetic metric. The element can hold these values * `ApplicationCache` * `Callback` * `CumulativeLayoutShift` * `DNSLookup` * `DOMComplete` * `DOMContentLoaded` * `DOMInteractive` * `FailedRequestsResources` * `FirstContentfulPaint` * `FirstInputDelay` * `FirstInputStart` * `FirstPaint` * `HTMLDownloaded` * `HttpErrors` * `JavaScriptErrors` * `LargestContentfulPaint` * `LoadEventEnd` * `LoadEventStart` * `LongTasks` * `NavigationStart` * `OnDOMContentLoaded` * `OnLoad` * `Processing` * `RedirectTime` * `Request` * `RequestStart` * `ResourceCount` * `Response` * `SecureConnect` * `SpeedIndex` * `TCPConnect` * `TimeToFirstByte` * `TotalDuration` * `TransferSize` * `UserActionDuration` * `VisuallyComplete` |
| metricKey | string | The unique key of the metric.  The key must have the `calc:synthetic` prefix. |
| monitorIdentifier | string | The Dynatrace entity ID of the synthetic monitor to which the metric belongs. |
| name | string | The name of the metric, displayed in the UI. |

#### The `SyntheticMetricDimension` object

Dimension of the calculated synthetic metric.

| Element | Type | Description |
| --- | --- | --- |
| dimension | string | The dimension of the metric. The element can hold these values * `Event` * `Location` * `ResourceOrigin` |
| topX | integer | The number of top values to be calculated. |

#### The `SyntheticMetricFilter` object

Filter of the calculated synthetic metric.

| Element | Type | Description |
| --- | --- | --- |
| actionType | string | Only user actions of the specified type are included in the metric calculation. The element can hold these values * `Custom` * `Load` * `Xhr` |
| errorCode | integer | Only executions finished with the specified error code are included in the metric calculation. |
| event | string | Only the specified browser clickpath event is included in the metric calculation.  Specify the Dynatrace entity ID of the event here. You can fetch the list of clickpath events of the monitor with the [GET a synthetic monitor﻿](https://dt-url.net/4oe3kka) request from the Environment API |
| hasError | boolean | The execution status of the monitors to be included in the metric calculation:  * `true`: Only failed executions are included. * `false`: All executions are included. |
| location | string | Only executions from the specified location are included in the metric calculation.  Specify the Dynatrace entity ID of the location here. You can fetch the list of locations the monitor is running from with the [GET a synthetic monitor﻿](https://dt-url.net/4oe3kka) request from the Environment API. |

### Response body JSON models

```
{



"dimensions": [



{



"dimension": "Location"



}



],



"enabled": true,



"filter": {



"event": "SYNTHETIC_TEST_STEP-1234",



"hasError": true



},



"metric": "UserActionDuration",



"metricKey": "calc:synthetic.browser.mymetric",



"monitorIdentifier": "SYNTHETIC_TEST-1234",



"name": "MyMetric"



}
```

## Related topics

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.")