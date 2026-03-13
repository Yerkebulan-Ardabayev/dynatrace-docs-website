---
title: Строковые функции
source: https://www.dynatrace.com/docs/platform/grail/dynatrace-query-language/functions/string-functions
scraped: 2026-03-06T21:22:55.672336
---

# Строковые функции

# Строковые функции

* Latest Dynatrace
* Справочник
* Обновлено 29 янв. 2026

Строковые функции позволяют создавать выражения, которые обрабатывают текстовые строки различными способами.

Чувствительность к регистру

Все функции сопоставления строк по умолчанию чувствительны к регистру. При необходимости параметр `caseSensitive` позволяет изменить это поведение.

```
...



| fieldsAdd str_found = contains(content, "FlushCommand", caseSensitive:false)
```

## concat

Объединяет выражения в одну строку.

#### Синтаксис

`concat(expression, ... [, delimiter: ])`

#### Параметры

#### Возвращаемое значение

Тип возвращаемого значения -- `string`.

#### Примеры

##### Пример 1

```
data record(a = "DQL", b = "is", c = "awesome!")



| fieldsAdd concat(a, b, c, delimiter: " ")
```

Запустить в Playground

Результат запроса:

## contains

Выполняет поиск подстроки в строковом выражении. Возвращает `true`, если подстрока найдена, и `false` в противном случае.

#### Синтаксис

`contains(expression, substring [, caseSensitive])`

#### Параметры

#### Возвращаемое значение

Тип возвращаемого значения -- `boolean`.

#### Примеры

##### Пример 1

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language")



| fieldsAdd contains(content, "DQL"),



contains(content, "dql", caseSensitive: false),



contains(content, "Query")
```

Запустить в Playground

Результат запроса:

## decodeUrl

Возвращает декодированную URL-строку.

#### Синтаксис

`decodeUrl(expression)`

#### Параметры

#### Возвращаемое значение

Тип возвращаемого значения -- `string`.

#### Примеры

##### Пример 1

```
data record(content = "https%3A%2F%2Fwww.dynatrace.com%2Fplatform%2Fgrail"),



record(content = "https://www.dynatrace.com/platform/grail")



| fieldsAdd decodeUrl(content)
```

Запустить в Playground

Результат запроса:

## encodeUrl

Кодирует URL-строку, заменяя символы, которые не являются числами или буквами, символами процента и шестнадцатеричными числами.

#### Синтаксис

`encodeUrl(expression)`

#### Параметры

#### Возвращаемое значение

Тип возвращаемого значения -- `string`.

#### Примеры

##### Пример 1

```
data record(content = "https://www.dynatrace.com/platform/grail")



| fieldsAdd encodeUrl(content)
```

Запустить в Playground

Результат запроса:

## endsWith

Проверяет, заканчивается ли строковое выражение указанным суффиксом. Возвращает `true`, если да, и `false` в противном случае.

#### Синтаксис

`endsWith(expression, suffix [, caseSensitive])`

#### Параметры

#### Возвращаемое значение

Тип возвращаемого значения -- `boolean`.

#### Примеры

##### Пример 1

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language")



| fieldsAdd endsWith(content, "awesome!"),



endsWith(content, "AWESOME!", caseSensitive: false),



endsWith(content, "Language")
```

Запустить в Playground

Результат запроса:

## escape

Возвращает экранированную строку.

Правила экранирования

1. Одинарные и двойные кавычки экранируются. Обратные кавычки не экранируются.

2. Обратные косые черты экранируются.

3. ASCII-символы backspace, form feed, перевод строки, возврат каретки, горизонтальная табуляция экранируются.

4. ASCII-символы в диапазоне 0x20 - 0x7e (печатные ASCII-символы), не охваченные ни одним из вышеуказанных правил, остаются без изменений.

5. Все остальные ASCII-символы представляются как `\xhh`. Это применяется к следующим символам

   * символы в диапазоне 0x00 - 0x07
   * символ 0x0b (вертикальная табуляция)
   * символы в диапазоне 0x0e - 0x1f
   * символ 0x7f

