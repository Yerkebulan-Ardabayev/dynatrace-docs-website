---
title: Log viewer (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer
scraped: 2026-02-19T21:28:44.516983
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

Category

Description

Example

Text search

Text searches help you find individual word occurrences. You can search text without any syntax (as long as no special characters or keywords are present, such as `OR` `"` `=` `\` ) In this text search we identify words and ignore any non alphanumeric (whitespaces, interpunction) characters between them.

Spaces are interpreted as AND operators:  
`search words` is equivalent to `content="search" AND content="words"`.

Also, this mode allows you to use double quotes:  
`"search phrase" more` is equivalent to `content="search phrase" AND content="more"`.

Searches are case-sensitive for attribute names, and case-insensitive for attribute values.
`content="SEARCH"` is equivalent to `content="search"`, but `MyAttribute="MyValue"` in NOT equivalent to `myattribute="MyValue"`.

The query has a limit of 20 relations: logical operators (AND, OR) or comparison operators (`=`, `!=`).

```
error



search words



"search phrase" more



content="SEARCH"
```

Attributes

Search for records that have a specified attribute with a specified value.  
Search for records that do not have a specified attribute with a specified value.  
Search for records that do not contain a specified phrase in the content field.  
You can write numbers without quotes, including positive and negative decimals (for example, -123.34)

```
host.name="HOST1"



host.name!="HOST1"



content!="search text"



http.code=123
```

Phrases

A phrase is a group of words surrounded by double quotes. Phrases are treated just like single-word terms in queries. This allows you to search log data for a specified phrase in the content field. It returns only those records in which the entire phrase matches. In this example, the word `search` must be immediately followed by the word `text`.

Keep in mind that using a phrase search for content takes into account only alphanumeric characters in the same manner as the text search described above.

```
content="search text"
```

Boolean operators

Allowed operators are `AND`, `OR` and can be written in either uppercase or lowercase. Log data matches `AND` when it contains both surrounding strings. Log data matches `OR` when it contains at least one of the surrounding strings. The logical operator `AND` is automatically inserted between single-word terms that are not surrounded by parentheses.  
**Precedence**: `AND`, `OR`

```
status="INFO" AND host.name="HOST1"
```

```
status="INFO" OR host.name="HOST1"
```

Grouping

Parentheses `( )` can be used to group clauses into sub-queries.

```
status="INFO" AND



(host.name="HOST1" OR host.name="HOST2")
```

Wildcards

Wildcards can be used to represent a variable or unknown alphanumeric characters in search terms. An asterisk `*` can be used to represent any string composed of alphanumeric characters. The `*` wildcard is only acceptable at the end of the search term. The search term cannot start with the `*` wildcard and the `*` wildcard cannot be used within the search term itself.

```
host.name="host*"
```

Special characters

Escaping special characters in attribute names or attribute values:

For attribute names:  
An attribute can contain any chars but `"=!\` or white space. If an attribute contains any of the special characters or keywords (like `AND` or `OR`), you need to wrap the whole name in backticks (`). Additionally, if an attribute name contains a backtick, you need to escape it with a backslash (\).

For attribute values:  
Special chars: `*` `"` `\` must be escaped with `\`.

For free text search mode:  
Wrap keywords with double quotes.

Values that contain special characters must be wrapped with double quotes and special characters must be escaped with `\`

```
`attri=bute`="\"abc"
```

Entity Selector[1](#fn-1-1-def)

Search for records using entity selector.

For more information, see [Environment API v2 - Entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.").

```
attribute inEntitySelector "$(entitySelector)"
```

```
dt.source_entity inEntitySelector "type(\"HOST\")"
```

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

Уникальные атрибуты журнала данных (атрибуты с высокой кардинальностью), такие как `span_id` и `trace_id`, генерируют излишне обширные списки доступных атрибутов, что может повлиять на производительность просмотрщика журналов. Из-за этого они не перечислены в **Доступных атрибутах**. Вы можете по-прежнему использовать их в расширенном запросе поиска.