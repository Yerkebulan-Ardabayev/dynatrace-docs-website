---
title: Типы данных DQL
source: https://www.dynatrace.com/docs/platform/grail/dynatrace-query-language/data-types
scraped: 2026-03-06T21:20:40.056889
---

# Типы данных DQL

# Типы данных DQL

* Latest Dynatrace
* Справочник
* Обновлено 24 октября 2024 г.

Dynatrace Query Language работает со строго типизированными данными: функции и операторы принимают только объявленные типы данных. Тип присваивается данным во время разбора или с помощью функций приведения типов. DQL также распознает типы значений, выраженные в литеральной нотации (например, при использовании константных значений в функциях).

## Примитивные типы

### Boolean

Boolean имеет только два возможных значения: `true` и `false`.

* **Литеральная нотация**
  Значение Boolean может быть выражено в верхнем или нижнем регистре: `true`, `TRUE`, `false`, `FALSE`
* **Преобразование в Boolean**

  + Преобразует строковые значения `true`, `TRUE` в значение Boolean `true`, а остальные значения -- в `false`.
  + Преобразует числовое значение `0` в Boolean `false`. Другие числовые значения преобразуются в Boolean `true`.

  ```
  ...



  | fields toBoolean("true"), toBoolean("TrUe"), toBoolean("1"), toBoolean(3), toBoolean("test"), toBoolean(0)
  ```
* **Выражения**

  ```
  boolean_expr1 AND boolean_expr2



  boolean_expr1 OR boolean_expr2



  boolean_expr1 XOR boolean_expr2



  NOT boolean_expr
  ```

### Long

Знаковый тип long имеет минимальное значение -2^63 и максимальное значение 2^63-1.

* **Литеральная нотация**
  LONG может быть выражен в десятичной или шестнадцатеричной нотации:
  **десятичная:** `-9223372036854775808` до `9223372036854775807`
  **шестнадцатеричная:** `0x0` до `0xFFFFFFFFFFFFFFFF`
* **Преобразование в Long**

  ```
  ..



  | fields toLong("83457264009472472"), toLong(30), toLong(25.34)
  ```

### Double

64-битное число с плавающей запятой двойной точности стандарта IEEE 754.

* **Литеральная нотация**

  **десятичная:** `2.34`
  **научная:** `2.4e2`
* **Преобразование в Double**
  Преобразует числовые значения и выражения в значение double.

  ```
  ...



  | fields toDouble("1234.5"), toDouble(4+3/2)
  ```

### Timestamp

Ссылка на момент времени с точностью до наносекунды.

Основное использование выражений времени -- указание пользовательского временного диапазона запроса в строке запроса DQL:

```
fetch logs, from:-2h, to:-20m
```

**Функции и сравнение**

```
...



| fields time = toTimestamp("2022-08-01T12:00:00+01:00")



| fieldsAdd time == now(), time > now()-10d, newTime = time + 3d
```

### Timeframe

Определенный временной интервал с временем начала и временем окончания в виде меток времени с точностью до наносекунды.
Для отображения полного результата запроса, включая наносекунды, измените визуализацию данных в Notebooks на raw.

```
data record(tf = timeframe(from:now()-2h, to:now()))



| fields tf, tf[start], tf[end]
```

### Duration

Длительность между двумя метками времени, состоящая из величины и единицы измерения времени.

```
...



| fields duration = 1s
```

**Временные литералы**

Следующие временные литералы могут использоваться для выражения длительности:

