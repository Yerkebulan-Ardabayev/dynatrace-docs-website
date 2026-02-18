---
title: Drilldowns and navigation
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/drilldowns-and-navigation
scraped: 2026-02-18T21:17:22.328471
---

# Drilldowns and navigation

# Drilldowns and navigation

* Latest Dynatrace
* How-to guide
* 1-min read
* Updated on Jan 26, 2026

This document explains how to create and use drilldown links based on intents or URLs in ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** or ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**. Drilldown links allow you to navigate across dashboards, notebooks, Dynatrace apps, or external systems while preserving context.

The following options simplify workflows by enabling deeper analysis with just a few clicks, making it easy to investigate issues or explore related data directly from visualizations. In the following, we will leverage and go through use cases to explain the concepts and show how to set things up.

## Use cases

You can drill into related data within Dynatrace or in external systems by passing relevant context. Depending on your use case, you can choose to pass context automatically (using **Open with** based on [intentsï»¿](https://dt-url.net/intents)) or manually (via custom links to dashboards or external systems).

### Automatic context passing: explore details in Dynatrace apps

Use **automated context passing** to investigate data quickly, without needing manual configuration.

For example:

* Investigate log lines to identify patterns.
* Examine traces or spans to pinpoint issues.
* View detailed host information.

**Options for automated context passing**:

* [Open with](#open-with) opens the selected item in another Dynatrace app.
* [Suggested apps](#suggested-app-links) are suggested Dynatrace app links added to the menu automatically based on the item you selected.

### Manual context passing: Link to external systems or dashboards

Use **manual context passing** if you need to link to external tools or manually configure dashboard or notebook drilldowns.

For example:

* **Link to external systems**: Integrate with tools like ServiceNow, Jira, or GitHub by passing relevant IDsâsuch as a ServiceNow incident or Jira issue IDâinto the link.
* **Link to another dashboard or notebook**: Link an overview dashboard (for example, one showing multiple services) to a detailed one that focuses on a single service or application.

**Options for manual context passing**:

* [Link from the visualization menu via custom UI-based links](#visualization-custom-ui-based-link)
* [Link from a table via a markdown column](#table-markdown-column)

URL format determines whether to open a new tab

When using these options to link to another dashboard or notebook, the URL format you choose determines whether to open the target in a new tab:

* To open the target in a new tab, use:  
  `https://<your-environment>/ui/[dashboards|notebooks]/...`  
  (be sure to replace `<your-environment>`)
* To open the target in the same tab, start your link with:  
  `/ui/[dashboards|notebooks]/...`  
  (without `https://<your-environment>`)

## Open with

To navigate between apps in the Dynatrace platform, you can use **Open with** while preserving context, such as the selected timeframe, entities, or filters. When you select **Open with**, a window displays a list of actions you can perform in other apps. The available actions depend on whether the target app can work with the data (fields) provided by the source app and which apps are installed in your environment.

You can use **Open with** at different levels, such as for a section in a notebook, a tile in a dashboard, or even a specific data point or its underlying fields. The further down you goâfrom tile to data point, or from data point to its underlying fieldsâthe more specific the context becomes, meaning fewer fields are passed to the target app.

For example, if you select a row in a table that contains a `dt.smartscape.host` field (`host ID`), and then select **Open with**, you will see a **Go to Host** option. This is because the target app, the ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations** app, can handle the `dt.smartscape.host` field.

If you're developing Dynatrace apps, see [Intentsï»¿](https://dt-url.net/intents) for everything you need to know about passing the user flow from one app to another.

### General usage

To use **Open with** with a tile or section

1. In your dashboard or notebook, select the tiles or sections you want to use in another app. You can select multiple items simultaneously if needed.
2. Open the  menu and select  **Open with**.
3. In the **Open with** window, choose an action provided by an app to navigate to while preserving context.

   The app opens, processing the context (fields) passed from the tiles or sections. What happens next depends on the action and how the app uses the data.

### Examples

The following are just a few common ways people use **Open with** to pass information between Dynatrace apps.

Notebook to dashboard

To copy a notebook section to a dashboard (as a dashboard tile)

1. In the notebook, select the notebook section that you want to copy to a dashboard.
2. Open the  menu and select ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Add to dashboard**.
3. In **Select destination**:

   * If you want to create a new dashboard with the selected notebook section as a tile, select **New dashboard**.
   * If you want to add the selected notebook section as another tile in an existing dashboard, select the existing dashboard from the list and then select **Confirm**.

   The dashboard opens with the selected section copied into it as a dashboard tile.

To copy a notebook section to a different app (not ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**), open the  menu and select  **Open with**, and then select the target app.

Dashboard to notebook

To copy a dashboard tile to a notebook (as a notebook section)

1. In the dashboard, select the tile that you want to copy to a notebook.
2. Open the  menu and select ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Add to notebook**.
3. In **Select destination**:

   * If you want to create a new notebook with the selected dashboard tile as a section, select **New notebook**.
   * If you want to add the selected dashboard tile as another section in an existing notebook, select the existing notebook from the list and then select **Confirm**.

   The notebook opens with the selected tile copied into it as a notebook section.

To copy a dashboard tile to a different app (not ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**), open the  menu and select  **Open with**, and then select the target app.

Dashboard Grail query to workflow

To copy a Grail query from a dashboard to [![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.") as a task in a workflow

1. In the dashboard, select the query tile that you want to copy to a workflow.
2. Select  >  **Open with**.
3. In the **Open with** window, select the **Automate DQL Query** ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** option.

   ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** opens with the selected query added as a workflow task.
4. Edit the workflow as needed.

## Suggested app links

Suggested app links are an extension of [Open with](#open-with) added to streamline your workflow. Based on the data of your tiles/sections and the data point or fields in your selection, Dynatrace automatically identifies the most relevant action and app combination and adds it directly to the respective menu.

For example, when there is a host ID field in the data, you will see the **Go to Host** option above the **Open with** in the menu.

## Link from visualization via custom links

The **Add Link** feature allows you to create links in the UI directly from your visualizations and navigate to external systems, dashboards, notebooks, or other resources. With it you can:

* Add links from the **visualization menu**, enabling quick setup without leaving the visualization.
* Manage links in the **Links section** of the visualization tab, where you can:

  + Add new links.
  + Edit or remove existing links.
  + Reorder links, with changes reflected in the visualization menu.

### Add and manage links



The  **Add Link** feature allows you to create links directly from your visualizations. These links can navigate to external systems, other Dynatrace apps, or resources, enabling seamless context passing for faster troubleshooting and analysis.

#### Add a link

1. Open the  **Links** section in the visualization tab of your selected visualization.
2. Select  to open **Add link**.
3. Configure the link:

   * **Name**: Enter a descriptive name such as "Go to Host" to display in the menu.
   * **Icon**: Select an icon such as "Logs" to represent the link in the menu.
   * **URL**: Use [dynamic placeholders](#dynamic-placeholders) to insert data fields or variables. For example, select  **Insert placeholder** and add the `:name` placeholder to the your URL like `https://myhost/host={{:name}}`
   * Use the **Preview** section at the bottom to see how placeholders will be replaced with actual data and to test your link.
4. Select **Add link** to save. The link will now appear in the visualization's tooltip menu.

#### Manage links

Use the **Links** section to manage and organize your links:

* **Edit**: To update an existing link, select it (or select  **Edit** in the  menu) or simply select the name.
* **Duplicate**: To copy an existing link, select  **Duplicate** in the  menu.
* **Remove**: To delete a link, select it and choose  **Delete** in the  menu.
* **Reorder**: Adjust the display order of links by dragging  their definitions up or down in the list in the  **Links** section.

### Use dynamic placeholders

Dynamic placeholders allow you to create links that adapt to the data in your visualization. They dynamically populate URLs with context-aware data, such as time ranges, metric values, or entities like hosts.

Depending on your use case, you can use one of three types of placeholders:

1. **Data point** placeholders dynamically resolve values based on the specific data point being clicked. These placeholders are especially useful in time-based or segmented visualizations. The following placeholders are available out of the box:

   * `:name`: The name of the data point (for example, the series name in a line chart, typically displayed in the legend).
   * `:value`: The value of the data point (for example, the value at the point clicked on a line chart).
   * `:from`: The start timestamp of the time slot the value represents (for time-based visualizations).
   * `:to`: The end timestamp of the time slot the value represents.

   **Example:**
   In a line chart segmented by host, selecting on a specific data point could resolve the `:name` placeholder to the host name and the `:value` placeholder to the metric value at that point in time.
2. **Existing variables** let you reference existing variables defined in your dashboard.

   **Example:**  
   Use `$variableName` to pass a user-selected value into the link.
3. **Existing fields** allow you to reference the full set of data returned in the visualizationâs result. Unlike Data point placeholders, which represent a single point of data, Existing Fields provide access to the entire dataset (for example, all points in a series or all column values in a table).

   **Example:**  
   If a metric query returns an array of values, you can use a field placeholder to reference the entire array.

To use placeholders in your links:

Start typing `{{` when editing a **URL** to display a menu of placeholder suggestions:

* `{{`: Displays all available placeholders.
* `{{$`: Displays existing variables.
* `{{:`: Displays all data point placholders.

Alternatively, select  **Insert placeholder** to choose placeholders from a dropdown menu.

### Encoding links and placeholder values

To prevent errors, encoding ensures your URLs work correctly when they include special characters, such as spaces, ampersands, or reserved characters.
Neither the static parts of your links nor the dynamic placeholders are encoded automatically, so you need to handle encoding manually to avoid issues.

#### Static parts of the URL

Static parts of the URL must be manually encoded if they include special characters. For example, replace spaces with `%20`, ampersands `&` with `%26`, and other reserved characters as needed.

Use a free tool like [URL Encoder/Decoderï»¿](https://www.url-encode-decode.com/) to encode your static URLs before pasting them into the URL field.

#### Dynamic placeholders

Dynamic placeholders are not automatically encoded. If your placeholder values may contain special characters, you can use Dynatrace Query Language (DQL) functions to encode them properly. Commonly used DQL functions include:

* `encodeUrl()`: Encodes the entire URL.
* `escape()`: Escapes reserved characters.
* `replaceString()`: Replaces specific characters (for example, converting `+` to `%20`).

**Example:** Encoding a log field to ensure itâs URL-safe:

```
fetch logs



| summarize occurences=count(), by:{content}



| fieldsAdd contentEncoded = replaceString(escape(encodeUrl(content)), "+", "%20")



| fields contentEncoded, occurences
```

### Supported visualizations and link behavior

* **Table**

  + Links are visible for each column, enabling interaction with individual data points while leveraging others. For example, selecting a link in the `Status` column might use another field's value when navigating.
* **Unsupported visualizations**

  + Map visualizations such as [Choropleth](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-map-choropleth "Create and edit choropleth map visualizations on your Dynatrace dashboards and notebooks."), [Dot](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-map-dot "Create and edit dot map visualizations on your Dynatrace dashboards and notebooks."), [Connection](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-map-connection "Create and edit connection map visualizations on your Dynatrace dashboards and notebooks."), and [Bubble](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-map-bubble "Create and edit bubble map visualizations on your Dynatrace dashboards and notebooks.")
  + [Single value](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-chart-single-value "Create and edit single value visualizations on your Dynatrace dashboards and notebooks.")
  + [Gauge chart](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-gauge "Create and edit gauge visualizations on your Dynatrace dashboards and notebooks.")
  + [Meter bar chart](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-meterbar "Create and edit meter bar visualizations on your Dynatrace dashboards and notebooks.")
* **All other visualizations**

  + For visualizations with data splits (for example, line charts by host), links dynamically adjust based on the data series. For example, using the placeholder `{{:name}}` in a line chart segmented by host will replace the placeholder with the respective host name for each series (line).

## Link from table via a markdown column

Tables in Dynatrace provide a powerful way to display data and include clickable links for seamless navigation. Links in tables can be added in three levels of complexity:

1. [Basic: auto-detected raw links](#table-auto-detected-links): automatically display raw URLs as clickable links.
2. [Intermediate: links with a display name](#table-user-friendly-links): Use markdown column formatting to rename links for better readability.
3. [Advanced: intent-based links](#table-intent-based-links): Use Dynatrace Query Language (DQL) to dynamically create [intentï»¿](https://dt-url.net/intents)-based links with encoded parameters for advanced navigation to other apps in Dynatrace.

The following steps walk you through these levels of complexity using a single example that builds progressively.

### Basic: auto-detected, raw links

Dynatrace automatically detects URLs in table cells and renders them as clickable links when the column type of the cell is set to **Markdown**.

To enable link detection:

1. Start with a **Table Visualization** in Dynatrace.
2. Go to the **Visual** tab.
3. In the **Columns** section, select  **Column type** to add a new column type. Select the column with the raw links and set the column type to **Markdown**.

   **Example:**
   Hereâs a simple dataset with URLs that you can try on the [Dynatrace playgroundï»¿](https://wkf10640.apps.dynatrace.com/ui/apps/dynatrace.dashboards/dashboard/35295fb4-3d3d-4919-994d-3f8869cab1b7#from=2026-01-21T14%3A19%3A00.000Z&to=2026-01-21T16%3A20%3A00.000Z&tileIds=27):

   ```
   data record(website="Dynatrace main page", link="http://www.dynatrace.com"),



   record(website="Dynatrace community", link="https://community.dynatrace.com/")
   ```

### Intermediate: links with a display name



To make links more user-friendly, you can provide a display name (for example, "Dynatrace main page") using Markdown formatting. This replaces raw URLs with descriptive labels that are easier for users to read and understand.

To provide user-friendly links:

1. Adjust your DQL to create a new column that formats links in Markdown syntax.

   * Use the `fieldsAdd` function to generate a composite field, for example, `markdownLink`, in the format `[Display Name](URL)`.
   * Use the DQL `concat()` function to easily construct such a field (see the following example).
2. Go to the **Visual** tab.
3. In the **Columns** section, select  **Column type** to add a new column type. Select the column with the raw links and set the column type to **Markdown**. For example, `markdownLink`.

   **Example:**:
   Hereâs a the dataset with URLs and the markdown notation that you can try on the [Dynatrace playgroundï»¿](https://wkf10640.apps.dynatrace.com/ui/apps/dynatrace.dashboards/dashboard/35295fb4-3d3d-4919-994d-3f8869cab1b7#from=2026-01-21T14%3A19%3A00.000Z&to=2026-01-21T16%3A20%3A00.000Z&tileIds=27):

   ```
   data record(website="Dynatrace main page", link="http://www.dynatrace.com"),



   record(website="Dynatrace community", link="https://community.dynatrace.com/")



   | fieldsAdd markdownLink = concat("[", website, "](", link, ")")
   ```

### Advanced: intent-based links

Intent-based links take link creation to the next level by dynamically passing context (such as error codes, timeframes, or other filters) to other Dynatrace applications for advanced workflows. This is done using **Dynatrace Query Language (DQL)** and proper URL encoding to handle special characters.

In this section, weâll walk through generating dynamic intent-based links step by step using DQL. The resulting links will include:

* A **user-friendly display name**, constructed in Markdown format.
* **Dynamic parameters**, such as error codes and timeframes, to tailor the link for downstream navigation.
* Proper **encoding of special characters** in URL query parameters.

To create intent-based links

1. **Fetch the base data**

   Use DQL to fetch the relevant dataset and filter content as needed. For example, you can retrieve logs matching specific error codes:

   ```
   fetch logs



   | filter matchesPhrase(content, "failed to complete the order: rpc error: code") and status == "ERROR"



   | parse content, """DATA 'desc = ' LD:errorCode '    '"""



   | summarize total = count(), by:{errorCode}
   ```
2. **Add the base URL of the target app**

   Define the base URL of the Dynatrace app youâre linking to. In this case, weâre linking logs to the ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs** app:

   ```
   | fieldsAdd LogAppURL = "/ui/apps/dynatrace.logs/#"
   ```
3. **Encode the query components**

   To create a proper intent-based link, use the encodeUrl() function to encode each part of the URL. Break the query into components for clarity.

   1. Query filter: Filter the logs matching specific error codes:

      ```
      | fieldsAdd QueryPart1 = """{"version":0,"data":{"queryConfig":{"query":"fetch logs\n| filter matchesPhrase(content,\"\"\""""



      | fieldsAdd QueryPart1 = encodeUrl(QueryPart1)



      | fieldsAdd QueryPart1 = replaceString(QueryPart1, "+", "%20")
      ```
   2. Dynamic field value: Encode the error codes dynamically:

      ```
      | fieldsAdd QueryPart2 = escape(errorCode)



      | fieldsAdd QueryPart2 = encodeUrl(QueryPart2)



      | fieldsAdd QueryPart2 = replaceString(QueryPart2, "+", "%20")
      ```
   3. Timeframe: Encode the dashboardâs timeframe:

      ```
      | fieldsAdd QueryTimeFrame = """\"\"\") ","timeframe":{"from":$dt_timeframe_from,"to":$dt_timeframe_to},"filter":{"version":"12.2.4","subQueries":[{"id":"A","isEnabled":true,"datatype":"logs","filter":""}],"globalCommands":{"sort":{"field":"timestamp","direction":"desc"}}},"segments":[],"showDqlEditor":true},"tableConfig":{"visibleColumns":["timestamp","status","content"],"columnAttributes":{"columnWidths":{},"lineWraps":{},"tableLineWrap":false},"columnOrder":["timestamp","status","content"]}}}"""
      ```
   4. Create the final link. Combine the base URL, the query components, and Markdown formatting into a user-friendly link:

      ```
      | fieldsAdd errorCodeLink = concat("[", errorCode, "](", LogAppURL, QueryPart1, QueryPart2, QueryTimeFrame, ")")



      | fields errorCodeLink, total
      ```

Try the full example on the [Dynatrace playgroundï»¿](https://wkf10640.apps.dynatrace.com/ui/apps/dynatrace.dashboards/dashboard/35295fb4-3d3d-4919-994d-3f8869cab1b7#from=2026-01-21T14%3A19%3A00.000Z&to=2026-01-21T16%3A20%3A00.000Z&tileIds=22).