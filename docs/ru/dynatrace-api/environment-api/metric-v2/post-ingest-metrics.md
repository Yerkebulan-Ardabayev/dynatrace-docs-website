---
title: Metrics API - POST ingest data points
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/metric-v2/post-ingest-metrics
scraped: 2026-03-05T21:37:11.920249
---

# Metrics API — POST отправка точек данных


Отправляет пользовательские точки данных в Dynatrace.

Вы можете получить доступ к принятым точкам данных через:

* Data Explorer
* Запрос GET точек данных метрик API Metric v2.

Предоставленные точки данных должны соответствовать протоколу приёма метрик. Вам не нужно предварительно регистрировать метрику. После того как Dynatrace примет и обработает данные, вы сможете использовать их так же, как любые другие метрики в Dynatrace, например, в графиках или событиях метрик. Вы также можете предоставить метаданные для принятой метрики через Settings API.

Предпочитаете принимать метрики прямо на хосте?

Вы также можете отправлять точки данных напрямую с хоста, отслеживаемого OneAgent, в модуль Extensions Execution Controller (EEC) OneAgent по защищённому каналу, используя локальный эндпоинт `http://localhost:<port>/metrics/ingest`, не требующий токенной аутентификации. Порт по умолчанию — `14499`. При использовании этого метода к каждой метрике добавляется зарезервированное измерение Dynatrace `dt.entity.host=<host-ID>`.

Вы можете использовать измерение `dt.process.id=<PID>` для добавления идентификатора группы процессов. Когда идентификатор группы процессов предоставлен, к данной метрике будет добавлено измерение `dt.entity.process_group_instance`. Это работает только при приёме метрик OneAgent через API `dynatrace_ingest`.

Подробнее см. в разделе OneAgent metric API.

Нельзя принимать метрики с префиксом ключа `dt.` — он зарезервирован для использования Dynatrace.

Запрос принимает полезную нагрузку в формате `text/plain`. Размер полезной нагрузки ограничен 1 МБ.

Ограничение на количество метрик отсутствует.

|  |  |  |
| --- | --- | --- |
| POST | Managed | `https://{your-environment-id}.live.dynatrace.com/api/v2/metrics/ingest` |
| POST | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/metrics/ingest` |

## Аутентификация

Для выполнения этого запроса необходим токен доступа с областью действия `metrics.ingest`.

Чтобы узнать, как получить и использовать его, см. Токены и аутентификация.

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| body | string | Точки данных, предоставленные в [линейном протоколе](https://dt-url.net/5d63ic1). Каждая строка представляет одну точку данных. | body | Обязательный |

### Объекты тела запроса

#### Объект `RequestBody`

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **202** | [ValidationResponse](#openapi-definition-ValidationResponse) | Предоставленные точки данных метрик приняты и будут обработаны в фоновом режиме. |
| **400** | [ValidationResponse](#openapi-definition-ValidationResponse) | Некоторые точки данных недействительны. Действительные точки данных приняты и будут обработаны в фоновом режиме. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ValidationResponse`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [MetricIngestError](#openapi-definition-MetricIngestError) | - |
| linesInvalid | integer | - |
| linesOk | integer | - |
| warnings | [Warnings](#openapi-definition-Warnings) | - |

#### Объект `MetricIngestError`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | - |
| invalidLines | [InvalidLine[]](#openapi-definition-InvalidLine) | - |
| message | string | - |

#### Объект `InvalidLine`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | string | - |
| line | integer | - |

#### Объект `Warnings`

| Элемент | Тип | Описание |
| --- | --- | --- |
| changedMetricKeys | [WarningLine[]](#openapi-definition-WarningLine) | - |
| message | string | - |

#### Объект `WarningLine`

| Элемент | Тип | Описание |
| --- | --- | --- |
| line | integer | - |
| warning | string | - |

### JSON-модели тела ответа

```
{


"error": {


"code": 1,


"invalidLines": [


{


"error": "string",


"line": 1


}


],


"message": "string"


},


"linesInvalid": 1,


"linesOk": 1,


"warnings": {


"changedMetricKeys": [


{


"line": 1,


"warning": "string"


}


],


"message": "string"


}


}
```

## Пример

С помощью этой команды `curl` вы отправите метрику `cpu.temperature`, назначенную измерению `HOST-06F288EE2A930951`.

```
curl -L -X POST 'https://mySampleEnv.live.dynatrace.com/api/v2/metrics/ingest' \


-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \


-H 'Content-Type: text/plain' \


--data-raw 'cpu.temperature,dt.entity.host=HOST-06F288EE2A930951,cpu=1 55'
```

## Связанные темы

* Протокол приёма метрик
* Метаданные пользовательских метрик
