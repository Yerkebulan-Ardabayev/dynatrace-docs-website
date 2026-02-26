---
title: String functions
source: https://www.dynatrace.com/docs/platform/grail/dynatrace-query-language/functions/string-functions
scraped: 2026-02-26T21:16:09.755877
---

# String functions

# String functions

* Latest Dynatrace
* Reference
* Updated on Jan 29, 2026

String functions allow you to create expressions that manipulate text strings in a variety of ways.

Case sensitivity

All string matching functions are case-sensitive per default. If otherwise required, the `caseSensitive` parameter provides the ability to change the behavior.

```
...



| fieldsAdd str_found = contains(content, "FlushCommand", caseSensitive:false)
```

## concat

Concatenates the expressions into a single string.

#### Syntax

`concat(expression, â¦ [, delimiter: ])`

#### Parameters

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(a = "DQL", b = "is", c = "awesome!")



| fieldsAdd concat(a, b, c, delimiter: " ")
```

Run in Playground

Query result:

## contains

Searches the string expression for a substring. Returns `true` if the substring was found, `false` otherwise.

#### Syntax

`contains(expression, substring [, caseSensitive])`

#### Parameters

#### Returns

The data type of the returned value is `boolean`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language")



| fieldsAdd contains(content, "DQL"),



contains(content, "dql", caseSensitive: false),



contains(content, "Query")
```

Run in Playground

Query result:

## decodeUrl

Returns a URL-decoded string.

#### Syntax

`decodeUrl(expression)`

#### Parameters

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(content = "https%3A%2F%2Fwww.dynatrace.com%2Fplatform%2Fgrail"),



record(content = "https://www.dynatrace.com/platform/grail")



| fieldsAdd decodeUrl(content)
```

Run in Playground

Query result:

## encodeUrl

Encodes a URL string by replacing characters that aren't numbers or letters with percentage symbols and hexadecimal numbers.

#### Syntax

`encodeUrl(expression)`

#### Parameters

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(content = "https://www.dynatrace.com/platform/grail")



| fieldsAdd encodeUrl(content)
```

Run in Playground

Query result:

## endsWith

Checks if a string expression ends with a suffix. Returns `true` if does, `false` otherwise.

#### Syntax

`endsWith(expression, suffix [, caseSensitive])`

#### Parameters

#### Returns

The data type of the returned value is `boolean`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language")



| fieldsAdd endsWith(content, "awesome!"),



endsWith(content, "AWESOME!", caseSensitive: false),



endsWith(content, "Language")
```

Run in Playground

Query result:

## escape

Returns an escaped string.

Escaping rules

1. Single and double quotes are escaped. Backticks are not escaped.

2. Backslashes are escaped.

3. ASCII characters backspace, form feed, new line, carriage return, horizontal tabs are escaped.

4. ASCII characters within the range 0x20 - 0x7e (printable ASCII characters), that are not covered by any of the above rules, stay as they are.

5. All other ASCII characters are represented as `\xhh`. This applies to the following characters

   * characters within the range 0x00 - 0x07
   * character 0x0b (vertical tab)
   * characters within the range 0x0e - 0x1f
   * character 0x7f

6. All characters in extended ASCII space (0x80-0xff) and Unicode characters outside of the ASCII space are represented as `\uhhhh`.

#### Syntax

`escape(expression)`

#### Parameters

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(content = """"foo@bar.com""")



| fieldsAdd escape(content)
```

Run in Playground

Query result:

| content | escape(content) |
| --- | --- |
| `"foo@bar.com` | `\"foo@bar.com` |

## getCharacter

Returns the character at a given position from a string expression. Negative values for the position parameter are counted from the end of the string. If a position refers to a position outside the string, the function returns NULL.

#### Syntax

`getCharacter(expression, position)`

#### Parameters

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language")



| fieldsAdd getCharacter(content, 1),



getCharacter(content, 17),



