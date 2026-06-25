---
title: Failure detection API - JSON models
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/failure-detection/json-models
scraped: 2026-05-12T12:02:27.166760
---

# Failure detection API - JSON models

# Failure detection API - JSON models

* Reference
* Published Jan 11, 2021

JSON-модели API **Failure detection rules** сильно различаются в зависимости от поля **type** некоторых объектов. JSON-модели для каждой вариации перечислены ниже.

## Вариации объекта `FdpTagPredicate`

Объект `FdpTagPredicate` является базовым для условий по тегам в наборах параметров обнаружения сбоев. Фактический набор полей зависит от поля **type** условия.

### STRING\_EQUALS

FdpTagStringEquals

Parameters

JSON model

#### Объект `FdpTagStringStartsWith`

Предикат типа `STRING_STARTS_WITH`. Он проверяет, начинается ли тег (являющийся строкой) с эталонного значения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| ignoreCase | boolean | - |
| negated | boolean | - |
| value | string | Эталонное значение. Условие выполняется, когда тег (являющийся строкой) начинается с этого значения. |

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

#### Объект `FdpTagStringEquals`

Предикат типа `STRING_EQUALS`. Он проверяет, равен ли тег (являющийся строкой) эталонному значению.

| Элемент | Тип | Описание |
| --- | --- | --- |
| ignoreCase | boolean | - |
| negated | boolean | - |
| value | string | Эталонное значение. Условие выполняется, когда тег (являющийся строкой) равен этому значению. |

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

#### Объект `FdpTagStringEndsWith`

Предикат типа `STRING_ENDS_WITH`. Он проверяет, заканчивается ли тег (являющийся строкой) эталонным значением.

| Элемент | Тип | Описание |
| --- | --- | --- |
| ignoreCase | boolean | - |
| negated | boolean | - |
| value | string | Эталонное значение. Условие выполняется, когда тег (являющийся строкой) заканчивается этим значением. |

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

#### Объект `FdpTagStringContainsSubstring`

Предикат типа `STRING_CONTAINS_SUBSTRING`. Он проверяет, содержит ли тег (являющийся строкой) эталонное значение.

| Элемент | Тип | Описание |
| --- | --- | --- |
| ignoreCase | boolean | - |
| negated | boolean | - |
| value | string | Эталонное значение. Условие выполняется, когда тег (являющийся строкой) содержит это значение. |

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

#### Объект `FdpTagIntegerEquals`

Предикат типа `INTEGER_EQUALS`. Он проверяет, равен ли тег (являющийся целым числом) эталонному значению.

| Элемент | Тип | Описание |
| --- | --- | --- |
| negated | boolean | - |
| value | string | Эталонное значение. |

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

#### Объект `FdpTagIntegerLessThan`

Предикат типа `INTEGER_LESS_THAN`. Он проверяет, меньше ли тег (являющийся целым числом) эталонного значения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| value | string | Эталонное значение. |

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

#### Объект `FdpTagIntegerLessThanOrEqual`

Предикат типа `INTEGER_LESS_THAN_OR_EQUAL`. Он проверяет, меньше ли тег (являющийся целым числом) эталонного значения или равен ему.

| Элемент | Тип | Описание |
| --- | --- | --- |
| value | string | Эталонное значение. |

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

#### Объект `FdpTagIntegerGreaterThan`

Предикат типа `INTEGER_GREATER_THAN`. Он проверяет, больше ли тег (являющийся целым числом) эталонного значения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| value | string | Эталонное значение. |

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

#### Объект `FdpTagIntegerGreaterThanOrEqual`

Предикат типа `INTEGER_GREATER_THAN_OR_EQUAL`. Он проверяет, больше ли тег (являющийся целым числом) эталонного значения или равен ему.

| Элемент | Тип | Описание |
| --- | --- | --- |
| value | string | Эталонное значение. |

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

#### Объект `FdpTagDoubleEquals`

Предикат типа `DOUBLE_EQUALS`. Он проверяет, равен ли тег (являющийся числом с плавающей точкой) эталонному значению.

| Элемент | Тип | Описание |
| --- | --- | --- |
| negated | boolean | - |
| value | number | Эталонное значение. |

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

#### Объект `FdpTagDoubleLessThan`

Предикат типа `DOUBLE_LESS_THAN`. Он проверяет, меньше ли тег (являющийся числом с плавающей точкой) эталонного значения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| value | number | Эталонное значение. |

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

#### Объект `FdpTagDoubleLessThanOrEqual`

Предикат типа `DOUBLE_LESS_THAN_OR_EQUAL`. Он проверяет, меньше ли тег (являющийся числом с плавающей точкой) эталонного значения или равен ему.

| Элемент | Тип | Описание |
| --- | --- | --- |
| value | number | Эталонное значение. |

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

#### Объект `FdpTagDoubleGreaterThan`

Предикат типа `DOUBLE_GREATER_THAN`. Он проверяет, больше ли тег (являющийся числом с плавающей точкой) эталонного значения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| value | number | Эталонное значение. |

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

