---
title: OneAgent remote configuration management API - GET завершённые задания
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/remote-configuration/oneagent/get-finished-jobs
scraped: 2026-05-12T11:55:11.349608
---

# OneAgent remote configuration management API - GET завершённые задания

# OneAgent remote configuration management API - GET завершённые задания

* Справочник
* Опубликовано 06 октября 2022 г.

Перечисляет завершённые задания конфигурации для OneAgent.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/oneagents/remoteConfigurationManagement` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/oneagents/remoteConfigurationManagement` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `oneAgents.read`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| from | string | Начало запрашиваемого таймфрейма для задания remote configuration management.  Можно использовать один из следующих форматов:  * Таймстамп в миллисекундах UTC. * Человекочитаемый формат `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не задан, используется UTC. Вместо `T` можно использовать пробел. Секунды и доли секунды опциональны. * Относительный таймфрейм, отсчитываемый от текущего момента. Формат: `now-NU/A`, где `N` это количество, `U` единица времени, `A` выравнивание. Выравнивание округляет все меньшие значения до ближайшего нуля в прошлом. Например, `now-1y/w` это год назад с выравниванием по неделе.   Также можно указать относительный таймфрейм без выравнивания: `now-NU`.   Поддерживаемые единицы времени для относительного таймфрейма: + `m`: минуты   + `h`: часы   + `d`: дни   + `w`: недели   + `M`: месяцы   + `y`: годы | query | Необязательный |
| to | string | Конец запрашиваемого таймфрейма для задания remote configuration management.  Можно использовать один из следующих форматов:  * Таймстамп в миллисекундах UTC. * Человекочитаемый формат `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не задан, используется UTC. Вместо `T` можно использовать пробел. Секунды и доли секунды опциональны. * Относительный таймфрейм, отсчитываемый от текущего момента. Формат: `now-NU/A`, где `N` это количество, `U` единица времени, `A` выравнивание. Выравнивание округляет все меньшие значения до ближайшего нуля в прошлом. Например, `now-1y/w` это год назад с выравниванием по неделе.   Также можно указать относительный таймфрейм без выравнивания: `now-NU`.   Поддерживаемые единицы времени для относительного таймфрейма: + `m`: минуты   + `h`: часы   + `d`: дни   + `w`: недели   + `M`: месяцы   + `y`: годы  Если не задано, используется текущий таймстамп. | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [RemoteConfigurationManagementJobList](#openapi-definition-RemoteConfigurationManagementJobList) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `RemoteConfigurationManagementJobList`

Список заданий remote configuration management.

| Поле | Тип | Описание |
| --- | --- | --- |
| jobs | [RemoteConfigurationManagementJobSummary[]](#openapi-definition-RemoteConfigurationManagementJobSummary) | Список заданий remote configuration management. |

#### Объект `RemoteConfigurationManagementJobSummary`

Задание remote configuration management с базовыми данными.

| Поле | Тип | Описание |
| --- | --- | --- |
| endTime | string | Дата (в формате ISO 8601: yyyy-MM-dd'T'HH:mm:ss.SSS'Z') завершения задания remote configuration management. Это поле присутствует только для завершённых заданий. |
| entityType | string | Тип сущностей, изменяемых remote configuration management. Поле может принимать значения: * `ACTIVE_GATE` * `ONE_AGENT` |
| id | string | ID задания remote configuration management. |
| startTime | string | Дата (в формате ISO 8601: yyyy-MM-dd'T'HH:mm:ss.SSS'Z') запуска задания remote configuration management. |

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



"jobs": [



{



"endTime": "2020-11-05T08:15:30.144Z",



"entityType": "ACTIVE_GATE or ONE_AGENT",



"id": "7974003406714390819",



"startTime": "2020-11-05T08:15:30.144Z"



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