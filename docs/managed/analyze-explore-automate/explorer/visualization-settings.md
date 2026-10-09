---
title: Visualization settings
source: https://docs.dynatrace.com/managed/analyze-explore-automate/explorer/visualization-settings
---

# Visualization settings

# Visualization settings

* Reference
* 10-min read
* Updated on Oct 06, 2026

Data Explorer offers ten visualization types. You select and configure a visualization here, and a visualization you pin to a dashboard keeps its settings as a dashboard tile.

## Visualization types

[### Graph

Metric values over time as lines, columns, or areas.](/managed/analyze-explore-automate/explorer/visualization-settings#graph "Look up each Data Explorer visualization, what it shows, its limits, its own settings, and the shared settings that carry over to dashboard tiles.")[### Stacked column

Metric values over time as stacked columns.](/managed/analyze-explore-automate/explorer/visualization-settings#stacked-column "Look up each Data Explorer visualization, what it shows, its limits, its own settings, and the shared settings that carry over to dashboard tiles.")[### Stacked area

Metric values over time as stacked areas.](/managed/analyze-explore-automate/explorer/visualization-settings#stacked-area "Look up each Data Explorer visualization, what it shows, its limits, its own settings, and the shared settings that carry over to dashboard tiles.")[### Pie

One metric as a pie or doughnut chart.](/managed/analyze-explore-automate/explorer/visualization-settings#pie "Look up each Data Explorer visualization, what it shows, its limits, its own settings, and the shared settings that carry over to dashboard tiles.")[### Single value

One metric merged into a single aggregate value.](/managed/analyze-explore-automate/explorer/visualization-settings#single-value "Look up each Data Explorer visualization, what it shows, its limits, its own settings, and the shared settings that carry over to dashboard tiles.")[### Table

Query results as table rows, with one metric per column.](/managed/analyze-explore-automate/explorer/visualization-settings#table "Look up each Data Explorer visualization, what it shows, its limits, its own settings, and the shared settings that carry over to dashboard tiles.")[### Top list

One metric as a ranked list of results.](/managed/analyze-explore-automate/explorer/visualization-settings#top-list "Look up each Data Explorer visualization, what it shows, its limits, its own settings, and the shared settings that carry over to dashboard tiles.")[### Heatmap

One metric as a value distribution in buckets.](/managed/analyze-explore-automate/explorer/visualization-settings#heatmap "Look up each Data Explorer visualization, what it shows, its limits, its own settings, and the shared settings that carry over to dashboard tiles.")[### Honeycomb

One cell per result, colored by threshold.](/managed/analyze-explore-automate/explorer/visualization-settings#honeycomb "Look up each Data Explorer visualization, what it shows, its limits, its own settings, and the shared settings that carry over to dashboard tiles.")[### Histogram

A histogram metric's values as counts per bucket.](/managed/analyze-explore-automate/explorer/visualization-settings#histogram "Look up each Data Explorer visualization, what it shows, its limits, its own settings, and the shared settings that carry over to dashboard tiles.")

Select a visualization from the list in the upper-left corner of Data Explorer. When you switch visualizations, settings that don't apply to the new visualization are ignored, and an information icon in the list warns you. If you switch back, you might need to reconfigure them.

To choose which metrics of a multi-metric query a visualization shows, select the letter next to a metric or .

For how each visualization looks as a dashboard tile, see [Visualizations](/managed/analyze-explore-automate/dashboards/visualizations "Look up how each Data Explorer visualization looks as a dashboard tile, which tile behavior it supports, and where to find its settings.") in the Dashboards section.

## Graph

A graph shows metric values over time as lines, columns, or areas. A graph can show any selection of metrics in the query, with up to 20 series per metric.

![Graph with an area metric and a line metric in Data Explorer](https://dt-cdn.net/images/visualization-example-graph-area-and-line-1586-2d9ef73a87.png)

Graph with an area metric and a line metric in Data Explorer

**Chart mode** is a dropdown next to the color palette of each metric, and sets the metric to `Line`, `Column chart`, `Area`, `Stacked column`, or `Stacked area`.

Baselines, correlated metrics, and focus are graph actions rather than settings. See [Add a baseline](/managed/analyze-explore-automate/explorer/use-data-explorer-results#baselines "Interact with Data Explorer results, pin them to a dashboard, share them, export them, copy API requests, and resolve common result issues."), [Add correlated metrics](/managed/analyze-explore-automate/explorer/use-data-explorer-results#correlated-metrics "Interact with Data Explorer results, pin them to a dashboard, share them, export them, copy API requests, and resolve common result issues."), and [Focus on a metric series](/managed/analyze-explore-automate/explorer/use-data-explorer-results#focus "Interact with Data Explorer results, pin them to a dashboard, share them, export them, copy API requests, and resolve common result issues.").

For how the tile looks, see [Graph tiles](/managed/analyze-explore-automate/dashboards/visualizations#graph "Look up how each Data Explorer visualization looks as a dashboard tile, which tile behavior it supports, and where to find its settings.").

Shared settings that apply: Unit and format, resolution, legend, connect gaps, rename, color palette, color override, axes, and thresholds. See [Shared settings](#shared-settings).

## Stacked column

A stacked column chart shows metric values over time as stacked columns. Your metric selection controls which metrics are stacked, and only metrics with the same unit can be stacked.

![Stacked column chart of several metrics in Data Explorer](https://dt-cdn.net/images/visualization-example-stacked-column-1586-a2237bad33.png)

Stacked column chart of several metrics in Data Explorer

For how the tile looks, see [Stacked column tiles](/managed/analyze-explore-automate/dashboards/visualizations#stacked-column "Look up how each Data Explorer visualization looks as a dashboard tile, which tile behavior it supports, and where to find its settings.").

Shared settings that apply: Unit and format, resolution, legend, connect gaps, rename, color palette, color override, axes, and thresholds. See [Shared settings](#shared-settings).

## Stacked area

A stacked area chart shows metric values over time as stacked areas. Your metric selection controls which metrics are stacked, and only metrics with the same unit can be stacked.

![Stacked area chart of several metrics in Data Explorer](https://dt-cdn.net/images/visualization-example-stacked-area-1583-b9048b662e.png)

Stacked area chart of several metrics in Data Explorer

For how the tile looks, see [Stacked area tiles](/managed/analyze-explore-automate/dashboards/visualizations#stacked-area "Look up how each Data Explorer visualization looks as a dashboard tile, which tile behavior it supports, and where to find its settings.").

Shared settings that apply: Unit and format, resolution, legend, connect gaps, rename, color palette, color override, axes, and thresholds. See [Shared settings](#shared-settings).

## Pie

A pie shows query results as a pie or doughnut chart. By default, it shows the first metric of a multi-metric query. Thresholds don't apply to a pie.

For how the tile looks, see [Pie tiles](/managed/analyze-explore-automate/dashboards/visualizations#pie "Look up how each Data Explorer visualization looks as a dashboard tile, which tile behavior it supports, and where to find its settings.").

Shared settings that apply: Unit and format, legend, fold transformation, rename, color palette, and color override. See [Shared settings](#shared-settings).

## Single value

A single value shows one metric and merges all its dimensions into a single aggregate.

![Single value visualization in Data Explorer](https://dt-cdn.net/images/visualization-example-single-value-1596-744c260a83.png)

Single value visualization in Data Explorer

### Show trend

**Show trend** shows the trend in the tile, based on the first and last data points of the selected timeframe.

### Show sparkline

**Show sparkline** shows a sparkline in the tile.

### Threshold background

**Threshold background** reflects the threshold color in the tile background when turned on.

For how the tile looks, see [Single value tiles](/managed/analyze-explore-automate/dashboards/visualizations#single-value "Look up how each Data Explorer visualization looks as a dashboard tile, which tile behavior it supports, and where to find its settings.").

Shared settings that apply: Unit and format, fold transformation, rename, and thresholds. See [Shared settings](#shared-settings).

## Table

A table shows query results as rows, with one metric per column. A table can show any selection of metrics in the query, and shows 100 rows by default.

![Table with two metrics split by dimension in Data Explorer](https://dt-cdn.net/images/visualization-example-table-two-metrics-split-1590-45fa100eb8.png)

Table with two metrics split by dimension in Data Explorer

### Sort

* A table is sorted by the first metric in the query, in descending order of its aggregation. To sort by another metric, move it to the top of the query definition.
* **Sort by** sets the dimension to sort by, with the order `ASC` or `DESC`.

### Columns

The **Columns** section turns individual columns on or off. The selection also applies to table tiles.

### Rows

In Data Explorer, results are limited to 100 rows by default. **Limit** sets another value, and **Limit** > **Maximum** removes the limit, as does removing `:limit(100)` in advanced mode. For the row limit on a table tile, see [Table tiles](/managed/analyze-explore-automate/dashboards/visualizations#table "Look up how each Data Explorer visualization looks as a dashboard tile, which tile behavior it supports, and where to find its settings.").

### Pages

Page controls are at the bottom of the **Result** section, and on table tiles. For the page size of a table tile, see [Table tiles](/managed/analyze-explore-automate/dashboards/visualizations#table "Look up how each Data Explorer visualization looks as a dashboard tile, which tile behavior it supports, and where to find its settings.").

### Table thresholds

* A table can have one threshold definition per metric. **Add threshold** adds one for another metric, and the trash can icon deletes one.
* **Link cell color to thresholds** colors the background of every cell by threshold. When it's off, only the cell data is colored.
* Tile text color adjusts automatically for contrast with the threshold color.

For how the tile looks, see [Table tiles](/managed/analyze-explore-automate/dashboards/visualizations#table "Look up how each Data Explorer visualization looks as a dashboard tile, which tile behavior it supports, and where to find its settings.").

Shared settings that apply: Unit and format, fold transformation, rename, and thresholds. See [Shared settings](#shared-settings).

## Top list

A top list shows a ranked list of results. A top list doesn't show multiple metrics: only the metric selected in the query editor runs, and the first metric is selected by default.

![Top list visualization in Data Explorer](https://dt-cdn.net/images/visualization-example-top-list-1596-f2a02801a3.png)

Top list visualization in Data Explorer

For how the tile looks, see [Top list tiles](/managed/analyze-explore-automate/dashboards/visualizations#top-list "Look up how each Data Explorer visualization looks as a dashboard tile, which tile behavior it supports, and where to find its settings.").

Shared settings that apply: Unit and format, fold transformation, rename, color override, and thresholds. See [Shared settings](#shared-settings).

## Heatmap

A heatmap shows the value distribution in buckets. By default, it shows the first metric of a multi-metric query.

![Heatmap visualization in Data Explorer](https://dt-cdn.net/images/visualization-example-heatmap-1601-ba27fd4447.png)

Heatmap visualization in Data Explorer

**Y axis** shows the Y axis by value or split by dimensions. **Buckets** sets the number of buckets on each axis. The default is `Auto`; clear a number to return to `Auto`.

For how the tile looks, see [Heatmap tiles](/managed/analyze-explore-automate/dashboards/visualizations#heatmap "Look up how each Data Explorer visualization looks as a dashboard tile, which tile behavior it supports, and where to find its settings.").

Shared settings that apply: Unit and format, resolution, legend, show labels, rename, color palette, and thresholds. See [Shared settings](#shared-settings).

## Honeycomb

A honeycomb shows one cell per result, colored by threshold. By default, it shows the first metric of a multi-metric query and 100 cells. To show more, use **Limit** > **Maximum**, or remove `:limit(100)` from the query in advanced mode. Hover over a cell on a tile to see details, and select it for drilldown options.

![Honeycomb visualization in Data Explorer](https://dt-cdn.net/images/visualization-example-honeycomb-1600-2064dff7eb.png)

Honeycomb visualization in Data Explorer

**Show hive** works with **Show legend**:

* **Show hive** only: the hive is the only representation of the results.
* **Show legend** only: the legend is the only representation of the results.
* Both: the hive is the primary visualization, with the legend under it.

For how the tile looks, see [Honeycomb tiles](/managed/analyze-explore-automate/dashboards/visualizations#honeycomb "Look up how each Data Explorer visualization looks as a dashboard tile, which tile behavior it supports, and where to find its settings.").

Shared settings that apply: Unit and format, legend, show labels, fold transformation, rename, color palette, and thresholds. See [Shared settings](#shared-settings).

## Histogram

A histogram shows the value distribution of a histogram metric, such as response times or request sizes, so you can see value distributions, percentiles, and outliers at a glance. The visualization requires a [histogram metric](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#histograms "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply."), whose metric key ends in `.histogram`.

The chart shows one bar per bucket, labeled by its value range. The first and last buckets are open-ended. Each bar shows the count of that bucket alone, not the cumulative counts that the `:histogram` transformation returns. For the transformation and for percentiles, see [Analyze an explicit histogram](/managed/analyze-explore-automate/explorer/explorer-advanced-query-editor#example-histogram "Learn how to build and edit advanced Data Explorer queries, use metric transformations and expressions, and compare metrics across timeframes.").

![Histogram visualization in Data Explorer](https://dt-cdn.net/images/data-explorer-1590-1be3bb1b48.png)

Histogram visualization in Data Explorer

For how the tile looks, see [Histogram tiles](/managed/analyze-explore-automate/dashboards/visualizations#histogram "Look up how each Data Explorer visualization looks as a dashboard tile, which tile behavior it supports, and where to find its settings.").

Shared settings that apply: Unit and format, resolution, legend, rename, color palette, color override, and thresholds. See [Shared settings](#shared-settings).

## Shared settings

These options appear in the **Settings** section. Its contents depend on the selected visualization.

| Setting | Visualizations | Description |
| --- | --- | --- |
| **Resolution** | Graph, Stacked column, Stacked area, Heatmap, Histogram | X axis (time) granularity; `Auto` or a value from the list |
| **Show legend** | Graph, Stacked column, Stacked area, Pie, Heatmap, Honeycomb, Histogram | Shows a legend; in a heatmap, the legend matches colors to the value range |
| **Show labels** | Heatmap, Honeycomb | Shows a count for each heatmap bucket, or a label and value in each honeycomb cell |
| **Connect gaps** | Graph, Stacked column, Stacked area | Connects gaps in the chart when turned on (off by default) |
| **Fold transformation** | Pie, Single value, Table, Top list, Honeycomb | Combines a timeseries into a single data point; default `Auto` |

The **Settings** section also lists options for each metric in the query.

| Setting | Visualizations | Description |
| --- | --- | --- |
| **Rename** | All | Display name on the chart and in the legend, or the column heading in a table; the query keeps the original metric name. Set it with the pencil icon next to the metric name. |
| **Chart mode** | Graph | Dropdown next to the color palette with `Line`, `Column chart`, `Area`, `Stacked column`, or `Stacked area` |
| **Color palette** | Graph, Stacked column, Stacked area, Pie, Heatmap, Honeycomb, Histogram | Color palette for the metric |
| **Color override** | Graph, Stacked column, Stacked area, Pie, Top list, Histogram | Fixed color for one series, such as a selected host, that overrides the palette |

### Resolution

Some resolutions are unavailable for some timeframes. If you select an incompatible combination, Dynatrace applies a resolution automatically and displays a message such as `Auto-resolution applied. Resolution value of [6 hours] applied. Selected timeframe doesn't allow for [5 minutes] resolution.` Select a different resolution to override it.

For the data point limit of a dashboard tile, see [Tile behavior](/managed/analyze-explore-automate/dashboards/visualizations#tile-behavior "Look up how each Data Explorer visualization looks as a dashboard tile, which tile behavior it supports, and where to find its settings.").

### Connect gaps

**Connect gaps** draws a continuous line across intervals without data. It's available for Graph, Stacked column, and Stacked area.

### Legend

The legend is active: select a legend entry to turn the display of that entry on or off.

### Fold transformation values

* `Auto` selects the most appropriate time aggregation for the metric.
* Other values: `Last value`, `Average`, `Count`, `Maximum`, `Minimum`, `Sum`, `Median`, `Value`, `Percentile 10th`, `Percentile 75th`, `Percentile 90th`.
* `Last value` shows the last reported value instead of an aggregation.

The fold transformation affects the resolution:

* With `Auto` in a table, single value, top list, or honeycomb, the `Inf` (infinity) resolution is used for backward compatibility. If the metric selector doesn't support `Inf`, the `fold` transformation is added to the end of the query.
* With any other value, `fold` is used.

All metric selectors use the same total value mechanism, `fold` or `Inf`, so adding a selector that requires `fold` might change the results of the other selectors. To see the query Data Explorer sends, select  > **Copy request** in the **Result** section.

### Unit and format

You set **Unit** and **Format** for each metric. These settings control how values are displayed, and also apply to values you export to a CSV file.

| Setting | Values | Description |
| --- | --- | --- |
| **Unit** | `None`, `Auto`, a unit, or a custom string | `None` shows no unit; `Auto` lets Dynatrace select a display unit; other units depend on the metric's unit; enter a custom unit or suffix in the box and select it from the list |
| **Format** | `None`, `Auto`, `0`, `0.0`, `0.00`, `0.000` | Decimal places; `Auto` shows `5.06 %` where `None` shows `5.062357754177517 %` |

In advanced mode, use `:setUnit(<unit>)` to select from a wider range of units.

Dynatrace uses this order-of-magnitude notation:

| Notation | Factor | Meaning |
| --- | --- | --- |
| `k` | `10^3` | Kilo, thousand |
| `M` | `10^6` | Mega, million |
| `G` | `10^9` | Giga, billion |
| `T` | `10^12` | Tera, trillion |

Examples:

* **Bytes**: `Auto` selects a readable unit such as `GiB`, or `GB` for a decimal base, which is used when the metric defines no base. Select `B`, `KiB`, `MiB`, or `GiB` for a fixed unit, or `None` for raw bytes.
* **Dollars and cents**: `Auto` with **Format** `0.00` shows exact amounts; `k (thousand)`, `M (million)`, or `G (billion)` with **Format** `0` shows large amounts without cents.
* **Counts**: `Auto` with **Format** `None` shows an exact count; `k`, `M`, `G`, or `T` with **Format** `0.0`, `0.00`, or `0.000` shows a rough count.

### Axes

The **Axes** section is available for Graph, Stacked column, and Stacked area. The section lists the X axis and each Y axis.

| Setting | Values | Description |
| --- | --- | --- |
| Name | Text | Axis name, shown vertically next to a Y axis and horizontally under the X axis; the X axis has no name by default. Set it with the pencil icon next to the axis. |
| **Axis metric** | Metrics | Metrics plotted on that Y axis |
| Visibility |  | Hides or shows the axis |
| **Position** | `Left`, `Right` | Side of the chart for a Y axis; default `Left` for the first Y axis |
| **Min, Max** | `Auto, Auto` or two comma-separated numbers | Range of a Y axis (default `Auto, Auto`); the X axis has only a name and visibility |
| **Add Y axis** | Button | Adds a Y axis for a metric, unavailable when every metric already has an axis; only the first two metrics get a Y axis automatically |

### Thresholds

The **Threshold** section sets threshold values and colors for every visualization except Pie, and the colors also apply to dashboard tiles.

* Set **Unit** before the thresholds. Threshold values then match the selected unit, so you enter `MiB` values without the unit. If you change **Unit** later, the thresholds aren't adjusted. With **Unit** `Auto`, enter thresholds in the base unit, such as bytes.
* Threshold colors are optional, and  hides or shows them without deleting the values.

## Result problems

For missing series and empty table cells, see [Troubleshoot results](/managed/analyze-explore-automate/explorer/use-data-explorer-results#troubleshooting "Interact with Data Explorer results, pin them to a dashboard, share them, export them, copy API requests, and resolve common result issues.").