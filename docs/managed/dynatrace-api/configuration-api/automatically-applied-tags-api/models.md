---
title: Automatically applied tags API - JSON models
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/automatically-applied-tags-api/models
---

# Automatically applied tags API - JSON models

# Automatically applied tags API - JSON models

* Reference
* Published Aug 13, 2019

Deprecated

This API is deprecated. Use the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") with the [Automatically applied tags](/managed/dynatrace-api/environment-api/settings/schemas/builtin-tags-auto-tagging "View builtin:tags.auto-tagging settings schema table of your monitoring environment via the Dynatrace API.") (`builtin:tags.auto-tagging`) schema instead.

Some JSON models of the **Automatically applied tags** API vary depending on the **type** of the model. The JSON models for each variation are listed below.

## Variations of the `ConditionKey` object

The `ConditionKey` object is the base for all conditions. The actual set of fields depends on the **type** of the condition.

### HOST\_CUSTOM\_METADATA\_KEY

CustomHostMetadataConditionKey

Parameters

JSON model

#### The `CustomHostMetadataConditionKey` object

The key for dynamic attributes of the `HOST_CUSTOM_METADATA_KEY` type.

| Element | Type | Description |
| --- | --- | --- |
| dynamicKey | [CustomHostMetadataKey](#openapi-definition-CustomHostMetadataKey) | The key of the attribute, which need dynamic keys.  Not applicable otherwise, as the attibute itself acts as a key. |

#### The `CustomHostMetadataKey` object

The key of the attribute, which need dynamic keys.

Not applicable otherwise, as the attibute itself acts as a key.

| Element | Type | Description |
| --- | --- | --- |
| key | string | The actual key of the custom metadata. |
| source | string | The source of the custom metadata. The element can hold these values * `ENVIRONMENT` * `GOOGLE_COMPUTE_ENGINE` * `PLUGIN` |

```
{



"attribute": "HOST_CUSTOM_METADATA",



"type": "HOST_CUSTOM_METADATA_KEY",



"dynamicKey": {



"source": "ENVIRONMENT",



"key": "myKey"



}



}
```

### PROCESS\_CUSTOM\_METADATA\_KEY

CustomProcessMetadataConditionKey

Parameters

JSON model

#### The `CustomProcessMetadataConditionKey` object

The key for dynamic attributes of the `PROCESS_CUSTOM_METADATA_KEY` type.

| Element | Type | Description |
| --- | --- | --- |
| dynamicKey | [CustomProcessMetadataKey](#openapi-definition-CustomProcessMetadataKey) | The key of the attribute, which need dynamic keys.  Not applicable otherwise, as the attibute itself acts as a key. |

#### The `CustomProcessMetadataKey` object

The key of the attribute, which need dynamic keys.

Not applicable otherwise, as the attibute itself acts as a key.

| Element | Type | Description |
| --- | --- | --- |
| key | string | The actual key of the custom metadata. |
| source | string | The source of the custom metadata. The element can hold these values * `AGENT` * `CLOUD_FOUNDRY` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` * `PLUGIN` |

```
{



"attribute": "PROCESS_GROUP_DETECTED_NAME",



"type": "PROCESS_CUSTOM_METADATA_KEY",



"dynamicKey": {



"source": "KUBERNETES",



"key": "myKey"



}



}
```

### PROCESS\_PREDEFINED\_METADATA\_KEY

ProcessMetadataConditionKey

Parameters

JSON model

#### The `ProcessMetadataConditionKey` object

The key for dynamic attributes of the `PROCESS_PREDEFINED_METADATA_KEY` type.

| Element | Type | Description |
| --- | --- | --- |
| dynamicKey | string | The key of the attribute, which need dynamic keys.  Not applicable otherwise, as the attibute itself acts as a key. The element can hold these values * `AEM_ENV_TYPE` * `AEM_PROGRAM` * `AEM_SERVICE` * `AEM_TIER` * `AMAZON_ECR_IMAGE_ACCOUNT_ID` * `AMAZON_ECR_IMAGE_REGION` * `AMAZON_LAMBDA_FUNCTION_NAME` * `AMAZON_REGION` * `APACHE_CONFIG_PATH` * `APACHE_SPARK_MASTER_IP_ADDRESS` * `ASP_DOT_NET_CORE_APPLICATION_PATH` * `AWS_ECS_CLUSTER` * `AWS_ECS_CONTAINERNAME` * `AWS_ECS_CONTAINER_ARN` * `AWS_ECS_DOCKER_ID` * `AWS_ECS_DOCKER_NAME` * `AWS_ECS_FAMILY` * `AWS_ECS_REVISION` * `AWS_ECS_TASK_ARN` * `AZURE_APP_SERVICE_WEBSITE_INSTANCE_ID` * `AZURE_APP_SERVICE_WEBSITE_OWNER_NAME` * `AZURE_APP_SERVICE_WEBSITE_SITE_NAME` * `AZURE_CONTAINER_APP_ENV_DNS_SUFFIX` * `AZURE_CONTAINER_APP_HOSTNAME` * `AZURE_CONTAINER_APP_NAME` * `AZURE_CONTAINER_APP_REPLICA_NAME` * `AZURE_SERVICE_FABRIC_APPLICATIONID` * `AZURE_SERVICE_FABRIC_APPLICATIONNAME` * `AZURE_SERVICE_FABRIC_CODEPACKAGENAME` * `AZURE_SERVICE_FABRIC_HOSTEDSERVICENAME` * `AZURE_SERVICE_FABRIC_INSTANCEID` * `AZURE_SERVICE_FABRIC_REPLICAID` * `AZURE_SERVICE_FABRIC_SERVICEPACKAGENAME` * `AZURE_SPRING_APPLICATION_NAME` * `AZURE_SPRING_CLOUD_CONFIG_URI` * `CASSANDRA_CLUSTER_NAME` * `CATALINA_BASE` * `CATALINA_HOME` * `CLOUD_FOUNDRY_APP_ID` * `CLOUD_FOUNDRY_APP_NAME` * `CLOUD_FOUNDRY_INSTANCE_INDEX` * `CLOUD_FOUNDRY_SPACE_ID` * `CLOUD_FOUNDRY_SPACE_NAME` * `COLDFUSION_JVM_CONFIG_FILE` * `COLDFUSION_SERVICE_NAME` * `COMMAND_LINE_ARGS` * `CONTAINER_ID` * `CONTAINER_IMAGE_NAME` * `CONTAINER_IMAGE_VERSION` * `CONTAINER_NAME` * `DATASOURCE_MONITORING_CONFIG_ID` * `DECLARATIVE_CONFIG_RULE_ID` * `DECLARATIVE_ID` * `DOTNET_COMMAND` * `DOTNET_COMMAND_PATH` * `DYNATRACE_CLUSTER_ID` * `DYNATRACE_NODE_ID` * `ELASTICSEARCH_CLUSTER_NAME` * `ELASTICSEARCH_NODE_NAME` * `EQUINOX_CONFIG_PATH` * `EXE_NAME` * `EXE_PATH` * `GAE_VERSION` * `GLASS_FISH_DOMAIN_NAME` * `GLASS_FISH_INSTANCE_NAME` * `GOOGLE_APP_ENGINE_INSTANCE` * `GOOGLE_APP_ENGINE_SERVICE` * `GOOGLE_CLOUD_INSTANCE_ID` * `GOOGLE_CLOUD_INSTANCE_REGION` * `GOOGLE_CLOUD_PROJECT` * `GOOGLE_CLOUD_RUN_EXECUTION` * `GOOGLE_CLOUD_RUN_JOB` * `GOOGLE_CLOUD_RUN_REVISION` * `GOOGLE_CLOUD_RUN_SERVICE` * `HEROKU_APP_DEFAULT_DOMAIN_NAME` * `HEROKU_DYNO` * `HEROKU_RELEASE_VERSION` * `HYBRIS_BIN_DIRECTORY` * `HYBRIS_CONFIG_DIRECTORY` * `HYBRIS_DATA_DIRECTORY` * `IBM_APPLID` * `IBM_CICS_IMS_APPLID` * `IBM_CICS_IMS_JOBNAME` * `IBM_CICS_REGION` * `IBM_CTG_NAME` * `IBM_IMS_CONNECT_REGION` * `IBM_IMS_CONTROL_REGION` * `IBM_IMS_MESSAGE_PROCESSING_REGION` * `IBM_IMS_SOAP_GW_NAME` * `IBM_INTEGRATION_NODE_NAME` * `IBM_INTEGRATION_SERVER_NAME` * `IBM_JOBNAME` * `IIS_APP_POOL` * `IIS_ROLE_NAME` * `JAVA_JAR_FILE` * `JAVA_JAR_PATH` * `JAVA_MAIN_CLASS` * `JAVA_MAIN_MODULE` * `JBOSS_HOME` * `JBOSS_MODE` * `JBOSS_SERVER_NAME` * `KUBERNETES_BASE_POD_NAME` * `KUBERNETES_CLUSTER_ID` * `KUBERNETES_CONTAINER_NAME` * `KUBERNETES_FULL_POD_NAME` * `KUBERNETES_NAMESPACE` * `KUBERNETES_POD_UID` * `KUBERNETES_RULE_RESULT` * `MSSQL_INSTANCE_NAME` * `NODE_JS_APP_BASE_DIRECTORY` * `NODE_JS_APP_NAME` * `NODE_JS_SCRIPT_NAME` * `ORACLE_SID` * `OSAGENT_GROUPID_NAME` * `OSAGENT_INSTANCEID_NAME` * `PG_ID_CALC_INPUT_KEY_LINKAGE` * `PHP_SCRIPT_PATH` * `PHP_WORKING_DIRECTORY` * `PYTHON_MODULE` * `PYTHON_SCRIPT` * `PYTHON_SCRIPT_PATH` * `RKE2_TYPE` * `RUBY_APP_ROOT_PATH` * `RUBY_SCRIPT_PATH` * `RULE_RESULT` * `SOFTWAREAG_INSTALL_ROOT` * `SOFTWAREAG_PRODUCTPROPNAME` * `SPRINGBOOT_APP_NAME` * `SPRINGBOOT_PROFILE_NAME` * `SPRINGBOOT_STARTUP_CLASS` * `TIBCO_BUSINESSWORKS_CE_APP_NAME` * `TIBCO_BUSINESSWORKS_CE_VERSION` * `TIBCO_BUSINESS_WORKS_APP_NODE_NAME` * `TIBCO_BUSINESS_WORKS_APP_SPACE_NAME` * `TIBCO_BUSINESS_WORKS_DOMAIN_NAME` * `TIBCO_BUSINESS_WORKS_ENGINE_PROPERTY_FILE` * `TIBCO_BUSINESS_WORKS_ENGINE_PROPERTY_FILE_PATH` * `TIBCO_BUSINESS_WORKS_HOME` * `VARNISH_INSTANCE_NAME` * `WEBSPHERE_LIBERTY_SERVER_NAME` * `WEB_LOGIC_CLUSTER_NAME` * `WEB_LOGIC_DOMAIN_NAME` * `WEB_LOGIC_HOME` * `WEB_LOGIC_NAME` * `WEB_SPHERE_CELL_NAME` * `WEB_SPHERE_CLUSTER_NAME` * `WEB_SPHERE_NODE_NAME` * `WEB_SPHERE_SERVER_NAME` * `Z_CM_VERSION` |

```
{



"attribute": "PROCESS_GROUP_PREDEFINED_METADATA",



"type": "PROCESS_PREDEFINED_METADATA_KEY",



"dynamicKey": "JAVA_JAR_FILE"



}
```

### STRING

StringConditionKey

Parameters

JSON model

#### The `StringConditionKey` object

The key for dynamic attributes of the `STRING` type.

| Element | Type | Description |
| --- | --- | --- |
| dynamicKey | string | The key of the attribute, which need dynamic keys.  Not applicable otherwise, as the attibute itself acts as a key. |

```
{



"attribute": "HOST_GROUP_NAME",



"type": "STRING",



"dynamicKey": "myKey"



}
```

## Variations of the `ComparisonBasic` object

The `ComparisonBasic` object is the base for all comparison operations. The actual set of fields depends on the **type** of the comparison.

### APPLICATION\_TYPE

ApplicationTypeComparison

Parameters

JSON model

#### The `ApplicationTypeComparison` object

Comparison for `APPLICATION_TYPE` attributes.

| Element | Type | Description |
| --- | --- | --- |
| operator | string | Operator of the comparison. You can reverse it by setting **negate** to `true`.  Possible values depend on the **type** of the comparison. Find the list of actual models in the description of the **type** field and check the description of the model you need. The element can hold these values * `EQUALS` * `EXISTS` |
| value | string | The value to compare to. The element can hold these values * `AGENTLESS_MONITORING` * `AUTO_INJECTED` * `DEFAULT` * `SAAS_VENDOR` |

```
{



"operator": "EQUALS",



"value": "SAAS_VENDOR",



"negate": false,



"type": "APPLICATION_TYPE"



}
```

### AZURE\_COMPUTE\_MODE

AzureComputeModeComparison

Parameters

JSON model

#### The `AzureComputeModeComparison` object

Comparison for `AZURE_COMPUTE_MODE` attributes.

| Element | Type | Description |
| --- | --- | --- |
| operator | string | Operator of the comparison. You can reverse it by setting **negate** to `true`.  Possible values depend on the **type** of the comparison. Find the list of actual models in the description of the **type** field and check the description of the model you need. The element can hold these values * `EQUALS` * `EXISTS` |
| value | string | The value to compare to. The element can hold these values * `DEDICATED` * `SHARED` |

```
{



"operator": "EQUALS",



"value": "DEDICATED",



"negate": false,



"type": "AZURE_COMPUTE_MODE"



}
```

### AZURE\_SKU

AzureSkuComparision

Parameters

JSON model

#### The `AzureSkuComparision` object

Comparison for `AZURE_SKU` attributes.

| Element | Type | Description |
| --- | --- | --- |
| operator | string | Operator of the comparison. You can reverse it by setting **negate** to `true`.  Possible values depend on the **type** of the comparison. Find the list of actual models in the description of the **type** field and check the description of the model you need. The element can hold these values * `EQUALS` * `EXISTS` |
| value | string | The value to compare to. The element can hold these values * `BASIC` * `DYNAMIC` * `FREE` * `PREMIUM` * `SHARED` * `STANDARD` |

```
{



"operator": "EQUALS",



"value": "PREMIUM",



"negate": false,



"type": "AZURE_SKU"



}
```

### BITNESS

BitnessComparison

Parameters

JSON model

#### The `BitnessComparision` object

Comparison for `BITNESS` attributes.

| Element | Type | Description |
| --- | --- | --- |
| operator | string | Operator of the comparison. You can reverse it by setting **negate** to `true`.  Possible values depend on the **type** of the comparison. Find the list of actual models in the description of the **type** field and check the description of the model you need. The element can hold these values * `EQUALS` * `EXISTS` |
| value | string | The value to compare to. The element can hold these values * `32` * `64` |

```
{



"operator": "EQUALS",



"value": "64",



"negate": false,



"type": "BITNESS"



}
```

### CLOUD\_TYPE

CloudTypeComparison

Parameters

JSON model

#### The `CloudTypeComparison` object

Comparison for `CLOUD_TYPE` attributes.

| Element | Type | Description |
| --- | --- | --- |
| operator | string | Operator of the comparison. You can reverse it by setting **negate** to `true`.  Possible values depend on the **type** of the comparison. Find the list of actual models in the description of the **type** field and check the description of the model you need. The element can hold these values * `EQUALS` * `EXISTS` |
| value | string | The value to compare to. The element can hold these values * `AZURE` * `EC2` * `GOOGLE_CLOUD_PLATFORM` * `OPENSTACK` * `ORACLE` * `UNRECOGNIZED` |

```
{



"operator": "EQUALS",



"value": "ORACLE",



"negate": false,



"type": "CLOUD_TYPE"



}
```

### CUSTOM\_APPLICATION\_TYPE

CustomApplicationTypeComparison

Parameters

JSON model

#### The `CustomApplicationTypeComparison` object

Comparison for `CUSTOM_APPLICATION_TYPE` attributes.

| Element | Type | Description |
| --- | --- | --- |
| operator | string | Operator of the comparison. You can reverse it by setting **negate** to `true`.  Possible values depend on the **type** of the comparison. Find the list of actual models in the description of the **type** field and check the description of the model you need. The element can hold these values * `EQUALS` * `EXISTS` |
| value | string | The value to compare to. The element can hold these values * `AMAZON_ECHO` * `DESKTOP` * `EMBEDDED` * `IOT` * `MICROSOFT_HOLOLENS` * `UFO` |

```
{



"operator": "EQUALS",



"value": "EMBEDDED",



"negate": false,



"type": "CUSTOM_APPLICATION_TYPE"



}
```

### DATABASE\_TOPOLOGY

DatabaseTopologyComparison

Parameters

JSON model

#### The `DatabaseTopologyComparison` object

Comparison for `DATABASE_TOPOLOGY` attributes.

| Element | Type | Description |
| --- | --- | --- |
| operator | string | Operator of the comparison. You can reverse it by setting **negate** to `true`.  Possible values depend on the **type** of the comparison. Find the list of actual models in the description of the **type** field and check the description of the model you need. The element can hold these values * `EQUALS` * `EXISTS` |
| value | string | The value to compare to. The element can hold these values * `CLUSTER` * `EMBEDDED` * `FAILOVER` * `IPC` * `LOAD_BALANCING` * `SINGLE_SERVER` * `UNSPECIFIED` |

```
{



"operator": "EQUALS",



"value": "LOAD_BALANCING",



"negate": false,



"type": "DATABASE_TOPOLOGY"



}
```

### DCRUM\_DECODER\_TYPE

DcrumDecoderComparison

Parameters

JSON model

#### The `DcrumDecoderComparison` object

Comparison for `DCRUM_DECODER_TYPE` attributes.

| Element | Type | Description |
| --- | --- | --- |
| operator | string | Operator of the comparison. You can reverse it by setting **negate** to `true`.  Possible values depend on the **type** of the comparison. Find the list of actual models in the description of the **type** field and check the description of the model you need. The element can hold these values * `EQUALS` * `EXISTS` |
| value | string | The value to compare to. The element can hold these values * `ALL_OTHER` * `CITRIX_APPFLOW` * `CITRIX_ICA` * `CITRIX_ICA_OVER_SSL` * `DB2_DRDA` * `HTTP` * `HTTPS` * `HTTP_EXPRESS` * `INFORMIX` * `MYSQL` * `ORACLE` * `SAP_GUI` * `SAP_GUI_OVER_HTTP` * `SAP_GUI_OVER_HTTPS` * `SAP_HANA_DB` * `SAP_RFC` * `SSL` * `TDS` |

```
{



"operator": "EQUALS",



"value": "MYSQL",



"negate": false,



"type": "DCRUM_DECODER_TYPE"



}
```

### ENTITY\_ID

EntityIdComparison

Parameters

JSON model

#### The `EntityIdComparison` object

Comparison for `ENTITY_ID` attributes.

| Element | Type | Description |
| --- | --- | --- |
| operator | string | Operator of the comparison. You can reverse it by setting **negate** to `true`.  Possible values depend on the **type** of the comparison. Find the list of actual models in the description of the **type** field and check the description of the model you need. The element can hold these values * `EQUALS` |
| value | string | The value to compare to. |

```
{



"operator": "EQUALS",



"value": "HOST-80FF8584D8954C1D",



"negate": false,



"type": "ENTITY_ID"



}
```

### HYPERVISOR\_TYPE

HypervisorTypeComparison

Parameters

JSON model

#### The `HypervisorTypeComparision` object

Comparison for `HYPERVISOR_TYPE` attributes.

| Element | Type | Description |
| --- | --- | --- |
| operator | string | Operator of the comparison. You can reverse it by setting **negate** to `true`.  Possible values depend on the **type** of the comparison. Find the list of actual models in the description of the **type** field and check the description of the model you need. The element can hold these values * `EQUALS` * `EXISTS` |
| value | string | The value to compare to. The element can hold these values * `AHV` * `AWS_NITRO` * `GVISOR` * `HYPER_V` * `KVM` * `LPAR` * `QEMU` * `UNRECOGNIZED` * `VIRTUAL_BOX` * `VMWARE` * `WPAR` * `XEN` |

```
{



"operator": "EQUALS",



"value": "HYPER_V",



"negate": false,



"type": "HYPERVISOR_TYPE"



}
```

### INDEXED\_NAME

IndexedNameComparison

Parameters

JSON model

#### The `IndexedNameComparison` object

Comparison for `INDEXED_NAME` attributes.

| Element | Type | Description |
| --- | --- | --- |
| caseSensitive | boolean | The comparison is case-sensitive (`true`) or insensitive (`false`). |
| operator | string | Operator of the comparison. You can reverse it by setting **negate** to `true`.  Possible values depend on the **type** of the comparison. Find the list of actual models in the description of the **type** field and check the description of the model you need. The element can hold these values * `CONTAINS` * `EQUALS` * `EXISTS` |
| value | string | The value to compare to. |

```
{



"operator": "EQUALS",



"value": "string",



"negate": false,



"type": "INDEXED_NAME"



}
```

### INDEXED\_STRING

IndexedStringComparison

Parameters

JSON model

#### The `IndexedStringComparison` object

Comparison for `INDEXED_STRING` attributes.

| Element | Type | Description |
| --- | --- | --- |
| caseSensitive | boolean | The comparison is case-sensitive (`true`) or insensitive (`false`). |
| operator | string | Operator of the comparison. You can reverse it by setting **negate** to `true`.  Possible values depend on the **type** of the comparison. Find the list of actual models in the description of the **type** field and check the description of the model you need. The element can hold these values * `EQUALS` * `EXISTS` |
| value | string | The value to compare to. |

```
{



"operator": "EQUALS",



"value": "string",



"negate": false,



"type": "INDEXED_STRING"



}
```

### INDEXED\_TAG

IndexedTagComparison

Parameters

JSON model

#### The `IndexedTagComparison` object

Comparison for `INDEXED_TAG` attributes.

| Element | Type | Description |
| --- | --- | --- |
| operator | string | Operator of the comparison. You can reverse it by setting **negate** to `true`.  Possible values depend on the **type** of the comparison. Find the list of actual models in the description of the **type** field and check the description of the model you need. The element can hold these values * `EQUALS` * `EXISTS` * `TAG_KEY_EQUALS` |
| value | [TagInfo](#openapi-definition-TagInfo) | Tag of a Dynatrace entity. |

#### The `TagInfo` object

Tag of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| context | string | The origin of the tag, such as AWS or Cloud Foundry.  Custom tags use the `CONTEXTLESS` value. The element can hold these values * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | The key of the tag.  Custom tags have the tag value here. |
| value | string | The value of the tag.  Not applicable to custom tags. |

```
{



"operator": "EQUALS",



"value": {



"context": "CONTEXTLESS",



"key": "hostOS"



},



"negate": false,



"type": "INDEXED_TAG"



}
```

### INTEGER

IntegerComparison-integer

Parameters

JSON model

#### The `IntegerComparison` object

Comparison for `INTEGER` attributes.

| Element | Type | Description |
| --- | --- | --- |
| operator | string | Operator of the comparison. You can reverse it by setting **negate** to `true`.  Possible values depend on the **type** of the comparison. Find the list of actual models in the description of the **type** field and check the description of the model you need. The element can hold these values * `EQUALS` * `EXISTS` * `GREATER_THAN` * `GREATER_THAN_OR_EQUAL` * `LOWER_THAN` * `LOWER_THAN_OR_EQUAL` |
| value | integer | The value to compare to. |

```
{



"operator": "GREATER_THAN",



"value": 88,



"negate": false,



"type": "INTEGER"



}
```

### IP\_ADDRESS

IpAddressComparison

Parameters

JSON model

#### The `IpAddressComparison` object

Comparison for `IP_ADDRESS` attributes.

| Element | Type | Description |
| --- | --- | --- |
| caseSensitive | boolean | The comparison is case-sensitive (`true`) or insensitive (`false`). |
| operator | string | Operator of the comparison. You can reverse it by setting **negate** to `true`.  Possible values depend on the **type** of the comparison. Find the list of actual models in the description of the **type** field and check the description of the model you need. The element can hold these values * `BEGINS_WITH` * `CONTAINS` * `ENDS_WITH` * `EQUALS` * `EXISTS` * `IS_IP_IN_RANGE` * `REGEX_MATCHES` |
| value | string | The value to compare to. |

```
{



"operator": "BEGINS_WITH",



"value": "192",



"negate": false,



"type": "IP_ADDRESS",



"caseSensitive": false



}
```

### MOBILE\_PLATFORM

MobilePlatformComparison

Parameters

JSON model

#### The `MobilePlatformComparison` object

Comparison for `MOBILE_PLATFORM` attributes.

| Element | Type | Description |
| --- | --- | --- |
| operator | string | Operator of the comparison. You can reverse it by setting **negate** to `true`.  Possible values depend on the **type** of the comparison. Find the list of actual models in the description of the **type** field and check the description of the model you need. The element can hold these values * `EQUALS` * `EXISTS` |
| value | string | The value to compare to. The element can hold these values * `ANDROID` * `IOS` * `LINUX` * `MAC_OS` * `OTHER` * `TVOS` * `WINDOWS` |

```
{



"operator": "EQUALS",



"value": "IOS",



"negate": false,



"type": "MOBILE_PLATFORM"



}
```

### OS\_ARCHITECTURE

OsArchitectureComparison

Parameters

JSON model

#### The `OsArchitectureComparison` object

Comparison for `OS_ARCHITECTURE` attributes.

| Element | Type | Description |
| --- | --- | --- |
| operator | string | Operator of the comparison. You can reverse it by setting **negate** to `true`.  Possible values depend on the **type** of the comparison. Find the list of actual models in the description of the **type** field and check the description of the model you need. The element can hold these values * `EQUALS` * `EXISTS` |
| value | string | The value to compare to. The element can hold these values * `ARM` * `IA64` * `PARISC` * `PPC` * `PPCLE` * `S390` * `SPARC` * `X86` * `ZOS` |

```
{



"operator": "EQUALS",



"value": "IA64",



"negate": false,



"type": "OS_ARCHITECTURE"



}
```

### OS\_TYPE

OsTypeComparison

Parameters

JSON model

#### The `OsTypeComparison` object

Comparison for `OS_TYPE` attributes.

| Element | Type | Description |
| --- | --- | --- |
| operator | string | Operator of the comparison. You can reverse it by setting **negate** to `true`.  Possible values depend on the **type** of the comparison. Find the list of actual models in the description of the **type** field and check the description of the model you need. The element can hold these values * `EQUALS` * `EXISTS` |
| value | string | The value to compare to. The element can hold these values * `AIX` * `DARWIN` * `HPUX` * `LINUX` * `SOLARIS` * `WINDOWS` * `ZOS` |

```
{



"operator": "EQUALS",



"value": "LINUX",



"negate": false,



"type": "OS_TYPE"



}
```

### PAAS\_TYPE

PaasTypeComparison

Parameters

JSON model

#### The `PaasTypeComparison` object

Comparison for `PAAS_TYPE` attributes.

| Element | Type | Description |
| --- | --- | --- |
| operator | string | Operator of the comparison. You can reverse it by setting **negate** to `true`.  Possible values depend on the **type** of the comparison. Find the list of actual models in the description of the **type** field and check the description of the model you need. The element can hold these values * `EQUALS` * `EXISTS` |
| value | string | The value to compare to. The element can hold these values * `AWS_ECS_EC2` * `AWS_ECS_FARGATE` * `AWS_LAMBDA` * `AZURE_FUNCTIONS` * `AZURE_WEBSITES` * `CLOUD_FOUNDRY` * `GOOGLE_APP_ENGINE` * `GOOGLE_CLOUD_RUN` * `HEROKU` * `KUBERNETES` * `OPENSHIFT` |

```
{



"operator": "EQUALS",



"value": "KUBERNETES",



"negate": false,



"type": "PAAS_TYPE"



}
```

### SERVICE\_TOPOLOGY

ServiceTopologyComparison

Parameters

JSON model

#### The `ServiceTopologyComparison` object

Comparison for `SERVICE_TOPOLOGY` attributes.

| Element | Type | Description |
| --- | --- | --- |
| operator | string | Operator of the comparison. You can reverse it by setting **negate** to `true`.  Possible values depend on the **type** of the comparison. Find the list of actual models in the description of the **type** field and check the description of the model you need. The element can hold these values * `EQUALS` * `EXISTS` |
| value | string | The value to compare to. The element can hold these values * `EXTERNAL_SERVICE` * `FULLY_MONITORED` * `OPAQUE_SERVICE` |

```
{



"operator": "EQUALS",



"value": "FULLY_MONITORED",



"negate": false,



"type": "SERVICE_TOPOLOGY"



}
```

### SERVICE\_TYPE

ServiceTypeComparison

Parameters

JSON model

#### The `ServiceTypeComparison` object

Comparison for `SERVICE_TYPE` attributes.

| Element | Type | Description |
| --- | --- | --- |
| operator | string | Operator of the comparison. You can reverse it by setting **negate** to `true`.  Possible values depend on the **type** of the comparison. Find the list of actual models in the description of the **type** field and check the description of the model you need. The element can hold these values * `EQUALS` * `EXISTS` |
| value | string | The value to compare to. The element can hold these values * `BACKGROUND_ACTIVITY` * `CICS_SERVICE` * `CUSTOM_SERVICE` * `DATABASE_SERVICE` * `ENTERPRISE_SERVICE_BUS_SERVICE` * `EXTERNAL` * `IBM_INTEGRATION_BUS_SERVICE` * `IMS_SERVICE` * `MESSAGING_SERVICE` * `QUEUE_LISTENER_SERVICE` * `RMI_SERVICE` * `RPC_SERVICE` * `SPAN` * `UNIFIED` * `WEB_REQUEST_SERVICE` * `WEB_SERVICE` * `ZOS_CONNECT` |

```
{



"operator": "EQUALS",



"value": "BACKGROUND_ACTIVITY",



"negate": false,



"type": "SERVICE_TYPE"



}
```

### SIMPLE\_HOST\_TECH

SimpleHostTechComparison

Parameters

JSON model

#### The `SimpleHostTechComparison` object

Comparison for `SIMPLE_HOST_TECH` attributes.

| Element | Type | Description |
| --- | --- | --- |
| operator | string | Operator of the comparison. You can reverse it by setting **negate** to `true`.  Possible values depend on the **type** of the comparison. Find the list of actual models in the description of the **type** field and check the description of the model you need. The element can hold these values * `EQUALS` * `EXISTS` |
| value | [SimpleHostTech](#openapi-definition-SimpleHostTech) | The value to compare to. |

#### The `SimpleHostTech` object

The value to compare to.

| Element | Type | Description |
| --- | --- | --- |
| type | string | Predefined technology, if technology is not predefined, then the verbatim type must be set The element can hold these values * `APPARMOR` * `BOSH` * `BOSHBPM` * `CLOUDFOUNDRY` * `CONTAINERD` * `CRIO` * `DIEGO_CELL` * `DOCKER` * `GARDEN` * `GRSECURITY` * `KUBERNETES` * `OPENSHIFT` * `OPENSTACK_COMPUTE` * `OPENSTACK_CONTROLLER` * `SELINUX` |
| verbatimType | string | Non-predefined technology, use for custom technologies. |

```
{



"operator": "EQUALS",



"value": {



"type": "CLOUDFOUNDRY"



},



"negate": false,



"type": "SIMPLE_HOST_TECH"



}
```

### SIMPLE\_TECH

SimpleTechComparison

Parameters

JSON model

#### The `SimpleTechComparison` object

Comparison for `SIMPLE_TECH` attributes.

| Element | Type | Description |
| --- | --- | --- |
| operator | string | Operator of the comparison. You can reverse it by setting **negate** to `true`.  Possible values depend on the **type** of the comparison. Find the list of actual models in the description of the **type** field and check the description of the model you need. The element can hold these values * `EQUALS` * `EXISTS` |
| value | [SimpleTech](#openapi-definition-SimpleTech) | The value to compare to. |

#### The `SimpleTech` object

The value to compare to.

| Element | Type | Description |
| --- | --- | --- |
| type | string | Predefined technology, if technology is not predefined, then the verbatim type must be set The element can hold these values * `ACTIVEMQ_CLIENT` * `ACTIVE_MQ` * `ACTIVE_MQ_ARTEMIS` * `ADOBE_EXPERIENCE_MANAGER` * `ADO_NET` * `AIOHTTP` * `AIX` * `AKKA` * `AMAZON_REDSHIFT` * `AMQP` * `APACHE_CAMEL` * `APACHE_CASSANDRA` * `APACHE_COUCH_DB` * `APACHE_DERBY` * `APACHE_HTTP_CLIENT_ASYNC` * `APACHE_HTTP_CLIENT_SYNC` * `APACHE_HTTP_SERVER` * `APACHE_KAFKA` * `APACHE_LOG4J` * `APACHE_PEKKO` * `APACHE_SOLR` * `APACHE_STORM` * `APACHE_SYNAPSE` * `APACHE_TOMCAT` * `APPARMOR` * `APPLICATION_INSIGHTS_SDK` * `ASP_DOTNET` * `ASP_DOTNET_CORE` * `ASP_DOTNET_CORE_SIGNALR` * `ASP_DOTNET_SIGNALR` * `ASYNC_HTTP_CLIENT` * `AWS_DYNAMO_DB` * `AWS_EVENT_BRIDGE` * `AWS_LAMBDA` * `AWS_RDS` * `AWS_SERVICE` * `AWS_SNS_CLIENT` * `AWS_SQS` * `AXIS` * `AZURE_FUNCTIONS` * `AZURE_SERVICE_BUS` * `AZURE_SERVICE_FABRIC` * `AZURE_STORAGE` * `BOSHBPM` * `BOTTLE` * `CICS_FILE_ACCESS` * `CITRIX` * `CITRIX_COMMON` * `CITRIX_DESKTOP_DELIVERY_CONTROLLERS` * `CITRIX_DIRECTOR` * `CITRIX_LICENSE_SERVER` * `CITRIX_PROVISIONING_SERVICES` * `CITRIX_STOREFRONT` * `CITRIX_VIRTUAL_DELIVERY_AGENT` * `CITRIX_WORKSPACE_ENVIRONMENT_MANAGEMENT` * `CITRIX_XEN` * `CLOUDFOUNDRY` * `CLOUDFOUNDRY_AUCTIONEER` * `CLOUDFOUNDRY_BOSH` * `CLOUDFOUNDRY_GOROUTER` * `CLR` * `CODEIGNITER` * `COLDFUSION` * `CONFLUENT_KAFKA_CLIENT` * `CONTAINERD` * `CORE_DNS` * `COSMOSDB` * `COUCHBASE` * `CRIO` * `CXF` * `DATASTAX` * `DB2` * `DB2_CLIENT` * `DIEGO_CELL` * `DOCKER` * `DOTNET` * `DOTNET_REMOTING` * `DRUPAL` * `DYNATRACE` * `ELASTIC_SEARCH` * `ENVOY` * `ERLANG` * `ETCD` * `F5_LTM` * `FALCON` * `FASTAPI` * `FLASK` * `FSHARP` * `GARDEN` * `GLASSFISH` * `GO` * `GOOGLE_CLOUD_FUNCTIONS` * `GRAAL_NATIVE_IMAGE` * `GRAAL_TRUFFLE` * `GRAPH_QL` * `GRPC` * `GRSECURITY` * `HADOOP` * `HADOOP_HDFS` * `HADOOP_YARN` * `HAPROXY` * `HEAT` * `HELIDON` * `HESSIAN` * `HORNET_Q` * `IBM_CICS_REGION` * `IBM_CICS_TRANSACTION_GATEWAY` * `IBM_IMS_CONNECT_REGION` * `IBM_IMS_CONTROL_REGION` * `IBM_IMS_MESSAGE_PROCESSING_REGION` * `IBM_IMS_SOAP_GATEWAY` * `IBM_INTEGRATION_BUS` * `IBM_MQ` * `IBM_MQ_CLIENT` * `IBM_WEBSHPRERE_APPLICATION_SERVER` * `IBM_WEBSHPRERE_LIBERTY` * `IBM_WEBSPHERE_APPLICATION_SERVER` * `IBM_WEBSPHERE_LIBERTY` * `IIS` * `IIS_APP_POOL` * `ISTIO` * `JAVA` * `JAVA_HTTPURLCONNECTION` * `JAVA_HTTPURLCONNETION` * `JAX_WS` * `JBOSS` * `JBOSS_EAP` * `JBOSS_LOGMANAGER` * `JDK_HTTP_CLIENT` * `JDK_HTTP_SERVER` * `JERSEY` * `JETTY` * `JOOMLA` * `JRUBY` * `JYTHON` * `KOTLIN` * `KOTLIN_COROUTINES` * `KTOR_CLIENT` * `KTOR_SERVER` * `KUBERNETES` * `LAMINAS` * `LARAVEL` * `LIBC` * `LIBVIRT` * `LINKERD` * `LINUX_SYSTEM` * `LOGSTASH_LOGBACK_ENCODER` * `MAGENTO` * `MARIADB` * `MEMCACHED` * `MICRONAUT` * `MICROSOFT_SQL_SERVER` * `MONGODB` * `MONGODB_CLIENT` * `MONGODB_CLIENT_DOTNET` * `MSSQL_CLIENT` * `MULE_ESB` * `MYSQL` * `MYSQL_CONNECTOR` * `NETFLIX_SERVO` * `NETTY` * `NGINX` * `NODE_JS` * `OK_HTTP_CLIENT` * `ONEAGENT_SDK` * `OPENCENSUS` * `OPENSHIFT` * `OPENSTACK_COMPUTE` * `OPENSTACK_CONTROLLER` * `OPENTELEMETRY` * `OPENTRACING` * `OPEN_LIBERTY` * `ORACLE_DATABASE` * `ORACLE_DB_LISTENER` * `ORACLE_WEBLOGIC` * `OWIN` * `OWIN_KATANA` * `PERL` * `PHP` * `PHP_FPM` * `PLAY` * `PODMAN` * `POSTGRE_SQL` * `POSTGRE_SQL_DOTNET_DATA_PROVIDER` * `POWER_DNS` * `PROGRESS` * `PYTHON` * `QOS_LOGBACK` * `QUARKUS` * `R2DBC` * `RABBITMQ_CLIENT` * `RABBIT_MQ` * `REACTOR_CORE` * `REDIS` * `RESTEASY` * `RESTLET` * `RIAK` * `RKE2` * `RSOCKET` * `RUBY` * `RUNC` * `RXJAVA` * `SAG_WEBMETHODS_IS` * `SANIC` * `SAP` * `SAP_HANADB` * `SAP_HYBRIS` * `SAP_MAXDB` * `SAP_SYBASE` * `SCALA` * `SECURITY_SOFTWARE` * `SELINUX` * `SHAREPOINT` * `SHELL` * `SLIM` * `SPARK` * `SPRING` * `SQLITE` * `STARLETTE` * `SYMFONY` * `THRIFT` * `TIBCO` * `TIBCO_BUSINESS_WORKS` * `TIBCO_EMS` * `TORNADO` * `UNDERTOW_IO` * `VARNISH_CACHE` * `VERTX` * `VIM2` * `VIOS` * `VIRTUAL_MACHINE_KVM` * `VIRTUAL_MACHINE_QEMU` * `WCF` * `WILDFLY` * `WINDOWS_CONTAINERS` * `WINDOWS_SYSTEM` * `WINK` * `WORDPRESS` * `YII` * `ZERO_MQ` * `ZOS_CONNECT` |
| verbatimType | string | Non-predefined technology, use for custom technologies. |

```
{



"operator": "EQUALS",



"value": {



"verbatimType": "MyTechnology"



},



"negate": false,



"type": "SIMPLE_TECH"



}
```

### STRING

StringComparison

Parameters

JSON model

#### The `StringComparison` object

Comparison for `STRING` attributes.

| Element | Type | Description |
| --- | --- | --- |
| caseSensitive | boolean | The comparison is case-sensitive (`true`) or insensitive (`false`). |
| operator | string | Operator of the comparison. You can reverse it by setting **negate** to `true`.  Possible values depend on the **type** of the comparison. Find the list of actual models in the description of the **type** field and check the description of the model you need. The element can hold these values * `BEGINS_WITH` * `CONTAINS` * `ENDS_WITH` * `EQUALS` * `EXISTS` * `REGEX_MATCHES` |
| value | string | The value to compare to. |

```
{



"operator": "CONTAINS",



"value": "myValue",



"negate": false,



"type": "STRING",



"caseSensitive": true



}
```

### SYNTHETIC\_ENGINE\_TYPE

SyntheticEngineTypeComparison

Parameters

JSON model

#### The `SyntheticEngineTypeComparison` object

Comparison for `SYNTHETIC_ENGINE_TYPE` attributes.

| Element | Type | Description |
| --- | --- | --- |
| operator | string | Operator of the comparison. You can reverse it by setting **negate** to `true`.  Possible values depend on the **type** of the comparison. Find the list of actual models in the description of the **type** field and check the description of the model you need. The element can hold these values * `EQUALS` * `EXISTS` |
| value | string | The value to compare to. The element can hold these values * `CLASSIC` * `CUSTOM` |

```
{



"operator": "EQUALS",



"value": "CLASSIC",



"negate": false,



"type": "SYNTHETIC_ENGINE_TYPE"



}
```

### TAG

TagComparison

Parameters

JSON model

#### The `TagComparison` object

Comparison for `TAG` attributes.

| Element | Type | Description |
| --- | --- | --- |
| operator | string | Operator of the comparison. You can reverse it by setting **negate** to `true`.  Possible values depend on the **type** of the comparison. Find the list of actual models in the description of the **type** field and check the description of the model you need. The element can hold these values * `EQUALS` * `TAG_KEY_EQUALS` |
| value | [TagInfo](#openapi-definition-TagInfo) | Tag of a Dynatrace entity. |

#### The `TagInfo` object

Tag of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| context | string | The origin of the tag, such as AWS or Cloud Foundry.  Custom tags use the `CONTEXTLESS` value. The element can hold these values * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | The key of the tag.  Custom tags have the tag value here. |
| value | string | The value of the tag.  Not applicable to custom tags. |

```
{



"operator": "TAG_KEY_EQUALS",



"value": {



"context": "CONTEXTLESS",



"key": "hostOS"



},



"negate": false,



"type": "TAG"



}
```

## Related topics

* [Define and apply tags](/managed/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically.")
* [Tags and metadata](/managed/manage/tags-and-metadata "Use tags and metadata to organize data in your Dynatrace environment.")