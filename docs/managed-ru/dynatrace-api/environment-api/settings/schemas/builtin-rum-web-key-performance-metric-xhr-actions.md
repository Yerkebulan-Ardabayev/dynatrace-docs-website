---
title: Settings API - Apdex configuration for XHR actions schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-key-performance-metric-xhr-actions
scraped: 2026-05-12T11:41:55.426214
---

# Settings API - Apdex configuration for XHR actions schema table

# Settings API - Apdex configuration for XHR actions schema table

* Published Dec 05, 2023

### Настройка Apdex для XHR-действий (`builtin:rum.web.key-performance-metric-xhr-actions)`

Выберите ключевую метрику производительности и задайте пороги Tolerating и Frustrated, чтобы [refine the Apdex calculations](https://dt-url.net/apdex-thresholds) для этого приложения.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.key-performance-metric-xhr-actions` | * `group:rum-kpm-settings` * `group:rum-settings` | `APPLICATION_METHOD` - User Action  `APPLICATION` - Web application |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.key-performance-metric-xhr-actions` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.key-performance-metric-xhr-actions` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.key-performance-metric-xhr-actions` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Ключевая метрика производительности `kpm` | enum | Возможные значения: * `USER_ACTION_DURATION` * `VISUALLY_COMPLETE` * `RESPONSE_END` * `RESPONSE_START` | Required |
| Пороги ключевой метрики производительности `thresholds` | [Thresholds](#Thresholds) | Задайте пороги производительности Tolerating и Frustrated для этого типа действия. | Required |
| Пороги fallback-метрики `fallbackThresholds` | [FallbackThresholds](#FallbackThresholds) | Если выбранная ключевая метрика производительности не обнаружена, используется метрика **User action duration**. | Required |

##### Объект `Thresholds`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Порог Tolerating `toleratedThresholdSeconds` | float | Если ключевая метрика производительности ниже этого значения, действие относится к зоне производительности Satisfied. | Required |
| Порог Frustrated `frustratingThresholdSeconds` | float | Если ключевая метрика производительности выше этого значения, действие относится к зоне производительности Frustrated. | Required |

##### Объект `FallbackThresholds`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Порог Tolerating [сек] `toleratedFallbackThresholdSeconds` | float | Если **User action duration** ниже этого значения, действие относится к зоне производительности Satisfied. | Required |
| Порог Frustrated [сек] `frustratingFallbackThresholdSeconds` | float | Если **User action duration** выше этого значения, действие относится к зоне производительности Frustrated. | Required |