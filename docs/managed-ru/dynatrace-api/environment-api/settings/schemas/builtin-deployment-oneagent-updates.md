---
title: Settings API - OneAgent updates schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-deployment-oneagent-updates
scraped: 2026-05-12T11:43:02.979285
---

# Settings API - OneAgent updates schema table

# Settings API - OneAgent updates schema table

* Published Dec 05, 2023

### Обновления OneAgent (`builtin:deployment.oneagent.updates)`

Выберите целевую версию OneAgent и настройте поведение обновлений. Выбранная версия также используется на страницах [Deployment API](https://dt-url.net/hh03wzk) и развёртывания OneAgent. О целевой версии OneAgent см. [OneAgent update](https://dt-url.net/9901p5j). О последних обновлениях см. [OneAgent release notes](https://dt-url.net/release-notes-oneagent). О поведении обновлений RUM JavaScript см. RUM JavaScript updates (`<your-dynatrace-url>//ui/settings/builtin:rum.web.rum-javascript-updates`).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:deployment.oneagent.updates` | * `group:updates` | `HOST` - Host  `HOST_GROUP` - Host Group  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:deployment.oneagent.updates` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:deployment.oneagent.updates` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:deployment.oneagent.updates` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Целевая версия `targetVersion` | text | - | Required |
| Ревизия `revision` | text | - | Required |
| Режим обновления `updateMode` | enum | Возможные значения: * `AUTOMATIC` * `AUTOMATIC_DURING_MW` * `MANUAL` | Required |
| Окна обновления `maintenanceWindows` | Set<[maintenanceWindow](#maintenanceWindow)> | - | Required |

##### Объект `maintenanceWindow`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Окно обновления `maintenanceWindow` | setting | Выберите окно обновления для обновлений OneAgent (`<your-dynatrace-url>//ui/settings/builtin:deployment.management.update-windows`) | Required |