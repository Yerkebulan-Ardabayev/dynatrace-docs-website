---
title: Передача журналов в Dynatrace с помощью Logstash (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data/stream-logs-to-dynatrace-with-logstash
scraped: 2026-03-04T21:31:54.309034
---

* Объяснение
* 1-минутное чтение

Мониторинг журналов Classic

Для последней версии Dynatrace см. Передача журналов в Dynatrace с помощью Logstash.

Мониторинг журналов Dynatrace использует OneAgent DaemonSet, который включает модуль журнала. Это рекомендуемый способ передачи журналов из узлов и подов в Dynatrace.

Альтернативно вы можете использовать [плагин вывода Logstash для Dynatrace](https://github.com/dynatrace-oss/logstash-output-dynatrace), который является открытым модулем, для передачи журналов.

![Конвейер Logstash в Dynatrace](https://dt-cdn.net/images/logstash-anna-new-eb3c5ac7a3.svg)

## Возможности

Поддерживает отправку журналов в точку входа журналов Dynatrace API v2.

Плагин вывода Logstash для Dynatrace также предоставляет следующие возможности:

* Аутентификация Dynatrace API
* Повтор попыток неудачных запросов из-за временных сетевых условий
* Разделение крупных полезных нагрузок на меньшие пакеты, гарантируя, что каждый пакет соблюдает ограничения API Dynatrace API (версия плагина `0.5.1+`)
* Необязательная сжатие gzip (версия плагина `0.6.1+`)
* Необязательная конфигурация прокси-сервера HTTP (версия плагина `0.5.0+`)
* Необязательно отключите проверку SSL для использования с самоподписанными сертификатами

## Развертывание интеграции

Для инструкций по развертыванию интеграции Logstash см. [документацию на GitHub](https://github.com/dynatrace-oss/logstash-output-dynatrace/blob/main/README.md)

**Пример конфигурации:**

```
output {


dynatrace?


id => "dynatrace_output"


ingest_endpoint_url => "${ACTIVE_GATE_URL}/api/v2/logs/ingest"


api_key => "${API_KEY}"


?


}
```