getCharacter(content, -1)
```

Run in Playground

Query result:

## indexOf

Returns the index of the first occurrence of a substring in a string expression.
Starts to search forward from a given index. Negative values for the `from` parameter are counted from the end of the string.
The default value for `from` is `0` (the search from the start of the string).
The search is case-sensitive.
If the defined substring is not found, the function returns `-1`.

#### Syntax

`indexOf(expression, substring [, from])`

#### Parameters

#### Returns

The data type of the returned value is `long`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language")



| fieldsAdd indexOf(content, "a"),



indexOf(content, "a", from: 10),



indexOf(content, "Query")
```

Run in Playground

Query result:

## jsonField

Parses a JSON string and extracts one value selected by its name.

#### Syntax

`jsonField(expression, fieldName [, seek])`

#### Parameters

#### Returns

The data type of the returned value is `long`, `double`, `boolean`, `string`, `array` or `record`.

#### Examples

##### Example 1

```
data record(content = """{



"name":"John",



"children":["Mallory", "Mary"],



"address":{"city":"Boston", "zip":"02210"}



}""")



| fieldsAdd jsonField(content, "name")
```

Run in Playground

Query result:

##### Example 2

```
data record(content = """JSON: {"name": "John"} ...""")



| fieldsAdd jsonField(content, "name", seek:false)



| fieldsAdd jsonField(content, "name", seek:true)
```

Run in Playground

Query result:

## jsonPath

Parses a JSON string and extracts one value selected by a JSONPath expression.

#### Syntax

`jsonPath(expression, jsonPath [, seek])`

#### Parameters

#### Returns

The data type of the returned value is `long`, `double`, `boolean`, `string`, `array` or `record`.

#### Examples

##### Example 1

```
data record(content = """{



"name":"John",



"children":["Mallory", "Mary"],



"address":{"city":"Boston", "zip":"02210"}



}""")



| fieldsAdd jsonPath(content, "$.children[0]")



| fieldsAdd jsonPath(content, "$.address.city")



| fieldsAdd jsonPath(content, "$['address']['zip']")
```

Run in Playground

Query result:

##### Example 2

```
data record(content = """JSON: {"name": "John"} ...""")



| fieldsAdd jsonPath(content, "$.name", seek:false)



| fieldsAdd jsonPath(content, "$.name", seek:true)
```

Run in Playground

Query result:

## lastIndexOf

Returns the index of the last occurrence of a substring in a string expression. Starts to search backward from a given index. Negative values for the from parameter are counted from the end of the string. The default value for from is -1 (search from the end of the string). The search is case-sensitive. If the substring is not found, the function returns `-1`.

#### Syntax

`lastIndexOf(expression, substring [, from])`

#### Parameters

#### Returns

The data type of the returned value is `long`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language")



| fieldsAdd lastIndexOf(content, "a"),



lastIndexOf(content, "a", from: 10),



lastIndexOf(content, "Query")
```

Run in Playground

Query result:

## levenshteinDistance

Computes the Levenshtein distance between two input strings.

#### Syntax

`levenshteinDistance(expression, expression)`

#### Parameters

#### Returns

The data type of the returned value is `long`.

#### Examples

##### Example 1

```
data record(a = "DQL is awesome!", b = "Grail is awesome!"),



record(a = "Dynatrace Query Language", b = "DQL"),



record(a = "Dynatrace Query Language", b = "dynatrace query language")



| fieldsAdd levenshteinDistance(a, b)
```

Run in Playground

Query result:

## like

Tests if a string expression matches a pattern. If the pattern does not contain percent signs, `like()` acts as the `==` operator (equality check). A percent character in the pattern `(%)` matches any sequence of zero or more characters. An underscore in the pattern `(\_)` matches a single character.

#### Syntax

`like(expression, pattern)`

#### Parameters

#### Returns

The data type of the returned value is `boolean`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language")



| fieldsAdd like(content, "%DQL%"),



like(content, "D%L%"),



like(content, "D_L%")
```

