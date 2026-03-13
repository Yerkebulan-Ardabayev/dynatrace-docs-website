---
title: Stream logs to Dynatrace with Logstash (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data/stream-logs-to-dynatrace-with-logstash
scraped: 2026-03-04T21:31:54.309034
---

# Потоковая передача логов в Dynatrace с помощью Logstash (Logs Classic)

# Потоковая передача логов в Dynatrace с помощью Logstash (Logs Classic)

* Classic
* Explanation
* 1-min read
* Updated on Jan 18, 2023

Log Monitoring Classic

Для новейшей версии Dynatrace см. [Потоковая передача логов в Dynatrace с помощью Logstash](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-with-logstash "Integrate Logstash to stream logs from nodes and pods to Dynatrace.").

[Dynatrace Log Monitoring](/docs/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.") использует DaemonSet OneAgent, который включает модуль логирования. Это рекомендуемый способ потоковой передачи логов с узлов и подов в Dynatrace.

В качестве альтернативы можно использовать [выходной плагин Dynatrace для Logstash](https://github.com/dynatrace-oss/logstash-output-dynatrace), который является модулем с открытым исходным кодом, для потоковой передачи логов.

![Logstash pipeline to Dynatrace](https://dt-cdn.net/images/logstash-anna-new-eb3c5ac7a3.svg)

## Возможности

Поддерживает отправку логов в [Dynatrace log ingest API v2](/docs/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Push custom logs to Dynatrace via the Log Monitoring API v2.").

Выходной плагин Dynatrace для Logstash также предоставляет следующие возможности:

* Аутентификация через Dynatrace API
* Повторные попытки при неудачных запросах из-за временных сетевых условий
* Разделение больших полезных нагрузок на меньшие пакеты с соблюдением лимитов Dynatrace API (версия плагина `0.5.1+`)
* Опциональное сжатие gzip (версия плагина `0.6.1+`)
* Опциональная настройка HTTP-прокси (версия плагина `0.5.0+`)
* Опциональное отключение проверки SSL для использования с самоподписанными сертификатами

## Развёртывание интеграции

Инструкции по развёртыванию интеграции Logstash см. в [документации на GitHub](https://github.com/dynatrace-oss/logstash-output-dynatrace/blob/main/README.md)

**Пример конфигурации:**

```
output {



dynatrace {



id => "dynatrace_output"



ingest_endpoint_url => "${ACTIVE_GATE_URL}/api/v2/logs/ingest"



api_key => "${API_KEY}"



}



}
```
