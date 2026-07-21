---
title: Log Monitoring API v2 - POST ingest logs
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs
---

# Log Monitoring API v2 - POST ingest logs

# Log Monitoring API v2 - POST ingest logs

* Справка
* Опубликовано 05 мая 2021 г.

Отправляет собственные логи в Dynatrace.

Эта конечная точка доступна в SaaS-среде, либо, в качестве альтернативы, её можно открыть на Environmentном ActiveGate с включённым модулем **Log analytics collector**. Этот модуль включён по умолчанию на всех ActiveGate.

Запрос принимает один из следующих типов полезной нагрузки:

* `text/plain`, ограничивается одним событием лога.
* `application/json`, `application/jsonl`, `application/jsonlines`, `application/jsonlines+json`, `application/x-ndjson`, `application/x-jsonlines`, поддерживают несколько событий лога в одной полезной нагрузке.

Обязательно указывай корректный заголовок **Content-Type** и кодируй полезную нагрузку в **UTF-8**, например: `application/json; charset=utf-8`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/logs/ingest` |
| POST | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/logs/ingest` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `logs.ingest`.

Подробнее о том, как получить и использовать его, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

При использовании обработки логов с пользовательским конвейером обработки (OpenPipeline) ingest поддерживает все типы данных JSON для значений атрибутов. Для этого требуется SaaS-версия 1.295+ при использовании конечной точки SaaS API или версия ActiveGate 1.295+ при использовании конечной точки ActiveGate API. Во всех остальных случаях все принятые значения преобразуются в строковый тип.

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| content-type | string | (Необязательный) Позволяет указать тип содержимого через query-параметр. Имеет приоритет над значением, указанным в заголовке Content-Type. | query | Необязательный |
| structure | string | (Необязательный) Модель данных, используемая для структурирования входных данных в записи логов. Допустимые значения: `raw`, `flattened`. Подробнее см. в [документации﻿](https://dt-url.net/lyi2yte?dt=m). Элемент может принимать следующие значения * `raw` * `flattened` | query | Необязательный |
| X-Dynatrace-Attr | string | (Необязательный) Содержит разделённые амперсандом пары ключ-значение, представляющие дополнительные атрибуты лога, добавляемые к каждой принятой записи лога. Если один и тот же ключ встречается несколько раз, все значения фиксируются как атрибут с несколькими значениями. Query-параметры имеют приоритет над значениями, указанными в этом заголовке. Подробнее см. в [документации﻿](https://dt-url.net/2f4394a?dt=m). | header | Необязательный |
| X-Dynatrace-Options | string | (Необязательный) Содержит разделённые амперсандом параметры, специфичные для Dynatrace. Поддерживаемые опции: (только SaaS) `structure` (значения: `raw`, `flattened`) определяет, как входные данные структурируются в записи логов. Query-параметры имеют приоритет над значениями заголовка. Подробнее см. в [документации﻿](https://dt-url.net/lyi2yte?dt=m). | header | Необязательный |
| body | [LogMessageJson](#openapi-definition-LogMessageJson) | Тело запроса. Содержит одно или несколько событий лога для приёма. Конечная точка принимает один из следующих типов полезной нагрузки, определяемых заголовком **Accept**: * `text/plain`: поддерживает только одно событие лога. * `application/json`: поддерживает несколько событий лога в одной полезной нагрузке в виде массива JSON. * `application/jsonl`, `application/jsonlines`, `application/x-ndjson`, `application/jsonlines+json` или `application/x-jsonlines`: поддерживает несколько событий лога в виде полезной нагрузки JSON-lines (один объект JSON на строку). | body | Необязательный |

### Объекты тела запроса

#### Объект `LogMessageJson`

Набор из одного или нескольких событий лога:

* в формате JSON:

  + массив объектов JSON событий лога, например:

    `[ { "message": "1" }, { "message": "2" } ]`
  + один объект JSON события лога, например:

    `{ "message": "1" }`
* в формате JSON lines: последовательность объектов JSON событий лога, разделённых переносами строк, например:

  ```
  { "message": "1" }



  { "message": "2" }
  ```

События лога из входных данных сопоставляются с записями логов Dynatrace, содержащими три специальных атрибута: timestamp, loglevel и content, а также карту прочих атрибутов. Эти четыре свойства устанавливаются на основе ключей, присутствующих во входном объекте JSON. Подробнее см. в [документации﻿](https://dt-url.net/lyi2yte?dt=m).

(Только SaaS) Обработка атрибутов зависит от модели данных, используемой для обработки входных данных. Действующая модель данных для конкретного запроса зависит от параметра `structure` или модели данных тенанта по умолчанию, которая определяется конфигурацией тенанта. Подробнее см. в [документации﻿](https://dt-url.net/lyi2yte?dt=m).

### Модель JSON тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать для использования в реальном запросе.

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
| **200** | [SuccessEnvelope](#openapi-definition-SuccessEnvelope) | Принята только часть входных событий из-за недействительности некоторых событий. Подробности см. в теле ответа. |
| **204** | - | Успешно. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные недействительны. |
| **402** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Причина связана либо со статусом лицензионного соглашения, либо с исчерпанием лицензии [DPS﻿](https://www.dynatrace.com/support/help/shortlink/dynatrace-platform-subscription). |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Запрошенный ресурс не существует. Это может произойти, если нет доступного ActiveGate с включённым модулем Log Analytics Collector. |
| **413** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Размер полезной нагрузки запроса слишком велик. Это может произойти, если размер полезной нагрузки в байтах превышает лимит или если принятая полезная нагрузка представляет собой массив JSON, размер которого превышает лимит. |
| **429** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Слишком много запросов. Это может произойти, если ActiveGate в данный момент не может обработать больше запросов или если приём логов отключён. Можно повторить с экспоненциальной задержкой. |
| **501** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Сервер либо не распознаёт метод запроса, либо не имеет возможности выполнить запрос. В Log Monitoring Classic это может произойти, если индексированное хранилище логов не включено. |
| **502** | - | Ошибка. Bad Gateway. Это может произойти, если промежуточная система (например, ActiveGate или прокси) сталкивается с проблемой при пересылке запроса. Можно повторить с экспоненциальной задержкой. |
| **503** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Сервер в данный момент не может обработать запрос. Это может произойти при перегрузке ActiveGate. Можно повторить с экспоненциальной задержкой. |
| **504** | - | Ошибка. Gateway Timeout. Может возникнуть из-за проблемы в базовой инфраструктуре, вызывающей задержку обработки запроса. Можно повторить с экспоненциальной задержкой. |
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
| code | integer | HTTP-код статуса |
| message | string | Подробное сообщение |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Модели JSON тела ответа

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

## Похожие темы

* [Недоступно в Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.")
* [Log Monitoring](/managed/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.")