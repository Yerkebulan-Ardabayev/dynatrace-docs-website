---
title: ActiveGate API - DELETE an auto-update job
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/activegates/auto-update-jobs/delete-job
scraped: 2026-05-12T12:00:00.646530
---

# ActiveGate API - DELETE an auto-update job

# ActiveGate API - DELETE an auto-update job

* Reference
* Published Jul 02, 2020

Удаляет указанную задачу авто-обновления ActiveGate.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/activeGates/{agId}/updateJobs/{jobId}` |
| DELETE | Environment and Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/activeGates/{agId}/updateJobs/{jobId}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `activeGates.write`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| agId | string | ID требуемого ActiveGate. | path | Обязательный |
| jobId | string | Уникальный идентификатор задачи обновления ActiveGate. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Задача обновления удалена. У ответа нет тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Входные данные некорректны. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Не найдено. Подробности в теле ответа. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка сервера. |

### Объекты тела ответа

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

В этом примере запрос удаляет задачу обновления с ID **-7240069678607892845** на ActiveGate с ID **1812885988**. Код ответа **204** означает, что удаление прошло успешно.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -L -X DELETE 'https://mySampleEnv.live.dynatrace.com/api/v2/activeGates/1812885988/updateJobs/-7240069678607892845' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/activeGates/1812885988/updateJobs/-7240069678607892845
```

#### Response code

204

## Связанные темы

* [Dynatrace ActiveGate](/managed/ingest-from/dynatrace-activegate "Изучите основные концепции, связанные с ActiveGate.")