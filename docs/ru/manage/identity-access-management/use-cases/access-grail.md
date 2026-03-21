---
title: Предоставление доступа к Grail
source: https://www.dynatrace.com/docs/manage/identity-access-management/use-cases/access-grail
scraped: 2026-03-06T21:24:18.105486
---

* Последняя Dynatrace
* 2 мин. чтения

Это руководство проведёт вас через процесс настройки доступа к данным в Grail для ваших пользователей. Контроль доступа к данным в Grail осуществляется на нескольких уровнях: бакеты, таблицы, записи и поля.

## Для кого это руководство

Это руководство предназначено для администраторов аккаунтов Dynatrace, которым необходимо использовать политики по умолчанию для предоставления пользователям доступа к данным, хранящимся в Grail.

## Что вы узнаете

В этом руководстве вы узнаете:

1. Какие политики по умолчанию доступны для доступа к Grail
2. Как использовать эти политики для предоставления доступа к данным мониторинга, хранящимся в Grail

## Шаги

Начнём с изучения доступных политик, а затем узнаем, как использовать эти политики для предоставления доступа к данным мониторинга, хранящимся в Grail.

### 1. Политики по умолчанию

Dynatrace поставляется с набором встроенных политик для доступа к данным. Все их названия начинаются с префикса `storage`. Например, рассмотрим политику **Storage Default Monitoring Read**, которая предоставляет следующие два разрешения:

```
ALLOW storage:buckets:read WHERE storage:bucket-name STARTSWITH "default_;"


ALLOW storage:events:read,storage:logs:read,storage:metrics:read,storage:entities:read,storage:bizevents:read,storage:spans:read;
```

Это предоставляет пользователю доступ ко всем таблицам и ко всем бакетам по умолчанию (они имеют префикс `default_`). При создании пользовательских бакетов пользователи должны получить явный доступ к ним.

**Примечание**: Встроенные политики предоставляют безусловный доступ к таблицам. Когда вы начнёте использовать разрешения на уровне записей, вам потребуется заменить политики по умолчанию собственными.

### 2. Предоставление доступа к данным, хранящимся в Grail

#### Storage Default Monitoring Read

Администраторы могут использовать это разрешение для предоставления пользователям доступа к таблицам и данным, хранящимся в бакетах по умолчанию (имена бакетов по умолчанию начинаются с префикса `default_`). Эта политика будет автоматически корректироваться по мере добавления новых таблиц в Grail в будущем.

Обратите внимание, что эта политика охватывает только бакеты по умолчанию. При добавлении пользовательских бакетов в Grail администраторам необходимо определить дополнительные разрешения.

```
ALLOW storage:buckets:read WHERE storage:bucket-name startsWith "default_";ALLOW storage:events:read, storage:logs:read, storage:metrics:read, storage:entities:read, storage:bizevents:read, storage:spans:read;
```

#### Storage Read для каждой таблицы

Каждая таблица включает политику, объединяющую доступ к таблице и бакету, под названием **Storage** `<имя_таблицы>` **Read**. Администраторы могут использовать эту политику для предоставления группе пользователей доступа к определённой таблице и связанным бакетам.

```
ALLOW storage:buckets:read WHERE storage:table-name = "logs";


ALLOW storage:logs:read;
```

#### Storage All System Data Read

Политика **Storage All System Data Read** предоставляет доступ к внутренним данным Dynatrace, таким как события аудита и события выполнения запросов. Администраторы могут назначить эту политику пользователям, которым необходим доступ к данным такого типа.

```
ALLOW storage:buckets:read;ALLOW storage:system:read;ALLOW storage:events:read, storage:logs:read, storage:metrics:read, storage:entities:read, storage:bizevents:read,storage:spans:read;
```

#### Storage All Grail Data Read

Политика **Storage All Grail Data Read** предоставляет нефильтрованный доступ ко всем данным в Grail.

```
ALLOW storage:buckets:read;


ALLOW storage:system:read;


ALLOW storage:events:read, storage:logs:read, storage:metrics:read, storage:entities:read, storage:bizevents:read,storage:spans:read;
```

Подробнее см. [документацию по разрешениям для бакетов и таблиц Grail](../../../platform/grail/organize-data/assign-permissions-in-grail.md "Узнайте, как назначать разрешения для бакетов и таблиц в Grail.").