---
title: Hosts API - GET a host
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/hosts-api/get-a-host
scraped: 2026-03-05T21:27:14.657488
---

# Hosts API — GET хоста


* Устарело

Этот API устарел. Используйте Monitored entities API вместо него. Более подробную информацию о переходе на новый API можно найти в руководстве по миграции.

Получает параметры указанного хоста.

Запрос возвращает полезную нагрузку в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/infrastructure/hosts/{meIdentifier}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/infrastructure/hosts/{meIdentifier}` |

## Аутентификация

Для выполнения этого запроса необходим токен доступа с областью `DataExport`.

Чтобы узнать, как получить и использовать его, см. Токены и аутентификация.

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| meIdentifier | string | Идентификатор сущности Dynatrace запрашиваемого хоста. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [Host](#openapi-definition-Host) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `Host`

Информация о хосте.

| Элемент | Тип | Описание |
| --- | --- | --- |
| agentVersion | [AgentVersion](#openapi-definition-AgentVersion) | Определяет версию агента, работающего на сущности в данный момент. |
| amiId | string | - |
| autoInjection | string | Статус автоматической инъекции. Элемент может содержать следующие значения: * `DISABLED_MANUALLY` * `DISABLED_ON_INSTALLATION` * `DISABLED_ON_SANITY_CHECK` * `ENABLED` * `FAILED_ON_INSTALLATION` |
| autoScalingGroup | string | - |
| awsInstanceId | string | - |
| awsInstanceType | string | - |
| awsNameTag | string | Имя, унаследованное от AWS. |
| awsSecurityGroup | string[] | - |
| azureComputeModeName | string | - Элемент может содержать следующие значения: * `DEDICATED` * `SHARED` |
| azureEnvironment | string | - |
| azureHostNames | string[] | - |
| azureResourceGroupName | string | - |
| azureResourceId | string | - |
| azureSiteNames | string[] | - |
| azureSku | string | - Элемент может содержать следующие значения: * `BASIC` * `DYNAMIC` * `FREE` * `PREMIUM` * `SHARED` * `STANDARD` |
| azureVmName | string | - |
| azureVmScaleSetName | string | - |
| azureVmSizeLabel | string | - |
| azureZone | string | - |
| beanstalkEnvironmentName | string | - |
| bitness | string | - Элемент может содержать следующие значения: * `32bit` * `64bit` |
| boshAvailabilityZone | string | Зона доступности Cloud Foundry BOSH. |
| boshDeploymentId | string | Идентификатор развёртывания Cloud Foundry BOSH. |
| boshInstanceId | string | Идентификатор экземпляра Cloud Foundry BOSH. |
| boshInstanceName | string | Имя экземпляра Cloud Foundry BOSH. |
| boshName | string | Имя Cloud Foundry BOSH. |
| boshStemcellVersion | string | Версия stemcell Cloud Foundry BOSH. |
| cloudPlatformVendorVersion | string | Определяет версию поставщика облачной платформы. |
| cloudType | string | - Элемент может содержать следующие значения: * `AZURE` * `EC2` * `GOOGLE_CLOUD_PLATFORM` * `OPENSTACK` * `ORACLE` * `UNRECOGNIZED` |
| consumedHostUnits | string | Потреблённые единицы хоста. Применимо только для [классического лицензирования Dynatrace](https://www.dynatrace.com/support/help/shortlink/application-and-infrastructure-host-units) |
| cpuCores | integer | - |
| customizedName | string | Пользовательское имя сущности |
| discoveredName | string | Обнаруженное имя сущности |
| displayName | string | Имя сущности Dynatrace, отображаемое в пользовательском интерфейсе. |
| entityId | string | Идентификатор сущности Dynatrace запрашиваемой сущности. |
| esxiHostName | string | - |
| firstSeenTimestamp | integer | Временная метка первого обнаружения сущности, в миллисекундах UTC |
| fromRelationships | object | - |
| gceInstanceId | string | Идентификатор экземпляра Google Compute Engine. |
| gceInstanceName | string | Имя экземпляра Google Compute Engine. |
| gceMachineType | string | Тип машины Google Compute Engine. |
| gceProject | string | Проект Google Compute Engine. |
| gceProjectId | string | Числовой идентификатор проекта Google Compute Engine. |
| gcePublicIpAddresses | string[] | Публичные IP-адреса Google Compute Engine. |
| gcpZone | string | Зона Google Cloud Platform. |
| hostGroup | [HostGroup](#openapi-definition-HostGroup) | - |
| hypervisorType | string | - Элемент может содержать следующие значения: * `AHV` * `AWS_NITRO` * `GVISOR` * `HYPERV` * `KVM` * `LPAR` * `QEMU` * `UNRECOGNIZED` * `VIRTUALBOX` * `VMWARE` * `WPAR` * `XEN` |
| ipAddresses | string[] | - |
| isMonitoringCandidate | boolean | - |
| kubernetesCluster | string | Кластер Kubernetes, в котором находится сущность. |
| kubernetesLabels | object | Метки Kubernetes, определённые для сущности. |
| kubernetesNode | string | Узел Kubernetes, на котором находится сущность. |
| lastSeenTimestamp | integer | Временная метка последнего обнаружения сущности, в миллисекундах UTC |
| localHostName | string | - |
| localIp | string | - |
| logicalCpuCores | integer | - |
| logicalCpus | integer | Количество логических CPU экземпляра AIX. |
| managementZones | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | Зоны управления, частью которых является сущность. |
| monitoringMode | string | - Элемент может содержать следующие значения: * `FULL_STACK` * `INFRASTRUCTURE` * `OFF` |
| networkZoneId | string | Идентификатор сетевой зоны, в которой находится сущность. |
| oneAgentCustomHostName | string | Пользовательское имя, определённое в конфигурации OneAgent. |
| openStackInstaceType | string | - |
| openstackAvZone | string | - |
| openstackComputeNodeName | string | - |
| openstackProjectName | string | - |
| openstackSecurityGroups | string[] | - |
| openstackVmName | string | - |
| osArchitecture | string | - Элемент может содержать следующие значения: * `ARM` * `IA64` * `PARISC` * `PPC` * `PPCLE` * `S390` * `SPARC` * `X86` * `ZOS` |
| osType | string | - Элемент может содержать следующие значения: * `AIX` * `DARWIN` * `HPUX` * `LINUX` * `SOLARIS` * `WINDOWS` * `ZOS` |
| osVersion | string | - |
| paasAgentVersions | [AgentVersion[]](#openapi-definition-AgentVersion) | Версии PaaS-агентов, работающих на сущности в данный момент. |
| paasMemoryLimit | integer | - |
| paasType | string | - Элемент может содержать следующие значения: * `AWS_ECS_EC2` * `AWS_ECS_FARGATE` * `AWS_LAMBDA` * `AZURE_FUNCTIONS` * `AZURE_WEBSITES` * `CLOUD_FOUNDRY` * `GOOGLE_APP_ENGINE` * `GOOGLE_CLOUD_RUN` * `HEROKU` * `KUBERNETES` * `OPENSHIFT` |
| publicHostName | string | - |
| publicIp | string | - |
| scaleSetName | string | - |
| simultaneousMultithreading | integer | Количество одновременных потоков экземпляра AIX. |
| softwareTechnologies | [TechnologyInfo[]](#openapi-definition-TechnologyInfo) | - |
| tags | [TagInfo[]](#openapi-definition-TagInfo) | Список тегов сущности. |
| toRelationships | object | - |
| userLevel | string | - Элемент может содержать следующие значения: * `NON_SUPERUSER` * `NON_SUPERUSER_STRICT` * `SUPERUSER` |
| virtualCpus | integer | Количество виртуальных CPU экземпляра AIX. |
| vmwareName | string | - |
| zosCPUModelNumber | string | Номер модели CPU. |
| zosCPUSerialNumber | string | Серийный номер CPU. |
| zosLpaName | string | Имя LPAR. |
| zosSystemName | string | Имя системы. |
| zosTotalGeneralPurposeProcessors | integer | Количество назначенных процессоров для этого LPAR. |
| zosTotalPhysicalMemory | integer | Память, назначенная хосту (терабайт). |
| zosTotalZiipProcessors | integer | Количество назначенных вспомогательных процессоров для этого LPAR. |
| zosVirtualization | string | Тип виртуализации на мейнфрейме. |

#### Объект `AgentVersion`

Определяет версию агента, работающего на сущности в данный момент.

| Элемент | Тип | Описание |
| --- | --- | --- |
| major | integer | Номер основной версии. |
| minor | integer | Номер дополнительной версии. |
| revision | integer | Номер ревизии. |
| sourceRevision | string | Строковое представление номера ревизии SVN. |
| timestamp | string | Строка временной метки: формат "yyyymmdd-hhmmss |

#### Объект `HostGroup`

| Элемент | Тип | Описание |
| --- | --- | --- |
| meId | string | Идентификатор сущности Dynatrace группы хостов. |
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
| context | string | Источник тега, например AWS или Cloud Foundry. Пользовательские теги используют значение `CONTEXTLESS`. Элемент может содержать следующие значения: * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | Ключ тега. Пользовательские теги содержат здесь значение тега. |
| value | string | Значение тега. Не применимо к пользовательским тегам. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния |
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

В этом примере запрос получает параметры хоста **tag009**, идентификатор которого **HOST-B7A6F9EE9F366CB5**.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -X GET \


https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/hosts/HOST-B7A6F9EE9F366CB5 \


-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/hosts/HOST-B7A6F9EE9F366CB5
```

#### Тело ответа

```
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


}
```

#### Код ответа

200

## Связанные темы

* Hosts Classic
