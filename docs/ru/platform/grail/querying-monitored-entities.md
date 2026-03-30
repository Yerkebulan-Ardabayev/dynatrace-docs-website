---
title: Запрос отслеживаемых сущностей в Grail
source: https://www.dynatrace.com/docs/platform/grail/querying-monitored-entities
scraped: 2026-03-04T21:37:09.081125
---

# Запрос контролируемых сущностей в Grail


Это руководство по эффективному использованию Dynatrace Query Language (DQL) для запроса контролируемых сущностей. Оно включает использование общих возможностей DQL, таких как развёртывание массивов, объединение данных с помощью команды `lookup` и использование встроенных функций разбора.

## Запрос типов сущностей

Для запроса контролируемых сущностей по их типу вы можете использовать представления `dt.entity.*`.

Чтобы начать запрос, откройте пустой запрос в ваших блокнотах и введите `fetch dt.entity`. Это вызовет диалог автозаполнения, в котором вы можете выбрать нужный тип сущности.

![Пример автозаполнения для типов сущностей.](https://dt-cdn.net/images/ft-entity-2-1439-af70ed8841.png)

Например, выполнение запроса `fetch dt.entity.host` извлекает все сущности хостов. По умолчанию записи сущностей включают идентификатор и имя сущности.

```
fetch dt.entity.host
```

Для включения дополнительных деталей вы можете использовать команду `fieldsAdd`. По мере ввода функция автозаполнения предлагает доступные поля для данного типа сущности.

Другой способ начать работу — использовать один из встроенных фрагментов запросов топологии.

![Пример начала работы с помощью встроенных фрагментов запросов топологии.](https://dt-cdn.net/images/topology-1447-687b6417ca.png)

## Запрос связей

Связи представлены как поля и могут быть добавлены аналогично другим полям. Например, вы можете добавить связь `runs` к записям хостов, чтобы получить список всех сущностей, работающих на данном хосте.

```
fetch dt.entity.host


| fieldsAdd runs
```

Поле `runs` является вложенной записью, содержащей поле для каждого типа сущности, работающей на определённом хосте. В зависимости от кардинальности эти поля представляют собой либо строки с одним идентификатором сущности, либо массивы строк со списком идентификаторов сущностей. В блокнотах выберите вложенную запись в списке результатов, чтобы увидеть её содержимое.

Если вы хотите видеть только группы процессов, работающие на данном хосте, вы можете указать это в команде `fieldsAdd`. Функция автозаполнения предоставит список возможных типов идентификаторов.

Выбор типа уточняет запрос, возвращая только массив, содержащий идентификаторы групп процессов.

```
fetch dt.entity.host


| fieldsAdd runs[dt.entity.process_group]
```

Имена полей для связей отличаются от оригинальных имён связей в предыдущей версии Dynatrace. Вместо одного имени с префиксами `fromRelationship` и `toRelationship` поля имеют различные имена с обеих сторон.

См. [таблицу сопоставления связей](#relationship-mapping-table) ниже, чтобы понять, как связи второго поколения представлены в виде полей DQL.

Обратите внимание, что связи 1:n возвращают только 100 идентификаторов сущностей на тип на запись. В таких случаях мы рекомендуем использовать вместо этого `classicEntitySelector()`.

## Поиск сущностей

Вы можете использовать команду `lookup` для объединения данных из связанных сущностей.

Например, чтобы включить теги хоста в экземпляры сервисов, вы можете получить доступ к хосту из экземпляра сервиса, следуя связи `runs_on`.

```
fetch dt.entity.service_instance


| fieldsAdd runs_on[dt.entity.host]
```

Важно отметить, что экземпляры сервисов всегда работают на одном хосте, что означает, что вы получаете один идентификатор хоста на запись экземпляра сервиса. Это позволяет использовать команду `lookup` для добавления имени хоста к вашим записям. Имя хоста добавляется как поле `lookup.entity.name`.

```
fetch dt.entity.service_instance


| fieldsAdd runs_on[dt.entity.host]


| lookup sourceField:`runs_on[dt.entity.host]`, lookupField:id, [ fetch dt.entity.host ]
```

## Развёртывание связей

Хосты могут запускать несколько экземпляров сервисов, поэтому поле `runs[dt.entity.service_instance]` является массивом идентификаторов сущностей.

```
fetch dt.entity.host


| fieldsAdd runs[dt.entity.service_instance]
```

Команда `lookup` не применяется к массивам идентификаторов, поэтому сначала необходимо использовать команду `expand` для получения отдельных записей на каждый идентификатор экземпляра сервиса.

```
fetch dt.entity.host


| fieldsAdd runs[dt.entity.service_instance]


| expand runs[dt.entity.service_instance]
```

В этом примере первая запись развёртывается в три. Теперь вы можете использовать команду `lookup` для получения деталей экземпляра сервиса, которые включаются в поле `lookup`.

```
fetch dt.entity.host


| fieldsAdd runs[dt.entity.service_instance]


| expand runs[dt.entity.service_instance]


| lookup sourceField:`runs[dt.entity.service_instance]`, lookupField:id, [ fetch dt.entity.service_instance]
```

## Теги сущностей

Теги сущностей состоят из трёх значений: контекст, ключ и значение. Dynatrace создаёт строковое представление этих значений в следующем формате:

`[<context>]<key>:<value>`

* Все вхождения символов `[`, `]` и `:` должны быть экранированы с помощью символа `\`.
* Поле `tags` возвращает строковые представления этих полей.

Следующий пример запроса извлекает список тегов сущностей хостов.

```
fetch dt.entity.host


| expand tags, alias:tag


| fields tag
```

Вы можете использовать команду `expand` для оптимизации фильтрации тегов. Этот пример фильтрует хосты на основе определённого имени кластера.

```
fetch dt.entity.host


| expand tags


| filter contains(tags, "[Environment]Cluster.Name:prod-eu-west-6-ireland")
```

Если вам нужен структурированный доступ к ключу, контексту или значению, вы можете использовать следующее выражение разбора DPL для разделения строкового представления на отдельные поля.

```
fetch dt.entity.host


| expand tags, alias:tag_string


| parse tag_string, """(('['LD:tag_context ']' LD:tag_key (!<<'\\' ':') LD:tag_value)|(LD:tag_key (!<<'\\' ':') LD:tag_value)|LD:tag_key)"""
```

## Список полей и связей

Используйте команду `describe` для получения списка полей и связей для каждого представления сущности.

Например, чтобы получить список всех полей и связей для представления сущности `service_instance`, введите `describe dt.entity.service_instance`:

```
describe dt.entity.service_instance
```

Учитывайте следующую информацию при работе с различными полями:

* Большинство полей сущностей имеют те же имена, что и в API v2 среды (например, gcpZone и oneAgentCustomName).
* Первая и последняя метки наблюдения сущности хранятся в поле lifetime, представленном как тип timeframe, состоящий из начальной и конечной метки времени. Время жизни сущности должно пересекаться с временным диапазоном запроса, чтобы сущность была включена в результаты запроса.
* Несколько имён сущностей имеют префикс 'entity.' (например, `entity.conditional_name`)
* Связи возвращаются как записи. Подробнее о них см. в разделе связи сущностей.

Команда `describe` является ценным инструментом для изучения схемы данных Grail.

```
describe dt.entity.service_instance


| filter in(data_types, "record")
```

## Разрешения

Для запроса сущностей необходимо разрешение `storage:entities:read`.

Grail не применяет фильтры зон управления. Пользователи с разрешением `storage:entities:read` могут запрашивать все сущности.

## Селекторы сущностей

Вы можете использовать функцию `classicEntitySelector()` для упрощения начала DQL-запросов к сущностям. Эта команда принимает селектор сущности в качестве строкового аргумента и возвращает список идентификаторов сущностей. Вы можете использовать этот список для фильтрации сущностей по идентификатору.

Например, вы можете отфильтровать экземпляры сервисов, работающие на хостах с определённым тегом.

```
fetch dt.entity.service


| filter in(id, classicEntitySelector("type(service), fromRelationship.runsOnHost(type(host), tag([AWS]Category:ABC))"))
```

Вы также можете получить этот результат с помощью нативного DQL следующим запросом.

```
fetch dt.entity.service


| fieldsAdd host.id = runs_on[dt.entity.host]


| expand host.id


| lookup sourceField:host.id, lookupField: id, fields:host.tags=tags, [ fetch dt.entity.host]


| expand host.tags


| filter host.tags == "[AWS]Category:ABC"
```

Этот запрос имеет ограничения, такие как возврат только 100 хостов на сущность сервиса, и в целом более сложен, чем предыдущий пример с использованием функции `classicEntitySelector`.

### Фильтрация по связям

Когда ваш запрос оценивает связи, мы рекомендуем использовать функцию `classicEntitySelector` вместо нативных DQL-запросов.

В следующих примерах нативный DQL-запрос будет медленнее и может давать неполные результаты по сравнению с запросом `classicEntitySelector`:

```
// fetch all hosts that run Java processes


// using native DQL


fetch dt.entity.host


| expand pgi=contains[dt.entity.process_group_instance]


| filter pgi in [


fetch dt.entity.process_group_instance


| filter matchesValue(softwareTechnologies, "*JAVA*")


| fields id


]
```

```
// fetch all hosts that run Java processes


// using classicEntitySelector()


fetch dt.entity.host


| filter in (id, classicEntitySelector("type(host),toRelationship.isProcessOf(type(PROCESS_GROUP_INSTANCE),softwareTechnologies(JAVA))"))
```

### Комбинирование `classicEntitySelector` с нативными фильтрами DQL

Если вы уже используете функцию `classicEntitySelector`, лучше добавить все критерии фильтрации в вызов функции, а не добавлять дополнительные нативные операторы фильтрации. Смешанный запрос медленнее, чем запрос, содержащий все условия фильтрации в селекторе сущностей.

```
// fetch all LINUX hosts that run Java processes


// using a mix of classicEntitySelector and native DQL filters


fetch dt.entity.host


| filter in (id, classicEntitySelector("type(host),toRelationship.isProcessOf(type(PROCESS_GROUP_INSTANCE),softwareTechnologies(JAVA))"))


| fieldsAdd osType


| filter osType == "LINUX"
```

```
// fetch all LINUX hosts that run Java processes


// using only classicEntitySelector


fetch dt.entity.host


| filter in (id, classicEntitySelector("type(host),osType(LINUX),toRelationship.isProcessOf(type(PROCESS_GROUP_INSTANCE),softwareTechnologies(JAVA))"))


| fieldsAdd osType
```

## Таблица сопоставления связей

Связи сущностей в предыдущей версии Dynatrace (например, в API v2 среды) сопоставлены с новыми именами в записях DQL в соответствии со следующей таблицей.

## Устранение неполадок

* **DQL-запрос возвращает другие или меньше сущностей, чем API v2 среды**
  Убедитесь, что вы используете тот же временной диапазон запроса `fetch dt.entity.*`. Функция `classicEntitySelector()` возвращает только сущности, время жизни которых пересекается с временным диапазоном запроса. По умолчанию DQL-запросы выполняются за последние 2 часа, тогда как временной диапазон по умолчанию в API среды составляет 72 часа.

## Связанные темы

* Что такое Dynatrace Grail?
* Команды DQL
* Справочник политик IAM
* Разрешения в Grail
* API среды v2 — селектор сущностей
