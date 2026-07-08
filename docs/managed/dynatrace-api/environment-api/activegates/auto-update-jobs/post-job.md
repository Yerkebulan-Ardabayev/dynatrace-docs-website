---
title: ActiveGate API - POST an auto-update job
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/activegates/auto-update-jobs/post-job
---

# ActiveGate API - POST an auto-update job

# ActiveGate API - POST an auto-update job

* Reference
* Published Jul 02, 2020

Creates a new auto-update job on the specified ActiveGate.

The job updates the ActiveGate to the specified version. You can fetch the list of available versions with the [GET available versions of ActiveGate](/managed/dynatrace-api/environment-api/deployment/activegate/get-activegate-versions "List available versions of ActiveGate via Dynatrace API.") call.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/activeGates/{agId}/updateJobs` |
| POST | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/activeGates/{agId}/updateJobs` |

## Authentication

To execute this request, you need an access token with `activeGates.write` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| agId | string | The ID of the required ActiveGate. | path | Required |
| body | [UpdateJob](#openapi-definition-UpdateJob) | JSON body of the request, containing update-job parameters. | body | Required |

### Request body objects

#### The `UpdateJob` object

Configuration of the ActiveGate update job.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| agType | string | The type of the ActiveGate. The element can hold these values * `CLUSTER` * `ENVIRONMENT` * `ENVIRONMENT_MULTI` | Optional |
| cancelable | boolean | The job can (`true`) or can't (`false`) be cancelled at the moment. | Optional |
| duration | integer | The duration of the update, in milliseconds. | Optional |
| environments | string[] | A list of environments (specified by IDs) the ActiveGate can connect to. | Optional |
| error | string | The information about update error. | Optional |
| jobId | string | The ID of the update job. | Optional |
| jobState | string | The status of the update job. The element can hold these values * `FAILED` * `IN_PROGRESS` * `PENDING` * `ROLLBACK` * `SCHEDULED` * `SKIPPED` * `SUCCEED` | Optional |
| startVersion | string | The initial version of the ActiveGate. | Optional |
| targetVersion | string | The target version of the update.  Specify the version in the `<major>.<minor>.<revision>.<timestamp>` format.  To update to the latest available version, use the `latest` value. | Required |
| timestamp | integer | The timestamp of the update job completion.  The `null` value means the job is still running. | Optional |
| updateMethod | string | The method of updating the ActiveGate or its component. The element can hold these values * `AUTOMATIC` * `MANUAL_INSTALLATION` * `ON_DEMAND` | Optional |
| updateType | string | The component to be updated. The element can hold these values * `ACTIVE_GATE` * `REMOTE_PLUGIN_AGENT` * `SYNTHETIC` * `Z_REMOTE` | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"agType": "ENVIRONMENT",



"cancelable": false,



"duration": 3608000,



"environments": [



"string"



],



"error": "string",



"jobId": "-3524498778810258605",



"jobState": "SUCCEED",



"startVersion": "1.185.0.20200201-120000",



"targetVersion": "1.190.0.20200301-130000",



"timestamp": 1582031917814,



"updateMethod": "AUTOMATIC",



"updateType": "ACTIVE_GATE"



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [UpdateJob](#openapi-definition-UpdateJob) | Success. The update-job have been created. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `UpdateJob` object

Configuration of the ActiveGate update job.

| Element | Type | Description |
| --- | --- | --- |
| agType | string | The type of the ActiveGate. The element can hold these values * `CLUSTER` * `ENVIRONMENT` * `ENVIRONMENT_MULTI` |
| cancelable | boolean | The job can (`true`) or can't (`false`) be cancelled at the moment. |
| duration | integer | The duration of the update, in milliseconds. |
| environments | string[] | A list of environments (specified by IDs) the ActiveGate can connect to. |
| error | string | The information about update error. |
| jobId | string | The ID of the update job. |
| jobState | string | The status of the update job. The element can hold these values * `FAILED` * `IN_PROGRESS` * `PENDING` * `ROLLBACK` * `SCHEDULED` * `SKIPPED` * `SUCCEED` |
| startVersion | string | The initial version of the ActiveGate. |
| targetVersion | string | The target version of the update.  Specify the version in the `<major>.<minor>.<revision>.<timestamp>` format.  To update to the latest available version, use the `latest` value. |
| timestamp | integer | The timestamp of the update job completion.  The `null` value means the job is still running. |
| updateMethod | string | The method of updating the ActiveGate or its component. The element can hold these values * `AUTOMATIC` * `MANUAL_INSTALLATION` * `ON_DEMAND` |
| updateType | string | The component to be updated. The element can hold these values * `ACTIVE_GATE` * `REMOTE_PLUGIN_AGENT` * `SYNTHETIC` * `Z_REMOTE` |

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



"agType": "ENVIRONMENT",



"cancelable": false,



"duration": 3608000,



"environments": [



"string"



],



"error": "string",



"jobId": "-3524498778810258605",



"jobState": "SUCCEED",



"startVersion": "1.185.0.20200201-120000",



"targetVersion": "1.190.0.20200301-130000",



"timestamp": 1582031917814,



"updateMethod": "AUTOMATIC",



"updateType": "ACTIVE_GATE"



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

## Validate payload

We recommend that you validate the payload before submitting it with an actual request. A response code of **204** indicates a valid payload.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/activeGates/{agId}/updateJobs/validator` |
| POST | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/activeGates/{agId}/updateJobs/validator` |

### Authentication

To execute this request, you need an access token with `activeGates.write` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Response

#### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Validated. The submitted update-job is valid. Response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

#### Response body objects

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

#### Response body JSON models

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

In this example, the request creates an update job to update the ActiveGate with the ID of **1812885988** to the **1.198.0.20200630-163221** version.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -L -X POST 'https://mySampleEnv.live.dynatrace.com/api/v2/activeGates/1812885988/updateJobs' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



--data-raw '{



"targetVersion": "1.198.0.20200630-163221"



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/activeGates/1812885988/updateJobs
```

#### Request body

```
{



"targetVersion": "1.198.0.20200630-163221"



}
```

#### Response body

```
{



"jobId": "-7240069678607892845",



"jobState": "PENDING",



"updateMethod": null,



"updateType": null,



"cancelable": true,



"startVersion": "1.195.5.20200522-174041",



"targetVersion": "1.198.0.20200630-163221",



"timestamp": null,



"agType": "ENVIRONMENT",



"environments": [



"mySampleEnv"



],



"error": null,



"duration": null



}
```

#### Response code

201

## Related topics

* [Dynatrace ActiveGate](/managed/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.")