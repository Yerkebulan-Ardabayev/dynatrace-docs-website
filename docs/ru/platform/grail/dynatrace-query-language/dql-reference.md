---
title: DQL language reference
source: https://www.dynatrace.com/docs/platform/grail/dynatrace-query-language/dql-reference
scraped: 2026-03-06T21:20:36.484418
---

# Справочник по языку DQL

# Справочник по языку DQL

* Latest Dynatrace
* Справочник
* Обновлено 6 ноября 2025 г.

Запрос DQL содержит одну или несколько [команд](/docs/platform/grail/dynatrace-query-language/commands "Список команд DQL."), каждая из которых возвращает табличный результат, содержащий записи (строки) и поля (столбцы). Все команды последовательно соединяются символом | (pipe). Данные передаются (или «пайпятся») от одной команды к следующей. На каждом шаге данные фильтруются или обрабатываются, а затем передаются на следующий шаг.

## Синтаксис DQL

Синтаксис можно описать следующим образом:

`command parameter,.. [, optionalparameter],... | command ...`

Синтаксически корректный пример запроса DQL:

```
fetch bizevents | summarize count()
```

Команда DQL состоит из обязательных и необязательных параметров, разделённых запятыми:

`summarize [field=] aggregation [, ...] [, by:{ [field=] groupexpression [, ...]}]`

* Обязательные параметры

  + aggregation
* Необязательные параметры

  + field
  + groupexpression

