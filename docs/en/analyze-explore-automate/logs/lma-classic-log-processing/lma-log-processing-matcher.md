---
title: DQL matcher in logs
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-classic-log-processing/lma-log-processing-matcher
scraped: 2026-02-20T21:13:41.232737
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

  Name

  Type

  Mandatory

  Default

  Constraints

  Description

  expression

  string, array

  yes

  The expression (string or array of strings) that should be checked.

  phrase

  string

  yes

  The phrase to search for.

  caseSensitive

  boolean

  no

  false

  This optional parameter (`caseSensitive`) is not supported by the matcher. The `matchesPhrase` function in the matcher performs only case insensitive search.

  Whether the match should be done case-sensitive.
* **Example**  
  In this example, you add a filter that matches log records that contain `error` phrase in their content.

  ```
  matchesPhrase(content, "error")
  ```

  ### Examples of event processing using DQL matchesPhrase function

  Part of the input event

  Processing query

  Match result

  Description

  `attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1"`

  `matchesPhrase(attribute, "192.168.0.1")`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  Exact match by single term.

  `attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.123"`

  `matchesPhrase(attribute, "192.168.0.1")`

  ![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

  Non-word character is expected after character `1`.

  `attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.123"`

  `matchesPhrase(attribute, "192.168.0.1*")`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  The query would match all IPs with the last octet between `100` and `199`.

  `attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1"`

  `matchesPhrase(attribute, "failed to login")`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  Exact phrase match.

  `attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1"`

  `matchesPhrase(attribute, "failed to log")`

  ![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

  `log` is not a full word, non-word character is expected after `log`.

  `attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1"`

  `matchesPhrase(attribute, "failed to log*")`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  If the query ends with a wildcard character, the validation of the succeeding character is skipped.

  `attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1"`

  `matchesPhrase(attribute, "ed to login")`

  ![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

  `ed` is not a full word, the preceding character `l` is a part of the word.

  `attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1"`

  `matchesPhrase(attribute, "*ed to login")`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  If the query starts with a wildcard character, the validation of the preceding character is skipped.

  `attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1"`

  `matchesPhrase(attribute, "*ed to log*")`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  If the query starts and ends with a wildcard character, the validation of the preceding and succeeding characters is skipped.

  `attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1"`

  `matchesPhrase(attribute, "kÃ¤Ã¤rmanÃ¼ failed")`

  ![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

  There should be an apostrophe (`'`) character between `kÃ¤Ã¤rmanÃ¼` and `failed`.

  `attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1"`

  `matchesPhrase(attribute, "rmanÃ¼' failed")`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  Non-ASCII character `Ã¤` is treated as non-word character.

  `attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1"`

  `matchesPhrase(attribute, " 'kÃ¤Ã¤rmanÃ¼' failed")`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  If the query starts with non-word character, the validation of the preceding character is skipped.

  `attribute="Failed to assign monitoring configuration for com.dynatrace.extension"`

  `matchesPhrase(attribute, "configuration for")`

  ![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

  There is a space in the query and a tabulator in the attribute value.

  `attribute="Failed to assign monitoring configuration for com.dynatrace.extension"`

  `matchesPhrase(attribute, "failed to")`

  ![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

  There is a single space in the query and a double space in the attribute value

  `attribute="Failed to assign monitoring configuration for com.dynatrace.extension"`

  `matchesPhrase(attribute, "failed to")`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  It is possible to search with multiple spaces.

  `attribute=["Gdansk, Poland", "Linz, Austria", "Klagenfurt, Austria"]`

  `matchesPhrase(attribute, "Austria")`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  The function handles multi-value attributes in "any-match" manner, in this case `Austria` is matched in second and third value.

  `attribute=["Gdansk, Poland", "Linz, Austria", "Klagenfurt, Austria"]`

  `matchesPhrase(attribute, "Pol*")`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  Wildcard can be used also when dealing with multi-value attributes.

### matchesValue

Searches the records for a specific value in a given attribute. Returns only matching records. This function is case insensitive for ASCII characters, it works with multi-value attributes (matching any of the values), and it doesn't support mid-value wildcards.

* **Syntax**  
  `matchesValue(expression, value [, caseSensitive])`
* **Parameters**

  Name

  Type

  Mandatory

  Default

  Constraints

  Description

  expression

  string, array

  yes

  The expression (value or array of values) that should be checked.

  value

  string

  yes

  The value to search for.

  caseSensitive

  boolean

  no

  false

  This optional parameter (`caseSensitive`) is not supported by the matcher. The `matchesValue` function in the matcher performs only case insensitive search.

  Whether the match should be done case-sensitive.
* **Example**  
  In this example, you add a filter record where `process.technology` attribute contains `nginx` value.

  ```
  matchesValue(process.technology, "nginx")
  ```

  ### Examples of event processing using DQL matchesValue function

  Part of the input event

  Processing query

  Match result

  Description

  `attribute="Dynatrace"`

  `matchesValue(attribute, "dynaTrace")`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  Case insensitive equality.

  `attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1"`

  `matchesValue(attribute, "192.168.0.1")`

  ![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

  The whole attribute value is considered.

  `attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1"`

  `matchesValue(attribute, "*192.168.0.1")`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  The value ends with `192.168.0.1`.

  `attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1"`

  `matchesValue(attribute, "user*")`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  The value starts with `user` (case-insensitively).

  `attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1"`

  `matchesValue(attribute, "*failed to log*")`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  The value contains the string `failed to log`.

  `attribute="Ãsterreich"`

  `matchesValue(attribute, "Ã¶sterreich")`

  ![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

  Case insensitive only for ASCII characters.

  `attribute="Ãsterreich"`

  `matchesValue(attribute, "Ãsterreich")`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  Exact match.

  `attribute=["Java", "DOCKER", "k8s"]`

  `matchesValue(attribute, "docker")`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  The function handles multi-value attributes in "any-match" manner, in this case, `docker` is matched in the second value.

  `attribute=["Java11", "java17"]`

  `matchesValue(attribute, "java")`

  ![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

  None of the values is equal to string java.

  `attribute=["Java11", "java17"]`

  `matchesValue(attribute, "java*")`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  Both values start with a string `java`.

### isNotNull

Tests if a value is not NULL.

* **Syntax**  
  `isNotNull(<value>)`
* **Example**  
  In this example, we filter (select) data where the `host.name` field contains a value.

  ```
  isNotNull(`host.name`)
  ```

  timestamp

  content

  event.type

  host.name

  `2022-08-03 11:27:19`

  `2022-08-03 09:27:19.836 [QueueProcessor] RemoteReporter...`

  `LOG`

  `HOST-AF-710319`

  **Examples of event processing using DQL isNotNull function.**

  Part of the input event

  Processing query

  Match result

  Description

  ```
  {



  attribute="Dynatrace"



  }
  ```

  `isNotNull(other)`

  ![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

  The `other` attribute does not exists

  ```
  {



  attribute="Dynatrace"



  }
  ```

  `isNotNull(attribute)`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  The `attribute` has non-null value.

  ```
  {



  attribute=null



  }
  ```

  `isNotNull(attribute)`

  ![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

  The `attribute` has null value.

### isNull

Tests if a value is NULL.

* **Syntax**  
  `isNull(<value>)`
* **Example**  
  In this example, we filter (select) data where the `host.name` field doesn't contain a value.

  ```
  filter isNull(`host.name`)
  ```

  timestamp

  content

  event.type

  host.name

  `2022-08-03 12:53:26`

  `2022-08-03T10:52:31Z localhost haproxy[12529]: 192.168.19.100:38440`

  `LOG`

  ### Examples of event processing using DQL isNull function.

  Part of the input event

  Processing query

  Match result

  Description

  ```
  {



  attribute="Dynatrace"



  }
  ```

  `isNull(other)`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  The `other` attribute does not exists.

  ```
  {



  attribute="Dynatrace"



  }
  ```

  `isNull(attribute)`

  ![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

  The `attribute` has non-null value.

  ```
  {



  attribute=null



  }
  ```

  `isNull(attribute)`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  The `attribute` has null value.

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

  Part of the input event

  Processing query

  Match result

  Description

  ```
  {



  attribute="Dynatrace"



  }
  ```

  `attribute == "Dynatrace"`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  The attribute is of the string type and has the same value.

  ```
  {



  attribute="Dynatrace"



  }
  ```

  `attribute == "dynatrace"`

  ![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

  The strict equality is case-sensitive.

  ```
  {



  attribute="1"



  }
  ```

  `attribute == 1`

  ![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

  The attributes have different data types

  ```
  {



  attribute="1.0"



  }
  ```

  `attribute == 1`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  Floating numbers can be compared to integer values if their decimals equal 0

  ```
  {



  attribute=["Java", "DOCKER", "k8s"]



  }
  ```

  `attribute == "Java"`

  ![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

  The attributes have different data types.

## Grouping

You can create conditional grouping with brackets `( )`.

```
matchesValue(process.technology, "nginx") and ( matchesPhrase(content, "error") or matchesPhrase(content, "warn") )
```

## Reuse expressions

All the matcher expressions used in either log events, metrics, processing or bucket configurations are valid DQL. That means you can also use these expressions together with DQL filter command, for example, in the [log viewer](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer "Learn how to use Dynatrace log viewer to analyze log data.").

## Related topics

* [Conversion to DQL for Logs](/docs/analyze-explore-automate/logs/logs-upgrade/lma-dql-conversion "Convert your current log monitoring rules to DQL.")