---
title: API отслеживаемых сущностей - GET все типы сущностей
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/entity-v2/get-all-entity-types
scraped: 2026-05-12T11:57:10.598292
---

# API отслеживаемых сущностей - GET все типы сущностей

# API отслеживаемых сущностей - GET все типы сущностей

* Справочник
* Опубликовано 24 апреля 2020 г.

Возвращает все типы отслеживаемых сущностей, обнаруженных в вашем окружении.

Дополнительно для каждого типа выводится список возможных свойств сущности этого типа. Обратите внимание, что это плейсхолдеры, показывающие какие свойства сущность может иметь в принципе, а не её реальные свойства. Чтобы посмотреть реальные свойства конкретной сущности, используйте запрос [GET an entity](/managed/dynatrace-api/environment-api/entity-v2/get-entity "Получить параметры отслеживаемой сущности через Dynatrace API.").

Размер вывода можно ограничить пагинацией:

1. Укажите число результатов на страницу в query-параметре **pageSize**.
2. Затем используйте курсор из поля **nextPageKey** предыдущего ответа в query-параметре **nextPageKey**, чтобы получать следующие страницы.

Запрос возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/entityTypes` |
| GET | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/entityTypes` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `entities.read`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| nextPageKey | string | Курсор для следующей страницы результатов. Находится в поле **nextPageKey** предыдущего ответа. Первая страница возвращается всегда, если query-параметр **nextPageKey** не указан. Когда **nextPageKey** задан для получения следующих страниц, все остальные query-параметры нужно опустить. | query | Необязательный |
| pageSize | integer | Количество типов сущностей в одном payload ответа. Максимально допустимый размер страницы: 500. Если не задан, используется 50. | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [EntityTypeList](#openapi-definition-EntityTypeList) | Успех |
| **400** | - | Ошибка. Больше типов сущностей для экспорта нет. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `EntityTypeList`

Список свойств всех доступных типов сущностей.

| Поле | Тип | Описание |
| --- | --- | --- |
| nextPageKey | string | Курсор для следующей страницы результатов. На последней странице имеет значение `null`. Используйте его в query-параметре **nextPageKey** для получения следующих страниц результата. |
| pageSize | integer | Количество записей на страницу. |
| totalCount | integer | Общее количество записей в результате. |
| types | [EntityType[]](#openapi-definition-EntityType) | Список метаинформации обо всех доступных типах сущностей. |

#### Объект `EntityType`

Список свойств типа отслеживаемой сущности.

| Поле | Тип | Описание |
| --- | --- | --- |
| dimensionKey | string | Ключ измерения (dimension), используемый в метриках для этой отслеживаемой сущности. |
| displayName | string | Отображаемое имя отслеживаемой сущности. |
| entityLimitExceeded | boolean | Указывает, превышен ли лимит создания сущностей этого типа. Если `true`, Dynatrace автоматически запускает процесс очистки для этого типа. Новые сущности продолжат создаваться, никаких действий не требуется. Применимо только к встроенным (builtin) типам. Для generic-типов создание и обновление блокируются. Generic-тип легко узнать: имя содержит двоеточие, например `my:type`. |
| fromRelationships | [ToPosition[]](#openapi-definition-ToPosition) | Список возможных связей, в которых тип отслеживаемой сущности занимает позицию FROM. |
| managementZones | string | Плейсхолдер для списка зон управления реальной сущности. |
| properties | [EntityTypePropertyDto[]](#openapi-definition-EntityTypePropertyDto) | Список дополнительных свойств типа отслеживаемой сущности. |
| tags | string | Плейсхолдер для списка тегов реальной сущности. |
| toRelationships | [FromPosition[]](#openapi-definition-FromPosition) | Список возможных связей, в которых тип отслеживаемой сущности занимает позицию TO. |
| type | string | Тип отслеживаемой сущности. |

#### Объект `ToPosition`

Позиция TO для связи.

| Поле | Тип | Описание |
| --- | --- | --- |
| id | string | ID связи. |
| toTypes | string[] | Список типов отслеживаемых сущностей, которые могут занимать позицию TO. |

#### Объект `EntityTypePropertyDto`

Свойство отслеживаемой сущности.

| Поле | Тип | Описание |
| --- | --- | --- |
| displayName | string | Отображаемое имя свойства. |
| id | string | ID свойства. |
| type | string | Тип свойства. |

#### Объект `FromPosition`

Позиция FROM для связи.

| Поле | Тип | Описание |
| --- | --- | --- |
| fromTypes | string[] | Список типов отслеживаемых сущностей, которые могут занимать позицию FROM. |
| id | string | ID связи. |

### JSON-модели тела ответа

```
{



"nextPageKey": "AQAAABQBAAAABQ==",



"pageSize": 1,



"totalCount": 1,



"types": [



{



"entityLimitExceeded": "false",



"fromRelationships": [



{



"id": "RUNS_ON_RESOURCE",



"toTypes": [



"CUSTOM_DEVICE"



]



},



{



"id": "IS_NETWORK_CLIENT_OF_HOST",



"toTypes": [



"HOST",



"CUSTOM_DEVICE"



]



}



],



"managementZones": "placeholder for management zones",



"properties": [



{



"id": "BITNESS",



"type": "Enum"



},



{



"id": "CPU_CORES",



"type": "Number"



}



],



"tags": "placeholder for tags",



"toRelationships": [



{



"fromTypes": [



"DISK"



],



"id": "IS_DISK_OF"



},



{



"fromTypes": [



"VMWARE_DATACENTER",



"GEOLOC_SITE"



],



"id": "IS_SITE_OF"



}



],



"type": "HOST"



}



]



}
```

## Пример

В этом примере запрос выводит все типы сущностей, обнаруженных в окружении **mySampleEnv**.

API-токен передаётся в заголовке **Authorization**.

Так как полный результат достаточно длинный, он сокращён до трёх записей. Соответственно, массив **properties** каждой сущности также сокращён до трёх записей.

#### Curl

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/entityTypes' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/entityTypes
```

#### Тело ответа

```
{



"totalCount": 33,



"pageSize": 33,



"types": [



{



"type": "APPLICATION",



"properties": [



{



"id": "applicationType",



"type": "Enum"



},



{



"id": "conditionalName",



"type": "String"



},



{



"id": "customizedName",



"type": "String"



}



],



"tags": "List",



"managementZones": "List",



"fromRelationships": [



{



"id": "calls",



"toTypes": [



"SERVICE"



]



}



],



"toRelationships": []



},



{



"type": "HOST",



"properties": [



{



"id": "ipAddresses",



"type": "List"



},



{



"id": "osType",



"type": "Enum"



},



{



"id": "osVersion",



"type": "String"



}



],



"tags": "List",



"managementZones": "List",



"fromRelationships": [



{



"id": "runsOn",



"toTypes": [



"EC2_INSTANCE",



"VIRTUALMACHINE",



"AZURE_VM",



"OPENSTACK_VM",



"GOOGLE_COMPUTE_ENGINE",



"HYPERVISOR"



]



},



{



"id": "runsOnResource",



"toTypes": [



"CUSTOM_DEVICE"



]



},



{



"id": "isInstanceOf",



"toTypes": [



"HOST_GROUP"



]



},



{



"id": "isNetworkClientOfHost",



"toTypes": [



"HOST",



"CUSTOM_DEVICE"



]



},



{



"id": "candidateTalksWith",



"toTypes": [



"CUSTOM_DEVICE",



"PROCESS_GROUP_INSTANCE"



]



}



],



"toRelationships": [



{



"id": "isProcessOf",



"fromTypes": [



"PROCESS_GROUP_INSTANCE"



]



},



{



"id": "runsOn",



"fromTypes": [



"OPENSTACK_VM",



"PROCESS_GROUP"



]



},



{



"id": "isSiteOf",



"fromTypes": [



"GEOLOC_SITE",



"VMWARE_DATACENTER"



]



},



{



"id": "talksWithCandidate",



"fromTypes": [



"CUSTOM_DEVICE",



"PROCESS_GROUP_INSTANCE"



]



},



{



"id": "isNetworkClientOfHost",



"fromTypes": [



"CUSTOM_DEVICE",



"HOST"



]



},



{



"id": "isDiskOf",



"fromTypes": [



"DISK"



]



},



{



"id": "runsOnHost",



"fromTypes": [



"SERVICE"



]



},



{



"id": "isContainerGroupInstanceOfHost",



"fromTypes": [



"CONTAINER_GROUP_INSTANCE"



]



}



]



},



{



"type": "SERVICE",



"properties": [



{



"id": "mainServiceSoftwareTech",



"type": "Map"



},



{



"id": "port",



"type": "Number"



},



{



"id": "serviceType",



"type": "Enum"



}



],



"tags": "List",



"managementZones": "List",



"fromRelationships": [



{



"id": "runsOn",



"toTypes": [



"CUSTOM_DEVICE_GROUP",



"PROCESS_GROUP"



]



},



{



"id": "runsOnProcessGroupInstance",



"toTypes": [



"CUSTOM_DEVICE",



"PROCESS_GROUP_INSTANCE"



]



},



{



"id": "runsOnHost",



"toTypes": [



"CUSTOM_DEVICE",



"HOST"



]



},



{



"id": "calls",



"toTypes": [



"SERVICE"



]



}



],



"toRelationships": [



{



"id": "calls",



"fromTypes": [



"MOBILE_APPLICATION",



"CUSTOM_APPLICATION",



"HTTP_CHECK",



"APPLICATION",



"SERVICE"



]



}



]



}



]



}
```

#### Код ответа

200

## Связанные темы

* [API пользовательских тегов](/managed/dynatrace-api/environment-api/custom-tags "Управляйте пользовательскими тегами отслеживаемых сущностей через Dynatrace API.")