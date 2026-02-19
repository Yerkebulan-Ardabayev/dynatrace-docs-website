---
title: Raw visualization
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-raw
scraped: 2026-02-19T21:16:44.740745
---

# Raw visualization

# Raw visualization

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jul 08, 2022

Select the **Raw** visualization to see the actual data returned by the query (rather than a visualization of the data).

![Raw visualization example](https://dt-cdn.net/images/raw-example-812-8a1234b934.png)

The raw data visualization above is based on the following query. Some data has been obfuscated.

```
timeseries avg=avg(dt.host.cpu.load),



max=max(dt.host.cpu.load),



min=min(dt.host.cpu.load),



by:dt.entity.host



| limit 1
```

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