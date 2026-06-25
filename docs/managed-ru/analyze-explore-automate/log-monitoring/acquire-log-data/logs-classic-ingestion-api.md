---
title: API приёма журналов (Logs Classic)
source: https://docs.dynatrace.com/managed/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api
scraped: 2026-05-12T11:13:33.224380
---

# API приёма журналов (Logs Classic)

# API приёма журналов (Logs Classic)

* Обзор
* Чтение: 3 мин
* Обновлено 30 января 2026 г.

Log Monitoring Classic

Dynatrace автоматически собирает данные журналов и событий из широкого спектра технологий. С помощью API приёма журналов можно передавать записи журналов в систему и позволять Dynatrace преобразовывать поток в осмысленные сообщения журналов.

API приёма журналов позволяет передавать записи журналов в систему. Доступен через [Приём JSON и TXT журналов (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api/log-classic-ingest-json-txt-logs "Узнайте, как обрабатываются JSON и TXT журналы.") или через [Приём OTLP журналов](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs "Узнайте, как Dynatrace принимает записи журналов OpenTelemetry и какие ограничения применяются.").

* Для Dynatrace Managed эндпоинт приёма журналов доступен на узлах начиная с версии Dynatrace 1.292.

* Если вы выбираете Environment ActiveGate в качестве эндпоинта в локальной среде или ваш Managed кластер имеет версию ниже 1.292, установите экземпляр ActiveGate:

1. Перейдите в **Deploy Dynatrace**.
2. Выберите **Install ActiveGate**.

Log ingestion API v2 автоматически включается на ActiveGate. ActiveGate отвечает за обслуживание эндпоинта, сбор данных и их пакетную пересылку в Dynatrace.

* Эндпоинты Managed (Dynatrace версии 1.292+):

  + `https://{your-domain}/e/{your-environment-id}/api/v2/logs/ingest`
  + `https://{your-domain}/e/{your-environment-id}/api/v2/otlp/v1/logs`

* Эндпоинты Environment ActiveGate:

  + `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/logs/ingest`
  + `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/otlp/v1/logs`

## Очередь данных журналов на Environment ActiveGate

Свойства очереди данных журналов можно настроить, отредактировав файл `custom.properties` (см. [Свойства и параметры конфигурации ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#generic-ingest "Узнайте, какие свойства ActiveGate можно настроить в зависимости от ваших нужд.")) на ActiveGate:

```
[generic_ingest]



#disk_queue_path=<custom_path> # defaults to temp folder



#disk_queue_max_size_mb=<limit> # defaults to 300 MB
```

503 Usable space limit reached

API приёма данных журналов возвращает ошибку `503 Usable space limit reached`, когда принятые данные журналов превышают настроенный размер очереди. Как правило, это временная ситуация, возникающая только во время всплесков. Если ошибка сохраняется, увеличьте значение `disk_queue_max_size_mb` в `custom.properties`.

## Пример

В этом примере API-запрос принимает данные журнала, которые создадут событие журнала с атрибутами `content`, `status`, `service.name` и `service.namespace`.

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

Посетите сообщество Dynatrace, а также ознакомьтесь с разделом [Устранение неполадок Log Monitoring (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/lmc-troubleshooting "Устраните проблемы, связанные с настройкой и конфигурацией Log Monitoring Classic.").

* [Troubleshooting log Ingestion via API - POST ingest logs](https://community.dynatrace.com/t5/Troubleshooting/Troubleshooting-log-Ingestion-via-API-POST-ingest-logs/ta-p/286608)

## Связанные темы

* [Log Monitoring API v2 — POST ingest logs](/managed/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Отправляйте пользовательские журналы в Dynatrace через Log Monitoring API v2.")
* [Приём OTLP журналов](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs "Узнайте, как Dynatrace принимает записи журналов OpenTelemetry.")