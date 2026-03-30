---
title: Unified analysis pages
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-ui/unified-analysis
scraped: 2026-03-06T21:25:40.142787
---

# Unified analysis pages


* Classic
* Overview
* 4-min read
* Published Mar 09, 2023

Dynatrace unified analysis pages bring all observability data and relevant analytical tools for effective analysis and troubleshooting into context. When exploring metrics, events, logs, and metadata for a problematic, domain-specific entity, you can find every observability signal related to this entity on one page.

The host overview page is an example of a unified analysis page available in most environments.

## Page types

There are two types of unified analysis pages:

* **List screen**  
  The list screen is automatically generated and enables you to browse all instances of a specific entity type. You can find the available customizations in List settings.
* **Details screen**  
  The entity details screen brings all observability signals attached to an entity into context. Like the list screen, a details screen is automatically generated for every entity in your environment. You can find the available customizations in Details settings.

## Cards

On the entity page, you can define various types of cards.

### Chart group

Use the chart group component to group configured charts in a grid. For configuration details, see Chart group cards.

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

For configuration details, see Entities list cards.

![Entity list example](https://dt-cdn.net/images/a84b28ad-48ba-40b6-b83e-c2962c2d2f86-1423-5c0e42d7a4.png)

### Metric table

Use the metric table card to show multiple metric data in one table.

For configuration details, see Metric table cards.

![Metric table card](https://dt-cdn.net/images/7dc47e10-5c1f-494d-bb1c-865fec747246-1598-1442ff2964.png)

### Properties

Use the properties card to show attributes and tags. By default, it displays all attributes coming from the Monitored entities API. For more information, see Notifications bar.

See Properties cards for configuration details.

![Properties card example](https://dt-cdn.net/images/properties-528-184d1764f0-528-10fef21345.png)

### Logs

Use the logs cardâwhich has the same functionalities as the Log viewerâto display a bar chart representing different log occurrences within the selected timeframe and a detailed table where each log is an entry with additional properties such as timestamp, status, and content.

See Logs cards for configuration details.

![logs-card](https://dt-cdn.net/images/screenshot-2023-03-14-at-10-16-08-624-bf7cf1200b.png)

### Messages

Use the message card to show information when a certain condition is satisfied. For configuration details, see Message cards. There are two types of message card visualization:

* **Message**âa card that just displays text information.
* **Card**âa card with a title, description, and available actions.

For example, display the message card if OneAgent is not deployed:

![Message card example](https://dt-cdn.net/images/screenshot-from-2022-02-02-11-45-21-2531-4541e56bf6.png)

### Events

Use the events card to display events related to the specified entities.

See Events cards for configuration details.

![Events card example](https://dt-cdn.net/images/screenshot-2023-03-14-at-14-12-35-571-7d4521137a.png)

### Health

Use the health card to display specific metrics in a visual format. By default, it provides a quick overview of up to six distinct tiles, each representing a unique metric or data point.

Single tile reacts to certain events on connected metrics and may take different colors:

* greenâthere is data on at least one connected metric
* redâthere is an open problem related to at least one connected metric
* grayâthere is a closed problem related to at least one connected metric
* whiteâthere is no data for this tile in current timeframe

See Health cards for configuration details.

![Health card](https://dt-cdn.net/images/dee80e89-6646-420a-810d-0e7e2566677b-1640-4b6291895b.png)

## Concepts

### Actions

Actions define what happens after selecting one of the available options available from the **More** (**â¦**) menu in the upper-right corner of every card.

See Actions for configuration details.

### Filtering

Unified analysis supports filtering entities by indexed entity attributes. You can enable filtering for the list screen and in the context of specific cards. Entity filtering can be configured at two levels:

* At the page level, where filtering affects all cards on the screen. There are separate configurations for the details screen and list screen.
* In the entity list level, where filtering affects only a single list.

### Injections

If you want to display the cards on the page without modifying their layout, see Extend built-in unified analysis pages.

### Exploratory analysis

The exploratory analysis analyzes only the metrics from the graph charts that are in the chart groups, entities lists, and metric tables. For more information, see DavisÂ® causal correlation analysis.

**Next step**: Unified analysis tutorial