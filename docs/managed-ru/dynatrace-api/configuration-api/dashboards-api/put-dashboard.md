---
title: Dashboards API - PUT a dashboard
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/dashboards-api/put-dashboard
---

# Dashboards API - PUT a dashboard

# Dashboards API - PUT a dashboard

* Справочник
* Опубликовано 30 августа 2019

Обновляет указанный дашборд.

Запрос принимает и возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/dashboards/{id}` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/dashboards/{id}` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

Подробнее о том, как получить и использовать токен, читайте в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Модели JSON для каждого типа плитки смотри в разделе [Tile JSON models](/managed/dynatrace-api/configuration-api/dashboards-api/dashboards-api-tile-models "Learn the variations of tile JSON models in the Dynatrace Dashboards Classic API.").

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID дашборда, который нужно обновить.  ID в теле запроса должен совпадать с этим ID. | path | Обязательный |
| body | [Dashboard](#openapi-definition-Dashboard) | Тело JSON запроса. Содержит обновлённые параметры дашборда. | body | Необязательный |

### Объекты тела запроса

#### Объект `Dashboard`

Конфигурация дашборда.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| dashboardMetadata | [DashboardMetadata](#openapi-definition-DashboardMetadata) | Параметры дашборда. | Обязательный |
| id | string | ID дашборда. | Опциональный |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки | Опциональный |
| tiles | [Tile](#openapi-definition-Tile)[] | Список плиток на дашборде. | Обязательный |

#### Объект `DashboardMetadata`

Параметры дашборда.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| dashboardFilter | [DashboardFilter](#openapi-definition-DashboardFilter) | Фильтры, применённые к дашборду. | Опциональный |
| dynamicFilters | [DynamicFilters](#openapi-definition-DynamicFilters) | Конфигурация фильтра дашборда. | Опциональный |
| hasConsistentColors | boolean | Плитка использует согласованные цвета при отрисовке содержимого. | Опциональный |
| name | string | Название дашборда. | Обязательный |
| owner | string | Владелец дашборда. | Обязательный |
| preset | boolean | Дашборд является предустановленным (`true`) или пользовательским (`false`). | Опциональный |
| shared | boolean | Дашборд является общим (`true`) или приватным (`false`). | Опциональный |
| tags | string[] | Набор тегов, назначенных дашборду. | Опциональный |
| tilesNameSize | string | Общий размер плиток. Значение по умолчанию, medium. Элемент может принимать следующие значения: * `small` * `medium` * `large` | Опциональный |

#### Объект `DashboardFilter`

Фильтры, применённые к дашборду.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| managementZone | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Краткое представление сущности Dynatrace. | Опциональный |
| timeframe | string | Временной интервал дашборда по умолчанию. | Опциональный |

#### Объект `EntityShortRepresentation`

Краткое представление сущности Dynatrace.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. | Опциональный |
| id | string | ID сущности Dynatrace. | Обязательный |
| name | string | Название сущности Dynatrace. | Опциональный |

#### Объект `DynamicFilters`

Конфигурация фильтра дашборда.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| filters | string[] | Набор всех возможных глобальных фильтров дашборда, которые можно применить к дашборду.  На данный момент поддерживаются следующие значения:  ```  OS_TYPE,  SERVICE_TYPE,  DEPLOYMENT_TYPE,  APPLICATION_INJECTION_TYPE,  PAAS_VENDOR_TYPE,  DATABASE_VENDOR,  HOST_VIRTUALIZATION_TYPE,  HOST_MONITORING_MODE,  KUBERNETES_CLUSTER,  RELATED_CLOUD_APPLICATION,  RELATED_NAMESPACE,  SERVICE_TAG_KEY:<tagname>,  HOST_TAG_KEY:<tagname>,  APPLICATION_TAG_KEY:<tagname>,  CUSTOM_DIMENSION:<key>,  PROCESS_GROUP_TAG_KEY:<tagname>,  PROCESS_GROUP_INSTANCE_TAG_KEY:<tagname> ``` | Обязательный |
| genericTagFilters | [DashboardGenericTagFilter](#openapi-definition-DashboardGenericTagFilter)[] | Набор универсальных фильтров по тегам, которые можно применить к дашборду. | Обязательный |

#### Объект `DashboardGenericTagFilter`

Универсальные фильтры по тегам, которые можно применить к дашборду.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| displayName | string | Отображаемое имя, используемое для идентификации этого универсального фильтра. | Опциональный |
| entityTypes | string[] | Типы сущностей, затрагиваемые тегом. | Обязательный |
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

Конфигурация плитки.

Фактический набор полей зависит от типа плитки. Список фактических объектов см. в описании поля **tileType** или в разделе [Dashboards API, модели Tile JSON﻿](https://dt-url.net/2wc3spx?dt=m).

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| bounds | [TileBounds](#openapi-definition-TileBounds) | Позиция и размер плитки. | Обязательный |
| configured | boolean | Плитка настроена и готова к использованию (`true`) или просто размещена на дашборде (`false`). | Опциональный |
| isAutoRefreshDisabled | boolean | Автообновление плитки отключено. Работает только для определённых типов плиток. | Опциональный |
| name | string | Название плитки. | Обязательный |
| nameSize | string | Размер названия плитки. Значение по умолчанию, null. Элемент может принимать следующие значения: * `small` * `medium` * `large` | Опциональный |
| tileFilter | [TileFilter](#openapi-definition-TileFilter) | Фильтр, применённый к плитке.  Переопределяет фильтр дашборда. | Опциональный |
| tileType | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `DATA_EXPLORER` -> DataExplorerTile * `CUSTOM_CHARTING` -> CustomChartingTile * `DTAQL` -> UserSessionQueryTile * `MARKDOWN` -> MarkdownTile * `IMAGE` -> ImageTile * `HOSTS` -> FilterableEntityTile * `APPLICATIONS` -> FilterableEntityTile * `SERVICES` -> FilterableEntityTile * `DATABASES_OVERVIEW` -> FilterableEntityTile * `SYNTHETIC_TESTS` -> FilterableEntityTile * `APPLICATION_WORLDMAP` -> AssignedEntitiesWithMetricTile * `RESOURCES` -> AssignedEntitiesWithMetricTile * `THIRD_PARTY_MOST_ACTIVE` -> AssignedEntitiesWithMetricTile * `UEM_CONVERSIONS_PER_GOAL` -> AssignedEntitiesWithMetricTile * `HOST` -> AssignedEntitiesWithMetricTile * `PROCESS_GROUPS_ONE` -> AssignedEntitiesWithMetricTile * `SYNTHETIC_SINGLE_WEBCHECK` -> SyntheticSingleWebcheckTile * `APPLICATION` -> AssignedEntitiesTile * `VIRTUALIZATION` -> AssignedEntitiesTile * `AWS` -> AssignedEntitiesTile * `SERVICE_VERSATILE` -> AssignedEntitiesTile * `SESSION_METRICS` -> AssignedEntitiesTile * `USERS` -> AssignedEntitiesTile * `UEM_KEY_USER_ACTIONS` -> AssignedEntitiesTile * `BOUNCE_RATE` -> AssignedEntitiesTile * `UEM_CONVERSIONS_OVERALL` -> AssignedEntitiesTile * `UEM_JSERRORS_OVERALL` -> AssignedEntitiesTile * `MOBILE_APPLICATION` -> AssignedEntitiesTile * `SYNTHETIC_SINGLE_EXT_TEST` -> AssignedEntitiesTile * `SYNTHETIC_HTTP_MONITOR` -> AssignedEntitiesTile * `DATABASE` -> AssignedEntitiesTile * `CUSTOM_APPLICATION` -> AssignedEntitiesTile * `APPLICATION_METHOD` -> AssignedEntitiesTile * `LOG_ANALYTICS` -> AssignedEntitiesTile * `OPENSTACK` -> AssignedEntitiesTile * `OPENSTACK_PROJECT` -> AssignedEntitiesTile * `OPENSTACK_AV_ZONE` -> AssignedEntitiesTile * `DEVICE_APPLICATION_METHOD` -> AssignedEntitiesTile * `DEM_KEY_USER_ACTION` -> AssignedEntitiesTile * `SLO` -> AssignedEntitiesWithMetricTile * `SCALABLE_LIST` -> ScalableListTile * `HEADER` -> Tile * `OPEN_PROBLEMS` -> ProblemTile * `PURE_MODEL` -> Tile * `DOCKER` -> Tile * `NETWORK_MEDIUM` -> Tile * `APPLICATIONS_MOST_ACTIVE` -> Tile * `NETWORK` -> Tile * `UEM_ACTIVE_SESSIONS` -> Tile * `DCRUM_SERVICES` -> Tile Элемент может принимать следующие значения: * `APPLICATION` * `APPLICATIONS` * `APPLICATIONS_MOST_ACTIVE` * `APPLICATION_METHOD` * `APPLICATION_WORLDMAP` * `AWS` * `BOUNCE_RATE` * `CUSTOM_APPLICATION` * `CUSTOM_CHARTING` * `DATABASE` * `DATABASES_OVERVIEW` * `DATA_EXPLORER` * `DCRUM_SERVICES` * `DEM_KEY_USER_ACTION` * `DEVICE_APPLICATION_METHOD` * `DOCKER` * `DTAQL` * `HEADER` * `HOST` * `HOSTS` * `IMAGE` * `LOG_ANALYTICS` * `MARKDOWN` * `MOBILE_APPLICATION` * `NETWORK` * `NETWORK_MEDIUM` * `OPENSTACK` * `OPENSTACK_AV_ZONE` * `OPENSTACK_PROJECT` * `OPEN_PROBLEMS` * `PROCESS_GROUPS_ONE` * `PURE_MODEL` * `RESOURCES` * `SCALABLE_LIST` * `SERVICES` * `SERVICE_VERSATILE` * `SESSION_METRICS` * `SLO` * `SYNTHETIC_HTTP_MONITOR` * `SYNTHETIC_SINGLE_EXT_TEST` * `SYNTHETIC_SINGLE_WEBCHECK` * `SYNTHETIC_TESTS` * `THIRD_PARTY_MOST_ACTIVE` * `UEM_ACTIVE_SESSIONS` * `UEM_CONVERSIONS_OVERALL` * `UEM_CONVERSIONS_PER_GOAL` * `UEM_JSERRORS_OVERALL` * `UEM_KEY_USER_ACTIONS` * `USERS` * `VIRTUALIZATION` | Обязательный |

#### Объект `TileBounds`

Позиция и размер плитки.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| height | integer | Высота плитки в пикселях. | Опциональный |
| left | integer | Горизонтальное расстояние от верхнего левого угла дашборда до верхнего левого угла плитки, в пикселях. | Опциональный |
| top | integer | Вертикальное расстояние от верхнего левого угла дашборда до верхнего левого угла плитки, в пикселях. | Опциональный |
| width | integer | Ширина плитки в пикселях. | Опциональный |

#### Объект `TileFilter`

Фильтр, применённый к плитке.

Переопределяет фильтр дашборда.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| managementZone | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Краткое представление сущности Dynatrace. | Опциональный |
| timeframe | string | Временной интервал плитки по умолчанию. | Опциональный |

### Модель тела запроса JSON

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать для использования в реальном запросе.

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
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успешно. Новый dashboard создан. Ответ не содержит тела. |
| **204** | - | Успешно. Dashboard обновлён. Ответ не содержит тела |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные некорректны |

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
| code | integer | Код статуса HTTP |
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

## Проверка полезной нагрузки

Рекомендуется проверять полезную нагрузку перед её отправкой в реальном запросе. Код ответа **204** означает, что полезная нагрузка корректна.

Запрос принимает полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/dashboards/{id}/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/dashboards/{id}/validator` |

### Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

О том, как его получить и использовать, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/dashboards/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/dashboards/validator` |

### Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

О том, как его получить и использовать, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Пример

В этом примере запрос добавляет плитку **Service health** в **Sample dashboard** из примера [GET-запроса](/managed/dynatrace-api/configuration-api/dashboards-api/get-dashboard#example "Просмотр dashboard через Dynatrace Classic API.").

Плитка показывает состояние всех сервисов, принадлежащих management zone **Easytravel**. Она расположена рядом с существующей плиткой **Host health** и имеет такой же размер (**304x304** пикселей).

Токен API передаётся в заголовке **Authorization**.

Поскольку тело запроса длинное, в этом примере раздел **Curl** оно усечено. Полное тело см. в разделе **Request body**. Можно скачать или скопировать пример тела запроса, чтобы опробовать его самостоятельно. Обязательно измените ID и имя management zone **Easytravel** на management zone, существующую в вашем окружении, либо задайте этому полю значение `null`.

#### Curl

```
curl -X PUT \



https://mySampleEnv.live.dynatrace.com/api/config/v1/dashboards/2768e6ca-e199-4433-9e0d-2922aec2099b \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{<truncated - see the Request body section >}'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/dashboards/2768e6ca-e199-4433-9e0d-2922aec2099b
```

#### Тело запроса

```
{



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



"assignedEntities": ["APPLICATION-8E41C8C247910758"]



},



{



"name": "Service health",



"tileType": "SERVICES",



"configured": true,



"bounds": {



"top": 0,



"left": 608,



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



}



]



}
```

#### Код ответа

204

#### Результат

![Sample dashboard - modified](https://dt-cdn.net/images/sample-dashboard-upd-947-ef255c99d0.png)

Sample dashboard, изменённый

## Похожие темы

* [Dashboards](/managed/analyze-explore-automate/dashboards-classic "Узнайте, как создавать Dynatrace Dashboards Classic, управлять ими и использовать их.")