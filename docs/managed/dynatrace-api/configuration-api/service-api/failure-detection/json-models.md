---
title: Failure detection API - JSON models
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/failure-detection/json-models
---

# Failure detection API - JSON models

# Failure detection API - JSON models

* Reference
* Published Jan 11, 2021

JSON models of the **Failure detection rules** API vary greatly, depending on the **type** of some objects. Here you can find JSON models for each variation.

## Variations of the `FdpTagPredicate` object

The `FdpTagPredicate` object is the base of tag conditions for failure detection parameter sets. The actual set of fields depends on the **type** of the condition.

### STRING\_EQUALS

FdpTagStringEquals

Parameters

JSON model

#### The `FdpTagStringStartsWith` object

The predicate of the `STRING_STARTS_WITH` type. It checks whether the tag (which is a string) starts with the reference value.

| Element | Type | Description |
| --- | --- | --- |
| ignoreCase | boolean | - |
| negated | boolean | - |
| value | string | The reference value. The condition is fulfilled when the tag (which is a string) starts with this value. |

```
{



"type": "STRING_STARTS_WITH",



"ignoreCase": true,



"values": "reference value"



}
```

### STRING\_STARTS\_WITH

FdpTagStringStartsWith

Parameters

JSON model

#### The `FdpTagStringEquals` object

The predicate of the `STRING_EQUALS` type. It checks whether the tag (which is a string) equals the reference value.

| Element | Type | Description |
| --- | --- | --- |
| ignoreCase | boolean | - |
| negated | boolean | - |
| value | string | The reference value. The condition is fulfilled when the tag (which is a string) equals this value. |

```
{



"type": "STRING_EQUALS",



"ignoreCase": true,



"values": "reference value"



}
```

### STRING\_ENDS\_WITH

FdpTagStringEndsWith

Parameters

JSON model

#### The `FdpTagStringEndsWith` object

The predicate of the `STRING_ENDS_WITH` type. It checks whether the tag (which is a string) ends with the reference value.

| Element | Type | Description |
| --- | --- | --- |
| ignoreCase | boolean | - |
| negated | boolean | - |
| value | string | The reference value. The condition is fulfilled when the tag (which is a string) ends with this value. |

```
{



"type": "STRING_ENDS_WITH",



"ignoreCase": true,



"values": "reference value"



}
```

### STRING\_CONTAINS\_SUBSTRING

FdpTagStringContainsSubstring

Parameters

JSON model

#### The `FdpTagStringContainsSubstring` object

The predicate of the `STRING_CONTAINS_SUBSTRING` type. It checks whether the tag (which is a string) contains the reference value.

| Element | Type | Description |
| --- | --- | --- |
| ignoreCase | boolean | - |
| negated | boolean | - |
| value | string | The reference value. The condition is fulfilled when the tag (which is a string) contains this value. |

```
{



"type": "STRING_CONTAINS_SUBSTRING",



"ignoreCase": true,



"values": "reference value"



}
```

### INTEGER\_EQUALS

FdpTagIntegerEquals

Parameters

JSON model

#### The `FdpTagIntegerEquals` object

The predicate of the `INTEGER_EQUALS` type. It checks whether the tag (which is an integer) equals the reference value.

| Element | Type | Description |
| --- | --- | --- |
| negated | boolean | - |
| value | string | The reference value. |

```
{



"type": "INTEGER_EQUALS",



"values": 10



}
```

### INTEGER\_LESS\_THAN

FdpTagIntegerLessThan

Parameters

JSON model

#### The `FdpTagIntegerLessThan` object

The predicate of the `INTEGER_LESS_THAN` type. It checks whether the tag (which is an integer) is less than the reference value.

| Element | Type | Description |
| --- | --- | --- |
| value | string | The reference value. |

```
{



"type": "INTEGER_LESS_THAN",



"values": 10



}
```

### INTEGER\_LESS\_THAN\_OR\_EQUAL

FdpTagIntegerLessThanOrEqual

Parameters

JSON model

#### The `FdpTagIntegerLessThanOrEqual` object

The predicate of the `INTEGER_LESS_THAN_OR_EQUAL` type. It checks whether the tag (which is an integer) is less than or equals the reference value.

