---
title: Processes API - Получение всех процессов (GET)
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/processes-api/get-all
scraped: 2026-03-05T21:26:44.386556
---

* Устаревший

Этот API устарел. Используйте Monitored entities API вместо него. Дополнительную информацию о переходе на новый API можно найти в руководстве по миграции.

Получает список всех процессов в вашей среде Dynatrace вместе с их параметрами и связями.

Полный список может быть обширным, поэтому его можно сузить, указав параметры фильтрации, например, теги. Подробнее см. в разделе **Параметры**.

Вы также можете ограничить вывод с помощью пагинации:

1. Укажите количество результатов на странице в параметре запроса **pageSize**.
2. Затем используйте курсор из заголовка ответа **Next-Page-Key** в параметре запроса **nextPageKey** для получения последующих страниц.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/infrastructure/processes` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/infrastructure/processes` |

## Аутентификация

Для выполнения этого запроса необходим токен доступа с областью действия `DataExport`.

Чтобы узнать, как получить и использовать его, см. Токены и аутентификация.

## Параметры

Временной диапазон ограничен **максимальным периодом в 3 дня**.

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| startTimestamp | integer | Начальная временная метка запрашиваемого временного диапазона в миллисекундах (UTC). Если не задана, используется значение 72 часа назад от текущего момента. | query | Необязательный |
| endTimestamp | integer | Конечная временная метка запрашиваемого временного диапазона в миллисекундах (UTC). Если не задана, используется текущая временная метка. Временной диапазон не должен превышать 3 дня. | query | Необязательный |
| relativeTime | string | Относительный временной диапазон, отсчитываемый назад от текущего момента. Элемент может содержать следующие значения * `min` * `5mins` * `10mins` * `15mins` * `30mins` * `hour` * `2hours` * `6hours` * `day` * `3days` | query | Необязательный |
| tag | string[] | Фильтрует результирующий набор процессов по указанному тегу. Можно указать несколько тегов в следующем формате: `tag=tag1&tag=tag2`. Процесс должен соответствовать **всем** указанным тегам. Для тегов типа ключ-значение, таких как импортированные теги AWS или CloudFoundry, используйте следующий формат: `tag=[context]key:value`. Для пользовательских тегов типа ключ-значение опустите контекст: `tag=key:value`. | query | Необязательный |
| entity | string[] | Фильтрует результат только по указанным процессам. Для указания нескольких процессов используйте следующий формат: `entity=ID1&entity=ID2`. | query | Необязательный |
| hostTag | string[] | Фильтрует процессы по хосту, на котором они работают. Укажите теги интересующего хоста. | query | Необязательный |
| host | string[] | Фильтрует процессы по хосту, на котором они работают. Укажите идентификаторы Dynatrace интересующих хостов. Для указания нескольких хостов используйте следующий формат: `host=hostID1&host=hostID2`. Применяется логика **ИЛИ**. | query | Необязательный |
| actualMonitoringState | string | Фильтрует процессы по фактическому состоянию мониторинга процесса. Элемент может содержать следующие значения * `OFF` * `ON` | query | Необязательный |
| expectedMonitoringState | string | Фильтрует процессы по ожидаемому состоянию мониторинга процесса. Элемент может содержать следующие значения * `OFF` * `ON` | query | Необязательный |
| managementZone | integer | Возвращать только процессы, которые являются частью указанной зоны управления. | query | Необязательный |
| includeDetails | boolean | Включает (`true`) или исключает (`false`) детали, запрашиваемые из связанных сущностей. Исключение деталей может ускорить запросы. Если не задано, используется `true`. | query | Необязательный |
| pageSize | integer | Количество процессов на странице результатов. Если не задано, пагинация не используется и результат содержит все процессы, соответствующие указанным критериям фильтрации. | query | Необязательный |
| nextPageKey | string | Курсор для следующей страницы результатов. Вы можете найти его в заголовке **Next-Page-Key** предыдущего ответа. При использовании пагинации первая страница всегда возвращается без этого курсора. Все остальные параметры запроса должны оставаться такими же, как в первом запросе, для получения последующих страниц. | query | Необязательный |

## Ответ