* `ns`: наносекунды
* `ms`: миллисекунды
* `s`: секунды
* `m`: минуты
* `h`: часы
* `d`: дни[1](#fn-1-1-def)
* `w`: недели
* `M`: месяцы
* `q`: кварталы
* `y`: годы

1

При использовании `d` в вычислениях он рассматривается как календарный день, в противном случае представляет длительность `24h`.

**Календарные длительности**

Вы можете использовать календарные длительности (`d`, `w`, `M`, `q` и `y`) в вычислениях, как показано в примере ниже, но не в качестве значений полей.

```
fetch logs, from: now()-1M+2w
```

**Создание длительности**

Во многих случаях разобранное числовое значение семантически представляет длительность. Функция `duration()` позволяет создать поле типа `duration` с указанной единицей измерения, используя доступные временные литералы.

```
...



| fields     dur = 62



| fieldsAdd  dur_ms = duration(dur, unit:"ms")



| fieldsAdd  dur_ms > 50ms
```

**Преобразование в длительность**

Преобразование значения в наносекундах в `duration`:

```
...



...



| fields     dur = toDuration(62*1000000000*60*60*24)



| fieldsAdd  dur > 60d
```

Преобразование периода между timestamp1 и timestamp2 в `duration`:

Для иллюстрации мы вычисляем возраст последнего сообщения лога, полученного от определенного хоста.

```
...



...



fetch       logs



| filter    dt.entity.host == "HOST-DD5679D1A0C6426C"



| sort      timestamp desc



| limit     1



| fields    timestamp, age_message = now()-timestamp
```

### String

Последовательность символов с указанной кодировкой.

* **Литеральная нотация**
  Заключите строку в двойные кавычки. При необходимости экранируйте двойные кавычки в строке обратной косой чертой `\`. Строка может содержать одинарные кавычки.
  Также вы можете заключать строки в тройные кавычки, например """someString""".

  + Внутри тройных кавычек экранирование не требуется.
  + Тройные кавычки не допускаются как часть строки. В таком случае вы можете использовать стандартные строки или функцию [concat](functions/string-functions.md#concat "A list of DQL string functions.").
* **Преобразование в String**
  Все типы данных DQL могут быть преобразованы в строку:

  ```
  ...



  | fields toString(toBoolean(1)), toString(array(1,2,3)), toString(1), toString(toTimestamp(now())), toString(toIpAddress("192.168.0.1"))
  ```

### IpAddress

Представляет адрес IPv4 или IPv6.

### UID

Тип данных, используемый для представления 64-битных и 128-битных идентификаторов.

Вы можете использовать следующие функции DQL для создания данных типа `UID`:

* [uid64](functions/conversion-and-casting-functions.md#uid64 "A list of DQL conversion and casting functions.")
* [uid128](functions/conversion-and-casting-functions.md#uid128 "A list of DQL conversion and casting functions.")
* [toUid](functions/conversion-and-casting-functions.md#toUid "A list of DQL conversion and casting functions.")

## Составные типы

### Array

Структура данных, содержащая последовательность значений, каждое из которых идентифицируется индексом.

* **Доступ к элементам массива**

  ```
  ...



  | fieldsAdd int_array = array(1,2,2,3,4,5)



  | fields first_element = int_array[0], fifth_element = int_array[4]
  ```
* **Сравнение массивов**
  Для массивов напрямую можно использовать только оператор равенства `==`.

  ```
  ...



  | ...



  | fields a=array(1,2), b=array(1,2,3), c=array("a","b"), d=toArray("c,d")



  | fields a == b, arraySize(b) > arraySize(c)
  ```

Полный список [функций DQL для работы с массивами](functions.md#array-functions "A list of DQL functions.") см. для получения дополнительной информации.

### Record

Набор пар ключ-значение, где значение может быть любым типом данных DQL.

* **Доступ к элементам RECORD**
  Доступ к элементам данных осуществляется по ключу:

  ```
  ...



  | fields person = record({name="john", age=33, address=record({city="Atlanta", pcode="30308"})})



  | fields person[name], person[address][pcode]
  ```
* **Преобразование в RECORD**
  Функция `record(expression,...)` преобразует одно или несколько выражений, возвращающих любой тип данных, в `RECORD`:

  ```
  ...



  | fields t = record(a=1+2,b=3,c=toString(timestamp))
  ```

  Разбор

  Разбор строк JSON или пар ключ-значение приводит к получению данных типа `RECORD`.

  ```
  STRUCTURE{matcher_expr, ...}:fieldname



  JSON{matcher_expr, ...}:fieldname



  KVP{matcher_expr, ...}:fieldname



  $subpattern:fieldname
  ```
* **Разбор данных пар ключ-значение**

  ```
  ...



  | fields str = "name=\"john\"; age=33; city=\"Atlanta\""



  | parse str, "KVP{LD:key'='(LONG:valueLong | STRING:valueStr)'; '?}:person"



  | fields person[name], person[age], person[city]
  ```
* **Разбор данных JSON**

  ```
  ...



  | fields str = "{\"type\":\"update\",\"host\":\"CI_preprod_1\",\"version\":\"10.2.2367\"}"



  | parse str,"JSON:event"



  | fields event[type], event[host], event[version]
  ```

## Связанные темы

* [Dynatrace Query Language](../dynatrace-query-language.md "How to use Dynatrace Query Language.")
* [Использование запросов DQL](dql-guide.md "Find out how DQL works and what are DQL key concepts.")
* [Сравнение DQL с SQL и другими языками](dql-comparison.md "See how DQL compares to other query languages.")
* [Справочник по языку DQL](dql-reference.md "Dynatrace Query Language syntax reference.")
* [Команды DQL](commands.md "A list of DQL commands.")
* [Функции DQL](functions.md "A list of DQL functions.")
* [Операторы DQL](operators.md "A list of DQL Operators.")
* [Лучшие практики DQL](dql-best-practices.md "Best practices for using Dynatrace Query Language.")