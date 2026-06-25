---
title: Settings API - Apdex configuration for custom actions schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-key-performance-metric-custom-actions
scraped: 2026-05-12T11:43:16.876223
---

# Settings API - Apdex configuration for custom actions schema table

# Settings API - Apdex configuration for custom actions schema table

* Published Dec 05, 2023

### Настройка Apdex для пользовательских действий (`builtin:rum.web.key-performance-metric-custom-actions)`

Задайте пороги производительности Tolerating и Frustrated, чтобы [refine the Apdex calculations](https://dt-url.net/apdex-thresholds) для этого приложения.

Ключевая метрика производительности для пользовательских действий всегда **User action duration**.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.key-performance-metric-custom-actions` | * `group:rum-kpm-settings` * `group:rum-settings` | `APPLICATION_METHOD` - User Action  `APPLICATION` - Web application |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.key-performance-metric-custom-actions` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.key-performance-metric-custom-actions` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.key-performance-metric-custom-actions` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Пороги User action duration `thresholds` | [Thresholds](#Thresholds) | - | Required |

##### Объект `Thresholds`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Порог Tolerating [сек] `toleratedThresholdSeconds` | float | Если **User action duration** ниже этого значения, действие относится к зоне производительности Satisfied. | Required |
| Порог Frustrated [сек] `frustratingThresholdSeconds` | float | Если **User action duration** выше этого значения, действие относится к зоне производительности Frustrated. | Required |