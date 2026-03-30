---
title: Миграция с Topology and Smartscape API на Monitored entities API
source: https://www.dynatrace.com/docs/dynatrace-api/basics/deprecation-migration-guides/topology-v1-to-entity-v2
scraped: 2026-03-05T21:27:12.459284
---

Topology and Smartscape API устарел начиная с Dynatrace версии 1.263. Его замена -- Monitored entities API. Мы рекомендуем выполнить миграцию на новый API при первой возможности.

Эта миграция затрагивает URL-адреса конечных точек, параметры запросов и параметры тела запроса/ответа, а также область действия токена для аутентификации запросов.

## Новые возможности

Monitored entities API предлагает следующие новые возможности:

* Конечная точка, не зависящая от типа сущности -- вы можете запрашивать любой тип сущности через один и тот же URL
* Мощный entity selector, помогающий фильтровать нужные сущности
* Унифицированный селектор временного интервала
* Настраиваемое возвращаемое значение -- вы можете контролировать, какие свойства сущности включаются в ответ
* Конечные точки типов сущностей
* Конечные точки пользовательских тегов

## Базовый URL

| Новый Monitored entities | Старый Topology and Smartscape |
| --- | --- |
| `/api/v2/entities` | `/api/v1/entity/applications` `/api/v1/entity/infrastrucutre/hosts` `/api/v1/entity/infrastrucutre/processes` `/api/v1/entity/infrastrucutre/process-groups` `/api/v1/entity/services` |
| `/api/v2/entities/custom` | `/api/v1/entity/infrastructure/custom/{customDeviceId}` |
| `/api/v2/tags` | `/api/v1/entity/applications/{meIdentifier}` `/api/v1/entity/infrastrucutre/hosts/{meIdentifier}` `/api/v1/entity/infrastrucutre/process-groups/{meIdentifier}` `/api/v1/entity/services/{meIdentifier}` |

## Область действия токена аутентификации

| Новый Monitored entities | Старый Topology and Smartscape |
| --- | --- |
| **Read entities** (`entities.read`) **Write entities** (`entities.write`) | **Access problem and event feed, metrics, and topology** (`DataExport`) |

## Параметры

Чтобы узнать о новых параметрах запроса/тела, см. документацию отдельных запросов в Monitored entities API.

## Изменения в рабочем процессе

При обновлении до Monitored entities API некоторые рабочие процессы требуют отправки дополнительных запросов или обращения к дополнительным конечным точкам. Обязательно адаптируйте свою автоматизацию соответствующим образом.

### Пагинация

При массовом запросе сущностей используется пагинация для уменьшения размера полезной нагрузки.

1. Укажите количество сущностей на страницу в параметре запроса **pageSize**.
2. Используйте курсор из поля **nextPageKey** предыдущего ответа в параметре запроса **nextPageKey** для получения последующих страниц.

### Создание пользовательских устройств

В Monitored entities API вы не можете назначить теги пользовательскому устройству при создании. Если вам нужно назначить теги пользовательскому устройству, используйте отдельный запрос к конечной точке POST custom tags.

### Отправка данных на пользовательские устройства

В Monitored entities API вы не можете отправлять данные на пользовательские устройства. Используйте вместо этого вызов POST ingest data points.

## Примеры

Вот несколько примеров различий в использовании API.

### Список сущностей

В этом примере мы запрашиваем список хостов, которые были активны в течение последних 2 часов. Кроме того, нам не нужна полная информация о хосте: нужен только режим мониторинга и список тегов, назначенных хосту. Результат ограничен двумя записями.

Сравните следующие вкладки, чтобы увидеть, как это делается с помощью нового Monitored entities API и устаревшего Topology and Smartscape API:

Monitored entities API

Topology and Smartscape API

В Monitored entities API:

* Вы можете контролировать, какие поля возвращаются (через параметр **fields**). В этом примере мы используем поля **monitoringMode** и **tags**. Тип, отображаемое имя и идентификатор сущности всегда включаются в ответ.
* Временной интервал определяется через параметр запроса **from**. Он поддерживает несколько форматов; см. документацию отдельных запросов для получения дополнительной информации.
* Результат запроса разбит на страницы. Вы можете контролировать размер страницы с помощью параметра **pageSize**. В этом примере параметр не установлен, поэтому используется значение по умолчанию -- 50 записей на страницу.

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/entities?fields=properties.monitoringMode,tags&entitySelector=type(%22HOST%22)&from=now-2h
```

#### Параметры запроса

```
fields=properties.monitoringMode,tags


