---
title: Explore data
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/explore-data
scraped: 2026-02-18T05:34:15.134563
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

### Сортировка результатов

1. Выберите **Сортировка**.
2. После выбора **Сортировка** используйте меню **Сортировать по**, чтобы выбрать поле, по которому вы хотите сортировать, и выбрать, хотите ли вы результаты в порядке возрастания или убывания.

   * `value.A` выбрано по умолчанию
   * Сортировка применяется ко всем метрикам, включенным в запрос

### Ограничение

Чтобы изменить ограничение результатов, измените значение **Ограничение** на максимальное количество записей, которые вы хотите вернуть.

Если настройка **Ограничение** не отображается, выберите **Ограничение** и затем установите значение.

## Бизнес-события

Эта функция исследования идентична описанной для журналов.

Чтобы начать исследование бизнес-событий

1. Откройте **![Панели управления](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Панели управления") **Панели управления**** или **![Тетради](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Тетради") **Тетради**** и выберите в пустой тетради или заголовке документа панели управления.
2. Выберите **Бизнес-события**, чтобы добавить раздел или плитку на основе этого.
3. Просмотрите результаты (если результаты не отображаются изначально, выберите **Выполнить**).

Готово. Вы извлекли первые 20 бизнес-событий всего за несколько кликов.

Чтобы сделать это более полезным, теперь нажмите в поле, чтобы получить предложения фильтров.

Предложения фильтров доступны для любого поля, кроме содержимого.

