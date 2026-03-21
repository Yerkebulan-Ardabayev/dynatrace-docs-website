---
title: DPL Positional Matchers
source: https://www.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/log-processing-positional-matchers
scraped: 2026-03-05T21:39:17.344467
---

# DPL: позиционные сопоставители


* Latest Dynatrace

## Начало строки

**BOS, BOF**

Совпадает с началом строки.

#### Пример

Извлечение первой строки из строки:

```
"name";"age"


Homer Simpson;40


Charles Montgomery Burns;104
```

```
BOF LD:header EOL;
```

В результате первая строка разбирается в поле `header`. Разбор последующих строк завершается неудачей, так как они не начинаются с маркера начала файла.

| header |
| --- |
| `''name'';''age''` |
|  |

## Середина строки

**MOS, MOF**

Совпадает с любыми байтами в середине строки.

#### Пример

Извлечение записей после первой строки в строке:

```
"name";"age"


Homer Simpson;40


Charles Montgomery Burns;104
```

```
MOF LD:name ';' INT:age EOL
```

В результате строки 2 и 3 разбираются в поля `name` и `age`. Строка 1 не разбирается, так как начинается с маркера начала строки.

| name | age |
| --- | --- |
|  | `-1` |
| `Homer Simpson` | `40` |
| `Charles Montgomery Burns` | `40` |

## Конец строки

**EOS, EOF**

Совпадает с концом строки.

#### Пример

Извлечение последней строки из строки:

```
"name";"age"


Homer Simpson;40


Charles Montgomery Burns;104


total:2 persons, average age: 72 years
```

Следующий шаблон совпадает только тогда, когда последняя строка следует за маркером конца строки:

```
LD:footer EOS
```

В результате последняя строка извлекается в поле `footer`. Первые три строки не разбираются, так как они не являются последними в строке.

| footer |
| --- |
|  |
| `total:2 persons, average age: 72 years` |