6. Все символы в расширенном ASCII-пространстве (0x80-0xff) и символы Unicode за пределами ASCII-пространства представляются как `\uhhhh`.

#### Синтаксис

`escape(expression)`

#### Параметры

#### Возвращаемое значение

Тип возвращаемого значения -- `string`.

#### Примеры

##### Пример 1

```
data record(content = """"foo@bar.com""")



| fieldsAdd escape(content)
```

Запустить в Playground

Результат запроса:

| content | escape(content) |
| --- | --- |
| `"foo@bar.com` | `\"foo@bar.com` |

## getCharacter

Возвращает символ на указанной позиции из строкового выражения. Отрицательные значения параметра позиции отсчитываются с конца строки. Если позиция выходит за пределы строки, функция возвращает NULL.

#### Синтаксис

`getCharacter(expression, position)`

#### Параметры

#### Возвращаемое значение

Тип возвращаемого значения -- `string`.

#### Примеры

##### Пример 1

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language")



| fieldsAdd getCharacter(content, 1),



getCharacter(content, 17),



getCharacter(content, -1)
```

Запустить в Playground

Результат запроса:

## indexOf

Возвращает индекс первого вхождения подстроки в строковом выражении.
Начинает поиск вперед с указанного индекса. Отрицательные значения параметра `from` отсчитываются с конца строки.
Значение по умолчанию для `from` равно `0` (поиск с начала строки).
Поиск чувствителен к регистру.
Если указанная подстрока не найдена, функция возвращает `-1`.

#### Синтаксис

`indexOf(expression, substring [, from])`

#### Параметры

#### Возвращаемое значение

Тип возвращаемого значения -- `long`.

#### Примеры

##### Пример 1

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language")



| fieldsAdd indexOf(content, "a"),



indexOf(content, "a", from: 10),



indexOf(content, "Query")
```

Запустить в Playground

Результат запроса:

## jsonField

Разбирает JSON-строку и извлекает одно значение, выбранное по имени.

#### Синтаксис

`jsonField(expression, fieldName [, seek])`

#### Параметры

#### Возвращаемое значение

Тип возвращаемого значения -- `long`, `double`, `boolean`, `string`, `array` или `record`.

#### Примеры

##### Пример 1

```
data record(content = """{



"name":"John",



"children":["Mallory", "Mary"],



"address":{"city":"Boston", "zip":"02210"}



}""")



| fieldsAdd jsonField(content, "name")
```

Запустить в Playground

Результат запроса:

##### Пример 2

```
data record(content = """JSON: {"name": "John"} ...""")



| fieldsAdd jsonField(content, "name", seek:false)



| fieldsAdd jsonField(content, "name", seek:true)
```

Запустить в Playground

Результат запроса:

## jsonPath

Разбирает JSON-строку и извлекает одно значение, выбранное с помощью выражения JSONPath.

#### Синтаксис

`jsonPath(expression, jsonPath [, seek])`

#### Параметры

#### Возвращаемое значение

Тип возвращаемого значения -- `long`, `double`, `boolean`, `string`, `array` или `record`.

#### Примеры

##### Пример 1

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

Запустить в Playground

Результат запроса:

##### Пример 2

```
data record(content = """JSON: {"name": "John"} ...""")



| fieldsAdd jsonPath(content, "$.name", seek:false)



| fieldsAdd jsonPath(content, "$.name", seek:true)
```

Запустить в Playground

Результат запроса:

## lastIndexOf

Возвращает индекс последнего вхождения подстроки в строковом выражении. Начинает поиск назад с указанного индекса. Отрицательные значения параметра from отсчитываются с конца строки. Значение по умолчанию для from равно -1 (поиск с конца строки). Поиск чувствителен к регистру. Если подстрока не найдена, функция возвращает `-1`.

#### Синтаксис

`lastIndexOf(expression, substring [, from])`

#### Параметры

#### Возвращаемое значение

Тип возвращаемого значения -- `long`.

#### Примеры

##### Пример 1

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language")



