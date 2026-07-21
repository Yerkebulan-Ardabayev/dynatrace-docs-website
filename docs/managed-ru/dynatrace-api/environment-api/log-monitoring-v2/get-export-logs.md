---
title: Log Monitoring API v2 - GET экспорт логов
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/log-monitoring-v2/get-export-logs
scraped: 2026-05-12T11:54:15.310165
---

# Log Monitoring API v2 - GET экспорт логов

# Log Monitoring API v2 - GET экспорт логов

* Справочник
* Обновлено 20 ноября 2025 г.

Получает записи логов, соответствующие заданным критериям. Подходящие записи логов сортируются по критериям, указанным в query-параметре **sort**.

В отличие от запроса [GET search logs](/managed/dynatrace-api/environment-api/log-monitoring-v2/get-search-logs "Получение записей логов через Log Monitoring API v2."), этот запрос не накладывает ограничения на общее число результирующих записей логов. Однако если результирующий лог слишком велик, применяется пагинация. Размер страницы можно задать в query-параметре **pageSize**. В таких случаях первый ответ содержит **nextPageKey** для второй страницы. Используйте его в query-параметре **nextPageKey**, чтобы получить вторую страницу, которая, в свою очередь, содержит **nextPageKey** для третьей страницы, и так далее.

Запрос возвращает payload в формате `application/json`.

Этот API работает только с Log Monitoring Classic.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/logs/export` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/logs/export` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `logs.read`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| from | string | Начало запрашиваемого временного диапазона.  Можно использовать один из следующих форматов:  * Метка времени в миллисекундах UTC. * Человекочитаемый формат `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не указан, используется UTC. Вместо `T` можно использовать пробел. Секунды и доли секунды необязательны. * Относительный диапазон, назад от текущего момента. Формат: `now-NU/A`, где `N` это количество времени, `U` это единица времени, а `A` это выравнивание. Выравнивание округляет все меньшие значения до ближайшего нуля в прошлом. Например, `now-1y/w` это один год назад, выровненный по неделе.   Также можно указать относительный диапазон без выравнивания: `now-NU`.   Поддерживаемые единицы времени для относительного диапазона: + `m`: минуты   + `h`: часы   + `d`: дни   + `w`: недели   + `M`: месяцы   + `y`: годы  Если не задано, используется относительный диапазон в две недели (`now-2w`). | query | Необязательный |
| to | string | Конец запрашиваемого временного диапазона.  Можно использовать один из следующих форматов:  * Метка времени в миллисекундах UTC. * Человекочитаемый формат `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не указан, используется UTC. Вместо `T` можно использовать пробел. Секунды и доли секунды необязательны. * Относительный диапазон, назад от текущего момента. Формат: `now-NU/A`, где `N` это количество времени, `U` это единица времени, а `A` это выравнивание. Выравнивание округляет все меньшие значения до ближайшего нуля в прошлом. Например, `now-1y/w` это один год назад, выровненный по неделе.   Также можно указать относительный диапазон без выравнивания: `now-NU`.   Поддерживаемые единицы времени для относительного диапазона: + `m`: минуты   + `h`: часы   + `d`: дни   + `w`: недели   + `M`: месяцы   + `y`: годы  Если не задано, используется текущая метка времени. | query | Необязательный |
| nextPageKey | string | Курсор для следующей страницы результатов. Его можно найти в поле **nextPageKey** предыдущего ответа.  Первая страница всегда возвращается, если query-параметр **nextPageKey** не указан.  Когда **nextPageKey** задан для получения последующих страниц, необходимо опустить все остальные query-параметры. | query | Необязательный |
| pageSize | integer | Количество результатов на странице результатов. | query | Необязательный |
| query | string | Поисковый запрос по логам.  Запрос должен использовать [Dynatrace search query language](https://dt-url.net/pe03s6f?dt=m). | query | Необязательный |
| sort | string | Определяет порядок сортировки записей логов.  Каждое поле имеет знаковый префикс (+/-) для порядка сортировки. Если знаковый префикс не задан, применяется опция `+`.  В настоящее время сортировка доступна только по timestamp (+timestamp для самых старых записей сначала, или -timestamp для самых новых записей сначала).  Когда миллисекундного разрешения, предоставляемого timestamp, недостаточно, записи логов сортируются по порядку их появления в источнике логов (удалённый процесс, пишущий в эндпоинт REST API, или удалённый процесс, из которого собираются логи). | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ExportedLogRecordList](#openapi-definition-ExportedLogRecordList) | Успех |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Входные данные некорректны. |
| **501** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Сервер либо не распознаёт метод запроса, либо не может выполнить запрос. Может произойти, когда включено хранилище логов Grail. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ExportedLogRecordList`

Список экспортированных записей логов.

| Элемент | Тип | Описание |
| --- | --- | --- |
| nextPageKey | string | Курсор для следующей страницы результатов. На последней странице имеет значение `null`.  Используйте его в query-параметре **nextPageKey**, чтобы получить последующие страницы результата. |
| pageSize | integer | Количество записей на странице. |
| results | [LogRecord[]](#openapi-definition-LogRecord) | Список полученных записей логов. |
| totalCount | integer | Общее количество записей в результате. |
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



"nextPageKey": "___-2lZ43q0AAAAdeJxjYAAC1sLS1KJKBhjggtIijFCGHEwCAFiHAoP___7aVnjerQ",



"pageSize": 100,



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



"totalCount": 150



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