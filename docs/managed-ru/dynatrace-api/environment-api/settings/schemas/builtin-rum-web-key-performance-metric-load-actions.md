---
title: Settings API - Apdex configuration for load actions schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-key-performance-metric-load-actions
scraped: 2026-05-12T11:46:22.790442
---

# Settings API - Apdex configuration for load actions schema table

# Settings API - Apdex configuration for load actions schema table

* Published Dec 05, 2023

### Настройка Apdex для load-действий (`builtin:rum.web.key-performance-metric-load-actions)`

Выберите ключевую метрику производительности и задайте пороги Tolerating и Frustrated, чтобы [refine the Apdex calculations](https://dt-url.net/apdex-thresholds) для этого приложения.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.key-performance-metric-load-actions` | * `group:rum-kpm-settings` * `group:rum-settings` | `APPLICATION_METHOD` - User Action  `APPLICATION` - Web application |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.key-performance-metric-load-actions` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.key-performance-metric-load-actions` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.key-performance-metric-load-actions` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Ключевая метрика производительности `kpm` | enum | Возможные значения: * `USER_ACTION_DURATION` * `VISUALLY_COMPLETE` * `SPEED_INDEX` * `DOM_INTERACTIVE` * `LOAD_EVENT_END` * `LOAD_EVENT_START` * `RESPONSE_END` * `RESPONSE_START` * `FIRST_INPUT_DELAY` * `LARGEST_CONTENTFUL_PAINT` * `CUMULATIVE_LAYOUT_SHIFT` | Required |
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