---
title: Synthetic monitors API - GET a monitor
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic/synthetic-monitors/get-a-monitor
---

# Synthetic monitors API - GET a monitor

# Synthetic monitors API - GET a monitor

* Reference
* Published Jul 25, 2019

Gets the properties of the specified monitor, including its JSON script.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/synthetic/monitors/{monitorId}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/synthetic/monitors/{monitorId}` |

## Authentication

To execute this request, you need an access token with one of the following scopes:

* `ExternalSyntheticIntegration`
* `ReadSyntheticData`

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| monitorId | string | The ID of the required synthetic monitor | path | Required |

## Response

To find all model variations that depend on the type of the model, see [JSON models](/managed/dynatrace-api/environment-api/synthetic/synthetic-monitors/models "Learn the variations of models in the Synthetic monitors v1 API.").

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [SyntheticMonitor](#openapi-definition-SyntheticMonitor) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `SyntheticMonitor` object

The synthetic monitor.

The actual set of fields depends the type of the monitor. Find the list of actual objects in the description of the **type** field or see [Synthetic monitors API - JSON models﻿](https://dt-url.net/2523se9).

| Element | Type | Description |
| --- | --- | --- |
| anomalyDetection | [AnomalyDetection](#openapi-definition-AnomalyDetection) | The anomaly detection configuration. |
| automaticallyAssignedApps | string[] | A set of automatically assigned applications. |
| createdFrom | string | The origin of a monitor The element can hold these values * `API` * `GUI` |
| enabled | boolean | The monitor is enabled (`true`) or disabled (`false`). |
| entityId | string | The entity ID of the monitor. |
| frequencyMin | integer | The frequency of the monitor, in minutes.  You can use one of the following values: `5`, `10`, `15`, `30`, and `60`. |
| locations | string[] | A list of locations from which the monitor is executed.  To specify a location, use its entity ID. For public locations in `GEOLOCATION-9999453BE4BDB3CD` form and `SYNTHETIC_LOCATION-DF80ACFB688C583B` for private ones. |
| managementZones | [ManagementZone](#openapi-definition-ManagementZone)[] | A set of management zones to which the monitor belongs to. |
| manuallyAssignedApps | string[] | A set of manually assigned applications. |
| name | string | The name of the monitor. |
| script | object | The script of a [browser﻿](https://dt-url.net/9c103rda) or HTTP monitor. |
| tags | [TagWithSourceInfo](#openapi-definition-TagWithSourceInfo)[] | A set of tags assigned to the monitor. |
| type | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `BROWSER` -> BrowserSyntheticMonitor * `HTTP` -> HttpSyntheticMonitor The element can hold these values * `BROWSER` * `HTTP` |

#### The `AnomalyDetection` object

The anomaly detection configuration.

| Element | Type | Description |
| --- | --- | --- |
| loadingTimeThresholds | [LoadingTimeThresholdsPolicyDto](#openapi-definition-LoadingTimeThresholdsPolicyDto) | Performance thresholds configuration. |
| outageHandling | [OutageHandlingPolicy](#openapi-definition-OutageHandlingPolicy) | Outage handling configuration. |

#### The `LoadingTimeThresholdsPolicyDto` object

Performance thresholds configuration.

| Element | Type | Description |
| --- | --- | --- |
| enabled | boolean | Performance threshold is enabled (`true`) or disabled (`false`). |
| thresholds | [LoadingTimeThreshold](#openapi-definition-LoadingTimeThreshold)[] | The list of performance threshold rules. |

#### The `LoadingTimeThreshold` object

The performance threshold rule.

| Element | Type | Description |
| --- | --- | --- |
| eventIndex | integer | Specify the event to which an ACTION threshold applies. |
| requestIndex | integer | Specify the request to which an ACTION threshold applies. |
| type | string | The type of the threshold: total loading time or action loading time. The element can hold these values * `ACTION` * `TOTAL` |
| valueMs | integer | Notify if monitor takes longer than *X* milliseconds to load. |

#### The `OutageHandlingPolicy` object

Outage handling configuration.

| Element | Type | Description |
| --- | --- | --- |
| globalOutage | boolean | When enabled (`true`), generate a problem and send an alert when the monitor is unavailable at all configured locations. |
| globalOutagePolicy | [GlobalOutagePolicy](#openapi-definition-GlobalOutagePolicy) | Global outage handling configuration. |
| localOutage | boolean | When enabled (`true`), generate a problem and send an alert when the monitor is unavailable for one or more consecutive runs at any location. |
| localOutagePolicy | [LocalOutagePolicy](#openapi-definition-LocalOutagePolicy) | Local outage handling configuration.  Alert if **affectedLocations** of locations are unable to access the web application **consecutiveRuns** times consecutively. |
| retryOnError | boolean | Schedule retry if browser monitor execution results in a fail. For HTTP monitors this property is ignored. |

#### The `GlobalOutagePolicy` object

Global outage handling configuration.

| Element | Type | Description |
| --- | --- | --- |
| consecutiveRuns | integer | Alert if all locations are unable to access the web application *X* times consecutively. |

#### The `LocalOutagePolicy` object

Local outage handling configuration.

Alert if **affectedLocations** of locations are unable to access the web application **consecutiveRuns** times consecutively.

| Element | Type | Description |
| --- | --- | --- |
| affectedLocations | integer | The number of affected locations to trigger an alert. |
| consecutiveRuns | integer | The number of consecutive fails to trigger an alert. |

#### The `ManagementZone` object

The configuration of a management zone.

| Element | Type | Description |
| --- | --- | --- |
| id | string | The ID of the management zone. |
| name | string | The name of the management zone. |

#### The `TagWithSourceInfo` object

Tag with source of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| context | string | The origin of the tag, such as AWS or Cloud Foundry.  Custom tags use the `CONTEXTLESS` value. The element can hold these values * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | The key of the tag.  Custom tags have the tag value here. |
| source | string | The source of the tag, such as USER, RULE\_BASED or AUTO The element can hold these values * `AUTO` * `RULE_BASED` * `USER` |
| value | string | The value of the tag.  Not applicable to custom tags. |

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



"anomalyDetection": {



"loadingTimeThresholds": {



"enabled": true,



"thresholds": [



{



"eventIndex": 1,



"requestIndex": 1,



"type": "ACTION",



"valueMs": 1



}



]



},



"outageHandling": {



"globalOutage": true,



"globalOutagePolicy": {



"consecutiveRuns": 1



},



"localOutage": true,



"localOutagePolicy": {



"affectedLocations": 1,



"consecutiveRuns": 1



},



"retryOnError": true



}



},



"automaticallyAssignedApps": [



"string"



],



"createdFrom": "API",



"enabled": true,



"entityId": "string",



"frequencyMin": 1,



"locations": [



"string"



],



"managementZones": [



{



"id": "string",



"name": "string"



}



],



"manuallyAssignedApps": [



"string"



],



"name": "string",



"script": {},



"tags": [



{



"context": "AWS",



"key": "string",



"source": "AUTO",



"value": "string"



}



],



"type": "BROWSER"



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

## Example

In this example, the request lists the parameters of the **dynatrace.com** monitor, which is a **browser clickpath** that navigates to [https://www.dynatrace.com/﻿](https://www.dynatrace.com/) and signs up for a free trial.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/monitors/SYNTHETIC_TEST-0000000000025434 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/monitors/SYNTHETIC_TEST-0000000000025434
```

