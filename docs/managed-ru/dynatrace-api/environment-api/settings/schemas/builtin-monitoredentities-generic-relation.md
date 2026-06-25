---
title: Settings API - Generic relationships schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-monitoredentities-generic-relation
scraped: 2026-05-12T11:42:40.817185
---

# Settings API - Generic relationships schema table

# Settings API - Generic relationships schema table

* Published Dec 05, 2023

### Универсальные связи (`builtin:monitoredentities.generic.relation)`

Ищете поддержку извлечения топологии? См. страницу помощи [topology model](https://www.dynatrace.com/support/help/shortlink/topology-model#custom-topology-model "Visit Dynatrace support center").

Типы сущностей могут быть связаны между собой. Реестр связей содержит правила, по которым связи между связанными сущностями устанавливаются автоматически.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:monitoredentities.generic.relation` | * `group:topology-model` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitoredentities.generic.relation` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:monitoredentities.generic.relation` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitoredentities.generic.relation` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | Включает или выключает связь | Required |
| Source-фильтры `sources` | Set<[SourceFilter](#SourceFilter)> | Укажите все источники, которые должны проверяться для этого правила связи. Связь создаётся только когда совпал любой из фильтров. | Required |
| Кем создано `createdBy` | text | Пользователь или расширение, создавшие эту связь. | Required |
| Имя source type `fromType` | text | Задайте тип сущности как источник связи. | Required |
| Роль source type `fromRole` | text | Укажите роль для source-сущности. Если source и destination имеют одинаковый тип, разные роли позволяют идентифицировать направление связи. Если роль не задана, для связи учитывается любая роль source type. | Optional |
| Тип связи `typeOfRelation` | enum | Тип связи между Source Type и Destination Type Возможные значения: * `INSTANCE_OF` * `RUNS_ON` * `CHILD_OF` * `CALLS` * `PART_OF` * `SAME_AS` | Required |
| Destination type `toType` | text | Задайте тип сущности как destination связи. Можно выбрать тот же тип, что и source. В этом случае также можно назначить разные роли для source и destination, чтобы получить направленные связи. | Required |
| Роль destination type `toRole` | text | Укажите роль для destination-сущности. Если source и destination имеют одинаковый тип, разные роли позволяют идентифицировать направление связи. Если роль не задана, для связи учитывается любая роль destination type. | Optional |

##### Объект `SourceFilter`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Тип источника данных `sourceType` | enum | Укажите source type фильтра, чтобы определить, какой источник данных следует проверять. Возможные значения: * `Metrics` * `Logs` * `Spans` * `Entities` * `Topology` * `Events` * `Business Events` | Required |
| Условие `condition` | text | Задайте фильтр, который должен совпасть, чтобы произошло извлечение.  Поддерживаются два разных фильтра: `$eq(value)` гарантирует, что источник в точности равен 'value', а `$prefix(value)` гарантирует, что источник начинается ровно с 'value'. Если значение содержит символы '(', ')' или '~', экранируйте их, поставив '~' перед ними. | Required |
| Mapping rules `mappingRules` | Set<[MappingRule](#MappingRule)> | Укажите все свойства, которые должны сравниваться. Связь между сущностями создаётся, если совпадают все mapping rules. | Required |

##### Объект `MappingRule`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Source-свойство `sourceProperty` | text | Чувствительное к регистру имя свойства source type. | Required |
| Нормализация source `sourceTransformation` | enum | Нормализовать текст или оставить как есть? Возможные значения: * `Leave text as-is` * `To upper case` * `To lower case` | Required |
| Destination-свойство `destinationProperty` | text | Чувствительное к регистру имя свойства destination type. | Required |
| Нормализация destination `destinationTransformation` | enum | Нормализовать текст или оставить как есть? Возможные значения: * `Leave text as-is` * `To upper case` * `To lower case` | Required |