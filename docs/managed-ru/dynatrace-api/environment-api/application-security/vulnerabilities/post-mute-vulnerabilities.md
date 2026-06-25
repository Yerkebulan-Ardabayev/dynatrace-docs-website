---
title: Vulnerabilities API - POST mute vulnerabilities
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/application-security/vulnerabilities/post-mute-vulnerabilities
scraped: 2026-05-12T11:58:54.210061
---

# Vulnerabilities API - POST mute vulnerabilities

# Vulnerabilities API - POST mute vulnerabilities

* Reference
* Updated on Sep 25, 2024

Заглушает несколько уязвимостей. Заглушенные уязвимости скрыты из списка уязвимостей в Dynatrace.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/securityProblems/mute` |
| POST | Environment and Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/securityProblems/mute` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `securityProblems.write`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| body | [SecurityProblemsBulkMute](#openapi-definition-SecurityProblemsBulkMute) | JSON-тело запроса. Содержит информацию о заглушении. | body | Опциональный |

### Объекты тела запроса

#### Объект `SecurityProblemsBulkMute`

Информация о заглушении нескольких security problems.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| comment | string | Комментарий о причине заглушения. | Опциональный |
| reason | string | Причина заглушения security problems. Элемент может принимать значения * `CONFIGURATION_NOT_AFFECTED` * `FALSE_POSITIVE` * `IGNORE` * `OTHER` * `VULNERABLE_CODE_NOT_IN_USE` | Обязательный |
| securityProblemIds | string[] | ID security problems для заглушения. | Обязательный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать для использования в реальном запросе.

```
{



"comment": "string",



"reason": "CONFIGURATION_NOT_AFFECTED",



"securityProblemIds": [



"string"



]



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [SecurityProblemsBulkMuteResponse](#openapi-definition-SecurityProblemsBulkMuteResponse) | Успех. Security problem(s) заглушены. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка сервера. |

### Объекты тела ответа

#### Объект `SecurityProblemsBulkMuteResponse`

Ответ заглушения нескольких security problems.

| Элемент | Тип | Описание |
| --- | --- | --- |
| summary | [SecurityProblemBulkMutingSummary[]](#openapi-definition-SecurityProblemBulkMutingSummary) | Сводка о том, какие security problems были заглушены и какие уже были заглушены ранее. |

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

Заглушить две уязвимости, `2919200225913269102` и `4537041069803077238`, поскольку конфигурация не затронута.

#### Curl

```
curl -X 'POST' 'https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/mute' \



-H 'accept: application/json; charset=utf-8' \



-H 'Authorization: Api-Token [your_token]' \



-H 'Content-Type: application/json; charset=utf-8' \



-d '{



"comment": "Example mute batch",



"reason": "CONFIGURATION_NOT_AFFECTED",



"securityProblemIds": [



"2919200225913269102", "4537041069803077238"



]



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/mute
```

#### Request body

```
{



"comment": "Example mute batch",



"reason": "CONFIGURATION_NOT_AFFECTED",



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

## Связанные темы

* [Application Security](/managed/secure/application-security "Доступ к функциям Dynatrace Application Security.")
* [Davis Security Advisor API](/managed/dynatrace-api/environment-api/application-security/davis-security-advice "Просмотрите рекомендации Davis Security Advisor через Dynatrace API.")