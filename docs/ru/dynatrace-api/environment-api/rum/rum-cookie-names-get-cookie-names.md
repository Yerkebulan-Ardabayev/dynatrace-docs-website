---
title: Имена файлов cookie RUM API - Получение имен файлов cookie
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/rum/rum-cookie-names-get-cookie-names
scraped: 2026-03-06T21:28:53.298305
---

# RUM cookie names API — GET: получение имён cookie


Возвращает список имён cookie RUM.

Запрос возвращает полезную нагрузку типа `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/rum/cookieNames` |
| GET | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/rum/cookieNames` |

## Аутентификация

Для выполнения этого запроса необходим токен доступа с областью действия `rumCookieNames.read`.

Чтобы узнать, как получить и использовать токен, см. раздел Токены и аутентификация.

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

* Real User Monitoring
* Cookie-файлы
