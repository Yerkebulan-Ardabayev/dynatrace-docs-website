---
title: Management zones API - POST a management zone
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/management-zones-api/post-mz
---

# Management zones API - POST a management zone

# Management zones API - POST a management zone

* Reference
* Published Sep 02, 2019

Deprecated

This API is deprecated. Use the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") with the [Management zones settings](/managed/dynatrace-api/environment-api/settings/schemas/builtin-management-zones "View builtin:management-zones settings schema table of your monitoring environment via the Dynatrace API.") (`builtin:management-zones`) schema instead.

Creates a new management zone.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/managementZones` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/managementZones` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

To find all JSON models that depend on the type of the model, refer to [JSON models](/managed/dynatrace-api/configuration-api/management-zones-api/json-models "Learn the variations of models in the Management zones API.").

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [ManagementZone](#openapi-definition-ManagementZone) | The JSON body of the request. Contains parameters of the new management zone. | body | Optional |

### Request body objects

#### The `ManagementZone` object

The configuration of the management zone. It defines how the management zone applies.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| description | string | The description of the management zone. | Optional |
| dimensionalRules | [MzDimensionalRule](#openapi-definition-MzDimensionalRule)[] | A list of dimensional data rules for management zone usage.  If several rules are specified, the **OR** logic applies. | Optional |
| entitySelectorBasedRules | [EntitySelectorBasedMzRule](#openapi-definition-EntitySelectorBasedMzRule)[] | A list of entity-selector based rules for management zone usage.  If several rules are specified, the **OR** logic applies. | Optional |
| id | string | The ID of the management zone. | Optional |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging | Optional |
| name | string | The name of the management zone. | Required |
| rules | [MzRule](#openapi-definition-MzRule)[] | A list of rules for management zone usage.  If several rules are specified, the **OR** logic applies. | Optional |

#### The `MzDimensionalRule` object

The dimensional rule of the management zone usage. It defines how the management zone applies.

Each rule is evaluated independently of all other rules.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| appliesTo | string | The target of the rule. The element can hold these values * `ANY` * `LOG` * `METRIC` | Required |
| conditions | [MzDimensionalRuleCondition](#openapi-definition-MzDimensionalRuleCondition)[] | A list of conditions for the management zone.  The management zone applies only if **all** conditions are fulfilled. | Required |
| enabled | boolean | The rule is enabled (`true`) or disabled (`false`). | Required |

#### The `MzDimensionalRuleCondition` object

A condition of the management zone dimensional rule.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| conditionType | string | The type of the condition. The element can hold these values * `DIMENSION` * `LOG_FILE_NAME` * `METRIC_KEY` | Required |
| key | string | The reference value for comparison.  For conditions of the `DIMENSION` type, specify the key here. | Required |
| ruleMatcher | string | How we compare the values. The element can hold these values * `BEGINS_WITH` * `EQUALS` | Required |
| value | string | The value of the dimension.  Only applicable when the **conditionType** is set to `DIMENSION`. | Optional |

#### The `EntitySelectorBasedMzRule` object

The entity-selector-based rule for management zone usage. It allows adding entities to a management zone via an entity selector.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| enabled | boolean | The rule is enabled (`true`) or disabled (`false`). | Optional |
| entitySelector | string | The entity selector string, by which the entities are selected. | Required |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| clusterVersion | string | Dynatrace version. | Optional |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. | Optional |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. | Optional |

#### The `MzRule` object

The rule of the management zone usage. It defines how the management zone applies.

Each rule is evaluated independently of all other rules.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| conditions | [EntityRuleEngineCondition](#openapi-definition-EntityRuleEngineCondition)[] | A list of matching rules for the management zone.  The management zone applies only if **all** conditions are fulfilled. | Required |
| enabled | boolean | The rule is enabled (`true`) or disabled (`false`). | Required |
| propagationTypes | string[] | How to apply the management zone to underlying entities:  * `SERVICE_TO_HOST_LIKE`: Apply to underlying hosts of matching services. * `SERVICE_TO_PROCESS_GROUP_LIKE`: Apply to underlying process groups of matching services. * `PROCESS_GROUP_TO_HOST`: Apply to underlying hosts of matching process groups. * `PROCESS_GROUP_TO_SERVICE`: Apply to all services provided by matching process groups. * `HOST_TO_PROCESS_GROUP_INSTANCE`: Apply to processes running on matching hosts. * `CUSTOM_DEVICE_GROUP_TO_CUSTOM_DEVICE`: Apply to custom devices in matching custom device groups. * `AZURE_TO_PG`: Apply to process groups connected to matching Azure entities. * `AZURE_TO_SERVICE`: Apply to services provided by matching Azure entities. The element can hold these values * `AZURE_TO_PG` * `AZURE_TO_SERVICE` * `CUSTOM_DEVICE_GROUP_TO_CUSTOM_DEVICE` * `HOST_TO_PROCESS_GROUP_INSTANCE` * `PROCESS_GROUP_TO_HOST` * `PROCESS_GROUP_TO_SERVICE` * `SERVICE_TO_HOST_LIKE` * `SERVICE_TO_PROCESS_GROUP_LIKE` | Optional |
| type | string | The type of Dynatrace entities the management zone can be applied to. The element can hold these values * `APPMON_SERVER` * `APPMON_SYSTEM_PROFILE` * `AWS_ACCOUNT` * `AWS_APPLICATION_LOAD_BALANCER` * `AWS_AUTO_SCALING_GROUP` * `AWS_CLASSIC_LOAD_BALANCER` * `AWS_NETWORK_LOAD_BALANCER` * `AWS_RELATIONAL_DATABASE_SERVICE` * `AZURE` * `BROWSER_MONITOR` * `CLOUD_APPLICATION` * `CLOUD_APPLICATION_NAMESPACE` * `CLOUD_FOUNDRY_FOUNDATION` * `CUSTOM_APPLICATION` * `CUSTOM_DEVICE` * `CUSTOM_DEVICE_GROUP` * `DATA_CENTER_SERVICE` * `ENTERPRISE_APPLICATION` * `ESXI_HOST` * `EXTERNAL_MONITOR` * `HOST` * `HOST_GROUP` * `HTTP_MONITOR` * `KUBERNETES_CLUSTER` * `KUBERNETES_SERVICE` * `MOBILE_APPLICATION` * `MULTIPROTOCOL_MONITOR` * `OPENSTACK_ACCOUNT` * `PROCESS_GROUP` * `QUEUE` * `SERVICE` * `WEB_APPLICATION` | Required |

#### The `EntityRuleEngineCondition` object

A condition defines how to execute matching logic for an entity.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| comparisonInfo | [ComparisonBasic](#openapi-definition-ComparisonBasic) | Defines how the matching is actually performed: what and how are we comparing.  The actual set of fields and possible values of the **operator** field depend on the type of the comparison. Find the list of actual objects in the description of the **type** field or see [JSON models﻿](https://dt-url.net/0b83s6z). | Required |
| key | [ConditionKey](#openapi-definition-ConditionKey) | The key to identify the data we're matching.  The actual set of fields and possible values depend on the type of the key. Find the list of actual objects in the description of the **type** field or see [JSON models﻿](https://dt-url.net/0b83s6z). | Required |

#### The `ComparisonBasic` object

Defines how the matching is actually performed: what and how are we comparing.

The actual set of fields and possible values of the **operator** field depend on the type of the comparison. Find the list of actual objects in the description of the **type** field or see [JSON models﻿](https://dt-url.net/0b83s6z).

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| negate | boolean | Reverses the comparison **operator**. For example it turns the **begins with** into **does not begin with**. | Required |
| operator | string | Operator of the comparison. You can reverse it by setting **negate** to `true`.  Possible values depend on the **type** of the comparison. Find the list of actual models in the description of the **type** field and check the description of the model you need. | Required |
| type | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `STRING` -> StringComparison * `INDEXED_NAME` -> IndexedNameComparison * `INDEXED_STRING` -> IndexedStringComparison * `INTEGER` -> IntegerComparison * `SERVICE_TYPE` -> ServiceTypeComparison * `PAAS_TYPE` -> PaasTypeComparison * `CLOUD_TYPE` -> CloudTypeComparison * `AZURE_SKU` -> AzureSkuComparision * `AZURE_COMPUTE_MODE` -> AzureComputeModeComparison * `ENTITY_ID` -> EntityIdComparison * `SIMPLE_TECH` -> SimpleTechComparison * `SIMPLE_HOST_TECH` -> SimpleHostTechComparison * `SERVICE_TOPOLOGY` -> ServiceTopologyComparison * `DATABASE_TOPOLOGY` -> DatabaseTopologyComparison * `OS_TYPE` -> OsTypeComparison * `HYPERVISOR_TYPE` -> HypervisorTypeComparision * `IP_ADDRESS` -> IpAddressComparison * `OS_ARCHITECTURE` -> OsArchitectureComparison * `BITNESS` -> BitnessComparision * `APPLICATION_TYPE` -> ApplicationTypeComparison * `MOBILE_PLATFORM` -> MobilePlatformComparison * `CUSTOM_APPLICATION_TYPE` -> CustomApplicationTypeComparison * `DCRUM_DECODER_TYPE` -> DcrumDecoderComparison * `SYNTHETIC_ENGINE_TYPE` -> SyntheticEngineTypeComparison * `TAG` -> TagComparison * `INDEXED_TAG` -> IndexedTagComparison The element can hold these values * `APPLICATION_TYPE` * `AZURE_COMPUTE_MODE` * `AZURE_SKU` * `BITNESS` * `CLOUD_TYPE` * `CUSTOM_APPLICATION_TYPE` * `DATABASE_TOPOLOGY` * `DCRUM_DECODER_TYPE` * `ENTITY_ID` * `HYPERVISOR_TYPE` * `INDEXED_NAME` * `INDEXED_STRING` * `INDEXED_TAG` * `INTEGER` * `IP_ADDRESS` * `MOBILE_PLATFORM` * `OS_ARCHITECTURE` * `OS_TYPE` * `PAAS_TYPE` * `SERVICE_TOPOLOGY` * `SERVICE_TYPE` * `SIMPLE_HOST_TECH` * `SIMPLE_TECH` * `STRING` * `SYNTHETIC_ENGINE_TYPE` * `TAG` | Required |
| value | [AnyValue](#openapi-definition-AnyValue) | The value to compare to. | Optional |

#### The `AnyValue` object

A schema representing an arbitrary value type.

#### The `ConditionKey` object

The key to identify the data we're matching.

The actual set of fields and possible values depend on the type of the key. Find the list of actual objects in the description of the **type** field or see [JSON models﻿](https://dt-url.net/0b83s6z).

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| attribute | string | The attribute to be used for comparison. The element can hold these values * `APPMON_SERVER_NAME` * `APPMON_SYSTEM_PROFILE_NAME` * `AWS_ACCOUNT_ID` * `AWS_ACCOUNT_NAME` * `AWS_APPLICATION_LOAD_BALANCER_NAME` * `AWS_APPLICATION_LOAD_BALANCER_TAGS` * `AWS_AUTO_SCALING_GROUP_NAME` * `AWS_AUTO_SCALING_GROUP_TAGS` * `AWS_AVAILABILITY_ZONE_NAME` * `AWS_CLASSIC_LOAD_BALANCER_FRONTEND_PORTS` * `AWS_CLASSIC_LOAD_BALANCER_NAME` * `AWS_CLASSIC_LOAD_BALANCER_TAGS` * `AWS_NETWORK_LOAD_BALANCER_NAME` * `AWS_NETWORK_LOAD_BALANCER_TAGS` * `AWS_RELATIONAL_DATABASE_SERVICE_DB_NAME` * `AWS_RELATIONAL_DATABASE_SERVICE_ENDPOINT` * `AWS_RELATIONAL_DATABASE_SERVICE_ENGINE` * `AWS_RELATIONAL_DATABASE_SERVICE_INSTANCE_CLASS` * `AWS_RELATIONAL_DATABASE_SERVICE_NAME` * `AWS_RELATIONAL_DATABASE_SERVICE_PORT` * `AWS_RELATIONAL_DATABASE_SERVICE_TAGS` * `AZURE_ENTITY_NAME` * `AZURE_ENTITY_TAGS` * `AZURE_MGMT_GROUP_NAME` * `AZURE_MGMT_GROUP_UUID` * `AZURE_REGION_NAME` * `AZURE_SCALE_SET_NAME` * `AZURE_SUBSCRIPTION_NAME` * `AZURE_SUBSCRIPTION_UUID` * `AZURE_TENANT_NAME` * `AZURE_TENANT_UUID` * `AZURE_VM_NAME` * `BROWSER_MONITOR_NAME` * `BROWSER_MONITOR_TAGS` * `CLOUD_APPLICATION_LABELS` * `CLOUD_APPLICATION_NAME` * `CLOUD_APPLICATION_NAMESPACE_LABELS` * `CLOUD_APPLICATION_NAMESPACE_NAME` * `CLOUD_FOUNDRY_FOUNDATION_NAME` * `CLOUD_FOUNDRY_ORG_NAME` * `CUSTOM_APPLICATION_NAME` * `CUSTOM_APPLICATION_PLATFORM` * `CUSTOM_APPLICATION_TAGS` * `CUSTOM_APPLICATION_TYPE` * `CUSTOM_DEVICE_DETECTED_NAME` * `CUSTOM_DEVICE_DNS_ADDRESS` * `CUSTOM_DEVICE_GROUP_NAME` * `CUSTOM_DEVICE_GROUP_TAGS` * `CUSTOM_DEVICE_IP_ADDRESS` * `CUSTOM_DEVICE_METADATA` * `CUSTOM_DEVICE_NAME` * `CUSTOM_DEVICE_PORT` * `CUSTOM_DEVICE_TAGS` * `CUSTOM_DEVICE_TECHNOLOGY` * `DATA_CENTER_SERVICE_DECODER_TYPE` * `DATA_CENTER_SERVICE_IP_ADDRESS` * `DATA_CENTER_SERVICE_METADATA` * `DATA_CENTER_SERVICE_NAME` * `DATA_CENTER_SERVICE_PORT` * `DATA_CENTER_SERVICE_TAGS` * `DOCKER_CONTAINER_NAME` * `DOCKER_FULL_IMAGE_NAME` * `DOCKER_IMAGE_VERSION` * `DOCKER_STRIPPED_IMAGE_NAME` * `EC2_INSTANCE_AMI_ID` * `EC2_INSTANCE_AWS_INSTANCE_TYPE` * `EC2_INSTANCE_AWS_SECURITY_GROUP` * `EC2_INSTANCE_BEANSTALK_ENV_NAME` * `EC2_INSTANCE_ID` * `EC2_INSTANCE_NAME` * `EC2_INSTANCE_PRIVATE_HOST_NAME` * `EC2_INSTANCE_PUBLIC_HOST_NAME` * `EC2_INSTANCE_TAGS` * `ENTERPRISE_APPLICATION_DECODER_TYPE` * `ENTERPRISE_APPLICATION_IP_ADDRESS` * `ENTERPRISE_APPLICATION_METADATA` * `ENTERPRISE_APPLICATION_NAME` * `ENTERPRISE_APPLICATION_PORT` * `ENTERPRISE_APPLICATION_TAGS` * `ESXI_HOST_CLUSTER_NAME` * `ESXI_HOST_HARDWARE_MODEL` * `ESXI_HOST_HARDWARE_VENDOR` * `ESXI_HOST_NAME` * `ESXI_HOST_PRODUCT_NAME` * `ESXI_HOST_PRODUCT_VERSION` * `ESXI_HOST_TAGS` * `EXTERNAL_MONITOR_ENGINE_DESCRIPTION` * `EXTERNAL_MONITOR_ENGINE_NAME` * `EXTERNAL_MONITOR_ENGINE_TYPE` * `EXTERNAL_MONITOR_NAME` * `EXTERNAL_MONITOR_TAGS` * `GEOLOCATION_SITE_NAME` * `GOOGLE_CLOUD_PLATFORM_ZONE_NAME` * `GOOGLE_COMPUTE_INSTANCE_ID` * `GOOGLE_COMPUTE_INSTANCE_MACHINE_TYPE` * `GOOGLE_COMPUTE_INSTANCE_NAME` * `GOOGLE_COMPUTE_INSTANCE_PROJECT` * `GOOGLE_COMPUTE_INSTANCE_PROJECT_ID` * `GOOGLE_COMPUTE_INSTANCE_PUBLIC_IP_ADDRESSES` * `HOST_AIX_LOGICAL_CPU_COUNT` * `HOST_AIX_SIMULTANEOUS_THREADS` * `HOST_AIX_VIRTUAL_CPU_COUNT` * `HOST_ARCHITECTURE` * `HOST_AWS_NAME_TAG` * `HOST_AZURE_COMPUTE_MODE` * `HOST_AZURE_SKU` * `HOST_AZURE_WEB_APPLICATION_HOST_NAMES` * `HOST_AZURE_WEB_APPLICATION_SITE_NAMES` * `HOST_BITNESS` * `HOST_BOSH_AVAILABILITY_ZONE` * `HOST_BOSH_DEPLOYMENT_ID` * `HOST_BOSH_INSTANCE_ID` * `HOST_BOSH_INSTANCE_NAME` * `HOST_BOSH_NAME` * `HOST_BOSH_STEMCELL_VERSION` * `HOST_CLOUD_TYPE` * `HOST_CPU_CORES` * `HOST_CUSTOM_METADATA` * `HOST_DETECTED_NAME` * `HOST_GROUP_ID` * `HOST_GROUP_NAME` * `HOST_HYPERVISOR_TYPE` * `HOST_IP_ADDRESS` * `HOST_KUBERNETES_LABELS` * `HOST_LOGICAL_CPU_CORES` * `HOST_NAME` * `HOST_ONEAGENT_CUSTOM_HOST_NAME` * `HOST_OS_TYPE` * `HOST_OS_VERSION` * `HOST_PAAS_MEMORY_LIMIT` * `HOST_PAAS_TYPE` * `HOST_TAGS` * `HOST_TECHNOLOGY` * `HTTP_MONITOR_NAME` * `HTTP_MONITOR_TAGS` * `KUBERNETES_CLUSTER_NAME` * `KUBERNETES_NODE_NAME` * `KUBERNETES_SERVICE_NAME` * `MOBILE_APPLICATION_NAME` * `MOBILE_APPLICATION_PLATFORM` * `MOBILE_APPLICATION_TAGS` * `NAME_OF_COMPUTE_NODE` * `NETWORK_AVAILABILITY_MONITOR_NAME` * `NETWORK_AVAILABILITY_MONITOR_TAGS` * `OPENSTACK_ACCOUNT_NAME` * `OPENSTACK_ACCOUNT_PROJECT_NAME` * `OPENSTACK_AVAILABILITY_ZONE_NAME` * `OPENSTACK_PROJECT_NAME` * `OPENSTACK_REGION_NAME` * `OPENSTACK_VM_INSTANCE_TYPE` * `OPENSTACK_VM_NAME` * `OPENSTACK_VM_SECURITY_GROUP` * `PROCESS_GROUP_AZURE_HOST_NAME` * `PROCESS_GROUP_AZURE_SITE_NAME` * `PROCESS_GROUP_CUSTOM_METADATA` * `PROCESS_GROUP_DETECTED_NAME` * `PROCESS_GROUP_ID` * `PROCESS_GROUP_LISTEN_PORT` * `PROCESS_GROUP_NAME` * `PROCESS_GROUP_PREDEFINED_METADATA` * `PROCESS_GROUP_TAGS` * `PROCESS_GROUP_TECHNOLOGY` * `PROCESS_GROUP_TECHNOLOGY_EDITION` * `PROCESS_GROUP_TECHNOLOGY_VERSION` * `QUEUE_NAME` * `QUEUE_TECHNOLOGY` * `QUEUE_VENDOR` * `SERVICE_AKKA_ACTOR_SYSTEM` * `SERVICE_CTG_SERVICE_NAME` * `SERVICE_DATABASE_HOST_NAME` * `SERVICE_DATABASE_NAME` * `SERVICE_DATABASE_TOPOLOGY` * `SERVICE_DATABASE_VENDOR` * `SERVICE_DETECTED_NAME` * `SERVICE_ESB_APPLICATION_NAME` * `SERVICE_IBM_CTG_GATEWAY_URL` * `SERVICE_IIB_APPLICATION_NAME` * `SERVICE_MESSAGING_LISTENER_CLASS_NAME` * `SERVICE_NAME` * `SERVICE_PORT` * `SERVICE_PUBLIC_DOMAIN_NAME` * `SERVICE_REMOTE_ENDPOINT` * `SERVICE_REMOTE_SERVICE_NAME` * `SERVICE_TAGS` * `SERVICE_TECHNOLOGY` * `SERVICE_TECHNOLOGY_EDITION` * `SERVICE_TECHNOLOGY_VERSION` * `SERVICE_TOPOLOGY` * `SERVICE_TYPE` * `SERVICE_WEB_APPLICATION_ID` * `SERVICE_WEB_CONTEXT_ROOT` * `SERVICE_WEB_SERVER_ENDPOINT` * `SERVICE_WEB_SERVER_NAME` * `SERVICE_WEB_SERVICE_NAME` * `SERVICE_WEB_SERVICE_NAMESPACE` * `VMWARE_DATACENTER_NAME` * `VMWARE_VM_NAME` * `WEB_APPLICATION_NAME` * `WEB_APPLICATION_NAME_PATTERN` * `WEB_APPLICATION_TAGS` * `WEB_APPLICATION_TYPE` | Required |
| type | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `PROCESS_CUSTOM_METADATA_KEY` -> CustomProcessMetadataConditionKey * `HOST_CUSTOM_METADATA_KEY` -> CustomHostMetadataConditionKey * `PROCESS_PREDEFINED_METADATA_KEY` -> ProcessMetadataConditionKey * `STRING` -> StringConditionKey * `STATIC` -> StaticConditionKey The element can hold these values * `HOST_CUSTOM_METADATA_KEY` * `PROCESS_CUSTOM_METADATA_KEY` * `PROCESS_PREDEFINED_METADATA_KEY` * `STATIC` * `STRING` | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"description": "sampleDescription",



"dimensionalRules": [



{



"appliesTo": "METRIC",



"conditions": [



{



"conditionType": "DIMENSION",



"key": "alwaysRequired",



"ruleMatcher": "EQUALS",



"value": "requiredForDimension_forbiddenForMetricKeyAndLogFileName"



}



],



"enabled": true



}



],



"entitySelectorBasedRules": [



{



"enabled": true,



"entitySelector": "type(HOST) AND cpuCores(4)"



}



],



"name": "sampleManagementZone",



"rules": [



{



"conditions": [



{



"comparisonInfo": {



"caseSensitive": false,



"negate": false,



"operator": "BEGINS_WITH",



"type": "STRING",



"value": "sample"



},



"key": {



"attribute": "SERVICE_DATABASE_NAME"



}



},



{



"comparisonInfo": {



"negate": false,



"operator": "EXISTS",



"type": "STRING"



},



"key": {



"attribute": "SERVICE_WEB_SERVER_NAME"



}



},



{



"comparisonInfo": {



"caseSensitive": false,



"negate": false,



"operator": "BEGINS_WITH",



"type": "STRING",



"value": "sample"



},



"key": {



"attribute": "PROCESS_GROUP_CUSTOM_METADATA",



"dynamicKey": {



"key": "kubernetes.io/limit-ranger",



"source": "KUBERNETES"



},



"type": "PROCESS_CUSTOM_METADATA_KEY"



}



}



],



"enabled": true,



"propagationTypes": [



"SERVICE_TO_HOST_LIKE"



],



"type": "SERVICE"



}



]



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Success. The management zone has been created. The response contains the ID of the new zone. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid |

### Response body objects

#### The `EntityShortRepresentation` object

The short representation of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the Dynatrace entity. |
| id | string | The ID of the Dynatrace entity. |
| name | string | The name of the Dynatrace entity. |

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



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



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
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/managementZones/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/managementZones/validator` |

### Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Response

#### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Validated. The submitted configuration is valid. Response does not have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid |

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

In this example, the request creates a new management zone with the **Mainframe** name. It includes all **services** that run on hosts with the **z/OS** architecture and **underlying process groups**.

The API token is passed in the **Authorization** header.

The request body is lengthy, so it is truncated in the **Curl** section. See the full body in the **Request body** section. You can download or copy the example request body to try it out on your own.

#### Curl

```
curl -L -X POST 'https://mySampleEnv.live.dynatrace.com/api/config/v1/managementZones' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



--data-raw '{ <truncated - see the Request body section > }'
```

### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/managementZones
```

#### Request body

```
{



"name": "Mainframe",



"rules": [



{



"type": "SERVICE",



"enabled": true,



"propagationTypes": ["SERVICE_TO_PROCESS_GROUP_LIKE"],



"conditions": [



{



"key": {



"attribute": "HOST_ARCHITECTURE"



},



"comparisonInfo": {



"type": "OS_ARCHITECTURE",



"operator": "EQUALS",



"value": "ZOS",



"negate": false



}



}



]



}



]



}
```

#### Response body

```
{



"id": "2072664797514502900",



"name": "Mainframe"



}
```

#### Response code

201

#### Result

The new management zone looks like this in the UI:

![POST management zone](https://dt-cdn.net/images/post-mz-1345-ff7bd6a94e.png)

POST management zone

## Related topics

* [Management zones](/managed/manage/identity-access-management/permission-management/management-zones "Learn about management zones concepts, how to define management zones, and how to make the most of them.")