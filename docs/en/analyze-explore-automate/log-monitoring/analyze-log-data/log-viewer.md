---
title: Log viewer (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer
scraped: 2026-02-25T21:33:52.522193
---

# Log viewer (Logs Classic)

# Log viewer (Logs Classic)

* Explanation
* 9-min read
* Updated on Jan 18, 2023

Log Monitoring Classic

The log viewer enables you to browse logs within a certain timeframe using detected aspects of the log content. You can use **Available attributes** to narrow down your log view and focus on a specific aspect of the log content.

To access the log viewer, go to ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic**. The log viewer has four sections:

## Search

In **Filter by**, you can set filters to narrow down the log events that are displayed in the results table. Select **Advanced query** to edit the query manually.

* With **Filter by** displayed (the default), the filter is in autocomplete mode, where you select from a set of detected log data fields to filter the results (limit of 10 different attributes). For filters with the same attributes, only one statement needs to be true. For filters with different attributes, all statements need to be true. While in the auto-complete mode, selected filters and **Available attributes** are synchronized automatically.

  When using a search query in the simple mode:

  + If the searched attribute names are the same, the **OR** operator is applied. The search results include items that match any of the specified attribute names. It provides a broader search, allowing for variations in attribute names.
  + If the searched attribute names differ, the **AND** operator is applied. The search results include only items that simultaneously match **all** of the specified attribute names. It narrows down the search to items that match multiple criteria.
* With **Advanced query** selected, you can specify more complex criteria for log events by using combinations of keywords, phrases, logical operators, and parentheses (limit of 10 different attributes). The Dynatrace search query language provides you with complete flexibility over searches through log content. You can use the query entry to quickly text search the content of the log data. Any string entered in the query text box without specifying the log data attribute will be treated as a simple text search on the log data content.

When filtering over log content, you can only use full tokens. The log content is split into tokens according to rules from the [Unicode Text Segmentationï»¿](https://unicode.org/reports/tr29/). Alternatively, you can use the wildcard \* at the end of the token.

You can turn **Advanced query** on and off to switch between the auto-complete and advanced modes. Dynatrace will transform the auto-complete filters to a query and vice versa provided that the query in the advanced mode can be transformed. Some complex queries with logical operators cannot be converted to auto-complete filters, in which case switching to auto-complete mode becomes unavailable.

In the advanced mode, you can run an empty query to return unfiltered log data.

Dynatrace search query language

1

Not applicable for log events, log metrics, and processing.

## Chart

The log chart is a histogram of log events over time that gives you a quick overview of logs and their severity within the selected timeframe.

## Results table

The results table under the chart displays the log events that match the provided query and filter within the selected timeframe. Each row in the table represents a log record and can be expanded for detailed log data. The first 100 matching records are displayed, but you can view more results by selecting **Show 100 more** at the bottom of the table.

By default, ingested log records are sorted according to timestamp and then according to the order that is maintained in the log source, where a log source is a remote process writing to a REST API endpoint or a remote process on which logs are detected.

By default, the log viewer displays a maximum of 1,000 log events. If you don't see expected results, run a more exact query or narrow down the timeframe to see better focused log data.

To show or hide specific columns in the result table

1. Select **Format table**.  
   This lists Dynatrace generated and reserved log attributes that you can add to the results table for visibility and use as dimensions when creating a log metric. For example, you can use the `dt.entity.process_group` attribute to display the process group instance for which the log event occurred.
2. Select or clear checkboxes to display or hide the corresponding columns in the table.

To export table data

1. Select **Actions**.
2. Select **Download table (JSON)** or **Download table (CSV)**, depending on the format you need.
   While your search query may return more than 1,000 log records, the result table will display only the first 1,000 log records. As a result, the exported table data will contain only the 1,000 log records visible in the table. The exported log records will include complete log data for each record, even if it is not displayed in the table column.

## Available attributes

**Available attributes** (displayed to the left of the table) provide you with an overview and the ability to filter the log data. **Available attributes** are automatically detected attributes of the data presented in the table. You can use them to quickly filter the result table data for a specific log data attribute. Each available attribute displays up to ten most popular values for that attribute. To filter all values for a particular attribute, create and run a query in the log viewer search.

## Log details

Unique log data attributes (high-cardinality attributes) such as `span_id` and `trace_id` generate unnecessarily excessive lists of available attributes that may impact log viewer performance. Because of this, they aren't listed in **Available attributes**. You can still use them in an advanced search query.