entitySelector=type("HOST")


from=now-2h
```

#### Тело ответа

```
{


"totalCount": 85,


"pageSize": 50,


"nextPageKey": "AQAMdHlwZSgiSE9TV==",


"entities": [


{


"entityId": "HOST-01A00204B50FF735",


"type": "HOST",


"displayName": "easytravel-backend.internal",


"properties": {


"monitoringMode": "FULL_STACK"


},


"tags": [


{


"context": "CONTEXTLESS",


"key": "Stage",


"value": "PreProduction",


"stringRepresentation": "Stage:PreProduction"


},


{


"context": "CONTEXTLESS",


"key": "OS",


"value": "Linux",


"stringRepresentation": "OS:Linux"


},


{


"context": "CONTEXTLESS",


"key": "backend",


"stringRepresentation": "backend"


}


]


},


{


"entityId": "HOST-0AF138A0258C7DFF",


"type": "HOST",


"displayName": "easytravel-frontend.prod",


"properties": {


"monitoringMode": "FULL_STACK"


},


"tags": [


{


"context": "CONTEXTLESS",


"key": "Stage",


"value": "Production",


"stringRepresentation": "Stage:Production"


},


{


"context": "CONTEXTLESS",


"key": "OS",


"value": "Windows",


"stringRepresentation": "OS:Windows"


},


{


"context": "CONTEXTLESS",


"key": "frontend",


"stringRepresentation": "frontend"


}


]


}


]


}
```

В Topology and Smartscape API:

* У вас ограниченный контроль над возвращаемыми полями -- вы можете использовать **includeDetails** для удаления некоторых свойств, но не можете выбрать конкретные поля для включения.
* Временной интервал определяется через параметр запроса **relativeTime**, который предоставляет ограниченный набор предопределённых значений. Также можно использовать поля **startTimestamp** и **endTimestamp**. Кроме того, размер временного интервала ограничен 3 днями.
* Все сущности возвращаются в одной полезной нагрузке; пагинация недоступна.

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/hosts?relativeTime=2hours&includeDetails=false
```

#### Параметры запроса

```
relativeTime=2hours


includeDetails=false
```

#### Тело ответа

```
[


{


"entityId": "HOST-01A00204B50FF735",


"displayName": "easytravel-backend.internal",


"discoveredName": "APM-ET-MF2",


"firstSeenTimestamp": 1627476376157,


"lastSeenTimestamp": 1679410093531,


"tags": [


{


"context": "CONTEXTLESS",


"key": "Stage",


"value": "PreProduction"


},


{


"context": "CONTEXTLESS",


"key": "OS",


"value": "Linux"


},


{


"context": "CONTEXTLESS",


"key": "backend"


}


],


"fromRelationships": {},


"toRelationships": {},


"osType": "LINUX",


"osArchitecture": "X86",


"osVersion": "Ubuntu 20.04.1 LTS (Focal Fossa) (kernel 5.4.0-135-generic)",


"hypervisorType": "VMWARE",


"ipAddresses": [


"192.168.0.1"


],


"bitness": "64bit",


"cpuCores": 4,


"logicalCpuCores": 4,


"monitoringMode": "FULL_STACK",


"networkZoneId": "default",


"agentVersion": {


"major": 1,


"minor": 259,


"revision": 339,


"timestamp": "20230228-182655",


"sourceRevision": ""


},


"consumedHostUnits": 2.0,


"userLevel": "SUPERUSER",


"autoInjection": "ENABLED",


"oneAgentCustomHostName": "easytravel-backend.internal",


"managementZones": [


{


"id": "460039148655162069",


"name": "backend"


}


]


},


{


"entityId": "HOST-0AF138A0258C7DFF",


"displayName": "easytravel-frontend.prod",


"firstSeenTimestamp": 1619706183299,


"lastSeenTimestamp": 1679409948352,


"tags": [


{


"context": "CONTEXTLESS",


"key": "Stage",


"value": "Production",


"stringRepresentation": "Stage:Production"


},


{


"context": "CONTEXTLESS",


"key": "OS",


"value": "Windows",


"stringRepresentation": "OS:Windows"


},


{


"context": "CONTEXTLESS",


"key": "frontend",


"stringRepresentation": "frontend"


}


],


"fromRelationships": {},


"toRelationships": {},


"osType": "WINDOWS",


"osArchitecture": "X86",


"osVersion": "Windows Server 2008 R2 Datacenter Service Pack 1, ver. 6.1.7601",


"hypervisorType": "XEN",


"ipAddresses": [


"192.168.0.2",


"192.168.0.3"


],


"bitness": "64bit",


"cpuCores": 1,


"logicalCpuCores": 2,


"cloudType": "EC2",


"monitoringMode": "FULL_STACK",


"networkZoneId": "default",


"agentVersion": {


"major": 1,


"minor": 247,


"revision": 277,


"timestamp": "20221006-094946",


"sourceRevision": ""


},


"consumedHostUnits": 0.5,


"userLevel": "SUPERUSER",


"autoInjection": "ENABLED",


"softwareTechnologies": [


{


"type": "CITRIX",


"edition": null,


"version": null


}


],


"managementZones": [


{


"id": "-4279023605659327282",


"name": "frontend"


}


]


}


]
```

