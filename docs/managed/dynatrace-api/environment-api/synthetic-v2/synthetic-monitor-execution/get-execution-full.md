---
title: Synthetic monitor executions API v2 - GET full info on an execution
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-monitor-execution/get-execution-full
---

# Synthetic monitor executions API v2 - GET full info on an execution

# Synthetic monitor executions API v2 - GET full info on an execution

* Reference
* Published Jun 27, 2022

Gets full results of an on-demand execution of a synthetic monitor.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/synthetic/executions/{executionId}/fullReport` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/synthetic/executions/{executionId}/fullReport` |

## Authentication

To execute this request, you need an access token with one of the following scopes:

* `syntheticExecutions.read`
* `ExternalSyntheticIntegration`
* `ReadSyntheticData`

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| executionId | integer | The identifier of the on-demand execution. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [SyntheticOnDemandExecution](#openapi-definition-SyntheticOnDemandExecution) | Success. The response contains detailed information about the on-demand execution. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Execution with the given ID doesn't exist. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `SyntheticOnDemandExecution` object

Describes the status of an on-demand execution.

| Element | Type | Description |
| --- | --- | --- |
| batchId | string | The identifier of the batch. |
| customizedScript | [ObjectNode](#openapi-definition-ObjectNode) | Customized script properties for this on-demand batch execution. |
| dataDeliveryTimestamp | integer | The timestamp when whole data set has been collected on server, in UTC milliseconds. |
| executionId | string | The identifier of the execution. |
| executionStage | string | Execution stage. The element can hold these values * `DATA_RETRIEVED` * `EXECUTED` * `NOT_TRIGGERED` * `TIMED_OUT` * `TRIGGERED` * `WAITING` |
| executionTimestamp | integer | The timestamp when execution was finished, in UTC milliseconds. |
| fullResults | [ExecutionFullResults](#openapi-definition-ExecutionFullResults) | Contains extended monitor's execution details. |
| locationId | string | The identifier of the location from where the monitor is to be executed. |
| metadata | object | Metadata map for the execution batch. |
| monitorId | string | The identifier of the monitor. |
| nextExecutionId | string | Next execution id for sequential mode. |
| processingMode | string | The processing mode of the execution. The element can hold these values * `DISABLE_PROBLEM_DETECTION` * `EXECUTIONS_DETAILS_ONLY` * `NONE` * `STANDARD` * `UNKNOWN` |
| schedulingTimestamp | integer | The scheduling timestamp, in UTC milliseconds. |
| simpleResults | [ExecutionSimpleResults](#openapi-definition-ExecutionSimpleResults) | Contains basic results of the monitor's on-demand execution. |
| source | string | The source of the triggering request. The element can hold these values * `API` * `UI` |
| userId | string | The name of the user who triggered the on-demand execution. |

#### The `ObjectNode` object

Customized script properties for this on-demand batch execution.

#### The `ExecutionFullResults` object

Contains extended monitor's execution details.

| Element | Type | Description |
| --- | --- | --- |
| errorCode | string | Error code. |
| executionStepCount | integer | Number executed steps. |
| executionSteps | [ExecutionStep](#openapi-definition-ExecutionStep)[] | Details about the monitor's step execution. |
| failedStepName | string | Failed step name. |
| failedStepSequenceId | integer | Failed step sequence id. |
| failureMessage | string | Failure message. |
| status | string | Execution status. |

#### The `ExecutionStep` object

Contains detailed information about the monitor's step execution.

| Element | Type | Description |
| --- | --- | --- |
| monitorType | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `BROWSER` -> BMAction * `HTTP` -> MonitorRequestExecutionResult The element can hold these values * `BROWSER` * `HTTP` |

#### The `ExecutionSimpleResults` object

Contains basic results of the monitor's on-demand execution.

| Element | Type | Description |
| --- | --- | --- |
| chromeError | boolean | Informs whether is Chrome error. |
| engineId | integer | Synthetic engine id on which monitor was executed. |
| errorCode | string | Error code. |
| executedSteps | integer | Number of the executed steps by Synthetic engine |
| failureMessage | string | Failure message. |
| hostNameResolutionTime | integer | A hostname resolution time measured in milliseconds. |
| httperror | boolean | Informs whether is HTTP error. |
| ~~peerCertificateExpiryDate~~ | integer | DEPRECATED  An expiry date of the first SSL certificate from the certificate chain. |
| publicLocation | boolean | Flag informs whether request was executed on public location. |
| redirectionTime | integer | Total number of milliseconds spent on handling all redirect requests, measured in milliseconds. |
| redirectsCount | integer | Number of redirects. |
| responseBodySizeLimitExceeded | boolean | A flag indicating that the response payload size limit of 10MB has been exceeded. |
| responseSize | integer | Request's response size in bytes. |
| responseStatusCode | integer | Response status code. |
| startTimestamp | integer | Start timestamp. |
| status | string | Execution status. |
| tcpConnectTime | integer | A TCP connect time measured in milliseconds. |
| timeToFirstByte | integer | A time to first byte measured in milliseconds. |
| tlsHandshakeTime | integer | A TLS handshake time measured in milliseconds. |
| totalTime | integer | A total time measured in milliseconds. |

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



"batchId": "22396514015719218",



"customizedScript": {



"requests": [



{



"sequenceId": "1",



"url": "https://www.somepage.org",



"validation": {



"rules": [



{



"passIfFound": "true",



"type": "httpStatusesList",



"value": "=201"



}



]



}



}



]



},



"dataDeliveryTimestamp": "1629891701171",



"executionId": "7002396514015719218",



"executionStage": "DATA_RETRIEVED",



"executionTimestamp": "1629891695487",



"locationId": "SYNTHETIC_LOCATION-9BB04DAEBA71B8CA",



"metadata": {



"key": "value",



"version": "1.255.20221022"



},



"monitorId": "HTTP_CHECK-6349B98E1CD87352",



"processingMode": "STANDARD",



"schedulingTime": "1629891686877",



"simpleResults": [



{



"engineId": "1993198092",



"executedSteps": "1",



"healthStatus": "HEALTHY",



"hostNameResolutionTime": "50",



"publicLocation": "false",



"redirectionTime": "576",



"responseBodySizeLimitExceeded": "false",



"responseSize": "1530652",



"responseStatusCode": "200",



"startTimestamp": "1629891693487",



"tcpConnectTime": "127",



"tlsHandshakeTime": "167",



"totalTime": "955"



}



],



"source": "API",



"userId": "someUserIdentifier"



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