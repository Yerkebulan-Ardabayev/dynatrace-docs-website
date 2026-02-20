---
title: DPL Universally Unique Identifiers
source: https://www.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/log-processing-uuid-numbers
scraped: 2026-02-20T21:23:11.132704
---

# DPL Universally Unique Identifiers

# DPL Universally Unique Identifiers

* Latest Dynatrace
* Reference
* Published Jan 17, 2023

Matches valid Universally Unique Identifiers (UUIDs), such as social security numbers. Creates a UUID string parser.

output type

quantifier

configuration

STRING

none

none

### Example

```
This is a string with UUID b79cb3ba-745e-5d9a-8903-4a02327a7e09 somewhere in the middle
```

Pattern:

```
UUIDSTRING:uuid LD
```

Parsing results: UUID is extracted from the string.

uuid

b79cb3ba-745e-5d9a-8903-4a02327a7e09