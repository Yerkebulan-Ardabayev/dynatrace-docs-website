---
title: Мониторинг Azure Managed Instance для Apache Cassandra
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-managed-instance-for-apache-cassandra
scraped: 2026-03-06T21:36:09.966171
---

# Мониторинг Azure Managed Instance для Apache Cassandra

# Мониторинг Azure Managed Instance для Apache Cassandra

* Последняя версия Dynatrace
* Практическое руководство
* Чтение: 11 минут
* Опубликовано 18 апреля 2022 г.

С точки зрения данных и инфраструктуры это [расширение Prometheus 2.0](/docs/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions "Узнайте, как создать расширение Prometheus с использованием платформы расширений.") позволяет отслеживать и анализировать активность ваших кластеров Apache Cassandra. Оно визуализирует состояние кластера и отображает такие метрики, как использование ЦП, подключения, задержка запросов, приостановка и время сборки мусора. Кроме того, с помощью [Dynatrace Intelligence](/docs/dynatrace-intelligence "Ознакомьтесь с возможностями Dynatrace Intelligence.") автоматически обнаруживаются проблемы производительности и выполняется точный анализ первопричин.

## Предварительные требования

* Создан и запущен [Azure Managed Instance для Apache Cassandra](https://docs.microsoft.com/en-us/azure/managed-instance-apache-cassandra/).
* Виртуальная машина Ubuntu, развёрнутая в виртуальной сети Azure, в которой присутствует управляемый экземпляр.
* Сервер Prometheus настроен для сбора данных с узлов Cassandra и с заданной [конфигурацией relabel](https://github.com/datastax/metric-collector-for-apache-cassandra/blob/master/dashboards/prometheus/prometheus.yaml).
* [Environment ActiveGate версии 1.231+](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-install-an-environment-activegate "Ознакомьтесь с пошаговой процедурой установки Environment ActiveGate на Linux.") с доступом к серверу Prometheus.

## Настройка

1. Создайте виртуальную машину Ubuntu в той же виртуальной сети, что и Azure Managed Instance для Apache Cassandra.
2. Убедитесь, что на виртуальной машине установлен Docker.
3. Создайте файл `prometheus.yml` на виртуальной машине со следующим содержимым.
   Добавьте IP-адрес и порт `9443` каждого узла Cassandra в раздел `static_configs`. IP-адреса можно получить из раздела Data Center на портале Azure для вашего кластера Cassandra.

   ```
   static_configs:



   - targets: ["<Node_IP_1>:9443", "<Node_IP_2>:9443", "<Node_IP_N>:9443"]
   ```

prometheus.yml

```
global:



scrape_interval: 15s



scrape_timeout: 10s



evaluation_interval: 15s



alerting:



alertmanagers:



- static_configs:



- targets: []



scheme: http



timeout: 10s



scrape_configs:



- job_name: prometheus



scrape_interval: 15s



scrape_timeout: 15s



metrics_path: /metrics



scheme: http



static_configs:



- targets:



- localhost:9090



- job_name: "mcac"



scrape_interval: 15s



scrape_timeout:  15s



static_configs:



- targets: ["<Node_IP_1>:9443", "<Node_IP_2>:9443", "<Node_IP_N>:9443"]



honor_labels: true



honor_timestamps: false



scheme: https



tls_config:



insecure_skip_verify: true



metric_relabel_configs:



#drop metrics we can calculate from prometheus directly



- source_labels: [__name__]



regex: .*rate_(mean|1m|5m|15m)



action: drop



#save the original name for all metrics



- source_labels: [__name__]



regex: (collectd_mcac_.+)



target_label: prom_name



replacement: ${1}



- source_labels: ["prom_name"]



regex: .+_bucket_(\d+)



target_label: le



replacement: ${1}



- source_labels: ["prom_name"]



regex: .+_bucket_inf



target_label: le



replacement: +Inf



- source_labels: ["prom_name"]



regex: .*_histogram_p(\d+)



target_label: quantile



replacement: .${1}



- source_labels: ["prom_name"]



regex: .*_histogram_min



target_label: quantile



replacement: "0"



- source_labels: ["prom_name"]



regex: .*_histogram_max



target_label: quantile



replacement: "1"



#Table Metrics *ALL* we can drop



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.table\.(\w+)



action: drop



#Table Metrics



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.table\.(\w+)\.(\w+)\.(\w+)



target_label: table



replacement: ${3}



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.table\.(\w+)\.(\w+)\.(\w+)



target_label: keyspace



replacement: ${2}



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.table\.(\w+)\.(\w+)\.(\w+)



target_label: __name__



replacement: mcac_table_${1}



#Keyspace Metrics



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.keyspace\.(\w+)\.(\w+)



target_label: keyspace



replacement: ${2}



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.keyspace\.(\w+)\.(\w+)



target_label: __name__



replacement: mcac_keyspace_${1}



#ThreadPool Metrics (one type is repair.task so we just ignore the second part)



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.thread_pools\.(\w+)\.(\w+)\.(\w+).*



target_label: pool_type



replacement: ${2}



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.thread_pools\.(\w+)\.(\w+)\.(\w+).*



target_label: pool_name



replacement: ${3}



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.thread_pools\.(\w+)\.(\w+)\.(\w+).*



target_label: __name__



replacement: mcac_thread_pools_${1}



#ClientRequest Metrics



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.client_request\.(\w+)\.(\w+)$



target_label: request_type



replacement: ${2}



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.client_request\.(\w+)\.(\w+)$



target_label: __name__



replacement: mcac_client_request_${1}



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.client_request\.(\w+)\.(\w+)\.(\w+)$



target_label: cl



replacement: ${3}



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.client_request\.(\w+)\.(\w+)\.(\w+)$



target_label: request_type



replacement: ${2}



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.client_request\.(\w+)\.(\w+)\.(\w+)$



target_label: __name__



replacement: mcac_client_request_${1}_cl



#Cache Metrics



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.cache\.(\w+)\.(\w+)



target_label: cache_name



replacement: ${2}



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.cache\.(\w+)\.(\w+)



target_label: __name__



replacement: mcac_cache_${1}



#CQL Metrics



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.cql\.(\w+)



target_label: __name__



replacement: mcac_cql_${1}



#Dropped Message Metrics



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.dropped_message\.(\w+)\.(\w+)



target_label: message_type



replacement: ${2}



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.dropped_message\.(\w+)\.(\w+)



target_label: __name__



replacement: mcac_dropped_message_${1}



#Streaming Metrics



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.streaming\.(\w+)\.(.+)$



target_label: peer_ip



replacement: ${2}



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.streaming\.(\w+)\.(.+)$



target_label: __name__



replacement: mcac_streaming_${1}



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.streaming\.(\w+)$



target_label: __name__



replacement: mcac_streaming_${1}



#CommitLog Metrics



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.commit_log\.(\w+)



target_label: __name__



replacement: mcac_commit_log_${1}



#Compaction Metrics



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.compaction\.(\w+)



target_label: __name__



replacement: mcac_compaction_${1}



#Storage Metrics



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.storage\.(\w+)



target_label: __name__



replacement: mcac_storage_${1}



#Batch Metrics



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.batch\.(\w+)



target_label: __name__



replacement: mcac_batch_${1}



#Client Metrics



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.client\.(\w+)



target_label: __name__



replacement: mcac_client_${1}



#BufferPool Metrics



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.buffer_pool\.(\w+)



target_label: __name__



replacement: mcac_buffer_pool_${1}



#Index Metrics



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.index\.(\w+)



target_label: __name__



replacement: mcac_sstable_index_${1}



#HintService Metrics



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.hinted_hand_off_manager\.([^\-]+)-(\w+)



target_label: peer_ip



replacement: ${2}



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.hinted_hand_off_manager\.([^\-]+)-(\w+)



target_label: __name__



replacement: mcac_hints_${1}



#HintService Metrics



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.hints_service\.hints_delays\-(\w+)



target_label: peer_ip



replacement: ${1}



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.hints_service\.hints_delays\-(\w+)



target_label: __name__



replacement: mcac_hints_hints_delays



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.hints_service\.([^\-]+)



target_label: __name__



replacement: mcac_hints_${1}



# Misc



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.memtable_pool\.(\w+)



target_label: __name__



replacement: mcac_memtable_pool_${1}



- source_labels: ["mcac"]



regex: com\.datastax\.bdp\.type\.performance_objects\.name\.cql_slow_log\.metrics\.queries_latency



target_label: __name__



replacement: mcac_cql_slow_log_query_latency



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.read_coordination\.(.*)



target_label: read_type



replacement: $1



- source_labels: ["mcac"]



regex: org\.apache\.cassandra\.metrics\.read_coordination\.(.*)



target_label: __name__



replacement: mcac_read_coordination_requests



#GC Metrics



- source_labels: ["mcac"]



regex: jvm\.gc\.(\w+)\.(\w+)



target_label: collector_type



replacement: ${1}



- source_labels: ["mcac"]



regex: jvm\.gc\.(\w+)\.(\w+)



target_label: __name__



replacement: mcac_jvm_gc_${2}



#JVM Metrics



- source_labels: ["mcac"]



regex: jvm\.memory\.(\w+)\.(\w+)



target_label: memory_type



replacement: ${1}



- source_labels: ["mcac"]



regex: jvm\.memory\.(\w+)\.(\w+)



target_label: __name__



replacement: mcac_jvm_memory_${2}



- source_labels: ["mcac"]



regex: jvm\.memory\.pools\.(\w+)\.(\w+)



target_label: pool_name



replacement: ${2}



- source_labels: ["mcac"]



regex: jvm\.memory\.pools\.(\w+)\.(\w+)



target_label: __name__



replacement: mcac_jvm_memory_pool_${2}



- source_labels: ["mcac"]



regex: jvm\.fd\.usage



target_label: __name__



replacement: mcac_jvm_fd_usage



- source_labels: ["mcac"]



regex: jvm\.buffers\.(\w+)\.(\w+)



target_label: buffer_type



replacement: ${1}



- source_labels: ["mcac"]



regex: jvm\.buffers\.(\w+)\.(\w+)



target_label: __name__



replacement: mcac_jvm_buffer_${2}



#Append the prom types back to formatted names



- source_labels: [__name__, "prom_name"]



regex: (mcac_.*);.*(_micros_bucket|_bucket|_micros_count_total|_count_total|_total|_micros_sum|_sum|_stddev).*



separator: ;



target_label: __name__



replacement: ${1}${2}



- regex: prom_name



action: labeldrop
```

4. Запустите контейнер Docker сервера Prometheus.

   Обязательно измените путь в команде ниже, чтобы он указывал на файл `prometheus.yml` из предыдущего шага.

   ```
   docker run \



   -d \



   -p 9090:9090 \



   -v /path/to/prometheus.yml:/etc/prometheus/prometheus.yml \



   prom/prometheus
   ```
5. Если ваша виртуальная машина недоступна из интернета, установите [Dynatrace Environment ActiveGate](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-install-an-environment-activegate "Ознакомьтесь с пошаговой процедурой установки Environment ActiveGate на Linux.") на вашу виртуальную машину Ubuntu.
   **Рекомендуется:** Задайте [свойство](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate#group "Узнайте о параметрах командной строки, доступных для ActiveGate на Linux.") `group` при установке.

## Включение и настройка расширения

1. В Dynatrace Hub выберите **Azure Managed Instance for Apache Cassandra**.
2. Включите расширение.
3. Убедитесь, что конечная точка Prometheus публикует метрики Cassandra. Используйте один из следующих запросов:

   `{__name__=~"mcac.*"}`

   `http://<Prometheus Server URL>:9090/api/v1/query?query=%7B__name__%3D%7E%22mcac.*%22%7D`
4. Добавьте конечную точку вашего сервера Prometheus в конфигурацию мониторинга расширения:

   `http://<Prometheus Server URL>:9090/api/v1`

   `<Prometheus Server URL>` не обязательно должен быть общедоступным. Если вы установите ActiveGate на той же виртуальной машине или в той же виртуальной сети, что и сервер Prometheus, можно использовать `localhost` или частный IP-адрес.
5. Выберите группу ActiveGate, для которой нужно включить это расширение.
6. Добавьте описание конфигурации мониторинга и выберите наборы функций метрик, которые вы хотите собирать.
7. С расширением поставляется панель мониторинга с именем **Azure Managed Instance for Apache Cassandra Overview**.

## Метрики

Доступные метрики перечислены ниже.

* Метаданные метрик и измерения доступны через [Data Explorer](/docs/analyze-explore-automate/explorer "Выполняйте запросы по метрикам и преобразовывайте результаты для получения необходимых сведений.") после включения расширения.
* Дополнительные сведения о собираемых метриках см. в [документации по мониторингу Apache Cassandra](https://cassandra.apache.org/doc/latest/cassandra/operating/metrics.html).

### Метрики узла кластера

| Название метрики | Ключ метрики | Описание |
| --- | --- | --- |
| Storage Load | com.dynatrace.extension.prometheus.azure\_cassandra\_storage\_load | Размер данных на диске, которыми управляет этот узел, в байтах. |
| Storage Exceptions | com.dynatrace.extension.prometheus.azure\_cassandra\_storage\_exceptions.count | Количество пойманных внутренних исключений. В нормальном режиме работы должно быть равно нулю. |
| Commit Log Pending Tasks | com.dynatrace.extension.prometheus.azure\_cassandra\_commit\_log\_pending\_tasks | Количество записанных сообщений журнала фиксации, ожидающих fsync. |
| Commit Log Completed Tasks Total | com.dynatrace.extension.prometheus.azure\_cassandra\_commit\_log\_completed\_tasks\_total.count | Общее количество сообщений журнала фиксации, записанных с момента запуска/перезапуска. |
| Buffer Pool Size | com.dynatrace.extension.prometheus.azure\_cassandra\_buffer\_pool\_size | Размер управляемого пула буферов в байтах. |
| Buffer Pool Misses Total | com.dynatrace.extension.prometheus.azure\_cassandra\_buffer\_pool\_misses\_total.count | Количество промахов в пуле. Чем это значение выше, тем больше происходит выделений памяти. |
| Client Connected Native Clients | com.dynatrace.extension.prometheus.azure\_cassandra\_client\_connected\_native\_clients | Количество клиентов, подключённых к серверу нативного протокола этого узла. |
| Client Auth Failure Total | com.dynatrace.extension.prometheus.azure\_cassandra\_client\_auth\_failure\_total.count | Количество клиентов, испытывающих сбои аутентификации. |
| Client Auth Success Total | com.dynatrace.extension.prometheus.azure\_cassandra\_client\_auth\_success\_total.count | Количество клиентов, успешно прошедших аутентификацию. |
| Storage Total Hints Total | com.dynatrace.extension.prometheus.azure\_cassandra\_storage\_total\_hints\_total.count | Количество hint-сообщений, записанных на этот узел с момента запуска/перезапуска. Включает по одной записи для каждого хоста, которому нужно направить hint для каждого hint. |
| CQL Prepared Statements Executed Total | com.dynatrace.extension.prometheus.azure\_cassandra\_cql\_prepared\_statements\_executed\_total.count | Количество выполненных подготовленных операторов. |
| CQL Regular Statements Executed Total | com.dynatrace.extension.prometheus.azure\_cassandra\_cql\_regular\_statements\_executed\_total.count | Количество выполненных неподготовленных операторов. |
| Dropped Messages Total | com.dynatrace.extension.prometheus.azure\_cassandra\_dropped\_messages\_total.count | Количество потерянных сообщений. |
| JVM GC Count | com.dynatrace.extension.prometheus.azure\_cassandra\_jvm\_gc\_count.count | Общее количество выполненных сборок мусора. |
| JVM GC Time | com.dynatrace.extension.prometheus.azure\_cassandra\_jvm\_gc\_time.count | Приблизительное накопленное время выполнения сборок мусора в миллисекундах. |
| JVM Memory Used | com.dynatrace.extension.prometheus.azure\_cassandra\_jvm\_memory\_used | Объём используемой памяти в байтах. |
| JVM Memory Usage | func:com.dynatrace.extension.prometheus.azure\_cassandra\_jvm\_memory\_usage | Отношение используемой памяти к максимальной памяти. |
| Thread Pools Active Tasks | com.dynatrace.extension.prometheus.azure\_cassandra\_thread\_pools\_active\_tasks | Количество задач, активно обрабатываемых этим пулом. |
| Thread Pools Total Blocked Tasks Total | com.dynatrace.extension.prometheus.azure\_cassandra\_thread\_pools\_total\_blocked\_tasks\_total.count | Количество задач, заблокированных из-за насыщения очереди. |
| Thread Pools Completed Tasks | com.dynatrace.extension.prometheus.azure\_cassandra\_thread\_pools\_completed\_tasks | Количество выполненных задач. |
| Client Request Latency Total | com.dynatrace.extension.prometheus.azure\_cassandra\_client\_request\_latency\_total.count | Задержка клиентских запросов. |
| Client Request Failures Total | com.dynatrace.extension.prometheus.azure\_cassandra\_client\_request\_failures\_total.count | Количество обнаруженных сбоев транзакций. |
| Client Request Unavailables Total | com.dynatrace.extension.prometheus.azure\_cassandra\_client\_request\_unavailables\_total.count | Количество обнаруженных исключений недоступности. |
| Cache Hit Rate | func:com.dynatrace.extension.prometheus.azure\_cassandra\_cache\_hit\_rate | Коэффициент попаданий в кэш за всё время. |
| Cache Capacity | com.dynatrace.extension.prometheus.azure\_cassandra\_cache\_capacity | Ёмкость кэша в байтах. |
| Cache Misses Total | com.dynatrace.extension.prometheus.azure\_cassandra\_cache\_misses\_total.count | Общее количество промахов кэша. |
| Cache Size | com.dynatrace.extension.prometheus.azure\_cassandra\_cache\_size | Общий размер занятого кэша в байтах. |

### Метрики пространства ключей

| Название метрики | Ключ метрики | Описание |
| --- | --- | --- |
| Keyspace All Memtables Live Data Size | com.dynatrace.extension.prometheus.azure\_cassandra\_keyspace\_all\_memtables\_live\_data\_size | Общий объём живых данных, хранящихся в memtable (включая вторичные индексы и ожидающие сброса memtable), расположенных вне кучи, без учёта накладных расходов структур данных. |
| Keyspace Bloom Filter Disk Space Used | com.dynatrace.extension.prometheus.azure\_cassandra\_keyspace\_bloom\_filter\_disk\_space\_used | Дисковое пространство, используемое фильтром Блума (в байтах). |
| Keyspace Live Disk Space Used | com.dynatrace.extension.prometheus.azure\_cassandra\_keyspace\_live\_disk\_space\_used | Дисковое пространство, используемое SSTable, принадлежащими данной таблице (в байтах). |
| Keyspace Memtable Columns Count | com.dynatrace.extension.prometheus.azure\_cassandra\_keyspace\_memtable\_columns\_count.gauge | Общее количество столбцов в memtable. |
| Keyspace Memtable Live Data Size | com.dynatrace.extension.prometheus.azure\_cassandra\_keyspace\_memtable\_live\_data\_size | Общий объём живых данных, хранящихся в memtable, без учёта накладных расходов структур данных. |
| Keyspace Memtable Switch Count | com.dynatrace.extension.prometheus.azure\_cassandra\_keyspace\_memtable\_switch\_count.gauge | Количество случаев, когда сброс приводил к замене memtable. |
| Keyspace Pending Compaction | com.dynatrace.extension.prometheus.azure\_cassandra\_keyspace\_pending\_compaction | Расчётное количество оставшихся операций уплотнения. |
| Keyspace Pending Flushes | com.dynatrace.extension.prometheus.azure\_cassandra\_keyspace\_pending\_flushes | Расчётное количество ожидающих задач сброса для данной таблицы. |
| Keyspace Read Total Latency Total | com.dynatrace.extension.prometheus.azure\_cassandra\_keyspace\_read\_total\_latency\_total.count | Задержка чтения. |
| Keyspace Total Disk Space Used | com.dynatrace.extension.prometheus.azure\_cassandra\_keyspace\_total\_disk\_space\_used | Общее дисковое пространство, используемое SSTable, принадлежащими данной таблице, включая устаревшие, ожидающие сборки мусора. |
| Keyspace Write Total Latency Total | com.dynatrace.extension.prometheus.azure\_cassandra\_keyspace\_write\_total\_latency\_total.count | Задержка записи. |

### Метрики таблицы

| Название метрики | Ключ метрики | Описание |
| --- | --- | --- |
| Table Bloom Filter Disk Space Used | com.dynatrace.extension.prometheus.azure\_cassandra\_table\_bloom\_filter\_disk\_space\_used | Дисковое пространство, используемое фильтром Блума (в байтах). |
| Table Bloom Filter False Positives | com.dynatrace.extension.prometheus.azure\_cassandra\_table\_bloom\_filter\_false\_positives | Количество ложноположительных результатов фильтра Блума таблицы. |
| Table Bloom Filter False Ratio | func:com.dynatrace.extension.prometheus.azure\_cassandra\_table\_bloom\_filter\_false\_ratio | Коэффициент ложноположительных результатов фильтра Блума таблицы. |
| Table Bytes Flushed Total | com.dynatrace.extension.prometheus.azure\_cassandra\_table\_bytes\_flushed\_total.count | Общее количество байт, сброшенных с момента запуска/перезапуска сервера. |
| Table Compaction Bytes Written Total | com.dynatrace.extension.prometheus.azure\_cassandra\_table\_compaction\_bytes\_written\_total.count | Общее количество байт, уплотнённых с момента запуска/перезапуска сервера. |
| Table Compression Ratio | func:com.dynatrace.extension.prometheus.azure\_cassandra\_table\_compression\_ratio | Текущий коэффициент сжатия для всех SSTable. |
| Table Dropped Mutations Total | com.dynatrace.extension.prometheus.azure\_cassandra\_table\_dropped\_mutations\_total.count | Количество потерянных мутаций в данной таблице. |
| Table Estimated Partition Count | com.dynatrace.extension.prometheus.azure\_cassandra\_table\_estimated\_partition\_count.gauge | Приблизительное количество ключей в таблице. |
| Table Key Cache Hit Rate | func:com.dynatrace.extension.prometheus.azure\_cassandra\_table\_key\_cache\_hit\_rate | Коэффициент попаданий в ключевой кэш для данной таблицы. |
| Table Live Disk Space Used Total | com.dynatrace.extension.prometheus.azure\_cassandra\_table\_live\_disk\_space\_used\_total | Дисковое пространство, используемое SSTable, принадлежащими данной таблице (в байтах). |
| Table Live SSTable Count | com.dynatrace.extension.prometheus.azure\_cassandra\_table\_live\_ss\_table\_count.gauge | Количество SSTable на диске для данной таблицы. |
| Table Memtable Columns Count | com.dynatrace.extension.prometheus.azure\_cassandra\_table\_memtable\_columns\_count.gauge | Общее количество столбцов в memtable. |
| Table Memtable Live Data Size | com.dynatrace.extension.prometheus.azure\_cassandra\_table\_memtable\_live\_data\_size | Общий объём живых данных, хранящихся в memtable, без учёта накладных расходов структур данных. |
| Table Memtable Switch Count Total | com.dynatrace.extension.prometheus.azure\_cassandra\_table\_memtable\_switch\_count\_total.count | Количество случаев, когда сброс приводил к замене memtable. |
| Table Pending Compactions | com.dynatrace.extension.prometheus.azure\_cassandra\_table\_pending\_compactions | Расчётное количество ожидающих операций уплотнения для данной таблицы. |
| Table Pending Flushes Total | com.dynatrace.extension.prometheus.azure\_cassandra\_table\_pending\_flushes\_total.count | Расчётное количество ожидающих операций сброса для данной таблицы. |
| Table Read Total Latency Total | com.dynatrace.extension.prometheus.azure\_cassandra\_table\_read\_total\_latency\_total.count | Задержка чтения для данной таблицы. |
| Table Row Cache Hit Total | com.dynatrace.extension.prometheus.azure\_cassandra\_table\_row\_cache\_hit\_total.count | Количество попаданий в кэш строк таблицы. |
| Table Row Cache Miss Total | com.dynatrace.extension.prometheus.azure\_cassandra\_table\_row\_cache\_miss\_total.count | Количество промахов кэша строк таблицы. |
| Table Total Disk Space Used Total | com.dynatrace.extension.prometheus.azure\_cassandra\_table\_total\_disk\_space\_used\_total | Общее дисковое пространство, используемое SSTable, принадлежащими данной таблице, включая устаревшие, ожидающие сборки мусора. |
| Table Write Total Latency Total | com.dynatrace.extension.prometheus.azure\_cassandra\_table\_write\_total\_latency\_total.count | Задержка записи для данной таблицы. |
