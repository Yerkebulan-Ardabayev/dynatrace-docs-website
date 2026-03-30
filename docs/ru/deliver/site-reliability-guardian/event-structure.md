---
title: Структура события Site Reliability guardian
source: https://www.dynatrace.com/docs/deliver/site-reliability-guardian/event-structure
scraped: 2026-03-05T21:35:41.303232
---

# Структура событий Site Reliability Guardian

Для каждой валидации записываются: одно событие **started**, одно **finished** и `n` событий **objective** (по одному на объектив).

## Lifecycle guardian (события SDLC)

Базовый запрос:

```
fetch events
| filter event.kind == "SDLC_EVENT"
| filter event.provider == "dynatrace.site.reliability.guardian"
```

Типы событий:

**validation started:**
```
fetch events
| filter event.kind == "SDLC_EVENT"
| filter event.provider == "dynatrace.site.reliability.guardian"
| filter event.type == "validation"
| filter event.status == "started"
```

**validation finished:**
```
fetch events
| filter event.kind == "SDLC_EVENT"
| filter event.provider == "dynatrace.site.reliability.guardian"
| filter event.type == "validation"
| filter event.status == "finished"
```

**validation.objective:**
```
fetch events
| filter event.kind == "SDLC_EVENT"
| filter event.provider == "dynatrace.site.reliability.guardian"
| filter event.type == "validation.objective"
```

Данные guardian хранятся с префиксом `dt.srg.`. Структура полей соответствует Семантическому словарю для событий SDLC.

## Business guardian (бизнес-события)

Базовый запрос:

```
fetch bizevents
| filter event.provider == "dynatrace.site.reliability.guardian"
```

Типы событий:

**guardian.validation.started:**
```
fetch bizevents
| filter event.provider == "dynatrace.site.reliability.guardian"
| filter event.type == "guardian.validation.started"
```

**guardian.validation.finished:**
```
fetch bizevents
| filter event.provider == "dynatrace.site.reliability.guardian"
| filter event.type == "guardian.validation.finished"
```

**guardian.validation.objective:**
```
fetch bizevents
| filter event.provider == "dynatrace.site.reliability.guardian"
| filter event.type == "guardian.validation.objective"
```

Подробности полей событий см. в документации для интеграции с дашбордами и другими инструментами.