| Element | Type | Description |
| --- | --- | --- |
| value | string | The reference value. |

```
{



"type": "INTEGER_LESS_THAN_OR_EQUAL",



"values": 10



}
```

### INTEGER\_GREATER\_THAN

FdpTagIntegerGreaterThan

Parameters

JSON model

#### The `FdpTagIntegerGreaterThan` object

The predicate of the `INTEGER_GREATER_THAN` type. It checks whether the tag (which is an integer) is greater than the reference value.

| Element | Type | Description |
| --- | --- | --- |
| value | string | The reference value. |

```
{



"type": "INTEGER_GREATER_THAN",



"values": 10



}
```

### INTEGER\_GREATER\_THAN\_OR\_EQUAL

FdpTagIntegerGreaterThanOrEqual

Parameters

JSON model

#### The `FdpTagIntegerGreaterThanOrEqual` object

The predicate of the `INTEGER_GREATER_THAN_OR_EQUAL` type. It checks whether the tag (which is an integer) is greater than or equals the reference value.

| Element | Type | Description |
| --- | --- | --- |
| value | string | The reference value. |

```
{



"type": "INTEGER_GREATER_THAN_OR_EQUAL",



"values": 10



}
```

### DOUBLE\_EQUALS

FdpTagDoubleEquals

Parameters

JSON model

#### The `FdpTagDoubleEquals` object

The predicate of the `DOUBLE_EQUALS` type. It checks whether the tag (which is a double) equals the reference value.

| Element | Type | Description |
| --- | --- | --- |
| negated | boolean | - |
| value | number | The reference value. |

```
{



"type": "DOUBLE_EQUALS",



"values": 10



}
```

### DOUBLE\_LESS\_THAN

FdpTagDoubleLessThan

Parameters

JSON model

#### The `FdpTagDoubleLessThan` object

The predicate of the `DOUBLE_LESS_THAN` type. It checks whether the tag (which is a double) is less than the reference value.

| Element | Type | Description |
| --- | --- | --- |
| value | number | The reference value. |

```
{



"type": "DOUBLE_LESS_THAN",



"values": 10



}
```

### DOUBLE\_LESS\_THAN\_OR\_EQUAL

FdpTagDoubleLessThanOrEqual

Parameters

JSON model

#### The `FdpTagDoubleLessThanOrEqual` object

The predicate of the `DOUBLE_LESS_THAN_OR_EQUAL` type. It checks whether the tag (which is a double) is less than or equals the reference value.

| Element | Type | Description |
| --- | --- | --- |
| value | number | The reference value. |

```
{



"type": "DOUBLE_LESS_THAN_OR_EQUAL",



"values": 10



}
```

### DOUBLE\_GREATER\_THAN

FdpTagDoubleGreaterThan

Parameters

JSON model

#### The `FdpTagDoubleGreaterThan` object

The predicate of the `DOUBLE_GREATER_THAN` type. It checks whether the tag (which is a double) is greater than the reference value.

| Element | Type | Description |
| --- | --- | --- |
| value | number | The reference value. |

```
{



"type": "DOUBLE_GREATER_THAN",



"values": 10



}
```

### DOUBLE\_GREATER\_THAN\_OR\_EQUAL

FdpTagDoubleGreaterThanOrEqual

Parameters

JSON model

#### The `FdpTagDoubleGreaterThanOrEqual` object

The predicate of the `DOUBLE_GREATER_THAN_OR_EQUAL` type. It checks whether the tag (which is a double) is greater than or equals the reference value.

| Element | Type | Description |
| --- | --- | --- |
| value | number | The reference value. |

```
{



"type": "DOUBLE_GREATER_THAN_OR_EQUAL",



"values": 10



}
```

## Variations of the `FdcPredicate` object

The `FdcPredicate` object is the base for predicates of a failure detection rule's condition. The actual set of fields depends on the **type** of the condition.

### STRING\_EQUALS

FdcPredicateStringEquals

Parameters

JSON model

#### The `FdcPredicateStringEquals` object

The predicate of the `STRING_EQUALS` type. It checks whether the attribute (which is a string) equals one of the reference values.

