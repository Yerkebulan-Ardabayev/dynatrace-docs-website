---
title: Segments in DQL queries
source: https://www.dynatrace.com/docs/manage/segments/concepts/segments-concepts-queries
scraped: 2026-02-15T08:59:12.127444
---

# Segments in DQL queries

# Segments in DQL queries

* Latest Dynatrace
* Explanation
* 2-min read
* Published Mar 29, 2023

Segments are designed to act as context for DQL queries. Similar to **timeframes**, segments will directly impact how much data is scanned and returned for a given query.

## Key terms

Grail
:   Grail is the Dynatrace data lakehouse designed explicitly for observability data. It acts as a single unified storage solution for logs, metrics, traces, events, and more.

Dynatrace Query Language (DQL)
:   Dynatrace Query Language (DQL) is a powerful tool to explore your data and discover patterns, identify anomalies and outliers, create statistical modeling, and more based on data stored in Dynatrace Grail.

## Segments in DQL queries

Grail acts as the primary backend for apps on the Dynatrace platform. Data displayed in those apps is fetched from Grail using DQL queries.

* In more technical apps, such as **Notebooks** and **Dashboards**, you can directly craft and manipulate DQL queries.
* Other apps update data on the screen based on user interactions with simple web UI elements, issuing DQL queries underneath to fetch data.

Segments act as an optional context for DQL queries, injecting user-defined, preconfigured filter conditions.

During query execution, Grail evaluates only relevant conditions of segments passed based on the query's targeted data object. While a `fetch logs` query will look at filter conditions for logs only, a `timeseries` query will only evaluate filter conditions for metrics, and so on.

* Multiple conditions for the same data object in a single segment will result in OR-combined filter conditions.
* Conditions from multiple different segments will result in AND-combined filter conditions to form an intersection of parallelly selected segments.

For details on how segments are passed in the context of a DQL Query API request, see [ExecuteRequestï»¿](https://dt-url.net/6h03utf).