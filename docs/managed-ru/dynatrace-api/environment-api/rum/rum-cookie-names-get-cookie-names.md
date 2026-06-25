---
title: RUM cookie names API - GET cookie names
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/rum/rum-cookie-names-get-cookie-names
scraped: 2026-05-12T11:37:15.677727
---

# RUM cookie names API - GET cookie names

# RUM cookie names API - GET cookie names

* Reference
* Published Jun 25, 2024

Выводит список имён cookie RUM.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/rum/cookieNames` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/rum/cookieNames` |

## Аутентификация

Для выполнения запроса необходим access token со scope `rumCookieNames.read`.

О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Запрос не предоставляет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [CookieNames](#openapi-definition-CookieNames) | Успех. Ответ содержит все имена cookie RUM |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `CookieNames`

Список всех имён cookie.

| Элемент | Тип | Описание |
| --- | --- | --- |
| domainValidationCookieName | string | Имя cookie проверки домена. |
| latencyCookieName | string | Имя cookie задержки. |
| pageContextCookieName | string | Имя cookie контекста страницы. |
| sessionCookieName | string | Имя cookie сессии. |
| sessionReplayCookieName | string | Имя cookie Session Replay. |
| sessionReplayViewIdCookieName | string | Имя cookie ID представления Session Replay. |
| sessionTimeoutCookieName | string | Имя cookie тайм-аута сессии. |
| sourceActionCookieName | string | Имя cookie исходного действия. |
| visitorCookieName | string | Имя cookie посетителя. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния |
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



"domainValidationCookieName": "dtValidationCookie",



"latencyCookieName": "dtLatC",



"pageContextCookieName": "dtPC",



"sessionCookieName": "dtCookie",



"sessionReplayCookieName": "dtSR",



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

* [Мониторинг реальных пользователей](/managed/observe/digital-experience/rum-concepts/rum-overview "Узнайте о Real User Monitoring, ключевых метриках производительности, мониторинге мобильных приложений и многом другом.")
* [Cookie и клиентское хранилище для RUM и Session Replay](/managed/manage/data-privacy-and-security/data-privacy/rum-cookies-and-web-storage "Узнайте, как Dynatrace RUM и Session Replay используют cookie, веб-хранилище и IndexedDB.")