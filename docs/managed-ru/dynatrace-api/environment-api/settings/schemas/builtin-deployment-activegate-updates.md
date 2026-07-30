---
title: Settings API - ActiveGate updates schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-deployment-activegate-updates
---

# Settings API - ActiveGate updates schema table

# Settings API - ActiveGate updates schema table

* Опубликовано 05 декабря 2023

### Обновления ActiveGate (`builtin:deployment.activegate.updates)`

Настройка поведения обновлений ActiveGate. Подробнее о последних обновлениях: [ActiveGate release notes﻿](https://dt-url.net/release-notes-activegate).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:deployment.activegate.updates` | * `group:updates` | `ENVIRONMENT_ACTIVE_GATE`  `environment` |

Получение схемы через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:deployment.activegate.updates` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:deployment.activegate.updates` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:deployment.activegate.updates` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью **Read settings** (`settings.read`). Подробнее о получении и использовании токена: [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательно |
| --- | --- | --- | --- |
| Target version `targetVersion` | text | - | Обязательно |
| Update mode `updateMode` | enum | Элемент принимает следующие значения enum * `AUTOMATIC` * `AUTOMATIC_DURING_UW` * `MANUAL` | Обязательно |
| Update windows `updateWindows` | Set<[updateWindow](#updateWindow)> | - | Обязательно |

##### Объект `updateWindow`

| Свойство | Тип | Описание | Обязательно |
| --- | --- | --- | --- |
| Update window `updateWindow` | setting | Выбор окна обновлений для обновлений ActiveGate (`<your-dynatrace-url>//ui/settings/builtin:deployment.management.update-windows`) | Обязательно |