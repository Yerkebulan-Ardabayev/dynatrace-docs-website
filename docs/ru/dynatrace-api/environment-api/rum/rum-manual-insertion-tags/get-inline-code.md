---
title: GET inline code
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-inline-code
scraped: 2026-03-04T21:33:10.946309
---

# GET inline code

# GET inline code

* Reference
* Updated on Sep 18, 2025

Возвращает самую последнюю версию [встроенного кода](../../../../observe/digital-experience/web-applications/initial-setup/snippet-formats.md#inline-code "Select a format for the RUM JavaScript snippet that best fits your specific use case") для ручной вставки в код вашего веб-приложения. Включает как конфигурацию, так и код мониторинга RUM.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/rum/inlineCode/{applicationId}` |
| GET | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/rum/inlineCode/{applicationId}` |

## Аутентификация

Для выполнения этого запроса вам необходим токен доступа с областью разрешений `rumManualInsertionTags.read`.

Сведения о том, как получить и использовать токен, см. в разделе [Токены и аутентификация](../../../../discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication.md).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| applicationId | string | Идентификатор веб-приложения. | path | Обязательный |

## Ответ

Ответ содержит полезную нагрузку типа `text/plain` с последней версией [встроенного кода](../../../../observe/digital-experience/web-applications/initial-setup/snippet-formats.md#inline-code "Select a format for the RUM JavaScript snippet that best fits your specific use case") для указанного приложения.