Run in Playground

Query result:

## lower

Converts a string to lowercase.

#### Syntax

`lower(expression)`

#### Parameters

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language")



| fieldsAdd lower(content)
```

Run in Playground

Query result:

## matchesPattern



Tests if a string expression matches the DPL pattern and returns `true` if it does, otherwise, returns `false`.

#### Syntax

`matchesPattern(expression, pattern)`

#### Parameters

#### Returns

The data type of the returned value is `boolean`.

#### Examples

##### Example 1

```
data record(content = "2023-11-01 12:52:12 : 766"),



record(content = "2023-11-01 12:53:00:123"),



record(content = "2023-11-01 12:55:59 : 192.168.0.1")



| fieldsAdd matchesPattern(content, "TIME ' : ' LONG"),



matchesPattern(content, "TIME ' : ' IP")
```

Run in Playground

Query result:

| content | matchesPattern(content, "TIME ' : ' LONG") | matchesPattern(content, "TIME ' : ' IP") |
| --- | --- | --- |
| `2023-11-01 12:52:12 : 766` | `true` | `false` |
| `2023-11-01 12:53:00:123` | `false` | `false` |
| `2023-11-01 12:55:59 : 192.168.0.1` | `false` | `true` |

## matchesPhrase

Matches a phrase against the input string expression using token matchers.

#### Syntax

`matchesPhrase(expression, phrase [, caseSensitive])`

#### Parameters

#### Returns

The data type of the returned value is `boolean`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language"),



record(content = array("DQL", "is", "awesome", "!", "Dynatrace Query Language"))



| fieldsAdd matchesPhrase(content, "DQL"),



matchesPhrase(content, "Dyna"),



matchesPhrase(content, "query"),



matchesPhrase(content, "query", caseSensitive: true)
```

Run in Playground

Query result:

## matchesValue

Searches records for a specific value in a given attribute. Returns `true` or `false`.

#### Syntax

`matchesValue(expression, value, â¦ [, caseSensitive])`

#### Parameters

#### Returns

The data type of the returned value is `boolean`.

#### Examples

##### Example 1

Values are matched case-insensitive by default:

```
data record(content = "User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1")



| fieldsAdd matchesValue(content, "User*"),



matchesValue(content, "user*"),



matchesValue(content, "user*", caseSensitive: true)
```

Run in Playground

Query result:

##### Example 2

Values are matched from the beginning. To match parts of the value, use `*` as wildcard symbol:

```
data record(content = "User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1")



| fieldsAdd matchesValue(content, "192.168.0.1"),



matchesValue(content, "*192.168.0.1"),



matchesValue(content, "*failed to log*")
```

Run in Playground

Query result:

##### Example 3

Only ASCII characters are matched case-insensitive:

```
data record(content = "Ãsterreich")



| fieldsAdd matchesValue(content, "Ã¶sterreich"),



matchesValue(content, "Ãsterreich")
```

Run in Playground

Query result:

##### Example 4

The function handles values of arrays in "any-match" manner.

```
data record(technologies = array("Java11", "java17"))



| fieldsAdd matchesValue(technologies, "Java11"),



matchesValue(technologies, "java"),



matchesValue(technologies, "java*")
```

Run in Playground

Query result:

#### Multi-pattern comparison

The `matchesValue()` function supports matching against multiple patterns. You can use it by either providing an array or a list of patterns with the `value` parameter. Only strings are supported as patterns. Other datatypes don't produce a match and are ignored. The `matchesValue()` function returns true if any of the patterns matches. In case none of the patterns produce a match, `false` is returned.

#### Example

```
data record(content = array("DQL", "is", "awesome", "!"))



| fieldsAdd matchesValue(content, array("Grail", "dql")),



matchesValue(content, {"Grail", "dql"}),



matchesValue(content, {"Grail", "dq*"}),



matchesValue(content, {"Grail", "dq*"}, caseSensitive: true)
```

