---
title: Settings API - Generic types schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-monitoredentities-generic-type
scraped: 2026-05-12T11:44:33.661297
---

# Settings API - Generic types schema table

# Settings API - Generic types schema table

* Опубликовано 05 декабря 2023 г.

### Generic types (`builtin:monitoredentities.generic.type)`

Ищете поддержку извлечения топологии? Справочную страницу см. в [topology model](https://www.dynatrace.com/support/help/shortlink/topology-model#custom-topology-model "Visit Dynatrace support center").

Generic type позволяет задать правила создания custom monitored entities на основе данных ingest.

| Schema ID | Группы схемы | Scope |
| --- | --- | --- |
| `builtin:monitoredentities.generic.type` | * `group:topology-model` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitoredentities.generic.type` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:monitoredentities.generic.type` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitoredentities.generic.type` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | Включает или отключает тип | Required |
| Имя типа `name` | text | Имя типа сущности. Имя должно быть уникальным и не меняться после создания. | Required |
| Отображаемое имя типа `displayName` | text | Человекочитаемое имя для этого типа сущности. | Required |
| Создано `createdBy` | text | Пользователь или расширение, создавшее этот тип. | Required |
| Список правил `rules` | [ExtractionRule](#ExtractionRule)[] | Задайте список правил, которые оцениваются по порядку. Когда совпадает **любое** правило, по нему извлекается сущность, и последующие правила не оцениваются.  Правила оцениваются в порядке их появления в этом списке. Каждое правило описывает, как создать одну сущность из ingested data. Оно задаёт свойства (имя, идентификатор и прочие атрибуты), которые сохраняются как часть сущности. Правило также описывает фильтры, которые должны совпасть с ingest data, чтобы сущность была создана.  Многие свойства extraction rule используют *placeholders* для динамической оценки и трансформации ingest data. Такие свойства называются *patterns* и позволяют комбинировать значения dimension со статическим текстом. Полученный результат используется при извлечении сущности. Один pattern может содержать несколько placeholders, каждый ссылается на свой dimension-ключ. При извлечении сущности placeholders заменяются на соответствующие значения dimension.  Placeholders начинаются с `{` и заканчиваются `}` (эти символы не могут быть частью статического текста pattern). Вложенные placeholders запрещены.  **Example:**  Ingest data line: `temperature,room=5.30 gauge,min=17.1,max=17.3,sum=34.4,count=2`  ID Pattern: `ROOM_{room}`  Даст ID `ROOM_5.30`.  **Example:**  Ingest data line: `device.packets.received,device_number=123,if=eth0 1024`  Attribute Value Extraction Pattern: `192.168.1.{device_number}`  Даст строку `192.168.1.123`, которую можно сохранить как IP-адрес. | Required |

##### Объект `ExtractionRule`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Шаблон извлекаемого ID `idPattern` | text | ID patterns состоят из статического текста и placeholders, ссылающихся на dimensions в ingest data. ID pattern **должен** содержать хотя бы один placeholder, чтобы гарантировать создание разных сущностей.  Следите, чтобы pattern давал один и тот же ID для одной и той же сущности. Например, использование timestamp или счётчико-подобных dimension в составе ID приведёт к созданию новой сущности на каждую ingest data, и это категорически не рекомендуется.  Каждый dimension-ключ, на который ссылается placeholder идентификатора, должен присутствовать, иначе сущность не будет извлечена. Если такого dimension-ключа нет, правило не будет рассматриваться. Если требуется извлекать тот же тип сущности при разных именах ключей, создайте несколько правил, извлекающих один и тот же тип. В этом случае следите, чтобы каждый ID pattern давал одно и то же значение для одной и той же сущности. | Required |
| Шаблон имени экземпляра `instanceNamePattern` | text | Задайте pattern, который используется для атрибута name сущности. Можно использовать placeholders, ссылающиеся на dimensions источника данных. | Optional |
| Шаблон иконки `iconPattern` | text | Задайте pattern, который используется для атрибута icon сущности. Извлекаемые значения должны ссылаться на barista icon ids. Можно использовать placeholders, ссылающиеся на dimensions источника данных. | Optional |
| Фильтры источников `sources` | Set<[SourceFilter](#SourceFilter)> | Задайте все источники, которые должны проверяться этим правилом. Правило срабатывает, если совпал любой из указанных фильтров источника. | Required |
| Дополнительно обязательные dimensions `requiredDimensions` | Set<[DimensionFilter](#DimensionFilter)> | Помимо dimensions, на которые уже ссылается ID pattern, можно указать дополнительные dimensions, без которых правило не будет оцениваться. | Required |
| Атрибуты `attributes` | Set<[AttributeEntry](#AttributeEntry)> | Применяются все правила извлечения атрибутов, найденные атрибуты добавляются к извлекаемому типу. | Required |
| Роль `role` | text | Если из одной строки ingest требуется извлекать несколько сущностей одного типа, задайте несколько правил с разными roles. | Optional |

##### Объект `SourceFilter`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Тип datasource ingest `sourceType` | enum | Укажите тип источника фильтра, чтобы определить, какой источник данных проверяется на ingest. Возможные значения: * `Metrics` * `Logs` * `Spans` * `Entities` * `Topology` * `Events` * `Business Events` | Required |
| Условие `condition` | text | Задайте фильтр, который должен совпасть, чтобы произошло извлечение.  Поддерживаются три фильтра: `$eq(value)` гарантирует точное совпадение источника с 'value', `$prefix(value)` гарантирует, что источник начинается ровно с 'value', `$exists()` гарантирует наличие любого источника, совпадающего с dimension-фильтром. Если значение содержит символы '(', ')' или '~', их необходимо экранировать, поставив перед ними '~'. | Required |

##### Объект `DimensionFilter`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Dimension-ключ `key` | text | Dimension-ключ, который должен присутствовать в ingest data, чтобы фильтр совпал. | Required |
| Шаблон значения dimension `valuePattern` | text | Шаблон значения dimension, который должен присутствовать в ingest data, чтобы фильтр совпал. | Optional |

##### Объект `AttributeEntry`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Ключ атрибута `key` | text | Ключ атрибута, это уникальное имя атрибута. | Required |
| Отображаемое имя атрибута `displayName` | text | Человекочитаемое имя атрибута для этого правила извлечения. Оставьте пустым, чтобы использовать ключ в качестве отображаемого имени. | Optional |
| Шаблон извлечения значения атрибута `pattern` | text | Pattern для задания значения извлекаемого атрибута. Может быть статическим значением, placeholders или их комбинацией. | Required |