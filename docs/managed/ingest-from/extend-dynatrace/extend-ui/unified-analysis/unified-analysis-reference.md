---
title: Unified analysis reference
source: https://docs.dynatrace.com/managed/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-reference
scraped: 2026-05-12T12:34:47.983946
---

# Unified analysis reference

# Unified analysis reference

* Reference
* 34-min read
* Published May 19, 2022

This is a general description of the unified analysis extension YAML file and ways to create custom visualizations and configure cards, dashboards, and injections.

## Details settings

To customize the details screen, start with the `detailsSettings` and specify the types of information to be included on a unified analysis page. This enables you to customize the page to show all of the data points, charts, and visuals that are most relevant and beneficial to you.

```
detailsSettings:



staticContent:



showProblems: true



showProperties: true



showTags: true



showGlobalFilter: true



showAddTag: true



layout:



autoGenerate: false



cards:



- key: cpu_mem



type: CHART_GROUP



- key: disks



type: ENTITIES_LIST
```

### `staticContent`

Enable or disable static elements like problems, properties, tags, global filter and **Add tag** option.

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| `showProblems` | boolean | If `true`, the details screen shows the problem card. | Required |
| `showProperties` | boolean | If `true`, the details screem shows the properties card. | Required |
| `showTags` | boolean | If `true`, the details screem shows the entity tags. | Required |
| `showFilterBar` | boolean | If `true`, the details screen shows the filter bar. | Required |
| `showAddTag` | boolean | If `true`, the details screen shows the **Add tag** option. | Required |

### `layout`

Reference cards that should be shown on the screen (like chart groups or entity lists) or use the automatically generated screen layout.

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| `autoGenerate` | boolean | If `true`, the screen content is automatically generated. | Required |
| `cards` | enum | Possible values for `type` field: `CHART_GROUP`, `ENTITIES_LIST`, `EVENTS`, `LOGS`, `MESSAGE`, `METRIC_TABLE`, `INJECTIONS`, `BREAK_LINE`, `HEALTH_CARD`, `CARD_GROUP`. | Optional |

## Details injections

The `detailsInjections` field defines injections for the entity details page. This information can be used to better evaluate user experience and also help with root-cause analysis.

Injections must be supported by the screenâthe layout needs to include an injected cards placeholder.

