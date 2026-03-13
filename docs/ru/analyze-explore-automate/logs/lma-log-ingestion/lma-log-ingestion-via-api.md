---
title: Log ingestion API
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api
scraped: 2026-03-06T21:28:26.746272
---

# API приёма логов

# API приёма логов

* Latest Dynatrace
* Overview
* 3-min read
* Updated on Oct 08, 2025

## Приём через API приёма логов

Когда установка OneAgent невозможна, используйте API приёма логов. Например, в бессерверных средах, таких как AWS Fargate, где ведение логов опирается на встроенный маршрутизатор логов, такой как Fluent Bit, который легко интегрируется с API приёма логов Dynatrace. API приёма логов позволяет передавать записи логов в хранилище данных Grail и преобразовывать поток в осмысленные сообщения логов с помощью Dynatrace. Вы можете настроить интеграцию API приёма логов для широкого спектра сценариев использования, включая пользовательские интеграции. Вы можете использовать наши поддерживаемые интеграции для облаков или средств доставки логов, а также для ваших пользовательских сценариев.

![log-api](https://dt-cdn.net/images/log-api-1980-03664b6a2d.png)

Вы можете настроить интеграцию API приёма логов для любых средств доставки логов, которые интегрируются с Dynatrace REST API, например, [OpenTelemetry Collector](../../../ingest-from/opentelemetry/collector.md "Узнайте об OpenTelemetry Collector от Dynatrace."), [Fluentbit](lma-stream-logs-with-fluent-bit.md "Интеграция Fluent Bit для потоковой передачи логов в Dynatrace."), [Fluentd](lma-stream-logs-fluentd-k8s.md "Интеграция Fluentd с Dynatrace для потоковой передачи логов с узлов и подов в Dynatrace."), [Logstash](lma-stream-logs-with-logstash.md "Интеграция Logstash для потоковой передачи логов с узлов и подов в Dynatrace.").

Dynatrace автоматически собирает данные логов и событий из широкого спектра технологий. С помощью API приёма логов вы можете передавать записи логов в систему и позволить Dynatrace преобразовать поток в осмысленные сообщения логов.

![LMA - Generic log ingestion API](https://dt-cdn.net/images/lma-generic-log-ingestion-api-2500-090a5b5c43.png)

API приёма логов позволяет передавать записи логов в систему. Он доступен через [Приём JSON и TXT логов](lma-log-ingestion-via-api/lma-ingest-json-txt-logs.md "Узнайте, как обрабатываются JSON и TXT логи в сглаженном или необработанном режиме.") или через [Приём OTLP логов](../../../ingest-from/opentelemetry/otlp-api/ingest-logs.md "Узнайте, как Dynatrace принимает записи логов OpenTelemetry и какие ограничения применяются.").

* Для Dynatrace SaaS конечная точка приёма логов доступна в вашей среде.
* Если в качестве конечной точки в вашей локальной среде вы выбрали Environment ActiveGate, установите экземпляр ActiveGate: в Dynatrace Hub выберите **ActiveGate** > **Set up**. API приёма логов v2 автоматически включается на ActiveGate.
* Конечная точка включена по умолчанию на всех ваших ActiveGate.
* ActiveGate отвечает за обслуживание конечной точки, сбор данных и пересылку их в Dynatrace пакетами.
* Конечные точки SaaS:

  + `https://{your-environment-id}.live.dynatrace.com/api/v2/logs/ingest`
  + `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp/v1/logs`
* Конечные точки Environment ActiveGate:

  + `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/logs/ingest`
  + `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/otlp/v1/logs`
* Для сред Kubernetes вы можете использовать [Fluentd](lma-stream-logs-fluentd-k8s.md "Интеграция Fluentd с Dynatrace для потоковой передачи логов с узлов и подов в Dynatrace.") или [Fluent Bit](lma-log-ingestion-via-oa/lma-fluent-bit-logs-k8s.md "Интеграция Fluent Bit в Kubernetes для потоковой передачи логов в Dynatrace.") для пересылки логов в Dynatrace.

ActiveGate будет собирать и пытаться автоматически преобразовать любые данные логов, содержащие следующие элементы:

* Содержимое лога
* Временная метка
* Атрибуты ключ-значение

При использовании обработки логов с пользовательским конвейером обработки (OpenPipeline) приём поддерживает все типы данных JSON для значений атрибутов. Для этого требуется версия SaaS 1.295+ при использовании конечной точки SaaS API или версия ActiveGate 1.295+ при использовании конечной точки ActiveGate API. Во всех остальных случаях все принятые значения преобразуются в строковый тип.

### Повторная отправка неудачных запросов

API-клиенты должны повторно выполнять запросы приёма логов, завершившиеся с повторяемыми ошибками.

В документации каждой конечной точки API указано, какие коды ответов допускают повторную попытку. При повторной отправке клиент должен реализовать стратегию экспоненциальной задержки.

## Очередь данных логов

Вы можете настроить свойства очереди данных логов, отредактировав файл `custom.properties` (см. [Свойства и параметры конфигурации ActiveGate](../../../ingest-from/dynatrace-activegate/configuration/configure-activegate.md#generic-ingest "Узнайте, какие свойства ActiveGate вы можете настроить в соответствии с вашими потребностями и требованиями.")) на вашем ActiveGate для установки следующих значений:

```
[generic_ingest]



#disk_queue_path=<custom_path> # defaults to temp folder



#disk_queue_max_size_mb=<limit> # defaults to 300 MB
```

503 Usable space limit reached

API приёма данных логов возвращает ошибку `503 Usable space limit reached`, когда принятые данные логов превышают настроенный размер очереди. Обычно это временная ситуация, возникающая только при пиковых нагрузках. Если эта ошибка сохраняется, увеличьте значение `disk_queue_max_size_mb` в `custom.properties`, чтобы позволить буферизацию пиковых нагрузок приёма логов.

## Пример

В этом примере API-запрос принимает данные логов в формате JSON, которые создадут событие лога с определёнными атрибутами `content`, `status`, `service.name` и `service.namespace`.

API-токен передаётся в заголовке Authorization.

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

Посетите Dynatrace Community для ознакомления с руководствами по устранению неполадок, а также см. [Устранение неполадок Log Management and Analytics](../lma-troubleshooting.md "Исправление проблем, связанных с настройкой и конфигурацией Log Management and Analytics.").

* [Устранение неполадок приёма логов через API - POST ingest logs](https://community.dynatrace.com/t5/Troubleshooting/Troubleshooting-log-Ingestion-via-API-POST-ingest-logs/ta-p/286608)

## Связанные темы

* [Приём JSON и TXT логов](lma-log-ingestion-via-api/lma-ingest-json-txt-logs.md "Узнайте, как обрабатываются JSON и TXT логи в сглаженном или необработанном режиме.")
* [Log Monitoring API v2 - POST ingest logs](../../../dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs.md "Отправляйте пользовательские логи в Dynatrace через Log Monitoring API v2.")
* [Приём OTLP логов](../../../ingest-from/opentelemetry/otlp-api/ingest-logs.md "Узнайте, как Dynatrace принимает записи логов OpenTelemetry и какие ограничения применяются.")
* [API приёма логов OpenTelemetry](../../../dynatrace-api/environment-api/opentelemetry/post-logs.md "Отправляйте логи OpenTelemetry в Dynatrace через API.")
* [Автоматическое обогащение логов](lma-log-ingestion-via-api/lma-log-data-transformation.md "API приёма логов автоматически преобразует данные логов в выходные значения для атрибута loglevel.")
