---
title: Visualizations
source: https://docs.dynatrace.com/managed/analyze-explore-automate/dashboards/visualizations
---

# Visualizations

# Visualizations

* Reference
* 3-min read
* Updated on Oct 06, 2026

A visualization you create in Data Explorer becomes a dashboard tile when you [pin it](/managed/analyze-explore-automate/dashboards/pin-tiles-to-a-dashboard "Pin a filtered Dynatrace page or a Data Explorer chart to a dashboard as a tile, then update, copy, or clone that tile to other dashboards."), and you configure it in [Visualization settings](/managed/analyze-explore-automate/explorer/visualization-settings "Look up each Data Explorer visualization, what it shows, its limits, its own settings, and the shared settings that carry over to dashboard tiles.") in the Data Explorer section.

## Visualization types

[### Graph

Metric values over time as lines, columns, or areas.](/managed/analyze-explore-automate/dashboards/visualizations#graph "Look up how each Data Explorer visualization looks as a dashboard tile, which tile behavior it supports, and where to find its settings.")[### Stacked column

Metric values over time as stacked columns.](/managed/analyze-explore-automate/dashboards/visualizations#stacked-column "Look up how each Data Explorer visualization looks as a dashboard tile, which tile behavior it supports, and where to find its settings.")[### Stacked area

Metric values over time as stacked areas.](/managed/analyze-explore-automate/dashboards/visualizations#stacked-area "Look up how each Data Explorer visualization looks as a dashboard tile, which tile behavior it supports, and where to find its settings.")[### Pie

One metric as a pie or doughnut chart.](/managed/analyze-explore-automate/dashboards/visualizations#pie "Look up how each Data Explorer visualization looks as a dashboard tile, which tile behavior it supports, and where to find its settings.")[### Single value

One metric merged into a single aggregate value.](/managed/analyze-explore-automate/dashboards/visualizations#single-value "Look up how each Data Explorer visualization looks as a dashboard tile, which tile behavior it supports, and where to find its settings.")[### Table

Query results as table rows, with one metric per column.](/managed/analyze-explore-automate/dashboards/visualizations#table "Look up how each Data Explorer visualization looks as a dashboard tile, which tile behavior it supports, and where to find its settings.")[### Top list

One metric as a ranked list of results.](/managed/analyze-explore-automate/dashboards/visualizations#top-list "Look up how each Data Explorer visualization looks as a dashboard tile, which tile behavior it supports, and where to find its settings.")[### Heatmap

One metric as a value distribution in buckets.](/managed/analyze-explore-automate/dashboards/visualizations#heatmap "Look up how each Data Explorer visualization looks as a dashboard tile, which tile behavior it supports, and where to find its settings.")[### Honeycomb

One cell per result, colored by threshold.](/managed/analyze-explore-automate/dashboards/visualizations#honeycomb "Look up how each Data Explorer visualization looks as a dashboard tile, which tile behavior it supports, and where to find its settings.")[### Histogram

A histogram metric's values as counts per bucket.](/managed/analyze-explore-automate/dashboards/visualizations#histogram "Look up how each Data Explorer visualization looks as a dashboard tile, which tile behavior it supports, and where to find its settings.")

## Graph

A graph tile shows metric values over time as lines, columns, or areas, with up to 20 series per metric.

![Graph with two metrics pinned to a dashboard as a tile](https://dt-cdn.net/images/graph-tile-870-488b205898.png)

Graph with two metrics pinned to a dashboard as a tile

For settings, see [Graph settings](/managed/analyze-explore-automate/explorer/visualization-settings#graph "Look up each Data Explorer visualization, what it shows, its limits, its own settings, and the shared settings that carry over to dashboard tiles.").

## Stacked column

A stacked column tile shows metric values over time as stacked columns. You can stack only metrics with the same unit.

For settings, see [Stacked column settings](/managed/analyze-explore-automate/explorer/visualization-settings#stacked-column "Look up each Data Explorer visualization, what it shows, its limits, its own settings, and the shared settings that carry over to dashboard tiles.").

## Stacked area

A stacked area tile shows metric values over time as stacked areas. You can stack only metrics with the same unit.

![Stacked area chart pinned to a dashboard as a tile](https://dt-cdn.net/images/visualization-example-stacked-area-tile-382-9587cad22e.png)

Stacked area chart pinned to a dashboard as a tile

For settings, see [Stacked area settings](/managed/analyze-explore-automate/explorer/visualization-settings#stacked-area "Look up each Data Explorer visualization, what it shows, its limits, its own settings, and the shared settings that carry over to dashboard tiles.").

## Pie

A pie tile shows query results as a pie or doughnut chart. By default, it shows the first metric of a multi-metric query.

![Pie chart pinned to a dashboard as a tile](https://dt-cdn.net/images/example-tile-pie-299-0d33c675a7.png)

Pie chart pinned to a dashboard as a tile

For settings, see [Pie settings](/managed/analyze-explore-automate/explorer/visualization-settings#pie "Look up each Data Explorer visualization, what it shows, its limits, its own settings, and the shared settings that carry over to dashboard tiles.").

## Single value

A single value tile shows one metric, with all its dimensions merged into a single aggregate.

![Single value pinned to a dashboard as a tile](https://dt-cdn.net/images/single-value-tile-692-7cd9f1dfd1.png)

Single value pinned to a dashboard as a tile

The tile can also show a trend, a sparkline, and a threshold background:

* [Trend](/managed/analyze-explore-automate/explorer/visualization-settings#trend "Look up each Data Explorer visualization, what it shows, its limits, its own settings, and the shared settings that carry over to dashboard tiles."), based on the first and last data points of the timeframe:

  ![Two identical single value tiles, with the trend turned off on the left and turned on on the right](https://dt-cdn.net/images/single-value-trend-off-on-609-98c831bf73.png)

  Two identical single value tiles, with the trend turned off on the left and turned on on the right
* [Sparkline](/managed/analyze-explore-automate/explorer/visualization-settings#show-sparkline "Look up each Data Explorer visualization, what it shows, its limits, its own settings, and the shared settings that carry over to dashboard tiles."):

  ![Two identical single value tiles, with the sparkline turned off on the left and turned on on the right](https://dt-cdn.net/images/single-value-sparkline-off-on-608-c9f1a6cb61.png)

  Two identical single value tiles, with the sparkline turned off on the left and turned on on the right
* Threshold background, the threshold color in the tile background:

  ![Two identical single value tiles, with the threshold background turned off on the left and turned on on the right](https://dt-cdn.net/images/single-value-threshold-background-off-on-609-c0be9c322d.png)

  Two identical single value tiles, with the threshold background turned off on the left and turned on on the right

For settings, see [Single value settings](/managed/analyze-explore-automate/explorer/visualization-settings#single-value "Look up each Data Explorer visualization, what it shows, its limits, its own settings, and the shared settings that carry over to dashboard tiles.").

## Table

A table tile shows query results as rows, with one metric per column.

![Table pinned to a dashboard as a tile](https://dt-cdn.net/images/example-tile-table-342-b738cc1b64.png)

Table pinned to a dashboard as a tile

* The query limit sets the maximum number of rows, shown in pages.
* Page controls are on the tile.
* The page size adjusts to the tile size.
* Columns you turn off in the Data Explorer **Columns** section are also hidden on the table tile.

For settings, see [Table settings](/managed/analyze-explore-automate/explorer/visualization-settings#table "Look up each Data Explorer visualization, what it shows, its limits, its own settings, and the shared settings that carry over to dashboard tiles.").

## Top list

A top list tile shows a ranked list of results for one metric. By default, it shows the first metric of a multi-metric query.

![Top list pinned to a dashboard as a tile](https://dt-cdn.net/images/example-tile-top-list-263-57605443d4.png)

Top list pinned to a dashboard as a tile

For settings, see [Top list settings](/managed/analyze-explore-automate/explorer/visualization-settings#top-list "Look up each Data Explorer visualization, what it shows, its limits, its own settings, and the shared settings that carry over to dashboard tiles.").

## Heatmap

A heatmap tile shows the value distribution of one metric in buckets. By default, it shows the first metric of a multi-metric query.

For settings, see [Heatmap settings](/managed/analyze-explore-automate/explorer/visualization-settings#heatmap "Look up each Data Explorer visualization, what it shows, its limits, its own settings, and the shared settings that carry over to dashboard tiles.").

## Honeycomb

A honeycomb tile shows one cell per result, colored by threshold, for example green, yellow, and red. Hover over a cell to see details, and select it for drilldown options.

![Honeycomb pinned to a dashboard as a tile](https://dt-cdn.net/images/example-tile-honeycomb-307-83b6e4bf37.png)

Honeycomb pinned to a dashboard as a tile

For settings, see [Honeycomb settings](/managed/analyze-explore-automate/explorer/visualization-settings#honeycomb "Look up each Data Explorer visualization, what it shows, its limits, its own settings, and the shared settings that carry over to dashboard tiles.").

## Histogram

A histogram tile shows the value distribution of a histogram metric, with one bar per bucket.

![Histogram pinned to a dashboard as a tile](https://dt-cdn.net/images/dashboard-1260-3a410212b9.png)

Histogram pinned to a dashboard as a tile

For settings, see [Histogram settings](/managed/analyze-explore-automate/explorer/visualization-settings#histogram "Look up each Data Explorer visualization, what it shows, its limits, its own settings, and the shared settings that carry over to dashboard tiles.").

## Tile behavior

* A tile created with Data Explorer shows at most 4,000 data points per query. Beyond that, Dynatrace switches to a coarser resolution. The limit doesn't apply in Data Explorer.
* The legend is active: select a legend entry to show or hide it.
* Threshold colors, units, and formats carry over to tiles.