---
title: Configure and use a table visualization in Dynatrace
source: https://docs.dynatrace.com/managed/analyze-explore-automate/dashboards-classic/charts-and-tiles/visualization-table
---

# Configure and use a table visualization in Dynatrace

# Configure and use a table visualization in Dynatrace

* How-to guide
* 4-min read
* Published Dec 13, 2021

[Dashboards Classic](/managed/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.")

To visualize your query results as a table, one metric per column, select  `Table` from the list above the query definition, in the upper-left corner of the page.

#### Example in Data Explorer

![Data Explorer: Table with two metrics (split)](https://dt-cdn.net/images/visualization-example-table-two-metrics-split-1590-45fa100eb8.png)

Data Explorer: Table with two metrics (split)

#### Example pinned to a dashboard as a tile

![Example table tile](https://dt-cdn.net/images/example-tile-table-342-b738cc1b64.png)

Example table tile

## Change visualization

When switching between visualizations, be aware that some visualization settings are visualization-specific.

* If you select a visualization and configure **Settings** for that visualization, and then you switch to a different visualization, some of your settings for the first visualization may be ignored because they don't apply to the newly selected visualization. An information icon in the list of visualizations will alert you to the possibility.

  ![Data Explorer: Visualization switch warning](https://dt-cdn.net/images/change-visualization-warning-1277-9438aaceea.png)

  Data Explorer: Visualization switch warning
* If you switch back to the original visualization, you may need to reconfigure some visualization settings.

## Change metric selection

Your visualization can show any selection of metrics in a multi-metric query.

To toggle metrics on and off, you can select the letter next to the metric you want to visualize, or you can select the eye icon .

![Data Explorer: Toggle metric](https://dt-cdn.net/images/eye-toggle-metric-1238-d343b9cc0e.png)

Data Explorer: Toggle metric

## Sort by column and order

By default, Data Explorer tables are sorted by the first metric in the table query (in descending order based on the aggregation chosen).

To sort a Data Explorer table by a different column, you need to change the column order.

1. Locate the metric by which you want to sort the table.
2. Drag ![Drag handle](https://dt-cdn.net/images/drag-handle-turquoise-600-1aa0e5ea00.svg "Drag handle") that metric to the top position in the query definition.
3. Run the query.

   The table will be sorted by the metric you dragged to the first place in the query definition.

To set the sort order

1. If **Sort by** is not already displayed for the metric, select  and then select `Sort by` from the list.
2. Set **Sort by** to the dimension by which you want to sort.
3. Select the sort order: `ASC` (ascending) or `DESC` (descending).

## Settings

The **Settings** section is one of the expandable sections in the right panel of Data Explorer. The contents of the **Settings** section may vary depending on the visualization you have selected.

![Data Explorer: Settings section](https://dt-cdn.net/images/data-explorer-settings-settings-322-7b365c52e5.png)

Data Explorer: Settings section

### Fold transformation

The fold transformation combines a data points list (a timeseries: a collection of data points over the time period) into a single data point.

* The default fold transformation is `Auto`, which automatically selects the most appropriate time aggregation based on the metric.
* You can manually override `Auto` with any of the following: `Last value`, `Average`, `Count`, `Maximum`, `Minimum`, `Sum`, `Median`, `Value`, `Percentile 10th`, `Percentile 75th`, `Percentile 90th`.
* If you need to see the last reported value for a metric (rather than an aggregation), select `Last value`.

Fold transformation and resolution

Be aware that the **Fold transformation** setting affects the resolution.

* If **Fold transformation** is set to `Auto` for visualization `Table`, `Single value`, `Top list`, or `Honeycomb`, the `Inf` (infinity) resolution is used to maintain backward compatibility. If the chosen metric selector doesn't support the `Inf` resolution, the `fold` transformation is automatically added to the end of the query.
* If **Fold transformation** is set to a value other than `Auto`, `fold` is used.

Because all metric selectors are queried using the same total value mechanism (either `fold` or `Inf`), adding a new selector that requires `fold` might change the result of the other selectors.

To inspect the actual query used by Data Explorer, go to the **Result** section in Data Explorer and select  > **Copy request**.

## Settings per metric

Table column names are the same as the metric names by default. You can change the name of table column headings. The query definition retains the metric's original name.

To rename a column

1. In the **Settings** section, select  for the metric/column you want to rename.

   ![Rename metric](https://dt-cdn.net/images/single-value-rename-metric-232-266-b358f19b2b.png)

   Rename metric
2. Edit the name, and then select the checkmark to save the new name.

### Unit and Format

Use the **Unit** and **Format** settings to determine how your data is displayed. If you export to a CSV file, the **Unit** and **Format** settings are also reflected in the exported values.

#### Unit

Use the **Unit** setting to set the unit in which the metric is displayed.

* `None` = No unit displayed
* `Auto` = Dynatrace selects an appropriate display unit
* Other selections specify the exact unit to display. The options here depend on the metric's unit. A time metric, for example, offers alternative units for displaying time.
* To add a custom unit/suffix string, type the custom string in the **Unit** box and then select it from the list.
* In **Advanced mode**, you can use `:setUnit(<unit>)` to select from a wider range of units.

Examples of order-of-magnitude notation in Dynatrace:

| Notation | Factor | Meaning |
| --- | --- | --- |
| k | 10^3 | kilo, thousand |
| M | 10^6 | mega, million |
| G | 10^9 | giga, billion |
| T | 10^12 | tera, trillion |

#### Format

Use the **Format** setting to configure the number of decimal places displayed for the selected metric.

* `None` = No formatting.
* `Auto` = Dynatrace selects an appropriate format. For example, where `None` would display `5.062357754177517 %`, `Auto` would display `5.06 %`.
* Other selections specify the number of decimal places to display: `0`, `0.0`, `0.00`, `0.000`

#### Examples

Example: bytes

When the basic unit of the metric is **bytes**:

* If you set **Unit** to `Auto`, Dynatrace automatically expresses the results in a human-readable unit, which in this case could be `GiB`.

  A byte-based unit can have either a binary or decimal base, which will determine whether Dynatrace selects, for example, `GiB` or `GB`. If no base is defined in the metric itself, a decimal base is used.
* If the automatically selected unit isn't suitable in your case, you can force Dynatrace to express the same values in a specific unit (**Unit** = `B`, `KiB`, `MiB`, or `GiB`).
* If you want to see raw data (no conversion), you can set **Unit** to `None` and see the results in the basic unit of the metric (which in this case is bytes).

Example: dollars and cents

When the basic unit of a metric is **dollars and cents**:

* For smaller values, to see the results expressed in exact dollars and cents: set **Unit** to `Auto`, and set **Format** to `0.00` (to have two decimal places for the cents).
* For larger values, to see the results expressed in thousands, millions, or billions of dollars and no cents: set **Unit** to `k (thousand)`, `M (million)`, `G (billion)`, and set **Format** to `0` (to see nothing after the decimal point).

Example: exact counts

When the basic unit for the metric is a **count**:

* To see an exact count:

  + Set **Unit** to `Auto`
  + Set **Format** to `None`
* To see a rough count:

  + Set **Unit** to `k (thousand)`, `M (million)`, `G (billion)`, or `T (trillion)`, depending on the magnitude of your values
  + Set **Format** to `0.0`, `0.00`, or `0.0000`, depending on how many decimal places make sense in combination with the selected **Unit** setting

Example: thresholds

When setting threshold values:

* If you select a **Unit** (for example, `MiB`), the **Threshold** settings are then prepared to match the selected unit, so you just need to enter threshold values without specifying `MiB`.
* If you set **Unit** to `Auto` (to let Dynatrace automatically scale the displayed output), you still need to set **Threshold** values in a specific unit such as bytes.

## Columns

Use the checkboxes in the **Columns** section of the Data Explorer table visualization to enable and disable columns individually. These selections are reflected in the resulting table dashboard tiles.

## Rows

### Data Explorer

By default, the number of results is limited to 100.

To set an explicit limit

1. If **Limit** is not already displayed in the query editor, select  and then select `Limit` from the list.
2. Set **Limit** to one of the available values.

Use **Limit** > **Maximum** to remove the limit or turn on **Advanced mode** and remove `:limit(100)` from the query.

### Dashboard table tile

In a dashboard table tile, the maximum number of rows displayed is determined by the query limit set in Data Explorer. Results are displayed in pages on the tile.

## Pages

Use the controls at the bottom of the **Result** section of a Data Explorer table visualization to page through tables.

* Table dashboard tiles also have page controls.
* The page size of a table dashboard tile is automatically resized to match the size of the tile.

## Threshold

To enhance your visualizations, you can set thresholds that are reflected in your visualization.

A table can have as many thresholds as there are metrics displayed on the table. This example has five metrics, five columns, each with a different threshold definition. **Link cell color to thresholds** is turned on.

![Example table with different thresholds for each metric/column](https://dt-cdn.net/images/threshold-definition-table-with-multiple-thresholds-1065-2f6a222655.png)

Example table with different thresholds for each metric/column

Tile text color is adjusted automatically for contrast with the background threshold color.

### Set table thresholds

To make per-metric threshold settings

1. Optional In the **Threshold** section, select **Link cell color to thresholds**

   * When this is turned on, the background of every cell in the table is colored according to threshold.

     ![Link cell background color to thresholds](https://dt-cdn.net/images/threshold-definition-link-cell-color-327-9b26a66881.png)

     Link cell background color to thresholds
   * When this is turned off, only the cell data is colored.
2. Make per-metric threshold settings.

   * Select a metric name

     ![Select metric for thresholds](https://dt-cdn.net/images/threshold-definition-select-metric-328-b862ac5975.png)

     Select metric for thresholds
   * Set the threshold values for that metric

     ![Add threshold values](https://dt-cdn.net/images/threshold-definition-set-threshold-values-327-82ef5b0bb1.png)

     Add threshold values
   * Optional Adjust threshold colors

     ![Adjust the threshold colors](https://dt-cdn.net/images/threshold-definition-adjust-threshold-color-269-2e5d1f3fb4.png)

     Adjust the threshold colors

Select **Add threshold** as needed to add thresholds for another metric.

![Add thresholds for another metric](https://dt-cdn.net/images/threshold-definition-add-threshold-327-b69320f466.png)

Add thresholds for another metric

### Hide or show threshold colors

To hide or show threshold colors (per threshold definition) without deleting the threshold settings, in the **Thresholds** section, select  for that metric.

![Show or display threshold colors](https://dt-cdn.net/images/threshold-definition-hide-or-show-309-d695bc3f22.png)

Show or display threshold colors

### Delete threshold settings

To delete the threshold settings for a metric, in the **Thresholds** section, select the trash can icon for that metric.

![Delete threshold settings](https://dt-cdn.net/images/threshold-definition-delete-309-99ef47b511.png)

Delete threshold settings

## FAQ

Why am I not seeing all series of my metric?

* The *default* number of displayed series per metric is `20`. Consequently, some series might be missing in Data Explorer. To ensure the series data you're looking for is displayed, provide more specific filters such as a management zone or an entity name filter.
* The *maximum* number of displayed series per metric is `100`. Note that this limit applies even if you remove the [**limit** transformation](/managed/dynatrace-api/environment-api/metric-v2/metric-selector#limit "Configure the metric selector for the Metric v2 API.") from the metric selector on the [**Code** tab](/managed/analyze-explore-automate/explorer/explorer-advanced-query-editor "Build advanced queries using the Data Explorer advanced mode.").

If series data is absent for a metric expression, see [Why is the result of my metric expression empty?](/managed/dynatrace-api/environment-api/metric-v2/metric-faq#empty-result-metric-expression "Frequently asked questions about the Metrics API v2.").

Why are some table cells empty when they should have values?

The root cause of this issue is often the same as for [Why am I not seeing all series of my metric?](#missing-series)

The metric series are limited to a certain number.

Suppose you query `builtin:host.cpu.usage` and `builtin:host.cpu.idle` split by `dt.entity.host`. For both metrics, the top 100 hosts are requested per default. But the top 100 hosts of the `builtin:host.cpu.usage` metric probably diverges from the top 100 hosts of the `builtin:host.cpu.idle` metric, leading to empty cells in the table for some hosts.