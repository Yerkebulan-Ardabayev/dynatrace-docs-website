---
title: Configure and use a single-value visualization in Dynatrace
source: https://docs.dynatrace.com/managed/analyze-explore-automate/dashboards-classic/charts-and-tiles/visualization-single-value
---

# Configure and use a single-value visualization in Dynatrace

# Configure and use a single-value visualization in Dynatrace

* How-to guide
* 1-min read
* Published Dec 13, 2021

[Dashboards Classic](/managed/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.")

To visualize your query results as a single-value chart or tile, select  `Single value` from the list above the query definition, in the upper-left corner of the page.

* This visualization shows one metric as a single-value chart or tile
* It merges all dimensions to a single aggregate.

#### Example in Data Explorer

![Data Explorer: Single value visualization](https://dt-cdn.net/images/visualization-example-single-value-1596-744c260a83.png)

Data Explorer: Single value visualization

#### Example dashboard tile

![Example single value tile](https://dt-cdn.net/images/single-value-tile-692-7cd9f1dfd1.png)

Example single value tile

## Change visualization

When switching between visualizations, be aware that some visualization settings are visualization-specific.

* If you select a visualization and configure **Settings** for that visualization, and then you switch to a different visualization, some of your settings for the first visualization may be ignored because they don't apply to the newly selected visualization. An information icon in the list of visualizations will alert you to the possibility.

  ![Data Explorer: Visualization switch warning](https://dt-cdn.net/images/change-visualization-warning-1277-9438aaceea.png)

  Data Explorer: Visualization switch warning
* If you switch back to the original visualization, you may need to reconfigure some visualization settings.

## Change metric selection

By default, this visualization shows the first metric of a multi-metric query.

To select a different metric from a multi-metric query, you can select the letter next to the metric you want to visualize, or you can select the eye icon .

![Data Explorer: Toggle metric](https://dt-cdn.net/images/eye-toggle-metric-1238-d343b9cc0e.png)

Data Explorer: Toggle metric

## Settings

The **Settings** section is one of the expandable sections in the right panel of Data Explorer. The contents of the **Settings** section may vary depending on the visualization you have selected.

![Data Explorer: Settings section](https://dt-cdn.net/images/data-explorer-settings-settings-322-7b365c52e5.png)

Data Explorer: Settings section

### Show trend

Determines whether the tile displays the trend (based on the first and last datapoints of the selected timeframe). In this example, there are two identical tiles, one with **Show trend** turned off, and then the same tile with **Show trend** turned on (trending down).

![Trend turned off (left) and trend turned on (right)](https://dt-cdn.net/images/single-value-trend-off-on-609-98c831bf73.png)

Trend turned off (left) and trend turned on (right)

### Show sparkline

Determines whether the tile displays a sparkline. In this example, there are two identical tiles, one with **Show sparkline** turned off, and then the same tile with **Show sparkline** turned on.

![Sparkline off (left) and on (right)](https://dt-cdn.net/images/single-value-sparkline-off-on-608-c9f1a6cb61.png)

Sparkline off (left) and on (right)

### Threshold background

Determines whether the threshold color is reflected in the background color of the tile. In this example, there are two identical tiles, one with **Threshold background** turned off, and then the same tile with **Threshold background** turned on.

![Threshold background off (left) and on (right)](https://dt-cdn.net/images/single-value-threshold-background-off-on-609-c0be9c322d.png)

Threshold background off (left) and on (right)

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

The **Settings** section also displays visualization options per metric selected for the query.

### Rename a metric

You can change the name of a metric as it is displayed on the chart and in the chart legend. The query definition retains the metric's original name.

1. In the **Settings** section, select  for the metric you want to rename.
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

## Threshold

The **Threshold** section is one of the expandable sections in the right panel of Data Explorer. The contents of this section may vary depending on the visualization you have selected. Use threshold settings to enhance your visualizations and tiles.

![Data Explorer: Threshold section](https://dt-cdn.net/images/data-explorer-settings-threshold-323-3ddaf51ec3.png)

Data Explorer: Threshold section

Set threshold values after you set **Unit**:

* If you set **Unit** first, the threshold settings are prepared to match the selected unit.
* If you change **Unit** after you set threshold values, the threshold values are not automatically adjusted to match the new unit setting.

### Set thresholds

1. In the **Thresholds** section, enter threshold values

   ![Set threshold values](https://dt-cdn.net/images/threshold-definition-set-threshold-values-graph-249-e0895fe995.png)

   Set threshold values
2. Adjust threshold colors Optional

   ![Adjust the threshold colors](https://dt-cdn.net/images/threshold-definition-adjust-threshold-color-269-2e5d1f3fb4.png)

   Adjust the threshold colors

### Hide or show threshold colors

To hide or show threshold colors without deleting the threshold settings, in the **Thresholds** section, select .

![Hide or show thresholds](https://dt-cdn.net/images/threshold-definition-hide-or-show-graph-249-989dc64199.png)

Hide or show thresholds