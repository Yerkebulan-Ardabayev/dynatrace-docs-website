---
title: Settings API - Processing schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-logmonitoring-log-dpp-rules
scraped: 2026-05-12T11:46:42.020872
---

# Settings API - Processing schema table

# Settings API - Processing schema table

* Published Dec 05, 2023

### Обработка (`builtin:logmonitoring.log-dpp-rules)`

Логи можно преобразовывать через правила обработки. Учтите, что правила обрабатываются последовательно, поэтому порядок важен: другой порядок правил может дать другой результат.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:logmonitoring.log-dpp-rules` | * `group:log-monitoring.analysis` * `group:log-monitoring` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.log-dpp-rules` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:logmonitoring.log-dpp-rules` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.log-dpp-rules` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Активно `enabled` | boolean | - | Required |
| Имя правила `ruleName` | text | - | Required |
| Сопоставитель `query` | text | - | Required |
| `ProcessorDefinition` | [ProcessorDefinition](#ProcessorDefinition) | - | Required |
| `RuleTesting` | [RuleTesting](#RuleTesting) |  | Required |

##### Объект `ProcessorDefinition`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Определение процессора `rule` | text | - | Required |

##### Объект `RuleTesting`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Образец лога `sampleLog` | text | Образец лога в формате JSON. | Required |