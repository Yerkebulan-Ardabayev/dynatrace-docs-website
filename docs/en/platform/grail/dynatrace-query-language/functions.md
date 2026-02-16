---
title: DQL functions
source: https://www.dynatrace.com/docs/platform/grail/dynatrace-query-language/functions
scraped: 2026-02-16T21:15:01.295469
---

# DQL functions

# DQL functions

* Latest Dynatrace
* Reference
* Updated on Feb 02, 2026

DQL functions grouped by category. For in-depth information on a specific function, select its name.

## [Aggregation functions](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions "A list of DQL aggregation functions.")

Aggregation functions compute results from a list of records.

Name

Description

[avg](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#avg "A list of DQL aggregation functions.")

Calculates the average value of a field for a list of records.

[collectArray](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#collectArray "A list of DQL aggregation functions.")

Collects the values of the provided field into an array.

[collectDistinct](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#collectDistinct "A list of DQL aggregation functions.")

Collects distinct values of the provided field into an array.

[correlation](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#correlation "A list of DQL aggregation functions.")

Calculates the Pearson correlation of two numeric fields for a list of records.

[count](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#count "A list of DQL aggregation functions.")

Counts the total number of records.

[countDistinct](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#countDistinct "A list of DQL aggregation functions.")

Calculates the cardinality of unique values of a field for a list of records.

[countDistinctApprox](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#countDistinctApprox "A list of DQL aggregation functions.")

Calculates the cardinality of unique values of a field for a list of records based on a stochastic estimation.

[countDistinctExact](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#countDistinctExact "A list of DQL aggregation functions.")

Calculates the cardinality of unique values for the provided expression up to a maximum of 1M distinct values.

[countIf](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#countIf "A list of DQL aggregation functions.")

Counts the number of records that match the condition.

[max](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#max "A list of DQL aggregation functions.")

Calculates the maximum value of a field for a list of records.

[median](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#median "A list of DQL aggregation functions.")

Calculates the median of an expression.

[min](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#min "A list of DQL aggregation functions.")

Calculates the minimum value of a field for a list of records.

[percentile](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#percentile "A list of DQL aggregation functions.")

Calculates a given percentile of an expression.

[stddev](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#stddev "A list of DQL aggregation functions.")

Calculates the standard deviation of a field for a list of records.

[sum](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#sum "A list of DQL aggregation functions.")

Calculates the sum of a field for a list of records.

[takeAny](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#takeAny "A list of DQL aggregation functions.")

Returns any non-null value of a field for a list of records.

[takeFirst](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#takeFirst "A list of DQL aggregation functions.")

Returns the first value of a field for a list of records.

[takeLast](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#takeLast "A list of DQL aggregation functions.")

Returns the last value of a field for a list of records.

[takeMax](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#takeMax "A list of DQL aggregation functions.")

Returns the maximum value of a field for a list of records.

[takeMin](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#takeMin "A list of DQL aggregation functions.")

Returns the minimum value of a field for a list of records.

[variance](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#variance "A list of DQL aggregation functions.")

Calculates the variance of a field for a list of records.

## [String functions](/docs/platform/grail/dynatrace-query-language/functions/string-functions "A list of DQL string functions.")

String functions allow you to create expressions that manipulate text strings in a variety of ways.

Name

Description

[concat](/docs/platform/grail/dynatrace-query-language/functions/string-functions#concat "A list of DQL string functions.")

Concatenates the expressions into a single string.

[contains](/docs/platform/grail/dynatrace-query-language/functions/string-functions#contains "A list of DQL string functions.")

Searches the string expression for a substring.

[decodeUrl](/docs/platform/grail/dynatrace-query-language/functions/string-functions#decodeUrl "A list of DQL string functions.")

Returns a URL-decoded string.

[encodeUrl](/docs/platform/grail/dynatrace-query-language/functions/string-functions#encodeUrl "A list of DQL string functions.")

Encodes a URL string.

[endsWith](/docs/platform/grail/dynatrace-query-language/functions/string-functions#endsWith "A list of DQL string functions.")

Checks if a string expression ends with a suffix.

[escape](/docs/platform/grail/dynatrace-query-language/functions/string-functions#escape "A list of DQL string functions.")

Returns an escaped string.

[getCharacter](/docs/platform/grail/dynatrace-query-language/functions/string-functions#getCharacter "A list of DQL string functions.")

Returns the character at a given position from a string expression.

[indexOf](/docs/platform/grail/dynatrace-query-language/functions/string-functions#indexOf "A list of DQL string functions.")

Returns the index of the first occurrence of a substring in a string expression.

[jsonField](/docs/platform/grail/dynatrace-query-language/functions/string-functions#jsonField "A list of DQL string functions.")

Parses a JSON string and extracts one value selected by its name.

[jsonPath](/docs/platform/grail/dynatrace-query-language/functions/string-functions#jsonPath "A list of DQL string functions.")

Parses a JSON string and extracts one value selected by a JSONPath expression.

[lastIndexOf](/docs/platform/grail/dynatrace-query-language/functions/string-functions#lastIndexOf "A list of DQL string functions.")

Returns the index of the last occurrence of a substring in a string expression.

[levenshteinDistance](/docs/platform/grail/dynatrace-query-language/functions/string-functions#levenshteinDistance "A list of DQL string functions.")

Computes the Levenshtein distance between two input strings.

[like](/docs/platform/grail/dynatrace-query-language/functions/string-functions#like "A list of DQL string functions.")

Tests if a string expression matches a pattern.

[lower](/docs/platform/grail/dynatrace-query-language/functions/string-functions#lower "A list of DQL string functions.")

Converts a string to lowercase.

[matchesPattern](/docs/platform/grail/dynatrace-query-language/functions/string-functions#matchesPattern "A list of DQL string functions.")

Tests if a string expression matches the DPL pattern.

[matchesPhrase](/docs/platform/grail/dynatrace-query-language/functions/string-functions#matchesPhrase "A list of DQL string functions.")

Matches a phrase against the input string expression using token matchers.

[matchesValue](/docs/platform/grail/dynatrace-query-language/functions/string-functions#matchesValue "A list of DQL string functions.")

Searches records for a specific value in a given attribute. Returns true or false.

[parse](/docs/platform/grail/dynatrace-query-language/functions/string-functions#parse "A list of DQL string functions.")

Extracts a single value from a string as specified in the pattern or a record if there are multiple named matchers.

[parseAll](/docs/platform/grail/dynatrace-query-language/functions/string-functions#parseAll "A list of DQL string functions.")

Extracts several values from a string as specified in the pattern.

[punctuation](/docs/platform/grail/dynatrace-query-language/functions/string-functions#punctuation "A list of DQL string functions.")

Extracts punctuation characters out of an input string.

[replacePattern](/docs/platform/grail/dynatrace-query-language/functions/string-functions#replacePattern "A list of DQL string functions.")

Replaces each substring of a string that matches the DPL pattern with the given string.

[replaceString](/docs/platform/grail/dynatrace-query-language/functions/string-functions#replaceString "A list of DQL string functions.")

Replaces each substring of a string with a given string

[splitByPattern](/docs/platform/grail/dynatrace-query-language/functions/string-functions#splitByPattern "A list of DQL string functions.")

Splits a string into an array at each occurrence of the DPL pattern.

[splitString](/docs/platform/grail/dynatrace-query-language/functions/string-functions#splitString "A list of DQL string functions.")

Splits a string according to the parameters set.

[startsWith](/docs/platform/grail/dynatrace-query-language/functions/string-functions#startsWith "A list of DQL string functions.")

Checks if a string expression starts with a prefix. Returns true if does, false otherwise.

[stringLength](/docs/platform/grail/dynatrace-query-language/functions/string-functions#stringLength "A list of DQL string functions.")

Returns the length of a string expression.

[substring](/docs/platform/grail/dynatrace-query-language/functions/string-functions#substring "A list of DQL string functions.")

Gets a code unit range using a start index (inclusive) and an end index (exclusive).

[trim](/docs/platform/grail/dynatrace-query-language/functions/string-functions#trim "A list of DQL string functions.")

Removes leading and trailing whitespaces.

[unescape](/docs/platform/grail/dynatrace-query-language/functions/string-functions#unescape "A list of DQL string functions.")

Returns an unescaped string.

[unescapeHtml](/docs/platform/grail/dynatrace-query-language/functions/string-functions#unescapeHtml "A list of DQL string functions.")

Unescapes HTML in a string by replacing ASCII characters with HTML syntax.

[upper](/docs/platform/grail/dynatrace-query-language/functions/string-functions#upper "A list of DQL string functions.")

Converts a string to uppercase.

## [Conversion and casting functions](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions "A list of DQL conversion and casting functions.")

Conversion and casting functions convert the expression or value from one data type to another type.

Name

Description

[asArray](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#asArray "A list of DQL conversion and casting functions.")

Returns array value if the value is array, otherwise, returns null.

[asBinary](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#asBinary "A list of DQL conversion and casting functions.")

Returns binary value (byte array) if the value is binary, otherwise, returns null.

[asBoolean](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#asBoolean "A list of DQL conversion and casting functions.")

Returns boolean value if the value is boolean, otherwise, returns null.

[asDouble](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#asDouble "A list of DQL conversion and casting functions.")

Returns double value if the value is double, otherwise, returns null.

[asDuration](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#asDuration "A list of DQL conversion and casting functions.")

Returns duration value if the value is duration, otherwise, returns null.

[asIp](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#asIp "A list of DQL conversion and casting functions.")

You can use this function to cast to an IP address.

[asLong](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#asLong "A list of DQL conversion and casting functions.")

Returns long value if the value is long, otherwise, null.

[asNumber](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#asNumber "A list of DQL conversion and casting functions.")

Returns same value if the value is integer, long, double, otherwise. returns null.

[asRecord](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#asRecord "A list of DQL conversion and casting functions.")

Returns record value if the value is record, otherwise, returns null.

[asString](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#asString "A list of DQL conversion and casting functions.")

Returns string value if the value is string, otherwise, returns null.

[asTimeframe](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#asTimeframe "A list of DQL conversion and casting functions.")

Returns timeframe value if the value is timeframe, otherwise. returns null.

[asTimestamp](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#asTimestamp "A list of DQL conversion and casting functions.")

Returns timestamp value if the value is timestamp, otherwise, returns null.

[asUid](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#asUid "A list of DQL conversion and casting functions.")

Returns a uid value if the value is a uid, otherwise, returns null.

[decode](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#decode "A list of DQL conversion and casting functions.")

The decode functions allow decoding an encoded string representation into a plain string or binary data.

[encode](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#encode "A list of DQL conversion and casting functions.")

The encode functions allow encoding binary data and plain strings into an encoded string representation.

[getHighBits](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#getHighBits "A list of DQL conversion and casting functions.")

Extracts the most significant bits of a uid value or IP address.

[getLowBits](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#getLowBits "A list of DQL conversion and casting functions.")

Extracts the least significant bits of a uid value or IP address.

[hexStringToNumber](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#hexStringToNumber "A list of DQL conversion and casting functions.")

Converts a hexadecimal string to a number.

[isUid128](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#isUid128 "A list of DQL conversion and casting functions.")

Tests if a uid value is of subtype uid128.

[isUid64](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#isUid64 "A list of DQL conversion and casting functions.")

Tests if a uid value is of subtype uid64.

[isUuid](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#isUuid "A list of DQL conversion and casting functions.")

Tests if a uid value is of subtype uuid.

[numberToHexString](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#numberToHexString "A list of DQL conversion and casting functions.")

Converts a number to a hexadecimal string.

[toArray](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#toArray "A list of DQL conversion and casting functions.")

Returns the value if it is an array.

[toBoolean](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#toBoolean "A list of DQL conversion and casting functions.")

Converts a value to Boolean if the value is of a suitable type.

[toDouble](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#toDouble "A list of DQL conversion and casting functions.")

Converts a value to double if the value is of a suitable type.

[toDuration](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#toDuration "A list of DQL conversion and casting functions.")

Converts a value to duration if the value is of a suitable type.

[toIp](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#toIp "A list of DQL conversion and casting functions.")

You can use this function to convert an expression to an IP address.

[toLong](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#toLong "A list of DQL conversion and casting functions.")

Converts a value to long if the value is of a suitable type.

[toString](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#toString "A list of DQL conversion and casting functions.")

Returns the string representation of a value.

[toTimeframe](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#toTimeframe "A list of DQL conversion and casting functions.")

Converts a value to timeframe if the value is of a suitable type.

[toTimestamp](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#toTimestamp "A list of DQL conversion and casting functions.")

Converts a value to timestamp if the value is of a suitable type.

[toUid](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#toUid "A list of DQL conversion and casting functions.")

Converts a value to uid if the value is of a suitable type.

[type](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#type "A list of DQL conversion and casting functions.")

Returns the type of value as a string.

[uid128](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#uid128 "A list of DQL conversion and casting functions.")

Creates a uid of subtype uid128 from two long expressions.

[uid64](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#uid64 "A list of DQL conversion and casting functions.")

Creates a uid of subtype uid64 from a long expression.

[uuid](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#uuid "A list of DQL conversion and casting functions.")

Creates a uid of subtype uuid from two long expressions.

[smartscapeId](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#smartscapeId "A list of DQL conversion and casting functions.")

Creates a smartscapeId from the given string and long expression.

[asSmartscapeId](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#asSmartscapeId "A list of DQL conversion and casting functions.")

Returns smartscapeId value if the value is `smartscapeId`, otherwise returns `null`.

[toSmartscapeId](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#toSmartscapeId "A list of DQL conversion and casting functions.")

Converts a value to `smartscapeId` if the value is of a suitable type.

## [Conditional functions](/docs/platform/grail/dynatrace-query-language/functions/conditional-functions "A list of DQL conditional functions.")

Functions that return a conditional result.

Name

Description

[coalesce](/docs/platform/grail/dynatrace-query-language/functions/conditional-functions#coalesce "A list of DQL conditional functions.")

Returns the first non-null argument, if any, otherwise null.

[if](/docs/platform/grail/dynatrace-query-language/functions/conditional-functions#if "A list of DQL conditional functions.")

Evaluates the condition, and returns the value of either the then or else parameter.

## [Boolean functions](/docs/platform/grail/dynatrace-query-language/functions/boolean-functions "A list of DQL boolean functions.")

Functions that evaluate boolean expressions and test the presence of values.

Name

Description

[isFalseOrNull](/docs/platform/grail/dynatrace-query-language/functions/boolean-functions#isFalseOrNull "A list of DQL boolean functions.")

Evaluates if an expression is false or null.

[isNotNull](/docs/platform/grail/dynatrace-query-language/functions/boolean-functions#isNotNull "A list of DQL boolean functions.")

Tests if a value is not null.

[isNull](/docs/platform/grail/dynatrace-query-language/functions/boolean-functions#isNull "A list of DQL boolean functions.")

Tests if a value is null.

[isTrueOrNull](/docs/platform/grail/dynatrace-query-language/functions/boolean-functions#isTrueOrNull "A list of DQL boolean functions.")

Evaluates if an expression is true or null.

## [Time functions](/docs/platform/grail/dynatrace-query-language/functions/time-functions "A list of DQL time functions.")

Time functions return the decimal number for a particular time value, calculate the number of time units (days, months, years) between two dates, and allow to determine timestamps and timeframes, among others.

Name

Description

[duration](/docs/platform/grail/dynatrace-query-language/functions/time-functions#duration "A list of DQL time functions.")

Creates a duration from the given amount and time unit.

[formatTimestamp](/docs/platform/grail/dynatrace-query-language/functions/time-functions#formatTimestamp "A list of DQL time functions.")

Formats a given timestamp according to a format string using a given pattern.

[getDayOfMonth](/docs/platform/grail/dynatrace-query-language/functions/time-functions#getDayOfMonth "A list of DQL time functions.")

Extracts the day of the month from a timestamp.

[getDayOfWeek](/docs/platform/grail/dynatrace-query-language/functions/time-functions#getDayOfWeek "A list of DQL time functions.")

Extracts the day of the week from a timestamp.

[getDayOfYear](/docs/platform/grail/dynatrace-query-language/functions/time-functions#getDayOfYear "A list of DQL time functions.")

Extracts the day of the year from a timestamp.

[getEnd](/docs/platform/grail/dynatrace-query-language/functions/time-functions#getEnd "A list of DQL time functions.")

Extracts the end timestamp from a timeframe.

[getHour](/docs/platform/grail/dynatrace-query-language/functions/time-functions#getHour "A list of DQL time functions.")

Extracts the hour from a timestamp.

[getMinute](/docs/platform/grail/dynatrace-query-language/functions/time-functions#getMinute "A list of DQL time functions.")

Extracts the minute from a timestamp.

[getMonth](/docs/platform/grail/dynatrace-query-language/functions/time-functions#getMonth "A list of DQL time functions.")

Extracts the month from a timestamp.

[getStart](/docs/platform/grail/dynatrace-query-language/functions/time-functions#getStart "A list of DQL time functions.")

Extracts the start timestamp from a timeframe.

[getSecond](/docs/platform/grail/dynatrace-query-language/functions/time-functions#getSecond "A list of DQL time functions.")

Extracts the second from a timestamp.

[getYear](/docs/platform/grail/dynatrace-query-language/functions/time-functions#getYear "A list of DQL time functions.")

Extracts the year from a timestamp.

[getWeekOfYear](/docs/platform/grail/dynatrace-query-language/functions/time-functions#getWeekOfYear "A list of DQL time functions.")

Extracts the week of the year from a timestamp.

[now](/docs/platform/grail/dynatrace-query-language/functions/time-functions#now "A list of DQL time functions.")

Returns the current time as a fixed timestamp of the query start.

[timeframe](/docs/platform/grail/dynatrace-query-language/functions/time-functions#timeframe "A list of DQL time functions.")

Creates a timeframe structure from the given start and end timestamps.

[timestamp](/docs/platform/grail/dynatrace-query-language/functions/time-functions#timestamp "A list of DQL time functions.")

Creates a timestamp using provided values in mandatory parameters.

[timestampFromUnixMillis](/docs/platform/grail/dynatrace-query-language/functions/time-functions#timestampFromUnixMillis "A list of DQL time functions.")

Creates a timestamp from the given milliseconds since Unix epoch.

[timestampFromUnixNanos](/docs/platform/grail/dynatrace-query-language/functions/time-functions#timestampFromUnixNanos "A list of DQL time functions.")

Creates a timestamp from the given nanoseconds since Unix epoch.

[timestampFromUnixSeconds](/docs/platform/grail/dynatrace-query-language/functions/time-functions#timestampFromUnixSeconds "A list of DQL time functions.")

Creates a timestamp from the given seconds since Unix epoch.

[unixMillisFromTimestamp](/docs/platform/grail/dynatrace-query-language/functions/time-functions#unixMillisFromTimestamp "A list of DQL time functions.")

Converts a timestamp into milliseconds since Unix epoch.

[unixNanosFromTimestamp](/docs/platform/grail/dynatrace-query-language/functions/time-functions#unixNanosFromTimestamp "A list of DQL time functions.")

Converts a timestamp into nanoseconds since Unix epoch.

[unixSecondsFromTimestamp](/docs/platform/grail/dynatrace-query-language/functions/time-functions#unixSecondsFromTimestamp "A list of DQL time functions.")

Converts a timestamp into seconds since Unix epoch.

## [Array functions](/docs/platform/grail/dynatrace-query-language/functions/array-functions "A list of DQL array functions.")

Functions related to a collection of items of the same data type stored at adjacent memory locations.

Name

Description

[array](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array "A list of DQL array functions.")

Creates an array from the list of given parameters.

[arrayAvg](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-avg "A list of DQL array functions.")

Returns the average of an array.

[arrayConcat](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-concat "A list of DQL array functions.")

Concatenates multiple arrays into a single array.

[arrayCumulativeSum](/docs/platform/grail/dynatrace-query-language/functions/array-functions#arrayCumulativeSum "A list of DQL array functions.")

Returns the cumulative sum, also known as the running total, of the elements of the input array.

[arrayDelta](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-delta "A list of DQL array functions.")

Returns an array where each element is the difference from the previous non-null element.

[arrayDiff](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-diff "A list of DQL array functions.")

Calculates the element-wise difference between consecutive elements in an array.

[arrayDistinct](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-distinct "A list of DQL array functions.")

Returns the array without duplicates.

[arrayElement](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-element "A list of DQL array functions.")

Extracts a single element with the given index from an array.

[arrayFirst](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-first "A list of DQL array functions.")

Returns the first non-null element of an array.

[arrayFlatten](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-flatten "A list of DQL array functions.")

Returns a flattened array.

[arrayIndexOf](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-index-of "A list of DQL array functions.")

Returns position of the first member in the array, which is equal to the given value.

[arrayLast](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-last "A list of DQL array functions.")

Returns the last non-null element of an array.

[arrayLastIndexOf](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-last-index-of "A list of DQL array functions.")

Returns position of the last member in the array, which is equal to the given value.

[arrayMax](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-max "A list of DQL array functions.")

Returns the biggest number of an array.

[arrayMedian](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-median "A list of DQL array functions.")

Returns the median of the members of an array.

[arrayMin](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-min "A list of DQL array functions.")

Returns the smallest number of an array.

[arrayMovingAvg](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-moving-avg "A list of DQL array functions.")

Replaces each element of the input array with the average of current and previous elements within the window.

[arrayMovingMax](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-moving-max "A list of DQL array functions.")

Replaces each element of the input array with the maximum of current and previous elements within the window.

[arrayMovingMin](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-moving-min "A list of DQL array functions.")

Replaces each element of the input array with the minimum of current and previous elements within the window.

[arrayMovingSum](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-moving-sum "A list of DQL array functions.")

Replaces each element of the input array with the sum of current and previous elements within the window.

[arrayPercentile](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-percentile "A list of DQL array functions.")

Calculates a given percentile of an array.

[arrayRemoveNulls](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-remove-nulls "A list of DQL array functions.")

Returns the array where null elements are removed.

[arrayReverse](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-reverse "A list of DQL array functions.")

Returns the array with elements in reversed order.

[arraySize](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-size "A list of DQL array functions.")

Returns the size of an array.

[arraySlice](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-slice "A list of DQL array functions.")

Extracts a slice from the input array using a `from` index (inclusive) and a `to` index (exclusive).

[arraySort](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-sort "A list of DQL array functions.")

Returns the array with elements sorted in ascending order by default.

[arraySum](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-sum "A list of DQL array functions.")

Returns the sum of an array.

[arraytoString](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-to-String "A list of DQL array functions.")

Converts an array into a string.

## [Vector distance functions](/docs/platform/grail/dynatrace-query-language/functions/vector-distance-functions "A list of DQL vector distance functions.")

Functions that calculate the distance between numeric array expressions.

Name

Description

[vectorL1Distance](/docs/platform/grail/dynatrace-query-language/functions/vector-distance-functions#vectorL1Distance "A list of DQL vector distance functions.")

Calculates the taxicab distance between numeric array expressions.

[vectorL2Distance](/docs/platform/grail/dynatrace-query-language/functions/vector-distance-functions#vectorL2Distance "A list of DQL vector distance functions.")

Calculates the Euclidean distance between numeric array expressions.

[vectorCosineDistance](/docs/platform/grail/dynatrace-query-language/functions/vector-distance-functions#vectorCosineDistance "A list of DQL vector distance functions.")

Calculates the cosine distance between numeric array expressions.

[vectorInnerProductDistance](/docs/platform/grail/dynatrace-query-language/functions/vector-distance-functions#vectorInnerProductDistance "A list of DQL vector distance functions.")

Calculates the negative dot product between numeric array expressions.

## [Network functions](/docs/platform/grail/dynatrace-query-language/functions/network-functions "A list of DQL array functions.")

Functions related to IP addresses.

Name

Description

[ip](/docs/platform/grail/dynatrace-query-language/functions/network-functions#ip "A list of DQL array functions.")

You can use this function to create an IP address.

[ipIn](/docs/platform/grail/dynatrace-query-language/functions/network-functions#ipIn "A list of DQL array functions.")

This function can be used to check if a list of IP addresses or an IP network (e.g. 127.0.0.1/8) contains particular IP addresses

[ipIsLinkLocal](/docs/platform/grail/dynatrace-query-language/functions/network-functions#ipIsLinkLocal "A list of DQL array functions.")

Checks if an IP address is a link-local IP address.

[ipIsLoopback](/docs/platform/grail/dynatrace-query-language/functions/network-functions#ipIsLoopback "A list of DQL array functions.")

Checks if an IP address is a loopback IP address.

[ipIsPrivate](/docs/platform/grail/dynatrace-query-language/functions/network-functions#ipIsPrivate "A list of DQL array functions.")

Checks if an IP address is a private IP address.

[ipIsPublic](/docs/platform/grail/dynatrace-query-language/functions/network-functions#ipIsPublic "A list of DQL array functions.")

Checks if an IP address is a public IP address.

[ipMask](/docs/platform/grail/dynatrace-query-language/functions/network-functions#ipMask "A list of DQL array functions.")

You can use this function to mask an IP address with given bits.

[isIp](/docs/platform/grail/dynatrace-query-language/functions/network-functions#isIp "A list of DQL array functions.")

Checks if an expression is an IPv4/v6 address.

[isIpV4](/docs/platform/grail/dynatrace-query-language/functions/network-functions#isIpV4 "A list of DQL array functions.")

Checks if an expression is an IPv4 address.

[isIpV6](/docs/platform/grail/dynatrace-query-language/functions/network-functions#isIpV6 "A list of DQL array functions.")

Checks if an expression is an IPv6 address.

## [Hash functions](/docs/platform/grail/dynatrace-query-language/functions/hash-functions "A list of DQL hash functions.")

Hash related functions.

Name

Description

[hashCrc32](/docs/platform/grail/dynatrace-query-language/functions/hash-functions#hashCrc32 "A list of DQL hash functions.")

Returns a CRC32 hash for a given string expression.

[hashMd5](/docs/platform/grail/dynatrace-query-language/functions/hash-functions#hashMd5 "A list of DQL hash functions.")

Computes the MD5 hash for a given string expression.

[hashSha1](/docs/platform/grail/dynatrace-query-language/functions/hash-functions#hashSha1 "A list of DQL hash functions.")

Computes the SHA-1 hash for a given string expression.

[hashSha256](/docs/platform/grail/dynatrace-query-language/functions/hash-functions#hashSha256 "A list of DQL hash functions.")

Returns a SHA-256 hash for the given expression.

[hashSha512](/docs/platform/grail/dynatrace-query-language/functions/hash-functions#hashSha512 "A list of DQL hash functions.")

Returns a SHA-512 hash for the given expression.

[hashXxHash32](/docs/platform/grail/dynatrace-query-language/functions/hash-functions#hashXxHash32 "A list of DQL hash functions.")

Returns a xxHash32 hash for a given string expression.

[hashXxHash64](/docs/platform/grail/dynatrace-query-language/functions/hash-functions#hashXxHash64 "A list of DQL hash functions.")

Returns a xxHash64 hash for a given string expression.

## [Bitwise functions](/docs/platform/grail/dynatrace-query-language/functions/bitwise-functions "A list of DQL bitwise functions.")

Bitwise operations performing on long expressions.

Name

Description

[bitwiseAnd](/docs/platform/grail/dynatrace-query-language/functions/bitwise-functions#bitwiseAnd "A list of DQL bitwise functions.")

Calculates the bitwise and between two long expressions.

[bitwiseCountOnes](/docs/platform/grail/dynatrace-query-language/functions/bitwise-functions#bitwiseCountOnes "A list of DQL bitwise functions.")

Counts the bits assigned to one of the long expressions.

[bitwiseNot](/docs/platform/grail/dynatrace-query-language/functions/bitwise-functions#bitwiseNot "A list of DQL bitwise functions.")

Inverts the bits included in the long expression.

[bitwiseShiftLeft](/docs/platform/grail/dynatrace-query-language/functions/bitwise-functions#bitwiseShiftLeft "A list of DQL bitwise functions.")

Shifts the long expressions by the number of given bits to the left.

[bitwiseShiftRight](/docs/platform/grail/dynatrace-query-language/functions/bitwise-functions#bitwiseShiftRight "A list of DQL bitwise functions.")

Shifts the long expression by number of given bits to the right.

[bitwiseOr](/docs/platform/grail/dynatrace-query-language/functions/bitwise-functions#bitwiseOr "A list of DQL bitwise functions.")

Calculates the bitwise or between two long expressions.

[bitwiseXor](/docs/platform/grail/dynatrace-query-language/functions/bitwise-functions#bitwiseXor "A list of DQL bitwise functions.")

Calculates the bitwise xor between two long expressions.

## [Mathematical functions](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions "A list of DQL mathematical functions.")

Functions executing mathematical calculations.

Name

Description

[abs](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#abs "A list of DQL mathematical functions.")

Returns the absolute value of numeric\_expression.

[acos](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#acos "A list of DQL mathematical functions.")

Computes arc cosine of expression.

[asin](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#asin "A list of DQL mathematical functions.")

Computes arc sine of expression.

[atan](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#atan "A list of DQL mathematical functions.")

Computes the arc tangent of expression.

[atan2](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#atan2 "A list of DQL mathematical functions.")

Computes the angle theta from the conversion of rectangular coordinates (x, y) to polar coordinates (r, theta).

[bin](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#bin "A list of DQL mathematical functions.")

Rounds values down to a multiple of a given numeric bin size.

[ceil](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#ceil "A list of DQL mathematical functions.")

Calculates the smallest (closest to negative infinity) double value greater than or equal to the numeric\_expression; is equal to a mathematical integer.

[cos](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#cos "A list of DQL mathematical functions.")

Computes the trigonometric cosine of an angle expression (in radians).

[cosh](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#cosh "A list of DQL mathematical functions.")

Computes the hyperbolic cosine of an angle expression.

[cbrt](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#cbrt "A list of DQL mathematical functions.")

Calculates the real cubic root of a numeric expression.

[degreeToRadian](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#degreeToRadian "A list of DQL mathematical functions.")

Converts the numeric expression of an angle in degrees to an approximately equivalent angle as expressed in radians.

[e](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#e "A list of DQL mathematical functions.")

Returns Eulerâs number.

[exp](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#exp "A list of DQL mathematical functions.")

Calculates the exponential function e^x, where e is the Euler's number and x is a numeric expression.

[floor](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#floor "A list of DQL mathematical functions.")

Calculates the largest (closest to positive infinity) double value less than or equal to the numeric\_expression; and is equal to a mathematical integer.

[hypotenuse](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#hypotenuse "A list of DQL mathematical functions.")

Returns sqrt (x^2 + y^2).

[log](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#log "A list of DQL mathematical functions.")

Calculates the natural logarithm (the base is e, the Euler's number) of a numeric expression.

[log1p](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#log1p "A list of DQL mathematical functions.")

Calculates log(1+x), where log is the natural logarithm and x is a numeric expression.

[log10](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#log10 "A list of DQL mathematical functions.")

Calculates the decadic (common) logarithm (the base is 10) of a numeric expression.

[pi](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#pi "A list of DQL mathematical functions.")

Returns the constant value of PI (Archimedesâ number).

[power](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#power "A list of DQL mathematical functions.")

Raises a numeric expression to a given power.

[radianToDegree](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#radianToDegree "A list of DQL mathematical functions.")

Converts the numeric expression of an angle in radians to an approximately equivalent angle as expressed in degrees.

[random](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#random "A list of DQL mathematical functions.")

Creates a random double value.

[range](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#range "A list of DQL mathematical functions.")

Aligns the given value/timestamp to value range based on the provided alignment parameter.

[round](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#round "A list of DQL mathematical functions.")

Rounds any numeric value to the specified number of decimal places.

[signum](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#signum "A list of DQL mathematical functions.")

Returns the signum (sign) result of an argument.

[sin](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#sin "A list of DQL mathematical functions.")

Computes the trigonometric sine of angle expression (in radians).

[sinh](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#sinh "A list of DQL mathematical functions.")

Computes the hyperbolic sine of expression.

[sqrt](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#sqrt "A list of DQL mathematical functions.")

Computes the positive square root of a numeric expression.

[tan](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#tan "A list of DQL mathematical functions.")

Computes the trigonometric tangent of angle expression (in radians).

[tanh](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#tanh "A list of DQL mathematical functions.")

Computes the hyperbolic tangent of expression.

## [Join functions](/docs/platform/grail/dynatrace-query-language/functions/join-functions "A list of DQL join functions.")

Functions that join records from subqueries.

Name

Description

[lookup](/docs/platform/grail/dynatrace-query-language/functions/join-functions#lookup "A list of DQL join functions.")

Returns a record from a subquery (the lookup table) producing a match between a field in the source table (sourceField) and a field in the lookup table (lookupField).

[getNodeName](/docs/platform/grail/dynatrace-query-language/functions/join-functions#getNodeName "A list of DQL join functions.")

Returns the Smartscape node name.

[getNodeField](/docs/platform/grail/dynatrace-query-language/functions/join-functions#getNodeField "A list of DQL join functions.")

Returns the field value for a Smartscape node.

## [General functions](/docs/platform/grail/dynatrace-query-language/functions/general-functions "A list of DQL general functions.")

Functions with a general purpose.

Name

Description

[classicEntitySelector](/docs/platform/grail/dynatrace-query-language/functions/general-functions#classic-entity-selector "A list of DQL general functions.")

Returns entities matching the specified entity selector.

[entityAttr](/docs/platform/grail/dynatrace-query-language/functions/general-functions#entity-attr "A list of DQL general functions.")

Returns the attribute value for an entity.

[entityName](/docs/platform/grail/dynatrace-query-language/functions/general-functions#entity-name "A list of DQL general functions.")

Returns the name of an entity.

[exists](/docs/platform/grail/dynatrace-query-language/functions/general-functions#exists "A list of DQL general functions.")

Tests if a field exists.

[in](/docs/platform/grail/dynatrace-query-language/functions/general-functions#in "A list of DQL general functions.")

Tests if a value is a member of an array.

[record](/docs/platform/grail/dynatrace-query-language/functions/general-functions#record "A list of DQL general functions.")

Creates a record from the keys and values of the parameter.

## Related topics

* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Use DQL queries](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.")
* [DQL compared to SQL and more](/docs/platform/grail/dynatrace-query-language/dql-comparison "See how DQL compares to other query languages.")
* [DQL language reference](/docs/platform/grail/dynatrace-query-language/dql-reference "Dynatrace Query Language syntax reference.")
* [DQL commands](/docs/platform/grail/dynatrace-query-language/commands "A list of DQL commands.")
* [DQL operators](/docs/platform/grail/dynatrace-query-language/operators "A list of DQL Operators.")
* [DQL data types](/docs/platform/grail/dynatrace-query-language/data-types "A list of DQL data types.")
* [DQL best practices](/docs/platform/grail/dynatrace-query-language/dql-best-practices "Best practices for using Dynatrace Query Language.")