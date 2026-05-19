---
title: Settings API - Hub Requests schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-hub-manage-permissions
scraped: 2026-05-12T11:49:48.005356
---

# Settings API - Hub Requests schema table

# Settings API - Hub Requests schema table

* Published Jul 31, 2024

### Запросы Hub (`app:dynatrace.hub:manage.permissions)`

Добавьте хотя бы одного администратора со всеми необходимыми правами для выполнения запросов.

Для получения уведомлений о запросах можно указать командные или индивидуальные адреса электронной почты.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.hub:manage.permissions` | - | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.hub:manage.permissions` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.hub:manage.permissions` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.hub:manage.permissions` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Контактный email `email` | text | - | Required |
| Имя `description` | text | - | Required |