---
title: DQL best practices
source: https://www.dynatrace.com/docs/platform/grail/dynatrace-query-language/dql-best-practices
scraped: 2026-03-06T21:23:18.368123
---

# Лучшие практики DQL

# Лучшие практики DQL

* Latest Dynatrace
* Справочник
* Обновлено 13 окт. 2025

На этой странице описаны действия, которые можно предпринять для повышения производительности запросов.

### Сужайте временной диапазон запроса

Более короткое окно анализа обеспечивает лучшую производительность на идентичных наборах данных. Используйте доступные селекторы временного диапазона, предоставляемые пользовательским интерфейсом, или напрямую укажите временной диапазон запроса в команде [fetch](/docs/platform/grail/dynatrace-query-language/commands "A list of DQL commands.").

```
fetch bizevents, from:-10m
```

### Используйте доступные возможности выборки

Grail выполняет выборку входящих данных при записи и позволяет выбирать эти разделы в команде DQL [fetch](/docs/platform/grail/dynatrace-query-language/commands "A list of DQL commands."). В зависимости от указанного значения возвращается доля (`1/<samplingRatio>`) всех доступных необработанных записей.

Допустимые значения для выборки:

* 1: Значение по умолчанию, выборка не применяется.
* 10
* 100
* 1000
* 10000

Следующий запрос использует выборку для повышения производительности запроса при наблюдении приблизительного количества спанов на вызов функции.

```
fetch spans, samplingRatio:100



| summarize c=count(), by: { span.kind, code.namespace, code.function }



| fieldsAdd c = c*100
```

### Дополнительные возможности ограничения объёма сканируемых данных

Команда DQL [fetch](/docs/platform/grail/dynatrace-query-language/commands "A list of DQL commands.") предоставляет дополнительные возможности для ограничения обработки данных:

* остановка обработки после указанного объёма данных

```
fetch logs, scanLimitGBytes:100
```

* фильтрация по определённым бакетам Grail

```
fetch logs, bucket:{"default_logs", "logs_365_*"}
```

### Рекомендуемый порядок команд

Рекомендуемый порядок команд

1. Сократите количество обрабатываемых записей, фильтруя данные с помощью, например, команд `filter` или `search`.

   * Старайтесь избегать преобразований вроде `| filter matchesValue(lower(k8s.namespace.name), "astro*")` и фильтруйте непосредственно по полю: `| filter k8s.namespace.name ~ "astro*"`.
   * Для текстового поиска используйте сопоставление по словам или фразам: `| filter content ~ "refused"`
   * Старайтесь использовать включающие фильтры и избегайте отрицаний, таких как `| filter not k8s.namespace.name ~ "astro*"`
   * Избегайте `join` и `lookup` для фильтрации, если это не необходимо. Рекомендуется фильтрация по обогащённым полям.
2. Определите объём обрабатываемых данных, выбирая поля на ранних этапах с помощью команд `fields`, `fieldsKeep` или `fieldsRemove`.
3. Обработайте полученный набор данных для достижения требуемого результата. Как правило, используются непреобразующие команды, такие как `fieldsAdd`, `parse`, `append`.
4. Агрегируйте набор данных с помощью команды `summarize` для создания табличного результата и `maketimeseries`, если требуется временной график. Не используйте `limit` перед агрегацией данных, чтобы избежать неправильных агрегатов, если это не сделано намеренно.

**Пример**

Применение описанных выше практик приводит к следующему шаблону:

```
fetch logs, bucket:{"astroshop_log_*"}, from:-1d@d, samplingRatio:10



| filter loglevel=="ERROR" and k8s.namespace.name ~ "astroshop"



| filter content ~ "error"



| summarize c=count(), by:pod.name



| sort c desc



| limit 5
```

Рекомендуется размещать `sort` в конце запроса. Сортировка сразу после `fetch` с продолжением запроса снизит производительность.

**Примеры**

Этот пример показывает запрос, где `sort` размещён сразу после `fetch`.

Рекомендуется размещать `sort` в конце запроса. Сортировка сразу после `fetch` с продолжением запроса снизит производительность. Пример:

```
fetch logs



| sort timestamp desc



| filter content ~ "error"
```

Этот пример показывает рекомендуемый порядок с `sort` в конце запроса.

```
fetch logs



| filter content ~ "error"



| sort timestamp desc
```

Вы можете повторять одну и ту же команду в одном запросе, придерживаясь рекомендуемого порядка. В примере ниже сначала фильтруется полученное содержимое, затем снова фильтруется разобранное содержимое, но команда `sort` и функция `summarize` сохраняют свои позиции:

```
fetch logs, bucket:{"astroshop_log_*"}, from:-1d@d, samplingRatio:10



| filter loglevel == "ERROR" and k8s.namespace.name ~ "astroshop"



| parse content, "ipaddr:ip ld ' POST ' ld:action ' HTTP/1.1 ' long:status ld"



| filter action == "/cart" or action == "/cart/checkout"



| summarize count = count(), by:{ ip, log.source }



| sort count desc
```

### Используйте сравнение строк с осторожностью

* Используйте `==` или `!=`, когда значение поля известно.

  ```
  fetch logs



  | filter k8s.container.name == "coredns"
  ```
* Используйте `~`, когда значение поля известно лишь частично или неизвестно.

  ```
  fetch logs



  | filter k8s.container.name ~ "core*"
  ```

### Имена полей, которых следует избегать или использовать в обратных кавычках

Не рекомендуется использовать следующие восемь зарезервированных ключевых слов в качестве идентификаторов полей (имён полей) или измерений:

* true
* false
* null
* mod
* and
* or
* xor
* not

Тем не менее, вы можете использовать эти слова в качестве имён полей, идентификаторов и измерений, если заключите их в обратные кавычки ('`').

Например, если у вас есть измерение с именем 'true':

```
...



| fields x = true // создаёт логическое поле, которое всегда истинно
```

```
...



| fields x = `true` // позволяет обратиться к пользовательскому измерению с именем 'true'
```

Аналогично, если вам нужно отсортировать по полю с именем 'not':

```
...



| sort not desc // сортирует по логическому значению измерения `desc`
```

```
...



| sort `not` desc // сортирует по убыванию по полю с именем `not`
```

## Связанные темы

* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Использование запросов DQL](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.")
* [Сравнение DQL с SQL и другими языками](/docs/platform/grail/dynatrace-query-language/dql-comparison "See how DQL compares to other query languages.")
* [Справочник по языку DQL](/docs/platform/grail/dynatrace-query-language/dql-reference "Dynatrace Query Language syntax reference.")
* [Команды DQL](/docs/platform/grail/dynatrace-query-language/commands "A list of DQL commands.")
* [Функции DQL](/docs/platform/grail/dynatrace-query-language/functions "A list of DQL functions.")
* [Операторы DQL](/docs/platform/grail/dynatrace-query-language/operators "A list of DQL Operators.")
* [Типы данных DQL](/docs/platform/grail/dynatrace-query-language/data-types "A list of DQL data types.")