| fieldsAdd lastIndexOf(content, "a"),



lastIndexOf(content, "a", from: 10),



lastIndexOf(content, "Query")
```

Запустить в Playground

Результат запроса:

## levenshteinDistance

Вычисляет расстояние Левенштейна между двумя входными строками.

#### Синтаксис

`levenshteinDistance(expression, expression)`

#### Параметры

#### Возвращаемое значение

Тип возвращаемого значения -- `long`.

#### Примеры

##### Пример 1

```
data record(a = "DQL is awesome!", b = "Grail is awesome!"),



record(a = "Dynatrace Query Language", b = "DQL"),



record(a = "Dynatrace Query Language", b = "dynatrace query language")



| fieldsAdd levenshteinDistance(a, b)
```

Запустить в Playground

Результат запроса:

## like

Проверяет, соответствует ли строковое выражение шаблону. Если шаблон не содержит символов процента, `like()` действует как оператор `==` (проверка равенства). Символ процента в шаблоне `(%)` соответствует любой последовательности из нуля или более символов. Символ подчеркивания в шаблоне `(\_)` соответствует одному символу.

#### Синтаксис

`like(expression, pattern)`

#### Параметры

#### Возвращаемое значение

Тип возвращаемого значения -- `boolean`.

#### Примеры

##### Пример 1

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language")



| fieldsAdd like(content, "%DQL%"),



like(content, "D%L%"),



like(content, "D_L%")
```

Запустить в Playground

Результат запроса:

## lower

Преобразует строку в нижний регистр.

#### Синтаксис

`lower(expression)`

#### Параметры

#### Возвращаемое значение

Тип возвращаемого значения -- `string`.

#### Примеры

##### Пример 1

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language")



| fieldsAdd lower(content)
```

Запустить в Playground

Результат запроса:

## matchesPattern

Проверяет, соответствует ли строковое выражение шаблону DPL, и возвращает `true`, если да, в противном случае -- `false`.

#### Синтаксис

`matchesPattern(expression, pattern)`

#### Параметры

#### Возвращаемое значение

Тип возвращаемого значения -- `boolean`.

#### Примеры

##### Пример 1

```
data record(content = "2023-11-01 12:52:12 : 766"),



record(content = "2023-11-01 12:53:00:123"),



record(content = "2023-11-01 12:55:59 : 192.168.0.1")



| fieldsAdd matchesPattern(content, "TIME ' : ' LONG"),



matchesPattern(content, "TIME ' : ' IP")
```

Запустить в Playground

Результат запроса:

| content | matchesPattern(content, "TIME ' : ' LONG") | matchesPattern(content, "TIME ' : ' IP") |
| --- | --- | --- |
| `2023-11-01 12:52:12 : 766` | `true` | `false` |
| `2023-11-01 12:53:00:123` | `false` | `false` |
| `2023-11-01 12:55:59 : 192.168.0.1` | `false` | `true` |

## matchesPhrase

Сопоставляет фразу с входным строковым выражением с использованием токенных сопоставителей.

#### Синтаксис

`matchesPhrase(expression, phrase [, caseSensitive])`

#### Параметры

#### Возвращаемое значение

Тип возвращаемого значения -- `boolean`.

#### Примеры

##### Пример 1

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language"),



record(content = array("DQL", "is", "awesome", "!", "Dynatrace Query Language"))



| fieldsAdd matchesPhrase(content, "DQL"),



matchesPhrase(content, "Dyna"),



matchesPhrase(content, "query"),



matchesPhrase(content, "query", caseSensitive: true)
```

Запустить в Playground

Результат запроса:

## matchesValue

Выполняет поиск записей с определенным значением в указанном атрибуте. Возвращает `true` или `false`.

#### Синтаксис

`matchesValue(expression, value, ... [, caseSensitive])`

#### Параметры

#### Возвращаемое значение

Тип возвращаемого значения -- `boolean`.

#### Примеры

##### Пример 1

По умолчанию значения сопоставляются без учета регистра:

