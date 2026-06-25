---
title: Dashboards API - POST a dashboard
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/dashboards-api/post-dashboard
scraped: 2026-05-12T11:14:42.629636
---

# Dashboards API - POST a dashboard

# Dashboards API - POST a dashboard

* Reference
* Published Aug 30, 2019

Создаёт новый дашборд.

Запрос принимает и возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/dashboards` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/dashboards` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

В теле не должно быть ID. ID назначается автоматически Dynatrace.

JSON-модели для каждого типа плитки смотрите в [Tile JSON models](/managed/dynatrace-api/configuration-api/dashboards-api/dashboards-api-tile-models "Изучите варианты JSON-моделей плиток в Dynatrace Dashboards Classic API.").

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [Dashboard](#openapi-definition-Dashboard) | JSON-тело запроса. Содержит параметры нового дашборда. | body | Optional |

### Объекты тела запроса

#### Объект `Dashboard`

Конфигурация дашборда.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| dashboardMetadata | [DashboardMetadata](#openapi-definition-DashboardMetadata) | Параметры дашборда. | Required |
| id | string | ID дашборда. | Optional |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные для отладки | Optional |
| tiles | [Tile[]](#openapi-definition-Tile) | Список плиток на дашборде. | Required |

#### Объект `DashboardMetadata`

Параметры дашборда.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| dashboardFilter | [DashboardFilter](#openapi-definition-DashboardFilter) | Фильтры, применённые к дашборду. | Optional |
| dynamicFilters | [DynamicFilters](#openapi-definition-DynamicFilters) | Конфигурация фильтров дашборда. | Optional |
| hasConsistentColors | boolean | Плитка использует согласованные цвета при отрисовке своего содержимого. | Optional |
| name | string | Имя дашборда. | Required |
| owner | string | Владелец дашборда. | Required |
| preset | boolean | Дашборд предустановленный (`true`) или кастомный (`false`). | Optional |
| shared | boolean | Дашборд общий (`true`) или приватный (`false`). | Optional |
| tags | string[] | Набор тегов, назначенных дашборду. | Optional |
| tilesNameSize | string | Общий размер плиток. Значение по умолчанию medium Возможные значения: * `small` * `medium` * `large` | Optional |

#### Объект `DashboardFilter`

Фильтры, применённые к дашборду.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| managementZone | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Краткое представление сущности Dynatrace. | Optional |
| timeframe | string | Таймфрейм дашборда по умолчанию. | Optional |

#### Объект `EntityShortRepresentation`

Краткое представление сущности Dynatrace.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. | Optional |
| id | string | ID сущности Dynatrace. | Required |
| name | string | Имя сущности Dynatrace. | Optional |

#### Объект `DynamicFilters`

Конфигурация фильтров дашборда.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| filters | string[] | Набор всех возможных глобальных фильтров дашборда, которые можно применить к дашборду  В настоящее время поддерживаются значения:  ```  OS_TYPE,  SERVICE_TYPE,  DEPLOYMENT_TYPE,  APPLICATION_INJECTION_TYPE,  PAAS_VENDOR_TYPE,  DATABASE_VENDOR,  HOST_VIRTUALIZATION_TYPE,  HOST_MONITORING_MODE,  KUBERNETES_CLUSTER,  RELATED_CLOUD_APPLICATION,  RELATED_NAMESPACE,  SERVICE_TAG_KEY:<tagname>,  HOST_TAG_KEY:<tagname>,  APPLICATION_TAG_KEY:<tagname>,  CUSTOM_DIMENSION:<key>,  PROCESS_GROUP_TAG_KEY:<tagname>,  PROCESS_GROUP_INSTANCE_TAG_KEY:<tagname> ``` | Required |
| genericTagFilters | [DashboardGenericTagFilter[]](#openapi-definition-DashboardGenericTagFilter) | Набор универсальных фильтров по тегам, которые можно применить к дашборду | Required |

#### Объект `DashboardGenericTagFilter`

Универсальные фильтры по тегам, которые можно применить к дашборду.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| displayName | string | Отображаемое имя для идентификации этого универсального фильтра. | Optional |
| entityTypes | string[] | Типы сущностей, на которые влияет тег. | Required |
| suggestionsFromEntityType | string | Тип сущности, для которого должны предоставляться подсказки. | Optional |
| tagKey | string | Ключ тега для этого фильтра. | Optional |

#### Объект `ConfigurationMetadata`

Метаданные для отладки

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Optional |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Optional |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Optional |

#### Объект `Tile`

Конфигурация плитки.

Фактический набор полей зависит от типа плитки. Список фактических объектов смотрите в описании поля **tileType** или в [Dashboards API - Tile JSON models](https://dt-url.net/2wc3spx).

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| bounds | [TileBounds](#openapi-definition-TileBounds) | Позиция и размер плитки. | Required |
| configured | boolean | Плитка настроена и готова к использованию (`true`) или просто размещена на дашборде (`false`). | Optional |
| isAutoRefreshDisabled | boolean | Автообновление плитки отключено. Работает только для определённых типов плиток. | Optional |
| name | string | Имя плитки. | Required |
| nameSize | string | Размер имени плитки. Значение по умолчанию null. Возможные значения: * `small` * `medium` * `large` | Optional |
| tileFilter | [TileFilter](#openapi-definition-TileFilter) | Фильтр, применённый к плитке.  Он переопределяет фильтр дашборда. | Optional |
| tileType | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из следующих объектов:  * `DATA_EXPLORER` -> DataExplorerTile * `CUSTOM_CHARTING` -> CustomChartingTile * `DTAQL` -> UserSessionQueryTile * `MARKDOWN` -> MarkdownTile * `IMAGE` -> ImageTile * `HOSTS` -> FilterableEntityTile * `APPLICATIONS` -> FilterableEntityTile * `SERVICES` -> FilterableEntityTile * `DATABASES_OVERVIEW` -> FilterableEntityTile * `SYNTHETIC_TESTS` -> FilterableEntityTile * `APPLICATION_WORLDMAP` -> AssignedEntitiesWithMetricTile * `RESOURCES` -> AssignedEntitiesWithMetricTile * `THIRD_PARTY_MOST_ACTIVE` -> AssignedEntitiesWithMetricTile * `UEM_CONVERSIONS_PER_GOAL` -> AssignedEntitiesWithMetricTile * `HOST` -> AssignedEntitiesWithMetricTile * `PROCESS_GROUPS_ONE` -> AssignedEntitiesWithMetricTile * `SYNTHETIC_SINGLE_WEBCHECK` -> SyntheticSingleWebcheckTile * `APPLICATION` -> AssignedEntitiesTile * `VIRTUALIZATION` -> AssignedEntitiesTile * `AWS` -> AssignedEntitiesTile * `SERVICE_VERSATILE` -> AssignedEntitiesTile * `SESSION_METRICS` -> AssignedEntitiesTile * `USERS` -> AssignedEntitiesTile * `UEM_KEY_USER_ACTIONS` -> AssignedEntitiesTile * `BOUNCE_RATE` -> AssignedEntitiesTile * `UEM_CONVERSIONS_OVERALL` -> AssignedEntitiesTile * `UEM_JSERRORS_OVERALL` -> AssignedEntitiesTile * `MOBILE_APPLICATION` -> AssignedEntitiesTile * `SYNTHETIC_SINGLE_EXT_TEST` -> AssignedEntitiesTile * `SYNTHETIC_HTTP_MONITOR` -> AssignedEntitiesTile * `DATABASE` -> AssignedEntitiesTile * `CUSTOM_APPLICATION` -> AssignedEntitiesTile * `APPLICATION_METHOD` -> AssignedEntitiesTile * `LOG_ANALYTICS` -> AssignedEntitiesTile * `OPENSTACK` -> AssignedEntitiesTile * `OPENSTACK_PROJECT` -> AssignedEntitiesTile * `OPENSTACK_AV_ZONE` -> AssignedEntitiesTile * `DEVICE_APPLICATION_METHOD` -> AssignedEntitiesTile * `DEM_KEY_USER_ACTION` -> AssignedEntitiesTile * `SLO` -> AssignedEntitiesWithMetricTile * `SCALABLE_LIST` -> ScalableListTile * `HEADER` -> Tile * `OPEN_PROBLEMS` -> ProblemTile * `PURE_MODEL` -> Tile * `DOCKER` -> Tile * `NETWORK_MEDIUM` -> Tile * `APPLICATIONS_MOST_ACTIVE` -> Tile * `NETWORK` -> Tile * `UEM_ACTIVE_SESSIONS` -> Tile * `DCRUM_SERVICES` -> Tile Возможные значения: * `APPLICATION` * `APPLICATIONS` * `APPLICATIONS_MOST_ACTIVE` * `APPLICATION_METHOD` * `APPLICATION_WORLDMAP` * `AWS` * `BOUNCE_RATE` * `CUSTOM_APPLICATION` * `CUSTOM_CHARTING` * `DATABASE` * `DATABASES_OVERVIEW` * `DATA_EXPLORER` * `DCRUM_SERVICES` * `DEM_KEY_USER_ACTION` * `DEVICE_APPLICATION_METHOD` * `DOCKER` * `DTAQL` * `HEADER` * `HOST` * `HOSTS` * `IMAGE` * `LOG_ANALYTICS` * `MARKDOWN` * `MOBILE_APPLICATION` * `NETWORK` * `NETWORK_MEDIUM` * `OPENSTACK` * `OPENSTACK_AV_ZONE` * `OPENSTACK_PROJECT` * `OPEN_PROBLEMS` * `PROCESS_GROUPS_ONE` * `PURE_MODEL` * `RESOURCES` * `SCALABLE_LIST` * `SERVICES` * `SERVICE_VERSATILE` * `SESSION_METRICS` * `SLO` * `SYNTHETIC_HTTP_MONITOR` * `SYNTHETIC_SINGLE_EXT_TEST` * `SYNTHETIC_SINGLE_WEBCHECK` * `SYNTHETIC_TESTS` * `THIRD_PARTY_MOST_ACTIVE` * `UEM_ACTIVE_SESSIONS` * `UEM_CONVERSIONS_OVERALL` * `UEM_CONVERSIONS_PER_GOAL` * `UEM_JSERRORS_OVERALL` * `UEM_KEY_USER_ACTIONS` * `USERS` * `VIRTUALIZATION` | Required |

#### Объект `TileBounds`

Позиция и размер плитки.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| height | integer | Высота плитки в пикселях. | Optional |
| left | integer | Расстояние по горизонтали от верхнего левого угла дашборда до верхнего левого угла плитки в пикселях. | Optional |
| top | integer | Расстояние по вертикали от верхнего левого угла дашборда до верхнего левого угла плитки в пикселях. | Optional |
| width | integer | Ширина плитки в пикселях. | Optional |

#### Объект `TileFilter`

Фильтр, применённый к плитке.

Он переопределяет фильтр дашборда.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| managementZone | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Краткое представление сущности Dynatrace. | Optional |
| timeframe | string | Таймфрейм плитки по умолчанию. | Optional |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

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
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успех. Новый дашборд создан. Тело ответа содержит сгенерированный ID. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод |

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
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

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

## Validate payload

Рекомендуется валидировать payload перед отправкой реального запроса. Код ответа **204** означает валидный payload.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/dashboards/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/dashboards/validator` |

### Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Validated. Переданный дашборд валиден. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод |

#### Объекты тела ответа

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
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### JSON-модели тела ответа

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

В этом примере запрос создаёт новый дашборд с именем **REST example**. Дашборд показывает данные для зоны управления **Easytravel** в таймфрейме **последние 2 часа**.

Дашборд содержит всего одну плитку: плитку **User Session Query**, которая запрашивает все user action, которые по их статусу Apdex либо **tolerating**, либо **frustrated**.

API-токен передаётся в заголовке **Authorization**.

Поскольку тело запроса объёмное, в этом примере оно усечено в секции **Curl**. Полное тело смотрите в секции **Request body**. Вы можете скачать или скопировать пример тела запроса, чтобы попробовать его самостоятельно. Обязательно замените ID и имя зоны управления **Easytravel** на зону управления, которая существует в вашем окружении, либо задайте этому полю значение `null`.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/config/v1/dashboards \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{<truncated - see the Request body section >}'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/dashboards
```

#### Тело запроса

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

#### Тело ответа

```
{



"id": "7dd386fe-f91d-42e3-a2ec-0c88070933f4",



"name": "REST example"



}
```

#### Код ответа

204

#### Результат

![New dashboard](https://dt-cdn.net/images/rest-example-dashboard-1684-9a9bf56653.png)

New dashboard

## Связанные темы

* [Дашборды](/managed/analyze-explore-automate/dashboards-classic "Узнайте, как создавать дашборды Dynatrace Dashboards Classic, управлять ими и использовать их.")