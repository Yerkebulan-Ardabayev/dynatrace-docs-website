---
title: Premium HA — аварийное восстановление центра обработки данных из резервной копии
source: https://docs.dynatrace.com/managed/managed-cluster/high-availability/data-center-disaster-recovery-from-backup
scraped: 2026-05-12T12:06:57.040997
---

# Premium HA — аварийное восстановление ЦОД из резервной копии

# Premium HA — аварийное восстановление ЦОД из резервной копии

* Updated on Jan 13, 2026

Premium High Availability

Dynatrace Premium High Availability (Premium HA) — это готовое самодостаточное решение, обеспечивающее практически нулевое время простоя и непрерывный мониторинг без потери данных в сценариях переключения при отказе. Данное решение требует дополнительного лицензирования для вашего развёртывания.

В данной процедуре восстановления используется следующая терминология:

* **Source-DC** — исходный (выживший) центр обработки данных, в котором расположен Managed-кластер.
* **Target-DC** — целевой (утраченный) центр обработки данных, предназначенный для восстановления.
* **seed-узел** — любой узел в **Source-DC**, который будет использоваться для выполнения задач установки и распределения конфигурации.

Процедура включает раздельную миграцию и репликацию компонентов Dynatrace Managed, чтобы они были подготовлены к репликации данных между двумя центрами обработки данных.
См. [Обзор компонентов Dynatrace Managed](/managed/managed-cluster/basics/managed-components "Understand the Dynatrace Managed architecture, including the Managed Cluster, the Cluster Management Console, and Mission Control.").

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Удалите Dynatrace Managed на всех работающих узлах**](/managed/managed-cluster/high-availability/data-center-disaster-recovery-from-backup#step-1 "Learn how to recover lost data center from backup in a multiple data center deployment.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Восстановите центр обработки данных из резервной копии**](/managed/managed-cluster/high-availability/data-center-disaster-recovery-from-backup#step-2 "Learn how to recover lost data center from backup in a multiple data center deployment.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Удалите утраченный ЦОД из конфигурации**](/managed/managed-cluster/high-availability/data-center-disaster-recovery-from-backup#step-3 "Learn how to recover lost data center from backup in a multiple data center deployment.")[![Шаг 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Шаг 4")

**Распределите установщик**](/managed/managed-cluster/high-availability/data-center-disaster-recovery-from-backup#step-4 "Learn how to recover lost data center from backup in a multiple data center deployment.")[![Шаг 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Шаг 5")

**Подготовьте данные кластера к репликации**](/managed/managed-cluster/high-availability/data-center-disaster-recovery-from-backup#step-5 "Learn how to recover lost data center from backup in a multiple data center deployment.")[![Шаг 6](https://dt-cdn.net/images/step-6-f906c6c957.svg "Шаг 6")

**Создайте топологию центра обработки данных**](/managed/managed-cluster/high-availability/data-center-disaster-recovery-from-backup#step-6 "Learn how to recover lost data center from backup in a multiple data center deployment.")[![Шаг 7](https://dt-cdn.net/images/step-7-35139ef2d6.svg "Шаг 7")

**Откройте правила фаервола**](/managed/managed-cluster/high-availability/data-center-disaster-recovery-from-backup#step-7 "Learn how to recover lost data center from backup in a multiple data center deployment.")[![Шаг 8](https://dt-cdn.net/images/step-8-72c2162189.svg "Шаг 8")

**Установите узлы второго ЦОД**](/managed/managed-cluster/high-availability/data-center-disaster-recovery-from-backup#step-8 "Learn how to recover lost data center from backup in a multiple data center deployment.")[![Шаг 9](https://dt-cdn.net/images/step-9-caa5a7bd32.svg "Шаг 9")

**Выполните миграцию Cassandra**](/managed/managed-cluster/high-availability/data-center-disaster-recovery-from-backup#step-9 "Learn how to recover lost data center from backup in a multiple data center deployment.")[![Шаг 10](https://dt-cdn.net/images/step-10-f1909063b2.svg "Шаг 10")

**Выполните миграцию Elasticsearch**](/managed/managed-cluster/high-availability/data-center-disaster-recovery-from-backup#anchor_pha_migrate_elastic "Learn how to recover lost data center from backup in a multiple data center deployment.")[![Шаг 11](https://dt-cdn.net/images/number-step-gray-11-5cb9304947.svg "Шаг 11")

**Выполните миграцию сервера**](/managed/managed-cluster/high-availability/data-center-disaster-recovery-from-backup#step-11 "Learn how to recover lost data center from backup in a multiple data center deployment.")[![Шаг 12](https://dt-cdn.net/images/number-step-gray-12-0eaef2f87b.svg "Шаг 12")

**Включите новый ЦОД**](/managed/managed-cluster/high-availability/data-center-disaster-recovery-from-backup#step-12 "Learn how to recover lost data center from backup in a multiple data center deployment.")

### Сбор информации

Приведённые команды используют переменные в вызовах REST API. Потребуется следующая информация:

* `<seed-node-ip>` — IP-адрес **seed-узла** из **Source-DC**.  
  Это может быть любой узел, работающий в существующем центре обработки данных и используемый для выполнения задач установки и распределения конфигурации.
* `<nodes-ips>` — список IPv4-адресов новых узлов в **Target-DC**.  
  Пример: `"176.16.0.5", "176.16.0.6", "176.16.0.7"`
* `<api-token>` — действующий токен Cluster API (требуется область действия ServiceProviderAPI).  
  Можно сгенерировать в Cluster Management Console Dynatrace Managed. См. [Cluster API — аутентификация](/managed/dynatrace-api/cluster-api/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").
* `<dynatrace-directory>` — директория, в которой установлен Dynatrace Managed на seed-узле.  
  Директория установки Dynatrace Managed по умолчанию: `/opt/dynatrace-managed`
* `<datacenter-1>` — имя **Source-DC** должно совпадать с именем **Cassandra DC**.  
  Имя Cassandra DC по умолчанию: `datacenter1`.

  Получение имени ЦОД.

  Для получения имени ЦОД выполните следующую команду на **seed-узле** перед началом миграции:

  `sudo <dynatrace-directory>/utils/cassandra-nodetool.sh status`

  Ответ будет содержать имя **Source-DC**. Пример для ЦОД с именем `datacenter1`:

  ```
  Datacenter: datacenter1



  =======================



  Status=Up/Down



  |/ State=Normal/Leaving/Joining/Moving



  --  Address        Load       Tokens       Owns (effective)  Host ID                               Rack



  UN  10.176.42.20   65.54 GB   256          100.0%            f053dd8d-ecf3-7834-b099-68542439817b  rack1



  UN  10.176.42.244  65.47 GB   256          100.0%            2aa7e790-a423-9273-88f9-45bcd158dd6e  rack1



  UN  10.176.42.168  65.47 GB   256          100.0%            48543bca-41f5-26d3-b2fd-6cfdf5c0f3b2  rack1
  ```
* `<datacenter-2>` — имя **Target-DC** должно оставаться неизменным. Пример: `dc-us-east-2`.

Имя утраченного центра обработки данных

При восстановлении в **Target-DC** необходимо использовать то же имя утраченного центра обработки данных.

### Установка переменных

Установите следующие переменные окружения на **seed-узле** в **Source-DC** и на КАЖДОМ УЗЛЕ в **Target-DC**:

```
SEED_IP=<seed-ip>



DT_DIR=<dynatrace-directory>



NODES_IPS=$(echo '[<nodes-ips]')



API_TOKEN=<api-token>



SDC_NAME=<datacenter-1>



TDC_NAME=<datacenter-2>
```

Например:

```
SEED_IP=10.176.37.201



DT_DIR=/opt/dynatrace-managed



NODES_IPS=$(echo '["10.176.37.218", "10.176.37.227", "10.176.37.120"]')



API_TOKEN=R_SZOpV4RTOmjr9fFmK4x



SDC_NAME=datacenter1



TDC_NAME=dc-us-east-2
```

### Проверка пользовательских настроек

Если в кластере Cassandra или Elasticsearch настроены `custom.settings`, включающие rack awareness, обратитесь к специалисту Dynatrace через онлайн-чат для применения этих настроек перед установкой **Target-DC**.

Для проверки наличия пользовательских настроек выполните на **seed-узле**:

```
ls $DT_DIR/installer/custom.settings
```

Если файл `custom.settings` существует, используются пользовательские настройки.

Коды возврата API

Каждый вызов REST API возвращает HTTP-код. Переходите к следующему шагу только при получении кода `200`. Ожидаемые коды возврата:

`200` — перейти к следующему шагу, текущий шаг выполнен успешно.  
`207` — запрос обрабатывается, повторите шаг через несколько минут.  
`40x` — проверьте путь запроса и аргументы, повторите запрос.  
`5xx` — обратитесь в службу поддержки.

### Шаг 1. Удалите Dynatrace Managed на всех работающих узлах

Следуйте официальной процедуре удаления узла кластера через командную строку или Cluster Management Console. См. [Удаление узла кластера](/managed/managed-cluster/operation/remove-a-cluster-node "Learn how to remove a new cluster node using either the command prompt or the Cluster Management Console.").

### Шаг 2. Восстановите центр обработки данных из резервной копии

Следуйте официальной процедуре восстановления ЦОД из резервной копии. См. [Резервное копирование и восстановление кластера](/managed/managed-cluster/operation/back-up-and-restore-a-cluster#cluster-restore "Understand the steps and commands required to restore a Dynatrace Managed cluster.").

### Шаг 3. Удалите утраченный ЦОД из конфигурации

Выполните следующий вызов Cluster API только на **seed-узле**:

```
curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/lostDatacenterCleanUp?Api-Token=$API_TOKEN -H  "accept: application/json" -H  "Content-Type: application/json"
```

Если код состояния не `200` и ответ не предлагает следующих шагов, обратитесь к специалисту Dynatrace через онлайн-чат.

### Шаг 4. Распределите установщик

На этом шаге необходимо скопировать установщик узла на каждый узел в **Target-DC**.

1. Войдите в Cluster Management Console Dynatrace Managed.
2. Перейдите на **Home** для просмотра страницы статуса развёртывания Dynatrace Managed.
3. Нажмите **Add new cluster node**.
4. Скопируйте командную строку `wget` из текстового поля **Run this command on the target host**.

   Не запускайте скрипт установщика

   Текстовое поле **Run this installer script with root rights** содержит команду для скрипта установки. Проигнорируйте эту команду — **не выполняйте предоставленный скрипт**.
5. Вставьте и выполните только командную строку `wget` в терминале каждого узла Target-DC.

### Шаг 5. Подготовьте данные кластера к репликации

На этом шаге необходимо подготовить индексы данных к репликации.

#### Подготовка данных кластера

Выполните следующий вызов Cluster API только на **seed-узле**:

```
curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/clusterReplicationPreparation?Api-Token=$API_TOKEN
```

Если код состояния не `200` и ответ не предлагает следующих шагов, обратитесь к специалисту Dynatrace через онлайн-чат.

#### Проверка статуса подготовки кластера

Выполните следующий вызов Cluster API только на **seed-узле**:

```
curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/clusterReplicationPreparation?Api-Token=$API_TOKEN -H  "accept: application/json"
```

Если код состояния не `200`, повторите попытку через несколько минут.

### Шаг 6. Создайте топологию центра обработки данных

На этом шаге необходимо создать конфигурацию, определяющую принадлежность узлов к центрам обработки данных.

Выполните следующий вызов Cluster API только на **seed-узле**:

```
curl -ikS -X POST -d "{\"newDatacenterName\" : \"$TDC_NAME\", \"nodesIp\" :$NODES_IPS}" https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/datacenterTopology?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

Если код состояния не `200` и ответ не предлагает следующих шагов, обратитесь к специалисту Dynatrace через онлайн-чат.

### Шаг 7. Откройте правила фаервола

На этом шаге необходимо добавить правила фаервола, открывающие порты для трафика с узлов **Target-DC**.

#### Открытие портов

Для открытия портов для трафика с новых узлов **Target-DC** выполните следующий вызов Cluster API только на **seed-узле**:

```
curl --noproxy '*' -ikS -X POST -d "$NODES_IPS" https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/clusterNodes/currentDc?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

В случае успеха код состояния будет `200`, а тело ответа будет содержать идентификатор запроса для проверки статуса правил фаервола.

Если код состояния не `200` и ответ не предлагает следующих шагов, обратитесь к специалисту Dynatrace через онлайн-чат.

#### Проверка правил фаервола

Установите переменную окружения с идентификатором запроса только на **seed-узле**. Идентификатор запроса получен из ответа предыдущего вызова API.

```
REQ_ID=<topology-configuration-request-id>
```

Для проверки статуса правил фаервола выполните следующий вызов Cluster API только на **seed-узле**:

```
curl -ikS https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/clusterNodes/currentDc/$REQ_ID?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

Если код состояния не `200`, повторите попытку через несколько минут.

### Шаг 8. Установите узлы второго ЦОД

На этом шаге необходимо установить Managed-узлы на всех хостах **Target-DC**, после чего проверить наличие сервиса Nodekeeper. Это будет свидетельствовать об успешной установке всех узлов в **Target-DC**.

#### Установка узлов в Target-DC

Выполните следующую команду на каждом узле в **Target-DC**. Следуйте инструкциям на экране — это будет стандартная установка нового узла.

```
sudo /bin/sh ./managed-installer.sh --install-new-dc --premium-ha on --datacenter $TDC_NAME --seed-auth $API_TOKEN
```

Операция должна занять около 3–5 минут. Ожидаемый результат:

```
Installation in new data center completed successfully after 2 minutes 51 seconds.
```

#### Проверка Nodekeeper в Target-DC

Выполните следующий вызов Cluster API только на **seed-узле** после завершения установки всех узлов в **Target-DC**:

```
curl -ikS https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/nodekeeper/healthCheck?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

Если код состояния не `200`, повторите попытку через несколько минут.

### Шаг 9. Выполните миграцию Cassandra

На этом шаге необходимо перенастроить Cassandra в **Source-DC** и **Target-DC** для межЦОД-репликации, запустить синхронизацию данных, перестроить данные Cassandra и проверить её состояние.

Продолжительность зависит от размера хранилища метрик и может составлять от нескольких минут до нескольких часов.

1. #### Миграция Cassandra в Target-DC

   На этом шаге необходимо перенастроить Cassandra для межЦОД-репликации и запустить синхронизацию данных.

   #### Миграция Cassandra

   Для запуска миграции Cassandra в ЦОД **Target-DC** выполните следующий вызов Cluster API только на **seed-узле**:

   ```
   curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/newDc?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
   ```

   В случае успеха код состояния будет `200`, а тело ответа будет содержать идентификатор запроса для проверки статуса миграции. Установите переменную окружения с идентификатором запроса только на **seed-узле**. Идентификатор получен из ответа предыдущего вызова API.

   ```
   REQ_ID=<migration-new-datacenter-request-id>
   ```

   Если код состояния не `200` и ответ не предлагает следующих шагов, обратитесь к специалисту Dynatrace через онлайн-чат.

   #### Проверка статуса миграции

   Для проверки статуса миграции выполните следующий вызов Cluster API только на **seed-узле**:

   ```
   curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/newDc/$REQ_ID?Api-Token=$API_TOKEN -H  "accept: application/json" -H  "Content-Type: application/json"
   ```

   Если код состояния не `200`, повторите попытку через несколько минут.
2. #### Перестройка данных Cassandra

   Перестройка данных Cassandra и проверка её состояния для релизов Dynatrace версии 254 и более ранних.

   На этом шаге необходимо выполнить перестройку Cassandra и проверить прогресс по статусу. В зависимости от размера базы данных Cassandra этот процесс может занять несколько часов.

   ##### Перестройка данных

   Для перестройки Cassandra выполните следующую команду последовательно на каждом новом узле **Target-DC**. Используйте команду `nohup` для предотвращения прерывания выполнения скрипта (например, при разрыве сессии) во время важных операций.

   ```
   sudo nohup $DT_DIR/utils/cassandra-nodetool.sh rebuild -- $SDC_NAME &
   ```

   ##### Проверка прогресса и статуса

   Для проверки прогресса и статуса выполните следующий вызов Cluster API только на **seed-узле**:

   ```
   curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/rebuildStatus?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
   ```

   Если код состояния не `200`, повторите попытку примерно через 15 минут. Помните, что процесс перестройки может занять значительное время.

   #### Проверка состояния Cassandra

   Для проверки состояния кластера Cassandra выполните `cassandra-nodetool.sh` с параметром `status` только на **seed-узле**:

   ```
   sudo $DT_DIR/utils/cassandra-nodetool.sh status
   ```

   Результат должен выглядеть примерно так:

   ```
   Datacenter: dc1



   ===============



   Status=Up/Down



   |/ State=Normal/Leaving/Joining/Moving



   --  Address        Load       Tokens       Owns (effective)  Host ID                               Rack



   UN  10.176.41.167  18.82 GB   256          100.0%            3af25127-4f99-4f43-afc3-216d7a2c10f8  rack1



   UN  10.176.41.154  19.44 GB   256          100.0%            5a618559-3a73-42ec-83f0-32d28e08beec  rack1



   UN  10.176.41.43   19.58 GB   256          100.0%            191f3b30-949a-4cf2-b620-68a40eebf31e  rack1



   Datacenter: dc2



   ===============



   Status=Up/Down



   |/ State=Normal/Leaving/Joining/Moving



   --  Address        Load       Tokens       Owns (effective)  Host ID                               Rack



   UN  10.176.42.54   19.18 GB   256          100.0%            852ce236-a430-400a-92a6-daeed99acf68  rack1



   UN  10.176.42.104  19.12 GB   256          100.0%            84479219-b64d-442c-a807-a832db9aae18  rack1



   UN  10.176.42.234  19.4 GB    256          100.0%            507b377c-5bfc-4667-b251-a9b7c453ed22  rack1
   ```

   Значения **Load** не должны существенно отличаться между узлами, а **Status** на всех узлах должен быть `UN`.

   На этом шаге необходимо выполнить перестройку Cassandra и проверить прогресс по статусу. В зависимости от размера базы данных Cassandra этот процесс может занять несколько часов.

   ##### Перестройка данных

   Для перестройки данных Cassandra в ЦОД **Target-DC** выполните следующий вызов Cluster API только на seed-узле:

   ```
   curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/rebuild?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
   ```

   В случае успеха код состояния будет `200`. Если код состояния не `200` и ответ не предлагает следующих шагов, обратитесь к специалисту Dynatrace через онлайн-чат в вашей среде Dynatrace.

   ##### Проверка статуса перестройки данных

   Для проверки статуса перестройки данных выполните следующий вызов Cluster API только на **seed-узле**:

   ```
   curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/rebuild?Api-Token=$API_TOKEN -H  "accept: application/json" -H  "Content-Type: application/json"
   ```

   Если код состояния не `200`, повторите попытку примерно через 15 минут. Помните, что процесс перестройки данных может занять значительное время.

   Если в ответе флаг ошибки установлен в `true`, обратитесь к специалисту Dynatrace через онлайн-чат в вашей среде.

### Шаг 10. Выполните миграцию Elasticsearch

На этом шаге необходимо выполнить миграцию Elasticsearch в ЦОД **Target-DC**, проверить конфигурацию и миграцию данных. Продолжительность зависит от объёма хранилища Elasticsearch и может составлять от нескольких минут до нескольких часов.

#### Миграция Elasticsearch в Target-DC

Запустите Elasticsearch. Последовательно выполните следующую команду на каждом узле **Target-DC**:

```
sudo $DT_DIR/launcher/elasticsearch.sh start
```

Для запуска миграции Elasticsearch в ЦОД **Target-DC** выполните следующий вызов Cluster API только на **seed-узле**:

```
curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/restore/elasticsearch/recover?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

В случае успеха код состояния будет 200.

#### Проверка прогресса и статуса

Для проверки статуса миграции Elasticsearch выполните следующий вызов Cluster API только на seed-узле:

```
curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/restore/elasticsearch/recover?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

Если код состояния не `200`, повторите попытку через несколько минут.

#### Проверка миграции данных

Для проверки миграции данных Elasticsearch выполните следующий вызов Cluster API только на **seed-узле**:

```
curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/elasticsearch/indexMigrationStatus?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

Если код состояния не `200`, повторите попытку через несколько минут.

### Шаг 11. Выполните миграцию сервера

На этом шаге необходимо выполнить миграцию сервера, обновить токены авторизации для подключения OneAgent и запустить NGINX в ЦОД **Target-DC**. Также необходимо обновить установщики в **Source-DC**, используемые для добавления узлов.

#### Миграция сервера

Для запуска кластера Dynatrace Managed в **Target-DC** выполните следующий вызов Cluster API только на **seed-узле**:

```
curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/restore/server/recovery?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

В случае успеха код состояния будет `200`, а тело ответа будет содержать идентификатор запроса для проверки готовности кластера. Установите переменную окружения с идентификатором запроса только на **seed-узле**. Идентификатор получен из ответа предыдущего вызова API.

```
REQ_ID=<migration-server-request-id>
```

Если код состояния не `200` и ответ не предлагает следующих шагов, обратитесь к специалисту Dynatrace через онлайн-чат.

#### Проверка готовности кластера

Для проверки готовности кластера выполните следующий вызов Cluster API только на **seed-узле**:

```
curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/restore/server/recovery/$REQ_ID?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

Если код состояния не `200`, повторите попытку через несколько минут.

### Шаг 12. Включите новый ЦОД

1. Включите трафик OneAgent.  
   Подробнее см. [Включение/отключение узла кластера](/managed/managed-cluster/configuration/cluster-node-capabilities "Find out how to enable/disable a cluster node via the Web UI or API call").
2. Включите резервное копирование в одном из центров обработки данных. После миграции резервное копирование отключено.  
   Подробнее см. [Резервное копирование и восстановление кластера](/managed/managed-cluster/operation/back-up-and-restore-a-cluster "Understand the steps and commands required to restore a Dynatrace Managed cluster.").