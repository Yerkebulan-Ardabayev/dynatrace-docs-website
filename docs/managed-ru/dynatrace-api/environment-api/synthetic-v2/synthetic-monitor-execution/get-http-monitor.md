---
title: Synthetic monitor executions API v2 - GET HTTP-монитор
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-monitor-execution/get-http-monitor
scraped: 2026-05-12T11:57:56.285583
---

# Synthetic monitor executions API v2 - GET HTTP-монитор

# Synthetic monitor executions API v2 - GET HTTP-монитор

* Справочник
* Опубликовано 20 апреля 2021 г.

Возвращает результат самого свежего выполнения указанного HTTP-монитора.

Запрос возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/synthetic/execution/{monitorId}/{resultType}` |
| GET | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/synthetic/execution/{monitorId}/{resultType}` |

## Аутентификация

Для выполнения запроса нужен access-токен с одним из следующих scope:

* `DataExport`
* `ExternalSyntheticIntegration`
* `ReadSyntheticData`

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| monitorId | string | Идентификатор HTTP-монитора, для которого возвращается результат последнего выполнения. | path | Обязательный |
| resultType | string | Определяет тип результата последнего выполнения HTTP-монитора. Поле может принимать значения: * `SUCCESS` * `FAILED` | path | Обязательный |
| locationId | string | Фильтрует результаты, оставляя те, что выполнены указанной синтетической локацией. Укажите ID локации. | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [MonitorExecutionResults](#openapi-definition-MonitorExecutionResults) | Успех. Ответ содержит подробные данные. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `MonitorExecutionResults`

Результаты выполнения всех запросов HTTP-монитора.

| Поле | Тип | Описание |
| --- | --- | --- |
| locationsExecutionResults | [LocationExecutionResults[]](#openapi-definition-LocationExecutionResults) | Список с результатами запросов, выполненных на назначенных локациях. |
| monitorId | string | ID монитора. |

#### Объект `LocationExecutionResults`

Результаты выполнения запросов HTTP-монитора на заданной локации

| Поле | Тип | Описание |
| --- | --- | --- |
| executionId | string | ID выполнения. |
| locationId | string | ID локации. |
| requestResults | [MonitorRequestExecutionResult[]](#openapi-definition-MonitorRequestExecutionResult) | Список результатов запросов монитора, выполненных на этой локации. |

#### Объект `MonitorRequestExecutionResult`

Результат выполнения запроса HTTP-монитора.

#### Объект `ExecutionStep`

Содержит подробную информацию о выполнении шага монитора.

| Поле | Тип | Описание |
| --- | --- | --- |
| monitorType | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из объектов:  * `BROWSER` -> BMAction * `HTTP` -> MonitorRequestExecutionResult Поле может принимать значения: * `BROWSER` * `HTTP` |

#### Объект `CustomLogLine`

Строка лога кастомного скрипта

| Поле | Тип | Описание |
| --- | --- | --- |
| logLevel | string | Уровень логирования сообщения |
| message | string | Сообщение |
| timestamp | integer | Метка времени этого сообщения лога |

#### Объект `MonitorRequestHeader`

Заголовок Http-запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| name | string | Имя заголовка. |
| value | string | Значение заголовка. |

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



"locationsExecutionResults": [



{



"executionId": "6136172183050046113",



"locationId": "7804738439930364165",



"requestResults": [



{



"engineId": 338502283,



"errorCode": 0,



"failureMessage": "",



"hostNameResolutionTime": 26,



"method": "GET",



"peerCertificateDetails": "[Certificate details]",



"peerCertificateExpiryDate": 1647302399000,



"publicLocation": false,



"redirectionTime": 70,



"redirectsCount": 1,



"requestBody": "",



"requestHeaders": [



{



"name": "User-Agent",



"value": "DynatraceSynthetic/1.215.1"



},



{



"name": "X-Dynatrace-Visit",



"value": "6136172183050046113"



},



{



"name": "X-Dynatrace-Test",



"value": "HTTP_CHECK-12B428F6D37A9197"



}



],



"requestId": "HTTP_CHECK_STEP-53071FC3C4F72E28",



"requestName": "Request name",



"resolvedIps": [



"80.252.0.145"



],



"responseBody": "<html><head>Title</head><body>Main Page</body></html>",



"responseBodySizeLimitExceeded": false,



"responseHeaders": [



{



"name": "Date",



"value": "Mon, 15 Mar 2021 11:09:30 GMT"



},



{



"name": "Content-Language",



"value": "en"



}



],



"responseMessage": "OK",



"responseSize": 1112,



"responseStatusCode": 200,



"sequenceNumber": 1,



"startTimestamp": 1615806570884,



"tcpConnectTime": 15,



"timeToFirstByte": 96,



"tlsHandshakeTime": 8,



"totalTime": 238,



"url": "https://www.examplePage.com",



"waitingTime": 47



}



]



}



],



"monitorId": "HTTP_CHECK-12B428F6D37A9197"



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