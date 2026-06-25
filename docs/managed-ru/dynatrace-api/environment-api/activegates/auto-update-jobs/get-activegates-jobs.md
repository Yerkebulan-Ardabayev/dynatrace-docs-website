---
title: ActiveGate API - GET ActiveGates with auto-update jobs
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/activegates/auto-update-jobs/get-activegates-jobs
scraped: 2026-05-12T11:59:56.438212
---

# ActiveGate API - GET ActiveGates with auto-update jobs

# ActiveGate API - GET ActiveGates with auto-update jobs

* Reference
* Published Jul 02, 2020

Возвращает список всех ActiveGate, у которых есть задачи авто-обновления. Список включает завершённые задачи (успешные или с ошибкой) и задачи в процессе выполнения.

Вы можете сузить вывод, указав параметры фильтрации в запросе.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/activeGates/updateJobs` |
| GET | Environment and Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/activeGates/updateJobs` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `activeGates.read`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| from | string | Начало запрашиваемого таймфрейма для задач обновления.  Можно использовать один из следующих форматов:  * Временная метка в миллисекундах UTC. * Человекочитаемый формат `2021-01-25T05:57:01.123+01:00`. Если зона не указана, используется UTC. Вместо `T` можно использовать пробел. Секунды и доли секунды опциональны. * Относительный таймфрейм назад от текущего момента. Формат: `now-NU/A`, где `N` это количество времени, `U` это единица измерения, а `A` это выравнивание. Выравнивание округляет все меньшие значения до ближайшего нуля в прошлом. Например, `now-1y/w` это год назад, выровненный по неделе.   Можно также указать относительный таймфрейм без выравнивания: `now-NU`.   Поддерживаемые единицы времени для относительного таймфрейма: + `m`: минуты   + `h`: часы   + `d`: дни   + `w`: недели   + `M`: месяцы   + `y`: годы  Если не задано, используется относительный таймфрейм в один день (`now-1d`).  Максимальный таймфрейм 31 день. | query | Опциональный |
| to | string | Конец запрашиваемого таймфрейма для задач обновления.  Можно использовать один из следующих форматов:  * Временная метка в миллисекундах UTC. * Человекочитаемый формат `2021-01-25T05:57:01.123+01:00`. Если зона не указана, используется UTC. Вместо `T` можно использовать пробел. Секунды и доли секунды опциональны. * Относительный таймфрейм назад от текущего момента. Формат: `now-NU/A`, где `N` это количество времени, `U` это единица измерения, а `A` это выравнивание. Выравнивание округляет все меньшие значения до ближайшего нуля в прошлом. Например, `now-1y/w` это год назад, выровненный по неделе.   Можно также указать относительный таймфрейм без выравнивания: `now-NU`.   Поддерживаемые единицы времени для относительного таймфрейма: + `m`: минуты   + `h`: часы   + `d`: дни   + `w`: недели   + `M`: месяцы   + `y`: годы  Если не задано, используется текущая временная метка. | query | Опциональный |
| startVersionCompareType | string | Фильтрует результирующий набор задач обновления по указанной исходной версии.  Здесь указывается оператор сравнения. Элемент может принимать значения * `EQUAL` * `GREATER` * `GREATER_EQUAL` * `LOWER` * `LOWER_EQUAL` | query | Опциональный |
| startVersion | string | Фильтрует результирующий набор задач обновления по исходной версии (обязательный формат `<major>.<minor>.<revision>`). | query | Опциональный |
| updateType | string | Фильтрует результирующий набор задач обновления по типу обновления. Элемент может принимать значения * `ACTIVE_GATE` * `REMOTE_PLUGIN_AGENT` * `SYNTHETIC` * `Z_REMOTE` | query | Опциональный |
| targetVersionCompareType | string | Фильтрует результирующий набор задач обновления по указанной целевой версии.  Здесь указывается оператор сравнения. Элемент может принимать значения * `EQUAL` * `GREATER` * `GREATER_EQUAL` * `LOWER` * `LOWER_EQUAL` | query | Опциональный |
| targetVersion | string | Фильтрует результирующий набор задач обновления по целевой версии (обязательный формат `<major>.<minor>.<revision>`). | query | Опциональный |
| lastUpdates | boolean | Если `true`, фильтрует результирующий набор задач обновления до самого последнего обновления каждого типа. | query | Опциональный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [UpdateJobsAll](#openapi-definition-UpdateJobsAll) | Успех |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Входные данные некорректны. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка сервера. |

### Объекты тела ответа

#### Объект `UpdateJobsAll`

Список ActiveGate с задачами обновления.

| Элемент | Тип | Описание |
| --- | --- | --- |
| allUpdateJobs | [UpdateJobList[]](#openapi-definition-UpdateJobList) | Список ActiveGate с задачами обновления. |

#### Объект `UpdateJobList`

Список задач обновления ActiveGate.

| Элемент | Тип | Описание |
| --- | --- | --- |
| agId | string | ID ActiveGate. |
| updateJobs | [UpdateJob[]](#openapi-definition-UpdateJob) | Список задач обновления ActiveGate. |

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



"allUpdateJobs": [



{



"agId": "0x3efdd092",



"updateJobs": [



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



]



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

## Связанные темы

* [Dynatrace ActiveGate](/managed/ingest-from/dynatrace-activegate "Изучите основные концепции, связанные с ActiveGate.")