---
title: Metrics API - POST приём точек данных
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/metric-v2/post-ingest-metrics
scraped: 2026-05-12T11:10:28.149778
---

# Metrics API - POST приём точек данных

# Metrics API - POST приём точек данных

* Справочник
* Опубликовано 21 августа 2020 г.

Отправляет пользовательские точки данных в Dynatrace.

Доступ к принятым точкам данных можно получить через:

* [Data Explorer](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразуйте результаты для получения нужных инсайтов.")
* Запрос [GET metric data points](/managed/dynatrace-api/environment-api/metric-v2/get-data-points "Читайте точки данных одной или нескольких метрик через Metrics v2 API.") Metric v2 API.

Предоставляемые точки данных должны соответствовать [Metrics ingestion protocol](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol "Узнайте, как работает протокол приёма данных для Dynatrace Metrics API."). Регистрировать метрику заранее не нужно. После того как Dynatrace приняла и обработала данные, их можно использовать так же, как любые другие метрики в Dynatrace, например в [charts](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразуйте результаты для получения нужных инсайтов.") или [metric events](/managed/dynatrace-intelligence/anomaly-detection/metric-events "Узнайте о metric events в Dynatrace"). Также можно предоставить [metadata](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/custom-metric-metadata "Предоставление метаданных для пользовательской метрики.") для принятой метрики через Settings API.

Предпочитаете принимать метрики прямо на хосте?

Также можно отправлять точки данных напрямую с хоста, отслеживаемого OneAgent, в модуль OneAgent Extensions Execution Controller (EEC) по защищённому каналу, используя локальный endpoint `http://localhost:<port>/metrics/ingest`, который не требует аутентификации по токену. Порт по умолчанию `14499`. При использовании этого метода к каждой метрике добавляется зарезервированное Dynatrace измерение `dt.entity.host=<host-ID>`.

Можно использовать измерение `dt.process.id=<PID>`, чтобы добавить измерение-идентификатор группы процессов. Когда указан идентификатор группы процессов, к данной метрике добавляется измерение `dt.entity.process_group_instance`. Это работает только при приёме метрик OneAgent через API [`dynatrace_ingest`](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-pipe "Узнайте, как принимать метрики с помощью локальной скриптовой интеграции.").

Подробнее смотрите [OneAgent metric API](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api "Используйте Dynatrace API для получения метрик отслеживаемых сущностей.").

Нельзя принимать метрики с префиксом ключа `dt.`: они зарезервированы для использования Dynatrace.

Запрос принимает payload `text/plain`. Payload ограничен 1 МБ.

Ограничения на количество метрик нет.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/metrics/ingest` |
| POST | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/metrics/ingest` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `metrics.ingest`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| body | string | Точки данных, предоставленные в [line protocol](https://dt-url.net/5d63ic1). Каждая строка представляет одну точку данных. | body | Обязательный |

### Объекты тела запроса

#### Объект `RequestBody`

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **202** | [ValidationResponse](#openapi-definition-ValidationResponse) | Предоставленные точки данных метрики приняты и будут обработаны в фоновом режиме. |
| **400** | [ValidationResponse](#openapi-definition-ValidationResponse) | Некоторые точки данных недействительны. Действительные точки данных приняты и будут обработаны в фоновом режиме. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ValidationResponse`

| Поле | Тип | Описание |
| --- | --- | --- |
| error | [MetricIngestError](#openapi-definition-MetricIngestError) | - |
| linesInvalid | integer | - |
| linesOk | integer | - |
| warnings | [Warnings](#openapi-definition-Warnings) | - |

#### Объект `MetricIngestError`

| Поле | Тип | Описание |
| --- | --- | --- |
| code | integer | - |
| invalidLines | [InvalidLine[]](#openapi-definition-InvalidLine) | - |
| message | string | - |

#### Объект `InvalidLine`

| Поле | Тип | Описание |
| --- | --- | --- |
| error | string | - |
| line | integer | - |

#### Объект `Warnings`

| Поле | Тип | Описание |
| --- | --- | --- |
| changedMetricKeys | [WarningLine[]](#openapi-definition-WarningLine) | - |
| message | string | - |

#### Объект `WarningLine`

| Поле | Тип | Описание |
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

С помощью этой команды `curl` вы примете метрику `cpu.temperature`, назначенную измерению `HOST-06F288EE2A930951`.

```
curl -L -X POST 'https://mySampleEnv.live.dynatrace.com/api/v2/metrics/ingest' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: text/plain' \



--data-raw 'cpu.temperature,dt.entity.host=HOST-06F288EE2A930951,cpu=1 55'
```

## Связанные темы

* [Metric ingestion protocol](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol "Узнайте, как работает протокол приёма данных для Dynatrace Metrics API.")
* [Custom metric metadata](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/custom-metric-metadata "Предоставление метаданных для пользовательской метрики.")