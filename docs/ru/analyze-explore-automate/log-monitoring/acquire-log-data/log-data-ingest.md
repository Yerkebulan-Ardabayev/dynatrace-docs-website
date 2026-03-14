---
title: Ввод журналов API (Классические журналы)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data/log-data-ingest
scraped: 2026-02-06T16:28:21.884183
---

# Ввод журналов API (Классические журналы)

# Ввод журналов API (Классические журналы)

* Обзор
* 3-минутное чтение
* Обновлено 22 января 2026 г.

Мониторинг журналов Classic

Для самой новой версии Dynatrace см. [Ввод журналов API](../../logs/lma-log-ingestion/lma-log-ingestion-via-api.md "Передайте журнальные данные в Dynatrace с помощью API и позвольте Dynatrace преобразовать их в осмысленные сообщения журнала.").

Dynatrace автоматически собирает журнальные и событийные данные из широкого спектра технологий. С помощью общего ввода журналов вы можете передавать журнальные записи в систему и позволять Dynatrace преобразовывать поток в осмысленные сообщения журнала.

Ввод журналов API позволяет передавать журнальные записи в систему. Он доступен через [Мониторинг журналов API v2 - POST ввод журналов](../../../dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs.md "Передайте пользовательские журналы в Dynatrace через Мониторинг журналов API v2.") для JSON и текстового формата или через [OTLP-конечную точку](../../../ingest-from/opentelemetry/otlp-api.md "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") для бинарного формата protobuf OTLP.

* Для Dynatrace SaaS конечная точка ввода журналов доступна в вашей среде.

* Если Environment ActiveGate является вашим выбором в качестве конечной точки в вашей локальной среде, установите экземпляр ActiveGate:

  В Dynatrace Hub выберите **ActiveGate** > **Настройка**. Ввод журналов API v2 автоматически активируется на ActiveGate, который отвечает за обслуживание конечной точки, сбор данных и их передачу в Dynatrace пакетами.

* Конечные точки SaaS:

  + `https://{your-environment-id}.live.dynatrace.com/api/v2/logs/ingest`
  + `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp/v1/logs`

* Конечные точки Environment ActiveGate:

  + `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/logs/ingest`
  + `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/otlp/v1/logs`

Конечная точка ввода будет собирать и пытаться автоматически преобразовать любые журнальные данные, содержащие следующие элементы JSON:

* Содержимое журнала
* Метка времени
* Атрибуты Key-Values

Чтобы просмотреть все предопределенные атрибуты Key-Values, такие как поддерживаемые семантические ключи атрибутов, проверьте [Мониторинг журналов API v2 - POST ввод журналов](../../../dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs.md "Передайте пользовательские журналы в Dynatrace через Мониторинг журналов API v2.").

## Очередь журнальных данных на Environment ActiveGate

Вы можете настроить свойства очереди журнальных данных, редактируя файл `custom.properties` (см. [Свойства и параметры конфигурации ActiveGate](../../../ingest-from/dynatrace-activegate/configuration/configure-activegate.md#generic-ingest "Узнайте, какие свойства ActiveGate можно настроить в соответствии с вашими потребностями и требованиями.")) на вашем ActiveGate, чтобы задать следующие значения:

```
[generic_ingest]



#disk_queue_path=<custom_path> # по умолчанию временная папка



#disk_queue_max_size_mb=<limit> # по умолчанию 300 МБ
```

503 Достигнут предел использования пространства

Конечная точка ввода журнальных данных API возвращает ошибку `503 Достигнут предел использования пространства`, когда принятые журнальные данные превышают настроенный размер очереди. Обычно это временная ситуация, которая возникает только во время пиков. Если эта ошибка сохраняется, увеличьте значение `disk_queue_max_size_mb` в `custom.properties`, чтобы позволить очереди журнальных данных обрабатывать пики.

## Пример

В этом примере запрос API передает журнальные данные, которые создадут событие журнала с определенными атрибутами журнала `content`, `status`, `service.name` и `service.namespace`.

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



"content": "Исключение: Пользовательский журнал ошибок, переданный через Ввод журналов API",



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

#### Содержимое ответа

```
Успех
```

#### Код ответа

`204`

## Устранение неполадок

Посетите сообщество Dynatrace для руководств по устранению неполадок, а также см. [Устранение неполадок Мониторинга журналов (Классические журналы)](../lmc-troubleshooting.md "Исправьте проблемы, связанные с настройкой и конфигурацией Мониторинга журналов Classic.").

* [Устранение неполадок ввода журналов через API - POST ввод журналов](https://community.dynatrace.com/t5/Troubleshooting/Troubleshooting-log-Ingestion-via-API-POST-ingest-logs/ta-p/286608)

## Связанные темы

* [Мониторинг журналов API v2 - POST ввод журналов](../../../dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs.md "Передайте пользовательские журналы в Dynatrace через Мониторинг журналов API v2.")