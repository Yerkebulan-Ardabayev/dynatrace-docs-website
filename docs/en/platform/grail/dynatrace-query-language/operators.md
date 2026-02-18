---
title: DQL operators
source: https://www.dynatrace.com/docs/platform/grail/dynatrace-query-language/operators
scraped: 2026-02-18T05:37:50.137739
---

# DQL operators

# DQL operators

* Latest Dynatrace
* Reference
* 22-min read
* Updated on Oct 28, 2025

The following table shows a list of all the DQL operators.

Operator

Description

`+`

Addition

`-`

Subtraction or arithmetic negation

`*`

Multiplication

`/`

Division

`%`

Modulo

`<`

Less than

`<=`

Less than or equal to

`>`

Greater than

`>=`

Greater than or equal to

`==`

Equals

`!=`

Does not equal

`not`

Logical NOT (negation)

`and`

Logical AND

`or`

Logical OR

`xor`

Logical XOR (exclusive or)

`in`

Subquery comparison

`@`

Time alignment

`~`

Search

The precedence for the operators is as follows (from strongest to weakest):

* `-` (arithmetic negation)
* `*`, `/`, `%`
* `@`
* `+`, `-` (subtraction)
* `~`
* `==`, `!=`, `>`, `>=`, `<`, `<=`
* `in`
* `not`
* `and`
* `xor`
* `or`

## Arithmetic operators

You can use arithmetic operators with numbers, represented by both the types `long` or `double`. In addition, some operators support the types `timestamp`, `timeframe`, `duration` or `ip`.

Operator

Description

Example

`+`

Addition

`2 + 2.5`

`-`

Subtraction

`0.2 - 0.11`

`*`

Multiplication

`4 * 5`, `60 * 1s`

`/`

Division

`10 / 2`, `1h / 60`

`%`

Modulo

`4 % 2`

`-`

Arithmetic negation

`-1`

### ADDITION

| ADDITION | Long | Double | String | Boolean | Timestamp | Duration | Timeframe | Binary | IP | UID | Array | Record |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Long | Applicable (long) | Applicable (double) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Applicable (IP) | Not applicable | Not applicable | Not applicable |
| Double | Applicable (double) | Applicable (double) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Applicable (IP) | Not applicable | Not applicable | Not applicable |
| String | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Boolean | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Timestamp | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Applicable (timestamp) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Duration | Not applicable | Not applicable | Not applicable | Not applicable | Applicable (timestamp) | Applicable (duration) | Applicable (timeframe) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Timeframe | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Applicable (timeframe) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Binary | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| IP | Applicable (IP) | Applicable (IP) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Applicable (IP) | Not applicable | Not applicable | Not applicable |
| UID | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Array | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Record | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |

### SUBTRACTION

| SUBTRACTION | Long | Double | String | Boolean | Timestamp | Duration | Timeframe | Binary | IP | UID | Array | Record |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Long | Applicable (long) | Applicable (double) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Double | Applicable (double) | Applicable (double) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| String | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Boolean | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Timestamp | Not applicable | Not applicable | Not applicable | Not applicable | Applicable (duration) | Applicable (timestamp) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Duration | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Applicable (duration) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Timeframe | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Applicable (timeframe) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Binary | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| IP | Applicable (IP) | Applicable (IP) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Applicable (IP) | Not applicable | Not applicable | Not applicable |
| UID | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Array | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Record | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |

### MULTIPLICATION

| MULTIPLICATION | Long | Double | String | Boolean | Timestamp | Duration | Timeframe | Binary | IP | UID | Array | Record |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Long | Applicable (long) | Applicable (double) | Not applicable | Not applicable | Not applicable | Applicable (duration) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Double | Applicable (double) | Applicable (double) | Not applicable | Not applicable | Not applicable | Applicable (duration, rounded to full nanos) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| String | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Boolean | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Timestamp | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Duration | Applicable (duration) | Applicable (duration, rounded to full nanos) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Timeframe | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Binary | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| IP | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| UID | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Array | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Record | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |

### DIVISION

Integer division

