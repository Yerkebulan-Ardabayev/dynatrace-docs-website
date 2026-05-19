---
title: Settings API - Salesforce Insights schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-biz-salesforce-insights-biz-salesforce-insights-settings
scraped: 2026-05-12T11:48:09.269211
---

# Settings API - Salesforce Insights schema table

# Settings API - Salesforce Insights schema table

* Published Dec 05, 2023

### Salesforce Insights (`app:dynatrace.biz.salesforce.insights:biz-salesforce-insights-settings)`

Настройки для AppEngine-приложения Salesforce Insights

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.biz.salesforce.insights:biz-salesforce-insights-settings` | - | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.biz.salesforce.insights:biz-salesforce-insights-settings` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.biz.salesforce.insights:biz-salesforce-insights-settings` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.biz.salesforce.insights:biz-salesforce-insights-settings` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя `name` | text | Имя конфигурации | Required |
| URL `url` | text | URL инстанса salesforce | Required |
| Типы событий `eventTypes` | Set<[EEventTypes](#EEventTypes)> | Возможные значения: * `LoginEvent` * `SessionHijackingEventStore` * `ReportAnomalyEventStore` * `ReportEvent` * `ApiAnomalyEventStore` * `LightningUriEvent` * `ListViewEvent` * `OpportunityFieldHistory` * `UriEvent` | Required |
| ID workflow `workflowId` | text | Изменение этого сломает приложение | Optional |
| Тип гранта `grant_type` | enum | Возможные значения: * `client_credentials` * `password` | Required |
| ID клиента `client_id` | secret | - | Required |
| Секрет клиента `client_secret` | secret | - | Required |
| Имя пользователя `username` | text | - | Required |
| Пароль `password` | secret | - | Required |