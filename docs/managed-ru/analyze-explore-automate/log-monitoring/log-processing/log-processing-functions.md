---
title: Функции обработки журналов (Logs Classic)
source: https://docs.dynatrace.com/managed/analyze-explore-automate/log-monitoring/log-processing/log-processing-functions
scraped: 2026-05-12T12:00:18.926101
---

# Функции обработки журналов (Logs Classic)

# Функции обработки журналов (Logs Classic)

* Обзор
* Чтение: 4 мин
* Обновлено 18 января 2023 г.

Log Monitoring Classic

Функции запросов используются для выполнения любых вычислений над полями в операторах [FIELDS\_ADD](/managed/analyze-explore-automate/log-monitoring/log-processing/log-processing-commands#dpl-command-fields-add "Используйте команды обработки журналов для преобразования входящих данных журнала для лучшего анализа или дальнейшей обработки.") и [FILTER\_OUT](/managed/analyze-explore-automate/log-monitoring/log-processing/log-processing-commands#dpl-command-filter-out "Используйте команды обработки журналов для преобразования входящих данных журнала для лучшего анализа или дальнейшей обработки.").

## Побитовые операции

### AND

**numeric\_expr1 & numeric\_expr2**

**BITWISE\_AND(numeric\_expr1, numeric\_expr2)**

Побитовое И между числовыми выражениями.

**BITWISE\_AND(ipaddr, numeric\_expr)**

Побитовое И между аргументами IPADDR и числовым.

тип вывода  
`LONG` или `IPADDR` в зависимости от типов входных аргументов.

**Пример**:

```
FIELDS_ADD(and_op:(ip & 0xffff), and_fn:BITWISE_AND(i, 0xffff));
```

| and\_op | and\_fn |
| --- | --- |
| 0.0.255.255 | 65535 |

### OR

**numeric\_expr1 | numeric\_expr2**

**BITWISE\_OR(numeric\_expr1, numeric\_expr2)**

Побитовое ИЛИ между числовыми выражениями.

тип вывода  
`LONG`

**Пример**:

```
FIELDS_ADD(or_op:(i | 1), or_fn:BITWISE_OR(d, 0xffff));
```

| or\_op | or\_fn |
| --- | --- |
| 1 | 65535 |

### XOR

**numeric\_expr1 ^ numeric\_expr2**

**BITWISE\_XOR(numeric\_expr1, numeric\_expr2)**

Побитовое исключающее ИЛИ (XOR) между числовыми выражениями.

тип вывода  
`LONG`

**Пример**:

```
FIELDS_ADD(xor_op:(i ^ 1), xor_fn:BITWISE_XOR(d, 0xffff));
```

| xor\_op | xor\_fn |
| --- | --- |
| 0 | 65534 |

### LEFT\_SHIFT

**numeric\_expr1 << numeric\_expr2**

**LEFT\_SHIFT(numeric\_expr1, numeric\_expr2)**

Побитовый сдвиг *numeric\_expr1* влево на количество бит *numeric\_expr2*.

тип вывода  
`LONG`

**Пример**:

```
FIELDS_ADD(lshift_op:(i << 1), lshift_fn:LEFT_SHIFT(d, 2));
```

| lshift\_op | lshift\_fn |
| --- | --- |
| 2 | 4 |

### RIGHT\_SHIFT

**numeric\_expr1 >> numeric\_expr2**

**RIGHT\_SHIFT(numeric\_expr1, numeric\_expr2)**

Побитовый сдвиг *numeric\_expr1* вправо на количество бит *numeric\_expr2*.

тип вывода  
`LONG`

**Пример**:

```
FIELDS_ADD(rshift_op:i >> 1, rshift_fn:RIGHT_SHIFT(d, 2));
```

| rshift\_op | rshift\_fn |
| --- | --- |
| 32767 | 16383 |

### ZERO\_FILL\_RIGHT\_SHIFT

**numeric\_expr1 >>> numeric\_expr2**

**ZERO\_FILL\_RIGHT\_SHIFT(numeric\_expr1, numeric\_expr2)**

Беззнаковый побитовый сдвиг *numeric\_expr1* вправо на количество бит *numeric\_expr2* (в крайнюю левую позицию записывается 0).

тип вывода  
`LONG`

**Пример**:

```
FIELDS_ADD(rshift_op:i >>> 1, rshift_fn:ZERO_FILL_RIGHT_SHIFT(d, 2));
```

| rshift\_op | rshift\_fn |
| --- | --- |
| 1073741824 | 536870912 |

### BITWISE\_NOT

**~ numeric\_expr**

**BITWISE\_NOT(numeric\_expr)**

Инвертирует биты *numeric\_expr*.

тип вывода  
`LONG`

**Пример**:

```
FIELDS_ADD(not_op:~i, not_fn:BITWISE_NOT(i));
```

| not\_op | not\_fn |
| --- | --- |
| -1 | -1 |

### BIT\_COUNT

**BIT\_COUNT(numeric\_expr)**

Возвращает количество бит, установленных в 1 в *numeric\_expr*.

тип вывода  
`LONG`

**Пример**:

```
FIELDS_ADD(BIT_COUNT(1));
```

| bit\_count |
| --- |
| 1 |

## Булевы операции

### AND

**boolean\_expr1 AND boolean\_expr2**

Логическое И между операндами *boolean\_expr1* и *boolean\_expr2*. Возвращает true только если оба операнда равны true.

Возвращает NULL, если правый операнд или оба операнда равны NULL.

тип вывода  
`BOOLEAN`

**Пример**:

```
FIELDS_ADD(BOOLEAN(1) AND BOOLEAN(0));
```

| boolean\_expr1 AND boolean\_expr2 |
| --- |
| false |

### OR

**boolean\_expr1 OR boolean\_expr2**

Логическое ИЛИ между операндами *boolean\_expr1* и *boolean\_expr2*. Возвращает true если хотя бы один из операндов равен true.

Возвращает NULL, если оба операнда равны NULL.

тип вывода  
`BOOLEAN`

**Пример**:

```
FIELDS_ADD(BOOLEAN(1) OR BOOLEAN(0));
```

| boolean\_expr1 OR boolean\_expr2 |
| --- |
| true |

### NOT

**NOT boolean\_expr**

Логическое НЕ *boolean\_expr*. Возвращает true, если *boolean\_expr* равен false, и false, если *boolean\_expr* равен true.

Возвращает NULL, если *boolean\_expr* равен NULL.

тип вывода  
`BOOLEAN`

**Пример**:

```
FIELDS_ADD(NOT BOOLEAN(1));
```

| NOT boolean\_expr |
| --- |
| false |

## Приведение типов (Casting)

### BOOLEAN

**BOOLEAN(numeric\_expr)**

Приводит числовое выражение к типу `BOOLEAN`. Возвращает false, если *numeric\_expr* равен 0, в противном случае — true.

Возвращает NULL, если *numeric\_expr* равен NULL.

тип вывода  
`BOOLEAN`

**Пример**:

```
FIELDS_ADD(BOOLEAN(0), BOOLEAN(1), BOOLEAN(2), BOOLEAN(i));
```

| BOOLEAN(0) | BOOLEAN(1) | BOOLEAN(2) | BOOLEAN(i) |
| --- | --- | --- | --- |
| false | true | true | false |
| false | true | true | true |
| false | true | true | true |

**BOOLEAN(string\_expr)**

Приводит строку к типу `BOOLEAN`. Возвращает true, если *string\_expr* равен `"true"` (без учёта регистра), в противном случае — false.

Возвращает NULL, если *string\_expr* равен NULL.

тип вывода  
`BOOLEAN`

**Пример**:

```
FIELDS_ADD(BOOLEAN("true"), BOOLEAN("True"), BOOLEAN("false"), BOOLEAN("random"));
```

| BOOLEAN("true") | BOOLEAN("True") | BOOLEAN("false") | BOOLEAN("random") |
| --- | --- | --- | --- |
| true | true | false | false |

### BYTES

**BYTES(array\_of\_integers)**

Создаёт `BYTES` из массива целых чисел. Если какой-либо элемент выходит за пределы диапазона \[0;255\], он усекается (берётся modulo 256).

Возвращает NULL, если аргумент равен NULL.

тип вывода  
`BYTES`

**Пример**:

```
FIELDS_ADD(BYTES([72,101,108,108,111,32,87,111,114,108,100,33]));
```

| bytes |
| --- |
| Hello World! |

### DOUBLE

**DOUBLE(numeric\_expr)**

**DOUBLE(string\_expr)**

Приводит числовое или строковое выражение к типу `DOUBLE`.

Возвращает NULL, если *numeric\_expr* или *string\_expr* равен NULL.

тип вывода  
`DOUBLE`

**Пример**:

```
FIELDS_ADD(DOUBLE(i), DOUBLE("10.02"), DOUBLE(t));
```

| DOUBLE(i) | DOUBLE("10.02") | DOUBLE(t) |
| --- | --- | --- |
| 0.0 | 10.02 | 1.569226843278E12 |
| 1.0 | 10.02 | 1.569226843278E12 |
| 2.0 | 10.02 | 1.569226843278E12 |

### DURATION

**DURATION(numeric\_expr)**

Приводит числовое выражение к типу `DURATION`. *numeric\_expr* интерпретируется в миллисекундах.

Возвращает NULL, если *numeric\_expr* равен NULL.

тип вывода  
`DURATION`

**Пример**:

```
FIELDS_ADD(DURATION(60000), DURATION(1));
```

| DURATION(60000) | DURATION(1) |
| --- | --- |
| 1min | 1ms |

**DURATION(string\_expr)**

Приводит строковое выражение к типу `DURATION`. Поддерживаются суффиксы: `ms`, `s`, `min`, `h`, `day`, `week`.

Возвращает NULL, если *string\_expr* равен NULL или не соответствует формату Duration.

тип вывода  
`DURATION`

**Пример**:

```
FIELDS_ADD(DURATION("10ms"), DURATION("1s"), DURATION("1min"), DURATION("1h"), DURATION("1day"), DURATION("1week"));
```

| DURATION("10ms") | DURATION("1s") | DURATION("1min") | DURATION("1h") | DURATION("1day") | DURATION("1week") |
| --- | --- | --- | --- | --- | --- |
| 10ms | 1s | 1min | 1h | 1day | 7day |

### INTEGER

**INTEGER(numeric\_expr)**

**INTEGER(string\_expr)**

**INTEGER(boolean\_expr)**

Приводит числовое, строковое или булево выражение к типу `INTEGER`. При приведении double к INTEGER используется усечение (truncation).

Возвращает NULL, если аргумент равен NULL.

тип вывода  
`INTEGER`

**Пример**:

```
FIELDS_ADD(INTEGER(d), INTEGER("10"), INTEGER(BOOLEAN(0)));
```

| INTEGER(d) | INTEGER("10") | INTEGER(BOOLEAN(0)) |
| --- | --- | --- |
| 0 | 10 | 0 |
| 1 | 10 | 0 |
| 2 | 10 | 0 |

### IPADDR

**IPADDR(string\_expr)**

Приводит строковое выражение к типу `IPADDR`.

Возвращает NULL, если *string\_expr* равен NULL или не является допустимым IP-адресом.

тип вывода  
`IPADDR`

**Пример**:

```
FIELDS_ADD(IPADDR("192.168.0.1"));
```

| ipaddr |
| --- |
| 192.168.0.1 |

**IPADDR(numeric\_expr)**

Приводит числовое выражение к типу `IPADDR`. Интерпретирует значение как IPv4-адрес.

тип вывода  
`IPADDR`

**Пример**:

```
FIELDS_ADD(IPADDR(3232235521));
```

| ipaddr |
| --- |
| 192.168.0.1 |

### LONG

**LONG(numeric\_expr)**

**LONG(string\_expr)**

**LONG(boolean\_expr)**

**LONG(timestamp\_expr)**

Приводит числовое, строковое, булево выражение или временную метку к типу `LONG`. При приведении double к LONG используется усечение (truncation). Временная метка конвертируется в миллисекунды эпохи (epoch milliseconds).

Возвращает NULL, если аргумент равен NULL.

тип вывода  
`LONG`

**Пример**:

```
FIELDS_ADD(LONG(d), LONG("10"), LONG(BOOLEAN(0)));
```

| LONG(d) | LONG("10") | LONG(BOOLEAN(0)) |
| --- | --- | --- |
| 0 | 10 | 0 |
| 1 | 10 | 0 |
| 2 | 10 | 0 |

### STRING

**STRING(any\_expr)**

Приводит любое выражение к типу `STRING`.

Возвращает NULL, если *any\_expr* равен NULL.

тип вывода  
`STRING`

**Пример**:

```
FIELDS_ADD(STRING(i), STRING(d), STRING(t), STRING(ip));
```

| STRING(i) | STRING(d) | STRING(t) | STRING(ip) |
| --- | --- | --- | --- |
| 0 | 0.0 | 2019-09-23 10:20:43.278 +0000 | 0.0.0.0 |

### TIMESTAMP

**TIMESTAMP(numeric\_expr)**

Приводит числовое выражение к типу `TIMESTAMP`. *numeric\_expr* интерпретируется как миллисекунды эпохи (epoch milliseconds).

Возвращает NULL, если *numeric\_expr* равен NULL.

тип вывода  
`TIMESTAMP`

**Пример**:

```
FIELDS_ADD(TIMESTAMP(1569226843278));
```

| timestamp |
| --- |
| 2019-09-23 10:20:43.278 +0000 |

**TIMESTAMP(string\_expr)**

Приводит строковое выражение к типу `TIMESTAMP`. *string\_expr* интерпретируется как дата-время ISO 8601.

Возвращает NULL, если *string\_expr* равен NULL или не соответствует формату.

тип вывода  
`TIMESTAMP`

**Пример**:

```
FIELDS_ADD(TIMESTAMP("2019-09-23T10:20:43.278Z"));
```

| timestamp |
| --- |
| 2019-09-23 10:20:43.278 +0000 |

### TO\_NULL

**TO\_NULL(any\_expr)**

Возвращает NULL для любого аргумента.

тип вывода  
`NULL`

**Пример**:

```
FIELDS_ADD(TO_NULL(i));
```

| to\_null |
| --- |
| NULL |

### TUPLE

**TUPLE(field, field, ...)**

Создаёт `TUPLE` из указанных полей.

тип вывода  
`TUPLE`

**Пример**:

```
FIELDS_ADD(TUPLE(i,t,s));
```

| tuple |
| --- |
| {i=0 t="2020-11-12 18:15:09.544000000 +0200" s="0ho0"} |

### VARIANT

**VARIANT(any\_expr)**

Приводит любое выражение к типу `VARIANT`.

тип вывода  
`VARIANT`

### VARIANT\_ARRAY

**VARIANT\_ARRAY(array\_expr)**

Приводит массив к типу `VARIANT_ARRAY`.

тип вывода  
`VARIANT_ARRAY`

### VARIANT\_OBJECT

**VARIANT\_OBJECT(any\_expr)**

**VARIANT\_OBJECT(field, field, ...)**

Приводит любое выражение или набор полей к типу `VARIANT_OBJECT`.

тип вывода  
`VARIANT_OBJECT`

**Пример**:

```
FIELDS_ADD(VARIANT_OBJECT(i,t,s));
```

| variant\_object |
| --- |
| {"i":0,"t":"2020-11-12 18:15:09.544000000 +0200","s":"0ho0"} |

### EMPTY\_ARRAY

**EMPTY\_ARRAY()**

Возвращает пустой массив.

тип вывода  
`ARRAY`

### NULL\_ARRAY

**NULL\_ARRAY()**

Возвращает NULL типа ARRAY.

тип вывода  
`ARRAY`

### NULL\_TUPLE

**NULL\_TUPLE()**

Возвращает NULL типа TUPLE.

тип вывода  
`TUPLE`

## Сравнение

### EQUAL

**expr1 = expr2**

Возвращает true, если *expr1* равно *expr2*. В противном случае возвращает false.

Возвращает NULL, если один из аргументов равен NULL.

тип вывода  
`BOOLEAN`

**Пример**:

```
FIELDS_ADD(i = 1);
```

| i = 1 |
| --- |
| false |
| true |
| false |

### NOT\_EQUAL

**expr1 != expr2**

**expr1 <> expr2**

Возвращает true, если *expr1* не равно *expr2*. В противном случае возвращает false.

Возвращает NULL, если один из аргументов равен NULL.

тип вывода  
`BOOLEAN`

### GREATER

**expr1 > expr2**

Возвращает true, если *expr1* больше *expr2*. В противном случае возвращает false.

Возвращает NULL, если один из аргументов равен NULL.

тип вывода  
`BOOLEAN`

### LESS

**expr1 < expr2**

Возвращает true, если *expr1* меньше *expr2*. В противном случае возвращает false.

Возвращает NULL, если один из аргументов равен NULL.

тип вывода  
`BOOLEAN`

### GREATER\_OR\_EQUAL

**expr1 >= expr2**

Возвращает true, если *expr1* больше или равно *expr2*. В противном случае возвращает false.

Возвращает NULL, если один из аргументов равен NULL.

тип вывода  
`BOOLEAN`

### LESS\_OR\_EQUAL

**expr1 <= expr2**

Возвращает true, если *expr1* меньше или равно *expr2*. В противном случае возвращает false.

Возвращает NULL, если один из аргументов равен NULL.

тип вывода  
`BOOLEAN`

### IS NULL

**expr IS NULL**

Возвращает true, если *expr* равен NULL. В противном случае возвращает false.

тип вывода  
`BOOLEAN`

**Пример**:

```
FIELDS_ADD(i IS NULL);
```

| i IS NULL |
| --- |
| false |

### IS NOT NULL

**expr IS NOT NULL**

Возвращает true, если *expr* не равен NULL. В противном случае возвращает false.

тип вывода  
`BOOLEAN`

**Пример**:

```
FIELDS_ADD(i IS NOT NULL);
```

| i IS NOT NULL |
| --- |
| true |

### IN

**expr IN \[value1, value2, ...\]**

Возвращает true, если *expr* содержится в списке значений. В противном случае возвращает false.

Возвращает NULL, если *expr* равен NULL.

тип вывода  
`BOOLEAN`

**Пример**:

```
FILTER_OUT(loglevel IN ['DEBUG', 'debug'])
```

### FALSE\_OR\_NULL

**FALSE\_OR\_NULL(boolean\_expr)**

Возвращает true, если *boolean\_expr* равен false или NULL. В противном случае возвращает false.

тип вывода  
`BOOLEAN`

### TRUE\_OR\_NULL

**TRUE\_OR\_NULL(boolean\_expr)**

Возвращает true, если *boolean\_expr* равен true или NULL. В противном случае возвращает false.

тип вывода  
`BOOLEAN`

## Составные данные

### VARIANT\_FIELD\_SELECT

**VARIANT\_FIELD\_SELECT(variant, string\_expr)**

Выбирает поле *string\_expr* из *variant* типа `VARIANT_OBJECT`.

Возвращает NULL, если *variant* или *string\_expr* равен NULL или если поле не найдено.

тип вывода  
`VARIANT`

**Пример**:

```
FIELDS_ADD(vo:VARIANT_OBJECT({i,t,s})) | FIELDS_ADD(VARIANT_FIELD_SELECT(vo, "i"));
```

| vo | variant\_field\_select |
| --- | --- |
| {"i":0,"t":"2020-11-12 18:15:09.544000000 +0200","s":"0ho0"} | 0 |

### TUPLE\_FIELD\_SELECT

**TUPLE\_FIELD\_SELECT(tuple, string\_expr)**

Выбирает поле *string\_expr* из *tuple* типа `TUPLE`.

тип вывода  
`VARIANT`

### ARRAY\_AVG

**ARRAY\_AVG(array)**

Возвращает среднее значение элементов числового массива.

Возвращает NULL, если массив пустой или равен NULL.

тип вывода  
`DOUBLE`

**Пример**:

```
FIELDS_ADD(array, ARRAY_AVG(array));
```

| array | array\_avg |
| --- | --- |
| [1, 2, 3] | 2.0 |

### ARRAY\_COUNT

**ARRAY\_COUNT(array)**

Возвращает количество ненулевых элементов в массиве.

тип вывода  
`LONG`

**Пример**:

```
FIELDS_ADD(array, ARRAY_COUNT(array));
```

| array | array\_count |
| --- | --- |
| [1, NULL, 3] | 2 |

### ARRAY\_FIRST

**ARRAY\_FIRST(array)**

Возвращает первый элемент массива.

Возвращает NULL, если массив пустой или равен NULL.

тип вывода  
тип элемента массива

### ARRAY\_LAST

**ARRAY\_LAST(array)**

Возвращает последний элемент массива.

Возвращает NULL, если массив пустой или равен NULL.

тип вывода  
тип элемента массива

### ARRAY\_MAX

**ARRAY\_MAX(array)**

Возвращает максимальный элемент числового массива.

Возвращает NULL, если массив пустой или равен NULL.

тип вывода  
тип элемента массива

### ARRAY\_MIN

**ARRAY\_MIN(array)**

Возвращает минимальный элемент числового массива.

Возвращает NULL, если массив пустой или равен NULL.

тип вывода  
тип элемента массива

### ARRAY\_JOIN

**ARRAY\_JOIN(array, separator)**

Объединяет элементы массива строк в одну строку, используя *separator* в качестве разделителя.

Возвращает NULL, если массив равен NULL.

тип вывода  
`STRING`

**Пример**:

```
FIELDS_ADD(ARRAY_JOIN(['a', 'b', 'c'], ', '));
```

| array\_join |
| --- |
| a, b, c |

### ARRAY\_SORT

**ARRAY\_SORT(array)**

**ARRAY\_SORT(array, 'ASC')**

**ARRAY\_SORT(array, 'DESC')**

Сортирует элементы массива в порядке возрастания (по умолчанию) или убывания.

Возвращает NULL, если массив равен NULL.

тип вывода  
тот же тип массива

### ARRAY\_SUM

**ARRAY\_SUM(array)**

Возвращает сумму элементов числового массива.

Возвращает NULL, если массив пустой или равен NULL.

тип вывода  
`LONG` или `DOUBLE`

**Пример**:

```
FIELDS_ADD(array, ARRAY_SUM(array));
```

| array | array\_sum |
| --- | --- |
| [1, 2, 3] | 6 |

### ARRAY\_IDX

**ARRAY\_IDX(array, index)**

Возвращает элемент массива по индексу *index*. Индексирование начинается с 0. Отрицательный индекс отсчитывается с конца.

Возвращает NULL, если массив равен NULL или индекс выходит за пределы.

тип вывода  
тип элемента массива

**Пример**:

```
FIELDS_ADD(array, ARRAY_IDX(array, 0));
```

| array | array\_idx |
| --- | --- |
| [10, 20, 30] | 10 |

### ARRAY\_SELECT

**ARRAY\_SELECT(array, from, to)**

Возвращает подмассив от индекса *from* до индекса *to* (не включая).

тип вывода  
тот же тип массива

### ARRAY\_LEN

**ARRAY\_LEN(array)**

Возвращает длину массива (количество элементов).

тип вывода  
`INTEGER`

**Пример**:

```
FIELDS_ADD(array, ARRAY_LEN(array));
```

| array | array\_len |
| --- | --- |
| [1, 2, 3] | 3 |

### ARRAY\_REMOVE\_NULLS

**ARRAY\_REMOVE\_NULLS(array)**

Возвращает массив с удалёнными элементами NULL.

тип вывода  
тот же тип массива

### ARRAY\_REVERSE

**ARRAY\_REVERSE(array)**

Возвращает массив с элементами в обратном порядке.

тип вывода  
тот же тип массива

### REMOVE\_NULLS

**REMOVE\_NULLS(array)**

Псевдоним для `ARRAY_REMOVE_NULLS`. Возвращает массив с удалёнными элементами NULL.

тип вывода  
тот же тип массива

### ARRAY\_UNIQ

**ARRAY\_UNIQ(array)**

Возвращает массив с удалёнными дублирующимися элементами (сохраняется первое вхождение).

тип вывода  
тот же тип массива

### SPREAD

**SPREAD(array)**

Разворачивает элементы массива в отдельные значения атрибута.

тип вывода  
тот же тип элементов массива

## Криптографические

### MD5

**MD5(string\_expr)**

Вычисляет MD5-хэш строки *string\_expr*.

Возвращает NULL, если *string\_expr* равен NULL.

тип вывода  
`STRING`

**Пример**:

```
FIELDS_ADD(MD5("Hello World!"));
```

| md5 |
| --- |
| ed076287532e86365e841e92bfc50d8c |

### SHA1

**SHA1(string\_expr)**

Вычисляет SHA-1 хэш строки *string\_expr*.

Возвращает NULL, если *string\_expr* равен NULL.

тип вывода  
`STRING`

**Пример**:

```
FIELDS_ADD(SHA1("Hello World!"));
```

| sha1 |
| --- |
| 2ef7bde608ce5404e97d5f042f95f89f1c232871 |

## Дата и время

### Операторы

**timestamp\_expr1 - timestamp\_expr2**

Вычисляет разность двух временных меток и возвращает результат типа `DURATION`.

**timestamp\_expr + duration\_expr**

**timestamp\_expr - duration\_expr**

Прибавляет или вычитает длительность из временной метки.

**duration\_expr1 + duration\_expr2**

**duration\_expr1 - duration\_expr2**

Прибавляет или вычитает две длительности.

**duration\_expr * numeric\_expr**

**duration\_expr / numeric\_expr**

Умножает или делит длительность на числовое значение.

### DAY

**DAY(timestamp)**

Возвращает день месяца из *timestamp* (1–31).

тип вывода  
`INTEGER`

**Пример**:

```
FIELDS_ADD(DAY(t));
```

| day |
| --- |
| 23 |

### DAY\_OF\_WEEK

**DAY\_OF\_WEEK(timestamp)**

Возвращает день недели из *timestamp* (1 = понедельник, 7 = воскресенье).

тип вывода  
`INTEGER`

### DAY\_OF\_YEAR

**DAY\_OF\_YEAR(timestamp)**

Возвращает номер дня в году из *timestamp* (1–366).

тип вывода  
`INTEGER`

### HOUR

**HOUR(timestamp)**

Возвращает часы из *timestamp* (0–23).

тип вывода  
`INTEGER`

**Пример**:

```
FIELDS_ADD(HOUR(t));
```

| hour |
| --- |
| 10 |

### MINUTE

**MINUTE(timestamp)**

Возвращает минуты из *timestamp* (0–59).

тип вывода  
`INTEGER`

### MONTH

**MONTH(timestamp)**

Возвращает месяц из *timestamp* (1–12).

тип вывода  
`INTEGER`

**Пример**:

```
FIELDS_ADD(MONTH(t));
```

| month |
| --- |
| 9 |

### NOW

**NOW()**

Возвращает текущее время в UTC.

тип вывода  
`TIMESTAMP`

**NOW()\[duration\]**

Возвращает временную метку, смещённую на указанную длительность относительно текущего момента. Отрицательное значение сдвигает в прошлое.

**Пример**:

```
FILTER_OUT(last_modified >= NOW()[-7 day])
```

### SECOND

**SECOND(timestamp)**

Возвращает секунды из *timestamp* (0–59).

тип вывода  
`INTEGER`

### STR\_SEC\_TO\_TIME

**STR\_SEC\_TO\_TIME(string\_expr)**

Конвертирует строку Unix-секунд к типу `TIMESTAMP`.

тип вывода  
`TIMESTAMP`

### STR\_TO\_TIME

**STR\_TO\_TIME(string\_expr, format\_str)**

Конвертирует строку *string\_expr* к типу `TIMESTAMP` в соответствии с форматом *format\_str*.

Возвращает NULL, если строка не соответствует формату.

тип вывода  
`TIMESTAMP`

**Пример**:

```
FIELDS_ADD(STR_TO_TIME("2019-09-23 10:20:43.278", "yyyy-MM-dd HH:mm:ss.SSS"));
```

| str\_to\_time |
| --- |
| 2019-09-23 10:20:43.278 +0000 |

### SYS\_TIME

**SYS\_TIME()**

Возвращает временную метку запуска обработки (время системы).

тип вывода  
`TIMESTAMP`

### TIME\_ADD

**TIME\_ADD(timestamp, duration)**

Прибавляет *duration* к *timestamp*.

тип вывода  
`TIMESTAMP`

### TIME\_ADD\_DAY

**TIME\_ADD\_DAY(timestamp, integer)**

Прибавляет *integer* дней к *timestamp*.

тип вывода  
`TIMESTAMP`

### TIME\_ADD\_WEEK

**TIME\_ADD\_WEEK(timestamp, integer)**

Прибавляет *integer* недель к *timestamp*.

тип вывода  
`TIMESTAMP`

### TIME\_ADD\_MONTH

**TIME\_ADD\_MONTH(timestamp, integer)**

Прибавляет *integer* месяцев к *timestamp*.

тип вывода  
`TIMESTAMP`

### TIME\_ADD\_YEAR

**TIME\_ADD\_YEAR(timestamp, integer)**

Прибавляет *integer* лет к *timestamp*.

тип вывода  
`TIMESTAMP`

### TIME\_SUB

**TIME\_SUB(timestamp, duration)**

Вычитает *duration* из *timestamp*.

тип вывода  
`TIMESTAMP`

### TIME\_SUB\_DAY

**TIME\_SUB\_DAY(timestamp, integer)**

Вычитает *integer* дней из *timestamp*.

тип вывода  
`TIMESTAMP`

### TIME\_SUB\_WEEK

**TIME\_SUB\_WEEK(timestamp, integer)**

Вычитает *integer* недель из *timestamp*.

тип вывода  
`TIMESTAMP`

### TIME\_SUB\_MONTH

**TIME\_SUB\_MONTH(timestamp, integer)**

Вычитает *integer* месяцев из *timestamp*.

тип вывода  
`TIMESTAMP`

### TIME\_SUB\_YEAR

**TIME\_SUB\_YEAR(timestamp, integer)**

Вычитает *integer* лет из *timestamp*.

тип вывода  
`TIMESTAMP`

### TIME\_SUBMOD

**TIME\_SUBMOD(timestamp, duration)**

Возвращает остаток от деления *timestamp* на *duration*.

тип вывода  
`DURATION`

### TIME\_SUBMOD\_DAY

**TIME\_SUBMOD\_DAY(timestamp)**

Возвращает время суток из *timestamp* как длительность от начала дня.

тип вывода  
`DURATION`

### TIME\_SUBMOD\_WEEK

**TIME\_SUBMOD\_WEEK(timestamp)**

Возвращает смещение от начала недели как длительность.

тип вывода  
`DURATION`

### TIME\_SUBMOD\_MONTH

**TIME\_SUBMOD\_MONTH(timestamp)**

Возвращает смещение от начала месяца как длительность.

тип вывода  
`DURATION`

### TIME\_SUBMOD\_YEAR

**TIME\_SUBMOD\_YEAR(timestamp)**

Возвращает смещение от начала года как длительность.

тип вывода  
`DURATION`

### TIME\_TO\_STR

**TIME\_TO\_STR(timestamp, format\_str)**

Конвертирует *timestamp* в строку в соответствии с форматом *format\_str*.

тип вывода  
`STRING`

**Пример**:

```
FIELDS_ADD(TIME_TO_STR(t, "yyyy-MM-dd'T'HH:mm:ss.SSSZ"));
```

| time\_to\_str |
| --- |
| 2019-09-23T10:20:43.278+0000 |

### TO\_STR\_SEC

**TO\_STR\_SEC(timestamp)**

Конвертирует *timestamp* в строку Unix-секунд.

тип вывода  
`STRING`

### YEAR

**YEAR(timestamp)**

Возвращает год из *timestamp*.

тип вывода  
`INTEGER`

**Пример**:

```
FIELDS_ADD(YEAR(t));
```

| year |
| --- |
| 2019 |

### WEEK\_OF\_YEAR

**WEEK\_OF\_YEAR(timestamp)**

Возвращает номер недели в году из *timestamp* (1–53).

тип вывода  
`INTEGER`

## Управление потоком

### IF

**IF(boolean\_expr, then\_expr)**

Возвращает *then\_expr*, если *boolean\_expr* равен true. В противном случае возвращает NULL.

тип вывода  
тип *then\_expr*

**IF(boolean\_expr) THEN (then\_expr)**

Эквивалентен `IF(boolean_expr, then_expr)`.

**IF(boolean\_expr) THEN (then\_expr) ELSE (else\_expr)**

Возвращает *then\_expr*, если *boolean\_expr* равен true. В противном случае возвращает *else\_expr*.

тип вывода  
общий тип *then\_expr* и *else\_expr*

**Пример**:

```
FIELDS_ADD(IF(i > 1) THEN ("big") ELSE ("small"));
```

| if |
| --- |
| small |
| small |
| big |

## Математические

### Операторы

**numeric\_expr1 + numeric\_expr2**

Сложение.

**numeric\_expr1 - numeric\_expr2**

Вычитание.

**numeric\_expr1 * numeric\_expr2**

Умножение.

**numeric\_expr1 / numeric\_expr2**

Деление. Деление на ноль возвращает NULL.

**numeric\_expr1 % numeric\_expr2**

Остаток от деления.

**- numeric\_expr**

Унарный минус.

### ABS

**ABS(numeric\_expr)**

Возвращает абсолютное значение *numeric\_expr*.

тип вывода  
тот же тип что и аргумент

**Пример**:

```
FIELDS_ADD(ABS(-5));
```

| abs |
| --- |
| 5 |

### ADD

**ADD(numeric\_expr1, numeric\_expr2)**

Эквивалентен оператору сложения `+`.

тип вывода  
`LONG` или `DOUBLE`

### ACOS

**ACOS(numeric\_expr)**

Возвращает арккосинус *numeric\_expr* в радианах.

тип вывода  
`DOUBLE`

### ASIN

**ASIN(numeric\_expr)**

Возвращает арксинус *numeric\_expr* в радианах.

тип вывода  
`DOUBLE`

### ATAN

**ATAN(numeric\_expr)**

Возвращает арктангенс *numeric\_expr* в радианах.

тип вывода  
`DOUBLE`

### ATAN2

**ATAN2(y, x)**

Возвращает угол тета в радианах в диапазоне от -π до π, преобразуя прямоугольные координаты (*x*, *y*) в полярные (*r*, *theta*).

тип вывода  
`DOUBLE`

### CBRT

**CBRT(numeric\_expr)**

Возвращает кубический корень *numeric\_expr*.

тип вывода  
`DOUBLE`

### CEIL

**CEIL(numeric\_expr)**

Возвращает наименьшее целое число, не меньшее *numeric\_expr*.

тип вывода  
`DOUBLE`

**Пример**:

```
FIELDS_ADD(CEIL(1.1));
```

| ceil |
| --- |
| 2.0 |

### COS

**COS(numeric\_expr)**

Возвращает косинус угла *numeric\_expr* в радианах.

тип вывода  
`DOUBLE`

### COSH

**COSH(numeric\_expr)**

Возвращает гиперболический косинус *numeric\_expr*.

тип вывода  
`DOUBLE`

### DEGREES

**DEGREES(numeric\_expr)**

Конвертирует радианы в градусы.

тип вывода  
`DOUBLE`

### DIVIDE

**DIVIDE(numeric\_expr1, numeric\_expr2)**

Эквивалентен оператору деления `/`.

тип вывода  
`LONG` или `DOUBLE`

### E

**E()**

Возвращает значение числа Эйлера (e ≈ 2.718281828...).

тип вывода  
`DOUBLE`

### EXP

**EXP(numeric\_expr)**

Возвращает e в степени *numeric\_expr*.

тип вывода  
`DOUBLE`

### EXPM1

**EXPM1(numeric\_expr)**

Возвращает (e^x - 1) для *numeric\_expr*. Более точный результат для малых значений *x*.

тип вывода  
`DOUBLE`

### FLOOR

**FLOOR(numeric\_expr)**

Возвращает наибольшее целое число, не превышающее *numeric\_expr*.

тип вывода  
`DOUBLE`

**Пример**:

```
FIELDS_ADD(FLOOR(1.9));
```

| floor |
| --- |
| 1.0 |

### FLOORDIV

**FLOORDIV(numeric\_expr1, numeric\_expr2)**

Возвращает целочисленное частное от деления (результат округлён вниз).

тип вывода  
`LONG`

### FLOORMOD

**FLOORMOD(numeric\_expr1, numeric\_expr2)**

Возвращает остаток от целочисленного деления с округлением вниз.

тип вывода  
`LONG`

### GETEXPONENT

**GETEXPONENT(double\_expr)**

Возвращает экспоненту (порядок) числа *double\_expr* согласно стандарту IEEE 754.

тип вывода  
`INTEGER`

### HYPOT

**HYPOT(numeric\_expr1, numeric\_expr2)**

Возвращает гипотенузу прямоугольного треугольника sqrt(x² + y²) без промежуточного переполнения или потери значимости.

тип вывода  
`DOUBLE`

### IEEEREMAINDER

**IEEEREMAINDER(numeric\_expr1, numeric\_expr2)**

Возвращает остаток деления *numeric\_expr1* на *numeric\_expr2* согласно стандарту IEEE 754.

тип вывода  
`DOUBLE`

### LOG

**LOG(numeric\_expr)**

Возвращает натуральный логарифм *numeric\_expr*.

тип вывода  
`DOUBLE`

### LOG1P

**LOG1P(numeric\_expr)**

Возвращает натуральный логарифм (1 + *numeric\_expr*). Более точный результат для малых значений.

тип вывода  
`DOUBLE`

### LOG10

**LOG10(numeric\_expr)**

Возвращает десятичный логарифм *numeric\_expr*.

тип вывода  
`DOUBLE`

### MODULO

**MODULO(numeric\_expr1, numeric\_expr2)**

Эквивалентен оператору остатка `%`.

тип вывода  
`LONG` или `DOUBLE`

### MULTIPLY

**MULTIPLY(numeric\_expr1, numeric\_expr2)**

Эквивалентен оператору умножения `*`.

тип вывода  
`LONG` или `DOUBLE`

### NEXTAFTER

**NEXTAFTER(double\_expr1, double\_expr2)**

Возвращает число double, следующее за *double\_expr1* в направлении *double\_expr2*.

тип вывода  
`DOUBLE`

### NEXTDOWN

**NEXTDOWN(double\_expr)**

Возвращает число double, следующее за *double\_expr* в направлении отрицательной бесконечности.

тип вывода  
`DOUBLE`

### NEXTUP

**NEXTUP(double\_expr)**

Возвращает число double, следующее за *double\_expr* в направлении положительной бесконечности.

тип вывода  
`DOUBLE`

### PI

**PI()**

Возвращает значение π (пи ≈ 3.141592653589793).

тип вывода  
`DOUBLE`

### POWER

**POWER(numeric\_expr1, numeric\_expr2)**

Возвращает *numeric\_expr1* в степени *numeric\_expr2*.

тип вывода  
`DOUBLE`

**Пример**:

```
FIELDS_ADD(POWER(2, 10));
```

| power |
| --- |
| 1024.0 |

### RADIANS

**RADIANS(numeric\_expr)**

Конвертирует градусы в радианы.

тип вывода  
`DOUBLE`

### RANDOM

**RANDOM()**

Возвращает случайное число double в диапазоне \[0.0, 1.0).

тип вывода  
`DOUBLE`

### RINT

**RINT(double\_expr)**

Возвращает ближайшее целое число, округляя к чётному при равноудалённости (банковское округление).

тип вывода  
`DOUBLE`

### ROUND

**ROUND(numeric\_expr)**

**ROUND(numeric\_expr, scale)**

Возвращает *numeric\_expr* округлённый до *scale* знаков после запятой (по умолчанию — до целого числа).

тип вывода  
`LONG` или `DOUBLE`

**Пример**:

```
FIELDS_ADD(ROUND(1.5), ROUND(2.5), ROUND(1.456, 2));
```

| ROUND(1.5) | ROUND(2.5) | ROUND(1.456,2) |
| --- | --- | --- |
| 2 | 3 | 1.46 |

### SCALB

**SCALB(double\_expr, integer\_expr)**

Возвращает *double\_expr* × 2^*integer\_expr* (точно, без потери значимости).

тип вывода  
`DOUBLE`

### SIGNUM

**SIGNUM(numeric\_expr)**

Возвращает знак числа: -1 для отрицательных, 0 для нуля, 1 для положительных.

тип вывода  
`DOUBLE`

### SIN

**SIN(numeric\_expr)**

Возвращает синус угла *numeric\_expr* в радианах.

тип вывода  
`DOUBLE`

### SINH

**SINH(numeric\_expr)**

Возвращает гиперболический синус *numeric\_expr*.

тип вывода  
`DOUBLE`

### SQRT

**SQRT(numeric\_expr)**

Возвращает квадратный корень *numeric\_expr*.

тип вывода  
`DOUBLE`

**Пример**:

```
FIELDS_ADD(SQRT(16));
```

| sqrt |
| --- |
| 4.0 |

### SUBMOD

**SUBMOD(numeric\_expr1, numeric\_expr2)**

Возвращает (*numeric\_expr1* - (*numeric\_expr1* % *numeric\_expr2*)).

тип вывода  
`LONG` или `DOUBLE`

### SUBTRACT

**SUBTRACT(numeric\_expr1, numeric\_expr2)**

Эквивалентен оператору вычитания `-`.

тип вывода  
`LONG` или `DOUBLE`

### TAN

**TAN(numeric\_expr)**

Возвращает тангенс угла *numeric\_expr* в радианах.

тип вывода  
`DOUBLE`

### TANH

**TANH(numeric\_expr)**

Возвращает гиперболический тангенс *numeric\_expr*.

тип вывода  
`DOUBLE`

### TOHEXSTRING

**TOHEXSTRING(numeric\_expr)**

Конвертирует числовое значение в шестнадцатеричную строку.

тип вывода  
`STRING`

**Пример**:

```
FIELDS_ADD(TOHEXSTRING(255));
```

| tohexstring |
| --- |
| ff |

### ULP

**ULP(double\_expr)**

Возвращает единицу наименьшей точности (ULP) числа *double\_expr*.

тип вывода  
`DOUBLE`

## Сетевые

### DSLICE

**DSLICE(ipaddr, prefix\_length)**

Выделяет *prefix\_length* значащих битов из IP-адреса *ipaddr* в соответствии с сетевой маской.

тип вывода  
`IPADDR`

**Пример**:

```
FIELDS_ADD(DSLICE(IPADDR("192.168.0.1"), 24));
```

| dslice |
| --- |
| 192.168.0.0 |

### IP\_TRUNC

**IP\_TRUNC(ipaddr, prefix\_length)**

Обнуляет биты хоста IP-адреса *ipaddr*, оставляя только *prefix\_length* первых (сетевых) битов.

тип вывода  
`IPADDR`

**Пример**:

```
FIELDS_ADD(IP_TRUNC(IPADDR("192.168.0.255"), 24));
```

| ip\_trunc |
| --- |
| 192.168.0.0 |

**IP\_TRUNC(ipaddr\_expr, mask\_ipaddr)**

Применяет маску *mask\_ipaddr* к IP-адресу *ipaddr\_expr* через операцию побитового И.

тип вывода  
`IPADDR`

**Пример**:

```
FIELDS_ADD(IP_TRUNC(IPADDR("192.168.0.12"), IPADDR("255.255.255.0")));
```

| ip\_trunc |
| --- |
| 192.168.0.0 |

### IS\_IPV4

**IS\_IPV4(ipaddr)**

Возвращает true, если *ipaddr* является IPv4-адресом.

тип вывода  
`BOOLEAN`

**Пример**:

```
FIELDS_ADD(IS_IPV4(IPADDR("192.168.0.1")));
```

| is\_ipv4 |
| --- |
| true |

### IS\_IPV6

**IS\_IPV6(ipaddr)**

Возвращает true, если *ipaddr* является IPv6-адресом.

тип вывода  
`BOOLEAN`

**Пример**:

```
FIELDS_ADD(IS_IPV6(IPADDR("2001:0db8:85a3::8a2e:0370:7334")));
```

| is\_ipv6 |
| --- |
| true |

### PARSEURI

**PARSEURI(uri\_str)**

Возвращает массив элементов URI, разобранных из строкового аргумента типа `STRING`.

Возвращает NULL, если аргумент равен NULL.

тип вывода  
`TUPLE`

**Пример**:

```
FIELDS_ADD(PARSEURI("https://docs.dynatrace.com:443/pages/dynatrace.html#sx-install"));
```

| parseuri |
| --- |
| {scheme="https" user=NULL host="docs.dynatrace.com" port=443 path="/pages/dynatrace.html" query=NULL fragment="sx-install"} |

## Строковые

### Операторы

**string\_expr1 + string\_expr2**

**string\_expr1 || string\_expr2**

Конкатенирует *string\_expr2* к *string\_expr1*.

тип вывода  
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

Возвращает декодированный из base16 *string\_expr*. Возвращает NULL, если *string\_expr* равен NULL.

тип вывода  
`BYTES`

**Пример**:

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

Возвращает *string\_expr*, закодированный в base16. Возвращает NULL, если *string\_expr* равен NULL.

тип вывода  
`STRING`

**Пример**:

```
FIELDS_ADD(BASE16_ENCODE('Red fox jumps over brown dog'));
```

| base16\_encode |
| --- |
| 52656420666f78206a756d7073206f7665722062726f776e20646f67 |

**BASE16\_ENCODE(bytes)**

**HEX(bytes)**

Возвращает *bytes*, закодированные в base16. Возвращает NULL, если аргумент равен NULL.

тип вывода  
`STRING`

**Пример**:

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

Возвращает `BYTES` base64-декодированного *string\_expr*. Возвращает NULL, если *string\_expr* равен NULL.

тип вывода  
`BYTES`

**Пример**:

```
FIELDS_ADD(encoded:'SGVsbG8gV29ybGQh')



| FIELDS_ADD(encoded, decoded_bytes:BASE64_DECODE(encoded))



| FIELDS_ADD(encoded, decoded_bytes, decoded_str:STRING(decoded_bytes));
```

| encoded | decoded\_bytes | decoded\_str |
| --- | --- | --- |
| SGVsbG8gV29ybGQh | [72,101,108,108,111,32,87,111,114,108,100,33] | Hello World! |

**BASE64\_DECODE\_STRING(string\_expr)**

Возвращает `STRING` base64-декодированного *string\_expr*. Возвращает NULL, если *string\_expr* равен NULL.

тип вывода  
`STRING`

**Пример**:

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

Возвращает *string\_expr*, закодированный в base64. Возвращает NULL, если *string\_expr* равен NULL.

тип вывода  
`STRING`

**Пример**:

```
FIELDS_ADD(BASE64_ENCODE('Hello World!'));
```

| base64\_encode |
| --- |
| SGVsbG8gV29ybGQh |

### CONCAT

**CONCAT(string\_expr, ...)**

Конкатенирует аргументы *expr* и возвращает результирующую строку. Максимальное количество аргументов — 128.

тип вывода  
`STRING`

**Пример**:

```
FIELDS_ADD(CONCAT('my ', '20 ', '$cents'));
```

| concat |
| --- |
| my 20 $cents |

### CHARAT

**CHARAT(string, pos)**

Возвращает символ в позиции *pos* строки *string*.

Возвращает NULL, если *string* равен NULL или *pos* выходит за пределы длины строки.

тип вывода  
`STRING`

**Пример**:

```
FIELDS_ADD(CHARAT("foo",0));
```

| charat |
| --- |
| f |

### CONTAINS

**CONTAINS(string1, string2)**

Возвращает true, если *string1* содержит *string2*. В противном случае возвращает false.

Возвращает NULL, если один из аргументов равен NULL.

Примечание

Сравнение чувствительно к регистру.

тип вывода  
`BOOLEAN`

**Пример**:

```
FIELDS_ADD(s, CONTAINS(s, "0"));
```

| s | contains |
| --- | --- |
| 0ho0 | true |
| 1ho1 | false |

### ENDS

**ENDS(string\_expr1, string\_expr2)**

Возвращает true, если *string\_expr1* заканчивается на *string\_expr2*. В противном случае возвращает false.

Возвращает NULL, если один из аргументов равен NULL.

Примечание

Сравнение чувствительно к регистру.

тип вывода  
`BOOLEAN`

**Пример**:

```
FIELDS_ADD(s, ENDS(s, "0"));
```

| s | ends |
| --- | --- |
| 0ho0 | true |
| 1ho1 | false |

### INDEXOF

**INDEXOF(str, substr, start\_pos)**

Возвращает индекс первого вхождения *substr* в *str*, начиная с позиции *start\_pos*. Если *start\_pos* отрицательный, поиск ведётся назад от *start\_pos*. Если не найдено, возвращает -1.

*start\_pos* отсчитывается с 0.

тип вывода  
`INTEGER`

**Пример**:

```
FIELDS_ADD(s, INDEXOF(s,"h",0));
```

| s | indexof |
| --- | --- |
| 0ho0 | 1 |

### LDIST

**LDIST(string\_expr1, string\_expr2)**

Вычисляет [расстояние Левенштейна](https://en.wikipedia.org/wiki/Levenshtein_distance) между *string\_expr1* и *string\_expr2*.

тип вывода  
`INTEGER`

**Пример**:

```
FIELDS_ADD(s1:s, s2:'0ho1') | FIELDS_ADD(s1, s2, LDIST(s1, s2));
```

| s1 | s2 | ldist |
| --- | --- | --- |
| 0ho0 | 0ho1 | 1 |

### LOWER

**LOWER(string)**

Конвертирует *string* в нижний регистр и возвращает результат.

тип вывода  
`STRING`

**Пример**:

```
FIELDS_ADD(LOWER('HeLlo WorlD'));
```

| lower |
| --- |
| hello world |

### MATCHES

**MATCHES(string, pattern\_expression)**

Возвращает true, если шаблонное выражение совпадает со *string*. В противном случае возвращает false.

тип вывода  
`BOOLEAN`

**Пример**:

```
FIELDS_ADD(MATCHES('hello world', "ALNUM SPACE ALNUM"))
```

| matches |
| --- |
| true |

### PARSE

**PARSE(string, pattern)**

Возвращает извлечённые поля первого совпадения *pattern* в *string*.

тип вывода

> 1. если шаблон не содержит экспортирующих матчеров — возвращает `BOOLEAN`, указывая на успех или неудачу разбора.
> 2. если шаблон содержит один экспортирующий матчер — возвращает совпавшее значение как отдельное значение.
> 3. если шаблон содержит более одного экспортирующего матчера — возвращает совпавшие значения как `TUPLE`.

**Пример**:

```
FIELDS_ADD(strings: "1 out of 10; 2 out of 10; 3 out of 10")



| FIELDS_ADD(PARSE(strings, "INT:prefix LD:string INT:suffix"))
```

| strings | parse |
| --- | --- |
| 1 out of 10; 2 out of 10; 3 out of 10 | {prefix=1 string=" out of " suffix=10} |

### PRINTF

**PRINTF(format, args...)**

Возвращает форматированную строку в соответствии с *format* (на основе [класса java.util.Formatter](https://docs.oracle.com/javase/8/docs/api/java/util/Formatter.html)) и аргументами.

тип вывода  
`STRING`

**Пример**:

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

Возвращает знаки пунктуации, содержащиеся в *string\_expr*.

**PUNCT(string\_expr, count, withSpace)**

Возвращает первые *count* знаков пунктуации из *string\_expr*, с пробелами или без (задаётся параметром *withSpace*).

Булев параметр *withSpace* включает в поиск пробел (ASCII 0x20) и печатает его как символ подчёркивания (ASCII 0x5F).

тип вывода  
`STRING`

**Пример**:

```
FIELDS_ADD(str:"Hi I'm home!") | FIELDS_ADD(PUNCT(str));
```

| punct |
| --- |
| '! |

### REPLACE\_STRING

**REPLACE\_STRING(string, target\_str, replace\_str)**

Заменяет каждое вхождение подстроки *target\_str* в *string* на *replace\_str*.

тип вывода  
`STRING`

**Пример**:

```
FIELDS_ADD(REPLACE_STRING('hello world', 'world', 'space'));
```

| REPLACE\_STRING |
| --- |
| hello space |

### REPLACE\_PATTERN

**REPLACE\_PATTERN(string, pattern\_expression, replacement\_template\_str)**

Заменяет каждое совпадение шаблона *pattern\_expression* в *string* на *replacement\_template\_str*.

тип вывода  
`STRING`

**Пример**:

```
FIELDS_ADD(REPLACE_PATTERN("aaa bbb ccc", "'a'+ SPACE 'b'+", "xxx"))
```

| replace\_pattern |
| --- |
| xxx ccc |

**Пример**:

```
FIELDS_ADD(REPLACE_PATTERN("label=valueA label=valueB", "'label=' NSPACE:exportedGroup", "modifiedLabel='modified ${exportedGroup}'"))
```

| replace\_pattern |
| --- |
| modifiedLabel='modified valueA' modifiedLabel='modified valueB' |

### SH\_ENTROPY

**SH\_ENTROPY(string\_expr)**

Вычисляет [энтропию Шеннона](https://en.wiktionary.org/wiki/Shannon_entropy) строки *string\_expr*.

тип вывода  
`DOUBLE`

**Пример**:

```
FIELDS_ADD(SH_ENTROPY("Hello world!"));
```

| sh\_entropy |
| --- |
| 3.0220552088742005 |

### SPLIT

**SPLIT(string, pattern\_expression)**

Разбивает *string* по совпадениям шаблона и возвращает результат как массив строк.

тип вывода  
`ARRAY`

**Пример**:

```
FIELDS_ADD(SPLIT('p1;p2;p3', "';'"))
```

| split |
| --- |
| [p1, p2, p3] |

### STRLEN

**STRLEN(string)**

Возвращает длину *string*.

тип вывода  
`INTEGER`

**Пример**:

```
FIELDS_ADD(STRLEN('hello world'));
```

| strlen |
| --- |
| 11 |

### STARTS

**STARTS(string1, string2)**

Возвращает true, если *string1* начинается с *string2*. В противном случае возвращает false.

Примечание

Сравнение чувствительно к регистру.

тип вывода  
`BOOLEAN`

**Пример**:

```
FIELDS_ADD(STARTS('Hello World!', 'Hell'));
```

| starts |
| --- |
| true |

### SUBSTR

**SUBSTR(string, startPos)**

Возвращает подстроку *string* от позиции *startPos* до конца. Если *startPos* отрицательный, подстрока берётся относительно конца строки.

тип вывода  
`STRING`

**Пример**:

```
FIELDS_ADD(SUBSTR('hello world', 6));
```

| substr |
| --- |
| world |

**SUBSTR(string, startPos, endPos)**

Возвращает подстроку *string* от позиции *startPos* до позиции *endPos*. Позиция отсчитывается с 0. Если *startPos* отрицательный, отсчёт ведётся с конца. Если *endPos* отрицательный, конец подстроки определяется относительно конца строки.

тип вывода  
`STRING`

**Пример**:

```
FIELDS_ADD(SUBSTR('my 20 $cents', 3,5));
```

| substr |
| --- |
| 20 |

### TRIM

**TRIM(string)**

Удаляет ведущие и замыкающие пробелы из *string*.

тип вывода  
`STRING`

**Пример**:

```
FIELDS_ADD(str:'  hello world         ') | FIELDS_ADD(str, TRIM(str));
```

| str | trim |
| --- | --- |
| hello world | hello world |

### UNESCAPE

**UNESCAPE(string)**

**DEESCAPE(string)**

Удаляет экранирование из *string*.

тип вывода  
`STRING`

**Пример**:

```
FIELDS_ADD(UNESCAPE("\""));
```

| unescape |
| --- |
| " |

### URLDECODE

**URLDECODE(string)**

Возвращает строку, декодированную из [URL-кодировки](https://en.wikipedia.org/wiki/Percent-encoding) (percent-encoding).

тип вывода  
`STRING`

**Пример**:

```
FIELDS_ADD(URLDECODE("Hello+world%21"));
```

| urldecode |
| --- |
| Hello world! |

### URLENCODE

**URLENCODE(string)**

Возвращает строку в URL-кодировке.

тип вывода  
`STRING`

**Пример**:

```
FIELDS_ADD(URLENCODE("Hello world!"));
```

| urlencode |
| --- |
| Hello+world%21 |

### HTMLUNESCAPE

**HTMLUNESCAPE(string)**

Декодирует HTML-сущности в *string*.

тип вывода  
`STRING`

**Пример**:

```
FIELDS_ADD(HTMLUNESCAPE("&lt;Fran&ccedil;ais&gt;"));
```

| htmlunescape |
| --- |
| <Français> |

### UPPER

**UPPER(string)**

Конвертирует *string* в верхний регистр.

тип вывода  
`STRING`

**Пример**:

```
FIELDS_ADD(UPPER('HeLlo WorlD'));
```

| upper |
| --- |
| HELLO WORLD |

## Прочие

### COALESCE

**COALESCE(expr1, expr2, exprN)**

Вычисляет входные выражения слева направо и возвращает первое ненулевое значение.

тип вывода  
общий тип аргументов, если аргументы одного типа; в противном случае — `VARIANT`.

**Пример**:

```
FIELDS_ADD(a:string(), b: 'b', c:'c')



| FIELDS_ADD(COALESCE(a, b, c))
```

| a | b | c | coalesce |
| --- | --- | --- | --- |
| NULL | b | c | b |

### COLUMN

**COLUMN(string\_expr)**

Выбирает столбец по имени *string\_expr*. Функция применяется, когда аргументы вычисляются динамически во время выполнения.

тип вывода  
тип выбранного столбца.

**Пример**:

```
FIELDS_ADD(ip_addr:COLUMN('ip'));
```

### FLAG

**FLAG(country\_code)**

Возвращает символ флага Unicode для кода страны ISO 3166 *country\_code*.

тип вывода  
`STRING`

**Пример**:

```
FIELDS_ADD(country:'Estonia', flag:FLAG('EE'));
```

| country | flag |
| --- | --- |
| Estonia | 🇪🇪 |

### HASH64

**HASH64(arg)**

Вычисляет 64-битное хэш-значение аргумента.

Примечание

Алгоритм не является криптографически стойким.

тип вывода  
`LONG`

**Пример**:

```
FIELDS_ADD(s, hash64:HASH64(s));
```

| s | hash64 |
| --- | --- |
| 0ho0 | -1180816457071597385 |

### REMOVE\_CHILD

**REMOVE\_CHILD(var\_obj, keys ...)**

Удаляет выбранные элементы (заданные одним или несколькими ключами *keys*) из аргумента типа `VARIANT_OBJECT` *var\_obj*.

тип вывода  
`VARIANT_OBJECT`

**Пример**: удаление элементов *t* и *s* из объекта variant:

```
FIELDS_ADD(vo:VARIANT_OBJECT({i,t,s}))



| FIELDS_ADD(REMOVE_CHILD(vo, "t", "s"))
```

| vo | remove\_child |
| --- | --- |
| {"i":0,"t":"2020-11-12 18:15:09.544000000 +0200","s":"0ho0"} | {"i":0} |

### SIZE

**SIZE(arg)**

Возвращает количество элементов в аргументе типа `ARRAY`, `TUPLE`, `VARIANT_ARRAY`, `VARIANT_OBJECT` или `BYTES`.

тип вывода  
`INTEGER`

**Пример**:

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

Возвращает размер аргумента в байтах.

тип вывода  
`LONG`

**Пример**:

```
FIELDS_ADD(int:i, sizeof_int:SIZEOF(i), tuple, sizeof_tuple:SIZEOF(tuple));
```

| int | sizeof\_int | tuple | sizeof\_tuple |
| --- | --- | --- | --- |
| 0 | 4 | {i=0 ip=0.0.0.0 ip6=0.0.0.0 s="0ho0" t="0ho0" ips=[] ip6s=[]} | 63 |

### TYPE

**TYPE(arg)**

Возвращает строку, идентифицирующую тип данных аргумента.

тип вывода  
`STRING`

**Пример**:

```
FIELDS_ADD(int_t:TYPE(i),i, time_t:TYPE(t),t, type_array:TYPE(array),array);
```

| int\_t | i | time\_t | t | type\_array | array |
| --- | --- | --- | --- | --- | --- |
| INTEGER | 0 | TIMESTAMP | 2019-09-23 10:20:43.278 +0000 | ARRAY | [] |

## Связанные темы

* [Примеры обработки журналов (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples "Примеры сценариев обработки журналов.")