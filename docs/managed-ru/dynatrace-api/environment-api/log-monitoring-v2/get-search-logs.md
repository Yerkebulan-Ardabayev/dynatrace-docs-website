---
title: Log Monitoring API v2 - GET поиск логов
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/log-monitoring-v2/get-search-logs
scraped: 2026-05-12T11:54:16.614018
---

# Log Monitoring API v2 - GET поиск логов

# Log Monitoring API v2 - GET поиск логов

* Справочник
* Обновлено 20 ноября 2025 г.

Получает записи логов, соответствующие заданным критериям. Подходящие записи логов сортируются по критериям, указанным в query-параметре **sort**, после чего возвращаются первые *X* записей (как указано в query-параметре **limit**). Чтобы выполнить запрос без ограничения по размеру, используйте запрос [GET export logs](/managed/dynatrace-api/environment-api/log-monitoring-v2/get-export-logs "Получение записей логов через Log Monitoring API v2.").

Если результирующий лог слишком велик, он делится на срезы. В таких случаях первый ответ содержит **nextSliceKey** для второго среза. Используйте его в query-параметре **nextSliceKey**, чтобы получить второй срез, который, в свою очередь, содержит **nextSliceKey** для третьего среза, и так далее.

Результаты могут быть распределены между срезами неравномерно, и некоторые срезы могут быть пустыми.

Запрос возвращает payload в формате `application/json`.

Этот API работает только с Log Monitoring Classic.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/logs/search` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/logs/search` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `logs.read`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| from | string | Начало запрашиваемого временного диапазона.  Можно использовать один из следующих форматов:  * Метка времени в миллисекундах UTC. * Человекочитаемый формат `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не указан, используется UTC. Вместо `T` можно использовать пробел. Секунды и доли секунды необязательны. * Относительный диапазон, назад от текущего момента. Формат: `now-NU/A`, где `N` это количество времени, `U` это единица времени, а `A` это выравнивание. Выравнивание округляет все меньшие значения до ближайшего нуля в прошлом. Например, `now-1y/w` это один год назад, выровненный по неделе.   Также можно указать относительный диапазон без выравнивания: `now-NU`.   Поддерживаемые единицы времени для относительного диапазона: + `m`: минуты   + `h`: часы   + `d`: дни   + `w`: недели   + `M`: месяцы   + `y`: годы  Если не задано, используется относительный диапазон в две недели (`now-2w`). | query | Необязательный |
| to | string | Конец запрашиваемого временного диапазона.  Можно использовать один из следующих форматов:  * Метка времени в миллисекундах UTC. * Человекочитаемый формат `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не указан, используется UTC. Вместо `T` можно использовать пробел. Секунды и доли секунды необязательны. * Относительный диапазон, назад от текущего момента. Формат: `now-NU/A`, где `N` это количество времени, `U` это единица времени, а `A` это выравнивание. Выравнивание округляет все меньшие значения до ближайшего нуля в прошлом. Например, `now-1y/w` это один год назад, выровненный по неделе.   Также можно указать относительный диапазон без выравнивания: `now-NU`.   Поддерживаемые единицы времени для относительного диапазона: + `m`: минуты   + `h`: часы   + `d`: дни   + `w`: недели   + `M`: месяцы   + `y`: годы  Если не задано, используется текущая метка времени. | query | Необязательный |
| limit | integer | Желаемое количество записей логов.  Максимально допустимый лимит: 1000.  Если не задано, используется 1000. | query | Необязательный |
| query | string | Поисковый запрос по логам.  Запрос должен использовать [Dynatrace search query language](https://dt-url.net/pe03s6f). | query | Необязательный |
| sort | string | Определяет порядок сортировки записей логов.  Каждое поле имеет знаковый префикс (+/-) для порядка сортировки. Если знаковый префикс не задан, применяется опция `+`.  В настоящее время сортировка доступна только по timestamp (+timestamp для самых старых записей сначала, или -timestamp для самых новых записей сначала).  Когда миллисекундного разрешения, предоставляемого timestamp, недостаточно, записи логов сортируются по порядку их появления в источнике логов (удалённый процесс, пишущий в эндпоинт REST API, или удалённый процесс, из которого собираются логи). | query | Необязательный |
| nextSliceKey | string | Курсор для следующего среза результатов. Его можно найти в поле **nextSliceKey** предыдущего ответа.  Первый срез всегда возвращается, если этот параметр не указан.  Если этот параметр задан, все остальные query-параметры игнорируются.  Не поддерживается в *Log Management and Analytics, powered by Grail*. | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [LogRecordsList](#openapi-definition-LogRecordsList) | Успех |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Входные данные некорректны. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `LogRecordsList`

Список полученных записей логов.

| Элемент | Тип | Описание |
| --- | --- | --- |
| nextSliceKey | string | Курсор для следующего среза записей логов. Всегда null в *Log Management and Analytics, powered by Grail*. |
| results | [LogRecord[]](#openapi-definition-LogRecord) | Список полученных записей логов. |
| sliceSize | integer | Общее количество записей в срезе. |
| warnings | string | Необязательные предупреждающие сообщения. |

#### Объект `LogRecord`

Одна запись лога.

| Элемент | Тип | Описание |
| --- | --- | --- |
| additionalColumns | object | Дополнительные столбцы записи лога. |
| content | string | Содержимое записи лога. |
| eventType | string | Тип события |
| status | string | Статус лога (на основе уровня лога). Элемент может принимать значения * `ERROR` * `INFO` * `NONE` * `NOT_APPLICABLE` * `WARN` |
| timestamp | integer | Метка времени записи лога, в миллисекундах UTC. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"nextSliceKey": "___-2hI03q0AAAAAAAAAAAAAA-gAAAAAAAAH0P____8AAABkAAAACXRpbWVzdGFtcAD___7aEjTerQ",



"results": [



{



"additionalColumns": {



"custom.attribute": [



"value1",



"value2"



],



"loglevel": [



"SEVERE"



]



},



"content": "example log content",



"event.type": "LOG",



"status": "ERROR",



"timestamp": "1631193089000"



}



],



"sliceSize": 100



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

* [Log Monitoring](/managed/analyze-explore-automate/log-monitoring "Как включить Log Monitoring, какие инсайты он предоставляет и многое другое.")