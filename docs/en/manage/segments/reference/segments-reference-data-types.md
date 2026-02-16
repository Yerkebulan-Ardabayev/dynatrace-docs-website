---
title: Supported data types in segments
source: https://www.dynatrace.com/docs/manage/segments/reference/segments-reference-data-types
scraped: 2026-02-16T09:16:27.489558
---

# Supported data types in segments

# Supported data types in segments

* Latest Dynatrace
* Reference
* 1-min read
* Published Mar 29, 2023

Prior knowledge

* [Include data in segments](/docs/manage/segments/concepts/segments-concepts-includes#data-types "Learn how data of different types can be included in segments.")

We recommend constructing segments with a single `Data (all types)` include block when possible. This gives you the most flexibility for using the segment in different scenarios.

Type

Applicable to

`Data (all types)`

Applicable to queries for any signal data type (such as `fetch logs`), entities (such as `smartscapeNodes "*"`, `fetch dt.entity.host`), or data in other Grail-tables (such as `fetch metric.series`).

`Metrics`, `Logs`, `Spans`, etc.

Applicable to any query for the specific signal data type (such as `fetch logs`).

`Entities`

Applicable to queries for entities (such as `smartscapeNodes "*"`, `fetch dt.entity.host`).

`Host (dt.entity.host)`, etc.

Applicable to queries for classic entities of specified type (such as fetch `dt.entity.host`).