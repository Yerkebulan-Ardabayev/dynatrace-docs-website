---
title: Vulnerabilities API - POST unmute vulnerabilities
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/application-security/vulnerabilities/post-problems-unmute
scraped: 2026-03-04T21:30:54.459729
---

# Vulnerabilities API - POST включение уязвимостей


Включает несколько уязвимостей. Включённые уязвимости отображаются в списке уязвимостей в Dynatrace.

Запрос принимает полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/securityProblems/unmute` |
| POST | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/securityProblems/unmute` |

## Аутентификация

Для выполнения этого запроса необходим токен доступа с областью `securityProblems.write`.

Чтобы узнать, как получить и использовать его, см. [Токены и аутентификация](../../../../discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication.md).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| body | [SecurityProblemsBulkUnmute](#openapi-definition-SecurityProblemsBulkUnmute) | JSON-тело запроса. Содержит информацию о включении. | body | Необязательный |

### Объекты тела запроса

#### Объект `SecurityProblemsBulkUnmute`

Информация о включении нескольких проблем безопасности.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| comment | string | Комментарий о причине включения. | Необязательный |
| reason | string | Причина включения проблем безопасности. Элемент может содержать следующие значения: * `AFFECTED` | Обязательный |
| securityProblemIds | string[] | Идентификаторы проблем безопасности, которые необходимо включить. | Обязательный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Она должна быть адаптирована для использования в реальном запросе.

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
| **200** | [SecurityProblemsBulkUnmuteResponse](#openapi-definition-SecurityProblemsBulkUnmuteResponse) | Успешно. Проблемы безопасности были включены. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `SecurityProblemsBulkUnmuteResponse`

Ответ на включение нескольких проблем безопасности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| summary | [SecurityProblemBulkMutingSummary[]](#openapi-definition-SecurityProblemBulkMutingSummary) | Сводка о том, какие проблемы безопасности были включены и какие уже были включены ранее. |

#### Объект `SecurityProblemBulkMutingSummary`

Сводка об отключении/включении проблемы безопасности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| muteStateChangeTriggered | boolean | Было ли изменение состояния отключения для данной проблемы безопасности инициировано этим запросом. |
| reason | string | Содержит причину, если запрошенная операция не была выполнена. Элемент может содержать следующие значения: * `ALREADY_MUTED` * `ALREADY_UNMUTED` |
| securityProblemId | string | Идентификатор проблемы безопасности, которая была отключена/включена. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | Код состояния HTTP |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | - Элемент может содержать следующие значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
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

Включение двух уязвимостей, `2919200225913269102` и `4537041069803077238`.

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

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/unmute
```

#### Тело запроса

```
{


"comment": "Example unmute bulk",


"reason": "AFFECTED",


"securityProblemIds": [


"2919200225913269102", "4537041069803077238"


]


}
```

#### Тело ответа

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

Здесь `muteStateChangeTriggered` указывает на успешность операции.

Обратите внимание, что включение уязвимости может занять до одной минуты.

## Связанные темы

* [Application Security](../../../../secure/application-security.md "Доступ к функциям Dynatrace Application Security.")
* [Davis Security Advisor API](../davis-security-advice.md "Просмотр рекомендаций Davis Security Advisor через Dynatrace API.")