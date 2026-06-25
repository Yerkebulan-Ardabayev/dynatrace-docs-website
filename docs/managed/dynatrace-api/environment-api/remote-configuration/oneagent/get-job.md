---
title: OneAgent remote configuration management API - GET a configuration job
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/remote-configuration/oneagent/get-job
scraped: 2026-05-12T11:55:13.403753
---

# OneAgent remote configuration management API - GET a configuration job

# OneAgent remote configuration management API - GET a configuration job

* Reference
* Published Oct 06, 2022

Gets parameters of a configuration job for OneAgents.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/oneagents/remoteConfigurationManagement/{id}` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/oneagents/remoteConfigurationManagement/{id}` |

## Authentication

To execute this request, you need an access token with `oneAgents.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the required remote configuration management job. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [RemoteConfigurationManagementJob](#openapi-definition-RemoteConfigurationManagementJob) | Success |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The requested resource doesn't exist. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `RemoteConfigurationManagementJob` object

Remote configuration management job.

| Element | Type | Description |
| --- | --- | --- |
| endTime | string | Date (in ISO 8601 format: yyyy-MM-dd'T'HH:mm:ss.SSS'Z') when the remote configuration management job was finished. This field is present only for finished jobs. |
| entityType | string | Type of entities modified by remote configuration management. The element can hold these values * `ACTIVE_GATE` * `ONE_AGENT` |
| failedEntities | [RemoteIdentityOperationFailedEntityDto[]](#openapi-definition-RemoteIdentityOperationFailedEntityDto) | A list of failed remote configuration management jobs. |
| id | string | The ID of the remote configuration management job. |
| inProgressEntities | string[] | A list of in-progress remote configuration management jobs. |
| operations | [RemoteConfigurationManagementOperation[]](#openapi-definition-RemoteConfigurationManagementOperation) | A list of executed (successful and failed) remote configuration management jobs. |
| processedEntitiesCount | integer | Number of entities that were already processed at the time the response was created. |
| startTime | string | Date (in ISO 8601 format: yyyy-MM-dd'T'HH:mm:ss.SSS'Z') when the remote configuration management job was started. |
| timeoutTime | string | Date (in ISO 8601 format: yyyy-MM-dd'T'HH:mm:ss.SSS'Z') when the running remote configuration management job will time-out. This field is present only for running jobs. |
| totalEntitiesCount | integer | Total number of entities to process. |

#### The `RemoteIdentityOperationFailedEntityDto` object

Failed remote configuration management information.

| Element | Type | Description |
| --- | --- | --- |
| entityId | string | Entity ID for which remote configuration management request was failed |
| failureMessage | string | Communication settings changing failure error description |
| failureReason | string | Reason of communication settings changing failure. The element can hold these values * `CONNECTION_FAILURE` * `TIMEOUT` |

#### The `RemoteConfigurationManagementOperation` object

Definition of a single remote configuration management operation.

| Element | Type | Description |
| --- | --- | --- |
| attribute | string | The attribute which is affected by the operation. The element can hold these values * `group` * `hostGroup` * `hostProperty` * `hostTag` * `networkZone` |
| operation | string | The operation performed on given attribute. The element can hold these values * `clear` * `set` |
| value | string | The value which should be assigned to given attribute. |

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



"endTime": "2020-11-05T08:15:30.144Z",



"entityType": "ACTIVE_GATE or ONE_AGENT",



"failedEntities": [



{



"entityId": "HOST-D454A967666E7970",



"failureMessage": "Failed to access new tenant: f47ac10b-58cc-4372-a567-0e02b2c3d479",



"failureReason": "CONNECTION_FAILURE"



}



],



"id": "7974003406714390819",



"inProgressEntities": [



"HOST-D454A967666E7970"



],



"operations": [



{



"attribute": "networkZone",



"operation": "set",



"value": "exampleNetworkZoneName"



}



],



"processedEntitiesCount": 1,



"startTime": "2020-11-05T08:15:30.144Z",



"timeoutTime": "2020-11-05T08:15:30.144Z",



"totalEntitiesCount": 1



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