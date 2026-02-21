---
title: Перейти от Topology и Smartscape API к Monitored entities API
source: https://www.dynatrace.com/docs/dynatrace-api/basics/deprecation-migration-guides/topology-v1-to-entity-v2
scraped: 2026-02-21T21:11:51.298468
---

# Перейти от Topology и Smartscape API к Monitored entities API

# Перейти от Topology и Smartscape API к Monitored entities API

* Ссылка
* Опубликовано 22 марта 2023 г.

[Topology и Smartscape API](/docs/dynatrace-api/environment-api/topology-and-smartscape "Узнайте о Dynatrace Topology и Smartscape API.") был заменен с [Dynatrace версией 1.263](/docs/whats-new/dynatrace-api/sprint-242 "Журнал изменений для Dynatrace API версии 1.242"). Его заменой является [Monitored entities API](/docs/dynatrace-api/environment-api/entity-v2 "Узнайте о Dynatrace Monitored entities API."). Мы рекомендуем перейти на новую API как можно скорее.

Этот переход влияет на URL-адреса конечных точек, параметры запросов и параметры тела запроса/ответа, а также на область действия токена для аутентификации запросов.

## Новые функции

Monitored entities API предлагает следующие новые функции:

* Конечная точка, независимая от типа сущности — вы можете запрашивать любые типы сущностей через один и тот же URL
* Мощный [селектор сущностей](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Настройте селектор сущностей для Environment API конечных точек.") для фильтрации сущностей, которые вы хотите прочитать
* Унифицированный селектор временного интервала
* Настраиваемое возвращаемое значение — вы можете контролировать, какие свойства сущности включены в ответ
* Конечные точки типов сущностей
* Конечные точки пользовательских тегов

## Базовый URL

| новые Monitored entities | старый Topology и Smartscape |
| --- | --- |
| `/api/v2/entities` | `/api/v1/entity/applications` `/api/v1/entity/infrastrucutre/hosts` `/api/v1/entity/infrastrucutre/processes` `/api/v1/entity/infrastrucutre/process-groups` `/api/v1/entity/services` |
| `/api/v2/entities/custom` | `/api/v1/entity/infrastructure/custom/{customDeviceId}` |
| `/api/v2/tags` | `/api/v1/entity/applications/{meIdentifier}` `/api/v1/entity/infrastrucutre/hosts/{meIdentifier}` `/api/v1/entity/infrastrucutre/process-groups/{meIdentifier}` `/api/v1/entity/services/{meIdentifier}` |

## Область действия токена аутентификации

| новые Monitored entities | старый Topology и Smartscape |
| --- | --- |
| **Чтение сущностей** (`entities.read`) **Запись сущностей** (`entities.write`) | **Доступ к ленте проблем и событий, метрикам и топологии** (`DataExport`) |

## Параметры

Чтобы узнать о новых параметрах запроса/тела, см. документацию отдельных запросов в [Monitored entities API](/docs/dynatrace-api/environment-api/entity-v2 "Узнайте о Dynatrace Monitored entities API.").

## Изменения в рабочем процессе

С обновлением до Monitored entities API некоторые рабочие процессы требуют отправки дополнительных запросов или вызова дополнительных конечных точек. Убедитесь, что вы адаптируете свою автоматизацию соответственно.

### Пагинация

Когда вы запрашиваете сущности в批ке, используется пагинация для уменьшения размера полезной нагрузки.

1. Укажите количество сущностей на странице в параметре запроса **pageSize**.
2. Используйте курсор из поля **nextPageKey** предыдущего ответа в параметре запроса **nextPageKey**, чтобы получить последующие страницы.

### Создание пользовательских устройств

В Monitored entities API вы не можете присвоить теги пользовательскому устройству при его создании. Если вам нужно присвоить теги вашему пользовательскому устройству, используйте отдельный запрос к конечной точке [POST пользовательские теги](/docs/dynatrace-api/environment-api/custom-tags/post-tags "Присвойте пользовательские теги отслеживаемым сущностям через Dynatrace API.").

### Отчетность данных в пользовательские устройства

В Monitored entities API вы не можете отчитываться о данных в пользовательские устройства. Вместо этого используйте вызов [POST ингестируемые данные](/docs/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Ингестируйте пользовательские метрики в Dynatrace через Metrics v2 API.").

## Примеры

Вот некоторые примеры различий в использовании API.

### Список сущностей

В этом примере мы запрашиваем список хостов, которые были активны в течение последних 2 часов. Кроме того, нам не нужна полная информация о хосте: нам нужен только режим мониторинга и список тегов, присвоенных хосту. Результат обрезан до двух записей.

Сравните следующие вкладки, чтобы увидеть, как мы делаем это, используя новые Monitored entities API и устаревший Topology и Smartscape API:

Monitored entities API

Topology и Smartscape API

В Monitored entities API:

* Вы можете контролировать, какие поля возвращаются (через параметр **fields**). В этом примере мы используем поля **monitoringMode** и **tags**. Тип, отображаемое имя и идентификатор сущности всегда включены в ответ.
* Временной интервал определяется через параметр запроса **from**. Он поддерживает несколько форматов; см. документацию отдельных запросов, чтобы узнать больше о них.
* Результат запроса разделен на страницы. Вы можете контролировать размер страницы с помощью параметра **pageSize**. В этом примере параметр не установлен; поэтому используется значение по умолчанию — 50 записей на странице.

#### URL-адрес запроса

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



"properties":?



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

В Topology и Smartscape API:

* У вас есть ограниченный контроль над возвращаемыми полями — вы можете использовать **includeDetails**, чтобы удалить некоторые свойства, но вы не можете выбрать конкретные поля для включения.
* Временной интервал определяется через параметр запроса **relativeTime**, который предоставляет ограниченное количество предопределенных значений. Альтернативно вы можете использовать поля **startTimestamp** и **endTimestamp**. Кроме того, размер временного интервала ограничен 3 днями.
* Все сущности возвращаются в одном полезном грузе; пагинация недоступна.

#### URL-адрес запроса

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



"agentVersion":?



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



"agentVersion":?



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



)



],



