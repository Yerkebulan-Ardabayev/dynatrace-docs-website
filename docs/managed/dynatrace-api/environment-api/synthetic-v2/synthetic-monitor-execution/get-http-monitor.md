---
title: Synthetic monitor executions API v2 - GET HTTP monitor
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-monitor-execution/get-http-monitor
scraped: 2026-05-12T11:57:56.285583
---

# Synthetic monitor executions API v2 - GET HTTP monitor

# Synthetic monitor executions API v2 - GET HTTP monitor

* Reference
* Published Apr 20, 2021

Gets the result of the most recent execution of the specified HTTP monitor.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/synthetic/execution/{monitorId}/{resultType}` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/synthetic/execution/{monitorId}/{resultType}` |

## Authentication

To execute this request, you need an access token with one of the following scopes:

* `DataExport`
* `ExternalSyntheticIntegration`
* `ReadSyntheticData`

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| monitorId | string | Identifier of the HTTP monitor for which last execution result is returned. | path | Required |
| resultType | string | Defines the result type of the last HTTP monitor's execution. The element can hold these values * `SUCCESS` * `FAILED` | path | Required |
| locationId | string | Filters the results to those executed by specified Synthetic location. Specify the ID of the location. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [MonitorExecutionResults](#openapi-definition-MonitorExecutionResults) | Success. The response contains detailed data. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `MonitorExecutionResults` object

Results of the execution of all HTTP monitor's requests.

| Element | Type | Description |
| --- | --- | --- |
| locationsExecutionResults | [LocationExecutionResults[]](#openapi-definition-LocationExecutionResults) | The list with the results of the requests executed on assigned locations. |
| monitorId | string | Monitor id. |

#### The `LocationExecutionResults` object

Results of the execution HTTP monitor's requests at a given location

| Element | Type | Description |
| --- | --- | --- |
| executionId | string | Execution id. |
| locationId | string | Location id. |
| requestResults | [MonitorRequestExecutionResult[]](#openapi-definition-MonitorRequestExecutionResult) | The list of the monitor's request results executed on this location. |

#### The `MonitorRequestExecutionResult` object

A result of the execution HTTP monitor's request.

#### The `ExecutionStep` object

Contains detailed information about the monitor's step execution.

| Element | Type | Description |
| --- | --- | --- |
| monitorType | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `BROWSER` -> BMAction * `HTTP` -> MonitorRequestExecutionResult The element can hold these values * `BROWSER` * `HTTP` |

#### The `CustomLogLine` object

A custom script log line

| Element | Type | Description |
| --- | --- | --- |
| logLevel | string | Log level of the message |
| message | string | The message |
| timestamp | integer | A timestamp of this log message |

#### The `MonitorRequestHeader` object

A header of the Http request

| Element | Type | Description |
| --- | --- | --- |
| name | string | Header's name. |
| value | string | Header's value. |

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



"locationsExecutionResults": [



{



"executionId": "6136172183050046113",



"locationId": "7804738439930364165",



"requestResults": [



{



"engineId": 338502283,



"errorCode": 0,



"failureMessage": "",



"hostNameResolutionTime": 26,



"method": "GET",



"peerCertificateDetails": "[Certificate details]",



"peerCertificateExpiryDate": 1647302399000,



"publicLocation": false,



"redirectionTime": 70,



"redirectsCount": 1,



"requestBody": "",



"requestHeaders": [



{



"name": "User-Agent",



"value": "DynatraceSynthetic/1.215.1"



},



{



"name": "X-Dynatrace-Visit",



"value": "6136172183050046113"



},



{



"name": "X-Dynatrace-Test",



"value": "HTTP_CHECK-12B428F6D37A9197"



}



],



"requestId": "HTTP_CHECK_STEP-53071FC3C4F72E28",



"requestName": "Request name",



"resolvedIps": [



"80.252.0.145"



],



"responseBody": "<html><head>Title</head><body>Main Page</body></html>",



"responseBodySizeLimitExceeded": false,



"responseHeaders": [



{



"name": "Date",



"value": "Mon, 15 Mar 2021 11:09:30 GMT"



},



{



"name": "Content-Language",



"value": "en"



}



],



"responseMessage": "OK",



"responseSize": 1112,



"responseStatusCode": 200,



"sequenceNumber": 1,



"startTimestamp": 1615806570884,



"tcpConnectTime": 15,



"timeToFirstByte": 96,



"tlsHandshakeTime": 8,



"totalTime": 238,



"url": "https://www.examplePage.com",



"waitingTime": 47



}



]



}



],



"monitorId": "HTTP_CHECK-12B428F6D37A9197"



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

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.")