---
title: Settings API - Access tokens schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-tokens-token-settings
scraped: 2026-05-12T11:41:15.495240
---

# Settings API - Access tokens schema table

# Settings API - Access tokens schema table

* Published Dec 05, 2023

### Access tokens (`builtin:tokens.token-settings)`

Настройте генерацию access token Dynatrace API и personal access token. Подробнее о токенах и аутентификации см. [Dynatrace API authentication documentation](https://dt-url.net/8543sda).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:tokens.token-settings` | * `group:integration.token-management` * `group:integration` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:tokens.token-settings` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:tokens.token-settings` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:tokens.token-settings` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Создавать токены Dynatrace API в новом формате `newDynatraceTokenFormatEnabled` | boolean | См. этот [blog post](https://dt-url.net/ho02y5r) с подробностями о новом формате токенов Dynatrace API. | Required |
| Включить personal access tokens `patEnabled` | boolean | Разрешить пользователям этого окружения генерировать personal access tokens на основе разрешений пользователя. Учтите, что существующие personal access tokens становятся непригодными к использованию, пока эта настройка отключена. | Required |