### Назначение тегов сущностям

В этом примере мы назначаем дополнительные теги (**Datacenter:Linz** и **Rack:014**) хостам из примера со списком сущностей.

Сравните следующие вкладки, чтобы увидеть, как это делается с помощью нового Monitored entities API и устаревшего Topology and Smartscape API:

Monitored entities API

Topology and Smartscape API

В новом Monitored entities API вы можете назначать теги нескольким сущностям одновременно, выбирая их через entity selector. В этом примере мы выбираем хосты по их идентификаторам сущностей.

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/tags?entitySelector=entityId(%22HOST-01A00204B50FF735%22,%22HOST-0AF138A0258C7DFF%22)
```

#### Параметры запроса

```
entitySelector=entityId("HOST-01A00204B50FF735","HOST-0AF138A0258C7DFF")
```

#### Тело запроса

```
{


"tags": [


{


"key": "Datacenter",


"value": "Linz"


},


{


"key": "Rack",


"value": "014"


}


]


}
```

#### Тело ответа

```
{


"matchedEntitiesCount": 2,


"appliedTags": [


{


"context": "CONTEXTLESS",


"key": "Datacenter",


"value": "Linz",


"stringRepresentation": "Datacenter:Linz"


},


{


"context": "CONTEXTLESS",


"key": "Rack",


"value": "014",


"stringRepresentation": "Rack:014"


}


]


}
```

В устаревшем Topology and Smartscape API вы можете назначать теги только одной сущности за раз. Пример показывает назначение тегов только для одного из двух хостов. Для назначения тегов другому хосту необходим второй запрос с той же полезной нагрузкой.

Кроме того, теги не хранятся в формате `key:value`. Через этот API можно установить только часть `key` тега.

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/hosts/HOST-01A00204B50FF735
```

#### Тело запроса

```
{


"tags": [


"Datacenter:Linz",


"Rack:014"


]


}
```

### Создание пользовательских устройств

В этом примере мы создаём пользовательское устройство с идентификатором `restExample` и следующими параметрами:

* тип: `F5-Firewall`
* IP-адрес `172.16.115.211`
* порт прослушивания `9999`

Сравните следующие вкладки, чтобы увидеть, как это делается с помощью нового Monitored entities API и устаревшего Topology and Smartscape API:

Monitored entities API

Topology and Smartscape API

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/entities/custom
```

#### Тело запроса

```
{


"customDeviceId": "restExample",


"displayName": "F5 Firewall 24",


"ipAddresses": ["172.16.115.211"],


"listenPorts": ["9999"],


"type": "F5-Firewall",


"favicon": "http://assets.dynatrace.com/global/icons/f5.png",


"configUrl": "http://192.128.0.1:8080",


"properties": {


"Sample Property 1": "Sample value 1"


}


}
```

#### Тело ответа

```
{


"entityId": "CUSTOM_DEVICE-1525F193C0578E2C",


"groupId": "CUSTOM_DEVICE_GROUP-FC2E2ABF54F513D8"


}
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/custom/restExample
```

#### Тело запроса

```
{


"displayName": "F5 Firewall 24",


"ipAddresses": ["172.16.115.211"],


"listenPorts": ["9999"],


"type": "F5-Firewall",


"favicon": "http://assets.dynatrace.com/global/icons/f5.png",


"configUrl": "http://192.128.0.1:8080",


"tags": ["REST example"],


"properties": {


"Sample Property 1": "Sample value 1"


}


}
```

#### Тело ответа

```
{


"entityId": "CUSTOM_DEVICE-6A567B33AADC306E",


"groupId": "CUSTOM_DEVICE_GROUP-FC2E2ABF54F513D8"


}
```

## Связанные темы

* Access tokens API
* Tokens API v1
