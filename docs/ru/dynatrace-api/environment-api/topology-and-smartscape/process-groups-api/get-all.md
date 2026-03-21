---
title: Process groups API - Получение всех групп процессов (GET)
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/process-groups-api/get-all
scraped: 2026-03-05T21:27:08.699035
---

* Устаревший

Этот API устарел. Используйте [Monitored entities API](../../entity-v2.md "Узнайте о Dynatrace Monitored entities API.") вместо него. Дополнительную информацию о переходе на новый API можно найти в [руководстве по миграции](../../../basics/deprecation-migration-guides/topology-v1-to-entity-v2.md "Перенесите вашу автоматизацию на Monitored entities API.").

Получает список всех [групп процессов](../../../../observe/infrastructure-observability/process-groups.md "Анализируйте группы процессов и настраивайте именование, обнаружение и мониторинг групп процессов.") в вашей среде Dynatrace вместе с их параметрами и связями.

Полный список может быть обширным, поэтому его можно сузить, указав параметры фильтрации, например, теги. Подробнее см. в разделе **Параметры**.

Вы также можете ограничить вывод с помощью пагинации:

1. Укажите количество результатов на странице в параметре запроса **pageSize**.
2. Затем используйте курсор из заголовка ответа **Next-Page-Key** в параметре запроса **nextPageKey** для получения последующих страниц.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/infrastructure/process-groups` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/infrastructure/process-groups` |

## Аутентификация

Для выполнения этого запроса необходим токен доступа с областью действия `DataExport`.

Чтобы узнать, как получить и использовать его, см. [Токены и аутентификация](../../../../discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication.md).

## Параметры

Временной диапазон ограничен **максимальным периодом в 3 дня**.

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| startTimestamp | integer | Начальная временная метка запрашиваемого временного диапазона в миллисекундах (UTC). Если не задана, используется значение 72 часа назад от текущего момента. | query | Необязательный |
| endTimestamp | integer | Конечная временная метка запрашиваемого временного диапазона в миллисекундах (UTC). Если не задана, используется текущая временная метка. Временной диапазон не должен превышать 3 дня. | query | Необязательный |
| relativeTime | string | Относительный временной диапазон, отсчитываемый назад от текущего момента. Элемент может содержать следующие значения * `min` * `5mins` * `10mins` * `15mins` * `30mins` * `hour` * `2hours` * `6hours` * `day` * `3days` | query | Необязательный |
| tag | string[] | Фильтрует результирующий набор групп процессов по указанному тегу. Можно указать несколько тегов в следующем формате: `tag=tag1&tag=tag2`. Группа процессов должна соответствовать **всем** указанным тегам. Для тегов типа ключ-значение, таких как импортированные теги AWS или CloudFoundry, используйте следующий формат: `tag=[context]key:value`. Для пользовательских тегов типа ключ-значение опустите контекст: `tag=key:value`. | query | Необязательный |
| entity | string[] | Фильтрует результат только по указанным группам процессов. Для указания нескольких групп процессов используйте следующий формат: `entity=ID1&entity=ID2`. | query | Необязательный |
| host | string[] | Фильтрует группы процессов по хосту, на котором они работают. Укажите идентификаторы Dynatrace интересующих хостов. Для указания нескольких хостов используйте следующий формат: `host=hostID1&host=hostID2`. Применяется логика **ИЛИ**. | query | Необязательный |
| managementZone | integer | Возвращать только группы процессов, которые являются частью указанной зоны управления. | query | Необязательный |
| includeDetails | boolean | Включает (`true`) или исключает (`false`) детали, запрашиваемые из связанных сущностей. Исключение деталей может ускорить запросы. Если не задано, используется `true`. | query | Необязательный |
| pageSize | integer | Количество групп процессов на странице результатов. Если не задано, пагинация не используется и результат содержит все группы процессов, соответствующие указанным критериям фильтрации. | query | Необязательный |
| nextPageKey | string | Курсор для следующей страницы результатов. Вы можете найти его в заголовке **Next-Page-Key** предыдущего ответа. При использовании пагинации первая страница всегда возвращается без этого курсора. Все остальные параметры запроса должны оставаться такими же, как в первом запросе, для получения последующих страниц. | query | Необязательный |

## Заголовки ответа

| Заголовок | Тип | Описание |
| --- | --- | --- |
| Total-Count | integer | Приблизительное количество результатов. |
| Next-Page-Key | string | Курсор для следующей страницы результатов. Без него вы получите первую страницу снова. |
| Page-Size | string | Максимальное количество результатов на странице. |

## Ответ

### Коды ответов

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ProcessGroup[]](#openapi-definition-ProcessGroup) | Успех |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные недопустимы. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ResponseBody`

#### Объект `ProcessGroup`

Параметры группы процессов.

| Элемент | Тип | Описание |
| --- | --- | --- |
| azureHostName | string | - |
| azureSiteName | string | - |
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
| context | string | Источник тега, например AWS или Cloud Foundry. Пользовательские теги используют значение `CONTEXTLESS`. Элемент может содержать следующие значения * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | Ключ тега. Пользовательские теги содержат здесь значение тега. |
| value | string | Значение тега. Не применимо к пользовательским тегам. |

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

## Пример

В этом примере запрос перечисляет все группы процессов среды, обнаруженные **за последние 5 минут**.

API-токен передаётся в заголовке **Authorization**.

Результат сокращён до двух записей.

#### Curl

```
curl -X GET \


'https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/process-groups?relativeTime=5mins' \


-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/process-groups?relativeTime=5mins
```

#### Тело ответа

```
[


{


"entityId": "PROCESS_GROUP-B34081EFF9E5F516",


"displayName": "Apache Web Server apache2",


"discoveredName": "Apache Web Server apache2",


"firstSeenTimestamp": 1405316247660,


"lastSeenTimestamp": 1545149212556,


"tags": [],


"fromRelationships": {},


"toRelationships": {


"runsOn": [


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


]


},


{


"entityId": "PROCESS_GROUP-E5C3CC7EC1F80B5B",


"displayName": "PHP-FPM",


"discoveredName": "PHP-FPM",


"firstSeenTimestamp": 1503909407206,


"lastSeenTimestamp": 1545149349700,


"tags": [],


"fromRelationships": {


"runsOn": [


"HOST-74CDC8809AD43931",


"HOST-9A81EACCA0270218"


]


},


"toRelationships": {


"isInstanceOf": [


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


]
```

#### Код ответа

200

## Связанные темы

* [Группы процессов](../../../../observe/infrastructure-observability/process-groups.md "Анализируйте группы процессов и настраивайте именование, обнаружение и мониторинг групп процессов.")