---
title: Dashboards API - Tile JSON models
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/dashboards-api/dashboards-api-tile-models
---

# Dashboards API - Tile JSON models

# Dashboards API - Tile JSON models

* Справка
* Опубликовано 11 марта 2019 г.

JSON модели плиток дашборда сильно различаются в зависимости от типа плитки. Ниже перечислены JSON модели для каждого типа плитки.

## AssignedEntitiesTile

Этот тип применяется к следующим плиткам:

* AWS (`AWS`)
* Bounce rate (`BOUNCE_RATE`)
* Custom application (`CUSTOM_APPLICATION`)
* Database performance (`DATABASE`)
* External monitor (`SYNTHETIC_SINGLE_EXT_TEST`)
* HTTP monitor (`SYNTHETIC_HTTP_MONITOR`)
* JavaScript errors (`UEM_JSERRORS_OVERALL`)
* Key user actions overview (`UEM_KEY_USER_ACTIONS`)
* Key user action (`DEM_KEY_USER_ACTION`)
* Log event (`LOG_ANALYTICS`)

* Mobile app (`MOBILE_APPLICATION`)
* Service or request (`SERVICE_VERSATILE`)
* Service-level objective (`SLO`)
* Top conversion goals (`UEM_CONVERSIONS_OVERALL`)
* User behavior (`SESSION_METRICS`)
* User breakdown (`USERS`)
* VMware (`VIRTUALIZATION`)
* Web application (`APPLICATION`)
* User action (`APPLICATION_METHOD` или `APPLICATION_METHOD`)

AssignedEntitiesTile

Параметры

JSON модель

#### Объект `AssignedEntitiesTile`

Конфигурация плитки с назначенной сущностью Dynatrace.

Пример, плитка Bounce rate, показывающая данные из назначенного приложения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| assignedEntities | string[] | Список сущностей Dynatrace, назначенных плитке. |

```
{



"name": "AWS",



"tileType": "AWS",



"configured": true,



"bounds": {



"top": 192,



"left": 62,



"width": 304,



"height": 152



},



"tileFilter": {



"timeframe": "Today"



},



"assignedEntities": [



"556925984968688946"



]



}
```

## FilterableEntityTile

Этот тип применяется к следующим плиткам:

* Application health (`APPLICATIONS`)
* Database health (`DATABASES_OVERVIEW`)
* Host health (`HOSTS`)
* Service health (`SERVICES`)
* Synthetic monitor health (`SYNTHETIC_TESTS`)

FilterableEntityTile

Параметры

JSON модель

#### Объект `FilterableEntityTile`

Конфигурация плитки со встроенным пользовательским фильтром.

Пример, плитка Service health, которая может использовать пользовательский период времени.

