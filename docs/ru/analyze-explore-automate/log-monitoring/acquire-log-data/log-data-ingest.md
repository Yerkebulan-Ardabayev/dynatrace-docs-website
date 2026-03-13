---
title: Log ingestion API (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data/log-data-ingest
scraped: 2026-02-06T16:28:21.884183
---

# API загрузки журналов (Logs Classic)

# API загрузки журналов (Logs Classic)

* Overview
* 3-min read
* Updated on Jan 22, 2026

Log Monitoring Classic

Для последней версии Dynatrace см. [API загрузки журналов](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api "Stream log data to Dynatrace using API and have Dynatrace transform it into meaningful log messages.").

Dynatrace автоматически собирает данные журналов и событий из широкого спектра технологий. С помощью универсальной загрузки журналов вы можете передавать записи журналов в систему, а Dynatrace преобразует поток в понятные сообщения журналов.

API загрузки журналов позволяет передавать записи журналов в систему. Он доступен через [Log Monitoring API v2 — POST ingest logs](/docs/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Push custom logs to Dynatrace via the Log Monitoring API v2.") для форматов JSON и text или через [конечную точку OTLP](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") для формата OTLP binary protobuf.

* Для Dynatrace SaaS конечная точка загрузки журналов доступна в вашей среде.

* Если вы выбираете Environment ActiveGate в качестве конечной точки в локальной среде, установите экземпляр ActiveGate:

  В Dynatrace Hub выберите **ActiveGate** > **Set up**. Log ingestion API v2 автоматически включается на ActiveGate, который отвечает за обслуживание конечной точки, сбор данных и их пакетную пересылку в Dynatrace.

* Конечные точки SaaS:

  + `https://{your-environment-id}.live.dynatrace.com/api/v2/logs/ingest`
  + `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp/v1/logs`

* Конечные точки Environment ActiveGate:

  + `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/logs/ingest`
  + `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/otlp/v1/logs`

Конечная точка загрузки собирает и пытается автоматически преобразовать любые данные журналов, содержащие следующие элементы JSON:

* Содержимое журнала
* Метка времени
* Атрибуты в формате ключ-значение

Для просмотра всех предопределённых атрибутов ключ-значение, включая поддерживаемые семантические ключи атрибутов, обратитесь к [Log Monitoring API v2 — POST ingest logs](/docs/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Push custom logs to Dynatrace via the Log Monitoring API v2.").

## Очередь данных журналов на Environment ActiveGate

Вы можете настроить свойства очереди данных журналов, отредактировав файл `custom.properties` (см. [Свойства конфигурации и параметры ActiveGate](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#generic-ingest "Learn which ActiveGate properties you can configure based on your needs and requirements.")) на вашем ActiveGate, задав следующие значения:

```
[generic_ingest]



#disk_queue_path=<custom_path> # по умолчанию используется временная папка



#disk_queue_max_size_mb=<limit> # по умолчанию 300 МБ
```

503 Достигнут лимит используемого пространства

API загрузки данных журналов возвращает ошибку `503 Usable space limit reached`, когда загружаемые данные журналов превышают настроенный размер очереди. Как правило, это временная ситуация, возникающая только во время пиковых нагрузок. Если эта ошибка сохраняется, увеличьте значение `disk_queue_max_size_mb` в `custom.properties`, чтобы позволить пиковым загрузкам журналов помещаться в очередь.

## Пример

В этом примере API-запрос загружает данные журнала, в результате чего будет создано событие журнала с заданными атрибутами `content`, `status`, `service.name` и `service.namespace`.

Токен API передаётся в заголовке Authorization.

Ответ содержит код ответа `204`.

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

Посетите сообщество Dynatrace для получения руководств по устранению неполадок, а также см. [Устранение неполадок Log Monitoring (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/lmc-troubleshooting "Fix issues related to the setup and configuration of Log Monitoring Classic.").

* [Устранение неполадок при загрузке журналов через API — POST ingest logs](https://community.dynatrace.com/t5/Troubleshooting/Troubleshooting-log-Ingestion-via-API-POST-ingest-logs/ta-p/286608)

## Связанные темы

* [Log Monitoring API v2 — POST ingest logs](/docs/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Push custom logs to Dynatrace via the Log Monitoring API v2.")
