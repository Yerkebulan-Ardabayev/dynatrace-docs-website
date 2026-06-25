---
title: Settings API - Business event processing schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-bizevents-processing-pipelines-rule
scraped: 2026-05-12T11:39:41.637456
---

# Settings API - Business event processing schema table

# Settings API - Business event processing schema table

* Published Dec 05, 2023

### Обработка Business event (`builtin:bizevents-processing-pipelines.rule)`

Входящие business events можно преобразовывать через правила обработки с помощью [this syntax](https://dt-url.net/pz030w5). Учтите: правила обрабатываются последовательно, поэтому порядок важен, разный порядок может давать разные результаты.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:bizevents-processing-pipelines.rule` | * `group:business-analytics` * `group:business-analytics.ingest-pipeline` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:bizevents-processing-pipelines.rule` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:bizevents-processing-pipelines.rule` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:bizevents-processing-pipelines.rule` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | - | Required |
| Имя правила `ruleName` | text | - | Required |
| Сопоставитель (DQL) `matcher` | text | [See our documentation](https://dt-url.net/bp234rv) | Required |
| Поля преобразования `transformationFields` | [TransformationField](#TransformationField)[] | - | Required |
| Определение процессора `script` | text | [See our documentation](https://dt-url.net/pz030w5) | Required |
| `RuleTesting` | [RuleTesting](#RuleTesting) |  | Required |

##### Объект `TransformationField`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Тип `type` | enum | Возможные значения: * `STRING` * `BOOLEAN` * `INT` * `LONG` * `DOUBLE` * `DURATION` * `TIMESTAMP` * `IPADDR` | Required |
| Имя `name` | text | - | Required |
| Опционально `optional` | boolean | - | Required |
| Является массивом `array` | boolean | - | Required |
| Только для чтения `readonly` | boolean | - | Required |

##### Объект `RuleTesting`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Образец события `sampleEvent` | text | Образец события для тестового прогона. Поддерживается только формат JSON. | Required |