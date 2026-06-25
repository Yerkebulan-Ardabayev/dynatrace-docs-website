---
title: Settings API - Key requests schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-settings-subscriptions-service
scraped: 2026-05-12T11:44:31.650816
---

# Settings API - Key requests schema table

# Settings API - Key requests schema table

* Published Dec 05, 2023

### Ключевые запросы (`builtin:settings.subscriptions.service)`

Конфигурация для указания ключевых запросов для конкретного сервиса. У каждого сервиса может быть несколько ключевых запросов.

* Ключевые запросы можно использовать для долгосрочной истории метрик и выделенных плиток дашбордов для построения графиков и прямого доступа с дашборда. Правила именования запросов могут влиять на ключевые запросы и наоборот.
* При настройке правила именования запросов, влияющего на ключевые запросы, чтобы переименованный запрос остался ключевым, укажите здесь итоговое имя (после применения всех правил именования запросов).

Подробнее о ключевых запросах в нашей [help](https://dt-url.net/ss03uui "Visit dynatrace.com").

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:settings.subscriptions.service` | - | `SERVICE` - Service |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:settings.subscriptions.service` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:settings.subscriptions.service` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:settings.subscriptions.service` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имена ключевых запросов `keyRequestNames` | set | - | Required |