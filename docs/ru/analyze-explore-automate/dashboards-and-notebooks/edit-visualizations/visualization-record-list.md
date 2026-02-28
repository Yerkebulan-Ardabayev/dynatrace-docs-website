---
title: Record list
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-record-list
scraped: 2026-02-28T21:21:02.129137
---

# Record list

# Record list

* Latest Dynatrace
* How-to guide
* 1-min read
* Updated on Jan 28, 2026

When to use a record list visualization

Use a record list visualization:

* When you want to see the actual records returned by the query at a glance.
* When you are interested in the structure of the records and how the field values are distributed.
* When you want to further explore the data via interactions.

![Record list example](https://dt-cdn.net/images/record-list-visualization-example-946-6f65d21f49.png)

Lists the records returned from the query. Some data has been obfuscated in the example.

## Record list interactions

### Field-specific

Select a field to display a menu of field-specific options. The available options might vary per field.

* **Copy field name** copies the field name of the selected field to the clipboard.
* **Explain value**âuse AI to explain the field.
* **Add command to query**âa section of field-specific commands that you can automatically add to your query, such as:

  + **Sort ascending** adds a command to your query to `sort <fieldname> asc`
  + **Sort descending** adds a command to your query to `sort <fieldname> desc`
  + **Summarize** counts how often each of the distinct values are present in the result (for example, counting how often each host ID is present).
  + **Extract fields**
* **Open with** passes the whole record to the **Open with** dialog, not taking into account which field you selected.

### Value-specific

Select a value to display a menu of value-specific options. The available options might vary per value type.

* **Copy value** copies the selected value to the clipboard. This menu item also displays the type of the selected value.
* **Explain value**âuse AI to explain the value.
* **View in fullscreen** applies only to strings. It displays the value in a fullscreen window.

  + and  navigate from record to record.
  + copies the current value to the clipboard.
  + closes the window and returns to the table.
* The **Add command to query** section of the menu lists related commands that you can automatically add to your query, such as:

  + **Less than**
  + **Less than or equal**
  + **Equal**
  + **Greater than**
  + **Greater than or equal**
  + **Not equal**
  + **Later than**
  + **Earlier than**
  + **Â±5 seconds**
  + **Extract fields**
  + **Add entity names** adds a lookup (result is added in a separate field called `dt.entity.<entity>.name`) of the actual entity name associated to a given entity ID.
  + **Expand**
  + **Reduce to single value** makes your results suitable for certain visualizations such as [Single value](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-chart-single-value "Create and edit single value visualizations on your Dynatrace dashboards and notebooks."), [Table](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-table "Create and edit table visualizations on your Dynatrace dashboards and notebooks."), or [Categorical bar chart](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-chart-bar-categorical "Create and edit categorical chart visualizations on your Dynatrace dashboards and notebooks.").

* A recommended appâfor example, ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **View Kubernetes workload**âmay be listed for quick access.
* **Open with** passes the whole record to the **Open with** dialog, not taking into account which value you selected.

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