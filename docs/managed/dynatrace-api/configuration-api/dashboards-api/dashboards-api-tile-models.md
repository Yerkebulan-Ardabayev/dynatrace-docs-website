---
title: "Dashboards API - Tile JSON models"
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/dashboards-api/dashboards-api-tile-models
updated: 2026-02-09
---

# Dashboards API - Tile JSON models

# Dashboards API - Tile JSON models

* Reference
* Published Mar 11, 2019

JSON models of dashboard tiles vary greatly, depending on the type of the tile. The JSON models for each tile type are listed below.

## AssignedEntitiesTile

This type applies to the following tiles:

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
* User action (`APPLICATION_METHOD` or `APPLICATION_METHOD`)

AssignedEntitiesTile

Parameters

JSON model

#### The `AssignedEntitiesTile` object

Configuration of a tile with an assigned Dynatrace entity.

An example is the Bounce rate tile, showing the data from an assigned application.

| Element | Type | Description |
| --- | --- | --- |
| assignedEntities | string[] | The list of Dynatrace entities, assigned to the tile. |

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

This type applies to the following tiles:

* Application health (`APPLICATIONS`)
* Database health (`DATABASES_OVERVIEW`)
* Host health (`HOSTS`)
* Service health (`SERVICES`)
* Synthetic monitor health (`SYNTHETIC_TESTS`)

FilterableEntityTile

Parameters

JSON model

#### The `FilterableEntityTile` object

Configuration of a tile with the built-in custom filter.

An example is the Service health tile, which may use a custom timeframe.

