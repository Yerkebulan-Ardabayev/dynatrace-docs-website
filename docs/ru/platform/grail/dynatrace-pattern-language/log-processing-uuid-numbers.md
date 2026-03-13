---
title: DPL — Универсальные уникальные идентификаторы
source: https://www.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/log-processing-uuid-numbers
scraped: 2026-03-06T21:25:46.961981
---

# DPL — Универсальные уникальные идентификаторы

# DPL — Универсальные уникальные идентификаторы

* Последняя Dynatrace
* Справочник
* Опубликовано 17 января 2023 г.

Сопоставляет корректные универсальные уникальные идентификаторы (UUID), например номера социального страхования. Создаёт парсер строк UUID.

### Пример

```
This is a string with UUID b79cb3ba-745e-5d9a-8903-4a02327a7e09 somewhere in the middle
```

Шаблон:

```
UUIDSTRING:uuid LD
```

Результат разбора: UUID извлекается из строки.