### Коды ответов

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ProcessGroupInstance[]](#openapi-definition-ProcessGroupInstance) | Успех |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные недопустимы. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ResponseBody`

#### Объект `ProcessGroupInstance`

Параметры процесса.

| Элемент | Тип | Описание |
| --- | --- | --- |
| agentVersions | [AgentVersion[]](#openapi-definition-AgentVersion) | Версии OneAgent, работающих в данный момент на сущности. |
| azureHostName | string | - |
| azureSiteName | string | - |
| bitness | string | -Элемент может содержать следующие значения * `32bit` * `64bit` |
| customizedName | string | Пользовательское имя сущности |
| discoveredName | string | Обнаруженное имя сущности |
| displayName | string | Имя сущности Dynatrace, отображаемое в пользовательском интерфейсе. |
| entityId | string | Идентификатор сущности Dynatrace требуемой сущности. |
| firstSeenTimestamp | integer | Временная метка первого обнаружения сущности в миллисекундах UTC |
| fromRelationships | object | - |
| lastSeenTimestamp | integer | Временная метка последнего обнаружения сущности в миллисекундах UTC |
| listenPorts | integer[] | - |
| managementZones | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | Зоны управления, частью которых является сущность. |
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
| major | integer | Номер мажорной версии. |
| minor | integer | Номер минорной версии. |
| revision | integer | Номер ревизии. |
| sourceRevision | string | Строковое представление номера ревизии SVN. |
| timestamp | string | Строка временной метки: формат "yyyymmdd-hhmmss |

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
| actualMonitoringState | string | Текущее фактическое состояние мониторинга сущности. Элемент может содержать следующие значения * `OFF` * `ON` |
| expectedMonitoringState | string | Состояние мониторинга, ожидаемое из конфигурации. Элемент может содержать следующие значения * `OFF` * `ON` |
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
| context | string | Источник тега, например AWS или Cloud Foundry. Пользовательские теги используют значение `CONTEXTLESS`. Элемент может содержать следующие значения * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
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
| parameterLocation | string | -Элемент может содержать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
[


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


]
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

## Заголовки ответа

| Заголовок | Тип | Описание |
| --- | --- | --- |
| Total-Count | integer | Приблизительное количество результатов. |
| Next-Page-Key | string | Курсор для следующей страницы результатов. Без него вы получите первую страницу снова. |
| Page-Size | string | Максимальное количество результатов на странице. |

## Пример

В этом примере запрос перечисляет все процессы в вашей среде Dynatrace, обнаруженные **за последние 5 минут**.

API-токен передаётся в заголовке **Authorization**.

Результат сокращён до двух записей.

#### Curl

```
curl -X GET \


'https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/processes?relativeTime=5mins' \


-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/processes?relativeTime=5mins
```

#### Тело ответа

```
[


{


"entityId": "PROCESS_GROUP_INSTANCE-EC9688429EB24B6B",


"displayName": "Apache Web Server apache2",


"discoveredName": "Apache Web Server apache2",


"firstSeenTimestamp": 1464951001104,


"lastSeenTimestamp": 1544024894801,


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


443,


80


],


"bitness": "64bit",


"monitoringState": {


"actualMonitoringState": "ON",


"expectedMonitoringState": "ON",


"restartRequired": false


},


"agentVersions": [


{


"major": 1,


"minor": 157,


"revision": 167,


"timestamp": "20181127-152923",


"sourceRevision": ""


}


]


},


{


"entityId": "PROCESS_GROUP_INSTANCE-C43E52A77ED8F809",


"displayName": "OneAgent network monitoring",


"discoveredName": "OneAgent network monitoring",


"firstSeenTimestamp": 1543571247077,


"lastSeenTimestamp": 1544024847791,


"tags": [


{


"context": "CONTEXTLESS",


"key": "sample tag"


}


],


"fromRelationships": {


"isProcessOf": [


"HOST-CCEA78FDE257A4B9"


],


"isInstanceOf": [


"PROCESS_GROUP-E2B399E9E7FF43C0"


],


"isNetworkClientOf": [


"PROCESS_GROUP_INSTANCE-9E7865921C2C984E"


]


},


"toRelationships": {},


"metadata": {


"hostGroups": [


"wazuh"


]


},


"softwareTechnologies": [


{


"type": "APMNG",


"edition": null,


"version": null


}


],


"bitness": "64bit",


"monitoringState": {


"actualMonitoringState": "ON",


"expectedMonitoringState": "ON",


"restartRequired": false


}


}


]
```

#### Код ответа

200

## Связанные темы

* Группы процессов