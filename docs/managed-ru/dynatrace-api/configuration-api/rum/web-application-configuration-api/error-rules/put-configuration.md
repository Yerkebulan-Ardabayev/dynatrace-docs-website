---
title: Web application configuration API - PUT error rules
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/error-rules/put-configuration
---

# Web application configuration API - PUT error rules

# Web application configuration API - PUT error rules

* Справка
* Опубликовано 24 сентября 2020

Обновляет конфигурацию правил ошибок в указанном приложении.

Запрос принимает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/web/{id}/errorRules` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/web/{id}/errorRules` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

О том, как получить и использовать токен, читай в разделе [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID нужного веб-приложения. | path | Обязательный |
| body | [ApplicationErrorRules](#openapi-definition-ApplicationErrorRules) | Тело JSON запроса. Содержит обновлённую конфигурацию правил ошибок. | body | Опциональный |

### Объекты тела запроса

#### Объект `ApplicationErrorRules`

Конфигурация правил ошибок в веб-приложении.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| customErrorRules | [CustomErrorRule](#openapi-definition-CustomErrorRule)[] | Упорядоченный список пользовательских ошибок. Правила проверяются сверху вниз, применяется первое подходящее правило. | Обязательный |
| httpErrorRules | [HttpErrorRule](#openapi-definition-HttpErrorRule)[] | Упорядоченный список HTTP-ошибок. Правила проверяются сверху вниз, применяется первое подходящее правило. | Обязательный |
| ignoreCustomErrorsInApdexCalculation | boolean | Исключить (`true`) или включить (`false`) пользовательские ошибки, перечисленные в **customErrorRules**, в расчёт Apdex. | Обязательный |
| ignoreHttpErrorsInApdexCalculation | boolean | Исключить (`true`) или включить (`false`) HTTP-ошибки, перечисленные в **httpErrorRules**, в расчёт Apdex. | Обязательный |
| ignoreJavaScriptErrorsInApdexCalculation | boolean | Исключить (`true`) или включить (`false`) ошибки JavaScript в расчёт Apdex. | Обязательный |

#### Объект `CustomErrorRule`

Конфигурация пользовательской ошибки в веб-приложении.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| capture | boolean | Захватывать (`true`) или игнорировать (`false`) ошибку. | Обязательный |
| customAlerting | boolean | Включить (`true`) или исключить (`false`) ошибку из Davis AI [обнаружения и анализа проблем﻿](https://dt-url.net/a963kd2?dt=m). | Обязательный |
| impactApdex | boolean | Включить (`true`) или исключить (`false`) ошибку из расчёта Apdex. | Обязательный |
| keyMatcher | string | Операция сопоставления для **keyPattern**. Элемент может принимать значения * `BEGINS_WITH` * `CONTAINS` * `ENDS_WITH` * `EQUALS` | Опциональный |
| keyPattern | string | Ключ ошибки для поиска. | Опциональный |
| valueMatcher | string | Операция сопоставления для **valuePattern**. Элемент может принимать значения * `BEGINS_WITH` * `CONTAINS` * `ENDS_WITH` * `EQUALS` | Опциональный |
| valuePattern | string | Значение ошибки для поиска. | Опциональный |

#### Объект `HttpErrorRule`

Конфигурация HTTP-ошибки в веб-приложении.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| capture | boolean | Захватывать (`true`) или игнорировать (`false`) ошибку. | Обязательный |
| considerBlockedRequests | boolean | Если `true`, сопоставлять по ошибкам с нарушениями правил CSP. | Опциональный |
| considerForAi | boolean | Включить (`true`) или исключить (`false`) ошибку из Davis AI [обнаружения и анализа проблем﻿](https://dt-url.net/a963kd2?dt=m). | Обязательный |
| considerUnknownErrorCode | boolean | Если `true`, сопоставлять по ошибкам с неизвестным кодом статуса HTTP. | Обязательный |
| errorCodes | string | Код статуса HTTP или диапазон кодов статуса для сопоставления. Это поле обязательно, если **considerUnknownErrorCode** И **considerBlockedRequests** оба установлены в `false`. | Опциональный |
| filter | string | Правило сопоставления для URL. Элемент может принимать значения * `BEGINS_WITH` * `CONTAINS` * `ENDS_WITH` * `EQUALS` | Опциональный |
| filterByUrl | boolean | Если `true`, фильтровать ошибки по URL. | Обязательный |
| impactApdex | boolean | Включить (`true`) или исключить (`false`) ошибку из расчёта Apdex. | Обязательный |
| url | string | URL для поиска. | Опциональный |

### Модель тела JSON запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать для использования в реальном запросе.

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
| **204** | - | Успешно. Конфигурация обновлена. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные недопустимы. |

### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | Код статуса HTTP |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Модели тела JSON ответа

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

## Смежные темы

* [Настройка обнаружения ошибок для веб-приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-errors "Настройте приложение для захвата или игнорирования ошибок запросов, пользовательских и JavaScript-ошибок.")