Обязательным параметром является `aggregation`. Для синтаксической корректности команды необходимо указать хотя бы один вызов [функции агрегации](/docs/platform/grail/dynatrace-query-language/functions#aggregation-functions "Список функций DQL.").

```
| summarize count()
```

Необязательно, присвоение с помощью знака равенства `(=)` переопределяет имя поля по умолчанию с `count()` на `event_count`.

```
| summarize event_count = count()
```

Необязательный параметр `by:` определяет список `groupexpression`. Результат будет содержать столько записей, сколько существует уникальных значений всех `groupexpression`.

```
| summarize event_count = count(), by:{country=client.loc_cc, customer}
```

## Правила именования полей

Проверка синтаксиса DQL применяет следующие правила именования:

![Пример запроса DQL, демонстрирующий использование команды, параметров и идентификаторов полей.](https://dt-cdn.net/images/dql-ref-2418-19b3237798.png)

* Имена полей могут содержать любую последовательность символов Unicode.
* Имена полей, содержащие символы, отличные от `a-zA-Z0-9_.`, должны быть заключены в обратные кавычки.
* Имена полей, начинающиеся с символа, отличного от `a-zA-Z_`, должны быть заключены в обратные кавычки.
* Обратная косая черта `\` используется как символ экранирования.
* Обратные кавычки и обратные косые черты в имени поля необходимо экранировать.

Примеры допустимых имён полей:

* `dt.entity.host`
* `location_US_EAST_1`
* `` `my host*` `` — должно быть заключено в обратные кавычки
* `` `LOCAL_MACHINE\\Software` `` — используется одинарная обратная косая черта в имени поля

## Параметры

Параметры команд или функций должны разделяться запятой. Необязательные параметры должны быть именованными.

Параметры могут быть:

* значением или выражением (например: `now()-1h`)
* блоком выполнения (например: `[fetch logs]`). Блок выполнения содержит подзапрос.
* группой параметров (см. ниже)

### Группы параметров

Если несколько параметров, обязательных или необязательных, связаны между собой, их следует группировать с помощью фигурных скобок (`{}`). Это особенно важно, если группа является именованной. Использование фигурных скобок не влияет на тип данных. Если вы решите группировать параметры, вы не сможете использовать с ними [операторы DQL](/docs/platform/grail/dynatrace-query-language/operators "Список операторов DQL.").

Пример ниже показывает две группы параметров. Первая группа содержит агрегации (без имени), а вторая — поля, по которым выполняется суммаризация (`by:`).

```
| summarize {min(value), max(value)}, by:{field1, field2}
```

## Последовательная обработка данных

Следующий запрос DQL использует семь шагов конвейера для перехода от необработанных данных логов к агрегированной таблице, показывающей статистику производительности выполнения задач.

![Пример запроса DQL, демонстрирующий использование команды, функции, параметров и выражения.](https://dt-cdn.net/images/new-dql-query-3-1763-7b83cbcf34.png)

* **Строка 1**

  ```
  fetch       logs, from:now()-10m
  ```

  Вы извлекаете данные логов с помощью команды [`fetch`](/docs/platform/grail/dynatrace-query-language/commands/data-source-commands#fetch "Команды источников данных DQL"). Кроме того, необязательный параметр `from:` указывает начальную метку времени запроса.
* **Строка 2**

  ```
  // fetched all logs from the last hour: now() - 1h to now()
  ```

  Закомментированная строка. Эта строка будет пропущена при выполнении запроса.
* **Строка 3**

  ```
  | filter    endsWith(log.source, "pgi.log")
  ```

  Команда [`filter`](/docs/platform/grail/dynatrace-query-language/commands/filtering-commands#filter "Команды фильтрации и поиска DQL") фильтрует записи логов на основе функции [`endsWith`](/docs/platform/grail/dynatrace-query-language/functions/string-functions#endsWith "Список строковых функций DQL."), которая извлекает файлы логов, имена которых заканчиваются заданной строкой (строка `pgi.log`).
* **Строка 4**

  ```
  | parse     content, "LD IPADDR:ip ':' LONG:payload SPACE LD 'HTTP_STATUS' SPACE INT:http_status  LD (EOL| EOS)"
  ```

  Мы используем команду [`parse`](/docs/platform/grail/dynatrace-query-language/commands/extraction-and-parsing-commands#parse "Команды извлечения DQL") для извлечения пар ключ-значение, содержащих статистику выполнения, из необработанной текстовой строки лога. В данном случае она добавляет поля `IP address`, `payload` и `http_status` к результату и преобразует их типы данных в требуемые форматы.
* **Строки 5, 6, 7, 8**

  ```
  | summarize total_payload = sum(payload),



  failedRequests = countIf(http_status >= 400),



  successfulRequests = countIf(http_status < 400),



  by:{ip, host.name}
  ```

  Команда [`summarize`](/docs/platform/grail/dynatrace-query-language/commands/aggregation-commands#summarize "Команды агрегации DQL") является ключевым элементом DQL, поскольку позволяет выполнять множественные агрегации по одному или нескольким полям. Этот запрос группирует результаты по `ip` и `host.name`. Полученные записи включают общее значение payload, вычисленное с помощью функции [`sum`](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#sum "Список функций агрегации DQL."), и два столбца, вычисленных с помощью функции [`countif`](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#countIf "Список функций агрегации DQL."):

  + столбец с количеством неудачных запросов (определяемых как запросы с `http_status` >=400)
  + столбец с количеством успешных запросов (определяемых как запросы с `http_status` <400)
    Этот запрос группирует полученные записи по `ip` и `host.name`.
* **Строка 9**

  ```
  |fieldsAdd total_payload_MB = total_payload/1000000
  ```

  С помощью команды [`fieldsAdd`](/docs/platform/grail/dynatrace-query-language/commands#fields-add "Список команд DQL.") вы добавляете новое поле, показывающее общий payload, преобразованный в мегабайты, на основе математического выражения.
* **Строка 10**

  ```
  |fields    ip, host.name, failedRequests, successfulRequests, total_payload_MB
  ```

  С помощью команды [`fields`](/docs/platform/grail/dynatrace-query-language/commands/selection-and-modification-commands#fields "Команды выбора и модификации DQL") вы определяете, какие поля необходимо извлечь.
* **Строка 11**

  ```
  | sort  failedRequests desc
  ```

  Команда [`sort`](/docs/platform/grail/dynatrace-query-language/commands/ordering-commands#sort "Команды сортировки DQL") используется для финализации результата. В данном случае результаты сортируются по количеству неудачных запросов от наибольшего к наименьшему.

## Основные строительные блоки DQL

* [Команды](/docs/platform/grail/dynatrace-query-language/commands "Список команд DQL.")
* [Функции](/docs/platform/grail/dynatrace-query-language/functions "Список функций DQL.")
  Функции могут использоваться для выполнения любых необходимых вычислений над полями [команд DQL](/docs/platform/grail/dynatrace-query-language/commands "Список команд DQL.").

* [Типы данных](/docs/platform/grail/dynatrace-query-language/data-types "Список типов данных DQL.")
  Dynatrace Query Language работает со строго типизированными данными: функции и операторы принимают только объявленные типы данных. Тип присваивается данным при разборе или с помощью функций приведения типов. DQL также распознаёт типы значений, выраженные в литеральной нотации (например, использование константных значений в функциях).

## Связанные темы

* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "Как использовать Dynatrace Query Language.")
* [Использование запросов DQL](/docs/platform/grail/dynatrace-query-language/dql-guide "Узнайте, как работает DQL и каковы ключевые концепции DQL.")
* [Сравнение DQL с SQL и другими языками](/docs/platform/grail/dynatrace-query-language/dql-comparison "Сравнение DQL с другими языками запросов.")
* [Команды DQL](/docs/platform/grail/dynatrace-query-language/commands "Список команд DQL.")
* [Функции DQL](/docs/platform/grail/dynatrace-query-language/functions "Список функций DQL.")
* [Операторы DQL](/docs/platform/grail/dynatrace-query-language/operators "Список операторов DQL.")
* [Типы данных DQL](/docs/platform/grail/dynatrace-query-language/data-types "Список типов данных DQL.")
* [Лучшие практики DQL](/docs/platform/grail/dynatrace-query-language/dql-best-practices "Лучшие практики использования Dynatrace Query Language.")
