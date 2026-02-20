---
title: Categorical chart visualization
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-chart-bar-categorical
scraped: 2026-02-20T21:09:54.080443
---

# Categorical chart visualization

# Categorical chart visualization

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Jul 08, 2022

When to use a categorical bar chart visualization

Use a categorical bar chart:

* When you want to group your data according to defined categories and compare their aggregated values rather than see them over time. It's particularly useful when you have more than five distinct categories, where a pie or donut visualization becomes insufficient to compare the different proportions.
* When you have frequency or count data for distinct categories. For example, requests by response code, errors by error type, or log lines by status.

## Example

![Categorical bar chart](https://dt-cdn.net/images/categorical-bar-chart-841-fb2d9e3530.png)

The above categorical bar chart is based on the following query.

```
fetch logs



| summarize count(), by:{loglevel}
```

In the **Categorical bar chart options** section, **Category axis label** is set to `loglevel` to show the label on the X-axis.

This categorical bar chart shows the values on the vertical axis and the categories along the horizontal axis.

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

For a categorical bar chart, the data mapping section includes:

* **Values**: the value (numerical) to display. If multiple values are listed, you can select more than one at a time.
* **Categories**: the column of your result that is displayed as the category.

## Categorical chart options

To learn about options quickly and decide what works best for you, turn options on and off and see the effect immediately on your chart. For example, does it look best with a label or without? Turn that option on and off and see for yourself.

### Axes

* **Category axis label**
* **Value axis label**
* **Min** and **Max**
* **Relative values**

### General

* **Color mode**âselect multi-color or single-color mode.
* **Color palettes**âselect a color palette from the list.
* **Legend position**âselect where to display the visualization legend:

  + **Automatic**âDynatrace chooses an appropriate location
  + **Hidden**âno legend is displayed
  + **Bottom**âthe legend is displayed along the bottom of the visualization
  + **Right**âthe legend is displayed on the right side of the visualization
* **Vertical layout**âDetermines the orientation of the chart:

  + **Horizontal**âthe bars are oriented horizontally, from left to right
  + **Vertical**âthe bars are oriented vertically, from bottom to top
* **Category tick label layout**âspecifies the orientation of the category tick labels:

  + **Horizontal**âthe category tick labels are oriented horizontally, from left to right
  + **Vertical**âthe category tick labels are oriented vertically, from bottom to top

### Overrides

* **Category colors**âto override a category color, select from the list.

## Query limits

Use the **Query limits** section to check and adjust the Grail query limits per notebook section or dashboard tile. These settings determine the maximum limits when fetching data. Exceeding any limit will generate a warning.

Dashboard tiles and notebook sections created in Dynatrace earlier than version 1.296 are not affected. Those existing tiles/sections will return the same results as before.

* **Read data limit (GB)**

  The limit in gigabytes for the amount of data that will be scanned during a read.
* **Record limit**

  The maximum number of result records that this query will return. Default: 1,000 records. To see more records, you need to increase the value of **Record limit**.

  + If your query has no `limit`, such as

    ```
    fetch logs
    ```

    the value of **Record limit** is applied. By default, you will see up to 1,000 records.
  + If your query also includes a `limit`, such as

    ```
    fetch logs



    | limit 2000
    ```

    the lower of the two values (either `limit` in your query, or **Record limit** in the web UI) is applied.

    In the example above, you would still see only 1,000 records unless you increased the value of **Record limit**.
* **Result size limit**

  The maximum number of result bytes that this query will return. For better performance with typical queries and smaller documents, the default is set to 1 MB.
* **Sampling (Logs and Spans only)**

  Results in the selection of a subset of Log or Span records.

## Thresholds

### Configure thresholds

To configure thresholds in a dashboard or notebook visualization

1. Select  to edit the visualization tile.
2. Select **Thresholds**.

   * In ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, select the **Visual** tab in the side panel, and then select **Thresholds**.
   * In ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, select **Thresholds** in the side panel.
3. Select  **Threshold**.
4. Define the thresholds. For each range:

   * Select a color to display for that range
   * Select the operator to define the threshold for that range
   * Enter a static value to compare (using the selected operator) with the returned value
   * Enter a label to associate with the defined range.

     + Labels apply only to charts with a Y axis, such as timeseries charts and the categorical bar chart.
     + Labels can't be defined for tables and the single value chart.

Example threshold settings in Dashboards

This example uses a bar chart, but the options apply to other visualizations.

1. In ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, create a dashboard.
2. Select  and, in the **Snippets** section of the menu, select **Metrics** > **Chart top 10 hosts by CPU usage**.
3. In the section edit panel, select the **Visual** tab and select **Bar**.
4. Select **Thresholds**.
5. Select  **Threshold**.

   An empty set of threshold fields is displayed.
6. Define the thresholds for the displayed metric. You can observe your changes in the Y axis of the chart.

   In this example, we define three ranges of CPU usage with corresponding colors and labels.

   You can see the ranges displayed on the Y-axis and in the tooltip.

To reset to defaults (discard threshold settings), select the trash can  next to the item.

### Edit thresholds

1. Select  to edit the visualization tile.
2. Select **Thresholds**.

   * In ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, select the **Visual** tab in the side panel, and then select **Thresholds**.
   * In ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, select **Thresholds** in the side panel.
3. From this point, you can do the following (expand rows for details):

   Add thresholds

   To add thresholds (if the selected visualization supports additional thresholds), select  **Threshold**.

   Turn off thresholds

   To turn off (hide) existing thresholds, use the switch. No settings are lost. You can turn them back on if you change your mind.

   Delete thresholds

   To delete existing thresholds, select the trash can .

   Edit threshold settings

   To change existing threshold settings, just edit the fields.

   Add a range

   To add a range to existing thresholds, select  **Add range**.

   Delete a range

   To delete a range from existing thresholds, select the delete button in that row.

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