| Element | Type | Description |
| --- | --- | --- |
| ignoreCase | boolean | The condition is case sensitive (`false`) or case insensitive (`true`).  If not set, then `false` is used, making the condition case sensitive. |
| values | string[] | A list of reference values. The condition is fulfilled when the attribute (which is a string) equals *any* of these. |

```
{



"type": "STRING_EQUALS",



"ignoreCase": true,



"values": [



"value1",



"value2"



]



}
```

### STRING\_STARTS\_WITH

FdcPredicateStringStartsWith

Parameters

JSON model

#### The `FdcPredicateStringStartsWith` object

The predicate of the `STRING_STARTS_WITH` type. It checks whether the attribute (which is a string) starts with one of the reference values.

| Element | Type | Description |
| --- | --- | --- |
| ignoreCase | boolean | The condition is case sensitive (`false`) or case insensitive (`true`).  If not set, then `false` is used, making the condition case sensitive. |
| values | string[] | A list of reference values. The condition is fulfilled when the attribute (which is a string) start with *any* of these. |

```
{



"type": "STRING_STARTS_WITH",



"ignoreCase": true,



"values": [



"value1",



"value2"



]



}
```

### STRING\_ENDS\_WITH

FdcPredicateStringEndsWith

Parameters

JSON model

#### The `FdcPredicateStringEndsWith` object

The predicate of the `STRING_ENDS_WITH`  type. It checks whether the attribute (which is a string) ends with one of the reference values.

| Element | Type | Description |
| --- | --- | --- |
| ignoreCase | boolean | The condition is case sensitive (`false`) or case insensitive (`true`).  If not set, then `false` is used, making the condition case sensitive. |
| values | string[] | A list of reference values. The condition is fulfilled when the attribute (which is a string) ends with *any* of these. |

```
{



"type": "STRING_ENDS_WITH",



"ignoreCase": true,



"values": [



"value1",



"value2"



]



}
```

### STRING\_CONTAINS\_SUBSTRING

FdcPredicateStringContains

Parameters

JSON model

#### The `FdcPredicateStringContains` object

The predicate of the `STRING_CONTAINS_SUBSTRING` type. It checks whether the attribute (which is a string) contains one of the reference values.

| Element | Type | Description |
| --- | --- | --- |
| ignoreCase | boolean | The condition is case sensitive (`false`) or case insensitive (`true`).  If not set, then `false` is used, making the condition case sensitive. |
| values | string[] | A list of reference values. The condition is fulfilled when the attribute (which is a string) contains *any* of these. |

```
{



"type": "STRING_CONTAINS_SUBSTRING",



"ignoreCase": true,



"values": [



"value1",



"value2"



]



}
```

### INTEGER\_EQUALS

FdcPredicateIntegerEquals

Parameters

JSON model

#### The `FdcPredicateIntegerEquals` object

The predicate of the `INTEGER_EQUALS` type. It checks whether the attribute (which is an integer) equals one of the reference values.

| Element | Type | Description |
| --- | --- | --- |
| values | integer[] | The reference value. The condition is fulfilled when the attribute (which is an integer) equals *any* of these. |

```
{



"type": "INTEGER_EQUALS",



"values": [



10,



20



]



}
```

### INTEGER\_LESS\_THAN

FdcPredicateIntegerLessThan

Parameters

JSON model

#### The `FdcPredicateIntegerLessThan` object

The predicate of the `INTEGER_LESS_THAN` type. It checks whether the attribute (which is an integer) is less than the reference value.

| Element | Type | Description |
| --- | --- | --- |
| value | integer | The reference value. The condition is fulfilled when the attribute (which is an integer) is less than this value. |

```
{



"type": "INTEGER_LESS_THAN",



"value": 10



}
```

### INTEGER\_LESS\_THAN\_OR\_EQUAL

FdcPredicateIntegerLessThanOrEqual

Parameters

JSON model

#### The `FdcPredicateIntegerLessThanOrEqual` object

The predicate of the `INTEGER_LESS_THAN_OR_EQUAL` type. It checks whether the attribute (which is an integer) is less than or equals the reference value.

| Element | Type | Description |
| --- | --- | --- |
| value | integer | The reference value. The condition is fulfilled when the attribute (which is an integer) is less than or equals this value. |

