---
title: Synthetic monitor executions API v2 - GET полная информация о выполнении
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-monitor-execution/get-execution-full
scraped: 2026-05-12T11:57:47.690127
---

# Synthetic monitor executions API v2 - GET полная информация о выполнении

# Synthetic monitor executions API v2 - GET полная информация о выполнении

* Справочник
* Опубликовано 27 июня 2022 г.

Возвращает полные результаты выполнения синтетического монитора по требованию.

Запрос возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/synthetic/executions/{executionId}/fullReport` |
| GET | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/synthetic/executions/{executionId}/fullReport` |

## Аутентификация

Для выполнения запроса нужен access-токен с одним из следующих scope:

* `syntheticExecutions.read`
* `ExternalSyntheticIntegration`
* `ReadSyntheticData`

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| executionId | integer | Идентификатор выполнения по требованию. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [SyntheticOnDemandExecution](#openapi-definition-SyntheticOnDemandExecution) | Успех. Ответ содержит подробную информацию о выполнении по требованию. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Входные данные некорректны. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Выполнение с заданным ID не существует. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `SyntheticOnDemandExecution`

Описывает статус выполнения по требованию.

| Поле | Тип | Описание |
| --- | --- | --- |
| batchId | string | Идентификатор пакета. |
| customizedScript | [ObjectNode](#openapi-definition-ObjectNode) | Кастомизированные свойства скрипта для этого пакетного выполнения по требованию. |
| dataDeliveryTimestamp | integer | Метка времени, когда весь набор данных был собран на сервере, в UTC миллисекундах. |
| executionId | string | Идентификатор выполнения. |
| executionStage | string | Стадия выполнения. Поле может принимать значения: * `DATA_RETRIEVED` * `EXECUTED` * `NOT_TRIGGERED` * `TIMED_OUT` * `TRIGGERED` * `WAITING` |
| executionTimestamp | integer | Метка времени завершения выполнения, в UTC миллисекундах. |
| fullResults | [ExecutionFullResults](#openapi-definition-ExecutionFullResults) | Содержит расширенные детали выполнения монитора. |
| locationId | string | Идентификатор локации, с которой должен выполняться монитор. |
| metadata | object | Карта метаданных для пакета выполнения. |
| monitorId | string | Идентификатор монитора. |
| nextExecutionId | string | ID следующего выполнения для последовательного режима. |
| processingMode | string | Режим обработки выполнения. Поле может принимать значения: * `DISABLE_PROBLEM_DETECTION` * `EXECUTIONS_DETAILS_ONLY` * `NONE` * `STANDARD` * `UNKNOWN` |
| schedulingTimestamp | integer | Метка времени планирования, в UTC миллисекундах. |
| simpleResults | [ExecutionSimpleResults](#openapi-definition-ExecutionSimpleResults) | Содержит базовые результаты выполнения монитора по требованию. |
| source | string | Источник инициирующего запроса. Поле может принимать значения: * `API` * `UI` |
| userId | string | Имя пользователя, инициировавшего выполнение по требованию. |

#### Объект `ObjectNode`

Кастомизированные свойства скрипта для этого пакетного выполнения по требованию.

#### Объект `ExecutionFullResults`

Содержит расширенные детали выполнения монитора.

| Поле | Тип | Описание |
| --- | --- | --- |
| errorCode | string | Код ошибки. |
| executionStepCount | integer | Количество выполненных шагов. |
| executionSteps | [ExecutionStep[]](#openapi-definition-ExecutionStep) | Детали выполнения шагов монитора. |
| failedStepName | string | Имя неудавшегося шага. |
| failedStepSequenceId | integer | ID последовательности неудавшегося шага. |
| failureMessage | string | Сообщение об ошибке. |
| status | string | Статус выполнения. |

#### Объект `ExecutionStep`

Содержит подробную информацию о выполнении шага монитора.

| Поле | Тип | Описание |
| --- | --- | --- |
| monitorType | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из объектов:  * `BROWSER` -> BMAction * `HTTP` -> MonitorRequestExecutionResult Поле может принимать значения: * `BROWSER` * `HTTP` |

#### Объект `ExecutionSimpleResults`

Содержит базовые результаты выполнения монитора по требованию.

| Поле | Тип | Описание |
| --- | --- | --- |
| chromeError | boolean | Сообщает, является ли это ошибкой Chrome. |
| engineId | integer | ID синтетического движка, на котором выполнялся монитор. |
| errorCode | string | Код ошибки. |
| executedSteps | integer | Количество шагов, выполненных синтетическим движком |
| failureMessage | string | Сообщение об ошибке. |
| hostNameResolutionTime | integer | Время разрешения имени хоста в миллисекундах. |
| httperror | boolean | Сообщает, является ли это HTTP-ошибкой. |
| ~~peerCertificateExpiryDate~~ | integer | УСТАРЕЛО  Дата истечения первого SSL-сертификата из цепочки сертификатов. |
| publicLocation | boolean | Флаг сообщает, был ли запрос выполнен на публичной локации. |
| redirectionTime | integer | Общее число миллисекунд, затраченных на обработку всех запросов перенаправления, измеренное в миллисекундах. |
| redirectsCount | integer | Количество перенаправлений. |
| responseBodySizeLimitExceeded | boolean | Флаг, указывающий, что лимит размера payload ответа в 10 МБ был превышен. |
| responseSize | integer | Размер ответа на запрос в байтах. |
| responseStatusCode | integer | Код состояния ответа. |
| startTimestamp | integer | Метка времени начала. |
| status | string | Статус выполнения. |
| tcpConnectTime | integer | Время TCP-соединения в миллисекундах. |
| timeToFirstByte | integer | Время до первого байта в миллисекундах. |
| tlsHandshakeTime | integer | Время TLS-рукопожатия в миллисекундах. |
| totalTime | integer | Общее время в миллисекундах. |

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



"customizedScript": {



"requests": [



{



"sequenceId": "1",



"url": "https://www.somepage.org",



"validation": {



"rules": [



{



"passIfFound": "true",



"type": "httpStatusesList",



"value": "=201"



}



]



}



}



]



},



"dataDeliveryTimestamp": "1629891701171",



"executionId": "7002396514015719218",



"executionStage": "DATA_RETRIEVED",



"executionTimestamp": "1629891695487",



"locationId": "SYNTHETIC_LOCATION-9BB04DAEBA71B8CA",



"metadata": {



"key": "value",



"version": "1.255.20221022"



},



"monitorId": "HTTP_CHECK-6349B98E1CD87352",



"processingMode": "STANDARD",



"schedulingTime": "1629891686877",



"simpleResults": [



{



"engineId": "1993198092",



"executedSteps": "1",



"healthStatus": "HEALTHY",



"hostNameResolutionTime": "50",



"publicLocation": "false",



"redirectionTime": "576",



"responseBodySizeLimitExceeded": "false",



"responseSize": "1530652",



"responseStatusCode": "200",



"startTimestamp": "1629891693487",



"tcpConnectTime": "127",



"tlsHandshakeTime": "167",



"totalTime": "955"



}



],



"source": "API",



"userId": "someUserIdentifier"



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