---
title: Мониторинг Google Compute Engine с метриками Operations suite
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/google-compute-engine/compute-engine-monitoring
scraped: 2026-03-04T21:35:51.753899
---

* 18 мин. чтения

Интеграция Dynatrace с Google Cloud использует данные, собранные из Google Operations API, для непрерывного мониторинга работоспособности и производительности сервисов Google Cloud. Помимо объединения всех релевантных данных в дашборды, она также обеспечивает оповещения и отслеживание событий.

## Предварительные требования

Настройка интеграции

## Добавление сервисов и наборов функций Необязательно

После интеграции Dynatrace автоматически начинает мониторинг ряда предустановленных сервисов Google Cloud и наборов функций (метрик). Помимо них, вы можете добавить дополнительные сервисы или наборы функций для мониторинга. Подробнее см. в разделе [Добавление и удаление сервисов](../gcp-guide/deploy-k8.md#manage "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.").

Список наборов функций, доступных для данного сервиса, см. в разделе [Таблица метрик](#table).

## Просмотр метрик

После развёртывания интеграции вы можете просматривать метрики отслеживаемых сервисов в браузере метрик, Data Explorer, а также в плитках дашбордов.

## Таблица метрик

Для Google Compute Engine доступны следующие наборы функций.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| gce\_instance/default\_metrics | Отброшенные байты | Byte | compute.googleapis.com/firewall/dropped\_bytes\_count |
| gce\_instance/default\_metrics | Отброшенные пакеты | Count | compute.googleapis.com/firewall/dropped\_packets\_count |
| gce\_instance/default\_metrics | Количество задач в очереди выполнения | Count | compute.googleapis.com/guest/cpu/runnable\_task\_count |
| gce\_instance/default\_metrics | Использование CPU | Second | compute.googleapis.com/guest/cpu/usage\_time |
| gce\_instance/default\_metrics | Использование диска в байтах | Byte | compute.googleapis.com/guest/disk/bytes\_used |
| gce\_instance/default\_metrics | Время ввода/вывода | MilliSecond | compute.googleapis.com/guest/disk/io\_time |
| gce\_instance/default\_metrics | Объединённые дисковые операции | Count | compute.googleapis.com/guest/disk/merged\_operation\_count |
| gce\_instance/default\_metrics | Переданные байты диска | Byte | compute.googleapis.com/guest/disk/operation\_bytes\_count |
| gce\_instance/default\_metrics | Дисковые операции | Count | compute.googleapis.com/guest/disk/operation\_count |
| gce\_instance/default\_metrics | Время дисковой операции | MilliSecond | compute.googleapis.com/guest/disk/operation\_time |
| gce\_instance/default\_metrics | Длина очереди | Count | compute.googleapis.com/guest/disk/queue\_length |
| gce\_instance/default\_metrics | Взвешенное время ввода/вывода | MilliSecond | compute.googleapis.com/guest/disk/weighted\_io\_time |
| gce\_instance/default\_metrics | Использование анонимной памяти в байтах | Byte | compute.googleapis.com/guest/memory/anonymous\_used |
| gce\_instance/default\_metrics | Использование памяти в байтах | Byte | compute.googleapis.com/guest/memory/bytes\_used |
| gce\_instance/default\_metrics | Использование грязных страниц в байтах | Byte | compute.googleapis.com/guest/memory/dirty\_used |
| gce\_instance/default\_metrics | Использование кэш-памяти страниц в байтах | Byte | compute.googleapis.com/guest/memory/page\_cache\_used |
| gce\_instance/default\_metrics | Использование невытесняемой памяти в байтах | Byte | compute.googleapis.com/guest/memory/unevictable\_used |
| gce\_instance/default\_metrics | Количество проблем | Count | compute.googleapis.com/guest/system/problem\_count |
| gce\_instance/default\_metrics | Состояние проблемы | Count | compute.googleapis.com/guest/system/problem\_state |
| gce\_instance/default\_metrics | Время работы | Second | compute.googleapis.com/guest/system/uptime |
| gce\_instance/default\_metrics | Зарезервированные vCPU | Count | compute.googleapis.com/instance/cpu/reserved\_cores |
| gce\_instance/default\_metrics | Время ожидания планировщика | Second | compute.googleapis.com/instance/cpu/scheduler\_wait\_time |
| gce\_instance/default\_metrics | Использование CPU | Second | compute.googleapis.com/instance/cpu/usage\_time |
| gce\_instance/default\_metrics | Утилизация CPU | Percent | compute.googleapis.com/instance/cpu/utilization |
| gce\_instance/default\_metrics | Пиковые байты чтения диска | Byte | compute.googleapis.com/instance/disk/max\_read\_bytes\_count |
| gce\_instance/default\_metrics | Пиковые операции чтения диска | Count | compute.googleapis.com/instance/disk/max\_read\_ops\_count |
| gce\_instance/default\_metrics | Пиковые байты записи диска | Byte | compute.googleapis.com/instance/disk/max\_write\_bytes\_count |
| gce\_instance/default\_metrics | Пиковые операции записи диска | Count | compute.googleapis.com/instance/disk/max\_write\_ops\_count |
| gce\_instance/default\_metrics | Байты чтения диска | Byte | compute.googleapis.com/instance/disk/read\_bytes\_count |
| gce\_instance/default\_metrics | Операции чтения диска | Count | compute.googleapis.com/instance/disk/read\_ops\_count |
| gce\_instance/default\_metrics | Ограниченные байты чтения | Byte | compute.googleapis.com/instance/disk/throttled\_read\_bytes\_count |
| gce\_instance/default\_metrics | Ограниченные операции чтения | Count | compute.googleapis.com/instance/disk/throttled\_read\_ops\_count |
| gce\_instance/default\_metrics | Ограниченные байты записи | Byte | compute.googleapis.com/instance/disk/throttled\_write\_bytes\_count |
| gce\_instance/default\_metrics | Ограниченные операции записи | Count | compute.googleapis.com/instance/disk/throttled\_write\_ops\_count |
| gce\_instance/default\_metrics | Байты записи диска | Byte | compute.googleapis.com/instance/disk/write\_bytes\_count |
| gce\_instance/default\_metrics | Операции записи диска | Count | compute.googleapis.com/instance/disk/write\_ops\_count |
| gce\_instance/default\_metrics | Проверка при раннем запуске | Count | compute.googleapis.com/instance/integrity/early\_boot\_validation\_status |
| gce\_instance/default\_metrics | Проверка при позднем запуске | Count | compute.googleapis.com/instance/integrity/late\_boot\_validation\_status |
| gce\_instance/default\_metrics | Общий объём памяти ВМ | Byte | compute.googleapis.com/instance/memory/balloon/ram\_size |
| gce\_instance/default\_metrics | Используемая память ВМ | Byte | compute.googleapis.com/instance/memory/balloon/ram\_used |
| gce\_instance/default\_metrics | Замена памяти ВМ (входящий) | Byte | compute.googleapis.com/instance/memory/balloon/swap\_in\_bytes\_count |
| gce\_instance/default\_metrics | Замена памяти ВМ (исходящий) | Byte | compute.googleapis.com/instance/memory/balloon/swap\_out\_bytes\_count |
| gce\_instance/default\_metrics | Полученные байты | Byte | compute.googleapis.com/instance/network/received\_bytes\_count |
| gce\_instance/default\_metrics | Полученные пакеты | Count | compute.googleapis.com/instance/network/received\_packets\_count |
| gce\_instance/default\_metrics | Отправленные байты | Byte | compute.googleapis.com/instance/network/sent\_bytes\_count |
| gce\_instance/default\_metrics | Отправленные пакеты | Count | compute.googleapis.com/instance/network/sent\_packets\_count |
| gce\_instance/default\_metrics | Время работы | Second | compute.googleapis.com/instance/uptime |
| gce\_instance/default\_metrics | Общее время работы | Second | compute.googleapis.com/instance/uptime\_total |
| gce\_instance/default\_metrics | Отброшенные пакеты | Count | compute.googleapis.com/mirroring/dropped\_packets\_count |
| gce\_instance/default\_metrics | Зеркалированные байты | Byte | compute.googleapis.com/mirroring/mirrored\_bytes\_count |
| gce\_instance/default\_metrics | Зеркалированные пакеты | Count | compute.googleapis.com/mirroring/mirrored\_packets\_count |
| gce\_instance/default\_metrics | Выделенные порты | Unspecified | compute.googleapis.com/nat/allocated\_ports |
| gce\_instance/default\_metrics | Количество закрытых соединений | Unspecified | compute.googleapis.com/nat/closed\_connections\_count |
| gce\_instance/default\_metrics | Количество отброшенных входящих пакетов | Unspecified | compute.googleapis.com/nat/dropped\_received\_packets\_count |
| gce\_instance/default\_metrics | Количество отброшенных исходящих пакетов | Unspecified | compute.googleapis.com/nat/dropped\_sent\_packets\_count |
| gce\_instance/default\_metrics | Количество новых соединений | Unspecified | compute.googleapis.com/nat/new\_connections\_count |
| gce\_instance/default\_metrics | Открытые соединения | Unspecified | compute.googleapis.com/nat/open\_connections |
| gce\_instance/default\_metrics | Использование портов | Unspecified | compute.googleapis.com/nat/port\_usage |
| gce\_instance/default\_metrics | Количество полученных байт | Byte | compute.googleapis.com/nat/received\_bytes\_count |
| gce\_instance/default\_metrics | Количество полученных пакетов | Unspecified | compute.googleapis.com/nat/received\_packets\_count |
| gce\_instance/default\_metrics | Количество отправленных байт | Byte | compute.googleapis.com/nat/sent\_bytes\_count |
| gce\_instance/default\_metrics | Количество отправленных пакетов | Unspecified | compute.googleapis.com/nat/sent\_packets\_count |
| gce\_instance/agent | Количество запросов API агента мониторинга | Count | agent.googleapis.com/agent/api\_request\_count |
| gce\_instance/agent | Количество записей лога агента логирования | Count | agent.googleapis.com/agent/log\_entry\_count |
| gce\_instance/agent | Количество повторных записей лога агента логирования | Count | agent.googleapis.com/agent/log\_entry\_retry\_count |
| gce\_instance/agent | Использование памяти агента мониторинга | Byte | agent.googleapis.com/agent/memory\_usage |
| gce\_instance/agent | Количество точек метрик агента мониторинга | Count | agent.googleapis.com/agent/monitoring/point\_count |
| gce\_instance/agent | Количество запросов API агента логирования | Count | agent.googleapis.com/agent/request\_count |
| gce\_instance/agent | Размер меток процессов агента мониторинга | Byte | agent.googleapis.com/agent/streamspace\_size |
| gce\_instance/agent | Агент мониторинга ограничивает процессы | Count | agent.googleapis.com/agent/streamspace\_size\_throttling |
| gce\_instance/agent | Время работы агента мониторинга/логирования | Second | agent.googleapis.com/agent/uptime |
| gce\_instance/agent | Открытые соединения | Count | agent.googleapis.com/apache/connections |
| gce\_instance/agent | Свободные обработчики | Count | agent.googleapis.com/apache/idle\_workers |
| gce\_instance/agent | Запросы | Count | agent.googleapis.com/apache/request\_count |
| gce\_instance/agent | Доска состояния | Count | agent.googleapis.com/apache/scoreboard |
| gce\_instance/agent | Трафик | Byte | agent.googleapis.com/apache/traffic |
| gce\_instance/agent | Количество попаданий в кэш | Count | agent.googleapis.com/cassandra/cache/hits |
| gce\_instance/agent | Задержка чтения | MicroSecond | agent.googleapis.com/cassandra/client\_request/latency/50p |
| gce\_instance/agent | Задержка чтения | MicroSecond | agent.googleapis.com/cassandra/client\_request/latency/95p |
| gce\_instance/agent | Задержка чтения | MicroSecond | agent.googleapis.com/cassandra/client\_request/latency/99p |
| gce\_instance/agent | Задержка чтения | MicroSecond | agent.googleapis.com/cassandra/client\_request/latency/max |
| gce\_instance/agent | Степень сжатия | Count | agent.googleapis.com/cassandra/column\_family/compression\_ratio |
| gce\_instance/agent | Максимальный размер строки | Byte | agent.googleapis.com/cassandra/column\_family/max\_row\_size |
| gce\_instance/agent | Размер журнала фиксации | Byte | agent.googleapis.com/cassandra/commitlog\_total\_size |
| gce\_instance/agent | Завершённые задачи | Count | agent.googleapis.com/cassandra/completed\_tasks |
| gce\_instance/agent | Задачи | Count | agent.googleapis.com/cassandra/current\_tasks |
| gce\_instance/agent | Отброшенные сообщения | Count | agent.googleapis.com/cassandra/dropped\_message/dropped\_count |
| gce\_instance/agent | Исключения | Count | agent.googleapis.com/cassandra/storage\_service\_exception\_count |
| gce\_instance/agent | Объём хранилища | Byte | agent.googleapis.com/cassandra/storage\_service\_load |
| gce\_instance/agent | Задержка запроса | MilliSecond | agent.googleapis.com/couchdb/average\_request\_time |
| gce\_instance/agent | Пакетные запросы | Count | agent.googleapis.com/couchdb/httpd/bulk\_request\_count |
| gce\_instance/agent | Запросы | Count | agent.googleapis.com/couchdb/httpd/request\_count |
| gce\_instance/agent | Методы запросов | Count | agent.googleapis.com/couchdb/httpd/request\_method\_count |
| gce\_instance/agent | Коды ответов | Count | agent.googleapis.com/couchdb/httpd/response\_code\_count |
| gce\_instance/agent | Временные чтения представлений | Count | agent.googleapis.com/couchdb/httpd/temporary\_view\_read\_count |
| gce\_instance/agent | Чтения представлений | Count | agent.googleapis.com/couchdb/httpd/view\_read\_count |
| gce\_instance/agent | Открытые базы данных | Count | agent.googleapis.com/couchdb/open\_databases |
| gce\_instance/agent | Открытые файлы | Count | agent.googleapis.com/couchdb/open\_files |
| gce\_instance/agent | Чтения | Count | agent.googleapis.com/couchdb/read\_count |
| gce\_instance/agent | Записи | Count | agent.googleapis.com/couchdb/write\_count |
| gce\_instance/agent | Нагрузка CPU (15 мин) | Count | agent.googleapis.com/cpu/load\_15m |
| gce\_instance/agent | Нагрузка CPU (1 мин) | Count | agent.googleapis.com/cpu/load\_1m |
| gce\_instance/agent | Нагрузка CPU (5 мин) | Count | agent.googleapis.com/cpu/load\_5m |
| gce\_instance/agent | Использование CPU | Second | agent.googleapis.com/cpu/usage\_time |
| gce\_instance/agent | Утилизация CPU | Percent | agent.googleapis.com/cpu/utilization |
| gce\_instance/agent | Использование диска | Byte | agent.googleapis.com/disk/bytes\_used |
| gce\_instance/agent | Время ввода/вывода диска | MilliSecond | agent.googleapis.com/disk/io\_time |
| gce\_instance/agent | Объединённые дисковые операции | Count | agent.googleapis.com/disk/merged\_operations |
| gce\_instance/agent | Дисковые операции | Count | agent.googleapis.com/disk/operation\_count |
| gce\_instance/agent | Время дисковой операции | MilliSecond | agent.googleapis.com/disk/operation\_time |
| gce\_instance/agent | Ожидающие дисковые операции | Count | agent.googleapis.com/disk/pending\_operations |
| gce\_instance/agent | Утилизация диска | Percent | agent.googleapis.com/disk/percent\_used |
| gce\_instance/agent | Байты чтения диска | Byte | agent.googleapis.com/disk/read\_bytes\_count |
| gce\_instance/agent | Взвешенное время ввода/вывода диска | MilliSecond | agent.googleapis.com/disk/weighted\_io\_time |
| gce\_instance/agent | Байты записи диска | Byte | agent.googleapis.com/disk/write\_bytes\_count |
| gce\_instance/agent | Размер кэша | Byte | agent.googleapis.com/elasticsearch/cache\_memory\_usage |
| gce\_instance/agent | Вытеснения полей | Count | agent.googleapis.com/elasticsearch/field\_eviction\_count |
| gce\_instance/agent | Вытеснения фильтров | Count | agent.googleapis.com/elasticsearch/filter\_cache\_eviction\_count |
| gce\_instance/agent | Количество сборок мусора | Count | agent.googleapis.com/elasticsearch/gc\_collection\_count |
| gce\_instance/agent | Использование памяти | Byte | agent.googleapis.com/elasticsearch/memory\_usage |
| gce\_instance/agent | Сетевой трафик | Byte | agent.googleapis.com/elasticsearch/network |
| gce\_instance/agent | Документы | Count | agent.googleapis.com/elasticsearch/num\_current\_documents |
| gce\_instance/agent | Узлы данных | Count | agent.googleapis.com/elasticsearch/num\_data\_nodes |
| gce\_instance/agent | Открытые соединения | Count | agent.googleapis.com/elasticsearch/num\_http\_connections |
| gce\_instance/agent | Узлы | Count | agent.googleapis.com/elasticsearch/num\_nodes |
| gce\_instance/agent | Открытые файлы | Count | agent.googleapis.com/elasticsearch/num\_open\_files |
| gce\_instance/agent | Открытые соединения | Count | agent.googleapis.com/elasticsearch/num\_server\_connections |
| gce\_instance/agent | Шарды | Count | agent.googleapis.com/elasticsearch/num\_shards |
| gce\_instance/agent | Завершённые операции | Count | agent.googleapis.com/elasticsearch/operation\_count |
| gce\_instance/agent | Время операции | MilliSecond | agent.googleapis.com/elasticsearch/operation\_time |
| gce\_instance/agent | Максимальное количество потоков | Count | agent.googleapis.com/elasticsearch/peak\_threads |
| gce\_instance/agent | Размер хранилища | Byte | agent.googleapis.com/elasticsearch/storage\_size |
| gce\_instance/agent | Потоки | Count | agent.googleapis.com/elasticsearch/threads |
| gce\_instance/agent | IPC-соединения | Count | agent.googleapis.com/hbase/ipc/connections |
| gce\_instance/agent | Размер очереди IPC | Count | agent.googleapis.com/hbase/ipc/queue\_length |
| gce\_instance/agent | IPC-трафик | Byte | agent.googleapis.com/hbase/ipc/traffic\_count |
| gce\_instance/agent | Нагрузка | Count | agent.googleapis.com/hbase/master/average\_load |
| gce\_instance/agent | Неактивные серверы регионов | Count | agent.googleapis.com/hbase/master/dead\_region\_servers |
| gce\_instance/agent | Активные серверы регионов | Count | agent.googleapis.com/hbase/master/live\_region\_servers |
| gce\_instance/agent | Обращения к блочному кэшу | Count | agent.googleapis.com/hbase/regionserver/block\_cache/access\_count |
| gce\_instance/agent | Количество вытесненных блоков | Count | agent.googleapis.com/hbase/regionserver/block\_cache/evicted\_blocks\_count |
| gce\_instance/agent | Процент попаданий в блочный кэш | Percent | agent.googleapis.com/hbase/regionserver/block\_cache/hit\_ratio\_percent |
| gce\_instance/agent | Размер блочного кэша | Byte | agent.googleapis.com/hbase/regionserver/block\_cache/memory |
| gce\_instance/agent | Количество блоков | Count | agent.googleapis.com/hbase/regionserver/block\_cache/num\_items |
| gce\_instance/agent | Размер очереди вызовов | Count | agent.googleapis.com/hbase/regionserver/call\_queue/length |
| gce\_instance/agent | Размер очереди компактификации | Count | agent.googleapis.com/hbase/regionserver/compaction\_queue/length |
| gce\_instance/agent | Размер очереди сброса | Count | agent.googleapis.com/hbase/regionserver/flush\_queue/length |
| gce\_instance/agent | Использование кучи | Byte | agent.googleapis.com/hbase/regionserver/memory/heap\_usage |
| gce\_instance/agent | Файлы memstore | Count | agent.googleapis.com/hbase/regionserver/memstore/files |
| gce\_instance/agent | Размер индекса memstore | Byte | agent.googleapis.com/hbase/regionserver/memstore/index\_size |
| gce\_instance/agent | Открытые хранилища memstore | Count | agent.googleapis.com/hbase/regionserver/memstore/open\_stores |
| gce\_instance/agent | Размер memstore | Byte | agent.googleapis.com/hbase/regionserver/memstore/size |
| gce\_instance/agent | Онлайн-регионы | Count | agent.googleapis.com/hbase/regionserver/online\_regions |
| gce\_instance/agent | Количество запросов | Count | agent.googleapis.com/hbase/regionserver/request\_count |
| gce\_instance/agent | Частота RPC-запросов | PerSecond | agent.googleapis.com/hbase/regionserver/requests/total\_rate |
| gce\_instance/agent | Медленные операции | Count | agent.googleapis.com/hbase/regionserver/slow\_operation\_count |
| gce\_instance/agent | Средняя задержка пакетов Thrift | NanoSecond | agent.googleapis.com/hbase/thrift/batch\_latency/average |
| gce\_instance/agent | Средняя задержка вызовов Thrift | NanoSecond | agent.googleapis.com/hbase/thrift/call\_latency/average |
| gce\_instance/agent | Размер очереди вызовов Thrift | Count | agent.googleapis.com/hbase/thrift/call\_queue/length |
| gce\_instance/agent | Средняя задержка медленных вызовов Thrift | NanoSecond | agent.googleapis.com/hbase/thrift/slow\_call\_latency/average |
| gce\_instance/agent | Среднее время в очереди Thrift | NanoSecond | agent.googleapis.com/hbase/thrift/time\_in\_queue/average |
| gce\_instance/agent | Открытые соединения IIS | Count | agent.googleapis.com/iis/current\_connections |
| gce\_instance/agent | Переданные байты IIS | Byte | agent.googleapis.com/iis/network/transferred\_bytes\_count |
| gce\_instance/agent | Соединения IIS | Count | agent.googleapis.com/iis/new\_connection\_count |
| gce\_instance/agent | Запросы IIS | Count | agent.googleapis.com/iis/request\_count |
| gce\_instance/agent | Сетевые ошибки | Count | agent.googleapis.com/interface/errors |
| gce\_instance/agent | Сетевые пакеты | Count | agent.googleapis.com/interface/packets |
| gce\_instance/agent | Сетевой трафик | Byte | agent.googleapis.com/interface/traffic |
| gce\_instance/agent | Количество сборок мусора | Count | agent.googleapis.com/jvm/gc/count |
| gce\_instance/agent | Время сборки мусора | MilliSecond | agent.googleapis.com/jvm/gc/time |
| gce\_instance/agent | Использование памяти | Byte | agent.googleapis.com/jvm/memory/usage |
| gce\_instance/agent | Время CPU | NanoSecond | agent.googleapis.com/jvm/os/cpu\_time |
| gce\_instance/agent | Открытые файлы | Count | agent.googleapis.com/jvm/os/open\_files |
| gce\_instance/agent | Потоки-демоны | Count | agent.googleapis.com/jvm/thread/num\_daemon |
| gce\_instance/agent | Потоки | Count | agent.googleapis.com/jvm/thread/num\_live |
| gce\_instance/agent | Максимальное количество потоков | Count | agent.googleapis.com/jvm/thread/peak |
| gce\_instance/agent | Время работы | MilliSecond | agent.googleapis.com/jvm/uptime |
| gce\_instance/agent | Неудачные запросы | Count | agent.googleapis.com/kafka/broker/topics/failed\_request\_count |
| gce\_instance/agent | Входящие сообщения | Count | agent.googleapis.com/kafka/broker/topics/incoming\_message\_count |
| gce\_instance/agent | Трафик | Byte | agent.googleapis.com/kafka/broker/topics/traffic |
| gce\_instance/agent | Активные контроллеры | Count | agent.googleapis.com/kafka/controller/kafka/active |
| gce\_instance/agent | Офлайн-разделы | Count | agent.googleapis.com/kafka/controller/kafka/offline\_partitions |
| gce\_instance/agent | Выборы лидеров | Count | agent.googleapis.com/kafka/controller/leader\_elections/election\_count |
| gce\_instance/agent | Выборы лидеров с устаревшими данными | Count | agent.googleapis.com/kafka/controller/leader\_elections/unclean\_count |
| gce\_instance/agent | Сбросы | Count | agent.googleapis.com/kafka/log/flush\_count |
| gce\_instance/agent | Запросы | Count | agent.googleapis.com/kafka/network/request\_count |
| gce\_instance/agent | Отложенные запросы чистилища | Count | agent.googleapis.com/kafka/purgatory/num\_delayed\_requests |
| gce\_instance/agent | Запросы чистилища | Count | agent.googleapis.com/kafka/purgatory/size |
| gce\_instance/agent | Максимальное отставание | Count | agent.googleapis.com/kafka/replica\_fetcher/max\_lag |
| gce\_instance/agent | Минимальная частота выборки | PerSecond | agent.googleapis.com/kafka/replica\_fetcher/min\_fetch\_rate |
| gce\_instance/agent | Получающие реплики | Count | agent.googleapis.com/kafka/replica\_manager/isr/expand\_count |
| gce\_instance/agent | Отстающие реплики | Count | agent.googleapis.com/kafka/replica\_manager/isr/shrink\_count |
| gce\_instance/agent | Лидеры | Count | agent.googleapis.com/kafka/replica\_manager/leaders |
| gce\_instance/agent | Разделы | Count | agent.googleapis.com/kafka/replica\_manager/partitions |
| gce\_instance/agent | Ненадёжные разделы | Count | agent.googleapis.com/kafka/replica\_manager/under\_replicated\_partitions |
| gce\_instance/agent | Команды | Count | agent.googleapis.com/memcached/command\_count |
| gce\_instance/agent | Соединения | Count | agent.googleapis.com/memcached/current\_connections |
| gce\_instance/agent | Элементы | Count | agent.googleapis.com/memcached/current\_items |
| gce\_instance/agent | Вытеснения | Count | agent.googleapis.com/memcached/eviction\_count |
| gce\_instance/agent | Использование памяти | Byte | agent.googleapis.com/memcached/memory |
| gce\_instance/agent | Трафик | Byte | agent.googleapis.com/memcached/network |
| gce\_instance/agent | Операции | Count | agent.googleapis.com/memcached/operation\_count |
| gce\_instance/agent | Процент попаданий | Percent | agent.googleapis.com/memcached/operation\_hitratio |
| gce\_instance/agent | Время CPU | Second | agent.googleapis.com/memcached/rusage |
| gce\_instance/agent | Потоки | Count | agent.googleapis.com/memcached/threads |
| gce\_instance/agent | Использование памяти | Byte | agent.googleapis.com/memory/bytes\_used |
| gce\_instance/agent | Утилизация памяти | Percent | agent.googleapis.com/memory/percent\_used |
| gce\_instance/agent | Попадания в кэш | Count | agent.googleapis.com/mongodb/cache/hits |
| gce\_instance/agent | Промахи кэша | Count | agent.googleapis.com/mongodb/cache/misses |
| gce\_instance/agent | Коллекции | Count | agent.googleapis.com/mongodb/collections |
| gce\_instance/agent | Соединения | Count | agent.googleapis.com/mongodb/connections |
| gce\_instance/agent | Размер данных | Byte | agent.googleapis.com/mongodb/data\_size |
| gce\_instance/agent | Экстенты | Count | agent.googleapis.com/mongodb/extents |
| gce\_instance/agent | Время удержания глобальной блокировки | MilliSecond | agent.googleapis.com/mongodb/global\_lock\_hold\_time |
| gce\_instance/agent | Размер индекса | Byte | agent.googleapis.com/mongodb/index\_size |
| gce\_instance/agent | Индексы | Count | agent.googleapis.com/mongodb/indexes |
| gce\_instance/agent | Использование памяти | MebiByte | agent.googleapis.com/mongodb/memory\_usage |
| gce\_instance/agent | Объекты | Count | agent.googleapis.com/mongodb/objects |
| gce\_instance/agent | Операции | Count | agent.googleapis.com/mongodb/operation\_count |
| gce\_instance/agent | Размер хранилища | Byte | agent.googleapis.com/mongodb/storage\_size |
| gce\_instance/agent | Открытые соединения SQL Server | Count | agent.googleapis.com/mssql/connections/user |
| gce\_instance/agent | Частота транзакций SQL Server | PerSecond | agent.googleapis.com/mssql/transaction\_rate |
| gce\_instance/agent | Частота транзакций записи SQL Server | PerSecond | agent.googleapis.com/mssql/write\_transaction\_rate |
| gce\_instance/agent | Страницы пула буферов | Count | agent.googleapis.com/mysql/buffer\_pool/num\_pages |
| gce\_instance/agent | Операции пула буферов | Count | agent.googleapis.com/mysql/buffer\_pool/operation\_count |
| gce\_instance/agent | Размер пула буферов | Byte | agent.googleapis.com/mysql/buffer\_pool\_size |
| gce\_instance/agent | Команды | Count | agent.googleapis.com/mysql/command\_count |
| gce\_instance/agent | Обработчики | Count | agent.googleapis.com/mysql/handler\_count |
| gce\_instance/agent | Двойная запись InnoDB | Count | agent.googleapis.com/mysql/innodb/doublewrite\_count |
| gce\_instance/agent | Операции с журналом InnoDB | Count | agent.googleapis.com/mysql/innodb/log\_operation\_count |
| gce\_instance/agent | Операции InnoDB | Count | agent.googleapis.com/mysql/innodb/operation\_count |
| gce\_instance/agent | Операции со страницами InnoDB | Count | agent.googleapis.com/mysql/innodb/page\_operation\_count |
| gce\_instance/agent | Блокировки InnoDB | Count | agent.googleapis.com/mysql/innodb/row\_lock\_count |
| gce\_instance/agent | Строковые операции InnoDB | Count | agent.googleapis.com/mysql/innodb/row\_operation\_count |
| gce\_instance/agent | Блокировки | Count | agent.googleapis.com/mysql/lock\_count |
| gce\_instance/agent | Операции QCache | Count | agent.googleapis.com/mysql/qcache/operation\_count |
| gce\_instance/agent | Запросы QCache | Count | agent.googleapis.com/mysql/qcache/query\_count |
| gce\_instance/agent | Задержка репликации | Second | agent.googleapis.com/mysql/slave\_replication\_lag |
| gce\_instance/agent | Сортировки | Count | agent.googleapis.com/mysql/sort\_count |
| gce\_instance/agent | Потоки | Count | agent.googleapis.com/mysql/thread\_count |
| gce\_instance/agent | TCP-соединения | Count | agent.googleapis.com/network/tcp\_connections |
| gce\_instance/agent | Принятые соединения | Count | agent.googleapis.com/nginx/connections/accepted\_count |
| gce\_instance/agent | Активные соединения | Count | agent.googleapis.com/nginx/connections/current |
| gce\_instance/agent | Обработанные соединения | Count | agent.googleapis.com/nginx/connections/handled\_count |
| gce\_instance/agent | Запросы | Count | agent.googleapis.com/nginx/request\_count |
| gce\_instance/agent | Утилизация файла подкачки | Percent | agent.googleapis.com/pagefile/percent\_used |
| gce\_instance/agent | Прочитанные блоки | Count | agent.googleapis.com/postgresql/blocks\_read\_count |
| gce\_instance/agent | Фиксации | Count | agent.googleapis.com/postgresql/commit\_count |
| gce\_instance/agent | Размер БД | Byte | agent.googleapis.com/postgresql/db\_size |
| gce\_instance/agent | Обработчики | Count | agent.googleapis.com/postgresql/num\_backends |
| gce\_instance/agent | Строки БД | Count | agent.googleapis.com/postgresql/num\_tuples |
| gce\_instance/agent | Операции | Count | agent.googleapis.com/postgresql/operation\_count |
| gce\_instance/agent | Откаты | Count | agent.googleapis.com/postgresql/rollback\_count |
| gce\_instance/agent | Процессы | Count | agent.googleapis.com/processes/count\_by\_state |
| gce\_instance/agent | CPU процессов | Second | agent.googleapis.com/processes/cpu\_time |
| gce\_instance/agent | Чтение с диска процессами | Byte | agent.googleapis.com/processes/disk/read\_bytes\_count |
| gce\_instance/agent | Запись на диск процессами | Byte | agent.googleapis.com/processes/disk/write\_bytes\_count |
| gce\_instance/agent | Количество форков | Count | agent.googleapis.com/processes/fork\_count |
| gce\_instance/agent | Резидентная память процессов | Byte | agent.googleapis.com/processes/rss\_usage |
| gce\_instance/agent | Виртуальная память процессов | Byte | agent.googleapis.com/processes/vm\_usage |
| gce\_instance/agent | Потребители | Count | agent.googleapis.com/rabbitmq/consumers |
| gce\_instance/agent | Частота доставки | PerSecond | agent.googleapis.com/rabbitmq/delivery\_rate |
| gce\_instance/agent | Сообщения | Count | agent.googleapis.com/rabbitmq/num\_messages |
| gce\_instance/agent | Частота публикации | PerSecond | agent.googleapis.com/rabbitmq/publish\_rate |
| gce\_instance/agent | Несохранённые изменения | Count | agent.googleapis.com/redis/changes\_since\_last\_save |
| gce\_instance/agent | Заблокированные клиенты | Count | agent.googleapis.com/redis/clients/blocked |
| gce\_instance/agent | Подключённые клиенты | Count | agent.googleapis.com/redis/clients/connected |
| gce\_instance/agent | Команды | Count | agent.googleapis.com/redis/commands\_processed |
| gce\_instance/agent | Соединения реплик | Count | agent.googleapis.com/redis/connections/slaves |
| gce\_instance/agent | Соединения | Count | agent.googleapis.com/redis/connections/total |
| gce\_instance/agent | Истёкшие ключи | Count | agent.googleapis.com/redis/expired\_keys |
| gce\_instance/agent | Использование памяти | Byte | agent.googleapis.com/redis/memory/usage |
| gce\_instance/agent | Использование памяти Lua | Byte | agent.googleapis.com/redis/memory/usage\_lua |
| gce\_instance/agent | Каналы PubSub | Count | agent.googleapis.com/redis/pubsub/channels |
| gce\_instance/agent | Шаблоны PubSub | Count | agent.googleapis.com/redis/pubsub/patterns |
| gce\_instance/agent | Время работы | Second | agent.googleapis.com/redis/uptime |
| gce\_instance/agent | Задержка 95% (1 мин) | MicroSecond | agent.googleapis.com/riak/latency/95th\_percentile |
| gce\_instance/agent | Средняя задержка (1 мин) | MicroSecond | agent.googleapis.com/riak/latency/average |
| gce\_instance/agent | Максимальная задержка (1 мин) | MicroSecond | agent.googleapis.com/riak/latency/maximum |
| gce\_instance/agent | Использование памяти | Byte | agent.googleapis.com/riak/memory\_usage |
| gce\_instance/agent | 95% смежных объектов (1 мин) | Count | agent.googleapis.com/riak/num\_siblings/95th\_percentile |
| gce\_instance/agent | Среднее количество смежных объектов (1 мин) | Count | agent.googleapis.com/riak/num\_siblings/average |
| gce\_instance/agent | Максимальное количество смежных объектов (1 мин) | Count | agent.googleapis.com/riak/num\_siblings/maximum |
| gce\_instance/agent | 95% размера объекта (1 мин) | Byte | agent.googleapis.com/riak/object\_size/95th\_percentile |
| gce\_instance/agent | Средний размер объекта (1 мин) | Byte | agent.googleapis.com/riak/object\_size/average |
| gce\_instance/agent | Максимальный размер объекта (1 мин) | Byte | agent.googleapis.com/riak/object\_size/maximum |
| gce\_instance/agent | Операции | Count | agent.googleapis.com/riak/operation\_count |
| gce\_instance/agent | Использование подкачки | Byte | agent.googleapis.com/swap/bytes\_used |
| gce\_instance/agent | Операции ввода/вывода подкачки | Count | agent.googleapis.com/swap/io |
| gce\_instance/agent | Утилизация подкачки | Percent | agent.googleapis.com/swap/percent\_used |
| gce\_instance/agent | Сессии | Count | agent.googleapis.com/tomcat/manager/sessions |
| gce\_instance/agent | Ошибки | Count | agent.googleapis.com/tomcat/request\_processor/error\_count |
| gce\_instance/agent | Время обработки | MilliSecond | agent.googleapis.com/tomcat/request\_processor/processing\_time |
| gce\_instance/agent | Запросы | Count | agent.googleapis.com/tomcat/request\_processor/request\_count |
| gce\_instance/agent | Трафик | Byte | agent.googleapis.com/tomcat/request\_processor/traffic\_count |
| gce\_instance/agent | Занятые потоки | Count | agent.googleapis.com/tomcat/threads/busy |
| gce\_instance/agent | Текущие потоки | Count | agent.googleapis.com/tomcat/threads/current |
| gce\_instance/agent | Успешные соединения с бэкендом | Count | agent.googleapis.com/varnish/backend\_connection\_count |
| gce\_instance/agent | Операции с кэшем | Count | agent.googleapis.com/varnish/cache\_operation\_count |
| gce\_instance/agent | Клиентские соединения | Count | agent.googleapis.com/varnish/client\_connection\_count |
| gce\_instance/agent | Открытые соединения | Count | agent.googleapis.com/zookeeper/connections\_count |
| gce\_instance/agent | Размер данных | Byte | agent.googleapis.com/zookeeper/data\_size |
| gce\_instance/agent | Последователи | Count | agent.googleapis.com/zookeeper/followers/count |
| gce\_instance/agent | Синхронизированные последователи | Count | agent.googleapis.com/zookeeper/followers/synced\_count |
| gce\_instance/agent | Полученные пакеты | Count | agent.googleapis.com/zookeeper/network/received\_packets\_count |
| gce\_instance/agent | Отправленные пакеты | Count | agent.googleapis.com/zookeeper/network/sent\_packets\_count |
| gce\_instance/agent | Узлы | Count | agent.googleapis.com/zookeeper/nodes/count |
| gce\_instance/agent | Эфемерные узлы | Count | agent.googleapis.com/zookeeper/nodes/ephemeral\_count |
| gce\_instance/agent | Наблюдатели | Count | agent.googleapis.com/zookeeper/nodes/watches\_count |
| gce\_instance/agent | Средняя задержка запроса | MilliSecond | agent.googleapis.com/zookeeper/requests/latency/average |
| gce\_instance/agent | Максимальная задержка запроса | MilliSecond | agent.googleapis.com/zookeeper/requests/latency/maximum |
| gce\_instance/agent | Минимальная задержка запроса | MilliSecond | agent.googleapis.com/zookeeper/requests/latency/minimum |
| gce\_instance/agent | Ожидающие запросы | Count | agent.googleapis.com/zookeeper/requests/outstanding\_count |
| gce\_instance/agent | Ожидающие синхронизации | Count | agent.googleapis.com/zookeeper/sync\_operations/pending\_count |
| gce\_instance/firewallinsights | Количество срабатываний брандмауэра ВМ | Count | firewallinsights.googleapis.com/vm/firewall\_hit\_count |
| gce\_instance/firewallinsights | Временная метка последнего использования брандмауэра ВМ | Count | firewallinsights.googleapis.com/vm/firewall\_last\_used\_timestamp |
| gce\_instance/istio | Количество закрытых клиентских соединений | Byte | istio.io/service/client/connection\_close\_count |
| gce\_instance/istio | Количество открытых клиентских соединений | Byte | istio.io/service/client/connection\_open\_count |
| gce\_instance/istio | Количество полученных байт клиентом | Byte | istio.io/service/client/received\_bytes\_count |
| gce\_instance/istio | Байты клиентских запросов | Byte | istio.io/service/client/request\_bytes |
| gce\_instance/istio | Количество клиентских запросов | Count | istio.io/service/client/request\_count |
| gce\_instance/istio | Байты клиентских ответов | Byte | istio.io/service/client/response\_bytes |
| gce\_instance/istio | Задержки обхода клиента | MilliSecond | istio.io/service/client/roundtrip\_latencies |
| gce\_instance/istio | Количество отправленных байт клиентом | Byte | istio.io/service/client/sent\_bytes\_count |
| gce\_instance/istio | Количество закрытых серверных соединений | Byte | istio.io/service/server/connection\_close\_count |
| gce\_instance/istio | Количество открытых серверных соединений | Byte | istio.io/service/server/connection\_open\_count |
| gce\_instance/istio | Количество полученных байт сервером | Byte | istio.io/service/server/received\_bytes\_count |
| gce\_instance/istio | Байты серверных запросов | Byte | istio.io/service/server/request\_bytes |
| gce\_instance/istio | Количество серверных запросов | Count | istio.io/service/server/request\_count |
| gce\_instance/istio | Байты серверных ответов | Byte | istio.io/service/server/response\_bytes |
| gce\_instance/istio | Задержки серверных ответов | MilliSecond | istio.io/service/server/response\_latencies |
| gce\_instance/istio | Количество отправленных байт сервером | Byte | istio.io/service/server/sent\_bytes\_count |
| gce\_instance\_vm\_flow/default\_metrics | Исходящие байты | Byte | networking.googleapis.com/vm\_flow/egress\_bytes\_count |
| gce\_instance\_vm\_flow/default\_metrics | Входящие байты | Byte | networking.googleapis.com/vm\_flow/ingress\_bytes\_count |
| gce\_instance\_vm\_flow/default\_metrics | Задержки RTT | MilliSecond | networking.googleapis.com/vm\_flow/rtt |
| instance\_group/default\_metrics | Размер группы экземпляров | Count | compute.googleapis.com/instance\_group/size |
| autoscaler/default\_metrics | Пропускная способность обслуживания | Count | autoscaler.googleapis.com/capacity |
| autoscaler/default\_metrics | Текущая утилизация автомасштабировщика | Count | autoscaler.googleapis.com/current\_utilization |
| tpu\_worker/default\_metrics | Утилизация CPU контейнера | Percent | tpu.googleapis.com/container/cpu/utilization |
| tpu\_worker/default\_metrics | Использование памяти контейнера | Byte | tpu.googleapis.com/container/memory/usage |
| tpu\_worker/default\_metrics | Утилизация CPU | Percent | tpu.googleapis.com/cpu/utilization |
| tpu\_worker/default\_metrics | Использование памяти | Byte | tpu.googleapis.com/memory/usage |
| tpu\_worker/default\_metrics | Полученные байты сети | Byte | tpu.googleapis.com/network/received\_bytes\_count |
| tpu\_worker/default\_metrics | Отправленные байты сети | Byte | tpu.googleapis.com/network/sent\_bytes\_count |
| tpu\_worker/default\_metrics | Утилизация MXU | Percent | tpu.googleapis.com/tpu/mxu/utilization |

## Связанные темы

* Интеграции Google Cloud