```
{



"type": "INTEGER_LESS_THAN_OR_EQUAL",



"value": 10



}
```

### INTEGER\_GREATER\_THAN

FdcPredicateIntegerGreaterThan

Parameters

JSON model

#### The `FdcPredicateIntegerGreaterThan` object

The predicate of the `INTEGER_GREATER_THAN` type. It checks whether the attribute (which is an integer) is greater than the reference value.

| Element | Type | Description |
| --- | --- | --- |
| value | integer | The reference value. The condition is fulfilled when the attribute (which is an integer) is greater than this value. |

```
{



"type": "INTEGER_GREATER_THAN",



"value": 10



}
```

### INTEGER\_GREATER\_THAN\_OR\_EQUAL

FdcPredicateIntegerGreaterThanOrEqual

Parameters

JSON model

#### The `FdcPredicateIntegerGreaterThanOrEqual` object

The predicate of the `INTEGER_GREATER_THAN_OR_EQUAL` type. It checks whether the attribute (which is an integer) is greater than or equals the reference value.

| Element | Type | Description |
| --- | --- | --- |
| value | integer | The reference value. The condition is fulfilled when the attribute (which is an integer) is greater than or equals this value. |

```
{



"type": "INTEGER_GREATER_THAN_OR_EQUAL",



"value": 10



}
```

### LONG\_EQUALS

FdcPredicateLongEquals

Parameters

JSON model

#### The `FdcPredicateLongEquals` object

The predicate of the `LONG_EQUALS` type. It checks whether the attribute (which is a long) equals one of the reference values.

| Element | Type | Description |
| --- | --- | --- |
| values | string[] | A list of reference values. The condition is fulfilled when the attribute (which is a long) equals *any* of these. |

```
{



"type": "LONG_EQUALS",



"values": [



10,



20



]



}
```

### LONG\_LESS\_THAN

FdcPredicateLongLessThan

Parameters

JSON model

#### The `FdcPredicateLongLessThan` object

The predicate of the `LONG_LESS_THAN` type. It checks whether the attribute (which is a long) is less than the reference value.

| Element | Type | Description |
| --- | --- | --- |
| value | string | The reference value. The condition is fulfilled when the attribute (which is a long) is less than this value. |

```
{



"type": "LONG_LESS_THAN",



"value": 20



}
```

### LONG\_LESS\_THAN\_OR\_EQUAL

FdcPredicateLongLessThanOrEqual

Parameters

JSON model

#### The `FdcPredicateLongLessThanOrEqual` object

The predicate of the `LONG_LESS_THAN_OR_EQUAL` type. It checks whether the attribute (which is a long) is less than or equals the reference value.

| Element | Type | Description |
| --- | --- | --- |
| value | string | The reference value. The condition is fulfilled when the attribute (which is a long) is less than or equals this value. |

```
{



"type": "LONG_LESS_THAN_OR_EQUAL",



"value": 20



}
```

### LONG\_GREATER\_THAN

FdcPredicateLongGreaterThan

Parameters

JSON model

#### The `FdcPredicateLongGreaterThan` object

The predicate of the `LONG_GREATER_THAN` type. It checks whether the attribute (which is a long) is greater than the reference value.

| Element | Type | Description |
| --- | --- | --- |
| value | string | The reference value. The condition is fulfilled when the attribute (which is a long) is greater than this value. |

```
{



"type": "LONG_GREATER_THAN",



"value": 20



}
```

### LONG\_GREATER\_THAN\_OR\_EQUAL

FdcPredicateLongGreaterThanOrEqual

Parameters

JSON model

#### The `FdcPredicateLongGreaterThanOrEqual` object

The predicate of the `LONG_GREATER_THAN_OR_EQUAL` type. It checks whether the attribute (which is a long) is greater than or equals the reference value.

| Element | Type | Description |
| --- | --- | --- |
| value | string | The reference value. The condition is fulfilled when the attribute (which is a long) is greater than or equals this value. |

```
{



"type": "LONG_GREATER_THAN_OR_EQUAL",



"value": 20



}
```

### TAG\_KEY\_EQUALS

FdcPredicateTagKeyEquals

Parameters

JSON model

