---
title: Vulnerabilities API - POST unmute vulnerabilities
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/application-security/vulnerabilities/post-problems-unmute
scraped: 2026-05-12T11:59:05.094212
---

# Vulnerabilities API - POST unmute vulnerabilities

# Vulnerabilities API - POST unmute vulnerabilities

* Reference
* Updated on Sep 25, 2024

Снимает заглушение нескольких уязвимостей. Уязвимости со снятым заглушением отображаются в списке уязвимостей в Dynatrace.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/securityProblems/unmute` |
| POST | Environment and Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/securityProblems/unmute` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `securityProblems.write`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| body | [SecurityProblemsBulkUnmute](#openapi-definition-SecurityProblemsBulkUnmute) | JSON-тело запроса. Содержит информацию о снятии заглушения. | body | Опциональный |

### Объекты тела запроса

#### Объект `SecurityProblemsBulkUnmute`

Информация о снятии заглушения нескольких security problems.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| comment | string | Комментарий о причине снятия заглушения. | Опциональный |
| reason | string | Причина снятия заглушения security problems. Элемент может принимать значения * `AFFECTED` | Обязательный |
| securityProblemIds | string[] | ID security problems для снятия заглушения. | Обязательный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать для использования в реальном запросе.

```
{



"comment": "string",



"reason": "AFFECTED",



"securityProblemIds": [



"string"



]



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [SecurityProblemsBulkUnmuteResponse](#openapi-definition-SecurityProblemsBulkUnmuteResponse) | Успех. Заглушение security problem(s) снято. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка сервера. |

### Объекты тела ответа

#### Объект `SecurityProblemsBulkUnmuteResponse`

Ответ снятия заглушения нескольких security problems.

| Элемент | Тип | Описание |
| --- | --- | --- |
| summary | [SecurityProblemBulkMutingSummary[]](#openapi-definition-SecurityProblemBulkMutingSummary) | Сводка о том, для каких security problems было снято заглушение и для каких заглушение уже было снято ранее. |

#### Объект `SecurityProblemBulkMutingSummary`

Сводка (снятия) заглушения security problem.

| Элемент | Тип | Описание |
| --- | --- | --- |
| muteStateChangeTriggered | boolean | Было ли изменение состояния заглушения для данной security problem инициировано этим запросом. |
| reason | string | Содержит причину, если запрошенная операция не была выполнена. Элемент может принимать значения * `ALREADY_MUTED` * `ALREADY_UNMUTED` |
| securityProblemId | string | ID security problem, для которой было применено (снятие) заглушение. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния. |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений. |
| message | string | Сообщение об ошибке. |

#### Объект `ConstraintViolation`

Список нарушений ограничений.

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"summary": [



{



"muteStateChangeTriggered": true,



"reason": "ALREADY_MUTED",



"securityProblemId": "string"



}



]



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

## Пример

Снять заглушение двух уязвимостей, `2919200225913269102` и `4537041069803077238`.

#### Curl

```
curl -X 'POST' 'https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/unmute' \



-H 'accept: application/json; charset=utf-8' \



-H 'Authorization: Api-Token [your_token]' \



-H 'Content-Type: application/json; charset=utf-8' \



-d '{



"comment": "Example unmute bulk",



"reason": "AFFECTED",



"securityProblemIds": [



"2919200225913269102", "4537041069803077238"



]



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/unmute
```

#### Request body

```
{



"comment": "Example unmute bulk",



"reason": "AFFECTED",



"securityProblemIds": [



"2919200225913269102", "4537041069803077238"



]



}
```

#### Response body

```
{



"summary": [



{



"securityProblemId": "2919200225913269102",



"muteStateChangeTriggered": true



},



{



"securityProblemId": "4537041069803077238",



"muteStateChangeTriggered": true



}



]



}
```

Здесь `muteStateChangeTriggered` означает успешность операции.

Обратите внимание, что снятие заглушения уязвимости может занять до одной минуты.

## Связанные темы

* [Application Security](/managed/secure/application-security "Доступ к функциям Dynatrace Application Security.")
* [Davis Security Advisor API](/managed/dynatrace-api/environment-api/application-security/davis-security-advice "Просмотрите рекомендации Davis Security Advisor через Dynatrace API.")