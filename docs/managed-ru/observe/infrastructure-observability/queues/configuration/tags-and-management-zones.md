---
title: Теги и зоны управления для очередей
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/queues/configuration/tags-and-management-zones
scraped: 2026-05-12T12:04:58.819468
---

# Теги и зоны управления для очередей

# Теги и зоны управления для очередей

* How-to guide
* 2-min read
* Published May 16, 2022

Теги и зоны управления можно использовать для организации объектов очередей в вашей среде и упрощения их поиска. Теги и зоны управления применяются к объектам очередей так же, как и к другим объектам, однако их необходимо применять через [селектор объектов](/managed/dynatrace-api/environment-api/entity-v2/entity-selector "Настройка селектора объектов для конечных точек Environment API.").

## Определение автоматически применяемого тега

Выполните следующие шаги для автоматического применения тега к объектам очередей. Дополнительные сведения о тегах см. в разделе [Определение и применение тегов](/managed/manage/tags-and-metadata/setup/how-to-define-tags "Узнайте, как определять и применять теги вручную и автоматически.").

1. Перейдите в **Settings** > **Tags** > **Automatically applied tags**.
2. Выберите **Create tag** и введите имя для нового тега в поле **Tag name**.
3. Выберите **Add a new rule**.
4. Необязательно Укажите **Optional tag value**. Это значение будет отображаться рядом с именем тега через `:` и используется для предоставления более точной информации об объекте очереди.
5. В списке **Rule type** выберите тип **Entity selector**.
6. Используйте один из следующих фрагментов кода для применения тегов от объекта сервиса, группы процессов, хоста или группы хостов к объекту очереди через [селектор объектов](/managed/dynatrace-api/environment-api/entity-v2/entity-selector#tag "Настройка селектора объектов для конечных точек Environment API."). Замените `yourKey:yourValue` своими значениями тегов.

   Сервисы-производители

   Сервисы-потребители

   Группы процессов

   Хосты

   Группы хостов

   ```
   type(QUEUE),toRelationships.indirectlySendsToQueue(type(SERVICE),tag("yourKey:yourValue "))
   ```

   ```
   type(QUEUE),toRelationships.listensOnQueue(type(SERVICE),fromRelationships.calls(type(SERVICE),tag("yourKey:yourValue")))
   ```

   ```
   type(QUEUE),toRelationships.isInstanceOf(type(QUEUE_INSTANCE),fromRelationships.runsOn(type(PROCESS_GROUP_INSTANCE),fromRelationships.isInstanceOf(type(PROCESS_GROUP),tag("yourKey:yourValue"))))
   ```

   ```
   type(QUEUE),toRelationships.isInstanceOf(type(QUEUE_INSTANCE),fromRelationships.runsOn(type(PROCESS_GROUP_INSTANCE),fromRelationships.isProcessOf(type(HOST),tag("yourKey:yourValue"))))
   ```

   ```
   type(QUEUE),toRelationships.isInstanceOf(type(QUEUE_INSTANCE),fromRelationships.runsOn(type(PROCESS_GROUP_INSTANCE),fromRelationships.isProcessOf(type(HOST),fromRelationships.isInstanceOf(type(HOST_GROUP),tag(("yourKey:yourValue")))))
   ```
7. Выберите **Preview** для проверки результатов, возвращаемых конкретным селектором объектов.
8. Выберите **Save changes**.

Пример правила на основе селектора объектов

![Селектор объектов очереди](https://dt-cdn.net/images/queue-entity-selector-1688-9b93f73016.png)

Селектор объектов очереди

## Добавление объектов очередей в существующие зоны управления

Выполните следующие шаги для добавления объектов очередей в существующие зоны управления. Дополнительные сведения о зонах управления см. в разделе [Настройка зон управления](/managed/manage/identity-access-management/permission-management/management-zones/set-up-management-zones "Создание зон управления и назначение прав доступа.").

1. Перейдите в **Settings** > **Preferences** > **Management zones**.
2. Отредактируйте существующую зону управления и выберите **Add a new rule**.
3. В списке **Rule applies to** выберите **Entity selector**.
4. Используйте один из следующих фрагментов кода для добавления объекта очереди на основе тегов от объекта сервиса, группы процессов, хоста или группы хостов в зону управления через [селектор объектов](/managed/dynatrace-api/environment-api/entity-v2/entity-selector#tag "Настройка селектора объектов для конечных точек Environment API."). Замените `yourKey:yourValue` своими значениями тегов.

Сервисы-производители

Сервисы-потребители

Группы процессов

Хосты

Группы хостов

```
type(QUEUE),toRelationships.indirectlySendsToQueue(type(SERVICE),tag("yourKey:yourValue "))
```

```
type(QUEUE),toRelationships.listensOnQueue(type(SERVICE),fromRelationships.calls(type(SERVICE),tag("yourKey:yourValue")))
```

```
type(QUEUE),toRelationships.isInstanceOf(type(QUEUE_INSTANCE),fromRelationships.runsOn(type(PROCESS_GROUP_INSTANCE),fromRelationships.isInstanceOf(type(PROCESS_GROUP),tag("yourKey:yourValue"))))
```

```
type(QUEUE),toRelationships.isInstanceOf(type(QUEUE_INSTANCE),fromRelationships.runsOn(type(PROCESS_GROUP_INSTANCE),fromRelationships.isProcessOf(type(HOST),tag("yourKey:yourValue"))))
```

```
type(QUEUE),toRelationships.isInstanceOf(type(QUEUE_INSTANCE),fromRelationships.runsOn(type(PROCESS_GROUP_INSTANCE),fromRelationships.isProcessOf(type(HOST),fromRelationships.isInstanceOf(type(HOST_GROUP),tag(("yourKey:yourValue")))))
```

5. Выберите **Preview** для проверки результатов, возвращаемых конкретным селектором объектов.
6. Для сохранения конфигурации зоны управления выберите **Save changes** в правом нижнем углу страницы.

Пример зоны управления на основе селектора объектов

![Зона управления для очередей](https://dt-cdn.net/images/queue-management-zone-1688-12745271e1.png)

Зона управления для очередей

## Связанные темы

* [Определение и применение тегов](/managed/manage/tags-and-metadata/setup/how-to-define-tags "Узнайте, как определять и применять теги вручную и автоматически.")
* [Настройка зон управления](/managed/manage/identity-access-management/permission-management/management-zones/set-up-management-zones "Создание зон управления и назначение прав доступа.")