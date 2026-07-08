---
title: Synthetic monitors API - PUT a monitor
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic/synthetic-monitors/put-a-monitor
---

# Synthetic monitors API - PUT a monitor

# Synthetic monitors API - PUT a monitor

* Reference
* Published Sep 24, 2018

Updates the specified monitor.

The configuration of the monitor is passed via its JSON script.

You can copy the script of an existing monitor and adjust it as needed.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/synthetic/monitors/{monitorId}` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/synthetic/monitors/{monitorId}` |

## Authentication

To execute this request, you need an access token with `ExternalSyntheticIntegration` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

To find all model variations that depend on the type of the model, see [JSON models](/managed/dynatrace-api/environment-api/synthetic/synthetic-monitors/models "Learn the variations of models in the Synthetic monitors v1 API.").

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| monitorId | string | The ID of the synthetic monitor to be updated. | path | Required |
| body | [SyntheticMonitorUpdate](#openapi-definition-SyntheticMonitorUpdate) | The synthetic monitor update.  The actual set of fields depends the type of the monitor. Find the list of actual objects in the description of the **type** field or see [Synthetic monitors API - JSON models﻿](https://dt-url.net/2523se9). | body | Optional |

### Request body objects

#### The `SyntheticMonitorUpdate` object

The synthetic monitor update.

The actual set of fields depends the type of the monitor. Find the list of actual objects in the description of the **type** field or see [Synthetic monitors API - JSON models﻿](https://dt-url.net/2523se9).

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| anomalyDetection | [AnomalyDetection](#openapi-definition-AnomalyDetection) | The anomaly detection configuration. | Optional |
| enabled | boolean | The monitor is enabled (`true`) or disabled (`false`). | Required |
| frequencyMin | integer | The frequency of the monitor, in minutes.  You can use one of the following values: `5`, `10`, `15`, `30`, and `60`. | Required |
| locations | string[] | A list of locations from which the monitor is executed.  To specify a location, use its entity ID. For public locations use `GEOLOCATION-9999453BE4BDB3CD` form and `SYNTHETIC_LOCATION-DF80ACFB688C583B` for private ones. | Required |
| manuallyAssignedApps | string[] | A set of manually assigned applications. | Required |
| name | string | The name of the monitor. | Required |
| script | object | The script of a [browser﻿](https://dt-url.net/9c103rda) or HTTP monitor. | Required |
| tags | [TagWithSourceInfo](#openapi-definition-TagWithSourceInfo)[] | A set of tags assigned to the monitor.  You can specify only the value of the tag here and the `CONTEXTLESS` context and source 'USER' will be added automatically. But preferred option is usage of TagWithSourceDto model. | Required |
| type | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `BROWSER` -> BrowserSyntheticMonitorUpdate * `HTTP` -> HttpSyntheticMonitorUpdate The element can hold these values * `BROWSER` * `HTTP` | Required |

#### The `AnomalyDetection` object

The anomaly detection configuration.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| loadingTimeThresholds | [LoadingTimeThresholdsPolicyDto](#openapi-definition-LoadingTimeThresholdsPolicyDto) | Performance thresholds configuration. | Optional |
| outageHandling | [OutageHandlingPolicy](#openapi-definition-OutageHandlingPolicy) | Outage handling configuration. | Optional |

#### The `LoadingTimeThresholdsPolicyDto` object

Performance thresholds configuration.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| enabled | boolean | Performance threshold is enabled (`true`) or disabled (`false`). | Required |
| thresholds | [LoadingTimeThreshold](#openapi-definition-LoadingTimeThreshold)[] | The list of performance threshold rules. | Required |

#### The `LoadingTimeThreshold` object

The performance threshold rule.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| eventIndex | integer | Specify the event to which an ACTION threshold applies. | Optional |
| requestIndex | integer | Specify the request to which an ACTION threshold applies. | Optional |
| type | string | The type of the threshold: total loading time or action loading time. The element can hold these values * `ACTION` * `TOTAL` | Required |
| valueMs | integer | Notify if monitor takes longer than *X* milliseconds to load. | Required |

#### The `OutageHandlingPolicy` object

Outage handling configuration.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| globalOutage | boolean | When enabled (`true`), generate a problem and send an alert when the monitor is unavailable at all configured locations. | Required |
| globalOutagePolicy | [GlobalOutagePolicy](#openapi-definition-GlobalOutagePolicy) | Global outage handling configuration. | Optional |
| localOutage | boolean | When enabled (`true`), generate a problem and send an alert when the monitor is unavailable for one or more consecutive runs at any location. | Required |
| localOutagePolicy | [LocalOutagePolicy](#openapi-definition-LocalOutagePolicy) | Local outage handling configuration.  Alert if **affectedLocations** of locations are unable to access the web application **consecutiveRuns** times consecutively. | Required |
| retryOnError | boolean | Schedule retry if browser monitor execution results in a fail. For HTTP monitors this property is ignored. | Optional |

#### The `GlobalOutagePolicy` object

Global outage handling configuration.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| consecutiveRuns | integer | Alert if all locations are unable to access the web application *X* times consecutively. | Required |

#### The `LocalOutagePolicy` object

Local outage handling configuration.

Alert if **affectedLocations** of locations are unable to access the web application **consecutiveRuns** times consecutively.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| affectedLocations | integer | The number of affected locations to trigger an alert. | Required |
| consecutiveRuns | integer | The number of consecutive fails to trigger an alert. | Required |

#### The `TagWithSourceInfo` object

Tag with source of a Dynatrace entity.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| context | string | The origin of the tag, such as AWS or Cloud Foundry.  Custom tags use the `CONTEXTLESS` value. The element can hold these values * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` | Required |
| key | string | The key of the tag.  Custom tags have the tag value here. | Required |
| source | string | The source of the tag, such as USER, RULE\_BASED or AUTO The element can hold these values * `AUTO` * `RULE_BASED` * `USER` | Optional |
| value | string | The value of the tag.  Not applicable to custom tags. | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"anomalyDetection": {



"loadingTimeThresholds": {



"enabled": true,



"thresholds": [



{



"requestIndex": 1,



"type": "TOTAL",



"valueMs": 100



}



]



},



"outageHandling": {



"globalOutage": true,



"localOutage": true,



"localOutagePolicy": {



"affectedLocations": 1,



"consecutiveRuns": 3



}



}



},



"enabled": true,



"events": [],



"frequencyMin": 5,



"keyPerformanceMetrics": {



"loadActionKpm": "VISUALLY_COMPLETE",



"xhrActionKpm": "VISUALLY_COMPLETE"



},



"locations": [



"GEOLOCATION-9999453BE4BDB3CD",



"SYNTHETIC_LOCATION-DF80ACFB688C583B"



],



"manuallyAssignedApps": [



"APPLICATION-4ADF0EF407C7C545"



],



"name": "Browser Monitor Example",



"script": {



"configuration": {



"device": {



"deviceName": "Desktop",



"orientation": "landscape"



}



},



"events": [



{



"description": "Loading of \"example.com\"",



"type": "navigate",



"url": "http://example.com",



"wait": {



"waitFor": "page_complete"



}



}



],



"type": "availability",



"version": "1.0"



},



"tags": [



"example"



],



"type": "BROWSER"



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. The synthetic monitor has been updated. The response doesn't have a body. |
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

## Example

In this example, the request updates the **dynatrace.com** monitor from the [GET monitor example](/managed/dynatrace-api/environment-api/synthetic/synthetic-monitors/get-a-monitor#example "View a synthetic monitor via the Synthetic v1 API."), changing the list of locations from which it is executed and increasing the frequency to **10 minutes**.

The API token is passed in the **Authorization** header.

Since the request body is lengthy, it is truncated in this example **Curl** section. See the full body in the **Request body** section. You can download or copy the example request body to try it out on your own. Before using it, make sure that the location from the example is available in your environment. You can fetch the list of available locations with the [**GET all synthetic locations**](/managed/dynatrace-api/environment-api/synthetic/synthetic-locations/get-all-locations "List all synthetic locations via the Synthetic v1 API.") call. If the location is not available, replace it with any location you're using.

#### Curl

```
curl -X PUT \



https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/monitors/SYNTHETIC_TEST-0000000000025434 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{<truncated - see the Request body section > }



'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/monitors/SYNTHETIC_TEST-0000000000025434
```

#### Request body

```
{



"frequencyMin": 10,



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



"type": "browser",



"name": "dynatrace.com",



"locations": [



"GEOLOCATION-0A41430434C388A9",



"GEOLOCATION-95196F3C9A4F4215",



"GEOLOCATION-0DF9A0E1095A5A62"



],



"enabled": true,



"script": {



"type": "clickpath",



"version": "1.0",



"configuration": {



"device": {



"deviceName": "Desktop",



"orientation": "landscape"



}



},



"events": [



{



"type": "navigate",



"description": "Loading of \"http://www.dynatrace.com\"",



"url": "http://www.dynatrace.com",



"wait": {



"waitFor": "page_complete"



}



},



{



"type": "click",



"description": "click on \"Free trial\"",



"target": {



"locators": [



{



"type": "css",



"value": "a:contains(\"Free trial\"):eq(1)"



},



{



"type": "css",



"value": ".btn:eq(1)"



},



{



"type": "css",



"value": "#content div div div div div div div p:nth-child(3) a"



},



{



"type": "css",



"value": "#content div.homepage-hero-wrapper div.gallery div.flickity-viewport div.flickity-slider div.gallery-cell div.section div.column p.cta--row a.btn:eq(0)"



}



]



},



"button": 0,



"wait": {



"waitFor": "page_complete"



}



},



{



"type": "click",



"description": "click on \"email\"",



"target": {



"locators": [



{



"type": "css",



"value": "input[type=\"email\"][name=\"email\"]:eq(0)"



},



{



"type": "dom",



"value": "document.forms[0][\"email\"]"



},



{



"type": "css",



"value": ".inputfield:eq(0)"



},



{



"type": "css",



"value": "#content div div:nth-child(2) form:nth-child(9) input:nth-child(3)"



},



{



"type": "css",



"value": "#content div.section div.tile form.cta input.inputfield:eq(0)"



}



]



},



"button": 0



},



{



"type": "keystrokes",



"description": "keystrokes on \"email\"",



"target": {



"locators": [



{



"type": "css",



"value": "input[type=\"email\"][name=\"email\"]:eq(0)"



},



{



"type": "dom",



"value": "document.forms[0][\"email\"]"



},



{



"type": "css",



"value": ".inputfield:eq(0)"



},



{



"type": "css",



"value": "#content div div:nth-child(2) form:nth-child(9) input:nth-child(3)"



},



{



"type": "css",



"value": "#content div.section div.tile form.cta input.inputfield:eq(0)"



}



]



},



"textValue": "sample@sample.com",



"masked": false,



"simulateBlurEvent": true



},



{



"type": "click",



"description": "click on \"Start free trial\"",



"target": {



"locators": [



{



"type": "css",



"value": "input[type=\"submit\"]:eq(0)"



},



{



"type": "dom",



"value": "document.forms[0][19]"



},



{



"type": "css",



"value": ".btn:eq(1)"



},



{



"type": "css",



"value": "#content div div:nth-child(2) form:nth-child(9) div:nth-child(22) input"



},



{



"type": "css",



"value": "#content div.section div.tile form.cta div.cta__formgroup input.btn:eq(0)"



}



]



},



"button": 0,



"wait": {



"waitFor": "page_complete"



}



}



]



},



"tags": []



}
```

#### Response code

204

## Related topics

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.")
* [Script mode for browser monitor configuration in Classic](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/script-mode-for-browser-monitor-configuration "Create or edit your browser monitors in JSON format.")
* [Script mode for HTTP monitor configuration in Classic](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/script-mode-for-http-monitor-configuration-classic "Create or edit your HTTP monitors in JSON format.")