---
title: OneAgent remote configuration management API - POST a target change
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/remote-configuration/oneagent/execute-migration
scraped: 2026-05-12T11:55:09.331450
---

# OneAgent remote configuration management API - POST a target change

# OneAgent remote configuration management API - POST a target change

* Reference
* Published Aug 05, 2025

The cluster version of the target environment must be newer than or equal to the OneAgent version.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/oneagents/managedRemoteCommunicationSettings/execute` |
| POST | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/oneagents/managedRemoteCommunicationSettings/execute` |

## Authentication

To execute this request, you need an access token with `oneAgents.write` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

You identify your OneAgents by their IDs. Use the [OneAgent on a host](/managed/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Check the configuration of OneAgent instances on your hosts via Dynatrace API.") request to learn the IDs of OneAgents that you'd like to configure.

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| restart | boolean | One Agents will be restarted (`true`) or not (`false`) after configuration. By default OneAgents will be restarted when network zone, host group, host tags or host properties are reconfigured - the restart is required to apply the changes. | query | Optional |
| body | [RemoteConfigurationManagementOperationOneAgentRequest](#openapi-definition-RemoteConfigurationManagementOperationOneAgentRequest) | JSON body of the request, containing remote configuration management job definition. | body | Required |

### Request body objects

#### The `RemoteConfigurationManagementOperationOneAgentRequest` object

Remote configuration management operation creation request.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| entities | string[] | A list of entities IDs for which remote configuration management is to be executed. | Required |
| operations | [RemoteConfigurationManagementOperation[]](#openapi-definition-RemoteConfigurationManagementOperation) | A list of remote configuration management operations to be executed. | Required |

#### The `RemoteConfigurationManagementOperation` object

Definition of a single remote configuration management operation.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| attribute | string | The attribute which is affected by the operation. The element can hold these values * `group` * `hostGroup` * `hostProperty` * `hostTag` * `networkZone` | Required |
| operation | string | The operation performed on given attribute. The element can hold these values * `clear` * `set` | Required |
| value | string | The value which should be assigned to given attribute. | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"entities": [



"HOST-D454A967666E7970",



"HOST-811760CFF2A5E872"



],



"operations": [



{



"attribute": "networkZone",



"operation": "set",



"value": "exampleNetworkZoneName"



}



]



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [RemoteConfigurationManagementJob](#openapi-definition-RemoteConfigurationManagementJob) | Created |
| **400** | [RemoteConfigurationManagementValidationResult](#openapi-definition-RemoteConfigurationManagementValidationResult) | Failed. The input is invalid. |
| **409** | - | Other remote configuration management job is currently being executed |
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

#### The `RemoteConfigurationManagementValidationResult` object

The result of remote configuration management validation.

| Element | Type | Description |
| --- | --- | --- |
| invalidEntities | [RemoteConfigurationManagementEntityValidationError[]](#openapi-definition-RemoteConfigurationManagementEntityValidationError) | A list of validation errors for entities. |
| invalidOperations | [RemoteConfigurationManagementOperationValidationError[]](#openapi-definition-RemoteConfigurationManagementOperationValidationError) | A list of validation errors for operations. |

#### The `RemoteConfigurationManagementEntityValidationError` object

Entity validation error for remote configuration management.

| Element | Type | Description |
| --- | --- | --- |
| entity | string | The ID of the entity for which validation failed. |
| reasons | string[] | The reason of entity validation failure. The element can hold these values * `CLOUD_NATIVE_NOT_SUPPORTED` * `NOT_ALLOWED_WITH_CLUSTER_ACTIVE_GATE` * `NOT_CONNECTED` * `RUNNING_IN_CONTAINER` * `STANDALONE_NOT_SUPPORTED` * `VERSION_NOT_SUPPORTED` |

#### The `RemoteConfigurationManagementOperationValidationError` object

Validation error of remote configuration management operation definition.

| Element | Type | Description |
| --- | --- | --- |
| attribute | string | The attribute which is affected by the operation. The element can hold these values * `group` * `hostGroup` * `hostProperty` * `hostTag` * `networkZone` |
| operation | string | The operation performed on given attribute. The element can hold these values * `clear` * `set` |
| reason | string | The reason of validation failure. |
| value | string | The value which should be assigned to given attribute. |

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



"invalidEntities": [



{



"entity": "entityId",



"reasons": [



"RUNNING_IN_CONTAINER"



]



}



],



"invalidOperations": [



{



"attribute": "networkZone",



"operation": "set",



"reason": "Value must not start with a period",



"value": ".exampleInvalidNetworkZoneName"



}



]



}
```

The response is not sent to the client until all OneAgents defined in the payload are processed. A OneAgent is considered to be processed when the reconfiguration message is sent to it; the actual reconfiguration is handled independently by the OneAgent.

## Validate payload

We recommend that you validate the payload before submitting it with an actual request. A response code of **204** indicates a valid payload.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/oneagents/remoteConfigurationManagement/validator` |
| POST | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/oneagents/remoteConfigurationManagement/validator` |

### Authentication

To execute this request, you need an access token with `oneAgents.write` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Response

#### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. Response doesn't have a body. |
| **400** | [RemoteConfigurationManagementValidationResult](#openapi-definition-RemoteConfigurationManagementValidationResult) | Failed. The input is invalid. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

#### Response body objects

#### The `RemoteConfigurationManagementValidationResult` object

The result of remote configuration management validation.

| Element | Type | Description |
| --- | --- | --- |
| invalidEntities | [RemoteConfigurationManagementEntityValidationError[]](#openapi-definition-RemoteConfigurationManagementEntityValidationError) | A list of validation errors for entities. |
| invalidOperations | [RemoteConfigurationManagementOperationValidationError[]](#openapi-definition-RemoteConfigurationManagementOperationValidationError) | A list of validation errors for operations. |

#### The `RemoteConfigurationManagementEntityValidationError` object

Entity validation error for remote configuration management.

| Element | Type | Description |
| --- | --- | --- |
| entity | string | The ID of the entity for which validation failed. |
| reasons | string[] | The reason of entity validation failure. The element can hold these values * `CLOUD_NATIVE_NOT_SUPPORTED` * `NOT_ALLOWED_WITH_CLUSTER_ACTIVE_GATE` * `NOT_CONNECTED` * `RUNNING_IN_CONTAINER` * `STANDALONE_NOT_SUPPORTED` * `VERSION_NOT_SUPPORTED` |

#### The `RemoteConfigurationManagementOperationValidationError` object

Validation error of remote configuration management operation definition.

| Element | Type | Description |
| --- | --- | --- |
| attribute | string | The attribute which is affected by the operation. The element can hold these values * `group` * `hostGroup` * `hostProperty` * `hostTag` * `networkZone` |
| operation | string | The operation performed on given attribute. The element can hold these values * `clear` * `set` |
| reason | string | The reason of validation failure. |
| value | string | The value which should be assigned to given attribute. |

#### Response body JSON models

```
{



"invalidEntities": [



{



"entity": "entityId",



"reasons": [



"RUNNING_IN_CONTAINER"



]



}



],



"invalidOperations": [



{



"attribute": "networkZone",



"operation": "set",



"reason": "Value must not start with a period",



"value": ".exampleInvalidNetworkZoneName"



}



]



}
```