---
title: Изменение расположения хранилища
source: https://docs.dynatrace.com/managed/managed-cluster/operation/change-storage-location
scraped: 2026-05-12T11:53:16.490832
---

# Change storage location

# Change storage location

* Updated on Jul 01, 2024

Dynatrace Managed хранит несколько типов данных мониторинга в зависимости от сценария использования. Расположение хранилищ по умолчанию указано в разделе [Аппаратные и системные требования Dynatrace Managed](/managed/managed-cluster/installation/managed-hardware-requirements#storage "Review the hardware sizing, storage, and multi-node cluster requirements before installing Dynatrace Managed on your infrastructure.").

Изменение существующих путей к хранилищам может потребоваться в следующих случаях:

* Хранилище заполнено и необходима миграция на больший том.
* Текущее хранилище расположено на временном томе и необходимо перенести его на другой том.
* Текущее хранилище расположено на общем томе и требуется перенести данные на выделенный том.

Для изменения путей к хранилищам

1. Создайте резервную копию данных.

   Ошибка в данной процедуре может привести к потере данных. Перед началом рекомендуем скопировать все файлы хранилища в безопасное место. По возможности сначала выполните эту процедуру на тестовом развёртывании.
2. Остановите все сервисы Dynatrace на узле.  
   По умолчанию скрипт расположен в `<PRODUCT_PATH>/launcher/`. Убедитесь, что скрипт `dynatrace.sh` имеет права на выполнение. После запуска дождитесь завершения скрипта и убедитесь, что никакие сервисы Dynatrace не работают.

   ```
   [root@host]# <PRODUCT_PATH>/launcher/dynatrace.sh stop
   ```
3. Переместите хранилище данных в новое расположение.  
   Учтите, что хранилища нельзя вкладывать одно в другое. Например, хранилище Cassandra не может быть поддиректорией хранилища сессий.

   ```
   [root@host]# cp -pR /old_location/cassandra/* /new_location/cassandra
   ```
4. Убедитесь, что пользователь `dynatrace:dynatrace` является владельцем новой директории.

   ```
   [root@host]# chown -R dynatrace:dynatrace /new_location
   ```
5. Обновите новое расположение данных в `/etc/dynatrace.conf`.  
   Расположение должно быть указано либо как абсолютный путь, либо как значение на основе предопределённых переменных. Это должна быть директория, не симлинк.  
   Обновите следующий раздел:

   ```
   # Paths to directories with component's data



   DATASTORE_PATH = /var/opt/dynatrace-managed



   CASSANDRA_DATASTORE_PATH = DATASTORE_PATH/CASSANDRA_DIR



   ELASTICSEARCH_DATASTORE_PATH = DATASTORE_PATH/ELASTICSEARCH_DIR



   SERVER_DATASTORE_PATH = DATASTORE_PATH/SERVER_DIR



   SERVER_REPLAY_DATASTORE_PATH = SERVER_DATASTORE_PATH/replayData



   NODEKEEPER_DATASTORE_PATH = DATASTORE_PATH/NODEKEEPER_DIR
   ```
6. Запустите реконфигурацию через установщик. Используйте команду `nohup`, чтобы предотвратить прерывание выполнения скрипта (например, при разрыве сессии) во время важных операций.

   ```
   [root@host]# nohup <PRODUCT_PATH>/installer/reconfigure.sh --no-start &
   ```

   Этот шаг критически важен для распространения изменений из `/etc/dynatrace.conf` во все соответствующие конфигурационные файлы. Флаг `--no-start` позволит выполнить финальную проверку изменений перед запуском сервисов Dynatrace.

   Вывод скрипта должен выглядеть примерно так:

   ```
   Reconfiguration completed successfully after 1 minute 9 seconds.



   Dynatrace binaries are located in directory /opt/dynatrace-managed



   Dynatrace data is located in directory /new_location



   Dynatrace metrics repository is located in directory /new_location/cassandra



   Dynatrace Elasticsearch store is located in directory /new_location/elasticsearch



   Dynatrace server store is located in directory /new_location/sessionstorage



   Dynatrace session replay store is located in directory /new_location/replayData



   Don't forget to start Dynatrace Server and log in at https://<your_ip>
   ```
7. Запустите все сервисы Dynatrace.

   ```
   [root@host]# <PRODUCT_PATH>/launcher/dynatrace.sh start
   ```
8. Проверьте журналы, чтобы убедиться, что все сервисы запустились без ошибок.

## Пути к директориям по умолчанию и необходимое свободное пространство для установки и обновления

Пути к директориям в следующей таблице являются путями по умолчанию. Фактические пути могут отличаться, если установка выполнялась в нестандартную директорию.

Пользовательские директории

Если расположения хранилищ были изменены, `SERVER_DATASTORE_PATH`, `CASSANDRA_DATASTORE_PATH`, `ELASTICSEARCH_DATASTORE_PATH` должны находиться в отдельных директориях и не могут быть поддиректориями друг друга.

| **Символ директории** | **Путь к директории** | **Описание** | **Необходимое свободное место для установки** | **Необходимое свободное место для обновления** |
| --- | --- | --- | --- | --- |
| SELFMON\_AGENT\_INSTALL\_PATH  См. также [Дисковое пространство для OneAgent](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/disk-space-requirements-for-oneagent-installation-and-update-on-linux "Learn the OneAgent directory structure and disk space requirements for OneAgent installation on Linux.") | `/opt/dynatrace` | Основная директория для бинарных файлов OneAgent самомониторинга. | 3 ГБ [1](#fn-1-1-def) | 1,4 ГБ [1](#fn-1-1-def) |
| PRODUCT\_PATH | `/opt/dynatrace-managed` | Основная директория для бинарных файлов Dynatrace Managed | 7 ГБ [1](#fn-1-1-def) | 5 ГБ [1](#fn-1-1-def) |
| DATASTORE\_PATH | `/var/opt/dynatrace-managed` | Основная директория для данных Dynatrace Managed | 24 ГБ | 3 ГБ |
| LOG\_PATH | `DATASTORE_PATH` `/log` | Журналы всех компонентов, сервисов и инструментов Dynatrace Managed | 2 ГБ | 1 ГБ |
| CASSANDRA\_DATASTORE\_PATH | `DATASTORE_PATH` `/cassandra` | Репозиторий метрик | 25 ГБ | 1 ГБ |
| ELASTICSEARCH\_DATASTORE\_PATH | `DATASTORE_PATH` `/elasticsearch` | Хранилище Elasticsearch | 3 ГБ | 1 ГБ |
| SERVER\_DATASTORE\_PATH | `DATASTORE_PATH` `/server/tenantData` | Хранилище транзакций | 14 ГБ | 1 ГБ |
| SERVER\_REPLAY\_DATASTORE\_PATH | `DATASTORE_PATH` `/server/replayData` | Хранилище Session Replay | 14 ГБ | 1 ГБ |
| AGENT\_BUILD\_UNITS\_PATH | `DATASTORE_PATH` `/agents` | Установочные пакеты OneAgent и ActiveGate (если загружены сервером Dynatrace или установлены из отдельных пакетов) | 20 ГБ | 1 ГБ |
| SERVER\_BUILD\_UNITS\_PATH | `DATASTORE_PATH` `/installer` | Установщик Dynatrace Managed для добавления узлов в кластер, подготовленный в процессе установки/обновления | 2 ГБ | 1 ГБ |

1

Это значение является частью общего значения, необходимого для директории `/opt`. Общее необходимое свободное место на диске представляет собой сумму необходимых значений для `/opt/dynatrace-managed` и `/opt/dynatrace`.

Not supported

Обратите внимание, что вложенные точки монтирования в расположении `DATASTORE_PATH/server` для `/tenantData` и/или `/replayData` не поддерживаются.

## Расширение размера тома хранилища

Для расширения размера тома хранилища необходимо воспользоваться процедурой расширения диска от вашего поставщика хранилища. При использовании динамического хранилища, скорее всего, можно изменить параметры диска (размер, пропускную способность, тип), и хост применит их автоматически. В противном случае может потребоваться перемонтирование диска. После увеличения размера тома необходимо также расширить раздел тома, чтобы воспользоваться дополнительным дисковым пространством. Сервисы Dynatrace Managed должны автоматически обнаружить эти изменения.

## Кластер Dynatrace Managed: недостаточно свободного места на диске

При нехватке дискового пространства на любой из используемых точек монтирования кластер генерирует следующее событие:

Insufficient disk space on <mountPoint> on <path>

You need at least <required MB> free for <storage type>. Currently, only <current free disk space> of a total of <disk size> is available. Providing enough disk space is vital to the health of your cluster and ensures your monitoring data is safe, consistent, and available. Ignoring that message may cause data loss.

Если затронуто хранилище данных транзакций, генерируется дополнительное событие кластера, которое автоматически усекает данные и адаптирует период хранения данных. Подробнее см. раздел [Адаптивное хранение данных](/managed/manage/data-privacy-and-security/data-privacy/adaptive-data-retention "Find out how the retention time for the data stored in the transaction, Session Replay, and Log monitoring storages is adjusted.").