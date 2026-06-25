---
title: Settings API - AIX kernel extension schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-host-monitoring-aix-kernel-extension
scraped: 2026-05-12T11:45:44.619720
---

# Settings API - AIX kernel extension schema table

# Settings API - AIX kernel extension schema table

* Published Dec 05, 2023

### Расширение ядра AIX (`builtin:host.monitoring.aix-kernel-extension)`

Dynatrace может автоматически инжектировать модули глубокого мониторинга кода OneAgent для мониторинга AIX. В противном случае требуется ручное инструментирование для мониторинга приложений Java, Apache, WebLogic и Websphere на AIX. Подробнее см. [Install OneAgent on AIX](https://dt-url.net/l24t0pm1).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:host.monitoring.aix-kernel-extension` | - | `HOST` - Host |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:host.monitoring.aix-kernel-extension` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:host.monitoring.aix-kernel-extension` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:host.monitoring.aix-kernel-extension` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Использовать глобальные настройки `useGlobalSettings` | boolean | - | Required |
| Разрешить расширение ядра AIX `enabled` | boolean | - | Required |