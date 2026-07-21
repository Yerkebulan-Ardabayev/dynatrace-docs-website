---
title: Rack-aware преобразование с использованием репликации
source: https://docs.dynatrace.com/managed/managed-cluster/high-availability/rack-aware-replication
---

# Rack-aware преобразование с использованием репликации

# Rack-aware преобразование с использованием репликации

* Практическое руководство
* Чтение 4 мин
* Обновлено 15 июн, 2026

Метод расширения с использованием репликации полезен для небольших Dynatrace Managed Clusters, где один узел может содержать полную реплику. Если текущий объём хранилища метрик (база данных Cassandra) на узел превышает 1 ТБ, используй метод [rack-aware преобразования с использованием восстановления](/managed/managed-cluster/high-availability/rack-aware-restore "Learn how to convert a Dynatrace Managed Cluster to rack-aware topology using the backup and restore method, including preparation and installer parameters."). Можно использовать существующие узлы, постепенно (один за другим) переустанавливая их с параметром rack-aware. Опционально можно использовать дополнительное оборудование в качестве новых узлов и удалять один узел при установке нового узла с параметром rack-aware.

Преимущество этого подхода в том, что он не влияет на доступность Managed Cluster. Чтобы поддерживать доступность Managed Cluster, Dynatrace Managed использует свои встроенные методы репликации для сохранения данных. Удаление и добавление узла в Managed Cluster занимает время. Продолжительность зависит от размера хранилища метрик и скорости диска или сети. Некоторые операции с кластером могут занимать даже один или два дня. В это время Dynatrace Managed блокирует все остальные операции с кластером (добавление и удаление узлов, обновление и резервное копирование). Если планируется выполнить переустановку на существующем хосте, нужно подождать 72 часа, прежде чем повторно подключать этот хост к Managed Cluster.

![Process of converting Managed Cluster to rack-aware.](https://cdn.bfldr.com/B686QPH3/as/f92j44kp5b2xm3ttwqfr2q9n/Rack_aware_conversion_using_replication-Light_Mode?auto=webp&format=png&position=1)

Процесс преобразования Managed Cluster в rack-aware.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Подготовка**](#preparation)[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Расширение Managed Cluster на новые стойки**](#extend-racks)[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Проверка преобразования**](#verify)

## Шаг 1 Подготовка

1. Подготовь базу данных Cassandra для распределения реплик по Managed Cluster (требуется Python 2.7).

   Этот шаг применим только к Dynatrace Managed версии 1.304 и более ранних.

   На одном из существующих узлов измени keyspace, чтобы поменять настройки snitch с помощью Cassandra Query Language (CQL):

   ```
   sudo <managed-installation-dir>/cassandra/bin/cqlsh <node_IP>
   ```

   Где `<managed-installation-dir>`, это каталог бинарных файлов Dynatrace Managed, а `<node-IP>`, это IP текущего узла (узла, который используется в данный момент).

   Откроется оболочка CQL:

   ```
   Connected to 00aa0a0a-1ab1-11a1-aaa1-0a0a0aa1a1aa at xx.xxx.xx.xxx:9042.



   [cqlsh 5.0.1 | Cassandra 3.0.23 | CQL spec 3.4.0 | Native protocol v4]



   Use HELP for help.



   cqlsh>
   ```

   Затем выполни:

   ```
   ALTER KEYSPACE ruxitdb WITH REPLICATION = {'class': 'NetworkTopologyStrategy', 'datacenter1':3};
   ```

   По завершении введи `exit`.
2. Подготовь Managed Cluster к добавлению узлов в разных стойках.

   На каждом существующем узле отредактируй `/etc/dynatrace.conf` и настрой следующие параметры:

   ```
   CASSANDRA_NODE_RACK = rack1



   CASSANDRA_NODE_RACK_DC = datacenter1



   ELASTICSEARCH_NODE_RACK = rack1
   ```

   Выполни `sudo /opt/dynatrace-managed/installer/reconfigure.sh`, чтобы применить изменения конфигурации для узла Managed Cluster.

   Выполняй последовательно

   Запускай скрипт `reconfigure.sh` последовательно, поскольку он вызывает перезапуск процессов, и при параллельном запуске на нескольких узлах есть риск простоя базы данных Cassandra.
3. Подготовь новые узлы.

   Убедись, что дисковый раздел, выделенный под хранилище Cassandra на новом узле, достаточен для размещения всей базы данных Cassandra (с запасом на компакцию и новые данные). Размер диска должен быть как минимум вдвое больше суммарного объёма хранилища Cassandra на всех существующих узлах. Держи данные Cassandra на отдельном томе, чтобы избежать проблем с местом на диске, вызванных другими типами данных.
4. Убедись, что настройки стоек корректно соответствуют физическим стойкам и дата-центрам. В идеале, по завершении всего преобразования в каждой стойке должно быть равное количество узлов.

## Шаг 2 Расширение Managed Cluster на новые стойки

При первоначальном развёртывании Dynatrace Managed все узлы по умолчанию группируются в одной стойке по умолчанию, размещённой в дата-центре по умолчанию. Даже если развёртывание не является rack-aware, все узлы уже находятся в `datacenter1` `rack1`. Чтобы избежать добавления нового узла в стойку по умолчанию, не используй `rack1` в качестве значения параметра `--rack-name` для новой стойки.

Если преобразование Managed Cluster выполняется в том же дата-центре, используй значение параметра по умолчанию `datacenter1`.

Следуй этим шагам, чтобы расширить Managed Cluster на новые стойки.

Нагрузка на CPU во время bootstrapping

Если узлу сложно справляться с нагрузкой данных, можно временно остановить процесс сервера Dynatrace Managed на этом узле и высвободить больше циклов CPU для Cassandra.

1. Добавь новый узел с параметрами стойки в Managed Cluster.

   Используй процедуру [Добавление узла Managed Cluster](/managed/managed-cluster/installation/add-cluster-node "Add a node to your Managed Cluster by downloading the installer, running it on the target host, and monitoring synchronization progress.") и добавь параметры `--rack-name` и `--rack-dc` к команде установки. Например:

   ```
   /bin/sh dynatrace-managed-installer.sh --seed-auth abcdefjhij1234567890 --rack-name rack2 --rack-dc datacenter1
   ```

   Дождись, пока узел полностью присоединится к Managed Cluster. В зависимости от размера базы данных, bootstrapping Cassandra может занять несколько дней.
2. Добавь ещё один узел в ту же стойку, с теми же параметрами стойки.

   Для второго узла bootstrapping Cassandra ожидается быстрее.
3. Продолжай добавлять новые узлы в `rack2`. Когда в `rack2` окажется достаточно узлов (1/3 целевого размера Managed Cluster), начни добавлять новые узлы с параметрами стойки в `rack3`, учитывая требования к дисковому пространству.
4. Удали исходные узлы, которые были настроены без rack awareness (в стойке по умолчанию `rack1`), когда в `rack3` окажется достаточно узлов.

## Шаг 3 Проверка преобразования

Когда преобразование завершено, стойки отображаются на странице **Deployment status** в Cluster Management Console:

![Cluster Management Console deployment status page of a Managed Cluster that's rack-aware](https://dt-cdn.net/images/cmcstatus-2263-58f0a8359d.png)

Страница статуса развёртывания Cluster Management Console для Managed Cluster с поддержкой rack-aware