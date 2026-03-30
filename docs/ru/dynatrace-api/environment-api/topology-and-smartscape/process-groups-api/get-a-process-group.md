---
title: Process groups API - GET a process group
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/process-groups-api/get-a-process-group
scraped: 2026-03-05T21:27:02.504672
---

# Process groups API — получение группы процессов


* Устарело

Этот API устарел. Используйте вместо него Monitored entities API. Дополнительную информацию о переходе на новый API можно найти в руководстве по миграции.

Получает параметры указанной группы процессов.

Запрос создаёт ответ в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/infrastructure/process-groups/{meIdentifier}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/infrastructure/process-groups/{meIdentifier}` |

## Аутентификация

Для выполнения этого запроса необходим токен доступа с областью видимости `DataExport`.

Чтобы узнать, как его получить и использовать, см. Токены и аутентификация.

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| meIdentifier | string | Идентификатор сущности Dynatrace для запрашиваемой группы процессов. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ProcessGroup](#openapi-definition-ProcessGroup) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ProcessGroup`

Параметры группы процессов.

| Элемент | Тип | Описание |
| --- | --- | --- |
| azureHostName | string | - |
| azureSiteName | string | - |
| customizedName | string | Пользовательское имя сущности |
| discoveredName | string | Обнаруженное имя сущности |
| displayName | string | Имя сущности Dynatrace, отображаемое в интерфейсе. |
| entityId | string | Идентификатор сущности Dynatrace для запрашиваемой сущности. |
| firstSeenTimestamp | integer | Временная метка первого обнаружения сущности, в миллисекундах UTC |
| fromRelationships | object | - |
| lastSeenTimestamp | integer | Временная метка последнего обнаружения сущности, в миллисекундах UTC |
| listenPorts | integer[] | - |
| managementZones | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | Зоны управления, в которые входит сущность. |
| metadata | object | - |
| softwareTechnologies | [TechnologyInfo[]](#openapi-definition-TechnologyInfo) | - |
| tags | [TagInfo[]](#openapi-definition-TagInfo) | Список тегов сущности. |
| toRelationships | object | - |

#### Объект `EntityShortRepresentation`

Краткое представление сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. |
| id | string | Идентификатор сущности Dynatrace. |
| name | string | Имя сущности Dynatrace. |

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
| key | string | Ключ тега. Пользовательские теги содержат значение тега здесь. |
| value | string | Значение тега. Не применимо к пользовательским тегам. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
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


"azureHostName": "string",


"azureSiteName": "string",


"customizedName": "string",


"discoveredName": "string",


"displayName": "string",


"entityId": "string",


"firstSeenTimestamp": 1,


"fromRelationships": {


"isNetworkClientOfProcessGroup": [


"string"


],


"runsOn": [


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


"isInstanceOf": [


"string"


],


"isNetworkClientOfProcessGroup": [


"string"


],


"runsOn": [


"string"


]


}


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

В этом примере запрос получает сведения о группе процессов **PHP-FPM**, имеющей идентификатор **PROCESS\_GROUP-E5C3CC7EC1F80B5B**.

Токен API передаётся в заголовке **Authorization**.

#### Curl

```
curl -X GET \


'https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/process-groups/PROCESS_GROUP-E5C3CC7EC1F80B5B' \


-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/process-groups/PROCESS_GROUP-E5C3CC7EC1F80B5B
```

#### Тело ответа

```
{


"entityId": "PROCESS_GROUP-E5C3CC7EC1F80B5B",


"displayName": "PHP-FPM",


"discoveredName": "PHP-FPM",


"firstSeenTimestamp": 1503909407206,


"lastSeenTimestamp": 1545150389821,


"tags": [],


"fromRelationships": {


"isNetworkClientOfProcessGroup": [


"PROCESS_GROUP-49C926A7091830E3"


],


"runsOn": [


"HOST-249385B2CEBFE51F",


"HOST-890A0495CB619DDF",


"HOST-3FBF48320E4079EF"


]


},


"toRelationships": {


"isInstanceOf": [


"PROCESS_GROUP_INSTANCE-BBFBABB27B2686F2",


"PROCESS_GROUP_INSTANCE-7E988C3503AE8803"


],


"isNetworkClientOfProcessGroup": [


"PROCESS_GROUP-49C926A7091830E3"


],


"runsOn": [


"SERVICE-72503CBDD2AEF066"


]


},


"metadata": {


"hostGroups": [


"authoring"


],


"commandLineArgs": [


"/usr/sbin/php-fpm7.0 --nodaemonize --fpm-config /etc/php/7.0/fpm/php-fpm.conf"


],


"executables": [


"php-fpm7.0"


],


"executablePaths": [


"/usr/sbin/php-fpm7.0"


]


},


"softwareTechnologies": [


{


"type": "SQLITE",


"edition": null,


"version": null


},


{


"type": "PHP",


"edition": "FPM",


"version": "7.0.32"


},


{


"type": "PHP_FPM",


"edition": null,


"version": null


}


]


}
```

#### Код ответа

200

## Связанные темы

* Группы процессов