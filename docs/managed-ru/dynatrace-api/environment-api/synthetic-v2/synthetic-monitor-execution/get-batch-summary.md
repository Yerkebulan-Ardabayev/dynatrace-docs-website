---
title: Synthetic monitor executions API v2 - GET сводка пакетного выполнения
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-monitor-execution/get-batch-summary
scraped: 2026-05-12T11:57:45.502000
---

# Synthetic monitor executions API v2 - GET сводка пакетного выполнения

# Synthetic monitor executions API v2 - GET сводка пакетного выполнения

* Справочник
* Опубликовано 27 июня 2022 г.

Возвращает сводку пакетного выполнения синтетических мониторов.

Запрос возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/synthetic/executions/batch/{batchId}` |
| GET | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/synthetic/executions/batch/{batchId}` |

## Аутентификация

Для выполнения запроса нужен access-токен с одним из следующих scope:

* `syntheticExecutions.read`
* `ExternalSyntheticIntegration`
* `ReadSyntheticData`

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| batchId | integer | Идентификатор пакета выполнений. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [SyntheticOnDemandBatchStatus](#openapi-definition-SyntheticOnDemandBatchStatus) | Успех |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Входные данные некорректны. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Пакет с заданным ID не существует. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `SyntheticOnDemandBatchStatus`

Содержит информацию о выполнениях по требованию, инициированных в рамках пакета.

| Поле | Тип | Описание |
| --- | --- | --- |
| batchId | string | Идентификатор пакета. |
| batchStatus | string | Статус пакета. Поле может принимать значения: * `FAILED` * `FAILED_TO_EXECUTE` * `NOT_TRIGGERED` * `RUNNING` * `SUCCESS` |
| executedCount | integer | Количество инициированных выполнений с результатом SUCCESS или FAILED. |
| failedCount | integer | Количество инициированных выполнений с результатом FAILED. |
| failedExecutions | [SyntheticOnDemandFailedExecutionStatus[]](#openapi-definition-SyntheticOnDemandFailedExecutionStatus) | - |
| failedToExecute | [SyntheticOnDemandFailedExecutionStatus[]](#openapi-definition-SyntheticOnDemandFailedExecutionStatus) | - |
| failedToExecuteCount | integer | Количество выполнений, которые были инициированы и завершились по тайм-ауту из-за проблемы с синтетическим движком. |
| metadata | object | Карта строка-в-строку свойств метаданных для пакета |
| triggeredCount | integer | Количество инициированных выполнений в рамках пакета. |
| triggeringProblems | [SyntheticOnDemandTriggeringProblemDetails[]](#openapi-definition-SyntheticOnDemandTriggeringProblemDetails) | - |
| triggeringProblemsCount | integer | Количество выполнений, которые не были инициированы из-за каких-либо проблем. |
| userId | string | Имя пользователя, инициировавшего выполнение пакета. |

#### Объект `SyntheticOnDemandFailedExecutionStatus`

Содержит информацию о выполнениях по требованию, которые завершились неудачно или не смогли быть выполнены.

| Поле | Тип | Описание |
| --- | --- | --- |
| errorCode | string | Код ошибки. |
| executionId | string | Идентификатор выполнения. |
| executionStage | string | Стадия выполнения. Поле может принимать значения: * `DATA_RETRIEVED` * `EXECUTED` * `NOT_TRIGGERED` * `TIMED_OUT` * `TRIGGERED` * `WAITING` |
| executionTimestamp | integer | Метка времени завершения выполнения, в UTC миллисекундах. |
| failureMessage | string | Сообщение об ошибке. |
| locationId | string | Идентификатор локации, с которой должен выполняться монитор. |
| monitorId | string | Идентификатор монитора. |

#### Объект `SyntheticOnDemandTriggeringProblemDetails`

Содержит детали проблем, возникших при инициировании выполнений по требованию.

| Поле | Тип | Описание |
| --- | --- | --- |
| cause | string | Причина того, что сущность не была инициирована. |
| details | string | Детали проблемы инициирования. |
| entityId | string | Идентификатор сущности. |
| executionId | string | Идентификатор выполнения. |
| locationId | string | Идентификатор локации. |

#### Объект `ErrorEnvelope`

| Поле | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Поле | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Поле | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Поле может принимать значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"batchId": "22396514015719218",



"batchStatus": "FAILED_TO_EXECUTE",



"executedCount": 1,



"failedCount": 1,



"failedExecutions": [



{



"errorCode": "CONSTRAINT_VIOLATED(3)",



"executionId": "1629891693487",



"executionStage": "EXECUTED",



"executionTimestamp": "1629891695487",



"failureMessage": "Validate text match failed",



"locationId": "SYNTHETIC_LOCATION-9BB04DAEBA71B8CA",



"monitorId": "HTTP_CHECK-6349B98E1CD87352"



}



],



"failedToExecute": [



{



"executionId": "478437504",



"executionStage": "TIMED_OUT",



"locationId": "SYNTHETIC_LOCATION-90380DA8A44C74BD",



"monitorId": "SYNTHETIC_TEST-027011D7D27CC892"



}



],



"failedToExecuteCount": 1,



"metadata": {



"key": "value",



"version": "1.255.20221022"



},



"triggeredCount": 3,



"triggeringProblems": [



{



"cause": "Location not found",



"entityId": "HTTP_CHECK-6349B98E1CD87352",



"locationId": "SYNTHETIC_LOCAT-9BB04DAEBA71B8CA"



},



{



"cause": "Incorrect application identifier format",



"entityId": "APPLICATION-WRONG"



}



],



"triggeringProblemsCount": 2,



"userId": "admin"



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

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Узнайте о Synthetic Monitoring и о том, как создать браузерный монитор одного URL, браузерный clickpath или HTTP-монитор.")