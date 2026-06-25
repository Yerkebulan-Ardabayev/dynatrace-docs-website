---
title: Settings API - Allowed attributes schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-attribute-allow-list
scraped: 2026-05-12T11:47:32.791958
---

# Settings API - Allowed attributes schema table

# Settings API - Allowed attributes schema table

* Published Dec 05, 2023

### Разрешённые атрибуты (`builtin:attribute-allow-list)`

Dynatrace автоматически захватывает все атрибуты OpenTelemetry; чтобы избежать случайного сохранения персональных данных, сохраняются только значения тех атрибутов, ключи которых указаны в allow-list ниже. Это позволяет соответствовать требованиям приватности, контролируя объём сохраняемых данных мониторинга. Подробнее о настройках приватности Dynatrace см. документацию [Data privacy and security](https://dt-url.net/bo210srx).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:attribute-allow-list` | * `group:service-monitoring` * `group:service-monitoring.spans` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:attribute-allow-list` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:attribute-allow-list` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:attribute-allow-list` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | Если true, значение указанного ключа сохраняется. | Required |
| Ключ атрибута `key` | text | Ключ атрибута, который нужно сохранять | Required |