---
title: DQL language reference
source: https://www.dynatrace.com/docs/platform/grail/dynatrace-query-language/dql-reference
scraped: 2026-02-22T21:14:06.791427
---

# DQL language reference

# DQL language reference

* Latest Dynatrace
* Reference
* Updated on Nov 06, 2025

A DQL query contains at least one or more [commands](/docs/platform/grail/dynatrace-query-language/commands "A list of DQL commands."), each of which returns tabular output containing records (lines or rows) and fields (columns). All commands are sequenced by a | (pipe). Data flows or is piped from one command to the next. The data is filtered or manipulated at each step and then streamed into the following step.

## DQL Syntax

The syntax can be described as follows:

`command parameter,.. [, optionalparameter],... | command â¦`

A syntactically valid example of a DQL query is:

```
fetch bizevents | summarize count()
```

A DQL command consists of mandatory and optional parameters which are comma-separated:

`summarize [field=] aggregation [, ...] [, by:{ [field=] groupexpression [, ...]}]`

* Mandatory parameters

  + aggregation
* Optional parameters

  + field
  + groupexpression

The required parameter is `aggregation`. For this command to be syntactically valid, at least one call to an [aggregation function](/docs/platform/grail/dynatrace-query-language/functions#aggregation-functions "A list of DQL functions.") has to be specified.

```
| summarize count()
```

Optionally, an assignment by using the equals sign `(=)` overrides the default field name from `count()` to `event_count`.

```
| summarize event_count = count()
```

The optional `by:` parameter defines a list of `groupexpression`. The output will have as many records as there are distinct values of all the `groupexpression`.

```
| summarize event_count = count(), by:{country=client.loc_cc, customer}
```

## Field naming rules

DQL Syntax verification applies the following naming rules:

![An example of a DQL query showing demonstrating the use of a command,  parameters and field identifiers.](https://dt-cdn.net/images/dql-ref-2418-19b3237798.png)

* Field names can use any sequence of Unicode characters.
* Field names using any character other than `a-zA-Z0-9_.` must be enclosed in backticks.
* Field names starting with any character other than `a-zA-Z_` must be enclosed in backticks.
* Backslash `\` is used as escape character.
* You need to escape backticks and backslashes in the field name.

Examples of valid field names are:

* `dt.entity.host`
* `location_US_EAST_1`
* `` `my host*` `` â must be enclosed in backticks
* `` `LOCAL_MACHINE\\Software` `` â uses a single backslash in the field name

## Parameters

Parameters for commands or functions have to be separated with a comma. Optional parameters need to be named.

Parameters can be:

* a value or an expression (for example: `now()-1h`)
* an execution block (for example: `[fetch logs]`). The execution block holds a sub-query.
* a group of parameters (see below)

### Parameter groups

If several parameters, either mandatory or optional, belong together, you should group them with curly braces (`{}`). This is especially important if the group is named. Using curly braces doesn't affect the data type. If you choose to group your parameters, you won't be able to use [DQL operators](/docs/platform/grail/dynatrace-query-language/operators "A list of DQL Operators.") with them.

The below example shows two groups of parameters. The first group holds the aggregations (not named), while the second group holds the fields by which to summarize (`by:`).

```
| summarize {min(value), max(value)}, by:{field1, field2}
```

## Sequential data processing

The following DQL query uses seven pipeline steps to get from raw log data to an aggregated table showing performance statistics for task execution.

![An example of a DQL query showing demonstrating the use of a command, a function, parameters and an expression.](https://dt-cdn.net/images/new-dql-query-3-1763-7b83cbcf34.png)

* **Line 1**

  ```
  fetch       logs, from:now()-10m
  ```

  You retrieve the log data using the [`fetch`](/docs/platform/grail/dynatrace-query-language/commands/data-source-commands#fetch "DQL data source commands") command. In addition, the optional `from:` parameter specifies the query start timestamp.
* **Line 2**

  ```
  // fetched all logs from the last hour: now() â 1h to now()
  ```

  Commented out line. This line will be omitted in query execution.
* **Line 3**

  ```
  | filter    endsWith(log.source, "pgi.log")
  ```

  The [`filter`](/docs/platform/grail/dynatrace-query-language/commands/filtering-commands#filter "DQL filter and search commands") command filters the log records based on the [`endsWith`](/docs/platform/grail/dynatrace-query-language/functions/string-functions#endsWith "A list of DQL string functions.") function that retrieves log files whose names end with the predefined string (the `pgi.log` string).
* **Line 4**

  ```
  | parse     content, "LD IPADDR:ip ':' LONG:payload SPACE LD 'HTTP_STATUS' SPACE INT:http_status  LD (EOL| EOS)"
  ```

  We use the [`parse`](/docs/platform/grail/dynatrace-query-language/commands/extraction-and-parsing-commands#parse "DQL extraction commands") command to extract key-value pairs containing execution statistics out of the raw log text string. In this case, it adds the `IP address`, `payload` and `http_status` fields to the result and transforms their data types into required formats.
* **Line 5, 6, 7, 8**

  ```
  | summarize total_payload = sum(payload),



  failedRequests = countIf(http_status >= 400),



  successfulRequests = countIf(http_status < 400),



  by:{ip, host.name}
  ```

  The [`summarize`](/docs/platform/grail/dynatrace-query-language/commands/aggregation-commands#summarize "DQL aggregation commands") command is a key element of DQL as it allows multiple aggregations across one or more fields. This query groups the results by `ip` and `host.name`. The retrieved records include the total value of payload, calculated using the [`sum`](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#sum "A list of DQL aggregation functions.") function, and two columns calculated using the [`countif`](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#countIf "A list of DQL aggregation functions.") function:

  + a column with numbers of failed requests (defined as those having `http_status` >=400)
  + a column with numbers of successful requests (defined as those having `http_status` <400)  
    This query groups the retrieved records by `ip` and `host.name`.
* **Line 9**

  ```
  |fieldsAdd total_payload_MB = total_payload/1000000
  ```

  With the [`fieldsAdd`](/docs/platform/grail/dynatrace-query-language/commands#fields-add "A list of DQL commands.") command, you add a new field showing the total payload converted into megabytes, basing on a mathematical expression.
* **Line 10**

  ```
  |fields    ip, host.name, failedRequests, successfulRequests, total_payload_MB
  ```

  With the [`fields`](/docs/platform/grail/dynatrace-query-language/commands/selection-and-modification-commands#fields "DQL selection and modification commands") command, you can determine which fields you need to retrieve.
* **Line 11**

  ```
  | sort  failedRequests desc
  ```

  The [`sort`](/docs/platform/grail/dynatrace-query-language/commands/ordering-commands#sort "DQL ordering commands") command is used to finalize the result. In this case, the results are sorted according to the number of failed requests, from the highest to lowest.

## DQL key building blocks

* [Commands](/docs/platform/grail/dynatrace-query-language/commands "A list of DQL commands.")
* [Functions](/docs/platform/grail/dynatrace-query-language/functions "A list of DQL functions.")  
  Functions can be used to perform any desired computation on fields of [DQL commands](/docs/platform/grail/dynatrace-query-language/commands "A list of DQL commands.").

* [Data types](/docs/platform/grail/dynatrace-query-language/data-types "A list of DQL data types.")  
  The Dynatrace Query Language operates with strongly typed data: functions and operators accept only declared types of data. The type is assigned to data during parsing or by using casting functions. DQL also recognizes value types expressed in literal notation (for example, using constant values in functions).

## Related topics

* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Use DQL queries](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.")
* [DQL compared to SQL and more](/docs/platform/grail/dynatrace-query-language/dql-comparison "See how DQL compares to other query languages.")
* [DQL commands](/docs/platform/grail/dynatrace-query-language/commands "A list of DQL commands.")
* [DQL functions](/docs/platform/grail/dynatrace-query-language/functions "A list of DQL functions.")
* [DQL operators](/docs/platform/grail/dynatrace-query-language/operators "A list of DQL Operators.")
* [DQL data types](/docs/platform/grail/dynatrace-query-language/data-types "A list of DQL data types.")
* [DQL best practices](/docs/platform/grail/dynatrace-query-language/dql-best-practices "Best practices for using Dynatrace Query Language.")