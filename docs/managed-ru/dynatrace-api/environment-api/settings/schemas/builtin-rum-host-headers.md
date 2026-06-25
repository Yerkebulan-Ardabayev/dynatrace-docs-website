---
title: Settings API - Identify host names schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-host-headers
scraped: 2026-05-12T11:39:12.521925
---

# Settings API - Identify host names schema table

# Settings API - Identify host names schema table

* Published Dec 05, 2023

### Идентификация имён хостов (`builtin:rum.host-headers)`

Укажите HTTP-заголовки запросов, которые OneAgent может использовать для идентификации имён хостов приложения, когда Dynatrace не может определить их автоматически. Указанные заголовки обрабатываются последовательно, приоритет имеют те, что выше в списке. Узнайте, почему это важно и когда определить имена не получается.

Dynatrace использует имена хостов как часть URL, который сопоставляется с правилами определения приложения; эти правила контролируют, когда OneAgent внедряет JavaScript-тег RUM. Например, если веб-сервер работает за файрволом и использует другое имя хоста, правило определения приложения не совпадёт и OneAgent не внедрит RUM в приложение.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.host-headers` | * `group:web-and-mobile-monitoring.web-applications` * `group:web-and-mobile-monitoring` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.host-headers` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.host-headers` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.host-headers` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Формат HTTP-заголовка `headerName` | text | - | Required |