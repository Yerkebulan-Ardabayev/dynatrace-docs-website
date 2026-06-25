---
title: Settings API - IP determination schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-ip-determination
scraped: 2026-05-12T11:43:44.156923
---

# Settings API - IP determination schema table

# Settings API - IP determination schema table

* Published Dec 05, 2023

### Определение IP (`builtin:rum.ip-determination)`

Эти настройки используются для веб-приложений, мобильных приложений и пользовательских приложений.

**Идентификация клиентских IP-адресов**

Клиентские IP-адреса автоматически определяются на основе HTTP-заголовка запроса. Если клиентские IP-адреса используют другой заголовок, создайте пользовательское правило для их идентификации.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.ip-determination` | * `group:web-and-mobile-monitoring.geographic-regions` * `group:web-and-mobile-monitoring` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.ip-determination` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.ip-determination` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.ip-determination` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя HTTP-заголовка с IP клиента `headerName` | text | - | Required |