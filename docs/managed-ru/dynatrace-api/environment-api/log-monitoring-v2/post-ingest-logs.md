---
title: Log Monitoring API v2 - POST ingest логов
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs
scraped: 2026-05-12T11:14:01.154743
---

# Log Monitoring API v2 - POST ingest логов

# Log Monitoring API v2 - POST ingest логов

* Справочник
* Опубликовано 05 мая 2021 г.

Отправляет пользовательские логи в Dynatrace.

Этот эндпоинт доступен в вашем SaaS-окружении, либо, как альтернатива, его можно открыть на Environmental ActiveGate с включённым модулем **Log analytics collector**. Этот модуль включён по умолчанию на всех ваших ActiveGate.

Запрос принимает один из следующих типов payload:

* `text/plain`, ограничен одним событием лога.
* `application/json`, `application/jsonl`, `application/jsonlines`, `application/jsonlines+json`, `application/x-ndjson`, `application/x-jsonlines`, поддерживают несколько событий лога в одном payload.

Обязательно задайте правильный заголовок **Content-Type** и кодируйте payload в **UTF-8**, например: `application/json; charset=utf-8`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/logs/ingest` |
| POST | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/logs/ingest` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `logs.ingest`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

При использовании обработки логов с пользовательским конвейером обработки (OpenPipeline) ingest поддерживает все типы данных JSON для значений атрибутов. Для этого требуется версия SaaS 1.295+ при использовании SaaS API-эндпоинта или версия ActiveGate 1.295+ при использовании ActiveGate API-эндпоинта. Во всех остальных случаях все загружаемые значения преобразуются в строковый тип.

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| content-type | string | (Необязательно) Позволяет передать content type через query-параметр. Имеет приоритет над значением, переданным в заголовке Content-Type. | query | Необязательный |
| structure | string | (Необязательно) Модель данных, используемая для структурирования входных данных в записи логов. Допустимые значения: `raw`, `flattened`. Подробнее смотрите в [documentation](https://dt-url.net/lyi2yte). Элемент может принимать значения * `raw` * `flattened` | query | Необязательный |
| X-Dynatrace-Attr | string | (Необязательно) Содержит пары ключ-значение, разделённые амперсандом, представляющие дополнительные атрибуты лога, добавляемые к каждой загружаемой записи лога. Если один и тот же ключ встречается несколько раз, все значения собираются в атрибут с несколькими значениями. Query-параметры имеют приоритет над значениями, переданными в этом заголовке. | header | Необязательный |
| X-Dynatrace-Options | string | (Необязательно) Содержит специфичные для Dynatrace параметры, разделённые амперсандом. Поддерживаемые опции: (только SaaS) `structure` (значения: `raw`, `flattened`) определяет, как входные данные структурируются в записи логов. Query-параметры имеют приоритет над значениями заголовка. Подробнее смотрите в [documentation](https://dt-url.net/lyi2yte). | header | Необязательный |
| body | [LogMessageJson](#openapi-definition-LogMessageJson) | Тело запроса. Содержит одно или несколько событий лога для загрузки.  Эндпоинт принимает один из следующих типов payload, определяемых заголовком **Accept**:  * `text/plain`: поддерживает только одно событие лога. * `application/json`: поддерживает несколько событий лога в одном payload в виде JSON-массива. * `application/jsonl`, `application/jsonlines`, `application/x-ndjson`, `application/jsonlines+json`, или `application/x-jsonlines`: поддерживает несколько событий лога в виде payload JSON-lines (один JSON-объект на строку). | body | Необязательный |

### Объекты тела запроса

#### Объект `LogMessageJson`

Набор из одного или нескольких событий лога:

* в формате JSON:

  + массив JSON-объектов событий лога, например:

    `[ { "message": "1" }, { "message": "2" } ]`
  + один JSON-объект события лога, например:

    `{ "message": "1" }`
* в формате JSON lines: последовательность JSON-объектов событий лога, разделённых переводами строк, например:

  ```
  { "message": "1" }



  { "message": "2" }
  ```

События лога из входных данных сопоставляются с записями логов Dynatrace, содержащими три специальных атрибута: timestamp, loglevel и content, а также карту других атрибутов. Эти четыре свойства устанавливаются на основе ключей, присутствующих во входном JSON-объекте. Подробнее смотрите в [documentation](https://dt-url.net/lyi2yte).

(Только SaaS) Обработка атрибутов зависит от модели данных, используемой для обработки входных данных. Эффективная модель данных для конкретного запроса зависит от параметра `structure` или модели данных тенанта по умолчанию, которая определяется конфигурацией тенанта. Подробнее можно узнать в [documentation](https://dt-url.net/lyi2yte).

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её необходимо адаптировать для использования в реальном запросе.

```
[



{



"content": "Exception: Custom error log sent via Generic Log Ingest",



"log.source": "/var/log/syslog",



"timestamp": "2025-12-17T22:12:31.0000",



"severity": "error",



"custom.attribute": "attribute value",



"complex": {



"key-1": "attribute value-1",



"key-2": 234.2



},



"array.attr": [



"value-1",



1,



null,



true,



[



1,



2,



3



],



{



"key": "value"



}



]



},



{



"message": "User1 logged in successfully",



"log.source": "/var/log/syslog",



"@timestamp": "1765281600"



},



{



"payload": "Exception: Custom error log sent via Generic Log Ingest",



"log.source": "/var/log/syslog"



},



{



"log": "My log message without additional attributes"



}



]
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [SuccessEnvelope](#openapi-definition-SuccessEnvelope) | Только часть входных событий была загружена из-за невалидности событий. Подробности смотрите в теле ответа. |
| **204** | - | Успех. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Входные данные некорректны. |
| **402** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Это связано либо со статусом вашего лицензионного соглашения, либо с тем, что вы исчерпали свою [DPS license](https://www.dynatrace.com/support/help/shortlink/dynatrace-platform-subscription). |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Запрашиваемый ресурс не существует. Это может произойти, когда нет доступного ActiveGate с включённым модулем Log Analytics Collector. |
| **413** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Размер payload запроса слишком велик. Это может произойти, когда размер payload в байтах превышает лимит или когда загружаемый payload это JSON-массив с размером, превышающим лимит. |
| **429** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Слишком много запросов. Это может произойти, когда ActiveGate в данный момент не может обработать больше запросов или когда загрузка логов отключена. Повторяемо со стратегией экспоненциальной задержки. |
| **501** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Сервер либо не распознаёт метод запроса, либо не может выполнить запрос. В Log Monitoring Classic это может произойти, когда индексированное хранилище логов не включено. |
| **502** | - | Неудача. Bad Gateway. Это может произойти, если промежуточная система (например, ActiveGate или прокси) сталкивается с проблемой при пересылке запроса. Повторяемо со стратегией экспоненциальной задержки. |
| **503** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Сервер в данный момент не может обработать запрос. Это может произойти, когда ActiveGate перегружен. Повторяемо со стратегией экспоненциальной задержки. |
| **504** | - | Неудача. Gateway Timeout. Это может произойти из-за проблемы в нижележащей инфраструктуре, вызывающей задержку обработки запроса. Повторяемо со стратегией экспоненциальной задержки. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `SuccessEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| details | [Success](#openapi-definition-Success) | - |

#### Объект `Success`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния |
| message | string | Подробное сообщение |

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



"details": {



"code": 1,



"message": "string"



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

## Связанные темы

* [Недоступно в Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.")
* [Log Monitoring](/managed/analyze-explore-automate/log-monitoring "Как включить Log Monitoring, какие инсайты он предоставляет и многое другое.")