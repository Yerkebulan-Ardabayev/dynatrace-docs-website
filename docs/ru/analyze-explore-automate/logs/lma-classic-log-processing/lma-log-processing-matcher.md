---
title: DQL matcher in logs
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-classic-log-processing/lma-log-processing-matcher
scraped: 2026-03-01T21:22:56.017928
---

# DQL matcher in logs

# DQL matcher in logs

* Latest Dynatrace
* Reference
* 1-min read
* Updated on Oct 15, 2025

With [Dynatrace on Grail](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more."), you can use [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") (DQL) functions and logical operators in matchers.

The matcher filters the ingested data and reduces the scope of data processed by the rule that you create. You can use the matcher in log and event processing, log metrics, log events, and log buckets to:

* Filter records containing a specified phrase.
* Search log data for a specific value in a given attribute.
* Test if a value is NULL.
* Use logical operators to connect two or more expressions.

  To learn about the use of logical operators in DQL, see [Logical or equality operators](/docs/platform/grail/dynatrace-query-language/operators#dql-logical-or-equality-operators "A list of DQL Operators.").

## Functions

### matchesPhrase

Filters records containing a specified phrase. Returns only matching records. This function is case insensitive for ASCII characters, it works with multi-value attributes (matching any of the values), and the asterisk character (`*`) is a wildcard only referring to a single term, not the whole field value.

* **Validation**  
  The `matchesPhrase` function performs case-insensitive [contains](/docs/platform/grail/dynatrace-query-language/functions#contains "A list of DQL functions.") for the whole query string and doesn't support mid-string wildcards.
  For found results, additional validation takes place:

  + if the query starts with a word character, the preceding character must be a non-word character.
  + if the query ends with a word character, the succeeding character must be a non-word character.
  + if the query starts with an asterisk, no validation of the preceding character is performed.
  + if the query ends with an asterisk, no validation of the succeeding character is performed.
* **Syntax**  
  `matchesPhrase(expression, phrase [, caseSensitive])`
* **Parameters**
* **Example**  
  In this example, you add a filter that matches log records that contain `error` phrase in their content.

  ```
  matchesPhrase(content, "error")
  ```

  ### Examples of event processing using DQL matchesPhrase function

### matchesValue

Searches the records for a specific value in a given attribute. Returns only matching records. This function is case insensitive for ASCII characters, it works with multi-value attributes (matching any of the values), and it doesn't support mid-value wildcards.

* **Syntax**  
  `matchesValue(expression, value [, caseSensitive])`
* **Parameters**
* **Example**  
  In this example, you add a filter record where `process.technology` attribute contains `nginx` value.

  ```
  matchesValue(process.technology, "nginx")
  ```

  ### Examples of event processing using DQL matchesValue function

### isNotNull

Tests if a value is not NULL.

* **Syntax**  
  `isNotNull(<value>)`
* **Example**  
  In this example, we filter (select) data where the `host.name` field contains a value.

  ```
  isNotNull(`host.name`)
  ```

  **Examples of event processing using DQL isNotNull function.**

### isNull

Tests if a value is NULL.

* **Syntax**  
  `isNull(<value>)`
* **Example**  
  In this example, we filter (select) data where the `host.name` field doesn't contain a value.

  ```
  filter isNull(`host.name`)
  ```

  ### Examples of event processing using DQL isNull function.

## Operators

Logical operators can be used to connect two or more expressions. Check out [Logical or equality operators](/docs/platform/grail/dynatrace-query-language/operators#dql-logical-or-equality-operators "A list of DQL Operators.") to find out more about the behavior of logical operators in DQL.

### OR

Logical addition.

* **Syntax**  
  `<expression_1> or <expression_2>`
* **Example**  
  In this example, you add a matcher to filter records where the content contains either `timestamp` phrase or `trigger` phrase.

  ```
  matchesPhrase(content, "timestamp") or matchesPhrase(content, "trigger")
  ```

### AND

Logical multiplication.

* **Syntax**  
  `<expression_1> and <expression_2>`
* **Example**  
  In this example, you add a matcher to filter records where the content contains `timestamp` phrase and `trigger` phrase.

  ```
  matchesPhrase(content, "timestamp") and matchesPhrase(content, "trigger")
  ```

### NOT

Logical negation.

* **Syntax**  
  `not <expression>`
* **Example**  
  In this example, you add a matcher to filter records where the content doesn't contain `timestamp` phrase.

  ```
  not matchesPhrase(content, "timestamp")
  ```

### Strict equality

[Logical operator](/docs/platform/grail/dynatrace-query-language/operators "A list of DQL Operators.") (`==`) indicating an exact match.

Data types need to be identical. However, if the decimal value is `0`, floating numbers can be compared with integer data. For example, `1==1.0`  
For strings, the search is case-sensitive.

Contrary to `matchesValue` function, `strict equality` operator performs case-sensitive comparison, doesn't support wildcards and doesn't operate on elements being part of multi-value attributes.

* **Syntax**  
  `<expression1> == <expression2>`
* **Examples**

  Examples of using the strict equality operator.

## Grouping

You can create conditional grouping with brackets `( )`.

```
matchesValue(process.technology, "nginx") and ( matchesPhrase(content, "error") or matchesPhrase(content, "warn") )
```

## Reuse expressions

All the matcher expressions used in either log events, metrics, processing or bucket configurations are valid DQL. That means you can also use these expressions together with DQL filter command, for example, in the [log viewer](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer "Learn how to use Dynatrace log viewer to analyze log data.").

## Related topics

* [Conversion to DQL for Logs](/docs/analyze-explore-automate/logs/logs-upgrade/lma-dql-conversion "Convert your current log monitoring rules to DQL.")