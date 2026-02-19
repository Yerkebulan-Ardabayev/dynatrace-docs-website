---
title: Table visualization
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-table
scraped: 2026-02-19T21:16:09.460974
---

# Table visualization

# Table visualization

* Latest Dynatrace
* How-to guide
* 5-min read
* Updated on Sep 24, 2025

When to use a table visualization

Use the table visualization:

* When you want to get a first sample and impression of the data returned by your query or code. For example, show me the top recent 100 log lines for my application or host.
* When you want to go through many records at a time. Where data density and being able to compare records one by one is more important than seeing all fields that are contained in the result at the same time.
* When you need to further explore the data via interactions.

## Example

![Example table visualization](https://dt-cdn.net/images/table-example-01a-776-2528f83012.png)

The table above is based on the following query.

```
timeseries cpu=avg(dt.host.cpu.usage), by:{dt.entity.host}



| sort arrayAvg(cpu), direction:"descending"



| limit 3
```

* The title is set to **Chart average CPU across all hosts**.
* The visualization type is set to **Table**.
* In the  **Columns** section:

  + **Visibility and order**: select **Edit**  to configure visible columns and their order. In the example, the `dt.entity.host` column is not selected (to hide the host names) and the other three columns (`timeframe`, `interval`, and `cpu`) are selected.
  + **Custom column types**: the `cpu` column (a timeseries) is set to  **Sparkline**.

## Table interactions

### Table-specific

Left-click a column header to locally sort the results by that column.

* indicates unsorted
* indicates that the table is sorted ascending by that column
* indicates that the table is sorted descending by that column

### Column-specific

Right-click a column header, or hover over the column header and select , to display a menu of column-specific commands. The available options might vary per column.

* **Move left** moves the selected column one position to the left.
* **Move right** moves the selected column one position to the right.
* **Hide column** hides the selected column. To display a hidden column again, edit the table and, in the  **Columns** section, edit  the **Visibility and order** settings to configure visible columns and their order.
* **Enable line wrap** and  **Disable line wrap** specify whether to wrap text in the selected column.
* **Copy field name** copies the field name of the selected column to the clipboard.
* The **Add command to query** section of the menu lists related command that you can automatically add to your query, such as:

  + **Sort ascending** adds a command to your query to `sort <fieldname> asc`
  + **Sort descending** adds a command to your query to `sort <fieldname> desc`
* **Summarize** counts how often each of the distinct values in a certain column are present in the result (for example, counting how often each host ID is present).
* **Add entity names** adds a lookup (result is added in a separate field called `dt.entity.<entity>.name`) of the actual entity name associated to a given entity ID in a table column.
* **Convert to histogram** associates given numeric values to histogram bins and how often values fall into each bin.

### Row-specific

Left-click anywhere in a row to select the entire row. With a row selected, you can then left-click and drag within a cell in that row to select exactly what you want to copy (**Ctrl**+**C**) from the cell.

### Cell-specific

Right-click a cell, or hover over the cell and select , to display a menu of cell-specific commands. The available options might vary per cell.

* **Copy value** copies the value in the cell to your clipboard.
* **View in fullscreen** applies only to strings. It displays the cell content in a fullscreen window.

  + and  navigate from record to record.
  + copies the current value to the clipboard.
  + closes the window and returns to the table.
* A recommended appâfor example, ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **View Kubernetes workload**âmay be listed for quick access.
* **Open with** passes the whole record to the **Open with** dialog, not taking into account which field you selected. This results in a broader range of possible **Open with** options.
* The **Add command to query** section of the cell menu lists commands that you can automatically add to your query, such as:

  + to filter the query results by the selected cell and the corresponding operator (for example, **Greater than** the cell value).
  + **Add entity names** adds a lookup (result is added in a separate field called `dt.entity.<entity>.name`) of the actual entity name associated to a given entity ID.

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

## Columns

* **Visibility and order**: select **Edit**  to configure visible columns and their order.

  When you download table data to a file (select  > **Download result** > **CSV**), the download includes only the columns selected here.

  This is useful when, for example, you want to download a CSV file, open it in a spreadsheet, and share the spreadsheet with others, but you want to exclude irrelevant or sensitive data from your download.
* **Line wrap**: Specifies whether to wrap lines that extend beyond the column width.

  + **All**: Applies line wrap to all table columns.
  + **Custom**: Applies line wrap to selected table columns.
* **Monospaced font**: Specifies whetherr to use a monospaced font.

  + **All**: Applies monospaced font to all table columns.
  + **Custom**: Applies monospaced font to selected table columns.
* **Custom column types**: Specifies formatting for columns. Select  **Column type** to add a row, and then select one or more columns and how you want to format the selected columns.

Table results

If a table result contains more than 50 columns, your result will only show the first 50 columns. If your result is larger than 50, you'll see a warning informing you of this. The warning will allow you to **Modify visibility**, where you can select which columns should be displayed and change the order of how they're displayed.

## Cells

* **Density**âdetermines how compact the table rows are displayed vertically.

  + **Condensed** is the tightest display option, for when you need to maximize the number of rows displayed.
  + **Default** is an average display option, with typical spacing between rows.
  + **Comfortable** specifies maximum spacing between rows.
* **Apply threshold color to**

  + **Value** applies the threshold color to the value displayed by the cell.
  + **Background** applies the threshold color to the background of the cell.
* **Show threshold in row** applies the threshold color to the entire row.

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