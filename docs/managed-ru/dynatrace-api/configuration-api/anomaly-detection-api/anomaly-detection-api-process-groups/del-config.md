---
title: Process groups anomaly detection API - DELETE configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-process-groups/del-config
scraped: 2026-05-12T11:19:12.612818
---

# Process groups anomaly detection API - DELETE configuration

# Process groups anomaly detection API - DELETE configuration

* Reference
* Published Jun 03, 2020

Удаляет конфигурацию обнаружения аномалий для указанной process group.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/processGroups/{id}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/processGroups/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID сущности Dynatrace нужной process group. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Конфигурация обновлена. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Process group не существует |

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

## Пример

В этом примере запрос удаляет конфигурацию обнаружения аномалий для process group с ID **PROCESS\_GROUP-52B42D0616D556F5** из примера [GET request](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-process-groups/get-config#example "Просмотр конфигурации обнаружения аномалий для process group через Dynatrace API.").

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -L -X DELETE 'https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/processGroups/PROCESS_GROUP-52B42D0616D556F5' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/processGroups/PROCESS_GROUP-52B42D0616D556F5
```

#### Код ответа

204

#### Результат

![DEL anomaly detection config - process group](https://dt-cdn.net/images/del-config-603-da5d855f0e.png)

DEL anomaly detection config - process group

## Связанные темы

* [Davis® AI](/managed/dynatrace-intelligence "Познакомьтесь с возможностями Davis AI.")
* [Process groups](/managed/observe/infrastructure-observability/process-groups "Анализ process groups и настройка их именования, обнаружения и мониторинга.")