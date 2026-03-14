---
title: Processes API - GET a process
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/processes-api/get-a-process
scraped: 2026-03-05T21:27:00.159340
---

# Processes API — GET процесса


* Справочник
* Обновлено 22 марта 2023 г.
* Устаревший

Этот API устарел. Используйте вместо него [API мониторинга сущностей](../../entity-v2.md "Learn about the Dynatrace Monitored entities API."). Дополнительную информацию о переходе на новый API можно найти в [руководстве по миграции](../../../basics/deprecation-migration-guides/topology-v1-to-entity-v2.md "Migrate your automation to the Monitored entities API.").

Получает параметры указанного [процесса](../../../../observe/infrastructure-observability/process-groups.md "Analyze process groups and customize process group naming, detection, and monitoring.").

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/infrastructure/processes/{meIdentifier}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/infrastructure/processes/{meIdentifier}` |

## Аутентификация

Для выполнения этого запроса вам необходим токен доступа с областью действия `DataExport`.

Чтобы узнать, как получить и использовать его, см. [Токены и аутентификация](../../../../discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication.md).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| meIdentifier | string | Идентификатор сущности Dynatrace требуемого процесса. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ProcessGroupInstance](#openapi-definition-ProcessGroupInstance) | Успешно |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ProcessGroupInstance`

Параметры процесса.

