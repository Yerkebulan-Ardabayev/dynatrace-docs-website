---
title: GET OneAgent JavaScript tag with SRI
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-oneagent-javascript-tag-with-sri
scraped: 2026-03-01T21:25:54.381923
---

# GET тег OneAgent JavaScript с SRI

# GET тег OneAgent JavaScript с SRI

* Справочник
* Обновлено 18 сентября 2025 г.

Возвращает самую актуальную версию [тега OneAgent JavaScript с SRI](../../../../observe/digital-experience/web-applications/initial-setup/snippet-formats.md#oneagent-js-tag-sri "Выберите формат фрагмента RUM JavaScript, который наилучшим образом соответствует вашему конкретному варианту использования") для ручного встраивания в код вашего веб-приложения. Он включает конфигурацию, ссылку на код мониторинга и хэш целостности. Дополнительные сведения о поддержке SRI для RUM см. в разделе [Использование Subresource Integrity (SRI) для кода мониторинга реальных пользователей](../../../../observe/digital-experience/web-applications/initial-setup/subresource-integrity.md "Используйте функцию браузера Subresource Integrity (SRI), чтобы обеспечить целостность кода мониторинга реальных пользователей.").

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/rum/oneAgentJavaScriptTagWithSri/{applicationId}` |
| GET | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/rum/oneAgentJavaScriptTagWithSri/{applicationId}` |

## Аутентификация

Для выполнения этого запроса необходим токен доступа с областью действия `rumManualInsertionTags.read`.

Сведения о том, как получить и использовать токен, см. в разделе [Токены и аутентификация](../../../../discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication.md).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| applicationId | string | Идентификатор веб-приложения. | path | Обязательный |
| scriptExecutionAttribute | string | Задаёт атрибут выполнения скрипта: async, defer или none. Если указан, переопределяет настроенное значение. Элемент может принимать следующие значения: * `ASYNC` * `DEFER` * `NONE` | query | Необязательный |

## Ответ

Ответ содержит полезную нагрузку `text/plain` с самой актуальной версией [тега OneAgent JavaScript с SRI](../../../../observe/digital-experience/web-applications/initial-setup/snippet-formats.md#oneagent-js-tag-sri "Выберите формат фрагмента RUM JavaScript, который наилучшим образом соответствует вашему конкретному варианту использования") для указанного приложения.
