---
title: GET OneAgent JavaScript tag
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-oneagent-javascript-tag
scraped: 2026-03-02T21:19:10.698775
---

Возвращает наиболее актуальный [тег JavaScript OneAgent](../../../../observe/digital-experience/web-applications/initial-setup/snippet-formats.md#oneagent-js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case") для ручной вставки в код вашего веб-приложения. Включает конфигурацию и ссылку на код мониторинга.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/rum/oneAgentJavaScriptTag/{applicationId}` |
| GET | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/rum/oneAgentJavaScriptTag/{applicationId}` |

## Аутентификация

Для выполнения этого запроса требуется токен доступа с областью действия `rumManualInsertionTags.read`.

Чтобы узнать, как получить и использовать токен, см. раздел Tokens and authentication.

## Параметры

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| applicationId | string | Идентификатор веб-приложения. | path | Required |
| scriptExecutionAttribute | string | Задаёт атрибут выполнения скрипта: async, defer или none. Если указан, переопределяет настроенное значение. Допустимые значения: * `ASYNC` * `DEFER` * `NONE` | query | Optional |

## Ответ

Ответ содержит полезную нагрузку `text/plain` с наиболее актуальной версией [тега JavaScript OneAgent](../../../../observe/digital-experience/web-applications/initial-setup/snippet-formats.md#oneagent-js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case") для указанного приложения.