| Элемент | Тип | Описание |
| --- | --- | --- |
| chartVisible | boolean | - |
| filterConfig | [CustomFilterConfig](#openapi-definition-CustomFilterConfig) | Конфигурация пользовательского фильтра плитки. |

#### Объект `CustomFilterConfig`

Конфигурация пользовательского фильтра плитки.

| Элемент | Тип | Описание |
| --- | --- | --- |
| chartConfig | [CustomFilterChartConfig](#openapi-definition-CustomFilterChartConfig) | Конфигурация пользовательского графика. |
| customName | string | Имя плитки, заданное пользователем |
| defaultName | string | Имя плитки по умолчанию |
| filtersPerEntityType | object | Список фильтров, применяемых к определённым типам сущностей. |
| type | string | Тип фильтра.  Показывает, к какой сущности относится фильтр.  Пользовательские графики имеют тип `MIXED`. Элемент может принимать следующие значения * `ALB` * `APPLICATION` * `APPLICATION_METHOD` * `APPMON` * `ASG` * `AWS_CREDENTIALS` * `AWS_CUSTOM_SERVICE` * `AWS_LAMBDA_FUNCTION` * `CLOUD_APPLICATION` * `CLOUD_APPLICATION_INSTANCE` * `CLOUD_APPLICATION_NAMESPACE` * `CONTAINER_GROUP_INSTANCE` * `CUSTOM_APPLICATION` * `CUSTOM_DEVICES` * `CUSTOM_SERVICES` * `DATABASE` * `DATABASE_KEY_REQUEST` * `DCRUM_APPLICATION` * `DCRUM_ENTITY` * `DYNAMO_DB` * `EBS` * `EC2` * `ELB` * `ENVIRONMENT` * `ESXI` * `EXTERNAL_SYNTHETIC_TEST` * `GLOBAL_BACKGROUND_ACTIVITY` * `HOST` * `IOT` * `KUBERNETES_CLUSTER` * `KUBERNETES_NODE` * `MDA_SERVICE` * `MIXED` * `MOBILE_APPLICATION` * `MONITORED_ENTITY` * `NLB` * `PG_BACKGROUND_ACTIVITY` * `PROBLEM` * `PROCESS_GROUP_INSTANCE` * `RDS` * `REMOTE_PLUGIN` * `SERVICE` * `SERVICE_KEY_REQUEST` * `SYNTHETIC_BROWSER_MONITOR` * `SYNTHETIC_HTTPCHECK` * `SYNTHETIC_HTTPCHECK_STEP` * `SYNTHETIC_LOCATION` * `SYNTHETIC_TEST` * `SYNTHETIC_TEST_STEP` * `UI_ENTITY` * `VIRTUAL_MACHINE` * `WEB_CHECK` |

#### Объект `CustomFilterChartConfig`

Конфигурация пользовательского графика.

| Элемент | Тип | Описание |
| --- | --- | --- |
| axisLimits | object | Необязательные пользовательские пределы оси Y. |
| leftAxisCustomUnit | string | Пользовательская единица измерения для левой оси Y. Элемент может принимать следующие значения * `Ampere` * `Billion` * `Bit` * `BitPerHour` * `BitPerMinute` * `BitPerSecond` * `Byte` * `BytePerHour` * `BytePerMinute` * `BytePerSecond` * `Cores` * `Count` * `Day` * `DecibelMilliWatt` * `GibiByte` * `GibiBytePerHour` * `GibiBytePerMinute` * `GibiBytePerSecond` * `Giga` * `GigaByte` * `GigaBytePerHour` * `GigaBytePerMinute` * `GigaBytePerSecond` * `Hertz` * `Hour` * `KibiByte` * `KibiBytePerHour` * `KibiBytePerMinute` * `KibiBytePerSecond` * `Kilo` * `KiloByte` * `KiloBytePerHour` * `KiloBytePerMinute` * `KiloBytePerSecond` * `KiloMetrePerHour` * `MSU` * `MebiByte` * `MebiBytePerHour` * `MebiBytePerMinute` * `MebiBytePerSecond` * `Mega` * `MegaByte` * `MegaBytePerHour` * `MegaBytePerMinute` * `MegaBytePerSecond` * `MetrePerHour` * `MetrePerSecond` * `MicroSecond` * `MilliCores` * `MilliSecond` * `MilliSecondPerMinute` * `Million` * `Minute` * `Month` * `NanoSecond` * `NanoSecondPerMinute` * `NotApplicable` * `PerHour` * `PerMinute` * `PerSecond` * `Percent` * `Pixel` * `Promille` * `Ratio` * `Second` * `State` * `Trillion` * `Unspecified` * `Volt` * `Watt` * `Week` * `Year` |
| legendShown | boolean | Определяет, должна ли отображаться легенда. |
| resultMetadata | object | Дополнительная информация об отображаемой на графике метрике. |
| rightAxisCustomUnit | string | Пользовательская единица измерения для правой оси Y. Элемент может принимать следующие значения * `Ampere` * `Billion` * `Bit` * `BitPerHour` * `BitPerMinute` * `BitPerSecond` * `Byte` * `BytePerHour` * `BytePerMinute` * `BytePerSecond` * `Cores` * `Count` * `Day` * `DecibelMilliWatt` * `GibiByte` * `GibiBytePerHour` * `GibiBytePerMinute` * `GibiBytePerSecond` * `Giga` * `GigaByte` * `GigaBytePerHour` * `GigaBytePerMinute` * `GigaBytePerSecond` * `Hertz` * `Hour` * `KibiByte` * `KibiBytePerHour` * `KibiBytePerMinute` * `KibiBytePerSecond` * `Kilo` * `KiloByte` * `KiloBytePerHour` * `KiloBytePerMinute` * `KiloBytePerSecond` * `KiloMetrePerHour` * `MSU` * `MebiByte` * `MebiBytePerHour` * `MebiBytePerMinute` * `MebiBytePerSecond` * `Mega` * `MegaByte` * `MegaBytePerHour` * `MegaBytePerMinute` * `MegaBytePerSecond` * `MetrePerHour` * `MetrePerSecond` * `MicroSecond` * `MilliCores` * `MilliSecond` * `MilliSecondPerMinute` * `Million` * `Minute` * `Month` * `NanoSecond` * `NanoSecondPerMinute` * `NotApplicable` * `PerHour` * `PerMinute` * `PerSecond` * `Percent` * `Pixel` * `Promille` * `Ratio` * `Second` * `State` * `Trillion` * `Unspecified` * `Volt` * `Watt` * `Week` * `Year` |
| series | [CustomFilterChartSeriesConfig](#openapi-definition-CustomFilterChartSeriesConfig)[] | Список отображаемых на графике метрик. |
| type | string | Тип графика. Элемент может принимать следующие значения * `PIE` * `SINGLE_VALUE` * `TIMESERIES` * `TOP_LIST` |

#### Объект `CustomChartingItemMetadataConfig`

Дополнительные метаданные для отображаемой на графике метрики.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customColor | string | Цвет метрики на графике, в шестнадцатеричном формате. |
| lastModified | integer | Временная метка последнего изменения метаданных, в миллисекундах UTC. |

#### Объект `CustomFilterChartSeriesConfig`

Конфигурация отображаемой на графике метрики.

| Элемент | Тип | Описание |
| --- | --- | --- |
| aggregation | string | Отображаемая на графике агрегация метрики. Элемент может принимать следующие значения * `AVG` * `COUNT` * `DISTINCT` * `FASTEST10PERCENT` * `MAX` * `MEDIAN` * `MIN` * `NONE` * `OF_INTEREST_RATIO` * `OTHER_RATIO` * `PERCENTILE` * `PER_MIN` * `SLOWEST10PERCENT` * `SLOWEST5PERCENT` * `SUM` * `SUM_DIMENSIONS` |
| aggregationRate | string | -Элемент может принимать следующие значения * `HOUR` * `MINUTE` * `SECOND` * `TOTAL` |
| dimensions | [CustomFilterChartSeriesDimensionConfig](#openapi-definition-CustomFilterChartSeriesDimensionConfig)[] | Конфигурация разбивки отображаемой на графике метрики. |
| entityType | string | Тип сущности Dynatrace, предоставившей отображаемую на графике метрику. |
| metric | string | Имя отображаемой на графике метрики. |
| percentile | integer | Отображаемый на графике перцентиль.  Применимо, только если для **aggregation** задано значение `PERCENTILE`. |
| sortAscending | boolean | Сортировка по возрастанию (`true`) или по убыванию (`false`). |
| sortColumn | boolean | - |
| type | string | Визуализация графика временного ряда. Элемент может принимать следующие значения * `AREA` * `BAR` * `LINE` |

#### Объект `CustomFilterChartSeriesDimensionConfig`

Конфигурация разбивки отображаемой на графике метрики.

| Элемент | Тип | Описание |
| --- | --- | --- |
| entityDimension | boolean | - |
| id | string | ID измерения, по которому разбивается метрика. |
| name | string | Имя измерения, по которому разбивается метрика. |
| values | string[] | Значение разбивки. |

```
{



"name": "Host health",



"tileType": "HOSTS",



"configured": true,



"bounds": {



"top": 47,



"left": 415,



"width": 304,



"height": 304



},



"tileFilter": {



"timeframe": "-3h to now",



"managementZone": {



"id": "9130632296508575249",



"name": "Easytravel"



}



},



"filterConfig": null,



"chartVisible": true



}
```

## AssignedEntitiesWithMetricTile

Этот тип применяется к следующим плиткам:

* World map (`APPLICATION_WORLDMAP`)
* Host (`HOST`)
* Process group (`PROCESS_GROUPS_ONE`)
* Resources (`RESOURCES`)
* Most used 3rd parties (`THIRD_PARTY_MOST_ACTIVE`)
* Conversion goal (`UEM_CONVERSIONS_PER_GOAL`)

AssignedEntitiesWithMetricTile

Параметры

Модель JSON

#### Объект `AssignedEntitiesWithMetricTile`

Конфигурация плитки с назначенной сущностью Dynatrace и назначенной метрикой.

Пример: плитка Worldmap, показывающая данные назначенной метрики производительности или поведения назначенного приложения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| assignedEntities | string[] | Список сущностей Dynatrace, назначенных плитке. |
| metric | string | Метрика, назначенная плитке. |

```
{



"name": "World map",



"tileType": "APPLICATION_WORLDMAP",



"configured": true,



"bounds": {



"top": 118,



"left": 194,



"width": 304,



"height": 304



},



"tileFilter": {



"timeframe": "-12h to now",



"managementZone": null



},



"assignedEntities": [



"APPLICATION-C93B8002996906CD"



],



"metric": "SESSION_USERS"



}
```

## DataExplorerTile

Этот тип применяется к следующим плиткам:

* Плитка Data Explorer (`DATA_EXPLORER`)

DataExplorerTile

Параметры

JSON model

#### Объект `DataExplorerTile`

Конфигурация плитки data explorer.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customName | string | Имя плитки, заданное пользователем. |
| metricExpressions | string[] | Выражения метрик, сгенерированные этой конфигурацией |
| queries | [DataExplorerQuery](#openapi-definition-DataExplorerQuery)[] | Список запросов для исследования |
| queriesSettings | [DataExplorerQuerySettings](#openapi-definition-DataExplorerQuerySettings) | Конфигурация запросов |
| visualConfig | [VisualizationConfiguration](#openapi-definition-VisualizationConfiguration) | Конфигурация визуализации. |

#### Объект `DataExplorerQuery`

Конфигурация запроса data explorer.

| Элемент | Тип | Описание |
| --- | --- | --- |
| defaultValue | number | Заменяет пустые точки данных указанным значением |
| enabled | boolean | Статус запроса |
| filterBy | [DataExplorerFilter](#openapi-definition-DataExplorerFilter) | Фильтр для запросов data explorer. |
| foldTransformation | string | Свёртывающее преобразование. Элемент может принимать следующие значения: * `LAST_VALUE` * `TOTAL` |
| generatedMetricSelector | string | Сгенерированный селектор метрики |
| histogram | boolean | Нужно ли применять оператор гистограммы к селектору метрики |
| id | string | Идентификатор запроса |
| limit | integer | Ограничение результатов запроса |
| metric | string | Идентификатор метрики |
| metricSelector | string | Селектор метрики |
| rate | string | Преобразует метрику на основе счётчика (например, байты) в метрику на основе скорости (байты в секунду). Элемент может принимать следующие значения: * `HOUR` * `MINUTE` * `MONTH` * `NONE` * `SECOND` * `WEEK` * `YEAR` |
| sortBy | string | Порядок сортировки, применяемый к запросу. Элемент может принимать следующие значения: * `ASC` * `DESC` |
| sortByDimension | string | Измерение, к которому применяется сортировка. Если null, сортировка идёт по значению |
| spaceAggregation | string | Пространственная агрегация, применяемая к запросу. Элемент может принимать следующие значения: * `AUTO` * `AVG` * `COUNT` * `MAX` * `MEDIAN` * `MIN` * `PERCENTILE_10` * `PERCENTILE_75` * `PERCENTILE_90` * `SUM` * `VALUE` |
| splitBy | string[] | Разбиения, применяемые к запросу |
| timeAggregation | string | Временное агрегирование, применяемое к запросу. Элемент может принимать следующие значения: * `AVG` * `COUNT` * `DEFAULT` * `MAX` * `MEDIAN` * `MIN` * `SUM` * `VALUE` |
| timeShift | [DataExplorerTimeShift](#openapi-definition-DataExplorerTimeShift) | TimeShift для запросов data explorer. |

#### Объект `DataExplorerFilter`

Фильтр для запросов data explorer.

| Элемент | Тип | Описание |
| --- | --- | --- |
| criteria | [DexpFilterCriterion](#openapi-definition-DexpFilterCriterion)[] | - |
| entityAttribute | string | - |
| filter | string | - |
| filterOperator | string | Элемент может принимать следующие значения: * `AND` * `NOT` * `OR` |
| filterType | string | Элемент может принимать следующие значения: * `DIMENSION` * `ENTITY_ATTRIBUTE` * `ID` * `NAME` * `TAG` |
| globalEntity | string | - |
| nestedFilters | [DataExplorerFilter](#openapi-definition-DataExplorerFilter)[] | - |
| relationship | [DexpFilterRelationship](#openapi-definition-DexpFilterRelationship) | - |

#### Объект `DexpFilterCriterion`

Критерий для фильтров data explorer.

| Элемент | Тип | Описание |
| --- | --- | --- |
| evaluator | string | Элемент может принимать следующие значения: * `EQ` * `IN` * `NE` * `PREFIX` |
| matchExactly | boolean | - |
| value | string | - |

#### Объект `DexpFilterRelationship`

| Элемент | Тип | Описание |
| --- | --- | --- |
| id | string | Идентификатор связи, например runsOn, isStepOf и т. д. |
| targetEntity | string | Целевая сущность связи, например HOST, VCENTER, SERVICE и т. д. |
| type | string | Тип связи. Элемент может принимать следующие значения: * `fromRelationship` * `toRelationship` |

#### Объект `DataExplorerTimeShift`

TimeShift для запросов data explorer.

| Элемент | Тип | Описание |
| --- | --- | --- |
| factor | integer | - |
| unit | string | Элемент может принимать следующие значения: * `DAY` * `HOUR` * `MINUTE` * `SECOND` * `WEEK` |

#### Объект `DataExplorerQuerySettings`

Конфигурация запросов

| Элемент | Тип | Описание |
| --- | --- | --- |
| foldAggregation | string | Свёртывающая агрегация. Элемент может принимать следующие значения: * `AUTO` * `AVG` * `COUNT` * `MAX` * `MEDIAN` * `MIN` * `PERCENTILE_10` * `PERCENTILE_75` * `PERCENTILE_90` * `SUM` * `VALUE` |
| foldTransformation | string | Свёртывающее преобразование. Элемент может принимать следующие значения: * `LAST_VALUE` * `TOTAL` |
| globalLimitQueryId | string | Идентификатор запроса метрики глобального лимита |
| resolution | string | Разрешение |

#### Объект `VisualizationConfiguration`

Конфигурация визуализации.

| Элемент | Тип | Описание |
| --- | --- | --- |
| axes | [Axes](#openapi-definition-Axes) | Конфигурация осей |
| global | [VisualizationGlobalProperties](#openapi-definition-VisualizationGlobalProperties) | Глобальная конфигурация визуализации |
| graphChartSettings | [GraphChartSettings](#openapi-definition-GraphChartSettings) | Настройки для визуализации графика |
| heatmapSettings | [HeatmapSettings](#openapi-definition-HeatmapSettings) | Настройки для визуализации тепловой карты |
| honeycombSettings | [HoneycombSettings](#openapi-definition-HoneycombSettings) | Настройки для визуализации honeycomb |
| rules | [VisualizationRule](#openapi-definition-VisualizationRule)[] | Правила для визуализации |
| singleValueSettings | [SingleValueSettings](#openapi-definition-SingleValueSettings) | Настройки для визуализации одиночного значения |
| tableSettings | [TableSettings](#openapi-definition-TableSettings) | Настройки для визуализации таблицы |
| thresholds | [VisualizationThreshold](#openapi-definition-VisualizationThreshold)[] | Пороговые значения для визуализации |
| type | string | Идентификатор запроса. Элемент может принимать следующие значения: * `GRAPH_CHART` * `HEATMAP` * `HISTOGRAM` * `HONEYCOMB` * `PIE_CHART` * `SINGLE_VALUE` * `STACKED_AREA` * `STACKED_COLUMN` * `TABLE` * `TOP_LIST` |

#### Объект `Axes`

Конфигурация осей

| Элемент | Тип | Описание |
| --- | --- | --- |
| xAxis | [Axis](#openapi-definition-Axis) | Конфигурация оси x |
| yAxes | [YAxis](#openapi-definition-YAxis)[] | Конфигурация осей y |

#### Объект `Axis`

Конфигурация оси x

| Элемент | Тип | Описание |
| --- | --- | --- |
| displayName | string | - |
| visible | boolean | - |

#### Объект `YAxis`

Конфигурация осей y

| Элемент | Тип | Описание |
| --- | --- | --- |
| defaultAxis | boolean | - |
| displayName | string | - |
| max | string | - |
| min | string | - |
| position | string | Элемент может принимать следующие значения: * `LEFT` * `RIGHT` |
| queryIds | string[] | - |
| visible | boolean | - |

#### Объект `VisualizationGlobalProperties`

Глобальная конфигурация визуализации

| Элемент | Тип | Описание |
| --- | --- | --- |
| hasTrendline | boolean | - |
| hideLegend | boolean | - |
| seriesType | string | Элемент может принимать следующие значения: * `AREA` * `COLUMN` * `LINE` * `STACKED_AREA` * `STACKED_COLUMN` |
| theme | string | Элемент может принимать следующие значения: * `BLUE` * `DEFAULT` * `GRAY` * `GREEN` * `ORANGE` * `PURPLE` * `RED` * `ROYALBLUE` * `TURQUOISE` * `YELLOW` |
| threshold | [VisualizationThreshold](#openapi-definition-VisualizationThreshold) | Пороговые значения для визуализации |

#### Объект `VisualizationThreshold`

Пороговые значения для визуализации

| Элемент | Тип | Описание |
| --- | --- | --- |
| axisTarget | string | Элемент может принимать следующие значения: * `LEFT` * `RIGHT` |
| columnId | string | - |
| queryId | string | - |
| rules | [VisualizationThresholdRule](#openapi-definition-VisualizationThresholdRule)[] | - |
| visible | boolean | - |

#### Объект `VisualizationThresholdRule`

| Элемент | Тип | Описание |
| --- | --- | --- |
| color | string | - |
| value | number | - |

#### Объект `GraphChartSettings`

Настройки для визуализации графика

| Элемент | Тип | Описание |
| --- | --- | --- |
| connectNulls | boolean | - |

#### Объект `HeatmapSettings`

Настройки для визуализации тепловой карты

| Элемент | Тип | Описание |
| --- | --- | --- |
| showLabels | boolean | - |
| xAxisBuckets | integer | Число сегментов на оси X |
| yAxis | string | Критерий агрегации оси Y. Элемент может принимать следующие значения: * `DIMENSIONS` * `VALUE` |
| yAxisBuckets | integer | Число сегментов на оси Y |

#### Объект `HoneycombSettings`

Настройки для визуализации honeycomb

| Элемент | Тип | Описание |
| --- | --- | --- |
| showHive | boolean | - |
| showLabels | boolean | - |
| showLegend | boolean | - |

#### Объект `VisualizationRule`

Правила для визуализации

| Элемент | Тип | Описание |
| --- | --- | --- |
| matcher | string | - |
| properties | [VisualizationProperties](#openapi-definition-VisualizationProperties) | - |
| seriesOverrides | [VisualizationSerieOverride](#openapi-definition-VisualizationSerieOverride)[] | - |
| unitTransform | string | - |
| valueFormat | string | - |

#### Объект `VisualizationProperties`

| Элемент | Тип | Описание |
| --- | --- | --- |
| alias | string | - |
| color | string | - |
| seriesType | string | Элемент может принимать следующие значения: * `AREA` * `COLUMN` * `LINE` * `STACKED_AREA` * `STACKED_COLUMN` |

#### Объект `VisualizationSerieOverride`

| Элемент | Тип | Описание |
| --- | --- | --- |
| color | string | - |
| name | string | - |

#### Объект `SingleValueSettings`

Настройки для визуализации одиночного значения

| Элемент | Тип | Описание |
| --- | --- | --- |
| linkTileColorToThreshold | boolean | - |
| showSparkLine | boolean | - |
| showTrend | boolean | - |

#### Объект `TableSettings`

Настройки для визуализации таблицы

| Элемент | Тип | Описание |
| --- | --- | --- |
| hiddenColumns | string[] | - |
| isThresholdBackgroundAppliedToCell | boolean | - |

```
{



"name": "Data Explorer results",



"tileType": "DATA_EXPLORER",



"configured": true,



"bounds": {



"top": 0,



"left": 0,



"width": 304,



"height": 304



},



"tileFilter": {},



"customName": "Data Explorer results",



"queries": [



{



"id": "A",



"metric": "builtin:host.cpu.usage",



"timeAggregation": "DEFAULT",



"splitBy": [



"dt.entity.host"



],



"sortBy": "DESC",



"filterBy": {



"filterOperator": "AND",



"nestedFilters": [],



"criteria": []



},



"limit": 100,



"enabled": true



}



],



"visualConfig": {



"type": "GRAPH_CHART",



"global": {



"hideLegend": false



},



"rules": [



{



"matcher": "A:",



"unitTransform": "Promille",



"valueFormat": "0,00",



"properties": {



"color": "DEFAULT",



"seriesType": "LINE"



},



"seriesOverrides": []



}



],



"axes": {



"xAxis": {



"displayName": "",



"visible": true



},



"yAxes": [



{



"displayName": "",



"visible": true,



"min": "AUTO",



"max": "AUTO",



"position": "LEFT",



"queryIds": [



"A"



],



"defaultAxis": true



}



]



},



"heatmapSettings": {



"yAxis": "VALUE"



},



"singleValueSettings": {



"showSparkLine": false



},



"thresholds": [



{



"axisTarget": "LEFT",



"rules": [



{



"color": "#7dc540"



},



{



"color": "#f5d30f"



},



{



"value": 50,



"color": "#dc172a"



}



],



"queryId": "",



"visible": true



}



],



"tableSettings": {



"isThresholdBackgroundAppliedToCell": false



},



"graphChartSettings": {



"connectNulls": true



},



"honeycombSettings": {



"showHive": true,



"showLegend": true,



"showLabels": false



}



},



"queriesSettings": {



"resolution": ""



},



"metricExpressions": [



"resolution=null&(builtin:host.cpu.usage:splitBy(\"dt.entity.host\"):sort(value(auto,descending)):limit(100)):limit(100):names"



]



}
```

## CustomChartingTile

Этот тип применяется к следующим плиткам:

* Custom chart (`CUSTOM_CHARTING`)

CustomChartingTile

Параметры

JSON model

#### Объект `CustomChartingTile`

Конфигурация плитки настраиваемой диаграммы.

| Элемент | Тип | Описание |
| --- | --- | --- |
| filterConfig | [CustomFilterConfig](#openapi-definition-CustomFilterConfig) | Конфигурация настраиваемого фильтра плитки. |

#### Объект `CustomFilterConfig`

Конфигурация настраиваемого фильтра плитки.

| Элемент | Тип | Описание |
| --- | --- | --- |
| chartConfig | [CustomFilterChartConfig](#openapi-definition-CustomFilterChartConfig) | Конфигурация настраиваемой диаграммы. |
| customName | string | Название плитки, заданное пользователем |
| defaultName | string | Название плитки по умолчанию |
| filtersPerEntityType | object | Список фильтров, применяемых к конкретным типам сущностей. |
| type | string | Тип фильтра. Показывает, к какой сущности относится фильтр. Настраиваемые диаграммы имеют тип `MIXED`. Элемент может принимать следующие значения * `ALB` * `APPLICATION` * `APPLICATION_METHOD` * `APPMON` * `ASG` * `AWS_CREDENTIALS` * `AWS_CUSTOM_SERVICE` * `AWS_LAMBDA_FUNCTION` * `CLOUD_APPLICATION` * `CLOUD_APPLICATION_INSTANCE` * `CLOUD_APPLICATION_NAMESPACE` * `CONTAINER_GROUP_INSTANCE` * `CUSTOM_APPLICATION` * `CUSTOM_DEVICES` * `CUSTOM_SERVICES` * `DATABASE` * `DATABASE_KEY_REQUEST` * `DCRUM_APPLICATION` * `DCRUM_ENTITY` * `DYNAMO_DB` * `EBS` * `EC2` * `ELB` * `ENVIRONMENT` * `ESXI` * `EXTERNAL_SYNTHETIC_TEST` * `GLOBAL_BACKGROUND_ACTIVITY` * `HOST` * `IOT` * `KUBERNETES_CLUSTER` * `KUBERNETES_NODE` * `MDA_SERVICE` * `MIXED` * `MOBILE_APPLICATION` * `MONITORED_ENTITY` * `NLB` * `PG_BACKGROUND_ACTIVITY` * `PROBLEM` * `PROCESS_GROUP_INSTANCE` * `RDS` * `REMOTE_PLUGIN` * `SERVICE` * `SERVICE_KEY_REQUEST` * `SYNTHETIC_BROWSER_MONITOR` * `SYNTHETIC_HTTPCHECK` * `SYNTHETIC_HTTPCHECK_STEP` * `SYNTHETIC_LOCATION` * `SYNTHETIC_TEST` * `SYNTHETIC_TEST_STEP` * `UI_ENTITY` * `VIRTUAL_MACHINE` * `WEB_CHECK` |

#### Объект `CustomFilterChartConfig`

Конфигурация настраиваемой диаграммы.

| Элемент | Тип | Описание |
| --- | --- | --- |
| axisLimits | object | Необязательные настраиваемые границы оси Y. |
| leftAxisCustomUnit | string | Настраиваемая единица измерения для левой оси Y. Элемент может принимать следующие значения * `Ampere` * `Billion` * `Bit` * `BitPerHour` * `BitPerMinute` * `BitPerSecond` * `Byte` * `BytePerHour` * `BytePerMinute` * `BytePerSecond` * `Cores` * `Count` * `Day` * `DecibelMilliWatt` * `GibiByte` * `GibiBytePerHour` * `GibiBytePerMinute` * `GibiBytePerSecond` * `Giga` * `GigaByte` * `GigaBytePerHour` * `GigaBytePerMinute` * `GigaBytePerSecond` * `Hertz` * `Hour` * `KibiByte` * `KibiBytePerHour` * `KibiBytePerMinute` * `KibiBytePerSecond` * `Kilo` * `KiloByte` * `KiloBytePerHour` * `KiloBytePerMinute` * `KiloBytePerSecond` * `KiloMetrePerHour` * `MSU` * `MebiByte` * `MebiBytePerHour` * `MebiBytePerMinute` * `MebiBytePerSecond` * `Mega` * `MegaByte` * `MegaBytePerHour` * `MegaBytePerMinute` * `MegaBytePerSecond` * `MetrePerHour` * `MetrePerSecond` * `MicroSecond` * `MilliCores` * `MilliSecond` * `MilliSecondPerMinute` * `Million` * `Minute` * `Month` * `NanoSecond` * `NanoSecondPerMinute` * `NotApplicable` * `PerHour` * `PerMinute` * `PerSecond` * `Percent` * `Pixel` * `Promille` * `Ratio` * `Second` * `State` * `Trillion` * `Unspecified` * `Volt` * `Watt` * `Week` * `Year` |
| legendShown | boolean | Определяет, нужно ли показывать легенду. |
| resultMetadata | object | Дополнительная информация о метрике на диаграмме. |
| rightAxisCustomUnit | string | Настраиваемая единица измерения для правой оси Y. Элемент может принимать следующие значения * `Ampere` * `Billion` * `Bit` * `BitPerHour` * `BitPerMinute` * `BitPerSecond` * `Byte` * `BytePerHour` * `BytePerMinute` * `BytePerSecond` * `Cores` * `Count` * `Day` * `DecibelMilliWatt` * `GibiByte` * `GibiBytePerHour` * `GibiBytePerMinute` * `GibiBytePerSecond` * `Giga` * `GigaByte` * `GigaBytePerHour` * `GigaBytePerMinute` * `GigaBytePerSecond` * `Hertz` * `Hour` * `KibiByte` * `KibiBytePerHour` * `KibiBytePerMinute` * `KibiBytePerSecond` * `Kilo` * `KiloByte` * `KiloBytePerHour` * `KiloBytePerMinute` * `KiloBytePerSecond` * `KiloMetrePerHour` * `MSU` * `MebiByte` * `MebiBytePerHour` * `MebiBytePerMinute` * `MebiBytePerSecond` * `Mega` * `MegaByte` * `MegaBytePerHour` * `MegaBytePerMinute` * `MegaBytePerSecond` * `MetrePerHour` * `MetrePerSecond` * `MicroSecond` * `MilliCores` * `MilliSecond` * `MilliSecondPerMinute` * `Million` * `Minute` * `Month` * `NanoSecond` * `NanoSecondPerMinute` * `NotApplicable` * `PerHour` * `PerMinute` * `PerSecond` * `Percent` * `Pixel` * `Promille` * `Ratio` * `Second` * `State` * `Trillion` * `Unspecified` * `Volt` * `Watt` * `Week` * `Year` |
| series | [CustomFilterChartSeriesConfig](#openapi-definition-CustomFilterChartSeriesConfig)[] | Список метрик, отображаемых на диаграмме. |
| type | string | Тип диаграммы. Элемент может принимать следующие значения * `PIE` * `SINGLE_VALUE` * `TIMESERIES` * `TOP_LIST` |

#### Объект `CustomChartingItemMetadataConfig`

Дополнительные метаданные для метрики на диаграмме.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customColor | string | Цвет метрики на диаграмме, в hex-формате. |
| lastModified | integer | Метка времени последнего изменения метаданных, в миллисекундах UTC. |

#### Объект `CustomFilterChartSeriesConfig`

Конфигурация метрики на диаграмме.

| Элемент | Тип | Описание |
| --- | --- | --- |
| aggregation | string | Агрегация метрики на диаграмме. Элемент может принимать следующие значения * `AVG` * `COUNT` * `DISTINCT` * `FASTEST10PERCENT` * `MAX` * `MEDIAN` * `MIN` * `NONE` * `OF_INTEREST_RATIO` * `OTHER_RATIO` * `PERCENTILE` * `PER_MIN` * `SLOWEST10PERCENT` * `SLOWEST5PERCENT` * `SUM` * `SUM_DIMENSIONS` |
| aggregationRate | string | -Элемент может принимать следующие значения * `HOUR` * `MINUTE` * `SECOND` * `TOTAL` |
| dimensions | [CustomFilterChartSeriesDimensionConfig](#openapi-definition-CustomFilterChartSeriesDimensionConfig)[] | Конфигурация разбивки метрики на диаграмме. |
| entityType | string | Тип Dynatrace сущности, от которой получена метрика на диаграмме. |
| metric | string | Название метрики на диаграмме. |
| percentile | integer | Процентиль на диаграмме. Применимо только если **aggregation** установлен в `PERCENTILE`. |
| sortAscending | boolean | Сортировка по возрастанию (`true`) или по убыванию (`false`). |
| sortColumn | boolean | - |
| type | string | Визуализация диаграммы временного ряда. Элемент может принимать следующие значения * `AREA` * `BAR` * `LINE` |

#### Объект `CustomFilterChartSeriesDimensionConfig`

Конфигурация разбивки метрики на диаграмме.

| Элемент | Тип | Описание |
| --- | --- | --- |
| entityDimension | boolean | - |
| id | string | ID измерения, по которому разбивается метрика. |
| name | string | Название измерения, по которому разбивается метрика. |
| values | string[] | Значение разбивки. |

```
{



"name": "Custom chart",



"tileType": "CUSTOM_CHARTING",



"configured": true,



"bounds": {



"top": 115,



"left": 205,



"width": 304,



"height": 304



},



"tileFilter": {



"timeframe": "-1d to -12h",



"managementZone": {



"id": "9130632296508575249",



"name": "Easytravel"



}



},



"filterConfig": {



"type": "MIXED",



"customName": "CPU idle",



"defaultName": "Custom chart",



"chartConfig": {



"type": "TIMESERIES",



"series": [



{



"metric": "builtin:host.cpu.idle",



"aggregation": "AVG",



"percentile": null,



"type": "LINE",



"entityType": "HOST",



"dimensions": [],



"sortAscending": false,



"sortColumn": false,



"aggregationRate": "TOTAL"



},



{



"metric": "builtin:host.cpu.load",



"aggregation": "MAX",



"percentile": null,



"type": "AREA",



"entityType": "HOST",



"dimensions": [],



"sortAscending": false,



"sortColumn": true,



"aggregationRate": "TOTAL"



}



],



"resultMetadata": {}



},



"filtersPerEntityType": {



"HOST": {



"AUTO_TAGS": [



"easyTravel"



]



}



}



}



}
```

## MarkdownTile

Этот тип применяется к следующим плиткам:

* Markdown (`MARKDOWN`)

MarkdownTile

Параметры

JSON model

#### Объект `MarkdownTile`

Конфигурация плитки Markdown.

| Элемент | Тип | Описание |
| --- | --- | --- |
| markdown | string | Содержимое плитки в формате markdown. |

```
{



"name": "Markdown",



"tileType": "MARKDOWN",



"configured": true,



"bounds": {



"top": 252,



"left": 173,



"width": 304,



"height": 152



},



"tileFilter": {



"timeframe": null,



"managementZone": null



},



"markdown": "## This is a Markdown tile\n\nIt supports **rich text** and [links](https://dynatrace.com)"



}
```

## ProblemTile

Этот тип применяется к следующим плиткам:

* Problems (`OPEN_PROBLEMS`)

ProblemTile

Параметры

JSON model

#### Объект `ProblemTile`

Конфигурация плитки проблем.

| Элемент | Тип | Описание |
| --- | --- | --- |
| entitySelector | string | Область сущностей плитки проблем. Дополнительную информацию можно найти в эндпоинте Problems API v2 '/problems'. |
| problemSelector | string | Определяет область плитки проблем. Учитываются только проблемы, соответствующие заданным критериям. Дополнительную информацию можно найти в эндпоинте Problems API v2 '/problems'. |
| useBackgroundColor | boolean | Использовать цвет фона в зависимости от статуса проблемы: красный, если есть открытые проблемы, зелёный в остальных случаях. |

```
{



"name": "Host health",



"tileType": "OPEN_PROBLEMS",



"configured": true,



"bounds": {



"top": 47,



"left": 415,



"width": 304,



"height": 304



},



"tileFilter": {



"timeframe": "-3h to now",



"managementZone": {



"id": "9130632296508575249",



"name": "Easytravel"



}



},



"problemSelector": "status(\"open\")",



"entitySelector": "type(\"HOST\"),tag(\"easyTravel\")"



}
```

## ScalableListTile

ScalableListTile

Parameters

JSON model

#### Объект `ScalableListTile`

Конфигурация плитки со встроенным идентификатором пользовательского фильтра. Предназначено только для внутреннего использования.

| Элемент | Тип | Описание |
| --- | --- | --- |
| chartVisible | boolean | - |
| customFilterId | string | ID пользовательского фильтра. |
| entitySpecificTileType | string | Тип плитки, специфичной для сущности. Элемент может принимать следующие значения * `APPLICATION` * `APPLICATIONS` * `APPLICATIONS_MOST_ACTIVE` * `APPLICATION_WORLDMAP` * `AWS` * `BOUNCE_RATE` * `CUSTOM_APPLICATION` * `CUSTOM_CHARTING` * `DATABASE` * `DATABASES_OVERVIEW` * `DATA_EXPLORER` * `DCRUM_SERVICES` * `DEM_KEY_USER_ACTION` * `DTAQL` * `HEADER` * `HOST` * `HOSTS` * `IMAGE` * `LOGS_EVENTS_QUERY` * `LOG_ANALYTICS` * `LOG_QUERY` * `MARKDOWN` * `MOBILE_APPLICATION` * `NETWORK` * `NETWORK_MEDIUM` * `OPEN_PROBLEMS` * `PROCESS_GROUPS_ONE` * `PURE_MODEL` * `RESOURCES` * `SCALABLE_LIST` * `SERVICES` * `SERVICE_VERSATILE` * `SESSION_METRICS` * `SLO` * `SYNTHETIC_HTTP_MONITOR` * `SYNTHETIC_SINGLE_EXT_TEST` * `SYNTHETIC_SINGLE_WEBCHECK` * `SYNTHETIC_TESTS` * `THIRD_PARTY_MOST_ACTIVE` * `UEM_ACTIVE_SESSIONS` * `UEM_CONVERSIONS_OVERALL` * `UEM_CONVERSIONS_PER_GOAL` * `UEM_JSERRORS_OVERALL` * `UEM_KEY_USER_ACTIONS` * `USERS` * `VIRTUALIZATION` |

```
{



"name": "ScalableList",



"nameSize": "",



"tileType": "Image",



"configured": true,



"bounds": {



"top": 112,



"left": 45,



"width": 304,



"height": 304



},



"tileFilter": {



"timeframe": null,



"managementZone": null



},



"entitySpecificTileType": "DATA_EXLORER"



}
```

## SyntheticSingleWebcheckTile

Этот тип применяется к следующим плиткам:

* Browser monitor (`SYNTHETIC_SINGLE_WEBCHECK`)

SyntheticSingleWebcheckTile

Parameters

JSON model

#### Объект `SyntheticSingleWebcheckTile`

Конфигурация плитки Browser monitor.

| Элемент | Тип | Описание |
| --- | --- | --- |
| assignedEntities | string[] | Список Dynatrace сущностей, назначенных плитке. |
| excludeMaintenanceWindows | boolean | Включать (`false') или исключать (`true`) окна обслуживания из расчётов доступности. |

```
{



"name": "Browser monitor",



"tileType": "SYNTHETIC_SINGLE_WEBCHECK",



"configured": true,



"bounds": {



"top": 209,



"left": 214,



"width": 304,



"height": 304



},



"tileFilter": {



"timeframe": "-24h to now",



"managementZone": null



},



"assignedEntities": [



"SYNTHETIC_TEST-0000000000016ACF"



],



"excludeMaintenanceWindows": true



}
```

## Tile

Этот тип применяется к следующим плиткам:

* Data center services health (`DCRUM_SERVICES`)
* Docker (`DOCKER`)
* Header (`HEADER`)
* Live user activity (`UEM_ACTIVE_SESSIONS`)
* Network metric (`NETWORK`)
* Network status (`NETWORK_MEDIUM`)
* Smartscape (`PURE_MODEL`)
* Top web applications (`APPLICATIONS_MOST_ACTIVE`)

Tile

Parameters

JSON model

#### Объект `Tile`

Конфигурация плитки.

Фактический набор полей зависит от типа плитки. Список фактических объектов приведён в описании поля **tileType**, либо см. [Dashboards API - Tile JSON models﻿](https://dt-url.net/2wc3spx?dt=m).

| Элемент | Тип | Описание |
| --- | --- | --- |
| bounds | [TileBounds](#openapi-definition-TileBounds) | Позиция и размер плитки. |
| configured | boolean | Плитка настроена и готова к использованию (`true`) или просто размещена на дашборде (`false`). |
| isAutoRefreshDisabled | boolean | Автообновление плитки отключено. Работает только для определённых типов плиток. |
| name | string | Название плитки. |
| nameSize | string | Размер названия плитки. Значение по умолчанию null. Элемент может принимать следующие значения * `small` * `medium` * `large` |
| tileFilter | [TileFilter](#openapi-definition-TileFilter) | Фильтр, применяемый к плитке. Он переопределяет фильтр дашборда. |
| tileType | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `DATA_EXPLORER` -> DataExplorerTile * `CUSTOM_CHARTING` -> CustomChartingTile * `DTAQL` -> UserSessionQueryTile * `MARKDOWN` -> MarkdownTile * `IMAGE` -> ImageTile * `HOSTS` -> FilterableEntityTile * `APPLICATIONS` -> FilterableEntityTile * `SERVICES` -> FilterableEntityTile * `DATABASES_OVERVIEW` -> FilterableEntityTile * `SYNTHETIC_TESTS` -> FilterableEntityTile * `APPLICATION_WORLDMAP` -> AssignedEntitiesWithMetricTile * `RESOURCES` -> AssignedEntitiesWithMetricTile * `THIRD_PARTY_MOST_ACTIVE` -> AssignedEntitiesWithMetricTile * `UEM_CONVERSIONS_PER_GOAL` -> AssignedEntitiesWithMetricTile * `HOST` -> AssignedEntitiesWithMetricTile * `PROCESS_GROUPS_ONE` -> AssignedEntitiesWithMetricTile * `SYNTHETIC_SINGLE_WEBCHECK` -> SyntheticSingleWebcheckTile * `APPLICATION` -> AssignedEntitiesTile * `VIRTUALIZATION` -> AssignedEntitiesTile * `AWS` -> AssignedEntitiesTile * `SERVICE_VERSATILE` -> AssignedEntitiesTile * `SESSION_METRICS` -> AssignedEntitiesTile * `USERS` -> AssignedEntitiesTile * `UEM_KEY_USER_ACTIONS` -> AssignedEntitiesTile * `BOUNCE_RATE` -> AssignedEntitiesTile * `UEM_CONVERSIONS_OVERALL` -> AssignedEntitiesTile * `UEM_JSERRORS_OVERALL` -> AssignedEntitiesTile * `MOBILE_APPLICATION` -> AssignedEntitiesTile * `SYNTHETIC_SINGLE_EXT_TEST` -> AssignedEntitiesTile * `SYNTHETIC_HTTP_MONITOR` -> AssignedEntitiesTile * `DATABASE` -> AssignedEntitiesTile * `CUSTOM_APPLICATION` -> AssignedEntitiesTile * `APPLICATION_METHOD` -> AssignedEntitiesTile * `LOG_ANALYTICS` -> AssignedEntitiesTile * `OPENSTACK` -> AssignedEntitiesTile * `OPENSTACK_PROJECT` -> AssignedEntitiesTile * `OPENSTACK_AV_ZONE` -> AssignedEntitiesTile * `DEVICE_APPLICATION_METHOD` -> AssignedEntitiesTile * `DEM_KEY_USER_ACTION` -> AssignedEntitiesTile * `SLO` -> AssignedEntitiesWithMetricTile * `SCALABLE_LIST` -> ScalableListTile * `HEADER` -> Tile * `OPEN_PROBLEMS` -> ProblemTile * `PURE_MODEL` -> Tile * `DOCKER` -> Tile * `NETWORK_MEDIUM` -> Tile * `APPLICATIONS_MOST_ACTIVE` -> Tile * `NETWORK` -> Tile * `UEM_ACTIVE_SESSIONS` -> Tile * `DCRUM_SERVICES` -> Tile Элемент может принимать следующие значения * `APPLICATION` * `APPLICATIONS` * `APPLICATIONS_MOST_ACTIVE` * `APPLICATION_METHOD` * `APPLICATION_WORLDMAP` * `AWS` * `BOUNCE_RATE` * `CUSTOM_APPLICATION` * `CUSTOM_CHARTING` * `DATABASE` * `DATABASES_OVERVIEW` * `DATA_EXPLORER` * `DCRUM_SERVICES` * `DEM_KEY_USER_ACTION` * `DEVICE_APPLICATION_METHOD` * `DOCKER` * `DTAQL` * `HEADER` * `HOST` * `HOSTS` * `IMAGE` * `LOG_ANALYTICS` * `MARKDOWN` * `MOBILE_APPLICATION` * `NETWORK` * `NETWORK_MEDIUM` * `OPENSTACK` * `OPENSTACK_AV_ZONE` * `OPENSTACK_PROJECT` * `OPEN_PROBLEMS` * `PROCESS_GROUPS_ONE` * `PURE_MODEL` * `RESOURCES` * `SCALABLE_LIST` * `SERVICES` * `SERVICE_VERSATILE` * `SESSION_METRICS` * `SLO` * `SYNTHETIC_HTTP_MONITOR` * `SYNTHETIC_SINGLE_EXT_TEST` * `SYNTHETIC_SINGLE_WEBCHECK` * `SYNTHETIC_TESTS` * `THIRD_PARTY_MOST_ACTIVE` * `UEM_ACTIVE_SESSIONS` * `UEM_CONVERSIONS_OVERALL` * `UEM_CONVERSIONS_PER_GOAL` * `UEM_JSERRORS_OVERALL` * `UEM_KEY_USER_ACTIONS` * `USERS` * `VIRTUALIZATION` |

#### Объект `TileBounds`

Позиция и размер плитки.

| Элемент | Тип | Описание |
| --- | --- | --- |
| height | integer | Высота плитки в пикселях. |
| left | integer | Расстояние по горизонтали от верхнего левого угла дашборда до верхнего левого угла плитки, в пикселях. |
| top | integer | Расстояние по вертикали от верхнего левого угла дашборда до верхнего левого угла плитки, в пикселях. |
| width | integer | Ширина плитки в пикселях. |

#### Объект `TileFilter`

Фильтр, применяемый к плитке.

Он переопределяет фильтр дашборда.

| Элемент | Тип | Описание |
| --- | --- | --- |
| managementZone | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Краткое представление Dynatrace сущности. |
| timeframe | string | Временной интервал плитки по умолчанию. |

#### Объект `EntityShortRepresentation`

Краткое представление Dynatrace сущности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание Dynatrace сущности. |
| id | string | ID Dynatrace сущности. |
| name | string | Название Dynatrace сущности. |

```
{



"name": "Tile",



"nameSize": "",



"tileType": "TILE",



"configured": true,



"bounds": {



"top": 112,



"left": 45,



"width": 304,



"height": 304



},



"tileFilter": {



"timeframe": null,



"managementZone": null



}



}
```

## UserSessionQueryTile

Этот тип применяется к следующим плиткам:

* Запрос сеанса пользователя (`DTAQL`)

UserSessionQueryTile

Параметры

JSON model

#### Объект `UserSessionQueryTile`

Конфигурация плитки User session query.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customName | string | Название плитки, заданное пользователем. |
| limit | integer | Лимит результатов, если не задан, используется значение системы по умолчанию |
| query | string | [Запрос сеанса пользователя﻿](https://dt-url.net/dtusql?dt=m), выполняемый плиткой. |
| timeFrameShift | string | Временной период сравнения запроса. Если указан, дополнительно возвращаются результаты того же запроса со сдвигом на указанный период. |
| type | string | Визуализация плитки. Элемент может принимать следующие значения * `COLUMN_CHART` * `FUNNEL` * `LINE_CHART` * `NOT_CONFIGURED` * `PIE_CHART` * `SINGLE_VALUE` * `TABLE` |
| visualizationConfig | [UserSessionQueryTileConfiguration](#openapi-definition-UserSessionQueryTileConfiguration) | Конфигурация плитки визуализации User session query. |

#### Объект `UserSessionQueryTileConfiguration`

Конфигурация плитки визуализации User session query.

| Элемент | Тип | Описание |
| --- | --- | --- |
| hasAxisBucketing | boolean | Группировка по оси, при включении объединяет похожие серии на одной виртуальной оси. |

```
{



"name": "User Sessions Query",



"tileType": "DTAQL",



"configured": true,



"bounds": {



"top": 112,



"left": 45,



"width": 304,



"height": 304



},



"tileFilter": {



"timeframe": "Today",



"managementZone": {



"id": "9130632296508575249",



"name": "Easytravel"



}



},



"customName": "User sessions query results",



"query": " SELECT country, city, COUNT(*) FROM usersession GROUP BY country, city",



"type": "COLUMN_CHART"



}
```

## Похожие темы

* [Dashboards](/managed/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.")