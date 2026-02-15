---
title: DQL commands
source: https://www.dynatrace.com/docs/platform/grail/dynatrace-query-language/commands
scraped: 2026-02-15T21:14:57.124713
---

# DQL commands

# DQL commands

* Latest Dynatrace
* Reference
* Updated on Nov 19, 2025

This page provides a list of DQL commands grouped by categories. To get more in-depth information on a specific command, click on its name.

## [Data source commands](/docs/platform/grail/dynatrace-query-language/commands/data-source-commands "DQL data source commands")

Name

Description

[data](/docs/platform/grail/dynatrace-query-language/commands/data-source-commands#data "DQL data source commands")

Generates sample data during query runtime.

[describe](/docs/platform/grail/dynatrace-query-language/commands/data-source-commands#describe "DQL data source commands")

Describes the on-read schema extraction definition for a given data object.

[fetch](/docs/platform/grail/dynatrace-query-language/commands/data-source-commands#fetch "DQL data source commands")

Loads data from the specified resource.

[load](/docs/platform/grail/dynatrace-query-language/commands/data-source-commands#load "DQL data source commands")

Loads data from the specified resource. It's used with [lookup data](/docs/platform/grail/lookup-data "Learn about lookup data in Grail.").

## [Metric commands](/docs/platform/grail/dynatrace-query-language/commands/metric-commands "DQL metric commands")

Name

Description

[timeseries](/docs/platform/grail/dynatrace-query-language/commands/metric-commands#timeseries "DQL metric commands")

Combines loading, filtering and aggregating metrics data into a time series output.

[metrics](/docs/platform/grail/dynatrace-query-language/commands/metric-commands#metrics "DQL metric commands")

Retrieves metric series.

## [Filter and search commands](/docs/platform/grail/dynatrace-query-language/commands/filtering-commands "DQL filter and search commands")

Name

Description

[dedup](/docs/platform/grail/dynatrace-query-language/commands/filtering-commands#dedup "DQL filter and search commands")

Removes duplicates from a list of records.

[filter](/docs/platform/grail/dynatrace-query-language/commands/filtering-commands#filter "DQL filter and search commands")

Reduces the number of records in a list by keeping only those records that match the specified condition.

[filterOut](/docs/platform/grail/dynatrace-query-language/commands/filtering-commands#filterOut "DQL filter and search commands")

Removes records that match a specific condition.

[search](/docs/platform/grail/dynatrace-query-language/commands/filtering-commands#search "DQL filter and search commands")

Searches for records that match the specified search condition.

## [Selection and modification commands](/docs/platform/grail/dynatrace-query-language/commands/selection-and-modification-commands "DQL selection and modification commands")

Name

Description

[fields](/docs/platform/grail/dynatrace-query-language/commands/selection-and-modification-commands#fields "DQL selection and modification commands")

Keeps only specified fields.

[fieldsAdd](/docs/platform/grail/dynatrace-query-language/commands/selection-and-modification-commands#fieldsAdd "DQL selection and modification commands")

Evaluates an expression and appends or replaces a field.

[fieldsKeep](/docs/platform/grail/dynatrace-query-language/commands/selection-and-modification-commands#fieldsKeep "DQL selection and modification commands")

Keeps selected fields.

[fieldsRemove](/docs/platform/grail/dynatrace-query-language/commands/selection-and-modification-commands#fieldsRemove "DQL selection and modification commands")

Removes fields from the result.

[fieldsRename](/docs/platform/grail/dynatrace-query-language/commands/selection-and-modification-commands#fieldsRename "DQL selection and modification commands")

Renames a field.

## [Extraction and parsing commands](/docs/platform/grail/dynatrace-query-language/commands/extraction-and-parsing-commands "DQL extraction commands")

Name

Description

[parse](/docs/platform/grail/dynatrace-query-language/commands/extraction-and-parsing-commands#parse "DQL extraction commands")

Parses a record field and puts the result into one or more fields as specified in the pattern.

## [Ordering commands](/docs/platform/grail/dynatrace-query-language/commands/ordering-commands "DQL ordering commands")

Name

Description

[limit](/docs/platform/grail/dynatrace-query-language/commands/ordering-commands#limit "DQL ordering commands")

Limits the number of returned records.

[sort](/docs/platform/grail/dynatrace-query-language/commands/ordering-commands#sort "DQL ordering commands")

Sorts the records.

## [Structuring commands](/docs/platform/grail/dynatrace-query-language/commands/structuring-commands "DQL structuring commands")

Name

Description

[expand](/docs/platform/grail/dynatrace-query-language/commands/structuring-commands#expand "DQL structuring commands")

Expands an array into separate records.

[fieldsFlatten](/docs/platform/grail/dynatrace-query-language/commands/structuring-commands#fieldsFlatten "DQL structuring commands")

Extracts/flattens fields from a nested record.

## [Aggregation commands](/docs/platform/grail/dynatrace-query-language/commands/aggregation-commands "DQL aggregation commands")

Name

Description

[fieldsSummary](/docs/platform/grail/dynatrace-query-language/commands/aggregation-commands#fieldsSummary "DQL aggregation commands")

Calculates the cardinality of field values that the specified fields have.

[makeTimeseries](/docs/platform/grail/dynatrace-query-language/commands/aggregation-commands#makeTimeseries "DQL aggregation commands")

Creates timeseries from the data in the stream.

[summarize](/docs/platform/grail/dynatrace-query-language/commands/aggregation-commands#summarize "DQL aggregation commands")

Groups together records that have the same values for a given field and aggregates them.

## [Correlation and join commands](/docs/platform/grail/dynatrace-query-language/commands/correlation-and-join-commands "DQL correlation and join commands")

Name

Description

[append](/docs/platform/grail/dynatrace-query-language/commands/correlation-and-join-commands#append "DQL correlation and join commands")

Appends a given list of records by the records returned by a sub-query.

[join](/docs/platform/grail/dynatrace-query-language/commands/correlation-and-join-commands#join "DQL correlation and join commands")

Joins all records from the source and the sub-query as long as they fulfill the join condition.

[joinNested](/docs/platform/grail/dynatrace-query-language/commands/correlation-and-join-commands#join-nested "DQL correlation and join commands")

Adds matching results from the sub-query as an array of nested records.

[lookup](/docs/platform/grail/dynatrace-query-language/commands/correlation-and-join-commands#lookup "DQL correlation and join commands")

Adds fields from a subquery to the source table by finding a match between a field in the source table and the lookup table.

## [Smartscape commands](/docs/platform/grail/dynatrace-query-language/commands/smartscape-commands "DQL Smartscape commands")

Name

Description

[smartscapeNodes](/docs/platform/grail/dynatrace-query-language/commands/smartscape-commands#smartscapeNodes "DQL Smartscape commands")

Loads Smartscape nodes using a type pattern (use `*` for all types).

[smartscapeEdges](/docs/platform/grail/dynatrace-query-language/commands/smartscape-commands#smartscapeEdges "DQL Smartscape commands")

Loads Smartscape edges using an edge type pattern (use `*` for all types).

[traverse](/docs/platform/grail/dynatrace-query-language/commands/smartscape-commands#traverse "DQL Smartscape commands")

Traverses source nodes to target nodes in the specified direction, following edge types defined by edgeTypes.

## Related topics

* [Use DQL queries](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.")
* [DQL language reference](/docs/platform/grail/dynatrace-query-language/dql-reference "Dynatrace Query Language syntax reference.")
* [DQL functions](/docs/platform/grail/dynatrace-query-language/functions "A list of DQL functions.")
* [DQL operators](/docs/platform/grail/dynatrace-query-language/operators "A list of DQL Operators.")
* [DQL data types](/docs/platform/grail/dynatrace-query-language/data-types "A list of DQL data types.")
* [DQL best practices](/docs/platform/grail/dynatrace-query-language/dql-best-practices "Best practices for using Dynatrace Query Language.")