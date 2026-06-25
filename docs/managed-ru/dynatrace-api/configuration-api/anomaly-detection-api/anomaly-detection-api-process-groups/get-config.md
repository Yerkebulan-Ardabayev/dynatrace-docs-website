---
title: Process groups anomaly detection API - GET configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-process-groups/get-config
scraped: 2026-05-12T11:19:14.058424
---

# Process groups anomaly detection API - GET configuration

# Process groups anomaly detection API - GET configuration

* Reference
* Published Jun 03, 2020

Возвращает конфигурацию обнаружения аномалий для указанной process group.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/processGroups/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/processGroups/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID сущности Dynatrace нужной process group. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [AnomalyDetectionPG](#openapi-definition-AnomalyDetectionPG) | Успех |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Process group не существует |

### Объекты тела ответа

#### Объект `AnomalyDetectionPG`

Конфигурация обнаружения аномалий для process group.

| Элемент | Тип | Описание |
| --- | --- | --- |
| availabilityMonitoring | [AvailabilityMonitoringPG](#openapi-definition-AvailabilityMonitoringPG) | Конфигурация мониторинга доступности для process group. |

#### Объект `AvailabilityMonitoringPG`

Конфигурация мониторинга доступности для process group.

| Элемент | Тип | Описание |
| --- | --- | --- |
| method | string | Как отслеживать доступность process group:  * `PROCESS_IMPACT`: оповещать, если любой процесс группы становится недоступен. * `MINIMUM_THRESHOLD`: оповещать, если число активных процессов в группе опускается ниже заданного порога. * `OFF`: мониторинг доступности отключён. Возможные значения: * `MINIMUM_THRESHOLD` * `OFF` * `PROCESS_IMPACT` |
| minimumThreshold | integer | Оповещать, если число активных процессов в группе меньше этого значения. |

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



"availabilityMonitoring": {



"method": "MINIMUM_THRESHOLD",



"minimumThreshold": 5



}



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

В этом примере запрос возвращает конфигурацию обнаружения аномалий для process group с ID **PROCESS\_GROUP-52B42D0616D556F5**.

API-токен передаётся в заголовке **Authorization**.

Конфигурация имеет следующие настройки:

![GET anomaly detection config - process group](https://dt-cdn.net/images/get-config-641-4141d73410.png)

GET anomaly detection config - process group

#### Curl

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/processGroups/PROCESS_GROUP-52B42D0616D556F5' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/processGroups/PROCESS_GROUP-52B42D0616D556F5
```

#### Тело ответа

```
{



"availabilityMonitoring": {



"method": "MINIMUM_THRESHOLD",



"minimumThreshold": 10



}



}
```

#### Код ответа

200

## Связанные темы

* [Davis® AI](/managed/dynatrace-intelligence "Познакомьтесь с возможностями Davis AI.")
* [Process groups](/managed/observe/infrastructure-observability/process-groups "Анализ process groups и настройка их именования, обнаружения и мониторинга.")