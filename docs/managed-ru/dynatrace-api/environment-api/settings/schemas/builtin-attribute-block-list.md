---
title: Settings API - Blocked attributes schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-attribute-block-list
scraped: 2026-05-12T11:40:57.640587
---

# Settings API - Blocked attributes schema table

# Settings API - Blocked attributes schema table

* Published Feb 26, 2024

### Заблокированные атрибуты (`builtin:attribute-block-list)`

Dynatrace автоматически захватывает все атрибуты OpenTelemetry; чтобы избежать случайного сохранения персональных данных, можно исключить отдельные ключи атрибутов, значения которых не должны сохраняться. Это позволяет соответствовать требованиям приватности, контролируя объём сохраняемых данных мониторинга. Подробнее о настройках приватности Dynatrace см. документацию [Data privacy and security](https://dt-url.net/bo210srx).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:attribute-block-list` | * `group:service-monitoring` * `group:service-monitoring.spans` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:attribute-block-list` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:attribute-block-list` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:attribute-block-list` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | Если true, значение указанного ключа не сохраняется. | Required |
| Ключ атрибута `key` | text | Ключ атрибута, который не должен сохраняться | Required |