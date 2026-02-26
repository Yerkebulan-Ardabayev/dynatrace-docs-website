---
title: Scatterplot visualization
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-scatterplot
scraped: 2026-02-26T21:30:46.832653
---

# Scatterplot visualization

# Scatterplot visualization

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Oct 24, 2025

When to use a scatterplot visualization

Use the scatterplot visualization when you want to:

* **Identify relationships, correlations, or patterns between two continuous variables.**

  For example, to see if thereâs a correlation between the number of users on your platform and the response time of your application.
* **Visualize the distribution of data points.**

  For example, to observe how requests are distributed across different response time ranges.
* **Detect outliers or anomalies in your data.**

  For example, to identify requests with unusually high durations compared to others.

## Examples

### Example 1

![Scatterplot example: "Scatterplot (CPU and memory usage)"](https://dt-cdn.net/images/scatterplot-example-01-813-d8505fceb4.png)

The scatterplot visualization above is based on the following query.

```
timeseries { cpu.usage = avg(dt.host.cpu.usage, scalar: true), memory.usage = avg(dt.host.memory.usage, scalar: true) }, union: TRUE, by: { dt.entity.host }



| fieldsAdd dt.entity.host.name = entityName(dt.entity.host)



| fields dt.entity.host, dt.entity.host.name, cpu.usage, memory.usage



| limit 1000
```

### Example 2

![Scatterplot example: "Scatterplot (Service latency and throughput)"](https://dt-cdn.net/images/scatterplot-example-02-814-571d34c416.png)

The scatterplot visualization above is based on the following query.

```
timeseries {service.response.time = avg(dt.service.request.response_time, scalar: true), service.response.count = sum(dt.service.request.count, scalar: true)}, union: TRUE, by: { dt.entity.service }



| fieldsAdd dt.entity.service.name = entityName(dt.entity.service)



| fields dt.entity.service.name, dt.entity.service, service.response.count, service.response.time



| limit 1000
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

The scatterplot data mapping section includes:

* **X-axis**: Select the value to use for the X-axis of your scatterplot. Suitable values are Timeframe, Numerical (Double and Long), Categorical (String and Boolean).
* **Y-axis**: Select the value to use for the Y-axis of your scatterplot. Suitable values are Numerical (Double and Long), Categorical (String and Boolean).
* **Names**: The elements displayed, for example, in the legend and series names. Suitable fields are Categorical (String and Boolean), Numerical (Double and Long), or Field name.

Possible X/Y combinations are:

| X-axis | Y-axis |
| --- | --- |
| Timeframe | Array |
| Numerical | Numerical |
| Numerical | Categorical |
| Categorical | Categorical |
| Categorical | Numerical |

**Notes**:

* Timeframe is only supported in the X-axis and is the combination of Timestamp + Duration.
* Timestamp is considered a numerical type.

## X-axis

These settings determine the appearance of your scatterplot's X-axis.

* **Show label**: turn it on to define a label for the X-axis.
* **Reverse**: turn it on to reverse the direction of the X-axis.
* **Position**: select where you want to display the X-axis in relation to your scatterplot.
* **Min value**:

  + **Auto** selects a suitable minimum based on data (0 or min value)
  + **Min value** sets to the minimum value in the data
  + **Custom** lets you set a manual minimum value
* **Max value**:

  + **Auto** selects a suitable maximum based on data (0 or max value)
  + **Max value** sets to the maximum value in the data
  + **Custom** lets you set a manual maximum value
* **Tick label layout**: select whether to display the X-axis values horizontally or vertically.

## Y-axis

These settings determine the appearance of your scatterplot's Y-axis.

* **Show label**: turn it on to define a label for the Y-axis.
* **Reverse**: turn it on to reverse the direction of the Y-axis.
* **Position**: select where you want to display the Y-axis in relation to your scatterplot.
* **Min value**:

  + **Auto** selects a suitable minimum based on data (0 or min value)
  + **Min value** sets to the minimum value in the data
  + **Custom** lets you set a manual minimum value
* **Max value**:

  + **Auto** selects a suitable maximum based on data (0 or max value)
  + **Max value** sets to the maximum value in the data
  + **Custom** lets you set a manual maximum value

## Legend and tooltip

* **Show legend**: To display a scatterplot legend, turn on **Show legend** and select the legend **Position**:

  + **Auto**: Selects an appropriate location based on the scatterplot size and the available space.
  + **Bottom**: Displays a legend under the scatterplot.
  + **Right**: Displays a legend to the right of the scatterplot.
* **Text truncation**: Determines how to truncate text when the full text can't be displayed.

  + **Aâ¦**: Trim from the right end of the text (when the right end is less important)
  + **Aâ¦B**: Trim from the middle of the text (when the middle is less important)
  + **â¦B**: Trim from the left end of the text (when the left end is less important)

## Color

These settings determine how color is used in your scatterplot.

* **Color palette**: Displays colors from the selected color palette.
* **Custom**: Displays colors defined by you.

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