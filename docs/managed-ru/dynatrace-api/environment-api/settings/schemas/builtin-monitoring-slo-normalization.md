---
title: Settings API - Service-level objective setup schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-monitoring-slo-normalization
scraped: 2026-05-12T11:48:30.982744
---

# Settings API - Service-level objective setup schema table

# Settings API - Service-level objective setup schema table

* Published Dec 05, 2023

### Настройка целей уровня обслуживания (`builtin:monitoring.slo.normalization)`

Используйте эти настройки для конфигурации оценок целей уровня обслуживания.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:monitoring.slo.normalization` | * `group:cloud-automation.monitoring.slo` * `group:cloud-automation` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitoring.slo.normalization` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:monitoring.slo.normalization` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitoring.slo.normalization` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Нормализовать бюджет ошибок `normalize` | boolean | Если установлено в true, оставшийся бюджет ошибок будет показан в процентах от общего бюджета ошибок. Подробнее см. [SLO normalization help](https://dt-url.net/slo-normalize-error-budget). | Required |