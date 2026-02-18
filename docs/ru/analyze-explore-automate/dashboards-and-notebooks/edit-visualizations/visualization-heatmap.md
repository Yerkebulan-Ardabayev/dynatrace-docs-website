---
title: Heatmap visualization
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-heatmap
scraped: 2026-02-18T21:27:08.697234
---

# Heatmap visualization

# Heatmap visualization

* Latest Dynatrace
* How-to guide
* 2-min read
* Updated on Jun 17, 2025

When to use a heatmap visualization

The heatmap visualization offers a compact and flexible matrix visualization for visualizing aggregated datasets.

* When you want to identify patterns and outliers across metrics in large aggregated datasets
* When you want to correlate and compare time, numerical, and categorical-based metrics with one another

## Examples

### Example 1

![Heatmap example 1: Heatmap (Response time by service)](https://dt-cdn.net/images/heatmap-example-01-resp-705-31ffafba81.png)

The heatmap visualization above is based on the following query.

```
timeseries response_time = avg(dt.service.request.response_time), by: { dt.entity.service }



| fields response_time, entityName(dt.entity.service), interval, timeframe, dt.entity.service



| limit 10
```

### Example 2

![Heatmap example 2: Heatmap (Vulnerability score by event.status for Security events)](https://dt-cdn.net/images/heatmap-example-02-vuln-715-6e2f83a092.png)

The heatmap visualization above is based on the following query.

The query below has been updated to align with the new Grail security events table. For the complete list of updates and actions needed to accomplish the migration, follow the steps in the [Grail security table migration guide](/docs/secure/threat-observability/migration "Understand the changes in the new Grail security table and learn how to migrate to it.").

```
fetch security.events



| summarize count = count(), by:{range(vulnerability.risk.score, 0.5), event.status}
```

## Chart interactions

### Selection interactions

When you select a value on a chart and pin the displayed tooltip open, you can then hover over the tooltip to display a menu of selection-specific options.

The chart interactions available to you depend on your query and visualization. For example, if you select a host on a line chart and hover over the tooltip, you will see a menu of items such as:

* **Copy name**âcopy the name of the selected host.
* **Fields**âa section with a submenu for each query field. A field submenu offers field-specific options such as:

  + **Copy value**âcopy the value of the field. Also displays the field type.
  + **Hide**âhide the field in the chart.
  + **Explain value**âuse AI to explain the field.
  + **Add command to query**âa section of field-specific commands that you can automatically add to your query.
  + A recommended app may also be listed.
* **Visual options**âopens the edit panel so you can change visualization options for the selected item.
* **Set color**âopens the edit panel so you can change the color of the selected item.
* ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Go to host**âopens the selection in ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations**.

  In general, if there are recommended apps to open the selected item, the menu offers direct links to those apps, followed by an **Open with** option to select a different target app.
* **Open with**âfor details, see [Drilldowns and navigation](/docs/analyze-explore-automate/dashboards-and-notebooks/drilldowns-and-navigation "Drill down from Dashboards and Notebooks using links based on intents or URLs.").

## Title

Use the title field at the top of the options panel (initially `Untitled tile` or `Untitled section`) to add a title to your dashboard tile or notebook section.

* You can use emojis such as ð and ð and â¤ï¸.
* You can use variables.

**Example:**

1. Define variables called `Status` and `Emoji` in your dashboard.
2. Set the title to `Current $Emoji status is $Status`.
3. Set `Status` to `Good`.
4. Set `Emoji` to `ð`.

The title will be displayed as `Current ð status is Good`.

## Visualization

If you aren't sure that you chose the right visualization, use the [visualization selector](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations#select-visualization "Create, edit, and view visualizations on your Dynatrace dashboards and notebooks.") to try different visualizations.

To learn about options quickly and decide what works best for you, turn options on and off and see the effect immediately on your chart. For example, does it look best with a label or without? Turn that option on and off and see for yourself.

## Data mapping

The data mapping section shows how a column of your result is mapped to the visualization.

Expand for general rules on data mapping settings

Expand the  **Data mapping** section of your visualization settings to see how data in your result is mapped to your visualization, and to adjust those settings if needed.

* Mandatory fields are marked with an asterisk (`*`). Example:

  ![Example data mapping: line chart](https://dt-cdn.net/images/example-data-mapping-line-chart-1-732-eb9cca00d8.png)
* Data types are displayed next to field names in dropdowns and mapped fields.
* Units are displayed when thereâs only one assigned.
* Result fields are grouped into **Suitable** and **Unsuitable**. Fields are marked as unsuitable if they cannot be used to display data in the visualization. Example:

  ![Example data mapping: line chart, Time dropdown](https://dt-cdn.net/images/example-data-mapping-line-chart-2-763-9cc593d261.png)
* Automatic application of data mapping default settings:

  Dynatrace version 1.319+

  + Already existing tiles and sections are considered to be user-defined. Their data mapping configurations aren't updated automatically.
  + Newly created tiles and sections apply a data mapping setting by default. If you don't modify these settings manually, these settings might change if a new execution of the tile/section modifies the results and there are fields missing or new fields that better suit the data mapping.

### Visualization-specific data mapping settings

The heatmap data mapping section includes:

* **X-axis**: Select the value to use for the X-axis of your heatmap.

  + **Numeric**: Requires a nested start and end value, which is best achieved with the DQL `range` function together with the `summarize` command.
  + **Time**: Requires a nested start and end timestamp as well as an interval field. This is easiest achieved with the DQL `timeseries` or `makeTimeseries` command.
  + **String**: Requires at least one string value that can be mapped as a category. It can be achieved with the DQL `summarize` command together with a specific field to summarize by, or with the `by` command to specify the fields the series should be split by.
* **Interval**: displayed under **X-axis** if you select a timeframe for **X-axis**, this value is automatically mapped and canât be changed. It lets you know which fields are mapped for timeseries-based results. It takes the first available interval field from the result set whenever a timeseries is used (also includes any makeTimeseries-based data).
* **Y-axis**: Select the value to use for the Y-axis of your heatmap.

  + **Numeric**: Requires a nested start and end value, which is best achieved with the DQL `range` function together with the `summarize` command.
  + **Time**: Requires a nested start and end timestamp as well as an interval field. This is easiest achieved with the DQL `timeseries` or `makeTimeseries` command.
  + **String**: Requires at least one string value that can be mapped as a category. It can be achieved with the DQL `summarize` command together with a specific field to summarize by, or with the `by` command to specify the fields the series should be split by.
* **Interval**: displayed under **Y-axis** if you select a timeframe for **Y-axis**, this value is automatically mapped and canât be changed. It lets you know which fields are mapped for timeseries-based results. It takes the first available interval field from the result set whenever a timeseries is used (also includes any makeTimeseries-based data).
* **Value field**: Select the value (numerical or string field) to display on your heatmap.

## X-axis

These settings determine the appearance of your heatmap's X-axis.

* **Show label**: turn it on to define a label for the X-axis.
* **Reverse**: turn it on to reverse the direction of the X-axis.
* **Position**: select where you want to display the X-axis in relation to your heatmap.
* **Tick label layout**: select whether to display the X-axis values horizontally or vertically.

## Y-axis

These settings determine the appearance of your heatmap's Y-axis.

* **Show label**: turn it on to define a label for the Y-axis.
* **Reverse**: turn it on to reverse the direction of the Y-axis.
* **Position**: select where you want to display the Y-axis in relation to your heatmap.

## Legend and tooltip

* **Show legend**: To display a heatmap legend, turn on **Show legend** and select the legend **Position**:

  + **Auto**: Selects an appropriate location based on the heatmap size and the available space.
  + **Bottom**: Displays a legend under the heatmap.
  + **Right**: Displays a legend to the right of the heatmap.
* **Text truncation**: Determines how to truncate text when the full text can't be displayed.

  + **Aâ¦**: Trim from the right end of the text (when the right end is less important)
  + **Aâ¦B**: Trim from the middle of the text (when the middle is less important)
  + **â¦B**: Trim from the left end of the text (when the left end is less important)

## Color



These settings determine how color is used in your heatmap.

* **Color palette**: Displays colors from the selected color palette.
* **Custom colors**: Displays colors defined by you.

  For each custom color you want to add

  1. Select  **Color**.
  2. Enter a value, operator, and color to use for that value and operator.

## Units and formats

To override the default units and formats in a dashboard or notebook visualization

1. Select  to edit the visualization tile.
2. Select the **Visual** tab.
3. Select **Units and formats**.
4. Select **Override**.
5. Select  **Override**
6. In the dropdown list, select the item for which you want to add a unit override.

   This is a numeric column of the underlying DQL result, so it varies according to the query. For example:

   * A `fetch events` query returns events. The dropdown list here lets you select a numeric field (such as `transfer_size`) from the results.
   * A `timeseries avg(dt.host.cpu.usage)` query returns a single timeseries for `avg(dt.host.cpu.usage)`. That timeseries is then the only selectable option in the list.
7. Define the override.

   * **Default unit**: The base unit in which the values were captured. It's `None` if it was not included in the DQL result, or its automatically defined by the unit passed from the DQL result. This field doesn't lead to any conversion.
   * **Displayed unit**: Once you define a default unit, you can use **Displayed unit** for conversion. For example, if the DQL result defined your numeric value in the result as `Bytes`, **Displayed unit** now offers a suitable list of byte conversions such as `Kilobyte` and `Megabyte`. Unlike the **Default unit**, the **Displayed unit** is always a numeric conversion.
   * **Decimals** displays the default number of decimals (degree of precision) to display. To see it in action, change the **Decimals** selection and observe the change in the visualization.
   * **Suffix** displays the suffix to display after the unit. To see it in action, enter a string and observe the change in the visualization. When you don't find the unit you're looking for, you can use **Suffix** to display the desired unit.
8. Turn on **Abbreviate large numbers** if you want to display large figures in abbreviated form. For example, `1053` becomes `1.1K`.

To reset to defaults (discard override settings for the selected item), select the trash can  next to the item.

Example for dashboards

This example uses a line chart, but the options apply to other visualizations.

1. In ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, create a dashboard.
2. Select  and, in the **Snippets** section of the menu, select **Metrics** > **Chart average CPU across all hosts**.
3. In the section edit panel, select the **Visual** tab and select **Line**.
4. Select **Units and formats**.

   ![Select Units and formats](https://dt-cdn.net/images/units-example-proc-01-1450-635695f6b8.png)
5. Select  **Override**.

   ![Select Add Override.](https://dt-cdn.net/images/units-example-proc-02-1450-e1805870b1.png)
6. In the dropdown list, select the metric for which you want to add an override. There's only one metric to select in this example.
7. Define the override for the displayed metric. You can observe your changes in the Y-axis of the chart.

   * **Default unit** displays `Percent (%)`, which is the default unit for the selected metric. Try a different setting, such as `One` to instead display the result as a fraction of 1.
   * **Displayed unit** displays `Auto`. You can change it to a different unit, such as `One` to instead display the result as a fraction of 1.

     Only linear and static conversions are supported. For example, you cannot convert `Degree Celsius(Â°C)` into `Degree Fahrenheit(Â°F)`, or convert `Usd(US$)` into `Eur(â¬)`.
   * **Decimals** displays the default number of decimal points (degree of precision) to display. To see it in action, change the **Decimals** selection and observe the change in the visualization.

     For example, change this:

     ![Decimals setting before](https://dt-cdn.net/images/units-example-proc-03-1454-6a84518802.png)

     To this:

     ![Decimals setting after](https://dt-cdn.net/images/units-example-proc-04-1450-03cc893027.png)
   * **Suffix** displays the optional suffix to display after the unit. To see it in action, enter a string and observe the change in the visualization.

To reset to defaults (discard override settings for the selected metric), select the trash can  next to the metric.