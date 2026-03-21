---
title: Мониторинг Google Kubernetes Engine
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/google-gke/google-kubernetes-engine-monitoring
scraped: 2026-03-06T21:37:54.098381
---

* 7 мин. чтения

Интеграция Dynatrace с Google Cloud использует данные, собранные из Google Operations API, для непрерывного мониторинга работоспособности и производительности сервисов Google Cloud. Помимо объединения всех релевантных данных в дашборды, она также обеспечивает оповещения и отслеживание событий.

## Предварительные требования

[Настройка интеграции](../gcp-guide/deploy-k8.md "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.")

## Добавление сервисов и наборов функций Необязательно

После интеграции Dynatrace автоматически начинает мониторинг ряда предустановленных сервисов Google Cloud и наборов функций (метрик). Помимо них, вы можете добавить дополнительные сервисы или наборы функций для мониторинга. Подробнее см. в разделе [Добавление и удаление сервисов](../gcp-guide/deploy-k8.md#manage "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.").

Список наборов функций, доступных для данного сервиса, см. в разделе [Таблица метрик](#table).

## Просмотр метрик

После развёртывания интеграции вы можете просматривать метрики отслеживаемых сервисов в [браузере метрик](../../../../analyze-explore-automate/dashboards-classic/metrics-browser.md "Просмотр метрик с помощью браузера метрик Dynatrace."), [Data Explorer](../../../../analyze-explore-automate/explorer.md "Запрашивайте метрики и преобразуйте результаты для получения нужных данных."), а также в плитках дашбордов.

## Таблица метрик

Для Google Kubernetes Engine доступны следующие наборы функций.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| k8s\_cluster/default\_metrics | Записи логов | Count | logging.googleapis.com/log\_entry\_count |
| k8s\_node/default\_metrics | Доступные для выделения ядра | Unspecified | kubernetes.io/node/cpu/allocatable\_cores |
| k8s\_node/default\_metrics | Утилизация выделяемого CPU | Count | kubernetes.io/node/cpu/allocatable\_utilization |
| k8s\_node/default\_metrics | Время использования CPU | Second | kubernetes.io/node/cpu/core\_usage\_time |
| k8s\_node/default\_metrics | Всего ядер | Unspecified | kubernetes.io/node/cpu/total\_cores |
| k8s\_node/default\_metrics | Доступное для выделения эфемерное хранилище | Byte | kubernetes.io/node/ephemeral\_storage/allocatable\_bytes |
| k8s\_node/default\_metrics | Свободные inode | Count | kubernetes.io/node/ephemeral\_storage/inodes\_free |
| k8s\_node/default\_metrics | Всего inode | Count | kubernetes.io/node/ephemeral\_storage/inodes\_total |
| k8s\_node/default\_metrics | Общий объём эфемерного хранилища | Byte | kubernetes.io/node/ephemeral\_storage/total\_bytes |
| k8s\_node/default\_metrics | Использование эфемерного хранилища | Byte | kubernetes.io/node/ephemeral\_storage/used\_bytes |
| k8s\_node/default\_metrics | Доступная для выделения память | Byte | kubernetes.io/node/memory/allocatable\_bytes |
| k8s\_node/default\_metrics | Утилизация выделяемой памяти | Count | kubernetes.io/node/memory/allocatable\_utilization |
| k8s\_node/default\_metrics | Общий объём памяти | Byte | kubernetes.io/node/memory/total\_bytes |
| k8s\_node/default\_metrics | Использование памяти | Byte | kubernetes.io/node/memory/used\_bytes |
| k8s\_node/default\_metrics | Полученные байты | Byte | kubernetes.io/node/network/received\_bytes\_count |
| k8s\_node/default\_metrics | Переданные байты | Byte | kubernetes.io/node/network/sent\_bytes\_count |
| k8s\_node/default\_metrics | Ёмкость PID | Count | kubernetes.io/node/pid\_limit |
| k8s\_node/default\_metrics | Использование PID | Count | kubernetes.io/node/pid\_used |
| k8s\_node/default\_metrics | Время использования CPU | Second | kubernetes.io/node\_daemon/cpu/core\_usage\_time |
| k8s\_node/default\_metrics | Использование памяти | Byte | kubernetes.io/node\_daemon/memory/used\_bytes |
| k8s\_pod/default\_metrics | Полученные байты | Byte | kubernetes.io/pod/network/received\_bytes\_count |
| k8s\_pod/default\_metrics | Переданные байты | Byte | kubernetes.io/pod/network/sent\_bytes\_count |
| k8s\_pod/default\_metrics | Ёмкость тома | Byte | kubernetes.io/pod/volume/total\_bytes |
| k8s\_pod/default\_metrics | Использование тома | Byte | kubernetes.io/pod/volume/used\_bytes |
| k8s\_pod/default\_metrics | Утилизация тома | Count | kubernetes.io/pod/volume/utilization |
| k8s\_pod/istio | Количество закрытых клиентских соединений | Byte | istio.io/service/client/connection\_close\_count |
| k8s\_pod/istio | Количество открытых клиентских соединений | Byte | istio.io/service/client/connection\_open\_count |
| k8s\_pod/istio | Полученные байты клиентом | Byte | istio.io/service/client/received\_bytes\_count |
| k8s\_pod/istio | Байты клиентского запроса | Byte | istio.io/service/client/request\_bytes |
| k8s\_pod/istio | Количество клиентских запросов | Count | istio.io/service/client/request\_count |
| k8s\_pod/istio | Байты клиентского ответа | Byte | istio.io/service/client/response\_bytes |
| k8s\_pod/istio | Задержки клиентских запросов | MilliSecond | istio.io/service/client/roundtrip\_latencies |
| k8s\_pod/istio | Отправленные байты клиентом | Byte | istio.io/service/client/sent\_bytes\_count |
| k8s\_container/default\_metrics | Время использования CPU | Second | kubernetes.io/container/cpu/core\_usage\_time |
| k8s\_container/default\_metrics | Лимит ядер | Unspecified | kubernetes.io/container/cpu/limit\_cores |
| k8s\_container/default\_metrics | Утилизация лимита CPU | Count | kubernetes.io/container/cpu/limit\_utilization |
| k8s\_container/default\_metrics | Запрошенные ядра | Unspecified | kubernetes.io/container/cpu/request\_cores |
| k8s\_container/default\_metrics | Утилизация запрошенного CPU | Count | kubernetes.io/container/cpu/request\_utilization |
| k8s\_container/default\_metrics | Лимит эфемерного хранилища | Byte | kubernetes.io/container/ephemeral\_storage/limit\_bytes |
| k8s\_container/default\_metrics | Запрос эфемерного хранилища | Byte | kubernetes.io/container/ephemeral\_storage/request\_bytes |
| k8s\_container/default\_metrics | Использование эфемерного хранилища | Byte | kubernetes.io/container/ephemeral\_storage/used\_bytes |
| k8s\_container/default\_metrics | Лимит памяти | Byte | kubernetes.io/container/memory/limit\_bytes |
| k8s\_container/default\_metrics | Утилизация лимита памяти | Count | kubernetes.io/container/memory/limit\_utilization |
| k8s\_container/default\_metrics | Ошибки страниц | Count | kubernetes.io/container/memory/page\_fault\_count |
| k8s\_container/default\_metrics | Запрос памяти | Byte | kubernetes.io/container/memory/request\_bytes |
| k8s\_container/default\_metrics | Утилизация запрошенной памяти | Count | kubernetes.io/container/memory/request\_utilization |
| k8s\_container/default\_metrics | Использование памяти | Byte | kubernetes.io/container/memory/used\_bytes |
| k8s\_container/default\_metrics | Количество перезапусков | Count | kubernetes.io/container/restart\_count |
| k8s\_container/default\_metrics | Время работы | Second | kubernetes.io/container/uptime |
| k8s\_container/agent | Количество запросов API агента мониторинга | Count | agent.googleapis.com/agent/api\_request\_count |
| k8s\_container/agent | Количество записей лога агента логирования | Count | agent.googleapis.com/agent/log\_entry\_count |
| k8s\_container/agent | Количество повторных записей лога агента логирования | Count | agent.googleapis.com/agent/log\_entry\_retry\_count |
| k8s\_container/agent | Использование памяти агентом мониторинга | Byte | agent.googleapis.com/agent/memory\_usage |
| k8s\_container/agent | Количество точек метрик агента мониторинга | Count | agent.googleapis.com/agent/monitoring/point\_count |
| k8s\_container/agent | Количество запросов API агента логирования | Count | agent.googleapis.com/agent/request\_count |
| k8s\_container/agent | Размер меток процессов агента мониторинга | Byte | agent.googleapis.com/agent/streamspace\_size |
| k8s\_container/agent | Агент мониторинга ограничивает процессы | Count | agent.googleapis.com/agent/streamspace\_size\_throttling |
| k8s\_container/agent | Время работы агента мониторинга/логирования | Second | agent.googleapis.com/agent/uptime |
| k8s\_container/apigee | Задержка клиентских запросов Apigee Cassandra | Count | apigee.googleapis.com/cassandra/clientrequest\_latency |
| k8s\_container/apigee | Ожидающие задачи компактификации Apigee Cassandra | Count | apigee.googleapis.com/cassandra/compaction\_pendingtasks |
| k8s\_container/apigee | Выделенные байты JVM Apigee Cassandra по области | Byte | apigee.googleapis.com/cassandra/jvm\_memory\_bytes\_committed |
| k8s\_container/apigee | Начальные байты памяти Apigee Cassandra | Byte | apigee.googleapis.com/cassandra/jvm\_memory\_bytes\_init |
| k8s\_container/apigee | Максимальные байты памяти Apigee Cassandra | Byte | apigee.googleapis.com/cassandra/jvm\_memory\_bytes\_max |
| k8s\_container/apigee | Использованные байты JVM Apigee Cassandra | Byte | apigee.googleapis.com/cassandra/jvm\_memory\_bytes\_used |
| k8s\_container/apigee | Выделенные байты пула памяти JVM Apigee Cassandra | Byte | apigee.googleapis.com/cassandra/jvm\_memory\_pool\_bytes\_committed |
| k8s\_container/apigee | Начальные байты пула памяти JVM Apigee Cassandra | Byte | apigee.googleapis.com/cassandra/jvm\_memory\_pool\_bytes\_init |
| k8s\_container/apigee | Максимальные байты пула памяти JVM Apigee Cassandra | Byte | apigee.googleapis.com/cassandra/jvm\_memory\_pool\_bytes\_max |
| k8s\_container/apigee | Байты пула памяти Apigee Cassandra | Byte | apigee.googleapis.com/cassandra/jvm\_memory\_pool\_bytes\_used |
| k8s\_container/apigee | Пользовательское и системное CPU в секундах Apigee Cassandra | Second | apigee.googleapis.com/cassandra/process\_cpu\_seconds\_total |
| k8s\_container/apigee | Максимальное количество дескрипторов файлов процесса Apigee Cassandra | Count | apigee.googleapis.com/cassandra/process\_max\_fds |
| k8s\_container/apigee | Открытые дескрипторы файлов процесса Apigee Cassandra | Count | apigee.googleapis.com/cassandra/process\_open\_fds |
| k8s\_container/apigee | Количество ошибок сервера Apigee | Count | apigee.googleapis.com/server/fault\_count |
| k8s\_container/apigee | Задержки сервера Apigee | MilliSecond | apigee.googleapis.com/server/latencies |
| k8s\_container/apigee | NIO сервера Apigee | Count | apigee.googleapis.com/server/nio |
| k8s\_container/apigee | Количество потоков сервера Apigee | Count | apigee.googleapis.com/server/num\_threads |
| k8s\_container/apigee | Количество запросов сервера Apigee | Count | apigee.googleapis.com/server/request\_count |
| k8s\_container/apigee | Количество ответов сервера Apigee | Count | apigee.googleapis.com/server/response\_count |
| k8s\_container/apigee | Использованные байты диска Apigee UDCA | Byte | apigee.googleapis.com/udca/disk/used\_bytes |
| k8s\_container/apigee | Количество локальных файлов сервера Apigee UDCA | Count | apigee.googleapis.com/udca/server/local\_file\_count |
| k8s\_container/apigee | Разница между текущим временем и временем новейшего файла Apigee UDCA | Second | apigee.googleapis.com/udca/server/local\_file\_latest\_ts |
| k8s\_container/apigee | Разница между текущим временем и временем старейшего файла Apigee UDCA | Second | apigee.googleapis.com/udca/server/local\_file\_oldest\_ts |
| k8s\_container/apigee | Количество удалённых файлов Apigee UDCA | Count | apigee.googleapis.com/udca/server/pruned\_file\_count |
| k8s\_container/apigee | Количество записей в кэше повторов Apigee UDCA | Count | apigee.googleapis.com/udca/server/retry\_cache\_size |
| k8s\_container/apigee | Общие задержки сервера Apigee UDCA | Second | apigee.googleapis.com/udca/server/total\_latencies |
| k8s\_container/apigee | Задержки загрузки сервера Apigee UDCA | Second | apigee.googleapis.com/udca/server/upload\_latencies |
| k8s\_container/apigee | Количество HTTP-ошибок сервера Apigee UDCA | Count | apigee.googleapis.com/udca/upstream/http\_error\_count |
| k8s\_container/apigee | HTTP-задержки сервера Apigee UDCA | Second | apigee.googleapis.com/udca/upstream/http\_latencies |
| k8s\_container/apigee | Количество загруженных файлов Apigee UDCA | Count | apigee.googleapis.com/udca/upstream/uploaded\_file\_count |
| k8s\_container/apigee | Распределение размеров загруженных файлов Apigee UDCA | Byte | apigee.googleapis.com/udca/upstream/uploaded\_file\_sizes |
| k8s\_container/apigee | Задержки upstream Apigee | MilliSecond | apigee.googleapis.com/upstream/latencies |
| k8s\_container/apigee | Количество запросов upstream Apigee | Count | apigee.googleapis.com/upstream/request\_count |
| k8s\_container/apigee | Количество ответов upstream Apigee | Count | apigee.googleapis.com/upstream/response\_count |
| k8s\_container/istio | Задержки конвергенции конфигурации | MilliSecond | istio.io/control/config\_convergence\_latencies |
| k8s\_container/istio | Количество событий конфигурации | Count | istio.io/control/config\_event\_count |
| k8s\_container/istio | Количество отправок конфигурации | Count | istio.io/control/config\_push\_count |
| k8s\_container/istio | Количество валидаций конфигурации | Count | istio.io/control/config\_validation\_count |
| k8s\_container/istio | Прокси-клиенты | Count | istio.io/control/proxy\_clients |
| k8s\_container/istio | Количество отклонённых конфигураций | Count | istio.io/control/rejected\_config\_count |
| k8s\_container/istio | Количество инъекций sidecar | Count | istio.io/control/sidecar\_injection\_count |
| k8s\_container/istio | Количество закрытых серверных соединений | Byte | istio.io/service/server/connection\_close\_count |
| k8s\_container/istio | Количество открытых серверных соединений | Byte | istio.io/service/server/connection\_open\_count |
| k8s\_container/istio | Полученные байты сервером | Byte | istio.io/service/server/received\_bytes\_count |
| k8s\_container/istio | Байты серверного запроса | Byte | istio.io/service/server/request\_bytes |
| k8s\_container/istio | Количество серверных запросов | Count | istio.io/service/server/request\_count |
| k8s\_container/istio | Байты серверного ответа | Byte | istio.io/service/server/response\_bytes |
| k8s\_container/istio | Задержки серверных ответов | MilliSecond | istio.io/service/server/response\_latencies |
| k8s\_container/istio | Отправленные байты сервером | Byte | istio.io/service/server/sent\_bytes\_count |
| k8s\_container/nginx | Nginx connections\_accepted | Unspecified | kubernetes.io/nginx/connections\_accepted |
| k8s\_container/nginx | Nginx connections\_active | Unspecified | kubernetes.io/nginx/connections\_active |
| k8s\_container/nginx | Nginx connections\_handled | Unspecified | kubernetes.io/nginx/connections\_handled |
| k8s\_container/nginx | Nginx connections\_reading | Unspecified | kubernetes.io/nginx/connections\_reading |
| k8s\_container/nginx | Nginx connections\_waiting | Unspecified | kubernetes.io/nginx/connections\_waiting |
| k8s\_container/nginx | Nginx connections\_writing | Unspecified | kubernetes.io/nginx/connections\_writing |
| k8s\_container/nginx | Nginx http\_requests\_total | Unspecified | kubernetes.io/nginx/http\_requests\_total |
| k8s\_container/nginx | Nginx nginxexporter\_build\_info | Count | kubernetes.io/nginx/nginxexporter\_build\_info |
| k8s\_container/nginx | Nginx up | Count | kubernetes.io/nginx/up |

## Связанные темы

* [Интеграции Google Cloud](../../gcp-integrations.md "Настройка и конфигурирование Dynatrace на Google Cloud.")
