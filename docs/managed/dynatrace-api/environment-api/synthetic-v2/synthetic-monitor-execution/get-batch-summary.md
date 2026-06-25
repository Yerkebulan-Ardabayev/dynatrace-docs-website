---
title: Synthetic monitor executions API v2 - GET summary of a batch execution
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-monitor-execution/get-batch-summary
scraped: 2026-05-12T11:57:45.502000
---

# Synthetic monitor executions API v2 - GET summary of a batch execution

# Synthetic monitor executions API v2 - GET summary of a batch execution

* Reference
* Published Jun 27, 2022

Gets the summary of a batch execution of synthetic monitors.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/synthetic/executions/batch/{batchId}` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/synthetic/executions/batch/{batchId}` |

## Authentication

To execute this request, you need an access token with one of the following scopes:

* `syntheticExecutions.read`
* `ExternalSyntheticIntegration`
* `ReadSyntheticData`

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| batchId | integer | The batch identifier of the executions. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [SyntheticOnDemandBatchStatus](#openapi-definition-SyntheticOnDemandBatchStatus) | Success |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Batch with the given ID doesn't exist. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `SyntheticOnDemandBatchStatus` object

Contains information about on-demand executions triggered within the batch.

| Element | Type | Description |
| --- | --- | --- |
| batchId | string | The identifier of the batch. |
| batchStatus | string | The status of the batch. The element can hold these values * `FAILED` * `FAILED_TO_EXECUTE` * `NOT_TRIGGERED` * `RUNNING` * `SUCCESS` |
| executedCount | integer | The number of triggered executions with the result SUCCESS or FAILED. |
| failedCount | integer | The number of triggered executions with the result FAILED. |
| failedExecutions | [SyntheticOnDemandFailedExecutionStatus[]](#openapi-definition-SyntheticOnDemandFailedExecutionStatus) | - |
| failedToExecute | [SyntheticOnDemandFailedExecutionStatus[]](#openapi-definition-SyntheticOnDemandFailedExecutionStatus) | - |
| failedToExecuteCount | integer | The number of executions that were triggered and timed out because of a problem with the Synthetic engine. |
| metadata | object | String to string map of metadata properties for batch |
| triggeredCount | integer | The number of triggered executions within the batch. |
| triggeringProblems | [SyntheticOnDemandTriggeringProblemDetails[]](#openapi-definition-SyntheticOnDemandTriggeringProblemDetails) | - |
| triggeringProblemsCount | integer | The number of executions that were not triggered due to some problems. |
| userId | string | The name of the user who triggered execution of the batch. |

#### The `SyntheticOnDemandFailedExecutionStatus` object

Contains information about on-demand executions that failed or failed to be executed.

| Element | Type | Description |
| --- | --- | --- |
| errorCode | string | Error code. |
| executionId | string | The identifier of the execution. |
| executionStage | string | Execution stage. The element can hold these values * `DATA_RETRIEVED` * `EXECUTED` * `NOT_TRIGGERED` * `TIMED_OUT` * `TRIGGERED` * `WAITING` |
| executionTimestamp | integer | The timestamp when execution was finished, in UTC milliseconds. |
| failureMessage | string | Failure message. |
| locationId | string | The identifier of the location from where the monitor is to be executed. |
| monitorId | string | The identifier of the monitor. |

#### The `SyntheticOnDemandTriggeringProblemDetails` object

Contains the details of problems encountered while triggering on-demand executions.

| Element | Type | Description |
| --- | --- | --- |
| cause | string | The cause of not triggering entity. |
| details | string | The details of triggering problem. |
| entityId | string | The entity identifier. |
| executionId | string | The execution identifier. |
| locationId | string | The location identifier. |

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



"batchId": "22396514015719218",



"batchStatus": "FAILED_TO_EXECUTE",



"executedCount": 1,



"failedCount": 1,



"failedExecutions": [



{



"errorCode": "CONSTRAINT_VIOLATED(3)",



"executionId": "1629891693487",



"executionStage": "EXECUTED",



"executionTimestamp": "1629891695487",



"failureMessage": "Validate text match failed",



"locationId": "SYNTHETIC_LOCATION-9BB04DAEBA71B8CA",



"monitorId": "HTTP_CHECK-6349B98E1CD87352"



}



],



"failedToExecute": [



{



"executionId": "478437504",



"executionStage": "TIMED_OUT",



"locationId": "SYNTHETIC_LOCATION-90380DA8A44C74BD",



"monitorId": "SYNTHETIC_TEST-027011D7D27CC892"



}



],



"failedToExecuteCount": 1,



"metadata": {



"key": "value",



"version": "1.255.20221022"



},



"triggeredCount": 3,



"triggeringProblems": [



{



"cause": "Location not found",



"entityId": "HTTP_CHECK-6349B98E1CD87352",



"locationId": "SYNTHETIC_LOCAT-9BB04DAEBA71B8CA"



},



{



"cause": "Incorrect application identifier format",



"entityId": "APPLICATION-WRONG"



}



],



"triggeringProblemsCount": 2,



"userId": "admin"



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