#### Response body

```
{



"entityId": "SYNTHETIC_TEST-0000000000025434",



"name": "dynatrace.com",



"frequencyMin": 15,



"enabled": true,



"type": "browser",



"script": {



"type": "clickpath",



"version": "1.0",



"configuration": {



"device": {



"deviceName":"Desktop",



"orientation":"landscape"



}



},



"events": [



{



"type":"navigate",



"description":"Loading of \"http://www.dynatrace.com\"",



"url":"http://www.dynatrace.com",



"wait": {



"waitFor":"page_complete"



}



},



{



"type":"click",



"description":"click on \"Free trial\"",



"target": {



"locators": [



{



"type":"css",



"value":"a:contains(\"Free trial\"):eq(1)"



},



{



"type":"css",



"value":".btn:eq(1)"



},



{



"type":"css",



"value":"#content div div div div div div div p:nth-child(3) a"



},



{



"type":"css",



"value":"#content div.homepage-hero-wrapper div.gallery div.flickity-viewport div.flickity-slider div.gallery-cell div.section div.column p.cta--row a.btn:eq(0)"



}



]



},



"button": 0,



"wait": {



"waitFor":"page_complete"



}



}



{



"type":"click",



"description":"click on \"email\"",



"target": {



"locators": [



{



"type":"css",



"value":"input[type=\"email\"][name=\"email\"]:eq(0)"



},



{



"type":"dom",



"value":"document.forms[0][\"email\"]"



},



{



"type":"css",



"value":".inputfield:eq(0)"



},



{



"type":"css",



"value":"#content div div:nth-child(2) form:nth-child(9) input:nth-child(3)"



},



{



"type":"css",



"value":"#content div.section div.tile form.cta input.inputfield:eq(0)"



}



]



},



"button":0



},



{



"type":"keystrokes",



"description":"keystrokes on \"email\"",



"target":{



"locators":[



{



"type":"css",



"value":"input[type=\"email\"][name=\"email\"]:eq(0)"



},



{



"type":"dom",



"value":"document.forms[0][\"email\"]"



},



{



"type":"css",



"value":".inputfield:eq(0)"



},



{



"type":"css",



"value":"#content div div:nth-child(2) form:nth-child(9) input:nth-child(3)"



},



{



"type":"css",



"value":"#content div.section div.tile form.cta input.inputfield:eq(0)"



}



]



},



"textValue":"sample@sample.com",



"masked":false,



"simulateBlurEvent":true



},



{



"type":"click",



"description":"click on \"Start free trial\"",



"target":{



"locators":[



{



"type":"css",



"value":"input[type=\"submit\"]:eq(0)"



},



{



"type":"dom",



"value":"document.forms[0][19]"



},



{



"type":"css",



"value":".btn:eq(1)"



},



{



"type":"css",



"value":"#content div div:nth-child(2) form:nth-child(9) div:nth-child(22) input"



},



{



"type":"css",



"value":"#content div.section div.tile form.cta div.cta__formgroup input.btn:eq(0)"



}



]



},



"button":0,



"wait":{



"waitFor":"page_complete"



}



}



]



},



"locations": [



"GEOLOCATION-B69A5A40388CC698",



"GEOLOCATION-A9022AAFA0763F56"



],



"anomalyDetection": {



"outageHandling": {



"globalOutage": true,



"localOutage": false,



"localOutagePolicy": {



"affectedLocations": 1,



"consecutiveRuns": 3



}



},



"loadingTimeThresholds": {



"enabled": false,



"thresholds": []



}



},



"tags": [],



"managementZones": [



{



"id": "-7832237287622819191",



"name": "!!allSynthetic"



}



]



}
```

#### Response code

200

## Related topics

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.")
* [Script mode for browser monitor configuration in Classic](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/script-mode-for-browser-monitor-configuration "Create or edit your browser monitors in JSON format.")
* [Script mode for HTTP monitor configuration in Classic](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/script-mode-for-http-monitor-configuration-classic "Create or edit your HTTP monitors in JSON format.")