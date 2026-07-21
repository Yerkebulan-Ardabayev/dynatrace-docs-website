---
title: Rack-aware конвертация с использованием восстановления
source: https://docs.dynatrace.com/managed/managed-cluster/high-availability/rack-aware-restore
---

# Rack-aware конвертация с использованием восстановления

# Rack-aware конвертация с использованием восстановления

* Практическое руководство
* 3 мин на чтение
* Обновлено 07 июля 2026 г.

Конвертация Managed Cluster в rack-aware развёртывание с использованием метода резервного копирования и восстановления.

Метод восстановления универсален и подходит для более крупных Managed Cluster и более сложных изменений топологии. Однако процесс восстановления занимает много времени, а поскольку резервное копирование выполняется ежедневно, часть данных теряется. Хранилище транзакций ([distributed traces](/managed/observe/application-observability/distributed-traces "Gain observability into highly distributed, cloud-native architectures to effectively trace and analyze transactions in real time.")) не входит в резервную копию. Для небольших Managed Cluster, где один узел может содержать полную реплику, вместо этого нужно использовать метод [rack-aware конвертации с использованием репликации](/managed/managed-cluster/high-availability/rack-aware-replication "Learn how to convert a Dynatrace Managed Cluster to a rack-aware deployment using the replication method, including preparation and node migration steps.").

![Process of converting Managed Cluster to rack-aware via backup and restore](https://cdn.bfldr.com/B686QPH3/as/spnxnjg7r477s8gb9qtctg/Rack_aware_conversion_using_restore-Light_Mode?auto=webp&format=png&position=1)

Процесс конвертации Managed Cluster в rack-aware через резервное копирование и восстановление

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Подготовка**](#preparation)[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Восстановление Managed Cluster в новые racks**](#restore)[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Проверка конвертации**](#verify)

## Шаг 1 Подготовка

1. Убедиться, что для Managed Cluster есть недавняя резервная копия. См. [Резервное копирование и восстановление Managed Cluster](/managed/managed-cluster/operation/back-up-and-restore-a-cluster "Understand the steps and commands required to restore a Dynatrace Managed cluster.").
2. Подготовить новые узлы. Убедиться, что раздел диска, выделенный под хранилище Cassandra на новом узле, достаточен для размещения всей базы данных Cassandra (с запасом на компакцию и новые данные). Диск должен быть как минимум вдвое больше, чем суммарный объём хранилища Cassandra всех существующих узлов Managed Cluster. Данные Cassandra нужно размещать на отдельном томе, чтобы избежать проблем с нехваткой места на диске из-за разных типов данных.

## Шаг 2 Восстановление Managed Cluster в новые racks

Чтобы восстановить Managed Cluster в новые racks:

1. Остановить существующий Managed Cluster, чтобы предотвратить подключение двух Managed Cluster с одинаковым ID к Dynatrace Mission Control.  
   См. [Запуск/остановка/перезапуск узла](/managed/managed-cluster/operation/start-stop-restart-node "Properly shut down and restart Dynatrace Managed nodes using command line parameters.").
2. Выполнить процедуру восстановления кластера ([Резервное копирование и восстановление Managed Cluster](/managed/managed-cluster/operation/back-up-and-restore-a-cluster#cluster-restore "Understand the steps and commands required to restore a Dynatrace Managed cluster.")) с одним изменением: запустить установщик Dynatrace Managed на каждом узле с параметрами rack.

   **Запустить установщик параллельно на каждом узле**, используя следующие параметры:

   * `--rack-name`: определяет rack, к которому будет принадлежать этот узел.
   * `--rack-dc`: определяет дата-центр, к которому будет принадлежать этот узел.
   * `--restore`: переключает установщик в режим восстановления.
   * `--cluster-ip`: IPv4-адрес узла, на котором запускается установщик.
   * `--cluster-nodes`: список ID и IP-адресов всех узлов Managed Cluster, разделённых запятыми, включая тот узел, на котором запускается установщик, в следующем формате `<node_id>:<node_ip>,<node_id>:<node_ip>`.
   * `--seed-ip`: IPv4-адрес seed-узла.
   * `--backup-file`: путь к резервному файлу `*.tar`, который включает путь к точке монтирования общего файлового хранилища, ID кластера, ID узла, версию резервной копии и файл резервной копии `*.tar` в следующем формате:  
     `<path-to-backup>/<UUID>/node_<node_id>/files/<backup_version_number>/<backup_file>`

   Пример пути резервной копии

   В этом примере пути:
   `/mnt/backup/bckp/c9dd47f0-87d7-445e-bbeb-26429fac06c6/node_1/files/19/backup-001.tar`
   части пути следующие:

   * `<path-to-backup>` = `/mnt/backup/bckp/`
   * `<UUID>` = `c9dd47f0-87d7-445e-bbeb-26429fac06c6`
   * `<node_id>` = `1`
   * `<backup_version_number>` = `19`

   Пока резервное копирование выполняется, могут присутствовать две директории резервных копий с разными номерами версий:

   * Директория с меньшим номером версии содержит старую резервную копию. Эта директория удаляется после завершения резервного копирования.
   * Директория с большим номером версии содержит резервную копию, которая создаётся в данный момент.

   Номер версии резервной копии увеличивается с каждым выполнением резервного копирования.

   ID и IP-адреса нужно взять из инвентаризации, созданной перед началом работы. Например:

   * IP-адрес узла, который нужно восстановить: `10.176.41.168`.
   * ID узлов и новые IP-адреса всех узлов Managed Cluster: `1: 10.176.41.168, 3: 10.176.41.169, 5: 10.176.41.170`.

   ```
   sudo ./tmp/backup-001-dynatrace-managed-installer.sh



   --rack-name rack2



   --rack-dc datacenter1



   --restore



   --cluster-ip "10.176.41.168"



   --cluster-nodes "1:10.176.41.168,3:10.176.41.169,5:10.176.41.170"



   --seed-ip "10.176.41.169"



   --backup-file /mnt/backup/bckp/c9dd47f0-87d7-445e-bbeb-26429fac06c6/node_1/files/19/backup-001.tar
   ```

## Шаг 3 Проверка конвертации

Процесс восстановления размещает загруженные данные непосредственно в целевых racks. После завершения конвертации страница **Deployment status** в Cluster Management Console показывает racks:

![Cluster Management Console deployment status page of a Managed Cluster that's rack-aware](https://dt-cdn.net/images/cmcstatus-2263-58f0a8359d.png)

Страница статуса развёртывания Cluster Management Console для Managed Cluster, который является rack-aware