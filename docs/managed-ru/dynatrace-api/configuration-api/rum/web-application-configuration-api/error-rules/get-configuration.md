---
title: Web application configuration API - GET error rules
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/error-rules/get-configuration
---

# Web application configuration API - GET error rules

# Web application configuration API - GET error rules

* Справка
* Опубликовано 24 сен. 2020 г.

Получение конфигурации правил ошибок в указанном приложении.

Запрос формирует полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace для Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/web/{id}/errorRules` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/web/{id}/errorRules` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `ReadConfig`.

Подробнее о том, как получить и использовать токен, см. в разделе [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID нужного веб-приложения. | путь | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ApplicationErrorRules](#openapi-definition-ApplicationErrorRules) | Успешно |

### Объекты тела ответа

#### Объект `ApplicationErrorRules`

Конфигурация правил ошибок в веб-приложении.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customErrorRules | [CustomErrorRule](#openapi-definition-CustomErrorRule)[] | Упорядоченный список пользовательских ошибок. Правила проверяются сверху вниз, применяется первое совпавшее правило. |
| httpErrorRules | [HttpErrorRule](#openapi-definition-HttpErrorRule)[] | Упорядоченный список ошибок HTTP. Правила проверяются сверху вниз, применяется первое совпавшее правило. |
| ignoreCustomErrorsInApdexCalculation | boolean | Исключить (`true`) или включить (`false`) в расчёт Apdex пользовательские ошибки, перечисленные в **customErrorRules**. |
| ignoreHttpErrorsInApdexCalculation | boolean | Исключить (`true`) или включить (`false`) в расчёт Apdex ошибки HTTP, перечисленные в **httpErrorRules**. |
| ignoreJavaScriptErrorsInApdexCalculation | boolean | Исключить (`true`) или включить (`false`) в расчёт Apdex ошибки JavaScript. |

#### Объект `CustomErrorRule`

Конфигурация пользовательской ошибки в веб-приложении.

| Элемент | Тип | Описание |
| --- | --- | --- |
| capture | boolean | Захватывать (`true`) или игнорировать (`false`) ошибку. |
| customAlerting | boolean | Учитывать (`true`) или не учитывать (`false`) ошибку в Davis AI [обнаружении и анализе проблем﻿](https://dt-url.net/a963kd2?dt=m). |
| impactApdex | boolean | Учитывать (`true`) или не учитывать (`false`) ошибку в расчёте Apdex. |
| keyMatcher | string | Операция сопоставления для **keyPattern**. Элемент может принимать следующие значения * `BEGINS_WITH` * `CONTAINS` * `ENDS_WITH` * `EQUALS` |
| keyPattern | string | Ключ ошибки для поиска. |
| valueMatcher | string | Операция сопоставления для **valuePattern**. Элемент может принимать следующие значения * `BEGINS_WITH` * `CONTAINS` * `ENDS_WITH` * `EQUALS` |
| valuePattern | string | Значение ошибки для поиска. |

#### Объект `HttpErrorRule`

Конфигурация ошибки HTTP в веб-приложении.

| Элемент | Тип | Описание |
| --- | --- | --- |
| capture | boolean | Захватывать (`true`) или игнорировать (`false`) ошибку. |
| considerBlockedRequests | boolean | Если `true`, сопоставлять по ошибкам, у которых есть нарушения правил CSP. |
| considerForAi | boolean | Учитывать (`true`) или не учитывать (`false`) ошибку в Davis AI [обнаружении и анализе проблем﻿](https://dt-url.net/a963kd2?dt=m). |
| considerUnknownErrorCode | boolean | Если `true`, сопоставлять по ошибкам с неизвестным кодом статуса HTTP. |
| errorCodes | string | Код статуса HTTP или диапазон кодов статуса для сопоставления. Это поле обязательно, если **considerUnknownErrorCode** И **considerBlockedRequests** оба установлены в `false`. |
| filter | string | Правило сопоставления для URL. Элемент может принимать следующие значения * `BEGINS_WITH` * `CONTAINS` * `ENDS_WITH` * `EQUALS` |
| filterByUrl | boolean | Если `true`, фильтровать ошибки по URL. |
| impactApdex | boolean | Учитывать (`true`) или не учитывать (`false`) ошибку в расчёте Apdex. |
| url | string | URL для поиска. |

### Модели JSON тела ответа

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

## Похожие темы

* [Настройка обнаружения ошибок для веб-приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-errors "Настройте приложение для захвата или игнорирования ошибок запросов, пользовательских ошибок и ошибок JavaScript.")