```
data record(content = "User 'kaarmanue' failed to login from 192.168.0.1")



| fieldsAdd matchesValue(content, "User*"),



matchesValue(content, "user*"),



matchesValue(content, "user*", caseSensitive: true)
```

Запустить в Playground

Результат запроса:

##### Пример 2

Значения сопоставляются с начала. Для сопоставления частей значения используйте `*` в качестве подстановочного символа:

```
data record(content = "User 'kaarmanue' failed to login from 192.168.0.1")



| fieldsAdd matchesValue(content, "192.168.0.1"),



matchesValue(content, "*192.168.0.1"),



matchesValue(content, "*failed to log*")
```

Запустить в Playground

Результат запроса:

##### Пример 3

Без учета регистра сопоставляются только ASCII-символы:

```
data record(content = "Oesterreich")



| fieldsAdd matchesValue(content, "oesterreich"),



matchesValue(content, "Oesterreich")
```

Запустить в Playground

Результат запроса:

##### Пример 4

Функция обрабатывает значения массивов в режиме "any-match" (совпадение любого элемента).

```
data record(technologies = array("Java11", "java17"))



| fieldsAdd matchesValue(technologies, "Java11"),



matchesValue(technologies, "java"),



matchesValue(technologies, "java*")
```

Запустить в Playground

Результат запроса:

#### Сопоставление с несколькими шаблонами

Функция `matchesValue()` поддерживает сопоставление с несколькими шаблонами. Вы можете использовать массив или список шаблонов с параметром `value`. В качестве шаблонов поддерживаются только строки. Другие типы данных не дают совпадения и игнорируются. Функция `matchesValue()` возвращает true, если любой из шаблонов совпадает. Если ни один из шаблонов не дает совпадения, возвращается `false`.

#### Пример

```
data record(content = array("DQL", "is", "awesome", "!"))



| fieldsAdd matchesValue(content, array("Grail", "dql")),



matchesValue(content, {"Grail", "dql"}),



matchesValue(content, {"Grail", "dq*"}),



matchesValue(content, {"Grail", "dq*"}, caseSensitive: true)
```

Запустить в Playground

Результат запроса:

## parse

Извлекает одно значение из строки в соответствии с шаблоном или запись, если имеется несколько именованных сопоставителей.

#### Синтаксис

`parse(expression, pattern)`

#### Параметры

#### Возвращаемое значение

Функция `parse` возвращает одно значение, которое может быть примитивного типа или записью. Результат имеет примитивный тип в случае одного именованного сопоставителя в шаблоне DPL. Если в шаблоне несколько именованных сопоставителей, результатом является запись, содержащая поля, соответствующие именам сопоставителей.
Поля, созданные из результата функции `parse`, по умолчанию получают имя именованного сопоставителя в шаблоне DPL. В случае нескольких именованных сопоставителей в шаблоне имя поля по умолчанию -- `parsed_record`. Вы также можете определить альтернативные имена полей с помощью выражения-псевдонима.

#### Примеры

##### Пример 1

```
data record(src = "1 2"),



record(src = "45 46 47 48")



| fieldsAdd parse(src, "LONG:result"),



value = parse(src, "LONG:result"),



parse(src, "LONG:field1 ' ' LONG:field2")
```

Запустить в Playground

Результат запроса:

| src | result | value | parsed\_record |
| --- | --- | --- | --- |
| `1 2` | `1` | `1` | **field1**: `1` **field2**: `2` |
| `45 46 47 48` | `45` | `45` | **field1**: `45` **field2**: `46` |

## parseAll

