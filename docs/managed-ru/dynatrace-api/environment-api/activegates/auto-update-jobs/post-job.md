---
title: ActiveGate API - POST an auto-update job
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/activegates/auto-update-jobs/post-job
scraped: 2026-05-12T12:00:02.830137
---

# ActiveGate API - POST an auto-update job

# ActiveGate API - POST an auto-update job

* Reference
* Published Jul 02, 2020

Создаёт новую задачу авто-обновления на указанном ActiveGate.

Задача обновляет ActiveGate до указанной версии. Список доступных версий можно получить через вызов [GET available versions of ActiveGate](/managed/dynatrace-api/environment-api/deployment/activegate/get-activegate-versions "Список доступных версий ActiveGate через Dynatrace API.").

Запрос принимает и возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/activeGates/{agId}/updateJobs` |
| POST | Environment and Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/activeGates/{agId}/updateJobs` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `activeGates.write`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| agId | string | ID требуемого ActiveGate. | path | Обязательный |
| body | [UpdateJob](#openapi-definition-UpdateJob) | JSON-тело запроса, содержащее параметры задачи обновления. | body | Обязательный |

### Объекты тела запроса

#### Объект `UpdateJob`

Конфигурация задачи обновления ActiveGate.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| agType | string | Тип ActiveGate. Элемент может принимать значения * `CLUSTER` * `ENVIRONMENT` * `ENVIRONMENT_MULTI` | Опциональный |
| cancelable | boolean | Задачу можно (`true`) или нельзя (`false`) отменить в данный момент. | Опциональный |
| duration | integer | Длительность обновления в миллисекундах. | Опциональный |
| environments | string[] | Список окружений (заданных по ID), к которым может подключаться ActiveGate. | Опциональный |
| error | string | Информация об ошибке обновления. | Опциональный |
| jobId | string | ID задачи обновления. | Опциональный |
| jobState | string | Статус задачи обновления. Элемент может принимать значения * `FAILED` * `IN_PROGRESS` * `PENDING` * `ROLLBACK` * `SCHEDULED` * `SKIPPED` * `SUCCEED` | Опциональный |
| startVersion | string | Исходная версия ActiveGate. | Опциональный |
| targetVersion | string | Целевая версия обновления.  Версия указывается в формате `<major>.<minor>.<revision>.<timestamp>`.  Чтобы обновиться до последней доступной версии, используйте значение `latest`. | Обязательный |
| timestamp | integer | Временная метка завершения задачи обновления.  Значение `null` означает, что задача всё ещё выполняется. | Опциональный |
| updateMethod | string | Метод обновления ActiveGate или его компонента. Элемент может принимать значения * `AUTOMATIC` * `MANUAL_INSTALLATION` * `ON_DEMAND` | Опциональный |
| updateType | string | Компонент, который нужно обновить. Элемент может принимать значения * `ACTIVE_GATE` * `REMOTE_PLUGIN_AGENT` * `SYNTHETIC` * `Z_REMOTE` | Опциональный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать для использования в реальном запросе.

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

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [UpdateJob](#openapi-definition-UpdateJob) | Успех. Задача обновления создана. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Входные данные некорректны. |
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

## Validate payload

Рекомендуем валидировать payload перед отправкой реального запроса. Код ответа **204** означает, что payload корректен.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/activeGates/{agId}/updateJobs/validator` |
| POST | Environment and Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/activeGates/{agId}/updateJobs/validator` |

### Аутентификация

Для выполнения этого запроса нужен access token со scope `activeGates.write`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Валидация пройдена. Отправленная задача обновления корректна. У ответа нет тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Входные данные некорректны. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка сервера. |

#### Объекты тела ответа

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

В этом примере запрос создаёт задачу обновления для ActiveGate с ID **1812885988** до версии **1.198.0.20200630-163221**.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -L -X POST 'https://mySampleEnv.live.dynatrace.com/api/v2/activeGates/1812885988/updateJobs' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



--data-raw '{



"targetVersion": "1.198.0.20200630-163221"



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/activeGates/1812885988/updateJobs
```

#### Request body

```
{



"targetVersion": "1.198.0.20200630-163221"



}
```

#### Response body

```
{



"jobId": "-7240069678607892845",



"jobState": "PENDING",



"updateMethod": null,



"updateType": null,



"cancelable": true,



"startVersion": "1.195.5.20200522-174041",



"targetVersion": "1.198.0.20200630-163221",



"timestamp": null,



"agType": "ENVIRONMENT",



"environments": [



"mySampleEnv"



],



"error": null,



"duration": null



}
```

#### Response code

201

## Связанные темы

* [Dynatrace ActiveGate](/managed/ingest-from/dynatrace-activegate "Изучите основные концепции, связанные с ActiveGate.")