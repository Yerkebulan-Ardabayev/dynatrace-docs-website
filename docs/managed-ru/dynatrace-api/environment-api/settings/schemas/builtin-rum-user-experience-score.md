---
title: Settings API - User experience score schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-user-experience-score
scraped: 2026-05-12T11:45:48.369609
---

# Settings API - User experience score schema table

# Settings API - User experience score schema table

* Published Dec 05, 2023

### Оценка пользовательского опыта (`builtin:rum.user-experience-score)`

Для каждой пользовательской сессии рассчитывается [user experience score](https://dt-url.net/39034wt). Оценки отражают общую производительность, удобство использования и обнаруженные ошибки каждой сессии. Опыт классифицируется как Satisfying, Tolerable или Frustrating.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.user-experience-score` | * `group:web-and-mobile-monitoring` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.user-experience-score` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.user-experience-score` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.user-experience-score` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Если последнее пользовательское действие в сессии классифицировано как Frustrating, классифицировать всю сессию как Frustrating `considerLastAction` | boolean | - | Required |
| Учитывать rage-клики и rage-тапы при расчёте оценки `considerRageClick` | boolean | - | Required |
| Порог для Frustrating user experience `maxFrustratedUserActionsThreshold` | integer | User experience считается Frustrating, когда выбранный процент или больше пользовательских действий в сессии оценены как Frustrating. | Required |
| Порог для Satisfying user experience `minSatisfiedUserActionsThreshold` | integer | User experience считается Satisfying, когда минимум выбранный процент пользовательских действий в сессии оценены как Satisfying. | Required |