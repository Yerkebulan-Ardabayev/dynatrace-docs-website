---
title: OneAgent remote configuration management API - POST a job preview
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/remote-configuration/oneagent/post-job-preview
---

# OneAgent remote configuration management API - POST a job preview

# OneAgent remote configuration management API - POST a job preview

* Reference
* Updated on Jul 29, 2025

You can generate a preview before performing the actual configuration change.

The preview tells you:

* How many entities are currently configured as described in the payload
* How many entities will be configured this way when the reconfiguration request is sent

The preview is not supported for tags and properties.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/oneagents/remoteConfigurationManagement/preview` |
| POST | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/oneagents/remoteConfigurationManagement/preview` |

## Authentication

To execute this request, you need an access token with `oneAgents.write` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [RemoteConfigurationManagementOperationOneAgentRequest](#openapi-definition-RemoteConfigurationManagementOperationOneAgentRequest) | JSON body of the request, containing remote configuration management job definition. | body | Required |

### Request body objects

#### The `RemoteConfigurationManagementOperationOneAgentRequest` object

Remote configuration management operation creation request.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| entities | string[] | A list of entities IDs for which remote configuration management is to be executed. | Required |
| operations | [RemoteConfigurationManagementOperation](#openapi-definition-RemoteConfigurationManagementOperation)[] | A list of remote configuration management operations to be executed. | Required |

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
| **200** | [RemoteConfigurationManagementPreviewList](#openapi-definition-RemoteConfigurationManagementPreviewList) | Success |
| **400** | [RemoteConfigurationManagementValidationResult](#openapi-definition-RemoteConfigurationManagementValidationResult) | Failed. The input is invalid. |
| **422** | - | Endpoint was executed for not supported operation type |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `RemoteConfigurationManagementPreviewList` object

A list of remote configuration management jobs previews.

| Element | Type | Description |
| --- | --- | --- |
| previews | [RemoteConfigurationManagementJobPreview](#openapi-definition-RemoteConfigurationManagementJobPreview)[] | A list of remote configuration management jobs previews. |

#### The `RemoteConfigurationManagementJobPreview` object

A preview of remote configuration management job.

| Element | Type | Description |
| --- | --- | --- |
| alreadyConfiguredEntitiesCount | integer | The number of entities that are currently configured as defined by remote configuration management operation. |
| attribute | string | The attribute which is affected by the operation. The element can hold these values * `group` * `hostGroup` * `hostProperty` * `hostTag` * `networkZone` |
| operation | string | The operation performed on given attribute. The element can hold these values * `clear` * `set` |
| targetEntitiesCount | integer | The number of entities that will be configured as defined by remote configuration management after it is completed. |
| value | string | The value which should be assigned to given attribute. |

#### The `RemoteConfigurationManagementValidationResult` object

The result of remote configuration management validation.

| Element | Type | Description |
| --- | --- | --- |
| invalidEntities | [RemoteConfigurationManagementEntityValidationError](#openapi-definition-RemoteConfigurationManagementEntityValidationError)[] | A list of validation errors for entities. |
| invalidOperations | [RemoteConfigurationManagementOperationValidationError](#openapi-definition-RemoteConfigurationManagementOperationValidationError)[] | A list of validation errors for operations. |

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



"previews": [



{



"alreadyConfiguredEntitiesCount": 1,



"attribute": "networkZone",



"operation": "set",



"targetEntitiesCount": 2,



"value": "exampleNetworkZoneName"



}



]



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