---
title: Process groups anomaly detection API - PUT configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-process-groups/put-config
scraped: 2026-05-12T11:19:11.287141
---

# Process groups anomaly detection API - PUT configuration

# Process groups anomaly detection API - PUT configuration

* Reference
* Published Jun 03, 2020

Обновляет конфигурацию обнаружения аномалий для указанной process group.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/processGroups/{id}` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/processGroups/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID сущности Dynatrace нужной process group. | path | Required |
| body | [AnomalyDetectionPG](#openapi-definition-AnomalyDetectionPG) | JSON-тело запроса с параметрами обнаружения аномалий для process group. | body | Optional |

### Объекты тела запроса

#### Объект `AnomalyDetectionPG`

Конфигурация обнаружения аномалий для process group.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| availabilityMonitoring | [AvailabilityMonitoringPG](#openapi-definition-AvailabilityMonitoringPG) | Конфигурация мониторинга доступности для process group. | Optional |

#### Объект `AvailabilityMonitoringPG`

Конфигурация мониторинга доступности для process group.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| method | string | Как отслеживать доступность process group:  * `PROCESS_IMPACT`: оповещать, если любой процесс группы становится недоступен. * `MINIMUM_THRESHOLD`: оповещать, если число активных процессов в группе опускается ниже заданного порога. * `OFF`: мониторинг доступности отключён. Возможные значения: * `MINIMUM_THRESHOLD` * `OFF` * `PROCESS_IMPACT` | Required |
| minimumThreshold | integer | Оповещать, если число активных процессов в группе меньше этого значения. | Optional |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

```
{



"availabilityMonitoring": {



"method": "MINIMUM_THRESHOLD",



"minimumThreshold": 5



}



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Конфигурация обновлена. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |

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

## Validate payload

Рекомендуется валидировать payload перед отправкой реального запроса. Код ответа **204** означает валидный payload.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/processGroups/{id}/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/processGroups/{id}/validator` |

### Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Validated. Переданная конфигурация валидна. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |

#### Объекты тела ответа

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

#### JSON-модели тела ответа

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

В этом примере запрос обновляет конфигурацию обнаружения аномалий для process group с ID **PROCESS\_GROUP-52B42D0616D556F5** из примера [GET request](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-process-groups/get-config#example "Просмотр конфигурации обнаружения аномалий для process group через Dynatrace API."). Он меняет метод обнаружения на **PROCESS\_IMPACT**.

API-токен передаётся в заголовке **Authorization**.

Вы можете скачать или скопировать пример тела запроса, чтобы попробовать его самостоятельно. Сначала обязательно создайте резервную копию текущей конфигурации вызовом **GET process group anomaly detection configuration**.

#### Curl

```
curl -L -X PUT 'https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/processGroups/PROCESS_GROUP-52B42D0616D556F5' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



--data-raw '{



"availabilityMonitoring": {



"method": "PROCESS_IMPACT"



}



}'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/processGroups/PROCESS_GROUP-52B42D0616D556F5
```

#### Тело запроса

```
{



"availabilityMonitoring": {



"method": "PROCESS_IMPACT"



}



}
```

#### Код ответа

204

#### Результат

![PUT anomaly detection config - process group](https://dt-cdn.net/images/put-config-619-6a113b1650.png)

PUT anomaly detection config - process group

## Связанные темы

* [Davis® AI](/managed/dynatrace-intelligence "Познакомьтесь с возможностями Davis AI.")
* [Process groups](/managed/observe/infrastructure-observability/process-groups "Анализ process groups и настройка их именования, обнаружения и мониторинга.")