---
title: Hosts API - Получение всех хостов (GET)
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/hosts-api/get-all
scraped: 2026-03-05T21:26:52.254636
---

# Hosts API - Получение всех хостов (GET)

# Hosts API - Получение всех хостов (GET)

* Справочник
* Обновлено 22 мар. 2023
* Устаревший

Этот API устарел. Используйте [Monitored entities API](../../entity-v2.md "Узнайте о Dynatrace Monitored entities API.") вместо него. Дополнительную информацию о переходе на новый API можно найти в [руководстве по миграции](../../../basics/deprecation-migration-guides/topology-v1-to-entity-v2.md "Перенесите вашу автоматизацию на Monitored entities API.").

Получает список всех хостов в вашей среде Dynatrace вместе с их параметрами.

Полный список может быть обширным, поэтому его можно сузить, указав параметры фильтрации, например, теги. Подробнее см. в разделе **Параметры**.

Вы также можете ограничить вывод с помощью пагинации:

1. Укажите количество результатов на странице в параметре запроса **pageSize**.
2. Затем используйте курсор из заголовка ответа **Next-Page-Key** в параметре запроса **nextPageKey** для получения последующих страниц.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/infrastructure/hosts` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/infrastructure/hosts` |

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
| tag | string[] | Фильтрует результирующий набор хостов по указанному тегу. Можно указать несколько тегов в следующем формате: `tag=tag1&tag=tag2`. Хост должен соответствовать **всем** указанным тегам. Для тегов типа ключ-значение, таких как импортированные теги AWS или CloudFoundry, используйте следующий формат: `tag=[context]key:value`. Для пользовательских тегов типа ключ-значение опустите контекст: `tag=key:value`. | query | Необязательный |
| showMonitoringCandidates | boolean | Включает (`true`) или исключает (`false`) кандидатов на мониторинг в ответе. Кандидаты на мониторинг — это сетевые сущности, которые обнаружены, но не мониторятся. | query | Необязательный |
| entity | string[] | Фильтрует результат только по указанным хостам. Для указания нескольких хостов используйте следующий формат: `entity=ID1&entity=ID2`. | query | Необязательный |
| managementZone | integer | Возвращать только хосты, которые являются частью указанной зоны управления. | query | Необязательный |
| hostGroupId | string | Фильтрует результирующий набор хостов по указанной группе хостов. Укажите идентификатор Dynatrace группы хостов, которая вас интересует. | query | Необязательный |
| hostGroupName | string | Фильтрует результирующий набор хостов по указанной группе хостов. Укажите имя группы хостов, которая вас интересует. | query | Необязательный |
| includeDetails | boolean | Включает (`true`) или исключает (`false`) детали, запрашиваемые из связанных сущностей. Исключение деталей может ускорить запросы. Если не задано, используется `true`. | query | Необязательный |
| pageSize | integer | Количество хостов на странице результатов. Если не задано, пагинация не используется и результат содержит все хосты, соответствующие указанным критериям фильтрации. | query | Необязательный |
| nextPageKey | string | Курсор для следующей страницы результатов. Вы можете найти его в заголовке **Next-Page-Key** предыдущего ответа. При использовании пагинации первая страница всегда возвращается без этого курсора. Все остальные параметры запроса должны оставаться такими же, как в первом запросе, для получения последующих страниц. | query | Необязательный |

## Ответ

