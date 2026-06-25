---
title: Мониторинг Google Kubernetes Engine
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/google-gke/google-kubernetes-engine-monitoring
scraped: 2026-05-12T11:50:41.052189
---

# Мониторинг Google Kubernetes Engine

# Мониторинг Google Kubernetes Engine

* Практическое руководство
* Чтение: 7 мин
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

Для Google Kubernetes Engine доступны следующие наборы функций.

| Набор функций | Имя | Единица измерения | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| k8s\_cluster/default\_metrics | Log entries | Количество | logging.googleapis.com/log\_entry\_count |
| k8s\_node/default\_metrics | Allocatable cores | Не указано | kubernetes.io/node/cpu/allocatable\_cores |
| k8s\_node/default\_metrics | CPU allocatable utilization | Количество | kubernetes.io/node/cpu/allocatable\_utilization |
| k8s\_node/default\_metrics | CPU usage time | Секунда | kubernetes.io/node/cpu/core\_usage\_time |
| k8s\_node/default\_metrics | Total cores | Не указано | kubernetes.io/node/cpu/total\_cores |
| k8s\_node/default\_metrics | Allocatable ephemeral storage | Байт | kubernetes.io/node/ephemeral\_storage/allocatable\_bytes |
| k8s\_node/default\_metrics | Free inodes | Количество | kubernetes.io/node/ephemeral\_storage/inodes\_free |
| k8s\_node/default\_metrics | Total inodes | Количество | kubernetes.io/node/ephemeral\_storage/inodes\_total |
| k8s\_node/default\_metrics | Total ephemeral storage | Байт | kubernetes.io/node/ephemeral\_storage/total\_bytes |
| k8s\_node/default\_metrics | Ephemeral storage usage | Байт | kubernetes.io/node/ephemeral\_storage/used\_bytes |
| k8s\_node/default\_metrics | Allocatable memory | Байт | kubernetes.io/node/memory/allocatable\_bytes |
| k8s\_node/default\_metrics | Memory allocatable utilization | Количество | kubernetes.io/node/memory/allocatable\_utilization |
| k8s\_node/default\_metrics | Total memory | Байт | kubernetes.io/node/memory/total\_bytes |
| k8s\_node/default\_metrics | Memory usage | Байт | kubernetes.io/node/memory/used\_bytes |
| k8s\_node/default\_metrics | Bytes received | Байт | kubernetes.io/node/network/received\_bytes\_count |
| k8s\_node/default\_metrics | Bytes transmitted | Байт | kubernetes.io/node/network/sent\_bytes\_count |
| k8s\_node/default\_metrics | PID capacity | Количество | kubernetes.io/node/pid\_limit |
| k8s\_node/default\_metrics | PID usage | Количество | kubernetes.io/node/pid\_used |
| k8s\_node/default\_metrics | CPU usage time | Секунда | kubernetes.io/node\_daemon/cpu/core\_usage\_time |
| k8s\_node/default\_metrics | Memory usage | Байт | kubernetes.io/node\_daemon/memory/used\_bytes |
| k8s\_pod/default\_metrics | Bytes received | Байт | kubernetes.io/pod/network/received\_bytes\_count |
| k8s\_pod/default\_metrics | Bytes transmitted | Байт | kubernetes.io/pod/network/sent\_bytes\_count |
| k8s\_pod/default\_metrics | Volume capacity | Байт | kubernetes.io/pod/volume/total\_bytes |
| k8s\_pod/default\_metrics | Volume usage | Байт | kubernetes.io/pod/volume/used\_bytes |
| k8s\_pod/default\_metrics | Volume utilization | Количество | kubernetes.io/pod/volume/utilization |
| k8s\_pod/istio | Client Connection Close Count | Байт | istio.io/service/client/connection\_close\_count |
| k8s\_pod/istio | Client Connection Open Count | Байт | istio.io/service/client/connection\_open\_count |
| k8s\_pod/istio | Client Received Bytes Count | Байт | istio.io/service/client/received\_bytes\_count |
| k8s\_pod/istio | Client Request Bytes | Байт | istio.io/service/client/request\_bytes |
| k8s\_pod/istio | Client Request Count | Количество | istio.io/service/client/request\_count |
| k8s\_pod/istio | Client Response Bytes | Байт | istio.io/service/client/response\_bytes |
| k8s\_pod/istio | Client Roundtrip Latencies | Миллисекунда | istio.io/service/client/roundtrip\_latencies |
| k8s\_pod/istio | Client Sent Bytes Count | Байт | istio.io/service/client/sent\_bytes\_count |
| k8s\_container/default\_metrics | CPU usage time | Секунда | kubernetes.io/container/cpu/core\_usage\_time |
| k8s\_container/default\_metrics | Limit cores | Не указано | kubernetes.io/container/cpu/limit\_cores |
| k8s\_container/default\_metrics | CPU limit utilization | Количество | kubernetes.io/container/cpu/limit\_utilization |
| k8s\_container/default\_metrics | Request cores | Не указано | kubernetes.io/container/cpu/request\_cores |
| k8s\_container/default\_metrics | CPU request utilization | Количество | kubernetes.io/container/cpu/request\_utilization |
| k8s\_container/default\_metrics | Ephemeral storage limit | Байт | kubernetes.io/container/ephemeral\_storage/limit\_bytes |
| k8s\_container/default\_metrics | Ephemeral storage request | Байт | kubernetes.io/container/ephemeral\_storage/request\_bytes |
| k8s\_container/default\_metrics | Ephemeral storage usage | Байт | kubernetes.io/container/ephemeral\_storage/used\_bytes |
| k8s\_container/default\_metrics | Memory limit | Байт | kubernetes.io/container/memory/limit\_bytes |
| k8s\_container/default\_metrics | Memory limit utilization | Количество | kubernetes.io/container/memory/limit\_utilization |
| k8s\_container/default\_metrics | Page faults | Количество | kubernetes.io/container/memory/page\_fault\_count |
| k8s\_container/default\_metrics | Memory request | Байт | kubernetes.io/container/memory/request\_bytes |
| k8s\_container/default\_metrics | Memory request utilization | Количество | kubernetes.io/container/memory/request\_utilization |
| k8s\_container/default\_metrics | Memory usage | Байт | kubernetes.io/container/memory/used\_bytes |
| k8s\_container/default\_metrics | Restart count | Количество | kubernetes.io/container/restart\_count |
| k8s\_container/default\_metrics | Uptime | Секунда | kubernetes.io/container/uptime |
| k8s\_container/agent | Monitoring Agent API Request Count | Количество | agent.googleapis.com/agent/api\_request\_count |
| k8s\_container/agent | Logging Agent Log Entry Count | Количество | agent.googleapis.com/agent/log\_entry\_count |
| k8s\_container/agent | Logging Agent Retried Log Entry Writes Count | Количество | agent.googleapis.com/agent/log\_entry\_retry\_count |
| k8s\_container/agent | Monitoring Agent Memory Usage | Байт | agent.googleapis.com/agent/memory\_usage |
| k8s\_container/agent | Monitoring Agent Metric Point Count | Количество | agent.googleapis.com/agent/monitoring/point\_count |
| k8s\_container/agent | Logging Agent API Request Count | Количество | agent.googleapis.com/agent/request\_count |
| k8s\_container/agent | Monitoring Agent Process Labels Size | Байт | agent.googleapis.com/agent/streamspace\_size |
| k8s\_container/agent | Monitoring Agent is Throttling Processes | Количество | agent.googleapis.com/agent/streamspace\_size\_throttling |
| k8s\_container/agent | Monitoring/Logging Agent Uptime | Секунда | agent.googleapis.com/agent/uptime |
| k8s\_container/apigee | Apigee Cassandra client request latency | Количество | apigee.googleapis.com/cassandra/clientrequest\_latency |
| k8s\_container/apigee | Apigee Cassandra pending compaction tasks | Количество | apigee.googleapis.com/cassandra/compaction\_pendingtasks |
| k8s\_container/apigee | Apigee Cassandra bytes committed per area | Байт | apigee.googleapis.com/cassandra/jvm\_memory\_bytes\_committed |
| k8s\_container/apigee | Apigee Cassandra initial memory bytes | Байт | apigee.googleapis.com/cassandra/jvm\_memory\_bytes\_init |
| k8s\_container/apigee | Apigee Cassandra max bytes of memory | Байт | apigee.googleapis.com/cassandra/jvm\_memory\_bytes\_max |
| k8s\_container/apigee | Apigee Cassandra used JVM memory bytes | Байт | apigee.googleapis.com/cassandra/jvm\_memory\_bytes\_used |
| k8s\_container/apigee | Apigee Cassandra bytes committed per memory pool | Байт | apigee.googleapis.com/cassandra/jvm\_memory\_pool\_bytes\_committed |
| k8s\_container/apigee | Apigee Cassandra initial bytes of JVM memory pool | Байт | apigee.googleapis.com/cassandra/jvm\_memory\_pool\_bytes\_init |
| k8s\_container/apigee | Apigee Cassandra JVM memory pool bytes max | Байт | apigee.googleapis.com/cassandra/jvm\_memory\_pool\_bytes\_max |
| k8s\_container/apigee | Apigee Cassandra bytes per memory pool | Байт | apigee.googleapis.com/cassandra/jvm\_memory\_pool\_bytes\_used |
| k8s\_container/apigee | Apigee Cassandra user and system CPU in seconds | Секунда | apigee.googleapis.com/cassandra/process\_cpu\_seconds\_total |
| k8s\_container/apigee | Apigee Cassandra process max file descriptors | Количество | apigee.googleapis.com/cassandra/process\_max\_fds |
| k8s\_container/apigee | Apigee Cassandra process open file descriptors | Количество | apigee.googleapis.com/cassandra/process\_open\_fds |
| k8s\_container/apigee | Apigee server fault count | Количество | apigee.googleapis.com/server/fault\_count |
| k8s\_container/apigee | Apigee server latencies | Миллисекунда | apigee.googleapis.com/server/latencies |
| k8s\_container/apigee | Apigee server nio | Количество | apigee.googleapis.com/server/nio |
| k8s\_container/apigee | Apigee server thread count | Количество | apigee.googleapis.com/server/num\_threads |
| k8s\_container/apigee | Apigee server request count | Количество | apigee.googleapis.com/server/request\_count |
| k8s\_container/apigee | Apigee server response count | Количество | apigee.googleapis.com/server/response\_count |
| k8s\_container/apigee | Apigee UDCA disk used bytes | Байт | apigee.googleapis.com/udca/disk/used\_bytes |
| k8s\_container/apigee | Apigee UDCA server local file count | Количество | apigee.googleapis.com/udca/server/local\_file\_count |
| k8s\_container/apigee | Apigee UDCA server timestamp difference between current time and latest file | Секунда | apigee.googleapis.com/udca/server/local\_file\_latest\_ts |
| k8s\_container/apigee | Apigee UDCA server timestamp difference between current time and oldest file | Секунда | apigee.googleapis.com/udca/server/local\_file\_oldest\_ts |
| k8s\_container/apigee | Apigee UDCA pruned file count | Количество | apigee.googleapis.com/udca/server/pruned\_file\_count |
| k8s\_container/apigee | Apigee UDCA outstanding number of entries in retry cache | Количество | apigee.googleapis.com/udca/server/retry\_cache\_size |
| k8s\_container/apigee | Apigee UDCA server total latencies | Секунда | apigee.googleapis.com/udca/server/total\_latencies |
| k8s\_container/apigee | Apigee UDCA server upload latencies | Секунда | apigee.googleapis.com/udca/server/upload\_latencies |
| k8s\_container/apigee | Apigee UDCA server HTTP error count | Количество | apigee.googleapis.com/udca/upstream/http\_error\_count |
| k8s\_container/apigee | Apigee UDCA server HTTP latencies | Секунда | apigee.googleapis.com/udca/upstream/http\_latencies |
| k8s\_container/apigee | Apigee UDCA uploaded file count | Количество | apigee.googleapis.com/udca/upstream/uploaded\_file\_count |
| k8s\_container/apigee | Apigee UDCA uploaded file size distribution | Байт | apigee.googleapis.com/udca/upstream/uploaded\_file\_sizes |
| k8s\_container/apigee | Apigee upstream latencies | Миллисекунда | apigee.googleapis.com/upstream/latencies |
| k8s\_container/apigee | Apigee upstream request count | Количество | apigee.googleapis.com/upstream/request\_count |
| k8s\_container/apigee | Apigee upstream response count | Количество | apigee.googleapis.com/upstream/response\_count |
| k8s\_container/istio | Config Convergence Latencies | Миллисекунда | istio.io/control/config\_convergence\_latencies |
| k8s\_container/istio | Config Event Count | Количество | istio.io/control/config\_event\_count |
| k8s\_container/istio | Config Push Count | Количество | istio.io/control/config\_push\_count |
| k8s\_container/istio | Config Validation Count | Количество | istio.io/control/config\_validation\_count |
| k8s\_container/istio | Proxy Clients | Количество | istio.io/control/proxy\_clients |
| k8s\_container/istio | Rejected Config Count | Количество | istio.io/control/rejected\_config\_count |
| k8s\_container/istio | Sidecar Injection Count | Количество | istio.io/control/sidecar\_injection\_count |
| k8s\_container/istio | Server Connection Close Count | Байт | istio.io/service/server/connection\_close\_count |
| k8s\_container/istio | Server Connection Open Count | Байт | istio.io/service/server/connection\_open\_count |
| k8s\_container/istio | Server Received Bytes Count | Байт | istio.io/service/server/received\_bytes\_count |
| k8s\_container/istio | Server Request Bytes | Байт | istio.io/service/server/request\_bytes |
| k8s\_container/istio | Server Request Count | Количество | istio.io/service/server/request\_count |
| k8s\_container/istio | Server Response Bytes | Байт | istio.io/service/server/response\_bytes |
| k8s\_container/istio | Server Response Latencies | Миллисекунда | istio.io/service/server/response\_latencies |
| k8s\_container/istio | Server Sent Bytes Count | Байт | istio.io/service/server/sent\_bytes\_count |
| k8s\_container/nginx | Nginx connections\_accepted | Не указано | kubernetes.io/nginx/connections\_accepted |
| k8s\_container/nginx | Nginx connections\_active | Не указано | kubernetes.io/nginx/connections\_active |
| k8s\_container/nginx | Nginx connections\_handled | Не указано | kubernetes.io/nginx/connections\_handled |
| k8s\_container/nginx | Nginx connections\_reading | Не указано | kubernetes.io/nginx/connections\_reading |
| k8s\_container/nginx | Nginx connections\_waiting | Не указано | kubernetes.io/nginx/connections\_waiting |
| k8s\_container/nginx | Nginx connections\_writing | Не указано | kubernetes.io/nginx/connections\_writing |
| k8s\_container/nginx | Nginx http\_requests\_total | Не указано | kubernetes.io/nginx/http\_requests\_total |
| k8s\_container/nginx | Nginx nginxexporter\_build\_info | Количество | kubernetes.io/nginx/nginxexporter\_build\_info |
| k8s\_container/nginx | Nginx up | Количество | kubernetes.io/nginx/up |

## Связанные темы

* [Интеграции Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations "Настройка и конфигурирование Dynatrace в Google Cloud.")