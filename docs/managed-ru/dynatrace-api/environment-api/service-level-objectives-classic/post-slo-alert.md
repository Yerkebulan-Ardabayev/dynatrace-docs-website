---
title: Service-level objectives API - POST алерт SLO
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/service-level-objectives-classic/post-slo-alert
scraped: 2026-05-12T11:57:43.472211
---

# Service-level objectives API - POST алерт SLO

# Service-level objectives API - POST алерт SLO

* Справочник
* Обновлено 7 января 2025 г.

Создаёт новый алерт цели уровня обслуживания (SLO).

Запрос принимает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/slo/{id}/alert` |
| POST | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/slo/{id}/alert` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `slo.write`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| from | string | Начало запрашиваемого временного диапазона.  Можно использовать один из следующих форматов:  * Метка времени в UTC миллисекундах. * Человекочитаемый формат `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не указан, используется UTC. Вместо `T` можно использовать пробел. Секунды и доли секунды необязательны. * Относительный диапазон, назад от текущего момента. Формат `now-NU/A`, где `N` это количество времени, `U` это единица времени, а `A` это выравнивание. Выравнивание округляет все меньшие значения к ближайшему нулю в прошлом. Например, `now-1y/w` это один год назад, выровненный по неделе.   Можно также указать относительный диапазон без выравнивания: `now-NU`.   Поддерживаемые единицы времени для относительного диапазона:  + `m`: минуты   + `h`: часы   + `d`: дни   + `w`: недели   + `M`: месяцы   + `y`: годы  Если не задано, используется относительный диапазон в две недели (`now-2w`). | query | Необязательный |
| to | string | Конец запрашиваемого временного диапазона.  Можно использовать один из следующих форматов:  * Метка времени в UTC миллисекундах. * Человекочитаемый формат `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не указан, используется UTC. Вместо `T` можно использовать пробел. Секунды и доли секунды необязательны. * Относительный диапазон, назад от текущего момента. Формат `now-NU/A`, где `N` это количество времени, `U` это единица времени, а `A` это выравнивание. Выравнивание округляет все меньшие значения к ближайшему нулю в прошлом. Например, `now-1y/w` это один год назад, выровненный по неделе.   Можно также указать относительный диапазон без выравнивания: `now-NU`.   Поддерживаемые единицы времени для относительного диапазона:  + `m`: минуты   + `h`: часы   + `d`: дни   + `w`: недели   + `M`: месяцы   + `y`: годы  Если не задано, используется текущая метка времени. | query | Необязательный |
| timeFrame | string | Временной диапазон для вычисления значений SLO:  * `CURRENT`: собственный временной диапазон SLO. * `GTF`: временной диапазон, заданный параметрами **from** и **to**.  Если не задано, используется значение `CURRENT`. Поле может принимать значения: * `CURRENT` * `GTF` | query | Необязательный |
| id | string | ID требуемого SLO. | path | Обязательный |
| body | [AbstractSloAlertDto](#openapi-definition-AbstractSloAlertDto) | JSON-тело запроса. Содержит параметры нового алерта SLO. | body | Обязательный |

### Объекты тела запроса

#### Объект `AbstractSloAlertDto`

| Поле | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| alertName | string | Имя алерта. | Обязательный |
| alertThreshold | number | Порог алерта. Алерты статуса срабатывают, если значение опускается ниже этого, алерты скорости расходования срабатывают, если значение превышает его. | Обязательный |
| alertType | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из объектов:  * `BURN_RATE` -> BurnRateAlert * `STATUS` -> StatusAlert Поле может принимать значения: * `BURN_RATE` * `STATUS` | Обязательный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные поля. Для реального запроса её нужно адаптировать.

```
{



"alertName": "Payment service availability burn rate alert",



"alertThreshold": 10,



"alertType": "BURN_RATE"



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успех. Новый алерт создан. Ответ содержит параметры нового алерта. Заголовок ответа **location** содержит ID нового алерта. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Некорректный ввод. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Запрошенный ресурс не существует. |
| **412** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Предусловие для создания алерта SLO не выполнено. func-метрика SLO не может быть создана или не создана этим SLO. |
| **500** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Внутренняя ошибка сервера. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `EntityShortRepresentation`

Краткое представление сущности Dynatrace.

| Поле | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. |
| id | string | ID сущности Dynatrace. |
| name | string | Имя сущности Dynatrace. |

#### Объект `ErrorEnvelope`

| Поле | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Поле | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния. |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений. |
| message | string | Сообщение об ошибке. |

#### Объект `ConstraintViolation`

Список нарушений ограничений.

| Поле | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | Поле может принимать значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



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

* [Service-Level Objectives](/managed/deliver/service-level-objectives-classic "Мониторинг и алертинг по service-level objectives в Dynatrace через Service-Level Objectives Classic.")