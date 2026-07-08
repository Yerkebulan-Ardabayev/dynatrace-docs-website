---
title: Synthetic monitor executions API v2 - POST batch execution
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-monitor-execution/post-batch-execution
---

# Synthetic monitor executions API v2 - POST batch execution

# Synthetic monitor executions API v2 - POST batch execution

* Reference
* Published Jun 27, 2022

Triggers a batch execution of synthetic monitors.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/synthetic/executions/batch` |
| POST | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/synthetic/executions/batch` |

## Authentication

To execute this request, you need an access token with one of the following scopes:

* `syntheticExecutions.write`
* `ExternalSyntheticIntegration`

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [SyntheticOnDemandExecutionRequest](#openapi-definition-SyntheticOnDemandExecutionRequest) | The JSON body of the request. Contains the parameters of the triggered on-demand execution. | body | Required |

### Request body objects

#### The `SyntheticOnDemandExecutionRequest` object

Contains parameters for the on-demand execution of monitors identified by tags, applications, or services.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| failOnPerformanceIssue | boolean | If true, the execution will fail in case of performance issue. | Optional |
| failOnSslWarning | boolean | Applies to HTTP monitors only. If true, the execution will fail in case of an SSL certificate expiration warning or if the certificate is missing. | Optional |
| group | [SyntheticOnDemandExecutionRequestGroup](#openapi-definition-SyntheticOnDemandExecutionRequestGroup) | Contains parameters for the on-demand execution of monitors identified by tags, applications, or services. | Optional |
| metadata | object | String to string map of metadata properties for execution | Optional |
| monitors | [SyntheticOnDemandExecutionRequestMonitor](#openapi-definition-SyntheticOnDemandExecutionRequestMonitor)[] | List of monitors to be triggered. | Optional |
| processingMode | string | The execution's processing mode The element can hold these values * `STANDARD` * `DISABLE_PROBLEM_DETECTION` * `EXECUTIONS_DETAILS_ONLY` | Optional |
| stopOnProblem | boolean | If true, no executions will be scheduled if a problem occurs. | Optional |
| takeScreenshotsOnSuccess | boolean | If true, the screenshots will be taken during the execution of a browser monitor. | Optional |

#### The `SyntheticOnDemandExecutionRequestGroup` object

Contains parameters for the on-demand execution of monitors identified by tags, applications, or services.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| applications | string[] | List of application identifiers. Only monitors with all applications assigned will be executed. | Optional |
| locations | string[] | The locations from where monitors are to be executed. | Optional |
| services | string[] | List of service identifiers. Only monitors with all services assigned will be executed. | Optional |
| tags | string[] | List of tags. Only monitors with all tags assigned will be executed. | Optional |

#### The `SyntheticOnDemandExecutionRequestMonitor` object

Contains monitors to be executed on demand from the locations specified.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| customizedScript | object | Customized script properties for this on-demand batch execution. | Optional |
| executionCount | integer | The number of times the monitor is to be executed per location; if not set, the monitor will be executed once. | Optional |
| locations | string[] | The locations from where the monitor is to be executed. | Optional |
| monitorId | string | The monitor identifier. | Required |
| repeatMode | string | Execution repeat mode. If not set, the mode is SEQUENTIAL. The element can hold these values * `SEQUENTIAL` * `PARALLEL` | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"failOnPerformanceIssue": false,



"failOnSslWarning": true,



"group": {



"applications": [



"APPLICATION-CD4BEF05FA9DD044"



],



"services": [



"SERVICE-01C6C1282960638B",



"SERVICE-B18840B4E3115C1A"



],



"tags": [



"tag-production",



"another-tag"



]



},



"metadata": {



"key": "value",



"version": "1.255.20221022"



},



"monitors": [



{



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



"executionCount": 3,



"locations": [



"SYNTHETIC_LOCATION-9BB04DAEBA71B8CA",



"SYNTHETIC_LOCATION-ACCA399FAA1194DD"



],



"monitorId": "HTTP_CHECK-6349B98E1CD87352",



"repeatMode": "SEQUENTIAL"



}



],



"processingMode": "EXECUTIONS_DETAILS_ONLY",



"stopOnProblem": true,



"takeScreenshotsOnSuccess": true



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [SyntheticOnDemandExecutionResult](#openapi-definition-SyntheticOnDemandExecutionResult) | Success. The monitor's execution response details |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **503** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Unavailable |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `SyntheticOnDemandExecutionResult` object

The result of on-demand synthetic monitor execution.

| Element | Type | Description |
| --- | --- | --- |
| batchId | string | The batch identifier of the triggered executions. |
| triggered | [SyntheticOnDemandTriggeredMonitor](#openapi-definition-SyntheticOnDemandTriggeredMonitor)[] | Monitors for which on-demand executions were triggered. |
| triggeredCount | integer | The total number of the triggered executions within the batch. |
| triggeringProblemsCount | integer | The total number of problems within the batch. |
| triggeringProblemsDetails | [SyntheticOnDemandTriggeringProblemDetails](#openapi-definition-SyntheticOnDemandTriggeringProblemDetails)[] | List with the entities for which triggering problems occurred. |

#### The `SyntheticOnDemandTriggeredMonitor` object

Contains the list of on-demand executions of the monitor.

| Element | Type | Description |
| --- | --- | --- |
| executions | [SyntheticOnDemandTriggeredExecutionDetails](#openapi-definition-SyntheticOnDemandTriggeredExecutionDetails)[] | The list of triggered executions. |
| monitorId | string | The monitor identifier. |

#### The `SyntheticOnDemandTriggeredExecutionDetails` object

Contains details of the triggered on-demand execution.

| Element | Type | Description |
| --- | --- | --- |
| executionId | string | The execution's identifier. |
| locationId | string | The identifier of the location from which the monitor is to be executed. |

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



"triggered": [



{



"executions": [



{



"executionId": "1069999568093682590",



"locationId": "SYNTHETIC_LOCATION-9BB04DAE11123122"



}



],



"monitorId": "HTTP_CHECK-69A9B98E1CD87352"



}



],



"triggeredCount": 1,



"triggeringProblemsCount": 4,



"triggeringProblemsDetails": [



{



"cause": "Location not found",



"entityId": "HTTP_CHECK-6349B98E1CD87352",



"locationId": "SYNTHETIC_LOCAT-9BB04DAEBA71B8CA"



},



{



"cause": "Monitor not found",



"entityId": "HTTP_CHECK-6349B98E1CD85432"



},



{



"cause": "Incorrect monitor identifier format",



"entityId": "HTTP_HACK-AAAAAAA"



},



{



"cause": "Incorrect application identifier format",



"entityId": "APPLICATION-WRONG"



}



]



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