---
title: How dashboards scope and refresh data
source: https://docs.dynatrace.com/managed/analyze-explore-automate/dashboards/how-dashboards-scope-and-refresh-data
---

# How dashboards scope and refresh data

# How dashboards scope and refresh data

* Explanation
* 4-min read
* Updated on Oct 05, 2026

Every dashboard tile shows data for a timeframe and a management zone, optionally narrowed by dynamic filters, and refreshes on a schedule that depends on its timeframe. Knowing which setting wins helps you read a dashboard correctly and share it with the view you intend.

## Global timeframe and management zone

The global selectors for timeframe and management zone are available across all pages and views, in the upper-right corner. For the selector controls and the timeframe expressions they accept, see [Timeframe selector](/managed/discover-dynatrace/get-started/dynatrace-ui/ui-timeframe-selector "Learn how the timeframe selector works in Dynatrace Managed, including presets, absolute time, relative time, rounded time, and regional format settings.").

Timeframe and management zone selections are sticky: they carry over to every page you visit. For example, after you change the timeframe and management zone on a dashboard, the selections stay in place as you drill down from the **Applications** tile to individual application pages. The timeframe selector remembers up to 10 recently used timeframes.

Opening a new dashboard resets the timeframe and management zone to the dashboard's [defaults](#default). So does returning to the current dashboard by selecting **Dashboard** in the upper-left corner of the page.

## Dashboard defaults and tile overrides

Each dashboard can have a default timeframe and a default management zone. These override the global selection, and Dynatrace applies them every time you open the dashboard. The defaults also apply when you [share](/managed/analyze-explore-automate/dashboards/share-a-dashboard "Share a dashboard with specific users, groups, anyone with the link, or anonymous viewers, and subscribe people to weekly or monthly email reports.") the dashboard. An anonymous access link carries the dashboard's default timeframe and management zone. When the dashboard has no defaults, the link uses a timeframe of **last 2 hours** and the **All** management zone.

Each tile can also have its own timeframe and management zone, which override the dashboard's settings. A tile with its own setting shows a filter in its upper-right corner, and you can hover over it to see the setting.

The order of precedence, from strongest to weakest, is:

1. Tile-specific timeframe or management zone
2. Dashboard default timeframe or management zone
3. Global timeframe and management zone selection

To set these defaults, see [Create a dashboard](/managed/analyze-explore-automate/dashboards/create-a-dashboard "Create an empty, cloned, or imported dashboard, then add and configure tiles, set dashboard defaults, edit the dashboard JSON, and print it to PDF.").

## Management zones on dashboards

Management zones partition monitoring data based on team ownership and responsibility. Dynatrace filters dashboard content automatically whenever you select a management zone.

Team members who view a zone-specific dashboard without the required management zone permissions see a dashboard with no content. Data appears only after they select a management zone that they have permission to view.

If a metric has multiple entity types, management zone filtering isn't applied. The limitation affects metrics with the dimensions `dt.entity.monitored_entity` or `dt.entity.device_application`. For details, see [Filter metrics by management zone](/managed/analyze-explore-automate/metrics-classic/metrics-mz "How to filter metrics by management zone and related security considerations").

## Dynamic filter evaluation

Dynamic filters narrow the dashboard further from its filter bar. A filter can only be used with dimensions that exist on the metric.

Individual filters on a dashboard are combined with AND. Tag filters and custom dimension filters for the same dimension key or entity are combined with OR. Several filters, whether predefined or for another custom dimension, are also combined with AND.

Custom dimension filters and generic tag filters apply only to tiles that you create in [Data Explorer](/managed/analyze-explore-automate/explorer "Explore Data Explorer topics, from creating and editing metric queries to learning advanced query syntax and resolving common issues.") and pin to the dashboard. They don't apply to standard tiles that you drag to the dashboard from the **Tiles** pane in the dashboard editor, or that you pin from another page such as **Hosts**.

Explicit filters and dynamic filters behave differently:

* An explicit filter is defined in a Data Explorer query and applies to any tile created from that query. It applies only to series related to the selected dimension in that tile.
* A custom dimension dynamic filter also applies to all series in a tile that don't have the selected dimension.

To add filters to a dashboard, see [Add dynamic filters to a dashboard](/managed/analyze-explore-automate/dashboards/add-dynamic-filters-to-a-dashboard "Add dynamic filters to a dashboard, such as operating system, tag key, or custom dimension filters, and then use the filter bar to filter all tiles on it.").

## Tile refresh rates

Every dashboard tile refreshes automatically to update the visualized data. The refresh interval varies with the content of the tile and especially with the applied timeframe.

| Dashboard timeframe | Refresh interval |
| --- | --- |
| Last 2 hours and less | 1 minute |
| Last 2 hours to last 6 hours | 5 minutes |
| Last 6 hours to last 24 hours | 15 minutes |
| Last 24 hours to last 72 hours | 30 minutes |
| Last 72 hours and more | 1 hour |

* In environments under heavy load, Dynatrace might reduce the refresh rate to prevent overloading the Dynatrace Cluster.
* Unlike other tile types, an image tile doesn't refresh automatically. Refresh the dashboard manually to update its image tiles.

## Related topics

* [Create a dashboard](/managed/analyze-explore-automate/dashboards/create-a-dashboard "Create an empty, cloned, or imported dashboard, then add and configure tiles, set dashboard defaults, edit the dashboard JSON, and print it to PDF.")
* [Add dynamic filters to a dashboard](/managed/analyze-explore-automate/dashboards/add-dynamic-filters-to-a-dashboard "Add dynamic filters to a dashboard, such as operating system, tag key, or custom dimension filters, and then use the filter bar to filter all tiles on it.")
* [Share a dashboard](/managed/analyze-explore-automate/dashboards/share-a-dashboard "Share a dashboard with specific users, groups, anyone with the link, or anonymous viewers, and subscribe people to weekly or monthly email reports.")
* [Timeframe selector](/managed/discover-dynatrace/get-started/dynatrace-ui/ui-timeframe-selector "Learn how the timeframe selector works in Dynatrace Managed, including presets, absolute time, relative time, rounded time, and regional format settings.")