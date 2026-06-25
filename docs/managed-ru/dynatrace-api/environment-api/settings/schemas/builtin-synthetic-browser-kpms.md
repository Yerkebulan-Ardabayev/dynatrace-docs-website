---
title: Settings API - Key performance metrics schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-synthetic-browser-kpms
scraped: 2026-05-12T11:46:38.360970
---

# Settings API - Key performance metrics schema table

# Settings API - Key performance metrics schema table

* Published Dec 05, 2023

### Ключевые метрики производительности (`builtin:synthetic.browser.kpms)`

Выберите [key performance metric](https://dt-url.net/kpms), которая лучше всего отражает пользовательский опыт этого synthetic-монитора.

**Visually complete**: метрика по умолчанию для load- и XHR-действий. Она измеряет, сколько времени нужно для полной отрисовки видимой части экрана браузера пользователя.

Ключевая метрика производительности для пользовательских действий всегда **User action duration**.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:synthetic.browser.kpms` | * `group:synthetic.browser` | `SYNTHETIC_TEST` - Synthetic monitor |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.browser.kpms` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:synthetic.browser.kpms` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.browser.kpms` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Ключевая метрика производительности load-действия `loadActionKpm` | enum | Возможные значения: * `USER_ACTION_DURATION` * `VISUALLY_COMPLETE` * `SPEED_INDEX` * `DOM_INTERACTIVE` * `LOAD_EVENT_START` * `LOAD_EVENT_END` * `RESPONSE_START` * `RESPONSE_END` * `LARGEST_CONTENTFUL_PAINT` * `CUMULATIVE_LAYOUT_SHIFT` | Required |
| Ключевая метрика производительности XHR-действия `xhrActionKpm` | enum | Возможные значения: * `USER_ACTION_DURATION` * `VISUALLY_COMPLETE` * `RESPONSE_START` * `RESPONSE_END` | Required |