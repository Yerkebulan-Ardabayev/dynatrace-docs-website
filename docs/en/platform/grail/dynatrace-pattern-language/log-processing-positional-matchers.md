---
title: DPL Positional Matchers
source: https://www.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/log-processing-positional-matchers
scraped: 2026-02-18T05:47:11.744787
---

# DPL Positional Matchers

# DPL Positional Matchers

* Latest Dynatrace
* Reference
* Published Nov 08, 2022

## Beginning of string

**BOS, BOF**

Matches beginning of string

output type

quantifier

configuration

none

none

none

#### Example

Extracting the first line in the string:

```
"name";"age"



Homer Simpson;40



Charles Montgomery Burns;104
```

```
BOF LD:header EOL;
```

Results in the first line parsed into the `header` field. Parsing following lines fails, as they do not begin at the start of file marker.

| header |
| --- |
| `''name'';''age''` |
|  |

## Middle of string

**MOS, MOF**

Matches any bytes in the middle of string

output type

quantifier

configuration

none

none

none

#### Example

Extracting records after the first row in the string

```
"name";"age"



Homer Simpson;40



Charles Montgomery Burns;104
```

```
MOF LD:name ';' INT:age EOL
```

Results in lines 2 and 3 parsed to fields `name` and `age`. Line 1 fails to parse as it begins with the beginning of the string marker.

| name | age |
| --- | --- |
|  | `-1` |
| `Homer Simpson` | `40` |
| `Charles Montgomery Burns` | `40` |

## End of string

**EOS, EOF**

Matches end of string

output type

quantifier

configuration

none

none

none

#### Example

Extracting the last line of the string:

```
"name";"age"



Homer Simpson;40



Charles Montgomery Burns;104



total:2 persons, average age: 72 years
```

The following pattern matches only when the last line is followed by the end of string marker:

```
LD:footer EOS
```

Results in the last line being extracted to the `footer` field. First three lines fail to parse as they are not the last in the string.

| footer |
| --- |
|  |
| `total:2 persons, average age: 72 years` |