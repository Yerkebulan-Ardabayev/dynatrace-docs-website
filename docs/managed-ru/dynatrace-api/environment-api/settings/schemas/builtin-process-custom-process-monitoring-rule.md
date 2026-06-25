---
title: Settings API - Custom process monitoring rules schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-process-custom-process-monitoring-rule
scraped: 2026-05-12T11:41:20.465593
---

# Settings API - Custom process monitoring rules schema table

# Settings API - Custom process monitoring rules schema table

* Published Dec 05, 2023

### Пользовательские правила мониторинга процессов (`builtin:process.custom-process-monitoring-rule)`

Dynatrace OneAgent автоматически мониторит все process groups, обнаруженные в вашем окружении (процессы, работающие во время установки OneAgent, должны быть перезапущены, чтобы запустить мониторинг).

OneAgent дополнительно обеспечивает глубокий мониторинг для всех процессов, которые он может мониторить на уровнях request и PurePath. Задайте правила мониторинга процессов ниже, если не хотите автоматически мониторить все процессы или нужно задать исключение для конкретных процессов.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:process.custom-process-monitoring-rule` | * `group:processes-and-containers.processes` * `group:processes-and-containers` | `HOST_GROUP` - Host Group  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:process.custom-process-monitoring-rule` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:process.custom-process-monitoring-rule` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:process.custom-process-monitoring-rule` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | - | Required |
| Режим `mode` | enum | Возможные значения: * `MONITORING_OFF` * `MONITORING_ON` | Required |
| Условие `condition` | [Condition](#Condition) | - | Required |

##### Объект `Condition`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Цель условия `item` | enum | Возможные значения: * `UNKNOWN` * `APACHE_CONFIG_PATH` * `APACHE_SPARK_MASTER_IP_ADDRESS` * `CATALINA_BASE` * `CATALINA_HOME` * `CLOUD_FOUNDRY_APP_NAME` * `CLOUD_FOUNDRY_INSTANCE_INDEX` * `CLOUD_FOUNDRY_SPACE_ID` * `CLOUD_FOUNDRY_SPACE_NAME` * `COLDFUSION_JVM_CONFIG_FILE` * `CONTAINER_ID` * `CONTAINER_IMAGE_NAME` * `CONTAINER_NAME` * `DECLARATIVE_ID` * `DOTNET_COMMAND` * `DOTNET_COMMAND_PATH` * `ELASTIC_SEARCH_CLUSTER_NAME` * `ELASTIC_SEARCH_NODE_NAME` * `EXE_NAME` * `EXE_PATH` * `GLASSFISH_DOMAIN_NAME` * `GLASSFISH_INSTANCE_NAME` * `IIS_APP_POOL` * `IIS_ROLE_NAME` * `JAVA_JAR_FILE` * `JAVA_JAR_PATH` * `JAVA_MAIN_CLASS` * `JBOSS_MODE` * `JBOSS_HOME` * `JBOSS_SERVER_NAME` * `KUBERNETES_BASEPODNAME` * `KUBERNETES_CONTAINERNAME` * `KUBERNETES_FULLPODNAME` * `KUBERNETES_NAMESPACE` * `KUBERNETES_PODUID` * `NODEJS_APP_NAME` * `NODEJS_SCRIPT_NAME` * `RUXIT_CLUSTER_ID` * `RUXIT_NODE_ID` * `SERVICE_NAME` * `VARNISH_INSTANCE_NAME` * `WEBLOGIC_HOME` * `WEBLOGIC_NAME` * `WEBSPHERE_CELL_NAME` * `WEBSPHERE_CLUSTER_NAME` * `WEBSPHERE_NODE_NAME` * `WEBSPHERE_SERVER_NAME` * `WEBSPHERE_LIBERTY_SERVER_NAME` * `COMMAND_LINE_ARGS` * `AWS_ECR_ACCOUNT_ID` * `AWS_ECR_REGION` * `CONTAINER_IMAGE_VERSION` * `WEBLOGIC_CLUSTER_NAME` * `WEBLOGIC_DOMAIN_NAME` * `AWS_REGION` * `AWS_LAMBDA_FUNCTION_NAME` * `ASP_NET_CORE_APPLICATION_PATH` * `HYBRIS_CONFIG_DIR` * `HYBRIS_DATA_DIR` * `HYBRIS_BIN_DIR` * `NODEJS_APP_BASE_DIR` * `TIPCO_BUSINESSWORKS_PROPERTY_FILE` * `TIPCO_BUSINESSWORKS_PROPERTY_FILE_PATH` * `CLOUD_FOUNDRY_APPLICATION_ID` * `IIB_BROKER_NAME` * `IIB_EXECUTION_GROUP_NAME` * `PHP_CLI_SCRIPT_PATH` * `PHP_CLI_WORKING_DIR` * `GOOGLE_CLOUD_PROJECT` * `GAE_SERVICE` * `GAE_INSTANCE` * `IBM_CICS_REGION` * `IBM_IMS_CONTROL` * `IBM_IMS_MPR` * `IBM_IMS_CONNECT` * `TIBCO_BUSINESSWORKS_HOME` * `TIBCO_BUSINESSWORKS_DOMAIN_NAME` * `TIBCO_BUSINESSWORKS_APP_SPACE_NAME` * `TIBCO_BUSINESSWORKS_APP_NODE_NAME` * `IBM_CTG_NAME` * `IBM_CICS_IMS_APPLID` * `IBM_CICS_IMS_JOBNAME` * `IBM_APPLID` * `IBM_JOBNAME` * `IBM_IMS_SOAP_GW_NAME` * `Z_CM_VERSION` * `RKE2_TYPE` * `DATASOURCE_MONITORING_CONFIG_ID` * `EQUINOX_CONFIG_PATH` * `SOFTWAREAG_INSTALL_ROOT` * `SOFTWAREAG_PRODUCTPROPNAME` * `AWS_ECS_CLUSTER` * `AWS_ECS_CONTAINERNAME` * `AWS_ECS_FAMILY` * `AWS_ECS_REVISION` * `SPRINGBOOT_STARTUP_CLASS` * `SPRINGBOOT_APP_NAME` * `SPRINGBOOT_PROFILE_NAME` * `ORACLE_SID` * `MSSQL_INSTANCE_NAME` * `TIBCO_BUSINESSWORKS_CE_VERSION` * `TIBCO_BUSINESSWORKS_CE_APP_NAME` * `PG_ID_CALC_INPUT_KEY_LINKAGE` * `AZURE_CONTAINER_APP_NAME` * `AZURE_CONTAINER_APP_ENV_DNS_SUFFIX` * `PYTHON_SCRIPT` * `PYTHON_MODULE` * `PYTHON_SCRIPT_PATH` * `RUBY_SCRIPT_PATH` * `RUBY_APP_ROOT_PATH` | Required |
| Ключ переменной окружения `envVar` | text | поддерживается только с OneAgent 1.167+ | Required |
| Оператор условия `operator` | enum | Возможные значения: * `STARTS` * `NOT_STARTS` * `ENDS` * `NOT_ENDS` * `CONTAINS` * `NOT_CONTAINS` * `EQUALS` * `NOT_EQUALS` * `EXISTS` * `NOT_EXISTS` | Required |
| Значение условия `value` | text | - | Required |