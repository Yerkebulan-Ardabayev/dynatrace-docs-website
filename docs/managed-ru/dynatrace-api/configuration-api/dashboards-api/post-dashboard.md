---
title: Dashboards API - POST a dashboard
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/dashboards-api/post-dashboard
---

# Dashboards API - POST a dashboard

# Dashboards API - POST a dashboard

* Reference
* Published Aug 30, 2019

Создаёт новый дашборд.

Запрос принимает и возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/dashboards` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/dashboards` |

## Authentication

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

Подробнее о том, как получить и использовать токен, см. в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

В теле запроса нельзя указывать ID. ID присваивается автоматически Dynatrace.

Модели JSON для каждого типа плитки можно найти в разделе [Tile JSON models](/managed/dynatrace-api/configuration-api/dashboards-api/dashboards-api-tile-models "Learn the variations of tile JSON models in the Dynatrace Dashboards Classic API.").

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [Dashboard](#openapi-definition-Dashboard) | Тело JSON запроса. Содержит параметры нового дашборда. | body | Optional |

### Request body objects

#### Объект `Dashboard`

Конфигурация дашборда.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| dashboardMetadata | [DashboardMetadata](#openapi-definition-DashboardMetadata) | Параметры дашборда. | Обязательный |
| id | string | ID дашборда. | Опциональный |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки | Опциональный |
| tiles | [Tile](#openapi-definition-Tile)[] | Список тайлов на дашборде. | Обязательный |

#### Объект `DashboardMetadata`

Параметры дашборда.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| dashboardFilter | [DashboardFilter](#openapi-definition-DashboardFilter) | Фильтры, применённые к дашборду. | Опциональный |
| dynamicFilters | [DynamicFilters](#openapi-definition-DynamicFilters) | Конфигурация фильтра дашборда. | Опциональный |
| hasConsistentColors | boolean | Тайл использует единообразные цвета при отображении содержимого. | Опциональный |
| name | string | Имя дашборда. | Обязательный |
| owner | string | Владелец дашборда. | Обязательный |
| preset | boolean | Дашборд является пресетом (`true`) или пользовательским дашбордом (`false`). | Опциональный |
| shared | boolean | Дашборд является общим (`true`) или приватным (`false`). | Опциональный |
| tags | string[] | Набор тегов, назначенных дашборду. | Опциональный |
| tilesNameSize | string | Общий размер тайлов. Значение по умолчанию medium. Элемент может содержать следующие значения * `small` * `medium` * `large` | Опциональный |

#### Объект `DashboardFilter`

Фильтры, применённые к дашборду.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| managementZone | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Краткое представление сущности Dynatrace. | Опциональный |
| timeframe | string | Временной диапазон дашборда по умолчанию. | Опциональный |

#### Объект `EntityShortRepresentation`

Краткое представление сущности Dynatrace.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. | Опциональный |
| id | string | ID сущности Dynatrace. | Обязательный |
| name | string | Имя сущности Dynatrace. | Опциональный |

#### Объект `DynamicFilters`

Конфигурация фильтра дашборда.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| filters | string[] | Набор всех возможных глобальных фильтров дашборда, которые можно применить к дашборду.  На данный момент поддерживаются следующие значения:  ```  OS_TYPE,  SERVICE_TYPE,  DEPLOYMENT_TYPE,  APPLICATION_INJECTION_TYPE,  PAAS_VENDOR_TYPE,  DATABASE_VENDOR,  HOST_VIRTUALIZATION_TYPE,  HOST_MONITORING_MODE,  KUBERNETES_CLUSTER,  RELATED_CLOUD_APPLICATION,  RELATED_NAMESPACE,  SERVICE_TAG_KEY:<tagname>,  HOST_TAG_KEY:<tagname>,  APPLICATION_TAG_KEY:<tagname>,  CUSTOM_DIMENSION:<key>,  PROCESS_GROUP_TAG_KEY:<tagname>,  PROCESS_GROUP_INSTANCE_TAG_KEY:<tagname> ``` | Обязательный |
| genericTagFilters | [DashboardGenericTagFilter](#openapi-definition-DashboardGenericTagFilter)[] | Набор общих фильтров по тегам, которые можно применить к дашборду | Обязательный |

#### Объект `DashboardGenericTagFilter`

Общие фильтры по тегам, которые можно применить к дашборду.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| displayName | string | Отображаемое имя, используемое для идентификации этого общего фильтра. | Опциональный |
| entityTypes | string[] | Типы сущностей, затронутые тегом. | Обязательный |
| suggestionsFromEntityType | string | Тип сущности, для которого нужно предоставлять подсказки. | Опциональный |
| tagKey | string | Ключ тега для этого фильтра. | Опциональный |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Опциональный |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Опциональный |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Опциональный |

#### Объект `Tile`

Конфигурация тайла.

Фактический набор полей зависит от типа тайла. Список фактических объектов приведён в описании поля **tileType** или см. [Dashboards API, модели Tile JSON﻿](https://dt-url.net/2wc3spx?dt=m).

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| bounds | [TileBounds](#openapi-definition-TileBounds) | Позиция и размер тайла. | Обязательный |
| configured | boolean | Тайл настроен и готов к использованию (`true`) или просто размещён на дашборде (`false`). | Опциональный |
| isAutoRefreshDisabled | boolean | Автообновление тайла отключено. Работает только для определённых типов тайлов. | Опциональный |
| name | string | Имя тайла. | Обязательный |
| nameSize | string | Размер имени тайла. Значение по умолчанию null. Элемент может содержать следующие значения * `small` * `medium` * `large` | Опциональный |
| tileFilter | [TileFilter](#openapi-definition-TileFilter) | Фильтр, применённый к тайлу.  Переопределяет фильтр дашборда. | Опциональный |
| tileType | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `DATA_EXPLORER` -> DataExplorerTile * `CUSTOM_CHARTING` -> CustomChartingTile * `DTAQL` -> UserSessionQueryTile * `MARKDOWN` -> MarkdownTile * `IMAGE` -> ImageTile * `HOSTS` -> FilterableEntityTile * `APPLICATIONS` -> FilterableEntityTile * `SERVICES` -> FilterableEntityTile * `DATABASES_OVERVIEW` -> FilterableEntityTile * `SYNTHETIC_TESTS` -> FilterableEntityTile * `APPLICATION_WORLDMAP` -> AssignedEntitiesWithMetricTile * `RESOURCES` -> AssignedEntitiesWithMetricTile * `THIRD_PARTY_MOST_ACTIVE` -> AssignedEntitiesWithMetricTile * `UEM_CONVERSIONS_PER_GOAL` -> AssignedEntitiesWithMetricTile * `HOST` -> AssignedEntitiesWithMetricTile * `PROCESS_GROUPS_ONE` -> AssignedEntitiesWithMetricTile * `SYNTHETIC_SINGLE_WEBCHECK` -> SyntheticSingleWebcheckTile * `APPLICATION` -> AssignedEntitiesTile * `VIRTUALIZATION` -> AssignedEntitiesTile * `AWS` -> AssignedEntitiesTile * `SERVICE_VERSATILE` -> AssignedEntitiesTile * `SESSION_METRICS` -> AssignedEntitiesTile * `USERS` -> AssignedEntitiesTile * `UEM_KEY_USER_ACTIONS` -> AssignedEntitiesTile * `BOUNCE_RATE` -> AssignedEntitiesTile * `UEM_CONVERSIONS_OVERALL` -> AssignedEntitiesTile * `UEM_JSERRORS_OVERALL` -> AssignedEntitiesTile * `MOBILE_APPLICATION` -> AssignedEntitiesTile * `SYNTHETIC_SINGLE_EXT_TEST` -> AssignedEntitiesTile * `SYNTHETIC_HTTP_MONITOR` -> AssignedEntitiesTile * `DATABASE` -> AssignedEntitiesTile * `CUSTOM_APPLICATION` -> AssignedEntitiesTile * `APPLICATION_METHOD` -> AssignedEntitiesTile * `LOG_ANALYTICS` -> AssignedEntitiesTile * `OPENSTACK` -> AssignedEntitiesTile * `OPENSTACK_PROJECT` -> AssignedEntitiesTile * `OPENSTACK_AV_ZONE` -> AssignedEntitiesTile * `DEVICE_APPLICATION_METHOD` -> AssignedEntitiesTile * `DEM_KEY_USER_ACTION` -> AssignedEntitiesTile * `SLO` -> AssignedEntitiesWithMetricTile * `SCALABLE_LIST` -> ScalableListTile * `HEADER` -> Tile * `OPEN_PROBLEMS` -> ProblemTile * `PURE_MODEL` -> Tile * `DOCKER` -> Tile * `NETWORK_MEDIUM` -> Tile * `APPLICATIONS_MOST_ACTIVE` -> Tile * `NETWORK` -> Tile * `UEM_ACTIVE_SESSIONS` -> Tile * `DCRUM_SERVICES` -> Tile Элемент может содержать следующие значения * `APPLICATION` * `APPLICATIONS` * `APPLICATIONS_MOST_ACTIVE` * `APPLICATION_METHOD` * `APPLICATION_WORLDMAP` * `AWS` * `BOUNCE_RATE` * `CUSTOM_APPLICATION` * `CUSTOM_CHARTING` * `DATABASE` * `DATABASES_OVERVIEW` * `DATA_EXPLORER` * `DCRUM_SERVICES` * `DEM_KEY_USER_ACTION` * `DEVICE_APPLICATION_METHOD` * `DOCKER` * `DTAQL` * `HEADER` * `HOST` * `HOSTS` * `IMAGE` * `LOG_ANALYTICS` * `MARKDOWN` * `MOBILE_APPLICATION` * `NETWORK` * `NETWORK_MEDIUM` * `OPENSTACK` * `OPENSTACK_AV_ZONE` * `OPENSTACK_PROJECT` * `OPEN_PROBLEMS` * `PROCESS_GROUPS_ONE` * `PURE_MODEL` * `RESOURCES` * `SCALABLE_LIST` * `SERVICES` * `SERVICE_VERSATILE` * `SESSION_METRICS` * `SLO` * `SYNTHETIC_HTTP_MONITOR` * `SYNTHETIC_SINGLE_EXT_TEST` * `SYNTHETIC_SINGLE_WEBCHECK` * `SYNTHETIC_TESTS` * `THIRD_PARTY_MOST_ACTIVE` * `UEM_ACTIVE_SESSIONS` * `UEM_CONVERSIONS_OVERALL` * `UEM_CONVERSIONS_PER_GOAL` * `UEM_JSERRORS_OVERALL` * `UEM_KEY_USER_ACTIONS` * `USERS` * `VIRTUALIZATION` | Обязательный |

#### Объект `TileBounds`

Позиция и размер тайла.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| height | integer | Высота тайла в пикселях. | Опциональный |
| left | integer | Расстояние по горизонтали от верхнего левого угла дашборда до верхнего левого угла тайла, в пикселях. | Опциональный |
| top | integer | Расстояние по вертикали от верхнего левого угла дашборда до верхнего левого угла тайла, в пикселях. | Опциональный |
| width | integer | Ширина тайла в пикселях. | Опциональный |

#### Объект `TileFilter`

Фильтр, применённый к тайлу.

Переопределяет фильтр дашборда.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| managementZone | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Краткое представление сущности Dynatrace. | Опциональный |
| timeframe | string | Временной диапазон тайла по умолчанию. | Опциональный |

### Модель тела запроса JSON

Это модель тела запроса, показывающая возможные элементы. Её нужно скорректировать для использования в реальном запросе.

```
{



"dashboardMetadata": {



"dashboardFilter": {



"managementZone": {



"id": "3438779970106539862",



"name": "Example Management Zone"



},



"timeframe": "l_72_HOURS"



},



"dynamicFilters": {



"filters": [



"SERVICE_TYPE"



]



},



"name": "Example Dashboard",



"owner": "Example Owner",



"shared": true



},



"metadata": {



"clusterVersion": "Mock version",



"configurationVersions": [



4,



2



]



},



"tiles": [



{



"bounds": {



"height": 38,



"left": 0,



"top": 0,



"width": 304



},



"configured": true,



"name": "Hosts",



"tileFilter": {},



"tileType": "HEADER"



},



{



"bounds": {



"height": 38,



"left": 304,



"top": 0,



"width": 304



},



"configured": true,



"name": "Applications",



"tileFilter": {},



"tileType": "HEADER"



},



{



"bounds": {



"height": 304,



"left": 0,



"top": 38,



"width": 304



},



"chartVisible": true,



"configured": true,



"name": "Host health",



"tileFilter": {



"managementZone": {



"id": "3438779970106539862",



"name": "Example Management Zone"



}



},



"tileType": "HOSTS"



},



{



"bounds": {



"height": 304,



"left": 304,



"top": 38,



"width": 304



},



"chartVisible": true,



"configured": true,



"name": "Application health",



"tileFilter": {



"managementZone": {



"id": "3438779970106539862",



"name": "Example Management Zone"



}



},



"tileType": "APPLICATIONS"



}



]



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успешно. Новая dashboard создана. Тело ответа содержит сгенерированный ID. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные недействительны |

### Объекты тела ответа

#### Объект `EntityShortRepresentation`

Краткое представление сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. |
| id | string | ID сущности Dynatrace. |
| name | string | Имя сущности Dynatrace. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Модели тела ответа JSON

```
{



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



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

## Проверка payload

Рекомендуется проверить payload перед отправкой с реальным запросом. Код ответа **204** означает, что payload действителен.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/dashboards/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/dashboards/validator` |

### Аутентификация

Для выполнения этого запроса нужен токен доступа со scope `WriteConfig`.

О том, как его получить и использовать, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Проверено. Отправленная dashboard действительна. Тело ответа отсутствует. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные недействительны |

#### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### Модели тела ответа JSON

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

В этом примере запрос создаёт новую dashboard с именем **REST example**. Dashboard показывает данные для management zone **Easytravel** во временном диапазоне **последние 2 часа**.

Dashboard содержит всего один тайл, тайл **User Session Query**, который запрашивает все user actions, которые по своему статусу Apdex являются либо **tolerating**, либо **frustrated**.

Токен API передаётся в заголовке **Authorization**.

Поскольку тело запроса длинное, в этом примере оно усечено в разделе **Curl**. Полное тело см. в разделе **Request body**. Пример тела запроса можно скачать или скопировать, чтобы попробовать его самостоятельно. Обязательно замените ID и имя management zone **Easytravel** на management zone, существующую в вашей среде, или установите это поле в `null`.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/config/v1/dashboards \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{<truncated - see the Request body section >}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/dashboards
```

#### Request body

```
{



"dashboardMetadata": {



"name": "REST example",



"shared": true,



"sharingDetails": {



"linkShared": true,



"published": true



},



"dashboardFilter": {



"timeframe": "l_2_HOURS",



"managementZone": {



"id": "9130632296508575249",



"name": "Easytravel"



}



}



},



"tiles": [



{



"name": "User Sessions Query",



"tileType": "DTAQL",



"configured": true,



"bounds": {



"top": 0,



"left": 0,



"width": 1200,



"height": 450



},



"tileFilter": {



"managementZone": null



},



"customName": "User sessions query results",



"query": "select * FROM useraction where (apdexCategory IS 'TOLERATING' OR apdexCategory IS 'FRUSTRATED')",



"type": "TABLE",



"chartConfig": {



"xAxis": ["apdexCategory"],



"yAxis": ["application"]



}



}



]



}
```

#### Response body

```
{



"id": "7dd386fe-f91d-42e3-a2ec-0c88070933f4",



"name": "REST example"



}
```

#### Response code

204

#### Результат

![New dashboard](https://dt-cdn.net/images/rest-example-dashboard-1684-9a9bf56653.png)

New dashboard

## Похожие темы

* [Dashboards](/managed/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.")