| Element | Type | Description |
| --- | --- | --- |
| chartVisible | boolean | - |
| filterConfig | [CustomFilterConfig](#openapi-definition-CustomFilterConfig) | Configuration of the custom filter of a tile. |

#### The `CustomFilterConfig` object

Configuration of the custom filter of a tile.

| Element | Type | Description |
| --- | --- | --- |
| chartConfig | [CustomFilterChartConfig](#openapi-definition-CustomFilterChartConfig) | Configuration of a custom chart. |
| customName | string | The name of the tile, set by user |
| defaultName | string | The default name of the tile |
| filtersPerEntityType | object | A list of filters, applied to specific entity types. |
| type | string | The type of the filter.  It shows to which entity the filter belongs.  Custom charts have the `MIXED` type. The element can hold these values * `ALB` * `APPLICATION` * `APPLICATION_METHOD` * `APPMON` * `ASG` * `AWS_CREDENTIALS` * `AWS_CUSTOM_SERVICE` * `AWS_LAMBDA_FUNCTION` * `CLOUD_APPLICATION` * `CLOUD_APPLICATION_INSTANCE` * `CLOUD_APPLICATION_NAMESPACE` * `CONTAINER_GROUP_INSTANCE` * `CUSTOM_APPLICATION` * `CUSTOM_DEVICES` * `CUSTOM_SERVICES` * `DATABASE` * `DATABASE_KEY_REQUEST` * `DCRUM_APPLICATION` * `DCRUM_ENTITY` * `DYNAMO_DB` * `EBS` * `EC2` * `ELB` * `ENVIRONMENT` * `ESXI` * `EXTERNAL_SYNTHETIC_TEST` * `GLOBAL_BACKGROUND_ACTIVITY` * `HOST` * `IOT` * `KUBERNETES_CLUSTER` * `KUBERNETES_NODE` * `MDA_SERVICE` * `MIXED` * `MOBILE_APPLICATION` * `MONITORED_ENTITY` * `NLB` * `PG_BACKGROUND_ACTIVITY` * `PROBLEM` * `PROCESS_GROUP_INSTANCE` * `RDS` * `REMOTE_PLUGIN` * `SERVICE` * `SERVICE_KEY_REQUEST` * `SYNTHETIC_BROWSER_MONITOR` * `SYNTHETIC_HTTPCHECK` * `SYNTHETIC_HTTPCHECK_STEP` * `SYNTHETIC_LOCATION` * `SYNTHETIC_TEST` * `SYNTHETIC_TEST_STEP` * `UI_ENTITY` * `VIRTUAL_MACHINE` * `WEB_CHECK` |

#### The `CustomFilterChartConfig` object

Configuration of a custom chart.

| Element | Type | Description |
| --- | --- | --- |
| axisLimits | object | The optional custom y-axis limits. |
| leftAxisCustomUnit | string | The custom unit for the left Y-axis. The element can hold these values * `Ampere` * `Billion` * `Bit` * `BitPerHour` * `BitPerMinute` * `BitPerSecond` * `Byte` * `BytePerHour` * `BytePerMinute` * `BytePerSecond` * `Cores` * `Count` * `Day` * `DecibelMilliWatt` * `GibiByte` * `GibiBytePerHour` * `GibiBytePerMinute` * `GibiBytePerSecond` * `Giga` * `GigaByte` * `GigaBytePerHour` * `GigaBytePerMinute` * `GigaBytePerSecond` * `Hertz` * `Hour` * `KibiByte` * `KibiBytePerHour` * `KibiBytePerMinute` * `KibiBytePerSecond` * `Kilo` * `KiloByte` * `KiloBytePerHour` * `KiloBytePerMinute` * `KiloBytePerSecond` * `KiloMetrePerHour` * `MSU` * `MebiByte` * `MebiBytePerHour` * `MebiBytePerMinute` * `MebiBytePerSecond` * `Mega` * `MegaByte` * `MegaBytePerHour` * `MegaBytePerMinute` * `MegaBytePerSecond` * `MetrePerHour` * `MetrePerSecond` * `MicroSecond` * `MilliCores` * `MilliSecond` * `MilliSecondPerMinute` * `Million` * `Minute` * `Month` * `NanoSecond` * `NanoSecondPerMinute` * `NotApplicable` * `PerHour` * `PerMinute` * `PerSecond` * `Percent` * `Pixel` * `Promille` * `Ratio` * `Second` * `State` * `Trillion` * `Unspecified` * `Volt` * `Watt` * `Week` * `Year` |
| legendShown | boolean | Defines if a legend should be shown. |
| resultMetadata | object | Additional information about charted metric. |
| rightAxisCustomUnit | string | The custom unit for the right Y-axis. The element can hold these values * `Ampere` * `Billion` * `Bit` * `BitPerHour` * `BitPerMinute` * `BitPerSecond` * `Byte` * `BytePerHour` * `BytePerMinute` * `BytePerSecond` * `Cores` * `Count` * `Day` * `DecibelMilliWatt` * `GibiByte` * `GibiBytePerHour` * `GibiBytePerMinute` * `GibiBytePerSecond` * `Giga` * `GigaByte` * `GigaBytePerHour` * `GigaBytePerMinute` * `GigaBytePerSecond` * `Hertz` * `Hour` * `KibiByte` * `KibiBytePerHour` * `KibiBytePerMinute` * `KibiBytePerSecond` * `Kilo` * `KiloByte` * `KiloBytePerHour` * `KiloBytePerMinute` * `KiloBytePerSecond` * `KiloMetrePerHour` * `MSU` * `MebiByte` * `MebiBytePerHour` * `MebiBytePerMinute` * `MebiBytePerSecond` * `Mega` * `MegaByte` * `MegaBytePerHour` * `MegaBytePerMinute` * `MegaBytePerSecond` * `MetrePerHour` * `MetrePerSecond` * `MicroSecond` * `MilliCores` * `MilliSecond` * `MilliSecondPerMinute` * `Million` * `Minute` * `Month` * `NanoSecond` * `NanoSecondPerMinute` * `NotApplicable` * `PerHour` * `PerMinute` * `PerSecond` * `Percent` * `Pixel` * `Promille` * `Ratio` * `Second` * `State` * `Trillion` * `Unspecified` * `Volt` * `Watt` * `Week` * `Year` |
| series | [CustomFilterChartSeriesConfig[]](#openapi-definition-CustomFilterChartSeriesConfig) | A list of charted metrics. |
| type | string | The type of the chart. The element can hold these values * `PIE` * `SINGLE_VALUE` * `TIMESERIES` * `TOP_LIST` |

#### The `CustomChartingItemMetadataConfig` object

Additional metadata for charted metric.

| Element | Type | Description |
| --- | --- | --- |
| customColor | string | The color of the metric in the chart, hex format. |
| lastModified | integer | The timestamp of the last metadata modification, in UTC milliseconds. |

#### The `CustomFilterChartSeriesConfig` object

Configuration of a charted metric.

| Element | Type | Description |
| --- | --- | --- |
| aggregation | string | The charted aggregation of the metric. The element can hold these values * `AVG` * `COUNT` * `DISTINCT` * `FASTEST10PERCENT` * `MAX` * `MEDIAN` * `MIN` * `NONE` * `OF_INTEREST_RATIO` * `OTHER_RATIO` * `PERCENTILE` * `PER_MIN` * `SLOWEST10PERCENT` * `SLOWEST5PERCENT` * `SUM` * `SUM_DIMENSIONS` |
| aggregationRate | string | -The element can hold these values * `HOUR` * `MINUTE` * `SECOND` * `TOTAL` |
| dimensions | [CustomFilterChartSeriesDimensionConfig[]](#openapi-definition-CustomFilterChartSeriesDimensionConfig) | Configuration of the charted metric splitting. |
| entityType | string | The type of the Dynatrace entity that delivered the charted metric. |
| metric | string | The name of the charted metric. |
| percentile | integer | The charted percentile.  Only applicable if the **aggregation** is set to `PERCENTILE`. |
| sortAscending | boolean | Sort ascending (`true`) or descending (`false`). |
| sortColumn | boolean | - |
| type | string | The visualization of the timeseries chart. The element can hold these values * `AREA` * `BAR` * `LINE` |

#### The `CustomFilterChartSeriesDimensionConfig` object

Configuration of the charted metric splitting.

| Element | Type | Description |
| --- | --- | --- |
| entityDimension | boolean | - |
| id | string | The ID of the dimension by which the metric is split. |
| name | string | The name of the dimension by which the metric is split. |
| values | string[] | The splitting value. |

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

This type applies to the following tiles:

* World map (`APPLICATION_WORLDMAP`)
* Host (`HOST`)
* Process group (`PROCESS_GROUPS_ONE`)
* Resources (`RESOURCES`)
* Most used 3rd parties (`THIRD_PARTY_MOST_ACTIVE`)
* Conversion goal (`UEM_CONVERSIONS_PER_GOAL`)

AssignedEntitiesWithMetricTile

Parameters

JSON model

#### The `AssignedEntitiesWithMetricTile` object

Configuration of a tile with an assigned Dynatrace entity and an assigned metric.

An example is the Worldmap tile, showing the data from an assigned performance or behavior metric of an assigned application.

| Element | Type | Description |
| --- | --- | --- |
| assignedEntities | string[] | The list of Dynatrace entities, assigned to the tile. |
| metric | string | The metric assigned to the tile. |

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

This type applies to the following tiles:

* Data Explorer tile (`DATA_EXPLORER`)

DataExplorerTile

Parameters

JSON model

#### The `DataExplorerTile` object

Configuration of a data explorer tile.

| Element | Type | Description |
| --- | --- | --- |
| customName | string | The name of the tile, set by user. |
| metricExpressions | string[] | The metric expressions generated by this configuration |
| queries | [DataExplorerQuery[]](#openapi-definition-DataExplorerQuery) | The list queries to explore |
| queriesSettings | [DataExplorerQuerySettings](#openapi-definition-DataExplorerQuerySettings) | Configuration for the queries |
| visualConfig | [VisualizationConfiguration](#openapi-definition-VisualizationConfiguration) | Configuration of a visualization. |

#### The `DataExplorerQuery` object

Configuration of a data explorer query.

| Element | Type | Description |
| --- | --- | --- |
| defaultValue | number | Replaces null data points with the provided value |
| enabled | boolean | Status of the query |
| filterBy | [DataExplorerFilter](#openapi-definition-DataExplorerFilter) | Filter for data explorer queries. |
| foldTransformation | string | The fold transformation The element can hold these values * `LAST_VALUE` * `TOTAL` |
| generatedMetricSelector | string | Generated metric selector |
| id | string | The id of the query |
| limit | integer | Limit the results of the query |
| metric | string | The metric id |
| metricSelector | string | The metric selector |
| rate | string | Converts a count-based metric (for example, bytes) into a rate-based metric (bytes per second) The element can hold these values * `HOUR` * `MINUTE` * `MONTH` * `NONE` * `SECOND` * `WEEK` * `YEAR` |
| sortBy | string | The order of the sorting applied to the query The element can hold these values * `ASC` * `DESC` |
| sortByDimension | string | The dimension where sorting is applied. Sorting by value if null |
| spaceAggregation | string | Space aggregation applied to the query The element can hold these values * `AUTO` * `AVG` * `COUNT` * `MAX` * `MEDIAN` * `MIN` * `PERCENTILE_10` * `PERCENTILE_75` * `PERCENTILE_90` * `SUM` * `VALUE` |
| splitBy | string[] | The splittings applied to the query |
| timeAggregation | string | Time roll up applied to the query The element can hold these values * `AVG` * `COUNT` * `DEFAULT` * `MAX` * `MEDIAN` * `MIN` * `SUM` * `VALUE` |
| timeShift | [DataExplorerTimeShift](#openapi-definition-DataExplorerTimeShift) | TimeShift for data explorer queries. |

#### The `DataExplorerFilter` object

Filter for data explorer queries.

| Element | Type | Description |
| --- | --- | --- |
| criteria | [DexpFilterCriterion[]](#openapi-definition-DexpFilterCriterion) | - |
| entityAttribute | string | - |
| filter | string | - |
| filterOperator | string | -The element can hold these values * `AND` * `NOT` * `OR` |
| filterType | string | -The element can hold these values * `DIMENSION` * `ENTITY_ATTRIBUTE` * `ID` * `NAME` * `TAG` |
| globalEntity | string | - |
| nestedFilters | [DataExplorerFilter[]](#openapi-definition-DataExplorerFilter) | - |
| relationship | [DexpFilterRelationship](#openapi-definition-DexpFilterRelationship) | - |

#### The `DexpFilterCriterion` object

Criterion for data explorer filters.

| Element | Type | Description |
| --- | --- | --- |
| evaluator | string | -The element can hold these values * `EQ` * `IN` * `NE` * `PREFIX` |
| matchExactly | boolean | - |
| value | string | - |

#### The `DexpFilterRelationship` object

| Element | Type | Description |
| --- | --- | --- |
| id | string | The id of the relationship. e.g runsOn, isStepOf, etc |
| targetEntity | string | The target entity of the relationship. e.g HOST, VCENTER, SERVICE etc |
| type | string | The type of the relationship The element can hold these values * `fromRelationship` * `toRelationship` |

#### The `DataExplorerTimeShift` object

TimeShift for data explorer queries.

| Element | Type | Description |
| --- | --- | --- |
| factor | integer | - |
| unit | string | -The element can hold these values * `DAY` * `HOUR` * `MINUTE` * `SECOND` * `WEEK` |

#### The `DataExplorerQuerySettings` object

Configuration for the queries

| Element | Type | Description |
| --- | --- | --- |
| foldAggregation | string | The fold aggregation The element can hold these values * `AUTO` * `AVG` * `COUNT` * `MAX` * `MEDIAN` * `MIN` * `PERCENTILE_10` * `PERCENTILE_75` * `PERCENTILE_90` * `SUM` * `VALUE` |
| foldTransformation | string | The fold transformation The element can hold these values * `LAST_VALUE` * `TOTAL` |
| globalLimitQueryId | string | The query id of global limit metric |
| resolution | string | The resolution |

#### The `VisualizationConfiguration` object

Configuration of a visualization.

| Element | Type | Description |
| --- | --- | --- |
| axes | [Axes](#openapi-definition-Axes) | Axes configuration |
| global | [VisualizationGlobalProperties](#openapi-definition-VisualizationGlobalProperties) | Visualization global configuration |
| graphChartSettings | [GraphChartSettings](#openapi-definition-GraphChartSettings) | Settings for graph chart visualization |
| heatmapSettings | [HeatmapSettings](#openapi-definition-HeatmapSettings) | Settings for heatmap visualization |
| honeycombSettings | [HoneycombSettings](#openapi-definition-HoneycombSettings) | Settings for honeycomb visualization |
| rules | [VisualizationRule[]](#openapi-definition-VisualizationRule) | Rules for Visualization |
| singleValueSettings | [SingleValueSettings](#openapi-definition-SingleValueSettings) | Settings for single value visualization |
| tableSettings | [TableSettings](#openapi-definition-TableSettings) | Settings for table visualization |
| thresholds | [VisualizationThreshold[]](#openapi-definition-VisualizationThreshold) | Thresholds for Visualization |
| type | string | The id of the query The element can hold these values * `GRAPH_CHART` * `HEATMAP` * `HONEYCOMB` * `PIE_CHART` * `SINGLE_VALUE` * `STACKED_AREA` * `STACKED_COLUMN` * `TABLE` * `TOP_LIST` |

#### The `Axes` object

Axes configuration

| Element | Type | Description |
| --- | --- | --- |
| xAxis | [Axis](#openapi-definition-Axis) | x Axis configuration |
| yAxes | [YAxis[]](#openapi-definition-YAxis) | y Axes configuration |

#### The `Axis` object

x Axis configuration

| Element | Type | Description |
| --- | --- | --- |
| displayName | string | - |
| visible | boolean | - |

#### The `YAxis` object

y Axes configuration

| Element | Type | Description |
| --- | --- | --- |
| defaultAxis | boolean | - |
| displayName | string | - |
| max | string | - |
| min | string | - |
| position | string | -The element can hold these values * `LEFT` * `RIGHT` |
| queryIds | string[] | - |
| visible | boolean | - |

#### The `VisualizationGlobalProperties` object

Visualization global configuration

| Element | Type | Description |
| --- | --- | --- |
| hasTrendline | boolean | - |
| hideLegend | boolean | - |
| seriesType | string | -The element can hold these values * `AREA` * `COLUMN` * `LINE` * `STACKED_AREA` * `STACKED_COLUMN` |
| theme | string | -The element can hold these values * `BLUE` * `DEFAULT` * `GRAY` * `GREEN` * `ORANGE` * `PURPLE` * `RED` * `ROYALBLUE` * `TURQUOISE` * `YELLOW` |
| threshold | [VisualizationThreshold](#openapi-definition-VisualizationThreshold) | Thresholds for Visualization |

#### The `VisualizationThreshold` object

Thresholds for Visualization

| Element | Type | Description |
| --- | --- | --- |
| axisTarget | string | -The element can hold these values * `LEFT` * `RIGHT` |
| columnId | string | - |
| queryId | string | - |
| rules | [VisualizationThresholdRule[]](#openapi-definition-VisualizationThresholdRule) | - |
| visible | boolean | - |

#### The `VisualizationThresholdRule` object

| Element | Type | Description |
| --- | --- | --- |
| color | string | - |
| value | number | - |

#### The `GraphChartSettings` object

Settings for graph chart visualization

| Element | Type | Description |
| --- | --- | --- |
| connectNulls | boolean | - |

#### The `HeatmapSettings` object

Settings for heatmap visualization

| Element | Type | Description |
| --- | --- | --- |
| showLabels | boolean | - |
| xAxisBuckets | integer | Number of buckets in the X axis |
| yAxis | string | Y axis aggregation criteria The element can hold these values * `DIMENSIONS` * `VALUE` |
| yAxisBuckets | integer | Number of buckets in the Y axis |

#### The `HoneycombSettings` object

Settings for honeycomb visualization

| Element | Type | Description |
| --- | --- | --- |
| showHive | boolean | - |
| showLabels | boolean | - |
| showLegend | boolean | - |

#### The `VisualizationRule` object

Rules for Visualization

| Element | Type | Description |
| --- | --- | --- |
| matcher | string | - |
| properties | [VisualizationProperties](#openapi-definition-VisualizationProperties) | - |
| seriesOverrides | [VisualizationSerieOverride[]](#openapi-definition-VisualizationSerieOverride) | - |
| unitTransform | string | - |
| valueFormat | string | - |

#### The `VisualizationProperties` object

| Element | Type | Description |
| --- | --- | --- |
| alias | string | - |
| color | string | - |
| seriesType | string | -The element can hold these values * `AREA` * `COLUMN` * `LINE` * `STACKED_AREA` * `STACKED_COLUMN` |

#### The `VisualizationSerieOverride` object

| Element | Type | Description |
| --- | --- | --- |
| color | string | - |
| name | string | - |

#### The `SingleValueSettings` object

Settings for single value visualization

| Element | Type | Description |
| --- | --- | --- |
| linkTileColorToThreshold | boolean | - |
| showSparkLine | boolean | - |
| showTrend | boolean | - |

#### The `TableSettings` object

Settings for table visualization

| Element | Type | Description |
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

This type applies to the following tiles:

* Custom chart (`CUSTOM_CHARTING`)

CustomChartingTile

Parameters

JSON model

#### The `CustomChartingTile` object

Configuration of a custom chart tile.

| Element | Type | Description |
| --- | --- | --- |
| filterConfig | [CustomFilterConfig](#openapi-definition-CustomFilterConfig) | Configuration of the custom filter of a tile. |

#### The `CustomFilterConfig` object

Configuration of the custom filter of a tile.

| Element | Type | Description |
| --- | --- | --- |
| chartConfig | [CustomFilterChartConfig](#openapi-definition-CustomFilterChartConfig) | Configuration of a custom chart. |
| customName | string | The name of the tile, set by user |
| defaultName | string | The default name of the tile |
| filtersPerEntityType | object | A list of filters, applied to specific entity types. |
| type | string | The type of the filter.  It shows to which entity the filter belongs.  Custom charts have the `MIXED` type. The element can hold these values * `ALB` * `APPLICATION` * `APPLICATION_METHOD` * `APPMON` * `ASG` * `AWS_CREDENTIALS` * `AWS_CUSTOM_SERVICE` * `AWS_LAMBDA_FUNCTION` * `CLOUD_APPLICATION` * `CLOUD_APPLICATION_INSTANCE` * `CLOUD_APPLICATION_NAMESPACE` * `CONTAINER_GROUP_INSTANCE` * `CUSTOM_APPLICATION` * `CUSTOM_DEVICES` * `CUSTOM_SERVICES` * `DATABASE` * `DATABASE_KEY_REQUEST` * `DCRUM_APPLICATION` * `DCRUM_ENTITY` * `DYNAMO_DB` * `EBS` * `EC2` * `ELB` * `ENVIRONMENT` * `ESXI` * `EXTERNAL_SYNTHETIC_TEST` * `GLOBAL_BACKGROUND_ACTIVITY` * `HOST` * `IOT` * `KUBERNETES_CLUSTER` * `KUBERNETES_NODE` * `MDA_SERVICE` * `MIXED` * `MOBILE_APPLICATION` * `MONITORED_ENTITY` * `NLB` * `PG_BACKGROUND_ACTIVITY` * `PROBLEM` * `PROCESS_GROUP_INSTANCE` * `RDS` * `REMOTE_PLUGIN` * `SERVICE` * `SERVICE_KEY_REQUEST` * `SYNTHETIC_BROWSER_MONITOR` * `SYNTHETIC_HTTPCHECK` * `SYNTHETIC_HTTPCHECK_STEP` * `SYNTHETIC_LOCATION` * `SYNTHETIC_TEST` * `SYNTHETIC_TEST_STEP` * `UI_ENTITY` * `VIRTUAL_MACHINE` * `WEB_CHECK` |

#### The `CustomFilterChartConfig` object

Configuration of a custom chart.

| Element | Type | Description |
| --- | --- | --- |
| axisLimits | object | The optional custom y-axis limits. |
| leftAxisCustomUnit | string | The custom unit for the left Y-axis. The element can hold these values * `Ampere` * `Billion` * `Bit` * `BitPerHour` * `BitPerMinute` * `BitPerSecond` * `Byte` * `BytePerHour` * `BytePerMinute` * `BytePerSecond` * `Cores` * `Count` * `Day` * `DecibelMilliWatt` * `GibiByte` * `GibiBytePerHour` * `GibiBytePerMinute` * `GibiBytePerSecond` * `Giga` * `GigaByte` * `GigaBytePerHour` * `GigaBytePerMinute` * `GigaBytePerSecond` * `Hertz` * `Hour` * `KibiByte` * `KibiBytePerHour` * `KibiBytePerMinute` * `KibiBytePerSecond` * `Kilo` * `KiloByte` * `KiloBytePerHour` * `KiloBytePerMinute` * `KiloBytePerSecond` * `KiloMetrePerHour` * `MSU` * `MebiByte` * `MebiBytePerHour` * `MebiBytePerMinute` * `MebiBytePerSecond` * `Mega` * `MegaByte` * `MegaBytePerHour` * `MegaBytePerMinute` * `MegaBytePerSecond` * `MetrePerHour` * `MetrePerSecond` * `MicroSecond` * `MilliCores` * `MilliSecond` * `MilliSecondPerMinute` * `Million` * `Minute` * `Month` * `NanoSecond` * `NanoSecondPerMinute` * `NotApplicable` * `PerHour` * `PerMinute` * `PerSecond` * `Percent` * `Pixel` * `Promille` * `Ratio` * `Second` * `State` * `Trillion` * `Unspecified` * `Volt` * `Watt` * `Week` * `Year` |
| legendShown | boolean | Defines if a legend should be shown. |
| resultMetadata | object | Additional information about charted metric. |
| rightAxisCustomUnit | string | The custom unit for the right Y-axis. The element can hold these values * `Ampere` * `Billion` * `Bit` * `BitPerHour` * `BitPerMinute` * `BitPerSecond` * `Byte` * `BytePerHour` * `BytePerMinute` * `BytePerSecond` * `Cores` * `Count` * `Day` * `DecibelMilliWatt` * `GibiByte` * `GibiBytePerHour` * `GibiBytePerMinute` * `GibiBytePerSecond` * `Giga` * `GigaByte` * `GigaBytePerHour` * `GigaBytePerMinute` * `GigaBytePerSecond` * `Hertz` * `Hour` * `KibiByte` * `KibiBytePerHour` * `KibiBytePerMinute` * `KibiBytePerSecond` * `Kilo` * `KiloByte` * `KiloBytePerHour` * `KiloBytePerMinute` * `KiloBytePerSecond` * `KiloMetrePerHour` * `MSU` * `MebiByte` * `MebiBytePerHour` * `MebiBytePerMinute` * `MebiBytePerSecond` * `Mega` * `MegaByte` * `MegaBytePerHour` * `MegaBytePerMinute` * `MegaBytePerSecond` * `MetrePerHour` * `MetrePerSecond` * `MicroSecond` * `MilliCores` * `MilliSecond` * `MilliSecondPerMinute` * `Million` * `Minute` * `Month` * `NanoSecond` * `NanoSecondPerMinute` * `NotApplicable` * `PerHour` * `PerMinute` * `PerSecond` * `Percent` * `Pixel` * `Promille` * `Ratio` * `Second` * `State` * `Trillion` * `Unspecified` * `Volt` * `Watt` * `Week` * `Year` |
| series | [CustomFilterChartSeriesConfig[]](#openapi-definition-CustomFilterChartSeriesConfig) | A list of charted metrics. |
| type | string | The type of the chart. The element can hold these values * `PIE` * `SINGLE_VALUE` * `TIMESERIES` * `TOP_LIST` |

#### The `CustomChartingItemMetadataConfig` object

Additional metadata for charted metric.

| Element | Type | Description |
| --- | --- | --- |
| customColor | string | The color of the metric in the chart, hex format. |
| lastModified | integer | The timestamp of the last metadata modification, in UTC milliseconds. |

#### The `CustomFilterChartSeriesConfig` object

Configuration of a charted metric.

| Element | Type | Description |
| --- | --- | --- |
| aggregation | string | The charted aggregation of the metric. The element can hold these values * `AVG` * `COUNT` * `DISTINCT` * `FASTEST10PERCENT` * `MAX` * `MEDIAN` * `MIN` * `NONE` * `OF_INTEREST_RATIO` * `OTHER_RATIO` * `PERCENTILE` * `PER_MIN` * `SLOWEST10PERCENT` * `SLOWEST5PERCENT` * `SUM` * `SUM_DIMENSIONS` |
| aggregationRate | string | -The element can hold these values * `HOUR` * `MINUTE` * `SECOND` * `TOTAL` |
| dimensions | [CustomFilterChartSeriesDimensionConfig[]](#openapi-definition-CustomFilterChartSeriesDimensionConfig) | Configuration of the charted metric splitting. |
| entityType | string | The type of the Dynatrace entity that delivered the charted metric. |
| metric | string | The name of the charted metric. |
| percentile | integer | The charted percentile.  Only applicable if the **aggregation** is set to `PERCENTILE`. |
| sortAscending | boolean | Sort ascending (`true`) or descending (`false`). |
| sortColumn | boolean | - |
| type | string | The visualization of the timeseries chart. The element can hold these values * `AREA` * `BAR` * `LINE` |

#### The `CustomFilterChartSeriesDimensionConfig` object

Configuration of the charted metric splitting.

| Element | Type | Description |
| --- | --- | --- |
| entityDimension | boolean | - |
| id | string | The ID of the dimension by which the metric is split. |
| name | string | The name of the dimension by which the metric is split. |
| values | string[] | The splitting value. |

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

This type applies to the following tiles:

* Markdown (`MARKDOWN`)

MarkdownTile

Parameters

JSON model

#### The `MarkdownTile` object

Configuration of the Markdown tile.

| Element | Type | Description |
| --- | --- | --- |
| markdown | string | The markdown-formatted content of the tile. |

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

This type applies to the following tiles:

* Problems (`OPEN_PROBLEMS`)

ProblemTile

Parameters

JSON model

#### The `ProblemTile` object

Configuration of a problem tile.

| Element | Type | Description |
| --- | --- | --- |
| entitySelector | string | The entity scope of the problem tile. For further information please look at the Problems API v2 '/problems' endpoint. |
| problemSelector | string | Defines the scope of the problem tile. Only problems matching the specified criteria are taken into account. For further information please look at the Problems API v2 '/problems' endpoint. |
| useBackgroundColor | boolean | Use background color based on problem status: Red if there are open problems, green otherwise. |

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

#### The `ScalableListTile` object

Configuration of a tile with the built-in custom filter id. This is only for internal usage.

| Element | Type | Description |
| --- | --- | --- |
| chartVisible | boolean | - |
| customFilterId | string | The ID of the custom filter. |
| entitySpecificTileType | string | The type of the entity specific tile. The element can hold these values * `APPLICATION` * `APPLICATIONS` * `APPLICATIONS_MOST_ACTIVE` * `APPLICATION_WORLDMAP` * `AWS` * `BOUNCE_RATE` * `CUSTOM_APPLICATION` * `CUSTOM_CHARTING` * `DATABASE` * `DATABASES_OVERVIEW` * `DATA_EXPLORER` * `DCRUM_SERVICES` * `DEM_KEY_USER_ACTION` * `DTAQL` * `HEADER` * `HOST` * `HOSTS` * `IMAGE` * `LOGS_EVENTS_QUERY` * `LOG_ANALYTICS` * `LOG_QUERY` * `MARKDOWN` * `MOBILE_APPLICATION` * `NETWORK` * `NETWORK_MEDIUM` * `OPEN_PROBLEMS` * `PROCESS_GROUPS_ONE` * `PURE_MODEL` * `RESOURCES` * `SCALABLE_LIST` * `SERVICES` * `SERVICE_VERSATILE` * `SESSION_METRICS` * `SLO` * `SYNTHETIC_HTTP_MONITOR` * `SYNTHETIC_SINGLE_EXT_TEST` * `SYNTHETIC_SINGLE_WEBCHECK` * `SYNTHETIC_TESTS` * `THIRD_PARTY_MOST_ACTIVE` * `UEM_ACTIVE_SESSIONS` * `UEM_CONVERSIONS_OVERALL` * `UEM_CONVERSIONS_PER_GOAL` * `UEM_JSERRORS_OVERALL` * `UEM_KEY_USER_ACTIONS` * `USERS` * `VIRTUALIZATION` |

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

This type applies to the following tiles:

* Browser monitor (`SYNTHETIC_SINGLE_WEBCHECK`)

SyntheticSingleWebcheckTile

Parameters

JSON model

#### The `SyntheticSingleWebcheckTile` object

Configuration of the Browser monitor tile.

| Element | Type | Description |
| --- | --- | --- |
| assignedEntities | string[] | The list of Dynatrace entities, assigned to the tile. |
| excludeMaintenanceWindows | boolean | Include (`false') or exclude (`true`) maintenance windows from availability calculations. |

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

This type applies to the following tiles:

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

#### The `Tile` object

Configuration of a tile.

The actual set of fields depends on the type of the tile. Find the list of actual objects in the description of the **tileType** field or see [Dashboards API - Tile JSON modelsï»¿](https://dt-url.net/2wc3spx).

| Element | Type | Description |
| --- | --- | --- |
| bounds | [TileBounds](#openapi-definition-TileBounds) | The position and size of a tile. |
| configured | boolean | The tile is configured and ready to use (`true`) or just placed on the dashboard (`false`). |
| isAutoRefreshDisabled | boolean | The tile auto refresh is disabled. Only works for certain tile types. |
| name | string | The name of the tile. |
| nameSize | string | The size of the tile name. Default value is null. The element can hold these values * `small` * `medium` * `large` |
| tileFilter | [TileFilter](#openapi-definition-TileFilter) | A filter applied to a tile.  It overrides dashboard's filter. |
| tileType | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `DATA_EXPLORER` -> DataExplorerTile * `CUSTOM_CHARTING` -> CustomChartingTile * `DTAQL` -> UserSessionQueryTile * `MARKDOWN` -> MarkdownTile * `IMAGE` -> ImageTile * `HOSTS` -> FilterableEntityTile * `APPLICATIONS` -> FilterableEntityTile * `SERVICES` -> FilterableEntityTile * `DATABASES_OVERVIEW` -> FilterableEntityTile * `SYNTHETIC_TESTS` -> FilterableEntityTile * `APPLICATION_WORLDMAP` -> AssignedEntitiesWithMetricTile * `RESOURCES` -> AssignedEntitiesWithMetricTile * `THIRD_PARTY_MOST_ACTIVE` -> AssignedEntitiesWithMetricTile * `UEM_CONVERSIONS_PER_GOAL` -> AssignedEntitiesWithMetricTile * `HOST` -> AssignedEntitiesWithMetricTile * `PROCESS_GROUPS_ONE` -> AssignedEntitiesWithMetricTile * `SYNTHETIC_SINGLE_WEBCHECK` -> SyntheticSingleWebcheckTile * `APPLICATION` -> AssignedEntitiesTile * `VIRTUALIZATION` -> AssignedEntitiesTile * `AWS` -> AssignedEntitiesTile * `SERVICE_VERSATILE` -> AssignedEntitiesTile * `SESSION_METRICS` -> AssignedEntitiesTile * `USERS` -> AssignedEntitiesTile * `UEM_KEY_USER_ACTIONS` -> AssignedEntitiesTile * `BOUNCE_RATE` -> AssignedEntitiesTile * `UEM_CONVERSIONS_OVERALL` -> AssignedEntitiesTile * `UEM_JSERRORS_OVERALL` -> AssignedEntitiesTile * `MOBILE_APPLICATION` -> AssignedEntitiesTile * `SYNTHETIC_SINGLE_EXT_TEST` -> AssignedEntitiesTile * `SYNTHETIC_HTTP_MONITOR` -> AssignedEntitiesTile * `DATABASE` -> AssignedEntitiesTile * `CUSTOM_APPLICATION` -> AssignedEntitiesTile * `APPLICATION_METHOD` -> AssignedEntitiesTile * `LOG_ANALYTICS` -> AssignedEntitiesTile * `OPENSTACK` -> AssignedEntitiesTile * `OPENSTACK_PROJECT` -> AssignedEntitiesTile * `OPENSTACK_AV_ZONE` -> AssignedEntitiesTile * `DEVICE_APPLICATION_METHOD` -> AssignedEntitiesTile * `DEM_KEY_USER_ACTION` -> AssignedEntitiesTile * `SLO` -> AssignedEntitiesWithMetricTile * `SCALABLE_LIST` -> ScalableListTile * `HEADER` -> Tile * `OPEN_PROBLEMS` -> ProblemTile * `PURE_MODEL` -> Tile * `DOCKER` -> Tile * `NETWORK_MEDIUM` -> Tile * `APPLICATIONS_MOST_ACTIVE` -> Tile * `NETWORK` -> Tile * `UEM_ACTIVE_SESSIONS` -> Tile * `DCRUM_SERVICES` -> Tile The element can hold these values * `APPLICATION` * `APPLICATIONS` * `APPLICATIONS_MOST_ACTIVE` * `APPLICATION_METHOD` * `APPLICATION_WORLDMAP` * `AWS` * `BOUNCE_RATE` * `CUSTOM_APPLICATION` * `CUSTOM_CHARTING` * `DATABASE` * `DATABASES_OVERVIEW` * `DATA_EXPLORER` * `DCRUM_SERVICES` * `DEM_KEY_USER_ACTION` * `DEVICE_APPLICATION_METHOD` * `DOCKER` * `DTAQL` * `HEADER` * `HOST` * `HOSTS` * `IMAGE` * `LOG_ANALYTICS` * `MARKDOWN` * `MOBILE_APPLICATION` * `NETWORK` * `NETWORK_MEDIUM` * `OPENSTACK` * `OPENSTACK_AV_ZONE` * `OPENSTACK_PROJECT` * `OPEN_PROBLEMS` * `PROCESS_GROUPS_ONE` * `PURE_MODEL` * `RESOURCES` * `SCALABLE_LIST` * `SERVICES` * `SERVICE_VERSATILE` * `SESSION_METRICS` * `SLO` * `SYNTHETIC_HTTP_MONITOR` * `SYNTHETIC_SINGLE_EXT_TEST` * `SYNTHETIC_SINGLE_WEBCHECK` * `SYNTHETIC_TESTS` * `THIRD_PARTY_MOST_ACTIVE` * `UEM_ACTIVE_SESSIONS` * `UEM_CONVERSIONS_OVERALL` * `UEM_CONVERSIONS_PER_GOAL` * `UEM_JSERRORS_OVERALL` * `UEM_KEY_USER_ACTIONS` * `USERS` * `VIRTUALIZATION` |

#### The `TileBounds` object

The position and size of a tile.

| Element | Type | Description |
| --- | --- | --- |
| height | integer | The height of the tile, in pixels. |
| left | integer | The horizontal distance from the top left corner of the dashboard to the top left corner of the tile, in pixels. |
| top | integer | The vertical distance from the top left corner of the dashboard to the top left corner of the tile, in pixels. |
| width | integer | The width of the tile, in pixels. |

#### The `TileFilter` object

A filter applied to a tile.

It overrides dashboard's filter.

| Element | Type | Description |
| --- | --- | --- |
| managementZone | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | The short representation of a Dynatrace entity. |
| timeframe | string | The default timeframe of the tile. |

#### The `EntityShortRepresentation` object

The short representation of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the Dynatrace entity. |
| id | string | The ID of the Dynatrace entity. |
| name | string | The name of the Dynatrace entity. |

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

This type applies to the following tiles:

* User session query (`DTAQL`)

UserSessionQueryTile

Parameters

JSON model

#### The `UserSessionQueryTile` object

Configuration of a User session query tile.

| Element | Type | Description |
| --- | --- | --- |
| customName | string | The name of the tile, set by user. |
| limit | integer | The limit of the results, if not set will use the default value of the system |
| query | string | A [user session queryï»¿](https://dt-url.net/dtusql) executed by the tile. |
| timeFrameShift | string | The comparison timeframe of the query.  If specified, you additionally get the results of the same query with the specified time shift. |
| type | string | The visualization of the tile. The element can hold these values * `COLUMN_CHART` * `FUNNEL` * `LINE_CHART` * `NOT_CONFIGURED` * `PIE_CHART` * `SINGLE_VALUE` * `TABLE` |
| visualizationConfig | [UserSessionQueryTileConfiguration](#openapi-definition-UserSessionQueryTileConfiguration) | Configuration of a User session query visualization tile. |

#### The `UserSessionQueryTileConfiguration` object

Configuration of a User session query visualization tile.

| Element | Type | Description |
| --- | --- | --- |
| hasAxisBucketing | boolean | The axis bucketing when enabled groups similar series in the same virtual axis. |

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

## Related topics

* [Dashboards](/managed/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.")
