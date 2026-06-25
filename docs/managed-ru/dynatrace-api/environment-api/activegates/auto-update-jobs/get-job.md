---
title: ActiveGate API - GET an auto-update job
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/activegates/auto-update-jobs/get-job
scraped: 2026-05-12T11:59:54.422361
---

# ActiveGate API - GET an auto-update job

# ActiveGate API - GET an auto-update job

* Reference
* Published Jul 02, 2020

Возвращает параметры указанной задачи авто-обновления ActiveGate.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/activeGates/{agId}/updateJobs/{jobId}` |
| GET | Environment and Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/activeGates/{agId}/updateJobs/{jobId}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `activeGates.read`.

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
| **200** | [UpdateJob](#openapi-definition-UpdateJob) | Успех |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Не найдено. Подробности в теле ответа. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка сервера. |

### Объекты тела ответа

#### Объект `UpdateJob`

Конфигурация задачи обновления ActiveGate.

| Элемент | Тип | Описание |
| --- | --- | --- |
| agType | string | Тип ActiveGate. Элемент может принимать значения * `CLUSTER` * `ENVIRONMENT` * `ENVIRONMENT_MULTI` |
| cancelable | boolean | Задачу можно (`true`) или нельзя (`false`) отменить в данный момент. |
| duration | integer | Длительность обновления в миллисекундах. |
| environments | string[] | Список окружений (заданных по ID), к которым может подключаться ActiveGate. |
| error | string | Информация об ошибке обновления. |
| jobId | string | ID задачи обновления. |
| jobState | string | Статус задачи обновления. Элемент может принимать значения * `FAILED` * `IN_PROGRESS` * `PENDING` * `ROLLBACK` * `SCHEDULED` * `SKIPPED` * `SUCCEED` |
| startVersion | string | Исходная версия ActiveGate. |
| targetVersion | string | Целевая версия обновления.  Версия указывается в формате `<major>.<minor>.<revision>.<timestamp>`.  Чтобы обновиться до последней доступной версии, используйте значение `latest`. |
| timestamp | integer | Временная метка завершения задачи обновления.  Значение `null` означает, что задача всё ещё выполняется. |
| updateMethod | string | Метод обновления ActiveGate или его компонента. Элемент может принимать значения * `AUTOMATIC` * `MANUAL_INSTALLATION` * `ON_DEMAND` |
| updateType | string | Компонент, который нужно обновить. Элемент может принимать значения * `ACTIVE_GATE` * `REMOTE_PLUGIN_AGENT` * `SYNTHETIC` * `Z_REMOTE` |

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



"agType": "ENVIRONMENT",



"cancelable": false,



"duration": 3608000,



"environments": [



"string"



],



"error": "string",



"jobId": "-3524498778810258605",



"jobState": "SUCCEED",



"startVersion": "1.185.0.20200201-120000",



"targetVersion": "1.190.0.20200301-130000",



"timestamp": 1582031917814,



"updateMethod": "AUTOMATIC",



"updateType": "ACTIVE_GATE"



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

В этом примере запрос выводит параметры задачи авто-обновления с ID **-7537034309286328684** на ActiveGate с ID **2131628184**.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/activeGates/2131628184/updateJobs/-7537034309286328684' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/activeGates/2131628184/updateJobs/-7537034309286328684
```

#### Response body

```
{



"jobId": "-7537034309286328684",



"jobState": "SUCCEED",



"updateMethod": "AUTOMATIC",



"updateType": "SYNTHETIC",



"cancelable": false,



"startVersion": "1.198.0.20200629-183024",



"targetVersion": "1.198.0.20200630-114457",



"timestamp": 1593518788274,



"agType": "ENVIRONMENT",



"environments": [



"mySampleEnv"



],



"error": null,



"duration": 596047



}
```

#### Response code

200

## Связанные темы

* [Dynatrace ActiveGate](/managed/ingest-from/dynatrace-activegate "Изучите основные концепции, связанные с ActiveGate.")