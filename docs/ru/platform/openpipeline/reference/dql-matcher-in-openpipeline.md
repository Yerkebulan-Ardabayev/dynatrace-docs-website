---
title: DQL matcher in OpenPipeline
source: https://www.dynatrace.com/docs/platform/openpipeline/reference/dql-matcher-in-openpipeline
scraped: 2026-02-28T21:20:11.243915
---

# DQL matcher in OpenPipeline

# DQL matcher in OpenPipeline

* Latest Dynatrace
* Reference
* 8-min read
* Updated on Dec 15, 2025

With [Dynatrace powered by Grail](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more."), you can use [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") (DQL) functions and logical operators in matchers.

The matcher filters the ingested data and reduces the scope of data processed by the processor that you create. You can use the matcher in [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.") to:

* Filter records containing a specified phrase.
* Search data for a specific value in a given attribute.
* Test if a value is null.
* Use logical operators to connect two or more expressions.
* Request logs that show duration for requests longer than `1s`.

To learn about the use of logical operators in DQL, see [Logical or equality operators](/docs/platform/grail/dynatrace-query-language/operators#dql-logical-or-equality-operators "A list of DQL Operators.").

## Functions

### matchesPhrase

Filters records containing a specified phrase. Returns only matching records. This function is case insensitive for ASCII characters, it works with multi-value attributes (matching any of the values), and the asterisk character (`*`) is a wildcard only referring to a single term, not the whole field value.

##### Validation

The `matchesPhrase` function performs case-insensitive [contains](/docs/platform/grail/dynatrace-query-language/functions#contains "A list of DQL functions.") for the whole query string and doesn't support mid-string wildcards.
For found results, additional validation takes place:

* If the query starts with a word character, the preceding character must be a non-word character.
* If the query ends with a word character, the succeeding character must be a non-word character.
* If the query starts with an asterisk, no validation of the preceding character is performed.
* If the query ends with an asterisk, no validation of the succeeding character is performed.

##### Syntax

`matchesPhrase(expression, phrase)`

##### Parameters

##### Example

In this example, you add a filter that matches log records that contain `error` phrase in their content.

```
matchesPhrase(content, "error")
```

##### Examples of event processing using DQL matchesPhrase function

### matchesValue

Searches the records for a specific value in a given attribute. Returns only matching records. This function is case insensitive for ASCII characters, it works with multi-value attributes (matching any of the values), and it doesn't support mid-value wildcards.

##### Syntax

`matchesValue(expression, value)`

##### Parameters

##### Example

In this example, you add a filter record where `process.technology` attribute contains `nginx` value.

```
matchesValue(process.technology, "nginx")
```

##### Examples of event processing using DQL matchesValue function

### isNotNull

Tests if a value is not NULL.

##### Syntax

`isNotNull(<value>)`

##### Example

In this example, we filter (select) data where the `host.name` field contains a value.

```
isNotNull(`host.name`)
```

**Examples of event processing using DQL isNotNull function**

### isNull

Tests if a value is NULL.

##### Syntax

`isNull(<value>)`

##### Example

In this example, we filter (select) data where the `host.name` field doesn't contain a value.

```
filter isNull(`host.name`)
```

**Examples of event processing using DQL isNull function**

## Operators

Logical operators can be used to connect two or more expressions. Check out [Logical or equality operators](/docs/platform/grail/dynatrace-query-language/operators#dql-logical-or-equality-operators "A list of DQL Operators.") to find out more about the behavior of logical operators in DQL.

### OR

Logical addition.

##### Syntax

`<expression_1> or <expression_2>`

##### Example

In this example, you add a matcher to filter records where the content contains either `timestamp` phrase or `trigger` phrase.

```
matchesPhrase(content, "timestamp") or matchesPhrase(content, "trigger")
```

### AND

Logical multiplication.

##### Syntax

`<expression_1> and <expression_2>`

##### Example

In this example, you add a matcher to filter records where the content contains `timestamp` phrase and `trigger` phrase.

```
matchesPhrase(content, "timestamp") and matchesPhrase(content, "trigger")
```

### NOT

Logical negation.

##### Syntax

`not <expression>`

##### Example

In this example, you add a matcher to filter records where the content doesn't contain `timestamp` phrase.

```
not matchesPhrase(content, "timestamp")
```

### Boolean literals

The matcher supports the following conditions:

* `true`â the processor (DQL query) will be applied to all records
* `false`â the processor will not be applied to any of the records in the data set

##### Literal notation

A Boolean value can be expressed using either uppercase or lowercase letters: `true`, `TRUE`, `false`, `FALSE`.

### Iterative expressions

#### iAny

Checks an iterative boolean expression and returns `true`, if the expression was true at least once, `false` if it wasn't. For example:

```
iAny(a[] > 2)
```

### Numerical operators

With DQL matcher in OpenPipeline, you can use the following numerical operators:

* `<`âLess than, for example `http.request.body.size < 1024`
* `>`âGreater than, for example `http.request.body.size > 1024`
* `<=`âLess than or equal to, for example `http.request.body.size <= 1024`
* `>=`âGreater than or equal to, for example `http.request.body.size >= 1024`
* `==`âEquals, for example `http.request.body.size == 1024`

#### Strict equality

[Logical operator](/docs/platform/grail/dynatrace-query-language/operators "A list of DQL Operators.") (`==`) indicating an exact match.

Configuration scopes need to be identical. However, if the decimal value is `0`, floating numbers can be compared with integer data. For example, `1==1.0`.
For strings, the search is case-sensitive.

Contrary to `matchesValue` function, `strict equality` operator performs case-sensitive comparison, doesn't support wildcards and doesn't operate on elements being part of multi-value attributes.

##### Syntax

`fieldName == <expression>`

## Related topics

* [DQL Functions in OpenPipeline](/docs/platform/openpipeline/reference/openpipeline-dql-functions "A list of DQL functions available in OpenPipeline.")
* [DQL Commands](/docs/platform/openpipeline/reference/openpipeline-dql-commands "A list of DQL commands available in OpenPipeline.")
* [DQL Operators in OpenPipeline DQL processor](/docs/platform/openpipeline/reference/openpipeline-dql-operators "A list of DQL operators available in OpenPipeline DQL processor.")