| Элемент | Тип | Описание |
| --- | --- | --- |
| agentVersions | [AgentVersion[]](#openapi-definition-AgentVersion) | Версии OneAgent, работающие в данный момент на сущности. |
| azureHostName | string | - |
| azureSiteName | string | - |
| bitness | string | - Элемент может содержать следующие значения: * `32bit` * `64bit` |
| customizedName | string | Пользовательское имя сущности |
| discoveredName | string | Обнаруженное имя сущности |
| displayName | string | Имя сущности Dynatrace, отображаемое в пользовательском интерфейсе. |
| entityId | string | Идентификатор сущности Dynatrace требуемой сущности. |
| firstSeenTimestamp | integer | Метка времени первого обнаружения сущности в миллисекундах UTC |
| fromRelationships | object | - |
| lastSeenTimestamp | integer | Метка времени последнего обнаружения сущности в миллисекундах UTC |
| listenPorts | integer[] | - |
| managementZones | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | Зоны управления, к которым принадлежит сущность. |
| metadata | object | - |
| modules | string[] | - |
| monitoringState | [MonitoringState](#openapi-definition-MonitoringState) | Определяет текущее состояние мониторинга сущности. |
| softwareTechnologies | [TechnologyInfo[]](#openapi-definition-TechnologyInfo) | - |
| tags | [TagInfo[]](#openapi-definition-TagInfo) | Список тегов сущности. |
| toRelationships | object | - |
| versionedModules | [ProcessGroupInstanceModule[]](#openapi-definition-ProcessGroupInstanceModule) | - |

#### Объект `AgentVersion`

Определяет версию агента, работающего в данный момент на сущности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| major | integer | Номер основной версии. |
| minor | integer | Номер дополнительной версии. |
| revision | integer | Номер ревизии. |
| sourceRevision | string | Строковое представление номера ревизии SVN. |
| timestamp | string | Строка метки времени: формат "yyyymmdd-hhmmss |

#### Объект `EntityShortRepresentation`

Краткое представление сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. |
| id | string | Идентификатор сущности Dynatrace. |
| name | string | Имя сущности Dynatrace. |

#### Объект `MonitoringState`

Определяет текущее состояние мониторинга сущности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| actualMonitoringState | string | Текущее фактическое состояние мониторинга сущности. Элемент может содержать следующие значения: * `OFF` * `ON` |
| expectedMonitoringState | string | Состояние мониторинга, ожидаемое из конфигурации. Элемент может содержать следующие значения: * `OFF` * `ON` |
| restartRequired | boolean | Определяет, требуется ли перезапуск процесса для включения мониторинга |

#### Объект `TechnologyInfo`

| Элемент | Тип | Описание |
| --- | --- | --- |
| edition | string | - |
| type | string | - |
| version | string | - |

#### Объект `TagInfo`

Тег сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| context | string | Источник тега, например AWS или Cloud Foundry. Пользовательские теги используют значение `CONTEXTLESS`. Элемент может содержать следующие значения: * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | Ключ тега. Пользовательские теги содержат здесь значение тега. |
| value | string | Значение тега. Не применимо к пользовательским тегам. |

#### Объект `ProcessGroupInstanceModule`

| Элемент | Тип | Описание |
| --- | --- | --- |
| name | string | - |
| version | string | - |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | Код состояния HTTP |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | - Элемент может содержать следующие значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{


"agentVersions": [


{


"major": 1,


"minor": 1,


"revision": 1,


"sourceRevision": "string",


"timestamp": "string"


}


],


"azureHostName": "string",


"azureSiteName": "string",


"bitness": "32bit",


"customizedName": "string",


"discoveredName": "string",


"displayName": "string",


"entityId": "string",


"firstSeenTimestamp": 1,


"fromRelationships": {


"isInstanceOf": [


"string"


],


"isNetworkClientOf": [


"string"


],


"isProcessOf": [


"string"


]


},


"lastSeenTimestamp": 1,


"listenPorts": [


1


],


"managementZones": [


{


"description": "Dynatrace entity for the REST API example",


"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",


"name": "Dynatrace entity"


}


],


"metadata": {


"adobe.em.env_type": [


"string"


],


"adobe.em.program": [


"string"


],


"adobe.em.service": [


"string"


],


"adobe.em.tier": [


"string"


],


"agentValueMetadata": {},


"apacheConfigPaths": [


"string"


],


"apacheSparkMasterIpAddresses": [


"string"


],


"aspDotNetCoreApplicationPaths": [


"string"


],


"awsEcrImageAccountIds": [


"string"


],


"awsEcrImageRegions": [


"string"


],


"awsEcsCluster": [


"string"


],


"awsEcsContainerARN": [


"string"


],


"awsEcsContainerName": [


"string"


],


"awsEcsDockerID": [


"string"


],


"awsEcsDockerName": [


"string"


],


"awsEcsFamily": [


"string"


],


"awsEcsRevision": [


"string"


],


"awsEcsTaskARN": [


"string"


],


"awsLambdaFunctionNames": [


"string"


],


"awsRegions": [


"string"


],


"azure.containerapp.dnssuffix": [


"string"


],


"azure.containerapp.hostname": [


"string"


],


"azure.containerapp.name": [


"string"


],


"azure.containerapp.replica.name": [


"string"


],


"azure.servicefabric.application.id": [


"string"


],


"azure.servicefabric.application.name": [


"string"


],


"azure.servicefabric.codepackage.name": [


"string"


],


"azure.servicefabric.hostedservice.name": [


"string"


],


"azure.servicefabric.instance.id": [


"string"


],


"azure.servicefabric.replica.id": [


"string"


],


"azure.servicefabric.servicepackage.name": [


"string"


],


"azure.spring.application.name": [


"string"


],


"azure.spring.cloudconfiguri": [


"string"


],


"azure.website.instance.id": [


"string"


],


"azure.website.owner.name": [


"string"


],


"azure.website.site.name": [


"string"


],


"cassandraClusterNames": [


"string"


],


"catalinaBaseValues": [


"string"


],


"catalinaHomeValues": [


"string"


],


"cloudFoundryAppIds": [


"string"


],


"cloudFoundryAppNames": [


"string"


],


"cloudFoundryInstanceIndexes": [


"string"


],


"cloudFoundrySpaceIds": [


"string"


],


"cloudFoundrySpaceNames": [


"string"


],


"cloudfoundryMetadata": {},


"coldfusionJvmConfigFiles": [


"string"


],


"commandLineArgs": [


"string"


],


"datasourceMonitoringConfigId": [


"string"


],


"declarativeConfigRuleId": [


"string"


],


"declarativeId": [


"string"


],


"dockerContainerIds": [


"string"


],


"dockerContainerImageNames": [


"string"


],


"dockerContainerImageVersions": [


"string"


],


"dockerContainerNames": [


"string"


],


"dotNetCommands": [


"string"


],


"dotnetCommandPath": [


"string"


],


"dynatraceClusterIds": [


"string"


],


"dynatraceNodeIds": [


"string"


],


"elasticSearchClusterNames": [


"string"


],


"elasticSearchNodeNames": [


"string"


],


"envVariables": {},


"equinoxConfigPath": [


"string"


],


"executablePaths": [


"string"


],


"executables": [


"string"


],


"glassfishDomainNames": [


"string"


],


"glassfishInstanceNames": [


"string"


],


"google.appengine.version": [


"string"


],


"google.cloudrun.execution": [


"string"


],


"google.cloudrun.job": [


"string"


],


"google.cloudrun.revision": [


"string"


],


"googleAppEngineInstances": [


"string"


],


"googleAppEngineServices": [


"string"


],


"googleCloudInstanceId": [


"string"


],


"googleCloudInstanceRegion": [


"string"


],


"googleCloudProjects": [


"string"


],


"googleCloudRunService": [


"string"


],


"googleComputeEngineMetadata": {},


"heroku.appdefaultdomainname": [


"string"


],


"heroku.dyno": [


"string"


],


"heroku.releaseversion": [


"string"


],


"hostGroups": [


"string"


],


"hybrisBinDirectories": [


"string"


],


"hybrisConfigDirectories": [


"string"


],


"hybrisDataDirectories": [


"string"


],


"ibmApplid": [


"string"


],


"ibmCicsImsApplid": [


"string"


],


"ibmCicsImsJobName": [


"string"


],


"ibmCicsRegion": [


"string"


],


"ibmCtgName": [


"string"


],


"ibmImsConnectRegions": [


"string"


],


"ibmImsControlRegions": [


"string"


],


"ibmImsMessageProcessingRegions": [


"string"


],


"ibmImsSoapGwName": [


"string"


],


"ibmIntegrationNodeName": [


"string"


],


"ibmIntegrationServerName": [


"string"


],


"ibmJobName": [


"string"


],


"iisAppPools": [


"string"


],


"iisRoleNames": [


"string"


],


"javaJarFiles": [


"string"


],


"javaJarPaths": [


"string"


],


"javaMainClasses": [


"string"


],


"javaMainModules": [


"string"


],


"jbossHomes": [


"string"


],


"jbossModes": [


"string"


],


"jbossServerNames": [


"string"


],


"kubernetesAnnotations": {},


"kubernetesBasePodNames": [


"string"


],


"kubernetesClusterId": [


"string"


],


"kubernetesContainerNames": [


"string"


],


"kubernetesFullPodNames": [


"string"


],


"kubernetesNamespaces": [


"string"


],


"kubernetesPodUids": [


"string"


],


"kubernetesRuleResult": [


"string"


],


"linkage": [


"string"


],


"mssqlInstanceName": [


"string"


],


"nodejsAppBaseDirectories": [


"string"


],


"nodejsAppNames": [


"string"


],


"nodejsScriptNames": [


"string"


],


"oracleSid": [


"string"


],


"osagent.groupIdName": [


"string"


],


"osagent.instanceIdName": [


"string"


],


"phpScripts": [


"string"


],


"phpWorkingDirectories": [


"string"


],


"pluginMetadata": {},


"pythonModule": [


"string"


],


"pythonScript": [


"string"


],


"pythonScriptPath": [


"string"


],


"rke2Type": [


"string"


],


"rubyAppRootPaths": [


"string"


],


"rubyScriptPaths": [


"string"


],


"ruleResult": [


"string"


],


"serviceNames": [


"string"


],


"softwareAgInstallRoot": [


"string"


],


"softwareAgProductPropertyName": [


"string"


],


"springBootAppName": [


"string"


],


"springBootProfileName": [


"string"


],


"springBootStartupClass": [


"string"


],


"tibcoBWEnginePropertyFilePaths": [


"string"


],


"tibcoBusinessWorksAppNodeName": [


"string"


],


"tibcoBusinessWorksAppSpaceName": [


"string"


],


"tibcoBusinessWorksCeAppName": [


"string"


],


"tibcoBusinessWorksCeVersion": [


"string"


],


"tibcoBusinessWorksDomainName": [


"string"


],


"tibcoBusinessWorksEnginePropertyFiles": [


"string"


],


"tibcoBusinessWorksHome": [


"string"


],


"varnishInstanceNames": [


"string"


],


"weblogicClusterNames": [


"string"


],


"weblogicDomainNames": [


"string"


],


"weblogicHomeValues": [


"string"


],


"weblogicNames": [


"string"


],


"websphereCellNames": [


"string"


],


"websphereClusterNames": [


"string"


],


"websphereLibertyServerName": [


"string"


],


"websphereNodeNames": [


"string"


],


"websphereServerNames": [


"string"


],


"zCodeModuleVersion": [


"string"


]


},


"modules": [


"string"


],


"monitoringState": {


"actualMonitoringState": "OFF",


"expectedMonitoringState": "OFF",


"restartRequired": true


},


"softwareTechnologies": [


{


"edition": "string",


"type": "string",


"version": "string"


}


],


"tags": [


{


"context": "AWS",


"key": "string",


"value": "string"


}


],


"toRelationships": {


"isNetworkClientOf": [


"string"


],


"runsOnProcessGroupInstance": [


"string"


]


},


"versionedModules": [


{


"name": "string",


"version": "string"


}


]


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

## Пример

В этом примере запрос получает данные процесса **Apache Web Server apache2**, который имеет идентификатор **PROCESS\_GROUP\_INSTANCE-EC9688429EB24B6B**.

Токен API передаётся в заголовке **Authorization**.

#### Curl

```
curl -X GET \


https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/processes/PROCESS_GROUP_INSTANCE-EC9688429EB24B6B \


-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/processes/PROCESS_GROUP_INSTANCE-EC9688429EB24B6B
```

#### Тело ответа

```
{


"entityId": "PROCESS_GROUP_INSTANCE-EC9688429EB24B6B",


"displayName": "Apache Web Server apache2",


"discoveredName": "Apache Web Server apache2",


"firstSeenTimestamp": 1464951001104,


"lastSeenTimestamp": 1545147232609,


"tags": [],


"fromRelationships": {


"isProcessOf": [


"HOST-5FD609AD6757BE7D"


],


"isInstanceOf": [


"PROCESS_GROUP-B34081EFF9E5F516"


]


},


"toRelationships": {


"runsOnProcessGroupInstance": [


"SERVICE-C3173FEB08025322",


"SERVICE-443EACA6DCAEE651",


"SERVICE-B8C88BAA442098CF"


]


},


"metadata": {


"commandLineArgs": [


"/usr/sbin/apache2 -k start"


],


"executables": [


"apache2"


],


"executablePaths": [


"/usr/sbin/apache2"


],


"apacheConfigPaths": [


"/etc/apache2/apache2.conf"


]


},


"softwareTechnologies": [


{


"type": "PHP",


"edition": "Apache",


"version": "5.5.9"


},


{


"type": "APACHE_HTTPD",


"edition": null,


"version": "2.4.7"


},


{


"type": "SQLITE",


"edition": null,


"version": null


}


],


"listenPorts": [


80,


443


],


"bitness": "64bit",


"modules": [


"mod_auth_basic.c",


"mod_authn_file.c",


"mod_negotiation.c",


"mod_dir.c",


"mod_rewrite.c"


],


"monitoringState": {


"actualMonitoringState": "ON",


"expectedMonitoringState": "ON",


"restartRequired": false


},


"agentVersions": [


{


"major": 1,


"minor": 157,


"revision": 210,


"timestamp": "20181213-075558",


"sourceRevision": ""


}


]


}
```

#### Код ответа

200

## Связанные темы

* [Группы процессов](../../../../observe/infrastructure-observability/process-groups.md "Analyze process groups and customize process group naming, detection, and monitoring.")