---
title: Settings API - Apdex configuration schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-mobile-key-performance-metrics
scraped: 2026-05-12T11:47:31.013631
---

# Settings API - Apdex configuration schema table

# Settings API - Apdex configuration schema table

* Published Dec 05, 2023

### Настройка Apdex (`builtin:rum.mobile.key-performance-metrics)`

[Set the user-satisfaction performance thresholds](https://dt-url.net/4l023z2) (**Satisfactory**, **Tolerable** и **Frustrating**) для метрики **User action duration**, чтобы уточнить расчёты Apdex для этого приложения.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.mobile.key-performance-metrics` | * `group:rum-general` | `DEVICE_APPLICATION_METHOD` - Mobile app key user action  `MOBILE_APPLICATION` - Mobile App  `CUSTOM_APPLICATION` - Custom Application |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.mobile.key-performance-metrics` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.mobile.key-performance-metrics` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.mobile.key-performance-metrics` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| `thresholds` | [Thresholds](#Thresholds) | - | Required |
| Учитывать сообщённые ошибки и ошибки web-запросов в расчётах Apdex `frustratingIfReportedOrWebRequestError` | boolean | Считать пользовательские действия с сообщёнными ошибками или ошибками web-запросов ошибочными и оценивать их производительность как Frustrating. Отключите эту настройку, если ошибки не должны влиять на показатель Apdex. | Required |

##### Объект `Thresholds`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Tolerable performance [сек] `tolerableThresholdSeconds` | float | Если длительность действия ниже этого значения, Apdex считается **Satisfactory**. | Required |
| Frustrating performance [сек] `frustratingThresholdSeconds` | float | Если длительность действия выше этого значения, Apdex считается **Frustrating**. | Required |