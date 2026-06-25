---
title: Глобальные условия политик
source: https://docs.dynatrace.com/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-global-conditions
scraped: 2026-05-12T11:49:52.174517
---

# Глобальные условия политик

# Глобальные условия политик

* Reference
* 4-min read
* Published Jul 22, 2022

Глобальные условия (с префиксом `global:`) — это условия, которые можно применять к любому оператору политики, поскольку они не привязаны к конкретному сервису. Условия, специфичные для каждого сервиса, описаны в [Справочнике политик IAM](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Полный справочник политик IAM и соответствующих условий для всех сервисов Dynatrace.").

## Условия окружения и пользователя

### global:environmentId

Глобальное условие `global:environmentId` возвращает environmentId для сервисов в области видимости окружения.

### global:userGroup

Глобальное условие `global:userGroup` возвращает список идентификаторов групп, в которые входит пользователь.

#### Примеры

Данная политика предоставляет пользователям доступ к определённому идентификатору окружения. Это может быть полезно, если политику необходимо назначить на уровне кластера. В качестве альтернативы эту ситуацию можно разрешить, назначив безусловную политику на уровне окружения.

```
ALLOW environment:roles:viewer WHERE global:environmentId = "130fc95d-8917-4305-b5dc-4c96190ec6ac";
```

Данная политика предоставляет пользователям доступ только в том случае, если они являются членами групп, указанных в политике. Используйте этот подход, если необходимо иметь ограниченное количество политик для управления доступом.

```
ALLOW environment:roles:viewer WHERE global:userGroup = "basic-monitoring-access";
```

## Глобальные условия по дате и времени

Ниже приведены простые примеры работы с условиями на основе времени в операторах политик.

### global:date

Глобальное условие `global:date` используется следующим образом.

```
ALLOW service:resource:permission WHERE global:date > "2022-05-03Z" AND global:date < "2022-05-05Z";
```

В этом примере политика предоставляет доступ 4 мая 2022 года в часовом поясе UTC.

Операторы: `<`, `>`, `=`

Подробные сведения о форматах даты и времени см. в разделе [Форматы даты и времени](#date-and-time-formats) ниже.

### global:date-time

Глобальное условие `global:date-time` используется следующим образом.

```
ALLOW service:resource:permission WHERE global:date-time > "2022-05-03T05:00:00+01:00";
```

Операторы: `<`, `>`

Подробные сведения о форматах даты и времени см. в разделе [Форматы даты и времени](#date-and-time-formats) ниже.

### global:time-of-day

Глобальное условие `global:time-of-day` используется следующим образом.

```
ALLOW service:resource:permission WHERE global:time-of-day > "09:00+01:00" AND global:time-of-day < "17:00+01:00";
```

Операторы: `<`, `>`

Подробные сведения о форматах даты и времени см. в разделе [Форматы даты и времени](#date-and-time-formats) ниже.

### global:week-day

Глобальное условие `global:week-day` используется следующим образом.

```
ALLOW service:resource:permission WHERE global:week-day = "Monday";
```

Операторы: `=`, `!=`, `IN`

Подробные сведения о форматах даты и времени см. в разделе **Форматы даты и времени** ниже.

### Форматы даты и времени

Для `global:date`, `global:date-time` и `global:time-of-day` указывайте значение с часовым поясом в соответствии со стандартом [ISO/WD 8601-1](https://dt-url.net/bi03p33), где символ `Z` обозначает UTC.

Формат: день недели

Политика активна в определённые дни недели (часовой пояс GMT).

Пример:

```
ALLOW service:resource:permission WHERE global:week-day = "Monday";
```

Операторы: `=`, `!=`, `IN`

Формат: дата

Политика активна в заданном диапазоне дат. Необходимо указать часовой пояс.

Пример:

```
ALLOW service:resource:permission WHERE global:date > "2022-05-03Z" AND global:date < "2022-05-05Z";
```

В этом примере политика предоставляет доступ 4 мая 2022 года в часовом поясе UTC.
Операторы: `<`, `>`, `=`

Формат: дата и время

Политика активна в соответствии с заданными датой и временем. Необходимо указать часовой пояс.

Пример:

```
ALLOW service:resource:permission WHERE global:date-time > "2022-05-03T05:00:00+01:00";
```

Операторы: `<`, `>`

Формат: время суток

Политика активна каждый день в заданном временном диапазоне. Необходимо указать часовой пояс.

Пример:

```
ALLOW service:resource:permission WHERE global:time-of-day > "09:00+01:00" AND global:time-of-day < "17:00+01:00";
```

Операторы: `<`, `>`