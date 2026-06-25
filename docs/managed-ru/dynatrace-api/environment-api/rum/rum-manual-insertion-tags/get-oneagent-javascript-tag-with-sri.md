---
title: GET OneAgent JavaScript tag with SRI
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-oneagent-javascript-tag-with-sri
scraped: 2026-05-12T12:05:55.370431
---

# GET OneAgent JavaScript tag with SRI

# GET OneAgent JavaScript tag with SRI

* Reference
* Updated on Sep 18, 2025

Возвращает самый последний [OneAgent JavaScript tag with SRI](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#oneagent-js-tag-sri "Выберите формат фрагмента RUM JavaScript, который лучше всего подходит для вашего сценария.") для ручного внедрения в код вашего веб-приложения. Он включает конфигурацию, ссылку на код мониторинга и хеш целостности. Подробнее о поддержке SRI для RUM см. [Use Subresource Integrity (SRI) for Real User Monitoring code](/managed/observe/digital-experience/web-applications/initial-setup/subresource-integrity "Используйте браузерную функцию Subresource Integrity (SRI) для обеспечения целостности кода Real User Monitoring.").

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/rum/oneAgentJavaScriptTagWithSri/{applicationId}` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/rum/oneAgentJavaScriptTagWithSri/{applicationId}` |

## Аутентификация

Для выполнения запроса необходим access token со scope `rumManualInsertionTags.read`.

О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| applicationId | string | ID веб-приложения. | path | Required |
| scriptExecutionAttribute | string | Задаёт атрибут выполнения скрипта: async, defer или none. Если задан, переопределяет настроенное значение. Возможные значения: * `ASYNC` * `DEFER` * `NONE` | query | Optional |

## Ответ

Ответ содержит данные в формате `text/plain` с самой последней версией [OneAgent JavaScript tag with SRI](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#oneagent-js-tag-sri "Выберите формат фрагмента RUM JavaScript, который лучше всего подходит для вашего сценария.") для указанного приложения.