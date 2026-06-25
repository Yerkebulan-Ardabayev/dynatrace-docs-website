---
title: Web application configuration API - GET error rules
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/error-rules/get-configuration
scraped: 2026-05-12T11:16:47.475913
---

# Web application configuration API - GET error rules

# Web application configuration API - GET error rules

* Reference
* Published Sep 24, 2020

Возвращает конфигурацию правил ошибок в указанном приложении.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/web/{id}/errorRules` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/web/{id}/errorRules` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID нужного веб-приложения. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ApplicationErrorRules](#openapi-definition-ApplicationErrorRules) | Успех |

### Объекты тела ответа

#### Объект `ApplicationErrorRules`

Конфигурация правил ошибок в веб-приложении.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customErrorRules | [CustomErrorRule[]](#openapi-definition-CustomErrorRule) | Упорядоченный список пользовательских ошибок.  Правила оцениваются сверху вниз; применяется первое подходящее правило. |
| httpErrorRules | [HttpErrorRule[]](#openapi-definition-HttpErrorRule) | Упорядоченный список HTTP-ошибок.  Правила оцениваются сверху вниз; применяется первое подходящее правило. |
| ignoreCustomErrorsInApdexCalculation | boolean | Исключить (`true`) или включить (`false`) пользовательские ошибки, перечисленные в **customErrorRules**, в расчёт Apdex. |
| ignoreHttpErrorsInApdexCalculation | boolean | Исключить (`true`) или включить (`false`) HTTP-ошибки, перечисленные в **httpErrorRules**, в расчёт Apdex. |
| ignoreJavaScriptErrorsInApdexCalculation | boolean | Исключить (`true`) или включить (`false`) ошибки JavaScript в расчёт Apdex. |

#### Объект `CustomErrorRule`

Конфигурация пользовательской ошибки в веб-приложении.

| Элемент | Тип | Описание |
| --- | --- | --- |
| capture | boolean | Перехватывать (`true`) или игнорировать (`false`) ошибку. |
| customAlerting | boolean | Включить (`true`) или исключить (`false`) ошибку в [обнаружение и анализ проблем](https://dt-url.net/a963kd2) Davis AI. |
| impactApdex | boolean | Включить (`true`) или исключить (`false`) ошибку в расчёт Apdex. |
| keyMatcher | string | Операция сопоставления для **keyPattern**. Возможные значения: * `BEGINS_WITH` * `CONTAINS` * `ENDS_WITH` * `EQUALS` |
| keyPattern | string | Ключ искомой ошибки. |
| valueMatcher | string | Операция сопоставления для **valuePattern**. Возможные значения: * `BEGINS_WITH` * `CONTAINS` * `ENDS_WITH` * `EQUALS` |
| valuePattern | string | Значение искомой ошибки. |

#### Объект `HttpErrorRule`

Конфигурация HTTP-ошибки в веб-приложении.

| Элемент | Тип | Описание |
| --- | --- | --- |
| capture | boolean | Перехватывать (`true`) или игнорировать (`false`) ошибку. |
| considerBlockedRequests | boolean | Если `true`, сопоставлять по ошибкам с нарушениями правила CSP. |
| considerForAi | boolean | Включить (`true`) или исключить (`false`) ошибку в [обнаружение и анализ проблем](https://dt-url.net/a963kd2) Davis AI. |
| considerUnknownErrorCode | boolean | Если `true`, сопоставлять по ошибкам с неизвестным HTTP-кодом статуса. |
| errorCodes | string | HTTP-код статуса или диапазон кодов статуса для сопоставления.  Это поле обязательно, если **considerUnknownErrorCode** И **considerBlockedRequests** оба установлены в `false`. |
| filter | string | Правило сопоставления для URL. Возможные значения: * `BEGINS_WITH` * `CONTAINS` * `ENDS_WITH` * `EQUALS` |
| filterByUrl | boolean | Если `true`, фильтровать ошибки по URL. |
| impactApdex | boolean | Включить (`true`) или исключить (`false`) ошибку в расчёт Apdex. |
| url | string | Искомый URL. |

### JSON-модели тела ответа

```
{



"customErrorRules": [



{



"capture": true,



"customAlerting": true,



"impactApdex": true,



"keyMatcher": "BEGINS_WITH",



"keyPattern": "string",



"valueMatcher": "BEGINS_WITH",



"valuePattern": "string"



}



],



"httpErrorRules": [



{



"capture": true,



"considerBlockedRequests": true,



"considerForAi": true,



"considerUnknownErrorCode": true,



"errorCodes": "400",



"filter": "BEGINS_WITH",



"filterByUrl": true,



"impactApdex": true,



"url": "string"



}



],



"ignoreCustomErrorsInApdexCalculation": true,



"ignoreHttpErrorsInApdexCalculation": true,



"ignoreJavaScriptErrorsInApdexCalculation": true



}
```

## Связанные темы

* [Настройка обнаружения ошибок для веб-приложений](/managed/observe/digital-experience/web-applications/additional-configuration/configure-errors "Настройте захват или игнорирование ошибок запросов, пользовательских и JavaScript-ошибок.")