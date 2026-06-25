---
title: Log processing functions (Logs Classic)
source: https://docs.dynatrace.com/managed/analyze-explore-automate/log-monitoring/log-processing/log-processing-functions
scraped: 2026-05-12T12:00:18.926101
---

# Log processing functions (Logs Classic)

# Log processing functions (Logs Classic)

* Overview
* 4-min read
* Updated on Jan 18, 2023

Log Monitoring Classic

Query functions can be used to perform any desired computation on fields of the [FIELDS\_ADD](/managed/analyze-explore-automate/log-monitoring/log-processing/log-processing-commands#dpl-command-fields-add "Use log processing commands that reshape your incoming log data for better analysis or further processing.") and [FILTER\_OUT](/managed/analyze-explore-automate/log-monitoring/log-processing/log-processing-commands#dpl-command-filter-out "Use log processing commands that reshape your incoming log data for better analysis or further processing.") statements.

## Bitwise operations

### AND

**numeric\_expr1 & numeric\_expr2**

**BITWISE\_AND(numeric\_expr1, numeric\_expr2)**

Bitwise AND between numeric expressions.

**BITWISE\_AND(ipaddr, numeric\_expr)**

Bitwise AND between IPADDR and numeric arguments.

output type  
`LONG` or `IPADDR` depending on input argument types.

**Example**:

```
FIELDS_ADD(and_op:(ip & 0xffff), and_fn:BITWISE_AND(i, 0xffff));
```

| and\_op | and\_fn |
| --- | --- |
| 0.0.255.255 | 65535 |

### OR

**numeric\_expr1 | numeric\_expr2**

**BITWISE\_OR(numeric\_expr1, numeric\_expr2)**

Bitwise OR between numeric expressions.

output type  
`LONG`

**Example**:

```
FIELDS_ADD(or_op:(i | 1), or_fn:BITWISE_OR(d, 0xffff));
```

| or\_op | or\_fn |
| --- | --- |
| 1 | 65535 |

### XOR

**numeric\_expr1 ^ numeric\_expr2**

**BITWISE\_XOR(numeric\_expr1, numeric\_expr2)**

Bitwise XOR (exclusive or) between numeric expressions.

output type  
`LONG`

**Example**:

```
FIELDS_ADD(xor_op:(i ^ 1), xor_fn:BITWISE_XOR(d, 0xffff));
```

| xor\_op | xor\_fn |
| --- | --- |
| 0 | 65534 |

### LEFT\_SHIFT

**numeric\_expr1 << numeric\_expr2**

**LEFT\_SHIFT(numeric\_expr1, numeric\_expr2)**

Bitwise shift left *numeric\_expr1* by number of bits *numeric\_expr2*.

output type  
`LONG`

**Example**:

```
FIELDS_ADD(lshift_op:(i << 1), lshift_fn:LEFT_SHIFT(d, 2));
```

| lshift\_op | lshift\_fn |
| --- | --- |
| 2 | 4 |

### RIGHT\_SHIFT

**numeric\_expr1 >> numeric\_expr2**

**RIGHT\_SHIFT(numeric\_expr1, numeric\_expr2)**

Bitwise shift right *numeric\_expr1* by number of bits *numeric\_expr2*.

output type  
`LONG`

**Example**:

```
FIELDS_ADD(rshift_op:i >> 1, rshift_fn:RIGHT_SHIFT(d, 2));
```

| rshift\_op | rshift\_fn |
| --- | --- |
| 32767 | 16383 |

### ZERO\_FILL\_RIGHT\_SHIFT

**numeric\_expr1 >>> numeric\_expr2**

**ZERO\_FILL\_RIGHT\_SHIFT(numeric\_expr1, numeric\_expr2)**

Unsigned bitwise shift right *numeric\_expr1* by the number of bits of *numeric\_expr2* (shifts zero into leftmost position).

output type  
`LONG`

**Example**:

```
FIELDS_ADD(rshift_op:i >>> 1, rshift_fn:ZERO_FILL_RIGHT_SHIFT(d, 2));
```

| rshift\_op | rshift\_fn |
| --- | --- |
| 1073741824 | 536870912 |

### BITWISE\_NOT

**~ numeric\_expr**

**BITWISE\_NOT(numeric\_expr)**

Inverts the bits of numeric\_expr.

output type  
`LONG`

**Example**:

```
FIELDS_ADD(not_op:~i, not_fn:BITWISE_NOT(i));
```

| not\_op | not\_fn |
| --- | --- |
| -1 | -1 |

### BIT\_COUNT

**BIT\_COUNT(numeric\_expr)**

Returns count of bits set to 1 of *numeric\_expr*.

output type  
`LONG`

**Example**:

```
FIELDS_ADD(BIT_COUNT(1));
```

| bit\_count |
| --- |
| 1 |

## Boolean

### AND

**boolean\_expr1 AND boolean\_expr2**

Logical conjunction between operands *boolean\_expr1*, *boolean\_expr2*. Returns true only when both operands evaluates to true.

Returns NULL if right side operand or both operands evaluate to NULL.

output\_type  
`BOOLEAN`

Truth table:

| a | b | a AND b |
| --- | --- | --- |
| TRUE | TRUE | TRUE |
| TRUE | FALSE | FALSE |
| TRUE | NULL | NULL |
| FALSE | FALSE | FALSE |
| FALSE | NULL | FALSE |
| NULL | NULL | NULL |

**Example**:

```
FIELDS_ADD(false AND true);
```

| logical\_and |
| --- |
| false |

### OR

**boolean\_expr1 OR boolean\_expr2**

Logical disjunction between operands *boolean\_expr1*, *boolean\_expr2*. Returns true only when either of operands evaluate to true.

Returns NULL if right side operand or both operands evaluate to NULL.

output\_type  
`BOOLEAN`

Truth table:

| a | b | a OR b |
| --- | --- | --- |
| TRUE | TRUE | TRUE |
| TRUE | FALSE | TRUE |
| TRUE | NULL | TRUE |
| FALSE | FALSE | FALSE |
| FALSE | NULL | NULL |
| NULL | NULL | NULL |

**Example**:

```
FIELDS_ADD(false OR true);
```

| logical\_or |
| --- |
| true |

### XOR

**boolean\_expr1 XOR boolean\_expr2**

Logical exclusive disjunction between operands *boolean\_expr1*, *boolean\_expr2*.

Returns NULL either of the operands evaluate to NULL.

output\_type  
`BOOLEAN`

Truth table:

| a | b | a XOR b |
| --- | --- | --- |
| TRUE | TRUE | FALSE |
| TRUE | FALSE | TRUE |
| FALSE | TRUE | TRUE |
| FALSE | FALSE | FALSE |
| TRUE | NULL | NULL |
| FALSE | NULL | NULL |
| NULL | NULL | NULL |

**Example**:

```
FIELDS_ADD(true XOR true);
```

| logical\_or |
| --- |
| true |

### NOT

**NOT boolean\_expr**

Returns negation of *boolean\_expr*. Returns NULL if *boolean\_expr* evaluates to NULL.

output\_type  
`BOOLEAN`

Truth table:

| a | NOT a |
| --- | --- |
| TRUE | FALSE |
| FALSE | TRUE |
| NULL | NULL |

**Example**:

```
FIELDS_ADD(NOT true);
```

| logical\_not |
| --- |
| false |

## Casting

### BOOLEAN

**BOOLEAN(string)**

Returns TRUE on following *string* values:
`T, t, Y, y, 1, YES, yes, TRUE, true`.

Returns NULL if *string* argument evaluates to NULL.

Returns FALSE on any other *string* value.

output type  
`BOOLEAN`

**Example**:

```
FIELDS_ADD(bval:BOOLEAN('T'));
```

| bval |
| --- |
| true |

**BOOLEAN(numeric\_expr)**

*numeric\_expr* value 0 is converted to false, other values to true.

Returns NULL if *numeric\_expr* evaluates to NULL.

output type  
`BOOLEAN`

**Example**:

```
FIELDS_ADD(bval:BOOLEAN(i));
```

| bval |
| --- |
| false |
| true |
| true |

### BYTES

**BYTES(string)**

Converts *string* argument to `BYTES`. Returns NULL if *string* evaluates to NULL.

output type  
`BYTES`

**Example**:

```
FIELDS_ADD(b:BYTES('01'));
```

| b |
| --- |
| [48,49] |

**BYTES(numeric\_array)**

Converts *numeric\_array* values to `BYTES`. Returns NULL if *numeric\_array* evaluates to NULL.

output type  
`BYTES`

**Example**:

```
FIELDS_ADD(b:BYTES([1023,1024,1]));
```

| b |
| --- |
| [-1,0,1] |

### DOUBLE

**DOUBLE(numeric\_expr)**

Converts *numeric\_expr* to `DOUBLE`. Returns NULL if *numeric\_expr* evaluates to NULL.

output type  
`DOUBLE`

**Example**

```
FIELDS_ADD(d:DOUBLE(2 * 300));
```

| d |
| --- |
| 600.0 |

**DOUBLE(string)**

Converts *string* argument to `DOUBLE`. Returns NULL if *string* evaluates to NULL.

output type  
`DOUBLE`

**Example**

```
FIELDS_ADD(d:DOUBLE("-4"));
```

| d |
| --- |
| -4.0 |

### DURATION

**DURATION(nanoseconds)**

Converts numeric *nanoseconds* value to `DURATION`. Returns NULL if *nanoseconds* evaluates to NULL.

output type  
`DURATION`

**Example**

```
FIELDS_ADD(DURATION(1000*60*60*24*30*1000000));
```

| duration |
| --- |
| 30 days, 00:00:00.000 |

### INTEGER

**INTEGER, INT(numeric\_expr)**

Converts *numeric\_expr* to `INTEGER`. Returns NULL if *numeric\_expr* evaluates to NULL.

output type  
`INTEGER`

**Example**

```
FIELDS_ADD(i:INT(2.498));
```

| i |
| --- |
| 2 |

**INTEGER, INT(string)**

Converts *string* argument to `INTEGER`. Returns NULL if *string* evaluates to NULL.

output type  
`INTEGER`

**Example**

```
FIELDS_ADD(i:INT("-4"));
```

| i |
| --- |
| -4 |

**INTEGER, INT(timestamp)**

Converts *timestamp* argument to `INTEGER`. Returns NULL if *timestamp* evaluates to NULL.

output type  
`INTEGER`

**Example**

```
FIELDS_ADD(i:INT(TIMESTAMP("2019-03-14 22:41:55.000 +0000")));
```

| i |
| --- |
| 1552603315 |

### IPADDR

**IPADDR(numeric\_expr), IPV4(numeric\_expr)**

Converts *numeric\_expr* arg to `IPADDR`. Returns NULL if *numeric\_expr* evaluates to NULL.

output type  
`IPADDR`

**Example**

```
FIELDS_ADD(ip:IPADDR(-1062731520));
```

| ip |
| --- |
| 192.168.1.0 |

**IPADDR(hi\_64\_bit\_num, low\_64\_bit\_num), IPV6(IPADDR(hi\_64\_bit\_num, low\_64\_bit\_num))**

Converts 128-bit numeric argument to `IPADDR`. Returns NULL if arguments evaluate to NULL.

output type  
`IPADDR`

**Example**

```
FIELDS_ADD(ip:IPADDR(1,1));
```

| ip |
| --- |
| ::1:0:0:0:1 |

**IPADDR(string), IPV4(string), IPV6(string)**

Converts *string* arg to `IPADDR`. Returns NULL if *string* evaluates to NULL.

output type  
`IPADDR`

**Example**

```
FIELDS_ADD(ip:IPADDR("192.168.1.0"));
```

| ip |
| --- |
| 192.168.1.0 |

### LONG

**LONG(numeric\_expr)**

Converts *numeric\_expr* to `LONG`. Returns NULL if *numeric\_expr* evaluates to NULL.

output type  
`LONG`

**Example**

```
FIELDS_ADD(l:LONG(2.498));
```

| l |
| --- |
| 2 |

**LONG(string)**

Converts *string* argument to `LONG`. Returns NULL if *string* evaluates to NULL.

output type  
`LONG`

**Example**

```
FIELDS_ADD(l:LONG("-4"));
```

| l |
| --- |
| -4 |

### STRING

**STRING(*expr*)**

Converts *expr* returning any type to `STRING`. Returns NULL if *expr* evaluates to NULL.

output type  
`STRING`

**Example**

```
FIELDS_ADD(int_str:STRING(i), double_str:STRING(d), ip_str:STRING(ip));
```

| int\_str | double\_str | ip\_str |
| --- | --- | --- |
| 0 | 0.0 | 0.0.0.0 |
| 1 | 1.0 | 0.0.0.1 |
| 2 | 2.0 | 0.0.0.2 |

### TIMESTAMP

**TIMESTAMP(*integer*), T(*integer*)**

Converts *integer* seconds elapsed from [Unix epochï»¿](https://en.wikipedia.org/wiki/Epoch_(computing)) to `TIMESTAMP`.

Returns NULL if *integer* evaluates to NULL.

output type  
`TIMESTAMP`

**Example**

```
FIELDS_ADD(TIMESTAMP(1552603315));
```

| timestamp |
| --- |
| 2019-03-14 22:41:55.333000000 +0000 |

**TIMESTAMP(long), T(long)**

Converts *long* milliseconds elapsed from [Unix epochï»¿](https://en.wikipedia.org/wiki/Epoch_(computing)) to `TIMESTAMP`.

Returns NULL if *long* evaluates to NULL.

output type  
`TIMESTAMP`

**Example**

```
FIELDS_ADD(T(1552603315l*1000+333));
```

| timestamp |
| --- |
| 2019-03-14 22:41:55.333000000 +0000 |

**TIMESTAMP(year, month, day), T(year, month, day)**

Converts date specified by integer arguments to `TIMESTAMP`. Returns NULL if arguments evaluate to NULL.

output type  
`TIMESTAMP`

**Example**

```
FIELDS_ADD(TIMESTAMP(2019,03,14));
```

| timestamp |
| --- |
| 2019-03-14 00:00:00.000000000 +0000 |

**TIMESTAMP(year, month, day, hour), T(year, month, day, hour)**

Converts date and time specified by integer arguments to `TIMESTAMP`. Returns NULL if arguments evaluate to NULL.

output type  
`TIMESTAMP`

**Example**

```
FIELDS_ADD(TIMESTAMP(2019,03,14,22));
```

| timestamp |
| --- |
| 2019-03-14 22:00:00.000000000 +0000 |

**TIMESTAMP(year, month, day, hour, minutes), T(year, month, day, hour, minutes)**

Converts date and time specified by integer arguments to `TIMESTAMP`. Returns NULL if arguments evaluate to NULL.

output type  
`TIMESTAMP`

**Example**

```
FIELDS_ADD(TIMESTAMP(2019,03,14,22,41));
```

| timestamp |
| --- |
| 2019-03-14 22:41:00.000000000 +0000 |

**TIMESTAMP(year, month, day, hour, minutes, seconds), T(year, month, day, hour, minutes, seconds)**

Converts date and time specified by integer arguments to `TIMESTAMP`. Returns NULL if arguments evaluate to NULL.

output type  
`TIMESTAMP`

**Example**

```
FIELDS_ADD(TIMESTAMP(2019,03,14,22,41,55));
```

| timestamp |
| --- |
| 2019-03-14 22:41:55.000000000 +0000 |

**TIMESTAMP(year, month, day, hour, minutes, seconds, milliseconds)**

**T(year, month, day, hour, minutes, seconds, milliseconds)**

Converts date and time specified by integer arguments to `TIMESTAMP`. Returns NULL if arguments evaluate to NULL.

output type  
`TIMESTAMP`

**Example**

```
FIELDS_ADD(TIMESTAMP(2019,03,14,22,41,55,333));
```

| timestamp |
| --- |
| 2019-03-14 22:41:55.333000000 +0000 |

**TIMESTAMP(string), T(string)**

Converts following format *string* args to `TIMESTAMP`:

* "yyyy-MM-dd HH:mm:ss"
* "yyyy-MM-dd HH:mm:ss Z"
* "yyyy-MM-dd HH:mm:ss.SSS"
* "yyyy-MM-dd HH:mm:ss.SSS Z"
* "yyyy-MM-dd HH:mm:ss.f"
* "yyyy-MM-dd HH:mm:ss.f Z"

Returns NULL if argument *string* evaluates to NULL.

output type  
`TIMESTAMP`

**Example**

```
FIELDS_ADD(TIMESTAMP("2019-03-14 22:41:55.333 GMT"));
```

| timestamp |
| --- |
| 2019-03-14 22:41:55.333 +0000 |

### TO\_NULL

**TO\_NULL(*expr*)**

Returns NULL value.

output type  
the type of supplied argument

**Example**

```
FIELDS_ADD(n_i:TO_NULL(i), n_ip:TO_NULL(ip), n_time:TO_NULL(t), n_str:TO_NULL(s));
```

Result details (double click on resultset):

| name | value | type |
| --- | --- | --- |
| n\_i | NULL | INTEGER |
| n\_ip | NULL | IPADDR |
| n\_time | NULL | TIMESTAMP |
| n\_str | NULL | STRING |

### TUPLE

**TUPLE(*expr*, â¦)**

Converts one or more expressions returning any data type to `TUPLE`.

output type  
`TUPLE`

**Example**

```
FIELDS_ADD(t:TUPLE(1,2.0,"foo")) | FIELDS_ADD(TYPE(t));
```

| t | type |
| --- | --- |
| {f\_0=1 f\_1=2.0 f\_2="foo"} | TUPLE |

### VARIANT

**VARIANT(*expr*)**

**VAR(*expr*)**

Converts primitive type *expr* to `VARIANT`. Returns NULL if *expr* evaluates to NULL.

output type  
`VARIANT`

**Example**

```
FIELDS_ADD(var:VARIANT(s));
```

Result details (double click on resultset row):

| name | value | type |
| --- | --- | --- |
| var | 0ho0 | VARIANT<STRING> |

### VARIANT\_ARRAY

**VARIANT\_ARRAY(*arg*)**

**VAR\_ARR(*arg*)**

Converts `ARRAY` or primitive type *arg* to `VARIANT_array`

output type  
`VARIANT_array`

**Example**

```
FIELDS_ADD(res:VARIANT_ARRAY([1,2,3])) | FIELDS_ADD(TYPE(res));
```

| res | type |
| --- | --- |
| [1,2,3] | VARIANT\_ARRAY |

### VARIANT\_OBJECT

**VARIANT\_OBJECT(*expr*)**

Converts `TUPLE`, `VARIANT` or primitive type *expr* to `VARIANT_OBJECT`.

output type  
`VARIANT_OBJECT`

**Example**

```
FIELDS_ADD(vo_tuple:VARIANT_OBJECT({a:1, b:2})) | FIELDS_ADD(TYPE(vo_tuple));
```

| vo\_tuple | type |
| --- | --- |
| {"a":1,"b":2} | VARIANT\_OBJECT |

**EMPTY\_ARRAY(*type*)**

Creates an empty array of *type*

**NULL\_ARRAY(*type*)**

Creates a null array of *type*

output\_type  
`ARRAY`

**NULL\_TUPLE(*type*)**

Creates a null tuple of *type*

output\_type  
`TUPLE`

## Comparison

### EQUAL

**expr1 = expr2**

**EQUAL(expr1, expr2)**

Returns true if the expressions are equal.

Returns NULL if *expr1* or *expr2* arguments evaluate to NULL.

Returns FALSE otherwise.

output type  
`BOOLEAN`

**Example**:

```
FIELDS_ADD(1 = 1);
```

| equal |
| --- |
| true |

### NOT\_EQUAL

**expr1 <> expr2**

**expr1 != expr2**

**NOT\_EQUAL(expr1, expr2)**

Returns true if the expressions are not equal.

Returns NULL if *expr1* or *expr2* arguments evaluate to NULL.

Returns FALSE otherwise.

output type  
`BOOLEAN`

**Example**:

```
FIELDS_ADD(1 != 1);
```

| equal |
| --- |
| false |

### GREATER

**expr1 > expr2**

**GREATER(expr1, expr2)**

Returns true if *expr1* is greater than *expr2*.

Returns NULL if *expr1* or *expr2* arguments evaluate to NULL.

Returns FALSE otherwise.

output type  
`BOOLEAN`

**Example**:

```
FIELDS_ADD(gr_op:2 > 1, gr_f:GREATER(1,1));
```

| gr\_op | gr\_f |
| --- | --- |
| true | false |

### LESS

**expr1 < expr2**

**LESS(expr1, expr2)**

Returns true if *expr1* is less than *expr2*.

Returns NULL if *expr1* or *expr2* arguments evaluate to NULL.

Returns FALSE otherwise.

output type  
`BOOLEAN`

**Example**:

```
FIELDS_ADD(l_op:1 < 2, l_f:LESS(1,1));
```

| l\_op | l\_f |
| --- | --- |
| true | false |

### GREATER\_OR\_EQUAL

**expr1 >= expr2**

**GREATER\_OR\_EQUAL(expr1, expr2)**

Returns true if *expr1* is greater than or equal to *expr2*.

Returns NULL if *expr1* or *expr2* arguments evaluate to NULL.

Returns FALSE otherwise.

output type  
`BOOLEAN`

**Example**:

```
FIELDS_ADD(gr_op:2 >= 1, gr_f:GREATER_OR_EQUAL(1,1));
```

| gr\_op | gr\_f |
| --- | --- |
| true | true |

### LESS\_OR\_EQUAL

**expr1 <= expr2**

**LESS\_OR\_EQUAL(expr1, expr2)**

Returns true if *expr1* is less than or equal to *expr2*.

Returns NULL if *expr1* or *expr2* arguments evaluate to NULL.

Returns FALSE otherwise.

output type  
`BOOLEAN`

**Example**:

```
FIELDS_ADD(gr_op:1 <= 2, gr_f:GREATER_OR_EQUAL(1,1));
```

| gr\_op | gr\_f |
| --- | --- |
| true | true |

### IS NULL

**expr IS NULL**

**IS\_NULL(expr)**

Returns true if *expr* is NULL, otherwise returns false.

output type  
`BOOLEAN`

**Example**:

```
FIELDS_ADD(s, is_null:IS_NULL(s));
```

| s | is\_null |
| --- | --- |
| 0ho0 | false |

### IS NOT NULL

**expr IS NOT NULL**

**IS\_NOT\_NULL(expr)**

Returns true if *expr* is NOT NULL, otherwise returns false.

output type  
`BOOLEAN`

**Example**:

```
FIELDS_ADD(s, is_not_null:s IS NOT NULL);
```

| s | is\_not\_null |
| --- | --- |
| 0ho0 | true |

### IN

**expr IN array**

Returns true if *expr* is present in *array*, otherwise returns FALSE.

**expr NOT IN array**

A negated version of the above: Returns true if *expr* is not present in *array*, otherwise returns FALSE.

Returns NULL if *array* evaluates to NULL.

output type  
`BOOLEAN`

Note

the *expr* has to be the same type as items in the *array*.

**Example**:

```
FIELDS_ADD(str_in:'a' IN ['b','c','a']);
```

| str\_in |
| --- |
| true |

**expr IN list**

Returns true if *expr* is present in *list*, otherwise returns FALSE.

**expr NOT IN list**

A negated version of the above: Returns true if *expr* is not present in *list*, otherwise returns FALSE.

Returns NULL if *list* evaluates to NULL.

output type  
`BOOLEAN`

Note

All members of the *list* have to be the same type as the *expr* being testedâ¦

### FALSE\_OR\_NULL

**FALSE\_OR\_NULL(boolean\_expr)**

Returns true if *boolean\_expr* returns false or null

output type  
`BOOLEAN`

**Example**:

```
FIELDS_ADD(i, FALSE_OR_NULL(i = 0));
```

| i | false\_or\_null |
| --- | --- |
| 0 | false |
| 1 | true |

### TRUE\_OR\_NULL

**TRUE\_OR\_NULL(boolean\_expr)**

Returns true if *boolean\_expr* returns true or null

output type  
`BOOLEAN`

**Example**:

```
FIELDS_ADD(i, TRUE_OR_NULL(i = 0));
```

| i | true\_or\_null |
| --- | --- |
| 0 | true |
| 1 | false |

## Composite-data

### VARIANT\_FIELD\_SELECT

**VARIANT\_FIELD\_SELECT(variant, fieldname)**

Selects *fieldname* from VARIANT\_OBJECT or VARIANT\_ARRAY *variant* object. This function can be used when arguments are evaluated dynamically at runtime.

Note

The function is complementary to accessing object elements directly.

output type  
the type of the *fieldname* selected.

**Example**: select member named "ip" from a variant object:

```
FIELDS_ADD(obj:VARIANT_OBJECT(tuple)) | FIELDS_ADD(VARIANT_FIELD_SELECT(obj, 'ip'))
```

| variant\_field\_select |
| --- |
| 0.0.0.0 |

### TUPLE\_FIELD\_SELECT

**TUPLE\_FIELD\_SELECT(tuple, fieldname)**

Selects *fieldname* from *tuple*. This function can be used when arguments are evaluated dynamically at runtime.

Note

The function is complementary to accessing tuple elements directly.

output type  
the type of the *fieldname* selected

**Example**: select member named "ip" from a variant object:

```
FIELDS_ADD(tuple) | FIELDS_ADD(TUPLE_FIELD_SELECT(tuple, 'ip'))
```

| ip |
| --- |
| 0.0.0.0 |

### ARRAY\_AVG

**ARRAY\_AVG(array)**

Computes arithmetic mean of numeric *array* members.

output type  
`DOUBLE`

**Example**:

```
FIELDS_ADD(array:[0,1,2,3,4]) | FIELDS_ADD(ARRAY_AVG(array));
```

| array\_avg |
| --- |
| 2.0 |

### ARRAY\_COUNT

**ARRAY\_COUNT(array)**

Computes count of not NULL members of *array*.

output type  
`LONG`

**Example**:

```
FIELDS_ADD(array:[0,1,2,3,4]) | FIELDS_ADD(ARRAY_COUNT(array));
```

| array\_count |
| --- |
| 5 |

### ARRAY\_FIRST

**ARRAY\_FIRST(array)**

Returns the first value in the *array*.

output type  
the type of the array member

**Example**:

```
FIELDS_ADD(array:[0,1,2,3,4]) | FIELDS_ADD(ARRAY_FIRST(array));
```

| array\_first |
| --- |
| 0 |

### ARRAY\_LAST

**ARRAY\_LAST(array)**

Returns the last value in the *array*.

output type  
the type of the array member

**Example**:

```
FIELDS_ADD(array:[0,1,2,3,4]) | FIELDS_ADD(ARRAY_LAST(array));
```

| array\_last |
| --- |
| 4 |

### ARRAY\_MAX

**ARRAY\_MAX(array)**

Returns the max value of numeric *array* members.

output type  
the type of the array member

**Example**:

```
FIELDS_ADD(array:[0,1,2,3,4]) | FIELDS_ADD(ARRAY_MAX(array));
```

| array\_max |
| --- |
| 4 |

### ARRAY\_MIN

**ARRAY\_MIN(array) Returns min value of numeric *array* members.**

output type  
the type of the array member

**Example**:

```
FIELDS_ADD(array:[0,1,2,3,4]) | FIELDS_ADD(ARRAY_MIN(array));
```

| array\_min |
| --- |
| 0 |

### ARRAY\_JOIN

**ARRAY\_JOIN(array, str)**

Returns string with *array* elements concatenated in order of their appearance and separated by *str*.

output type  
`STRING`

**Example**:

```
FIELDS_ADD(array:[0,1,2,3,4]) | FIELDS_ADD(ARRAY_JOIN(array, " + "));
```

| array\_join |
| --- |
| 0 + 1 + 2 + 3 + 4 |

### ARRAY\_SORT

**ARRAY\_SORT(array)**

Returns copy of *array* with members sorted in ascending order.

output type  
`ARRAY`

**Example**:

```
FIELDS_ADD(array:[2,1,0,4,3]) | FIELDS_ADD(ARRAY_SORT(array));
```

| array\_sort |
| --- |
| [0, 1, 2, 3, 4] |

**ARRAY\_SORT(array, boolean)**

Returns sorted *array*. Sorting order is determined by *boolean* argument: if true then ascending, otherwise descending.

output type  
`ARRAY`

**Example**:

```
FIELDS_ADD(array:[2,1,0,4,3]) | FIELDS_ADD(ARRAY_SORT(array, false));
```

| array\_sort |
| --- |
| [4, 3, 2, 1, 0] |

### ARRAY\_SUM

**ARRAY\_SUM(array)**

Computes the sum of numeric *array* members.

output type  
`DOUBLE`

**Example**:

```
FIELDS_ADD(array:[0,1,2,3,4]) | FIELDS_ADD(ARRAY_SUM(array));
```

| array\_sum |
| --- |
| 10.0 |

### ARRAY\_IDX

**ARRAY\_IDX(array, expr)**

Returns position of the first member in *array* which is equal to *expr*. If not found returns NULL.

output type  
the type of array member

**Example**:

```
FIELDS_ADD(array:[0,1,2,3,4]) | FIELDS_ADD(ARRAY_IDX(array,4));
```

| array\_idx |
| --- |
| 4 |

### ARRAY\_SELECT

**ARRAY\_SELECT(array, integer)**

Returns element from *array* at position *integer*. If not found returns NULL.

output type  
the type of array member.

**Example**:

```
FIELDS_ADD(array:[0,1,2,3,4]) | FIELDS_ADD(ARRAY_SELECT(array,4));
```

| array\_4 |
| --- |
| 4 |

**ARRAY\_SELECT(array, start\_pos, end\_pos)**

Returns elements of *array* from *start\_pos* to *end\_pos* inclusive. If not found returns empty array.

output type  
`ARRAY`

**Example**:

```
FIELDS_ADD(array:[0,1,2,3,4]) | FIELDS_ADD(ARRAY_SELECT(array,1,3));
```

| array\_select |
| --- |
| [1, 2, 3] |

### ARRAY\_LEN

**ARRAY\_LEN(array)**

Returns the number of elements in *array*.

output type  
`INTEGER`

**Example**:

```
FIELDS_ADD(array:[0,1,2,3,4]) | FIELDS_ADD(ARRAY_LEN(array));
```

| array\_len |
| --- |
| 5 |

### ARRAY\_REMOVE\_NULLS

ARRAY\_REMOVE\_NULLS(array)

Removes elements with NULL values from *array*.

output type  
`ARRAY`

**Example**:

```
FIELDS_ADD(array:[0,1,TO_NULL(2),3,4])



| FIELDS_ADD(array, new_array:ARRAY_REMOVE_NULLS(array));
```

| array | new\_array |
| --- | --- |
| [0, 1, null, 3, 4] | [0, 1, 3, 4] |

### ARRAY\_REVERSE

ARRAY\_REVERSE(array)

Returns array with elements in reversed order.

output type  
`ARRAY`

**Example**:

```
FIELDS_ADD(arr:[0,1,2,3]) | FIELDS_ADD(arr, reverse_arr:ARRAY_REVERSE(arr))
```

| arr | reverse\_arr |
| --- | --- |
| [0, 1, 2, 3] | [3, 2, 1, 0] |

### REMOVE\_NULLS

REMOVE\_NULLS(variant\_object)

REMOVE\_NULLS(variant\_array)

REMOVE\_NULLS(array)

Removes elements with NULL values from *variant\_object*, *variant\_array* or *array* argument.

output type  
`VARIANT_OBJECT` or `VARIANT_ARRAY` or `ARRAY`

**Example**:

```
FIELDS_ADD(v_obj:VARIANT_OBJECT({a:1, b:"oho", c:TO_NULL(1)}))



| FIELDS_ADD(v_obj, REMOVE_NULLS(v_obj))



;
```

| v\_obj | remove\_nulls |
| --- | --- |
| {"a":1,"b":"oho","c":null} | {"a":1,"b":"oho"} |

### ARRAY\_UNIQ

**ARRAY\_UNIQ(array)**

Returns array with unique values from argument *array*.

output type  
`ARRAY`

**Example**:

```
FIELDS_ADD(arr:[1,2,3,4,5,1,1,2]) | FIELDS_ADD(arr, ARRAY_UNIQ(arr));
```

| arr | array\_uniq |
| --- | --- |
| [1, 2, 3, 4, 5, 1, 1, 2] | [1, 2, 3, 4, 5] |

### SPREAD

**SPREAD(tuple)**

Expands fields from the `TUPLE` argument to the fields of resultset row.

**Example:**

```
FIELDS_ADD(tuple, SPREAD(tuple));
```

| i | ip | ip6 | s | t | ips | ip6s |
| --- | --- | --- | --- | --- | --- | --- |
| 2 | 0.0.0.2 | 0.0.0.2 | 2ho2 | 2ho2 | [0.0.0.2, 0.0.0.3] | [0.0.0.2, 0.0.0.3] |
| 3 | 0.0.0.3 | 0.0.0.3 | 3ho3 | 3ho3 | [0.0.0.3, 0.0.0.4, 0.0.0.5] | [0.0.0.3, 0.0.0.4, 0.0.0.5] |

## Cryptographic

### MD5

**MD5(string\_expr)**

Computes MD5 hash value of *string\_expr*.

output type  
`STRING`

**Example**:

```
FIELDS_ADD(MD5('Dynatrace'));
```

| md5 |
| --- |
| 3ab8eea866f50ad0e62659e0550ca3ac |

### SHA

**SHA1(string\_expr)**

Computes SHA1 hash value of *string*.

output type  
`STRING`

**Example**:

```
FIELDS_ADD(SHA1('Dynatrace'));
```

| sha1 |
| --- |
| 52bf60ee2e00603e9db81b2e2f594b3f52d9431a |

## Date-time

### Operators

**timestamp\_value[+ amount time\_unit]**

Adds *amount* of *time\_units* to *timestamp\_value*.

Time units:  
ms or millis, sec or s, min or m, hour or h, day or d, week or w

output\_type  
`TIMESTAMP`

**Example**:

```
FIELDS_ADD(now(), now_add_1_min:now()[+1 min]);
```

| now | now\_add\_1\_min |
| --- | --- |
| 2020-04-30 12:26:30.354 +0300000000 | 2020-04-30 12:27:30.354 +0300000000 |

**timestamp\_value[- amount time\_unit]**

Subtracts *amount* of *time\_units* from *timestamp\_value*.

Time units: ms or millis, sec or s, min or m, hour or h, day or d, week or w

output\_type  
`TIMESTAMP`

**Example**:

```
FIELDS_ADD(now(), time_subtract_1_sec:now()[-1 sec]);
```

| now | time\_subtract\_1\_sec |
| --- | --- |
| 2020-04-30 12:28:25.235 +0300000000 | 2020-04-30 12:28:24.235 +0300000000 |

**timestamp\_value[amount time\_unit]**

**timestamp\_value[% amount time\_unit]**

Truncates the *timestamp\_value* to *amount* of *time\_units*.

Time units: ms or millis, sec or s, min or m, hour or h, day or d, week or w

output\_type  
`TIMESTAMP`

**Example**:

```
FIELDS_ADD(now(), now_truncated_1_h:now()[1 hour]);
```

| now | now\_truncated\_1\_h |
| --- | --- |
| 2019-09-18 12:04:45.839000000 +0000 | 2019-09-18 12:00:00.000000000 +0000 |

### DAY

**DAY(timestamp\_expr)**

Returns an integer representing the day of the month from *timestamp\_expr*.

output\_type  
`INTEGER`

**Example**:

```
FIELDS_ADD(DAY(T('2017-01-22 15:00:00')));
```

| day |
| --- |
| 22 |

### DAY\_OF\_WEEK

**DAY\_OF\_WEEK(timestamp\_expr)**

Returns an integer representing 1 - 7 day of the week from *timestamp\_expr*.

output\_type  
`INTEGER`

**Example**:

```
FIELDS_ADD(DAY_OF_WEEK(T('2017-01-22 15:00:00')));
```

| day\_of\_week |
| --- |
| 7 |

### DAY\_OF\_YEAR

**DAY\_OF\_YEAR(timestamp\_expr)**

Returns integer representing 1 - 365 day of the year (or 366 in the leap year) from *timestamp\_expr*

output\_type  
`INTEGER`

**Example**:

```
FIELDS_ADD(DAY_OF_YEAR(T('2017-05-22 15:00:00')));
```

| day\_of\_year |
| --- |
| 142 |

### HOUR

**HOUR(timestamp\_expr)**

Returns an integer representing 0 - 23 hour of the day from *timestamp\_expr*

output\_type  
`INTEGER`

**Example**:

```
FIELDS_ADD(HOUR(T('2016-09-23 17:58:00')));
```

| hour |
| --- |
| 17 |

### MINUTE

**MINUTE(timestamp\_expr)**

Returns an integer representing 0 - 59 minute of the hour from *timestamp\_expr*.

output\_type  
`INTEGER`

**Example**:

```
FIELDS_ADD(MINUTE(T('2016-09-23 17:58:00')));
```

| minute |
| --- |
| 58 |

### MONTH

**MONTH(timestamp\_expr)**

Returns an integer representing 1 - 12 month of the year from *timestamp\_expr*.

output\_type  
`INTEGER`

**Example**:

```
FIELDS_ADD(MONTH(T('2016-09-23 17:58:00')));
```

| month |
| --- |
| 9 |

### NOW

**NOW()**

Returns the query execution start timestamp.

output\_type  
`TIMESTAMP`

**Example**:

```
FIELDS_ADD(t, NOW());
```

| t | now |
| --- | --- |
| 2019-09-18 12:22:34.036000000 +0000 | 2019-09-18 12:22:34.036000000 +0000 |
| 2019-09-18 12:22:34.037000000 +0000 | 2019-09-18 12:22:34.036000000 +0000 |
| 2019-09-18 12:22:34.038000000 +0000 | 2019-09-18 12:22:34.036000000 +0000 |
| 2019-09-18 12:22:34.039000000 +0000 | 2019-09-18 12:22:34.036000000 +0000 |
| 2019-09-18 12:22:34.040000000 +0000 | 2019-09-18 12:22:34.036000000 +0000 |

### SECOND

**SECOND(timestamp\_expr)**

Returns integer representing 0 - 59 second of the minute from *timestamp\_expr*.

output\_type  
`INTEGER`

**Example**:

```
FIELDS_ADD(SECOND(T('2016-09-23 17:58:32')));
```

| second |
| --- |
| 32 |

### STR\_SEC\_TO\_TIME

**STR\_SEC\_TO\_TIME(seconds\_str)**

Converts *seconds\_str* seconds, elapsed from [Unix epochï»¿](https://en.wikipedia.org/wiki/Epoch_(computing)) to `TIMESTAMP`.

output\_type  
`TIMESTAMP`

**Example**:

```
FIELDS_ADD(STR_SEC_TO_TIME("1552603315"));
```

| str\_sec\_to\_time |
| --- |
| 2019-03-14 22:41:55.000000000 +0000 |

### STR\_TO\_TIME

**STR\_TO\_TIME(string)**

Converts *string* to `TIMESTAMP`. Argument string must be in one of the:

* "yyyy-MM-dd HH:mm:ss"
* "yyyy-MM-dd HH:mm:ss Z"
* "yyyy-MM-dd HH:mm:ss.SSS"
* "yyyy-MM-dd HH:mm:ss.SSS Z"

output\_type  
`TIMESTAMP`

**Example**:

```
FIELDS_ADD(STR_TO_TIME('2016-09-23 17:58:00'));
```

| t |
| --- |
| 2016-09-23 17:58:00.000000000 +0000 |

### SYS\_TIME

**SYS\_TIME()**

Returns the current timestamp from the operating system clock.

output\_type  
`TIMESTAMP`

**Example**:

```
FIELDS_ADD(SYS_TIME());
```

| sys\_time |
| --- |
| 2019-09-18 12:50:14.703000000 +0000 |

### TIME\_ADD

**TIME\_ADD(timestamp, millis)**

Adds *millis* of milliseconds to *timestamp*.

output\_type  
`TIMESTAMP`

**Example**:

```
FIELDS_ADD(t, TIME_ADD(t, 1000));
```

| t | time\_add |
| --- | --- |
| 2019-09-18 13:00:00.843000000 +0000 | 2019-09-18 13:00:01.843000000 +0000 |
| 2019-09-18 13:00:00.844000000 +0000 | 2019-09-18 13:00:01.844000000 +0000 |

### TIME\_ADD\_DAY

**TIME\_ADD\_DAY(timestamp, numeric\_expr)**

Adds *numeric\_expr* of days to *timestamp* and returns resulting TIMESTAMP value.

output\_type  
`TIMESTAMP`

**Example**:

```
FIELDS_ADD(now:NOW(), a_year_from_now:TIME_ADD_DAY(NOW(), 365));
```

| now | a\_year\_from\_now |
| --- | --- |
| 2020-07-06 13:17:13.828000000 +0300 | 2021-07-06 13:17:13.828000000 +0300 |

### TIME\_ADD\_WEEK

**TIME\_ADD\_WEEK(timestamp, numeric\_expr)**

Adds *numeric\_expr* of weeks to *timestamp* and returns resulting TIMESTAMP value.

output\_type  
`TIMESTAMP`

**Example**:

```
FIELDS_ADD(now:NOW(), about_a_year_from_now:TIME_ADD_WEEK(NOW(), 52))
```

| now | about\_a\_year\_from\_now |
| --- | --- |
| 2020-07-06 13:20:14.238000000 +0300 | 2021-07-05 13:20:14.238000000 +0300 |

### TIME\_ADD\_MONTH

**TIME\_ADD\_MONTH(timestamp, numeric\_expr)**

Adds *numeric\_expr* of months to *timestamp* and returns resulting TIMESTAMP value.

output\_type  
`TIMESTAMP`

**Example**:

```
FIELDS_ADD(now:NOW(), about_a_year_from_now:TIME_ADD_MONTH(NOW(), 12))
```

| now | about\_a\_year\_from\_now |
| --- | --- |
| 2020-07-06 13:21:23.209000000 +0300 | 2021-07-06 13:21:23.209000000 +0300 |

### TIME\_ADD\_YEAR

**TIME\_ADD\_YEAR(timestamp, numeric\_expr)**

Adds *numeric\_expr* of months to *timestamp* and returns resulting TIMESTAMP value.

output\_type  
`TIMESTAMP`

**Example**:

```
FIELDS_ADD(now:NOW(), a_century_from_now:TIME_ADD_YEAR(NOW(), 100))
```

| now | a\_century\_from\_now |
| --- | --- |
| 2020-07-06 13:23:22.497000000 +0300 | 2120-07-06 13:23:22.497000000 +0300 |

### TIME\_SUB

**TIME\_SUB(timestamp, millis)**

Subtracts *millis* milliseconds from *timestamp*.

output\_type  
`TIMESTAMP`

**Example**:

```
FIELDS_ADD(t, TIME_SUB(t, 60*1000));
```

| t | time\_sub |
| --- | --- |
| 2019-09-18 13:03:15.298000000 +0000 | 2019-09-18 13:02:15.298000000 +0000 |
| 2019-09-18 13:03:15.299000000 +0000 | 2019-09-18 13:02:15.299000000 +0000 |

### TIME\_SUB\_DAY

**TIME\_SUB\_DAY(timestamp, numeric\_expr)**

Subtracts *numeric\_expr* days from *timestamp* and returns resulting TIMESTAMP value.

output\_type  
`TIMESTAMP`

**Example**:

```
FIELDS_ADD(now:NOW(), a_day_ago:TIME_SUB_DAY(NOW(), 1));
```

| now | a\_day\_ago |
| --- | --- |
| 2020-07-06 13:26:22.474000000 +0300 | 2020-07-05 13:26:22.474000000 +0300 |

### TIME\_SUB\_WEEK

**TIME\_SUB\_DAY(timestamp, numeric\_expr)**

Subtracts *numeric\_expr* weeks from *timestamp* and returns resulting TIMESTAMP value.

output\_type  
`TIMESTAMP`

**Example**:

```
FIELDS_ADD(now:NOW(), a_week_ago:TIME_SUB_WEEK(NOW(), 1));
```

| now | a\_week\_ago |
| --- | --- |
| 2020-07-06 13:27:33.045000000 +0300 | 2020-06-29 13:27:33.045000000 +0300 |

### TIME\_SUB\_MONTH

**TIME\_SUB\_MONTH(timestamp, numeric\_expr)**

Subtracts *numeric\_expr* months from *timestamp* and returns resulting TIMESTAMP value.

output\_type  
`TIMESTAMP`

**Example**:

```
FIELDS_ADD(now:NOW(), a_month_ago:TIME_SUB_MONTH(NOW(), 1));
```

| now | a\_month\_ago |
| --- | --- |
| 2020-07-06 13:29:10.589000000 +0300 | 2020-06-06 13:29:10.589000000 +0300 |

### TIME\_SUB\_YEAR

**TIME\_SUB\_YEAR(timestamp, numeric\_expr)**

Subtracts *numeric\_expr* years from *timestamp* and returns resulting TIMESTAMP value.

output\_type  
`TIMESTAMP`

**Example**:

```
FIELDS_ADD(now:NOW(), a_century_ago:TIME_SUB_YEAR(NOW(), 100));
```

| now | a\_century\_ago |
| --- | --- |
| 2020-07-06 13:30:25.365000000 +0300 | 1920-07-06 13:30:25.365000000 +0200 |

### TIME\_SUBMOD

**TIME\_SUBMOD(timestamp, millis)**

Returns *timestamp* modulo *millis* - i.e truncates *timestamp* to the precision of *millis* milliseconds.

output\_type  
`TIMESTAMP`

**Example** Truncate timestamp to the precision of hour:

```
FIELDS_ADD(TIME_SUBMOD(T('2016-09-23 17:58:00'), 60*60*1000));
```

| time\_submod |
| --- |
| 2016-09-23 17:00:00.000000000 +0000 |

### TIME\_SUBMOD\_DAY

**TIME\_SUBMOD\_DAY(timestamp, numeric\_expr)**

Returns *timestamp* truncated to the precision of *numeric\_expr* days.

output\_type  
`TIMESTAMP`

**Example**:

```
FIELDS_ADD(now:NOW(), trunc_day:TIME_SUBMOD_DAY(NOW(), 1));
```

| now | trunc\_day |
| --- | --- |
| 2020-07-06 13:36:36.265000000 +0300 | 2020-07-06 00:00:00.000000000 +0300 |

### TIME\_SUBMOD\_WEEK

**TIME\_SUBMOD\_WEEK(timestamp, numeric\_expr)**

Returns *timestamp* truncated to the precision of *numeric\_expr* weeks.

output\_type  
`TIMESTAMP`

**Example**:

```
FIELDS_ADD(now:NOW(), trunc_4_week:TIME_SUBMOD_WEEK(NOW(), 4));
```

| now | trunc\_4\_week |
| --- | --- |
| 2020-07-06 13:38:37.376000000 +0300 | 2020-06-15 00:00:00.000000000 +0300 |

### TIME\_SUBMOD\_MONTH

**TIME\_SUBMOD\_WEEK(timestamp, numeric\_expr)**

Returns *timestamp* truncated to the precision of *numeric\_expr* months.

output\_type  
`TIMESTAMP`

**Example**:

```
FIELDS_ADD(now:NOW(), trunc_1_month:TIME_SUBMOD_MONTH(NOW(), 1));
```

| now | trunc\_1\_month |
| --- | --- |
| 2020-07-06 13:43:27.733000000 +0300 | 2020-07-01 00:00:00.000000000 +0300 |

### TIME\_SUBMOD\_YEAR

**TIME\_SUBMOD\_YEAR(timestamp, numeric\_expr)**

Returns *timestamp* truncated to the precision of *numeric\_expr* years.

output\_type  
`TIMESTAMP`

**Example**:

```
FIELDS_ADD(now:NOW(), trunc_1_year:TIME_SUBMOD_YEAR(NOW(), 1));
```

| now | trunc\_1\_year |
| --- | --- |
| 2020-07-06 13:44:38.594000000 +0300 | 2020-01-01 00:00:00.000000000 +0300 |

### TIME\_TO\_STR

**TIME\_TO\_STR(timestamp, format\_str)**

Converts *timestamp* to string as specified by `format_str <timestamp_format_str>`.

output\_type  
`STRING`

**Example**:

```
FIELDS_ADD(TIME_TO_STR(t, "EEEE, MMMM d 'anno domini' yyyy") );
```

| time\_to\_str |
| --- |
| Wednesday, September 18 anno domini 2019 |

### TO\_STR\_SEC

**TO\_STR\_SEC(timestamp)**

Converts *timestamp* to string of floating-point seconds elapsed from [Unix epochï»¿](https://en.wikipedia.org/wiki/Epoch_(computing)) (the
digits in the fraction part represent nanoseconds).

output\_type  
`STRING`

**Example**:

```
FIELDS_ADD(t, TO_STR_SEC(t));
```

| t | to\_str\_sec |
| --- | --- |
| 2019-09-18 13:25:24.438000000 +0000 | 1568813124.438000000 |

### YEAR

**YEAR(timestamp\_expr)**

Returns an integer representing year from *timestamp\_expr*.

output\_type  
`INTEGER`

**Example**:

```
FIELDS_ADD(YEAR(T('2017-01-22 15:00:00')));
```

| year |
| --- |
| 2017 |

### WEEK\_OF\_YEAR

**WEEK\_OF\_YEAR(timestamp\_expr)**

Returns an integer representing the week of the year of *timestamp\_expr*.

output\_type  
`INTEGER`

**Example**:

```
FIELDS_ADD(WEEK_OF_YEAR(T('2017-01-22 15:00:00')));
```

| week\_of\_year |
| --- |
| 3 |

## Flow-control

**IF(boolean\_expr,true\_expr,[else\_expr])**  
**IF\_THEN(boolean\_expr,true\_expr,[else\_expr])**  
**IF\_THEN\_ELSE(boolean\_expr,true\_expr,[else\_expr])**

Returns *true\_expr* if *boolean\_expr* evaluates to true, otherwise returns *else\_expr*.

output type  
the type returned by *true\_expr* or *else\_expr* (must be the same).

**Example**:

```
FIELDS_ADD(s, IF(s CONTAINS '0', 'contains zero', 'has no zero'));
```

| s | if\_then |
| --- | --- |
| 0ho0 | contains zero |
| 1ho1 | has no zero |

**IF\_THEN(boolean\_expr,true\_expr)**  
**IF\_THEN\_ELSE(boolean\_expr,true\_expr)**

Returns *true\_expr* if *boolean\_expr* evaluates to true, otherwise returns NULL.

output type  
the type returned by *true\_expr* or *else\_expr* (must be the same).

**Example**:

```
FIELDS_ADD(s, IF(s CONTAINS '0', 'contains zero'));
```

| s | if\_then |
| --- | --- |
| 0ho0 | contains zero |
| 1ho1 | NULL |

## Math

### Operators

**numeric\_expr1 + numeric\_expr2**

Arithmetic addition of *numeric\_expr2* to *numeric\_expr1*.

output type  
`LONG` when either of *numeric\_expr* is `INTEGER` or `LONG`

> `DOUBLE`
>
> `IPADDR` when either of *numeric\_expr* is `IPADDR`
>
> `TIMESTAMP` when one of *numeric\_expr* is `TIMESTAMP` (see also
> timestamp expressions)

**Example**:

```
FIELDS_ADD(i, int_add:i+1,



d, double_add:d+1,



ip, ipaddr_add:ip + 1,



t, time_add: t+1000);
```

| i | int\_add | d | double\_add | ip | ipaddr\_add | t | time\_add |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | 0.0 | 1.0 | 0.0.0.0 | 0.0.0.1 | 2019-09-18 09:25:00.687 +0000000000 | 2019-09-18 09:25:01.687 +0000000000 |
| 1 | 2 | 1.0 | 2.0 | 0.0.0.1 | 0.0.0.2 | 2019-09-18 09:25:00.688000000 +0000 | 2019-09-18 09:25:01.688 +0000000000 |

**numeric\_expr1 - numeric\_expr2**

Arithmetic subtraction of *numeric\_expr2* from *numeric\_expr1*.

output type  
`LONG` when either of *numeric\_expr* is `INTEGER` or `LONG`

> `DOUBLE` when either of *numeric\_expr* is `DOUBLE`
>
> `IPADDR` when either of *numeric\_expr* is `IPADDR`
>
> `TIMESTAMP` when one of *numeric\_expr* is `TIMESTAMP` (see also
> timestamp expressions)

**Example**:

```
FIELDS_ADD(i, int_sub:i-1,



d, double_sub:d-1,



ip, ipaddr_sub:ip - 1,



t, time_sub: t-1000);
```

| i | int\_sub | d | double\_sub | ip | ipaddr\_sub | t | time\_sub |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 1 | 2.0 | 1.0 | 0.0.0.2 | 0.0.0.1 | 2019-09-19 07:17:39.034000000 +0000 | 2019-09-19 07:17:38.034000000 +0000 |
| 3 | 2 | 3.0 | 2.0 | 0.0.0.3 | 0.0.0.2 | 2019-09-19 07:17:39.035000000 +0000 | 2019-09-19 07:17:38.035000000 +0000 |

**numeric\_expr1 \* numeric\_expr2**

Arithmetic multiplication of *numeric\_expr1* by *numeric\_expr2*.

output type  
`LONG` when either of *numeric\_expr* is `INTEGER` or `LONG`

> `DOUBLE` when either of *numeric\_expr* is `DOUBLE`

**Example**:

```
FIELDS_ADD(i, int_mult:i * 2, d, double_mult:d * 2);
```

| i | int\_mult | d | double\_mult |
| --- | --- | --- | --- |
| 0 | 0 | 0.0 | 0.0 |
| 1 | 2 | 1.0 | 2.0 |

**numeric\_expr1 / numeric\_expr2, DIVIDE(numeric\_expr1, numeric\_expr2)**

Arithmetic division of *numeric\_expr1* by *numeric\_expr2*.

output type  
`LONG` when either of *numeric\_expr* is `INTEGER` or `LONG`

> `DOUBLE` when either of *numeric\_expr* is `DOUBLE`

**Example**:

```
FIELDS_ADD(i, int_div:i / 2, d, double_div:d / 2);
```

| i | int\_div | d | double\_div |
| --- | --- | --- | --- |
| 2 | 1 | 2.0 | 1.0 |
| 3 | 1 | 3.0 | 1.5 |

**numeric\_expr1 % numeric\_expr2, MODULO(numeric\_expr1, numeric\_expr2)**

Computes remainder (modulo) of division *numeric\_expr1* by *numeric\_expr2*.

output type  
`LONG` when either of *numeric\_expr* is `INTEGER` or `LONG`

> `DOUBLE` when either of *numeric\_expr* is `DOUBLE`

**Example**:

```
FIELDS_ADD(i, int_mod:i % 2, d, double_mod:d % 2);
```

| i | int\_mod | d | double\_mod |
| --- | --- | --- | --- |
| 2 | 0 | 2.0 | 0.0 |
| 3 | 1 | 3.0 | 1.0 |

### ABS

**ABS(numeric\_expr)**

Returns absolute value of *numeric\_expr*. Returns NULL if *numeric\_expr* evaluatess to NULL.

output type  
`DOUBLE`

**Example**:

```
FIELDS_ADD(ABS(-10));
```

| abs |
| --- |
| 10 |

### ADD

**ADD(numeric\_expr1, numeric\_expr2)**

Arithmetic addition of *numeric\_expr2* to *numeric\_expr1*. Returns NULL if either of the arguments evaluates to NULL.

output type  
`LONG` when either of *numeric\_expr* is `INTEGER` or `LONG`

> `DOUBLE` when either of *numeric\_expr* is `DOUBLE`
>
> `IPADDR` when either of *numeric\_expr* is `IPADDR`
>
> `TIMESTAMP` when one of *numeric\_expr* is `TIMESTAMP` (see also
> timestamp expressions)

**Example**:

```
FIELDS_ADD(i, int_add:ADD(i, 1),



d, double_add:ADD(d, 1),



ip, ipaddr_add:ADD(ip, 1),



t, time_add:ADD(t, 1000)



);
```

| i | int\_add | d | double\_add | ip | ipaddr\_add | t | time\_add |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | 0.0 | 1.0 | 0.0.0.0 | 0.0.0.1 | 2019-09-19 07:28:24.073000000 +0000 | 2019-09-19 07:28:25.073000000 +0000 |
| 1 | 2 | 1.0 | 2.0 | 0.0.0.1 | 0.0.0.2 | 2019-09-19 07:28:24.074000000 +0000 | 2019-09-19 07:28:25.074000000 +0000 |

### ACOS

**ACOS(numeric\_expr)**

Computes arc cosine of *numeric expr*. The returned angle is in the range 0.0 through pi.

Returns NULL if *numeric\_expr* evaluates to NULL.

output type  
`DOUBLE`

**Example**:

```
FIELDS_ADD(ACOS(0.5));
```

| acos |
| --- |
| 1.0471975511965979 |

### ASIN

**ASIN(numeric\_expr)**

Computes arc sine of *numeric\_expr*. The returned angle is in the range -pi/2 through pi/2.

Returns NULL if *numeric\_expr* evaluates to NULL.

output type  
`DOUBLE`

**Example**:

```
FIELDS_ADD(ASIN(0.5));
```

| asin |
| --- |
| 0.5235987755982989 |

### ATAN

**ATAN(numeric\_expr)**

Computes arc tangent of *numeric\_expr*. The returned angle is in the range -p/2 through pi/2.

Returns NULL if *numeric\_expr* evaluates to NULL.

output type  
`DOUBLE`

**Example**:

```
FIELDS_ADD(ATAN(0.5));
```

| atan |
| --- |
| 0.4636476090008061 |

### ATAN2

**ATAN2(numeric\_expr1, numeric\_expr2)**

Computes the angle *theta* from the conversion of rectangular coordinates x,y to polar coordinates(r, *theta*).

Returns NULL if either of the arguments evaluates to NULL.

output type  
`DOUBLE`

**Example**:

```
FIELDS_ADD(ATAN2(0.5, 0.5));
```

| atan2 |
| --- |
| 0.7853981633974483 |

### CBRT

**CBRT(numeric\_expr)**

Computes the cube root of *numeric\_expr*.

Returns NULL if *numeric\_expr* evaluates to NULL.

output type  
`DOUBLE`

**Example**:

```
FIELDS_ADD(CBRT(27));
```

| cbrt |
| --- |
| 3.0 |

### CEIL

**CEIL(numeric\_expr)**

Computes the smallest (closest to negative infinity) double value that is greater than or equal to the *numeric\_expr* and is equal to a mathematical integer.

Returns NULL if *numeric\_expr* evaluates to NULL.

output type  
`DOUBLE`

**Example**:

```
FIELDS_ADD(CEIL(0.7));
```

| ceil |
| --- |
| 1.0 |

### COS

**COS(numeric\_expr)**

Computes the trigonometric cosine of an angle *numeric\_expr* (in radians).

Returns NULL if *numeric\_expr* evaluates to NULL.

output type  
`DOUBLE`

**Example**:

```
FIELDS_ADD(COS(0.5));
```

| cos |
| --- |
| 0.8775825618903728 |

### COSH

**COSH(numeric\_expr)**

Computes the hyperbolic cosine of an angle *numeric\_expr*.

Returns NULL if *numeric\_expr* evaluates to NULL.

output type  
`DOUBLE`

**Example**:

```
FIELDS_ADD(COSH(0.5));
```

| cosh |
| --- |
| 1.1276259652063807 |

### DEGREES

**DEGREES(numeric\_expr)**

Converts numeric expr angle (of radians) to an approximately equivalent angle of degrees.

Returns NULL if *numeric\_expr* evaluates to NULL.

output type  
`DOUBLE`

**Example**:

```
FIELDS_ADD(DEGREES(1.571));
```

| degrees |
| --- |
| 90.01166961505233 |

### DIVIDE

**DIVIDE(numeric\_expr1, numeric\_expr2)**

Arithmetic division of *numeric\_expr1* by *numeric\_expr2*. Returns NULL if any of the arguments evaluates to NULL.

output type  
`LONG` when either of *numeric\_expr* is `INTEGER` or `LONG`

> `DOUBLE` when either of *numeric\_expr* is `DOUBLE`

**Example**:

```
FIELDS_ADD(i, int_div:DIVIDE(i, 2), d, double_div:DIVIDE(d, 2));
```

| i | int\_div | d | double\_div |
| --- | --- | --- | --- |
| 2 | 1 | 2.0 | 1.0 |
| 3 | 1 | 3.0 | 1.5 |

### E

**E()**

Returns Euler's number.

output type  
`DOUBLE`

**Example**:

```
FIELDS_ADD(E());
```

| e |
| --- |
| 2.718281828459045 |

### EXP

**EXP(numeric\_expr)**

Computes Euler's number *e* raised to the power of *numeric\_expr*.

Returns NULL if *numeric\_expr* evaluates to NULL.

output type  
`DOUBLE`

**Example**:

```
FIELDS_ADD(EXP(2));
```

| exp |
| --- |
| 7.38905609893065 |

### EXPM1

**EXPM1(numeric\_expr)**

Returns e numeric\_expr -1

Returns NULL if *numeric\_expr* evaluates to NULL.

output type  
`DOUBLE`

**Example**:

```
FIELDS_ADD(EXPM1(2));
```

| expm1 |
| --- |
| 6.38905609893065 |

### FLOOR

**FLOOR(numeric\_expr)**

Computes the largest (closest to positive infinity) `DOUBLE` value, less than or equal to the *numeric expr* and is equal to a mathematical integer.

Returns NULL if *numeric\_expr* evaluates to NULL.

output type  
`DOUBLE`

**Example**:

```
FIELDS_ADD(FLOOR(2.71));
```

| floor |
| --- |
| 2.0 |

### FLOORDIV

**FLOORDIV(numeric\_expr1, numeric\_expr2)**

Computes mathematical integer floor of *numeric\_expr1* argument division by *numeric\_expr2*.

Returns NULL if either of the arguments evaluates to NULL.

output type  
`INTEGER` when both arguments are `INTEGER`

> `LONG` when any of the arguments are `LONG` or `DOUBLE`

**Example**:

```
FIELDS_ADD(FLOORDIV(5, 2.0));
```

| floordiv |
| --- |
| 2 |

### FLOORMOD

**FLOORMOD(numeric\_expr1, numeric\_expr2)**

Computes mathematical integer floor modulus of *numeric\_exp1* and *numeric\_expr2*.

Returns NULL if either of the arguments evaluates to NULL.

output type  
`INTEGER` when both arguments are `INTEGER`

> `LONG` when any of the arguments are `LONG` or `DOUBLE`

**Example**:

```
FIELDS_ADD(FLOORMOD(5, 2.71));
```

| floormod |
| --- |
| 1 |

### GETEXPONENT

**GETEXPONENT(numeric\_expr)**

Computes mathematical integer unbiased exponent used in the representation of *numeric\_expr* argument.

Returns NULL if *numeric\_expr* evaluates to NULL.

output type  
`INTEGER`

**Example**:

```
FIELDS_ADD(GETEXPONENT(28.71d));
```

| getexponent |
| --- |
| 4 |

### HYPOT

**HYPOT(numeric\_expr1, numeric\_expr2)**

Returns sqrt(x 2 +y2).

Returns NULL if *numeric\_expr* evaluates to NULL.

output type  
`DOUBLE`

**Example**:

```
FIELDS_ADD(HYPOT(3.0, 4))
```

| hypot |
| --- |
| 5.0 |

### IEEEREMAINDER

**IEEEREMAINDER(numeric\_expr1, numeric\_expr2)**

Returns `DOUBLE` value of the remainder operation on numeric arguments as prescribed by the IEEE 754 standard.

Returns NULL if either of the arguments evaluates to NULL.

output type  
`DOUBLE`

**Example**:

```
FIELDS_ADD(IEEEREMAINDER(7.389f, 5));
```

| ieeeremainder |
| --- |
| 2.3889999389648438 |

### LOG

**LOG(numeric\_expr)**

Computes the natural logarithm (base e) of *numeric\_expr*.

Returns NULL if *numeric\_expr* evaluates to NULL.

output type  
`DOUBLE`

**Example**:

```
FIELDS_ADD(LOG(7.389));
```

| log |
| --- |
| 1.9999924078065106 |

### LOG1P

**LOG1P(numeric\_expr)**

Computes the natural logarithm (base e) of the sum of the *numeric\_expr* and 1.

Returns NULL if *numeric\_expr* evaluates to NULL.

output type  
`DOUBLE`

**Example**:

```
FIELDS_ADD(LOG1P(7.389));
```

| log1p |
| --- |
| 2.1269213238641576 |

### LOG10

**LOG10(numeric\_expr)**

Computes base 10 logarithm of *numeric\_expr*.

Returns NULL if *numeric\_expr* evaluates to NULL.

output type  
`DOUBLE`

**Example**:

```
FIELDS_ADD(LOG10(7.389));
```

| log10 |
| --- |
| 0.8685856665587657 |

### MODULO

**MODULO(numeric\_expr1, numeric\_expr2)**

Computes remainder (modulo) of division *numeric\_expr1* by *numeric\_expr2*.

Returns NULL if either of the arguments evaluates to NULL.

output type  
`LONG` when either of *numeric\_expr* is `INTEGER` or `LONG`

> `DOUBLE` when either of *numeric\_expr* is `DOUBLE`

**Example**:

```
FIELDS_ADD(i, int_mod:MODULO(i, 2), d, double_mod:MODULO(d, 2));
```

| i | int\_mod | d | double\_mod |
| --- | --- | --- | --- |
| 2 | 0 | 2.0 | 0.0 |
| 3 | 1 | 3.0 | 1.0 |

### MULTIPLY

**MULTIPLY(numeric\_expr1, numeric\_expr2)**

Arithmetic multiplication of *numeric\_expr1* by *numeric\_expr2*.

Returns NULL if either of the arguments evaluates to NULL.

output type  
`LONG` when either of *numeric\_expr* is `INTEGER` or `LONG`

> `DOUBLE` when either of *numeric\_expr* is `DOUBLE`

**Example**:

```
FIELDS_ADD(i, int_mult:MULTIPLY(i, 2), d, double_mult:MULTIPLY(d, 2));
```

| i | int\_mult | d | double\_mult |
| --- | --- | --- | --- |
| 0 | 0 | 0.0 | 0.0 |
| 1 | 2 | 1.0 | 2.0 |

### NEXTAFTER

**NEXTAFTER(numeric\_expr1, numeric\_expr2)**

Returns number adjacent to the *numeric\_expr1* in the direction of the *numeric\_expr2*.

Returns NULL if either of the arguments evaluates to NULL.

output type  
`DOUBLE`

**Example**:

```
FIELDS_ADD(NEXTAFTER(3.33f, 2));
```

| nextafter |
| --- |
| 3.3299997 |

### NEXTDOWN

**NEXTDOWN(numeric\_expr)**

Returns the number adjacent to *numeric\_expr* argument in the direction of negative infinity.

Returns NULL if *numeric\_expr* evaluates to NULL.

output type  
`DOUBLE`

**Example**:

```
FIELDS_ADD(NEXTDOWN(3.33));
```

| nextdown |
| --- |
| 3.3299999999999996 |

### NEXTUP

**NEXTUP(numeric\_expr)**

Returns the number adjacent to *numeric\_expr* argument in the direction of positive infinity.

Returns NULL if *numeric\_expr* evaluates to NULL.

output type  
`DOUBLE`

**Example**:

```
FIELDS_ADD(NEXTUP(3.33));
```

| nextup |
| --- |
| 3.3300000000000005 |

### PI

**PI()**

Returns the value of pi.

output type  
`DOUBLE`

**Example**:

```
FIELDS_ADD(PI());
```

| pi |
| --- |
| 3.141592653589793 |

### POWER

**POWER(numeric\_expr1, numeric\_expr2)**

Computes the value of *numeric\_expr1* raised to the power of *numeric\_expr2*.

Returns NULL if either of the arguments evaluates to NULL.

output type  
`DOUBLE`

**Example**:

```
FIELDS_ADD(POWER(2, 3.5));
```

| power |
| --- |
| 11.313708498984761 |

### RADIANS

**RADIANS(numeric\_expr)**

Converts *numeric\_expr* angle of degrees to an approximately equivalent angle of radians.

Returns NULL if *numeric\_expr* evaluates to NULL.

output type  
`DOUBLE`

**Example**:

```
FIELDS_ADD(RADIANS(90));
```

| radians |
| --- |
| 1.5707963267948966 |

### RANDOM

**RANDOM()**

Returns random positive double value greater than or equal to 0.0 and less than 1.0.

output type  
`DOUBLE`

**Example**:

```
FIELDS_ADD(RANDOM());
```

| random |
| --- |
| 0.752088503910963 |

### RINT

**RINT(numeric\_expr)**

Returns the value that is closest in value to the *numeric\_expr* argument and is equal to a mathematical integer.

Returns NULL if *numeric\_expr* evaluates to NULL.

output type  
`DOUBLE`

**Example**:

```
FIELDS_ADD(RINT(12.396));
```

| rint |
| --- |
| 12.0 |

### ROUND

**ROUND(numeric\_expr)**

Computes closest mathematical integer to *numeric\_expr* with ties rounding up.

Returns NULL if *numeric\_expr* evaluates to NULL.

output type  
`DOUBLE`

**Example**:

```
FIELDS_ADD(ROUND(12.396));
```

| round |
| --- |
| 12.0 |

**ROUND(numeric\_expr, decimalplaces)**

Computes closest mathematical integer to *numeric\_expr* with *decimalplaces* number of decimals.

Returns NULL if *numeric\_expr* evaluates to NULL.

output type  
`DOUBLE`

**Example**:

```
FIELDS_ADD(ROUND(12.436,2));
```

| round |
| --- |
| 12.44 |

### SCALB

**SCALB(*numeric\_expr1*, *scale\_factor*)**

Returns FLOAT fÃ2scale\_factor

Returns NULL if either of the arguments evaluates to NULL.

output type  
`DOUBLE`

**Example**:

```
FIELDS_ADD(SCALB(0.524f, 6));
```

| scalb |
| --- |
| 33.536 |

### SIGNUM

**SIGNUM(numeric\_expr)**

Returns result of signum function of argument:

* 0 if *numeric\_expr* is 0,
* 1.0 if *numeric\_expr* is greater than 0
* -1.0 if *numeric\_expr* is less than 0

Returns NULL if *numeric\_expr* evaluates to NULL.

output type  
`DOUBLE`

**Example**:

```
FIELDS_ADD(SIGNUM(28.71));
```

| signum |
| --- |
| 1.0 |

### SIN

**SIN(numeric\_expr)**

Computes the trigonometric sine of angle *numeric\_expr* (in radians).

Returns NULL if *numeric\_expr* evaluates to NULL.

output type  
`DOUBLE`

**Example**:

```
FIELDS_ADD(SIN(0.524));
```

| sin |
| --- |
| 0.5003474302699141 |

### SINH

**SINH(numeric\_expr)**

Computes the hyperbolic sine of *numeric\_expr*.

Returns NULL if *numeric\_expr* evaluates to NULL.

output type  
`DOUBLE`

**Example**:

```
FIELDS_ADD(SINH(0.524));
```

| sinh |
| --- |
| 0.5483110094354913 |

### SQRT

**SQRT(numeric\_expr)**

Computes the positive square root of *numeric\_expr*.

Returns NULL if *numeric\_expr* evaluates to NULL.

output type  
`DOUBLE`

**Example**:

```
FIELDS_ADD(SQRT(9.781));
```

| sqrt |
| --- |
| 3.127459032505462 |

### SUBMOD

**SUBMOD(numeric\_expr1, numeric\_expr2)**

Subtracts *numeric\_expr1* modulo *numeric\_expr2* from *numeric\_expr1*.

Returns NULL if either of the arguments evaluates to NULL.

output type  
the type of *numeric\_expr1*

**Example**:

```
FIELDS_ADD(SUBMOD(9.2, 4));
```

| submod |
| --- |
| 8.0 |

### SUBTRACT

**SUBTRACT(numeric\_expr1, numeric\_expr2)**

Arithmetic subtraction of *numeric\_expr2* from *numeric\_expr1*.

output type  
`LONG` when either of *numeric\_expr* is `INTEGER` or `LONG`

> `DOUBLE` when either of *numeric\_expr* is `DOUBLE`
>
> `IPADDR` when either of *numeric\_expr* is `IPADDR`
>
> `TIMESTAMP` when one of *numeric\_expr* is `TIMESTAMP` (see also
> timestamp expressions)

**Example**:

```
FIELDS_ADD(i, int_sub:SUBTRACT(i, 1),



d, double_sub:SUBTRACT(d,1),



ip, ipaddr_sub:SUBTRACT(ip, 1),



t, time_sub:SUBTRACT(t, 1000));
```

| i | int\_sub | d | double\_sub | ip | ipaddr\_sub | t | time\_sub |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 1 | 2.0 | 1.0 | 0.0.0.2 | 0.0.0.1 | 2019-09-19 07:17:39.034000000 +0000 | 2019-09-19 07:17:38.034000000 +0000 |
| 3 | 2 | 3.0 | 2.0 | 0.0.0.3 | 0.0.0.2 | 2019-09-19 07:17:39.035000000 +0000 | 2019-09-19 07:17:38.035000000 +0000 |

### TAN

**TAN(numeric\_expr)**

Computes the trigonometric tangent of angle *numeric\_expr* (in radians).

Returns NULL if *numeric\_expr* evaluates to NULL.

output type  
`DOUBLE`

**Example**:

```
FIELDS_ADD(TAN(1.524));
```

| tan |
| --- |
| 21.353597524589244 |

### TANH

**TANH(numeric\_expr)**

Computes the hyperbolic tangent of *numeric\_expr*.

Returns NULL if *numeric\_expr* evaluates to NULL.

output type  
`DOUBLE`

**Example**:

```
FIELDS_ADD(TANH(1.524));
```

| tanh |
| --- |
| 0.9093922044597188 |

### TOHEXSTRING

**TOHEXSTRING (numeric\_expr)**

Converts `INTEGER` or `LONG` *numeric\_expr* to hexadecimal string.

Returns NULL if *numeric\_expr* evaluates to NULL.

output type  
`STRING`

**Example**:

```
FIELDS_ADD(TOHEXSTRING(1000));
```

| tohexstring |
| --- |
| 3e8 |

### ULP

**ULP(numeric\_expr)**

Returns size of an ulp of the *numeric\_expr* argument.

Returns NULL if *numeric\_expr* evaluates to NULL.

output type  
`DOUBLE`

**Example**:

```
FIELDS_ADD(ULP(1.524f));
```

| ulp |
| --- |
| 1.1920929E-7 |

## Network

### DSLICE

**DSLICE(domain, level)**

Returns substring of *domain* containing labels up to the level specified.

Returns NULL if argument evaluates to NULL.

output type  
`STRING`

**Example**:

```
FIELDS_ADD(DSLICE('www.dynatrace.com',2));
```

| dslice |
| --- |
| dynatrace.com |

### IP\_TRUNC

**IP\_TRUNC(ip\_addr, prefix\_len)**

Returns an `IPADDR` where first *prefix\_len* bits are equal to those in *ip\_addr* and the remaining are set to 0.

Returns NULL if argument evaluates to NULL.

output type  
`IPADDR`

**Example**: retain first 24-bits of an IPv4 address

```
FIELDS_ADD(ipv4:IPADDR("192.168.100.100"), ipv6:IPADDR("2a00:1450:4010:c05::69"))



| FIELDS_ADD(ipv4_trunc:IP_TRUNC(ipv4, 24), ipv6_trunc:IP_TRUNC(ipv6, 24))
```

| ipv4 | ip4\_trunc | ipv6 | ip6\_trunc |
| --- | --- | --- | --- |
| 192.168.100.100 | 192.168.100.0 | 2a00:1450:4010:c05::69 | 2a00:1400::0 |

**IP\_TRUNC(ip\_addr, ipv4\_prefix\_len, ipv6\_prefix\_len)**

Returns an `IPADDR` where first *prefix\_len* bits are equal to those in *ip\_addr* and the remaining are set to 0. Allows to specify different
prefix lengths for IPv4 and IPv6 type addresses (*ipv4\_prefix\_len* and *ipv6\_prefix\_len* respectively).

Returns NULL if argument evaluates to NULL.

output type  
`IPADDR`

**Example**: retain first 24-bits of an IPv4 address

```
FIELDS_ADD(ipv4:IPADDR("192.168.100.100"), ipv6:IPADDR("2a00:1450:4010:c05::69"))



| FIELDS_ADD(ipv4_trunc:IP_TRUNC(ipv4, 24,96), ipv6_trunc:IP_TRUNC(ipv6, 24,96))
```

| ipv4 | ip4\_trunc | ipv6 | ip6\_trunc |
| --- | --- | --- | --- |
| 192.168.100.100 | 192.168.100.0 | 2a00:1450:4010:c05::69 | 2a00:1450:4010:c05::0 |

### IS\_IPV4

**IS\_IPV4(ip\_expr)**

Returns true if `IPADDR` contains IPv4 address, otherwise returns false.

Returns NULL if argument evaluates to NULL.

output type  
`BOOLEAN`

**Example**:

```
FIELDS_ADD(IS_IPV4(200.100.32.45:99));
```

| is\_ipv4 |
| --- |
| true |

### IS\_IPV6

**IS\_IPV6(ip\_expr)**

Returns true if `IPADDR` contains IPv6 address, otherwise returns false.

Returns NULL if argument evaluates to NULL.

output type  
`BOOLEAN`

**Example**:

```
FIELDS_ADD(IS_IPV6(IPADDR('2a00:1450:4010:c05::69')));
```

| is\_ipv6 |
| --- |
| true |

### PARSEURI

**PARSEURI(uri\_str)**

Returns array of URI elements parsed from `STRING` type argument.

Returns NULL if argument evaluates to NULL.

output type  
`TUPLE`

**Example**:

```
FIELDS_ADD(PARSEURI("https://docs.dynatrace.com:443/pages/dynatrace.html#sx-install"));
```

| parseuri |
| --- |
| {scheme="https" user=NULL host="docs.dynatrace.com" port=443 path="/pages/dynatrace.html" query=NULL fragment="sx-install"} |

## Strings

### Operators

**string\_expr1 + string\_expr2**

**string\_expr1 || string\_expr2**

Concatenates *string\_expr2* to *string\_expr1*.

output type  
`STRING`

```
FIELDS_ADD(s, s + "! Red fox jumps over lazy dog!");
```

| s | add |
| --- | --- |
| 0ho0 | 0ho0! Red fox jumps over lazy dog! |

### BASE16

**BASE16\_DECODE(string\_expr)**

**UNHEX(string\_expr)**

Returns base16 decoded *string\_expr*. Returns NULL if *string\_expr* evaluates to NULL.

output type  
`BYTES`

**Example**:

```
FIELDS_ADD(encoded:'48656c6c6f20576f726c6421')



| FIELDS_ADD(encoded, decoded_bytes:BASE16_DECODE(encoded))



| FIELDS_ADD(encoded, decoded_bytes, decoded_str:STRING(decoded_bytes));
```

| encoded | decoded\_bytes | decoded\_str |
| --- | --- | --- |
| 48656c6c6f20576f726c6421 | [72,101,108,108,111,32,87,111,114,108,100,33] | Hello World! |

**BASE16\_ENCODE(string\_expr)**

**HEX(string\_expr)**

Returns base16 encoded *string\_expr*. Returns NULL if *string\_expr* evaluates to NULL.

output type  
`STRING`

**Example**:

```
FIELDS_ADD(BASE16_ENCODE('Red fox jumps over brown dog'));
```

| base16\_encode |
| --- |
| 52656420666f78206a756d7073206f7665722062726f776e20646f67 |

**BASE16\_ENCODE(bytes)**

**HEX(bytes)**

Returns base16 encoded *bytes*. Returns NULL if *string\_expr* evaluates to NULL.

output type  
`STRING`

**Example**:

```
FIELDS_ADD(BASE16_ENCODE(BYTES([0,1,2])));
```

| base16\_encode |
| --- |
| 000102 |

### BASE64

**BASE64\_DECODE(string\_expr)**

**UNBASE64(string\_expr)**

**BASE64DECODE(string\_expr)**

Returns `BYTES` of base64 decoded *string\_expr*. Returns NULL if *string\_expr* evaluates to NULL.

output type  
`BYTES`

**Example**:

```
FIELDS_ADD(encoded:'SGVsbG8gV29ybGQh')



| FIELDS_ADD(encoded, decoded_bytes:BASE64_DECODE(encoded))



| FIELDS_ADD(encoded, decoded_bytes, decoded_str:STRING(decoded_bytes));
```

| encoded | decoded\_bytes | decoded\_str |
| --- | --- | --- |
| SGVsbG8gV29ybGQh | [72,101,108,108,111,32,87,111,114,108,100,33] | Hello World! |

**BASE64\_DECODE\_STRING(string\_expr)**

Returns `STRING` of base64 decoded *string\_expr*. Returns NULL if *string\_expr* evaluates to NULL.

output type  
`STRING`

**Example**:

```
FIELDS_ADD(encoded:'SGVsbG8gV29ybGQh')



| FIELDS_ADD(encoded, decoded_bytes:BASE64_DECODE(encoded), decoded_string:BASE64_DECODE_STRING(encoded))
```

| encoded | decoded\_bytes | decoded\_string |
| --- | --- | --- |
| SGVsbG8gV29ybGQh | [72,101,108,108,111,32,87,111,114,108,100,33] | Hello World! |

**BASE64\_ENCODE(string\_expr)**

**BASE64(string\_expr)**

**BASE64ENCODE(string\_expr)**

Returns base64 encoded *string\_expr*. Returns NULL if *string\_expr* evaluates to NULL.

output type  
`STRING`

**Example**:

```
FIELDS_ADD(BASE64_ENCODE('Hello World!'));
```

| base64\_encode |
| --- |
| SGVsbG8gV29ybGQh |

### CONCAT

**CONCAT(string\_expr, â¦ )**

Concatenates *expr* arguments and returns resulting string. Max number of arguments is 128.

output type  
`STRING`

**Example**:

```
FIELDS_ADD(CONCAT('my ', '20 ', '$cents'));
```

| concat |
| --- |
| my 20 $cents |

### CHARAT

**CHARAT(string, pos)**

Returns character at *pos* in the *string*.

Returns NULL if *string* evaluates to NULL or if *pos* points beyond the length of *string*.

output type  
`STRING`

**Example**:

```
FIELDS_ADD(CHARAT("foo",0));
```

| charat |
| --- |
| f |

### CONTAINS

**CONTAINS(string1, string2)**

Returns true if *string1* contains *string2*. Otherwise returns false.

Returns NULL if either of the arguments evaluates to NULL.

Note

Comparison is case sensitive.

output type  
`BOOLEAN`

**Example**:

```
FIELDS_ADD(s, CONTAINS(s, "0"));
```

| s | contains |
| --- | --- |
| 0ho0 | true |
| 1ho1 | false |

### ENDS

**ENDS(string\_expr1, string\_expr2)**

Returns true if *string\_expr1* ends with *string\_expr2*. Otherwise returns false.

Returns NULL if either of the arguments evaluates to NULL.

Note

Comparison is case sensitive.

output type  
`BOOLEAN`

**Example**:

```
FIELDS_ADD(s, ENDS(s, "0"));
```

| s | contains |
| --- | --- |
| 0ho0 | true |
| 1ho1 | false |

### INDEXOF

**INDEXOF(str, substr, start\_pos)**

Returns the index within *str* of the first occurrence of the specified *substr*, starting at position start\_pos. If start\_pos is negative the search is done backward from the start\_pos. If not found then -1 is returned.

The start\_pos is counted from 0.

output type  
`INTEGER`

**Example**:

```
FIELDS_ADD(s, INDEXOF(s,"h",0));
```

| s | indexof |
| --- | --- |
| 0ho0 | 1 |

### LDIST

**LDIST(string\_expr1, string\_expr2)**

Computes [Levenshtein distanceï»¿](https://en.wikipedia.org/wiki/Levenshtein_distance) between *string\_expr1* and *string\_expr2*.

output type  
`INTEGER`

**Example**:

```
FIELDS_ADD(s1:s, s2:'0ho1') | FIELDS_ADD(s1, s2, LDIST(s1, s2));
```

| s | indexof |
| --- | --- |
| 0ho0 | 1 |

### LOWER

**LOWER(string)**

Converts *string* to lowercase and returns resulting string.

output type  
`STRING`

**Example**:

```
FIELDS_ADD(LOWER('HeLlo WorlD'));
```

| lower |
| --- |
| hello world |

### MATCHES

**MATCHES(string, pattern\_expression)**

Returns true if pattern expression matches *string*. Otherwise returns false.

output type  
`BOOLEAN`

**Example**:

```
FIELDS_ADD(MATCHES('hello world', "ALNUM SPACE ALNUM"))
```

| matches |
| --- |
| true |

### PARSE

**PARSE(string,pattern)**

Returns extracted fields of first match of the *pattern* in the *string*.

output type

> 1. in case the pattern does not contain any exported matchers then it returns `BOOLEAN`, indicating success or failure of parsing.
> 2. in case the pattern contains only one exported matcher then it returns matched value as a single value
> 3. in case the pattern contains more than one exported matcher then it returns matched values as `TUPLE`

**Example**:

```
FIELDS_ADD(strings: "1 out of 10; 2 out of 10; 3 out of 10")



| FIELDS_ADD(PARSE(strings, "INT:prefix LD:string INT:suffix"))
```

| strings | parse |
| --- | --- |
| 1 out of 10; 2 out of 10; 3 out of 10 | {prefix=1 string=" out of " suffix=10} |

### PRINTF

**PRINTF(format, argsâ¦)**

Returns a formatted string using *format* string (based on [java.util.Formatter classï»¿](https://docs.oracle.com/javase/8/docs/api/java/util/Formatter.html)) and arguments.

output type  
`STRING`

**Example**:

```
FIELDS_ADD(PRINTF("Result: %010x string: %s double: %2.2e", i, s, d*10000));
```

| printf |
| --- |
| Result: 0000000000 string: 0ho0 double: 0.00e+00 |
| Result: 0000000001 string: 1ho1 double: 1.00e+04 |
| Result: 0000000002 string: 2ho2 double: 2.00e+04 |

### PUNCT

**PUNCT(string\_expr)**

Returns punctuation characters contained in *string\_expr*.

**PUNCT(string\_expr, count, withSpace)**

Returns the first `punctuation characters <posix-character-classes>` (amount can be specified by the *count* parameter) from the string (specified by the *string\_expr* parameter) either with or without spaces (specified by the *withSpace* parameter).

Boolean *withSpace* includes space character (ASCII 0x20 hex) in search, and is printed out as underscore (ASCII 0x5F hex).

output type  
`STRING`

**Example**:

```
FIELDS_ADD(str:"Hi I'm home!") | FIELDS_ADD(PUNCT(str));
```

| punct |
| --- |
| '! |

### REPLACE\_STRING

**REPLACE\_STRING(string, target\_str, replace\_str)**

Replaces each substring of *string* that matches the *target\_str* with the *replace\_str*.

output type  
`STRING`

**Example**:

```
FIELDS_ADD(REPLACE_STRING('hello world', 'world', 'space'));
```

| REPLACE\_STRING |
| --- |
| hello space |

### REPLACE\_PATTERN

**REPLACE\_PATTERN(string, pattern\_expression, replacement\_template\_str)**

Replaces each substring of *string* that matches the pattern *pattern\_expression* with the *replacement\_template\_str*.

output type  
`STRING`

**Example**:

```
FIELDS_ADD(REPLACE_PATTERN("aaa bbb ccc", "'a'+ SPACE 'b'+", "xxx"))
```

| replace\_pattern |
| --- |
| xxx ccc |

**Example**:

```
FIELDS_ADD(REPLACE_PATTERN("label=valueA label=valueB", "'label=' NSPACE:exportedGroup", "modifiedLabel='modified ${exportedGroup}'"))
```

| replace\_pattern |
| --- |
| modifiedLabel='modified valueA' modifiedLabel='modified valueB' |

### SH\_ENTROPY

**SH\_ENTROPY(string\_expr)**

Computes [Shannon entropyï»¿](https://en.wiktionary.org/wiki/Shannon_entropy) of *string\_expr*

output type  
`DOUBLE`

**Example**:

```
FIELDS_ADD(SH_ENTROPY("Hello world!"));
```

| sh\_entropy |
| --- |
| 3.0220552088742005 |

### SPLIT

**SPLIT(string, pattern\_expression)**

Splits *string* around matches of given pattern and returns result as ARRAY of strings.

output type  
ARRAY

**Example**:

```
FIELDS_ADD(SPLIT('p1;p2;p3', "';'"))
```

| split |
| --- |
| [p1, p2, p3] |

### STRLEN

**STRLEN(string)**

Returns length of *string*.

output type  
`INTEGER`

**Example**:

```
FIELDS_ADD(STRLEN('hello world'));
```

| strlen |
| --- |
| 11 |

### STARTS

**STARTS(string1, string2)**

Returns true if *string1* starts with *string2*. Otherwise returns false.

Note

Comparison is case sensitive.

output type  
`BOOLEAN`

**Example**:

```
FIELDS_ADD(STARTS('Hello World!', 'Hell'));
```

| starts |
| --- |
| true |

### SUBSTR

**SUBSTR(string, startPos)**

Takes substring of *string* from position *startPos* to the end of *string*. If *startPos* is negative, then the substring is taken from the position relative to the end of *string*.

output type  
`STRING`

**Example**:

```
FIELDS_ADD(SUBSTR('hello world', 6));
```

| substr |
| --- |
| world |

**SUBSTR(string, startPos, endPos)**

Takes substring of *str* from position *startPos* to position *endPos*. Position is counted from 0 (i.e first element is at position 0). If
*startPos* is negative, then substring is taken from position relative to the end of string. If *endPos* is negative, then substring is taken
until position relative to the end of string.

output type  
`STRING`

**Example**:

```
FIELDS_ADD(SUBSTR('my 20 $cents', 3,5));
```

| substr |
| --- |
| 20 |

### TRIM

**TRIM(string)**

Removes leading and trailing whitespaces from *string*.

output type  
`STRING`

**Example**:

```
FIELDS_ADD(str:'  hello world         ') | FIELDS_ADD(str, TRIM(str));
```

| str | trim |
| --- | --- |
| hello world | hello world |

### UNESCAPE

**UNESCAPE(string)**

DEESCAPE(string)

Removes escaping from *string*.

output type  
`STRING`

**Example**:

```
FIELDS_ADD(UNESCAPE("\""));
```

| unescape |
| --- |
| " |

### URLDECODE

**URLDECODE(string)**

Returns [urldecodedï»¿](https://en.wikipedia.org/wiki/Percent-encoding) (also known as percent-encoding/decoding) *string*.

output type  
`STRING`

**Example**:

```
FIELDS_ADD(URLDECODE("Hello+world%21"));
```

| urldecode |
| --- |
| Hello world! |

### URLENCODE

**URLENCODE(string)**

Returns url-encoded *string*

output type  
`STRING`

**Example**:

```
FIELDS_ADD(URLENCODE("Hello world!"));
```

| urlencode |
| --- |
| Hello+world%21 |

### HTMLUNESCAPE

HTMLUNESCAPE(*string*)  
Unescapes HTML *string*

output type  
`STRING`

**Example**:

```
FIELDS_ADD(HTMLUNESCAPE("&lt;Fran&ccedil;ais&gt;"));
```

| htmlunescape |
| --- |
| <FranÃ§ais> |

### UPPER

**UPPER(string)**

Converts *string* to uppercase.

output type  
`STRING`

**Example**:

```
FIELDS_ADD(UPPER('HeLlo WorlD'));
```

| upper |
| --- |
| HELLO WORLD |

## Other

### COALESCE

**COALESCE(expr1, expr2, exprN)**

Evaluates input expressions from left to right and returns the first non-null expression.

output type  
the common type of arguments, if arguments are of the same type, otherwise VARIANT.

**Example**:

```
FIELDS_ADD(a:string(), b: 'b', c:'c')



| FIELDS_ADD(COALESCE(a, b, c))
```

| a | b | c | coalesce |
| --- | --- | --- | --- |
| NULL | b | c | b |

### COLUMN

**COLUMN(string\_expr)**

Selects column by name *string\_expr*. This function can be used when arguments are evaluated dynamically at runtime.
output type  
the type of the column selected.

**Example**:

```
FIELDS_ADD(ip_addr:COLUMN('ip'));
```

### FLAG

**FLAG(country\_code)**

Returns Unicode flag symbol of ISO 3166 *country\_code*.

output type  
`STRING`

**Example**

```
FIELDS_ADD(country:'Estonia', flag:FLAG('EE'));
```

| country | flag |
| --- | --- |
| Estonia | ðªðª |

### HASH64

**HASH64(arg)**

Computes 64-bit digest value of argument.

Note

The algorithm is not cryptographically secure.

output type  
`LONG`

**Example**

```
FIELDS_ADD(s, hash64:HASH64(s));
```

| s | hash64 |
| --- | --- |
| 0ho0 | -1180816457071597385 |

### REMOVE\_CHILD

**REMOVE\_CHILD(var\_obj, keys â¦)**

Removes selected members (specified by one or more *keys*) from VARIANT\_OBJECT type argument *var\_obj*.

output type  
`VARIANT_OBJECT`

**Example**: remove members *t* and *s* from a variant object:

```
FIELDS_ADD(vo:VARIANT_OBJECT({i,t,s}))



| FIELDS_ADD(REMOVE_CHILD(vo, "t", "s"))
```

| vo | remove\_child |
| --- | --- |
| {"i":0,"t":"2020-11-12 18:15:09.544000000 +0200","s":"0ho0"} | {"i":0} |

### SIZE

**SIZE(arg)**

Returns the number of elements in `ARRAY`, `TUPLE`, `VARIANT_ARRAY`, `VARIANT_OBJECT` or `BYTES` argument.

output type  
`INTEGER`

**Example**:

```
FIELDS_ADD(array, array_size:SIZE(array));
```

| array | array\_size |
| --- | --- |
| [] | 0 |
| [0.0.0.1] | 1 |
| [0.0.0.2, 0.0.0.3] | 2 |
| [0.0.0.3, 0.0.0.4, 0.0.0.5] | 3 |
| [0.0.0.4, 0.0.0.5, 0.0.0.6, 0.0.0.7] | 4 |

### SIZEOF

**SIZEOF(arg)**

Returns the argument size in bytes.

output type  
`LONG`

**Example**:

```
FIELDS_ADD(int:i, sizeof_int:SIZEOF(i), tuple, sizeof_tuple:SIZEOF(tuple));
```

| int | sizeof\_int | tuple | sizeof\_tuple |
| --- | --- | --- | --- |
| 0 | 4 | {i=0 ip=0.0.0.0 ip6=0.0.0.0 s="0ho0" t="0ho0" ips=[] ip6s=[]} | 63 |

### TYPE

**TYPE(arg)**

Returns the string identifying data type of the argument.

output type  
`STRING`

**Example**:

```
FIELDS_ADD(int_t:TYPE(i),i, time_t:TYPE(t),t, type_array:TYPE(array),array);
```

| int\_t | i | time\_t | t | type\_array | array |
| --- | --- | --- | --- | --- | --- |
| INTEGER | 0 | TIMESTAMP | 2019-09-23 10:20:43.278 +0000 | ARRAY | [] |

## Related topics

* [Log processing examples (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples "Example log processing scenarios.")