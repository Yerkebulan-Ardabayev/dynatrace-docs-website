---
title: Unified analysis pages
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-ui/unified-analysis
scraped: 2026-02-19T21:22:55.700780
---

# Unified analysis pages

# Unified analysis pages

* Overview
* 4-min read
* Published Mar 09, 2023

Dynatrace unified analysis pages bring all observability data and relevant analytical tools for effective analysis and troubleshooting into context. When exploring metrics, events, logs, and metadata for a problematic, domain-specific entity, you can find every observability signal related to this entity on one page.

The [host overview page](/docs/observe/infrastructure-observability/hosts/monitoring/host-monitoring "Monitor hosts with Dynatrace.") is an example of a unified analysis page available in most environments.

## Page types

There are two types of unified analysis pages:

* **List screen**  
  The list screen is automatically generated and enables you to browse all instances of a specific entity type. You can find the available customizations in [List settings](/docs/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-reference#list-settings "Learn about unified analysis syntax").
* **Details screen**  
  The entity details screen brings all observability signals attached to an entity into context. Like the list screen, a details screen is automatically generated for every entity in your environment. You can find the available customizations in [Details settings](/docs/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-reference#details-settings "Learn about unified analysis syntax").

## Cards

On the entity page, you can define various types of cards.

### Chart group

Use the chart group component to group configured charts in a grid. For configuration details, see [Chart group cards](/docs/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-reference#chart-group-cards "Learn about unified analysis syntax").

### Chart type

You can use the following chart types (controlled by the `visualizationType` field).

* **Graph chart:**

  ![Chart group example](https://dt-cdn.net/images/chart-group-1169-76d6ed5a9e.png)
* **Pie chart:**

  ![Pie chart](https://dt-cdn.net/images/pie-chart-519-7780ea60ce.png)
* **Single value:**

  ![Single value](https://dt-cdn.net/images/single-value-550-35129a06f1.png)

### Entity list

Use the entity list card to show entities of the same type, their attributes, and related entities in one table.

For configuration details, see [Entities list cards](/docs/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-reference#entities-list-cards "Learn about unified analysis syntax").

![Entity list example](https://dt-cdn.net/images/a84b28ad-48ba-40b6-b83e-c2962c2d2f86-1423-5c0e42d7a4.png)

### Metric table

Use the metric table card to show multiple metric data in one table.

For configuration details, see [Metric table cards](/docs/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-reference#metric-table-cards "Learn about unified analysis syntax").

![Metric table card](https://dt-cdn.net/images/7dc47e10-5c1f-494d-bb1c-865fec747246-1598-1442ff2964.png)

### Properties

Use the properties card to show attributes and tags. By default, it displays all attributes coming from the [Monitored entities API](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API."). For more information, see [Notifications bar](/docs/observe/infrastructure-observability/hosts/monitoring/host-monitoring#notifications-bar "Monitor hosts with Dynatrace.").

See [Properties cards](/docs/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-reference#properties-cards "Learn about unified analysis syntax") for configuration details.

![Properties card example](https://dt-cdn.net/images/properties-528-184d1764f0-528-10fef21345.png)

### Logs

Use the logs cardâwhich has the same functionalities as the [Log viewer](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer "Learn how to use Dynatrace log viewer to analyze log data.")âto display a bar chart representing different log occurrences within the selected timeframe and a detailed table where each log is an entry with additional properties such as timestamp, status, and content.

See [Logs cards](/docs/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-reference#logs-cards "Learn about unified analysis syntax") for configuration details.

![logs-card](https://dt-cdn.net/images/screenshot-2023-03-14-at-10-16-08-624-bf7cf1200b.png)

### Messages

Use the message card to show information when a certain condition is satisfied. For configuration details, see [Message cards](/docs/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-reference#message-cards "Learn about unified analysis syntax"). There are two types of message card visualization:

* **Message**âa card that just displays text information.
* **Card**âa card with a title, description, and available actions.

For example, display the message card if OneAgent is not deployed:

![Message card example](https://dt-cdn.net/images/screenshot-from-2022-02-02-11-45-21-2531-4541e56bf6.png)

### Events

Use the events card to display events related to the specified entities.

See [Events cards](/docs/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-reference#events-cards "Learn about unified analysis syntax") for configuration details.

![Events card example](https://dt-cdn.net/images/screenshot-2023-03-14-at-14-12-35-571-7d4521137a.png)

### Health

Use the health card to display specific metrics in a visual format. By default, it provides a quick overview of up to six distinct tiles, each representing a unique metric or data point.

Single tile reacts to certain events on connected metrics and may take different colors:

* greenâthere is data on at least one connected metric
* redâthere is an open problem related to at least one connected metric
* grayâthere is a closed problem related to at least one connected metric
* whiteâthere is no data for this tile in current timeframe

See [Health cards](/docs/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-reference#health-cards "Learn about unified analysis syntax") for configuration details.

![Health card](https://dt-cdn.net/images/dee80e89-6646-420a-810d-0e7e2566677b-1640-4b6291895b.png)

## Concepts

### Actions

Actions define what happens after selecting one of the available options available from the **More** (**â¦**) menu in the upper-right corner of every card.

See [Actions](/docs/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-reference#actions "Learn about unified analysis syntax") for configuration details.

### Filtering

Unified analysis supports filtering entities by indexed entity attributes. You can enable filtering for the list screen and in the context of specific cards. Entity filtering can be configured at two levels:

* At the page level, where filtering affects all cards on the screen. There are separate configurations for the [details screen](/docs/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-reference#details-filters "Learn about unified analysis syntax") and [list screen](/docs/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-reference#list-filters "Learn about unified analysis syntax").
* In the entity list level, where filtering affects only a single list.

### Injections

If you want to display the cards on the page without modifying their layout, see [Extend built-in unified analysis pages](/docs/ingest-from/extend-dynatrace/extend-ui/extend-unified-analysis-pages "Extend the built-in unified analysis page with additional data ingested by your extension.").

### Exploratory analysis

The exploratory analysis analyzes only the metrics from the graph charts that are in the chart groups, entities lists, and metric tables. For more information, see [DavisÂ® causal correlation analysis](/docs/dynatrace-intelligence/reference/ai-models/causal-correlation-analysis "Learn how Dynatrace Intelligence causal correlation analysis finds related metrics across your environment.").

**Next step**: [Unified analysis tutorial](/docs/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-tutorial "Learn how to upload sample data to your Dynatrace environment and create a simple unified analysis extension.")