---
title: Google App Engine with Operations suite metrics monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/google-app-engine/app-engine-monitoring
scraped: 2026-03-06T21:34:13.395203
---

# Мониторинг Google App Engine с метриками Operations suite

# Мониторинг Google App Engine с метриками Operations suite

* Последняя версия Dynatrace
* Практическое руководство
* Чтение: 3 мин
* Опубликовано 17 янв. 2022

Интеграция Dynatrace с Google Cloud использует данные, собранные через Google Operation API, для постоянного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все соответствующие данные в дашборды, она также обеспечивает оповещение и отслеживание событий.

## Предварительные требования

[Настройка интеграции](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Настройте мониторинг логов и метрик для сервисов GCP на новом кластере GKE Autopilot.")

## Добавление сервисов и наборов функций (необязательно)

После интеграции Dynatrace автоматически отслеживает ряд предустановленных сервисов Google Cloud и наборов функций (метрик). Помимо них, вы можете добавить дополнительные сервисы или наборы функций для мониторинга. Подробности см. в разделе [Добавление или удаление сервисов](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Настройте мониторинг логов и метрик для сервисов GCP на новом кластере GKE Autopilot.").

Список наборов функций, доступных для этого сервиса, см. в [Таблице метрик](#table).

## Просмотр метрик

После развёртывания интеграции вы можете просматривать метрики от отслеживаемых сервисов в [обозревателе метрик](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Просматривайте метрики с помощью обозревателя метрик Dynatrace."), [Data Explorer](/docs/analyze-explore-automate/explorer "Выполняйте запросы по метрикам и преобразуйте результаты для получения нужных данных.") и на плитках дашбордов.

## Таблица метрик

Для Google App Engine доступны следующие наборы функций.

| Набор функций | Название | Единица измерения | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| gae\_app/default\_metrics | Monitoring Agent API Request Count | Count | agent.googleapis.com/agent/api\_request\_count |
| gae\_app/default\_metrics | Logging Agent Log Entry Count | Count | agent.googleapis.com/agent/log\_entry\_count |
| gae\_app/default\_metrics | Logging Agent Retried Log Entry Writes Count | Count | agent.googleapis.com/agent/log\_entry\_retry\_count |
| gae\_app/default\_metrics | Monitoring Agent Memory Usage | Byte | agent.googleapis.com/agent/memory\_usage |
| gae\_app/default\_metrics | Monitoring Agent Metric Point Count | Count | agent.googleapis.com/agent/monitoring/point\_count |
| gae\_app/default\_metrics | Logging Agent API Request Count | Count | agent.googleapis.com/agent/request\_count |
| gae\_app/default\_metrics | Monitoring Agent Process Labels Size | Byte | agent.googleapis.com/agent/streamspace\_size |
| gae\_app/default\_metrics | Monitoring Agent is Throttling Processes | Count | agent.googleapis.com/agent/streamspace\_size\_throttling |
| gae\_app/default\_metrics | Monitoring/Logging Agent Uptime | Second | agent.googleapis.com/agent/uptime |
| gae\_app/default\_metrics | Autoscaling Metrics Utilization Capacity | Count | appengine.googleapis.com/flex/autoscaler/capacity |
| gae\_app/default\_metrics | Autoscaling Metrics Current Utilization | Count | appengine.googleapis.com/flex/autoscaler/current\_utilization |
| gae\_app/default\_metrics | Connections | Count | appengine.googleapis.com/flex/connections/current |
| gae\_app/default\_metrics | Reserved cores | Count | appengine.googleapis.com/flex/cpu/reserved\_cores |
| gae\_app/default\_metrics | CPU utilization | Percent | appengine.googleapis.com/flex/cpu/utilization |
| gae\_app/default\_metrics | Disk bytes read | Byte | appengine.googleapis.com/flex/disk/read\_bytes\_count |
| gae\_app/default\_metrics | Disk bytes written | Byte | appengine.googleapis.com/flex/disk/write\_bytes\_count |
| gae\_app/default\_metrics | Network bytes received. | Byte | appengine.googleapis.com/flex/network/received\_bytes\_count |
| gae\_app/default\_metrics | Network bytes sent. | Byte | appengine.googleapis.com/flex/network/sent\_bytes\_count |
| gae\_app/default\_metrics | Interception count | Count | appengine.googleapis.com/http/server/dos\_intercept\_count |
| gae\_app/default\_metrics | Quota denial count | Count | appengine.googleapis.com/http/server/quota\_denial\_count |
| gae\_app/default\_metrics | Response count | Count | appengine.googleapis.com/http/server/response\_count |
| gae\_app/default\_metrics | Response latency | MilliSecond | appengine.googleapis.com/http/server/response\_latencies |
| gae\_app/default\_metrics | Response count by style | Count | appengine.googleapis.com/http/server/response\_style\_count |
| gae\_app/default\_metrics | Memcache utilization | Count | appengine.googleapis.com/memcache/centi\_mcu\_count |
| gae\_app/default\_metrics | Hit ratio | Count | appengine.googleapis.com/memcache/hit\_ratio |
| gae\_app/default\_metrics | Memcache operations | Count | appengine.googleapis.com/memcache/operation\_count |
| gae\_app/default\_metrics | Memcache received bytes | Byte | appengine.googleapis.com/memcache/received\_bytes\_count |
| gae\_app/default\_metrics | Memcache sent bytes | Byte | appengine.googleapis.com/memcache/sent\_bytes\_count |
| gae\_app/default\_metrics | Used Cache Size | Byte | appengine.googleapis.com/memcache/used\_cache\_size |
| gae\_app/default\_metrics | Estimated instance count | Count | appengine.googleapis.com/system/billed\_instance\_estimate\_count |
| gae\_app/default\_metrics | CPU megacycles | Count | appengine.googleapis.com/system/cpu/usage |
| gae\_app/default\_metrics | Instance count | Count | appengine.googleapis.com/system/instance\_count |
| gae\_app/default\_metrics | Memory usage | Byte | appengine.googleapis.com/system/memory/usage |
| gae\_app/default\_metrics | Received bytes | Byte | appengine.googleapis.com/system/network/received\_bytes\_count |
| gae\_app/default\_metrics | Sent bytes | Byte | appengine.googleapis.com/system/network/sent\_bytes\_count |
| gae\_instance/default\_metrics | Connections | Count | appengine.googleapis.com/flex/instance/connections/current |
| gae\_instance/default\_metrics | CPU Utilization | Percent | appengine.googleapis.com/flex/instance/cpu/utilization |
| gae\_instance/default\_metrics | Network bytes received | Byte | appengine.googleapis.com/flex/instance/network/received\_bytes\_count |
| gae\_instance/default\_metrics | Network bytes sent | Byte | appengine.googleapis.com/flex/instance/network/sent\_bytes\_count |
| gae\_instance/default\_metrics | Websocket average duration | Second | appengine.googleapis.com/flex/instance/ws/avg\_duration |

## Связанные темы

* [Интеграции с Google Cloud](/docs/ingest-from/google-cloud-platform/gcp-integrations "Настройте и сконфигурируйте Dynatrace в Google Cloud.")
