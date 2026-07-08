---
title: WMI tutorial - unified analysis
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-05
---

# WMI tutorial - unified analysis

# WMI tutorial - unified analysis

* How-to guide
* 4-min read
* Published Mar 30, 2022

Unified analysis pages are windows into performance analysis and troubleshooting for this newly monitored technology.

They offer the possibility to eliminate further dashboarding or ad-hoc chart building. The `screens` section will define the details to be displayed on each entity's page as well as charts and lists of other related entities for quick drilldowns.

## Unified analysis detailed page

The details page is organized into `staticContent` and a `layout` for dynamic content that comprises `cards` (charts and lists).

`staticContent`

* `showProblems` - Show a panel for any Problems about this entity
* `showProperties` - Show the **Properties and tags** section
* `showTags` - Show the tags applied to this entity
* `showGlobalFilter` - Show the global filtering bar
* `showAddTag` - Show the **Add tag** button

The `layout` consists of different cards defined in the `chartsCards` and `entitiesListCards` subsections.

## Charts card

A chart card is a section of the screen that displays charts. All possible charts are defined in the card, and a number of them can be displayed at the same time on the screen. The others are available from the dropdown list above the chart.

Charts cards rely on [metric selectors](/managed/dynatrace-api/environment-api/metric-v2/metric-selector "Configure the metric selector for the Metric v2 API.") to correctly display metrics.

Simple chart card example:

```
chartsCards:



- key: "host-cpu-metrics"



displayName: "Host CPU"



numberOfVisibleCharts: 2



charts:



- displayName: "Idle CPU"



metrics:



- metricSelector: "custom.demo.host-observability.host.cpu.time.idle:SplitBy()"



- displayName: "User CPU"



metrics:



- metricSelector: "custom.demo.host-observability.host.cpu.time.user:SplitBy()"
```

## Entity list

An entity list is a list of entities that are somehow related to the currently viewed entity. Additional metrics can be charted in the details of each returned entity and will show as a single value in the list view.

