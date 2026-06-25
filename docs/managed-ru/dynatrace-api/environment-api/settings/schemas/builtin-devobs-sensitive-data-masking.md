---
title: Settings API - Sensitive Data Masking schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-devobs-sensitive-data-masking
scraped: 2026-05-12T11:45:13.719820
---

# Settings API - Sensitive Data Masking schema table

# Settings API - Sensitive Data Masking schema table

* Опубликовано 05 августа 2024 г.

### Маскирование чувствительных данных (`builtin:devobs.sensitive.data.masking)`

Создавайте правила, чтобы маскировать любую информацию, которую считаете чувствительной. Маскирование выполняется на OneAgent, персональные данные не передаются и не хранятся на серверах Dynatrace.

| Schema ID | Группы схемы | Scope |
| --- | --- | --- |
| `builtin:devobs.sensitive.data.masking` | * `group:observability-for-developers` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:devobs.sensitive.data.masking` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:devobs.sensitive.data.masking` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:devobs.sensitive.data.masking` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя правила `ruleName` | text | - | Required |
| Активно `enabled` | boolean | - | Required |
| Тип правила `ruleType` | enum | Выберите, маскировать по имени переменной или по regex. Возможные значения: * `VAR_NAME` * `REGEX` | Required |
| Имя переменной `ruleVarName` | text | - | Required |
| Тип сравнения `comparisonType` | enum | Выберите, как должно сопоставляться имя переменной. Возможные значения: * `EQUALS` * `CONTAINS` * `STARTS_WITH` * `ENDS_WITH` | Required |
| Regex-шаблон `ruleRegex` | text | - | Required |
| Замена данных `replacementType` | enum | Выберите, как должны заменяться чувствительные данные. Возможные значения: * `STRING` * `SHA256` | Required |
| Шаблон замены `replacementPattern` | text | - | Required |