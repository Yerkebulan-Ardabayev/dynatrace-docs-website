---
title: Приём журналов API (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api
scraped: 2026-03-06T21:16:13.984280
---

* 3-минутное чтение

Мониторинг журналов Classic

Для самой новой версии Dynatrace см. Приём журналов API.

Dynatrace автоматически собирает данные журналов и событий из широкого спектра технологий. С помощью приёма журналов API вы можете передавать записи журнала в систему и преобразовывать поток в осмысленные сообщения журнала.

Приём журналов API позволяет передавать записи журнала в систему. Он доступен через Приём JSON и журналов TXT (Logs Classic) или через Приём журналов OTLP.

* Для Dynatrace конечная точка приёма журналов доступна в вашей среде.

* Если Environment ActiveGate является вашим выбором для конечной точки в вашей локальной среде, установите экземпляр ActiveGate:

В Dynatrace Hub выберите **ActiveGate** > **Настройка**.

Приём журналов API v2 автоматически включен на ActiveGate. ActiveGate отвечает за обслуживание конечной точки, сбор данных и передачу их в Dynatrace пакетами.

* Конечные точк:

  + `https://{your-environment-id}.live.dynatrace.com/api/v2/logs/ingest`
  + `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp/v1/logs`

* Конечные точки Environment ActiveGate:

  + `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/logs/ingest`
  + `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/otlp/v1/logs`

## Очередь данных журнала на Environment ActiveGate

Вы можете настроить свойства очереди данных журнала, редактируя файл `custom.properties` (см. Свойства конфигурации и параметры ActiveGate) на вашем ActiveGate, чтобы задать следующие значения:

```
[generic_ingest]


#disk_queue_path=<custom_path> # по умолчанию временная папка


#disk_queue_max_size_mb=<limit> # по умолчанию 300 МБ
```

503 Достигнут предел использования пространства

Приём данных журнала API возвращает ошибку `503 Достигнут предел использования пространства`, когда принятые данные журнала превышают настроенный размер очереди. Обычно это временная ситуация, которая возникает только во время пиков. Если эта ошибка сохраняется, увеличьте значение `disk_queue_max_size_mb` в `custom.properties`, чтобы разрешить очереди приёма журналов во время пиков.

## Пример

В этом примере запрос API принимает данные журнала, которые создадут событие журнала с определёнными атрибутами журнала `content`, `status`, `service.name` и `service.namespace`.

Токен API передается в заголовке Authorization.

Ответ содержит код ответа `204`.

#### Curl

```
curl -X POST \


https://environment.activegate.domain.com:9999/e/abc123a/api/v2/logs/ingest \


-H 'Content-Type: application/json; charset=utf-8' \


-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \


-d '[


{


"content": "Исключение: пользовательский журнал ошибок, переданный через приём журналов API",


"status": "ошибка",


"service.name": "log-monitoring-tenant",


"service.namespace": "dev-stage-cluster"


}


]'
```

#### URL запроса

```
https://environment.activegate.domain.com:9999/e/abc123a/api/v2/logs/ingest
```

#### Содержание ответа

```
Успех
```

#### Код ответа

`204`

## Устранение неполадок

Посетите сообщество Dynatrace, чтобы получить руководства по устранению неполадок, а также см. Устранение неполадок мониторинга журналов (Logs Classic).

* [Устранение неполадок приёма журналов через API - POST принять журналы](https://community.dynatrace.com/t5/Troubleshooting/Troubleshooting-log-Ingestion-via-API-POST-ingest-logs/ta-p/286608)

## Связанные темы

* Мониторинг журналов API v2 - POST принять журналы
* Приём журналов OTLP