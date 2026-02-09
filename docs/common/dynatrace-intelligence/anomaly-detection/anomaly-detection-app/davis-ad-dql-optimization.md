---
title: "Anomaly Detection DQL optimization guide"
source: https://docs.dynatrace.com/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app/davis-ad-dql-optimization
updated: 2026-02-09
---

# Anomaly Detection DQL optimization guide

# Anomaly Detection DQL optimization guide

* Latest Dynatrace
* How-to guide
* 15-min read
* Updated on Dec 05, 2025

This page describes best practices for optimizing your DQL queries for ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** custom alerts to ensure a stable performance and minimized resource and time consumption.

[![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app "Explore anomaly detection configurations using the Anomaly Detection app.") uses the power of Grail to support a wide range of use cases through flexible DQL capabilities. This versatility allows for multiple solution approaches depending on the specific scenario. To ensure efficient and effective usage, this guide provides best practice examples that demonstrate how to get the most out of ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**.

## Minimize the volume of scanned data

Regardless of whether your queries are included in a rate card or not, we strongly recommend optimizing all DQL queries to minimize the amount of data being scanned. This will help you improve dashboard performance by significantly reducing rendering times and allow you to configure a greater number of read-based alerts within your environment.

## Manage your storage properly

A well-planned storage management strategy forms the foundation for optimal performance in your environment. We recommend organizing your [Dynatrace storage buckets](/docs/platform/grail/organize-data#built-in-grail-buckets "Insights on the Grail data model consisting of buckets, tables, and views.") based on the usage and access patterns of your teams to prevent excessive scanning across multiple teams or organizational units. We also suggest planning your storage structure upfront to simplify access permission policy management and ensure a more efficient and secure setup.

## Improve query optimization via DQL filters

### Rule 1: Always use a `bucket` filter

Buckets serve as the primary storage locations for raw data in Grail. By applying a bucket filter, you can direct Grail to analyze only the specific storage locations where the relevant data is expected, instead of scanning the entire storage. This approach helps you to:

* Reduce the processing cost.
* Minimize raw data movement across the network.
* Significantly improve the performance of dashboards and alerts.

You can see the examples of different bucket filtering options below:

Bucket filter in logs DQL query

```
fetch logs,bucket:{"bucketname"}
```

Bucket filter in spans DQL query

```
fetch spans, bucket:{"bucketname"}
```

Bucket filter in events DQL query

```
fetch events, bucket:{"bucketname"}
```

Incorporate the following DQL query to include the `dt.system.bucket` field, which identifies the source buckets for Grail records returned by an executed DQL query:

```
fetch logs



| fieldsAdd dt.system.bucket
```

This information helps you to pinpoint optimization opportunities in Grail by indicating where you can apply bucket filters. If dimensions originate from a single bucket while the query spans a broader scope, it can help you to identify potential targets for DQL optimization.

### Rule 2: Apply efficient filters as early as possible

The Dynatrace Grail storage engine is designed using highly distributed query nodes that independently scan and process raw data, including logs, traces, spans, and metrics. To maximize efficiency, we recommend excluding irrelevant portions of raw data as early as possible in the query request. This will help you reduce the scope of data collection and processing.

Do as much filtering as possible right after the `fetch` command.

The more raw data and buckets your DQL query excludes at the beginning, the more efficiently and quickly the result will be returned.

### Rule 3: Apply efficient string matching

Efficient string matching helps you to narrow your alerting scope and minimize the amount of time and resources necessary for running your custom alert. To apply efficient string matching in your custom alert we recommend that you:

* [Apply string comparison for known values](#apply-string-comparison).
* [Leverage token-based pattern matching](#leverage-token-based-matching).
* [Define fields and use filters when searching records](#tips-for-searching-records).
* [Be careful with when using partial matching](#tips-for-using-partial-matching).

#### Apply string comparison for known values

Use the `==` operator to filter known values. This is the most efficient way to narrow your alerting scope.

Filter fields matching the name `value`

```
| filter field == "value"
```

#### Leverage token-based pattern matching

In token-based pattern matching, Grail automatically splits incoming text into tokens. For example, a log message such as `ERROR checkout-id 3 http 504` is divided into multiple tokens by the matchers. This allows you to search for any part of the messageâfor instance, `ERROR`âand still find the full entry. Below are some examples of tokenization:

* Tokenized message, each token representing a term or a word:

  ```
  ERROR, checkout, id, 3, http, 504
  ```

Every non-alphanumeric character splits the incoming text into a separate token.

Let's take a look at a DQL query searching for a job failure to see how this works.

DQL, like many other data analysis tools, has a rich set of capabilities to match text. The `matchesPhrase()` function is built to match tokens. This means that the `| filter matchesPhrase(message, "error")` query will quickly and successfully match the necessary message, since Grail finds matching token `error`. Compared to `| filter contains(message, "error")`, it is less efficient because token matching is not applied.

Next, let's take a look at another example where we need to find a textual log message parsed by Grail. In this scenario, let's assume that a log message was a parsed, well-formed event in OpenPipeline and resulted in the following output:

```
status:âERRORâ<str> message:âERROR checkout-id 3 http 504â<str> errorcode:3<num> http.response:504<num>
```

In this case, the `~`operator is ideal for working with nested records or arrays. Similar to `matchesPhrase()`, it uses token-based pattern matching, but with the added advantage that it can match across multiple data types:

```
| filter message~âerrâ and http.response~504
```

It can further identify matches that occur inside nested records:

```
fetch spans| filter span.events~"err"
```

With the flexibility and finetuning abilities of DQL, you can search for matching names and keywords inside a list of `span.events` connected to a span, each consisting the multiple fields.

#### Tips for searching in records

To get the best results from tokenization, be specific about what you're looking for: define the field and use filters. Since the custom alert checks every field once per minute, failing to specify the field or utilizing tokenization without the filters might result in runtime-intense and resource-greedy queries.

For example, the query below, without a specified field or filters, will search through every field and consume additional resources:

```
| search "504" and "checkout"
```

Specifying the field, on the other hand, reduces the load and saves the time needed to find the match. For example:

* Filter fields with the key-value pairs `http.response==504` and `status=="ERROR"`: first choice

  ```
  | filter http.response==504 and status=="ERROR"
  ```

  Based on the most optimal OpenPipeline parsing, this type of filtering is always the first recommended choice.
* Use `search message` to look only through the `message` fields:

  ```
  | search message~"504" and message~"checkout"
  ```
* Filter `message` fields that have `504` and `checkout` elements:

  ```
  | filter message~"504" and message~"checkout"
  ```
* Filter `message` fields that match phrases `504` and `checkout` elements:

  ```
  | filter matchesPhrase(message,"504") and matchesPhrase(message,"checkout")
  ```

  This command might not be effective if the field is an array.
* Filter fields with the key-value pairs `http.response==504` and `status=="ERROR"`:

  ```
  | filter http.response==504 and status=="ERROR"
  ```

#### Tips for using partial matching on strings

Unlike the token filters above, these filters match only a part of the token. For example:

* Filtering fields that start with `value` will match fields like `value`, `values`, and `valueRange`. This might lead to including unnecessary fields.

  Filter fields that start with `value`

  ```
  | filter startWith(field, "value ")
  ```
* Filtering fields that contain the word `value` in the name is even broader than the `filter startWith()` command, and matches more potentially redundant fields.

  Filter fields that contain `value`

  ```
  | filter contains(field, "value")
  ```

To optimize filtering and avoid including redundant fields, we recommend trying the following:

* Always include a bucket filter.
* Include resource filters, like `dt.entity.<field> == "name"`.
* Include at least one entire token tilde or `matchesPhrase` filter.
* Either avoid less efficient filters or use them in addition to the filters mentioned above.

## Related topics

* [Anomaly Detection app](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app "Explore anomaly detection configurations using the Anomaly Detection app.")
* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Anomaly Detection DQL writing guide](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app/davis-ad-dql-best-practice "Best practices for creating Anomaly Detection custom alert DQL queries.")
