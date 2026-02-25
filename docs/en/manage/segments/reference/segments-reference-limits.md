---
title: Segment limits
source: https://www.dynatrace.com/docs/manage/segments/reference/segments-reference-limits
scraped: 2026-02-25T21:22:57.362193
---

# Segment limits

# Segment limits

* Latest Dynatrace
* Reference
* 1-min read
* Updated on Oct 21, 2025

## General

* 10,000 segments per environment
* 20 include blocks per segment
* 1 include block per type (for example, Logs, Metrics, Spans etc.)
* 1 expression per filter condition minimum
* 10 expressions per filter condition maximum
* 10,000 values in the variable dropdown
* 10 segments per query

### Classic entities

For classic entities, various limits apply. These limits don't apply to Smartscape on Grail.

* 1 additional include per classic entity type + relationship (entity includes only)
* Conditions for related classic entities can be empty
* 100 selected variable values per segment

## Include block conditions

### All data

* Only fields and values of type `STRING`, and `ARRAY_OR_STRINGS` are supported
* Only operators `=`, and `in()` are supported

  + You can use wildcards `*` for `starts-with`, `contains`, and `ends-with` matches. For details, see [Wildcards](/docs/discover-dynatrace/get-started/dynatrace-ui/ui-filter-field#wildcards "The filter field is a powerful tool that allows you to quickly find relevant information or narrow down results within apps.").
  + Asterisks are allowed to follow variable names in conditions for `starts-with` (for example, `foo = $bar*`)

### Classic entities

For classic entities, various limits apply. These limits don't apply to Smartscape on Grail.

* Only selected properties (suggested in the filter field) are allowed
* `starts-with`, `contains`, and `ends-with` are not supported

  + The only exception is `entity.name`, which supports `starts-with`
  + Other properties only support `equals`