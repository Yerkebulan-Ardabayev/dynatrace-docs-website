---
title: Теги очередей и зоны управления
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/queues/configuration/tags-and-management-zones
scraped: 2026-03-01T21:16:56.958006
---

Вы можете использовать теги и зоны управления для организации объектов очередей в вашей среде и упрощения их поиска. Теги и зоны управления применяются к объектам очередей так же, как и к другим объектам, однако их необходимо применять через [entity selector](../../../../dynatrace-api/environment-api/entity-v2/entity-selector.md "Настройте entity selector для конечных точек Environment API.").

## Определение автоматически применяемого тега

Выполните следующие шаги, чтобы автоматически применять тег к объектам очередей. Дополнительные сведения о тегах см. в разделе [Define and apply tags](../../../../manage/tags-and-metadata/setup/how-to-define-tags.md "Узнайте, как определять и применять теги вручную и автоматически.").

1. Перейдите в **Settings** > **Tags** > **Automatically applied tags**.
2. Выберите **Create tag** и введите имя нового тега в поле **Tag name**.
3. Выберите **Add a new rule**.
4. Необязательно: укажите **Optional tag value**. Это значение будет отображаться рядом с именем тега после `:` и используется для предоставления более точной информации об объекте очереди.
5. В списке **Rule type** выберите тип **Entity selector**.
6. Используйте один из следующих фрагментов кода для применения тегов из объекта сервиса, группы процессов, хоста или группы хостов к объекту очереди через [entity selector](../../../../dynatrace-api/environment-api/entity-v2/entity-selector.md#tag "Настройте entity selector для конечных точек Environment API."). Замените `yourKey:yourValue` собственными значениями тегов.

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
7. Выберите **Preview** для проверки результатов, возвращаемых конкретным entity selector.
8. Выберите **Save changes**.

Пример entity selector на основе правила

![Entity selector для очереди](https://dt-cdn.net/images/queue-entity-selector-1688-9b93f73016.png)

## Добавление объектов очередей в существующие зоны управления

Выполните следующие шаги, чтобы добавить объекты очередей в существующие зоны управления. Дополнительные сведения о зонах управления см. в разделе [Set up management zones](../../../../manage/identity-access-management/permission-management/management-zones/set-up-management-zones.md "Создание зон управления и назначение прав доступа.").

1. Перейдите в **Settings** > **Preferences** > **Management zones**.
2. Отредактируйте существующую зону управления и выберите **Add a new rule**.
3. В списке **Rule applies to** выберите **Entity selector**.
4. Используйте один из следующих фрагментов кода для добавления объекта очереди на основе тегов из объекта сервиса, группы процессов, хоста или группы хостов в зону управления через [entity selector](../../../../dynatrace-api/environment-api/entity-v2/entity-selector.md#tag "Настройте entity selector для конечных точек Environment API."). Замените `yourKey:yourValue` собственными значениями тегов.

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

5. Выберите **Preview** для проверки результатов, возвращаемых конкретным entity selector.
6. Чтобы сохранить конфигурацию зоны управления, выберите **Save changes** в правом нижнем углу страницы.

Пример зоны управления на основе entity selector

![Зона управления для очередей](https://dt-cdn.net/images/queue-management-zone-1688-12745271e1.png)

## Смотрите также

* [Define and apply tags](../../../../manage/tags-and-metadata/setup/how-to-define-tags.md "Узнайте, как определять и применять теги вручную и автоматически.")
* [Set up management zones](../../../../manage/identity-access-management/permission-management/management-zones/set-up-management-zones.md "Создание зон управления и назначение прав доступа.")
