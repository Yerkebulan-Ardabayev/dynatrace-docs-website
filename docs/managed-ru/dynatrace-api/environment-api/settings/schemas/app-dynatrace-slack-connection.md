---
title: Settings API - Slack schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-slack-connection
---

# Settings API - Slack schema table

# Settings API - Slack schema table

* Опубликовано 05 дек. 2023

### Slack (`app:dynatrace.slack:connection)`

Данные аутентификации для Slack API

(подробнее в [документации Slack api﻿](https://api.slack.com/authentication/basics/ "Visit Slack document"))

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.slack:connection` | - | `environment` |

Получить схему через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.slack:connection` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.slack:connection` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.slack:connection` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью **Read settings** (`settings.read`). Подробнее о получении и использовании: [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| Название соединения `name` | text | Укажите уникальное и легко узнаваемое название соединения со Slack App. | Обязательно |
| Bot-токен `token` | secret | Bot-токен, полученный в Slack App Management UI.  Формат токена: `xoxb-******` | Обязательно |
| Внешнее согласование `externalApproval` | boolean | Включение внешних согласований позволяет пользователям Slack напрямую отвечать на запросы согласования. | Необязательно |
| Подписывающий секрет `signingSecret` | secret | Подписывающий секрет, полученный в Slack App Management UI. | Обязательно |