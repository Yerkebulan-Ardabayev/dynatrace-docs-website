---
title: Third-party synthetic API - POST third-party monitors to Dynatrace
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic/third-party-synthetic/post-third-party-monitors
---

# Third-party synthetic API - POST third-party monitors to Dynatrace

# Third-party synthetic API - POST third-party monitors to Dynatrace

* Reference
* Published May 15, 2020

Pushes third-party synthetic monitors, locations, and monitor execution results to Dynatrace.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/synthetic/ext/tests` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/synthetic/ext/tests` |

## Authentication

To execute this request, you need an access token with `ExternalSyntheticIntegration` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [3rdPartySyntheticTests](#openapi-definition-3rdPartySyntheticTests) | The JSON body of the request. Contains third-party synthetic monitors, locations, and results. | body | Required |

### Request body objects

#### The `3rdPartySyntheticTests` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| locations | [3rdPartySyntheticLocation](#openapi-definition-3rdPartySyntheticLocation)[] | The list of third-party synthetic locations. | Required |
| messageTimestamp | integer | The timestamp of the message creation, in UTC milliseconds. | Required |
| syntheticEngineIconUrl | string | The URL of the third-party synthetic monitor icon. | Optional |
| syntheticEngineName | string | The type of the third-party synthetic monitor. | Required |
| testResults | [3rdPartySyntheticTestResult](#openapi-definition-3rdPartySyntheticTestResult)[] | The list of results of third-party synthetic monitor execution. | Optional |
| tests | [3rdPartySyntheticMonitor](#openapi-definition-3rdPartySyntheticMonitor)[] | The list of third-party synthetic monitors. | Required |

#### The `3rdPartySyntheticLocation` object

The third-party Synthetic location.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| id | string | The ID of the location. | Required |
| ip | string | The IP address of the location. | Optional |
| name | string | The name of the location, displayed in the UI. | Required |

#### The `3rdPartySyntheticTestResult` object

The results of third-party synthetic monitor execution.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| id | string | The ID of the third-party synthetic monitor. | Required |
| locationResults | [3rdPartySyntheticLocationTestResult](#openapi-definition-3rdPartySyntheticLocationTestResult)[] | Results of third-party monitor executions per location. | Required |
| totalStepCount | integer | Number of steps in the monitor. Defaults to number of SyntheticTestSteps. | Optional |

#### The `3rdPartySyntheticLocationTestResult` object

Results of third-party monitor executions per location.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| id | string | The ID of the location. | Required |
| responseTimeMillis | integer | The overall response time of the monitor from this location, in milliseconds.  If absent, it is calculated as the sum of response times of all steps. | Optional |
| startTimestamp | integer | The timestamp of text execution start, in UTC milliseconds. | Required |
| stepResults | [SyntheticMonitorStepResult](#openapi-definition-SyntheticMonitorStepResult)[] | Results of individual monitor steps. | Required |
| success | boolean | If the test was successful (`true`) or failed (`false`) - will influence availability timeseries. | Required |
| successRate | number | The overall availability of the monitor from this location, percent.  If absent, calculated as the number of successful steps compared to the overall number of steps. | Optional |

#### The `SyntheticMonitorStepResult` object

The result of the individual step of a synthetic monitor.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| error | [SyntheticMonitorError](#openapi-definition-SyntheticMonitorError) | The error message of a synthetic monitor step. | Optional |
| id | integer | ID of the step. It is unique within the test definition. | Required |
| responseTimeMillis | integer | The response time of the step, in milliseconds.  Absent when no meaningful response time is available (as may be the case for certain error conditions such as a misconfigured step script). | Optional |
| startTimestamp | integer | The timestamp of test step execution, UTC milliseconds. | Required |

#### The `SyntheticMonitorError` object

The error message of a synthetic monitor step.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| code | integer | The error code. | Required |
| message | string | The error message. | Required |

#### The `3rdPartySyntheticMonitor` object

The third-party synthetic monitor.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| deleted | boolean | The flag of the deleted monitor. Default is `false`.  If `true`, set the **enabled** parameter to `false`. | Optional |
| description | string | A description of the monitor. | Optional |
| drilldownLink | string | The URL to the results of monitor execution. | Optional |
| editLink | string | The URL to edit the monitor in the original UI. | Optional |
| enabled | boolean | The monitor is enabled (`true`) or disabled (`false`). Default is `true`.  If `true`, set the **deleted** parameter to `false`. | Optional |
| expirationTimestamp | integer | The timestamp of the monitor expiration, in UTC milliseconds. | Optional |
| id | string | The ID of the monitor. | Required |
| locations | [SyntheticTestLocation](#openapi-definition-SyntheticTestLocation)[] | Locations from which the synthetic monitor runs. | Required |
| noDataTimeout | integer | The timeout of the monitor, in seconds. If no result is reported within this time, the availability state switches to unmonitored. Default is doubled frequency of the monitor. | Optional |
| scheduleIntervalInSeconds | integer | The frequency of the monitor, in seconds. The monitor is repeated with the specified interval at the third-party source.  Dynatrace expects results of a monitor execution with the specified interval. If you report results to Dynatrace less often, adjust the **noDataTimeout** value accordingly. | Required |
| steps | [SyntheticTestStep](#openapi-definition-SyntheticTestStep)[] | Steps of the third-party monitor. | Optional |
| testSetup | string | The information on monitor setup, for example `browser`. | Optional |
| title | string | The name of the monitor. | Required |

#### The `SyntheticTestLocation` object

Synthetic test location.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| enabled | boolean | The location is enabled/disabled. Default is `true`, enabling the location. | Optional |
| id | string | The ID of the location. | Required |

#### The `SyntheticTestStep` object

The step of a synthetic monitor.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| id | integer | The ID of the step. | Required |
| title | string | The name of the step, displayed in the UI. | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"locations": [



{



"id": "string",



"ip": "string",



"name": "string"



}



],



"messageTimestamp": 1,



"syntheticEngineIconUrl": "string",



"syntheticEngineName": "string",



"testResults": [



{



"id": "string",



"locationResults": [



{



"id": "string",



"responseTimeMillis": 1,



"startTimestamp": 1,



"stepResults": [



{



"error": {



"code": 1,



"message": "string"



},



"id": 1,



"responseTimeMillis": 1,



"startTimestamp": 1



}



],



"success": true,



"successRate": 1



}



],



"totalStepCount": 1



}



],



"tests": [



{



"deleted": true,



"description": "string",



"drilldownLink": "string",



"editLink": "string",



"enabled": true,



"expirationTimestamp": 1,



"id": "string",



"locations": [



{



"enabled": true,



"id": "string"



}



],



"noDataTimeout": 1,



"scheduleIntervalInSeconds": 1,



"steps": [



{



"id": 1,



"title": "string"



}



],



"testSetup": "string",



"title": "string"



}



]



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. The information is accepted and stored. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
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

In this example, the request pushes the following data from third-party synthetic engine **My third-party synthetic** to Dynatrace:

* Three locations: **Linz1**, **Linz2**, and **Linz3**.
* Two monitors: **example of synthetic monitor - 1** and **example of synthetic monitor - 2**, each containing three steps and running from two locations.
* One result per step, per location, for each monitor.

Monitors have the following parameters:

|  | example of synthetic monitor - 1 | example of synthetic monitor - 2 |
| --- | --- | --- |
| Frequency | 300 seconds (5 minutes) | 300 seconds (5 minutes) |
| Locations | Linz1 Linz2 | Linz2 Linz3 |
| Steps | Step1-1 Step1-2 Step1-3 | Step2-1 Step2-2 Step3-3 |

The **example of synthetic monitor - 1** monitor has the following response times in milliseconds:

|  | Linz1 | Linz2 |
| --- | --- | --- |
| Step1-1 | 7790 | 2075 |
| Step1-2 | 2073 | 4079 |
| Step1-3 | 8650 | 3937 |

The **example of synthetic monitor - 2** monitor has the following response times in milliseconds:

|  | Linz2 | Linz3 |
| --- | --- | --- |
| Step2-1 | 2200 | 9123 |
| Step2-2 | 6903 | 9722 |
| Step2-3 | 4821 | 1717 |

The API token is passed in the **Authorization** header.

Since the request body is lengthy, it is truncated in this example **Curl** section. See the full body in the **Request body** section. You can download the request body JSON to perform a sample request in your environment. Be sure to replace the timestamps with recent ones or the results will be too old.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/ext/tests \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{ <truncated - see the Request body section >}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/ext/tests
```

#### Request body

```
{



"syntheticEngineName": "My third-party synthetic",



"syntheticEngineIconUrl": "https://static.thenounproject.com/png/1745-200.png",



"messageTimestamp": 1543572265528,



"locations": [



{



"id": "Linz1",



"ip": "127.0.0.1",



"name": "Linz1"



},



{



"id": "Linz2",



"ip": "127.0.0.2",



"name": "Linz2"



},



{



"id": "Linz3",



"ip": "127.0.0.3",



"name": "Linz3"



}



],



"tests": [



{



"id": "3rdPartySyntheticMonitor1",



"title": "example of synthetic monitor - 1",



"scheduleIntervalInSeconds": 300,



"locations": [



{



"id": "Linz1"



},



{



"id": "Linz2"



}



],



"steps": [



{



"id": 1,



"title": "Step1-1"



},



{



"id": 2,



"title": "Step1-2"



},



{



"id": 3,



"title": "Step1-3"



}



]



},



{



"id": "3rdPartySyntheticMonitor2",



"title": "example of synthetic monitor - 2",



"scheduleIntervalInSeconds": 300,



"locations": [



{



"id": "Linz2"



},



{



"id": "Linz3"



}



],



"steps": [



{



"id": 1,



"title": "Step2-1"



},



{



"id": 2,



"title": "Step2-2"



},



{



"id": 3,



"title": "Step2-3"



}



]



}



],



"testResults": [



{



"id": "3rdPartySyntheticMonitor1",



"totalStepCount": 3,



"locationResults": [



{



"id": "Linz1",



"startTimestamp": 1543572262538,



"success": true,



"stepResults": [



{



"id": 1,



"startTimestamp": 1543572262538,



"responseTimeMillis": 7790



},



{



"id": 2,



"startTimestamp": 1543572262538,



"responseTimeMillis": 2073



},



{



"id": 3,



"startTimestamp": 1543572262538,



"responseTimeMillis": 8650



}



]



},



{



"id": "Linz2",



"startTimestamp": 1543572262548,



"success": true,



"stepResults": [



{



"id": 1,



"startTimestamp": 1543572262548,



"responseTimeMillis": 2075



},



{



"id": 2,



"startTimestamp": 1543572262548,



"responseTimeMillis": 4079



},



{



"id": 3,



"startTimestamp": 1543572262548,



"responseTimeMillis": 3937



}



]



}



]



},



{



"id": "3rdPartySyntheticMonitor2",



"totalStepCount": 3,



"locationResults": [



{



"id": "Linz2",



"startTimestamp": 1543572262548,



"success": true,



"stepResults": [



{



"id": 1,



"startTimestamp": 1543572262548,



"responseTimeMillis": 2200



},



{



"id": 2,



"startTimestamp": 1543572262548,



"responseTimeMillis": 6903



},



{



"id": 3,



"startTimestamp": 1543572262548,



"responseTimeMillis": 4821



}



]



},



{



"id": "Linz3",



"startTimestamp": 1543572262558,



"success": true,



"stepResults": [



{



"id": 1,



"startTimestamp": 1543572262558,



"responseTimeMillis": 9123



},



{



"id": 2,



"startTimestamp": 1543572262558,



"responseTimeMillis": 9722



},



{



"id": 3,



"startTimestamp": 1543572262558,



"responseTimeMillis": 1717



}



]



}



]



}



]



}
```

#### Response code

204

#### Result

Highlight shows parameters, submitted in the request.

![External synthetic monitors](https://dt-cdn.net/images/ext-monitors-1340-4aaf90d700.png)

External synthetic monitors

![External synthetic monitor details](https://dt-cdn.net/images/ext-monitor-details-1850-2d6cb27a83.png)

External synthetic monitor details