---
title: Settings API - Automatically applied tags schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-tags-auto-tagging
---

# Settings API - Automatically applied tags schema table

# Settings API - Automatically applied tags schema table

* Published Dec 05, 2023

### Automatically applied tags (`builtin:tags.auto-tagging)`

Tags simplify searches for related services, process groups, and hosts. They also facilitate the collection of related metrics into meaningful groups for analysis.

In dynamic or large environments, manual tagging of such entities is often impractical. In such cases, it's recommended that you use automated rule-based tags.

Rule-based tags behave just like manually-applied tags, except they're applied automatically to new entities that match defined rules. Automated rule-based tags can't be removed manually from individual services, process groups, or hosts. Rule-based tags are removed automatically once an entity no longer matches a defined rule.

For value suggestions based on entity data and preview functionality, environment-wide "Access environment" permission is required.

Tagging rules are executed periodically in the background, for a limited timeframe. Any entity that matches a tagging rule will receive the specific tag, while removing tags from entities that no longer match. Be aware that for any condition that requires the relationship between multiple entities, all entities in this scope need to be present in this timeframe!

Depending on environment-size, rule count (tagging rules, as well as management zone and naming rules) and rule complexity, the application of all tags might be delayed! For faster, unchanging tagging, please utilize the tagging REST API!

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:tags.auto-tagging` | * `group:tags` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:tags.auto-tagging` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:tags.auto-tagging` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:tags.auto-tagging` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Tag name `name` | text | - | Required |
| Description `description` | text | - | Optional |
| Rules `rules` | Set<[Rule](#Rule)> | - | Required |

##### The `Rule` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | - | Required |
| Optional tag value `valueFormat` | text | Type '{' for placeholder suggestions.  Placeholders containing ' /' must be enclosed in quotation marks.  For example: {"placeholder/etc"} | Optional |
| Value Normalization `valueNormalization` | enum | The element has these enums * `Leave text as-is` * `To upper case` * `To lower case` | Required |
| Rule type `type` | enum | The element has these enums * `ME` * `SELECTOR` | Required |
| `attributeRule` | [AutoTagAttributeRule](#AutoTagAttributeRule) | - | Required |
| Entity selector `entitySelector` | text | Learn more about the [Entity selector﻿](https://dt-url.net/apientityselector). | Required |

##### The `AutoTagAttributeRule` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Rule applies to `entityType` | enum | The element has these enums * `SERVICE` * `PROCESS_GROUP` * `HOST` * `CUSTOM_DEVICE` * `ESXI_HOST` * `APPLICATION` * `DCRUM_APPLICATION` * `MOBILE_APPLICATION` * `CUSTOM_APPLICATION` * `SYNTHETIC_TEST` * `EXTERNAL_SYNTHETIC_TEST` * `HTTP_CHECK` * `MULTIPROTOCOL_MONITOR` * `AWS_CLASSIC_LOAD_BALANCER` * `AWS_RELATIONAL_DATABASE_SERVICE` * `AWS_APPLICATION_LOAD_BALANCER` * `AWS_NETWORK_LOAD_BALANCER` * `AZURE` | Required |
| Conditions `conditions` | Set<[AttributeCondition](#AttributeCondition)> | - | Required |
| Apply to underlying hosts of matching services `serviceToHostPropagation` | boolean | - | Required |
| Apply to underlying process groups of matching services `serviceToPGPropagation` | boolean | - | Required |
| Apply to underlying hosts of matching process groups `pgToHostPropagation` | boolean | - | Required |
| Apply to all services provided by the process groups `pgToServicePropagation` | boolean | - | Required |
| Apply to processes running on matching hosts `hostToPGPropagation` | boolean | - | Required |
| Apply to services provided by matching Azure entities `azureToServicePropagation` | boolean | - | Required |
| Apply to process groups connected to matching Azure entities `azureToPGPropagation` | boolean | - | Required |

##### The `AttributeCondition` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Property `key` | enum | The element has these enums * `SERVICE_AKKA_ACTOR_SYSTEM` * `SERVICE_DATABASE_HOST_NAME` * `SERVICE_DATABASE_NAME` * `SERVICE_DATABASE_TOPOLOGY` * `SERVICE_DATABASE_VENDOR` * `SERVICE_DETECTED_NAME` * `SERVICE_ESB_APPLICATION_NAME` * `SERVICE_IBM_CTG_GATEWAY_URL` * `SERVICE_CTG_SERVICE_NAME` * `SERVICE_MESSAGING_LISTENER_CLASS_NAME` * `SERVICE_PUBLIC_DOMAIN_NAME` * `SERVICE_REMOTE_ENDPOINT` * `SERVICE_REMOTE_SERVICE_NAME` * `SERVICE_NAME` * `SERVICE_PORT` * `SERVICE_TAGS` * `SERVICE_TOPOLOGY` * `SERVICE_TYPE` * `SERVICE_TECHNOLOGY` * `SERVICE_TECHNOLOGY_EDITION` * `SERVICE_TECHNOLOGY_VERSION` * `SERVICE_WEB_APPLICATION_ID` * `SERVICE_WEB_CONTEXT_ROOT` * `SERVICE_WEB_SERVER_ENDPOINT` * `SERVICE_WEB_SERVER_NAME` * `SERVICE_WEB_SERVICE_NAME` * `SERVICE_WEB_SERVICE_NAMESPACE` * `PROCESS_GROUP_AZURE_HOST_NAME` * `PROCESS_GROUP_AZURE_SITE_NAME` * `CLOUD_FOUNDRY_ORG_NAME` * `PROCESS_GROUP_CUSTOM_METADATA` * `PROCESS_GROUP_DETECTED_NAME` * `DOCKER_CONTAINER_NAME` * `DOCKER_FULL_IMAGE_NAME` * `DOCKER_IMAGE_VERSION` * `PROCESS_GROUP_LISTEN_PORT` * `PROCESS_GROUP_PREDEFINED_METADATA` * `PROCESS_GROUP_ID` * `PROCESS_GROUP_NAME` * `PROCESS_GROUP_TAGS` * `PROCESS_GROUP_TECHNOLOGY` * `PROCESS_GROUP_TECHNOLOGY_EDITION` * `PROCESS_GROUP_TECHNOLOGY_VERSION` * `HOST_AIX_LOGICAL_CPU_COUNT` * `HOST_AIX_SIMULTANEOUS_THREADS` * `HOST_AIX_VIRTUAL_CPU_COUNT` * `EC2_INSTANCE_AMI_ID` * `AWS_AVAILABILITY_ZONE_NAME` * `EC2_INSTANCE_AWS_INSTANCE_TYPE` * `HOST_AWS_NAME_TAG` * `EC2_INSTANCE_AWS_SECURITY_GROUP` * `HOST_ARCHITECTURE` * `HOST_AZURE_SKU` * `AZURE_VM_NAME` * `HOST_AZURE_COMPUTE_MODE` * `AZURE_REGION_NAME` * `AZURE_SCALE_SET_NAME` * `HOST_AZURE_WEB_APPLICATION_HOST_NAMES` * `HOST_AZURE_WEB_APPLICATION_SITE_NAMES` * `HOST_BOSH_AVAILABILITY_ZONE` * `HOST_BOSH_DEPLOYMENT_ID` * `HOST_BOSH_INSTANCE_ID` * `HOST_BOSH_INSTANCE_NAME` * `HOST_BOSH_STEMCELL_VERSION` * `EC2_INSTANCE_BEANSTALK_ENV_NAME` * `HOST_BITNESS` * `HOST_BOSH_NAME` * `HOST_CPU_CORES` * `HOST_CLOUD_TYPE` * `HOST_CUSTOM_METADATA` * `HOST_DETECTED_NAME` * `EC2_INSTANCE_ID` * `EC2_INSTANCE_NAME` * `EC2_INSTANCE_TAGS` * `OPENSTACK_REGION_NAME` * `GOOGLE_CLOUD_PLATFORM_ZONE_NAME` * `GOOGLE_COMPUTE_INSTANCE_ID` * `GOOGLE_COMPUTE_INSTANCE_MACHINE_TYPE` * `GOOGLE_COMPUTE_INSTANCE_NAME` * `GOOGLE_COMPUTE_INSTANCE_PROJECT` * `GOOGLE_COMPUTE_INSTANCE_PROJECT_ID` * `GOOGLE_COMPUTE_INSTANCE_PUBLIC_IP_ADDRESSES` * `HOST_IP_ADDRESS` * `HOST_GROUP_ID` * `HOST_GROUP_NAME` * `HOST_NAME` * `HOST_TAGS` * `HOST_HYPERVISOR_TYPE` * `KUBERNETES_CLUSTER_NAME` * `HOST_LOGICAL_CPU_CORES` * `HOST_OS_TYPE` * `HOST_OS_VERSION` * `HOST_ONEAGENT_CUSTOM_HOST_NAME` * `GEOLOCATION_SITE_NAME` * `OPENSTACK_VM_NAME` * `OPENSTACK_AVAILABILITY_ZONE_NAME` * `NAME_OF_COMPUTE_NODE` * `OPENSTACK_VM_INSTANCE_TYPE` * `OPENSTACK_PROJECT_NAME` * `OPENSTACK_VM_SECURITY_GROUP` * `HOST_PAAS_MEMORY_LIMIT` * `HOST_PAAS_TYPE` * `EC2_INSTANCE_PRIVATE_HOST_NAME` * `EC2_INSTANCE_PUBLIC_HOST_NAME` * `HOST_TECHNOLOGY` * `VMWARE_DATACENTER_NAME` * `VMWARE_VM_NAME` * `CUSTOM_DEVICE_DNS_ADDRESS` * `CUSTOM_DEVICE_IP_ADDRESS` * `CUSTOM_DEVICE_NAME` * `CUSTOM_DEVICE_PORT` * `CUSTOM_DEVICE_TAGS` * `CUSTOM_DEVICE_METADATA` * `CUSTOM_DEVICE_TECHNOLOGY` * `CUSTOM_DEVICE_GROUP_NAME` * `CUSTOM_DEVICE_GROUP_TAGS` * `DATA_CENTER_SERVICE_METADATA` * `DATA_CENTER_SERVICE_IP_ADDRESS` * `DATA_CENTER_SERVICE_DECODER_TYPE` * `DATA_CENTER_SERVICE_NAME` * `DATA_CENTER_SERVICE_PORT` * `DATA_CENTER_SERVICE_TAGS` * `WEB_APPLICATION_NAME` * `WEB_APPLICATION_NAME_PATTERN` * `WEB_APPLICATION_TAGS` * `WEB_APPLICATION_TYPE` * `MOBILE_APPLICATION_NAME` * `MOBILE_APPLICATION_PLATFORM` * `MOBILE_APPLICATION_TAGS` * `ENTERPRISE_APPLICATION_METADATA` * `ENTERPRISE_APPLICATION_IP_ADDRESS` * `ENTERPRISE_APPLICATION_DECODER_TYPE` * `ENTERPRISE_APPLICATION_NAME` * `ENTERPRISE_APPLICATION_PORT` * `ENTERPRISE_APPLICATION_TAGS` * `BROWSER_MONITOR_NAME` * `BROWSER_MONITOR_TAGS` * `EXTERNAL_MONITOR_ENGINE_DESCRIPTION` * `EXTERNAL_MONITOR_ENGINE_NAME` * `EXTERNAL_MONITOR_ENGINE_TYPE` * `EXTERNAL_MONITOR_NAME` * `EXTERNAL_MONITOR_TAGS` * `HTTP_MONITOR_NAME` * `HTTP_MONITOR_TAGS` * `NETWORK_AVAILABILITY_MONITOR_NAME` * `NETWORK_AVAILABILITY_MONITOR_TAGS` * `CUSTOM_APPLICATION_NAME` * `CUSTOM_APPLICATION_PLATFORM` * `CUSTOM_APPLICATION_TAGS` * `CUSTOM_APPLICATION_TYPE` * `AWS_ACCOUNT_ID` * `AWS_ACCOUNT_NAME` * `AWS_CLASSIC_LOAD_BALANCER_FRONTEND_PORTS` * `AWS_CLASSIC_LOAD_BALANCER_NAME` * `AWS_CLASSIC_LOAD_BALANCER_TAGS` * `AWS_RELATIONAL_DATABASE_SERVICE_DB_NAME` * `AWS_RELATIONAL_DATABASE_SERVICE_ENDPOINT` * `AWS_RELATIONAL_DATABASE_SERVICE_ENGINE` * `AWS_RELATIONAL_DATABASE_SERVICE_INSTANCE_CLASS` * `AWS_RELATIONAL_DATABASE_SERVICE_NAME` * `AWS_RELATIONAL_DATABASE_SERVICE_PORT` * `AWS_RELATIONAL_DATABASE_SERVICE_TAGS` * `AWS_AUTO_SCALING_GROUP_NAME` * `AWS_AUTO_SCALING_GROUP_TAGS` * `OPENSTACK_ACCOUNT_NAME` * `OPENSTACK_ACCOUNT_PROJECT_NAME` * `ESXI_HOST_CLUSTER_NAME` * `ESXI_HOST_NAME` * `ESXI_HOST_TAGS` * `ESXI_HOST_HARDWARE_MODEL` * `ESXI_HOST_HARDWARE_VENDOR` * `ESXI_HOST_PRODUCT_NAME` * `ESXI_HOST_PRODUCT_VERSION` * `APPMON_SERVER_NAME` * `APPMON_SYSTEM_PROFILE_NAME` * `CLOUD_FOUNDRY_FOUNDATION_NAME` * `AWS_APPLICATION_LOAD_BALANCER_NAME` * `AWS_APPLICATION_LOAD_BALANCER_TAGS` * `AWS_NETWORK_LOAD_BALANCER_NAME` * `AWS_NETWORK_LOAD_BALANCER_TAGS` * `CLOUD_APPLICATION_NAMESPACE_LABELS` * `CLOUD_APPLICATION_NAMESPACE_NAME` * `CLOUD_APPLICATION_LABELS` * `CLOUD_APPLICATION_NAME` * `KUBERNETES_SERVICE_NAME` * `AZURE_MGMT_GROUP_UUID` * `AZURE_MGMT_GROUP_NAME` * `AZURE_ENTITY_NAME` * `AZURE_SUBSCRIPTION_UUID` * `AZURE_SUBSCRIPTION_NAME` * `AZURE_ENTITY_TAGS` * `AZURE_TENANT_UUID` * `AZURE_TENANT_NAME` * `HOST_KUBERNETES_LABELS` * `KUBERNETES_NODE_NAME` * `QUEUE_NAME` * `QUEUE_VENDOR` * `QUEUE_TECHNOLOGY` | Required |
| Key source `dynamicKeySource` | text | - | Required |
| Dynamic key `dynamicKey` | text | - | Required |
| Operator `operator` | enum | The element has these enums * `EQUALS` * `NOT_EQUALS` * `EXISTS` * `NOT_EXISTS` * `BEGINS_WITH` * `NOT_BEGINS_WITH` * `CONTAINS` * `NOT_CONTAINS` * `ENDS_WITH` * `NOT_ENDS_WITH` * `GREATER_THAN` * `NOT_GREATER_THAN` * `GREATER_THAN_OR_EQUAL` * `NOT_GREATER_THAN_OR_EQUAL` * `LOWER_THAN` * `NOT_LOWER_THAN` * `LOWER_THAN_OR_EQUAL` * `NOT_LOWER_THAN_OR_EQUAL` * `TAG_KEY_EQUALS` * `NOT_TAG_KEY_EQUALS` * `IS_IP_IN_RANGE` * `NOT_IS_IP_IN_RANGE` * `REGEX_MATCHES` * `NOT_REGEX_MATCHES` | Required |
| Value `enumValue` | text | - | Required |
| Value `stringValue` | text | - | Required |
| Case sensitive `caseSensitive` | boolean | - | Required |
| Value `integerValue` | integer | - | Required |
| Value `entityId` | text | - | Required |
| Tag `tag` | text | Format: `[CONTEXT]tagKey:tagValue` | Required |