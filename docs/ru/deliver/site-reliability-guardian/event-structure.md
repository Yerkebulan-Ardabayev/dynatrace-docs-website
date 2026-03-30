---
title: Структура события Site Reliability guardian
source: https://www.dynatrace.com/docs/deliver/site-reliability-guardian/event-structure
scraped: 2026-03-05T21:35:41.303232
---

# Структура событий Site Reliability guardian

# Структура событий Site Reliability guardian


В зависимости от типа [guardian](../site-reliability-guardian.md#guardian "Автоматически проверяйте цели производительности, доступности и емкости ваших критически важных сервисов для принятия правильного решения о релизе.") — [Lifecycle guardian](../site-reliability-guardian.md#lifecycle-guardian "Автоматически проверяйте цели производительности, доступности и емкости ваших критически важных сервисов для принятия правильного решения о релизе.") или [Business guardian](../site-reliability-guardian.md#business-guardian "Автоматически проверяйте цели производительности, доступности и емкости ваших критически важных сервисов для принятия правильного решения о релизе.") — базовая структура событий различается.
Количество событий, записываемых Site Reliability guardian, одинаково, независимо от типа.
Для каждой валидации записываются одно событие **started** (начало), одно событие **finished** (завершение) и `n` событий **objective** (целевой показатель) — по одному для каждого целевого показателя соответствующего guardian.

## Lifecycle guardian (события SDLC)

Для запроса событий [Lifecycle guardian](../site-reliability-guardian.md#lifecycle-guardian "Автоматически проверяйте цели производительности, доступности и емкости ваших критически важных сервисов для принятия правильного решения о релизе.") с помощью DQL используйте следующий запрос:

```
fetch events


| filter event.kind == "SDLC_EVENT"


| filter event.provider == "dynatrace.site.reliability.guardian"
```

Существует два различных типа событий: `validation` и `validation.objective`.
Для типа событий `validation` есть два дополнительных подтипа в зависимости от статуса события: `started` и `finished`.

validation started

validation finished

validation.objective

Для запроса событий Lifecycle guardian `validation` `started` используйте следующий DQL-запрос:

```
fetch events


| filter event.kind == "SDLC_EVENT"


| filter event.provider == "dynatrace.site.reliability.guardian"


| filter event.type == "validation"


| filter event.status == "started"
```

Для запроса событий Lifecycle guardian `validation` `finished` используйте следующий DQL-запрос:

```
fetch events


| filter event.kind == "SDLC_EVENT"


| filter event.provider == "dynatrace.site.reliability.guardian"


| filter event.type == "validation"


| filter event.status == "finished"
```

Для запроса событий Lifecycle guardian `validation.objective` используйте следующий DQL-запрос:

```
fetch events


| filter event.kind == "SDLC_EVENT"


| filter event.provider == "dynatrace.site.reliability.guardian"


| filter event.type == "validation.objective"
```

Перечисленные выше события жизненного цикла имеют несколько общих полей.
Все данные, связанные с внутренней логикой guardian, хранятся с префиксом `dt.srg.`.
Структура остальных полей событий соответствует Семантическому словарю для событий валидации жизненного цикла разработки ПО.").

### Поля событий Lifecycle guardian

Если вы хотите интегрировать результаты валидации Lifecycle guardian с дашбордом или другими инструментами, которые вы создали, приведенные ниже поля событий станут хорошей отправной точкой для ваших запросов.

## Business guardian (бизнес-события)

Для запроса событий Business guardian с помощью DQL используйте следующий запрос:

```
fetch bizevents


| filter event.provider == "dynatrace.site.reliability.guardian"
```

Вы увидите три различных типа событий: `guardian.validation.started`, `guardian.validation.finished` и `guardian.validation.objective`.

guardian.validation.started

guardian.validation.finished

guardian.validation.objective

Для запроса событий Business `guardian.validation.started` используйте следующий DQL-запрос:

```
fetch bizevents


| filter event.provider == "dynatrace.site.reliability.guardian"


| filter event.type == "guardian.validation.started"
```

Для запроса событий Business `guardian.validation.finished` используйте следующий DQL-запрос:

```
fetch bizevents


| filter event.provider == "dynatrace.site.reliability.guardian"


| filter event.type == "guardian.validation.finished"
```

Для запроса событий Business `guardian.validation.objective` используйте следующий DQL-запрос:

```
fetch bizevents


| filter event.provider == "dynatrace.site.reliability.guardian"


| filter event.type == "guardian.validation.objective"
```

Перечисленные выше бизнес-события имеют несколько общих полей.

### Поля событий Business guardian

Если вы хотите интегрировать результаты валидации Business guardian с дашбордом или другими инструментами, которые вы создали, приведенные ниже поля событий станут хорошей отправной точкой для ваших запросов.