![Пример исследования бизнес-событий: Тетради, без фильтров](https://dt-cdn.net/images/explore-business-events-example-default-notebooks-1620-fa7dd14bad.png)

### Фильтр по event.provider

Давайте добавим фильтр **event.provider**, чтобы вернуть только те бизнес-события, где поле **event.provider** содержит определенную строку.

Для этого нам нужно указать

* Поле, по которому вы хотите фильтровать
* Оператор, который решает, как применяется фильтр
* Значение фильтра (строка, которая должна встречаться где-то в поле **event.provider**)

1. Вставьте курсор в поле фильтра и либо выберите **event.provider** из предложенных полей, либо введите его вручную.
2. Добавьте `=` как оператор либо выбрав его из предложений, либо введя его вручную.
3. Введите поставщика события, по которому вы хотите фильтровать.
4. Выберите **Выполнить** и просмотрите результаты.

Теперь результаты ограничены журналами, где поле **event.provider** содержит наше значение фильтра.

### Фильтр по event.type

Теперь давайте еще больше уточним исследование, указав тип события.

1. Вставьте курсор в поле фильтра сразу после нашего предыдущего фильтра **event.provider** либо выберите **event.type** из предложенных полей, либо введите его вручную.
2. Добавьте `=` как оператор либо выбрав его из предложений, либо введя его вручную.
3. Введите тип события, по которому вы хотите фильтровать.
4. Выберите **Выполнить** и просмотрите результаты.

Теперь результаты ограничены бизнес-событиями, где **event.provider** и **event.type** соответствуют нашим значениям фильтра.

### Суммировать

Чтобы суммировать результаты

1. Откройте меню **Команда** и выберите **Суммировать**.
2. Укажите, как вы хотите суммировать результаты.

   Вы можете выбрать между вариантами агрегации и выбрать поле, по которому результаты будут агрегированы.

### Преобразовать в временной ряд

Вы можете преобразовать события на основе журналов в формат временного ряда, подходящий для визуализации с помощью графических визуализаций. Это делается путем подсчета вхождений полей, указанных для каждого временного интервала.

Чтобы преобразовать события на основе журналов в формат временного ряда

1. Откройте меню **Команда** и выберите **Преобразовать в временной ряд**.
2. После выбора **Преобразовать в временной ряд** используйте выпадающее меню, чтобы выбрать поле, по которому вы хотите подсчитать вхождения журналов. Временные интервалы автоматически корректируются в соответствии с выбранным временем на верхней части панели управления или для соответствующего раздела в тетради.

### Группировать

Команда группировки используется для группировки данных метрик в фиксированные диапазоны (корзины) для гистограммных визуализаций. Она определяет размер корзины, который напрямую влияет на детализацию и масштаб оси X в диаграмме.

1. Откройте меню **Команда** и выберите **Группировать**.
2. Выберите поле, для которого вы хотите создать корзины.
3. Установите значение **Группировать**.

### Сортировка

Чтобы сортировать результаты

1. Выберите **Сортировка**.
2. После выбора **Сортировка** используйте меню **Сортировать по**, чтобы выбрать поле, по которому вы хотите сортировать, и выбрать, хотите ли вы результаты в порядке возрастания или убывания.

   * `value.A` выбрано по умолчанию
   * Сортировка применяется ко всем метрикам, включенным в запрос

### Ограничение

Чтобы изменить ограничение результатов, измените значение **Ограничение** на максимальное количество записей, которые вы хотите вернуть.

Если настройка **Ограничение** не отображается, выберите **Ограничение** и затем установите значение.

## События безопасности

Эта функция исследования идентична описанной для журналов.

Чтобы начать исследование событий безопасности

1. Откройте **![Панели управления](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Панели управления") **Панели управления**** или **![Тетради](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Тетради") **Тетради**** и выберите в пустой тетради или заголовке документа панели управления.
2. Выберите **События безопасности**, чтобы добавить раздел или плитку на основе этого.
3. Просмотрите результаты (если результаты не отображаются изначально, выберите **Выполнить**).

Готово. Вы извлекли первые 20 событий безопасности всего за несколько кликов.

Чтобы сделать это более полезным, теперь нажмите в поле, чтобы получить предложения фильтров.

Предложения фильтров доступны для любого поля, кроме содержимого.

![Пример исследования событий безопасности: Тетради, без фильтров](https://dt-cdn.net/images/explore-security-events-example-default-notebooks-1615-e3f261347b.png)

### Суммировать

Чтобы суммировать результаты

1. Откройте меню **Команда** и выберите **Суммировать**.
2. Укажите, как вы хотите суммировать результаты.

   Вы можете выбрать между вариантами агрегации и выбрать поле, по которому результаты будут агрегированы.

### Преобразовать в временной ряд

Вы можете преобразовать события на основе журналов в формат временного ряда, подходящий для визуализации с помощью графических визуализаций. Это делается путем подсчета вхождений полей, указанных для каждого временного интервала.

Чтобы преобразовать события на основе журналов в формат временного ряда

1. Откройте меню **Команда** и выберите **Преобразовать в временной ряд**.
2. После выбора **Преобразовать в временной ряд** используйте выпадающее меню, чтобы выбрать поле, по которому вы хотите подсчитать вхождения журналов. Временные интервалы автоматически корректируются в соответствии с выбранным временем на верхней части панели управления или для соответствующего раздела в тетради.

### Группировать

Команда группировки используется для группировки данных метрик в фиксированные диапазоны (корзины) для гистограммных визуализаций. Она определяет размер корзины, который напрямую влияет на детализацию и масштаб оси X в диаграмме.

1. Откройте меню **Команда** и выберите **Группировать**.
2. Выберите поле, для которого вы хотите создать корзины.
3. Установите значение **Группировать**.

### Сортировка

Чтобы сортировать результаты

1. Выберите **Сортировка**.
2. После выбора **Сортировка** используйте меню **Сортировать по**, чтобы выбрать поле, по которому вы хотите сортировать, и выбрать, хотите ли вы результаты в порядке возрастания или убывания.

   * `value.A` выбрано по умолчанию
   * Сортировка применяется ко всем метрикам, включенным в запрос

### Ограничение

Чтобы изменить ограничение результатов, измените значение **Ограничение** на максимальное количество записей, которые вы хотите вернуть.

Если настройка **Ограничение** не отображается, выберите **Ограничение** и затем установите значение.

## Запрос Grail

Когда вы исследуете данные, вы автоматически создаете запрос [DQL](/docs/platform/grail/dynatrace-query-language "Как использовать язык запросов Dynatrace") , который вы можете просмотреть, скопировать и использовать в качестве основы для более сложных запросов.

### Показать DQL

Чтобы увидеть DQL, созданный автоматически во время исследования с помощью интерфейса point-and-click, выберите **DQL**. Это показывает вам DQL, который вы можете скопировать и использовать в другом месте.

![Пример: показать DQL в плитке Explore](https://dt-cdn.net/images/explore-logs-show-dql-closed-636-58a6cfcf79.png)

![Пример: показать DQL в плитке Explore: расширено](https://dt-cdn.net/images/explore-logs-show-dql-open-633-3242ed63eb.png)

### Создать запрос DQL

Когда вы удовлетворены результатами, но хотите продолжить с более сложными командами DQL, вы можете легко создать стандартный раздел тетради или плитку панели управления на основе этого.

1. Откройте меню и выберите **Создать раздел DQL** или **Создать плитку DQL**
2. Отредактируйте получившийся раздел запроса или плитку по мере необходимости.
3. Если вам больше не нужна версия, созданная интерфейсом, вы можете удалить ее и использовать только дубликат раздела тетради или плитки панели управления с запросом DQL.

Результат этого шага эквивалентен

1. Откройте меню и выберите **DQL**.
2. Напишите запрос DQL (без помощи интерфейса), чтобы сделать все, что вы сделали в предыдущих примерах.

Это делает его отличным инструментом для начинающих и экспертов.