---
title: Руководство по оптимизации DQL для обнаружения аномалий
source: https://www.dynatrace.com/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app/davis-ad-dql-optimization
scraped: 2026-03-05T21:38:33.126042
---

Лучшие практики оптимизации DQL-запросов для пользовательских оповещений Anomaly Detection.

## Минимизация объёма сканируемых данных

Оптимизируйте все DQL-запросы для улучшения производительности и возможности настроить больше оповещений.

## Правильное управление хранилищем

Организуйте [бакеты Grail](../../../platform/grail/organize-data.md#built-in-grail-buckets) по паттернам использования команд для предотвращения избыточного сканирования.

## Правила оптимизации через фильтры DQL

### Правило 1: Всегда используйте фильтр `bucket`

Направляет Grail на конкретные хранилища вместо сканирования всего.

```
fetch logs,bucket:{"bucketname"}
fetch spans, bucket:{"bucketname"}
fetch events, bucket:{"bucketname"}
```

Определить бакет-источник:

```
fetch logs
| fieldsAdd dt.system.bucket
```

### Правило 2: Фильтруйте как можно раньше

Исключайте нерелевантные данные сразу после `fetch` для минимизации обработки.

### Правило 3: Эффективное сопоставление строк

**Сравнение для известных значений** (наиболее эффективно):
```
| filter field == "value"
```

**Сопоставление на основе токенов** -- Grail разбивает текст на токены. `matchesPhrase()` использует токенное сопоставление и эффективнее `contains()`:
```
| filter matchesPhrase(message, "error")
```

Оператор `~` -- аналог `matchesPhrase()` для вложенных записей и массивов:
```
| filter message~"err" and http.response~504
fetch spans | filter span.events~"err"
```

**Советы по поиску в записях:** Указывайте поле для фильтрации. Приоритет:
1. Пары ключ-значение: `| filter http.response==504 and status=="ERROR"`
2. Поиск по полю: `| filter message~"504"`
3. `matchesPhrase`: `| filter matchesPhrase(message,"504")`

**Частичное сопоставление** (`startsWith`, `contains`) -- менее эффективно, используйте совместно с:
* Фильтром по бакету
* Фильтрами по ресурсам (`dt.entity.<field> == "name"`)
* Хотя бы одним токенным фильтром

## Связанные темы

* Приложение Anomaly Detection
* Dynatrace Query Language
* Руководство по написанию DQL для обнаружения аномалий
