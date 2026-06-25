---
title: Мониторинг Google App Engine с метриками Operations suite
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/google-app-engine/app-engine-monitoring
scraped: 2026-05-12T11:50:23.325781
---

# Мониторинг Google App Engine с метриками Operations suite

# Мониторинг Google App Engine с метриками Operations suite

* Практическое руководство
* Чтение: 3 мин
* Опубликовано 17 января 2022 г.

Интеграция Dynatrace с Google Cloud использует данные, собранные через Google Operation API, для постоянного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все релевантные данные в дашбордах, она также обеспечивает оповещения и отслеживание событий.

## Предварительные условия

[Настройка интеграции](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.")

## Добавление сервисов и наборов функций Необязательно

После интеграции Dynatrace автоматически отслеживает ряд предустановленных сервисов и наборов функций (метрик) Google Cloud. Помимо них, в мониторинг можно добавить дополнительные сервисы или наборы функций. Подробнее см. [Добавление или удаление сервисов](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.").

Список наборов функций, доступных для этого сервиса, см. в разделе [Таблица метрик](#table).

## Просмотр метрик

После развёртывания интеграции метрики отслеживаемых сервисов можно просматривать в [Браузере метрик](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Просматривайте метрики с помощью браузера метрик Dynatrace."), [Data Explorer](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразовывайте результаты для получения нужных аналитических данных.") и на плитках ваших дашбордов.

## Таблица метрик

Для Google App Engine доступны следующие наборы функций.

| Набор функций | Имя | Единица измерения | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| gae\_app/default\_metrics | Monitoring Agent API Request Count | Количество | agent.googleapis.com/agent/api\_request\_count |
| gae\_app/default\_metrics | Logging Agent Log Entry Count | Количество | agent.googleapis.com/agent/log\_entry\_count |
| gae\_app/default\_metrics | Logging Agent Retried Log Entry Writes Count | Количество | agent.googleapis.com/agent/log\_entry\_retry\_count |
| gae\_app/default\_metrics | Monitoring Agent Memory Usage | Байт | agent.googleapis.com/agent/memory\_usage |
| gae\_app/default\_metrics | Monitoring Agent Metric Point Count | Количество | agent.googleapis.com/agent/monitoring/point\_count |
| gae\_app/default\_metrics | Logging Agent API Request Count | Количество | agent.googleapis.com/agent/request\_count |
| gae\_app/default\_metrics | Monitoring Agent Process Labels Size | Байт | agent.googleapis.com/agent/streamspace\_size |
| gae\_app/default\_metrics | Monitoring Agent is Throttling Processes | Количество | agent.googleapis.com/agent/streamspace\_size\_throttling |
| gae\_app/default\_metrics | Monitoring/Logging Agent Uptime | Секунда | agent.googleapis.com/agent/uptime |
| gae\_app/default\_metrics | Autoscaling Metrics Utilization Capacity | Количество | appengine.googleapis.com/flex/autoscaler/capacity |
| gae\_app/default\_metrics | Autoscaling Metrics Current Utilization | Количество | appengine.googleapis.com/flex/autoscaler/current\_utilization |
| gae\_app/default\_metrics | Connections | Количество | appengine.googleapis.com/flex/connections/current |
| gae\_app/default\_metrics | Reserved cores | Количество | appengine.googleapis.com/flex/cpu/reserved\_cores |
| gae\_app/default\_metrics | CPU utilization | Процент | appengine.googleapis.com/flex/cpu/utilization |
| gae\_app/default\_metrics | Disk bytes read | Байт | appengine.googleapis.com/flex/disk/read\_bytes\_count |
| gae\_app/default\_metrics | Disk bytes written | Байт | appengine.googleapis.com/flex/disk/write\_bytes\_count |
| gae\_app/default\_metrics | Network bytes received. | Байт | appengine.googleapis.com/flex/network/received\_bytes\_count |
| gae\_app/default\_metrics | Network bytes sent. | Байт | appengine.googleapis.com/flex/network/sent\_bytes\_count |
| gae\_app/default\_metrics | Interception count | Количество | appengine.googleapis.com/http/server/dos\_intercept\_count |
| gae\_app/default\_metrics | Quota denial count | Количество | appengine.googleapis.com/http/server/quota\_denial\_count |
| gae\_app/default\_metrics | Response count | Количество | appengine.googleapis.com/http/server/response\_count |
| gae\_app/default\_metrics | Response latency | Миллисекунда | appengine.googleapis.com/http/server/response\_latencies |
| gae\_app/default\_metrics | Response count by style | Количество | appengine.googleapis.com/http/server/response\_style\_count |
| gae\_app/default\_metrics | Memcache utilization | Количество | appengine.googleapis.com/memcache/centi\_mcu\_count |
| gae\_app/default\_metrics | Hit ratio | Количество | appengine.googleapis.com/memcache/hit\_ratio |
| gae\_app/default\_metrics | Memcache operations | Количество | appengine.googleapis.com/memcache/operation\_count |
| gae\_app/default\_metrics | Memcache received bytes | Байт | appengine.googleapis.com/memcache/received\_bytes\_count |
| gae\_app/default\_metrics | Memcache sent bytes | Байт | appengine.googleapis.com/memcache/sent\_bytes\_count |
| gae\_app/default\_metrics | Used Cache Size | Байт | appengine.googleapis.com/memcache/used\_cache\_size |
| gae\_app/default\_metrics | Estimated instance count | Количество | appengine.googleapis.com/system/billed\_instance\_estimate\_count |
| gae\_app/default\_metrics | CPU megacycles | Количество | appengine.googleapis.com/system/cpu/usage |
| gae\_app/default\_metrics | Instance count | Количество | appengine.googleapis.com/system/instance\_count |
| gae\_app/default\_metrics | Memory usage | Байт | appengine.googleapis.com/system/memory/usage |
| gae\_app/default\_metrics | Received bytes | Байт | appengine.googleapis.com/system/network/received\_bytes\_count |
| gae\_app/default\_metrics | Sent bytes | Байт | appengine.googleapis.com/system/network/sent\_bytes\_count |
| gae\_instance/default\_metrics | Connections | Количество | appengine.googleapis.com/flex/instance/connections/current |
| gae\_instance/default\_metrics | CPU Utilization | Процент | appengine.googleapis.com/flex/instance/cpu/utilization |
| gae\_instance/default\_metrics | Network bytes received | Байт | appengine.googleapis.com/flex/instance/network/received\_bytes\_count |
| gae\_instance/default\_metrics | Network bytes sent | Байт | appengine.googleapis.com/flex/instance/network/sent\_bytes\_count |
| gae\_instance/default\_metrics | Websocket average duration | Секунда | appengine.googleapis.com/flex/instance/ws/avg\_duration |

## Связанные темы

* [Интеграции Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations "Настройка и конфигурирование Dynatrace в Google Cloud.")