---
title: GET inline code
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-inline-code
scraped: 2026-05-12T12:05:53.574118
---

# GET inline code

# GET inline code

* Reference
* Updated on Sep 18, 2025

Возвращает самый последний [inline code](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#inline-code "Выберите формат фрагмента RUM JavaScript, который лучше всего подходит для вашего сценария.") для ручного внедрения в код вашего веб-приложения. Он включает как конфигурацию, так и код мониторинга RUM.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/rum/inlineCode/{applicationId}` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/rum/inlineCode/{applicationId}` |

## Аутентификация

Для выполнения запроса необходим access token со scope `rumManualInsertionTags.read`.

О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| applicationId | string | ID веб-приложения. | path | Required |

## Ответ

Ответ содержит данные в формате `text/plain` с самой последней версией [inline code](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#inline-code "Выберите формат фрагмента RUM JavaScript, который лучше всего подходит для вашего сценария.") для указанного приложения.