Run in Playground

Query result:

## parse

Extracts a single value from a string as specified in the pattern or a record if there are multiple named matchers.

#### Syntax

`parse(expression, pattern)`

#### Parameters

#### Returns

The `parse` function returns a single value, which can be either of primitive type or a record. The result is of primitive type in case of a single named matcher in the DPL pattern. If there are multiple named matchers in the pattern, then the result is a record containing fields corresponding to the names of the matchers.
Fields created from the output of the `parse` function by default get the name of the named matcher in the DPL pattern. In case of multiple named matchers in the pattern, the default field name is `parsed_record`. You can also define alternative field names using an alias expression.

#### Examples

##### Example 1

```
data record(src = "1 2"),



record(src = "45 46 47 48")



| fieldsAdd parse(src, "LONG:result"),



value = parse(src, "LONG:result"),



parse(src, "LONG:field1 ' ' LONG:field2")
```

Run in Playground

Query result:

| src | result | value | parsed\_record |
| --- | --- | --- | --- |
| `1 2` | `1` | `1` | **field1**: `1` **field2**: `2` |
| `45 46 47 48` | `45` | `45` | **field1**: `45` **field2**: `46` |

## parseAll

Extracts several values from a string as specified in the pattern.
Unlike the [`parse`](/docs/platform/grail/dynatrace-query-language/functions/string-functions#parse "A list of DQL string functions.") function, `parseAll` returns an array all the time. The array can be empty if no patterns matched. A single element can be primitive type or a record.

#### Syntax

`parseAll(expression, pattern)`

#### Parameters

#### Returns

The data type of the returned value is `array`.

#### Examples

##### Example 1

```
data record(src = "1 2"),



record(src = "45 46 47 48")



| fieldsAdd parseAll(src, "LONG:result"),



value = parseAll(src, "LONG:result"),



parseAll(src, "LONG:field1 ' ' LONG:field2")
```

Run in Playground

Query result:

| src | result | value | parsed\_records |
| --- | --- | --- | --- |
| `1 2` | `[1, 2]` | `[1, 2]` | [**field1:** `1` **field2** `2`] |
| `45 46 47 48` | `[45, 46, 47, 48]` | `[45, 46, 47, 48]` | [**field1:** `45` **field2** `46`, **field1:** `47` **field2** `48`] |

## punctuation

Extracts punctuation characters out of an input string.

#### Syntax

`punctuation(expression, [, count] [, withSpace])`

#### Parameters

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

In this example, we extract the punctuation characters from each input string.

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language"),



record(content = "${placeholder}")



| fieldsAdd punctuation(content),



punctuation(content, count: 2),



punctuation(content, count: 2, withSpace: true)
```

Run in Playground

Query result:

## replacePattern

Replaces each substring of a string that matches the DPL pattern with the given string. The pattern must be defined as a constant string expression. For additional details about pattern syntax, see the [DPL documentation](/docs/platform/grail/dynatrace-pattern-language "Use Dynatrace Pattern Language to describe patterns using matchers.").

#### Syntax

`replacePattern(expression, pattern, replacement)`

#### Parameters

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(content = "DQL 2019-08-01 09:30:00"),



record(content = "Dynatrace Query L4nguage")



| fieldsAdd replacePattern(content, "TIME", "is awesome!"),



replacePattern(content, "LONG", "a")
```

Run in Playground

Query result:

| content | replacePattern(content, "TIME", "is awsome!") | replacePattern(content, "LONG", "a") |
| --- | --- | --- |
| `DQL 2019-08-01 09:30:00` | `DQL is awesome!` | `DQL aaa a:a:a` |
| `Dynatrace Query L4nguage` | `Dynatrace Query L4nguage` | `Dynatrace Query Language` |

## replaceString

Replaces each substring of a string with a given string. This function replaces only exactly matched substrings from the original string to the replacement. Matching is case-sensitive and doesn't use any wildcards. All found patterns will be replaced if they do not intersect. For instance, replacing `abcabca` in a string with `abca` pattern produces only one replacement. Only the first occurrence at the beginning of the string will be replaced.

#### Syntax

`replaceString(expression, substring, replacement)`

#### Parameters

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language"),



record(content = "abcabca")



| fieldsAdd replaceString(content, "awesome", "simple"),



replaceString(content, "abca", "xyz")
```

Run in Playground

Query result:

## splitByPattern

Splits a string into an array at each occurrence of the DPL pattern.

#### Syntax

`splitByPattern(expression, pattern)`

#### Parameters

#### Returns

The data type of the returned value is `array`.

#### Examples

##### Example 1

```
data record(content = "one $1 two $4 three"),



record(content = "foo $1000 bar"),



record(content = "no separator"),



record(content = "")



| fieldsAdd splitByPattern(content, " ' $' LONG ' ' ")
```

Run in Playground

Query result:

| content | splitByPattern(content, " ' $' LONG ' ' ") |
| --- | --- |
| `one $1 two $4 three` | `[one, two, three]` |
| `foo $1000 bar` | `[foo, bar]` |
| `no separator` | `[no separator]` |
| *empty string* | `[]` |

## splitString



Splits a string according to the parameters set.  
Retrieves an array of substrings of the specified expression that are adjacent to occurrences of the given pattern.  
Parameters are interpreted literally. For example, splitting `www.dynatrace.org` by `.` results in `www` and `dynatrace` and `org`.  
Using an empty string as a pattern splits the string into one-byte substrings. For example, a split of four characters becomes an array of four strings having one byte each (splitting the `"1234"` expression results in `array("1", "2", "3", "4")`).

The non-ASCII characters are represented by multiple bytes. Splitting a string containing such characters by `""` breaks these bytes apart into separate invalid strings.

If the pattern is not found in the expression, it returns an array that contains only the input expression.

If the expression starts with one or more occurrences of the pattern, an empty string will be added for each occurrence. For example, `splitString("abc", "a")` results in `"", "bc"`. Analogically, empty strings are added if the pattern is found at the end of the expression.

An empty string is also added for adjacent occurrences of the pattern that do not border the start or end of the string. For example, `splitString("abbc", "b")` results in `"a", "", "c"`.

If the pattern is empty, it splits the expression into one-byte substrings. For example, `splitString("abc", "")` results in `"a", "b", "c"`.

#### Syntax

`splitString(expression, pattern)`

#### Parameters

#### Returns

The data type of the returned value is `array`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language")



| fieldsAdd splitString(content, " "),



splitString(content, "is"),



splitString(content, ""),



splitString(content, "XYZ")
```

Run in Playground

Query result:

## startsWith

Checks if a string expression starts with a prefix. Returns `true` if does, `false` otherwise.

#### Syntax

`startsWith(expression, prefix [, caseSensitive])`

#### Parameters

#### Returns

The data type of the returned value is `boolean`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language")



| fieldsAdd startsWith(content, "D"),



startsWith(content, "dql", caseSensitive: false)
```

Run in Playground

Query result:

## stringLength

Returns the length of a string expression. Length is defined as the number of UTF-16 code units, which is often the same as the number of characters in the string. In some cases, the number of characters is smaller than the number of UTF-16 code units, for example when Combining Diacritical Marks are used, or if characters outside the Basic Multilingual Plane (BMP), such as Emoji, are present.

If your use case requires consistent length for the same characters, consider ingesting strings after Unicode normalization.

No specific normalization form is guaranteed for Dynatrace-provided strings.

#### Syntax

`stringLength(expression)`

#### Parameters

#### Returns

The data type of the returned value is `long`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language"),



record(content = "ðâð¦º")



| fieldsAdd stringLength(content)
```

Run in Playground

Query result:

## substring

Gets a code unit range using a start index (inclusive) and an end index (exclusive).

Returns an empty string if from `>=` to.

`Indexes >=0` are relative to the start of the string and address consecutive characters from left to right, starting from the index position.

`Indexes <=-1` are relative to the last character of the string and are used to address characters from the right side of an expression, for example, `-2` is the penultimate character.

`Positive indexes` beyond the bounds of the string are assigned to the string length.

`Negative indexes` beyond the bounds of the string are equal to `0`. For example, in the `321` string, the index `-4` is beyond the bounds of the string therefore it equals `0`. However, the index `-2` is located within the bounds of that string and extracts `21` if used as a `from` the index.

The returned substring never starts or ends with an incomplete UTF-16 surrogate pair. Instead of that, it starts or ends with a question mark. This safeguards against the creation of invalid Unicode strings.

#### Syntax

`substring(expression [, from] [, to])`

#### Parameters

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language")



| fieldsAdd substring(content, from: 4),



substring(content, from: -2),



substring(content, from: 4, to: 9),



substring(content, from: -42, to: 42)
```

Run in Playground

Query result:

## trim

Removes leading and trailing whitespaces. Any code point <= ASCII 32 in decimal is considered a whitespace, where ASCII 32 is a blank space.

#### Syntax

`trim(expression)`

#### Parameters

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(content = " DQL is awesome!"),



record(content = " Dynatrace Query Language ")



| fieldsAdd trim(content)
```

Run in Playground

Query result:

## unescape

Returns an unescaped string.

Unescaping rules

1. Single quotes, double quotes and backticks are unescaped.

2. Backslashes are unescaped.

3. ASCII characters bell, backspace, form feed, new line, carriage return, horizontal tab and vertical tab are unescaped.

4. `\xhh` within standard ASCII space (0x00 - 0x7f) is replaced by the related character.

5. `\xhh` within extended ASCII space (0x80 - 0xff) is interpreted as `\u00hh` and replaced by the related Unicode character.

6. `\uhhhh` is replaced by the related Unicode character.

#### Syntax

`unescape(expression)`

#### Parameters

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(content = """"foo\x40bar\u002ecom""")



| fieldsAdd unescape(content)
```

Run in Playground

Query result:

| content | unescape(content) |
| --- | --- |
| `"foo\x40bar\u002ecom` | `"foo@bar.com` |

## unescapeHtml

Unescapes HTML in a string by replacing ASCII characters with HTML syntax.

#### Syntax

`unescapeHtml(expression)`

#### Parameters

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(content = "DQL is &lt;bold&gt;awesome&lt;/bold&gt;!"),



record(content = "&lt;a href=&quot;https://www.dynatrace.com/platform/grail&quot;&gt;Dynatrace Query Language&lt;/a&gt;")



| fieldsAdd unescapeHtml(content)
```

Run in Playground

Query result:

## upper

Converts a string to uppercase.

#### Syntax

`upper(expression)`

#### Parameters

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language")



| fieldsAdd upper(content)
```

Run in Playground

Query result:

## Related topics

* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Use DQL queries](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.")
* [DQL compared to SQL and more](/docs/platform/grail/dynatrace-query-language/dql-comparison "See how DQL compares to other query languages.")
* [DQL language reference](/docs/platform/grail/dynatrace-query-language/dql-reference "Dynatrace Query Language syntax reference.")
* [DQL commands](/docs/platform/grail/dynatrace-query-language/commands "A list of DQL commands.")
* [DQL operators](/docs/platform/grail/dynatrace-query-language/operators "A list of DQL Operators.")
* [DQL data types](/docs/platform/grail/dynatrace-query-language/data-types "A list of DQL data types.")
* [DQL best practices](/docs/platform/grail/dynatrace-query-language/dql-best-practices "Best practices for using Dynatrace Query Language.")