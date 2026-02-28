---
title: Dot map visualization
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-map-dot
scraped: 2026-02-28T21:20:44.528318
---

# Dot map visualization

# Dot map visualization

* Latest Dynatrace
* How-to guide
* 5-min read
* Published Apr 03, 2025

Dashboards version 1.311+ Notebooks version 1.311+

When to use

Use a dot map to pinpoint locations and represent specific values. Examples include server locations and their performance metrics, and office locations and operational metrics, such as employee count or revenue generated.

## Examples

To try out an example

1. Create a DQL tile in ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** or a DQL section in ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.
2. Copy the example data and paste it into the DQL edit box.
3. Run it.
4. Select the visualization and experiment with the visualization settings.

### Example 1

![Dot map example: basic](https://dt-cdn.net/images/dot-01-964-dc5a30507f.png)

The map above is based on the following data.

```
data



record(geo.location.latitude = 51.509865, geo.location.longitude = -0.118092),  // London, UK



record(geo.location.latitude = 40.712776, geo.location.longitude = -74.005974),  // New York, USA



record(geo.location.latitude = 35.689487, geo.location.longitude = 139.691711),  // Tokyo, Japan



record(geo.location.latitude = -33.868820, geo.location.longitude = 151.209290),  // Sydney, Australia



record(geo.location.latitude = 48.856613, geo.location.longitude = 2.352222),  // Paris, France



record(geo.location.latitude = 55.755825, geo.location.longitude = 37.617298),  // Moscow, Russia



record(geo.location.latitude = 34.052235, geo.location.longitude = -118.243683),  // Los Angeles, USA



record(geo.location.latitude = 19.432608, geo.location.longitude = -99.133209),  // Mexico City, Mexico



record(geo.location.latitude = 39.904202, geo.location.longitude = 116.407394),  // Beijing, China



record(geo.location.latitude = 52.520008, geo.location.longitude = 13.404954)  // Berlin, Germany
```

### Example 2

![Dot map example: with an additional numerical field](https://dt-cdn.net/images/dot-02-965-a7456fb511.png)

The map above is based on the following data.

```
data



record(geo.location.latitude = 51.509865, geo.location.longitude = -0.118092, revenue = toLong(random() * 10000000)),



record(geo.location.latitude = 48.864716, geo.location.longitude = 2.349014, revenue = toLong(random() * 10000000)),



record(geo.location.latitude = 41.902782, geo.location.longitude = 12.496366, revenue = toLong(random() * 10000000)),



record(geo.location.latitude = 52.520008, geo.location.longitude = 13.404954, revenue = toLong(random() * 10000000)),



record(geo.location.latitude = 40.416775, geo.location.longitude = -3.70379, revenue = toLong(random() * 10000000)),



record(geo.location.latitude = 51.9225, geo.location.longitude = 4.47917, revenue = toLong(random() * 10000000)),



record(geo.location.latitude = 59.329323, geo.location.longitude = 18.068581, revenue = toLong(random() * 10000000)),



record(geo.location.latitude = 50.075538, geo.location.longitude = 14.4378, revenue = toLong(random() * 10000000)),



record(geo.location.latitude = 37.98381, geo.location.longitude = 23.727539, revenue = toLong(random() * 10000000)),



record(geo.location.latitude = 55.676098, geo.location.longitude = 12.568337, revenue = toLong(random() * 10000000))
```

Important visualization settings for this example include:

### Example 3

![Dot map example: with a bearing field](https://dt-cdn.net/images/dot-03-973-cfe4ef9ef4.png)

The map above is based on the following data.

```
data



record(geo.location.latitude = 51.509865, geo.location.longitude = -0.118092, bearing = toLong(random() * 1000 % 360)),



record(geo.location.latitude = 48.864716, geo.location.longitude = 2.349014, bearing = toLong(random() * 1000 % 360)),



record(geo.location.latitude = 41.902782, geo.location.longitude = 12.496366, bearing = toLong(random() * 1000 % 360)),



record(geo.location.latitude = 52.520008, geo.location.longitude = 13.404954, bearing = toLong(random() * 1000 % 360)),



record(geo.location.latitude = 40.416775, geo.location.longitude = -3.70379, bearing = toLong(random() * 1000 % 360)),



record(geo.location.latitude = 51.9225, geo.location.longitude = 4.47917, bearing = toLong(random() * 1000 % 360)),



record(geo.location.latitude = 59.329323, geo.location.longitude = 18.068581, bearing = toLong(random() * 1000 % 360)),



record(geo.location.latitude = 50.075538, geo.location.longitude = 14.4378, bearing = toLong(random() * 1000 % 360)),



record(geo.location.latitude = 37.98381, geo.location.longitude = 23.727539, bearing = toLong(random() * 1000 % 360)),



record(geo.location.latitude = 55.676098, geo.location.longitude = 12.568337, bearing = toLong(random() * 1000 % 360))
```

Important visualization settings for this example include:

### Example 4

![Dot map example: with a string value](https://dt-cdn.net/images/dot-04-974-9042627d71.png)

The map above is based on the following data.

```
data



record(geo.location.latitude = 51.509865, geo.location.longitude = -0.118092, Lab = "London"),



record(geo.location.latitude = 48.864716, geo.location.longitude = 2.349014, Lab = "Paris"),



record(geo.location.latitude = 41.902782, geo.location.longitude = 12.496366, Lab = "Rome"),



record(geo.location.latitude = 52.520008, geo.location.longitude = 13.404954, Lab = "Berlin"),



record(geo.location.latitude = 40.416775, geo.location.longitude = -3.70379, Lab = "Madrid"),



record(geo.location.latitude = 51.9225, geo.location.longitude = 4.47917, Lab = "Rotterdam"),



record(geo.location.latitude = 59.329323, geo.location.longitude = 18.068581, Lab = "Stockholm"),



record(geo.location.latitude = 50.075538, geo.location.longitude = 14.4378, Lab = "Prague"),



record(geo.location.latitude = 37.98381, geo.location.longitude = 23.727539, Lab = "Athens"),



record(geo.location.latitude = 55.676098, geo.location.longitude = 12.568337, Lab = "Copenhagen")
```

Important visualization settings for this example include:

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

## View

* **Default zoom**

  Set a default zoom level for the map by selecting one of the following options:

  + **Data**: Automatically adjusts the zoom level to fit all the data points within the map view.
  + **World**: Sets the zoom level to display the entire world.
  + **Custom**: Lets you specify the coordinates for the mapâs center and set a custom zoom level.
* **Show country regions**

  Turn this on to show region outlines within countries.

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

* **Latitude**: Select a value from your query to use for the latitude of each point on the map.
* **Longitude**: Select a value from your query to use for the longitude of each point on the map.
* **Radius value**: Select a value from your query to use for the radius of the bubble around each point on the map.
* **Color value**: Select a value from your query to use for the color of the bubble around each point on the map.

## Shape

* **Style**: Select the symbol to display at each mapped point.

  + **Shape**: Select a standard shape from the list.
  + **Icon**: Select an icon from the list.
  + **Emoji**: Add an emoji with key combination **WIN**+**.** or **Win**+**;** or a character.
* **Size**: Set the display size (in pixels) for each displayed symbol.
* **Bearing**: Set the angle at which data points in the map are visualized.

  + **Fixed**: A fixed angle (`0`-`360`) at which to rotate the symbol. For example, `0` would not rotate the symbol, while `180` would flip the symbol upside down.
  + **Data**: A value (`0`-`360`) mapped from your dataset. Select from a list.

## Legend and tooltip

* **Show custom fields**: To display custom fields (name and value) when you hover over a map area, turn on **Show custom fields** and select each custom field you want to display.
* **Show legend**: To display a map legend, turn on **Show legend** and select the legend **Position**:

  + **Auto**: Selects an appropriate location based on the map size and the available space.
  + **Bottom**: Displays a legend under the map.
  + **Right**: Displays a legend to the right of the map.
* **Text truncation**: Determines how to truncate text when the full text can't be displayed.

  + **Aâ¦**: Trim from the right end of the text (when the right end is less important)
  + **Aâ¦B**: Trim from the middle of the text (when the middle is less important)
  + **â¦B**: Trim from the left end of the text (when the left end is less important)
* **Min value**: Sets the minimum value in the data.

  + **Auto**: Automatically selects a suitable minimum based on data (`0` or min value).
  + **Custom**: Lets you set a custom minimum value.
* **Max value**: Sets the maximum value in the data.

  + **Auto**: Automatically selects a suitable maximum based on data (0 or max value). Custom let's you set a custom maximum value.
  + **Custom**: Lets you set a custom maximum value.

## Color

* **Bubble colors**

  Select how to color the bubbles:

  + **Color palette**: Displays all bubbles in a color shade from the selected color palette. The shade used for each bubble corresponds to the value of **Color value** in relation to the other areas.

    Example

    If the values of **Color value** returned by your query range from `0` to `100`

    - A bubble with a value near `0` has a color shade from near the right end of the palette.
    - A bubble with a value near `100` has a color shade from near the left end of the palette.
  + **Single-color**: Displays all bubbles in the same color. Select a color from the list or enter the hex code for the color.
  + **Custom colors**: Displays each bubble in a custom color defined by you.

    For each custom color you want to add

    1. Select  **Color**.
    2. Enter a value, operator, and color to use for that value and operator.

    Example

    Suppose you want to color bubbles by three levels of **Color value**:

    - Green if **Color value** is less than `4,000`
    - Yellow if **Color value** reaches or exceeds a threshold of `4,000`
    - Red if **Color value** reaches or exceeds a threshold of `5,000`

    To configure this

    - Select  **Color** and add a custom color row with the value `0`, operator `â¥`, and the desired shade of green. If **Color value** is `0` or higher, the bubble will be green.
    - Select  **Color** and add a custom color row with the value `4,000`, operator `â¥`, and the desired shade of yellow. If **Color value** is `4,000` or higher, the bubble will be yellow.
    - Select  **Color** and add a custom color row with the value `5,000`, operator `â¥`, and the desired shade of red. If **Color value** is `5,000` or higher, the bubble will be red.

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