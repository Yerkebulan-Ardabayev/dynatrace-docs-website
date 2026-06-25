---
title: Log processing commands (Logs Classic)
source: https://docs.dynatrace.com/managed/analyze-explore-automate/log-monitoring/log-processing/log-processing-commands
scraped: 2026-05-12T12:00:16.464533
---

# Log processing commands (Logs Classic)

# Log processing commands (Logs Classic)

* Overview
* 2-min read
* Updated on Jan 18, 2023

Log Monitoring Classic

Log and event processing commands represent DQL statements and clauses. A **Rule definition** makes it possible to define a sequence of commands to achieve the desired goal of the processing rule.

A processing **Rule definition** consists of a left-to-right sequence of processing commands chained together using the pipe character (`|`). Conceptually, this is similar to Unix command pipelining, where the output of the command to the left of the pipe becomes the input of the command to the right of the pipe. The pipeline must always start with a command producing a structured data stream for subsequent commands.

## PARSE

The `PARSE` command parses the selected field with provided pattern expression, enhancing the log record with exported values.

### Examples

* [Parse out attributes from different formats within a single pattern expression.](/managed/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample5 "Example log processing scenarios.")
* [Parse out specific fields from JSON content.](/managed/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample4 "Example log processing scenarios.")

## USING

The USING command specifies the input to a given transformation by listing fields with options that can be passed from the incoming event to the transformation. This command must be the first command used in the processor definition.

Fields declaration format: `USING(<field_expression>, <field_expression>, ...)`  
Field expression format: `[IN|INOUT] name: [type[]?]`

The `USING` command in the processor definition is an equivalent of `USING(IN content:STRING)` statement.

Options:

* `IN`âread-only field, default option.
* `INOUT`âwriteable field.
* `type`âone of the following types: `STRING`, `BOOLEAN`, `INTEGER`, `LONG`, `DOUBLE`, `DURATION`, `TIMESTAMP`, `IPADDR`.
* `[]`âmarks a field as an array, meaning that multiple values of the attribute will be passed.
* `?`âmarks the field as optional, meaning that the transformation will be executed even if there is no such attribute in the event.

Example:

```
USING(content, event.type:STRING?, INOUT attribute:INT[]) | ...
```

In this case, three fields are passed from the incoming event to a transformation:  
`content`âread-only string field  
`event.type`âan optional, read-only string  
`attribute`âa writeable array of integers

## FIELDS\_ADD

The `FIELDS_ADD` command specifies a comma-separated list of literals, functions, names of fields, and expressions to be computed.

Format:

```
FIELDS_ADD( [ alias':' ]



{ *



| alias.*



| '@'position



| function



| expression



| literal



}



[ , ... ]



)
```

Each expression can be renamed using an alias. Aliases defined in a select command can be referenced in the following commands down the pipeline.

### Example

In the following example, we compute the sum of `field1` and `field2` and place the result in a field named `mySum`.

| field1 | field2 |
| --- | --- |
| 300 | 650 |

```
FIELDS_ADD(mySum:(field1 + field2))
```

| field1 | field2 | mySum |
| --- | --- | --- |
| 300 | 650 | 950 |

## FIELDS\_RENAME

The `FIELDS_RENAME` command renames specified fields of a record. It preserves field order and other fields.

Format: `FIELDS_RENAME(newName:field, name2:field2, ...)`

### Example

In the following example, we rename field `ip` to `src_addr` and rename field `f` to `value`.

| t | ip | s | f |
| --- | --- | --- | --- |
| 2020-09-23 15:14:42.947 +0300 | 0.0.0.0 | 0ho0 | 0.0 |

```
FIELDS_RENAME(src_addr:ip, value:f)
```

| t | src\_addr | s | value |
| --- | --- | --- | --- |
| 2020-09-23 15:14:42.947 +0300 | 0.0.0.0 | 0ho0 | 0.0 |

## FIELDS\_REMOVE

The `FIELDS_REMOVE` command removes specified fields from the output stream. The command is useful in scripts eliminating sensitive fields.

Format: `FIELDS_REMOVE(field, field, ...)`

### Example

In the following example, we add fields `t`, `ip`, `s` and `f`. Then we remove fields `s` and `ip`, leaving us with fields `t` and `f`.

```
FIELDS_REMOVE(s, ip)
```

| t | f |
| --- | --- |
| 2020-09-23 15:17:39.497 +0300 | 0.0 |
| 2020-09-23 15:17:39.498 +0300 | 1.0 |
| 2020-09-23 15:17:39.499 +0300 | 2.0 |

## FILTER\_OUT

The `FILTER_OUT` command discards the whole record using an expression returning a boolean value (boolean\_expression). This is a negative filter command. It may consist of multiple boolean expressions combined using AND, OR, and NOT operators. If the condition is fulfilled, the whole record is discarded and will not be passed to the next stage. For example, you can drop all records with the log level attribute `DEBUG` or `debug`.

Format: `FILTER_OUT(loglevel IN ['DEBUG', 'debug'])`

### Examples

* In the following example, we discard records where `_raw_text` (source raw record text) contains the string `vpns` or `_raw_text` is `NULL`

  ```
  FILTER_OUT(contains(_raw_text, '/vpns/'))
  ```
* In the following example, we discard records where the string field type is `logout` or type is `NULL`

  ```
  FILTER_OUT(type = 'logout')
  ```
* In the following example, we discard records where the timestamp field `last_modified` is greater than 7 days ago or `last_modified` is `NULL`

  ```
  FILTER_OUT(last_modified >= now()[-7 day])
  ```

## Related topics

* [Log processing examples (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples "Example log processing scenarios.")