### Коды ответов

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [Host[]](#openapi-definition-Host) | Успех |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные недопустимы. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ResponseBody`

#### Объект `Host`

Информация о хосте.

| Элемент | Тип | Описание |
| --- | --- | --- |
| agentVersion | [AgentVersion](#openapi-definition-AgentVersion) | Определяет версию агента, работающего в данный момент на сущности. |
| amiId | string | - |
| autoInjection | string | Статус автоинъекции. Элемент может содержать следующие значения * `DISABLED_MANUALLY` * `DISABLED_ON_INSTALLATION` * `DISABLED_ON_SANITY_CHECK` * `ENABLED` * `FAILED_ON_INSTALLATION` |
| autoScalingGroup | string | - |
| awsInstanceId | string | - |
| awsInstanceType | string | - |
| awsNameTag | string | Имя, унаследованное от AWS. |
| awsSecurityGroup | string[] | - |
| azureComputeModeName | string | -Элемент может содержать следующие значения * `DEDICATED` * `SHARED` |
| azureEnvironment | string | - |
| azureHostNames | string[] | - |
| azureResourceGroupName | string | - |
| azureResourceId | string | - |
| azureSiteNames | string[] | - |
| azureSku | string | -Элемент может содержать следующие значения * `BASIC` * `DYNAMIC` * `FREE` * `PREMIUM` * `SHARED` * `STANDARD` |
| azureVmName | string | - |
| azureVmScaleSetName | string | - |
| azureVmSizeLabel | string | - |
| azureZone | string | - |
| beanstalkEnvironmentName | string | - |
| bitness | string | -Элемент может содержать следующие значения * `32bit` * `64bit` |
| boshAvailabilityZone | string | Зона доступности Cloud Foundry BOSH. |
| boshDeploymentId | string | Идентификатор развёртывания Cloud Foundry BOSH. |
| boshInstanceId | string | Идентификатор экземпляра Cloud Foundry BOSH. |
| boshInstanceName | string | Имя экземпляра Cloud Foundry BOSH. |
| boshName | string | Имя Cloud Foundry BOSH. |
| boshStemcellVersion | string | Версия stemcell Cloud Foundry BOSH. |
| cloudPlatformVendorVersion | string | Определяет версию поставщика облачной платформы. |
| cloudType | string | -Элемент может содержать следующие значения * `AZURE` * `EC2` * `GOOGLE_CLOUD_PLATFORM` * `OPENSTACK` * `ORACLE` * `UNRECOGNIZED` |
| consumedHostUnits | string | Потреблённые единицы хостов. Применимо только для [классического лицензирования Dynatrace](https://www.dynatrace.com/support/help/shortlink/application-and-infrastructure-host-units) |
| cpuCores | integer | - |
| customizedName | string | Пользовательское имя сущности |
| discoveredName | string | Обнаруженное имя сущности |
| displayName | string | Имя сущности Dynatrace, отображаемое в пользовательском интерфейсе. |
| entityId | string | Идентификатор сущности Dynatrace требуемой сущности. |
| esxiHostName | string | - |
| firstSeenTimestamp | integer | Временная метка первого обнаружения сущности в миллисекундах UTC |
| fromRelationships | object | - |
| gceInstanceId | string | Идентификатор экземпляра Google Compute Engine. |
| gceInstanceName | string | Имя экземпляра Google Compute Engine. |
| gceMachineType | string | Тип машины Google Compute Engine. |
| gceProject | string | Проект Google Compute Engine. |
| gceProjectId | string | Числовой идентификатор проекта Google Compute Engine. |
| gcePublicIpAddresses | string[] | Публичные IP-адреса Google Compute Engine. |
| gcpZone | string | Зона Google Cloud Platform. |
| hostGroup | [HostGroup](#openapi-definition-HostGroup) | - |
| hypervisorType | string | -Элемент может содержать следующие значения * `AHV` * `AWS_NITRO` * `GVISOR` * `HYPERV` * `KVM` * `LPAR` * `QEMU` * `UNRECOGNIZED` * `VIRTUALBOX` * `VMWARE` * `WPAR` * `XEN` |
| ipAddresses | string[] | - |
| isMonitoringCandidate | boolean | - |
| kubernetesCluster | string | Кластер Kubernetes, в котором находится сущность. |
| kubernetesLabels | object | Метки Kubernetes, определённые на сущности. |
| kubernetesNode | string | Узел Kubernetes, на котором находится сущность. |
| lastSeenTimestamp | integer | Временная метка последнего обнаружения сущности в миллисекундах UTC |
| localHostName | string | - |
| localIp | string | - |
| logicalCpuCores | integer | - |
| logicalCpus | integer | Количество логических процессоров экземпляра AIX. |
| managementZones | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | Зоны управления, частью которых является сущность. |
| monitoringMode | string | -Элемент может содержать следующие значения * `FULL_STACK` * `INFRASTRUCTURE` * `OFF` |
| networkZoneId | string | Идентификатор сетевой зоны, в которой находится сущность. |
| oneAgentCustomHostName | string | Пользовательское имя, определённое в конфигурации OneAgent. |
| openStackInstaceType | string | - |
| openstackAvZone | string | - |
| openstackComputeNodeName | string | - |
| openstackProjectName | string | - |
| openstackSecurityGroups | string[] | - |
| openstackVmName | string | - |
| osArchitecture | string | -Элемент может содержать следующие значения * `ARM` * `IA64` * `PARISC` * `PPC` * `PPCLE` * `S390` * `SPARC` * `X86` * `ZOS` |
| osType | string | -Элемент может содержать следующие значения * `AIX` * `DARWIN` * `HPUX` * `LINUX` * `SOLARIS` * `WINDOWS` * `ZOS` |
| osVersion | string | - |
| paasAgentVersions | [AgentVersion[]](#openapi-definition-AgentVersion) | Версии PaaS-агентов, работающих в данный момент на сущности. |
| paasMemoryLimit | integer | - |
| paasType | string | -Элемент может содержать следующие значения * `AWS_ECS_EC2` * `AWS_ECS_FARGATE` * `AWS_LAMBDA` * `AZURE_FUNCTIONS` * `AZURE_WEBSITES` * `CLOUD_FOUNDRY` * `GOOGLE_APP_ENGINE` * `GOOGLE_CLOUD_RUN` * `HEROKU` * `KUBERNETES` * `OPENSHIFT` |
| publicHostName | string | - |
| publicIp | string | - |
| scaleSetName | string | - |
| simultaneousMultithreading | integer | Количество одновременных потоков экземпляра AIX. |
| softwareTechnologies | [TechnologyInfo[]](#openapi-definition-TechnologyInfo) | - |
| tags | [TagInfo[]](#openapi-definition-TagInfo) | Список тегов сущности. |
| toRelationships | object | - |
| userLevel | string | -Элемент может содержать следующие значения * `NON_SUPERUSER` * `NON_SUPERUSER_STRICT` * `SUPERUSER` |
| virtualCpus | integer | Количество виртуальных процессоров экземпляра AIX. |
| vmwareName | string | - |
| zosCPUModelNumber | string | Номер модели процессора. |
| zosCPUSerialNumber | string | Серийный номер процессора. |
| zosLpaName | string | Имя LPAR. |
| zosSystemName | string | Имя системы. |
| zosTotalGeneralPurposeProcessors | integer | Количество назначенных процессоров для этого LPAR. |
| zosTotalPhysicalMemory | integer | Память, назначенная хосту (терабайт). |
| zosTotalZiipProcessors | integer | Количество назначенных вспомогательных процессоров для этого LPAR. |
| zosVirtualization | string | Тип виртуализации на мейнфрейме. |

#### Объект `AgentVersion`

Определяет версию агента, работающего в данный момент на сущности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| major | integer | Номер мажорной версии. |
| minor | integer | Номер минорной версии. |
| revision | integer | Номер ревизии. |
| sourceRevision | string | Строковое представление номера ревизии SVN. |
| timestamp | string | Строка временной метки: формат "yyyymmdd-hhmmss |

#### Объект `HostGroup`

| Элемент | Тип | Описание |
| --- | --- | --- |
| meId | string | Идентификатор сущности Dynatrace для группы хостов. |
| name | string | Имя сущности Dynatrace, отображаемое в пользовательском интерфейсе. |

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



"agentVersion": {



"major": 1,



"minor": 1,



"revision": 1,



"sourceRevision": "string",



"timestamp": "string"



},



"amiId": "string",



"autoInjection": "DISABLED_MANUALLY",



"autoScalingGroup": "string",



"awsInstanceId": "string",



"awsInstanceType": "string",



"awsNameTag": "string",



"awsSecurityGroup": [



"string"



],



"azureComputeModeName": "DEDICATED",



"azureEnvironment": "string",



"azureHostNames": [



"string"



],



"azureResourceGroupName": "string",



"azureResourceId": "string",



"azureSiteNames": [



"string"



],



"azureSku": "BASIC",



"azureVmName": "string",



"azureVmScaleSetName": "string",



"azureVmSizeLabel": "string",



"azureZone": "string",



"beanstalkEnvironmentName": "string",



"bitness": "32bit",



"boshAvailabilityZone": "string",



"boshDeploymentId": "string",



"boshInstanceId": "string",



"boshInstanceName": "string",



"boshName": "string",



"boshStemcellVersion": "string",



"cloudPlatformVendorVersion": "string",



"cloudType": "AZURE",



"consumedHostUnits": "string",



"cpuCores": 1,



"customizedName": "string",



"discoveredName": "string",



"displayName": "string",



"entityId": "string",



"esxiHostName": "string",



"firstSeenTimestamp": 1,



"fromRelationships": {



"isNetworkClientOfHost": [



"string"



]



},



"gceInstanceId": "string",



"gceInstanceName": "string",



"gceMachineType": "string",



"gceProject": "string",



"gceProjectId": "string",



"gcePublicIpAddresses": [



"string"



],



"gcpZone": "string",



"hostGroup": {



"meId": "string",



"name": "string"



},



"hypervisorType": "AHV",



"ipAddresses": [



"string"



],



"isMonitoringCandidate": true,



"kubernetesCluster": "string",



"kubernetesLabels": {},



"kubernetesNode": "string",



"lastSeenTimestamp": 1,



"localHostName": "string",



"localIp": "string",



"logicalCpuCores": 1,



"logicalCpus": 1,



"managementZones": [



{



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



}



],



"monitoringMode": "FULL_STACK",



"networkZoneId": "string",



"oneAgentCustomHostName": "string",



"openStackInstaceType": "string",



"openstackAvZone": "string",



"openstackComputeNodeName": "string",



"openstackProjectName": "string",



"openstackSecurityGroups": [



"string"



],



"openstackVmName": "string",



"osArchitecture": "ARM",



"osType": "AIX",



"osVersion": "string",



"paasAgentVersions": [



{}



],



"paasMemoryLimit": 1,



"paasType": "AWS_ECS_EC2",



"publicHostName": "string",



"publicIp": "string",



"scaleSetName": "string",



"simultaneousMultithreading": 1,



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



"isNetworkClientOfHost": [



"string"



],



"isProcessOf": [



"string"



],



"isSiteOf": [



"string"



],



"runsOn": [



"string"



]



},



"userLevel": "NON_SUPERUSER",



"virtualCpus": 1,



"vmwareName": "string",



"zosCPUModelNumber": "string",



"zosCPUSerialNumber": "string",



"zosLpaName": "string",



"zosSystemName": "string",



"zosTotalGeneralPurposeProcessors": 1,



"zosTotalPhysicalMemory": 1,



"zosTotalZiipProcessors": 1,



"zosVirtualization": "string"



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

В этом примере запрос перечисляет все хосты в среде.

API-токен передаётся в заголовке **Authorization**.

Результат сокращён до двух записей.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/hosts \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/hosts
```

#### Тело ответа

```
[



{



"entityId": "HOST-B7A6F9EE9F366CB5",



"displayName": "tag009",



"discoveredName": "tag009",



"firstSeenTimestamp": 1538473087608,



"lastSeenTimestamp": 1538641647769,



"tags": [



{



"context": "CONTEXTLESS",



"key": "loadtest"



},



{



"context": "CONTEXTLESS",



"key": "host tag"



}



],



"fromRelationships": {



"isNetworkClientOfHost": [



"HOST-80FF8584D8954C1D",



"HOST-A281F848361E79A1"



]



},



"toRelationships": {



"isProcessOf": [



"PROCESS_GROUP_INSTANCE-9146FB8A6A155F93"



],



"isSiteOf": [



"GEOLOC_SITE-F72DF471AE5F56F6"



],



"isNetworkClientOfHost": [



"HOST-80FF8584D8954C1D"



],



"runsOn": [



"PROCESS_GROUP-83D74C22E79B074F"



]



},



"osType": "LINUX",



"osArchitecture": "X86",



"osVersion": "Ubuntu 18.04.1",



"ipAddresses": [



"127.0.0.1",



"192.168.1.1"



],



"bitness": "64bit",



"cpuCores": 4,



"logicalCpuCores": 8,



"consumedHostUnits": 2,



"managementZones": [



{



"id": "6164525246045854296",



"name": "Zone Service E"



},



{



"id": "5678",



"name": "Infrastructure Linux"



}



]



},



{



"entityId": "HOST-2540A456786EEBCA",



"displayName": "RD40",



"discoveredName": "RD40",



"firstSeenTimestamp": 1536455342329,



"lastSeenTimestamp": 1538661752404,



"tags": [



{



"context": "CONTEXTLESS",



"key": "loadtest"



},



],



"fromRelationships": {},



"toRelationships": {



"isProcessOf": [



"PROCESS_GROUP_INSTANCE-0014EF34F2D03461",



"PROCESS_GROUP_INSTANCE-306710DC5239D390"



],



"isSiteOf": [



"GEOLOC_SITE-2D77938DBFF32A41",



"AZURE_REGION-D4D61746B479FE16"



],



"runsOn": [



"PROCESS_GROUP-1527B48A2A57385A",



"PROCESS_GROUP-25544B628ABEDFAB"



]



},



"osType": "WINDOWS",



"osArchitecture": "X86",



"osVersion": "Windows Server 2016 Datacenter",



"hypervisorType": "HYPERV",



"ipAddresses": [



"127.0.0.1"



],



"bitness": "64bit",



"cpuCores": 2,



"logicalCpuCores": 2,



"cloudType": "AZURE",



"paasType": "AZURE_WEBSITES",



"paasMemoryLimit": 3583,



"azureHostNames": [



"contosomomentshkai3q.azurewebsites.net"



],



"azureSiteNames": [



"contosomomentshkai3q"



],



"azureComputeModeName": "DEDICATED",



"azureSku": "STANDARD",



"consumedHostUnits": 0.25,



"managementZones": [



{



"id": "5130731705740636866",



"name": "Windows"



}



]



}



]
```

#### Код ответа

200

## Связанные темы

* [Hosts Classic](../../../../observe/infrastructure-observability/hosts.md "Узнайте, как начать работу с мониторингом хостов, какие показатели влияют на состояние хоста, как настроить пользовательские имена хостов и многое другое.")