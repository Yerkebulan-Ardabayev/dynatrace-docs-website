---
title: API отслеживаемых сущностей - GET тип сущности
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/entity-v2/get-entity-type
scraped: 2026-05-12T11:57:08.321457
---

# API отслеживаемых сущностей - GET тип сущности

# API отслеживаемых сущностей - GET тип сущности

* Справочник
* Опубликовано 24 апреля 2020 г.

Возвращает список возможных свойств сущности указанного типа. Обратите внимание, что это плейсхолдеры, показывающие какие свойства сущность может иметь в принципе, а не её реальные свойства. Чтобы посмотреть реальные свойства конкретной сущности, используйте запрос [GET an entity](/managed/dynatrace-api/environment-api/entity-v2/get-entity "Получить параметры отслеживаемой сущности через Dynatrace API.").

Запрос возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/entityTypes/{type}` |
| GET | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/entityTypes/{type}` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `entities.read`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| type | string | Требуемый тип сущности. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [EntityType](#openapi-definition-EntityType) | Успех |
| **400** | - | Ошибка. Запрошенный тип отслеживаемой сущности не поддерживает экспорт или не существует. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

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
```

## Пример

В этом примере запрос выводит все возможные свойства сущностей типа **PROCESS\_GROUP\_INSTANCE**.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/entityTypes/PROCESS_GROUP_INSTANCE' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/entityTypes/PROCESS_GROUP_INSTANCE
```

#### Тело ответа

```
{



"type": "PROCESS_GROUP_INSTANCE",



"properties": [



{



"id": "appVersion",



"type": "String"



},



{



"id": "awsNameTag",



"type": "String"



},



{



"id": "azureHostName",



"type": "String"



},



{



"id": "azureSiteName",



"type": "String"



},



{



"id": "bitness",



"type": "Enum"



},



{



"id": "boshName",



"type": "String"



},



{



"id": "conditionalName",



"type": "String"



},



{



"id": "customPgMetadata",



"type": "Map"



},



{



"id": "customizedName",



"type": "String"



},



{



"id": "gardenApplicationNames",



"type": "List"



},



{



"id": "gcpZone",



"type": "String"



},



{



"id": "internalName",



"type": "String"



},



{



"id": "isDockerized",



"type": "Boolean"



},



{



"id": "jvmClrVersion",



"type": "String"



},



{



"id": "jvmVendor",



"type": "String"



},



{



"id": "listenPorts",



"type": "List"



},



{



"id": "metadata",



"type": "List"



},



{



"id": "modules",



"type": "List"



},



{



"id": "oneAgentCustomHostName",



"type": "String"



},



{



"id": "processType",



"type": "Enum"



},



{



"id": "softwareTechnologies",



"type": "List"



},



{



"id": "versionedModules",



"type": "List"



}



],



"tags": "List",



"managementZones": "List",



"fromRelationships": [



{



"id": "isProcessOf",



"toTypes": [



"HOST"



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



"PROCESS_GROUP"



]



},



{



"id": "talksWithCandidate",



"toTypes": [



"HOST"



]



},



{



"id": "isNetworkClientOf",



"toTypes": [



"CUSTOM_DEVICE",



"PROCESS_GROUP_INSTANCE"



]



}



],



"toRelationships": [



{



"id": "runsOnProcessGroupInstance",



"fromTypes": [



"SERVICE"



]



},



{



"id": "isHostGroupOf",



"fromTypes": [



"HOST_GROUP"



]



},



{



"id": "isNetworkClientOf",



"fromTypes": [



"CUSTOM_DEVICE",



"PROCESS_GROUP_INSTANCE"



]



},



{



"id": "candidateTalksWith",



"fromTypes": [



"HOST"



]



}



]



}
```

#### Код ответа

200

## Связанные темы

* [API пользовательских тегов](/managed/dynatrace-api/environment-api/custom-tags "Управляйте пользовательскими тегами отслеживаемых сущностей через Dynatrace API.")