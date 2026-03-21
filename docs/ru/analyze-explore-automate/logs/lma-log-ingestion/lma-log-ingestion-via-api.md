---
title: Прием журналов API
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api
scraped: 2026-03-06T21:28:26.746272
---

* Последние Dynatrace
* 3 мин. на чтение

## Прием через Прием журналов API

Если невозможно установить OneAgent, используйте Прием журналов API. Например, в бессерверных средах, таких как AWS Fargate, где ведение журналов полагается на встроенный маршрутизатор журналов, такой как Fluent Bit, который можно легко интегрировать с Dynatrace Приемом журналов API. Прием журналов API позволяет передавать записи журналов в озеро данных Grail, и Dynatrace преобразует поток в значимые сообщения журналов. Вы можете настроить интеграцию Приема журналов API для широкого спектра вариантов использования, а также включать пользовательские интеграции. Вы можете использовать наши поддерживаемые интеграции для облаков или сборщиков журналов, а также для ваших пользовательских сценариев.

![log-api](https://dt-cdn.net/images/log-api-1980-03664b6a2d.png)

Вы можете настроить интеграцию Приема журналов API для любых сборщиков журналов, которые интегрируются с Dynatrace REST API, например, [OpenTelemetry Collector](../../../ingest-from/opentelemetry/collector.md "Узнайте о Dynatrace OTel Collector."), [Fluentbit](lma-stream-logs-with-fluent-bit.md "Интегрируйте Fluent Bit для потоковой передачи журналов в Dynatrace."), [Fluentd](lma-stream-logs-fluentd-k8s.md "Интегрируйте Fluentd с Dynatrace для потоковой передачи журналов с узлов и подов в Dynatrace."), [Logstash](lma-stream-logs-with-logstash.md "Интегрируйте Logstash для потоковой передачи журналов с узлов и подов в Dynatrace.").

Dynatrace автоматически собирает данные журналов и событий из широкого спектра технологий. С помощью Приема журналов API вы можете передавать записи журналов в систему и позволить Dynatrace преобразовать поток в значимые сообщения журналов.

![LMA - Generic log ingestion API](https://dt-cdn.net/images/lma-generic-log-ingestion-api-2500-090a5b5c43.png)

Прием журналов API позволяет передавать записи журналов в систему. Он доступен через [Ingest JSON и TXT logs](lma-log-ingestion-via-api/lma-ingest-json-txt-logs.md "Узнайте, как обрабатываются JSON и TXT logs, в сжатом или необработанном режиме.") или через [Ingest OTLP logs](../../../ingest-from/opentelemetry/otlp-api/ingest-logs.md "Узнайте, как Dynatrace принимает записи журналов OpenTelemetry и какие ограничения применяются.").

* Для Dynatrace SaaS конечная точка приема журналов доступна в вашей среде.
* Если Environment ActiveGate является вашим выбором для конечной точки в вашей локальной среде, установите экземпляр ActiveGate: В Dynatrace Hub, выберите **ActiveGate** > **Настройка**. Прием журналов API v2 автоматически включен на ActiveGate.
* Конечная точка включена по умолчанию на всех ваших ActiveGates.
* ActiveGate отвечает за обслуживание конечной точки, сбор данных и их пересылку в Dynatrace пакетами.
* Конечные точки SaaS:

  + `https://{your-environment-id}.live.dynatrace.com/api/v2/logs/ingest`
  + `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp/v1/logs`
* Конечные точки Environment ActiveGate:

  + `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/logs/ingest`
  + `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/otlp/v1/logs`
* Для Kubernetes сред вы можете использовать [Fluentd](lma-stream-logs-fluentd-k8s.md "Интегрируйте Fluentd с Dynatrace для потоковой передачи журналов с узлов и подов в Dynatrace.") или [Fluent Bit](lma-log-ingestion-via-oa/lma-fluent-bit-logs-k8s.md "Интегрируйте Fluent Bit в Kubernetes для потоковой передачи журналов в Dynatrace.") для пересылки журналов в Dynatrace.

ActiveGate будет собирать и пытаться автоматически преобразовать любые данные журналов, содержащие следующие элементы:

* Содержимое журнала
* Временная метка
* Атрибуты "Ключ-Значение"

При использовании обработки журналов с пользовательским конвейером обработки (OpenPipeline), прием поддерживает все типы данных JSON для значений атрибутов. Это требует версии SaaS 1.295+ при использовании конечной точки SaaS API или версии ActiveGate 1.295+ при использовании конечной точки ActiveGate API. Во всех остальных случаях все принятые значения преобразуются в строковый тип.

### Повторные попытки неудачных запросов

Клиенты API должны повторно выполнять запросы на прием журналов, которые не удались из-за ошибок, подлежащих повторной попытке.

Документация к каждой конечной точке API указывает, какие коды ответа подлежат повторной попытке. При повторной попытке клиент реализует стратегию экспоненциальной отсрочки.

## Очередь данных журналов

Вы можете настроить свойства очереди данных журналов, отредактировав файл `custom.properties` (см. [Свойства и параметры конфигурации ActiveGate](../../../ingest-from/dynatrace-activegate/configuration/configure-activegate.md#generic-ingest "Узнайте, какие свойства ActiveGate вы можете настроить в соответствии с вашими потребностями и требованиями.")) на вашем ActiveGate, чтобы установить следующие значения:

```
[generic_ingest]

#disk_queue_path=<custom_path> # по умолчанию папка temp

#disk_queue_max_size_mb=<limit> # по умолчанию 300 МБ
```

503 Достигнут предел доступного дискового пространства

Прием журналов API возвращает ошибку `503 Достигнут предел доступного дискового пространства`, когда принятые данные журналов превышают настроенный размер очереди. Обычно это временная ситуация, которая возникает только во время пиков. Если эта ошибка сохраняется, увеличьте значение `disk_queue_max_size_mb` в `custom.properties`, чтобы разрешить пики приема журналов быть помещенными в очередь.

## Пример

В этом примере запрос API принимает данные журналов JSON, которые создадут событие журнала с определенными атрибутами журнала `content`, `status`, `service.name` и `service.namespace`.

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

Посетите Сообщество Dynatrace для получения руководств по устранению неполадок, а также ознакомьтесь с [Устранение неполадок управления журналами и аналитики](../lma-troubleshooting.md "Устранение проблем, связанных с настройкой и конфигурацией управления журналами и аналитики.").

* [Устранение неполадок приема журналов через API - POST ingest logs](https://community.dynatrace.com/t5/Troubleshooting/Troubleshooting-log-Ingestion-via-API-POST-ingest-logs/ta-p/286608)

## Связанные темы

* [Ingest JSON и TXT logs](lma-log-ingestion-via-api/lma-ingest-json-txt-logs.md "Узнайте, как обрабатываются JSON и TXT logs, в сжатом или необработанном режиме.")
* [Log Monitoring API v2 - POST ingest logs](../../../dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs.md "Отправляйте пользовательские журналы в Dynatrace через Log Monitoring API v2.")
* [Ingest OTLP logs](../../../ingest-from/opentelemetry/otlp-api/ingest-logs.md "Узнайте, как Dynatrace принимает записи журналов OpenTelemetry и какие ограничения применяются.")
* [OpenTelemetry logs ingest API](../../../dynatrace-api/environment-api/opentelemetry/post-logs.md "Отправляйте журналы OpenTelemetry в Dynatrace через API.")
* [Автоматическое обогащение журналов](lma-log-ingestion-via-api/lma-log-data-transformation.md "Прием журналов API автоматически преобразует данные журналов в выходные значения для атрибута loglevel.")