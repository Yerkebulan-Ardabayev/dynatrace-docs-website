---
title: Settings API - Infrastructure & Operations app settings schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-infraops-settings
scraped: 2026-05-12T11:42:17.034795
---

# Settings API - Infrastructure & Operations app settings schema table

# Settings API - Infrastructure & Operations app settings schema table

* Published May 27, 2024

### Настройки приложения Infrastructure & Operations (`app:dynatrace.infraops:settings)`

Используйте эти настройки для кастомизации работы приложения I&O. Обратите внимание: чтобы изменения вступили в силу, нужно перезагрузить приложение.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.infraops:settings` | - | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.infraops:settings` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.infraops:settings` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.infraops:settings` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Показывать кандидатов на мониторинг `show.monitoring.candidates` | boolean | Если установлено в true, приложение будет отображать кандидатов на мониторинг в таблице Hosts | Required |
| Показывать только app-хосты `show.standalone.hosts` | boolean | Если установлено в true, приложение будет отображать только app-хосты в таблице Hosts | Required |
| Порог насыщения сетевого интерфейса `interface.saturation.threshold` | float | Порог, при котором интерфейс сетевого устройства считается насыщенным. | Required |
| Ограничить количество сущностей в основных инвентарях `invex.dql.query.limit` | integer | Ограничить количество результатов, возвращаемых из Grail для сущностей Host, Network device и Extensions. | Required |
| Ограничить количество сортируемых строк в инвентарях `invex.dql.sort.limit` | integer | Лимит для сортировки на стороне сервера в инвентарях Host, Network device и Extensions. Сортировка отключается, когда количество строк превышает заданный порог. | Required |