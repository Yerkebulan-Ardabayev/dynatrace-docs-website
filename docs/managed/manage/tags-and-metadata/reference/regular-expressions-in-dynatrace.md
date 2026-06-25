---
title: Regular expressions in Dynatrace
source: https://docs.dynatrace.com/managed/manage/tags-and-metadata/reference/regular-expressions-in-dynatrace
scraped: 2026-05-12T11:11:35.590676
---

# Regular expressions in Dynatrace

# Regular expressions in Dynatrace

* Explanation
* 5-min read
* Published Mar 28, 2018

Regular expressions are very powerful if you want to find or extract a certain pattern in a string. However, with great power comes great responsibility. Regular expressions can lead to unexpected results ([lazy vs greedy matchingï»¿](https://www.regular-expressions.info/repeat.html)) and they can quickly become resource intensive ([catastrophic backtrackingï»¿](https://www.regular-expressions.info/catastrophic.html) and [repeated capture groupsï»¿](https://www.regular-expressions.info/captureall.html)).

Regular expressions are also often misunderstood. A small regular expression can easily consume a lot of processing power when used incorrectly. As an example, consider this regular expression `(.*)+b`. This expression may not look dangerous, but if you execute it against a larger string that doesn't contain `b`, this expression will result in a loop that lasts more than 10 seconds.

For these reasons, weâve restricted regular expressions within Dynatrace. In almost all cases however, this will not restrict you in functionality. It may force you though to learn a bit more about regular expressions.

## Restrictions

Read the restrictions provided below to understand how to use regular expressions in the context of Dynatrace.

### Quantified or repeated groups are not allowed

Quantified groups usually aren't needed and, as they can easily run out of control, we don't allow them. To better understand this, go to [https://regex101.comï»¿](https://regex101.com/r/swArJ6/30) and evaluate the following regex:

```
Regex: (a+)+b



Value:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
```

You'll notice that it will timeout. In this particular case, the problem is with the backtracking nature of a capture group. We have decided not to allow the usage of repeated groups altogether.

### Greedy matches in capture groups vs possessive matches.

Dynatrace doesnât allow greedy matches within capture groups. Use lazy or possessive matching instead.

The prototypical usage of regular expression is the term `.*`. A greedy match is defined as "Matches between zero and unlimited times, as many times as possible, giving back as needed (greedy)". The problem here is the "as many times" and the "giving back". People typically use this to match something until a boundary condition is met. Consider the following regex match:

```
Regex: key: (.*);



Value: something. key: value; something else
```

The regex engine will first search for `key:`  and then *greedy* match the group `(.*)` till **the end of the string**. Subsequently it checks if there is a `;` *after* that match; which will *never* be the case. It then has to backtrack one character at a time. Each time it will first check if the group still matches each time until it finds the `;`. As a small detail, it will also have to remember a new value for the group each time; as it is a capture group. All of this is very expensive and inefficient; and more importantly, increases in complexity with the length of the string to be matched.

A better way to do this is as follows:

```
Regex: key: ([^;]*+)



Value: something. key: value; something else
```

This match will match as long as no `;` is found after `key:` . The plus also turns this into a possessive match defined as: "Matches between zero and unlimited times, as many times as possible, without giving back (possessive)". The key point here is that it doesn't backtrack. In other words once something has matched, then engine will not reconsider and will not look back but only forward. This is also why we need to refine our match from everything (`.`) to everything but not `;`. We need to tell it to match *everything but not `;`*.

If you compare the [first regexï»¿](https://regex101.com/r/EG4nNO/1) against the [secondï»¿](https://regex101.com/r/Bh0tWf/1) in a regex debugger (follow the two links), you will also notice that the first takes 42 steps and the second 9! This is why we recommend that you should use possessive quantifiers in general.

### Capture groups are not allowed for simple matches

Capture groups in regular expressions are used to extract information. Sometimes this concept is misused for simple find matches. As this only adds overhead and is not needed, Dynatrace doesn't allow it. In most cases, you can use [atomic groupsï»¿](https://www.regular-expressions.info/atomic.html) instead. To ensure high product performance, further grouping restrictions might apply in regex definitions, for example in [request naming rules](/managed/observe/application-observability/services/service-detection/service-detection-v1/set-up-request-naming#limitations "Adjust request naming and define the operations your services offer.").

Dynatrace allows exactly one capture group in places where you need to extract a value. The logic here is that if the regular expression contains a group, Dynatrace will use it. Otherwise, the full match is used for extraction.

This means that you are not required to use capture groups at all. In most extraction scenarios, it's enough to simply define what you want to get. In an extraction case the following regex will capture the valueâno capture group needed.

If you want to capture for example the Windows version from a user agent string, you can use the following regex:

```
Regex: Windows NT[^)]+



Value: Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0 Safari/537.36
```

This will capture `Windows NT 10.0` and there is no need for a capture group.

### Dynatrace doesnât allow backreferences

Backreferences are often used to solve hierarchical or recursive matches, both of which have a high chance of being very expensive and aren't needed in Dynatrace.

## Other common misunderstandings

Often people assume that they need to match the full input text. This usually results in a regular expression like this:

```
Regex: .*key: [^;]*+.*



Value: something. key: value; something else
```

This matches the full string instead of just what is needed. This is based on the misunderstanding that a given regex will always match the full text, where it's usually used to find a substring. In Dynatrace, regex conditions typically search for the pattern and don't forcefully match the whole input. Leading and trailing (`.*`) matches aren't needed, so please don't use them.