When you divide a `long` value by another `long` value using the `/` operator, the result is also a `long` value, and any fractional part is discarded. To get a result with the fractional part (a `double` value), you need to convert or cast at least one of the operands to `double` (e.g., by using the [toDouble](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#toDouble "A list of DQL conversion and casting functions.") function).

| DIVISION | Long | Double | String | Boolean | Timestamp | Duration | Timeframe | Binary | IP | UID | Array | Record |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Long | Applicable (long) | Applicable (double) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Double | Applicable (double) | Applicable (double) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| String | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Boolean | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Timestamp | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Duration | Applicable (duration rounded to full nanos) | Applicable (duration rounded to full nanos) | Not applicable | Not applicable | Not applicable | Applicable (double) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Timeframe | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Binary | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| IP | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| UID | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Array | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Record | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |

The data type resulting from the operation is indicated in parentheses in the table above.

### MODULO

| MODULO | Long | Double | String | Boolean | Timestamp | Duration | Timeframe | Binary | IP | UID | Array | Record |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Long | Applicable (long) | Applicable (double) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Double | Applicable (double) | Applicable (double) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| String | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Boolean | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Timestamp | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Duration | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Applicable (duration) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Timeframe | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Binary | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| IP | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| UID | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Array | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Record | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |

### ARITHMETIC NEGATION

| NEGATION | Long | Double | String | Boolean | Timestamp | Duration | Timeframe | Binary | IP | UID | Array | Record |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SELF | Applicable (long) | Applicable (double) | Not applicable | Not applicable | Not applicable | Applicable (duration) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |

## Comparison operators

Operator

Description

Example

`<`

Less than

`8 < 9`, `now()-1m < now()`

`<=`

Less than or equal to

`4 <= 5`

`>`

Greater than

`5 > 4`, `"a" > "A"`

`>=`

Greater than or equal to

`4 >=4`

### Comparison operators (<, <=, >, >=)

* ( ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable") ) - `true` or `false` based on the result of the operator
* ( ![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") ) - `null`

| <, <=, >, >= | Long | Double | String | Boolean | Timestamp | Duration | Timeframe | Binary | IP | UID | Array | Record |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Long | Applicable | Applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Double | Applicable | Applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| String | Not applicable | Not applicable | Applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Boolean | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Timestamp | Not applicable | Not applicable | Not applicable | Not applicable | Applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Duration | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Timeframe | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Binary | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| IP | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Applicable | Not applicable | Not applicable | Not applicable |
| UID | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Array | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Record | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |

## Equality operators

Operator

Description

Example

`==`

Equals

`2 == 2`

`!=`

Does not equal

`1 != 2`

Equality comparisons (`==`, `!=`) use a tri-state boolean algebra (`true`, `false`, `null`). This means that if any side of the equality comparison is `null`, the overall result of the comparison is `null`.
There are four DQL functions that cover scenarios where missing or `null` records need to be retrieved:

* The [`isTrueOrNull` function](/docs/platform/grail/dynatrace-query-language/functions/boolean-functions#isTrueOrNull "A list of DQL boolean functions.")
* The [`isFalseOrNull` function](/docs/platform/grail/dynatrace-query-language/functions/boolean-functions#isFalseOrNull "A list of DQL boolean functions.")
* The [`isNull` function](/docs/platform/grail/dynatrace-query-language/functions/boolean-functions#isNull "A list of DQL boolean functions.")
* The [`isNotNull` function](/docs/platform/grail/dynatrace-query-language/functions/boolean-functions#isNotNull "A list of DQL boolean functions.")

For example, the below query that uses basic filtering does not provide records with `null` or missing values:

```
fetch logs



| filter log.source != "logsourcename"  // does not provide the records where `log.source` is null or missing
```

However, using the `isTrueOrNull` function includes those records with `null` and missing values:

```
fetch logs



| filter isTrueOrNull(log.source != "logsourcename") // also provides the records where `log.source` is null or missing
```

### Equality operators (==, !=)

* ( ![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") ) - `false` for non-comparable types in case of `==` operator, `true` for non-compatible types in case of `!=` operator
* ( ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable") ) - `true` or `false` based on the result of the operator
* `null` - if one of the operands is `null`
* `null == null` - `null`

| ==, != | Long | Double | String | Boolean | Timestamp | Duration | Timeframe | Binary | IP | UID | Array | Record |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Long | Applicable | Applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Double | Applicable | Applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| String | Not applicable | Not applicable | Applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Boolean | Not applicable | Not applicable | Not applicable | Applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Timestamp | Not applicable | Not applicable | Not applicable | Not applicable | Applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Duration | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Timeframe | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Binary | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| IP | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Applicable | Not applicable | Not applicable | Not applicable |
| UID | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Applicable | Not applicable | Not applicable |
| Array | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Applicable | Not applicable |
| Record | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Applicable |

## Logical operators

Operator

Description

Example (yields true)

`not`

Logical NOT (negation) - Negates a logical state

`not 2==1`

`and`

Logical AND (multiplication) - Yields `true` if both operands are `true`.

`not 2==1 and 1<2`

`or`

Logical OR (addition) - Yields `true` if one of the operands is `true`, regardless of the other operand.

`1 < 2 or 1 > 2`

`xor`

Logical XOR (exclusive OR) - Yields `true` if one of the operands is `true`, but `false` in case both are `true`.

`1 < 2 xor 1 > 2`

The behavior of logical operators follows the tri-state boolean logic.

* **AND**

  + `true` AND `null` = `null`
  + `null` AND `true` = `null`
  + `false` AND `null` = `false`
  + `null` AND `false` = `false`
  + `null` AND `null` = `null`
* **OR**

  + `true` OR `null` = `true`
  + `null` OR `true` = `true`
  + `false` OR `null` = `null`
  + `null` OR `false` = `null`
  + `null` OR `null` = `null`
* **XOR**

  + `true` XOR `null` = `null`
  + `null` XOR `true` = `null`
  + `false` XOR `null` = `null`
  + `null` XOR `false` = `null`
  + `null` XOR `null` = `null`
* **NOT**

  + NOT `null` = `null`

## Iterative expressions

Iterative expressions can be used to evaluate every element of a given array or every i-th element of one or more arrays.

### iAny

Checks an iterative boolean expression and returns `true`, if the expression was true at least once, `false` if it wasn't. For example:

```
fetch logs



| fieldsAdd a = array(1, 2, 3)



| filter iAny(a[] > 2)
```

### iCollectArray

Collects the results of an iterative expression into an array. For example:

```
fetch logs



| fieldsAdd a = array(1, 2, 3), b = array(10, 11, 12)



| fieldsAdd iCollectArray(a[] + b[])
```

### iIndex

Allows to access the index of an iterative expression element. For example, you can add the index of a value in the array and expand the array.

```
data record(a = array(2, 3, 7, 7, 1))



| fields a = record(value = a[], index = iIndex())



| expand a



| fields value = a[value], index = a[index]
```

iIndex only works in expressions where at least one iterative expression is present.

## Operators for subqueries

### in

The `in` comparison operator evaluates the occurrence of a value returned by the left side's expression within a list of values returned by the right side's DQL subquery.

**Syntax**

`expression in [execution block]`

**Usage and constraints**

Name

Type

Mandatory

Constraints

Description

left side

expression

yes

Either a field identifier or an expression.

The element to be found in the list returned by the right side's subquery.

right side

execution block

yes

It has to return a single field providing a list of values.

The DQL Subquery which returns the list of values to compare against.

**Example**

This example shows how to use the `in` keyword for filtering a host metric for the host's attribute:

```
timeseries avg(dt.host.cpu.usage), filter:dt.entity.host in [fetch dt.entity.host



| fieldsAdd tags



| expand tags



| filter tags == "ServiceNow" | fields id]
```

## Time alignment

The `@` operator aligns a timestamp to the provided time unit. It rounds down the timestamp to the beginning of the time unit.

#### Syntax

`[timestamp|duration|calendarDuration] @ unit`

#### Left side

On the left side of the `@` operator, you can use a `timestamp` expression, a `duration` expression, or a calendar duration.  
If you use the `@` operator without an expression on the left side, the operator will use the timestamp expression `now()` and will align the current time to the time unit. For example, `@h` is the beginning of the current hour, and equivalent to `now()@h`. Expressions of type `duration` and calendar durations are considered as an offset to `now()`.  
For example, `-2M@..`. is equivalent to `(now() - 2M)@...`.

#### Right side

The time unit can be any DQL supported [duration unit](/docs/platform/grail/dynatrace-query-language/data-types#duration "A list of DQL data types.") including `s` (second), `m` (minute), `h` (hour), or a calendar duration unit like `d` (day), `w` (week), `M` (month), `q` (quarter), and `y` (year).

Duration units (`h`, `m`, `s`, `ms`, `us`, and `ns`) allow to add a factor, for example, `@3h`.  
Leaving the factor out is equivalent to setting it to `1`. Note the following constraints when adding such factor:

* `h` supports all divisors of `24`: `1h`, `2h`, `3h`, `4h`, `6h`, `8h`, `12h`, `24h`. `@24h` is similar to `@1d` but might differ in the case of daylight-saving times.
* `m` and `s` support all divisors of `60`: `1m`, `2m`, `3m`, `4m`, `5m`, `6m`, `10m`, `12m`, `15m`, `20m`, `30m`, `60m`, and equivalently for `s`.
* `ms`, `us`, and `ns` support all divisors of `1000`.

By default, the week unit `w` uses the first day of the week as defined by your configured locale.
To explicitly specify the first day of the week, you can use the following time units:

* `w0` (Sunday)
* `w1` (Monday)
* `w2` (Tuesday)
* `w3` (Wednesday)
* `w4` (Thursday)
* `w5` (Friday)
* `w6` (Saturday)
* `w7` (Sunday)

For example, `@w1` means midnight of Monday of the current week.

##### Examples

For the following examples, the current time is Wednesday, 04 September 2024, 14:47:05+0200.

Time modifier

Description

Resulting time

`-2h@h`

2 hours ago, aligned to the hour

Wednesday, 04 September 2024, 12:00:00+0200

`-1d@d`

Yesterday, aligned to the day

Tuesday, 03 September 2024, 00:00:00+0200

`-7d@d`

7 days ago, aligned to the day

Wednesday, 28 August 2024, 00:00:00+0200

`@w0`

Start of this week, from Sunday

Sunday, 01 September 2024, 00:00:00+0200

`@w1`

Start of this week, from Monday

Monday, 02 September 2024, 00:00:00+0200

`@M`

Start of this month

Sunday, 01 September 2024, 00:00:00+0200

`-1M@M`

Start of last month

Thursday, 01 August 2024, 00:00:00+0200

`@q`

Start of this quarter

Monday, 01 July 2024, 00:00:00+0200

`@y`

Start of this year

Monday, 01 January 2024, 00:00:00+0100

## Search

You can use the `~` operator in expressions to match the value of an expression against a given search string. The performed comparison is case-insensitive and supports pattern matching using wildcards. The `~` operator returns a `boolean` value: `true` in case of a match, and `false` otherwise.

#### Syntax

`expression ~ "string literal"`

#### Left side

You can use any expression on the left side of the `~`operator. For details on how different data types work with this operator, see the [Returns](#search-returns) section.

#### Right side

The string literal to search for. It can be one of the following:

* A search string without a wildcard (`*`). For example:

  ```
  content ~ "error"
  ```
* A search string with a wildcard (`*`) as first and/or last character. For example:

  ```
  user ~ "*dynatrace.com"
  ```

#### Returns

##### Search strings without wildcards

The `~` operator searches the value as a string token inside a string. Its behavior depends on the data type of the expression on the left side:

* If the expression is of type `string`, the operator searches the value as a token inside the string. It's case-insensitive. For example, `"Hello World"` matches `~"world"`, but `"HelloWorld"` doesn't.
* If the expression is of type `long`, `double`, `smartscape ID`, `IP address`, or `UID`, the operator only matches if the string representation of its value is equal to the search string. For example, the IP address `192.0.0.1` matches `~"192.0.0.1"`, but not `~"192"`.
* If the expression is of type `array`, each element is checked. The operator matches if at least one of the elements in the array does.
* If the expression is of type `record`, the operator matches if any field name or value matches.
* If the expression is of type `boolean`, `timestamp`, `duration`, or `binary`, the result is always false.

Expression type

Expression value

Operation

Result

Note

String

`"Hello WORLD!"`

`~"world"`

`true`

String

`"helloWorld"`

`~"World"`

`false`

`helloWorld` is one token since there are no separators.

String

`"192.168.0.7"`

`~"192"`

`true`

As itâs a string, the field has four tokens.

IP

`192.168.0.7`

`~"192"`

`false`

Only strings are tokenized.

IP

`192.168.0.7`

`~"192.168.0.7"`

`true`

The value is auto-converted, so there's an exact match.

Long

`12`

`~"12"`

`true`

The value is auto-converted, so there's an exact match.

UID

`uuid(1,2)`

`~"00000000-0000-0001-0000-000000000002"`

`true`

The value is not tokenized, but can be auto-converted.

Smartscape ID

`smartscapeId("HOST", 1)`

`~"HOST-0000000000000001"`

`true`

The value is auto-converted.

Smartscape ID

`smartscapeId("HOST", 1)`

`~"host-0000000000000001"`

`false`

For a Smartscape ID, the check is case-sensitive.

Smartscape ID

`smartscapeId("HOST", 1)`

`~"HOST"`

`false`

The value isn't tokenized.

Record

`record(firstName="John",lastName="Doe")`

`~"john"`

`true`

Search also works in nested fields.

Record

`record(firstName="John",lastName="Doe")`

`~"lastName"`

`true`

Search also works in the names of nested fields.

Record

`record(firstName="John",lastName="Doe")`

`~"name"`

`false`

`firstName` and `lastName` are one token since they don't contain separators.

Record

`record(first name="John",last name="Doe")`

`~"name"`

`true`

Search also works in the names of nested fields.

Array

`array(1,2,3,5,8,13)`

`~"3"`

`true`

One element of the array is 3, which can be auto-converted to match `~"3"`.

Boolean

`true`

`~"true"`

`false`

Booleans aren't supported.

Duration

`1h`

`~"1h"`

`false`

Durations aren't supported.

##### Search strings with wildcards

The operator searches the pattern in the tokens of a string. Its behavior depends on the data type of the expression on the left side:

* If the expression is of type `string`, the result is true if at least one of the tokens matches the pattern.
* If the expression is of type `array`, the result is true if one of the elements of the array matches the pattern.
* If the expression is of type `record`, the result is true if the name or value of a nested field matches the pattern.
* If the expression is of any other type (`long`, `double`, `smartscape ID`, `IP address`, `UID`, `boolean`, `timestamp`, `duration`, or `binary`) patterns aren't supported and the result is always `false`.

Expression type

Expression value

Operation

Result

Note

String

`"AuthenticationError"`

`~"*error"`

`true`

String

`"There was an AuthenticationError"`

`~"authentication*"`

`true`

String

`"There was an NoAuthenticationError"`

`~"authentication*"`

`false`

String

`"helloWorld"`

`~"*ow*"`

`true`

String

`"hello world"`

`~"*ow*"`

`false`

String

`"192.168.0.7"`

`~"192.168.*"`

`true`

It matches as it's a string and not an IP address.

Record

`record(firstName="John",lastName="Doe")`

`~"*name"`

`true`

The string matches the name of the nested field in the record.

Record

`record(firstName="John",lastName="Doe")`

`~"*do*"`

`true`

The string matches the record.

Array

`array("hello", "world", "myCustomName")`

`~"my*"`

`true`

The string matches within the array.

IP

`192.168.0.7`

`~"192*"`

`false`

Only strings allow patterns.

Long

`192`

`~"1*"`

`false`

Only strings allow patterns.

Smartscape ID

`smartscapeId("HOST", 1)`

`~"HOST*"`

`false`

Only strings allow patterns.

Boolean

`true`

`~"t*"`

`false`

Only strings allow patterns.

Duration

`1h`

`~"*h"`

`false`

Only strings allow patterns.

## Related topics

* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Use DQL queries](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.")
* [DQL compared to SQL and more](/docs/platform/grail/dynatrace-query-language/dql-comparison "See how DQL compares to other query languages.")
* [DQL language reference](/docs/platform/grail/dynatrace-query-language/dql-reference "Dynatrace Query Language syntax reference.")
* [DQL commands](/docs/platform/grail/dynatrace-query-language/commands "A list of DQL commands.")
* [DQL functions](/docs/platform/grail/dynatrace-query-language/functions "A list of DQL functions.")
* [DQL data types](/docs/platform/grail/dynatrace-query-language/data-types "A list of DQL data types.")
* [DQL best practices](/docs/platform/grail/dynatrace-query-language/dql-best-practices "Best practices for using Dynatrace Query Language.")