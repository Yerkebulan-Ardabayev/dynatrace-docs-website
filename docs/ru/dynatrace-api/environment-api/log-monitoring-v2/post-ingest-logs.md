---
title: Log Monitoring API v2 - POST ingest logs
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs
scraped: 2026-03-04T21:35:09.361330
---

# Log Monitoring API v2 - POST отправка логов


* Справочник
* Опубликовано 05 мая 2021

Отправляет пользовательские логи в Dynatrace.

Этот эндпоинт доступен в вашей SaaS-среде или, в качестве альтернативы, вы можете предоставить его через ActiveGate среды с включённым модулем **Log analytics collector**. Этот модуль включён по умолчанию на всех ваших ActiveGate.

Запрос принимает один из следующих типов полезной нагрузки:

* `text/plain` — ограничен одним событием лога.
* `application/json`, `application/jsonl`, `application/jsonlines`, `application/jsonlines+json`, `application/x-ndjson`, `application/x-jsonlines` — поддерживают несколько событий логов в одной полезной нагрузке.

Обязательно установите правильный заголовок **Content-Type** и кодируйте полезную нагрузку в **UTF-8**, например: `application/json; charset=utf-8`.

|  |  |  |
| --- | --- | --- |
| POST | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/logs/ingest` |
| POST | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/logs/ingest` |

## Аутентификация

Для выполнения этого запроса необходим токен доступа с областью действия `logs.ingest`.

Чтобы узнать, как получить и использовать его, см. [Токены и аутентификация](../../../discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication.md).

## Параметры

При использовании обработки логов с пользовательским конвейером обработки (OpenPipeline) отправка поддерживает все типы данных JSON для значений атрибутов. Для этого требуется SaaS версии 1.295+ при использовании эндпоинта SaaS API или ActiveGate версии 1.295+ при использовании эндпоинта ActiveGate API. Во всех остальных случаях все отправляемые значения преобразуются в строковый тип.

| Параметр | Тип | Описание | Расположение | Обязательность |
| --- | --- | --- | --- | --- |
| content-type | string | (Необязательно) Позволяет указать тип содержимого через параметр запроса. Имеет приоритет над значением, указанным в заголовке Content-Type. | query | Необязательно |
| structure | string | (Необязательно) Модель данных, используемая для структурирования входных данных в записи логов. Допустимые значения: `raw`, `flattened`. Подробнее см. в [документации](https://dt-url.net/lyi2yte). Элемент может содержать следующие значения: * `raw` * `flattened` | query | Необязательно |
| X-Dynatrace-Attr | string | (Необязательно) Содержит разделённые амперсандом пары ключ-значение, представляющие дополнительные атрибуты логов, которые будут добавлены к каждой отправляемой записи лога. Если один и тот же ключ появляется несколько раз, все значения фиксируются как многозначный атрибут. Параметры запроса имеют приоритет над значениями, указанными в этом заголовке. | header | Необязательно |
| X-Dynatrace-Options | string | (Необязательно) Содержит разделённые амперсандом параметры, специфичные для Dynatrace. Поддерживаемые опции: (только SaaS) `structure` (значения: `raw`, `flattened`) определяет, как входные данные структурируются в записи логов. Параметры запроса имеют приоритет над значениями заголовка. Подробнее см. в [документации](https://dt-url.net/lyi2yte). | header | Необязательно |
| body | [LogMessageJson](#openapi-definition-LogMessageJson) | Тело запроса. Содержит одно или несколько событий логов для отправки. Эндпоинт принимает один из следующих типов полезной нагрузки, определяемых заголовком **Accept**: * `text/plain`: поддерживает только одно событие лога. * `application/json`: поддерживает несколько событий логов в одном JSON-массиве. * `application/jsonl`, `application/jsonlines`, `application/x-ndjson`, `application/jsonlines+json` или `application/x-jsonlines`: поддерживает несколько событий логов в формате JSON-lines (один JSON-объект на строку). | body | Необязательно |

### Объекты тела запроса

#### Объект `LogMessageJson`

Набор из одного или нескольких событий логов:

* в формате JSON:

  + массив JSON-объектов событий логов, например:

    `[ { "message": "1" }, { "message": "2" } ]`
  + один JSON-объект события лога, например:

    `{ "message": "1" }`
* в формате JSON lines: последовательность JSON-объектов событий логов, разделённых переносами строк, например:

  ```
  { "message": "1" }


  { "message": "2" }
  ```

События логов из входных данных сопоставляются с записями логов Dynatrace, содержащими три специальных атрибута: timestamp, loglevel и content, а также набор других атрибутов. Эти четыре свойства устанавливаются на основе ключей, присутствующих во входном JSON-объекте. Подробнее см. в [документации](https://dt-url.net/lyi2yte).

(Только SaaS) Обработка атрибутов зависит от модели данных, используемой для обработки входных данных. Эффективная модель данных для конкретного запроса зависит от параметра `structure` или модели данных тенанта по умолчанию, которая определяется конфигурацией тенанта. Подробнее можно узнать в [документации](https://dt-url.net/lyi2yte).

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
| **200** | [SuccessEnvelope](#openapi-definition-SuccessEnvelope) | Только часть входных событий была принята из-за невалидности событий. Подробности см. в теле ответа. |
| **204** | - | Успех. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные некорректны. |
| **402** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Это связано либо со статусом вашего лицензионного соглашения, либо с тем, что вы исчерпали свою [лицензию DPS](https://www.dynatrace.com/support/help/shortlink/dynatrace-platform-subscription). |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Запрашиваемый ресурс не существует. Это может произойти, когда нет доступного ActiveGate с включённым модулем Log Analytics Collector. |
| **413** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Размер полезной нагрузки запроса слишком велик. Это может произойти, когда размер полезной нагрузки в байтах превышает лимит или когда отправляемая полезная нагрузка является JSON-массивом, размер которого превышает лимит. |
| **429** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Слишком много запросов. Это может произойти, когда ActiveGate не может обработать больше запросов в данный момент или когда приём логов отключён. Повторите попытку с экспоненциальной задержкой. |
| **501** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Сервер либо не распознаёт метод запроса, либо не может его выполнить. В Log Monitoring Classic это может произойти, когда индексированное хранилище логов не включено. |
| **502** | - | Ошибка. Bad Gateway. Это может произойти, если промежуточная система (например, ActiveGate или прокси) столкнулась с проблемой при пересылке запроса. Повторите попытку с экспоненциальной задержкой. |
| **503** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Сервер в настоящее время не может обработать запрос. Это может произойти, когда ActiveGate перегружен. Повторите попытку с экспоненциальной задержкой. |
| **504** | - | Ошибка. Gateway Timeout. Это может произойти из-за проблемы в базовой инфраструктуре, вызывающей задержку обработки запроса. Повторите попытку с экспоненциальной задержкой. |
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
| parameterLocation | string | - Элемент может содержать следующие значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
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

* [API для приёма логов](../../../analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api.md "Stream log data to Dynatrace using API and have Dynatrace transform it into meaningful log messages.")
* [Log Monitoring Classic](../../../analyze-explore-automate/log-monitoring.md "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.")