---
title: Dashboards API - GET a dashboard
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/dashboards-api/get-dashboard
scraped: 2026-05-12T11:14:37.496244
---

# Dashboards API - GET a dashboard

# Dashboards API - GET a dashboard

* Reference
* Published Jan 23, 2019

Возвращает параметры указанного дашборда.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/dashboards/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/dashboards/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID нужного дашборда. | path | Required |

## Ответ

JSON-модели для каждого типа плитки смотрите в [Tile JSON models](/managed/dynatrace-api/configuration-api/dashboards-api/dashboards-api-tile-models "Изучите варианты JSON-моделей плиток в Dynatrace Dashboards Classic API.").

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [Dashboard](#openapi-definition-Dashboard) | Успех. Тело ответа содержит параметры дашборда. |

### Объекты тела ответа

#### Объект `Dashboard`

Конфигурация дашборда.

| Элемент | Тип | Описание |
| --- | --- | --- |
| dashboardMetadata | [DashboardMetadata](#openapi-definition-DashboardMetadata) | Параметры дашборда. |
| id | string | ID дашборда. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные для отладки |
| tiles | [Tile[]](#openapi-definition-Tile) | Список плиток на дашборде. |

#### Объект `DashboardMetadata`

Параметры дашборда.

| Элемент | Тип | Описание |
| --- | --- | --- |
| dashboardFilter | [DashboardFilter](#openapi-definition-DashboardFilter) | Фильтры, применённые к дашборду. |
| dynamicFilters | [DynamicFilters](#openapi-definition-DynamicFilters) | Конфигурация фильтров дашборда. |
| hasConsistentColors | boolean | Плитка использует согласованные цвета при отрисовке своего содержимого. |
| name | string | Имя дашборда. |
| owner | string | Владелец дашборда. |
| preset | boolean | Дашборд предустановленный (`true`) или кастомный (`false`). |
| shared | boolean | Дашборд общий (`true`) или приватный (`false`). |
| tags | string[] | Набор тегов, назначенных дашборду. |
| tilesNameSize | string | Общий размер плиток. Значение по умолчанию medium Возможные значения: * `small` * `medium` * `large` |

#### Объект `DashboardFilter`

Фильтры, применённые к дашборду.

| Элемент | Тип | Описание |
| --- | --- | --- |
| managementZone | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Краткое представление сущности Dynatrace. |
| timeframe | string | Таймфрейм дашборда по умолчанию. |

#### Объект `EntityShortRepresentation`

Краткое представление сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. |
| id | string | ID сущности Dynatrace. |
| name | string | Имя сущности Dynatrace. |

#### Объект `DynamicFilters`

Конфигурация фильтров дашборда.

| Элемент | Тип | Описание |
| --- | --- | --- |
| filters | string[] | Набор всех возможных глобальных фильтров дашборда, которые можно применить к дашборду  В настоящее время поддерживаются значения:  ```  OS_TYPE,  SERVICE_TYPE,  DEPLOYMENT_TYPE,  APPLICATION_INJECTION_TYPE,  PAAS_VENDOR_TYPE,  DATABASE_VENDOR,  HOST_VIRTUALIZATION_TYPE,  HOST_MONITORING_MODE,  KUBERNETES_CLUSTER,  RELATED_CLOUD_APPLICATION,  RELATED_NAMESPACE,  SERVICE_TAG_KEY:<tagname>,  HOST_TAG_KEY:<tagname>,  APPLICATION_TAG_KEY:<tagname>,  CUSTOM_DIMENSION:<key>,  PROCESS_GROUP_TAG_KEY:<tagname>,  PROCESS_GROUP_INSTANCE_TAG_KEY:<tagname> ``` |
| genericTagFilters | [DashboardGenericTagFilter[]](#openapi-definition-DashboardGenericTagFilter) | Набор универсальных фильтров по тегам, которые можно применить к дашборду |

#### Объект `DashboardGenericTagFilter`

Универсальные фильтры по тегам, которые можно применить к дашборду.

| Элемент | Тип | Описание |
| --- | --- | --- |
| displayName | string | Отображаемое имя для идентификации этого универсального фильтра. |
| entityTypes | string[] | Типы сущностей, на которые влияет тег. |
| suggestionsFromEntityType | string | Тип сущности, для которого должны предоставляться подсказки. |
| tagKey | string | Ключ тега для этого фильтра. |

#### Объект `ConfigurationMetadata`

Метаданные для отладки

| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |

#### Объект `Tile`

Конфигурация плитки.

Фактический набор полей зависит от типа плитки. Список фактических объектов смотрите в описании поля **tileType** или в [Dashboards API - Tile JSON models](https://dt-url.net/2wc3spx).

| Элемент | Тип | Описание |
| --- | --- | --- |
| bounds | [TileBounds](#openapi-definition-TileBounds) | Позиция и размер плитки. |
| configured | boolean | Плитка настроена и готова к использованию (`true`) или просто размещена на дашборде (`false`). |
| isAutoRefreshDisabled | boolean | Автообновление плитки отключено. Работает только для определённых типов плиток. |
| name | string | Имя плитки. |
| nameSize | string | Размер имени плитки. Значение по умолчанию null. Возможные значения: * `small` * `medium` * `large` |
| tileFilter | [TileFilter](#openapi-definition-TileFilter) | Фильтр, применённый к плитке.  Он переопределяет фильтр дашборда. |
| tileType | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из следующих объектов:  * `DATA_EXPLORER` -> DataExplorerTile * `CUSTOM_CHARTING` -> CustomChartingTile * `DTAQL` -> UserSessionQueryTile * `MARKDOWN` -> MarkdownTile * `IMAGE` -> ImageTile * `HOSTS` -> FilterableEntityTile * `APPLICATIONS` -> FilterableEntityTile * `SERVICES` -> FilterableEntityTile * `DATABASES_OVERVIEW` -> FilterableEntityTile * `SYNTHETIC_TESTS` -> FilterableEntityTile * `APPLICATION_WORLDMAP` -> AssignedEntitiesWithMetricTile * `RESOURCES` -> AssignedEntitiesWithMetricTile * `THIRD_PARTY_MOST_ACTIVE` -> AssignedEntitiesWithMetricTile * `UEM_CONVERSIONS_PER_GOAL` -> AssignedEntitiesWithMetricTile * `HOST` -> AssignedEntitiesWithMetricTile * `PROCESS_GROUPS_ONE` -> AssignedEntitiesWithMetricTile * `SYNTHETIC_SINGLE_WEBCHECK` -> SyntheticSingleWebcheckTile * `APPLICATION` -> AssignedEntitiesTile * `VIRTUALIZATION` -> AssignedEntitiesTile * `AWS` -> AssignedEntitiesTile * `SERVICE_VERSATILE` -> AssignedEntitiesTile * `SESSION_METRICS` -> AssignedEntitiesTile * `USERS` -> AssignedEntitiesTile * `UEM_KEY_USER_ACTIONS` -> AssignedEntitiesTile * `BOUNCE_RATE` -> AssignedEntitiesTile * `UEM_CONVERSIONS_OVERALL` -> AssignedEntitiesTile * `UEM_JSERRORS_OVERALL` -> AssignedEntitiesTile * `MOBILE_APPLICATION` -> AssignedEntitiesTile * `SYNTHETIC_SINGLE_EXT_TEST` -> AssignedEntitiesTile * `SYNTHETIC_HTTP_MONITOR` -> AssignedEntitiesTile * `DATABASE` -> AssignedEntitiesTile * `CUSTOM_APPLICATION` -> AssignedEntitiesTile * `APPLICATION_METHOD` -> AssignedEntitiesTile * `LOG_ANALYTICS` -> AssignedEntitiesTile * `OPENSTACK` -> AssignedEntitiesTile * `OPENSTACK_PROJECT` -> AssignedEntitiesTile * `OPENSTACK_AV_ZONE` -> AssignedEntitiesTile * `DEVICE_APPLICATION_METHOD` -> AssignedEntitiesTile * `DEM_KEY_USER_ACTION` -> AssignedEntitiesTile * `SLO` -> AssignedEntitiesWithMetricTile * `SCALABLE_LIST` -> ScalableListTile * `HEADER` -> Tile * `OPEN_PROBLEMS` -> ProblemTile * `PURE_MODEL` -> Tile * `DOCKER` -> Tile * `NETWORK_MEDIUM` -> Tile * `APPLICATIONS_MOST_ACTIVE` -> Tile * `NETWORK` -> Tile * `UEM_ACTIVE_SESSIONS` -> Tile * `DCRUM_SERVICES` -> Tile Возможные значения: * `APPLICATION` * `APPLICATIONS` * `APPLICATIONS_MOST_ACTIVE` * `APPLICATION_METHOD` * `APPLICATION_WORLDMAP` * `AWS` * `BOUNCE_RATE` * `CUSTOM_APPLICATION` * `CUSTOM_CHARTING` * `DATABASE` * `DATABASES_OVERVIEW` * `DATA_EXPLORER` * `DCRUM_SERVICES` * `DEM_KEY_USER_ACTION` * `DEVICE_APPLICATION_METHOD` * `DOCKER` * `DTAQL` * `HEADER` * `HOST` * `HOSTS` * `IMAGE` * `LOG_ANALYTICS` * `MARKDOWN` * `MOBILE_APPLICATION` * `NETWORK` * `NETWORK_MEDIUM` * `OPENSTACK` * `OPENSTACK_AV_ZONE` * `OPENSTACK_PROJECT` * `OPEN_PROBLEMS` * `PROCESS_GROUPS_ONE` * `PURE_MODEL` * `RESOURCES` * `SCALABLE_LIST` * `SERVICES` * `SERVICE_VERSATILE` * `SESSION_METRICS` * `SLO` * `SYNTHETIC_HTTP_MONITOR` * `SYNTHETIC_SINGLE_EXT_TEST` * `SYNTHETIC_SINGLE_WEBCHECK` * `SYNTHETIC_TESTS` * `THIRD_PARTY_MOST_ACTIVE` * `UEM_ACTIVE_SESSIONS` * `UEM_CONVERSIONS_OVERALL` * `UEM_CONVERSIONS_PER_GOAL` * `UEM_JSERRORS_OVERALL` * `UEM_KEY_USER_ACTIONS` * `USERS` * `VIRTUALIZATION` |

#### Объект `TileBounds`

Позиция и размер плитки.

| Элемент | Тип | Описание |
| --- | --- | --- |
| height | integer | Высота плитки в пикселях. |
| left | integer | Расстояние по горизонтали от верхнего левого угла дашборда до верхнего левого угла плитки в пикселях. |
| top | integer | Расстояние по вертикали от верхнего левого угла дашборда до верхнего левого угла плитки в пикселях. |
| width | integer | Ширина плитки в пикселях. |

#### Объект `TileFilter`

Фильтр, применённый к плитке.

Он переопределяет фильтр дашборда.

| Элемент | Тип | Описание |
| --- | --- | --- |
| managementZone | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Краткое представление сущности Dynatrace. |
| timeframe | string | Таймфрейм плитки по умолчанию. |

### JSON-модели тела ответа

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

## Пример

В этом примере запрос возвращает параметры дашборда **Sample dashboard** с ID **2768e6ca-e199-4433-9e0d-2922aec2099b**.

API-токен передаётся в заголовке **Authorization**.

В UI дашборд выглядит так:

![Sample dashboard](https://dt-cdn.net/images/sample-dashboard-651-0530cd435d.png)

Sample dashboard

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/dashboards/2768e6ca-e199-4433-9e0d-2922aec2099b \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/dashboards/2768e6ca-e199-4433-9e0d-2922aec2099b
```

#### Тело ответа

```
{



"metadata": {



"clusterVersion": "1.166.0.20190311-110828",



"configurationVersions": [



2



]



},



"id": "2768e6ca-e199-4433-9e0d-2922aec2099b",



"dashboardMetadata": {



"name": "Sample dashboard",



"shared": true,



"owner": "john.smith",



"sharingDetails": {



"linkShared": true,



"published": true



},



"dashboardFilter": {



"timeframe": "l_2_HOURS",



"managementZone": null



}



},



"tiles": [



{



"name": "Host health",



"tileType": "HOSTS",



"configured": true,



"bounds": {



"top": 0,



"left": 304,



"width": 304,



"height": 304



},



"tileFilter": {



"managementZone": {



"id": "9130632296508575249",



"name": "Easytravel"



}



},



"filterConfig": null,



"chartVisible": true



},



{



"name": "User behavior",



"tileType": "SESSION_METRICS",



"configured": true,



"bounds": {



"top": 0,



"left": 0,



"width": 304,



"height": 304



},



"tileFilter": {



"managementZone": null



},



"assignedEntities": [



"APPLICATION-8E41C8C247910758"



]



}



]



}
```

#### Код ответа

200

## Связанные темы

* [Дашборды](/managed/analyze-explore-automate/dashboards-classic "Узнайте, как создавать дашборды Dynatrace Dashboards Classic, управлять ими и использовать их.")