---
title: Мониторинг Google Compute Engine с метриками Operations Suite
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/google-compute-engine/compute-engine-monitoring
scraped: 2026-03-04T21:35:51.753899
---

# Мониторинг Google Compute Engine с метриками Operations Suite

# Мониторинг Google Compute Engine с метриками Operations Suite

* Последняя версия Dynatrace
* Практическое руководство
* 18 минут чтения
* Опубликовано 17 января 2022 г.

Интеграция Dynatrace с Google Cloud использует данные, собранные из Google Operation API, для постоянного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все актуальные данные на дашбордах, она также обеспечивает оповещение и отслеживание событий.

## Предварительные требования

[Настроить интеграцию](../gcp-guide/deploy-k8.md "Настройте мониторинг логов и метрик для сервисов GCP на новом кластере GKE Autopilot.")

## Добавить сервисы и наборы функций (опционально)

После интеграции Dynatrace автоматически отслеживает ряд предустановленных сервисов Google Cloud и наборов функций (метрик). Помимо них, вы можете добавить в мониторинг дополнительные сервисы или наборы функций. Подробности см. в разделе [Добавить или удалить сервисы](../gcp-guide/deploy-k8.md#manage "Настройте мониторинг логов и метрик для сервисов GCP на новом кластере GKE Autopilot.").

Список наборов функций, доступных для данного сервиса, см. в [таблице метрик](#table).

## Просмотр метрик

После развёртывания интеграции вы можете просматривать метрики отслеживаемых сервисов в [браузере метрик](../../../../analyze-explore-automate/dashboards-classic/metrics-browser.md "Просматривайте метрики с помощью браузера метрик Dynatrace."), [Data Explorer](../../../../analyze-explore-automate/explorer.md "Запрашивайте метрики и преобразуйте результаты для получения нужной информации."), а также на плитках дашборда.

## Таблица метрик

Для Google Compute Engine доступны следующие наборы функций.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| gce\_instance/default\_metrics | Отброшенные байты | Байт | compute.googleapis.com/firewall/dropped\_bytes\_count |
| gce\_instance/default\_metrics | Отброшенные пакеты | Количество | compute.googleapis.com/firewall/dropped\_packets\_count |
| gce\_instance/default\_metrics | Количество задач в очереди выполнения | Количество | compute.googleapis.com/guest/cpu/runnable\_task\_count |
| gce\_instance/default\_metrics | Использование CPU | Секунда | compute.googleapis.com/guest/cpu/usage\_time |
| gce\_instance/default\_metrics | Использование диска в байтах | Байт | compute.googleapis.com/guest/disk/bytes\_used |
| gce\_instance/default\_metrics | Время ввода/вывода | Миллисекунда | compute.googleapis.com/guest/disk/io\_time |
| gce\_instance/default\_metrics | Объединённые дисковые операции | Количество | compute.googleapis.com/guest/disk/merged\_operation\_count |
| gce\_instance/default\_metrics | Переданные байты диска | Байт | compute.googleapis.com/guest/disk/operation\_bytes\_count |
| gce\_instance/default\_metrics | Дисковые операции | Количество | compute.googleapis.com/guest/disk/operation\_count |
| gce\_instance/default\_metrics | Время дисковой операции | Миллисекунда | compute.googleapis.com/guest/disk/operation\_time |
| gce\_instance/default\_metrics | Длина очереди | Количество | compute.googleapis.com/guest/disk/queue\_length |
| gce\_instance/default\_metrics | Время ввода/вывода | Миллисекунда | compute.googleapis.com/guest/disk/weighted\_io\_time |
| gce\_instance/default\_metrics | Использование анонимной памяти в байтах | Байт | compute.googleapis.com/guest/memory/anonymous\_used |
| gce\_instance/default\_metrics | Использование памяти в байтах | Байт | compute.googleapis.com/guest/memory/bytes\_used |
| gce\_instance/default\_metrics | Использование грязных страниц в байтах | Байт | compute.googleapis.com/guest/memory/dirty\_used |
| gce\_instance/default\_metrics | Использование кэш-памяти страниц в байтах | Байт | compute.googleapis.com/guest/memory/page\_cache\_used |
| gce\_instance/default\_metrics | Использование невытесняемой памяти в байтах | Байт | compute.googleapis.com/guest/memory/unevictable\_used |
| gce\_instance/default\_metrics | Количество проблем | Количество | compute.googleapis.com/guest/system/problem\_count |
| gce\_instance/default\_metrics | Состояние проблемы | Количество | compute.googleapis.com/guest/system/problem\_state |
| gce\_instance/default\_metrics | Время работы | Секунда | compute.googleapis.com/guest/system/uptime |
| gce\_instance/default\_metrics | Зарезервированные vCPU | Количество | compute.googleapis.com/instance/cpu/reserved\_cores |
| gce\_instance/default\_metrics | Время ожидания планировщика | Секунда | compute.googleapis.com/instance/cpu/scheduler\_wait\_time |
| gce\_instance/default\_metrics | Использование CPU | Секунда | compute.googleapis.com/instance/cpu/usage\_time |
| gce\_instance/default\_metrics | Утилизация CPU | Процент | compute.googleapis.com/instance/cpu/utilization |
| gce\_instance/default\_metrics | Пиковые байты чтения диска | Байт | compute.googleapis.com/instance/disk/max\_read\_bytes\_count |
| gce\_instance/default\_metrics | Пиковые операции чтения диска | Количество | compute.googleapis.com/instance/disk/max\_read\_ops\_count |
| gce\_instance/default\_metrics | Пиковые байты записи диска | Байт | compute.googleapis.com/instance/disk/max\_write\_bytes\_count |
| gce\_instance/default\_metrics | Пиковые операции записи диска | Количество | compute.googleapis.com/instance/disk/max\_write\_ops\_count |
| gce\_instance/default\_metrics | Байты чтения диска | Байт | compute.googleapis.com/instance/disk/read\_bytes\_count |
| gce\_instance/default\_metrics | Операции чтения диска | Количество | compute.googleapis.com/instance/disk/read\_ops\_count |
| gce\_instance/default\_metrics | Ограниченные байты чтения | Байт | compute.googleapis.com/instance/disk/throttled\_read\_bytes\_count |
| gce\_instance/default\_metrics | Ограниченные операции чтения | Количество | compute.googleapis.com/instance/disk/throttled\_read\_ops\_count |
| gce\_instance/default\_metrics | Ограниченные байты записи | Байт | compute.googleapis.com/instance/disk/throttled\_write\_bytes\_count |
| gce\_instance/default\_metrics | Ограниченные операции записи | Количество | compute.googleapis.com/instance/disk/throttled\_write\_ops\_count |
| gce\_instance/default\_metrics | Байты записи диска | Байт | compute.googleapis.com/instance/disk/write\_bytes\_count |
| gce\_instance/default\_metrics | Операции записи диска | Количество | compute.googleapis.com/instance/disk/write\_ops\_count |
| gce\_instance/default\_metrics | Проверка при раннем запуске | Количество | compute.googleapis.com/instance/integrity/early\_boot\_validation\_status |
| gce\_instance/default\_metrics | Проверка при позднем запуске | Количество | compute.googleapis.com/instance/integrity/late\_boot\_validation\_status |
| gce\_instance/default\_metrics | Общий объём памяти ВМ | Байт | compute.googleapis.com/instance/memory/balloon/ram\_size |
| gce\_instance/default\_metrics | Используемая память ВМ | Байт | compute.googleapis.com/instance/memory/balloon/ram\_used |
| gce\_instance/default\_metrics | Замена памяти ВМ (входящий) | Байт | compute.googleapis.com/instance/memory/balloon/swap\_in\_bytes\_count |
| gce\_instance/default\_metrics | Замена памяти ВМ (исходящий) | Байт | compute.googleapis.com/instance/memory/balloon/swap\_out\_bytes\_count |
| gce\_instance/default\_metrics | Полученные байты | Байт | compute.googleapis.com/instance/network/received\_bytes\_count |
| gce\_instance/default\_metrics | Полученные пакеты | Количество | compute.googleapis.com/instance/network/received\_packets\_count |
| gce\_instance/default\_metrics | Отправленные байты | Байт | compute.googleapis.com/instance/network/sent\_bytes\_count |
| gce\_instance/default\_metrics | Отправленные пакеты | Количество | compute.googleapis.com/instance/network/sent\_packets\_count |
| gce\_instance/default\_metrics | Время работы | Секунда | compute.googleapis.com/instance/uptime |
| gce\_instance/default\_metrics | Общее время работы | Секунда | compute.googleapis.com/instance/uptime\_total |
| gce\_instance/default\_metrics | Отброшенные пакеты | Количество | compute.googleapis.com/mirroring/dropped\_packets\_count |
| gce\_instance/default\_metrics | Зеркалированные байты | Байт | compute.googleapis.com/mirroring/mirrored\_bytes\_count |
| gce\_instance/default\_metrics | Зеркалированные пакеты | Количество | compute.googleapis.com/mirroring/mirrored\_packets\_count |
| gce\_instance/default\_metrics | Выделенные порты | Не указано | compute.googleapis.com/nat/allocated\_ports |
| gce\_instance/default\_metrics | Количество закрытых соединений | Не указано | compute.googleapis.com/nat/closed\_connections\_count |
| gce\_instance/default\_metrics | Количество отброшенных входящих пакетов | Не указано | compute.googleapis.com/nat/dropped\_received\_packets\_count |
| gce\_instance/default\_metrics | Количество отброшенных исходящих пакетов | Не указано | compute.googleapis.com/nat/dropped\_sent\_packets\_count |
| gce\_instance/default\_metrics | Количество новых соединений | Не указано | compute.googleapis.com/nat/new\_connections\_count |
| gce\_instance/default\_metrics | Открытые соединения | Не указано | compute.googleapis.com/nat/open\_connections |
| gce\_instance/default\_metrics | Использование портов | Не указано | compute.googleapis.com/nat/port\_usage |
| gce\_instance/default\_metrics | Количество полученных байт | Байт | compute.googleapis.com/nat/received\_bytes\_count |
| gce\_instance/default\_metrics | Количество полученных пакетов | Не указано | compute.googleapis.com/nat/received\_packets\_count |
| gce\_instance/default\_metrics | Количество отправленных байт | Байт | compute.googleapis.com/nat/sent\_bytes\_count |
| gce\_instance/default\_metrics | Количество отправленных пакетов | Не указано | compute.googleapis.com/nat/sent\_packets\_count |
| gce\_instance/agent | Количество запросов к API агента мониторинга | Количество | agent.googleapis.com/agent/api\_request\_count |
| gce\_instance/agent | Количество записей лога агента ведения журнала | Количество | agent.googleapis.com/agent/log\_entry\_count |
| gce\_instance/agent | Количество повторных попыток записи лога агента ведения журнала | Количество | agent.googleapis.com/agent/log\_entry\_retry\_count |
| gce\_instance/agent | Использование памяти агента мониторинга | Байт | agent.googleapis.com/agent/memory\_usage |
| gce\_instance/agent | Количество точек метрик агента мониторинга | Количество | agent.googleapis.com/agent/monitoring/point\_count |
| gce\_instance/agent | Количество запросов к API агента ведения журнала | Количество | agent.googleapis.com/agent/request\_count |
| gce\_instance/agent | Размер меток процессов агента мониторинга | Байт | agent.googleapis.com/agent/streamspace\_size |
| gce\_instance/agent | Агент мониторинга ограничивает процессы | Количество | agent.googleapis.com/agent/streamspace\_size\_throttling |
| gce\_instance/agent | Время работы агента мониторинга/ведения журнала | Секунда | agent.googleapis.com/agent/uptime |
| gce\_instance/agent | Открытые соединения | Количество | agent.googleapis.com/apache/connections |
| gce\_instance/agent | Свободные обработчики | Количество | agent.googleapis.com/apache/idle\_workers |
| gce\_instance/agent | Запросы | Количество | agent.googleapis.com/apache/request\_count |
| gce\_instance/agent | Доска состояния | Количество | agent.googleapis.com/apache/scoreboard |
| gce\_instance/agent | Трафик | Байт | agent.googleapis.com/apache/traffic |
| gce\_instance/agent | Количество попаданий в кэш | Количество | agent.googleapis.com/cassandra/cache/hits |
| gce\_instance/agent | Задержка чтения | Микросекунда | agent.googleapis.com/cassandra/client\_request/latency/50p |
| gce\_instance/agent | Задержка чтения | Микросекунда | agent.googleapis.com/cassandra/client\_request/latency/95p |
| gce\_instance/agent | Задержка чтения | Микросекунда | agent.googleapis.com/cassandra/client\_request/latency/99p |
| gce\_instance/agent | Задержка чтения | Микросекунда | agent.googleapis.com/cassandra/client\_request/latency/max |
| gce\_instance/agent | Степень сжатия | Количество | agent.googleapis.com/cassandra/column\_family/compression\_ratio |
| gce\_instance/agent | Максимальный размер строки | Байт | agent.googleapis.com/cassandra/column\_family/max\_row\_size |
| gce\_instance/agent | Размер журнала фиксации | Байт | agent.googleapis.com/cassandra/commitlog\_total\_size |
| gce\_instance/agent | Завершённые задачи | Количество | agent.googleapis.com/cassandra/completed\_tasks |
| gce\_instance/agent | Задачи | Количество | agent.googleapis.com/cassandra/current\_tasks |
| gce\_instance/agent | Отброшенные сообщения | Количество | agent.googleapis.com/cassandra/dropped\_message/dropped\_count |
| gce\_instance/agent | Исключения | Количество | agent.googleapis.com/cassandra/storage\_service\_exception\_count |
| gce\_instance/agent | Объём хранилища | Байт | agent.googleapis.com/cassandra/storage\_service\_load |
| gce\_instance/agent | Задержка запроса | Миллисекунда | agent.googleapis.com/couchdb/average\_request\_time |
| gce\_instance/agent | Пакетные запросы | Количество | agent.googleapis.com/couchdb/httpd/bulk\_request\_count |
| gce\_instance/agent | Запросы | Количество | agent.googleapis.com/couchdb/httpd/request\_count |
| gce\_instance/agent | Методы запросов | Количество | agent.googleapis.com/couchdb/httpd/request\_method\_count |
| gce\_instance/agent | Коды ответов | Количество | agent.googleapis.com/couchdb/httpd/response\_code\_count |
| gce\_instance/agent | Временные чтения представлений | Количество | agent.googleapis.com/couchdb/httpd/temporary\_view\_read\_count |
| gce\_instance/agent | Чтения представлений | Количество | agent.googleapis.com/couchdb/httpd/view\_read\_count |
| gce\_instance/agent | Открытые базы данных | Количество | agent.googleapis.com/couchdb/open\_databases |
| gce\_instance/agent | Открытые файлы | Количество | agent.googleapis.com/couchdb/open\_files |
| gce\_instance/agent | Чтения | Количество | agent.googleapis.com/couchdb/read\_count |
| gce\_instance/agent | Записи | Количество | agent.googleapis.com/couchdb/write\_count |
| gce\_instance/agent | Нагрузка CPU (15 мин) | Количество | agent.googleapis.com/cpu/load\_15m |
| gce\_instance/agent | Нагрузка CPU (1 мин) | Количество | agent.googleapis.com/cpu/load\_1m |
| gce\_instance/agent | Нагрузка CPU (5 мин) | Количество | agent.googleapis.com/cpu/load\_5m |
| gce\_instance/agent | Использование CPU | Секунда | agent.googleapis.com/cpu/usage\_time |
| gce\_instance/agent | Утилизация CPU | Процент | agent.googleapis.com/cpu/utilization |
| gce\_instance/agent | Использование диска | Байт | agent.googleapis.com/disk/bytes\_used |
| gce\_instance/agent | Время ввода/вывода диска | Миллисекунда | agent.googleapis.com/disk/io\_time |
| gce\_instance/agent | Объединённые дисковые операции | Количество | agent.googleapis.com/disk/merged\_operations |
| gce\_instance/agent | Дисковые операции | Количество | agent.googleapis.com/disk/operation\_count |
| gce\_instance/agent | Время дисковой операции | Миллисекунда | agent.googleapis.com/disk/operation\_time |
| gce\_instance/agent | Ожидающие дисковые операции | Количество | agent.googleapis.com/disk/pending\_operations |
| gce\_instance/agent | Утилизация диска | Процент | agent.googleapis.com/disk/percent\_used |
| gce\_instance/agent | Байты чтения диска | Байт | agent.googleapis.com/disk/read\_bytes\_count |
| gce\_instance/agent | Взвешенное время ввода/вывода диска | Миллисекунда | agent.googleapis.com/disk/weighted\_io\_time |
| gce\_instance/agent | Байты записи диска | Байт | agent.googleapis.com/disk/write\_bytes\_count |
| gce\_instance/agent | Размер кэша | Байт | agent.googleapis.com/elasticsearch/cache\_memory\_usage |
| gce\_instance/agent | Вытеснения полей | Количество | agent.googleapis.com/elasticsearch/field\_eviction\_count |
| gce\_instance/agent | Вытеснения фильтров | Количество | agent.googleapis.com/elasticsearch/filter\_cache\_eviction\_count |
| gce\_instance/agent | Количество сборок мусора | Количество | agent.googleapis.com/elasticsearch/gc\_collection\_count |
| gce\_instance/agent | Использование памяти | Байт | agent.googleapis.com/elasticsearch/memory\_usage |
| gce\_instance/agent | Сетевой трафик | Байт | agent.googleapis.com/elasticsearch/network |
| gce\_instance/agent | Документы | Количество | agent.googleapis.com/elasticsearch/num\_current\_documents |
| gce\_instance/agent | Узлы данных | Количество | agent.googleapis.com/elasticsearch/num\_data\_nodes |
| gce\_instance/agent | Открытые соединения | Количество | agent.googleapis.com/elasticsearch/num\_http\_connections |
| gce\_instance/agent | Узлы | Количество | agent.googleapis.com/elasticsearch/num\_nodes |
| gce\_instance/agent | Открытые файлы | Количество | agent.googleapis.com/elasticsearch/num\_open\_files |
| gce\_instance/agent | Открытые соединения | Количество | agent.googleapis.com/elasticsearch/num\_server\_connections |
| gce\_instance/agent | Шарды | Количество | agent.googleapis.com/elasticsearch/num\_shards |
| gce\_instance/agent | Завершённые операции | Количество | agent.googleapis.com/elasticsearch/operation\_count |
| gce\_instance/agent | Время операции | Миллисекунда | agent.googleapis.com/elasticsearch/operation\_time |
| gce\_instance/agent | Максимальное количество потоков | Количество | agent.googleapis.com/elasticsearch/peak\_threads |
| gce\_instance/agent | Размер хранилища | Байт | agent.googleapis.com/elasticsearch/storage\_size |
| gce\_instance/agent | Потоки | Количество | agent.googleapis.com/elasticsearch/threads |
| gce\_instance/agent | IPC-соединения | Количество | agent.googleapis.com/hbase/ipc/connections |
| gce\_instance/agent | Размер очереди IPC | Количество | agent.googleapis.com/hbase/ipc/queue\_length |
| gce\_instance/agent | IPC-трафик | Байт | agent.googleapis.com/hbase/ipc/traffic\_count |
| gce\_instance/agent | Нагрузка | Количество | agent.googleapis.com/hbase/master/average\_load |
| gce\_instance/agent | Неактивные серверы регионов | Количество | agent.googleapis.com/hbase/master/dead\_region\_servers |
| gce\_instance/agent | Активные серверы регионов | Количество | agent.googleapis.com/hbase/master/live\_region\_servers |
| gce\_instance/agent | Обращения к блочному кэшу | Количество | agent.googleapis.com/hbase/regionserver/block\_cache/access\_count |
| gce\_instance/agent | Количество вытесненных блоков | Количество | agent.googleapis.com/hbase/regionserver/block\_cache/evicted\_blocks\_count |
| gce\_instance/agent | Процент попаданий в блочный кэш | Процент | agent.googleapis.com/hbase/regionserver/block\_cache/hit\_ratio\_percent |
| gce\_instance/agent | Размер блочного кэша | Байт | agent.googleapis.com/hbase/regionserver/block\_cache/memory |
| gce\_instance/agent | Количество блоков | Количество | agent.googleapis.com/hbase/regionserver/block\_cache/num\_items |
| gce\_instance/agent | Размер очереди вызовов | Количество | agent.googleapis.com/hbase/regionserver/call\_queue/length |
| gce\_instance/agent | Размер очереди компактизации | Количество | agent.googleapis.com/hbase/regionserver/compaction\_queue/length |
| gce\_instance/agent | Размер очереди сброса | Количество | agent.googleapis.com/hbase/regionserver/flush\_queue/length |
| gce\_instance/agent | Использование кучи | Байт | agent.googleapis.com/hbase/regionserver/memory/heap\_usage |
| gce\_instance/agent | Файлы memstore | Количество | agent.googleapis.com/hbase/regionserver/memstore/files |
| gce\_instance/agent | Размер индекса memstore | Байт | agent.googleapis.com/hbase/regionserver/memstore/index\_size |
| gce\_instance/agent | Открытые хранилища memstore | Количество | agent.googleapis.com/hbase/regionserver/memstore/open\_stores |
| gce\_instance/agent | Размер memstore | Байт | agent.googleapis.com/hbase/regionserver/memstore/size |
| gce\_instance/agent | Онлайн-регионы | Количество | agent.googleapis.com/hbase/regionserver/online\_regions |
| gce\_instance/agent | Количество запросов | Количество | agent.googleapis.com/hbase/regionserver/request\_count |
| gce\_instance/agent | Частота RPC-запросов | В секунду | agent.googleapis.com/hbase/regionserver/requests/total\_rate |
| gce\_instance/agent | Медленные операции | Количество | agent.googleapis.com/hbase/regionserver/slow\_operation\_count |
| gce\_instance/agent | Средняя задержка пакетов Thrift | Наносекунда | agent.googleapis.com/hbase/thrift/batch\_latency/average |
| gce\_instance/agent | Средняя задержка вызовов Thrift | Наносекунда | agent.googleapis.com/hbase/thrift/call\_latency/average |
| gce\_instance/agent | Размер очереди вызовов Thrift | Количество | agent.googleapis.com/hbase/thrift/call\_queue/length |
| gce\_instance/agent | Средняя задержка медленных вызовов Thrift | Наносекунда | agent.googleapis.com/hbase/thrift/slow\_call\_latency/average |
| gce\_instance/agent | Среднее время в очереди Thrift | Наносекунда | agent.googleapis.com/hbase/thrift/time\_in\_queue/average |
| gce\_instance/agent | Открытые соединения IIS | Количество | agent.googleapis.com/iis/current\_connections |
| gce\_instance/agent | Переданные байты IIS | Байт | agent.googleapis.com/iis/network/transferred\_bytes\_count |
| gce\_instance/agent | Соединения IIS | Количество | agent.googleapis.com/iis/new\_connection\_count |
| gce\_instance/agent | Запросы IIS | Количество | agent.googleapis.com/iis/request\_count |
| gce\_instance/agent | Сетевые ошибки | Количество | agent.googleapis.com/interface/errors |
| gce\_instance/agent | Сетевые пакеты | Количество | agent.googleapis.com/interface/packets |
| gce\_instance/agent | Сетевой трафик | Байт | agent.googleapis.com/interface/traffic |
| gce\_instance/agent | Количество сборок мусора | Количество | agent.googleapis.com/jvm/gc/count |
| gce\_instance/agent | Время сборки мусора | Миллисекунда | agent.googleapis.com/jvm/gc/time |
| gce\_instance/agent | Использование памяти | Байт | agent.googleapis.com/jvm/memory/usage |
| gce\_instance/agent | Время CPU | Наносекунда | agent.googleapis.com/jvm/os/cpu\_time |
| gce\_instance/agent | Открытые файлы | Количество | agent.googleapis.com/jvm/os/open\_files |
| gce\_instance/agent | Потоки-демоны | Количество | agent.googleapis.com/jvm/thread/num\_daemon |
| gce\_instance/agent | Потоки | Количество | agent.googleapis.com/jvm/thread/num\_live |
| gce\_instance/agent | Максимальное количество потоков | Количество | agent.googleapis.com/jvm/thread/peak |
| gce\_instance/agent | Время работы | Миллисекунда | agent.googleapis.com/jvm/uptime |
| gce\_instance/agent | Неудачные запросы | Количество | agent.googleapis.com/kafka/broker/topics/failed\_request\_count |
| gce\_instance/agent | Входящие сообщения | Количество | agent.googleapis.com/kafka/broker/topics/incoming\_message\_count |
| gce\_instance/agent | Трафик | Байт | agent.googleapis.com/kafka/broker/topics/traffic |
| gce\_instance/agent | Активные контроллеры | Количество | agent.googleapis.com/kafka/controller/kafka/active |
| gce\_instance/agent | Офлайн-разделы | Количество | agent.googleapis.com/kafka/controller/kafka/offline\_partitions |
| gce\_instance/agent | Выборы лидеров | Количество | agent.googleapis.com/kafka/controller/leader\_elections/election\_count |
| gce\_instance/agent | Выборы лидеров с устаревшими данными | Количество | agent.googleapis.com/kafka/controller/leader\_elections/unclean\_count |
| gce\_instance/agent | Сбросы | Количество | agent.googleapis.com/kafka/log/flush\_count |
| gce\_instance/agent | Запросы | Количество | agent.googleapis.com/kafka/network/request\_count |
| gce\_instance/agent | Отложенные запросы чистилища | Количество | agent.googleapis.com/kafka/purgatory/num\_delayed\_requests |
| gce\_instance/agent | Запросы чистилища | Количество | agent.googleapis.com/kafka/purgatory/size |
| gce\_instance/agent | Максимальное отставание | Количество | agent.googleapis.com/kafka/replica\_fetcher/max\_lag |
| gce\_instance/agent | Минимальная частота выборки | В секунду | agent.googleapis.com/kafka/replica\_fetcher/min\_fetch\_rate |
| gce\_instance/agent | Получающие реплики | Количество | agent.googleapis.com/kafka/replica\_manager/isr/expand\_count |
| gce\_instance/agent | Отстающие реплики | Количество | agent.googleapis.com/kafka/replica\_manager/isr/shrink\_count |
| gce\_instance/agent | Лидеры | Количество | agent.googleapis.com/kafka/replica\_manager/leaders |
| gce\_instance/agent | Разделы | Количество | agent.googleapis.com/kafka/replica\_manager/partitions |
| gce\_instance/agent | Ненадёжные разделы | Количество | agent.googleapis.com/kafka/replica\_manager/under\_replicated\_partitions |
| gce\_instance/agent | Команды | Количество | agent.googleapis.com/memcached/command\_count |
| gce\_instance/agent | Соединения | Количество | agent.googleapis.com/memcached/current\_connections |
| gce\_instance/agent | Элементы | Количество | agent.googleapis.com/memcached/current\_items |
| gce\_instance/agent | Вытеснения | Количество | agent.googleapis.com/memcached/eviction\_count |
| gce\_instance/agent | Использование памяти | Байт | agent.googleapis.com/memcached/memory |
| gce\_instance/agent | Трафик | Байт | agent.googleapis.com/memcached/network |
| gce\_instance/agent | Операции | Количество | agent.googleapis.com/memcached/operation\_count |
| gce\_instance/agent | Процент попаданий | Процент | agent.googleapis.com/memcached/operation\_hitratio |
| gce\_instance/agent | Время CPU | Секунда | agent.googleapis.com/memcached/rusage |
| gce\_instance/agent | Потоки | Количество | agent.googleapis.com/memcached/threads |
| gce\_instance/agent | Использование памяти | Байт | agent.googleapis.com/memory/bytes\_used |
| gce\_instance/agent | Утилизация памяти | Процент | agent.googleapis.com/memory/percent\_used |
| gce\_instance/agent | Попадания в кэш | Количество | agent.googleapis.com/mongodb/cache/hits |
| gce\_instance/agent | Промахи кэша | Количество | agent.googleapis.com/mongodb/cache/misses |
| gce\_instance/agent | Коллекции | Количество | agent.googleapis.com/mongodb/collections |
| gce\_instance/agent | Соединения | Количество | agent.googleapis.com/mongodb/connections |
| gce\_instance/agent | Размер данных | Байт | agent.googleapis.com/mongodb/data\_size |
| gce\_instance/agent | Экстенты | Количество | agent.googleapis.com/mongodb/extents |
| gce\_instance/agent | Время удержания глобальной блокировки | Миллисекунда | agent.googleapis.com/mongodb/global\_lock\_hold\_time |
| gce\_instance/agent | Размер индекса | Байт | agent.googleapis.com/mongodb/index\_size |
| gce\_instance/agent | Индексы | Количество | agent.googleapis.com/mongodb/indexes |
| gce\_instance/agent | Использование памяти | МебиБайт | agent.googleapis.com/mongodb/memory\_usage |
| gce\_instance/agent | Объекты | Количество | agent.googleapis.com/mongodb/objects |
| gce\_instance/agent | Операции | Количество | agent.googleapis.com/mongodb/operation\_count |
| gce\_instance/agent | Размер хранилища | Байт | agent.googleapis.com/mongodb/storage\_size |
| gce\_instance/agent | Открытые соединения SQL Server | Количество | agent.googleapis.com/mssql/connections/user |
| gce\_instance/agent | Частота транзакций SQL Server | В секунду | agent.googleapis.com/mssql/transaction\_rate |
| gce\_instance/agent | Частота транзакций записи SQL Server | В секунду | agent.googleapis.com/mssql/write\_transaction\_rate |
| gce\_instance/agent | Страницы пула буферов | Количество | agent.googleapis.com/mysql/buffer\_pool/num\_pages |
| gce\_instance/agent | Операции пула буферов | Количество | agent.googleapis.com/mysql/buffer\_pool/operation\_count |
| gce\_instance/agent | Размер пула буферов | Байт | agent.googleapis.com/mysql/buffer\_pool\_size |
| gce\_instance/agent | Команды | Количество | agent.googleapis.com/mysql/command\_count |
| gce\_instance/agent | Обработчики | Количество | agent.googleapis.com/mysql/handler\_count |
| gce\_instance/agent | Двойная запись InnoDB | Количество | agent.googleapis.com/mysql/innodb/doublewrite\_count |
| gce\_instance/agent | Операции с журналом InnoDB | Количество | agent.googleapis.com/mysql/innodb/log\_operation\_count |
| gce\_instance/agent | Операции InnoDB | Количество | agent.googleapis.com/mysql/innodb/operation\_count |
| gce\_instance/agent | Операции со страницами InnoDB | Количество | agent.googleapis.com/mysql/innodb/page\_operation\_count |
| gce\_instance/agent | Блокировки InnoDB | Количество | agent.googleapis.com/mysql/innodb/row\_lock\_count |
| gce\_instance/agent | Строковые операции InnoDB | Количество | agent.googleapis.com/mysql/innodb/row\_operation\_count |
| gce\_instance/agent | Блокировки | Количество | agent.googleapis.com/mysql/lock\_count |
| gce\_instance/agent | Операции QCache | Количество | agent.googleapis.com/mysql/qcache/operation\_count |
| gce\_instance/agent | Запросы QCache | Количество | agent.googleapis.com/mysql/qcache/query\_count |
| gce\_instance/agent | Задержка репликации | Секунда | agent.googleapis.com/mysql/slave\_replication\_lag |
| gce\_instance/agent | Сортировки | Количество | agent.googleapis.com/mysql/sort\_count |
| gce\_instance/agent | Потоки | Количество | agent.googleapis.com/mysql/thread\_count |
| gce\_instance/agent | TCP-соединения | Количество | agent.googleapis.com/network/tcp\_connections |
| gce\_instance/agent | Принятые соединения | Количество | agent.googleapis.com/nginx/connections/accepted\_count |
| gce\_instance/agent | Активные соединения | Количество | agent.googleapis.com/nginx/connections/current |
| gce\_instance/agent | Обработанные соединения | Количество | agent.googleapis.com/nginx/connections/handled\_count |
| gce\_instance/agent | Запросы | Количество | agent.googleapis.com/nginx/request\_count |
| gce\_instance/agent | Утилизация файла подкачки | Процент | agent.googleapis.com/pagefile/percent\_used |
| gce\_instance/agent | Прочитанные блоки | Количество | agent.googleapis.com/postgresql/blocks\_read\_count |
| gce\_instance/agent | Фиксации | Количество | agent.googleapis.com/postgresql/commit\_count |
| gce\_instance/agent | Размер БД | Байт | agent.googleapis.com/postgresql/db\_size |
| gce\_instance/agent | Обработчики | Количество | agent.googleapis.com/postgresql/num\_backends |
| gce\_instance/agent | Строки БД | Количество | agent.googleapis.com/postgresql/num\_tuples |
| gce\_instance/agent | Операции | Количество | agent.googleapis.com/postgresql/operation\_count |
| gce\_instance/agent | Откаты | Количество | agent.googleapis.com/postgresql/rollback\_count |
| gce\_instance/agent | Процессы | Количество | agent.googleapis.com/processes/count\_by\_state |
| gce\_instance/agent | CPU процессов | Секунда | agent.googleapis.com/processes/cpu\_time |
| gce\_instance/agent | Чтение с диска процессами | Байт | agent.googleapis.com/processes/disk/read\_bytes\_count |
| gce\_instance/agent | Запись на диск процессами | Байт | agent.googleapis.com/processes/disk/write\_bytes\_count |
| gce\_instance/agent | Количество форков | Количество | agent.googleapis.com/processes/fork\_count |
| gce\_instance/agent | Резидентная память процессов | Байт | agent.googleapis.com/processes/rss\_usage |
| gce\_instance/agent | Виртуальная память процессов | Байт | agent.googleapis.com/processes/vm\_usage |
| gce\_instance/agent | Потребители | Количество | agent.googleapis.com/rabbitmq/consumers |
| gce\_instance/agent | Частота доставки | В секунду | agent.googleapis.com/rabbitmq/delivery\_rate |
| gce\_instance/agent | Сообщения | Количество | agent.googleapis.com/rabbitmq/num\_messages |
| gce\_instance/agent | Частота публикации | В секунду | agent.googleapis.com/rabbitmq/publish\_rate |
| gce\_instance/agent | Несохранённые изменения | Количество | agent.googleapis.com/redis/changes\_since\_last\_save |
| gce\_instance/agent | Заблокированные клиенты | Количество | agent.googleapis.com/redis/clients/blocked |
| gce\_instance/agent | Подключённые клиенты | Количество | agent.googleapis.com/redis/clients/connected |
| gce\_instance/agent | Команды | Количество | agent.googleapis.com/redis/commands\_processed |
| gce\_instance/agent | Соединения реплик | Количество | agent.googleapis.com/redis/connections/slaves |
| gce\_instance/agent | Соединения | Количество | agent.googleapis.com/redis/connections/total |
| gce\_instance/agent | Истёкшие ключи | Количество | agent.googleapis.com/redis/expired\_keys |
| gce\_instance/agent | Использование памяти | Байт | agent.googleapis.com/redis/memory/usage |
| gce\_instance/agent | Использование памяти Lua | Байт | agent.googleapis.com/redis/memory/usage\_lua |
| gce\_instance/agent | Каналы PubSub | Количество | agent.googleapis.com/redis/pubsub/channels |
| gce\_instance/agent | Шаблоны PubSub | Количество | agent.googleapis.com/redis/pubsub/patterns |
| gce\_instance/agent | Время работы | Секунда | agent.googleapis.com/redis/uptime |
| gce\_instance/agent | Задержка 95% (1 мин) | Микросекунда | agent.googleapis.com/riak/latency/95th\_percentile |
| gce\_instance/agent | Средняя задержка (1 мин) | Микросекунда | agent.googleapis.com/riak/latency/average |
| gce\_instance/agent | Максимальная задержка (1 мин) | Микросекунда | agent.googleapis.com/riak/latency/maximum |
| gce\_instance/agent | Использование памяти | Байт | agent.googleapis.com/riak/memory\_usage |
| gce\_instance/agent | 95% смежных объектов (1 мин) | Количество | agent.googleapis.com/riak/num\_siblings/95th\_percentile |
| gce\_instance/agent | Среднее количество смежных объектов (1 мин) | Количество | agent.googleapis.com/riak/num\_siblings/average |
| gce\_instance/agent | Максимальное количество смежных объектов (1 мин) | Количество | agent.googleapis.com/riak/num\_siblings/maximum |
| gce\_instance/agent | 95% размера объекта (1 мин) | Байт | agent.googleapis.com/riak/object\_size/95th\_percentile |
| gce\_instance/agent | Средний размер объекта (1 мин) | Байт | agent.googleapis.com/riak/object\_size/average |
| gce\_instance/agent | Максимальный размер объекта (1 мин) | Байт | agent.googleapis.com/riak/object\_size/maximum |
| gce\_instance/agent | Операции | Количество | agent.googleapis.com/riak/operation\_count |
| gce\_instance/agent | Использование подкачки | Байт | agent.googleapis.com/swap/bytes\_used |
| gce\_instance/agent | Операции ввода/вывода подкачки | Количество | agent.googleapis.com/swap/io |
| gce\_instance/agent | Утилизация подкачки | Процент | agent.googleapis.com/swap/percent\_used |
| gce\_instance/agent | Сессии | Количество | agent.googleapis.com/tomcat/manager/sessions |
| gce\_instance/agent | Ошибки | Количество | agent.googleapis.com/tomcat/request\_processor/error\_count |
| gce\_instance/agent | Время обработки | Миллисекунда | agent.googleapis.com/tomcat/request\_processor/processing\_time |
| gce\_instance/agent | Запросы | Количество | agent.googleapis.com/tomcat/request\_processor/request\_count |
| gce\_instance/agent | Трафик | Байт | agent.googleapis.com/tomcat/request\_processor/traffic\_count |
| gce\_instance/agent | Занятые потоки | Количество | agent.googleapis.com/tomcat/threads/busy |
| gce\_instance/agent | Текущие потоки | Количество | agent.googleapis.com/tomcat/threads/current |
| gce\_instance/agent | Успешные соединения с бэкендом | Количество | agent.googleapis.com/varnish/backend\_connection\_count |
| gce\_instance/agent | Операции с кэшем | Количество | agent.googleapis.com/varnish/cache\_operation\_count |
| gce\_instance/agent | Клиентские соединения | Количество | agent.googleapis.com/varnish/client\_connection\_count |
| gce\_instance/agent | Открытые соединения | Количество | agent.googleapis.com/zookeeper/connections\_count |
| gce\_instance/agent | Размер данных | Байт | agent.googleapis.com/zookeeper/data\_size |
| gce\_instance/agent | Последователи | Количество | agent.googleapis.com/zookeeper/followers/count |
| gce\_instance/agent | Синхронизированные последователи | Количество | agent.googleapis.com/zookeeper/followers/synced\_count |
| gce\_instance/agent | Полученные пакеты | Количество | agent.googleapis.com/zookeeper/network/received\_packets\_count |
| gce\_instance/agent | Отправленные пакеты | Количество | agent.googleapis.com/zookeeper/network/sent\_packets\_count |
| gce\_instance/agent | Узлы | Количество | agent.googleapis.com/zookeeper/nodes/count |
| gce\_instance/agent | Эфемерные узлы | Количество | agent.googleapis.com/zookeeper/nodes/ephemeral\_count |
| gce\_instance/agent | Наблюдатели | Количество | agent.googleapis.com/zookeeper/nodes/watches\_count |
| gce\_instance/agent | Средняя задержка запроса | Миллисекунда | agent.googleapis.com/zookeeper/requests/latency/average |
| gce\_instance/agent | Максимальная задержка запроса | Миллисекунда | agent.googleapis.com/zookeeper/requests/latency/maximum |
| gce\_instance/agent | Минимальная задержка запроса | Миллисекунда | agent.googleapis.com/zookeeper/requests/latency/minimum |
| gce\_instance/agent | Ожидающие запросы | Количество | agent.googleapis.com/zookeeper/requests/outstanding\_count |
| gce\_instance/agent | Ожидающие синхронизации | Количество | agent.googleapis.com/zookeeper/sync\_operations/pending\_count |
| gce\_instance/firewallinsights | Количество срабатываний брандмауэра ВМ | Количество | firewallinsights.googleapis.com/vm/firewall\_hit\_count |
| gce\_instance/firewallinsights | Временная метка последнего использования брандмауэра ВМ | Количество | firewallinsights.googleapis.com/vm/firewall\_last\_used\_timestamp |
| gce\_instance/istio | Количество закрытых клиентских соединений | Байт | istio.io/service/client/connection\_close\_count |
| gce\_instance/istio | Количество открытых клиентских соединений | Байт | istio.io/service/client/connection\_open\_count |
| gce\_instance/istio | Количество полученных байт клиентом | Байт | istio.io/service/client/received\_bytes\_count |
| gce\_instance/istio | Байты клиентских запросов | Байт | istio.io/service/client/request\_bytes |
| gce\_instance/istio | Количество клиентских запросов | Количество | istio.io/service/client/request\_count |
| gce\_instance/istio | Байты клиентских ответов | Байт | istio.io/service/client/response\_bytes |
| gce\_instance/istio | Задержки обхода клиента | Миллисекунда | istio.io/service/client/roundtrip\_latencies |
| gce\_instance/istio | Количество отправленных байт клиентом | Байт | istio.io/service/client/sent\_bytes\_count |
| gce\_instance/istio | Количество закрытых серверных соединений | Байт | istio.io/service/server/connection\_close\_count |
| gce\_instance/istio | Количество открытых серверных соединений | Байт | istio.io/service/server/connection\_open\_count |
| gce\_instance/istio | Количество полученных байт сервером | Байт | istio.io/service/server/received\_bytes\_count |
| gce\_instance/istio | Байты серверных запросов | Байт | istio.io/service/server/request\_bytes |
| gce\_instance/istio | Количество серверных запросов | Количество | istio.io/service/server/request\_count |
| gce\_instance/istio | Байты серверных ответов | Байт | istio.io/service/server/response\_bytes |
| gce\_instance/istio | Задержки серверных ответов | Миллисекунда | istio.io/service/server/response\_latencies |
| gce\_instance/istio | Количество отправленных байт сервером | Байт | istio.io/service/server/sent\_bytes\_count |
| gce\_instance\_vm\_flow/default\_metrics | Исходящие байты | Байт | networking.googleapis.com/vm\_flow/egress\_bytes\_count |
| gce\_instance\_vm\_flow/default\_metrics | Входящие байты | Байт | networking.googleapis.com/vm\_flow/ingress\_bytes\_count |
| gce\_instance\_vm\_flow/default\_metrics | Задержки RTT | Миллисекунда | networking.googleapis.com/vm\_flow/rtt |
| instance\_group/default\_metrics | Размер группы экземпляров | Количество | compute.googleapis.com/instance\_group/size |
| autoscaler/default\_metrics | Пропускная способность обслуживания | Количество | autoscaler.googleapis.com/capacity |
| autoscaler/default\_metrics | Текущая утилизация автомасштабировщика | Количество | autoscaler.googleapis.com/current\_utilization |
| tpu\_worker/default\_metrics | Утилизация CPU контейнера | Процент | tpu.googleapis.com/container/cpu/utilization |
| tpu\_worker/default\_metrics | Использование памяти контейнера | Байт | tpu.googleapis.com/container/memory/usage |
| tpu\_worker/default\_metrics | Утилизация CPU | Процент | tpu.googleapis.com/cpu/utilization |
| tpu\_worker/default\_metrics | Использование памяти | Байт | tpu.googleapis.com/memory/usage |
| tpu\_worker/default\_metrics | Полученные байты сети | Байт | tpu.googleapis.com/network/received\_bytes\_count |
| tpu\_worker/default\_metrics | Отправленные байты сети | Байт | tpu.googleapis.com/network/sent\_bytes\_count |
| tpu\_worker/default\_metrics | Утилизация MXU | Процент | tpu.googleapis.com/tpu/mxu/utilization |

## Связанные темы

* [Интеграции Google Cloud](../../gcp-integrations.md "Настройте и сконфигурируйте Dynatrace на Google Cloud.")
