---
title: Settings API - PHP schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-monitored-technologies-php
scraped: 2026-05-12T11:42:37.679277
---

# Settings API - PHP schema table

# Settings API - PHP schema table

* Published Dec 05, 2023

### PHP (`builtin:monitored-technologies.php)`

По умолчанию мониторинг PHP включён на всех хостах. Если вы хотите отключить мониторинг PHP на отдельных хостах, отключите его на этих хостах через их настройки.

Если вы хотите включить мониторинг PHP только на отдельных хостах, отключите глобальный мониторинг PHP и включите его на этих хостах через их настройки.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:monitored-technologies.php` | - | `HOST` - Host  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitored-technologies.php` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:monitored-technologies.php` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitored-technologies.php` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Мониторить PHP `enabled` | boolean | - | Required |
| Включить FastCGI-процессы PHP, запущенные Apache HTTP Server `enabledFastCGI` | boolean | Требуется включённый мониторинг PHP; начиная с Dynatrace OneAgent версии 1.191 параметр игнорируется и постоянно включён | Required |
| Мониторить веб-сервер PHP CLI `enablePhpCliServerInstrumentation` | boolean | Требуется включённый мониторинг PHP и Dynatrace OneAgent версии 1.261 или новее | Required |