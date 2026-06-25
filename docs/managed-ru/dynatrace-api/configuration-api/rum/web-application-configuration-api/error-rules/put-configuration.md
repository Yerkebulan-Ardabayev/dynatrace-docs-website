---
title: Web application configuration API - PUT error rules
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/error-rules/put-configuration
scraped: 2026-05-12T11:16:50.407322
---

# Web application configuration API - PUT error rules

# Web application configuration API - PUT error rules

* Reference
* Published Sep 24, 2020

Обновляет конфигурацию правил ошибок в указанном приложении.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/web/{id}/errorRules` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/web/{id}/errorRules` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID нужного веб-приложения. | path | Required |
| body | [ApplicationErrorRules](#openapi-definition-ApplicationErrorRules) | JSON-тело запроса. Содержит обновлённую конфигурацию правил ошибок. | body | Optional |

### Объекты тела запроса

#### Объект `ApplicationErrorRules`

Конфигурация правил ошибок в веб-приложении.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| customErrorRules | [CustomErrorRule[]](#openapi-definition-CustomErrorRule) | Упорядоченный список пользовательских ошибок.  Правила оцениваются сверху вниз; применяется первое подходящее правило. | Required |
| httpErrorRules | [HttpErrorRule[]](#openapi-definition-HttpErrorRule) | Упорядоченный список HTTP-ошибок.  Правила оцениваются сверху вниз; применяется первое подходящее правило. | Required |
| ignoreCustomErrorsInApdexCalculation | boolean | Исключить (`true`) или включить (`false`) пользовательские ошибки, перечисленные в **customErrorRules**, в расчёт Apdex. | Required |
| ignoreHttpErrorsInApdexCalculation | boolean | Исключить (`true`) или включить (`false`) HTTP-ошибки, перечисленные в **httpErrorRules**, в расчёт Apdex. | Required |
| ignoreJavaScriptErrorsInApdexCalculation | boolean | Исключить (`true`) или включить (`false`) ошибки JavaScript в расчёт Apdex. | Required |

#### Объект `CustomErrorRule`

Конфигурация пользовательской ошибки в веб-приложении.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| capture | boolean | Перехватывать (`true`) или игнорировать (`false`) ошибку. | Required |
| customAlerting | boolean | Включить (`true`) или исключить (`false`) ошибку в [обнаружение и анализ проблем](https://dt-url.net/a963kd2) Davis AI. | Required |
| impactApdex | boolean | Включить (`true`) или исключить (`false`) ошибку в расчёт Apdex. | Required |
| keyMatcher | string | Операция сопоставления для **keyPattern**. Возможные значения: * `BEGINS_WITH` * `CONTAINS` * `ENDS_WITH` * `EQUALS` | Optional |
| keyPattern | string | Ключ искомой ошибки. | Optional |
| valueMatcher | string | Операция сопоставления для **valuePattern**. Возможные значения: * `BEGINS_WITH` * `CONTAINS` * `ENDS_WITH` * `EQUALS` | Optional |
| valuePattern | string | Значение искомой ошибки. | Optional |

#### Объект `HttpErrorRule`

Конфигурация HTTP-ошибки в веб-приложении.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| capture | boolean | Перехватывать (`true`) или игнорировать (`false`) ошибку. | Required |
| considerBlockedRequests | boolean | Если `true`, сопоставлять по ошибкам с нарушениями правила CSP. | Optional |
| considerForAi | boolean | Включить (`true`) или исключить (`false`) ошибку в [обнаружение и анализ проблем](https://dt-url.net/a963kd2) Davis AI. | Required |
| considerUnknownErrorCode | boolean | Если `true`, сопоставлять по ошибкам с неизвестным HTTP-кодом статуса. | Required |
| errorCodes | string | HTTP-код статуса или диапазон кодов статуса для сопоставления.  Это поле обязательно, если **considerUnknownErrorCode** И **considerBlockedRequests** оба установлены в `false`. | Optional |
| filter | string | Правило сопоставления для URL. Возможные значения: * `BEGINS_WITH` * `CONTAINS` * `ENDS_WITH` * `EQUALS` | Optional |
| filterByUrl | boolean | Если `true`, фильтровать ошибки по URL. | Required |
| impactApdex | boolean | Включить (`true`) или исключить (`false`) ошибку в расчёт Apdex. | Required |
| url | string | Искомый URL. | Optional |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

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

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Конфигурация обновлена. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод |

### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```

## Связанные темы

* [Настройка обнаружения ошибок для веб-приложений](/managed/observe/digital-experience/web-applications/additional-configuration/configure-errors "Настройте захват или игнорирование ошибок запросов, пользовательских и JavaScript-ошибок.")