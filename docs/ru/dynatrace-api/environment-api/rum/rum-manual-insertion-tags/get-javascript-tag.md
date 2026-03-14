---
title: Получение тега JavaScript
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-javascript-tag
scraped: 2026-03-05T21:32:40.132058
---

# GET JavaScript tag

# GET JavaScript tag

* Reference
* Обновлено 18 сентября 2025 г.

Возвращает актуальный [JavaScript tag](../../../../observe/digital-experience/web-applications/initial-setup/snippet-formats.md#js-tag "Выберите формат RUM JavaScript-сниппета, наиболее подходящий для вашего конкретного случая использования") для ручной вставки в код вашего веб-приложения. Тег включает ссылку на внешний файл, содержащий как код мониторинга, так и его конфигурацию.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/rum/javaScriptTag/{applicationId}` |
| GET | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/rum/javaScriptTag/{applicationId}` |

## Аутентификация

Для выполнения этого запроса вам необходим токен доступа с областью действия `rumManualInsertionTags.read`.

Чтобы узнать, как его получить и использовать, см. [Токены и аутентификация](../../../../discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication.md).

## Параметры

| Параметр | Тип | Описание | Передаётся в | Обязательный |
| --- | --- | --- | --- | --- |
| applicationId | string | Идентификатор веб-приложения. | path | Обязательный |
| scriptExecutionAttribute | string | Задаёт атрибут выполнения скрипта: async, defer или none. Если указан, переопределяет настроенное значение. Допустимые значения: * `ASYNC` * `DEFER` * `NONE` | query | Необязательный |
| crossOriginAnonymous | boolean | Указывает, нужно ли добавлять атрибут crossorigin="anonymous" к тегу. Если указан, переопределяет настроенное значение. | query | Необязательный |

## Ответ

Ответ содержит полезную нагрузку `text/plain` с актуальной версией [JavaScript tag](../../../../observe/digital-experience/web-applications/initial-setup/snippet-formats.md#js-tag "Выберите формат RUM JavaScript-сниппета, наиболее подходящий для вашего конкретного случая использования") для указанного приложения.
