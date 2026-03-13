---
title: Dynatrace Intelligence DQL examples
source: https://www.dynatrace.com/docs/dynatrace-intelligence/use-cases/davis-dql-examples
scraped: 2026-03-06T21:20:33.076571
---

# Примеры DQL для Dynatrace Intelligence

# Примеры DQL для Dynatrace Intelligence

* Latest Dynatrace
* Reference
* 7-min read
* Updated on Jan 28, 2026

Эти примеры демонстрируют, как создавать мощные и гибкие дашборды состояния здоровья среды, используя DQL для анализа и группировки всех проблем и событий, обнаруженных Dynatrace Intelligence.

Проблемы Davis представляют результаты, полученные в ходе анализа корневых причин Dynatrace Intelligence. В Grail проблемы Davis и их обновления хранятся как события Grail.

* [Пример проблемы 1](/docs/dynatrace-intelligence/use-cases/davis-dql-examples#lpproblemexample1 "Build powerful health dashboards by slicing and dicing of Dynatrace Intelligence reported problems and events using DQL.")
  Подсчёт общего количества проблем за последние 24 часа.
* [Пример проблемы 2](/docs/dynatrace-intelligence/use-cases/davis-dql-examples#lpproblemexample2 "Build powerful health dashboards by slicing and dicing of Dynatrace Intelligence reported problems and events using DQL.")
  Подсчёт текущего количества активных проблем.
* [Пример проблемы 3](/docs/dynatrace-intelligence/use-cases/davis-dql-examples#lpproblemexample3 "Build powerful health dashboards by slicing and dicing of Dynatrace Intelligence reported problems and events using DQL.")
  Построение графика количества проблем за последние 7 дней для выявления тенденции стабильности вашей среды.
* [Пример проблемы 4](/docs/dynatrace-intelligence/use-cases/davis-dql-examples#lpproblemexample4 "Build powerful health dashboards by slicing and dicing of Dynatrace Intelligence reported problems and events using DQL.")
  Определение топ-10 сущностей, затронутых проблемами, в вашей среде.
* [Пример проблемы 5](/docs/dynatrace-intelligence/use-cases/davis-dql-examples#lpproblemexample5 "Build powerful health dashboards by slicing and dicing of Dynatrace Intelligence reported problems and events using DQL.")
  Объединение атрибутов сущностей с обнаруженными проблемами и применение фильтра по имени.
* [Пример проблемы 6](/docs/dynatrace-intelligence/use-cases/davis-dql-examples#lpproblemexample6 "Build powerful health dashboards by slicing and dicing of Dynatrace Intelligence reported problems and events using DQL.")
  Загрузка последнего состояния данной проблемы.
* [Пример проблемы 7](/docs/dynatrace-intelligence/use-cases/davis-dql-examples#lpproblemexample7 "Build powerful health dashboards by slicing and dicing of Dynatrace Intelligence reported problems and events using DQL.")
  Загрузка всех активных проблем с исключением помеченных как дубликаты.
* [Пример проблемы 8](/docs/dynatrace-intelligence/use-cases/davis-dql-examples#lpproblemexample8 "Build powerful health dashboards by slicing and dicing of Dynatrace Intelligence reported problems and events using DQL.")
  Расчёт среднего времени устранения проблем с течением времени.
* [Пример проблемы 9](/docs/dynatrace-intelligence/use-cases/davis-dql-examples#lpproblemexample9 "Build powerful health dashboards by slicing and dicing of Dynatrace Intelligence reported problems and events using DQL.")
  Отображение графика одновременно открытых проблем с течением времени.

События Davis представляют необработанные события, поступающие из различных пользовательских оповещений в Dynatrace или из OneAgent. Примерами являются события насыщения CPU, обнаруженные OneAgent, или события высокого времени сборки мусора.

* [Пример события Davis 1](/docs/dynatrace-intelligence/use-cases/davis-dql-examples#lpdaviseventexample1 "Build powerful health dashboards by slicing and dicing of Dynatrace Intelligence reported problems and events using DQL.")
  Построение графика количества событий перезапуска процессов за последние 7 дней.

## Подсчёт общего количества проблем за последние 24 часа

* Извлекает таблицу `dt.davis.problems`.
* Использует команду DQL summarize для получения общего количества уникальных проблем.
* Поле `event.id` содержит уникальный идентификатор проблемы, который остаётся стабильным при всех обновлениях, которые Dynatrace Intelligence сообщает для одной и той же проблемы.

```
fetch dt.davis.problems, from:now()-24h, to:now()



| summarize {problemCount = countDistinct(event.id)}
```

**Результат запроса**

## Подсчёт текущего количества уникальных активных проблем

* Извлекает таблицу `dt.davis.problems`.
* Группирует результат по уникальному полю `event.id`, содержащему идентификатор проблемы.
* Отфильтровывает все проблемы, которые больше не находятся в состоянии `ACTIVE`. Для этого команда DQL `takeLast` по полю `event.status` получает последнее состояние.

```
fetch dt.davis.problems



| filter event.status == "ACTIVE"



| summarize {activeProblems = countDistinct(event.id)}
```

**Результат запроса**

## Построение графика количества проблем за последние 7 дней

* Извлекает таблицу `dt.davis.problems`.
* Показывает количество проблем, произошедших в течение дня, за период 7 дней.
* Подсчитывает с разрешением в 6-часовые интервалы.
* Позволяет выявить тенденции стабильности вашей среды.

```
fetch dt.davis.problems, from:now()-7d



| makeTimeseries count(default:0)
```

**Результат запроса**

## Определение топ-3 сущностей, затронутых проблемами, в вашей среде

* Извлекает таблицу `dt.davis.problems`.
* Разворачивает поле-массив, содержащий идентификаторы всех затронутых сущностей, в отдельные поля.
* Подсчитывает все уникальные проблемы, сгруппированные по идентификаторам затронутых сущностей.
* Сортирует по количеству проблем.
* Возвращает топ-3 идентификатора сущностей.

```
fetch dt.davis.problems



| expand affected_entity_ids



| summarize count = countDistinct(display_id), by:{affected_entity_ids}



| sort count, direction:"descending"



| limit 3
```

**Результат запроса**

## Получение всех проблем для хоста с именем "myhost"

Этот пример объединяет атрибуты сущностей для фильтрации всех проблем по заданному имени хоста.

* Извлекает таблицу `dt.davis.problems`.
* Разворачивает поле-массив, содержащий идентификаторы всех затронутых сущностей, в отдельные поля.
* Выполняет поиск по топологии и сущностям по полю `affected_entity_ids`.
* Обогащает полученные записи двумя полями сущности с префиксом `host.`: `host.id` и `host.name`.
* Применяет фильтр по имени хоста `myhost`.

```
fetch dt.davis.problems



| expand affected_entity_ids



| fieldsAdd host.name = entityName(affected_entity_ids, type: "dt.entity.host")



| filter host.name == "myhost"
```

**Результат запроса**

## Загрузка последнего состояния данной проблемы

Этот пример показывает, как фильтровать проблемы по уникальному идентификатору.

* Извлекает таблицу `dt.davis.problems`.
* Фильтрует по уникальному отображаемому идентификатору проблемы.
* Позволяет найти проблемы, связанные с определённым идентификатором.

```
fetch dt.davis.problems



| filter display_id == "P-24051200"
```

**Результат запроса**

## Загрузка всех активных проблем с исключением помеченных как дубликаты

Этот пример показывает, как получить все активные проблемы, которые не были помечены как дубликаты.

Поскольку флаг дубликата появляется в ходе жизненного цикла проблемы, события обновления необходимо отсортировать по метке времени. Затем события нужно агрегировать, взяв последнее состояние полей duplicate и status. Корректно применить фильтр можно только после сортировки событий по метке времени.

* Извлекает таблицу `dt.davis.problems`.
* Отфильтровывает проблемы, помеченные как дубликаты.
* Отфильтровывает проблемы, которые уже закрыты.

```
fetch dt.davis.problems



| filter event.status == "ACTIVE" and not dt.davis.is_duplicate == "true"
```

**Результат запроса**

## Расчёт среднего времени устранения проблем с течением времени

Этот пример показывает, как рассчитать среднее время, необходимое для устранения всех обнаруженных проблем, путём суммирования разницы между началом и концом каждой проблемы с течением времени.

* Извлекает таблицу `dt.davis.problems`.
* Разворачивает поля проблемы в запись.
* Отфильтровывает все частые и дублирующиеся проблемы.
* Возвращает все закрытые проблемы.
* Преобразует значения во временной ряд средних значений с течением времени.

```
fetch dt.davis.problems, from:now()-7d



| filter event.status == "CLOSED"



| filter dt.davis.is_frequent_event == false and dt.davis.is_duplicate == false and maintenance.is_under_maintenance == false



| makeTimeseries `AVG Problem duration in hours` = avg(toLong(resolved_problem_duration)/3600000000000.0), time:event.end
```

## Отображение графика одновременно открытых проблем с течением времени

Этот пример показывает, как создать график, отображающий количество одновременно открытых проблем с течением времени. Пробелы в разрешении заполняются командой `spread`.

* Извлекает таблицу `dt.davis.problems`.
* Создаёт временной ряд подсчёта проблем.
* Заполняет промежутки между метками времени начала и конца проблемы корректным подсчётом с помощью команды `spread`.

```
fetch dt.davis.problems



| makeTimeseries count = count(), spread: timeframe(from: event.start, to: coalesce(event.end, now()))
```

## Построение графика количества событий насыщения CPU и высокого потребления памяти за последние 7 дней

* Извлекает таблицу `dt.davis.events` за последние 7 дней.
* Подсчитывает с разрешением в 60-минутные интервалы.

```
fetch dt.davis.events, from:now()-7d, to:now()



| filter event.kind == "DAVIS_EVENT"



| filter event.type == "OSI_HIGH_CPU" or event.type == "OSI_HIGH_MEMORY"



| makeTimeseries count =  count(default: 0)
```

**Результат запроса**