#### The `FdcPredicateTagKeyEquals` object

The predicate of the `TAG_KEY_EQUALS` type. It checks whether the attribute (which is the key of a tag) equals one of the reference values.

| Element | Type | Description |
| --- | --- | --- |
| keys | string[] | A list of reference values. The condition is fulfilled when the attribute (which is the key of a tag) equals *any* of these. |

```
{



"type": "TAG_KEY_EQUALS",



"keys": [



"key1",



"key2"



]



}
```

### TAG\_EQUALS

FdcPredicateTagEquals

Parameters

JSON model

#### The `FdcPredicateTagEquals` object

The predicate of the `TAG_EQUALS` type. It checks whether the attribute (which is a key:value pair) equals one of the reference values.

The reference value is a key:value pair, consisting of a key and a value that are at the **same position** in the respective list.

| Element | Type | Description |
| --- | --- | --- |
| keys | string[] | A list of reference tag keys.  The condition is fulfilled when the tag matches *any* key:value pair, consisting of a key and a value that are at the **same position** in the respective list. |
| values | string[] | A list of reference tag values.  The condition is fulfilled when the tag matches *any* key:value pair, consisting of a key and a value that are at the **same position** in the respective list. |

```
{



"type": "TAG_EQUALS",



"keys": [



"key1",



"key2"



],



"value": [



"value1",



"value2"



]



}
```

### SERVICE\_TYPE\_EQUALS

FdcPredicateServiceTypeEquals

Parameters

JSON model

#### The `FdcPredicateServiceTypeEquals` object

The predicate of the `SERVICE_TYPE_EQUALS` type. It checks whether the attribute (which is the type of the service) equals one of the reference values.

| Element | Type | Description |
| --- | --- | --- |
| values | string[] | A list of reference values. The condition is fulfilled when the attribute (which is the type of the service) equals *any* of these.The possible values are: WebRequest, WebService, Database, Method, WebSite, Messaging, Mobile, Process, Rmi, External, QueueListener, QueueInteraction, RemoteCall, SaasVendor, CustomApplication, Cics, Ims, CicsInteraction, ImsInteraction, EnterpriseServiceBus, ZosConnect. |

```
{



"type": "SERVICE_TYPE_EQUALS",



"values": [



"value1",



"value2"



]



}
```

### MANAGEMENT\_ZONES\_CONTAINS\_ALL

FdcPredicateManagementZonesContainsAll

Parameters

JSON model

#### The `FdcPredicateManagementZonesContainsAll` object

The predicate of the `MANAGEMENT_ZONES_CONTAINS_ALL` type. It checks whether the attribute (which is a set of management zones) contains **all** the reference values.

| Element | Type | Description |
| --- | --- | --- |
| values | string[] | A list of reference values. The condition is fulfilled when the attribute (which is a set of management zones) contains **all** the reference values.  Specify the ID or the name of the management zone here. |

```
{



"type": "MANAGEMENT_ZONES_CONTAINS_ALL",



"values": [



"management zone 1",



"management zone 2"



]



}
```

### SET\_OF\_INTEGERS\_CONTAINS\_ANY

FdcPredicateSetOfIntegersContainsAny

Parameters

JSON model

#### The `FdcPredicateLongLessThan` object

The predicate of the `LONG_LESS_THAN` type. It checks whether the attribute (which is a long) is less than the reference value.

| Element | Type | Description |
| --- | --- | --- |
| value | string | The reference value. The condition is fulfilled when the attribute (which is a long) is less than this value. |

```
{



"type": "SET_OF_INTEGERS_CONTAINS_ANY",



"values": [



10,



20



]



}
```

### SET\_OF\_INTEGERS\_CONTAINS\_ALL

FdcPredicateSetOfIntegersContainsAll

Parameters

JSON model

#### The `FdcPredicateLongLessThan` object

The predicate of the `LONG_LESS_THAN` type. It checks whether the attribute (which is a long) is less than the reference value.

| Element | Type | Description |
| --- | --- | --- |
| value | string | The reference value. The condition is fulfilled when the attribute (which is a long) is less than this value. |

```
{



"type": "SET_OF_INTEGERS_CONTAINS_ALL",



"values": [



10,



20



]



}
```