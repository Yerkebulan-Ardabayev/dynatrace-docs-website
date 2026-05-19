---
title: Settings API - Site Reliability Guardian schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-site-reliability-guardian-guardians
scraped: 2026-05-12T11:41:44.945846
---

# Settings API - Site Reliability Guardian schema table

# Settings API - Site Reliability Guardian schema table

* Published Dec 05, 2023

### Site Reliability Guardian (`app:dynatrace.site.reliability.guardian:guardians)`

Создание новых guardians и добавление objectives. [См. документацию](https://dt-url.net/site-reliability-guardian)

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.site.reliability.guardian:guardians` | - | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.site.reliability.guardian:guardians` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.site.reliability.guardian:guardians` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.site.reliability.guardian:guardians` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя `name` | text | - | Required |
| Описание `description` | text | - | Optional |
| Теги `tags` | set | Задайте пары ключ/значение, которые дополнительно описывают этот guardian. | Required |
| Переменные DQL `variables` | [Variable](#Variable)[] | Задайте переменные для динамического определения DQL-запросов | Required |
| Objectives `objectives` | [Objective](#Objective)[] | - | Required |
| Вид события `eventKind` | enum | Если задано null/'BIZ\_EVENT', события валидации сохраняются как bizevents в Grail. Если задано 'SDLC\_EVENT', события валидации сохраняются как SDLC events Возможные значения: * `BIZ_EVENT` * `SDLC_EVENT` | Optional |

##### Объект `Variable`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя `name` | text | - | Required |
| Значение `definition` | text | - | Required |

##### Объект `Objective`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя цели `name` | text | - | Required |
| Описание `description` | text | - | Optional |
| Тип цели `objectiveType` | enum | Возможные значения: * `DQL` * `REFERENCE_SLO` | Required |
| DQL-запрос `dqlQuery` | text | - | Required |
| Единица отображения `displayUnit` | [DisplayUnit](#DisplayUnit) | - | Optional |
| Включить авто-адаптивный порог `autoAdaptiveThresholdEnabled` | boolean | - | Optional |
| Эталонный SLO `referenceSlo` | text | Введите ключ метрики нужного SLO. Ключи метрик SLO должны начинаться с 'func:slo.' | Required |
| Оператор сравнения `comparisonOperator` | enum | Возможные значения: * `GREATER_THAN_OR_EQUAL` * `LESS_THAN_OR_EQUAL` | Required |
| Цель `target` | float | - | Optional |
| Предупреждение `warning` | float | - | Optional |
| Сегменты `segments` | [Segment](#Segment)[] | - | Required |
| Ссылки `links` | [ObjectiveLink](#ObjectiveLink)[] | Поля для добавления релевантных ссылок к этой цели. | Required |

##### Объект `DisplayUnit`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Базовая единица `base` | text | - | Required |
| отображать как единицу `display` | text | - | Required |
| Знаки после запятой `decimals` | integer | - | Required |

##### Объект `Segment`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| ID сегмента `id` | text | - | Required |
| Переменные сегмента `variables` | [SegmentVariable](#SegmentVariable)[] | - | Required |

##### Объект `ObjectiveLink`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| URL `url` | text | HTTPS-ссылка, связанная с этой целью. | Required |
| Отображаемый текст `label` | text | Краткое описание для ссылки. | Optional |

##### Объект `SegmentVariable`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя переменной `name` | text | - | Required |
| Значения переменной `values` | list | - | Required |