Entity lists rely on [entity selectors](/managed/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.") to correctly list related entities.

Simple entity list example:

```
entitiesListCards:



- key: "nic-list"



displayName: "Network Interfaces"



entitySelectorTemplate: "type(wmi:generic_network_device),fromRelationships.runsOn($(entityConditions)),wmi_network_type(Interface)"



displayCharts: false



displayIcons: true



enableDetailsExpandability: true
```

`$(entityConditions)` is a function that automatically maps to the currently viewed entity. This is mandatory for entity selectors used in the extension.

## The properties card

The `propertiesCard` of an entity can also be modified to include additional properties or hide unnecessary ones. Properties are extracted from entity attributes (when type is `ATTRIBUTE`) or through an entity selector (when type is `RELATION`).

## Define unified pages for your extension

1. Add the `screens` section to your `extension.yaml` using the template below.
2. Customize the details page settings for both the Generic Host and the Generic Network Device entity types.
3. Use charts cards to display all the metrics of each entity.
4. Add entity list cards so that a Generic Host can list out all Network Adapters and Interfaces running on it.
5. Add a relation based property so that a Generic Network Device displays what Generic Host it runs on.
6. Package and upload a new version of your extension.
7. Validate your screens are showing up as expected.

```
screens:



- entityType: wmi:generic_host



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



- type: "CHART_GROUP"



key: "wmi_host-chart-metrics"



- type: "ENTITIES_LIST"



key: "wmi_host-list-network_interfaces"



- type: "ENTITIES_LIST"



key: "wmi_host-list-network_adapters"



chartsCards:



- key: "wmi_host-chart-metrics"



displayName: "Generic Host Metrics"



numberOfVisibleCharts: 2



charts:



- displayName: "CPU Usage Breakdown"



visualization:



themeColor: BLUE



seriesType: AREA



metrics:



- metricSelector: "custom.demo.host-observability.host.cpu.time.idle:SplitBy()"



- metricSelector: "custom.demo.host-observability.host.cpu.time.user:SplitBy()"



- metricSelector: "custom.demo.host-observability.host.cpu.time.processor:SplitBy()"



- displayName: "CPU User"



visualization:



themeColor: BLUE



seriesType: LINE



metrics:



- metricSelector: "custom.demo.host-observability.host.cpu.time.user:SplitBy()"



- displayName: "CPU Idle"



visualization:



themeColor: BLUE



seriesType: LINE



metrics:



- metricSelector: "custom.demo.host-observability.host.cpu.time.idle:SplitBy()"



- displayName: "CPU Used"



visualization:



themeColor: BLUE



seriesType: LINE



metrics:



- metricSelector: "custom.demo.host-observability.host.cpu.time.processor:SplitBy()"



entitiesListCards:



- key: "wmi_host-list-network_interfaces"



displayName: "Network Interfaces"



entitySelectorTemplate: "type(wmi:generic_network_device),fromRelationships.runsOn($(entityConditions)),wmi_network_type(Interface)"



pageSize: 5



displayCharts: false



displayIcons: true



enableDetailsExpandability: true



numberOfVisibleCharts: 1



charts:



- displayName: "Traffic"



visualization:



themeColor: BLUE



seriesType: AREA



metrics:



- metricSelector: "custom.demo.host-observability.network.bytes.sent.persec:SplitBy()"



- metricSelector: "custom.demo.host-observability.network.bytes.received.persec:SplitBy()"



- key: "wmi_host-list-network_adapters"



displayName: "Network Adapters"



entitySelectorTemplate: "type(wmi:generic_network_device),fromRelationships.runsOn($(entityConditions)),wmi_network_type(Adapter)"



pageSize: 5



displayCharts: false



displayIcons: true



enableDetailsExpandability: true



numberOfVisibleCharts: 1



charts:



- displayName: "Traffic"



visualization:



themeColor: BLUE



seriesType: AREA



metrics:



- metricSelector: "custom.demo.host-observability.network.bytes.sent.persec:SplitBy()"



- metricSelector: "custom.demo.host-observability.network.bytes.received.persec:SplitBy()"



- entityType: wmi:generic_network_device



propertiesCard:



properties:



- type: ATTRIBUTE



attribute:



key: wmi_network_name



displayName: Name



- type: ATTRIBUTE



attribute:



key: wmi_network_type



displayName: Type



- type: RELATION



relation:



entitySelectorTemplate: type(wmi:generic_host),toRelationships.runsOn($(entityConditions))



displayName: Host



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



- type: "CHART_GROUP"



key: "wmi_network_device-chart-traffic"



chartsCards:



- key: "wmi_network_device-chart-traffic"



displayName: "Traffic"



numberOfVisibleCharts: 2



charts:



- displayName: "Traffic breakdown"



visualization:



themeColor: BLUE



seriesType: AREA



metrics:



- metricSelector: "custom.demo.host-observability.network.bytes.persec:SplitBy()"



- metricSelector: "custom.demo.host-observability.network.bytes.sent.persec:SplitBy()"



- metricSelector: "custom.demo.host-observability.network.bytes.received.persec:SplitBy()"



- displayName: "Bytes sent"



visualization:



themeColor: BLUE



seriesType: LINE



metrics:



- metricSelector: "custom.demo.host-observability.network.bytes.sent.persec:SplitBy()"



- displayName: "Bytes received"



visualization:



themeColor: BLUE



seriesType: LINE



metrics:



- metricSelector: "custom.demo.host-observability.network.bytes.sent.persec:SplitBy()"



- displayName: "Bytes"



visualization:



themeColor: BLUE



seriesType: LINE



metrics:



- metricSelector: "custom.demo.host-observability.network.bytes.sent.persec:SplitBy()"
```

## Results

Your customized unified analysis pages are displayed and populated as expected.

![result](https://dt-cdn.net/images/wmi-tutorial-ua-details-1626-532b22a38b.png)

result