#### Объект `FdpTagDoubleGreaterThanOrEqual`

Предикат типа `DOUBLE_GREATER_THAN_OR_EQUAL`. Он проверяет, больше ли тег (являющийся числом с плавающей точкой) эталонного значения или равен ему.

| Элемент | Тип | Описание |
| --- | --- | --- |
| value | number | Эталонное значение. |

```
{



"type": "DOUBLE_GREATER_THAN_OR_EQUAL",



"values": 10



}
```

## Вариации объекта `FdcPredicate`

Объект `FdcPredicate` является базовым для предикатов условия правила обнаружения сбоев. Фактический набор полей зависит от поля **type** условия.

### STRING\_EQUALS

FdcPredicateStringEquals

Parameters

JSON model

#### Объект `FdcPredicateStringEquals`

Предикат типа `STRING_EQUALS`. Он проверяет, равен ли атрибут (являющийся строкой) одному из эталонных значений.

| Элемент | Тип | Описание |
| --- | --- | --- |
| ignoreCase | boolean | Условие чувствительно к регистру (`false`) или нечувствительно (`true`).  Если не задано, используется `false`, делая условие чувствительным к регистру. |
| values | string[] | Список эталонных значений. Условие выполняется, когда атрибут (строка) равен *любому* из этих значений. |

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

#### Объект `FdcPredicateStringStartsWith`

Предикат типа `STRING_STARTS_WITH`. Он проверяет, начинается ли атрибут (являющийся строкой) с одного из эталонных значений.

| Элемент | Тип | Описание |
| --- | --- | --- |
| ignoreCase | boolean | Условие чувствительно к регистру (`false`) или нечувствительно (`true`).  Если не задано, используется `false`, делая условие чувствительным к регистру. |
| values | string[] | Список эталонных значений. Условие выполняется, когда атрибут (строка) начинается с *любого* из этих значений. |

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

#### Объект `FdcPredicateStringEndsWith`

Предикат типа `STRING_ENDS_WITH`.  Он проверяет, заканчивается ли атрибут (являющийся строкой) одним из эталонных значений.

| Элемент | Тип | Описание |
| --- | --- | --- |
| ignoreCase | boolean | Условие чувствительно к регистру (`false`) или нечувствительно (`true`).  Если не задано, используется `false`, делая условие чувствительным к регистру. |
| values | string[] | Список эталонных значений. Условие выполняется, когда атрибут (строка) заканчивается *любым* из этих значений. |

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

#### Объект `FdcPredicateStringContains`

Предикат типа `STRING_CONTAINS_SUBSTRING`. Он проверяет, содержит ли атрибут (являющийся строкой) одно из эталонных значений.

| Элемент | Тип | Описание |
| --- | --- | --- |
| ignoreCase | boolean | Условие чувствительно к регистру (`false`) или нечувствительно (`true`).  Если не задано, используется `false`, делая условие чувствительным к регистру. |
| values | string[] | Список эталонных значений. Условие выполняется, когда атрибут (строка) содержит *любое* из этих значений. |

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

#### Объект `FdcPredicateIntegerEquals`

Предикат типа `INTEGER_EQUALS`. Он проверяет, равен ли атрибут (являющийся целым числом) одному из эталонных значений.

| Элемент | Тип | Описание |
| --- | --- | --- |
| values | integer[] | Эталонное значение. Условие выполняется, когда атрибут (целое число) равен *любому* из этих значений. |

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

#### Объект `FdcPredicateIntegerLessThan`

Предикат типа `INTEGER_LESS_THAN`. Он проверяет, меньше ли атрибут (являющийся целым числом) эталонного значения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| value | integer | Эталонное значение. Условие выполняется, когда атрибут (являющийся целым числом) меньше этого значения. |

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

#### Объект `FdcPredicateIntegerLessThanOrEqual`

Предикат типа `INTEGER_LESS_THAN_OR_EQUAL`. Он проверяет, меньше ли атрибут (являющийся целым числом) эталонного значения или равен ему.

| Элемент | Тип | Описание |
| --- | --- | --- |
| value | integer | Эталонное значение. Условие выполняется, когда атрибут (являющийся целым числом) меньше этого значения или равен ему. |

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

#### Объект `FdcPredicateIntegerGreaterThan`

Предикат типа `INTEGER_GREATER_THAN`. Он проверяет, больше ли атрибут (являющийся целым числом) эталонного значения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| value | integer | Эталонное значение. Условие выполняется, когда атрибут (являющийся целым числом) больше этого значения. |

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

#### Объект `FdcPredicateIntegerGreaterThanOrEqual`

Предикат типа `INTEGER_GREATER_THAN_OR_EQUAL`. Он проверяет, больше ли атрибут (являющийся целым числом) эталонного значения или равен ему.

| Элемент | Тип | Описание |
| --- | --- | --- |
| value | integer | Эталонное значение. Условие выполняется, когда атрибут (являющийся целым числом) больше этого значения или равен ему. |

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

