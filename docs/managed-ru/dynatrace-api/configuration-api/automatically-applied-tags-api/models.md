---
title: Automatically applied tags API - JSON models
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/automatically-applied-tags-api/models
---

# Automatically applied tags API - JSON models

# Automatically applied tags API - JSON models

* Справочник
* Опубликовано 13 авг. 2019 г.

Устарело

Этот API считается устаревшим. Вместо него нужно использовать [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") со схемой [Automatically applied tags](/managed/dynatrace-api/environment-api/settings/schemas/builtin-tags-auto-tagging "View builtin:tags.auto-tagging settings schema table of your monitoring environment via the Dynatrace API.") (`builtin:tags.auto-tagging`).

Некоторые JSON модели API **Automatically applied tags** различаются в зависимости от **type** модели. JSON модели для каждого варианта перечислены ниже.

## Варианты объекта `ConditionKey`

Объект `ConditionKey`, это база для всех условий. Фактический набор полей зависит от **type** условия.

### HOST\_CUSTOM\_METADATA\_KEY

CustomHostMetadataConditionKey

Параметры

JSON модель

#### Объект `CustomHostMetadataConditionKey`

Ключ для динамических атрибутов типа `HOST_CUSTOM_METADATA_KEY`.

| Элемент | Тип | Описание |
| --- | --- | --- |
| dynamicKey | [CustomHostMetadataKey](#openapi-definition-CustomHostMetadataKey) | Ключ атрибута, для которого нужны динамические ключи. В остальных случаях неприменимо, так как в качестве ключа выступает сам атрибут. |

#### Объект `CustomHostMetadataKey`

Ключ атрибута, для которого нужны динамические ключи.

В остальных случаях неприменимо, так как в качестве ключа выступает сам атрибут.

| Элемент | Тип | Описание |
| --- | --- | --- |
| key | string | Фактический ключ пользовательских метаданных. |
| source | string | Источник пользовательских метаданных. Элемент может принимать следующие значения * `ENVIRONMENT` * `GOOGLE_COMPUTE_ENGINE` * `PLUGIN` |

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

Параметры

JSON модель

#### Объект `CustomProcessMetadataConditionKey`

Ключ для динамических атрибутов типа `PROCESS_CUSTOM_METADATA_KEY`.

| Элемент | Тип | Описание |
| --- | --- | --- |
| dynamicKey | [CustomProcessMetadataKey](#openapi-definition-CustomProcessMetadataKey) | Ключ атрибута, для которого нужны динамические ключи. В остальных случаях неприменимо, так как в качестве ключа выступает сам атрибут. |

#### Объект `CustomProcessMetadataKey`

Ключ атрибута, для которого нужны динамические ключи.

В остальных случаях неприменимо, так как в качестве ключа выступает сам атрибут.

| Элемент | Тип | Описание |
| --- | --- | --- |
| key | string | Фактический ключ пользовательских метаданных. |
| source | string | Источник пользовательских метаданных. Элемент может принимать следующие значения * `AGENT` * `CLOUD_FOUNDRY` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` * `PLUGIN` |

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

Параметры

JSON модель

#### Объект `ProcessMetadataConditionKey`

Ключ для динамических атрибутов типа `PROCESS_PREDEFINED_METADATA_KEY`.

| Элемент | Тип | Описание |
| --- | --- | --- |
| dynamicKey | string | Ключ атрибута, для которого нужны динамические ключи. В остальных случаях неприменимо, так как в качестве ключа выступает сам атрибут. Элемент может принимать следующие значения * `AEM_ENV_TYPE` * `AEM_PROGRAM` * `AEM_SERVICE` * `AEM_TIER` * `AMAZON_ECR_IMAGE_ACCOUNT_ID` * `AMAZON_ECR_IMAGE_REGION` * `AMAZON_LAMBDA_FUNCTION_NAME` * `AMAZON_REGION` * `APACHE_CONFIG_PATH` * `APACHE_SPARK_MASTER_IP_ADDRESS` * `ASP_DOT_NET_CORE_APPLICATION_PATH` * `AWS_ECS_CLUSTER` * `AWS_ECS_CONTAINERNAME` * `AWS_ECS_CONTAINER_ARN` * `AWS_ECS_DOCKER_ID` * `AWS_ECS_DOCKER_NAME` * `AWS_ECS_FAMILY` * `AWS_ECS_REVISION` * `AWS_ECS_TASK_ARN` * `AZURE_APP_SERVICE_WEBSITE_INSTANCE_ID` * `AZURE_APP_SERVICE_WEBSITE_OWNER_NAME` * `AZURE_APP_SERVICE_WEBSITE_SITE_NAME` * `AZURE_CONTAINER_APP_ENV_DNS_SUFFIX` * `AZURE_CONTAINER_APP_HOSTNAME` * `AZURE_CONTAINER_APP_NAME` * `AZURE_CONTAINER_APP_REPLICA_NAME` * `AZURE_SERVICE_FABRIC_APPLICATIONID` * `AZURE_SERVICE_FABRIC_APPLICATIONNAME` * `AZURE_SERVICE_FABRIC_CODEPACKAGENAME` * `AZURE_SERVICE_FABRIC_HOSTEDSERVICENAME` * `AZURE_SERVICE_FABRIC_INSTANCEID` * `AZURE_SERVICE_FABRIC_REPLICAID` * `AZURE_SERVICE_FABRIC_SERVICEPACKAGENAME` * `AZURE_SPRING_APPLICATION_NAME` * `AZURE_SPRING_CLOUD_CONFIG_URI` * `CASSANDRA_CLUSTER_NAME` * `CATALINA_BASE` * `CATALINA_HOME` * `CLOUD_FOUNDRY_APP_ID` * `CLOUD_FOUNDRY_APP_NAME` * `CLOUD_FOUNDRY_INSTANCE_INDEX` * `CLOUD_FOUNDRY_SPACE_ID` * `CLOUD_FOUNDRY_SPACE_NAME` * `COLDFUSION_JVM_CONFIG_FILE` * `COLDFUSION_SERVICE_NAME` * `COMMAND_LINE_ARGS` * `CONTAINER_ID` * `CONTAINER_IMAGE_NAME` * `CONTAINER_IMAGE_VERSION` * `CONTAINER_NAME` * `DATASOURCE_MONITORING_CONFIG_ID` * `DECLARATIVE_CONFIG_RULE_ID` * `DECLARATIVE_ID` * `DOTNET_COMMAND` * `DOTNET_COMMAND_PATH` * `DYNATRACE_CLUSTER_ID` * `DYNATRACE_NODE_ID` * `ELASTICSEARCH_CLUSTER_NAME` * `ELASTICSEARCH_NODE_NAME` * `EQUINOX_CONFIG_PATH` * `EXE_NAME` * `EXE_PATH` * `GAE_VERSION` * `GLASS_FISH_DOMAIN_NAME` * `GLASS_FISH_INSTANCE_NAME` * `GOOGLE_APP_ENGINE_INSTANCE` * `GOOGLE_APP_ENGINE_SERVICE` * `GOOGLE_CLOUD_INSTANCE_ID` * `GOOGLE_CLOUD_INSTANCE_REGION` * `GOOGLE_CLOUD_PROJECT` * `GOOGLE_CLOUD_RUN_EXECUTION` * `GOOGLE_CLOUD_RUN_JOB` * `GOOGLE_CLOUD_RUN_REVISION` * `GOOGLE_CLOUD_RUN_SERVICE` * `HEROKU_APP_DEFAULT_DOMAIN_NAME` * `HEROKU_DYNO` * `HEROKU_RELEASE_VERSION` * `HYBRIS_BIN_DIRECTORY` * `HYBRIS_CONFIG_DIRECTORY` * `HYBRIS_DATA_DIRECTORY` * `IBM_APPLID` * `IBM_CICS_IMS_APPLID` * `IBM_CICS_IMS_JOBNAME` * `IBM_CICS_REGION` * `IBM_CTG_NAME` * `IBM_IMS_CONNECT_REGION` * `IBM_IMS_CONTROL_REGION` * `IBM_IMS_MESSAGE_PROCESSING_REGION` * `IBM_IMS_SOAP_GW_NAME` * `IBM_INTEGRATION_NODE_NAME` * `IBM_INTEGRATION_SERVER_NAME` * `IBM_JOBNAME` * `IIS_APP_POOL` * `IIS_ROLE_NAME` * `JAVA_JAR_FILE` * `JAVA_JAR_PATH` * `JAVA_MAIN_CLASS` * `JAVA_MAIN_MODULE` * `JBOSS_HOME` * `JBOSS_MODE` * `JBOSS_SERVER_NAME` * `KUBERNETES_BASE_POD_NAME` * `KUBERNETES_CLUSTER_ID` * `KUBERNETES_CONTAINER_NAME` * `KUBERNETES_FULL_POD_NAME` * `KUBERNETES_NAMESPACE` * `KUBERNETES_POD_UID` * `KUBERNETES_RULE_RESULT` * `MSSQL_INSTANCE_NAME` * `NODE_JS_APP_BASE_DIRECTORY` * `NODE_JS_APP_NAME` * `NODE_JS_SCRIPT_NAME` * `ORACLE_SID` * `OSAGENT_GROUPID_NAME` * `OSAGENT_INSTANCEID_NAME` * `PG_ID_CALC_INPUT_KEY_LINKAGE` * `PHP_SCRIPT_PATH` * `PHP_WORKING_DIRECTORY` * `PYTHON_MODULE` * `PYTHON_SCRIPT` * `PYTHON_SCRIPT_PATH` * `RKE2_TYPE` * `RUBY_APP_ROOT_PATH` * `RUBY_SCRIPT_PATH` * `RULE_RESULT` * `SOFTWAREAG_INSTALL_ROOT` * `SOFTWAREAG_PRODUCTPROPNAME` * `SPRINGBOOT_APP_NAME` * `SPRINGBOOT_PROFILE_NAME` * `SPRINGBOOT_STARTUP_CLASS` * `TIBCO_BUSINESSWORKS_CE_APP_NAME` * `TIBCO_BUSINESSWORKS_CE_VERSION` * `TIBCO_BUSINESS_WORKS_APP_NODE_NAME` * `TIBCO_BUSINESS_WORKS_APP_SPACE_NAME` * `TIBCO_BUSINESS_WORKS_DOMAIN_NAME` * `TIBCO_BUSINESS_WORKS_ENGINE_PROPERTY_FILE` * `TIBCO_BUSINESS_WORKS_ENGINE_PROPERTY_FILE_PATH` * `TIBCO_BUSINESS_WORKS_HOME` * `VARNISH_INSTANCE_NAME` * `WEBSPHERE_LIBERTY_SERVER_NAME` * `WEB_LOGIC_CLUSTER_NAME` * `WEB_LOGIC_DOMAIN_NAME` * `WEB_LOGIC_HOME` * `WEB_LOGIC_NAME` * `WEB_SPHERE_CELL_NAME` * `WEB_SPHERE_CLUSTER_NAME` * `WEB_SPHERE_NODE_NAME` * `WEB_SPHERE_SERVER_NAME` * `Z_CM_VERSION` |

```
{



"attribute": "PROCESS_GROUP_PREDEFINED_METADATA",



"type": "PROCESS_PREDEFINED_METADATA_KEY",



"dynamicKey": "JAVA_JAR_FILE"



}
```

### STRING

StringConditionKey

Параметры

JSON модель

#### Объект `StringConditionKey`

Ключ для динамических атрибутов типа `STRING`.

| Элемент | Тип | Описание |
| --- | --- | --- |
| dynamicKey | string | Ключ атрибута, для которого нужны динамические ключи. В остальных случаях неприменимо, так как в качестве ключа выступает сам атрибут. |

```
{



"attribute": "HOST_GROUP_NAME",



"type": "STRING",



"dynamicKey": "myKey"



}
```

## Варианты объекта `ComparisonBasic`

Объект `ComparisonBasic`, это база для всех операций сравнения. Фактический набор полей зависит от **type** сравнения.

### APPLICATION\_TYPE

ApplicationTypeComparison

Параметры

JSON модель

#### Объект `ApplicationTypeComparison`

Сравнение для атрибутов `APPLICATION_TYPE`.

| Элемент | Тип | Описание |
| --- | --- | --- |
| operator | string | Оператор сравнения. Его можно инвертировать, задав **negate** равным `true`. Возможные значения зависят от **type** сравнения. Список фактических моделей приведён в описании поля **type**, там же нужно проверить описание нужной модели. Элемент может принимать следующие значения * `EQUALS` * `EXISTS` |
| value | string | Значение для сравнения. Элемент может принимать следующие значения * `AGENTLESS_MONITORING` * `AUTO_INJECTED` * `DEFAULT` * `SAAS_VENDOR` |

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

Параметры

JSON model

#### Объект `AzureComputeModeComparison`

Сравнение для атрибутов `AZURE_COMPUTE_MODE`.

| Элемент | Тип | Описание |
| --- | --- | --- |
| operator | string | Оператор сравнения. Можно инвертировать его, установив **negate** в `true`.  Возможные значения зависят от **type** сравнения. Список актуальных моделей приведён в описании поля **type**, там же есть описание нужной модели. Элемент может принимать следующие значения * `EQUALS` * `EXISTS` |
| value | string | Значение для сравнения. Элемент может принимать следующие значения * `DEDICATED` * `SHARED` |

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

Параметры

JSON model

#### Объект `AzureSkuComparision`

Сравнение для атрибутов `AZURE_SKU`.

| Элемент | Тип | Описание |
| --- | --- | --- |
| operator | string | Оператор сравнения. Можно инвертировать его, установив **negate** в `true`.  Возможные значения зависят от **type** сравнения. Список актуальных моделей приведён в описании поля **type**, там же есть описание нужной модели. Элемент может принимать следующие значения * `EQUALS` * `EXISTS` |
| value | string | Значение для сравнения. Элемент может принимать следующие значения * `BASIC` * `DYNAMIC` * `FREE` * `PREMIUM` * `SHARED` * `STANDARD` |

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

Параметры

JSON model

#### Объект `BitnessComparision`

Сравнение для атрибутов `BITNESS`.

| Элемент | Тип | Описание |
| --- | --- | --- |
| operator | string | Оператор сравнения. Можно инвертировать его, установив **negate** в `true`.  Возможные значения зависят от **type** сравнения. Список актуальных моделей приведён в описании поля **type**, там же есть описание нужной модели. Элемент может принимать следующие значения * `EQUALS` * `EXISTS` |
| value | string | Значение для сравнения. Элемент может принимать следующие значения * `32` * `64` |

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

Параметры

JSON model

#### Объект `CloudTypeComparison`

Сравнение для атрибутов `CLOUD_TYPE`.

| Элемент | Тип | Описание |
| --- | --- | --- |
| operator | string | Оператор сравнения. Можно инвертировать его, установив **negate** в `true`.  Возможные значения зависят от **type** сравнения. Список актуальных моделей приведён в описании поля **type**, там же есть описание нужной модели. Элемент может принимать следующие значения * `EQUALS` * `EXISTS` |
| value | string | Значение для сравнения. Элемент может принимать следующие значения * `AZURE` * `EC2` * `GOOGLE_CLOUD_PLATFORM` * `OPENSTACK` * `ORACLE` * `UNRECOGNIZED` |

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

Параметры

JSON model

#### Объект `CustomApplicationTypeComparison`

Сравнение для атрибутов `CUSTOM_APPLICATION_TYPE`.

| Элемент | Тип | Описание |
| --- | --- | --- |
| operator | string | Оператор сравнения. Можно инвертировать его, установив **negate** в `true`.  Возможные значения зависят от **type** сравнения. Список актуальных моделей приведён в описании поля **type**, там же есть описание нужной модели. Элемент может принимать следующие значения * `EQUALS` * `EXISTS` |
| value | string | Значение для сравнения. Элемент может принимать следующие значения * `AMAZON_ECHO` * `DESKTOP` * `EMBEDDED` * `IOT` * `MICROSOFT_HOLOLENS` * `UFO` |

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

Параметры

JSON model

#### Объект `DatabaseTopologyComparison`

Сравнение для атрибутов `DATABASE_TOPOLOGY`.

| Элемент | Тип | Описание |
| --- | --- | --- |
| operator | string | Оператор сравнения. Можно инвертировать его, установив **negate** в `true`.  Возможные значения зависят от **type** сравнения. Список актуальных моделей приведён в описании поля **type**, там же есть описание нужной модели. Элемент может принимать следующие значения * `EQUALS` * `EXISTS` |
| value | string | Значение для сравнения. Элемент может принимать следующие значения * `CLUSTER` * `EMBEDDED` * `FAILOVER` * `IPC` * `LOAD_BALANCING` * `SINGLE_SERVER` * `UNSPECIFIED` |

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

Параметры

JSON model

#### Объект `DcrumDecoderComparison`

Сравнение для атрибутов `DCRUM_DECODER_TYPE`.

| Элемент | Тип | Описание |
| --- | --- | --- |
| operator | string | Оператор сравнения. Можно инвертировать его, установив **negate** в `true`.  Возможные значения зависят от **type** сравнения. Список актуальных моделей приведён в описании поля **type**, там же есть описание нужной модели. Элемент может принимать следующие значения * `EQUALS` * `EXISTS` |
| value | string | Значение для сравнения. Элемент может принимать следующие значения * `ALL_OTHER` * `CITRIX_APPFLOW` * `CITRIX_ICA` * `CITRIX_ICA_OVER_SSL` * `DB2_DRDA` * `HTTP` * `HTTPS` * `HTTP_EXPRESS` * `INFORMIX` * `MYSQL` * `ORACLE` * `SAP_GUI` * `SAP_GUI_OVER_HTTP` * `SAP_GUI_OVER_HTTPS` * `SAP_HANA_DB` * `SAP_RFC` * `SSL` * `TDS` |

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

Параметры

JSON model

#### Объект `EntityIdComparison`

Сравнение для атрибутов `ENTITY_ID`.

| Элемент | Тип | Описание |
| --- | --- | --- |
| operator | string | Оператор сравнения. Можно инвертировать его, установив **negate** в `true`.  Возможные значения зависят от **type** сравнения. Список актуальных моделей приведён в описании поля **type**, там же есть описание нужной модели. Элемент может принимать следующие значения * `EQUALS` |
| value | string | Значение для сравнения. |

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

Параметры

JSON model

#### Объект `HypervisorTypeComparision`

Сравнение для атрибутов `HYPERVISOR_TYPE`.

| Элемент | Тип | Описание |
| --- | --- | --- |
| operator | string | Оператор сравнения. Можно инвертировать его, установив **negate** в `true`.  Возможные значения зависят от **type** сравнения. Список актуальных моделей приведён в описании поля **type**, там же есть описание нужной модели. Элемент может принимать следующие значения * `EQUALS` * `EXISTS` |
| value | string | Значение для сравнения. Элемент может принимать следующие значения * `AHV` * `AWS_NITRO` * `GVISOR` * `HYPER_V` * `KVM` * `LPAR` * `QEMU` * `UNRECOGNIZED` * `VIRTUAL_BOX` * `VMWARE` * `WPAR` * `XEN` |

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

Параметры

JSON model

#### Объект `IndexedNameComparison`

Сравнение для атрибутов `INDEXED_NAME`.

| Элемент | Тип | Описание |
| --- | --- | --- |
| caseSensitive | boolean | Сравнение чувствительно (`true`) или нечувствительно (`false`) к регистру. |
| operator | string | Оператор сравнения. Можно инвертировать его, установив **negate** в `true`.  Возможные значения зависят от **type** сравнения. Список актуальных моделей приведён в описании поля **type**, там же есть описание нужной модели. Элемент может принимать следующие значения * `CONTAINS` * `EQUALS` * `EXISTS` |
| value | string | Значение для сравнения. |

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

Параметры

JSON model

#### Объект `IndexedStringComparison`

Сравнение для атрибутов `INDEXED_STRING`.

| Элемент | Тип | Описание |
| --- | --- | --- |
| caseSensitive | boolean | Сравнение чувствительно (`true`) или нечувствительно (`false`) к регистру. |
| operator | string | Оператор сравнения. Можно инвертировать его, установив **negate** в `true`.  Возможные значения зависят от **type** сравнения. Список актуальных моделей приведён в описании поля **type**, там же есть описание нужной модели. Элемент может принимать следующие значения * `EQUALS` * `EXISTS` |
| value | string | Значение для сравнения. |

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

Параметры

JSON model

#### Объект `IndexedTagComparison`

Сравнение для атрибутов `INDEXED_TAG`.

| Элемент | Тип | Описание |
| --- | --- | --- |
| operator | string | Оператор сравнения. Его можно обратить, установив **negate** в `true`.  Возможные значения зависят от **type** сравнения. Список актуальных моделей приведён в описании поля **type**, там же можно посмотреть описание нужной модели. Элемент может принимать следующие значения * `EQUALS` * `EXISTS` * `TAG_KEY_EQUALS` |
| value | [TagInfo](#openapi-definition-TagInfo) | Тег сущности Dynatrace. |

#### Объект `TagInfo`

Тег сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| context | string | Источник тега, например AWS или Cloud Foundry.  Пользовательские теги используют значение `CONTEXTLESS`. Элемент может принимать следующие значения * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | Ключ тега.  У пользовательских тегов здесь находится значение тега. |
| value | string | Значение тега.  Не применимо к пользовательским тегам. |

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

Параметры

JSON model

#### Объект `IntegerComparison`

Сравнение для атрибутов `INTEGER`.

| Элемент | Тип | Описание |
| --- | --- | --- |
| operator | string | Оператор сравнения. Его можно обратить, установив **negate** в `true`.  Возможные значения зависят от **type** сравнения. Список актуальных моделей приведён в описании поля **type**, там же можно посмотреть описание нужной модели. Элемент может принимать следующие значения * `EQUALS` * `EXISTS` * `GREATER_THAN` * `GREATER_THAN_OR_EQUAL` * `LOWER_THAN` * `LOWER_THAN_OR_EQUAL` |
| value | integer | Значение для сравнения. |

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

Параметры

JSON model

#### Объект `IpAddressComparison`

Сравнение для атрибутов `IP_ADDRESS`.

| Элемент | Тип | Описание |
| --- | --- | --- |
| caseSensitive | boolean | Сравнение учитывает регистр (`true`) или не учитывает (`false`). |
| operator | string | Оператор сравнения. Его можно обратить, установив **negate** в `true`.  Возможные значения зависят от **type** сравнения. Список актуальных моделей приведён в описании поля **type**, там же можно посмотреть описание нужной модели. Элемент может принимать следующие значения * `BEGINS_WITH` * `CONTAINS` * `ENDS_WITH` * `EQUALS` * `EXISTS` * `IS_IP_IN_RANGE` * `REGEX_MATCHES` |
| value | string | Значение для сравнения. |

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

Параметры

JSON model

#### Объект `MobilePlatformComparison`

Сравнение для атрибутов `MOBILE_PLATFORM`.

| Элемент | Тип | Описание |
| --- | --- | --- |
| operator | string | Оператор сравнения. Его можно обратить, установив **negate** в `true`.  Возможные значения зависят от **type** сравнения. Список актуальных моделей приведён в описании поля **type**, там же можно посмотреть описание нужной модели. Элемент может принимать следующие значения * `EQUALS` * `EXISTS` |
| value | string | Значение для сравнения. Элемент может принимать следующие значения * `ANDROID` * `IOS` * `LINUX` * `MAC_OS` * `OTHER` * `TVOS` * `WINDOWS` |

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

Параметры

JSON model

#### Объект `OsArchitectureComparison`

Сравнение для атрибутов `OS_ARCHITECTURE`.

| Элемент | Тип | Описание |
| --- | --- | --- |
| operator | string | Оператор сравнения. Его можно обратить, установив **negate** в `true`.  Возможные значения зависят от **type** сравнения. Список актуальных моделей приведён в описании поля **type**, там же можно посмотреть описание нужной модели. Элемент может принимать следующие значения * `EQUALS` * `EXISTS` |
| value | string | Значение для сравнения. Элемент может принимать следующие значения * `ARM` * `IA64` * `PARISC` * `PPC` * `PPCLE` * `S390` * `SPARC` * `X86` * `ZOS` |

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

Параметры

JSON model

#### Объект `OsTypeComparison`

Сравнение для атрибутов `OS_TYPE`.

| Элемент | Тип | Описание |
| --- | --- | --- |
| operator | string | Оператор сравнения. Его можно обратить, установив **negate** в `true`.  Возможные значения зависят от **type** сравнения. Список актуальных моделей приведён в описании поля **type**, там же можно посмотреть описание нужной модели. Элемент может принимать следующие значения * `EQUALS` * `EXISTS` |
| value | string | Значение для сравнения. Элемент может принимать следующие значения * `AIX` * `DARWIN` * `HPUX` * `LINUX` * `SOLARIS` * `WINDOWS` * `ZOS` |

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

Параметры

JSON model

#### Объект `PaasTypeComparison`

Сравнение для атрибутов `PAAS_TYPE`.

| Элемент | Тип | Описание |
| --- | --- | --- |
| operator | string | Оператор сравнения. Его можно обратить, установив **negate** в `true`.  Возможные значения зависят от **type** сравнения. Список актуальных моделей приведён в описании поля **type**, там же можно посмотреть описание нужной модели. Элемент может принимать следующие значения * `EQUALS` * `EXISTS` |
| value | string | Значение для сравнения. Элемент может принимать следующие значения * `AWS_ECS_EC2` * `AWS_ECS_FARGATE` * `AWS_LAMBDA` * `AZURE_FUNCTIONS` * `AZURE_WEBSITES` * `CLOUD_FOUNDRY` * `GOOGLE_APP_ENGINE` * `GOOGLE_CLOUD_RUN` * `HEROKU` * `KUBERNETES` * `OPENSHIFT` |

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

Параметры

JSON model

#### Объект `ServiceTopologyComparison`

Сравнение для атрибутов `SERVICE_TOPOLOGY`.

| Элемент | Тип | Описание |
| --- | --- | --- |
| operator | string | Оператор сравнения. Его можно обратить, установив **negate** в `true`.  Возможные значения зависят от **type** сравнения. Список актуальных моделей приведён в описании поля **type**, там же можно посмотреть описание нужной модели. Элемент может принимать следующие значения * `EQUALS` * `EXISTS` |
| value | string | Значение для сравнения. Элемент может принимать следующие значения * `EXTERNAL_SERVICE` * `FULLY_MONITORED` * `OPAQUE_SERVICE` |

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

Параметры

JSON model

#### Объект `ServiceTypeComparison`

Сравнение для атрибутов `SERVICE_TYPE`.

| Элемент | Тип | Описание |
| --- | --- | --- |
| operator | string | Оператор сравнения. Его можно обратить, установив **negate** в `true`.  Возможные значения зависят от **type** сравнения. Список актуальных моделей приведён в описании поля **type**, там же можно посмотреть описание нужной модели. Элемент может принимать следующие значения * `EQUALS` * `EXISTS` |
| value | string | Значение для сравнения. Элемент может принимать следующие значения * `BACKGROUND_ACTIVITY` * `CICS_SERVICE` * `CUSTOM_SERVICE` * `DATABASE_SERVICE` * `ENTERPRISE_SERVICE_BUS_SERVICE` * `EXTERNAL` * `IBM_INTEGRATION_BUS_SERVICE` * `IMS_SERVICE` * `MESSAGING_SERVICE` * `QUEUE_LISTENER_SERVICE` * `RMI_SERVICE` * `RPC_SERVICE` * `SPAN` * `UNIFIED` * `WEB_REQUEST_SERVICE` * `WEB_SERVICE` * `ZOS_CONNECT` |

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

Параметры

JSON model

#### Объект `SimpleHostTechComparison`

Сравнение для атрибутов `SIMPLE_HOST_TECH`.

| Элемент | Тип | Описание |
| --- | --- | --- |
| operator | string | Оператор сравнения. Его можно обратить, установив **negate** в `true`.  Возможные значения зависят от **type** сравнения. Список актуальных моделей приведён в описании поля **type**, там же можно посмотреть описание нужной модели. Элемент может принимать следующие значения * `EQUALS` * `EXISTS` |
| value | [SimpleHostTech](#openapi-definition-SimpleHostTech) | Значение для сравнения. |

#### Объект `SimpleHostTech`

Значение для сравнения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| type | string | Предопределённая технология, если технология не предопределена, нужно указать verbatim type. Элемент может принимать следующие значения * `APPARMOR` * `BOSH` * `BOSHBPM` * `CLOUDFOUNDRY` * `CONTAINERD` * `CRIO` * `DIEGO_CELL` * `DOCKER` * `GARDEN` * `GRSECURITY` * `KUBERNETES` * `OPENSHIFT` * `OPENSTACK_COMPUTE` * `OPENSTACK_CONTROLLER` * `SELINUX` |
| verbatimType | string | Непредопределённая технология, используется для пользовательских технологий. |

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

Параметры

JSON model

#### Объект `SimpleTechComparison`

Сравнение для атрибутов `SIMPLE_TECH`.

| Элемент | Тип | Описание |
| --- | --- | --- |
| operator | string | Оператор сравнения. Можно инвертировать, установив **negate** в `true`. Возможные значения зависят от **type** сравнения. Список актуальных моделей приведён в описании поля **type**, там же можно посмотреть описание нужной модели. Элемент может принимать следующие значения * `EQUALS` * `EXISTS` |
| value | [SimpleTech](#openapi-definition-SimpleTech) | Значение для сравнения. |

#### Объект `SimpleTech`

Значение для сравнения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| type | string | Предопределённая технология, если технология не предопределена, нужно указать дословный тип. Элемент может принимать следующие значения * `ACTIVEMQ_CLIENT` * `ACTIVE_MQ` * `ACTIVE_MQ_ARTEMIS` * `ADOBE_EXPERIENCE_MANAGER` * `ADO_NET` * `AIOHTTP` * `AIX` * `AKKA` * `AMAZON_BEDROCK` * `AMAZON_REDSHIFT` * `AMQP` * `APACHE_CAMEL` * `APACHE_CASSANDRA` * `APACHE_COUCH_DB` * `APACHE_DERBY` * `APACHE_HTTP_CLIENT_ASYNC` * `APACHE_HTTP_CLIENT_SYNC` * `APACHE_HTTP_SERVER` * `APACHE_KAFKA` * `APACHE_LOG4J` * `APACHE_PEKKO` * `APACHE_SOLR` * `APACHE_STORM` * `APACHE_SYNAPSE` * `APACHE_TOMCAT` * `APPARMOR` * `APPLICATION_INSIGHTS_SDK` * `ASP_DOTNET` * `ASP_DOTNET_CORE` * `ASP_DOTNET_CORE_SIGNALR` * `ASP_DOTNET_SIGNALR` * `ASYNC_HTTP_CLIENT` * `AWS_DYNAMO_DB` * `AWS_EVENT_BRIDGE` * `AWS_KINESIS` * `AWS_LAMBDA` * `AWS_RDS` * `AWS_S3` * `AWS_SERVICE` * `AWS_SNS_CLIENT` * `AWS_SQS` * `AXIS` * `AZURE_BLOB` * `AZURE_EVENT_HUB` * `AZURE_FUNCTIONS` * `AZURE_SERVICE_BUS` * `AZURE_SERVICE_FABRIC` * `AZURE_STORAGE` * `BOSHBPM` * `BOTTLE` * `CICS_FILE_ACCESS` * `CITRIX` * `CITRIX_COMMON` * `CITRIX_DESKTOP_DELIVERY_CONTROLLERS` * `CITRIX_DIRECTOR` * `CITRIX_LICENSE_SERVER` * `CITRIX_PROVISIONING_SERVICES` * `CITRIX_STOREFRONT` * `CITRIX_VIRTUAL_DELIVERY_AGENT` * `CITRIX_WORKSPACE_ENVIRONMENT_MANAGEMENT` * `CITRIX_XEN` * `CLOUDFOUNDRY` * `CLOUDFOUNDRY_AUCTIONEER` * `CLOUDFOUNDRY_BOSH` * `CLOUDFOUNDRY_GOROUTER` * `CLR` * `CODEIGNITER` * `COLDFUSION` * `CONFLUENT_KAFKA_CLIENT` * `CONTAINERD` * `CORE_DNS` * `COSMOSDB` * `COUCHBASE` * `CRIO` * `CXF` * `DATASTAX` * `DB2` * `DB2_CLIENT` * `DIEGO_CELL` * `DOCKER` * `DOTNET` * `DOTNET_REMOTING` * `DRUPAL` * `DYNATRACE` * `ELASTIC_SEARCH` * `ENVOY` * `ERLANG` * `ETCD` * `F5_LTM` * `FALCON` * `FASTAPI` * `FLASK` * `FSHARP` * `GARDEN` * `GLASSFISH` * `GO` * `GOOGLE_CLOUD_FUNCTIONS` * `GRAAL_NATIVE_IMAGE` * `GRAAL_TRUFFLE` * `GRAPH_QL` * `GRPC` * `GRSECURITY` * `HADOOP` * `HADOOP_HDFS` * `HADOOP_YARN` * `HAPROXY` * `HEAT` * `HELIDON` * `HESSIAN` * `HORNET_Q` * `HTTPX` * `IBM_CICS_REGION` * `IBM_CICS_TRANSACTION_GATEWAY` * `IBM_IMS_CONNECT_REGION` * `IBM_IMS_CONTROL_REGION` * `IBM_IMS_MESSAGE_PROCESSING_REGION` * `IBM_IMS_SOAP_GATEWAY` * `IBM_INTEGRATION_BUS` * `IBM_MQ` * `IBM_MQ_CLIENT` * `IBM_WEBSHPRERE_APPLICATION_SERVER` * `IBM_WEBSHPRERE_LIBERTY` * `IBM_WEBSPHERE_APPLICATION_SERVER` * `IBM_WEBSPHERE_LIBERTY` * `IIS` * `IIS_APP_POOL` * `ISTIO` * `JAVA` * `JAVA_HTTPURLCONNECTION` * `JAVA_HTTPURLCONNETION` * `JAX_WS` * `JBOSS` * `JBOSS_EAP` * `JBOSS_LOGMANAGER` * `JDK_HTTP_CLIENT` * `JDK_HTTP_SERVER` * `JERSEY` * `JETTY` * `JOOMLA` * `JRUBY` * `JYTHON` * `KOTLIN` * `KOTLIN_COROUTINES` * `KTOR_CLIENT` * `KTOR_SERVER` * `KUBERNETES` * `LAMINAS` * `LARAVEL` * `LIBC` * `LIBVIRT` * `LINKERD` * `LINUX_SYSTEM` * `LOGSTASH_LOGBACK_ENCODER` * `MAGENTO` * `MARIADB` * `MEMCACHED` * `MICRONAUT` * `MICROSOFT_SQL_SERVER` * `MONGODB` * `MONGODB_CLIENT` * `MONGODB_CLIENT_DOTNET` * `MSSQL_CLIENT` * `MULE_ESB` * `MYSQL` * `MYSQL_CONNECTOR` * `NETFLIX_SERVO` * `NETTY` * `NGINX` * `NODE_JS` * `OK_HTTP_CLIENT` * `ONEAGENT_SDK` * `OPENCENSUS` * `OPENSHIFT` * `OPENSTACK_COMPUTE` * `OPENSTACK_CONTROLLER` * `OPENTELEMETRY` * `OPENTRACING` * `OPEN_LIBERTY` * `ORACLE_DATABASE` * `ORACLE_DB_LISTENER` * `ORACLE_WEBLOGIC` * `OWIN` * `OWIN_KATANA` * `PERL` * `PHP` * `PHP_FPM` * `PLAY` * `PODMAN` * `POSTGRE_SQL` * `POSTGRE_SQL_DOTNET_DATA_PROVIDER` * `POWER_DNS` * `PROGRESS` * `PYTHON` * `QOS_LOGBACK` * `QUARKUS` * `R2DBC` * `RABBITMQ_CLIENT` * `RABBIT_MQ` * `REACTOR_CORE` * `REDIS` * `REQUESTS` * `RESTEASY` * `RESTLET` * `RIAK` * `RKE2` * `RSOCKET` * `RUBY` * `RUNC` * `RXJAVA` * `SAG_WEBMETHODS_IS` * `SANIC` * `SAP` * `SAP_HANADB` * `SAP_HYBRIS` * `SAP_MAXDB` * `SAP_SYBASE` * `SCALA` * `SECURITY_SOFTWARE` * `SELINUX` * `SHAREPOINT` * `SHELL` * `SLIM` * `SPARK` * `SPRING` * `SQLITE` * `STARLETTE` * `SYMFONY` * `THRIFT` * `TIBCO` * `TIBCO_BUSINESS_WORKS` * `TIBCO_EMS` * `TORNADO` * `UNDERTOW_IO` * `URLLIB3` * `VARNISH_CACHE` * `VERTX` * `VIM2` * `VIOS` * `VIRTUAL_MACHINE_KVM` * `VIRTUAL_MACHINE_QEMU` * `WCF` * `WILDFLY` * `WINDOWS_CONTAINERS` * `WINDOWS_SYSTEM` * `WINK` * `WORDPRESS` * `YII` * `ZERO_MQ` * `ZOS_CONNECT` |
| verbatimType | string | Непредопределённая технология, используется для пользовательских технологий. |

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

Параметры

JSON model

#### Объект `StringComparison`

Сравнение для атрибутов `STRING`.

| Элемент | Тип | Описание |
| --- | --- | --- |
| caseSensitive | boolean | Сравнение чувствительно к регистру (`true`) или нечувствительно (`false`). |
| operator | string | Оператор сравнения. Можно инвертировать, установив **negate** в `true`. Возможные значения зависят от **type** сравнения. Список актуальных моделей приведён в описании поля **type**, там же можно посмотреть описание нужной модели. Элемент может принимать следующие значения * `BEGINS_WITH` * `CONTAINS` * `ENDS_WITH` * `EQUALS` * `EXISTS` * `REGEX_MATCHES` |
| value | string | Значение для сравнения. |

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

Параметры

JSON model

#### Объект `SyntheticEngineTypeComparison`

Сравнение для атрибутов `SYNTHETIC_ENGINE_TYPE`.

| Элемент | Тип | Описание |
| --- | --- | --- |
| operator | string | Оператор сравнения. Можно инвертировать, установив **negate** в `true`. Возможные значения зависят от **type** сравнения. Список актуальных моделей приведён в описании поля **type**, там же можно посмотреть описание нужной модели. Элемент может принимать следующие значения * `EQUALS` * `EXISTS` |
| value | string | Значение для сравнения. Элемент может принимать следующие значения * `CLASSIC` * `CUSTOM` |

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

Параметры

JSON model

#### Объект `TagComparison`

Сравнение для атрибутов `TAG`.

| Элемент | Тип | Описание |
| --- | --- | --- |
| operator | string | Оператор сравнения. Можно инвертировать, установив **negate** в `true`. Возможные значения зависят от **type** сравнения. Список актуальных моделей приведён в описании поля **type**, там же можно посмотреть описание нужной модели. Элемент может принимать следующие значения * `EQUALS` * `TAG_KEY_EQUALS` |
| value | [TagInfo](#openapi-definition-TagInfo) | Тег сущности Dynatrace. |

#### Объект `TagInfo`

Тег сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| context | string | Источник происхождения тега, например AWS или Cloud Foundry. Пользовательские теги используют значение `CONTEXTLESS`. Элемент может принимать следующие значения * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | Ключ тега. Для пользовательских тегов здесь указывается значение тега. |
| value | string | Значение тега. Не применимо к пользовательским тегам. |

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

## Связанные темы

* [Определение и применение тегов](/managed/manage/tags-and-metadata/setup/how-to-define-tags "Узнайте, как определять и применять теги вручную и автоматически.")
* [Теги и метаданные](/managed/manage/tags-and-metadata "Используйте теги и метаданные для организации данных в среде Dynatrace.")