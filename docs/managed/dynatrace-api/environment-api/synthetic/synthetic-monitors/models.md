---
title: Synthetic monitors API - JSON models
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic/synthetic-monitors/models
scraped: 2026-05-12T12:10:02.374167
---

# Synthetic monitors API - JSON models

# Synthetic monitors API - JSON models

* Reference
* Published Aug 19, 2019

Some JSON models of the **Synthetic monitors** API vary depending on the **type** of the model. The JSON models for each variation are listed below.

## Variations of the `SyntheticMonitor` object

### BROWSER

BrowserSyntheticMonitor

Parameters

JSON model

#### The `BrowserSyntheticMonitor` object

Browser synthetic monitor. Some fields are inherited from the base `SyntheticMonitor` model.

| Element | Type | Description |
| --- | --- | --- |
| events | [EventDto[]](#openapi-definition-EventDto) | A list of events for this monitor |
| keyPerformanceMetrics | [KeyPerformanceMetrics](#openapi-definition-KeyPerformanceMetrics) | The key performance metrics configuration. |

#### The `EventDto` object

| Element | Type | Description |
| --- | --- | --- |
| entityId | string | Event identifier |
| name | string | Event name |
| sequenceNumber | integer | Event sequence number |

#### The `KeyPerformanceMetrics` object

The key performance metrics configuration.

| Element | Type | Description |
| --- | --- | --- |
| loadActionKpm | string | Defines the key performance metric for load actions. The element can hold these values * `VISUALLY_COMPLETE` * `SPEED_INDEX` * `USER_ACTION_DURATION` * `TIME_TO_FIRST_BYTE` * `HTML_DOWNLOADED` * `DOM_INTERACTIVE` * `LOAD_EVENT_START` * `LOAD_EVENT_END` |
| xhrActionKpm | string | Defines the key performance metric for XHR actions. The element can hold these values * `VISUALLY_COMPLETE` * `USER_ACTION_DURATION` * `TIME_TO_FIRST_BYTE` * `RESPONSE_END` |

```
{



"entityId": "SYNTHETIC_TEST-790745B687BE4D0E",



"name": "Browser monitor",



"frequencyMin": 10,



"enabled": true,



"type": "BROWSER",



"createdFrom": "GUI",



"script": {



"type": "clickpath",



"version": "1.0",



"configuration": {



"device": {



"mobile": false,



"touchEnabled": false,



"width": 1024,



"height": 768,



"scaleFactor": 1



}



},



"events": [



{



"type": "navigate",



"description": "Loading of \"https://orf.at\"",



"url": "https://orf.at",



"wait": {



"waitFor": "page_complete"



}



}



]



},



"locations": [



"GEOLOCATION-0A41430434C388A9"



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



"enabled": true,



"thresholds": [



{



"type": "TOTAL",



"valueMs": 10000



}



]



}



},



"tags": [



{



"context": "CONTEXTLESS",



"key": "blabla"



}



],



"managementZones": [



{



"id": "-7832237287622819191",



"name": "!!allSynthetic"



}



],



"automaticallyAssignedApps": [



"APPLICATION-7ADA0EF404C7C545"



],



"manuallyAssignedApps": [



"APPLICATION-4ADF0EF407C7C545"



],



"keyPerformanceMetrics": {



"loadActionKpm": "VISUALLY_COMPLETE",



"xhrActionKpm": "VISUALLY_COMPLETE"



},



"events": [



{



"entityId": "SYNTHETIC_TEST_STEP-2E6FDA5B4BC39A27",



"name": "Loading of \"https://orf.at\"",



"sequenceNumber": 1



}



]



}
```

### HTTP

HttpSyntheticMonitor

Parameters

JSON model

#### The `HttpSyntheticMonitor` object

HTTP synthetic monitor. Some fields are inherited from base `SyntheticMonitor` model.

| Element | Type | Description |
| --- | --- | --- |
| requests | [RequestDto[]](#openapi-definition-RequestDto) | A list of events for this monitor |

#### The `RequestDto` object

| Element | Type | Description |
| --- | --- | --- |
| entityId | string | Request identifier |
| name | string | Request name |
| sequenceNumber | integer | Request sequence number |

```
{



"entityId": "HTTP_CHECK-B58DA1B8B892A05C",



"name": "HTTP monitor",



"frequencyMin": 1,



"enabled": true,



"type": "HTTP",



"createdFrom": "GUI",



"script": {



"version": "1.0",



"requests": [



{



"description": "orf.at",



"url": "https://orf.at",



"method": "GET",



"requestBody": "",



"configuration": {



"acceptAnyCertificate": true,



"followRedirects": true



},



"preProcessingScript": "",



"postProcessingScript": ""



}



]



},



"locations": [



"SYNTHETIC_LOCATION-61F43EECF5FB8345"



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



"thresholds": [



{



"type": "TOTAL",



"valueMs": 10000



}



]



}



},



"tags": [],



"managementZones": [



{



"id": "-7832237287622819191",



"name": "!!allSynthetic"



}



],



"automaticallyAssignedApps": [



"APPLICATION-4ADF0EF407C7C545"



],



"manuallyAssignedApps": [



"APPLICATION-7ADA0EF404C7C545"



],



"requests": [



{



"entityId": "HTTP_CHECK_STEP-E9208469D53BAF38",



"name": "orf.at",



"sequenceNumber": 1



}



]



}
```

## Variations of the `SyntheticMonitorUpdate` object

### BROWSER

BrowserSyntheticMonitorUpdate

Parameters

JSON model

#### The `BrowserSyntheticMonitorUpdate` object

Browser synthetic monitor update. Some fields are inherited from base `SyntheticMonitorUpdate` model.

| Element | Type | Description |
| --- | --- | --- |
| keyPerformanceMetrics | [KeyPerformanceMetrics](#openapi-definition-KeyPerformanceMetrics) | The key performance metrics configuration. |

#### The `KeyPerformanceMetrics` object

The key performance metrics configuration.

| Element | Type | Description |
| --- | --- | --- |
| loadActionKpm | string | Defines the key performance metric for load actions. The element can hold these values * `VISUALLY_COMPLETE` * `SPEED_INDEX` * `USER_ACTION_DURATION` * `TIME_TO_FIRST_BYTE` * `HTML_DOWNLOADED` * `DOM_INTERACTIVE` * `LOAD_EVENT_START` * `LOAD_EVENT_END` |
| xhrActionKpm | string | Defines the key performance metric for XHR actions. The element can hold these values * `VISUALLY_COMPLETE` * `USER_ACTION_DURATION` * `TIME_TO_FIRST_BYTE` * `RESPONSE_END` |

```
{



"name": "Browser monitor",



"frequencyMin": 10,



"enabled": true,



"type": "BROWSER",



"script": {



"type": "clickpath",



"version": "1.0",



"configuration": {



"device": {



"mobile": false,



"touchEnabled": false,



"width": 1024,



"height": 768,



"scaleFactor": 1



}



},



"events": [



{



"type": "navigate",



"description": "Loading of \"https://orf.at\"",



"url": "https://orf.at",



"wait": {



"waitFor": "page_complete"



}



}



]



},



"locations": [



"GEOLOCATION-0A41430434C388A9"



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



"enabled": true,



"thresholds": [



{



"type": "TOTAL",



"valueMs": 10000



}



]



}



},



"tags": [



{



"context": "CONTEXTLESS",



"key": "blabla"



}



],



"manuallyAssignedApps": [



"APPLICATION-4ADF0EF407C7C545"



],



"keyPerformanceMetrics": {



"loadActionKpm": "VISUALLY_COMPLETE",



"xhrActionKpm": "VISUALLY_COMPLETE"



}



}
```

### HTTP

HttpSyntheticMonitorUpdate

Parameters

JSON model

#### The `HttpSyntheticMonitorUpdate` object

HTTP synthetic monitor update. Some fields are inherited from base `SyntheticMonitorUpdate` model.

| Element | Type | Description |
| --- | --- | --- |
| anomalyDetection | [AnomalyDetection](#openapi-definition-AnomalyDetection) | The anomaly detection configuration. |
| enabled | boolean | The monitor is enabled (`true`) or disabled (`false`). |
| frequencyMin | integer | The frequency of the monitor, in minutes.  You can use one of the following values: `5`, `10`, `15`, `30`, and `60`. |
| locations | string[] | A list of locations from which the monitor is executed.  To specify a location, use its entity ID. For public locations use `GEOLOCATION-9999453BE4BDB3CD` form and `SYNTHETIC_LOCATION-DF80ACFB688C583B` for private ones. |
| manuallyAssignedApps | string[] | A set of manually assigned applications. |
| name | string | The name of the monitor. |
| script | object | The script of a [browserï»¿](https://dt-url.net/9c103rda) or HTTP monitor. |
| tags | [TagWithSourceInfo[]](#openapi-definition-TagWithSourceInfo) | A set of tags assigned to the monitor.  You can specify only the value of the tag here and the `CONTEXTLESS` context and source 'USER' will be added automatically. But preferred option is usage of TagWithSourceDto model. |
| type | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `BROWSER` -> BrowserSyntheticMonitorUpdate * `HTTP` -> HttpSyntheticMonitorUpdate The element can hold these values * `BROWSER` * `HTTP` |

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
| thresholds | [LoadingTimeThreshold[]](#openapi-definition-LoadingTimeThreshold) | The list of performance threshold rules. |

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

#### The `TagWithSourceInfo` object

Tag with source of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| context | string | The origin of the tag, such as AWS or Cloud Foundry.  Custom tags use the `CONTEXTLESS` value. The element can hold these values * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | The key of the tag.  Custom tags have the tag value here. |
| source | string | The source of the tag, such as USER, RULE\_BASED or AUTO The element can hold these values * `AUTO` * `RULE_BASED` * `USER` |
| value | string | The value of the tag.  Not applicable to custom tags. |

```
{



"name": "HTTP monitor",



"frequencyMin": 1,



"enabled": true,



"type": "HTTP",



"script": {



"version": "1.0",



"requests": [



{



"description": "orf.at",



"url": "https://orf.at",



"method": "GET",



"requestBody": "",



"configuration": {



"acceptAnyCertificate": true,



"followRedirects": true



},



"preProcessingScript": "",



"postProcessingScript": ""



}



]



},



"locations": [



"SYNTHETIC_LOCATION-61F43EECF5FB8345"



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



"thresholds": [



{



"type": "TOTAL",



"valueMs": 10000



}



]



}



},



"tags": [],



"manuallyAssignedApps": [



"APPLICATION-7ADA0EF404C7C545"



]



}
```

## Related topics

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.")