```
detailsInjections:



- type: CHART_GROUP



entitySelectorTemplate: type(custom:host), toRelationship.sameAs($(entityConditions))



key: injectedChartGroups



- type: ENTITIES_LIST



key: injectedList



width: HALF_SIZE



- type: EVENTS



key: injectedEvents



width: FULL_SIZE
```

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| `type` | enum | Defines the type of card available to inject. Possible values: `CHART_GROUP`, `ENTITIES_LIST`, `EVENTS`, `LOGS`, `MESSAGE`, `HEALTH_CARD`, `CARD_GROUP`, `METRIC_TABLE`. | Required |
| `key` | String | The unique key of the card, which is used to reference desired card configuration. | Required |
| `entitySelectorTemplate` | String | [Entity selector](/managed/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.") pointing to related entities. Details It can serve multiple purposesâselecting the entity where the chart will be displayed and filtering them based on certain rules or relating entities. It is used in conjunction with `entityType` to further refine which entities are applicable for the card. For example, if `entityType` is `HOST`, you can use `entitySelectorTemplate` to show the card only for hosts using a certain operating system.  `$entityConditions` acts as a dynamic placeholder, adapting to the context in which the card appears. For example, when the card is displayed on a page dedicated to a specific host, `$entityConditions` will automatically adjust to conditions applicable to that host.  For example, when the card with the following configuration is displayed on the host page.  ```  "entitySelectorTemplate": "type(NETWORK_INTERFACE) AND fromRelationships.isNetworkInterfaceOf($(entityConditions))" ```  The `$(entityConditions)` placeholder will be automatically replaced to point to the specific host entity.  ```  "entitySelectorTemplate": "type(NETWORK_INTERFACE) AND fromRelationships.isNetworkInterfaceOf(type(HOST) AND entityId(HOST-<id>))" ``` | Optional |
| `width` | enum | A value that determines how much vertical space the card is taking. Possible values: `HALF_SIZE`, `FULL_SIZE`. | Optional |

## Details filters

The `detailsFilter` field defines filters for the entity details screen. It enables you to customize the page to show only the data you want to see. It automatically displays metric dimension filters if there are any dimension splits on the screen (chart or metric table). To display only metric dimension filters, define it as empty (`detailsFilters: {}`).

```
detailsFilters:



relationships:



- type(HOST_GROUP), toRelationship.isInstanceOf($(entityConditions))



- type(AZURE_REGION), fromRelationship.isSiteOf($(entityConditions))



entityFilters:



- displayName: filters



filters:



- type: entityName



displayName: name



freeText: false



modifier: contains



defaultSearch: true



distinct: false



entityTypes:



- my:interface
```

### `relationships`

You can enable filtering by configuring the relationship between screen entity type and related entity type. For example, filter process list by host name:

```
relationships:



- type(HOST) AND toRelationship.isProcessOf($(entityConditions))
```

You can also configure the filtering on multiple levels. For example, filter the processes by host group name:

```
relationships:



- type(HOST) AND toRelationship.isProcessOf($(entityConditions))



- type(HOST) AND fromRelationship.isInstanceOf(type(HOST_GROUP))
```

### `entityFilters`

The block that defines the groups of filters (these are displayed slightly grayed out in the filtering list).

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| `filters` | Array | The actual filters that are part of this group. | Required |
| `type` | String | Must reference an attribute of the entity you are filtering. Note: every entity has `entityName` as a default attribute. | Required |
| `displayName` | String | How this filter is labelled within the web UI. | Required |
| `freeText` | boolean | If `true`, the user can freely type text; otherwise, they must select from a list of suggestions. Note: only default attributes such as `entityName` are capable of offering list of suggestions. | Required |
| `modifier` | boolean | When `freeText` is true, this defines how the text should be matched against the attribute. When `freeText` is false, this must be omitted. Note: All non-default attributes must match as `equals` regardless of this option. | Optional |
| `defaultSearch` | boolean | If `true`, if the user starts typing without selecting a filter first, this filter is selected by default. Only one filter within the `filtering` block may have this enabled. | Optional |
| `distinct` | boolean | If `true`, only one instance of this filter can be applied. | Required |
| `entityTypes` | Array | A mandatory list of entity types that this filter applies to. If you omit this, your filtering bar just shows a spinning wheel because of the incomplete definition. | Optional |

## List settings

The `listSettings` section enables you to customize the list view of the unified analysis page. You can change the selection and order of columns, how the list is sorted, and the number of rows to display.

```
listSettings:



staticContent:



showGlobalFilter: true



header:



title: My hosts



description: My hosts list



icon: host



layout:



autoGenerate: false



cards:



- type: CHART_GROUP



key: chart



- type: ENTITIES_LIST



key: entitiesList



- type: INJECTIONS
```

### `staticContent` Required

Enable or disable static elements like problems, properties, tags, global filter, and the **Add tag** option.

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| `showProblems` | boolean | If `true`, the details screen shows the problem card. | Optional |
| `showProperties` | boolean | If `true`, the details screem shows the properties card. | Optional |
| `showTags` | boolean | If `true`, the details screem shows the entity tags. | Optional |
| `showGlobalFilter` | boolean | If `true`, the details screen shows the filter bar. | Required |
| `showAddTag` | boolean | If `true`, the details screen shows the **Add tag** option. | Optional |
| `header` | Object | The definition of the page header. | Optional |
| `breadcrumbs` | Array | A list of breadcrumbs leading to the page. | Optional |
| `hideDefaultBreadcrumb` | boolean | If `true`, the default breadcrumb for the current page is hidden. | Optional |

### `layout` Required

Reference cards that should be shown on the screen (like chart groups or entity lists) or use the automatically generated screen layout.

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| `autoGenerate` | boolean | If `true`, the screen content is automatically generated. | Required |
| `cards` | enum | Possible values for `type` field: `CHART_GROUP`, `ENTITIES_LIST`, `MESSAGE`, `INJECTIONS`, `BREAK_LINE`. | Optional |

## List injections

The `listInjections` field defines injections for entity details screen. Injections must be supported by the screenâthe layout needs to include an injected cards placeholder.

```
listInjections:



- type: CHART_GROUP



key: injectedChartGroups



- type: ENTITIES_LIST



key: injectedList



width: HALF_SIZE
```

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| `type` | enum | Defines the type of card available to inject. Possible values: `CHART_GROUP`, `ENTITIES_LIST`, `MESSAGE`, `METRIC_TABLE`. | Required |
| `key` | String | The unique key of the card, which is used to reference desired card configuration. | Required |

## List filters

The `listFilters` field defines filters on the list page.

```
listFilters:



relationships:



- type(HOST_GROUP), toRelationship.isInstanceOf($(entityConditions))



- type(AZURE_REGION), fromRelationship.isSiteOf($(entityConditions))



entityFilters:



- displayName: filters



filters:



- type: entityName



entityTypes:



- HOST_GROUP



- AZURE_REGION



freeText: false



displayName: name



distinct: true
```

### `relationships`

You can enable filtering by configuring the relationship between screen entity type and related entity type. For example, filter process list by host name:

```
relationships:



- type(HOST) AND toRelationship.isProcessOf($(entityConditions))
```

You can also configure the filtering on multiple levels. For example, filter the processes by host group name:

```
relationships:



- type(HOST) AND toRelationship.isProcessOf($(entityConditions))



- type(HOST) AND fromRelationship.isInstanceOf(type(HOST_GROUP))
```

### `entityFilters`

The list of entity filters. For generic entities, the only filter types with suggestions are `entityName`, `tag`, `healthState`, and `ipAddress` / `dt.ip_addresses`. Any custom attributes must be set to `freeText: true` with `modifier: equals`. There are no suggestions supported, so you must type the exact value to filter.

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| `filters` | Array | The actual filters that are part of this group. | Required |
| `type` | String | Must reference an attribute of the entity you are filtering. Note: every entity has `entityName` as a default attribute. | Required |
| `displayName` | String | How this filter is labelled within the web UI. | Required |
| `freeText` | boolean | If `true`, the user can freely type text; otherwise, they must select from a list of suggestions. Note: only default attributes such as `entityName` are capable of offering list of suggestions. | Required |
| `modifier` | boolean | When `freeText` is true, this defines how the text should be matched against the attribute. When `freeText` is false, this must be omitted. Note: All non-default attributes must match as `equals` regardless of this option. | Optional |
| `defaultSearch` | boolean | If `true`, if the user starts typing without selecting a filter first, this filter is selected by default. Only one filter within the `filtering` block may have this enabled. | Optional |
| `distinct` | boolean | If `true`, only one instance of this filter can be applied. | Required |
| `entityTypes` | Array | A mandatory list of entity types that this filter applies to. If you omit this, your filtering bar just shows a spinning wheel because of the incomplete definition. | Optional |

## Properties card

The `propertiesCard` field displays the entity properties that are shown on the card as key-value pairs. By default, all available attribute properties are displayed.

```
propertiesCard:



properties:



- type: RELATION



relation:



entitySelectorTemplate: NOT VALIDATED IN SCHEMA



displayName: default



- type: ATTRIBUTE



attribute:



key: attribute



displayName: Attribute
```

### `properties` Required

Use this configuration to specify the properties card.

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| `type` | enum | Defines the type of property. Possible values: `RELATION`, `ATTRIBUTE`. | Optional |

### `RELATION`

Enables you to specify the relation to the specific entity.

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| `entitySelectorTemplate` | String | An [entity selector](/managed/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.") that is used to retrieve the selected entities. Details It can serve multiple purposesâselecting the entity where the chart will be displayed and filtering them based on certain rules or relating entities. It is used in conjunction with `entityType` to further refine which entities are applicable for the card. For example, if `entityType` is `HOST`, you can use `entitySelectorTemplate` to show the card only for hosts using a certain operating system.  `$entityConditions` acts as a dynamic placeholder, adapting to the context in which the card appears. For example, when the card is displayed on a page dedicated to a specific host, `$entityConditions` will automatically adjust to conditions applicable to that host.  For example, when the card with the following configuration is displayed on the host page.  ```  "entitySelectorTemplate": "type(NETWORK_INTERFACE) AND fromRelationships.isNetworkInterfaceOf($(entityConditions))" ```  The `$(entityConditions)` placeholder will be automatically replaced to point to the specific host entity.  ```  "entitySelectorTemplate": "type(NETWORK_INTERFACE) AND fromRelationships.isNetworkInterfaceOf(type(HOST) AND entityId(HOST-<id>))" ``` | Required |
| `displayName` | String | The name of the relation. | Required |
| `fallbackMessage` | String | Displays additional message if no entity is found. By default, the whole property is hidden. | Optional |

### `ATTRIBUTE`

Enables you to overwrite attribute display options.

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| `key` | String | Used to reference the desired attribute. | Required |
| `displayName` | String | The name of the attribute. | Optional |

## Chart group cards

The chart group cards enable you to visualize the specified metrics in dedicated charts.

* The `metricSelector` expression specifies the metrics your chart is based on. For more information, see [Metrics API - Metric selector](/managed/dynatrace-api/environment-api/metric-v2/metric-selector "Configure the metric selector for the Metric v2 API."). The examples below use simple metric selector expressions referring directly to the metric keys.

```
chartsCards:



- key: chartGroup



conditions:



- NOT VALIDATED IN SCHEMA



numberOfVisibleCharts: 2



charts:



- displayName: Chart



conditions:



- NOT VALIDATED IN SCHEMA



visualizationType: GRAPH_CHART



graphChartConfig:



visualization:



themeColor: DEFAULT



seriesType: LINE



metrics:



- metricSelector: NOT VALIDATED IN SCHEMA



- metricSelector: builtin:host.cpu.usage:avg



visualization:



themeColor: DEFAULT



seriesType: LINE



- displayName: Chart2



visualizationType: PIE_CHART



pieChartConfig:



metric:



metricSelector: NOT VALIDATED IN SCHEMA



defaultAggregation: AVG



showLegend: true



themeColor: ORANGE



- displayName: Chart3



visualizationType: SINGLE_VALUE



singleValueConfig:



metric:



metricSelector: NOT VALIDATED IN SCHEMA



displayName: Single value



defaultAggregation: COUNT



showSparkline: true



showTrend: true
```

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| `key` | String | The unique key of the card, which is used to reference desired card configuration | Required |
| [`conditions`](#conditions) | Array | Defines the conditions that need to be fulfilled for the chart group card to be visible. | Optional |
| `numberOfVisibleCharts` | Integer | The number of charts that are visible on the unified analysis page. | Required |
| `mode` | enum | Defines the chart group behavior and interactivity. Possile values: `NORMAL`, `STATIC`.[1](#fn-1-1-def) | Required |

1

`NORMAL` mode enables you to interact with the charts (view different data points or zoom in/out). Charts with `STATIC` mode are presented in a fixed, restricted manner.

### `charts`

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| `displayName` | String | The title of the card. | Required |
| [`conditions`](#conditions) | Array | Defines the conditions that need to be fulfilled for the chart group card to be visible. | Optional |

### `visualizationType`

The `visualizationType` defines the type for your chart: a graph chart `GRAPH_CHART`, a pie chart `PIE_CHART`, or a single value `SINGLE_VALUE`. If you don't specify the visualization type, the graph chart is rendered by default.

#### `GRAPH_CHART`

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| `visualization` | enum | Enables you to define a theme color, and series type (`COLUMN`, `LINE` or `AREA`). You can also enable showing the axis legend by setting the `showLegend` flag to `true`. | Required |
| `metrics` | Array | Defines how to retrieve data for a single line in the chart. | Required |
| `thresholds` | Array | Defines thresholds after which the background of the chart will change the color to the selected one. | Optional |

##### `metricSelector`

A metric selector expression for a dedicated metric line.

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| `visualization` | enum | Enables you to define a theme color, and series type (`COLUMN`, `LINE` or `AREA`). You can also enable showing the axis legend by setting the `showLegend` flag to `true`. | Optional |

#### `PIE_CHART`

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| `metric` | Object | Defines how to retrieve data for the pie chart. | Required |
| `defaultAggregation` | enum | Defines default aggregation of the chart timeseries. If not defined or selected one is not supported, it is deduced from metrics metadata. | Optional |

#### `SINGLE_VALUE`

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| `metric` | Object | Defines how to retrieve data for the single chart. | Required |
| `displayName` | String | Defines the name of the value. | Optional |
| `defaultAggregation` | enum | Defines default aggregation of the chart timeseries. If not defined or selected one is not supported, it is deduced from metrics metadata. | Optional |
| `showSparkline` | boolean | If `true`, the sparkline is visible. | Optional |
| `showTrend` | boolean | If `true`, the trend is visible. | Optional |
| `thresholds` | Array | Defines thresholds after which the background of the chart will change the color to the selected one. | Optional |
| `foldTransformation` | enum | Defines transformation method, which folds data into single value. Possible values: `AUTO`, `LAST_VALUE`, `MAX`, `MIN`, `SUM`, `MEDIAN`, `VALUE`, `PERCENTILE_10`, `PERCENTILE_75`, `PERCENTILE_90`. | Optional |

### List of available conditions

```
ConditionName|param1key=param1value|param2key=param2value
```

| Condition | Parameters | Minimum schema version | Description |
| --- | --- | --- | --- |
| `demo` | Not applicable | 224 | Used to demonstrate the conditions feature. |
| `isSaaS` | Not applicable | 233 | Indicates if the server deployment type is SaaS. |
| `featureFlag` | Feature flag key | 233 | Validates the status of a specific feature flag. |
| `entityAttribute` | Dynamic parameters[1](#fn-2-1-def) | 231 | Checks if the screen's monitored entity possesses certain attributes with specified values or if they exist with any value. |
| `relatedEntity` | `entitySelectorTemplate` | 230 | Validates the existence of a specified related entity in the environment. |
| `extensionConfigured` | `extensionId`, `aboveOrEqualVersion`, `belowOrEqualVersion`, `featureSets`, `activatedOnHost`[2](#fn-2-2-def) | 243 | Validates the presence of a specified extension in the environment, considering other parameters. |
| `uiPermission` | Specified UI permision | 243 | Confirms if you possess a specified permission (for example, `CONFIG_WRITE`). |
| `isActive` | Not applicable | 246 | Determines if the screen's monitored entity is active. |
| `serviceType` | Type of the service | 246 | Confirms the type of the service. The scope limited to `METype.SERVICE` details screens. |
| `typeExists` | Type of the service | 248 | Checks if a specified `METype` service is present in the environment. |
| `platform` | Not applicable | 254 | Checks 3rd generation compatibility. |
| `metricAvailable` | `metric`[3](#fn-2-3-def), `lastWrittenWithinDays`[4](#fn-2-4-def) | 256 | Verifies if a given metric key has associated metadata and the last time it was updated. |

1

When parameters are provided with a specific value, they are formatted as `key=value`. The system will verify the exact match of this `key-value` pair. If only the key is provided without any accompanying value, the system will simply check if that key is present using the `.exists()` method.

2

The extension is configured to operate on the current host.

3

Metric key

4

The specified number of days within which the system checks the most recent updates.

## Entities list cards

The entities list card displays other entities that are related to the focused entity. The YAML file below lists all Synology disks mapped to an instance of DiskStation Manager on which the details screen focuses.

* The `entitySelectorTemplate` expression specifies the entities to list on the card. For more information, see [Environment API v2 - Entity selector](/managed/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.").
* The expression `type(syn:disk),fromRelationships.runsOn($(entityConditions))` lists the entities of type `syn:disk` that have a relationship of `from` direction and `runsOn` type to the `syn:diskmanager` represented via the `$(entityConditions)` placeholder that stands for a focused entity.

```
entitiesListCards:



- key: disks



displayName: Synology disks



pageSize: 10



displayCharts: false



entitySelectorTemplate: "type(syn:disk),fromRelationships.runsOn($(entityConditions))"



displayIcons: true



enableDetailsExpandability: true



numberOfVisibleCharts: 2



columns:



- type: ATTRIBUTE



attribute:



key: some_attribute



displayName: Some attribute



- type: RELATION



relation:



entitySelectorTemplate: type("syn:partition"),fromRelationship.isChildOf($(entityConditions))



displayName: Partitions



displayAmount: false



fallbackMessage: "no partition"



filtering:



relationships:



- type(syn:partition), fromRelationship.isChildOf($(entityConditions))



entityFilters:



- displayName: filters



filters:



- type: entityName



displayName: name



freeText: true



modifier: contains



defaultSearch: true



distinct: false



entityTypes:



- my:interface



- type: entityName



displayName: Partition name



freeText: true



modifier: contains



defaultSearch: false



distinct: false



entityTypes:



- syn:partition
```

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| `key` | String | The unique key of the card, which is used to reference desired card configuration. | Required |
| `displayName` | String | The card title. | Optional |
| `pageSize` | Integer | The number of rows visible on a single page. | Required |
| `displayCharts` | boolean | If `true`, charts with aggregated data appears above table. | Required |
| `entitySelectorTemplate` | String | The [entity selector](/managed/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.") is used to find entities that are to be displayed on the list. Details It can serve multiple purposesâselecting the entity where the chart will be displayed and filtering them based on certain rules or relating entities. It is used in conjunction with `entityType` to further refine which entities are applicable for the card. For example, if `entityType` is `HOST`, you can use `entitySelectorTemplate` to show the card only for hosts using a certain operating system.  `$entityConditions` acts as a dynamic placeholder, adapting to the context in which the card appears. For example, when the card is displayed on a page dedicated to a specific host, `$entityConditions` will automatically adjust to conditions applicable to that host.  For example, when the card with the following configuration is displayed on the host page.  ```  "entitySelectorTemplate": "type(NETWORK_INTERFACE) AND fromRelationships.isNetworkInterfaceOf($(entityConditions))" ```  The `$(entityConditions)` placeholder will be automatically replaced to point to the specific host entity.  ```  "entitySelectorTemplate": "type(NETWORK_INTERFACE) AND fromRelationships.isNetworkInterfaceOf(type(HOST) AND entityId(HOST-<id>))" ``` | Optional |
| `displayIcons` | boolean | If `true`, the `name` column displays the icon of the entity. | Required |
| `enableDetailsExpandability` | boolean | If `true`, rows can be expanded with charts related to that row dimension values. | Required |
| `numberOfVisibleCharts` | Integer | The number of charts that are visible on the unified analysis page. | Required |
| `displayProblemImpactWidget` | boolean | If `true`, a widget indicating that some entities are not healthy will be displayed above the list. Make sure there is visible filtering with the health state filter. | Optional |
| `columns` | Object | Additional attribute or relation columns. | Optional |
| `filtering` | Object | The filtering inside the entity list card. It affects only that card's table and chart group. | Optional |

### `columns`

Additional columns that are displayed between Name and chart columns. There are 2 types available: ATTRIBUTE and RELATION.

#### `RELATION`

Enables you to specify the relation to the entity (1:1 relation) or list of entities (1:n relation).

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| `entitySelectorTemplate` | String | An [entity selector](/managed/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.") that is used to retrieve the selected entities. Details It can serve multiple purposesâselecting the entity where the chart will be displayed and filtering them based on certain rules or relating entities. It is used in conjunction with `entityType` to further refine which entities are applicable for the card. For example, if `entityType` is `HOST`, you can use `entitySelectorTemplate` to show the card only for hosts using a certain operating system.  `$entityConditions` acts as a dynamic placeholder, adapting to the context in which the card appears. For example, when the card is displayed on a page dedicated to a specific host, `$entityConditions` will automatically adjust to conditions applicable to that host.  For example, when the card with the following configuration is displayed on the host page.  ```  "entitySelectorTemplate": "type(NETWORK_INTERFACE) AND fromRelationships.isNetworkInterfaceOf($(entityConditions))" ```  The `$(entityConditions)` placeholder will be automatically replaced to point to the specific host entity.  ```  "entitySelectorTemplate": "type(NETWORK_INTERFACE) AND fromRelationships.isNetworkInterfaceOf(type(HOST) AND entityId(HOST-<id>))" ``` | Required |
| `displayName` | String | The name of the column. | Required |
| `displayAmount` | String | If `false`, entities are displayed as a list (up to 20 entities). If `true`, the number of related entities is displayed as a link to the list screen. The linked list is prefiltered only if it has configured `listFilters` with appropriate relationship and `entityName` filter (`freeText: true` and `modifier: contains`). | Required |
| `fallbackMessage` | String | Displays additional message if no entity is found. | Optional |

#### `ATTRIBUTE`

Enables you to specify custom attribute column.

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| `key` | String | Used to reference the desired attribute. | Required |
| `displayName` | String | The name of the attribute. | Required |

## Events cards

The events cards display the events related to specified entities.

```
eventsCards:



- key: events



displayName: Events



entitySelectorTemplates:



- "$(entityConditions)",



- "type(CONTAINER_GROUP_INSTANCE),fromRelationships.isInstanceOf($(entityConditions))",



- "type(PROCESS_GROUP_INSTANCE),fromRelationships.isPgiOfCgi(type(CONTAINER_GROUP_INSTANCE),fromRelationships.isInstanceOf($(entityConditions)))"



showFiltering: true



showPagination: true



pageSize: 10
```

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| `key` | String | The unique key of the card, which is used to reference desired card configuration. | Required |
| `displayName` | String | The card title. If not set, card are named `Events`. | Optional |
| `entitySelectorTemplates` | Array | The list of entity selector templates. It defines where the events are gathered from. If empty, the events are gathered for current entity. | Optional |
| `showFiltering` | boolean | If `true`, the filtering bar displays above events chart. | Required |
| `showPagination` | boolean | If `true`, the **Show more** action is available under events list. | Required |
| `pageSize` | Integer | The number of rows visible at card load. | Required |
| `description` | String | The description of the card. | Optional |
| `eventSelectorTemplate` | String | An event selector that is used to fetch events for related entities. | Optional |
| `displayChart` | boolean | Show or hide the chart in the card. | Optional |

## Logs cards

The `logsCards` field specifies the behavior of the logs card and has the same functionality as [Log viewer](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer#search "Learn how to use Dynatrace log viewer to analyze log data."). It consists of a bar chart representing different log occurrences during selected timeframe and detailed table where each log is an entry with additional properties like: timestamp, status, content.

```
logsCards:



- key: logs



displayName: Logs



enablePaging: true



filterQuery: event.type!="k8s" AND ($(logEntityAttributeKey) inEntitySelector "$(entityConditions)" OR dt.entity.container_group_instance inEntitySelector "type(CONTAINER_GROUP_INSTANCE),fromRelationships.isInstanceOf($(entityConditions))" OR dt.entity.process_group_instance inEntitySelector "type(PROCESS_GROUP_INSTANCE),fromRelationships.isPgiOfCgi(type(CONTAINER_GROUP_INSTANCE),fromRelationships.isInstanceOf($(entityConditions)))")



showFiltering: true



pageSize: 10
```

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| `key` | String | The unique key of the card, which is used to reference desired card configuration. | Required |
| `displayName` | String | The card title. | Optional |
| `enablePaging` | boolean | If `true`, enables paging of the log results in the table. | Optional |
| `filterQuery` | String | The predefined filtering for the log table. It is possible to to use LQL syntax also to more complex cases that include entity selectors with unified analysis placeholders in format: `expression {attribute} inEntitySelector "{entitySelector}"` to display logs of related entities. For example, `dt.entity.host inEntitySelector "type(PROCESS_GROUP_INSTANCE) AND fromRelationship.isProcessOf($(entityConditions))"`. | Optional |
| `showFiltering` | boolean | Controls the visibility of the filter bar. | Optional |
| `pageSize` | Integer | The number of rows visible on a single page. | Optional |
| `description` | String | The description of the card. | Optional |
| `displayChart` | boolean | Show or hide the chart in the card. | Optional |

## Message cards

The `messageCards` field specifies the behavior of the message card, like visualization options, theme, or text.

```
messageCards:



- key: message-card



type: CARD



card:



text: internal text



theme: MAIN



displayName: Message Card



- key: message-card2



type: MESSAGE



message:



text: internal text



theme: INFO
```

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| `key` | String | The unique key of the card, which is used to reference desired card configuration. | Required |
| `type` | enum | Defines the type of your message card. The possible values are: `CARD`, `MESSAGE`. | Required |

### `CARD`

Displays the message in the card format with title, description and buttons.

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| `text` | String | Defines the description of the card. | Required |
| `theme` | enum | Defines the color theme of the card. The possible values are: `WARNING`, `MAIN`, `CTA`. | Required |
| `displayName` | String | Defines the title of the card. | Optional |

### `MESSAGE`

Displays the message in the card format with description only.

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| `text` | String | Defines the description of the card. | Required |
| `theme` | enum | Defines the color theme of the message. The possible values are: `INFO`, `WARNING`, `ERROR`. | Required |

## Problems card

The `problemsCard` field specifies the behavior of the problems card.

```
problemsCard:



entitySelectorTemplates:



- NOT VALIDATED IN SCHEMA



- NOT VALIDATED IN SCHEMA1



- NOT VALIDATED IN SCHEMA2
```

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| `entitySelectorTemplates` | Array | Up to 10 entity selectors, used to fetch data for related entities. | Optional |

## Actions

The `actions` field defines actions that are available from the menu.

```
actions:



- actionScope: GLOBAL_DETAILS



actions:



- actionExpression: actionName|key1=value1



- actionScope: CHART_GROUP



key: chart



actionLocation: CHART



actions:



- actionExpression: actionName|key1=value1



- actionScope: ENTITIES_LIST



key: entitiesList



actionLocation: TABLE_ENTRY



actions:



- actionExpression: actionName|key1=value1
```

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| `actionScope` | enum | The defined action appears in the settings of the chosen card type. Possible values: `GLOBAL_DETAILS`, `GLOBAL_LIST`, `PROPERTIES`, `PROBLEMS`, `CHART_GROUP`, `ENTITIES_LIST`, `EVENTS`, `LOGS`, `METRIC_TABLE`. | Required |
| `key` | String | You can set the `key` if you want the action to be available only in one specific card. To add this actions in every card of this type, leave it empty. | Required |
| [`actionExpression`](#action-expression) | String | Defines the action expression. | Required |
| `actionLocation` | enum | Defines the location of your created action. Possible values: `HEADER`, `CHART`, `TABLE_ENTRY`. | Optional |

### List of available actions

```
ActionName|param1key=param1value|param2key=param2value
```

#### Generic actions

| Action | Parameters | Minimum schema version | Description |
| --- | --- | --- | --- |
| `configuration` | Not applicable | 221 | Creates a link to the entity configuration page. For example, host settings. |
| `relatedEntityConfiguration` | `entitySelectorTemplate`, `name` | 234 | Creates a link to the entity configuration page. For example, PGI settings from the host page. |
| `settings` | `name`, `scopeClass`[1](#fn-3-1-def), `scopeIdentifier`[2](#fn-3-2-def), `schemaId`[3](#fn-3-3-def) | 236 | Creates a link to the specified Settings 2.0 topic configuration UI. |
| `hubCapability` | `text`[4](#fn-3-4-def), `hubCapability`[5](#fn-3-5-def) | 243 | Creates a link to the specified Dynatrace Hub capability. |
| `hubExtension` | `text`[4](#fn-3-4-def), `extensionId`[6](#fn-3-6-def) | 243 | Creates a link to the specified Extension in Dynatrace Hub. |
| `relatedEntityScreen` | `entitySelectorTemplate`, `name` | 253 | Creates a link to the related entity unified analysis page. |
| `platform.intent` | `json`[7](#fn-3-7-def), `label`, `appId`, `intentId` | 254 | Platform intent action. |
| `smartscape` | Not applicable | 255 | Redirects to smartscape. |

1

Settings scope class

2

Settings scope identifier

3

Settings schema ID

4

Action display name

5

Hub capability URL part

6

Extension ID used as URL part

7

Entire intent JSON

#### Core actions

| Action | Parameters | Valid for condition | Minimum schema version | Description |
| --- | --- | --- | --- | --- |
| `core.editConfig` | Not applicable | `UAScreenFeatureFlags.ENABLE_CONFIG_BUTTONS` | 218 | Redirects to the entity's settings page and creates links for all its subtypes. |
| `core.shareScreenUrl` | Not applicable | Whole screen scope | 218 | Provides a link for sharing feedback. |
| `core.share.feedback` | Not applicable | Whole screen scope | 218 | Opens a feedback sharing form. |
| `core.dataExplorer` | Not applicable | Chart element type | 223 | Redirects charts to Data Explorer. |
| `core.alerting` | Not applicable | `CONFIG_WRITE` permissions, Chart element type | 224 | Redirects charts to set alerts on the selected metric. |
| `core.pinToDashboard` | Not applicable | Chart or Whole Services screen scope with `UAScreenFeatureFlags.ENABLE_PIN_TO_DASHBOARD` | 224 | Pins charts or entire services to the dashboard. |
| `core.problems` | Not applicable | - | 224 | Navigates to the **Problems** section. |
| `core.screenType` | Not applicable | `UAScreenFeatureFlags.ENABLE_CONFIG_BUTTONS` | 224 | Creates multiple predefined screen type actions. |
| `core.singleCard` | Not applicable | `UAScreenFeatureFlags.ENABLE_SINGLE_CARD_BUTTONS` | 232 | Displays a single card view. |
| `core.logs.createMetric` | Not applicable | Log card element type | 233 | Redirects to log settings to create a log metric. |
| `core.opt.out` | Not applicable | Whole screen scope | 235 | Navigates to the classic page view. |
| `core.useLocalConfig` | Not applicable | `UAScreenFeatureFlags.ENABLE_USE_LOCAL_CONFIG_BUTTON` | 236 | Activates the Local Config Mode. |
| `core.sidebar` | `screenTypeExpression`[1](#fn-4-1-def) | `UAScreenFeatureFlags.ENABLE_SIDE_BAR_BUTTONS` | 244 | Opens the sidebar. |
| `core.problems.details` | `pid`[2](#fn-4-2-def) | Details screen | 243 | Navigates to specific problem details. |
| `core.logs.filtered` | Not applicable | Log card element type | 246 | Redirects log cards to the **Log Viewer**. |
| `core.slos.create` | Not applicable | `CONFIG_WRITE` permissions, Slo List element type | 255 | Redirects charts to create a Service Level Objective (SLO). |

1

Screen type expression to be rendered in the sidebar

2

Problem ID

## Metric table cards

Metric table is a graphical representation of the metrics data related to the same dimension set.

```
metricTableCards:



- key: metricTable



pageSize: 5



displayCharts: true



enableDetailsExpandability: true



numberOfVisibleCharts: 2



filtering: {}



charts:



- displayName: Chart



conditions:



- NOT VALIDATED IN SCHEMA



visualizationType: GRAPH_CHART



graphChartConfig:



visualization:



themeColor: DEFAULT



seriesType: LINE



metrics:



- metricSelector: NOT VALIDATED IN SCHEMA



- metricSelector: builtin:process.cpu:splitBy("process.pid","process.parent_pid","process.executable.name","process.executable.path","process.command_line","process.owner", "dt.entity.process_group_instance")



visualization:



themeColor: DEFAULT



seriesType: LINE



conditions:



- NOT VALIDATED IN SCHEMA
```

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| `key` | String | The unique key of the card, which is used to reference desired card configuration. | Required |
| `pageSize` | Integer | The number of rows visible on a single page. | Required |
| `displayCharts` | boolean | If `true`, charts with aggregated data appears above the table. | Required |
| `enableDetailsExpandability` | boolean | If `true`, rows can be expanded with charts related to that row dimension values. | Required |
| `numberOfVisibleCharts` | Integer | Number of visible charts. | Required |
| `charts` | Object | Define the charts to display timeseries data in the table. Table columns are based on the dimensions from the metrics results of those charts. Make sure the metrics of all charts have the same dimensions in a result. | Optional |
| `conditions` | Array | Conditions for displaying the chart. | Optional |
| `filtering` | Object | The filtering inside the metric table card. It affects only that cards table and chart group. It automatically displays metric dimension filters if there are any dimension splits. To display only metric dimension filters, define it as empty (`detailsFilters: {}`). | Optional |

## Health cards

Health cards provide a visual representation of specific metrics within the Dynatrace UI. Each card can be tailored to display up to six distinct tiles, each representing a unique metric or data point.

Health tile can be used as navigation button to specify element on the page that will give more details about that metric.

```
healthCards:



- key: health_card



tiles:



- displayName: Uptime



metricSelector: builtin:host.uptime



displayMetricValue: 'true'



foldTransformation: LAST_VALUE



- displayName: CPU



metricSelector: builtin:host.cpu.usage:avg



displayMetricValue: 'true'



foldTransformation: LAST_VALUE



anchor:



cardName: Host performance



chartName: CPU usage



- displayName: Available memory



metricSelector: builtin:host.mem.avail.pct



displayMetricValue: 'true'



foldTransformation: LAST_VALUE



anchor:



cardName: Host performance



chartName: Memory usage



- displayName: Network



metricSelector: (builtin:host.net.nic.trafficIn:merge("dt.entity.network_interface"):avg)+(builtin:host.net.nic.trafficOut:merge("dt.entity.network_interface"):avg)



additionalMetricSelectors:



collection:



- builtin:host.net.nic.trafficIn:merge("dt.entity.network_interface")



- builtin:host.net.nic.trafficOut:merge("dt.entity.network_interface")



displayMetricValue: 'true'



foldTransformation: LAST_VALUE



anchor:



cardName: Host performance



chartName: Traffic
```

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| `key` | String | Unique key, which is used to map to this health card in the screen layout config. | Required |
| `tiles` | Array | Collection of tile definitions in the health card. Each tile can display a specific metric. A health card can have up to 6 tiles. | Optional |

### `tiles`

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| `displayName` | String | The name of the health card tile. | Required |
| `metricSelector` | String | Used to relate problems and specify the metric displayed on the tile. | Required |
| `additionalMetricSelectors` | Array | Used to relate problems. Hidden in the UI. | Optional |
| `displayMetricValue` | boolean | Determines whether the metric value should be displayed on the tile. | Optional |
| `foldTransformation` | Enum | Defines transformation method, which folds data into single value. Possible values: `AUTO`, `LAST_VALUE`, `MAX`, `MIN`, `SUM`, `MEDIAN`, `VALUE`, `PERCENTILE_10`, `PERCENTILE_75`, `PERCENTILE_90`. | Required |
| `anchor` | Object | Defines an element to redirect to when the tile is selected. This can be a specific card or chart name. | Optional |