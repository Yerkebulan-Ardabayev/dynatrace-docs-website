---
title: Settings API - Discovery findings default rules schema schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-discovery-coverage-discovery-findings-default-rules-schema
scraped: 2026-05-12T11:45:09.980253
---

# Settings API - Discovery findings default rules schema schema table

# Settings API - Discovery findings default rules schema schema table

* Published Feb 26, 2024

### Schema правил по умолчанию для находок Discovery (`app:dynatrace.discovery.coverage:discovery.findings.default.rules.schema)`

Правила по умолчанию для находок Discovery. Эта schema не подлежит ручным изменениям, кроме настройки Muted. Любые изменения (кроме отключения правила) будут перезаписаны значениями по умолчанию приложения Discovery & Coverage.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.discovery.coverage:discovery.findings.default.rules.schema` | - | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.discovery.coverage:discovery.findings.default.rules.schema` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.discovery.coverage:discovery.findings.default.rules.schema` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.discovery.coverage:discovery.findings.default.rules.schema` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Правило:  `rule` | [Rule](#Rule) | - | Required |
| Настройки: `settings` | [RuleSettings](#RuleSettings) | - | Required |

##### Объект `Rule`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| ID `id` | text | - | Required |
| Заголовок `title` | text | - | Required |
| Описание `description` | text | - | Required |
| Категория `category` | text | - | Required |
| Приоритет `priority` | text | - | Required |
| Действия `actions` | [Action](#Action)[] | - | Required |
| Запрос правила `query` | text | - | Optional |
| Scope окружения `environmentScope` | boolean | - | Required |
| Нулевой тариф `zeroRated` | boolean | - | Optional |

##### Объект `RuleSettings`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Отключено `muted` | boolean | - | Required |

##### Объект `Action`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя `name` | text | - | Required |
| Параметры `parameters` | [ActionParameter](#ActionParameter)[] | - | Required |
| Мгновенное действие `instantAction` | boolean | - | Optional |

##### Объект `ActionParameter`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя `name` | text | - | Required |
| Значение `value` | text | - | Required |