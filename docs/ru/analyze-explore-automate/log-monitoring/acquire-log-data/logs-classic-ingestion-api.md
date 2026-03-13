---
title: Log ingestion API (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api
scraped: 2026-03-06T21:16:13.984280
---

# Log ingestion API (Logs Classic)

# Log ingestion API (Logs Classic)

* Classic
* Overview
* 3-min read
* Updated on Jan 30, 2026

Log Monitoring Classic

Для новейшей версии Dynatrace см. [Log ingestion API](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api "Передавайте данные логов в Dynatrace через API и позвольте Dynatrace преобразовывать их в понятные сообщения логов.").

Dynatrace автоматически собирает данные логов и событий из широкого спектра технологий. С помощью Log ingestion API можно передавать записи логов в систему, а Dynatrace будет преобразовывать поток в понятные сообщения логов.

Log ingestion API позволяет передавать записи логов в систему. Он доступен через [Ingest JSON and TXT logs (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api/log-classic-ingest-json-txt-logs "Узнайте, как обрабатываются JSON и TXT логи.") или через [Ingest OTLP logs](/docs/ingest-from/opentelemetry/otlp-api/ingest-logs "Узнайте, как Dynatrace принимает записи логов OpenTelemetry и какие ограничения применяются.").

* Для Dynatrace SaaS конечная точка Log ingestion доступна в вашей среде.

* Если в качестве конечной точки в локальной среде выбран Environment ActiveGate, установите экземпляр ActiveGate:

В Dynatrace Hub выберите **ActiveGate** > **Set up**.

Log ingestion API v2 автоматически включается на ActiveGate. ActiveGate отвечает за обслуживание конечной точки, сбор данных и их пакетную пересылку в Dynatrace.

* Конечные точки SaaS:

  + `https://{your-environment-id}.live.dynatrace.com/api/v2/logs/ingest`
  + `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp/v1/logs`

* Конечные точки Environment ActiveGate:

  + `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/logs/ingest`
  + `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/otlp/v1/logs`

## Очередь данных логов на Environment ActiveGate

Свойства очереди данных логов можно настроить, отредактировав файл `custom.properties` (см. [Свойства конфигурации и параметры ActiveGate](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#generic-ingest "Узнайте, какие свойства ActiveGate можно настроить в соответствии с вашими потребностями и требованиями.")) на вашем ActiveGate, задав следующие значения:

```
[generic_ingest]



#disk_queue_path=<custom_path> # defaults to temp folder



#disk_queue_max_size_mb=<limit> # defaults to 300 MB
```

503 Usable space limit reached

API приёма данных логов возвращает ошибку `503 Usable space limit reached`, когда принятые данные логов превышают настроенный размер очереди. Как правило, это временная ситуация, возникающая только при пиковых нагрузках. Если эта ошибка не исчезает, увеличьте значение `disk_queue_max_size_mb` в `custom.properties`, чтобы обеспечить возможность постановки в очередь пиков приёма логов.

## Пример

В данном примере API-запрос принимает данные логов, которые создадут событие лога с заданными атрибутами `content`, `status`, `service.name` и `service.namespace`.

API-токен передаётся в заголовке Authorization.

Ответ содержит код `204`.

#### Curl

```
curl -X POST \



https://environment.activegate.domain.com:9999/e/abc123a/api/v2/logs/ingest \



-H 'Content-Type: application/json; charset=utf-8' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-d '[



{



"content": "Exception: Custom error log sent via Log ingestion API",



"status": "error",



"service.name": "log-monitoring-tenant",



"service.namespace": "dev-stage-cluster"



}



]'
```

#### URL запроса

```
https://environment.activegate.domain.com:9999/e/abc123a/api/v2/logs/ingest
```

#### Содержимое ответа

```
Success
```

#### Код ответа

`204`

## Устранение неполадок

Посетите Dynatrace Community для получения руководств по устранению неполадок, а также см. [Устранение неполадок Log Monitoring (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/lmc-troubleshooting "Исправляйте проблемы, связанные с настройкой и конфигурацией Log Monitoring Classic.").

* [Troubleshooting log Ingestion via API - POST ingest logs](https://community.dynatrace.com/t5/Troubleshooting/Troubleshooting-log-Ingestion-via-API-POST-ingest-logs/ta-p/286608)

## Связанные темы

* [Log Monitoring API v2 - POST ingest logs](/docs/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Отправляйте пользовательские логи в Dynatrace через Log Monitoring API v2.")
* [Ingest OTLP logs](/docs/ingest-from/opentelemetry/otlp-api/ingest-logs "Узнайте, как Dynatrace принимает записи логов OpenTelemetry и какие ограничения применяются.")
