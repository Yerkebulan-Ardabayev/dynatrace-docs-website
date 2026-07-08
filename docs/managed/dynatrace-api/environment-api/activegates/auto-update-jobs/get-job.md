---
title: ActiveGate API - GET an auto-update job
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/activegates/auto-update-jobs/get-job
---

# ActiveGate API - GET an auto-update job

# ActiveGate API - GET an auto-update job

* Reference
* Published Jul 02, 2020

Gets the parameters of the specified ActiveGate auto-update job.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/activeGates/{agId}/updateJobs/{jobId}` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/activeGates/{agId}/updateJobs/{jobId}` |

## Authentication

To execute this request, you need an access token with `activeGates.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| agId | string | The ID of the required ActiveGate. | path | Required |
| jobId | string | A unique identifier for a update-job of ActiveGate. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [UpdateJob](#openapi-definition-UpdateJob) | Success |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Not found. See response body for details. |
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

## Example

In this example, the request lists the parameters of the auto-update job with the ID of **-7537034309286328684** from the ActiveGate with the ID of **2131628184**.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/activeGates/2131628184/updateJobs/-7537034309286328684' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/activeGates/2131628184/updateJobs/-7537034309286328684
```

#### Response body

```
{



"jobId": "-7537034309286328684",



"jobState": "SUCCEED",



"updateMethod": "AUTOMATIC",



"updateType": "SYNTHETIC",



"cancelable": false,



"startVersion": "1.198.0.20200629-183024",



"targetVersion": "1.198.0.20200630-114457",



"timestamp": 1593518788274,



"agType": "ENVIRONMENT",



"environments": [



"mySampleEnv"



],



"error": null,



"duration": 596047



}
```

#### Response code

200

## Related topics

* [Dynatrace ActiveGate](/managed/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.")