"managementZones": [



{



"id": "-4279023605659327282",



"name": "frontend"



)



]



)



]



}
```

### Присвоение тегов сущности

В этом примере мы присваиваем дополнительные теги (**Datacenter:Linz** и **Rack:014**) хостам из списка сущностей example.

Сравните следующие вкладки, чтобы увидеть, как мы делаем это с помощью новых Мониторимых сущностей API и устаревшей Топологии и Smartscape API:

Мониторимые сущности API

Топология и Smartscape API

В новых Мониторимых сущностях API вы можете присваивать теги нескольким сущностям одновременно, выбирая их через [селектор сущностей](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Настройте селектор сущностей для Environment API конечных точек."). В этом примере мы выбираем хосты по их идентификаторам сущностей.

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



)



]



}
```

В устаревшей Топологии и Smartscape API вы можете присваивать теги только одной сущности за раз. Пример показывает присвоение тега только одному из двух хостов. Для присвоения тегов другому хосту требуется второй запрос с тем же полезным содержимым.

Кроме того, теги не хранятся в формате `key:value`. Вы можете задать только часть `key` тега через этот API.

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

В этом примере мы создаем пользовательское устройство с идентификатором `restExample` и следующими параметрами:

* тип: `F5-Firewall`
* IP-адрес `172.16.115.211`
* порт прослушивания `9999`

Сравните следующие вкладки, чтобы увидеть, как мы делаем это с помощью новых Мониторимых сущностей API и устаревшей Топологии и Smartscape API:

Мониторимые сущности API

Топология и Smartscape API

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



"properties": 



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



"properties": 



"Sample Property 1": "Sample value 1"



)



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

* [Токены доступа API](/docs/dynatrace-api/environment-api/tokens-v2/api-tokens "Управление Dynatrace API аутентификационными токенами.")
* [Токены API v1](/docs/dynatrace-api/environment-api/tokens-v1 "Узнайте, как управлять Dynatrace API аутентификационными токенами в вашей среде.")