Извлекает несколько значений из строки в соответствии с шаблоном.
В отличие от функции [`parse`](string-functions.md#parse "A list of DQL string functions."), `parseAll` всегда возвращает массив. Массив может быть пустым, если ни один шаблон не совпал. Отдельный элемент может быть примитивного типа или записью.

#### Синтаксис

`parseAll(expression, pattern)`

#### Параметры

#### Возвращаемое значение

Тип возвращаемого значения -- `array`.

#### Примеры

##### Пример 1

```
data record(src = "1 2"),



record(src = "45 46 47 48")



| fieldsAdd parseAll(src, "LONG:result"),



value = parseAll(src, "LONG:result"),



parseAll(src, "LONG:field1 ' ' LONG:field2")
```

Запустить в Playground

Результат запроса:

| src | result | value | parsed\_records |
| --- | --- | --- | --- |
| `1 2` | `[1, 2]` | `[1, 2]` | [**field1:** `1` **field2** `2`] |
| `45 46 47 48` | `[45, 46, 47, 48]` | `[45, 46, 47, 48]` | [**field1:** `45` **field2** `46`, **field1:** `47` **field2** `48`] |

## punctuation

Извлекает знаки пунктуации из входной строки.

#### Синтаксис

`punctuation(expression, [, count] [, withSpace])`

#### Параметры

#### Возвращаемое значение

Тип возвращаемого значения -- `string`.

#### Примеры

##### Пример 1

В этом примере мы извлекаем знаки пунктуации из каждой входной строки.

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language"),



record(content = "${placeholder}")



| fieldsAdd punctuation(content),



punctuation(content, count: 2),



punctuation(content, count: 2, withSpace: true)
```

Запустить в Playground

Результат запроса:

## replacePattern

Заменяет каждую подстроку строки, соответствующую шаблону DPL, указанной строкой. Шаблон должен быть определен как константное строковое выражение. Подробнее о синтаксисе шаблонов см. в [документации DPL](../../dynatrace-pattern-language.md "Use Dynatrace Pattern Language to describe patterns using matchers.").

#### Синтаксис

`replacePattern(expression, pattern, replacement)`

#### Параметры

#### Возвращаемое значение

Тип возвращаемого значения -- `string`.

#### Примеры

##### Пример 1

```
data record(content = "DQL 2019-08-01 09:30:00"),



record(content = "Dynatrace Query L4nguage")



| fieldsAdd replacePattern(content, "TIME", "is awesome!"),



replacePattern(content, "LONG", "a")
```

Запустить в Playground

Результат запроса:

| content | replacePattern(content, "TIME", "is awsome!") | replacePattern(content, "LONG", "a") |
| --- | --- | --- |
| `DQL 2019-08-01 09:30:00` | `DQL is awesome!` | `DQL aaa a:a:a` |
| `Dynatrace Query L4nguage` | `Dynatrace Query L4nguage` | `Dynatrace Query Language` |

## replaceString

Заменяет каждую подстроку строки указанной строкой. Эта функция заменяет только точно совпадающие подстроки из исходной строки на замену. Сопоставление чувствительно к регистру и не использует подстановочные символы. Все найденные вхождения заменяются, если они не пересекаются. Например, замена `abcabca` с шаблоном `abca` дает только одну замену. Заменяется только первое вхождение в начале строки.

#### Синтаксис

`replaceString(expression, substring, replacement)`

#### Параметры

#### Возвращаемое значение

Тип возвращаемого значения -- `string`.

#### Примеры

##### Пример 1

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language"),



record(content = "abcabca")



| fieldsAdd replaceString(content, "awesome", "simple"),



replaceString(content, "abca", "xyz")
```

Запустить в Playground

Результат запроса:

## splitByPattern

Разбивает строку в массив по каждому вхождению шаблона DPL.

#### Синтаксис

`splitByPattern(expression, pattern)`

#### Параметры

#### Возвращаемое значение

Тип возвращаемого значения -- `array`.

#### Примеры

##### Пример 1

```
data record(content = "one $1 two $4 three"),



record(content = "foo $1000 bar"),



record(content = "no separator"),



record(content = "")



| fieldsAdd splitByPattern(content, " ' $' LONG ' ' ")
```

Запустить в Playground

Результат запроса:

| content | splitByPattern(content, " ' $' LONG ' ' ") |
| --- | --- |
| `one $1 two $4 three` | `[one, two, three]` |
| `foo $1000 bar` | `[foo, bar]` |
| `no separator` | `[no separator]` |
| *пустая строка* | `[]` |

## splitString

Разбивает строку в соответствии с заданными параметрами.
Извлекает массив подстрок указанного выражения, смежных с вхождениями заданного шаблона.
Параметры интерпретируются буквально. Например, разбиение `www.dynatrace.org` по `.` дает `www`, `dynatrace` и `org`.
Использование пустой строки в качестве шаблона разбивает строку на однобайтовые подстроки. Например, разбиение четырех символов дает массив из четырех строк по одному байту каждая (разбиение выражения `"1234"` дает `array("1", "2", "3", "4")`).

Не-ASCII символы представляются несколькими байтами. Разбиение строки, содержащей такие символы, по `""` разделяет эти байты на отдельные недопустимые строки.

Если шаблон не найден в выражении, возвращается массив, содержащий только входное выражение.

Если выражение начинается с одного или нескольких вхождений шаблона, для каждого вхождения добавляется пустая строка. Например, `splitString("abc", "a")` дает `"", "bc"`. Аналогично, пустые строки добавляются, если шаблон найден в конце выражения.

Пустая строка также добавляется для смежных вхождений шаблона, которые не граничат с началом или концом строки. Например, `splitString("abbc", "b")` дает `"a", "", "c"`.

Если шаблон пуст, выражение разбивается на однобайтовые подстроки. Например, `splitString("abc", "")` дает `"a", "b", "c"`.

#### Синтаксис

`splitString(expression, pattern)`

#### Параметры

#### Возвращаемое значение

Тип возвращаемого значения -- `array`.

#### Примеры

##### Пример 1

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language")



| fieldsAdd splitString(content, " "),



splitString(content, "is"),



splitString(content, ""),



splitString(content, "XYZ")
```

Запустить в Playground

Результат запроса:

## startsWith

Проверяет, начинается ли строковое выражение с указанного префикса. Возвращает `true`, если да, и `false` в противном случае.

#### Синтаксис

`startsWith(expression, prefix [, caseSensitive])`

#### Параметры

#### Возвращаемое значение

Тип возвращаемого значения -- `boolean`.

#### Примеры

##### Пример 1

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language")



| fieldsAdd startsWith(content, "D"),



startsWith(content, "dql", caseSensitive: false)
```

Запустить в Playground

Результат запроса:

## stringLength

Возвращает длину строкового выражения. Длина определяется как количество кодовых единиц UTF-16, что часто совпадает с количеством символов в строке. В некоторых случаях количество символов меньше количества кодовых единиц UTF-16, например при использовании комбинирующих диакритических знаков или символов за пределами базовой многоязычной плоскости (BMP), таких как эмодзи.

Если для вашего случая использования требуется одинаковая длина для одних и тех же символов, рассмотрите возможность загрузки строк после нормализации Unicode.

Для строк, предоставляемых Dynatrace, конкретная форма нормализации не гарантируется.

#### Синтаксис

`stringLength(expression)`

#### Параметры

#### Возвращаемое значение

Тип возвращаемого значения -- `long`.

#### Примеры

##### Пример 1

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language"),



record(content = "emoji_placeholder")



| fieldsAdd stringLength(content)
```

Запустить в Playground

Результат запроса:

## substring

Получает диапазон кодовых единиц, используя начальный индекс (включительно) и конечный индекс (исключительно).

Возвращает пустую строку, если from `>=` to.

`Индексы >=0` отсчитываются относительно начала строки и обращаются к последовательным символам слева направо, начиная с позиции индекса.

`Индексы <=-1` отсчитываются относительно последнего символа строки и используются для обращения к символам с правой стороны выражения, например, `-2` -- это предпоследний символ.

`Положительные индексы`, выходящие за границы строки, приравниваются к длине строки.

`Отрицательные индексы`, выходящие за границы строки, равны `0`. Например, в строке `321` индекс `-4` выходит за границы строки, поэтому он равен `0`. Однако индекс `-2` находится в пределах границ этой строки и извлекает `21`, если используется как индекс `from`.

Возвращаемая подстрока никогда не начинается и не заканчивается неполной суррогатной парой UTF-16. Вместо этого она начинается или заканчивается вопросительным знаком. Это защищает от создания недопустимых строк Unicode.

#### Синтаксис

`substring(expression [, from] [, to])`

#### Параметры

#### Возвращаемое значение

Тип возвращаемого значения -- `string`.

#### Примеры

##### Пример 1

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language")



| fieldsAdd substring(content, from: 4),



substring(content, from: -2),



substring(content, from: 4, to: 9),



substring(content, from: -42, to: 42)
```

Запустить в Playground

Результат запроса:

## trim

Удаляет начальные и конечные пробельные символы. Любой кодовый пункт <= ASCII 32 в десятичной системе считается пробельным символом, где ASCII 32 -- это пробел.

#### Синтаксис

`trim(expression)`

#### Параметры

#### Возвращаемое значение

Тип возвращаемого значения -- `string`.

#### Примеры

##### Пример 1

```
data record(content = " DQL is awesome!"),



record(content = " Dynatrace Query Language ")



| fieldsAdd trim(content)
```

Запустить в Playground

Результат запроса:

## unescape

Возвращает деэкранированную строку.

Правила деэкранирования

1. Одинарные кавычки, двойные кавычки и обратные кавычки деэкранируются.

2. Обратные косые черты деэкранируются.

3. ASCII-символы bell, backspace, form feed, перевод строки, возврат каретки, горизонтальная табуляция и вертикальная табуляция деэкранируются.

4. `\xhh` в стандартном ASCII-пространстве (0x00 - 0x7f) заменяется соответствующим символом.

5. `\xhh` в расширенном ASCII-пространстве (0x80 - 0xff) интерпретируется как `\u00hh` и заменяется соответствующим символом Unicode.

6. `\uhhhh` заменяется соответствующим символом Unicode.

#### Синтаксис

`unescape(expression)`

#### Параметры

#### Возвращаемое значение

Тип возвращаемого значения -- `string`.

#### Примеры

##### Пример 1

```
data record(content = """"foo\x40bar\u002ecom""")



| fieldsAdd unescape(content)
```

Запустить в Playground

Результат запроса:

| content | unescape(content) |
| --- | --- |
| `"foo\x40bar\u002ecom` | `"foo@bar.com` |

## unescapeHtml

Деэкранирует HTML в строке, заменяя ASCII-символы с синтаксисом HTML.

#### Синтаксис

`unescapeHtml(expression)`

#### Параметры

#### Возвращаемое значение

Тип возвращаемого значения -- `string`.

#### Примеры

##### Пример 1

```
data record(content = "DQL is &lt;bold&gt;awesome&lt;/bold&gt;!"),



record(content = "&lt;a href=&quot;https://www.dynatrace.com/platform/grail&quot;&gt;Dynatrace Query Language&lt;/a&gt;")



| fieldsAdd unescapeHtml(content)
```

Запустить в Playground

Результат запроса:

## upper

Преобразует строку в верхний регистр.

#### Синтаксис

`upper(expression)`

#### Параметры

#### Возвращаемое значение

Тип возвращаемого значения -- `string`.

#### Примеры

##### Пример 1

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language")



| fieldsAdd upper(content)
```

Запустить в Playground

Результат запроса:

## Связанные темы

* [Dynatrace Query Language](../../dynatrace-query-language.md "How to use Dynatrace Query Language.")
* [Использование запросов DQL](../dql-guide.md "Find out how DQL works and what are DQL key concepts.")
* [Сравнение DQL с SQL и другими языками](../dql-comparison.md "See how DQL compares to other query languages.")
* [Справочник по языку DQL](../dql-reference.md "Dynatrace Query Language syntax reference.")
* [Команды DQL](../commands.md "A list of DQL commands.")
* [Операторы DQL](../operators.md "A list of DQL Operators.")
* [Типы данных DQL](../data-types.md "A list of DQL data types.")
* [Лучшие практики DQL](../dql-best-practices.md "Best practices for using Dynatrace Query Language.")
