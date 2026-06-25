---
title: Settings API - Outage handling schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-synthetic-multiprotocol-outage-handling
scraped: 2026-05-12T11:45:56.012075
---

# Settings API - Outage handling schema table

# Settings API - Outage handling schema table

* Published Jul 31, 2024

### Обработка простоев (`builtin:synthetic.multiprotocol.outage-handling)`

Dynatrace может генерировать проблемы как для глобальных, так и для локальных простоев на основе доступности всех настроенных расположений или только отдельных расположений в последовательных прогонах.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:synthetic.multiprotocol.outage-handling` | * `group:web-and-mobile-monitoring` * `group:synthetic.multiprotocol` * `group:web-and-mobile-monitoring.multiprotocol-monitor-default-settings` | `MULTIPROTOCOL_MONITOR` - Network availability monitor  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.multiprotocol.outage-handling` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:synthetic.multiprotocol.outage-handling` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.multiprotocol.outage-handling` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Генерировать проблему и отправлять оповещение, когда монитор недоступен во всех настроенных расположениях. `globalOutages` | boolean | - | Required |
| Оповестить, если все расположения не могут получить доступ к целевому адресу `globalConsecutiveOutageCountThreshold` | integer | - | Required |
| Генерировать проблему и отправлять оповещение, когда монитор недоступен в течение одного или нескольких последовательных прогонов в любом расположении. `localOutages` | boolean | - | Required |
| Оповестить, если как минимум `localLocationOutageCountThreshold` | integer | - | Required |
| не могут получить доступ к целевому адресу `localConsecutiveOutageCountThreshold` | integer | - | Required |