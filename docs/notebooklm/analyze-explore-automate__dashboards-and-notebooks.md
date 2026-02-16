# Dynatrace Documentation: analyze-explore-automate/dashboards-and-notebooks

Generated: 2026-02-16

Files combined: 36

---


## Source: dashboard-component-code.md


---
title: Add code to a dashboard
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-code
scraped: 2026-02-16T21:12:21.521840
---

# Add code to a dashboard

# Add code to a dashboard

* Latest Dynatrace
* How-to guide
* 10-min read
* Published Jul 08, 2022

Use a code tile to run JavaScript that can:

* Fetch external data via APIs
* Combine external data with your query results
* Map code results to your visualizations

## Add code

To add code to a dashboard

1. In the upper-right of the dashboard, select  **Add** >  **Code**.

   Keyboard shortcut: **Shift**+**C**

   ![Dashboards: Add tile button (Plus)](https://dt-cdn.net/images/updated-dashboards-add-tile-button-481-c21ba8f200.png)

   An empty tile is added to the dashboard and an **Options** side panel opens on the right.
2. Optional In **Tile title**, enter a title to display at the top of your tile.
3. In the numbered **Code** box, enter custom JavaScript to fetch external data from any available API. Use the [Fetch APIï»¿](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) to fetch data from external APIs.

   To make sure your requests aren't blocked, ask your administrator to allow your external data sources by adding them to the **External requests**.

   External requests enable outbound network connections from your Dynatrace environment to external services. They allow you to control access to public endpoints from the AppEngine with app functions and functions in Dashboards, Notebooks, and Automations.

   1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** >  **General** > **External requests**.
   2. Select  **New host pattern**.
   3. Add the domain names.
   4. Select **Add**.

   This way you can granularly control the web services your functions can connect to.

   Don't include the address prefix. For example, if the address is `https://some.service.org`, just add `some.service.org`.

## Run code warnings

When you open a document from another user, you may see the following message:

`This dashboard contains custom code. It is read-only until you review the code and select âAccept and runâ.`

When you run a code tile or section written by another person, Dynatrace executes the other person's JavaScript using your user account and your permissions. This is a powerful feature, but it needs to be used correctly and responsibly. The JavaScript code can access external APIs on your behalf (using your account and permissions).

To review code

1. Select **Review all code**.

   The **Review code** page displays each code tile's code in a separate box.
2. Review the code and decide whether you want to run it.

   If you want to run the code, you can approve it just this time or permanently.

   * To run the code just this time, select **Accept and run**. The next time you open this document, you will be asked once again to review the code before running it.
   * To permanently accept the code in this document, select **Always trust code in this document** and then select **Accept and run**.

## Example 1: Simple request and response to Table

In this simple example, we leverage the [dummyjson.comï»¿](https://dummyjson.com/docs/products) API to retrieve sample product data.
The result of this API call is multiple sample products in JSON format. By adding `.products` to the result, we can pass it directly to a [table](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-table "Create and edit table visualizations on your Dynatrace dashboards and notebooks.") visualization.

![Add code - example 1](https://dt-cdn.net/images/screenshot-2023-04-28-at-10-09-03-3352-8ebe772088.png)

```
export default async function () {



const url = "https://dummyjson.com/products";



const response = await fetch(url);



const result = await response.json();



return result.products;



}
```

## Example 2: Simple request and response to Single value

In this example, we build on example 1 by calculating the average price for all sample products and pass it to a [single value](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-chart-single-value "Create and edit single value visualizations on your Dynatrace dashboards and notebooks.") visualization.

![Add code - example 2](https://dt-cdn.net/images/screenshot-2023-04-28-at-11-38-07-3356-ca95b247f3.png)

```
export default async function () {



const url = "https://dummyjson.com/products";



const response = await fetch(url);



const result = await response.json();



let avgPrice = 0;



const numberOfProducts = result.products.length;



for (let i = 0; i < numberOfProducts; i++) {



avgPrice = avgPrice + 1;



}



return avgPrice;



}
```

## Example 3: Advanced request and response to Record list

In this example, we use the Dynatrace [Environment API](/docs/dynatrace-api/environment-api "Find out what you need to use the environment section of the Dynatrace API.") to retrieve events and create a table visualization.

![Add code - example 3](https://dt-cdn.net/images/screenshot-2023-04-28-at-14-02-51-3358-99746f6f57.webp)

```
export default async function () {



const environment = "https://{your-environment}"



const token = "<DYNATRACE_TOKEN_PLACEHOLDER>";



const params = '/api/v2/events?status("OPEN")';



const uri = environment + params;



const response = await fetch(uri, {



headers: {



Accept: "application/json",



Authorization: "Api-Token " + token



}});



const result = await response.json();



return result.events;



}
```

## More examples

To see more examples, open the  menu at the top of your dashboard and browse the snippets under **Code**.

![Add code - more examples](https://dt-cdn.net/images/screenshot-2023-04-28-at-14-04-13-3360-7569f80292.webp)


---


## Source: dashboard-component-data.md


---
title: Add data to a dashboard
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-data
scraped: 2026-02-16T21:12:37.372973
---

# Add data to a dashboard

# Add data to a dashboard

* Latest Dynatrace
* How-to guide
* 10-min read
* Updated on May 27, 2025

This page describes how to add data with a Grail query, and how to specify a custom timeframe and a segment.

The fastest and easiest way to explore your data is with our new [Explore](/docs/analyze-explore-automate/dashboards-and-notebooks/explore-data "Explore your data with our point-and-click interface.") tiles and sections. In a few seconds, you can find and analyze your logs, metrics, or business events. No DQL required!

Deprecated: `dt.entity.*` fields

If you see the following message:

`The dt.entity.* fields are deprecated. Please use dt.smartscape.* fields instead.`

we recommend that you use an equivalent `dt.smartscape.*` field instead.

The deprecated `dt.entity.*` fields will eventually be removed.

## Add data

To Query Grail

1. In the upper-right of the dashboard, select  **Add** >  **DQL**.

   Keyboard shortcut: **Shift**+**D**

   ![Dashboards: Add tile button (Plus)](https://dt-cdn.net/images/updated-dashboards-add-tile-button-481-c21ba8f200.png)

   A configuration side panel opens on the right to display two tabs:

   * **Data**
   * **Visual**
2. On the **Data** tab, use the [Dynatrace Query Language (DQL)](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") to define your query.
3. Select **Run** to execute the query.
4. On the **Visual** tab, choose a [visualization](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations "Create, edit, and view visualizations on your Dynatrace dashboards and notebooks.") format for your results.

   * means the visualization type is unavailable for your query.
5. Under the **Visualization** selector, expand the options sections to adjust visualization settings as needed.
6. Close the side panel when you're done.

   If you want to return to these settings, select your tile to display them.

## Specify a custom timeframe

To specify a custom timeframe in a dashboard tile

1. Edit the tile.
2. In the edit panel, turn on **Custom timeframe**.
3. Select the timeframe to apply to the selected tile.

   This timeframe overrides the dashboard timeframe set in the upper-right corner of the dashboard. Using this method, a dashboard can have multiple tiles, where each tile has its own timeframe.

You can also specify a custom timeframe in a data tile's DQL query. If you use this method (with a timeframe specified in the query), the above UI setting is disabled and the timeframe specified in the query is used.

Example timeframe specification in DQL:

```
fetch [recordtype], from:now() - 2h



| ....
```

For details on specifying a timeframe in DQL, see [Specify timeframe](/docs/platform/grail/dynatrace-query-language/dql-guide#specifytimeframe "Find out how DQL works and what are DQL key concepts.") in the DQL documentation.

## Select segments

To filter data, you can specify segments at two levels: dashboard and tile. Tile-level segment selections override dashboard-level segment selections.

Should I use segments or variables?

#### Segments

Use segments when you want to reuse them across dashboards. For example, use segments for recurring filters such as for your Kubernetes clusters, namespaces, workloads, or pods. Segments automatically apply on top of the queries of your tiles/sections, so you donât need to reference them within.

#### Variables

If you need more control over how a filter is applied, however, you might want to use variables.

* Variables allow you to fully control the underlying query or within your Explore section or tile, determining where and how they are applied. For example, you can specify how they connect with other filters applied (**AND**, **OR**) and you can control which operator is used for your filter (such as `equals`, `contains`, `startsWith`, and `endsWith`).
* Additionally, use variables when you need fine-grained control over how filters are interdependent.

* For details on segments, see [Segments](/docs/manage/segments "Segments logically structure monitoring data in Grail and function as convenient filters for data that users are allowed to access based on permissions.")
* For a ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**-specific segments use case, see [Analyze monitoring data with segments](/docs/manage/segments/getting-started/segments-getting-started-analyze-monitoring-data "Learn how to analyze monitoring data more efficiently by using segments in Dashboards.")

To select tile-level segments

1. Display the dashboard.
2. Select the tile and then select  in the tile controls to edit the tile.
3. In the edit panel, turn on **Custom segments**.
4. In the **Custom segments** list, select a segment.  
   If the segment requires an additional value selection, select it now.
5. To add another segment, select  **Segment**. Repeat this step for each segment you want to add for the selected tile.
6. Select **Apply** to apply the selection and filter data on the tile.

   * The segment selector  now displays the name of the selected segment or, if you select more than one segment, the number of selected segments.
   * To change your segment selection, select  again, make your changes, and select **Apply**.
   * To manage segments in general (list, create, view, edit, delete), select  and then select the **Manage segments** link.

## Data example 1

```
fetch logs



| summarize loglines = count(), by:{`1m interval` = bin(timestamp, 1m), status}
```

## Data example 2

### Create two variables

In case you haven't created a variable yet, first see [Add a variable to a dashboard](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-variable#add-a-variable "Add variables to your Dynatrace dashboards.").

1. Select **Add variable** and define the first variable.

   * **Name:** `Hosts`
   * **Type:** `Query`
   * **Query:**

     ```
     fetch logs



     | summarize count(), by:{`dt.entity.host`}



     | limit 100



     | sort `count()`, direction:"descending"



     | fields `dt.entity.host`
     ```
   * **Multi-select:** turned on
2. Select **Add variable** and define the second variable.

   * **Name:** `Loglevel`
   * **Type:** `Query`
   * **Query:**

     ```
     fetch logs, from:now() - 2h



     | summarize  count(), by:{loglevel}



     | sort `count()`, direction:"descending"



     | fields loglevel
     ```
   * **Multi-select:** turned on

### Add data

Now add data while referencing your previously created variables `$LogLevel` and `$Hosts` so that you can later use the variable filters on top of your dashboard to filter the tile according to your selections.

```
fetch logs



| filter in (loglevel, {$Loglevel})



| limit 10
```

Select **Run query**.


---


## Source: dashboard-component-markdown.md


---
title: Add Markdown to dashboard
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-markdown
scraped: 2026-02-16T21:12:36.018305
---

# Add Markdown to dashboard

# Add Markdown to dashboard

* Latest Dynatrace
* How-to guide
* 10-min read
* Published Jul 08, 2022

A Markdown tile can be anything from a minor note about something on the dashboard to a whole page of formatted information with links and pictures.

## Add a Markdown tile

To add a markdown tile to a dashboard

1. In the upper-right of the dashboard, open the  **Add** menu and select  **Add markdown**.

   Keyboard shortcut: **Shift**+**M**

   ![Dashboards: Add tile button (Plus)](https://dt-cdn.net/images/updated-dashboards-add-tile-button-481-c21ba8f200.png)

   An **Options** side panel opens on the right.
2. In the **Options** side panel, enter your text.

   * Use Markdown to format your text and add links and images.
   * The tile is updated as you edit.
   * While you're editing text, press Ctrl+Space to see options.
3. Close the **Options** side panel when you're done.

## Syntax

Use Markdown to format your annotations.

While you're typing in the edit box, your Markdown is rendered in the tile.

Press Ctrl+Space on an empty line to pop up a selectable list of available Markdown elements.

![How to edit a Markdown tile](https://dt-cdn.net/images/markdown-editing-1105-1fc4ba5612.png)

### Italics

Wrap text in single asterisks (`*like this*`) to get italics *like this*.

### Bold

Wrap text in double asterisks (`**like this**`) to get bold text **like this**.

### Strikethrough

Wrap text in double tildes (~~like this~~) to get strikethrough (crossed out) text ~~like this~~.

### Blockquote

Start a line with `>` to get blockquotes, where everything before you press Enter is quoted.

### Code

* Wrap text in backticks (`like this`) to get bold text `like this`.
* Wrap text in triple backticks (```like this```) to show a code block (multiple lines of `code text`).

### Headings

To add a heading, start the line with the `#` character like this: `# This is your heading text`.

### Horizontal line

To visually separate sections of your annotation, add a horizontal line with three dashes (`---`):

### Lists

Each line of an unordered (bulleted) list starts with an asterisk (`*`):

```
* Line 1



* Line 2
```

Alternatively, you can use a dash (`-`):

```
- Line 1



- Line 2
```

An ordered (numbered) list starts with a number and a period (`1.`) followed by a space and then your text:

```
1. The first line of my procedure.



2. The second line of my procedure.



3. The third line of my procedure.
```

If you use `1.` for each line number, the lines are renumbered automatically when you display the dashboard.

### Tables

To add a table, define the headers, the column formatting row, and then the rows of data you want to display

```
| Header 1 | Header2



--- | ---



content2 | content2
```

| Header 1 | Header2 |
| --- | --- |
| content2 | content2 |

### Special characters

You can use any printable characters, including emojis such as ð and ð and â¤ï¸.

### Links

You can link to other places in your dashboard and elsewhere.

A link in Markdown is a label and link of the form `[label](address)`, where:

* The `label` is freeform text to display on the link in your Markdown tile or section
* The `address` specifies what to open when someone selects the link, such as a website or a Dynatrace app

Link to

Syntax and examples

Website

```
[My label](https://www.example.com/)
```

Notebooks app

```
[My label](/ui/apps/dynatrace.notebooks/notebooks)
```

Specific notebook

**Syntax**:

```
[label](/ui/apps/dynatrace.notebooks/notebook/<notebookid>)
```

**Example**:

```
[My label](/ui/apps/dynatrace.notebooks/notebook/274edae4-dfe8-41fb-aced-5020fb1270bc)
```

To get the address

1. Display the target notebook.
2. Copy everything on the browser address line starting from `/ui/`.
3. Paste it into your Markdown as the address of a link.

Specific notebook section

**Syntax**:

```
[label](/ui/apps/dynatrace.notebooks/notebook/<notebookid>#<sectionid>)
```

**Example**:

```
[My label](/ui/apps/dynatrace.notebooks/notebook/274edae4-dfe8-41fb-aced-5020fb1270bc#cb69caf1-52ed-4e73-8a3e-120e8cd7e8f8)
```

To get the address

1. Display the target notebook.
2. Select the target section of the notebook.
3. Copy everything on the browser address line starting from `/ui/`.
4. Paste it into your Markdown as the address of a link.

Dashboards app

```
[My label](/ui/apps/dynatrace.dashboards/)
```

Specific dashboard

**Syntax**:

```
[label](/ui/apps/dynatrace.dashboards/<dashboardid>)
```

**Example**:

```
[My label](/ui/apps/dynatrace.dashboards/dashboard/9f24c36e-ca5f-401c-8e00-5e4b05c46bd2)
```

To get the address

1. Display the target dashboard.
2. Copy everything on the browser address line starting from `/ui/`.
3. Paste it into your Markdown as the address of a link.

Specific dashboard tile

**Syntax**:

```
[label](/ui/apps/dynatrace.dashboards/dashboard/<dashboardid>#tileIds=n)
```

**Example**:

```
[My label](/ui/apps/dynatrace.dashboards/dashboard/9f24c36e-ca5f-401c-8e00-5e4b05c46bd2#from=now%28%29-2h&to=now%28%29&tileIds=6)
```

To include a specific tile ID in the link

1. Display the target dashboard.
2. Select the target tile in the target dashboard.
3. Copy everything on the browser address line starting from `/ui/`.
4. Paste it into your Markdown as the address of a link.

### Images

To link to a picture, use this format:

`![alternate text](https://www.example.com/file-name.jpg)`

```
Here are some of the people who started [Dynatrace](https://www.dynatrace.com).



![Dynatrace founders](https://dt-cdn.net/images/original-dynatrace-team-1500-7334dbe9a8.jpg)
```

### Variables

To reference a [variable](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-variable "Add variables to your Dynatrace dashboards.") in an annotation, use the variable name prefixed by a `$` character. For example:

```
The status is $Status.
```

If the dashboard has a variable named `Status` and the current value of `Status` is `Good`, the above example would appear in your tile as "The status is Good." and it would be updated when the value of `Status` changes.

For details on variables, see [Add a variable to a dashboard](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-variable "Add variables to your Dynatrace dashboards.").


---


## Source: dashboard-component-snippet.md


---
title: Add a snippet to a dashboard
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-snippet
scraped: 2026-02-16T21:12:33.146537
---

# Add a snippet to a dashboard

# Add a snippet to a dashboard

* Latest Dynatrace
* How-to guide
* 10-min read
* Published Jul 08, 2022

Several data and code snippets are available out of the box. Use our predefined DQL or code snippets to quickly start your data analytics journey.

## Select a snippet

To get started based on a snippet

1. In the upper-right of the dashboard, select  **Add** to open the **Add** menu.

   Keyboard shortcut: **Ctrl**/**Cmd**+**Shift**+**Enter**

   ![Dashboards: Add tile button (Plus)](https://dt-cdn.net/images/updated-dashboards-add-tile-button-481-c21ba8f200.png)
2. Scroll down to the **Start with a snippet** section and choose one of the snippets. In this example, we select the  **Fetch logs** snippet, which is displayed in a preview panel.

   ![Example: select the "Fetch logs" snippet.](https://dt-cdn.net/images/add-snippet-menu-example-fetch-logs-754-d4435c09eb.png)
3. After you select a snippet, the edit panel displays the snippet you added.

   ![Example: "Fetch logs" snippet added.](https://dt-cdn.net/images/add-snippet-menu-example-fetch-logs-result-1436-77cc9fa8f1.png)
4. Edit the query or code (depending on the snippet type you selected) and the visualization settings as needed.
5. Select **Run** to see results.
6. Close the side panel when you're done.

## Examples

### Fetch logs

1. In ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, select  **Dashboard** to create a new dashboard.
2. In the upper-right of the dashboard, select  **Add** to open the add menu.

   ![Dashboards: Add tile button (Plus)](https://dt-cdn.net/images/updated-dashboards-add-tile-button-481-c21ba8f200.png)
3. In the menu, scroll down to the **Start with a snippet** section of the menu and select  **Fetch logs**.

That's it. You have created a dashboard with a DQL tile that fetches the 100 latest logs and displays them starting with the most recent.

![Example snippet: Fetch logs](https://dt-cdn.net/images/example-snippet-fetch-logs-1335-7f23a8343c.png)

The DQL behind your tile is the snippet you selected with  **Fetch logs**:

```
fetch logs



| sort timestamp desc



| limit 100
```

The DQL commands are run in order:

1. `fetch logs` gets the log data
2. `sort timestamp desc` sorts the data by timestamp in descending order
3. `limit 100` limits the results to the 100.

### Pie (Top 5 events by kind)

1. In ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, select  **Dashboard** to create a new dashboard.
2. In the upper-right of the dashboard, select  **Add** to open the add menu.

   ![Dashboards: Add tile button (Plus)](https://dt-cdn.net/images/updated-dashboards-add-tile-button-481-c21ba8f200.png)
3. In the menu, scroll down to the **Start with a snippet** section of the menu and select  **Pie (Top 5 events by kind)**.

This one creates a tile based on the following DQL:

```
fetch events



| summarize `event count`=count(), by:{event.kind}



| limit 5
```

The results are displayed as a pie chart.

![Example snippet: Pie (Top 5 events by kind)](https://dt-cdn.net/images/example-snippet-pie-top-five-events-1004-a42b6a2b21.png)

## What's next

The list of available snippets is long and growing. Create a new dashboard and try them out.

When you find something interesting:

* Inspect it to see how it works
* See if you can tweak and adapt it to your own purposes


---


## Source: dashboard-component-variable.md


---
title: Add a variable to a dashboard
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-variable
scraped: 2026-02-16T21:12:31.805843
---

# Add a variable to a dashboard

# Add a variable to a dashboard

* Latest Dynatrace
* How-to guide
* 10-min read
* Updated on Sep 02, 2025

Use variables to filter your dashboards, to act as variable values in code tiles, and as placeholders in tile titles and Markdown tile text.

Deprecated: `dt.entity.*` fields

If you see the following message:

`The dt.entity.* fields are deprecated. Please use dt.smartscape.* fields instead.`

we recommend that you use an equivalent `dt.smartscape.*` field instead.

The deprecated `dt.entity.*` fields will eventually be removed.

## Add a variable

To add a variable to a dashboard

1. In the dashboard header, open the  menu and select  **Variables**.
   Keyboard shortcut: **Shift**+**V**

   Keyboard shortcut: **Shift**+**V**

   ![Dashboards: Add tile button (Plus)](https://dt-cdn.net/images/updated-dashboards-add-tile-button-481-c21ba8f200.png)

   The **Variable** panel is displayed.
2. Define the variable.

   * **Name**: the name of the variable.

     + Only alpha-numerical values are allowed
     + Do not start a variable name with `dt_`
   * **Type**: can be one of the following:

     + **DQL**: the value is returned from a query you enter when you define the variable.

       - Select **Run** to test your query.
     + **Code**: the value is returned from code you enter when you define the variable.
     + **List**: a comma-separated values (CSV) list of values.

       - To define possible values, enter them (separated by commas) in the box under **Data**.
       - To define a default value, select one from the **Default value** list.
       - To allow multiple values to be selected at the same time, turn on **Multi-select**.
     + **Free Text**: free text. You can enter a **Default value**.
       Your changes are saved automatically.
3. Set **Display settings**.

   * If the variable dropdown should be displayed on the dashboard, turn on **Display as filter on dashboard**.  
     Turn it off when you want it hidden, such as when the variable is used as a static value across tiles but should not be displayed to the dashboard user.
   * If users should be able to select multiple values at the same time within the variable dropdown, turn on **Multi-select**.  
     Turn it off when you want to use only single values of the variable dropdown.
   * Select a **Default value** for the variable dropdown. If you don't enter anything in this field, the first available value is selected.
4. When you're finished, select **< Variable** at the top to go to the **Variables** panel, or select  to dismiss the **Variables** panel.

Variables in dashboards can be defined to depend on other variables.

* The value of a variable is recalculated if its definition refers to another variable and the other variable's value changes.

  For example, if the value of variable A changes, the value of any variable whose definition refers to variable A is recalculated.
* Loops are not allowed.

  For example, if the value of variable A depends on the value of variable B, the value of variable B can't depend on the value of variable A.

How you edit a variable depends on the **Type**. For details and examples, see:

* [DQL variable](#define-variable-dql)
* [List variable](#define-variable-list)
* [Code variable](#define-variable-code)
* [Free Text variable](#define-variable-free-text)

## Use a variable

After you create a variable, you're ready to use it in a query.

Always remember to prepend a variable name with `$` in your queries.

For example, if you create a variable named `MyTotal`, you need to refer to it as `$MyTotal` in your query.

For example:

1. Open the  menu and select  **Variables** to add a variable to your dashboard.
2. Define the following variable:

   * **Name**: `Host`
   * **Type**: DQL
   * **Query**:

     ```
     fetch dt.entity.host



     | fields entity.name
     ```
3. Turn on **Multi-select** so you can select more than one value at a time to show in your visualizations.

   Your changes are saved automatically.
4. Select  to dismiss the **Variable** panel.

### Use with a DQL tile

1. Open the  menu and select  **DQL**.
2. Copy and paste the following query into the  **DQL** box and select  **Run**.

   Note that the query refers to our new `Host` variable as `$Host`, with the dollar sign indicating that it's a variable name.

   ```
   fetch logs, scanLimitGBytes: 20



   | filter in(host.name, array($Host))



   | makeTimeseries count(), by:{ host.name }
   ```

   or when not using a multi-select variable you can reference it like

   ```
   fetch logs, scanLimitGBytes: 20



   | filter host.name == $Host



   | makeTimeseries count(), by:{ host.name }
   ```
3. Because you added a multi-select variable, you can use the value selector to determine which values are displayed in your visualizations.
4. You can of course use your variable in multiple queries.

### Use with an Explore tile

To use a variable in an [Explore data](/docs/analyze-explore-automate/dashboards-and-notebooks/explore-data "Explore your data with our point-and-click interface.") tile

1. Open the  menu and select **Logs**.
2. Select  and then select **host.name** from the **Available filters**.
3. In the added filter field, type `$` to get suggestions for all available variables and then select `$Host`.

Note: Adding variables in Explore tiles only works for single-select variables in combination with the **=** operator.

## List variables

To list all variables, do one of the following:

* Open the  menu and select  **All variables**.  
  Note that this menu is available only after you add at least one variable to a dashboard.

  ![Dashboards: example: variables on a dashboard](https://dt-cdn.net/images/variables-controls-602-78ff9fa615.png)

  In this example, four variables are defined for the dashboardâ`LogLevels`, `MyFreeTextVariable`, `Variable1`, and `Variable2`âand we can see their current values under their names.
* Select the  settings icon in the upper-right corner of the dashboard, and then select  **Variables**.

**Example**:

![Dashboards: example: variables list](https://dt-cdn.net/images/variables-list-738-5c887c7243.png)

In the above example:

* Four variables are defined for the dashboardâ`LogLevels`, `MyFreeTextVariable`, `Variable1`, and `Variable2`.
* Two of the variablesâ`Variable1` and `Variable2`âdisplay a  warning icon. For details, see the [Troubleshoot variables](#troubleshoot) section.

From here, you have the following variable-specific options:

* To review or change a variable definition, select its name.
* To add a variable, select  **Variable**.
* To hide or display a variable, select .
* To move a variable up or down the list, select  and drag the variable to a new position in the list.
* To see other variable-specific optionsâ**Edit**, **Duplicate**, **Move up**, **Move down**, and **Delete**âopen the  menu.

## Reset variables

To apply default values to variables, open the  menu and select  **Reset to default**.

This sets all variables to the default values specified in the variable configuration.

## Edit a variable

1. Open the  menu and select  **All variables**.
2. In the **Name** column, select the name of the variable that you want to edit.
3. Edit and verify the variable.  
   How you edit a variable depends on the **Type**. For details and examples, see:

   * [DQL variable](#define-variable-dql)
   * [List variable](#define-variable-list)
   * [Code variable](#define-variable-code)
   * [Free Text variable](#define-variable-free-text)
4. Select  to dismiss the **Variables** panel.

## Delete a variable

To delete a variable from a dashboard

1. Open the  menu and select **All variables**.
2. Find the variable you want to delete in the **Name** column, open the  menu for that row, and select  **Delete**.
3. Select  to dismiss the **Variables** panel.

## Change variable values

If a dashboard has one or more variables, they are listed by name along the upper-left of the dashboard, under the dashboard name. When you change variable values, the dashboard contents are recalculated and displayed according to the new values.

To change the value of a variable

1. In the upper-left of the dashboard, locate the variable name.
2. Use the menu or edit box under the variable name to change the value.

   * If the variable allows just one selection (value) at a time, select the value that you want to apply to the dashboard.
   * If the variable allows multiple selections (values) at a time, select the checkbox for each value you want to apply to the dashboard. The menu name for that variable shows how many values are selected.
   * For a Free Text variable, you can edit the text in the box under the variable name.

## Change variable order

To change the order of variables in your dashboard

1. Open the  menu and select  **All variables**.
2. Drag the variables into the order you want.

   Alternative: open the  menu for the variable you want to move and select  **Move up** or  **Move down**

## Variable types

### DQL variable

To define a DQL variable

1. Set **Name** the name you want to give your variable.

   * It will be displayed at the top of the dashboard, listed on the **Variables** panel, and referred to in code.
   * It can contain only letters (uppercase or lowercase) and numbers (for example, `status`, `myHosts`, or `Variable01`) and it can't start with `dt_`.
2. Set **Type** to `DQL`.
3. In **Data**, enter a query. Be sure to use [`summarize`](/docs/platform/grail/dynatrace-query-language/commands/aggregation-commands#summarize "DQL aggregation commands") and [`collectDistinct`](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#collectDistinct "A list of DQL aggregation functions.") to get distinct values from data sources such as logs.
4. Select **Run** and inspect the results in the **Preview** section to make sure it works as expected.
5. If you want to be able to select more than one value at a time, turn on **Multi-select**.

If you add both examples below to your dashboard, you can filter your dashboard by host and log severity level. Be sure to turn on **Multi-select** if you want to select more than one at a time.

#### Example DQL variable

* **Name:** Hosts
* **Type:** DQL
* **Definition:**

  ```
  fetch dt.entity.host



  | fields id
  ```

If you want to use a human-readable name, use `| fields entity.name` instead of `| fields id`.

#### Variable replacement

In DQL tiles, you have four options for wrapping a variable value and how the variable placeholder is replaced before the query is executed. These options apply only to DQL tiles and are ignored for Code and Markdown tiles.

$varName

default

If you don't specify a strategy (for example, `$varName`), the variable value is wrapped in doublequote (`"`) characters. This is useful for strings such as entity names or categories.

* Any quotes inside the variables are escaped and ignored
* To escape a doublequote character, use a double backslash:

  ```
  \\"
  ```

For example, for a service named `PaymentBackend`, in a DQL query where we filter for this service, with the default strategy, we would replace the variable placeholder after the `=` on the right side of the filter like this:

```
| filter dt.entity.service = "PaymentBackend"
```

$varName:noquote

If you follow the variable name with `:noquote` (for example, `$varName:noquote`), the variable value is not wrapped with quotes. This is useful for numbers, units, or function names.

* Only alphanumeric characters and dot (`.`), underscore (`_`), and hyphen (`-`) are allowed
* The query fails if values contains any other characters

For example, for a service named `PaymentBackend`, in a DQL query where we filter for this service, with the no-quote strategy, we would replace the variable placeholder after the `=` on the right side of the filter like this:

```
| filter dt.entity.service = PaymentBackend
```

$varName:backtick

If you follow the variable name with `:backtick` (for example, `$varName:backtick`), the variable value is wrapped in backtick characters.

* To escape a backtick, use a double backslash:

  ```
  \\`
  ```
* Any backticks inside the variables are escaped and ignored
* Example use: field identifiers

For example, for a service named `PaymentBackend`, in a DQL query where we filter for this service, with the backtick strategy, we would replace the variable placeholder after the `=` on the right side of the filter like this:

```
| filter dt.entity.service = `PaymentBackend`
```

$varName:triplequote

If you follow the variable name with `:triplequote` (for example, `$varName:triplequote`), the variable value is wrapped in `"""` characters. This is useful for raw content such as JSON without escaping.

* Nothing is escaped within the value
* Query fails if the value contains `"""`

For example, for a service named `PaymentBackend`, in a DQL query where we filter for this service, with the triple quote strategy, we would replace the variable placeholder after the `=` on the right side of the filter like this:

```
| filter dt.entity.service = """PaymentBackend"""
```

### List variable

To define a List variable

1. Set **Name** to the name you want to give your variable.

   * It will be displayed at the top of the dashboard, listed on the **Variables** panel, and referred to in code.
   * It can contain only letters (uppercase or lowercase) and numbers (for example, `status`, `myHosts`, or `Variable01`) and it can't start with `dt_`.
2. Set **Type** to `List`.
3. In **Data**, enter a comma-separated list of possible values for this variable, such as `dog,cat,horse`. Be sure to trim extra spaces from your list.
4. Inspect the results in the **Preview** section to make sure it works as expected.
5. If you want to be able to select more than one value at a time, turn on **Multi-select**.

   Your changes are saved automatically.
6. Close the **Variable** panel.

#### Example List variable

This example would add a `$Status` variable to your dashboard with the ability to select more than one status at a time, and with four possible values: WARN, ERROR, INFO, NONE.

* **Name:** Status
* **Type:** List
* **Definition:**

  ```
  WARN,ERROR,INFO,NONE
  ```
* **Multi-select:** on

### Code variable

To define a code variable

1. Set **Name** the name you want to give your variable.

   * It will be displayed at the top of the dashboard, listed on the **Variables** panel, and referred to in code.
   * It can contain only letters (uppercase or lowercase) and numbers (for example, `status`, `myHosts`, or `Variable01`) and it can't start with `dt_`.
2. Set **Type** to `Code`.
3. In **Data**, enter the JavaScript code.

   For security reasons, when using variables in code tiles, you can only access them within the default function.
4. Select **Run** and inspect the results in the **Preview** section to make sure it works as expected.
5. If you want to be able to select more than one value at a time, turn on **Multi-select**.

   Your changes are saved automatically.
6. Close the **Variable** panel.

#### Example code variable

* **Name:** CodeVariable
* **Type:** Code
* **Definition:**

  ```
  /*



  * This will run JavaScript in the DYNATRACE



  * serverless environment.



  * To generate variable options return string array.



  */



  export default async function () {



  return ["val1", "val2", "val3"]



  }
  ```

### Free Text variable

To define a Free Text variable

1. Set **Name** the name you want to give your variable.

   * It will be displayed at the top of the dashboard, listed on the **Variables** panel, and referred to in code.
   * It can contain only letters (uppercase or lowercase) and numbers (for example, `status`, `myHosts`, or `Variable01`) and it can't start with `dt_`.
2. Set **Type** to `Free Text`.
3. You can enter a **Default value**.

## Limitations when using variables in tiles

* Variables in your tiles can be of string or numeric type. Cases requiring a different data type (for example, [duration](/docs/platform/grail/dynatrace-query-language/data-types#duration "A list of DQL data types.")) lead to failed queries. Below are some examples of how to work around such situations.
* For security reasons, when using variables in code tiles, you can only access them within the default function.

### Resolution in DQL command

Straightforward usage of a `$resolution` variable (as in the following query) doesn't work because resolution requires a predefined data format, while a variable returns a string value.

```
fetch logs



| ...



| summarize count(), by: {loglevel, bin(timestamp, $resolution)}
```

As a workaround, you can use the [duration](/docs/platform/grail/dynatrace-query-language/functions/time-functions#duration "A list of DQL time functions.") function together with a DQL [conversion](/docs/platform/grail/dynatrace-query-language/functions#conversion-and-casting-functions "A list of DQL functions.") function. This provides the required output based on your `$resolution` value.

```
fetch logs



| ...



| summarize count(), by: {loglevel, bin(timestamp, duration(toLong($resolution), unit:"m"))}
```

### Convert your variable values to other data types

If you want to filter a numeric value but compare it with a string representation, you can use a native DQL [conversion](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#conversion-and-casting-functions "A list of DQL conversion and casting functions.") function such as [toString](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#toString "A list of DQL conversion and casting functions.").

```
fetch logs



| filter amount = toString($amount)



| ...
```

### Maximum total size of variables in dashboard URL

If variable values are larger than 30 KB, they can't be stored in the dashboard URL.

* If you share a dashboard URL with variable values that exceed the size limit, the variable values won't be stored in the URL, so a person opening the dashboard from the shared URL won't see the selected values.
* If you save a dashboard URL as a bookmark with variable values that exceed the size limit, and you open the dashboard from that bookmark after 90 days, the selected values won't be set.

## Troubleshoot variables

A dashboard with one or more variables defined displays the variables in a row under the dashboard name. In this example, you can see:

* The  variables menu
* Four variables: `LogLevels`, `MyFreeTextVariable`, `Variable1`, and `Variable2`
* A  warning icon

![Dashboards: example: variables on a dashboard](https://dt-cdn.net/images/variables-controls-602-78ff9fa615.png)

To investigate the warning, select the  warning icon (or select  >  **All variables**) to list all variables.

* There are the four variables again: `LogLevels`, `MyFreeTextVariable`, `Variable1`, and `Variable2`.
* Two of those variablesâ`Variable1` and `Variable2`âdisplay a  warning icon, indicating possible issues with each of them. To see why there's a warning for a specific variable, select it.

![Dashboards: example: variables list](https://dt-cdn.net/images/variables-list-738-5c887c7243.png)

In this example, we selected `Variable1` to display the variable definition and any related error or warning message. From here, we see that we forgot to reference the variable anywhere.

![Dashboards: example: troubleshoot a variable](https://dt-cdn.net/images/variables-display-one-725-db82d68b20.png)

## Related topics

* [DQL commands](/docs/platform/grail/dynatrace-query-language/commands "A list of DQL commands.")
* [DQL functions](/docs/platform/grail/dynatrace-query-language/functions "A list of DQL functions.")


---


## Source: dashboards-new.md


---
title: Dashboards
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new
scraped: 2026-02-16T21:10:00.897568
---

# Dashboards

# Dashboards

* Latest Dynatrace
* App
* 10-min read
* Updated on Jan 28, 2026

Prerequisites

### Permissions

The following table describes the required permissions.

Permission

Description

app-engine:functions:run

Allows the user to run functions

app-engine:apps:run

Allows the user to run functions

app-engine:edge-connects:read

Allows the user to read EdgeConnect configuration via functions

document:environment-shares:read

Allows the user to access shared dashboards

document:direct-shares:read

Allows the user to access shared dashboards

state:user-app-states:write

Allows the app to persist view settings like the selected timeframe or variable values

state:user-app-states:read

Allows the app to read view settings like the selected timeframe or variable values

state:user-app-states:delete

Allows the app to delete view settings like the selected timeframe or variable values

davis:analyzers:read

Allows the user to read configuration of Davis analyzers

davis:analyzers:execute

Allows the user to run Davis analyzers

10

rows per page

Page

1

of 1

Get started

Concepts

Use cases

With ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, you can create powerful, data-driven documents for custom analytics.

![Get real-time insights by transforming complex data into dynamic, interactive dashboards.](https://dt-cdn.net/hub/00_General.png)![Start fast using our ready-made dashboards, designed for your everyday needs.](https://dt-cdn.net/hub/01_Ready_made.png)![Build your dashboard effortlessly with only a few clicks.](https://dt-cdn.net/hub/02_Explore.png)![Customize any visualization with ease.](https://dt-cdn.net/hub/03_Customize.png)![Experience dynamic and interactive dashboards with versatile variable filtering.](https://dt-cdn.net/hub/04_Variables.png)![Share your insights with others in seconds.](https://dt-cdn.net/hub/05_Share.png)

1 of 6Get real-time insights by transforming complex data into dynamic, interactive dashboards.

## Dashboard tiles

In ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, a dashboard can consist of multiple tiles:

* [Explore](#explore): explore data such as your logs, metrics, and business events with our point-and-click interface.
* [Query](#query): displays data queried via Grail.
* [Code](#code): display data returned by code executed via Dynatrace functions.
* [Markdown](#markdown): static content edited in markdown.

### Explore tile

You can use the Explore options to explore your logs, metrics, business events, and more with our point-and-click interface. With zero knowledge of DQL or coding, you can create and start using dashboard tiles in minutes.

For more information, we have a whole [Explore data](/docs/analyze-explore-automate/dashboards-and-notebooks/explore-data "Explore your data with our point-and-click interface.") page that shows you how to create Explore tiles.

### Query tile

The query tiles allow you to easily query data from Grail and [visualize](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations "Create, edit, and view visualizations on your Dynatrace dashboards and notebooks.") the result in different ways.

A query tile consists of a query input where you can write a DQL query. In the query input, use **Ctrl**+**Space** to trigger autocompletion at any time.

You can control the timeframe for the query via the timeframe dropdown list. If the timeframe is defined in the query itself, the dropdown list is disabled.

### Code tile

The code section enables you to fetch data for your dashboard using Dynatrace functions.

### Markdown tile

A markdown section can be anything from a minor note about something on the dashboard to a whole page of formatted information with links and pictures.

* Easy to edit
* Attractive to look at

To insert queries from your dashboard with autocomplete, use **Ctrl**+**Space**.

You can link to other places in your dashboard and elsewhere.

Markdown link syntax

A link in Markdown is a label and link of the form `[label](address)`, where:

* The `label` is freeform text to display on the link in your Markdown tile or section
* The `address` specifies what to open when someone selects the link, such as a website or a Dynatrace app

Link to

Syntax and examples

Website

```
[My label](https://www.example.com/)
```

Notebooks app

```
[My label](/ui/apps/dynatrace.notebooks/notebooks)
```

Specific notebook

**Syntax**:

```
[label](/ui/apps/dynatrace.notebooks/notebook/<notebookid>)
```

**Example**:

```
[My label](/ui/apps/dynatrace.notebooks/notebook/274edae4-dfe8-41fb-aced-5020fb1270bc)
```

To get the address

1. Display the target notebook.
2. Copy everything on the browser address line starting from `/ui/`.
3. Paste it into your Markdown as the address of a link.

Specific notebook section

**Syntax**:

```
[label](/ui/apps/dynatrace.notebooks/notebook/<notebookid>#<sectionid>)
```

**Example**:

```
[My label](/ui/apps/dynatrace.notebooks/notebook/274edae4-dfe8-41fb-aced-5020fb1270bc#cb69caf1-52ed-4e73-8a3e-120e8cd7e8f8)
```

To get the address

1. Display the target notebook.
2. Select the target section of the notebook.
3. Copy everything on the browser address line starting from `/ui/`.
4. Paste it into your Markdown as the address of a link.

Dashboards app

```
[My label](/ui/apps/dynatrace.dashboards/)
```

Specific dashboard

**Syntax**:

```
[label](/ui/apps/dynatrace.dashboards/<dashboardid>)
```

**Example**:

```
[My label](/ui/apps/dynatrace.dashboards/dashboard/9f24c36e-ca5f-401c-8e00-5e4b05c46bd2)
```

To get the address

1. Display the target dashboard.
2. Copy everything on the browser address line starting from `/ui/`.
3. Paste it into your Markdown as the address of a link.

Specific dashboard tile

**Syntax**:

```
[label](/ui/apps/dynatrace.dashboards/dashboard/<dashboardid>#tileIds=n)
```

**Example**:

```
[My label](/ui/apps/dynatrace.dashboards/dashboard/9f24c36e-ca5f-401c-8e00-5e4b05c46bd2#from=now%28%29-2h&to=now%28%29&tileIds=6)
```

To include a specific tile ID in the link

1. Display the target dashboard.
2. Select the target tile in the target dashboard.
3. Copy everything on the browser address line starting from `/ui/`.
4. Paste it into your Markdown as the address of a link.

## Use cases

Dashboards enables you to:

* Use readymade dashboards to monitor your system status in real-time.
* Create custom dashboards effortlessly with an easy-to-use editor or Davis CoPilotâ¢.
* Drill down into your data through seamless integration with other Dynatrace Apps.
* Utilize the power of Davis AI for spotting anomalies and forecasting directly on your charts.
* Search for any data type across the platform and combine them even with external data in a single view.
* Configure variable filters to monitor different resources within a single dashboard.

These procedures describe the basics of using ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** and get you started on the way to customizing and creating your own dashboards.

## Use dashboards

### Use shortcuts

Keyboard shortcuts help you work faster in ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.

To list keyboard shortcuts, in ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, open the  menu and select  **Keyboard shortcuts** or use keyboard shortcut **Shift**+**?**

| Action | Keyboard shortcut |
| --- | --- |
| **General** |  |
| Multiselect tiles | Select a tile, press **Space** to get a double border around the tile, use arrow keys to go to another tile, and then press **Space** again to select multiple tiles |
| Select all tiles | **Ctrl**/**Cmd**+**A** |
| Delete selected tiles | **Del** |
| Copy selected tiles to clipboard | **Ctrl**/**Cmd**+**C** |
| Paste tiles from clipboard | **Ctrl**/**Cmd**+**V** |
| Add tile | **Ctrl**/**Cmd**+**Shift**+**Enter** |
|  |  |
| **Code tiles** |  |
| Add code | **Shift**+**C** |
| Execute code | **Ctrl**/**Cmd**+**Enter** |
|  |  |
| **Data tiles** |  |
| Add query | **Shift**+**D** |
| Run query | **Ctrl**/**Cmd**+**Enter** |
|  |  |
| **Markdown tiles** |  |
| Add markdown | **Shift**+**M** |
|  |  |
| **Service-Level Objective tiles** |  |
| Add Service-Level Objective | **Shift**+**S** |
|  |  |
| **Variables** |  |
| Add variable | **Shift**+**V** |

### List dashboards

#### List all dashboards

To list dashboards

1. Go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.
2. In the **Dashboards** panel, the **Last opened by you** section lists recently accessed dashboards.
3. Hover over a dashboard name and select  for a menu of available commands for that dashboard. In this example, we would display the menu for a dashboard called `my dashboard 3`.

   ![Dashboards: Last opened by you: dashboard-specific menu](https://dt-cdn.net/images/dashboards-last-opened-by-you-dashboard-specific-menu-269-08e78a134c.png)

   The commands you see in the menu depend on your permissions for that dashboard. For example, you can't rename someone else's dashboard unless they have given you edit permissions for that dashboard. (But you *can* make a copy of a shared dashboard and then edit your copy.)

   * **Rename** enables editing for the dashboard name
   * **Duplicate** makes a copy of the dashboard
   * **Download** writes the dashboard to a JSON file that you can import
   * **Change owner** assigns dashboard ownership to a new owner
   * **Move to trash** moves the dashboard to the trash can

   This icon  after a dashboard name means someone shared that dashboard with you.
4. To display a table of all dashboards to which you have accessâyour own dashboards and all dashboards that people have shared with youâselect  **All dashboards**.

   * To sort the table, select the **Name**, **Created**, or **Last modified** header.
   * To filter the table:

     + You can enter a search string in the  filter bar at the top of the table.
     + You can select **Owned by anyone**, **Owned by me**, or **Shared with me** in the list at the top of the table.
   * To create a new dashboard, select  **Dashboard** in the upper-left corner.
   * To upload a dashboard, select  **Upload** in the upper-left corner.
   * To delete a dashboard, select  **Move to trash**. If there's no  icon for a dashboard, it means you have permission to view that shared dashboard but not to delete it.
   * To list deleted dashboards, select the **Deleted** tab of the **Dashboards** page.

     + To restore a deleted dashboard, select  **Restore**.
     + To permanently delete a dashboard, select  **Delete permanently**.

#### List my dashboards

To list all dashboards you own

1. Go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.
2. In the **Dashboards** panel, select  **All dashboards**.
3. At the top of the **Dashboards** table, select **Owned by me**.

#### List dashboards shared with me

To list all dashboards shared with you

1. Go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.
2. In the **Dashboards** panel, select  **All dashboards**.
3. At the top of the **Dashboards** table, select **Shared with me**.

#### List ready-made dashboards

To list all ready-made dashboards

1. Go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.
2. In the **Dashboards** panel, select  **Ready-made dashboards**.

Alternatively, you can select  **All dashboards** and then change the filter at the top of the table from **All dashboards** to **Ready-made**.

What's special about ready-made documents

* Created and automatically distributed by Dynatrace as examples and templates.
* Read-only: you can edit them for use during your session, and you can save a copy with your changes, but you can't save your changes to the original document.
* This icon  in a table of documents indicates that it's a ready-made document.

### Display a dashboard

To display a dashboard

1. Go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.
2. Select the name of the dashboard. In this example, we open `my dashboard 2`.

   ![Open a dashboard](https://dt-cdn.net/images/open-my-dashboard-2-264-194755db23.png)

### Interact with a tile

If you see something on a dashboard that you want to zoom in on, you can maximize it and have a closer look, and then minimize it again when you're done.

When you maximize a tile, it is temporarily zoomed to the maximum size of the display so you can see the details of the selected tile.

To maximize a tile

1. Hover over the tile to display the tile-specific commands.
2. Select  **Maximize**.

To return to the normal dashboard view, select **Minimize** in the upper-right corner.

### Refresh a dashboard

When you open a dashboard for the first time, the refresh rate is set to `Off` (no automatic refresh).

#### Manual refresh

To refresh the current dashboard manually, in the upper-right corner of the dashboard, select  (in the   pair).

#### Automatic refresh

To refresh the current dashboard automatically, in the upper-right corner of the dashboard, select  (in the   pair) and select a refresh rate.

* `Off` turns off automatic refresh
* Other settings will refresh the dashboard at the specified interval

If you change the refresh rate, that rate is remembered the next time you open the dashboard.

A frequent refresh rate can keep you literally up to the minute, but a complex dashboard may take some time to recalculate each time it is refreshed. Choose a refresh rate that suits your needs and the complexity of the dashboard.

### Edit read-only dashboards

When you open a document (dashboard or notebook) for which you don't have write permission, you can still edit the document during your session. After you're finished, you have two options:

* Save your changes to a new document
* Discard your changes

Example:

1. Go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, list the ready-made dashboards, and select the **Getting started** dashboard.

   It says  **Ready-made** in the upper-left corner, next to the document name.
2. Select the Pie chart tile and then select  **Edit**.
3. Change the visualization from Pie to Donut.

   Now you are offered two buttons: **Save as new** and **Discard changes**.
4. Use the updated dashboard as needed. You have full edit access for this session.
5. When you're finished, select what to do with your changes:

   * **Save as new**âsaves your changes in a new copy of the edited dashboard.
   * **Discard changes**âdiscards your changes and returns you to the unedited read-only dashboard.

### Select the timeframe

To review or change settings that apply to an entire dashboard

1. Display the dashboard.
2. In the upper-right corner of the dashboard, select  **Settings**.

   The **Settings** panel is displayed.
3. Review or change settings as needed.

   Custom timeframe

   To set a default timeframe for a dashboard

   1. Display the dashboard.
   2. In the upper-right corner of the dashboard, select  **Settings**.
   3. Turn on **Custom timeframe**.
   4. Select the default timeframe for the selected dashboard.

      Changing this setting does not immediately update the timeframe of the current dashboard. The change is applied only to a new session with the dashboard (either for a different user, or for the same user returning to the dashboard for another session).

   For details about the dashboard timeframes, see [Select the timeframe](#dashboard-timeframe).

   Default segment

   To review or change the dashboard default segment

   1. Display the dashboard.
   2. In the upper-right corner of the dashboard, select  **Settings**.
   3. Turn on **Default segment**.
   4. Select the default segment for the selected dashboard.

      Changing this setting does not immediately update the segment of the current dashboard. The change is applied only to a new session with the dashboard (either for a different user, or for the same user returning to the dashboard for another session).

   For details about dashboard segments, see [Select segments](#segment).

   {$} Variables

   To review or change dashboard variables

   1. Display the dashboard.
   2. In the upper-right corner of the dashboard, select  **Settings**.

      The **Settings** panel is displayed.
   3. Select **Variables**.

   For details about dashboard variables, see [Add a variable to a dashboard](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-variable "Add variables to your Dynatrace dashboards.").

The timeframe describes the *when* of the data on the dashboard.

* When you open a dashboard for the first time, the standard global timeframe (**Last 2 hours**) is applied.
* If you change the global timeframe setting for your dashboard, that timeframe is applied the next time you open the dashboard. However, there are exceptions as described below.
* You can [set a dashboard-specific default timeframe](#timeframe-dashboard) that is applied each subsequent time you open the dashboard.
* You can [set a tile-specific timeframe](#timeframe-tile). This setting overrides the global timeframe.
* When you open a dashboard via a link, if a timeframe is included in the link, the link timeframe is applied and the default dashboard timeframe is ignored.

#### Change global timeframe

To change the global timeframe

1. In the upper-right corner of the dashboard, open the timeframe selector menu (the default is **Last 2 hours** ).
2. Select a new timeframe.

   * To select a standard timeframe, choose one of the standard **Relative timeframes**
   * To define a custom timeframe, define the timeframe in the **Custom timeframe** panel and select **Apply**.

     + Use the calendar buttons ![Calendar](https://dt-cdn.net/images/dashboards-app-dashboard-timeframe-calendar-b05d935595.svg "Calendar") to select calendar dates
     + Edit the resulting **From** and **To** settings to fine-tune the range

When you change the global timeframe:

* The new timeframe is displayed in the upper-right corner of the dashboard.
* The dashboard contents are recalculated and displayed according to the new timeframe. This overrides the default dashboard timeframe.
* This does not affect any tile-specific timeframe overrides. Tile-specific timeframes take precedence over any global timeframe settings.

#### Default dashboard timeframe

To set a default timeframe for a dashboard

1. Display the dashboard.
2. In the upper-right corner of the dashboard, select  **Settings**.
3. Turn on **Custom timeframe**.
4. Select the default timeframe for the selected dashboard.

   Changing this setting does not immediately update the timeframe of the current dashboard. The change is applied only to a new session with the dashboard (either for a different user, or for the same user returning to the dashboard for another session).

#### Tile-specific timeframe override

To specify a custom timeframe in a dashboard tile

1. Edit the tile.
2. In the edit panel, turn on **Custom timeframe**.
3. Select the timeframe to apply to the selected tile.

   This timeframe overrides the dashboard timeframe set in the upper-right corner of the dashboard. Using this method, a dashboard can have multiple tiles, where each tile has its own timeframe.

You can also specify a custom timeframe in a data tile's DQL query. If you use this method (with a timeframe specified in the query), the above UI setting is disabled and the timeframe specified in the query is used.

Example timeframe specification in DQL:

```
fetch [recordtype], from:now() - 2h



| ....
```

For details on specifying a timeframe in DQL, see [Specify timeframe](/docs/platform/grail/dynatrace-query-language/dql-guide#specifytimeframe "Find out how DQL works and what are DQL key concepts.") in the DQL documentation.

### Select segments

To filter data, you can specify segments at two levels: dashboard and tile. Tile-level segment selections override dashboard-level segment selections.

Should I use segments or variables?

#### Segments

Use segments when you want to reuse them across dashboards. For example, use segments for recurring filters such as for your Kubernetes clusters, namespaces, workloads, or pods. Segments automatically apply on top of the queries of your tiles/sections, so you donât need to reference them within.

#### Variables

If you need more control over how a filter is applied, however, you might want to use variables.

* Variables allow you to fully control the underlying query or within your Explore section or tile, determining where and how they are applied. For example, you can specify how they connect with other filters applied (**AND**, **OR**) and you can control which operator is used for your filter (such as `equals`, `contains`, `startsWith`, and `endsWith`).
* Additionally, use variables when you need fine-grained control over how filters are interdependent.

* For details on segments, see [Segments](/docs/manage/segments "Segments logically structure monitoring data in Grail and function as convenient filters for data that users are allowed to access based on permissions.")
* For a ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**-specific segments use case, see [Analyze monitoring data with segments](/docs/manage/segments/getting-started/segments-getting-started-analyze-monitoring-data "Learn how to analyze monitoring data more efficiently by using segments in Dashboards.")

#### Dashboard-level segments

To select dashboard-level segments

1. Display the dashboard.
2. Open the segment selector  at the top of the dashboard and, in **Filter by segments**, select a segment.  
   If the segment requires an additional value selection, select it now.
3. To add another segment, select  **Segment**. Repeat this step for each segment you want to add.
4. Select **Apply** to apply the selection and filter data on the dashboard.

   * The segment selector  now displays the name of the selected segment or, if you select more than one segment, the number of selected segments.
   * To change your segment selection, select  again, make your changes, and select **Apply**.
   * To manage segments in general (list, create, view, edit, delete), select  and then select the **Manage segments** link.

#### Tile-level segments

To select tile-level segments

1. Display the dashboard.
2. Select the tile and then select  in the tile controls to edit the tile.
3. In the edit panel, turn on **Custom segments**.
4. In the **Custom segments** list, select a segment.  
   If the segment requires an additional value selection, select it now.
5. To add another segment, select  **Segment**. Repeat this step for each segment you want to add for the selected tile.
6. Select **Apply** to apply the selection and filter data on the tile.

   * The segment selector  now displays the name of the selected segment or, if you select more than one segment, the number of selected segments.
   * To change your segment selection, select  again, make your changes, and select **Apply**.
   * To manage segments in general (list, create, view, edit, delete), select  and then select the **Manage segments** link.

### Dashboard settings

To review or change settings that apply to an entire dashboard

1. Display the dashboard.
2. In the upper-right corner of the dashboard, select  **Settings**.

   The **Settings** panel is displayed.
3. Review or change settings as needed.

   Custom timeframe

   To set a default timeframe for a dashboard

   1. Display the dashboard.
   2. In the upper-right corner of the dashboard, select  **Settings**.
   3. Turn on **Custom timeframe**.
   4. Select the default timeframe for the selected dashboard.

      Changing this setting does not immediately update the timeframe of the current dashboard. The change is applied only to a new session with the dashboard (either for a different user, or for the same user returning to the dashboard for another session).

   For details about the dashboard timeframes, see [Select the timeframe](#dashboard-timeframe).

   Default segment

   To review or change the dashboard default segment

   1. Display the dashboard.
   2. In the upper-right corner of the dashboard, select  **Settings**.
   3. Turn on **Default segment**.
   4. Select the default segment for the selected dashboard.

      Changing this setting does not immediately update the segment of the current dashboard. The change is applied only to a new session with the dashboard (either for a different user, or for the same user returning to the dashboard for another session).

   For details about dashboard segments, see [Select segments](#segment).

   {$} Variables

   To review or change dashboard variables

   1. Display the dashboard.
   2. In the upper-right corner of the dashboard, select  **Settings**.

      The **Settings** panel is displayed.
   3. Select **Variables**.

   For details about dashboard variables, see [Add a variable to a dashboard](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-variable "Add variables to your Dynatrace dashboards.").

### Run a code tile

When you open a document from another user, you may see the following message:

`This dashboard contains custom code. It is read-only until you review the code and select âAccept and runâ.`

When you run a code tile or section written by another person, Dynatrace executes the other person's JavaScript using your user account and your permissions. This is a powerful feature, but it needs to be used correctly and responsibly. The JavaScript code can access external APIs on your behalf (using your account and permissions).

To review code

1. Select **Review all code**.

   The **Review code** page displays each code tile's code in a separate box.
2. Review the code and decide whether you want to run it.

   If you want to run the code, you can approve it just this time or permanently.

   * To run the code just this time, select **Accept and run**. The next time you open this document, you will be asked once again to review the code before running it.
   * To permanently accept the code in this document, select **Always trust code in this document** and then select **Accept and run**.

### Download result

To download (export) the result of the current dashboard tile or notebook section to a local file

1. Select the tile or section.
2. On the command bar, open the  menu and select  **Download result** > [format].

   The format options available depend on the visualization.

   * **CSV**: The result is downloaded to a local comma-separated values (\*.csv) file. This option includes table formatting such as visible columns and unit formatting.
   * **CSV (raw)**: The result is downloaded to a local comma-separated values (\*.csv) file. This option includes the complete unformatted data.
   * **JSON**: The result is downloaded to a local JSON (\*.json) file.

   Some visualizations offer no option to download the result.

#### Possible issue with importing CSV into Excel

When you export results to a CSV fileâwhether **CSV** or **CSV (raw)**âwith line breaks in any result column/field, and then open the file with Microsoft Excel or try to convert the file into a table using Excel option **Data** > **Text to Columns**, you may encounter an issue in which the line breaks are incorrectly rendered in Excel. This is caused by an Excel limitation.

To avoid this issue, use Excel option **Data** > **From Text/CSV**.

## Manage dashboards

### Add dashboard to Dock

To add a dashboard to the Dock for easy access

1. Display the dashboard.
2. Open the  menu next to the dashboard name (in the upper-left corner of the dashboard).
3. Select  **Add to dock**.

   If you change the name of the dashboard, it's automatically updated on the Dock.

To remove a dashboard from the Dock

1. Hover over the dashboard name in the Dock.
2. Select  **Unpin from dock**.

### Rename a dashboard

To rename a dashboard from the **Dashboards** panel

1. Go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.

   The **Last opened by you** section lists your most recently accessed dashboards.
2. Hover over the name of the dashboard you want to rename and select  >  **Rename**. If the rename option isn't available, you don't have edit rights to that dashboard.

### Duplicate a dashboard

To duplicate a dashboard from the **Dashboards** panel

1. Go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.

   The **Last opened by you** section lists your most recently accessed dashboards.
2. Hover over the name of the dashboard you want to duplicate and select  >  **Make a copy**.

To make a copy of the current dashboard

1. At the top of the dashboard, open the dashboard menu  next to the dashboard name.
2. Select  **Duplicate** from the menu.

   A copy is created with the name **Copy of** + the name of the current dashboard. The copy is now listed in the **Dashboards** panel.

### Share a dashboard

If you own a dashboard or notebook, you can share it.

There are three ways to share a document with other Dynatrace users in your company:

* **Access for all (view-only)**: Give view-only access to everyone in your Dynatrace environment.
* **Share access**: Create and maintain a list of users and user groups with access the document.
* **Share links**: Create links (URLs) pointing to your document and distribute the links through the channels of your choice (email, for example).

These methods are not mutually exclusive. For example, you can maintain a focused list of users for ongoing access to the document (maybe everyone in a certain group edits the document regularly) and you can create and distribute view-only links for a wider audience as needed.

In any case, you control whether people can edit the document or only view it.

For details on sharing documents, see [Share documents](/docs/discover-dynatrace/get-started/dynatrace-ui/share "Share Dynatrace documents (dashboards, notebooks, and launchpads) with other Dynatrace users in your company.").

### Manage dashboard versions

Dashboard versions are saved automatically.

* You can access the 50 most recent versions of your dashboard.
* Each dashboard version is available for up to 30 days.

To view and manage dashboard versions

1. Display your dashboard.
2. In the upper-right corner of your dashboard, select ![History](https://dt-cdn.net/images/history-icon-dc67cc1e2c.svg "History").

   This displays a menu of the most recent versions of the current dashboard.

   * Date
   * Time
   * Name of the person who created that version
3. From any version entry in the **Versions** menu, you can select version-specific actions.

   * ![Preview](https://dt-cdn.net/images/icon-preview-1-138a2e67eb.svg "Preview") **Preview** displays a preview of the selected version.
   * **Restore** switches your dashboard to the selected version.
   * **Make a copy** creates a new dashboard from the selected version and displays the new dashboard. The original dashboard remains unchanged.
   * **Download** saves a JSON file of the selected version of the dashboard to your local machine.
   * **Preview in new tab** displays a preview of the selected version on a new browser tab.
   * **Delete this version** deletes the selected version.
4. To list and manage all versions of the dashboard in a separate window, go to the bottom of the **Versions** menu and select **Show all**.

For details, see [Manage document versions](/docs/analyze-explore-automate/dashboards-and-notebooks/document-version "View and manage versions of documents created in Dynatrace Notebooks and Dashboards.").

### Change dashboard owner

When you create a document (dashboard or notebook), you are the owner. To give ownership of the document to another Dynatrace user

1. Open the  document menu and select  **Change owner**.
2. Find and select a new owner, and then select **Change owner**.

   When you change the document owner, you immediately lose access to the document.

   * Be sure you are ready to transfer ownership before you select this command.
   * You can regain access to the document only if the new owner gives you permission.
3. After the transfer is complete, the new owner will receive email about the document ownership transfer.

### Download a dashboard

To download (export) the currently displayed dashboard as JSON

1. At the top of the dashboard, open the  menu to the right of the dashboard name.
2. Select  **Download** from the menu.

   The definition of the current dashboard is downloaded to a local JSON file.

To download (export) a dashboard from the ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** side panel

1. Go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.
2. In **Last opened by you**, hover over the name of the dashboard you want to export and select  **Download** from the  menu. The dashboard is downloaded to a local JSON file that you can upload.

   If your dashboard isn't listed in **Last opened by you**, select  **All dashboards** to display a table of all dashboards that you can access (your dashboards or dashboards shared with you). From there, you can find the dashboard and select  **Download** from the  menu.

### Upload a dashboard

To upload (import) the JSON definition of a dashboard from the **Dashboards** side panel

1. Go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.
2. In the **Dashboards** panel on the left, select  **Upload**.
3. Find and open the dashboard JSON definition file.

To upload (import) the JSON definition of a dashboard from the **Dashboards** table

1. Go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.
2. In the **Dashboards** panel on the left, select  **All dashboards**.

   A **Dashboards** table displays all dashboards by **Name** and **Last modified** date.
3. In the upper-left corner of the page, select  **Upload**.
4. Find and open the dashboard JSON definition file.

An uploaded dashboard is:

* Opened in Dynatrace.

  If you see a message about running custom code when you upload a dashboard, see [Run code warnings](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-code#run-code-warnings "Add code to your Dynatrace dashboards.") for more information.
* Added to your **Last opened by you** list.
* Added to the **Dashboards** page with **Last modified** set to the upload date and time.

### Delete a dashboard

To delete any dashboard on the **Dashboards** page

1. Go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.
2. In the **Dashboards** panel on the left, select  **All dashboards**.

   A table displays all dashboards by **Name** and **Last modified** date.
3. On the **Dashboards** page, select  **Move to trash** for the dashboard you want to delete.

### Dashboards via API: best practices

When creating or managing dashboards via API, these best practices can make your life easier.

* To get a solid start, create the dashboard in the ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** app and then [download](#dashboards-download) the dashboard configuration file.
* To verify changes made via API, [upload](#dashboards-upload) the file to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**. Does everything still look as expected?
* Be careful with layout changes, as empty vertical spaces cause tiles to shift upwards automatically on document load and cause the **Discard changes** button to appear.
* To examine changes in detail, select **Save as new** to download the document and compare it with the original version.
* Don't set the `version` property of the config to an arbitrary value. It's an internal property needed for migration purposes.

## Create and edit dashboards

### Create a dashboard

The fastest and easiest way to explore your data is with our new [Explore](/docs/analyze-explore-automate/dashboards-and-notebooks/explore-data "Explore your data with our point-and-click interface.") tiles and sections. In a few seconds, you can find and analyze your logs, metrics, or business events. No DQL required!

To create a new dashboard

1. Go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.
2. Select  **Dashboard**.

After you create an empty dashboard, you need to add tiles to it.

* Query Grail
* Add code
* Add Markdown
* Add a variable
* Add a snippet

### Query Grail

To Query Grail

1. In the upper-right of the dashboard, select  **Add** >  **DQL**.

   Keyboard shortcut: **Shift**+**D**

   ![Dashboards: Add tile button (Plus)](https://dt-cdn.net/images/updated-dashboards-add-tile-button-481-c21ba8f200.png)

   A configuration side panel opens on the right to display two tabs:

   * **Data**
   * **Visual**
2. On the **Data** tab, use the [Dynatrace Query Language (DQL)](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") to define your query.
3. Select **Run** to execute the query.
4. On the **Visual** tab, choose a [visualization](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations "Create, edit, and view visualizations on your Dynatrace dashboards and notebooks.") format for your results.

   * means the visualization type is unavailable for your query.
5. Under the **Visualization** selector, expand the options sections to adjust visualization settings as needed.
6. Close the side panel when you're done.

   If you want to return to these settings, select your tile to display them.

For details, see [Add data to a dashboard](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-data "Add data to your Dynatrace dashboards.").

### Add code

To add code to a dashboard

1. In the upper-right of the dashboard, select  **Add** >  **Code**.

   Keyboard shortcut: **Shift**+**C**

   ![Dashboards: Add tile button (Plus)](https://dt-cdn.net/images/updated-dashboards-add-tile-button-481-c21ba8f200.png)

   An empty tile is added to the dashboard and an **Options** side panel opens on the right.
2. Optional In **Tile title**, enter a title to display at the top of your tile.
3. In the numbered **Code** box, enter custom JavaScript to fetch external data from any available API. Use the [Fetch APIï»¿](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) to fetch data from external APIs.

   To make sure your requests aren't blocked, ask your administrator to allow your external data sources by adding them to the **External requests**.

   External requests enable outbound network connections from your Dynatrace environment to external services. They allow you to control access to public endpoints from the AppEngine with app functions and functions in Dashboards, Notebooks, and Automations.

   1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** >  **General** > **External requests**.
   2. Select  **New host pattern**.
   3. Add the domain names.
   4. Select **Add**.

   This way you can granularly control the web services your functions can connect to.

   Don't include the address prefix. For example, if the address is `https://some.service.org`, just add `some.service.org`.

For details, see [Add code to a dashboard](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-code "Add code to your Dynatrace dashboards.").

### Add markdown

To add a markdown tile to a dashboard

1. In the upper-right of the dashboard, open the  **Add** menu and select  **Add markdown**.

   Keyboard shortcut: **Shift**+**M**

   ![Dashboards: Add tile button (Plus)](https://dt-cdn.net/images/updated-dashboards-add-tile-button-481-c21ba8f200.png)

   An **Options** side panel opens on the right.
2. In the **Options** side panel, enter your text.

   * Use Markdown to format your text and add links and images.
   * The tile is updated as you edit.
   * While you're editing text, press Ctrl+Space to see options.
3. Close the **Options** side panel when you're done.

For details, see [Add Markdown to dashboard](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-markdown "Add Markdown-formatted annotations to your Dynatrace dashboards.").

### Add variable

Use variables to filter your dashboards, to act as variable values in code tiles, and as placeholders in tile titles and Markdown tile text.

To add a variable to a dashboard

1. In the dashboard header, open the  menu and select  **Variables**.
   Keyboard shortcut: **Shift**+**V**

   Keyboard shortcut: **Shift**+**V**

   ![Dashboards: Add tile button (Plus)](https://dt-cdn.net/images/updated-dashboards-add-tile-button-481-c21ba8f200.png)

   The **Variable** panel is displayed.
2. Define the variable.

   * **Name**: the name of the variable.

     + Only alpha-numerical values are allowed
     + Do not start a variable name with `dt_`
   * **Type**: can be one of the following:

     + **DQL**: the value is returned from a query you enter when you define the variable.

       - Select **Run** to test your query.
     + **Code**: the value is returned from code you enter when you define the variable.
     + **List**: a comma-separated values (CSV) list of values.

       - To define possible values, enter them (separated by commas) in the box under **Data**.
       - To define a default value, select one from the **Default value** list.
       - To allow multiple values to be selected at the same time, turn on **Multi-select**.
     + **Free Text**: free text. You can enter a **Default value**.
       Your changes are saved automatically.
3. Set **Display settings**.

   * If the variable dropdown should be displayed on the dashboard, turn on **Display as filter on dashboard**.  
     Turn it off when you want it hidden, such as when the variable is used as a static value across tiles but should not be displayed to the dashboard user.
   * If users should be able to select multiple values at the same time within the variable dropdown, turn on **Multi-select**.  
     Turn it off when you want to use only single values of the variable dropdown.
   * Select a **Default value** for the variable dropdown. If you don't enter anything in this field, the first available value is selected.
4. When you're finished, select **< Variable** at the top to go to the **Variables** panel, or select  to dismiss the **Variables** panel.

Variables in dashboards can be defined to depend on other variables.

* The value of a variable is recalculated if its definition refers to another variable and the other variable's value changes.

  For example, if the value of variable A changes, the value of any variable whose definition refers to variable A is recalculated.
* Loops are not allowed.

  For example, if the value of variable A depends on the value of variable B, the value of variable B can't depend on the value of variable A.

For details, see [Add a variable to a dashboard](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-variable "Add variables to your Dynatrace dashboards.").

### Add snippet

To get started based on a snippet

1. In the upper-right of the dashboard, select  **Add** to open the **Add** menu.

   Keyboard shortcut: **Ctrl**/**Cmd**+**Shift**+**Enter**

   ![Dashboards: Add tile button (Plus)](https://dt-cdn.net/images/updated-dashboards-add-tile-button-481-c21ba8f200.png)
2. Scroll down to the **Start with a snippet** section and choose one of the snippets. In this example, we select the  **Fetch logs** snippet, which is displayed in a preview panel.

   ![Example: select the "Fetch logs" snippet.](https://dt-cdn.net/images/add-snippet-menu-example-fetch-logs-754-d4435c09eb.png)
3. After you select a snippet, the edit panel displays the snippet you added.

   ![Example: "Fetch logs" snippet added.](https://dt-cdn.net/images/add-snippet-menu-example-fetch-logs-result-1436-77cc9fa8f1.png)
4. Edit the query or code (depending on the snippet type you selected) and the visualization settings as needed.
5. Select **Run** to see results.
6. Close the side panel when you're done.

For details, see [Add a snippet to a dashboard](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-snippet "Start with a snippet").

### Analyze data with AI

To analyze data using Dynatrace Intelligence Data Analyzers

1. Explore a timeseries.

   Example

   In your document (dashboard or notebook)

   1. Select  to add a new section or tile, and then select **Metrics** to explore metrics.

      ![Example: select Add > Metrics](https://dt-cdn.net/images/example-select-explore-metrics-637-025cadac69.png)
   2. In **Select metric**, select **Infrastructure** > **CPU** > **CPU usage %**.

      ![Example: select metric "CPU usage %"](https://dt-cdn.net/images/example-select-metric-cpu-usage-percent-771-a672aa20e2.png)
   3. Set **Split by** to `host.name`.

      ![Example: set "Split by" to host.name](https://dt-cdn.net/images/example-select-host-name-743-5bd89ea6a3.png)
   4. Set **Limit** to the maximum number of series to analyze. Dynatrace Intelligence Data Analyzer currently supports analysis up to 1000 series.

   You should get something like this:

   ![Example: complete query](https://dt-cdn.net/images/example-complete-query-737-dfa24f730d.png)
2. Run the query.
3. In the options panel on the right, scroll down and expand  **Davis AI**.

   Show me

   ![An example of selecting the Analyze and alert settings in the Dashboards app.](https://dt-cdn.net/images/dashboards-select-analyze-and-alert-settings-746-7155ef9415.png)

   ![The initial panel for the Analyze and alert settings in the Dashboards app.](https://dt-cdn.net/images/dashboards-analyze-and-alert-details-746-8d503491c8.png)
4. On the **Davis AI** panel, set **Analyzers** to the analyzer you want to use, and then configure the analyzer.

   * For an overview of anomaly detection, see [Anomaly detection](/docs/dynatrace-intelligence/anomaly-detection "How Dynatrace detects anomalies in your environment.")
   * For details on anomaly detection settings, see [Anomaly detection configuration](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration#analyzer "How to set up an alert for missing measurements.")

   * For details on forecast analyzer settings, [Dynatrace Intelligence predictive AI analysis](/docs/dynatrace-intelligence/reference/ai-models/forecast-analysis "Learn how Dynatrace Intelligence predictive AI generates forecasts.")

   Anomaly Detection: Auto adaptive threshold anomaly detection

   * **Number of signal fluctuations**âhow many times the signal fluctuation is added to the baseline to produce the actual threshold for alerting.
   * **Alert condition**âyour selection depends on whether you want to know when the metric is above, below, or outside (above or below) the normal range.

   For details, see [Anomaly detection configuration](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration#analyzer "How to set up an alert for missing measurements.").

   Anomaly Detection: Seasonal baseline anomaly detection

   * **Tolerance**âthe higher the tolerance, the broader the confidence band, leading to fewer triggered events.
   * **Alert condition**âyour selection depends on whether you want to know when the metric is above, below, or outside (above or below) the normal range.

   For details, see [Anomaly detection configuration](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration#analyzer "How to set up an alert for missing measurements.").

   Anomaly Detection: Static threshold anomaly detection

   * **Threshold**âa hard limit that a metric should not violate.
   * **Unit**âthe unit of the value.
   * **Alert condition**âyour selection depends on whether you want to know when the metric is above or below the threshold value.
   * **Suggest threshold**âDavis AI can help you to find the right threshold based on historical data.

   For details, see [Anomaly detection configuration](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration#analyzer "How to set up an alert for missing measurements.").

   Prediction: Forecast

   * **Data points to predict**âthe total steps the time series is forecasted. More steps generally results in less reliable forecasts and longer analyzer runtimes.
   * **Forecast offset**âan offset for the start of the forecast. For example, if the offset is set to `2`, the last two data points are ignored and a forecast for these points is returned as well.

   For details, see [Dynatrace Intelligence predictive AI analysis](/docs/dynatrace-intelligence/reference/ai-models/forecast-analysis "Learn how Dynatrace Intelligence predictive AI generates forecasts.").

   Advanced settings (for anomaly detection)

   You can use the default values or turn on **Show advanced properties** to fine-tune these settings.

   * **Alert on missing data**âalert if no data is detected within the sliding window.
   * **Violating samples**ânumber of samples in the sliding window that must violate to trigger an event.
   * **Sliding window**ânumber of samples that form the sliding window.
   * **Dealerting samples**ânumber of samples in the sliding window that must go back to normal to close the event.
5. By default, the analyzer is not enabled. To enable it, turn on the switch at the top of the edit panel (switch from **AI data analysis is not active** to **AI data analysis is active**).
6. To view the results, select the **Davis AI analysis** visualization and expand the **Davis AI analysis chart** section to review or change the visualization-specific settings:

   Show me

   ![Example of selecting "AI analysis" visualization and displaying visualization-specific settings in the Notebooks app.](https://dt-cdn.net/images/notebooks-ai-analysis-visualizations-757-4cf3f48b3c.png)

   The **Davis AI analysis** visualization has two sections: chart and visualization. You can use the **Visible sections** setting to display either or both of them.

   * **All**âshow a chart and a table. The chart reflects your table selections.
   * **Table**âshow only a table. You can sort columns that display a sort icon  in the header. Select the column header to toggle the sort order up  or down .
   * **Chart**âshow only a chart. Use the table to select entries you want to show on the chart.

#### Example: anomalous CPU usage percent

To detect when CPU usage percent exceeds 70 percent, in your document (dashboard or notebook)

1. Select  to add a new section or tile, and then select **Metrics** to explore metrics.

   Show me

   ![Example: select Add > Metrics](https://dt-cdn.net/images/example-select-explore-metrics-637-025cadac69.png)
2. In **Select metric**, select **Infrastructure** > **CPU** > **CPU usage %**.

   Show me

   ![Example: select metric "CPU usage %"](https://dt-cdn.net/images/example-select-metric-cpu-usage-percent-771-a672aa20e2.png)
3. Set **Split by** to `host.name`.

   Show me

   ![Example: set "Split by" to host.name](https://dt-cdn.net/images/example-select-host-name-743-5bd89ea6a3.png)
4. Set **Limit** to the maximum number of series to analyze. Davis analyzer currently supports analysis up to 1000 series.

   Show me

   ![Example: complete query](https://dt-cdn.net/images/example-complete-query-737-dfa24f730d.png)
5. Select **Run**.
6. In the edit panel, expand  **Davis AI**.

   Show me

   ![An example of selecting the Analyze and alert settings in the Dashboards app.](https://dt-cdn.net/images/dashboards-select-analyze-and-alert-settings-746-7155ef9415.png)

   ![The initial panel for the Analyze and alert settings in the Dashboards app.](https://dt-cdn.net/images/dashboards-analyze-and-alert-details-746-8d503491c8.png)
7. In the **Analyzers** list, select **Static threshold anomaly detection**.

   Show me

   ![Selecting the "Static threshold anomaly detection" analyzer in the Analyze and alert settings of the Dashboards app.](https://dt-cdn.net/images/dashboards-analyze-and-alert-select-static-threshold-anomaly-detection-752-45026264f0.png)
8. Set **Threshold** to `70` (enter a value) and **Alert condition** to **Alert if metric is above** (default).

   Show me

   ![Configuring settings for the "Static threshold anomaly detection" analyzer in the Dashboards app.](https://dt-cdn.net/images/dashboards-static-threshold-anomaly-detection-settings-748-4d20c8220e.png)
9. Activate the analyzer: at the top of the edit panel, switch from **AI data analysis is not active** to **AI data analysis is active**.
10. To view the results, select the **Davis AI analysis** visualization. Expand the **Davis AI analysis chart** section to see visualization-specifc settings.

    Show me

    ![Example of selecting "AI analysis" visualization and displaying visualization-specific settings in the Notebooks app.](https://dt-cdn.net/images/notebooks-ai-analysis-visualizations-757-4cf3f48b3c.png)
11. In the **Davis AI analysis chart** section, set **Visible sections** to **All**.
12. Review the results.

    In this example, we selected the hosts that exceeded the threshold.

    * The chart shows a line for the selected metric (`CPU usage %`) for each selected host.
    * A red bar across the top of the visualization indicates where the threshold for that metric was exceeded.
    * The table under the chart has those hosts selected.

    ![Example analyzer results with "AI analysis" visualization in the Notebooks app.](https://dt-cdn.net/images/notebooks-ai-analysis-chart-1920-5ac0e1f854.png)

### Change variable values

If a dashboard has one or more variables, they are listed by name along the upper-left of the dashboard, under the dashboard name. When you change variable values, the dashboard contents are recalculated and displayed according to the new values.

To change the value of a variable

1. In the upper-left of the dashboard, locate the variable name.
2. Use the menu or edit box under the variable name to change the value.

   * If the variable allows just one selection (value) at a time, select the value that you want to apply to the dashboard.
   * If the variable allows multiple selections (values) at a time, select the checkbox for each value you want to apply to the dashboard. The menu name for that variable shows how many values are selected.
   * For a Free Text variable, you can edit the text in the box under the variable name.

### Copy to another document

You can copy a dashboard tile to another document (such as a different dashboard or a notebook).

For example, an easy way to start a new notebook is to copy reusable tiles from existing dashboards to a new notebook and then edit the copied sections as part of the new notebook.

To copy a dashboard tile to a notebook (as a notebook section)

1. In the dashboard, select the tile that you want to copy to a notebook.
2. Open the  menu and select ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Add to notebook**.
3. In **Select destination**:

   * If you want to create a new notebook with the selected dashboard tile as a section, select **New notebook**.
   * If you want to add the selected dashboard tile as another section in an existing notebook, select the existing notebook from the list and then select **Confirm**.

   The notebook opens with the selected tile copied into it as a notebook section.

To copy a dashboard tile to a different app (not ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**), open the  menu and select  **Open with**, and then select the target app.

For details, see [Drilldowns and navigation](/docs/analyze-explore-automate/dashboards-and-notebooks/open-with "Drill down from Dashboards and Notebooks using links based on intents or URLs.").

### Edit a tile

To edit a tile

1. Select the tile to display the tile-specific commands.
2. Select  **Edit**.

   An **Options** panel opens on the right to display the tile or section configuration.
3. Select and drag the expander control left or right as needed to resize the **Options** panel for a better look at the code.

   ![Resize options panel](https://dt-cdn.net/images/options-panel-resize-155-a8c92d2683.png)

### Add or edit a tile title

You can add a title to any dashboard tile (except for a Markdown tile).

Regardless of the title setting, a title bar is automatically created as needed to display tile indicators such as for a warning or to indicate a custom tile timeframe.

1. Select the tile and  edit it.

   * The title is displayed in the box at the top of the tile edit panel.
   * If the tile has no title, the box displays `Untitled tile`.
2. Edit the title. Your edits are displayed as you type.

   A title can include emojis (such as ð and ð and â¤ï¸) and variables.

   **Example:**

   1. In your dashboard, define [variables](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-variable "Add variables to your Dynatrace dashboards.") called `Status` and `Emoji`.
   2. Set the title to `Current $Emoji status is $Status`.
   3. Set variable `Status` to `Good`.
   4. Set variable `Emoji` to `ð`.

   The title will be displayed as `Current ð status is Good`, and it will update automatically when the variable values change.

To remove a tile title, select the tile and  edit it, and then clear the title box.

### Configure a tile visualization

Each visualization has visualization-specific settings.

To edit a tile visualization, see the [visualization instructions](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations "Create, edit, and view visualizations on your Dynatrace dashboards and notebooks.").

## Layout

### Resize a tile

To resize a tile

1. Hover over the tile.
2. Select and drag  in the lower-right corner of the tile to change the dimensions of the tile.

   To help you select a specific size, the tile size is displayed on the tile command bar.

### Move a tile

You can move one tile at a time or select and move multiple tiles simultaneously.

To move a tile, drag the tile to a new position.

* If the tile has a title, select and drag  the title bar to move the tile.
* If the tile has no title, select the tile to display the tile-specific commands, and then select and drag  on the tile command bar to drag the selected tile to a new location.

  To help you align tiles, a background grid is displayed when you're moving a tile.

To move multiple tiles simultaneously

1. Select one tile.
2. Ctrl-click additional tiles that you want to move.

   * Each selected tile is highlighted.
   * The total number of selected tiles is displayed on the tile command bar.
3. Select and drag  **Move** to drag all of the selected tiles to a new location.

### Copy and paste a tile

You can copy and paste tiles to the same dashboard or another dashboard.

To copy and paste one tile

1. Select the tile to display the tile-specific commands.
2. On the tile command bar, select  **Copy to clipboard**.

   The selected tile is copied to your clipboard.
3. Paste the tile (Ctrl-V).

   * You can paste the copied tile to the current dashboard, in which case it's the equivalent of  **Duplicate**.
   * You can switch to another dashboard and paste the copied tile there.

To copy and paste multiple tiles simultaneously

1. Click one tile to select it.
2. Ctrl-click additional tiles that you want to copy and paste.

   * Each selected tile is highlighted.
   * The total number of selected tiles is displayed on the tile command bar.
3. On the tile command bar, select  **Copy to clipboard**.

   The selected tiles are copied to your clipboard.
4. Paste the tiles (Ctrl-V) to the same dashboard or switch to another dashboard and paste them there.

### Duplicate a tile

You can duplicate one tile at a time or duplicate multiple tiles simultaneously.

To duplicate one tile

1. Select the tile to display the tile-specific commands.
2. Select  **Duplicate**.

   A copy of the tile is created on the current dashboard.

To duplicate multiple tiles simultaneously

1. Click one tile to select it.
2. Ctrl-click additional tiles that you want to duplicate.

   * Each selected tile is highlighted.
   * The total number of selected tiles is displayed on the tile command bar.
3. On the tile command bar, select  **Duplicate**.

   The selected tiles are duplicated on the current dashboard.

### Split tile space to insert new tile

When laying out a dashboard, you can split the space that a tile uses on the grid, and insert a second tile next to the first tile within the same space.

* The first tile is unaffected other than that it now uses half the width or height it used before you split the space.
* The second (new) tile uses the other half of that layout space.
* This is available only when you select a single tile that is big enough to split. It's not available when you select multiple tiles, or if the size of the selected tile is too small to split.

For example, let's select a tile and add another tile to its right, so that the two tiles share the space originally used by the first tile.

1. Select the tile.
2. Hover over the tile to see the  split controlsâleft, right, and bottomâto indicate where you split that space and insert a new tile.

   ![Split a dashboard tile to insert another tile within the same space](https://dt-cdn.net/images/split-tiles-01-1515-c796df2c96.png)
3. In this example, select the  control on the right. It opens a menu similar to the  menu you would otherwise use to add a tile to the dashboard.
4. Select the tile type you want to add.
5. Edit the definition of the new tile and close the edit panel to see the changed layout.

   * The original tile is unchanged except that it now uses only the left half of the space it used before.
   * The new tile uses the right half of that space.
   * You can still adjust the tile sizes and positions manually.

### Delete a tile

You can delete one tile at a time or select and delete multiple tiles simultaneously.

To delete one tile

1. Select the tile to display the tile-specific commands.
2. On the tile command bar, select  **More actions** >  **Delete**.
3. In the **Are you sure you want to delete this tile?** message, select **Cancel** or **Delete**.

To delete multiple tiles simultaneously

1. Click one tile to select it.
2. Ctrl-click additional tiles that you want to delete.

   * Each selected tile is highlighted.
   * The total number of selected tiles is displayed on the tile command bar.
3. On the tile command bar, select  **Delete**.
4. In the **Are you sure you want to delete this tile?** message, select **Cancel** or **Delete**.


---


## Source: document-api.md


---
title: API for Dashboards and Notebooks
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/document-api
scraped: 2026-02-16T21:24:49.086188
---

# API for Dashboards and Notebooks

# API for Dashboards and Notebooks

* Latest Dynatrace
* Reference
* 2-min read
* Published Apr 23, 2024

The Dynatrace platform provides a collection of [platform servicesï»¿](https://dt-url.net/sx23ug5), each with a specific area of responsibility. You need one of these services, the [document serviceï»¿](https://dt-url.net/x403ua9), to manage Dynatrace documents such as dashboards and notebooks via API.

## Access document data

The ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** and ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** apps use the document service API to persist data as documents.

Documents are content-agnostic, but both notebook and dashboard documents have common metadata: a unique identifier, a name, and a description.

To distinguish notebook and dashboard documents, and to make them visible to the respective apps, they need the correct `type` document attribute: `dashboard` or `notebook`. This attribute can also be used to query the API as shown in the following examples.

#### List all accessible dashboards

```
https://environment/platform/document/v1/documents?filter=type='dashboard'
```

#### List all accessible notebooks

```
https://environment/platform/document/v1/documents?filter=type='notebook'
```

## Access full document service documentation

To see the full API documentation for the documents service

1. Go to the [Document serviceï»¿](https://dt-url.net/x403ua9) page of the [Dynatrace Developerï»¿](https://developer.dynatrace.com/) site.
2. In the **Related links** section, select the **Swagger API** link.

   You may need to sign in to your Dynatrace environment.


---


## Source: document-version.md


---
title: Manage document versions
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/document-version
scraped: 2026-02-16T21:12:28.964605
---

# Manage document versions

# Manage document versions

* Latest Dynatrace
* How-to guide
* 4-min read
* Published Jul 08, 2022

Platform | Notebooks Platform | Dashboards

Document (notebook or dashboard) versions are saved automatically.

* You can access the 50 most recent versions of your document.
* Each version is available for up to 30 days.

## History History menu

To view and manage document versions

1. Display your document (notebook or dashboard).
2. In the upper-right corner of your document, select ![History](https://dt-cdn.net/images/history-icon-dc67cc1e2c.svg "History").

   This displays a menu of the most recent versions of the current document.

   * Date
   * Time
   * Name of the person who created that version
3. From any version entry in the **History** menu, you can select version-specific actions.

   * ![Preview](https://dt-cdn.net/images/icon-preview-1-138a2e67eb.svg "Preview") **Preview** displays a preview of the selected version.
   * **Restore** switches your document to the selected version.
   * **Make a copy** creates a new document from the selected version and displays the new document. The original document remains unchanged.
   * **Download** saves a JSON file of the selected version of the document to your local machine.
   * **Preview in new tab** displays a preview of the selected version on a new browser tab.
   * **Delete this version** deletes the selected version.
4. To list and manage all versions of the document in a separate window, go to the bottom of the **History** menu and select **Show all**.

For details, see below.

## Preview Preview

**History** > **[version]** > ![Preview](https://dt-cdn.net/images/icon-preview-1-138a2e67eb.svg "Preview") **Preview** displays a preview of the selected version.

Changes made when previewing a version won't be saved or included when restoring that version.

A toolbar at the top of the preview offers the following options:

* **Restore** switches your document to the selected version.
* **Make a copy** creates a new document from the selected version and displays the new document. The original document remains unchanged.
* **Download** downloads a JSON file of the selected version of the document to your local machine.
* **Delete this version** removes the selected version from the document history.

Close the toolbar to close the preview and return to where you started.

## Restore

**History** > **[version]** >  **Restore** switches your document to the selected version.

## Make a copy

**History** > **[version]** >  **Make a copy** creates a new document from the selected version and displays the new document. The original document remains unchanged.

## Download

**History** > **[version]** >  **Download** downloads a JSON file of the selected version of the document to your local machine.

## Preview in new tab

**History** > **[version]** >  **Preview in new tab** is like **History** > **[version]** > **Preview**, but it displays the preview on a new tab.

A toolbar at the top of the preview offers the following options:

* **Restore** switches your document to the selected version.
* **Make a copy** creates a new document from the selected version and displays the new document. The original document remains unchanged.
* **Download** downloads a JSON file of the selected version of the document to your local machine.
* **Delete this version** removes the selected version from the document history.

## Delete this version

**History** > **[version]** >  **Delete this version** removes the selected version from the document history.

## Show all

**History** > **Show all** opens the **Version history** table, which displays all versions of the selected document. Use this table when you need to access versions that don't fit on the **History** menu. The **Version history** table goes back as far as 50 versions.

### Version

The **Version** column displays the version ID.

### Updated on

The **Updated on** column displays when the version was created.

### Updated by

The **Updated by** column displays the name of the person who created the version.

### Actions

The **Actions** column displays all of the actions available from the **History** > **[version]** menu.

* ![Preview](https://dt-cdn.net/images/icon-preview-1-138a2e67eb.svg "Preview") **Preview** displays a preview of the selected version.
* **Restore** switches your document to the selected version.
* **Make a copy** creates a new document from the selected version and displays the new document. The original document remains unchanged.
* **Download** saves a JSON file of the selected version of the document to your local machine.
* **Preview in new tab** displays a preview of the selected version on a new browser tab.
* **Delete this version** deletes the selected version.


---


## Source: visualization-chart-area.md


---
title: Area chart visualization
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-chart-area
scraped: 2026-02-15T21:16:39.899415
---

# Area chart visualization

# Area chart visualization

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Jul 08, 2022

When to use an area chart visualization

Use an area chart visualization:

* When you want to show how different categories contribute to an overall trend over time, emphasizing the magnitude of change in each category.
* When you need to compare the contributions between these different categories over time, it helps visualize the proportion of each category at a certain point in time.
* When you need to show cumulative data such as the number of sessions, or revenue, over time. Area charts can be effective in showing the sum/growth of values.

## Example

![Area chart example](https://dt-cdn.net/images/area-chart-773-85df352b18.png)

The chart above is based on the following query.

```
timeseries avg(dt.host.cpu.usage)
```

* The visualization type is set to **Area chart**.
* Other options are set to defaults.

## Chart interactions

To access the chart tools:

* When space is limited, hover over the chart and select  **Chart tools** to open a menu of chart tools.
* When there is sufficient space, the chart tools are displayed in a toolbar.

  ![Timeseries chart toolbar - full](https://dt-cdn.net/images/chart-tool-bar-269-c1d9a7bc39.png)

  When you hover over the chart, the chart toolbar is displayed by default in the lower-right corner of the chart and is collapsed.

### Toolbar options

**Icon**

**Name**

**Keyboard shortcut**

**Action**

**Move**

none

Move the chart toolbar. Select and drag the  icon.

**Explore**

`E`

Explore a section of the chart. Select **Explore**, and then click and drag left or right to select a section of the chart. The chart zooms to display the selected area.

**Pan**

`P`

Pan the chart to the left or right. Select **Pan**, and then click and drag left or right.

**Zoom in**

`Ctrl+Up`

Zoom in to the chart.

**Zoom out**

`Ctrl+Down`

Zoom out from the chart.

**Reset**

`R`

Restore the chart zoom level and timeframe to their original states.

**Collapse**

none

Shrink the chart toolbar to just  and .

**Expand**

none

Show the entire chart toolbar.

### Zoom rules

For a timeseries chart (Line, Area, Bar):

* You can't zoom on the chart if the timeframe is set in the DQL query.
* ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**

  If you zoom on a tile without a custom tile timeframe, the global timeframe for the dashboard is updated accordingly, so timeframes stay in sync across the dashboard except where a tile has its own overriding timeframe.

  If you zoom on a tile with a custom tile timeframe but without a timeframe in the query, the selected timeframe is applied to the custom tile timeframe and the changed timeframe is reflected in the dashboard.
* ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**

  If you zoom in a timeseries in a notebook section, the timeframe of the section changes, and the change is persisted in the notebook.

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
* **Open with**âfor details, see [Drilldowns and navigation](/docs/analyze-explore-automate/dashboards-and-notebooks/open-with "Drill down from Dashboards and Notebooks using links based on intents or URLs.").

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

For example, when working with DQL and a timeseries, in the result we have a column with a value array for each series (one row with that one cell of values). For a timeseries, this mapping is done fully automatically, but the data mapping shows you which underlying column is mapped.

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

Data mapping restrictions for event-based graph visualizations

Dynatrace version 1.322+

#### What changed?

To make data mapping easier and more intuitive, weâve restricted certain fields in the interface for event-based charts, showing only the most relevant options.

* **Before**: Prior to Dynatrace version 1.322, fields such as `timestamp`, `interval`, and `duration` could be mapped to the "names" option within the data mapping surface.
* **After**: Starting with Dynatrace version 1.322, these fields are no longer available for selection in the "names" option.

#### Impact

If your ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** or ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** charts rely on these fields, the affected tiles will display an error message, such as:

`Selected field unavailable. The field "" is no longer available. Try adjusting the data, or select another field or visualization.`

#### Resolution

To resolve this issue

1. Replace the existing `summarize` command with `makeTimeseries`.
2. Replace the `by: { ... 4h }` parameter with `interval: 4h` while using the same interval as with the previous configuration in the `by`.

After applying these changes, the data mapping will correctly allow suitable fields for the "names" option, and your tiles will function as expected.

### Visualization-specific data mapping settings

An area chart graphs one or more values over time, so the mapping needs to include the following:

* **Time**: the column of your result that is used for the X-axis ([timestamp](/docs/platform/grail/dynatrace-query-language/data-types#timestamp "A list of DQL data types.") or [timeframe](/docs/platform/grail/dynatrace-query-language/data-types#timeframe "A list of DQL data types.")).
* **Interval**: this value is automatically mapped and canât be changed. It lets you know which fields are mapped for timeseries-based results. It takes the first available interval field from the result set whenever a timeseries is used (also includes any makeTimeseries-based data).
* **Values**: a selection of one or more values that your chart graphs over time.
* **Names**: the elements displayed, for example, in the legend and series names.

## Area chart options

To learn about options quickly and decide what works best for you, turn options on and off and see the effect immediately on your chart. For example, does it look best with a label or without? Turn that option on and off and see for yourself.

### Color palettes

You can select a color palette from the list under **Color palettes**.

For a line chart, area chart, or bar chart, you can optionally [override the selected color palette](#series-overrides) for any series as needed.

### Legend position

Select where to display the visualization legend:

* **Automatic**âDynatrace chooses an appropriate location
* **Hidden**âno legend is displayed
* **Bottom**âthe legend is displayed along the bottom of the visualization
* **Right**âthe legend is displayed on the right side of the visualization

### Legend fields

Select which elements to display in the legend.

### Null values

**Connect null values**âspecifies whether to connect null values in the visualization.

### Time axis

Selects the X-axis.

### Left axis

Sets the scale of the left axis:

* **Logarithmic**
* **Linear**

### Min

The minimum of the visualization range.

* **Auto**âDynatrace automatically selects a suitable minimum based on data (0 or min-value).
* **Min-value**âThe minimum is set to the minimum data value.
* **Custom**âDisplays an edit box for you to enter a custom minimum value.

### Max

The maximum of the visualization range.

* **Auto**âDynatrace automatically selects a suitable maximum based on data (0 or max-value).
* **Max-value**âThe maximum is set to the maximum data value.
* **Custom**âDisplays an edit box for you to enter a custom maximum value.

### Label

Vertical text to display as a label for the Y-axis.

### Series overrides

For a line chart, area chart, or bar chart, you can optionally override the selected color palette for any series as needed.

The **Series overrides** section lists all configured overrides.

To add or change an override for a series

1. Edit the visualization tile.
2. Select the series for which you want to override the palette color. There are two ways to select a series:

   * On the graph, select the series and then select **Edit series** from the pop-up window
   * Select **Add override** in the **Series overrides** section in the lower-right corner of the page and then select the series from the list.
3. Change the **Color** setting to the color you want to display for the selected series.
4. Select **Update** to save your changes to the dashboard.

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


---


## Source: visualization-chart-band.md


---
title: Band chart visualization
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-chart-band
scraped: 2026-02-15T21:16:37.030713
---

# Band chart visualization

# Band chart visualization

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jul 08, 2022

When to use a band chart visualization

Use a band chart visualization:

* When you want to see the range or variability of data points. For instance, to forecast the data, or to show confidence intervals.
* When you want to show multiple statistical measures for the same data point to statistically analyze them. For example, when comparing the maximum and minimum of pod utilization over time to find proper limits.

## Example

![Band chart example](https://dt-cdn.net/images/band-chart-686-aeeec95104.png)

The chart above is based on the following query.

```
timeseries avg=avg(dt.host.cpu.load),



max=max(dt.host.cpu.load),



min=min(dt.host.cpu.load),



by:dt.entity.host



| limit 1
```

In general, to create a band chart similar to the one above, use [timeseries](/docs/platform/grail/dynatrace-query-language/commands/metric-commands#timeseries "DQL metric commands") to specify a DQL query that has the following:

* `max` (or `upper`) to define the upper limit of the band
* `min` (or `lower`) to define the lower limit of the band
* some third series to draw the line

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
* **Open with**âfor details, see [Drilldowns and navigation](/docs/analyze-explore-automate/dashboards-and-notebooks/open-with "Drill down from Dashboards and Notebooks using links based on intents or URLs.").

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

A band chart graphs a value over time, with upper and lower limits of the band.

In general, use [timeseries](/docs/platform/grail/dynatrace-query-language/commands/metric-commands#timeseries "DQL metric commands") to specify a DQL query that has the following:

* `max` (or `upper`) to define the upper limit of the band.
* `min` (or `lower`) to define the lower limit of the band.
* A third series to draw the line

So the mapping needs to include the following:

* **Time**: the column of your result that is used for the X-axis ([timestamp](/docs/platform/grail/dynatrace-query-language/data-types#timestamp "A list of DQL data types.") or [timeframe](/docs/platform/grail/dynatrace-query-language/data-types#timeframe "A list of DQL data types.")).
* **Interval**: this value is automatically mapped and canât be changed. It lets you know which fields are mapped for timeseries-based results. It takes the first available interval field from the result set whenever a timeseries is used (also includes any makeTimeseries-based data).
* **Band min values**: the upper limit of the band.
* **Band max values**: the lower limit of the band.
* **Values**: a selection of one or more values that your chart graphs over time.
* **Names**: the elements displayed, for example, in the legend and series names.

## Band chart options

To learn about options quickly and decide what works best for you, turn options on and off and see the effect immediately on your chart. For example, does it look best with a label or without? Turn that option on and off and see for yourself.

### Color palettes

You can select a color palette from the list under **Color palettes**.

For a line chart, area chart, or bar chart, you can optionally [override the selected color palette](#series-overrides) for any series as needed.

### Legend position

Select where to display the visualization legend:

* **Automatic**âDynatrace chooses an appropriate location
* **Hidden**âno legend is displayed
* **Bottom**âthe legend is displayed along the bottom of the visualization
* **Right**âthe legend is displayed on the right side of the visualization

### Null values

**Connect null values**âspecifies whether to connect null values in the visualization.

### Left axis

Sets the scale of the left axis:

* **Logarithmic**
* **Linear**

### Min

The minimum of the visualization range.

* **Auto**âDynatrace automatically selects a suitable minimum based on data (0 or min-value).
* **Min-value**âThe minimum is set to the minimum data value.
* **Custom**âDisplays an edit box for you to enter a custom minimum value.

### Max

The maximum of the visualization range.

* **Auto**âDynatrace automatically selects a suitable maximum based on data (0 or max-value).
* **Max-value**âThe maximum is set to the maximum data value.
* **Custom**âDisplays an edit box for you to enter a custom maximum value.

### Label

Vertical text to display as a label for the Y-axis.

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


---


## Source: visualization-chart-bar-categorical.md


---
title: Categorical chart visualization
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-chart-bar-categorical
scraped: 2026-02-15T21:16:10.283090
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
* **Open with**âfor details, see [Drilldowns and navigation](/docs/analyze-explore-automate/dashboards-and-notebooks/open-with "Drill down from Dashboards and Notebooks using links based on intents or URLs.").

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


---


## Source: visualization-chart-bar.md


---
title: Bar chart visualization
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-chart-bar
scraped: 2026-02-15T21:16:41.437389
---

# Bar chart visualization

# Bar chart visualization

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Jul 08, 2022

When to use a bar chart visualization

Use a bar chart:

* When you want to show the frequency of a single or a few (2-3) different categories over time.
* When you want to compare such categories and their contribution to the whole over time. A bar chart allows you to directly compare the values of different categories, which correspond to the length of the bar, similar to an area chart. This is particularly useful when you have discrete categorical data and you want to highlight differences.
* When you want to show ranking or order of data.

## Example

![Bar chart example](https://dt-cdn.net/images/bar-chart-777-54ca33eff5.png)

The chart above is based on the following query.

```
timeseries avg(dt.host.cpu.usage)
```

* The visualization type is set to **Bar chart**.
* Other options are set to defaults.

## Chart interactions

To access the chart tools:

* When space is limited, hover over the chart and select  **Chart tools** to open a menu of chart tools.
* When there is sufficient space, the chart tools are displayed in a toolbar.

  ![Timeseries chart toolbar - full](https://dt-cdn.net/images/chart-tool-bar-269-c1d9a7bc39.png)

  When you hover over the chart, the chart toolbar is displayed by default in the lower-right corner of the chart and is collapsed.

### Toolbar options

**Icon**

**Name**

**Keyboard shortcut**

**Action**

**Move**

none

Move the chart toolbar. Select and drag the  icon.

**Explore**

`E`

Explore a section of the chart. Select **Explore**, and then click and drag left or right to select a section of the chart. The chart zooms to display the selected area.

**Pan**

`P`

Pan the chart to the left or right. Select **Pan**, and then click and drag left or right.

**Zoom in**

`Ctrl+Up`

Zoom in to the chart.

**Zoom out**

`Ctrl+Down`

Zoom out from the chart.

**Reset**

`R`

Restore the chart zoom level and timeframe to their original states.

**Collapse**

none

Shrink the chart toolbar to just  and .

**Expand**

none

Show the entire chart toolbar.

### Zoom rules

For a timeseries chart (Line, Area, Bar):

* You can't zoom on the chart if the timeframe is set in the DQL query.
* ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**

  If you zoom on a tile without a custom tile timeframe, the global timeframe for the dashboard is updated accordingly, so timeframes stay in sync across the dashboard except where a tile has its own overriding timeframe.

  If you zoom on a tile with a custom tile timeframe but without a timeframe in the query, the selected timeframe is applied to the custom tile timeframe and the changed timeframe is reflected in the dashboard.
* ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**

  If you zoom in a timeseries in a notebook section, the timeframe of the section changes, and the change is persisted in the notebook.

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
* **Open with**âfor details, see [Drilldowns and navigation](/docs/analyze-explore-automate/dashboards-and-notebooks/open-with "Drill down from Dashboards and Notebooks using links based on intents or URLs.").

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

For example, when working with DQL and a timeseries, in the result we have a column with a value array for each series (one row with that one cell of values). For a timeseries, this mapping is done fully automatically, but the data mapping shows you which underlying column is mapped.

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

Data mapping restrictions for event-based graph visualizations

Dynatrace version 1.322+

#### What changed?

To make data mapping easier and more intuitive, weâve restricted certain fields in the interface for event-based charts, showing only the most relevant options.

* **Before**: Prior to Dynatrace version 1.322, fields such as `timestamp`, `interval`, and `duration` could be mapped to the "names" option within the data mapping surface.
* **After**: Starting with Dynatrace version 1.322, these fields are no longer available for selection in the "names" option.

#### Impact

If your ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** or ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** charts rely on these fields, the affected tiles will display an error message, such as:

`Selected field unavailable. The field "" is no longer available. Try adjusting the data, or select another field or visualization.`

#### Resolution

To resolve this issue

1. Replace the existing `summarize` command with `makeTimeseries`.
2. Replace the `by: { ... 4h }` parameter with `interval: 4h` while using the same interval as with the previous configuration in the `by`.

After applying these changes, the data mapping will correctly allow suitable fields for the "names" option, and your tiles will function as expected.

### Visualization-specific data mapping settings

A bar chart graphs one or more values over time, so the mapping needs to include the following:

* **Time**: the column of your result that is used for the X-axis ([timestamp](/docs/platform/grail/dynatrace-query-language/data-types#timestamp "A list of DQL data types.") or [timeframe](/docs/platform/grail/dynatrace-query-language/data-types#timeframe "A list of DQL data types.")).
* **Interval**: this value is automatically mapped and canât be changed. It lets you know which fields are mapped for timeseries-based results. It takes the first available interval field from the result set whenever a timeseries is used (also includes any makeTimeseries-based data).
* **Values**: a selection of one or more values that your chart graphs over time.
* **Names**: the elements displayed, for example, in the legend and series names.

## Bar chart options

To learn about options quickly and decide what works best for you, turn options on and off and see the effect immediately on your chart. For example, does it look best with a label or without? Turn that option on and off and see for yourself.

### Color palettes

You can select a color palette from the list under **Color palettes**.

For a line chart, area chart, or bar chart, you can optionally [override the selected color palette](#series-overrides) for any series as needed.

### Legend position

Select where to display the visualization legend:

* **Automatic**âDynatrace chooses an appropriate location
* **Hidden**âno legend is displayed
* **Bottom**âthe legend is displayed along the bottom of the visualization
* **Right**âthe legend is displayed on the right side of the visualization

### Legend fields

Select which elements to display in the legend.

### Time axis

Selects the X-axis.

### Left axis

Sets the scale of the left axis:

* **Logarithmic**
* **Linear**

### Min

The minimum of the visualization range.

* **Auto**âDynatrace automatically selects a suitable minimum based on data (0 or min-value).
* **Min-value**âThe minimum is set to the minimum data value.
* **Custom**âDisplays an edit box for you to enter a custom minimum value.

### Max

The maximum of the visualization range.

* **Auto**âDynatrace automatically selects a suitable maximum based on data (0 or max-value).
* **Max-value**âThe maximum is set to the maximum data value.
* **Custom**âDisplays an edit box for you to enter a custom maximum value.

### Label

Vertical text to display as a label for the Y-axis.

### Stack series

Specifies how to stack series: by absolute or relative values.

### Series overrides

For a line chart, area chart, or bar chart, you can optionally override the selected color palette for any series as needed.

The **Series overrides** section lists all configured overrides.

To add or change an override for a series

1. Edit the visualization tile.
2. Select the series for which you want to override the palette color. There are two ways to select a series:

   * On the graph, select the series and then select **Edit series** from the pop-up window
   * Select **Add override** in the **Series overrides** section in the lower-right corner of the page and then select the series from the list.
3. Change the **Color** setting to the color you want to display for the selected series.
4. Select **Update** to save your changes to the dashboard.

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


---


## Source: visualization-chart-donut.md


---
title: Donut visualization
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-chart-donut
scraped: 2026-02-15T21:16:24.332168
---

# Donut visualization

# Donut visualization

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jul 08, 2022

When to use a donut visualization

Use a donut visualization:

* When you have just a few (no more than 5 to 7) clearly distinguishable categories/slices in your data.
* When you want to save space and combine a single value with a breakdown.

## Example

![Donut chart example](https://dt-cdn.net/images/donut-chart-652-a27c8f767b.png)

The above donut chart is based on the following query.

```
fetch logs



| summarize count(), by:{loglevel}
```

In the **Donut chart options** section, **Show total** is turned on to show the `1.6M` value in the center of the donut.

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
* **Open with**âfor details, see [Drilldowns and navigation](/docs/analyze-explore-automate/dashboards-and-notebooks/open-with "Drill down from Dashboards and Notebooks using links based on intents or URLs.").

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

For a donut chart, the data mapping section includes:

* **Values**: the value to be reflected in the size of a slice.
* **Categories**: the column of your result that is displayed as a slice of the donut.

## Donut chart options

To learn about options quickly and decide what works best for you, turn options on and off and see the effect immediately on your chart. For example, does it look best with a label or without? Turn that option on and off and see for yourself.

### Color palettes

You can select a color palette from the list under **Color palettes**.

### Slice

Set **Slice** to the unit by which you want to cut up your chart. **Slice** and **Value** together determine how to map your query results to your chart.

### Value

Set **Value** to the value that determines the size of slices. **Slice** and **Value** together determine how to map your query results to your chart.

### Chart

Use **Hide labels** to display or hide the labels on your chart.

### Legend position

Select where to display the visualization legend:

* **Automatic**âDynatrace chooses an appropriate location
* **Hidden**âno legend is displayed
* **Bottom**âthe legend is displayed along the bottom of the visualization
* **Right**âthe legend is displayed on the right side of the visualization

### Total value

To show the total value in the center of a donut visualization, turn on **Show total**.

Use **Relative values (%)** to display chart values as absolute values or relative values (percentages of the total).

### Merges slices

Use the **Merge slices** settings to determine how to merge slices in your chart.

* **Absolute**

  For example, if you have three slices with the following values:

  + Slice 1: `40`
  + Slice 2: `5`
  + Slice 3: `5`

  If you select **Absolute** and set **Absolute limit** to `10`, slices 2 and 3 will merge into one group with the label set in **Group label**.
* **Relative (%)**

  For example, if you have three slices with the following values:

  + Slice 1 - `40` (80% of the total)
  + Slice 2 - `5` (10% of the total)
  + Slice 3 - `5` (10% of the total)

  If you select **Relative (%)** and set **Relative limit** to `20` (20%), slices 2 and 3 (which are each below the relative value of 20%) will merge into one group with the label set in **Group label**.
* **Number of slices**

  For example, if you have three slices with the following values:

  + Slice 1: `40`
  + Slice 2: `5`
  + Slice 3: `5`

  If you select **Number of slices** and set **Slice limit** to `2`, the first two slices will be displayed separately and the others will be merged into one group with the label set in **Group label**.

### Add color override

To override the color of a chart item, select **Add color override**, select the item from the list, and then set **Color** to the color you want to use for the selected item.

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


---


## Source: visualization-chart-line.md


---
title: Line chart visualization
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-chart-line
scraped: 2026-02-15T21:16:34.227797
---

# Line chart visualization

# Line chart visualization

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Jul 08, 2022

When to use a line chart visualization

Use a line chart visualization:

* When you want to analyze measurements and their trend over time. For example, to see whether all disks run out of capacity quickly or not.
* When you want to compare multiple series over time. For example, to see whether all your pods are equally utilized.
* When you want to find relationships or correlations between multiple series representing different variables. For example, to analyze whether certain application errors directly influence the number of bookings.

## Examples

### Example 1

![Line chart example](https://dt-cdn.net/images/line-chart-789-a56080c3c4.png)

The chart above is based on the following query.

```
timeseries avg(dt.host.cpu.usage)
```

* The visualization type is set to **Line chart**.
* Other options are set to defaults.

### Example 2

![Line chart example: code - multiple series](https://dt-cdn.net/images/line-chart-code-multiple-series-717-bf9d7c7781.png)

Example code

```
/*



* This example shows how to map data to use the built-in visualization for custom data.



*/



export default async function () {



// Sample the exponential function 10 times at 1-minute intervals.



const sampleCount = 10;



return {



records: new Array(sampleCount).fill(null).map((_, index, array) => {



const invertedIndex = array.length - index;



const time = new Date().getTime();



return {



'my series': Math.exp((index * 3) / 10),



'my series 2': Math.exp((index * 2) / 8),



timeframe: {



start: time - 1000 * 60 * invertedIndex,



end: time - 1000 * 60 * (invertedIndex - 1),



},



};



}),



types: [



{



indexRange: [0, sampleCount - 1],



mappings: {



timeframe: { type: 'timeframe' },



'my series': { type: 'double' },



'my series 2': {type: 'double'}



},



},



],



};



}
```

### Example 3

![Line chart example 3](https://dt-cdn.net/images/line-chart-example-03-703-a1bfea0dd7.png)

Example code

```
/*



* This example shows how to visualize your data without explicitly describing



* the types.



*/



export default async function () {



// Take 120 samples of a sine wave for a full period.



const sampleCount = 120;



return new Array(sampleCount).fill(null).map((_, index, array) => {



const invertedIndex = array.length - index;



const time = new Date().getTime();



return {



timestamp: new Date(time - 1000 * 60 * invertedIndex).toISOString(),



value: Math.sin((index / (array.length - 1)) * (2 * Math.PI)),



};



});



}
```

## Chart interactions

To access the chart tools:

* When space is limited, hover over the chart and select  **Chart tools** to open a menu of chart tools.
* When there is sufficient space, the chart tools are displayed in a toolbar.

  ![Timeseries chart toolbar - full](https://dt-cdn.net/images/chart-tool-bar-269-c1d9a7bc39.png)

  When you hover over the chart, the chart toolbar is displayed by default in the lower-right corner of the chart and is collapsed.

### Toolbar options

**Icon**

**Name**

**Keyboard shortcut**

**Action**

**Move**

none

Move the chart toolbar. Select and drag the  icon.

**Explore**

`E`

Explore a section of the chart. Select **Explore**, and then click and drag left or right to select a section of the chart. The chart zooms to display the selected area.

**Pan**

`P`

Pan the chart to the left or right. Select **Pan**, and then click and drag left or right.

**Zoom in**

`Ctrl+Up`

Zoom in to the chart.

**Zoom out**

`Ctrl+Down`

Zoom out from the chart.

**Reset**

`R`

Restore the chart zoom level and timeframe to their original states.

**Collapse**

none

Shrink the chart toolbar to just  and .

**Expand**

none

Show the entire chart toolbar.

### Zoom rules

For a timeseries chart (Line, Area, Bar):

* You can't zoom on the chart if the timeframe is set in the DQL query.
* ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**

  If you zoom on a tile without a custom tile timeframe, the global timeframe for the dashboard is updated accordingly, so timeframes stay in sync across the dashboard except where a tile has its own overriding timeframe.

  If you zoom on a tile with a custom tile timeframe but without a timeframe in the query, the selected timeframe is applied to the custom tile timeframe and the changed timeframe is reflected in the dashboard.
* ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**

  If you zoom in a timeseries in a notebook section, the timeframe of the section changes, and the change is persisted in the notebook.

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
* **Open with**âfor details, see [Drilldowns and navigation](/docs/analyze-explore-automate/dashboards-and-notebooks/open-with "Drill down from Dashboards and Notebooks using links based on intents or URLs.").

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

For example, when working with DQL and a timeseries, in the result we have a column with a value array for each series (one row with that one cell of values). For a timeseries, this mapping is done fully automatically, but the data mapping shows you which underlying column is mapped.

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

Data mapping restrictions for event-based graph visualizations

Dynatrace version 1.322+

#### What changed?

To make data mapping easier and more intuitive, weâve restricted certain fields in the interface for event-based charts, showing only the most relevant options.

* **Before**: Prior to Dynatrace version 1.322, fields such as `timestamp`, `interval`, and `duration` could be mapped to the "names" option within the data mapping surface.
* **After**: Starting with Dynatrace version 1.322, these fields are no longer available for selection in the "names" option.

#### Impact

If your ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** or ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** charts rely on these fields, the affected tiles will display an error message, such as:

`Selected field unavailable. The field "" is no longer available. Try adjusting the data, or select another field or visualization.`

#### Resolution

To resolve this issue

1. Replace the existing `summarize` command with `makeTimeseries`.
2. Replace the `by: { ... 4h }` parameter with `interval: 4h` while using the same interval as with the previous configuration in the `by`.

After applying these changes, the data mapping will correctly allow suitable fields for the "names" option, and your tiles will function as expected.

### Visualization-specific data mapping settings

A line chart graphs one or more values over time, so the mapping needs to include the following:

* **Time**: the column of your result that is used for the X-axis ([timestamp](/docs/platform/grail/dynatrace-query-language/data-types#timestamp "A list of DQL data types.") or [timeframe](/docs/platform/grail/dynatrace-query-language/data-types#timeframe "A list of DQL data types.")).
* **Interval**: this value is automatically mapped and canât be changed. It lets you know which fields are mapped for timeseries-based results. It takes the first available interval field from the result set whenever a timeseries is used (also includes any makeTimeseries-based data).
* **Values**: a selection of one or more values that your chart graphs over time.
* **Names**: the elements displayed, for example, in the legend and series names.

## Line chart options

To learn about options quickly and decide what works best for you, turn options on and off and see the effect immediately on your chart. For example, does it look best with a label or without? Turn that option on and off and see for yourself.

### Color palettes

You can select a color palette from the list under **Color palettes**.

For a line chart, area chart, or bar chart, you can optionally [override the selected color palette](#series-overrides) for any series as needed.

### Legend position

Select where to display the visualization legend:

* **Automatic**âDynatrace chooses an appropriate location
* **Hidden**âno legend is displayed
* **Bottom**âthe legend is displayed along the bottom of the visualization
* **Right**âthe legend is displayed on the right side of the visualization

### Legend fields

Select which elements to display in the legend.

### Null values

**Connect null values**âspecifies whether to connect null values in the visualization.

### Time axis

Selects the X-axis.

### Left axis

Sets the scale of the left axis:

* **Logarithmic**
* **Linear**

### Min

The minimum of the visualization range.

* **Auto**âDynatrace automatically selects a suitable minimum based on data (0 or min-value).
* **Min-value**âThe minimum is set to the minimum data value.
* **Custom**âDisplays an edit box for you to enter a custom minimum value.

### Max

The maximum of the visualization range.

* **Auto**âDynatrace automatically selects a suitable maximum based on data (0 or max-value).
* **Max-value**âThe maximum is set to the maximum data value.
* **Custom**âDisplays an edit box for you to enter a custom maximum value.

### Label

Vertical text to display as a label for the Y-axis.

### Series overrides

For a line chart, area chart, or bar chart, you can optionally override the selected color palette for any series as needed.

The **Series overrides** section lists all configured overrides.

To add or change an override for a series

1. Edit the visualization tile.
2. Select the series for which you want to override the palette color. There are two ways to select a series:

   * On the graph, select the series and then select **Edit series** from the pop-up window
   * Select **Add override** in the **Series overrides** section in the lower-right corner of the page and then select the series from the list.
3. Change the **Color** setting to the color you want to display for the selected series.
4. Select **Update** to save your changes to the dashboard.

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


---


## Source: visualization-chart-pie.md


---
title: Pie visualization
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-chart-pie
scraped: 2026-02-15T21:16:38.418495
---

# Pie visualization

# Pie visualization

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jul 08, 2022

## Example

When to use a pie visualization

Use a pie visualization:

* When you have just a few (no more than 5 to 7) clearly distinguishable categories/slices in your data. In such cases, a pie visualization can be simple and easy to read.
* When you want to show proportions or percentages of a whole. For example, showing pods by phase.
* When you want to highlight composition. For example, you might use a pie visualization to illustrate the distribution of errors by error type.

![Pie chart example](https://dt-cdn.net/images/pie-chart-642-aa7d7a76a4.png)

The above pie chart is based on the following query.

```
fetch logs



| summarize count(), by:{loglevel}
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
* **Open with**âfor details, see [Drilldowns and navigation](/docs/analyze-explore-automate/dashboards-and-notebooks/open-with "Drill down from Dashboards and Notebooks using links based on intents or URLs.").

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

For a pie chart, the data mapping section includes:

* **Values**: the value to be reflected in the size of a slice.
* **Categories**: the column of your result that is displayed as a slice of the pie.

## Pie chart options

To learn about options quickly and decide what works best for you, turn options on and off and see the effect immediately on your chart. For example, does it look best with a label or without? Turn that option on and off and see for yourself.

### Color palettes

You can select a color palette from the list under **Color palettes**.

### Slice

Set **Slice** to the unit by which you want to cut up your chart. **Slice** and **Value** together determine how to map your query results to your chart.

### Value

Set **Value** to the value that determines the size of slices. **Slice** and **Value** together determine how to map your query results to your chart.

### Chart

Use **Hide labels** to display or hide the labels on your chart.

### Legend position

Select where to display the visualization legend:

* **Automatic**âDynatrace chooses an appropriate location
* **Hidden**âno legend is displayed
* **Bottom**âthe legend is displayed along the bottom of the visualization
* **Right**âthe legend is displayed on the right side of the visualization

### Total value

Use **Relative values (%)** to display chart values as absolute values or relative values (percentages of the total).

### Merges slices

Use the **Merge slices** settings to determine how to merge slices in your chart.

* **Absolute**

  For example, if you have three slices with the following values:

  + Slice 1: `40`
  + Slice 2: `5`
  + Slice 3: `5`

  If you select **Absolute** and set **Absolute limit** to `10`, slices 2 and 3 will merge into one group with the label set in **Group label**.
* **Relative (%)**

  For example, if you have three slices with the following values:

  + Slice 1 - `40` (80% of the total)
  + Slice 2 - `5` (10% of the total)
  + Slice 3 - `5` (10% of the total)

  If you select **Relative (%)** and set **Relative limit** to `20` (20%), slices 2 and 3 (which are each below the relative value of 20%) will merge into one group with the label set in **Group label**.
* **Number of slices**

  For example, if you have three slices with the following values:

  + Slice 1: `40`
  + Slice 2: `5`
  + Slice 3: `5`

  If you select **Number of slices** and set **Slice limit** to `2`, the first two slices will be displayed separately and the others will be merged into one group with the label set in **Group label**.

### Add color override

To override the color of a chart item, select **Add color override**, select the item from the list, and then set **Color** to the color you want to use for the selected item.

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


---


## Source: visualization-chart-single-value.md


---
title: Single value visualization
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-chart-single-value
scraped: 2026-02-15T21:16:07.705906
---

# Single value visualization

# Single value visualization

* Latest Dynatrace
* How-to guide
* 2-min read
* Updated on Sep 17, 2025

When to use a single value visualization

Use a single value visualization when you want to:

* Show a single aggregated measurement and its trend over time.
* Express important business-related Key Performance Indicators (KPIs).
* Express infrastructure-related critical Service Level Objectives (SLOs).

## Examples

### Example 1 - DQL-based single value

![Single value example](https://dt-cdn.net/images/capture-2023-12-11-125352-918-338863a608.webp)

The visualization above is based on the following query.

```
timeseries sparkline=avg(dt.host.cpu.usage)



| fieldsAdd value=arrayAvg(sparkline)
```

In this example, the chart option selections included:

* **Record field**: `value`
* **Alignment**: `Center`
* **Show trend**: `On`
* **Trend value**: `Relative`
* **Show sparkline**: `On`
* **Sparkline**: `sparkline`

### Example 2 - Code-based single value

![Single value chart example](https://dt-cdn.net/images/single-value-example-01-519-29fd55a191.png)

Example code

```
/*



* This example shows how to map data to use the built-in visualization for custom data.



*/



export default async function () {



return {



records: [



{



value: 'CPU usage',



interval: '60000000000',



timeframe: {



start: '2023-11-13T07:24:00.000Z',



end: '2023-11-13T09:25:00.000Z',



},



series: [1832, 997, 432, 997, 2343, 997, 544, 997, 234],



},



],



types: [



{



mappings: {



value: {



type: 'string',



},



interval: {



type: 'duration',



},



timeframe: {



type: 'timeframe',



},



series: {



type: 'array',



types: [



{



mappings: {



element: {



type: 'double',



},



},



indexRange: [0, 120],



},



],



},



},



indexRange: [0, 0],



},



],



};



}
```

In this example, the chart option selections included:

* **Record field**: `value`
* **Alignment**: `Center`
* **Icon**: `Codeicon`
* **Show trend**: `On`
* **Trend value**: `Relative`
* **Show sparkline**: `On`

### Example 3 - Single value grid

![Example single value with grid](https://dt-cdn.net/images/single-value-example-03-grid-obfuscated-1368-5d87f06ff3.png)

The visualization above is based on the following query.

```
timeseries sparkline=avg(dt.host.cpu.usage), value=avg(dt.host.cpu.usage, scalar:true), by:{dt.entity.host}



| fieldsAdd name=entityName(dt.entity.host)



| sort arrayAvg(value), direction:"descending"



| limit 5
```

In this example, the chart option selections included:

* **Record field**: `value`
* **Show label**: `Data` > `name`
* **Alignment**: `Center`
* **Show trend**: `On`
* **Trend value**: `Relative`
* **Show sparkline**: `On`
* **Sparkline**: `sparkline`

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
* **Open with**âfor details, see [Drilldowns and navigation](/docs/analyze-explore-automate/dashboards-and-notebooks/open-with "Drill down from Dashboards and Notebooks using links based on intents or URLs.").

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

For a single-value chart, the data mapping section includes:

* **Single value**: the column of your result that is displayed in the single value visualization.
* **Sparkline**: the value to be reflected in a sparkline in the single value visualization. This also affects the trend, which is calculated as the difference between the first and last elements of the timeseries selected as a sparkline.
* **Interval**: this value is automatically mapped and canât be changed. It lets you know which fields are mapped for timeseries-based results. It takes the first available interval field from the result set whenever a timeseries is used (also includes any makeTimeseries-based data).
* **Trend**: Select `Auto` to automatically calculate the trend based on the data provided for the sparkline. Select `Custom` to choose a numeric field.

Grid view

When the result consists of multiple rows:

* Previously, only the last result was shown in a single value visualization.
* Since Dynatrace version 1.324, the single value visualization automatically switches to a grid view, with each value displayed as a separate single value. The maximum number of values displayed in the grid is 25.

Advantages:

* Improves transparency and prevents potentially misleading interpretations.
* No need for multiple visualizations of related results. All data is displayed in a consistent format on a single grid.

If you prefer the previous behavior (without the grid), you can apply a DQL [limit](/docs/platform/grail/dynatrace-query-language/commands/ordering-commands#limit "DQL ordering commands") and a [sort](/docs/platform/grail/dynatrace-query-language/commands/ordering-commands#sort "DQL ordering commands") command using [DQL](/docs/platform/grail/dynatrace-query-language/commands "A list of DQL commands.") or the [Explore interface](/docs/analyze-explore-automate/dashboards-and-notebooks/explore-data "Explore your data with our point-and-click interface.").

## Single value options

To learn about options quickly and decide what works best for you, turn options on and off and see the effect immediately on your chart. For example, does it look best with a label or without? Turn that option on and off and see for yourself.

### General

Use these options to specify the general display options of your visualization.

* **Show label** specifies whether to show the label on the visualization.

  + **Label** is the text of the label you want to show, such as `World ð trend`. This configuration option is displayed only if **Show label** is turned on.

    To set a label via DQL using an alias, turn on **Show label** but don't set **Label**.
* **Format** specifies whether to format values on the visualization.
* **Record field** specifies the field to display on the visualization.
* **Alignment** specifies left, center, or right alignment for displayed visualization elements.
* **Icon** specifies the icon to display before the value.

### Trend and Sparkline

Use these options to specify the trend and sparkline options of your visualization.

* **Show trend** turns the trend icon and value on or off.

  The following configuration option is displayed only if **Show trend** is turned on:

  + **Trend value** specifies whether to show an absolute or percentage trend value.
* **Show sparkline** turns the sparkline on or off.

  The following configuration options are displayed only if **Show sparkline** is turned on:

  + **Sparkline color** specifies the color of the sparkline.
  + **Sparkline variant** specifies whether to display the sparkline as a line or an area.
  + **Record field** specifies the record field to display as a sparkline on the visualization.
  + **Show ticks** specifies whether to display values along the X-axis.

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


---


## Source: visualization-gauge.md


---
title: Gauge chart
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-gauge
scraped: 2026-02-15T21:16:21.267676
---

# Gauge chart

# Gauge chart

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Mar 03, 2025

When to use gauge visualization

Use a gauge to visualize a single numerical value as a gauge.

## Examples

### Example 1

![Gauge visualization: example 1](https://dt-cdn.net/images/gauge-example-01-479-24a2a01700.png)

The gauge visualization above is based on the following query, which calculates `CPU` as the average host CPU usage. In the **Data mapping** settings, **Gauge value** is then set as `CPU`.

```
timeseries avg(dt.host.cpu.usage)



| fieldsAdd CPU = arrayAvg(`avg(dt.host.cpu.usage)`)



| fieldsKeep CPU
```

The **Visual** tab settings are as follows:

Section

Settings

Data mapping

* **Gauge value** = `CPU`

Gauge bar

* **Show label** = turned off
* **Min value** = set to `Auto`
* **Max value** = set to `Auto`

Color

* **Bar color** = `62903c`
* **Custom colors** =

  + `60` and (for the custom color) `dc671e`
  + `80` and (for the custom color) `cd3c44`

Units and formats

* Selected value = `CPU`
* **Unit** = `Percent (%)`
* **Displayed unit** = `Auto`
* **Decimals** = `0.00`

### Example 2

![Gauge visualization: example 2](https://dt-cdn.net/images/gauge-example-02-476-681bd11f53.png)

The gauge visualization above is based on the following query, which calculates `pctActive` as the percentage of total problems that are open. In the **Data mapping** settings, **Gauge value** is then set as `pctActive`.

```
fetch dt.davis.problems



| summarize count = count(), by:{event.status}



| summarize { active=toDouble(takeAny(if(event.status=="ACTIVE", count))), closed=toDouble(takeAny(if(event.status=="CLOSED", count)))}



| fieldsAdd total = active + closed



| fieldsAdd pctActive = (active / total) * 100



| fieldsKeep pctActive
```

The **Visual** tab settings are as follows:

Section

Settings

Data mapping

* **Gauge value** = `pctActive`

Gauge bar

* **Show label** = turned on and set to `Percentage of Open Problems`
* **Min value** = set to `Auto`
* **Max value** = set to `Auto`

Color

* **Bar color** = `438FB1`
* **Custom colors** = `90` and (for the custom color) `c21930`

Units and formats

* Selected value = `pctActive`
* **Unit** = `Percent (%)`
* **Displayed unit** = `Auto`
* **Decimals** = `0`

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

For a gauge chart, the data mapping section includes:

* **Gauge value**: the numeric value you want to represent as a gauge.

## Gauge bar

### Show label

To display a string in the center of the gauge, turn on **Show label** and enter the string.

### Min value

Determines where the gauge starts on the left.

* **Auto**âstarts the gauge at `0`
* **Custom**âspecifies a different gauge start point

### Max value

Determines where the gauge ends on the right.

* **Auto**

  + If the gauge value is less than `100`, the right end of the gauge = `100`
  + If the gauge value is greater than `100`, the right end of the gauge is the gauge value
* **Custom**âspecifies a different gauge end point

## Color

* To set the basic color of the gauge, select the desired color from the **Bar color** menu (or open the **Bar color** menu and enter the hex code for the color).
* You can add one or more **Custom colors** to define the colors to display when the gauge reaches certain values.

  For each custom color, enter the gauge value and set the corresponding color to use when the gauge value reaches that value. A vertical line is displayed on the gauge for each custom color value.

  Example

  Suppose you want your gauge to remain green normally, but turn yellow if it reaches `80`, and turn red if it reaches `90`:

  + Set **Bar color** to the desired shade of green
  + Select  **Color** and add a custom color row with the value `80` and the desired shade of yellow selected. If the gauge value reaches `80`, the gauge will turn yellow.
  + Select  **Color** again and add a custom color row with the value `90` and the desired shade of red selected. If the gauge value reaches `90`, the gauge will turn red.

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


---


## Source: visualization-heatmap.md


---
title: Heatmap visualization
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-heatmap
scraped: 2026-02-15T21:16:25.641086
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
* **Open with**âfor details, see [Drilldowns and navigation](/docs/analyze-explore-automate/dashboards-and-notebooks/open-with "Drill down from Dashboards and Notebooks using links based on intents or URLs.").

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


---


## Source: visualization-histogram.md


---
title: Histogram visualization
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-histogram
scraped: 2026-02-15T21:16:19.835272
---

# Histogram visualization

# Histogram visualization

* Latest Dynatrace
* How-to guide
* 3-min read
* Updated on Jun 17, 2025

When to use histogram visualization

Use a histogram to visualize the distribution of numerical values.

## Examples

### Example 1

![Histogram example](https://dt-cdn.net/images/histogram-example-02-b-661-2d1bce193f.png)

The histogram visualization above is based on the following query.

```
fetch spans



| filter span.kind == "server"



| filter duration < 1s



| summarize count(), by:{range(duration, 10ms)}
```

### Example 2

![Histogram example](https://dt-cdn.net/images/histogram-example-03-dark-713-d663a7e1b9.png)

The histogram visualization above is based on the following query of bizevents.

```
fetch bizevents



| filter event.type == "com.easytrade.trade-closed"



| filter direction == "longsell"



| filter amount <= 10000



| summarize count = count(), by:{range(amount, 300)}
```

### Example 3

![Histogram example](https://dt-cdn.net/images/histogram-example-04-754-573d3eed06.png)

The histogram visualization above is based on the following query. This shows the distribution of risk scores for open security events.

The query below has been updated to align with the new Grail security events table. For the complete list of updates and actions needed to accomplish the migration, follow the steps in the [Grail security table migration guide](/docs/secure/threat-observability/migration "Understand the changes in the new Grail security table and learn how to migrate to it.").

```
fetch security.events



| filter event.status == "OPEN"



| summarize count = count(), by:{range(vulnerability.risk.score, 0.5)}
```

### Example 4

![Histogram example](https://dt-cdn.net/images/histogram-example-05-704-a0fdd17c53.png)

The histogram visualization above is based on the following query. This is a variation on the previous example that shows an additional split by the security event status.

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
* **Open with**âfor details, see [Drilldowns and navigation](/docs/analyze-explore-automate/dashboards-and-notebooks/open-with "Drill down from Dashboards and Notebooks using links based on intents or URLs.").

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

The histogram is defined by an array of bins where each bin represents a continuous range of values. The data mapping section includes:

* **Range**: the width (size) of individual bars
* **Values**: the count or frequency (value) that determines the height of individual bars
* **Names**: the elements displayed, for example, in the legend and series names.

## Histogram chart options

To learn about options quickly and decide what works best for you, turn options on and off and see the effect immediately on your chart. For example, does it look best with a label or without? Turn that option on and off and see for yourself.

### Color palettes

You can select a color palette from the list under **Color palettes**.

### Legend position

Select where to display the visualization legend:

* **Automatic**âDynatrace chooses an appropriate location
* **Hidden**âno legend is displayed
* **Bottom**âthe legend is displayed along the bottom of the visualization
* **Right**âthe legend is displayed on the right side of the visualization

### X-axis

Sets the scale of the X-axis:

* **Logarithmic**
* **Linear**

### Min

The minimum value of the visualization's x-axis.

* **Auto**âDynatrace automatically selects a suitable minimum based on data (0 or min-value).
* **Min-value**âThe minimum is set to the minimum data value.
* **Custom**âDisplays an input field for you to enter a custom minimum value.

### Max

The maximum value of the visualization's x-axis.

* **Auto**âDynatrace automatically selects a suitable maximum based on data (0 or max-value).
* **Max-value**âThe maximum is set to the maximum data value.
* **Custom**âDisplays an input field for you to enter a custom maximum value.

### Label

Text to display as a label for the Y-axis.

### Y-axis

Sets the scale of the Y-axis:

* **Logarithmic**
* **Linear**

### Min

The minimum of the visualization range.

* **Auto**âDynatrace automatically selects a suitable minimum based on data (0 or min-value).
* **Min-value**âThe minimum is set to the minimum data value.
* **Custom**âDisplays an edit box for you to enter a custom minimum value.

### Max

The maximum of the visualization range.

* **Auto**âDynatrace automatically selects a suitable maximum based on data (0 or max-value).
* **Max-value**âThe maximum is set to the maximum data value.
* **Custom**âDisplays an edit box for you to enter a custom maximum value.

### Label

Text to display as a label for the Y-axis.

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


---


## Source: visualization-honeycomb.md


---
title: Honeycomb visualization
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-honeycomb
scraped: 2026-02-15T21:16:32.608130
---

# Honeycomb visualization

# Honeycomb visualization

* Latest Dynatrace
* How-to guide
* 2-min read
* Updated on Oct 07, 2025

When to use a honeycomb visualization

A honeycomb visualization offers a compact, high-density view of metrics across numerous entities, ideal for infrastructure monitoring. Use it to identify hotspots, group clusters, and drill down into your data.

## Examples

### Example 1: CPU usage of hosts

![Honeycomb example](https://dt-cdn.net/images/visualization-example-honeycomb-01-859-230a172dea.png)

The honeycomb visualization above is based on the following query.

```
timeseries avg(dt.host.cpu.usage), by:{dt.entity.host}



| fieldsAdd cpu = arrayAvg(`avg(dt.host.cpu.usage)`)
```

* Hover over a cell to see details
* Select a cell to open a menu of cell-specific options

![Honeycomb hover tooltip](https://dt-cdn.net/images/honeycomb-cell-tooltip-295-61aedfcf6e.png)

### Example 2: Davis event status

![Honeycomb example](https://dt-cdn.net/images/visualization-example-honeycomb-02-858-0e630d885d.png)

The honeycomb visualization above is based on the following query.

```
fetch dt.davis.problems
```

### Example 3: Vulnerabilities

![visualization-example-honeycomb](https://dt-cdn.net/images/visualization-example-honeycomb-03-865-12236460d5-703-cfabef4396.png)

The honeycomb visualization above is based on the following query.

The query below has been updated to align with the new Grail security events table. For the complete list of updates and actions needed to accomplish the migration, follow the steps in the [Grail security table migration guide](/docs/secure/threat-observability/migration "Understand the changes in the new Grail security table and learn how to migrate to it.").

```
fetch security.events



| filter event.status == "OPEN"



| summarize takeLast(vulnerability.davis_assessment.score), by:{vulnerability.display_id}
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
* **Open with**âfor details, see [Drilldowns and navigation](/docs/analyze-explore-automate/dashboards-and-notebooks/open-with "Drill down from Dashboards and Notebooks using links based on intents or URLs.").

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

For a honeycomb visualization, the data mapping section includes:

* **Value**: the numeric/string field from your query that you want to map to a cell.
* **Names**: the elements displayed, for example, in the legend and series names.

## Honeycomb options

To learn about options quickly and decide what works best for you, turn options on and off and see the effect immediately on your chart. For example, does it look best with a label or without? Turn that option on and off and see for yourself.

### Cell shape

You can set the cell shape to **Hexagon** (classic honeycomb shape), **Circle**, or **Square**.

### Show labels

Turn this on to display labels in the cells.

### Legend position

Select where to display the visualization legend:

* **Automatic**âDynatrace chooses an appropriate location
* **Hidden**âno legend is displayed
* **Bottom**âthe legend is displayed along the bottom of the visualization
* **Right**âthe legend is displayed on the right side of the visualization

**Automatic** prioritizes the legend placement to the right of the chart area. When the chart width is reduced, the legend is repositioned to the area beneath the chart.

### Color mode, color palette, and custom colors

In **Color mode**, select one of the following color modes.

#### Color palette

When **Color mode** is set to **Color palette**, a **Color palette** list is displayed. Select a color palette from the list.

#### Custom colors

When **Color mode** is set to **Custom colors**, a **Custom colors** section is displayed. Use it to map colors to value ranges. Values that are equal to or greater than the defined value will appear as the defined color. For each range, you select the value and the color.

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


---


## Source: visualization-map-bubble.md


---
title: Bubble map visualization
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-map-bubble
scraped: 2026-02-15T21:16:26.909710
---

# Bubble map visualization

# Bubble map visualization

* Latest Dynatrace
* How-to guide
* 5-min read
* Published Apr 03, 2025

Dashboards version 1.311+ Notebooks version 1.311+

When to use

Use a bubble map to represent values with varying bubble sizes and colors. Examples include error rates of different services, with bubble size representing frequency and color indicating severity, and revenue distribution across regions, with bubble size representing revenue and color indicating growth rate.

## Examples

To try out an example

1. Create a DQL tile in ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** or a DQL section in ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.
2. Copy the example data and paste it into the DQL edit box.
3. Run it.
4. Select the visualization and experiment with the visualization settings.

### Example 1

![Bubble map example](https://dt-cdn.net/images/map-bubble-example-01c-665-52c2ff17ed.png)

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
* **Open with**âfor details, see [Drilldowns and navigation](/docs/analyze-explore-automate/dashboards-and-notebooks/open-with "Drill down from Dashboards and Notebooks using links based on intents or URLs.").

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

For a bubble map visualization, the data mapping section includes:

* **Latitude**: Required Select a value from your query to use for the latitude of each point on the map.
* **Longitude**: Required Select a value from your query to use for the longitude of each point on the map.
* **Radius value**: Required Select a value from your query to use for the radius of the bubble around each point on the map.
* **Color value**: Optional Select a value from your query to use for the color of the bubble around each point on the map.

## Radius

Radius settings determine bubble size.

* **Zoom resize**: Whether to resize the bubble with zoom. Default: off.
* **Scale**: Determines how to scale the bubble radius.

  + **Fixed**: Don't scale the bubble radius.
  + **Linear**: Scale the bubble radius linearly (default).
  + **Log**: Scale the bubble radius logarithmically.
* **Min radius**: Minimum bubble radius. Default: `10`.
* **Max radius**: Maximum bubble radius. Default: `100`.

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


---


## Source: visualization-map-choropleth.md


---
title: Choropleth map visualization
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-map-choropleth
scraped: 2026-02-15T21:16:35.570199
---

# Choropleth map visualization

# Choropleth map visualization

* Latest Dynatrace
* How-to guide
* 4-min read
* Published Apr 03, 2025

Dashboards version 1.311+ Notebooks version 1.311+

When to use

Use a choropleth map to display data with color gradients by country or region. Examples include user experience scores by country, with color gradients indicating satisfaction levels, and market penetration rates by country to identify areas with high and low adoption.

## Examples

To try out an example

1. Create a DQL tile in ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** or a DQL section in ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.
2. Copy the example data and paste it into the DQL edit box.
3. Run it.
4. Select the visualization and experiment with the visualization settings.

### Example 1

![Choropleth example: users by country](https://dt-cdn.net/images/map-choropleth-example-01b-1355-e7eff1aa58.png)

The map above is based on the following data.

```
data



record(geo.country.iso_code = "US", users = toLong(random() * 10000)),



record(geo.country.iso_code = "GB", users = toLong(random() * 10000)),



record(geo.country.iso_code = "DE", users = toLong(random() * 10000)),



record(geo.country.iso_code = "FR", users = toLong(random() * 10000)),



record(geo.country.iso_code = "IT", users = toLong(random() * 10000)),



record(geo.country.iso_code = "ES", users = toLong(random() * 10000)),



record(geo.country.iso_code = "CN", users = toLong(random() * 10000)),



record(geo.country.iso_code = "JP", users = toLong(random() * 10000)),



record(geo.country.iso_code = "IN", users = toLong(random() * 10000)),



record(geo.country.iso_code = "BR", users = toLong(random() * 10000))
```

### Example 2

![Choropleth example: Apdex by country](https://dt-cdn.net/images/map-choropleth-example-02-1366-3c325e0083.png)

The map above is based on the following data.

```
data



record(geo.country.iso_code = "US", apdex = "Good" ),



record(geo.country.iso_code = "GB", apdex = "Good" ),



record(geo.country.iso_code = "DE", apdex = "Poor" ),



record(geo.country.iso_code = "FR", apdex = "Excellent" ),



record(geo.country.iso_code = "IT", apdex = "Fair" ),



record(geo.country.iso_code = "ES", apdex = "Good" ),



record(geo.country.iso_code = "CN", apdex = "Unacceptable" ),



record(geo.country.iso_code = "JP", apdex = "Poor" ),



record(geo.country.iso_code = "IN", apdex = "Good" ),



record(geo.country.iso_code = "BR", apdex = "Fair" )
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
* **Open with**âfor details, see [Drilldowns and navigation](/docs/analyze-explore-automate/dashboards-and-notebooks/open-with "Drill down from Dashboards and Notebooks using links based on intents or URLs.").

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

* **Country/subdivision code**: Select a string field from the list.

  Use [ISO 3166ï»¿](https://dt-url.net/8z03w7z) codes for countries and country subdivisions.

  + For details on country codes, see [ISO 3166-1 alpha-2ï»¿](https://dt-url.net/9r23wd1)
  + For details on country subdivision codes, see [ISO 3166-2ï»¿](https://dt-url.net/k943w0h)
* **Color value**: Select a string or numeric field from the list.

## Color

* **Region colors**

  Select how to color the regions:

  + **Color palette**: Displays all areas in a color shade from the selected color palette. The shade used for each area corresponds to the value of **Color value** in relation to the other areas.

    Example

    If the values of **Color value** returned by your query range from `0` to `100`

    - An area with a value near `0` has a color shade from near the right end of the palette.
    - An area with a value near `100` has a color shade from near the left end of the palette.
  + **Single-color**: Displays all areas in the same color. Select a color from the list or enter the hex code for the color.
  + **Custom**: Displays each area in a custom color defined by you.

    For each custom color you want to add

    1. Select  **Color**.
    2. Enter a value, operator, and color to use for that value and operator.

    Example

    Suppose you want to color a map by three levels of **Color value**:

    - Green if **Color value** is less than `4,000`
    - Yellow if **Color value** reaches or exceeds a threshold of `4,000`
    - Red if **Color value** reaches or exceeds a threshold of `5,000`

    To configure this

    - Select  **Color** and add a custom color row with the value `0`, operator `â¥`, and the desired shade of green. If **Color value** is `0` or higher, the area will be green.
    - Select  **Color** and add a custom color row with the value `4,000`, operator `â¥`, and the desired shade of yellow. If **Color value** is `4,000` or higher, the area will be yellow.
    - Select  **Color** and add a custom color row with the value `5,000`, operator `â¥`, and the desired shade of red. If **Color value** is `5,000` or higher, the area will be red.

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


---


## Source: visualization-map-connection.md


---
title: Connection map visualization
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-map-connection
scraped: 2026-02-15T21:16:18.308540
---

# Connection map visualization

# Connection map visualization

* Latest Dynatrace
* How-to guide
* 4-min read
* Published Apr 03, 2025

Dashboards version 1.311+ Notebooks version 1.311+

When to use

Use a connection map to visualize connections between mapped points. Examples include network traffic between servers or data centers, and flight routes to optimize scheduling and improve customer experience.

## Examples

To try out an example

1. Create a DQL tile in ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** or a DQL section in ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.
2. Copy the example data and paste it into the DQL edit box.
3. Run it.
4. Select the visualization and experiment with the visualization settings.

### Example 1

![Connection map example](https://dt-cdn.net/images/map-connection-example-01b-656-7b7590dcc9.png)

The map above is based on the following data.

```
data



record(flightNo="DT123", geo.location.latitude=48.2195335, geo.location.longitude=16.3784883), //Vienna



record(flightNo="DT123", geo.location.latitude=41.3826807, geo.location.longitude=2.1770239), //Barcelona



record(flightNo="DT456", geo.location.latitude=48.2195335, geo.location.longitude=16.3784883), //Vienna



record(flightNo="DT456", geo.location.latitude=48.1379879, geo.location.longitude=11.575182), //Munich



record(flightNo="DT354", geo.location.latitude=48.2195335, geo.location.longitude=16.3784883), //Vienna



record(flightNo="DT354", geo.location.latitude = 51.509865, geo.location.longitude = -0.118092), //London



record(flightNo="DT985", geo.location.latitude=48.2195335, geo.location.longitude=16.3784883), //Vienna



record(flightNo="DT985", geo.location.latitude = 52.520008, geo.location.longitude = 13.404954), //Berlin



record(flightNo="DT111", geo.location.latitude=48.2195335, geo.location.longitude=16.3784883), //Vienna



record(flightNo="DT111", geo.location.latitude = 48.864716, geo.location.longitude = 2.349014) //Paris



| summarize by:{flightNo}, geo.location.latitude=collectArray(geo.location.latitude), geo.location.longitude=collectArray(geo.location.longitude)
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
* **Open with**âfor details, see [Drilldowns and navigation](/docs/analyze-explore-automate/dashboards-and-notebooks/open-with "Drill down from Dashboards and Notebooks using links based on intents or URLs.").

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
* **Color value**: Select a value from your query to use for the color of each point on the map.

## Line

* **Line type**: Select the shape of a connection line.

  + **Linear**: A straight line between two points.
  + **Smooth**: A curved line between two points.
* **Stroke style**: Select the pattern of a connection line.

  + **Solid**: An unbroken line between two points.
  + **Dashed**: A dashed line between two points.
* **Direction indicator**: Where to show a direction indicator on a connection line.

  + **Start**: Display a direction indicator at the start of a connection line.
  + **End**: Display a direction indicator at the end of a connection line.
  + **Both**: Display a direction indicator at both ends of a connection line.
* **Thickness**: The thickness (`1`-`64` px) of a connection line.

## Legend and tooltip

* **Show custom fields**: To display custom fields (name and value) when you hover over a map area, turn on **Show custom fields** and select each custom field you want to display.
* **Text truncation**: Determines how to truncate text when the full text can't be displayed.

  + **Aâ¦**: Trim from the right end of the text (when the right end is less important)
  + **Aâ¦B**: Trim from the middle of the text (when the middle is less important)
  + **â¦B**: Trim from the left end of the text (when the left end is less important)
* **Show legend**: To display a map legend, turn on **Show legend** and select the legend **Position**:

  + **Auto**: Selects an appropriate location based on the map size and the available space.
  + **Bottom**: Displays a legend under the map.
  + **Right**: Displays a legend to the right of the map.

## Color

* **Line colors**

  Select how to color the connection lines:

  + **Color palette**: Displays all connection lines in a color shade from the selected color palette. The shade used for each connection line corresponds to the value of **Color value** in relation to the other areas.

    Example

    If the values of **Color value** returned by your query range from `0` to `100`

    - A connection line with a value near `0` has a color shade from near the right end of the palette.
    - A connection line with a value near `100` has a color shade from near the left end of the palette.
  + **Single-color**: Displays all connection lines in the same color. Select a color from the list or enter the hex code for the color.
  + **Custom colors**: Displays each connection line in a custom color defined by you.

    For each custom color you want to add

    1. Select  **Color**.
    2. Enter a value, operator, and color to use for that value and operator.

    Example

    Suppose you want to color connection lines by three levels of **Color value**:

    - Green if **Color value** is less than `4,000`
    - Yellow if **Color value** reaches or exceeds a threshold of `4,000`
    - Red if **Color value** reaches or exceeds a threshold of `5,000`

    To configure this

    - Select  **Color** and add a custom color row with the value `0`, operator `â¥`, and the desired shade of green. If **Color value** is `0` or higher, the connection line will be green.
    - Select  **Color** and add a custom color row with the value `4,000`, operator `â¥`, and the desired shade of yellow. If **Color value** is `4,000` or higher, the connection line will be yellow.
    - Select  **Color** and add a custom color row with the value `5,000`, operator `â¥`, and the desired shade of red. If **Color value** is `5,000` or higher, the connection line will be red.

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


---


## Source: visualization-map-dot.md


---
title: Dot map visualization
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-map-dot
scraped: 2026-02-15T21:16:22.780715
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

Section

Settings

Data mapping

* **Latitude** = `geo.location.latitude`
* **Longtude** = `geo.location.longitude`
* **Color value** = `revenue`

Shape

* **Style** = **Icon** (`Shop`)

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

Section

Settings

Data mapping

* **Latitude** = `geo.location.latitude`
* **Longtude** = `geo.location.longitude`

Shape

* **Style** = **Icon** (`Airplane Filled`)
* **Bearing** = **Data** (`bearing`)

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

Section

Settings

Data mapping

* **Latitude** = `geo.location.latitude`
* **Longtude** = `geo.location.longitude`

Shape

* **Style** = **Icon** (`Office Filled`)

Legend and tooltip

* **Show custom fields** = `Lab` (to display the lab name in the tooltip)

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
* **Open with**âfor details, see [Drilldowns and navigation](/docs/analyze-explore-automate/dashboards-and-notebooks/open-with "Drill down from Dashboards and Notebooks using links based on intents or URLs.").

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


---


## Source: visualization-meterbar.md


---
title: Meter bar chart
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-meterbar
scraped: 2026-02-15T21:16:31.189281
---

# Meter bar chart

# Meter bar chart

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Feb 13, 2025

When to use meter bar visualization

Use a meter bar to visualize a single numerical value as a progress bar.

## Examples

### Example 1

![Meter Bar visualization: example 1](https://dt-cdn.net/images/meter-bar-example-01-478-739cd09225.png)

The meter bar visualization above is based on the following query, which calculates `CPU` as the average host CPU usage. In the **Data mapping** settings, **Meter value** is then set as `CPU`.

```
timeseries avg(dt.host.cpu.usage)



| fieldsAdd CPU = arrayAvg(`avg(dt.host.cpu.usage)`)



| fieldsKeep CPU
```

The **Visual** tab settings are as follows:

Section

Settings

Data mapping

* **Meter value** = `CPU`

Meter bar

* **Show label** = turned on and set to `CPU Usage`
* **Show icon** = turned on and set to `HostsIcon`

Color

* **Bar color** = `62903c`
* **Custom colors** =

  + `60` and (for the custom color) `d56b1a`
  + `80` and (for the custom color) `8a0012`

Units and formats

* Selected value = `CPU`
* **Unit** = `Percent (%)`
* **Displayed unit** = `Auto`
* **Decimals** = `0.00`

### Example 2

![Meter Bar visualization: example 2](https://dt-cdn.net/images/meter-bar-example-02-474-3cf8cba784.png)

The meter bar visualization above is based on the following query, which calculates `pctActive` as the percentage of total problems that are open. In the **Data mapping** settings, **Meter value** is then set as `pctActive`.

```
fetch dt.davis.problems



| summarize count = count(), by:{event.status}



| summarize { active=toDouble(takeAny(if(event.status=="ACTIVE", count))), closed=toDouble(takeAny(if(event.status=="CLOSED", count)))}



| fieldsAdd total = active + closed



| fieldsAdd pctActive = (active / total) * 100



| fieldsKeep pctActive
```

The **Visual** tab settings are as follows:

Section

Settings

Data mapping

* **Meter value** = `pctActive`

Meter bar

* **Show label** = turned on and set to `Percentage of Open Problems`
* **Show icon** = turned on and set to `DavisAiSignetIcon`

Color

* **Bar color** = `438FB1`
* **Custom colors** = `90` and (for the custom color) `c21930`

Units and formats

* Selected value = `pctActive`
* **Unit** = `Percent (%)`
* **Displayed unit** = `Auto`
* **Decimals** = `0`

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
* **Open with**âfor details, see [Drilldowns and navigation](/docs/analyze-explore-automate/dashboards-and-notebooks/open-with "Drill down from Dashboards and Notebooks using links based on intents or URLs.").

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

For a meter chart, the data mapping section includes:

* **Meter value**: the numeric value you want to represent as a meter.

## Meter bar

### Show label

To display a string above the bar, turn on **Show label** and enter the string.

### Show icon

To display an icon above the bar, turn on **Show icon** and select an icon from the list. When **Show label** and **Show icon** are both selected, the icon is displayed before the label.

### Min value

Determines where the meter bar starts on the left.

* **Auto**âstarts the meter at `0`
* **Custom**âspecifies a different meter start point

### Max value

Determines where the meter bar ends on the right.

* **Auto**

  + If the meter value is less than `100`, the right end of the meter = `100`
  + If the meter value is greater than `100`, the right end of the meter is the meter value
* **Custom**âspecifies a different meter end point

## Color

* To set the basic color of the bar, select the desired color from the **Bar color** menu (or open the **Bar color** menu and enter the hex code for the color).
* You can add one or more **Custom colors** to define the colors to display when the meter reaches certain values.

  For each custom color, enter the meter value and set the corresponding color to use when the meter value reaches that value. A vertical line is displayed on the bar for each custom color value.

  Example

  Suppose you want your meter to remain green normally, but turn yellow if it reaches `80`, and turn red if it reaches `90`:

  + Set **Bar color** to the desired shade of green
  + Select  **Color** and add a custom color row with the value `80` and the desired shade of yellow selected. If the meter value reaches `80`, the bar will turn yellow.
  + Select  **Color** again and add a custom color row with the value `90` and the desired shade of red selected. If the meter value reaches `90`, the bar will turn red.

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


---


## Source: visualization-raw.md


---
title: Raw visualization
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-raw
scraped: 2026-02-15T21:16:29.746440
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


---


## Source: visualization-record-list.md


---
title: Record list
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-record-list
scraped: 2026-02-15T21:16:28.341412
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


---


## Source: visualization-scatterplot.md


---
title: Scatterplot visualization
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-scatterplot
scraped: 2026-02-16T21:29:57.995685
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
* **Open with**âfor details, see [Drilldowns and navigation](/docs/analyze-explore-automate/dashboards-and-notebooks/open-with "Drill down from Dashboards and Notebooks using links based on intents or URLs.").

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


---


## Source: visualization-table.md


---
title: Table visualization
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-table
scraped: 2026-02-15T21:16:06.375677
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


---


## Source: edit-visualizations.md


---
title: Edit visualizations for Notebooks and Dashboards
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations
scraped: 2026-02-16T21:12:30.296307
---

# Edit visualizations for Notebooks and Dashboards

# Edit visualizations for Notebooks and Dashboards

* Latest Dynatrace
* Reference
* 1-min read
* Updated on Oct 23, 2025

When you add a query from the  **Add** menu of the Dashboards or Notebooks app, you can choose how to visualize the results. Dynatrace offers several visualization types for your [dashboard tiles](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") and [notebook sections](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.").

## Select a visualization

After you run a query or code, you can select a visualization.

* In Notebooks, the **Visualization** section displays all visualization types.
* In Dashboards, the configuration panel includes a separate **Visual** tab that's active after you select **Run**.

To specify the visualization type, select it. The display is immediately updated so you can see what it will look like. You can try different visualizations to find the best one for what you want to display.

* If you select a visualization that's unsuitable for your query, a message will ask you to select a different visualization or modify your query. For visualization details, tips, and examples, see the visualization-specific documentation.
* To configure visualization options, expand the sections under the **Visualization** section.
* If you close the configuration panel, you can select  (in Dashboards) or  **Options** (in Notebooks) to display it again and make additional configuration changes.

## Example visualizations

Dynatrace offers several visualization types for your documents.

### Line chart example

![Line chart example](https://dt-cdn.net/images/line-chart-789-a56080c3c4.png)

For details, see [Line chart visualization](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-chart-line "Create and edit line chart visualizations on your Dynatrace dashboards and notebooks.").

### Area chart example

![Area chart example](https://dt-cdn.net/images/area-chart-773-85df352b18.png)

For details, see [Area chart visualization](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-chart-area "Create and edit area chart visualizations on your Dynatrace dashboards and notebooks.").

### Bar chart example

![Bar chart example](https://dt-cdn.net/images/bar-chart-777-54ca33eff5.png)

For details, see [Bar chart visualization](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-chart-bar "Create and edit bar chart visualizations on your Dynatrace dashboards and notebooks.").

### Table example

![Example table visualization](https://dt-cdn.net/images/table-example-01a-776-2528f83012.png)

For details, see [Table visualization](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-table "Create and edit table visualizations on your Dynatrace dashboards and notebooks.").

### Single value chart example

![Single value chart example](https://dt-cdn.net/images/single-value-example-01-519-29fd55a191.png)

For details, see [Single value visualization](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-chart-single-value "Create and edit single value visualizations on your Dynatrace dashboards and notebooks.").

### Raw example

![Raw visualization example](https://dt-cdn.net/images/raw-example-812-8a1234b934.png)

Displays the raw results of the query. Some data has been obfuscated in the example.

For details, see [Raw visualization](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-raw "Create and edit raw visualizations on your Dynatrace dashboards and notebooks.").

### Record list example

![Record list example](https://dt-cdn.net/images/record-list-visualization-example-946-6f65d21f49.png)

Lists the records returned from the query. Some data has been obfuscated in the example.

For details, see [Record list](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-record-list "View a query record list on your Dynatrace dashboards and notebooks.").

### Band chart example

![Band chart example](https://dt-cdn.net/images/band-chart-686-aeeec95104.png)

For details, see [Band chart visualization](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-chart-band "Create and edit band chart visualizations on your Dynatrace dashboards and notebooks.").

### Categorical chart example

![Categorical bar chart example](https://dt-cdn.net/images/categorical-bar-chart-841-fb2d9e3530.png)

For details, see [Categorical chart visualization](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-chart-bar-categorical "Create and edit categorical chart visualizations on your Dynatrace dashboards and notebooks.").

### Pie chart example

![Pie chart example](https://dt-cdn.net/images/pie-chart-642-aa7d7a76a4.png)

For details, see [Pie visualization](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-chart-pie "Create and edit pie visualizations on your Dynatrace dashboards and notebooks.").

### Donut chart example

![Donut chart example](https://dt-cdn.net/images/donut-chart-652-a27c8f767b.png)

For details, see [Donut visualization](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-chart-donut "Create and edit donut visualizations on your Dynatrace dashboards and notebooks.").

### Histogram example

![Histogram example](https://dt-cdn.net/images/histogram-example-03-dark-713-d663a7e1b9.png)

For details, see [Histogram visualization](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-histogram "Create and edit histogram visualizations on your Dynatrace dashboards and notebooks.").

### Honeycomb example

![Honeycomb example](https://dt-cdn.net/images/visualization-example-honeycomb-01-859-230a172dea.png)

For details, see [Honeycomb visualization](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-honeycomb "Create and edit honeycomb visualizations on your Dynatrace dashboards and notebooks.").

### Meter bar example

![Meter Bar visualization: example 1](https://dt-cdn.net/images/meter-bar-example-01-478-739cd09225.png)

For details, see [Meter bar chart](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-meterbar "Create and edit meter bar visualizations on your Dynatrace dashboards and notebooks.").

### Gauge example

![Gauge visualization: example 1](https://dt-cdn.net/images/gauge-example-01-479-24a2a01700.png)

For details, see [Gauge chart](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-gauge "Create and edit gauge visualizations on your Dynatrace dashboards and notebooks.").

### Choropleth map example

![Choropleth example: users by country](https://dt-cdn.net/images/map-choropleth-example-01b-1355-e7eff1aa58.png)

For details, see [Choropleth map visualization](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-map-choropleth "Create and edit choropleth map visualizations on your Dynatrace dashboards and notebooks.").

### Dot map example

![Dot map example: basic](https://dt-cdn.net/images/dot-01-964-dc5a30507f.png)

For details, see [Dot map visualization](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-map-dot "Create and edit dot map visualizations on your Dynatrace dashboards and notebooks.").

### Connection map example

![Connection map example](https://dt-cdn.net/images/map-connection-example-01b-656-7b7590dcc9.png)

For details, see [Connection map visualization](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-map-connection "Create and edit connection map visualizations on your Dynatrace dashboards and notebooks.").

### Bubble map example

![Bubble map example](https://dt-cdn.net/images/map-bubble-example-01c-665-52c2ff17ed.png)

For details, see [Bubble map visualization](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-map-bubble "Create and edit bubble map visualizations on your Dynatrace dashboards and notebooks.").

### Heatmap example

![Heatmap example 1: Heatmap (Response time by service)](https://dt-cdn.net/images/heatmap-example-01-resp-705-31ffafba81.png)

For details, see [Heatmap visualization](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-heatmap "Create and edit heatmap visualizations on your Dynatrace dashboards and notebooks.").

### Scatterplot example

![Scatterplot example: "Scatterplot (CPU and memory usage)"](https://dt-cdn.net/images/scatterplot-example-01-813-d8505fceb4.png)

For details, see [Scatterplot visualization](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-scatterplot "Create and edit scatterplot visualizations on your Dynatrace dashboards and notebooks.").


---


## Source: explore-data.md


---
title: Explore data
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/explore-data
scraped: 2026-02-16T21:12:27.525303
---

# Explore data

# Explore data

* Latest Dynatrace
* How-to guide
* 15-min read
* Updated on Jan 28, 2026

Dynatrace Dashboards and Notebooks offer the following options for exploring your data:

* Use [Dynatrace Intelligence generative AI](/docs/dynatrace-intelligence/copilot/copilot-overview "Learn about data security and other aspects of Dynatrace Intelligence generative AI.") and natural language to access data stored in Grail.
* Get started with our Explore interface for data types such as logs, metrics, and events.
* Advance with DQL to leverage the full power of Grail.

## Get started

To explore data such as logs, metrics, or business events with our point-and-click interface

1. In your document, open the  **Add** menu and select one of the following options, depending on what you want to explore.

   For this example, select  **Logs**, but there are other options.

   List options

   Option

   Description

   **Prompt**

   Enter a [plain-text query](#copilot) to get AI-powered insights from Grail.

   **Logs**

   [Explore logs](/docs/analyze-explore-automate/dashboards-and-notebooks/explore-data#explore-logs "Explore your data with our point-and-click interface.") via the UI. We use this option in the example that follows.

   **Metrics**

   [Explore metrics](/docs/analyze-explore-automate/dashboards-and-notebooks/explore-data#explore-metrics "Explore your data with our point-and-click interface.") via the UI.

   **Events**

   [Explore events](/docs/analyze-explore-automate/dashboards-and-notebooks/explore-data#explore-events "Explore your data with our point-and-click interface.") via the UI.

   **Problems**

   [Explore problems](/docs/analyze-explore-automate/dashboards-and-notebooks/explore-data#explore-problems "Explore your data with our point-and-click interface.") via the UI.

   **Traces**

   [Explore traces](/docs/analyze-explore-automate/dashboards-and-notebooks/explore-data#explore-traces "Explore your data with our point-and-click interface.") via the UI.

   **Business Events**

   [Explore business events](/docs/analyze-explore-automate/dashboards-and-notebooks/explore-data#explore-business-events "Explore your data with our point-and-click interface.") via the UI.

   **Security events**

   [Explore events](/docs/analyze-explore-automate/dashboards-and-notebooks/explore-data#explore-security-events "Explore your data with our point-and-click interface.") via the UI.

   The layouts differ slightly between Dashboards and Notebooks to suit the different contexts, but the functionality is the same.
2. Use the displayed elements to define your exploration.

   In this example, we focus on **Logs**. By default, the filter field and a default limit of 20 is added.

   * Click into the filter field and, for example, select **content** as a field from the list of suggested fields.
   * Add an operator and a search string right after.

     + Only operators relevant to the data type are suggested.
     + Read more on [how the filter field works](/docs/discover-dynatrace/get-started/dynatrace-ui/ui-filter-field "The filter field is a powerful tool that allows you to quickly find relevant information or narrow down results within apps.") in the dedicated documentation.

     Operator

     Description

     `=`

     equals

     `!=`

     doesn't equal

     `<`

     less than

     `<=`

     less than or equal to

     `>`

     greater than

     `>=`

     greater than or equal to

     `= *`

     is any value

     `!= *`

     isn't any value

     `in`

     matches one or more values in a list of values

     `not in`

     doesnât match any value in a list of values

     Note: Combining `=` with a wildcard in before `*`, after, or both, before your search term will resolve to a starts with, ends with, or contains filter respectively.
   * The  on the bottom of the definition opens a menu of additional commands you can add.
   * Select any ![remove filter](https://dt-cdn.net/images/remove-filter-9fadf8ea2a.svg "remove filter") in the definition to remove the element that comes before the ![remove filter](https://dt-cdn.net/images/remove-filter-9fadf8ea2a.svg "remove filter"). If you remove an element and then change your mind, you can use  to select it from the menu and add it back to your definition.
3. Select **Run** to test it and see your results.

When you need to cover more complex use cases, you can [create a DQL query](/docs/analyze-explore-automate/dashboards-and-notebooks/explore-data#create-a-dql-query "Explore your data with our point-and-click interface.") from it.

The result of this step is equivalent to opening the  menu, selecting  **DQL**, and writing a DQL query without this web UI assistance.
Then you can edit the DQL directly as needed, and you're free to delete the exploration version if you no longer need it.

* In **![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards****, open the  menu and select  **Create DQL tile**
* In **![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks****, open the  menu and select  **Create DQL section**

## Transition to Smartscape fields

As part of ongoing improvements to the Dynatrace platform, the `dt.entity.*` fields are now deprecated. To ensure consistency and accuracy in your queries and data exploration, we recommend transitioning to the equivalent `dt.smartscape.*` fields.

### What this means for you

Dynatrace automatically uses the new Smartscape notation whenever possible to enhance your experience.

If you encounter the following message:

"The `dt.entity.*` fields are deprecated. Please use `dt.smartscape.*` fields instead."

this indicates that the `dt.entity.*` fields will eventually be removed.

### What you should do

* Update your queries to replace `dt.entity.*` fields with the corresponding `dt.smartscape.*` fields.
* Review your dashboards and notebooks to ensure compatibility with the new Smartscape fields.

### Learn more

For more information about the benefits of Smartscape nodes and how they work, see [Smartscape on Grail](/docs/platform/grail/smartscape-on-grail "Learn about Smartscape on Grail features and how Smartscape uses the power of DQL.").

## Prompt

You can create a notebook section or dashboard tile using [Dynatrace Intelligence generative AI](/docs/dynatrace-intelligence/copilot/copilot-overview "Learn about data security and other aspects of Dynatrace Intelligence generative AI.") to translate your natural language questions into DQL queries.

### Generative AI in your dashboard

To create a dashboard tile using Dynatrace Intelligence generative AI

1. Go to [![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") and open or create a dashboard you can edit.
2. Open the  **Add** menu and select  **Prompt**.

   * A new Dynatrace Intelligence generative AI dashboard tile is created
   * A panel on the right displays:

     + An empty tile title field you can customize
     + A prompt box followed by some examples you can select to try
     + A **Run** button
3. Optional At the top of the prompt definition panel, enter a tile title.
4. In the prompt box, type a prompt. Try `average cpu usage percentage by host` or see the examples displayed in the web UI for inspiration.
5. Optional If your prompt doesn't specify a timeframe, you can still specify it for the dashboard in your dashboard header (default is **Last 2 hours**) or the **Custom timeframe** settings (for a tile-specific timeframe).
6. Select **Run**. Generative AI creates and runs the query for you.
7. Review the results.

   * To review the query, expand **DQL**  under the prompt box.
   * Optional You can't edit the query directly in Dynatrace Intelligence generative AI, but you have two options for reusing it:

     + Copy the query and paste it elsewhere manually.
     + Open the  menu in the tile header and select **Create DQL tile** to create a DQL tile from this query.
   * You can edit your original prompt and run it to update the query and results.  
     If you refresh your dashboard, the Dashboards app will first check if any prompts have been edited.

     + If a prompt has been edited, the DQL will first be regenerated and then run.
     + If no prompts have been edited, the existing generated DQL will simply be run.
8. Optional Select the **Visual** tab to change the visualization (refer to the [visualization-specific documentation](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations "Create, edit, and view visualizations on your Dynatrace dashboards and notebooks.") for more information).

### Generative AI in your notebook

To create a notebook section using Dynatrace Intelligence generative AI

1. Go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** and open or create a notebook you can edit.
2. Open the  **Add** menu and select  **Prompt**. A new Generative AI notebook section is created with an empty prompt box.
3. In the prompt box, type a prompt. Try `average cpu usage percentage by host` or see the examples displayed in the web UI for inspiration.
4. Optional If your prompt doesn't specify the timeframe, you can still specify it in your section header. The default is **Last 2 hours**.
5. Select **Run**. Generative AI creates and runs the query for you.

   Optional If you want to see the generated query before running it, open the  menu next to the **Run** button and select **Generate DQL only**.
6. Review the results.

   * You can review the query by expanding **DQL**  on the right.
   * Optional You can't edit the query directly in Dynatrace Intelligence generative AI, but you have two options for reusing it:

     + Copy the query and paste it elsewhere manually.
     + Open the  menu in the section header and select **Create DQL section** to create a DQL section from this query.
   * You can edit your original prompt, regenerate the query, and run it to update the results.  
     If you select **Rerun sections**, the Notebooks app will first check if any prompts have been edited.

     + If a prompt has been edited, the DQL will first be regenerated and then run.
     + If no prompts have been edited, the existing generated DQL will simply be run.
7. Optional Select the  **Options** in the section header to change the visualization (refer to the [visualization-specific documentation](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations "Create, edit, and view visualizations on your Dynatrace dashboards and notebooks.") for more information).

   Automatically select visualization

   To have Dynatrace automatically select a visualization for your query, turn on **Auto select** in the upper-right corner of your visualization settings pane.

   * If you manually select a different visualization, the **Auto select** switch will turn off.
   * To have Dynatrace once again automatically select a visualization, turn **Auto select** back on.

## Logs

This exploration functionality is the same in **![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**** and **![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks****. We use **![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**** in this example.

1. Open **![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**** and select  **Notebook** in the app header to create a new document.
2. In the empty document, open the  **Add** menu and select  **Logs**.
3. Inspect the results (initially, results are automatically fetched).

   Done. You have fetched the first 20 log lines with just a few clicks.

   ![Explore logs example: default results](https://dt-cdn.net/images/explore-logs-default-1346-80e91aedb3.png)

   To make it more useful, now click in the  box to get filter suggestions.

   ![Explore logs example: select filter](https://dt-cdn.net/images/explore-logs-filter-suggestions-642-20e57a42a9.png)

   Filter suggestions are available for any field apart from content.

### Filter by log.source

Starting from the previous example, let's add a **log.source** filter to return only those logs where the **log.source** field contains a certain string.

To do this, we need to specify

* A field, in this case **log.source**, in the filter
* A desired operator, such as `=`
* A filter value (a string that needs to occur somewhere in the **log.source** field)

1. Insert your cursor in the filter field and start typing **log.source**, or search for it via the search at the top of the suggestions, and select it.
2. Add `=` as an operator by either selecting it from the suggestions from the auto complete or by typing it.
3. Enter the string you want to search for.

   For this example, enter `oneagent` to get all logs where the **log.source** field contains `oneagent`.
4. Add `*` a wildcard before and after your filter term such that the results are restricted to logs where the **log.source** field contains `oneagent` instead of only considering exact matches.
5. Select **Run** and inspect the results.

   ![Explore logs example: filter by log.source = oneagent](https://dt-cdn.net/images/explore-logs-filter-log-source-oneagent-931-9d5b0bc8ab.png)

### Filter by content

Starting from the previous example, let's add a **content** filter to focus on logs where the content contains the string `crash` (and, because we are starting from the previous settings, where the **log.source** field contains `oneagent`).

1. Insert your cursor in the filter field immediately after the previously added **log.source** filter and either select **content** from the suggested fields or type it in.
2. Add `=` as an operator by either selecting it from the suggestions from the auto complete or by typing it.
3. Enter the string you want to search for.

   If you are using Dashboards, you can also reference existing [variables](#dashboard-component-variable) by entering a `$` sign and selecting the desired variable. In this example, we are looking for logs that contain the string `crash` somewhere in the content, so enter `crash`.
4. Add `*` a wildcard before and after your filter term such that the results are restricted to logs where the **content** field contains `crash` instead of only considering exact matches.
5. Select **Run** and inspect the results.

   Now the results are restricted to logs where the **log.source** field contains `oneagent` and the content contains the string `crash`. If you want to search for all occurrences where either one or the other filter applies, add an `OR` between the two filters.

   ![Explore logs example: filter by log.source = oneagent, content = crash](https://dt-cdn.net/images/explore-logs-filter-log-source-oneagent-content-crash-931-641a63c295.png)

### Filter by status

Starting from the previous example, let's add a **status** filter to focus on logs that contain status strings (and, because we're building on the previous settings, where the **log.source** field contains `oneagent` and the content contains the string `crash`).

1. Insert your cursor in the filter field immediately after the previously added **content** filter and either select `status` from the suggested fields or type it in.
2. Add `in` as an operator by either selecting it from the suggestions or by typing it.
3. Enter all statuses you want to filter by. Either use the value suggestions provided or type them in, separated by commas.
4. Select **Run** and inspect the results.

![Explore logs example: filter by log.source = oneagent, content = crash, status in ERROR](https://dt-cdn.net/images/explore-logs-filter-log-source-oneagent-content-crash-status-in-error-927-70de369da4.png)

### Summarize

To summarize your results

1. Open the  **Command** menu and select **Summarize**.
2. Specify how you want to summarize the results.

   You can choose between aggregation options and you can select the field by which the results are aggregated.

### Convert to time series

You can convert log-based events to a time series format appropriate to be visualized with graph visualizations. This is done by counting occurrences of fields specified for each timeslot.

To convert log-based events to a time series format

1. Open the  **Command** menu and select **Convert to time series**.
2. After you select **Convert to time series**, use the dropdown menu to select the field you want to count the occurences of the logs by. The time slots are automatically adjusted to the timeframe selected on top of the dashboard or for the respective section in a notebook.

### Bucketize

The bucketize command is used to group metric data into fixed-size ranges (buckets) for histogram visualizations. It defines the bucket size, which directly influences the granularity and scale of the x-axis in the chart.

1. Open the  **Command** menu for the metric and select **Bucketize**.
2. Select the field for which you want to create the buckets.
3. Set the **Bucketize** value.

### Sort

To sort your results

1. Select  **Sort**.
2. After you select **Sort**, use the **Sort by** menu to select the field you want to sort by, and to choose whether you want the results in ascending or descending order.

   * `value.A`  is selected by default
   * Sort applies to all metrics included in the query

### Limit

To change the limit of your results, change the value of **Limit** to the maximum number of records you want to return.

If the **Limit** setting is not displayed,  **Limit** and then set the value.

## Metrics

### Add

This exploration functionality is the same in **![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**** and **![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks****. We use **![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**** in these examples.

1. Open **![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**** and select  **Notebook** in the app header to create a new notebook.
2. In the empty notebook, open the  **Add** menu and select  **Metrics**.
3. Use the metric selector to select the metric you want to explore.

   ![Explore metrics example: select metric](https://dt-cdn.net/images/explore-metrics-select-metric-634-4c1cdd4968.png)

   For example, if you want to explore a metric for Kubernetes workloads, you can search for the string or use the menu to find what you want.

   How to search for a string and select a matching metric

   In this example, we searched for `cpu usage` and selected the best match.

   ![Explore metrics example: search for metric](https://dt-cdn.net/images/explore-metrics-search-and-select-781-73de6eb5e5.png)

   How to use the menu to select a metric

   In this example, we used the menu to find **All** > **Infrastructure** > **CPU** and then selected the best match.

   ![Explore metrics example: browse for metric](https://dt-cdn.net/images/explore-metrics-browse-and-select-764-2af4333626.png)

   Additional options are displayed after you select a metric.

   ![Explore metrics example: additional options after you select a metric](https://dt-cdn.net/images/explore-metrics-additional-options-after-metric-select-644-2f478d73c6.png)
4. Select **Run** to see what we have so far.

   Without making any additional settings, we get this line chart of the metric average over time.

   ![Explore metrics example: default chart after selecting metric](https://dt-cdn.net/images/explore-metrics-default-chart-after-metric-select-716-75bf621760.png)

#### Additional metric-specific options

To see additional options for a metric, use the metric-specific menus.

Metric-specific commands:

* [Filters](#metric-filter)
* [Split by](#metric-split-by)
* [Compare to previous period](#metric-compare-to-previous-period)
* [Default value](#metric-default-value)
* [Rate](#metric-rate)
* [Reduce to single value](#metric-reduce-to-single-value)
* [Hide](#metric-hide)
* [Duplicate](#metric-duplicate)
* [Delete](#metric-delete)
* [Alias](#metric-alias)
* [Bucketize](#metric-bucketize)

Global commands:

* [Sort](#metric-sort)
* [Limit](#metric-limit)
* [Interval](#metric-interval)

![Command scope in explore data](https://dt-cdn.net/images/command-scopes-705-b0be07d3b6.png)

### Add another metric or expression

* To add another metric, select the global  menu and then **Metric**.
* To add an [expression](#expressions), select the global  menu and then **Expression**.

### Hide or show

If you still aren't finished and you want to keep configurations for potential latter adjustments, you can hide or show selected metrics or expressions.

* To hide a metric or expression from the result, select the  menu for that metric or expression and then select **Hide**. This removes the metric from the underlying DQL query.
* To show it again, select the  menu for that metric or expression and then select **Show**.

### Duplicate

To make a copy of a metric or expression that you have already added, select the  menu for that metric or expression and then select **Duplicate**. Edit the copy as needed.

### Delete

To remove a metric or expression from your query, select the  menu for that metric or expression and then select **Delete**.

### Filter

Starting from the previous example, let's add a **host.name** filter to focus on specific hosts, where the **host.name** field contains a certain host name.

1. Select the metric-specific  menu and then select **Filters**.
2. Insert your cursor in the filter field and either select **host.name** from the suggested fields or type it in.
3. Add `=` as an operator by either selecting it from the auto-complete suggestions or by typing it in.
4. Enter a host name you want to filter by or use one of the value suggestions provided.
5. Select **Run** and inspect the results.

   ![Explore metrics example: Filter by host](https://dt-cdn.net/images/explore-metrics-filter-by-host-913-d93a73935d.png)

Note: As an alternative to using auto-enriched fields such as **host.name** or **k8s.pod.name**, names and tags are automatically offered as additional filter values for each entity contained in your data. For example, if your data contains the entity **dt.entity.host**, the two additional fields **dt.entity.host.name** and **dt.entity.host.tags** are offered in the field suggestions for you to use as a filter.

### Split by (Aggregate)

If **Split by** isn't displayed

1. Open the  **Command** menu for the metric and then select **Split by**.
2. Use the **Split by** menu to make your aggregation selection.

To see the same metric by host, we can aggregate on (**Split by**) `dt.entity.host` and then select **Run** again.

![Explore metrics example: select Split by](https://dt-cdn.net/images/explore-metrics-split-by-select-917-6ced2b5191.png)

Now we get a separate line per host.

![Explore metrics example: Split by dt.entity.host](https://dt-cdn.net/images/explore-metrics-split-by-select-dt-entity-host-921-02cdc26859.png)

### Limit results

To focus our exploration, we can set a limit on the results returned. If you add multiple metrics to your query, the limit applies to all of them.

1. Select  **Limit** to add a **Limit**.
2. Set **Limit** to the maximum number of records we want to return. In this case, we set the limit to 5, and then we ran it again to see the following results.

### Compare to previous period

To shift the metric to a previous period and add it for comparison

1. Select the metric-specific  menu and then select **Compare to previous period**.
2. Under **Compare to previous period**, enter the number and select the unit (seconds, minutes, hours, or days) for the relative time shift.

### Default value

To replace null values in your time series data with a default value

1. Select the metric-specific  menu and then select **Default value**.
2. Under **Default value**, enter a positive or negative numerical integer value that is used to replace null values.

### Rate

To visualize the rate at which a metric is changing

1. Select the metric-specific  menu and then select **Rate**.
2. Use the **Rate** menu to select a rate: **Per Second**, **Per Minute**, **Per Hour**, or **Per Day**.

### Reduce to single value

To make your results suitable for certain visualizations such as [Single value](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-chart-single-value "Create and edit single value visualizations on your Dynatrace dashboards and notebooks."), [Table](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-table "Create and edit table visualizations on your Dynatrace dashboards and notebooks."), or [Categorical bar chart](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations/visualization-chart-bar-categorical "Create and edit categorical chart visualizations on your Dynatrace dashboards and notebooks.")

1. Select the metric-specific  menu and then select **Reduce to single value**.
2. Use the **Reduce to single value** menu to select the value.

This reduces the time series data to a single scalar value over the selected timeframe and adds this as a new column called **value** that can then be used to properly map the results to your visualization.

### Alias

You might want to rename (add an alias to) a metric to make it more readable.

* Adding an alias gives the metric a more convenient alternate name for you to use in the current dashboard tile or notebook section. Instead of the raw metric name, the alias is displayed in your query definition and in the resulting dashboard tile or notebook section.
* Adding an alias doesn't affect the actual name or value of the metric, and it doesn't change how others see the metric. It doesn't even change the metric name in other dashboard tiles or notebook sections in the current document.

To add an alias for metric

1. Select the metric in your query definition. This makes the name of the metric editable.

   ![Explore metrics example: select metric to add alias](https://dt-cdn.net/images/explore-metrics-alias-select-638-cf2121f944.png)
2. Type an alias and press Enter.

   In this example, we added the metric `avg(dt.host.cpu.usage)` to our query, and now we want to give it a simpler alternative name, such as `Average host CPU usage`, to display instead of `avg(dt.host.cpu.usage)` in your notebook section or dashboard tile.

   Technical details

   Expand **DQL** in your query definition to see how your alias is handled in DQL.

### Bucketize

The bucketize command is used to group metric data into fixed-size ranges (buckets) for histogram visualizations. It defines the bucket size, which directly influences the granularity and scale of the x-axis in the chart.

1. Open the  **Command** menu for the metric and select **Bucketize**.
2. Set the **Bucketize** value.

### Interval

The interval defines the time granularity for metrics, determining how data is grouped and aggregated over time. It is expressed as a duration of each time slot (for example, 1h, 5m) for aggregating data points.

If you add multiple metrics to your query, the interval applies to all of them, ensuring consistency in data granularity across all metrics.

1. Select  **Interval** to add an **Interval** selector to your query.
2. Select an interval.

For details on how an interval is used in DQL, see [timeseries](/docs/platform/grail/dynatrace-query-language/commands/metric-commands#timeseries "DQL metric commands").

### Expressions

Add expressions to apply arithmetic based on your selected metrics.

1. Add the metrics you want to base your expression on.

   For example, to calculate the total capacity of all your disks, we can select:

   * **dt.host.disk.used** as our first metric, `A`
   * **dt.host.disk.avail** as our second metric, `B`.
2. Select the global  **Source** menu and then select **Expression**.
3. Define your expression by combining references from

   * Defined metrics such as `A`, `B`, and `C`
   * Supported mathematical and logical [operators](/docs/platform/grail/dynatrace-query-language/operators "A list of DQL Operators.") such as `+`, `-`, `/`, `*`, `(`, and `)`

   For example, to calculate the total disk capacity, we simply add both metrics together using `A+B`
4. Select **Run** and inspect the results.

![Explore metrics example: expression](https://dt-cdn.net/images/explore-metrics-example-expression-662-b59f306f98.png)

## Events

This exploration functionality is the same as described for logs.

To start exploring events

1. Open **![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**** or **![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**** and select  in an empty notebook or the document header of a dashboard.
2. Select  **Events** to add a section or tile based on it.
3. Inspect the results (if no results are initially displayed, select  **Run**).

Done. You have fetched the first 20 events with just a few clicks.

To make it more useful, now click in the  box to get filter suggestions.

Filter suggestions are available for any field apart from content.

![Explore events example: Notebooks, no filters](https://dt-cdn.net/images/explore-events-example-default-notebooks-1618-71dfb794ff.png)

### Summarize

To summarize your results

1. Open the  **Command** menu and select **Summarize**.
2. Specify how you want to summarize the results.

   You can choose between aggregation options and you can select the field by which the results are aggregated.

### Convert to time series

You can convert log-based events to a time series format appropriate to be visualized with graph visualizations. This is done by counting occurrences of fields specified for each timeslot.

To convert log-based events to a time series format

1. Open the  **Command** menu and select **Convert to time series**.
2. After you select **Convert to time series**, use the dropdown menu to select the field you want to count the occurences of the logs by. The time slots are automatically adjusted to the timeframe selected on top of the dashboard or for the respective section in a notebook.

### Bucketize

The bucketize command is used to group metric data into fixed-size ranges (buckets) for histogram visualizations. It defines the bucket size, which directly influences the granularity and scale of the x-axis in the chart.

1. Open the  **Command** menu for the metric and select **Bucketize**.
2. Select the field for which you want to create the buckets.
3. Set the **Bucketize** value.

### Sort

To sort your results

1. Select  **Sort**.
2. After you select **Sort**, use the **Sort by** menu to select the field you want to sort by, and to choose whether you want the results in ascending or descending order.

   * `value.A`  is selected by default
   * Sort applies to all metrics included in the query

### Limit

To change the limit of your results, change the value of **Limit** to the maximum number of records you want to return.

If the **Limit** setting is not displayed,  **Limit** and then set the value.

## Problems

A `problem` in Dynatrace represents an anomaly from a normal behavior or state, such as a slow service response or user-login process. Whenever a problem is detected, Dynatrace raises a specific problem event indicating such an anomaly. Every problem update is exported to Grail. Use the **Problems** explorer to query Grail for problems matching your search filters.

1. Open **![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**** or **![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**** and select  in an empty notebook or the document header of a dashboard.
2. Select  **Problems** to add a section or tile based on it.

   If you run it like that, with **Limit** set to `20` (the default), you get the first 20 results of fetching problem records from Grail.

   DQL equivalent

   In DQL, this is the equivalent of:

   ```
   fetch dt.davis.problems



   | limit 20
   ```
3. Inspect the results (if no results are initially displayed, select  **Run**).

Done. You have fetched the first 20 problems with just a few clicks.

To make it more useful, now click in the  box to get filter suggestions.

Filter suggestions are available for any field apart from content.

![Explore problems example: Notebooks, no filters](https://dt-cdn.net/images/explore-problems-example-default-notebooks-1627-5a6b1b8abb.png)

### Summarize

To summarize your results

1. Open the  **Command** menu and select **Summarize**.
2. Specify how you want to summarize the results.

   You can choose between aggregation options and you can select the field by which the results are aggregated.

### Convert to time series

You can convert log-based events to a time series format appropriate to be visualized with graph visualizations. This is done by counting occurrences of fields specified for each timeslot.

To convert log-based events to a time series format

1. Open the  **Command** menu and select **Convert to time series**.
2. After you select **Convert to time series**, use the dropdown menu to select the field you want to count the occurences of the logs by. The time slots are automatically adjusted to the timeframe selected on top of the dashboard or for the respective section in a notebook.

### Bucketize

The bucketize command is used to group metric data into fixed-size ranges (buckets) for histogram visualizations. It defines the bucket size, which directly influences the granularity and scale of the x-axis in the chart.

1. Open the  **Command** menu and select **Bucketize**.
2. Select the field for which you want to create the buckets.
3. Set the **Bucketize** value.

### Sort

To sort your results

1. Select  **Sort**.
2. After you select **Sort**, use the **Sort by** menu to select the field you want to sort by, and to choose whether you want the results in ascending or descending order.

   * `value.A`  is selected by default
   * Sort applies to all metrics included in the query

### Limit

To change the limit of your results, change the value of **Limit** to the maximum number of records you want to return.

If the **Limit** setting is not displayed,  **Limit** and then set the value.

## Traces

1. Open **![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**** or **![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**** and select  in an empty notebook or the document header of a dashboard.
2. Select  **Traces** to add a section or tile based on it.

   If you run it like that, with **Limit** set to `20` (the default), you get the first 20 results of fetching spans from Grail.

   DQL equivalent

   In DQL, this is the equivalent of:

   ```
   fetch spans



   | limit 20
   ```
3. Inspect the results (if no results are initially displayed, select  **Run**).

Done. You have fetched the first 20 spans with just a few clicks.

To make it more useful, now click in the  box to get filter suggestions.

Filter suggestions are available for any field apart from content.

![Explore traces example: Notebooks, no filters](https://dt-cdn.net/images/explore-traces-example-default-notebooks-1614-9e75005b4e.png)

### Summarize

To summarize your results

1. Open the  **Command** menu and select **Summarize**.
2. Specify how you want to summarize the results.

   You can choose between aggregation options and you can select the field by which the results are aggregated.

### Convert to time series

You can convert log-based events to a time series format appropriate to be visualized with graph visualizations. This is done by counting occurrences of fields specified for each timeslot.

To convert log-based events to a time series format

1. Open the  **Command** menu and select **Convert to time series**.
2. After you select **Convert to time series**, use the dropdown menu to select the field you want to count the occurences of the logs by. The time slots are automatically adjusted to the timeframe selected on top of the dashboard or for the respective section in a notebook.

### Bucketize

The bucketize command is used to group metric data into fixed-size ranges (buckets) for histogram visualizations. It defines the bucket size, which directly influences the granularity and scale of the x-axis in the chart.

1. Open the  **Command** menu and select **Bucketize**.
2. Select the field for which you want to create the buckets.
3. Set the **Bucketize** value.

### Sort

To sort your results

1. Select  **Sort**.
2. After you select **Sort**, use the **Sort by** menu to select the field you want to sort by, and to choose whether you want the results in ascending or descending order.

   * `value.A`  is selected by default
   * Sort applies to all metrics included in the query

### Limit

To change the limit of your results, change the value of **Limit** to the maximum number of records you want to return.

If the **Limit** setting is not displayed,  **Limit** and then set the value.

## Business events

This exploration functionality is the same as described for logs.

To start exploring business events

1. Open **![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**** or **![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**** and select  in an empty notebook or the document header of a dashboard.
2. Select  **Business Events** to add a section or tile based on it.
3. Inspect the results (if no results are initially displayed, select  **Run**).

Done. You have fetched the first 20 business events with just a few clicks.

To make it more useful, now click in the  box to get filter suggestions.

Filter suggestions are available for any field apart from content.

![Explore business events example: Notebooks, no filters](https://dt-cdn.net/images/explore-business-events-example-default-notebooks-1620-fa7dd14bad.png)

### Filter by event.provider

Let's add an **event.provider** filter to return only those business events where the **event.provider** field contains a certain string.

To do this, we need to specify

* The field you want to filter by
* The operator that decides how the filter is applied
* The filter value (a string that needs to occur somewhere in the **event.provider** field)

1. Insert your cursor in the filter field and either select **event.provider** from the suggested fields or type it in.
2. Add `=` as an operator by either selecting it from the suggestions or by typing it in.
3. Enter an event provider you want to filter by.
4. Select **Run** and inspect the results.

Now the results are restricted to logs where the **event.provider** field contains our filter value.

### Filter by event.type

Now let's further refine exploration by specifying an event type.

1. Insert your cursor in the filter field immediately after our previously added **event.provider** filter and either select **event.type** from the suggested fields or type it in.
2. Add `=` as an operator by either selecting it from the suggestions or by typing it in.
3. Enter the event type you want to filter by.
4. Select **Run** and inspect the results.

Now the results are restricted to business events where the **event.provider** and **event.type** match our filter values.

### Summarize

To summarize your results

1. Open the  **Command** menu and select **Summarize**.
2. Specify how you want to summarize the results.

   You can choose between aggregation options and you can select the field by which the results are aggregated.

### Convert to time series

You can convert log-based events to a time series format appropriate to be visualized with graph visualizations. This is done by counting occurrences of fields specified for each timeslot.

To convert log-based events to a time series format

1. Open the  **Command** menu and select **Convert to time series**.
2. After you select **Convert to time series**, use the dropdown menu to select the field you want to count the occurences of the logs by. The time slots are automatically adjusted to the timeframe selected on top of the dashboard or for the respective section in a notebook.

### Bucketize

The bucketize command is used to group metric data into fixed-size ranges (buckets) for histogram visualizations. It defines the bucket size, which directly influences the granularity and scale of the x-axis in the chart.

1. Open the  **Command** menu and select **Bucketize**.
2. Select the field for which you want to create the buckets.
3. Set the **Bucketize** value.

### Sort

To sort your results

1. Select  **Sort**.
2. After you select **Sort**, use the **Sort by** menu to select the field you want to sort by, and to choose whether you want the results in ascending or descending order.

   * `value.A`  is selected by default
   * Sort applies to all metrics included in the query

### Limit

To change the limit of your results, change the value of **Limit** to the maximum number of records you want to return.

If the **Limit** setting is not displayed,  **Limit** and then set the value.

## Security events

This exploration functionality is the same as described for logs.

To start exploring security events

1. Open **![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**** or **![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**** and select  in an empty notebook or the document header of a dashboard.
2. Select  **Security events** to add a section or tile based on it.
3. Inspect the results (if no results are initially displayed, select  **Run**).

Done. You have fetched the first 20 security events with just a few clicks.

To make it more useful, now click in the  box to get filter suggestions.

Filter suggestions are available for any field apart from content.

![Explore security events example: Notebooks, no filters](https://dt-cdn.net/images/explore-security-events-example-default-notebooks-1615-e3f261347b.png)

### Summarize

To summarize your results

1. Open the  **Command** menu and select **Summarize**.
2. Specify how you want to summarize the results.

   You can choose between aggregation options and you can select the field by which the results are aggregated.

### Convert to time series

You can convert log-based events to a time series format appropriate to be visualized with graph visualizations. This is done by counting occurrences of fields specified for each timeslot.

To convert log-based events to a time series format

1. Open the  **Command** menu and select **Convert to time series**.
2. After you select **Convert to time series**, use the dropdown menu to select the field you want to count the occurences of the logs by. The time slots are automatically adjusted to the timeframe selected on top of the dashboard or for the respective section in a notebook.

### Bucketize

The bucketize command is used to group metric data into fixed-size ranges (buckets) for histogram visualizations. It defines the bucket size, which directly influences the granularity and scale of the x-axis in the chart.

1. Open the  **Command** menu and select **Bucketize**.
2. Select the field for which you want to create the buckets.
3. Set the **Bucketize** value.

### Sort

To sort your results

1. Select  **Sort**.
2. After you select **Sort**, use the **Sort by** menu to select the field you want to sort by, and to choose whether you want the results in ascending or descending order.

   * `value.A`  is selected by default
   * Sort applies to all metrics included in the query

### Limit

To change the limit of your results, change the value of **Limit** to the maximum number of records you want to return.

If the **Limit** setting is not displayed,  **Limit** and then set the value.

## Query Grail

When you're exploring data, you're automatically creating a [DQL](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") query that you can view, copy, and use as the basis of more complex queries.

### Show DQL

To see the DQL that is created automatically during your exploration with the point-and-click interface, select **DQL**. This shows you the DQL that you can  copy and use elsewhere.

![Example: show DQL in an Explore tile](https://dt-cdn.net/images/explore-logs-show-dql-closed-636-58a6cfcf79.png)

![Example: show DQL in an Explore tile: expanded](https://dt-cdn.net/images/explore-logs-show-dql-open-633-3242ed63eb.png)

### Create a DQL query

When you're satisfied with the results but want to advance with more complex DQL commands, you can easily create a standard notebook section or dashboard tile based on it.

1. Open the  menu and select  **Create DQL section** or  **Create DQL tile**
2. Edit the resulting query section or tile as needed.
3. If you no longer need the UI-constructed version, you can delete it and just use the duplicate notebook section or dashboard tile with the DQL query.

The result of this step is equivalent to

1. Open the  menu and select  **DQL**.
2. Write a DQL query (without UI assistance) to do everything you did in the previous examples.

That's what makes this a great tool for beginners and experts.


---


## Source: notebooks.md


---
title: Notebooks
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks
scraped: 2026-02-16T21:12:11.174890
---

# Notebooks

# Notebooks

* Latest Dynatrace
* App
* 11-min read
* Updated on Jan 28, 2026

Prerequisites

### Permissions

The following table describes the required permissions.

Permission

Description

app-engine:apps:run

Allows the user to run functions

app-engine:functions:run

Allows the user to run functions

document:documents:read

Allows the user to access notebooks

document:documents:write

Allows the user to create and update notebooks

document:documents:delete

Allows the user to delete notebooks

document:trash.documents:read

Allows the user to access deleted notebooks

document:trash.documents:delete

Allows the user to permanently delete notebooks

document:trash.documents:restore

Allows the user to restore deleted notebooks

document:environment-shares:read

Allows the user to access shared notebooks

document:direct-shares:read

Allows the user to access shared notebooks

10

rows per page

Page

1

of 1

Get started

Concepts

Use cases

With ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, you can create powerful, data-driven documents for custom analytics.

![Create powerful, data-driven documents.](https://dt-cdn.net/hub/01_General_xWZn5HR.png)![Explore, analyze, and directly interact with all your data.](https://dt-cdn.net/hub/02_Explore_and__interact_paewzqz.png)![Transform data into insights and uncover the story behind the numbers.](https://dt-cdn.net/hub/Tell_the_story.png)![Create and share stunning reports with persisted data.](https://dt-cdn.net/hub/04_Reporting_pV4hDMB.png)![Include Davis AI powered anomaly detection and forecasting.](https://dt-cdn.net/hub/05_AI_e1KD03b.png)

1 of 5Create powerful, data-driven documents.

## Notebook sections

A notebook can consist of multiple sections:

* [Explore](#explore): explore data such as your logs, metrics, and business events with our point-and-click interface.
* [Query](#query): displays data queried via Grail.
* [Code](#code): display data returned by code executed via Dynatrace functions.
* [Markdown](#markdown): static content edited in markdown.

### Explore sections

You can use the Explore options to explore your logs, metrics, business events, and more with our point-and-click interface. With zero knowledge of DQL or coding, you can create and start using notebook sections in minutes.

For more information, we have a whole [Explore data](/docs/analyze-explore-automate/dashboards-and-notebooks/explore-data "Explore your data with our point-and-click interface.") page that shows you how to create Explore sections.

### Query section

The query sections allow you to easily query data from Grail and [visualize](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations "Create, edit, and view visualizations on your Dynatrace dashboards and notebooks.") the result in different ways.

![Query section](https://dt-cdn.net/images/notebooks-query-section-select-685-01cd3782b4.png)

The query section consists of a query input where you can write a DQL query. In the query input, use **Ctrl**+**Space** to trigger autocompletion at any time.

You can control the timeframe for the query via the timeframe dropdown list. If the timeframe is defined in the query itself, the dropdown list is disabled.

### Code section

The code section enables you to fetch data for your notebook using Dynatrace functions.

![Code section](https://dt-cdn.net/images/notebooks-code-section-select-694-e39f69d7ee.png)

### Markdown section

A markdown section can be anything from a minor note about something on the notebook to a whole page of formatted information with links and pictures.

Easy to edit:

![Markdown section: edit](https://dt-cdn.net/images/notebooks-markdown-section-edit-841-8301eddf20.png)

Attractive to look at:

![Markdown section: display](https://dt-cdn.net/images/notebooks-markdown-section-display-836-030ea62933.png)

To insert queries from your notebook with autocomplete, use **Ctrl**+**Space**.

#### Add links

You can link to other places in your notebook and elsewhere.

A link in Markdown is a label and link of the form `[label](address)`, where:

* The `label` is freeform text to display on the link in your Markdown tile or section
* The `address` specifies what to open when someone selects the link, such as a website or a Dynatrace app

Link to

Syntax and examples

Website

```
[My label](https://www.example.com/)
```

Notebooks app

```
[My label](/ui/apps/dynatrace.notebooks/notebooks)
```

Specific notebook

**Syntax**:

```
[label](/ui/apps/dynatrace.notebooks/notebook/<notebookid>)
```

**Example**:

```
[My label](/ui/apps/dynatrace.notebooks/notebook/274edae4-dfe8-41fb-aced-5020fb1270bc)
```

To get the address

1. Display the target notebook.
2. Copy everything on the browser address line starting from `/ui/`.
3. Paste it into your Markdown as the address of a link.

Specific notebook section

**Syntax**:

```
[label](/ui/apps/dynatrace.notebooks/notebook/<notebookid>#<sectionid>)
```

**Example**:

```
[My label](/ui/apps/dynatrace.notebooks/notebook/274edae4-dfe8-41fb-aced-5020fb1270bc#cb69caf1-52ed-4e73-8a3e-120e8cd7e8f8)
```

To get the address

1. Display the target notebook.
2. Select the target section of the notebook.
3. Copy everything on the browser address line starting from `/ui/`.
4. Paste it into your Markdown as the address of a link.

Dashboards app

```
[My label](/ui/apps/dynatrace.dashboards/)
```

Specific dashboard

**Syntax**:

```
[label](/ui/apps/dynatrace.dashboards/<dashboardid>)
```

**Example**:

```
[My label](/ui/apps/dynatrace.dashboards/dashboard/9f24c36e-ca5f-401c-8e00-5e4b05c46bd2)
```

To get the address

1. Display the target dashboard.
2. Copy everything on the browser address line starting from `/ui/`.
3. Paste it into your Markdown as the address of a link.

Specific dashboard tile

**Syntax**:

```
[label](/ui/apps/dynatrace.dashboards/dashboard/<dashboardid>#tileIds=n)
```

**Example**:

```
[My label](/ui/apps/dynatrace.dashboards/dashboard/9f24c36e-ca5f-401c-8e00-5e4b05c46bd2#from=now%28%29-2h&to=now%28%29&tileIds=6)
```

To include a specific tile ID in the link

1. Display the target dashboard.
2. Select the target tile in the target dashboard.
3. Copy everything on the browser address line starting from `/ui/`.
4. Paste it into your Markdown as the address of a link.

## Use cases

Notebooks enables you to:

* Query, analyze, and visualize all your security, observability, and business data such as logs, metrics, and events powered byâ¯ Grailï»¿.
* Predict future trends with embedded Davis forecast capabilities.
* Create and collaborate on interactive, data-driven, and persistent documents.
* Fetch and incorporate external data by runningâ¯ Dynatrace Functionsï»¿.
* Interact with data; start drill-downs by sorting, filtering, and aggregation, or even trigger workflows.
* Annotate and add context with markdown.

These procedures describe the basics of using ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** and get you started on the way to customizing and creating your own dashboards.

## Learning tips

A fast way to learn about notebooks is to open a ready-made notebook, make a copy, and start experimenting. You can undo and redo as needed.

### Open a ready-made notebook

To open a ready-made notebook

1. Go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.
2. In the **Notebooks** panel, select  **Ready-made notebooks**.

   ![Select "Ready-made notebooks" ](https://dt-cdn.net/images/ready-made-notebooks-list1-476-aa735fed50.png)

   Alternatively, you can select  **All notebooks** and then change the tab at the top of the table from **All** to  **Ready-made**.

   ![Notebooks: Select "Ready-made" tab](https://dt-cdn.net/images/notebooks-select-ready-made-tab-466-f52a4b69b3.png)
3. Select a notebook to open it.

### Make a copy

To make a copy of the current notebook

1. At the top of the notebook, open the  menu next to the notebook name.
2. Select  **Duplicate** from the menu.

Alternatively, go to the **Last opened by you** section of the sidebar, hover over the notebook you want to copy, and select  >  **Duplicate**.

### Undo and redo

You can quickly undo or redo a notebook edit.

* The  (**Undo**) and  (**Redo**) controls are displayed in the upper-left of your notebook after you make a change.
* If you prefer, you can use keyboard shortcuts.

  |  | **Undo** | **Redo** |
  | --- | --- | --- |
  | Windows | **Ctrl+Z** | **Ctrl+Shift+Z** |
  | Mac | **Cmd+Z** | **Cmd+Shift+Z** |

The number of undos could be limited depending on your notebook's size.

## Use notebooks

### Use shortcuts

keyboard shortcuts help you work faster in ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.

To list keyboard shortcuts, in ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, open the  menu and select  **Keyboard shortcuts** or use keyboard shortcut **Shift**+**?**

| Action | Keyboard shortcut |
| --- | --- |
| **General** |  |
| Close section | **Esc** |
| Add section | **Ctrl**/**Cmd**+**Shift**+**Enter** |
| Move section down | **Ctrl**/**Cmd**+**Alt**+ |
| Move section up | **Ctrl**/**Cmd**+**Alt**+ |
| Delete selected sections | **Del** |
| Duplicate selected sections | **Ctrl**/**Cmd**+**Shift**+**D** |
| Select all | **Ctrl**/**Cmd**+**A** |
| Undo | **Ctrl**/**Cmd**+**Z** |
| Redo | **Ctrl**/**Cmd**+**Shift**+**Z** |
| Open withâ¦ | **O** |
|  |  |
| **Data sections** |  |
| Add section | **Shift**+**D** |
| Run query | **Ctrl**/**Cmd**+**Enter** |
|  |  |
| **Code sections** |  |
| Add section | **Shift**+**C** |
| Execute code | **Ctrl**/**Cmd**+**Enter** |
|  |  |
| **Markdown sections** |  |
| Add section | **Shift**+**M** |
| Toggle between view and edit mode | **Ctrl**/**Cmd**+**Enter** |

### List notebooks

#### List all

To list all notebooks

1. Go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.
2. In the **Notebooks** panel, select **Owned by anyone**.

#### List my notebooks

To list all notebooks you own

1. Go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.
2. In the **Notebooks** panel, select **All**.
3. At the top of the **Notebooks** table, select **Owned by me**.

#### List notebooks shared with me

To list all notebooks that are shared with you

1. Go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.
2. In the **Notebooks** panel, select **All**.
3. At the top of the **Notebooks** table, select **Shared with me**.

#### List ready-made notebooks

What's special about ready-made documents

* Created and automatically distributed by Dynatrace as examples and templates.
* Read-only: you can edit them for use during your session, and you can save a copy with your changes, but you can't save your changes to the original document.
* This icon  in a table of documents indicates that it's a ready-made document.

To list all ready-made notebooks

1. Go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.
2. In the **Notebooks** panel, select  **Ready-made notebooks**.

   ![Select "Ready-made notebooks" ](https://dt-cdn.net/images/ready-made-notebooks-list1-476-aa735fed50.png)

   Alternatively, you can select  **All notebooks** and then change the tab at the top of the table from **All** to  **Ready-made**.

   ![Notebooks: Select "Ready-made" tab](https://dt-cdn.net/images/notebooks-select-ready-made-tab-466-f52a4b69b3.png)

For more about ready-made documents, see [Ready-made documents](/docs/analyze-explore-automate/dashboards-and-notebooks/ready-made-documents "Use ready-made documents right out of the box.").

### Find a notebook

The easiest way to search for a notebook is through the [global search](/docs/discover-dynatrace/get-started/dynatrace-ui#search "Navigate the latest Dynatrace").

The search can be triggered from any context using the **Ctrl**/**Cmd**+**K** keyboard shortcut. Notebooks with matching titles will show up in the results.

Alternatively, select  **All notebooks** in the sidebar. Enter a search term to list only matching notebooks.

### Create a notebook

To create a new notebook

1. Go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.
2. In the app header, select  **Notebook**.

Now you need to create one or more sections within your notebook. For details, see [Create a section](#section-create).

### Duplicate a notebook

To make a copy of the current notebook

1. At the top of the notebook, open the  menu next to the notebook name.
2. Select  **Duplicate** from the menu.

Alternatively, go to the **Last opened by you** section of the sidebar, hover over the notebook you want to copy, and select  >  **Duplicate**.

### Pin notebook to Dock

To add a notebook to the Dock for easy access

1. Display the notebook.
2. Open the  menu next to the notebook name (in the upper-left corner of the notebook).
3. Select  **Add to dock**.

   If you change the name of the notebook, it's automatically updated on the Dock.

To remove a notebook from the Dock

1. Hover over the notebook name in the Dock.
2. Select  **Unpin from dock**.

### Delete a notebook

To delete a notebook

1. At the top of the notebook, open the  menu next to the notebook name.
2. Select  **Delete** from the menu.

Alternatively, you can also trigger the same action in the **Last opened by you** section of the sidebar. Select  >  **Delete**.

To delete multiple notebooks, select  **All notebooks** and use the  buttons in the table.

## Create a section

Every notebook needs one or more sections.

### Create a Prompt section

To create a notebook section using [Dynatrace Intelligence generative AI](/docs/dynatrace-intelligence/copilot/copilot-overview "Learn about data security and other aspects of Dynatrace Intelligence generative AI.") to translate your natural language questions into DQL queries

1. Go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** and open or create a notebook you can edit.
2. Open the  **Add** menu and select  **Prompt**. A new Generative AI notebook section is created with an empty prompt box.
3. In the prompt box, type a prompt. Try `average cpu usage percentage by host` or see the examples displayed in the web UI for inspiration.
4. Optional If your prompt doesn't specify the timeframe, you can still specify it in your section header. The default is **Last 2 hours**.
5. Select **Run**. Generative AI creates and runs the query for you.

   Optional If you want to see the generated query before running it, open the  menu next to the **Run** button and select **Generate DQL only**.
6. Review the results.

   * You can review the query by expanding **DQL**  on the right.
   * Optional You can't edit the query directly in Dynatrace Intelligence generative AI, but you have two options for reusing it:

     + Copy the query and paste it elsewhere manually.
     + Open the  menu in the section header and select **Create DQL section** to create a DQL section from this query.
   * You can edit your original prompt, regenerate the query, and run it to update the results.  
     If you select **Rerun sections**, the Notebooks app will first check if any prompts have been edited.

     + If a prompt has been edited, the DQL will first be regenerated and then run.
     + If no prompts have been edited, the existing generated DQL will simply be run.
7. Optional Select the  **Options** in the section header to change the visualization (refer to the [visualization-specific documentation](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations "Create, edit, and view visualizations on your Dynatrace dashboards and notebooks.") for more information).

   Automatically select visualization

   To have Dynatrace automatically select a visualization for your query, turn on **Auto select** in the upper-right corner of your visualization settings pane.

   * If you manually select a different visualization, the **Auto select** switch will turn off.
   * To have Dynatrace once again automatically select a visualization, turn **Auto select** back on.

### Create an Explore section

The Explore sections offer the easiest way to get started.

* To learn more about Explore sections first, see [Explore data](/docs/analyze-explore-automate/dashboards-and-notebooks/explore-data "Explore your data with our point-and-click interface.").
* To dive right in, just display a notebook, open the  **Add** menu, and select an Explore option such as **Logs**, **Metrics**, **Events**, **Problems**, or **Business Events**.

### Create a Grail query section

The fastest and easiest way to explore your data is with an [Explore](#section-create-explore-data) section. In a few seconds, you can find and analyze your logs, metrics, or business events. No DQL required!

Deprecated: `dt.entity.*` fields

If you see the following message:

`The dt.entity.* fields are deprecated. Please use dt.smartscape.* fields instead.`

we recommend that you use an equivalent `dt.smartscape.*` field instead.

The deprecated `dt.entity.*` fields will eventually be removed.

To add data to a notebook

1. Open the  **Add** menu and select  **DQL**.

   Keyboard shortcut: **Shift**+**D**

   An empty section is added to the notebook and an **Options** side panel opens on the right.
2. In the section edit box, use the [Dynatrace Query Language (DQL)ï»¿](https://dt-url.net/bv03yk8) to define your query.
3. Select  **Run** to execute the DQL query.

   Keyboard shortcut: **Ctrl**/**Cmd**+**Enter**

   ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** automatically visualizes the result.
4. Select **Add title** to add the title header to this notebook section.
5. Select a [visualization](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations "Create, edit, and view visualizations on your Dynatrace dashboards and notebooks.") to display your results in your preferred format. Adjust visualization settings as needed.

   Automatically select visualization

   To have Dynatrace automatically select a visualization for your query, turn on **Auto select** in the upper-right corner of your visualization settings pane.

   * If you manually select a different visualization, the **Auto select** switch will turn off.
   * To have Dynatrace once again automatically select a visualization, turn **Auto select** back on.

### Create a code section

To add code fetching data for your notebook using Dynatrace functions

1. Open the  **Add** menu and select  **Code**.

   Keyboard shortcut: **Shift**+**C**

   ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** creates a code section with sample JavaScript code in the edit box.
2. Select  **Run** to execute the code.

   Keyboard shortcut: **Ctrl**/**Cmd**+**Enter**

   ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** runs the sample code and displays the result: "Hello, world!"
3. Edit the section as needed.

   * To change the code, edit it directly in the edit box above the result. For details, see [App functionsï»¿](https://dt-url.net/functions-help).
   * To configure the visualization, select  **Options**. For details, see [Edit visualizations for Notebooks and Dashboards](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations "Create, edit, and view visualizations on your Dynatrace dashboards and notebooks.").

To try an example code section

1. In your notebook, open the  **Add** menu, scroll down the menu to the **Library** section, and select any of the  code section examples.

   This adds the selected example code section to your notebook.
2. Read the comments in the code example for essential details.

### Create a Markdown section

To add a Markdown-formatted annotation to a notebook

1. Open the  **Add** menu and select  **Markdown**.

   Keyboard shortcut: **Shift**+**M**
2. Enter your text. Use Markdown to format your text and add links and images.

   * While you're typing in the edit box, your Markdown is rendered in the section.
   * Press Ctrl+Space on an empty line to pop up a selectable list of available Markdown elements.

   You can use the toolbar to insert common elements like a heading, bold text, or a link:

   ![Example: Notebooks: edit Markdown section](https://dt-cdn.net/images/notebooks-markdown-edit-969-a08f9afae1.png)

* **Italics**: wrap text in single asterisks (`*like this*`) to get italics *like this*.
* **Bold**: wrap text in double asterisks (`**like this**`) to get bold text **like this**.
* **Strikethrough**: wrap text in double tildes (~~like this~~) to get strikethrough (crossed out) text ~~like this~~.
* **Blockquote**: start a line with `>` to get blockquotes, where everything before you press Enter is quoted.
* **Code**:

  + Wrap text in backticks (`like this`) to get code text `like this`.
  + Wrap text in triple backticks (```like this```) to show a code block (multiple lines of `code text`).
* **Headings**: start a line with one or more `#` characters to create headings.
* **Horizontal line**: to visually separate sections of your annotation, add a horizontal line with three dashes (`---`).
* **Lists**: each line of an unordered (bulleted) list starts with an asterisk (`*`):

  ```
  * Line 1



  * Line 2
  ```

  Alternatively, you can use a dash (`-`):

  ```
  - Line 1



  - Line 2
  ```

  An ordered (numbered) list starts with a number and a period (`1.`) followed by a space and then your text:

  ```
  1. The first line of my procedure.



  2. The second line of my procedure.



  3. The third line of my procedure.
  ```

  If you use `1.` for each line number, the lines are renumbered automatically when you display the notebook.
* **Tables**: to add a table, define the headers, the column formatting row, and then the rows of data you want to display

  ```
  | Header 1 | Header2



  --- | ---



  content2 | content2
  ```

  | Header 1 | Header2 |
  | --- | --- |
  | content2 | content2 |
* **Special characters**: you can use any printable characters, including emojis such as ð and ð and â¤ï¸.
* **Links**: You can link to other places in your notebook and elsewhere.

  A link in Markdown is a label and link of the form `[label](address)`, where:

  + The `label` is freeform text to display on the link in your Markdown tile or section
  + The `address` specifies what to open when someone selects the link, such as a website or a Dynatrace app

  Link to

  Syntax and examples

  Website

  ```
  [My label](https://www.example.com/)
  ```

  Notebooks app

  ```
  [My label](/ui/apps/dynatrace.notebooks/notebooks)
  ```

  Specific notebook

  **Syntax**:

  ```
  [label](/ui/apps/dynatrace.notebooks/notebook/<notebookid>)
  ```

  **Example**:

  ```
  [My label](/ui/apps/dynatrace.notebooks/notebook/274edae4-dfe8-41fb-aced-5020fb1270bc)
  ```

  To get the address

  1. Display the target notebook.
  2. Copy everything on the browser address line starting from `/ui/`.
  3. Paste it into your Markdown as the address of a link.

  Specific notebook section

  **Syntax**:

  ```
  [label](/ui/apps/dynatrace.notebooks/notebook/<notebookid>#<sectionid>)
  ```

  **Example**:

  ```
  [My label](/ui/apps/dynatrace.notebooks/notebook/274edae4-dfe8-41fb-aced-5020fb1270bc#cb69caf1-52ed-4e73-8a3e-120e8cd7e8f8)
  ```

  To get the address

  1. Display the target notebook.
  2. Select the target section of the notebook.
  3. Copy everything on the browser address line starting from `/ui/`.
  4. Paste it into your Markdown as the address of a link.

  Dashboards app

  ```
  [My label](/ui/apps/dynatrace.dashboards/)
  ```

  Specific dashboard

  **Syntax**:

  ```
  [label](/ui/apps/dynatrace.dashboards/<dashboardid>)
  ```

  **Example**:

  ```
  [My label](/ui/apps/dynatrace.dashboards/dashboard/9f24c36e-ca5f-401c-8e00-5e4b05c46bd2)
  ```

  To get the address

  1. Display the target dashboard.
  2. Copy everything on the browser address line starting from `/ui/`.
  3. Paste it into your Markdown as the address of a link.

  Specific dashboard tile

  **Syntax**:

  ```
  [label](/ui/apps/dynatrace.dashboards/dashboard/<dashboardid>#tileIds=n)
  ```

  **Example**:

  ```
  [My label](/ui/apps/dynatrace.dashboards/dashboard/9f24c36e-ca5f-401c-8e00-5e4b05c46bd2#from=now%28%29-2h&to=now%28%29&tileIds=6)
  ```

  To include a specific tile ID in the link

  1. Display the target dashboard.
  2. Select the target tile in the target dashboard.
  3. Copy everything on the browser address line starting from `/ui/`.
  4. Paste it into your Markdown as the address of a link.
* **Images**: to link to a picture, use this format:

  `![alternate text](https://www.example.com/file-name.jpg)`

  ```
  Here are some of the people who started [Dynatrace](https://www.dynatrace.com).



  ![Dynatrace founders](https://dt-cdn.net/images/original-dynatrace-team-1500-7334dbe9a8.jpg)
  ```

### Start with a snippet

Several data and code snippets are available out of the box. Use our predefined DQL or code snippets to quickly start your data analytics journey.

To get started based on a snippet

1. In a notebook, select  **Add**.

   Keyboard shortcut: **Ctrl**/**Cmd**+**Shift**+**Enter**
2. Scroll down to the **Start with a snippet** section and choose one of the snippets. For example, select the  **Fetch logs** snippet, which is displayed in a preview panel.
3. When you select a snippet, a notebook section is created for the snippet.
4. Edit the query or code (depending on the snippet type you selected) and the visualization settings as needed.
5. Select  **Run** to see results.

   Keyboard shortcut: **Ctrl**/**Cmd**+**Enter**

The list of available snippets is long and growing. Create a new notebook and try them out.

When you find something interesting:

* Inspect it to see how it works
* See if you can tweak and adapt it to your own purposes

## Edit a section

### Undo and redo

You can quickly undo or redo a notebook edit.

* The  (**Undo**) and  (**Redo**) controls are displayed in the upper-left of your notebook after you make a change.
* If you prefer, you can use keyboard shortcuts.

  |  | **Undo** | **Redo** |
  | --- | --- | --- |
  | Windows | **Ctrl+Z** | **Ctrl+Shift+Z** |
  | Mac | **Cmd+Z** | **Cmd+Shift+Z** |

The number of undos could be limited depending on your notebook's size.

### Section edit controls

To see the edit commands for a section, select the section. If you have edit permission, the edit commands are displayed.

* is where you click to drag the selected section to a different position.
* **Run** starts your query. Keyboard shortcut: **Ctrl**/**Cmd**+**Enter**
* sets the segment.
* displays timeframe options.
* and  decrement and increment the timeframe.
* and  hide and show the input.
* opens the options panel, where you can select and adjust the [visualization](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations "Create, edit, and view visualizations on your Dynatrace dashboards and notebooks.").
* opens a menu of further options:

  + **Copy section** copies the selected section to the clipboard.
  + **Duplicate section** creates a copy of the selected section.
  + **Create DQL section** creates a DQL section from the selected [Explore](/docs/analyze-explore-automate/dashboards-and-notebooks/explore-data "Explore your data with our point-and-click interface.") section.
  + **Move section up** and  **Move section down** move the section up or down one row.  
    Alternative: use  to drag the section into a new position.
  + **Clear result** clears the result. Select  **Run** (or Ctrl+Enter) again to get new results.
  + **Delete section** removes the section from the notebook.
  + **Explain query** displays an AI-generated summary of the query.
  + **Dynatrace Query Language** opens DQL documentation.
  + **Copy query link** copies a link to the clipboard. If you open the link in a browser, the query will be opened in a new or existing notebook.
  + **Download result** downloads (exports) the result of the current notebook section.
  + ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Add to dashboard** opens the selected section in a dashboard.
  + **Open with** opens the section in another document. For details, see [Drilldowns and navigation](/docs/analyze-explore-automate/dashboards-and-notebooks/open-with "Drill down from Dashboards and Notebooks using links based on intents or URLs.").

You can select multiple sections and then apply the same command to all of them at once. For details, see [Manage multiple sections](#edit-manage-multiple-sections).

### Section edit panels

The available edit options will vary depending on the type of section you're editing.

* Prompt section: type a plain-text prompt in the edit box and select  **Run** (or Ctrl+Enter) to get an answer.

  ![Editing the generative AI prompt section in the Notebooks app.](https://dt-cdn.net/images/notebooks-dynatrace-intelligence-prompt-edit-2262-06425469c6.png)
* Explore data section: These sections are a great shortcut to results. To learn more about Explore sections, see [Explore data](/docs/analyze-explore-automate/dashboards-and-notebooks/explore-data "Explore your data with our point-and-click interface.").
* DQL section

  ![Example: Notebooks: edit DQL section](https://dt-cdn.net/images/notebooks-dql-edit-1156-a4d71cda36.png)
* Code section

  ![Example: Notebooks: edit Code section](https://dt-cdn.net/images/notebooks-code-edit-1151-83a2b34c65.png)
* Markdown section

  ![Example: Notebooks: edit Markdown section](https://dt-cdn.net/images/notebooks-markdown-edit-969-a08f9afae1.png)

### Select section segments

To filter data for a section, you can specify [segments](/docs/manage/segments "Segments logically structure monitoring data in Grail and function as convenient filters for data that users are allowed to access based on permissions.") for a section.

1. In the action bar for that section, select  and, in **Filter by segments**, select a segment.
2. If the segment requires an additional value selection, select it now.
3. To add another segment, select  **Segment**. Repeat this step for each segment you want to add for the selected notebook section.
4. Select **Apply** to apply the selection.

   * The segment selector  for that section now displays the name of the selected segment or, if you select more than one segment, the number of selected segments.
   * To change your segment selection, select  again, make your changes, and select **Apply**.
   * To manage segments in general (list, create, view, edit, delete), select  and then select the **Manage segments** link.

### Set section options

To open the **Options** panel (where you can select and customize a [visualization](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations "Create, edit, and view visualizations on your Dynatrace dashboards and notebooks.") for your section)

1. Select the section.
2. Select **Options**.

## Manage sections

### Undo and redo

You can quickly undo or redo a notebook edit.

* The  (**Undo**) and  (**Redo**) controls are displayed in the upper-left of your notebook after you make a change.
* If you prefer, you can use keyboard shortcuts.

  |  | **Undo** | **Redo** |
  | --- | --- | --- |
  | Windows | **Ctrl+Z** | **Ctrl+Shift+Z** |
  | Mac | **Cmd+Z** | **Cmd+Shift+Z** |

The number of undos could be limited depending on your notebook's size.

### Move a section

To move a section up or down within your notebook

1. Select the section.
2. Select and drag  the section to a new location within the notebook.

Alternate method:

1. Select the section.
2. Select  > **Move section up** or **Move section down**.

   Keyboard shortcut: **Ctrl**/**Cmd**+**Alt**+ or **Ctrl**/**Cmd**+**Alt**+

### Copy and paste sections

You can copy and paste sections to the same notebook or another notebook.

An easy way to start a new notebook is to copy reusable sections from existing notebooks to a new notebook and then edit the copied sections in the new notebook.

To copy and paste one or more sections

1. Click one section to select it.
2. You can select multiple sections and then copy all of them at once.

   * **Shift**+**Click**âselects one or more consecutive sections
   * **Ctrl/Cmd**+**Click**âselects one or more nonconsecutive sections
   * **Ctrl/Cmd**+**A**âselects all sections

   Each selected section is highlighted
3. Press **Ctrl/Cmd**+**C** to copy the selected sections to your clipboard.

   Menu alternative: on the section command bar, select  **Copy section**.
4. Press **Ctrl/Cmd**+**V** to paste the copied sections.

   * Pasting the copied sections to the current notebook is the equivalent of the  >  **Duplicate section** menu command.
   * To paste the copied sections to a different notebook, switch to the other notebook (or select  **Notebook** to create an empty notebook), and then paste (**Ctrl/Cmd**+**V**) the copied sections there.
5. To move the copied sections to new positions, select and drag  them as needed.

   You can select and drag one or more section at a time.

   * **Shift**+**Click**âselects one or more consecutive sections
   * **Ctrl/Cmd**+**Click**âselects one or more nonconsecutive sections
   * The  control is displayed on the section you selected last

### Delete a section

To remove a section from your notebook

1. Select the section.
2. Select  >  **Delete section**.

   Keyboard shortcut: **Del**

### Copy a link to a section

To copy a link to a section

1. Select the section.
2. Select  > **Copy [section type] link**.

### Download results of a section

To download (export) the result of the current dashboard tile or notebook section to a local file

1. Select the tile or section.
2. On the command bar, open the  menu and select  **Download result** > [format].

   The format options available depend on the visualization.

   * **CSV**: The result is downloaded to a local comma-separated values (\*.csv) file. This option includes table formatting such as visible columns and unit formatting.
   * **CSV (raw)**: The result is downloaded to a local comma-separated values (\*.csv) file. This option includes the complete unformatted data.
   * **JSON**: The result is downloaded to a local JSON (\*.json) file.

   Some visualizations offer no option to download the result.

#### Possible issue with importing CSV into Excel

When you export results to a CSV fileâwhether **CSV** or **CSV (raw)**âwith line breaks in any result column/field, and then open the file with Microsoft Excel or try to convert the file into a table using Excel option **Data** > **Text to Columns**, you may encounter an issue in which the line breaks are incorrectly rendered in Excel. This is caused by an Excel limitation.

To avoid this issue, use Excel option **Data** > **From Text/CSV**.

### Edit read-only notebook

When you open a document (dashboard or notebook) for which you don't have write permission, you can still edit the document during your session. After you're finished, you have two options:

* Save your changes to a new document
* Discard your changes

Example:

1. Go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, list the ready-made notebooks, and select the **Getting started** notebook.

   It says  **Ready-made** in the upper-left corner, next to the document name.
2. Select the Line chart section and then select  **Options**.
3. Change the visualization from Line to Area.

   Now you are offered two buttons: **Save as new** and **Discard changes**.
4. Use the updated notebook as needed. You have full edit access for this session.
5. When you're finished, select what to do with your changes:

   * **Save as new**âsaves your changes in a new copy of the edited notebook.
   * **Discard changes**âdiscards your changes and returns you to the unedited read-only notebook.

### Manage multiple sections

You can select multiple sections and then apply the same command to all of them at once.

* **Shift**+**Click**âselects one or more consecutive sections
* **Ctrl/Cmd**+**Click**âselects one or more nonconsecutive sections
* **Ctrl/Cmd**+**A**âselects all sections

  The **x sections** menu in the upper-right corner of the notebook offers commands that apply to all sections:

  + **Select all** selects all sections in the notebook.
  + **Run all** runs all sections in the notebook.

When you select multiple sections, the available commands include:

* is where you click to drag the selected sections to a different position.
* **Run x** runs all selected sections.
* set segments for all selected sections.
* sets the timeframe for all selected sections.
* and  hide and show the input for all selected sections.
* opens a menu of further options:

  + **Duplicate sections** creates a copy of the selected sections.
  + **Clear results** clears the results of the selected sections. Select  **Run** again to get new results.
  + **Delete sections** removes the selected sections from the notebook.
  + ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Add to dashboard** opens the selected sections in a dashboard.
  + **Open with** opens the selected sections in another document. For details, see [Drilldowns and navigation](/docs/analyze-explore-automate/dashboards-and-notebooks/open-with "Drill down from Dashboards and Notebooks using links based on intents or URLs.").

## Run a section

### Run code

To run a code section

1. Select the section.
2. Select **Run**.

After you run a code section, you can clear the code results

1. Select the section.
2. Select  > **Clear result**.

### Show/hide code

To display the code in a code section

1. Select the section.
2. Select **Show code**.

   The code is displayed in a panel above the section.

To hide the code panel again, select **Hide code**.

### Run query

To run a query section

1. Select the section.
2. Select **Run**.

After you run a query section, you can clear the query results

1. Select the section.
2. Select  > **Clear result**.

### Show/hide query

To display the query in a query section

1. Select the section.
2. Select **Show query**.

   The query is displayed in a panel above the section.

To hide the query panel again, select **Hide query**.

## Share with others

### Share a notebook

If you own a dashboard or notebook, you can share it.

There are three ways to share a document with other Dynatrace users in your company:

* **Access for all (view-only)**: Give view-only access to everyone in your Dynatrace environment.
* **Share access**: Create and maintain a list of users and user groups with access the document.
* **Share links**: Create links (URLs) pointing to your document and distribute the links through the channels of your choice (email, for example).

These methods are not mutually exclusive. For example, you can maintain a focused list of users for ongoing access to the document (maybe everyone in a certain group edits the document regularly) and you can create and distribute view-only links for a wider audience as needed.

In any case, you control whether people can edit the document or only view it.

For details on sharing documents, see [Share documents](/docs/discover-dynatrace/get-started/dynatrace-ui/share "Share Dynatrace documents (dashboards, notebooks, and launchpads) with other Dynatrace users in your company.").

You can also export a notebook as a JSON file and send the JSON to others, and then they can import the JSON.

### Export a notebook

To export a notebook

1. At the top of the notebook, open the  menu next to the notebook name.
2. Select  **Download** from the menu.

Alternatively, you can also trigger the same action in the **Last opened by you** section of the sidebar. Select  >  **Export as JSON**.

### Import a notebook

To import a notebook from a JSON file

1. Select  **All notebooks** in the document sidebar.
2. In the upper-left corner of the page, select  **Upload**.
   A file browser window opens.
3. Find and open the notebook JSON definition file.

The definition is imported as a new notebook and listed on the **Notebooks** page with **Last modified** set to the import date and time.

### Change notebook owner

When you create a document (dashboard or notebook), you are the owner. To give ownership of the document to another Dynatrace user

1. Open the  document menu and select  **Change owner**.
2. Find and select a new owner, and then select **Change owner**.

   When you change the document owner, you immediately lose access to the document.

   * Be sure you are ready to transfer ownership before you select this command.
   * You can regain access to the document only if the new owner gives you permission.
3. After the transfer is complete, the new owner will receive email about the document ownership transfer.

### Print or export to PDF

To print a notebook or export it to PDF

1. Open your notebook.
2. Optional Prepare your notebook sections for printing.

   For example:

   * Select **Run** to get the latest result before printing
   * Select **Hide input** to hide a section query and display only the result
   * Set [visualization options](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations "Create, edit, and view visualizations on your Dynatrace dashboards and notebooks."), such as hiding sensitive or irrelevant table columns that you don't want to print and distribute
3. From the notebook menu, select **Print view**.

   ![Open notebook menu from current notebook](https://dt-cdn.net/images/notebook-menu-from-notebook-411-119580207f.png)

   A printable view of the notebook is displayed on a **Print preview** page with print settings displayed at the top.
4. Select the page size (`A4` or `US Letter`) and orientation (`Portrait` or `Landscape`), and then select **Print**.

   The notebook is displayed in a print options window. Each notebook section prints to a new page.
5. Make additional print settings as needed, and then select **Save** or **Print** (depending on the print destination) to finish.

#### Known print limitations

* When printing in `Landscape` mode, a table may overlap the next section.
* When Dynatrace is in dark mode, printing a notebook uses dark mode color schemes. To avoid this, you can temporarily switch Dynatrace to light mode: from the Dynatrace user menu (in the lower-left corner of Dynatrace), select **Appearance** > **Light**.

## Analyze data

### Analyze data with AI

To analyze data using Dynatrace Intelligence Data Analyzers

1. Explore a timeseries.

   Example

   In your document (dashboard or notebook)

   1. Select  to add a new section or tile, and then select **Metrics** to explore metrics.

      ![Example: select Add > Metrics](https://dt-cdn.net/images/example-select-explore-metrics-637-025cadac69.png)
   2. In **Select metric**, select **Infrastructure** > **CPU** > **CPU usage %**.

      ![Example: select metric "CPU usage %"](https://dt-cdn.net/images/example-select-metric-cpu-usage-percent-771-a672aa20e2.png)
   3. Set **Split by** to `host.name`.

      ![Example: set "Split by" to host.name](https://dt-cdn.net/images/example-select-host-name-743-5bd89ea6a3.png)
   4. Set **Limit** to the maximum number of series to analyze. Dynatrace Intelligence Data Analyzer currently supports analysis up to 1000 series.

   You should get something like this:

   ![Example: complete query](https://dt-cdn.net/images/example-complete-query-737-dfa24f730d.png)
2. Run the query.
3. In the options panel on the right, scroll down and expand  **Davis AI**.

   Show me

   ![An example of selecting the Analyze and alert settings in the Dashboards app.](https://dt-cdn.net/images/dashboards-select-analyze-and-alert-settings-746-7155ef9415.png)

   ![The initial panel for the Analyze and alert settings in the Dashboards app.](https://dt-cdn.net/images/dashboards-analyze-and-alert-details-746-8d503491c8.png)
4. On the **Davis AI** panel, set **Analyzers** to the analyzer you want to use, and then configure the analyzer.

   * For an overview of anomaly detection, see [Anomaly detection](/docs/dynatrace-intelligence/anomaly-detection "How Dynatrace detects anomalies in your environment.")
   * For details on anomaly detection settings, see [Anomaly detection configuration](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration#analyzer "How to set up an alert for missing measurements.")

   * For details on forecast analyzer settings, [Dynatrace Intelligence predictive AI analysis](/docs/dynatrace-intelligence/reference/ai-models/forecast-analysis "Learn how Dynatrace Intelligence predictive AI generates forecasts.")

   Anomaly Detection: Auto adaptive threshold anomaly detection

   * **Number of signal fluctuations**âhow many times the signal fluctuation is added to the baseline to produce the actual threshold for alerting.
   * **Alert condition**âyour selection depends on whether you want to know when the metric is above, below, or outside (above or below) the normal range.

   For details, see [Anomaly detection configuration](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration#analyzer "How to set up an alert for missing measurements.").

   Anomaly Detection: Seasonal baseline anomaly detection

   * **Tolerance**âthe higher the tolerance, the broader the confidence band, leading to fewer triggered events.
   * **Alert condition**âyour selection depends on whether you want to know when the metric is above, below, or outside (above or below) the normal range.

   For details, see [Anomaly detection configuration](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration#analyzer "How to set up an alert for missing measurements.").

   Anomaly Detection: Static threshold anomaly detection

   * **Threshold**âa hard limit that a metric should not violate.
   * **Unit**âthe unit of the value.
   * **Alert condition**âyour selection depends on whether you want to know when the metric is above or below the threshold value.
   * **Suggest threshold**âDavis AI can help you to find the right threshold based on historical data.

   For details, see [Anomaly detection configuration](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration#analyzer "How to set up an alert for missing measurements.").

   Prediction: Forecast

   * **Data points to predict**âthe total steps the time series is forecasted. More steps generally results in less reliable forecasts and longer analyzer runtimes.
   * **Forecast offset**âan offset for the start of the forecast. For example, if the offset is set to `2`, the last two data points are ignored and a forecast for these points is returned as well.

   For details, see [Dynatrace Intelligence predictive AI analysis](/docs/dynatrace-intelligence/reference/ai-models/forecast-analysis "Learn how Dynatrace Intelligence predictive AI generates forecasts.").

   Advanced settings (for anomaly detection)

   You can use the default values or turn on **Show advanced properties** to fine-tune these settings.

   * **Alert on missing data**âalert if no data is detected within the sliding window.
   * **Violating samples**ânumber of samples in the sliding window that must violate to trigger an event.
   * **Sliding window**ânumber of samples that form the sliding window.
   * **Dealerting samples**ânumber of samples in the sliding window that must go back to normal to close the event.
5. By default, the analyzer is not enabled. To enable it, turn on the switch at the top of the edit panel (switch from **AI data analysis is not active** to **AI data analysis is active**).
6. To view the results, select the **Davis AI analysis** visualization and expand the **Davis AI analysis chart** section to review or change the visualization-specific settings:

   Show me

   ![Example of selecting "AI analysis" visualization and displaying visualization-specific settings in the Notebooks app.](https://dt-cdn.net/images/notebooks-ai-analysis-visualizations-757-4cf3f48b3c.png)

   The **Davis AI analysis** visualization has two sections: chart and visualization. You can use the **Visible sections** setting to display either or both of them.

   * **All**âshow a chart and a table. The chart reflects your table selections.
   * **Table**âshow only a table. You can sort columns that display a sort icon  in the header. Select the column header to toggle the sort order up  or down .
   * **Chart**âshow only a chart. Use the table to select entries you want to show on the chart.

#### Example: anomalous CPU usage percent

To detect when CPU usage percent exceeds 70 percent, in your document (dashboard or notebook)

1. Select  to add a new section or tile, and then select **Metrics** to explore metrics.

   Show me

   ![Example: select Add > Metrics](https://dt-cdn.net/images/example-select-explore-metrics-637-025cadac69.png)
2. In **Select metric**, select **Infrastructure** > **CPU** > **CPU usage %**.

   Show me

   ![Example: select metric "CPU usage %"](https://dt-cdn.net/images/example-select-metric-cpu-usage-percent-771-a672aa20e2.png)
3. Set **Split by** to `host.name`.

   Show me

   ![Example: set "Split by" to host.name](https://dt-cdn.net/images/example-select-host-name-743-5bd89ea6a3.png)
4. Set **Limit** to the maximum number of series to analyze. Davis analyzer currently supports analysis up to 1000 series.

   Show me

   ![Example: complete query](https://dt-cdn.net/images/example-complete-query-737-dfa24f730d.png)
5. Select **Run**.
6. In the edit panel, expand  **Davis AI**.

   Show me

   ![An example of selecting the Analyze and alert settings in the Dashboards app.](https://dt-cdn.net/images/dashboards-select-analyze-and-alert-settings-746-7155ef9415.png)

   ![The initial panel for the Analyze and alert settings in the Dashboards app.](https://dt-cdn.net/images/dashboards-analyze-and-alert-details-746-8d503491c8.png)
7. In the **Analyzers** list, select **Static threshold anomaly detection**.

   Show me

   ![Selecting the "Static threshold anomaly detection" analyzer in the Analyze and alert settings of the Dashboards app.](https://dt-cdn.net/images/dashboards-analyze-and-alert-select-static-threshold-anomaly-detection-752-45026264f0.png)
8. Set **Threshold** to `70` (enter a value) and **Alert condition** to **Alert if metric is above** (default).

   Show me

   ![Configuring settings for the "Static threshold anomaly detection" analyzer in the Dashboards app.](https://dt-cdn.net/images/dashboards-static-threshold-anomaly-detection-settings-748-4d20c8220e.png)
9. Activate the analyzer: at the top of the edit panel, switch from **AI data analysis is not active** to **AI data analysis is active**.
10. To view the results, select the **Davis AI analysis** visualization. Expand the **Davis AI analysis chart** section to see visualization-specifc settings.

    Show me

    ![Example of selecting "AI analysis" visualization and displaying visualization-specific settings in the Notebooks app.](https://dt-cdn.net/images/notebooks-ai-analysis-visualizations-757-4cf3f48b3c.png)
11. In the **Davis AI analysis chart** section, set **Visible sections** to **All**.
12. Review the results.

    In this example, we selected the hosts that exceeded the threshold.

    * The chart shows a line for the selected metric (`CPU usage %`) for each selected host.
    * A red bar across the top of the visualization indicates where the threshold for that metric was exceeded.
    * The table under the chart has those hosts selected.

    ![Example analyzer results with "AI analysis" visualization in the Notebooks app.](https://dt-cdn.net/images/notebooks-ai-analysis-chart-1920-5ac0e1f854.png)

### Start forecast analysis

From your notebook, you can trigger a series forecast analysis powered by Dynatrace Intelligence.

In this example, we issue the following query:

`timeseries avg(dt.host.cpu.usage), by:{ dt.entity.host }`

and then run a forecast for a time series selected in the results.

1. In a notebook, select  >  **DQL**.
2. Enter a query such as `timeseries avg(dt.host.cpu.usage), by:{ dt.entity.host }` to chart time series.
3. Select **Run query**.
4. Hover over the required time series in the sidebar and select  > **Filter and forecast**.

   ![Filter and forecast: select](https://dt-cdn.net/images/filter-and-forecase-select2-1183-5f9b6cae74.png)
5. The query is automatically updated to filter by the selected time series and the chart is extended to show the projection for the selected series.

   ![Filter and forecast: results](https://dt-cdn.net/images/filter-and-forecase-results-1117-910a185d8a.png)

For details, see [Dynatrace Intelligence predictive AI analysis](/docs/dynatrace-intelligence/reference/ai-models/forecast-analysis "Learn how Dynatrace Intelligence predictive AI generates forecasts.").

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Create powerful, data-driven documents for custom analytics and collaboration.](https://www.dynatrace.com/hub/detail/notebooks/?internal_source=doc&internal_medium=link&internal_campaign=cross)


---


## Source: open-with.md


---
title: Drilldowns and navigation
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/open-with
scraped: 2026-02-16T21:12:22.975784
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


---


## Source: ready-made-dashboards.md


---
title: Ready-made dashboards
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/ready-made-documents/ready-made-dashboards
scraped: 2026-02-16T21:09:52.217097
---

# Ready-made dashboards

# Ready-made dashboards

* Latest Dynatrace
* Reference
* 9-min read
* Published Jul 08, 2022

Dynatrace ready-made dashboards offer preconfigured data visualizations and filters designed for common scenarios like troubleshooting and optimization.

* Use them right out of the box
* Save a copy and customize your copy

Where to find ready-made dashboards

1. In Dynatrace, go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.
2. Choose a way to list all ready-made dashboards.

   ![Dashboards: Select "Ready-made" tab](https://dt-cdn.net/images/dashboards-select-ready-made-tab-469-5224ee5ca2.png)

   ![Select "Ready-made dashboards" under list of recent dashboards](https://dt-cdn.net/images/ready-made-dashboards-button-under-recent-dashboards-263-a29f7fe076.png)
3. Select the ready-made dashboard you want to use.  
   Try the **Explore in Playground** links below to see them in action.

Using read-only dashboards

When you open a document (dashboard or notebook) for which you don't have write permission, you can still edit the document during your session. After you're finished, you have two options:

* Save your changes to a new document
* Discard your changes

Example:

1. Go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, list the ready-made dashboards, and select the **Getting started** dashboard.

   It says  **Ready-made** in the upper-left corner, next to the document name.
2. Select the Pie chart tile and then select  **Edit**.
3. Change the visualization from Pie to Donut.

   Now you are offered two buttons: **Save as new** and **Discard changes**.
4. Use the updated dashboard as needed. You have full edit access for this session.
5. When you're finished, select what to do with your changes:

   * **Save as new**âsaves your changes in a new copy of the edited dashboard.
   * **Discard changes**âdiscards your changes and returns you to the unedited read-only dashboard.

## ActiveGate diagnostic overview

Offers a filterable diagnostic overview of ActiveGate with sections for:

* **Host vitals**âHealth metrics regarding host or container where ActiveGate is running.
* **Process**âHealth metrics regarding ActiveGate Java process.
* **Networking**âIncoming and outgoing network traffic.
* **REST.API**âAPI calls, errors, request size, and response size.

[Explore in Playgroundï»¿](https://dt-url.net/q143wbn).

Related Dynatrace app:  [Dynatrace ActiveGate](/docs/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.")

![Ready-made dashboard example: ActiveGate diagnostic overview](https://dt-cdn.net/images/activegate-diagnostic-overview-1433-31dccc87de.png)

## AWS Overview

Get broad visibility into the status of your monitored AWS Environments.

[Explore in Playgroundï»¿](https://dt-url.net/qz2336h).

Related Dynatrace app: ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") [Clouds](/docs/observe/infrastructure-observability/cloud-platform-monitoring/clouds-app "Monitor all cloud platforms at once.")

![Ready-made dashboard example: AWS Overview](https://dt-cdn.net/images/ready-made-aws-overview-3834-c36f9921b4.png)

## Azure Overview

Get broad visibility into the status of your monitored Azure Environments.

[Explore in Playgroundï»¿](https://dt-url.net/dp433oi).

Related Dynatrace app: [![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds**](/docs/observe/infrastructure-observability/cloud-platform-monitoring/clouds-app "Monitor all cloud platforms at once.")

![Ready-made dashboard example: Azure Overview](https://dt-cdn.net/images/ready-made-azure-overview-3834-391f0bda19.png)

## Cisco Device Overview

Display select key metrics for Cisco SNMP monitoring (health, interfaces, and BGP data) .

[Explore in Playgroundï»¿](https://dt-url.net/vu6333f)

Related Dynatrace app: ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") [Extensions](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.")

![Ready-made dashboard example: Cisco Device Overview](https://dt-cdn.net/images/ready-made-cisco-device-overview-1920-58959b879f.png)

## Container Scan Events Coverage

Summary of vulnerability scan events from container image scans reported by various products.

[Explore in Playgroundï»¿](https://dt-url.net/9163wft).

Related documentation: [Security integrations](/docs/secure/threat-observability/security-events-ingest "Ingest external security data into Grail.")

![Ready-made dashboard example: Container Scan Events Coverage](https://dt-cdn.net/images/container-scan-events-coverage-1438-2014fa781a.png)

## Container Vulnerability Findings

Overview of the vulnerability findings in the artifact registries of your container images.

[Explore in Playgroundï»¿](https://dt-url.net/u083wwj)

Related documentation: [Security integrations](/docs/secure/threat-observability/security-events-ingest "Ingest external security data into Grail.")

![Ready-made dashboard example: Container Vulnerability Findings](https://dt-cdn.net/images/container-vulnerability-findings-1438-e6133afd13.png)

## Dashboards - Getting started

Gives you a starting point with Dashboards and guides you to further resources.

[Explore in Playgroundï»¿](https://dt-url.net/lx8337c)

Related Dynatrace app: [![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.")

![Ready-made dashboard example: Dashboards - Getting started](https://dt-cdn.net/images/ready-made-dashboards-getting-started-dark-1405-a077c12d3d.png)

## Databases Overview

A database overview by database type, database status, and, for Oracle databases, the statements with the highest consumption.

[Explore in Playgroundï»¿](https://dt-url.net/x4a3wdv).

Related Dynatrace app: ![Databases](https://dt-cdn.net/images/dynatrace-database-256-1afe08286e.webp "Databases") [Databases app](/docs/observe/infrastructure-observability/databases/database-app "The Databases app gives you an overview of all your Extensions Framework 2.0-monitored databases.")

![Ready-made dashboard example: Databases Overview](https://dt-cdn.net/images/databases-overview-1320-e01a99a799.png)

## Extension Data Consumption

Control datapoints consumed by particular extensions.

[Explore in Playgroundï»¿](https://dt-url.net/mja33bw)

Related Dynatrace app: ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") [Extensions](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.")

![Ready-made dashboard example: Extension Data Consumption](https://dt-cdn.net/images/ready-made-extension-data-consumption-dark-1387-ab1f25ac38.png)

## IBM MQ Monitoring Overview

Display select metrics for IBM MQ queue managers, queues, channels, topics, and listeners.

[Explore in Playgroundï»¿](https://dt-url.net/ogc335g)

Related Dynatrace app: ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") [Extensions](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.")

![Ready-made dashboard example: IBM MQ Monitoring Overview](https://dt-cdn.net/images/ready-made-ibm-mq-monitoring-overview-1920-56883c156c.png)

## Infrastructure Observability Dashboard

Offers an overview of host observability, with a breakdown by environment, impacted hosts, host analysis, technologies and processes, metrics, network, and logs.

[Explore in Playgroundï»¿](https://dt-url.net/gpc3wam).

Related Dynatrace app: ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") [Infrastructure & Operations](/docs/observe/infrastructure-observability/infrastructure-and-operations "Monitor hosts, VMs, processes, and networks to detect issues and improve infrastructure performance.")

![Ready-made dashboard example: Infrastructure Observability Dashboard](https://dt-cdn.net/images/infrastructure-observability-dashboard-1432-35f83ede4a.png)

## Kafka Overview

Display the most important metrics of the extension and as an entry point for the entities

[Explore in Playgroundï»¿](https://dt-url.net/yie333z)

Related Dynatrace app: ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") [Extensions](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.")

![Ready-made dashboard example: Kafka Overview](https://dt-cdn.net/images/ready-made-kafka-overview-3840-9bbd89d659.png)

## Kubernetes Cluster

Get broad visibility into the scale, status, and resource usage of your Kubernetes clusters.

[Explore in Playgroundï»¿](https://dt-url.net/0vg33tv)

Related Dynatrace app: ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") [Kubernetes](/docs/observe/infrastructure-observability/kubernetes-app "Monitor and optimize Kubernetes with Dynatrace. Get real-time insights and health for clusters and workloads.")

![Ready-made dashboard example: Kubernetes Cluster](https://dt-cdn.net/images/ready-made-kubernetes-cluster-7680-ca562f4f97.png)

## Kubernetes Namespace - Pods

Analyze resource allocation of all pods within a namespace.

[Explore in Playgroundï»¿](https://dt-url.net/zvi339y)

Related Dynatrace app: ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") [Kubernetes](/docs/observe/infrastructure-observability/kubernetes-app "Monitor and optimize Kubernetes with Dynatrace. Get real-time insights and health for clusters and workloads.")

![Ready-made dashboard example: Kubernetes Namespace - Pods](https://dt-cdn.net/images/ready-made-kubernetes-namespace-pods-7680-84c7c1f4ba.png)

## Kubernetes Namespace - Workloads

Explore the resource utilization distribution across workloads in your namespace.

[Explore in Playgroundï»¿](https://dt-url.net/f4m33vt)

Related Dynatrace app: ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") [Kubernetes](/docs/observe/infrastructure-observability/kubernetes-app "Monitor and optimize Kubernetes with Dynatrace. Get real-time insights and health for clusters and workloads.")

![Ready-made dashboard example: Kubernetes Namespace - Workloads](https://dt-cdn.net/images/ready-made-kubernetes-namespace-workloads-7680-e811f53769.png)

## Kubernetes Node - Pods

Understand pod resource consumption on your Kubernetes nodes.

[Explore in Playgroundï»¿](https://dt-url.net/1jo33ba)

Related Dynatrace app: ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") [Kubernetes](/docs/observe/infrastructure-observability/kubernetes-app "Monitor and optimize Kubernetes with Dynatrace. Get real-time insights and health for clusters and workloads.")

![Ready-made dashboard example: Kubernetes Node - Pods](https://dt-cdn.net/images/ready-made-kubernetes-node-pods-7680-2fba73c7e9.png)

## Kubernetes Persistent Volumes

Inspect the utilization and size of your persistent volume claims.

[Explore in Playgroundï»¿](https://dt-url.net/0vq330he)

Related Dynatrace app: ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") [Kubernetes](/docs/observe/infrastructure-observability/kubernetes-app "Monitor and optimize Kubernetes with Dynatrace. Get real-time insights and health for clusters and workloads.")

![Ready-made dashboard example: Kubernetes Persistent Volumes](https://dt-cdn.net/images/ready-made-kubernetes-persistent-volumes-7680-a524779929.png)

## Log ingest overview

Get an overview of the log ingest volume and status of the log ingest pipeline. Identify log ingest issues and explore possible remediation steps.

[Explore in Playgroundï»¿](https://dt-url.net/f6s33ic)

Related Dynatrace app: ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") [Logs](/docs/analyze-explore-automate/logs "Log Management and Analytics provides a unified approach to controlling and studying your log data in Dynatrace.")

![Ready-made dashboard example: Log ingest overview](https://dt-cdn.net/images/ready-made-log-ingest-overview-7680-9aa180d1c0.png)

## Log query usage and costs

Get an overview of log query usage across the Dynatrace Platform and optimization tips for the environment administrator.

[Explore in Playgroundï»¿](https://dt-url.net/kbu33w5)

Related Dynatrace app: ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") [Logs](/docs/analyze-explore-automate/logs "Log Management and Analytics provides a unified approach to controlling and studying your log data in Dynatrace.")

![Ready-made dashboard example: Log query usage and costs](https://dt-cdn.net/images/ready-made-log-query-usage-and-costs-3840-27b2be0372.png)

## Network availability monitoring

Gain insights from synthetic monitoring using network availability monitors, which assess the performance and availability of network components. Following an overview, dashboard sections focus on ICMP, TCP, and DNS.

[Explore in Playgroundï»¿](https://dt-url.net/rxw33oy)

Related Dynatrace app: ![Synthetic](https://dt-cdn.net/images/synthetic-new-256-1ddb35ac79.png "Synthetic") [Synthetic](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app "View the synthetic monitors in your environment, search for monitors, and get a quick overview of a selected monitor.")

![Ready-made dashboard example: Network availability monitoring](https://dt-cdn.net/images/network-availability-monitoring-1920-7e5215d39f.png)

## Network devices

[Explore in Playgroundï»¿](https://dt-url.net/uyy33hp)

Related Dynatrace app: ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") [Infrastructure & Operations](/docs/observe/infrastructure-observability/infrastructure-and-operations "Monitor hosts, VMs, processes, and networks to detect issues and improve infrastructure performance.")

![Ready-made dashboard example: Network devices](https://dt-cdn.net/images/network-devices-3654-e5556c192b.png)

## Nutanix Overview

Check the status of your Nutanix infrastructure, including performance, usage, and availability of key Nutanix resources.

[Explore in Playgroundï»¿](https://dt-url.net/3b10337b)

Related Dynatrace app: ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") [Extensions](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.")

![Ready-made dashboard example: Nutanix Overview](https://dt-cdn.net/images/ready-made-nutanix-overview-7680-bd44577062.png)

## OpenPipeline usage overview

Offers an overview of your current usage of OpenPipeline (logs, metrics, spans, events, bizevents, and system events) and a breakdown by:

* Incoming records over time
* OpenPipeline processing compared to the classic log and business event processing pipelines
* Log ingest (where records come in, how they are routed, and in which buckets they are stored)

[Explore in Playgroundï»¿](https://dt-url.net/ooe3w1m).

Related Dynatrace app: ![OpenPipeline](https://dt-cdn.net/images/openpipeline-configurations-highresolution-1025-8c07f4c78c.webp "OpenPipeline") [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.")

![Ready-made dashboard example: OpenPipeline usage overview](https://dt-cdn.net/images/openpipeline-usage-overview-1441-d00df250d4.png)

## Oracle DB Overview

Browse the most important Oracle DB extension metrics and drill down into additional details.

[Explore in Playgroundï»¿](https://dt-url.net/tw1233r9)

Related Dynatrace app: ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") [Extensions](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.")

![Ready-made dashboard example: Oracle DB Overview](https://dt-cdn.net/images/ready-made-oracle-db-overview-dark-1401-ef84afea7b.png)

## Runtime contextualization of container findings for alert reduction

Use this dashboard to reduce noise from container vulnerability findings using runtime context.

[Explore in Playgroundï»¿](https://dt-url.net/lig3w5p).

Related documentation: [Security integrations](/docs/secure/threat-observability/security-events-ingest "Ingest external security data into Grail.")

![Ready-made dashboard example: Runtime contextualization of container findings for alert reduction](https://dt-cdn.net/images/runtime-contextualization-of-container-findings-for-alert-reduction-1434-66d158782e.png)

## Salesforce Data Ingest Overview

Display basic information about ingest volume and available event types, with filtering for certain event types.

[Explore in Playgroundï»¿](https://dt-url.net/ab1433kh)

Related Dynatrace app: ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") [Extensions](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.")

This dashboard has been removed from ready-made dashboards. To use it in your environment.

1. Go to the dashboard using the **Explore in Playground** link above.
2. [Download the dashboard JSON](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new#dashboards-download "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") from Playground.
3. [Upload the dashboard](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new#dashboards-upload "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") in your environment.

In upcoming releases, the extension-distributed dashboards will automatically appear among ready-made dashboards after you install the extensions in your environment.

![Ready-made dashboard example: Salesforce Data Ingest Overview](https://dt-cdn.net/images/ready-made-salesforce-data-ingest-overview-dark-1403-4b62332243.png)

## Salesforce Ingest and Outage

Use this dashboard to help identify potential salesforce outages.

[Explore in Playgroundï»¿](https://dt-url.net/3i1633rp)

Related Dynatrace app: ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") [Extensions](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.")

This dashboard has been removed from ready-made dashboards. To use it in your environment.

1. Go to the dashboard using the **Explore in Playground** link above.
2. [Download the dashboard JSON](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new#dashboards-download "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") from Playground.
3. [Upload the dashboard](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new#dashboards-upload "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") in your environment.

In upcoming releases, the extension-distributed dashboards will automatically appear among ready-made dashboards after you install the extensions in your environment.

![Ready-made dashboard example: Salesforce Ingest and Outage](https://dt-cdn.net/images/ready-made-salesforce-ingest-and-outage-dark-1413-12904c0115.png)

## Salesforce Overview

Get an overview of Salesforce Event Streaming performance and adoption metrics .

[Explore in Playgroundï»¿](https://dt-url.net/lj1833fp)

Related Dynatrace app: ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") [Extensions](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.")

This dashboard has been removed from ready-made dashboards. To use it in your environment.

1. Go to the dashboard using the **Explore in Playground** link above.
2. [Download the dashboard JSON](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new#dashboards-download "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") from Playground.
3. [Upload the dashboard](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new#dashboards-upload "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") in your environment.

In upcoming releases, the extension-distributed dashboards will automatically appear among ready-made dashboards after you install the extensions in your environment.

![Ready-made dashboard example: Salesforce Overview](https://dt-cdn.net/images/ready-made-salesforce-overview-dark-1404-7ef2c75c48.png)

## Salesforce Pages with Timeouts

Use this dashboard to perform detailed analysis on pages with a load time of more than 60 seconds.

[Explore in Playgroundï»¿](https://dt-url.net/oo1a33ut)

Related Dynatrace app: ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") [Extensions](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.")

This dashboard has been removed from ready-made dashboards. To use it in your environment.

1. Go to the dashboard using the **Explore in Playground** link above.
2. [Download the dashboard JSON](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new#dashboards-download "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") from Playground.
3. [Upload the dashboard](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new#dashboards-upload "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") in your environment.

In upcoming releases, the extension-distributed dashboards will automatically appear among ready-made dashboards after you install the extensions in your environment.

![Ready-made dashboard example: Salesforce Pages with Timeouts](https://dt-cdn.net/images/ready-made-salesforce-pages-with-timeouts-dark-1403-5ce4a0abb8.png)

## Salesforce User Activity Deep Dive

Details for performance and actions of a specific user for the Salesforce Event Streaming extension.

[Explore in Playgroundï»¿](https://dt-url.net/gq1c33t8)

Related Dynatrace app: ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") [Extensions](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.")

This dashboard has been removed from ready-made dashboards. To use it in your environment.

1. Go to the dashboard using the **Explore in Playground** link above.
2. [Download the dashboard JSON](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new#dashboards-download "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") from Playground.
3. [Upload the dashboard](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new#dashboards-upload "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") in your environment.

In upcoming releases, the extension-distributed dashboards will automatically appear among ready-made dashboards after you install the extensions in your environment.

![Ready-made dashboard example: Salesforce User Activity Deep Dive](https://dt-cdn.net/images/ready-made-salesforce-user-activity-deep-dive-dark-1413-2041d7ebad.png)

## SQL Server Overview

Browse the most important SQL Server extension metrics and drill down into additional details .

[Explore in Playgroundï»¿](https://dt-url.net/lz1e33cx)

Related Dynatrace app: ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") [Extensions](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.")

![Ready-made dashboard example: SQL Server Overview](https://dt-cdn.net/images/ready-made-sql-server-overview-7680-636e4461f1.png)

## VMware Extension Overview

Displays overview information about your VMware vCenter, including entity metrics and events.

[Explore in Playgroundï»¿](https://dt-url.net/t51g33g2)

Related Dynatrace app: ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") [Extensions](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.")

![Ready-made dashboard example: VMware Extension Overview](https://dt-cdn.net/images/ready-made-vmware-extension-overview-7680-b839d5c59d.png)

## Web availability and performance

Gain insights into the health of critical APIs and front-ends to ensure seamless user experience and offering transparency to address issues proactively. Following an overview, dashboard sections focus on HTTP monitors and browser monitors.

[Explore in Playgroundï»¿](https://dt-url.net/wv1i33mz)

Related Dynatrace app: ![Synthetic](https://dt-cdn.net/images/synthetic-new-256-1ddb35ac79.png "Synthetic") [Synthetic](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app "View the synthetic monitors in your environment, search for monitors, and get a quick overview of a selected monitor.")

![Ready-made dashboard example: Web availability and performance](https://dt-cdn.net/images/web-availability-and-performance-1920-da66ea8453.png)


---


## Source: ready-made-documents.md


---
title: Ready-made documents
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/ready-made-documents
scraped: 2026-02-16T21:23:43.906535
---

# Ready-made documents

# Ready-made documents

* Latest Dynatrace
* Reference
* 1-min read
* Published Jul 08, 2022

Use Dynatrace ready-made documents right out of the box.

What's special about ready-made documents

* Created and automatically distributed by Dynatrace as examples and templates.
* Read-only: you can edit them for use during your session, and you can save a copy with your changes, but you can't save your changes to the original document.
* This icon  in a table of documents indicates that it's a ready-made document.

[![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards")

## Dashboards](/docs/analyze-explore-automate/dashboards-and-notebooks/ready-made-documents/ready-made-dashboards "Use ready-made dashboards to visualize your data right out of the box.")[![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks")

## Notebooks](/docs/analyze-explore-automate/dashboards-and-notebooks/ready-made-documents/ready-made-notebooks "Use ready-made notebooks right out of the box.")

## Using read-only documents

When you open a document (dashboard or notebook) for which you don't have write permission, you can still edit the document during your session. After you're finished, you have two options:

* Save your changes to a new document
* Discard your changes

#### Example in Dashboards

1. Go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, list the ready-made dashboards, and select the **Getting started** dashboard.

   It says  **Ready-made** in the upper-left corner, next to the document name.
2. Select the Pie chart tile and then select  **Edit**.
3. Change the visualization from Pie to Donut.

   Now you are offered two buttons: **Save as new** and **Discard changes**.
4. Use the updated dashboard as needed. You have full edit access for this session.
5. When you're finished, select what to do with your changes:

   * **Save as new**âsaves your changes in a new copy of the edited dashboard.
   * **Discard changes**âdiscards your changes and returns you to the unedited read-only dashboard.

#### Example in Notebooks

1. Go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, list the ready-made notebooks, and select the **Getting started** notebook.

   It says  **Ready-made** in the upper-left corner, next to the document name.
2. Select the Line chart section and then select  **Options**.
3. Change the visualization from Line to Area.

   Now you are offered two buttons: **Save as new** and **Discard changes**.
4. Use the updated notebook as needed. You have full edit access for this session.
5. When you're finished, select what to do with your changes:

   * **Save as new**âsaves your changes in a new copy of the edited notebook.
   * **Discard changes**âdiscards your changes and returns you to the unedited read-only notebook.


---


## Source: use-cases.md


---
title: Notebooks and Dashboards use cases
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/use-cases
scraped: 2026-02-16T09:35:58.889788
---

# Notebooks and Dashboards use cases

# Notebooks and Dashboards use cases

* Latest Dynatrace
* How-to guide
* 1-min read
* Published May 17, 2024

The following use cases show some of the ways you can use Notebooks and Dashboards to leverage visualization and analysis of data ingested into Grail.

### Analyze and report with security snippets

Application Security

In this use case, you use snippets to visualize exposure to vulnerabilities, prioritize remediation efforts, and communicate findings to owning teams.

* [Built-in security query snippets](/docs/secure/use-cases#snippets "Use case scenarios for Application Security and Threat Observability.")

### Determine threat exposure with security templates

Application Security

In this use case, you use the Threat exposure template to visualize the risk and impact of vulnerabilities (Dashboards) or analyze the impact of vulnerabilities and prioritize remediation efforts (Notebooks).

* [Out-of-the-box templates](/docs/secure/use-cases#templates "Use case scenarios for Application Security and Threat Observability.")


---
