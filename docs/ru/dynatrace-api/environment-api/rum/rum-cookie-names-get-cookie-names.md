---
title: RUM cookie names API - GET cookie names
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/rum/rum-cookie-names-get-cookie-names
scraped: 2026-03-06T21:28:53.298305
---

# RUM cookie names API — GET: получение имён cookie

# RUM cookie names API — GET: получение имён cookie

* Reference
* Published Jun 25, 2024

Возвращает список имён cookie RUM.

Запрос возвращает полезную нагрузку типа `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/rum/cookieNames` |
| GET | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/rum/cookieNames` |

## Аутентификация

Для выполнения этого запроса необходим токен доступа с областью действия `rumCookieNames.read`.

Чтобы узнать, как получить и использовать токен, см. раздел [Токены и аутентификация](../../../discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication.md).

## Параметры

Запрос не имеет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [CookieNames](#openapi-definition-CookieNames) | Успешно. Ответ содержит все имена cookie RUM |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `CookieNames`

Список всех имён cookie.

| Элемент | Тип | Описание |
| --- | --- | --- |
| domainValidationCookieName | string | Имя cookie для проверки домена. |
| latencyCookieName | string | Имя cookie задержки. |
| pageContextCookieName | string | Имя cookie контекста страницы. |
| sessionCookieName | string | Имя cookie сессии. |
| sessionReplayViewIdCookieName | string | Имя cookie идентификатора просмотра в записи сессии. |
| sessionTimeoutCookieName | string | Имя cookie тайм-аута сессии. |
| sourceActionCookieName | string | Имя cookie действия-источника. |
| visitorCookieName | string | Имя cookie посетителя. |

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
| parameterLocation | string | -Элемент может принимать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"domainValidationCookieName": "dtValidationCookie",



"latencyCookieName": "dtLatC",



"pageContextCookieName": "dtPC",



"sessionCookieName": "dtCookie",



"sessionReplayViewIdCookieName": "dtsrVID",



"sessionTimeoutCookieName": "rxvt",



"sourceActionCookieName": "dtSA",



"visitorCookieName": "rxVisitor"



}
```

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

* [Real User Monitoring](../../../observe/digital-experience/rum-concepts/rum-overview.md "Learn about Real User Monitoring, key performance metrics, mobile app monitoring, and more.")
* [Cookie-файлы](../../../manage/data-privacy-and-security/data-privacy/cookies.md "Learn about first-party cookie usage in Dynatrace.")