#### Объект `FdcPredicateLongEquals`

Предикат типа `LONG_EQUALS`. Он проверяет, равен ли атрибут (являющийся long) одному из эталонных значений.

| Элемент | Тип | Описание |
| --- | --- | --- |
| values | string[] | Список эталонных значений. Условие выполняется, когда атрибут (long) равен *любому* из этих значений. |

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

#### Объект `FdcPredicateLongLessThan`

Предикат типа `LONG_LESS_THAN`. Он проверяет, меньше ли атрибут (являющийся long) эталонного значения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| value | string | Эталонное значение. Условие выполняется, когда атрибут (являющийся long) меньше этого значения. |

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

#### Объект `FdcPredicateLongLessThanOrEqual`

Предикат типа `LONG_LESS_THAN_OR_EQUAL`. Он проверяет, меньше ли атрибут (являющийся long) эталонного значения или равен ему.

| Элемент | Тип | Описание |
| --- | --- | --- |
| value | string | Эталонное значение. Условие выполняется, когда атрибут (являющийся long) меньше этого значения или равен ему. |

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

#### Объект `FdcPredicateLongGreaterThan`

Предикат типа `LONG_GREATER_THAN`. Он проверяет, больше ли атрибут (являющийся long) эталонного значения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| value | string | Эталонное значение. Условие выполняется, когда атрибут (являющийся long) больше этого значения. |

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

#### Объект `FdcPredicateLongGreaterThanOrEqual`

Предикат типа `LONG_GREATER_THAN_OR_EQUAL`. Он проверяет, больше ли атрибут (являющийся long) эталонного значения или равен ему.

| Элемент | Тип | Описание |
| --- | --- | --- |
| value | string | Эталонное значение. Условие выполняется, когда атрибут (являющийся long) больше этого значения или равен ему. |

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

#### Объект `FdcPredicateTagKeyEquals`

Предикат типа `TAG_KEY_EQUALS`. Он проверяет, равен ли атрибут (являющийся ключом тега) одному из эталонных значений.

| Элемент | Тип | Описание |
| --- | --- | --- |
| keys | string[] | Список эталонных значений. Условие выполняется, когда атрибут (являющийся ключом тега) равен *любому* из них. |

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

#### Объект `FdcPredicateTagEquals`

Предикат типа `TAG_EQUALS`. Он проверяет, равен ли атрибут (являющийся парой ключ:значение) одному из эталонных значений.

Эталонное значение это пара ключ:значение, состоящая из ключа и значения, находящихся на **одной и той же позиции** в соответствующих списках.

| Элемент | Тип | Описание |
| --- | --- | --- |
| keys | string[] | Список эталонных ключей тегов.  Условие выполняется, когда тег соответствует *любой* паре ключ:значение, состоящей из ключа и значения, находящихся на **одной и той же позиции** в соответствующих списках. |
| values | string[] | Список эталонных значений тегов.  Условие выполняется, когда тег соответствует *любой* паре ключ:значение, состоящей из ключа и значения, находящихся на **одной и той же позиции** в соответствующих списках. |

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

#### Объект `FdcPredicateServiceTypeEquals`

Предикат типа `SERVICE_TYPE_EQUALS`. Он проверяет, равен ли атрибут (являющийся типом сервиса) одному из эталонных значений.

| Элемент | Тип | Описание |
| --- | --- | --- |
| values | string[] | Список эталонных значений. Условие выполняется, когда атрибут (являющийся типом сервиса) равен *любому* из них.Возможные значения: WebRequest, WebService, Database, Method, WebSite, Messaging, Mobile, Process, Rmi, External, QueueListener, QueueInteraction, RemoteCall, SaasVendor, CustomApplication, Cics, Ims, CicsInteraction, ImsInteraction, EnterpriseServiceBus, ZosConnect. |

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

#### Объект `FdcPredicateManagementZonesContainsAll`

Предикат типа `MANAGEMENT_ZONES_CONTAINS_ALL`. Он проверяет, содержит ли атрибут (являющийся набором зон управления) **все** эталонные значения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| values | string[] | Список эталонных значений. Условие выполняется, когда атрибут (являющийся набором зон управления) содержит **все** эталонные значения.  Укажите здесь ID или имя зоны управления. |

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

#### Объект `FdcPredicateLongLessThan`

Предикат типа `LONG_LESS_THAN`. Он проверяет, меньше ли атрибут (являющийся long) эталонного значения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| value | string | Эталонное значение. Условие выполняется, когда атрибут (являющийся long) меньше этого значения. |

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

#### Объект `FdcPredicateLongLessThan`

Предикат типа `LONG_LESS_THAN`. Он проверяет, меньше ли атрибут (являющийся long) эталонного значения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| value | string | Эталонное значение. Условие выполняется, когда атрибут (являющийся long) меньше этого значения. |

```
{



"type": "SET_OF_INTEGERS_CONTAINS_ALL",



"values": [



10,



20



]



}
```