---
title: Добавление дата-центра
source: https://docs.dynatrace.com/managed/managed-cluster/high-availability/add-data-center
---

# Добавление дата-центра

# Добавление дата-центра

* Практическое руководство
* 12 мин чтения
* Обновлено 07 июля 2026

Чтобы создать глобально распределённое развёртывание с высокой доступностью (Premium High Availability, PHA), нужно добавить избыточный набор узлов к исходному развёртыванию Managed Cluster. Как правило, такие развёртывания с высокой доступностью охватывают несколько дата-центров. Dynatrace Managed позволяет добавлять зеркальные узлы, расположенные в другом дата-центре.

В этой процедуре используются следующие обозначения:

* **DC-1**, дата-центр, в котором расположен исходный Dynatrace Managed Cluster.
* **DC-2**, дополнительный дата-центр, предназначенный для развёртывания PHA.
* **seed node**, любой узел в **DC-1**, который будет использоваться для выполнения задач установки и распространения конфигурации.

Процедура выполняет миграцию и репликацию каждого компонента Dynatrace Managed по отдельности для подготовки к репликации данных между дата-центрами.
См. [Обзор компонентов Dynatrace Managed](/managed/managed-cluster/basics/managed-components "Understand the Dynatrace Managed architecture, including the Managed Cluster, the Cluster Management Console, and Mission Control.").

## Перед началом работы

* Перед началом процедуры миграции резервное копирование кластера **DC-1** должно быть отключено. Создайте свежую резервную копию Managed Cluster и отключите резервное копирование кластера незадолго до развёртывания дополнительного дата-центра.
* Миграция не должна занимать больше четырёх недель. Если миграция превысит четыре недели, обратитесь к эксперту по продуктам Dynatrace через онлайн-чат.
* Перед началом процедуры миграции автоматическое обновление кластера **DC-1** должно быть отключено. Managed Cluster **не должен** обновляться во время миграции. См. [Автоматическое обновление](/managed/managed-cluster/operation/update-cluster#automatic-update-recommended "Learn how to update a Managed cluster and how to schedule an automatic update."). Обратитесь к эксперту по продуктам Dynatrace через онлайн-чат, если опция автоматического обновления у вас отключена.
* Убедитесь, что машины подготовлены для Managed Cluster в **DC-2**.

  Рекомендация

  Поскольку **DC-2** будет реплицировать данные **DC-1**, выделите такое же количество узлов с таким же оборудованием, включая дисковое хранилище.
  Все узлы в **DC-1** и **DC-2** должны быть синхронизированы по времени. Настройте Network Time Protocol (NTP) для синхронизации времени на всех узлах.
* Развёртывание PHA требует не менее трёх узлов в **DC-1** и трёх соответствующих узлов в **DC-2**.
* Все узлы в обоих дата-центрах должны иметь возможность обмениваться данными друг с другом. Чтобы проверить, доступен ли узел в **DC-1** с хоста в **DC-2**, можно выполнить REST-вызов проверки состояния. Например, выполните следующую команду с хоста в **DC-2**:

```
curl -k https://<DC-1-node-IP>/rest/health
```

где `<DC-1-node-IP>`, это IP-адрес любого узла в **DC-1**. В ответе должно быть получено `"RUNNING"`, если соединение установлено успешно.

## Подготовка

Убедитесь, что ваша система соответствует указанным [требованиям к оборудованию и операционной системе](/managed/managed-cluster/installation/managed-hardware-requirements "Review the hardware sizing, storage, and multi-node cluster requirements before installing Dynatrace Managed on your infrastructure.").

### Сбор информации

В командах эти переменные используются при выполнении вызовов REST API. Для этого понадобится следующая информация:

* `<seed-node-ip>`, IP-адрес **seed node** из **DC-1**.
  Это может быть любой узел, работающий в существующем дата-центре, который будет использоваться для выполнения задач установки и распространения конфигурации.
* `<nodes-ips>`, список IPv4-адресов новых узлов в **DC-2**.
  Пример: `"176.16.0.5", "176.16.0.6", "176.16.0.7"`
* `<api-token>`, действительный токен Cluster API (требуется область действия ServiceProviderAPI).
  Его можно сгенерировать в Dynatrace Managed Cluster Management Console. См. [Cluster API, аутентификация](/managed/dynatrace-api/cluster-api/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").
* `<dynatrace-directory>`, каталог, в котором Dynatrace Managed установлен на seed node.
  Каталог установки Dynatrace Managed по умолчанию: `/opt/dynatrace-managed`
* `<datacenter-1>`, имя **DC-1** должно совпадать с именем **Cassandra DC**.
  Имя Cassandra DC по умолчанию: `datacenter1`.

  Получение имени DC.

  Чтобы получить имя DC, выполните эту команду на **seed node** перед началом миграции:

  ```
  sudo <dynatrace-directory>/utils/cassandra-nodetool.sh status
  ```

  Вы получите ответ, содержащий имя **DC-1**. Пример для DC с именем `datacenter1`:

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
* `<datacenter-2>`, имя **DC-2** может быть любой строкой, которая начинается и заканчивается буквенно-цифровым символом и не превышает 80 символов. Внутри имени допускаются подчёркивания и дефисы. Пример: `dc-us-east-2`.

### Настройка переменных

Чтобы упростить многочисленные вызовы REST API во время развёртывания, задайте переменные окружения на каждом узле в **DC-1** и **DC-2**.

```
SEED_IP=<seed-ip>



DT_DIR=<dynatrace-directory>



NODES_IPS=$(echo '[<nodes-ips]')



API_TOKEN=<api-token>



DC1_NAME=<datacenter-1>



DC2_NAME=<datacenter-2>
```

Например:

```
SEED_IP=10.176.37.201



DT_DIR=/opt/dynatrace-managed



NODES_IPS=$(echo '["10.176.37.218", "10.176.37.227", "10.176.37.120"]')



API_TOKEN=R_SZOpV4RTOmjr9fFmK4x



DC1_NAME=datacenter1



DC2_NAME=dc-us-east-2
```

### Проверка пользовательских настроек

Если ваш кластер Cassandra или Elasticsearch настроен с `custom.settings`, включающими rack-awareness, обратитесь к эксперту по продуктам Dynatrace через онлайн-чат, чтобы применить эти пользовательские настройки перед установкой **DC-2**.

Чтобы проверить, применены ли пользовательские настройки, выполните на **seed node**:

```
ls $DT_DIR/installer/custom.settings
```

Если файл `custom.settings` существует, значит используются пользовательские настройки.

## Проверка настройки сетевой зоны

Перед миграцией на PHA проверьте настройку сетевой зоны для OneAgent и Environment ActiveGate, использующих сетевую зону `default`.

При миграции и перезапуске узла Managed Cluster Dynatrace изменяет сетевую зону Embedded ActiveGate с `default` на имя дата-центра узла. Переназначение сетевой зоны может изменить маршрутизацию трафика OneAgent и Environment ActiveGate, который в настоящее время использует сетевую зону `default`.

Хотя PHA реализует оптимизации для снижения трафика между дата-центрами, ActiveGate должны отправлять данные в оба дата-центра для обеспечения избыточности. Настройте OneAgent и ActiveGate так, чтобы они предпочитали определённые сетевые зоны, сохраняя при этом возможность перехода на другую часть Managed Cluster в случае отказа дата-центра. Для этой цели также можно использовать балансировщики нагрузки.

Для активно-пассивных развёртываний приложений оставляйте ActiveGate активными в пассивных частях развёртывания, чтобы инфраструктура Dynatrace переключалась при отказе без переконфигурации или повторного обнаружения.

## Установка

Чтобы создать Managed Cluster во втором дата-центре, выполни следующую процедуру.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Обновление лицензии Elasticsearch**](/managed/managed-cluster/high-availability/add-data-center#update-elasticsearch "Learn how to replicate Managed Cluster nodes across two data centers to set up a Premium High Availability deployment with cross-data center replication.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Распространение установщика**](/managed/managed-cluster/high-availability/add-data-center#distribute-installer "Learn how to replicate Managed Cluster nodes across two data centers to set up a Premium High Availability deployment with cross-data center replication.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Создание топологии дата-центра**](/managed/managed-cluster/high-availability/add-data-center#create-topology "Learn how to replicate Managed Cluster nodes across two data centers to set up a Premium High Availability deployment with cross-data center replication.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Открытие правил файрвола**](/managed/managed-cluster/high-availability/add-data-center#open-firewall-rules "Learn how to replicate Managed Cluster nodes across two data centers to set up a Premium High Availability deployment with cross-data center replication.")[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

**Установка узлов второго дата-центра**](/managed/managed-cluster/high-availability/add-data-center#install-nodes "Learn how to replicate Managed Cluster nodes across two data centers to set up a Premium High Availability deployment with cross-data center replication.")[![Step 6](https://dt-cdn.net/images/step-6-f906c6c957.svg "Step 6")

**Репликация Cassandra**](/managed/managed-cluster/high-availability/add-data-center#replicate-cassandra "Learn how to replicate Managed Cluster nodes across two data centers to set up a Premium High Availability deployment with cross-data center replication.")[![Step 7](https://dt-cdn.net/images/step-7-35139ef2d6.svg "Step 7")

**Репликация Elasticsearch**](/managed/managed-cluster/high-availability/add-data-center#replicate-elastic "Learn how to replicate Managed Cluster nodes across two data centers to set up a Premium High Availability deployment with cross-data center replication.")[![Step 8](https://dt-cdn.net/images/step-8-72c2162189.svg "Step 8")

**Миграция сервера**](/managed/managed-cluster/high-availability/add-data-center#migrate-server "Learn how to replicate Managed Cluster nodes across two data centers to set up a Premium High Availability deployment with cross-data center replication.")[![Step 9](https://dt-cdn.net/images/step-9-caa5a7bd32.svg "Step 9")

**Миграция nodekeeper**](/managed/managed-cluster/high-availability/add-data-center#migrate-nodekeeper "Learn how to replicate Managed Cluster nodes across two data centers to set up a Premium High Availability deployment with cross-data center replication.")[![Step 10](https://dt-cdn.net/images/step-10-f1909063b2.svg "Step 10")

**Включение нового дата-центра**](/managed/managed-cluster/high-availability/add-data-center#enable-data-center "Learn how to replicate Managed Cluster nodes across two data centers to set up a Premium High Availability deployment with cross-data center replication.")

API коды возврата

Каждый из вызовов REST API возвращает HTTP-код. Переходи к следующему шагу только когда возвращённый код равен `200`. Ожидай следующие коды возврата:

`200` - переходи к следующему шагу, текущий шаг выполнен успешно.  
`207` - запрос обрабатывается. Повтори шаг через несколько минут, если ответа нет.  
`40x` - проверь путь запроса и аргументы, затем повтори запрос.  
`5xx` - обратись к эксперту по продуктам Dynatrace через живой чат.

### Шаг 1 Обновление лицензии Elasticsearch

Получи лицензию PHA. Запусти следующую команду на каждом существующем узле **DC-1** последовательно:

```
sudo nohup $DT_DIR/installer/reconfigure.sh --only els --premium-ha on &
```

### Шаг 2 Распространение установщика

На этом шаге ты копируешь установщик узла на каждый узел в **DC-2**.

1. Войди в Dynatrace Managed Cluster Management Console.
2. Перейди на страницу **Home**, чтобы увидеть статус развёртывания Dynatrace Managed.
3. Выбери **Install cluster node**.
4. Скопируй команду `wget` из текстового поля **Run this command on the target host**.

   Не запускай установочный скрипт

   Текстовое поле **Run this installer script with root rights** содержит команду для установочного скрипта. Игнорируй эту команду; **не запускай предложенный скрипт**.
5. Вставь и запусти в окне терминала только команду `wget`.

### Шаг 3 Создание топологии дата-центра

На этом шаге ты создаёшь конфигурацию, определяющую, какой узел принадлежит какому дата-центру.

Выполни следующий вызов API кластера только на **seed-узле**:

```
curl -ikS -X POST -d "{\"newDatacenterName\" : \"$DC2_NAME\", \"nodesIp\" :$NODES_IPS}" https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/datacenterTopology?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

Если код статуса не `200` и ответ не предлагает следующих шагов, обратись к эксперту по продуктам Dynatrace через живой чат.

### Шаг 4 Открытие правил файрвола

На этом шаге ты добавляешь правила файрвола, открывающие порты для трафика к новым узлам DC-2.

#### Открытие портов

Чтобы открыть порты для трафика от новых узлов **DC-2**, выполни следующий вызов API кластера только на **seed-узле**:

```
curl --noproxy '*' -ikS -X POST -d "$NODES_IPS" https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/clusterNodes/currentDc?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

При успешном выполнении код статуса равен `200`, а тело ответа содержит ID запроса, нужный для проверки статуса правил файрвола.

Если код статуса не `200` и ответ не предлагает следующих шагов, обратись к эксперту по продуктам Dynatrace через живой чат.

#### Проверка правил файрвола

Установи переменную окружения ID запроса только на **seed-узле**. ID запроса берётся из ответа предыдущего вызова API.

```
REQ_ID=<topology-configuration-request-id>
```

Чтобы проверить статус правил файрвола, выполни следующий вызов API кластера только на **seed-узле**:

```
curl -ikS https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/clusterNodes/currentDc/$REQ_ID?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

Если код статуса этого вызова не `200`, попробуй снова через несколько минут.

### Шаг 5 Установка узлов второго дата-центра

На этом шаге ты устанавливаешь узлы Managed Cluster на всех хостах в **DC-2** и, после завершения, проверяешь наличие службы Nodekeeper. Запущенная служба Nodekeeper указывает на то, что все узлы были успешно установлены в **DC-2**.

#### Установка узлов в DC-2

Запусти следующую команду на каждом узле в **DC-2**. Следуй инструкциям на экране, поскольку это будет типовая установка узла.

```
sudo /bin/sh ./managed-installer.sh --install-new-dc --premium-ha on --datacenter $DC2_NAME --seed-auth $API_TOKEN
```

Установка занимает от 3 до 5 минут. Ожидаемый результат похож на следующий:

```
Installation in new data center completed successfully after 2 minutes 51 seconds.
```

#### Проверка Nodekeeper в DC-2

Выполни следующий вызов API кластера только на **seed-узле**, когда установка всех узлов в **DC-2** завершится:

```
curl -ikS https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/nodekeeper/healthCheck?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

Если код статуса не `200`, попробуй снова через несколько минут.

### Шаг 6 Репликация Cassandra

На этом шаге Cassandra перенастраивается в **DC-1** и **DC-2** для репликации между дата-центрами, запускается синхронизация данных, выполняется перестроение данных Cassandra и проверяется состояние Cassandra.

Репликация Cassandra может занять от минут до часов, в зависимости от объёма хранилища метрик.

1. #### Репликация Cassandra в DC-1

   На этом шаге Cassandra перенастраивается для репликации между дата-центрами.

   #### Репликация Cassandra в DC-1

   Чтобы запустить репликацию Cassandra в дата-центре **DC-1**, выполни следующий вызов кластерного API только на **seed-узле**:

   ```
   curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/currentDc?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
   ```

   В случае успеха код состояния будет `200`, а в теле ответа будет содержаться ID запроса, нужный для проверки статуса репликации. Задай переменную окружения с ID запроса только на **seed-узле**. ID запроса берётся из ответа предыдущего вызова API.

   ```
   REQ_ID=<replication-old-datacenter-request-id>
   ```

   Если код состояния не `200` и ответ не подсказывает дальнейшие шаги, обратись к продуктовому эксперту Dynatrace через live chat.

   #### Проверка статуса репликации в DC-1

   Чтобы проверить статус репликации, выполни следующий вызов кластерного API только на **seed-узле**:

   ```
   curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/currentDc/$REQ_ID?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
   ```

   Если код состояния не `200`, попробуй снова через несколько минут.

2. #### Репликация Cassandra в DC-2

   На этом шаге Cassandra перенастраивается для репликации между дата-центрами и запускается синхронизация данных.

   #### Репликация Cassandra в DC-2

   Чтобы запустить репликацию Cassandra в дата-центре **DC-2**, выполни следующий вызов кластерного API только на **seed-узле**:

   ```
   curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/newDc?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
   ```

   В случае успеха код состояния будет `200`, а в теле ответа будет содержаться ID запроса, нужный для проверки статуса репликации. Задай переменную окружения с ID запроса только на **seed-узле**. ID запроса берётся из ответа предыдущего вызова API.

   ```
   REQ_ID=<replication-new-datacenter-request-id>
   ```

   Если код состояния не `200` и ответ не подсказывает дальнейшие шаги, обратись к продуктовому эксперту Dynatrace через live chat.

   #### Проверка статуса репликации в DC-2

   Чтобы проверить статус репликации, выполни следующий вызов кластерного API только на **seed-узле**:

   ```
   curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/newDc/$REQ_ID?Api-Token=$API_TOKEN -H  "accept: application/json" -H  "Content-Type: application/json"
   ```

   Если код состояния не `200`, попробуй снова через несколько минут.

3. #### Перестроение данных Cassandra

   На этом шаге Cassandra перестраивается, и прогресс проверяется через статус. В зависимости от размера базы данных Cassandra это может занять несколько часов.

   ##### Перестроение данных

   Чтобы перестроить данные Cassandra в дата-центре **DC-2**, выполни следующий вызов кластерного API только на **seed-узле**:

   ```
   curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/rebuild?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
   ```

   В случае успеха код состояния будет `200`. Если код состояния не `200` и ответ не подсказывает дальнейшие шаги, обратись к продуктовому эксперту Dynatrace через live chat в своей среде Dynatrace.

   ##### Проверка статуса перестроения данных

   Чтобы проверить статус перестроения данных, выполни следующий вызов кластерного API только на **seed-узле**:

   ```
   curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/rebuild?Api-Token=$API_TOKEN -H  "accept: application/json" -H  "Content-Type: application/json"
   ```

   Если код состояния не `200`, попробуй снова примерно через 15 минут. Учитывай, что процесс перестроения данных может занимать много времени.

   Если в ответе флаг ошибки установлен в true, обратись к продуктовому эксперту Dynatrace через live chat в своей среде.

### Шаг 7. Репликация Elasticsearch

На этом шаге Elasticsearch реплицируется в дата-центр **DC-2**, и проверяется конфигурация и репликация данных. Репликация Elasticsearch может занять от минут до часов, в зависимости от объёма хранилища.

#### Репликация Elasticsearch в DC-2

Чтобы запустить репликацию Elasticsearch в дата-центр **DC-2**, выполни следующий вызов кластерного API только на **seed-узле**:

```
curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/elasticsearch?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

В случае успеха код состояния будет `200`, а в теле ответа будет содержаться ID запроса, нужный для проверки статуса репликации. Задай переменную окружения с ID запроса только на **seed-узле**. ID запроса берётся из ответа предыдущего вызова API.

```
REQ_ID=<replication-elasticsearch-request-id>
```

Если код состояния не `200` и ответ не подсказывает дальнейшие шаги, обратись к продуктовому эксперту Dynatrace через live chat.

#### Проверка прогресса и статуса

Чтобы проверить статус репликации Elasticsearch, выполни следующий вызов кластерного API только на **seed-узле**:

```
curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/elasticsearch/$REQ_ID?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

Если код состояния не `200`, попробуй снова через несколько минут.

#### Проверка репликации данных

Чтобы проверить репликацию данных Elasticsearch, выполни следующий вызов кластерного API только на **seed-узле**:

```
curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/elasticsearch/indexMigrationStatus?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

Если код состояния не `200`, попробуй снова через несколько минут.

### Шаг 8. Миграция сервера

На этом шаге выполняется миграция сервера, обновляются токены авторизации, обеспечивающие подключение OneAgent, и запускается NGINX в дата-центре **DC-2**. Также обновляются установщики в **DC-1**, которые используются для добавления узлов.

#### Миграция сервера

Запусти Managed Cluster Dynatrace в **DC-2**, выполнив следующий вызов кластерного API только на **seed-узле**:

```
curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/server?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

В случае успеха код состояния будет `200`, а в теле ответа будет содержаться ID запроса, нужный для проверки готовности кластера. Задай переменную окружения с ID запроса только на **seed-узле**. ID запроса берётся из ответа предыдущего вызова API.

```
REQ_ID=<replication-server-request-id>
```

Если код состояния не `200` и ответ не подсказывает дальнейшие шаги, обратись к продуктовому эксперту Dynatrace через live chat.

#### Проверка готовности Managed Cluster

Чтобы проверить, готов ли Managed Cluster, выполни следующий вызов кластерного API только на **seed-узле**:

```
curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/server/$REQ_ID?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

Если код состояния не `200`, попробуй снова через несколько минут.

### Шаг 9. Миграция nodekeeper

На этом шаге выполняется миграция nodekeeper в **DC-1**.

#### Запуск миграции

Managed Dynatrace версии 1.319 и более ранних

Перед началом миграции запусти скрипт ниже вручную на каждом узле в **DC-1**.

```
/opt/dynatrace-managed/installer/reconfigure.sh --only ndk
```

Чтобы запустить миграцию nodekeeper в **DC-1**, выполни следующий вызов кластерного API только на **seed-узле**:

```
curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/nodekeeper/currentDc?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

#### Проверка статуса миграции

Чтобы проверить, мигрирован ли Managed Cluster, выполни следующий вызов кластерного API только на **seed-узле**:

```
curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/nodekeeper/currentDc/status?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

В случае успеха код состояния будет `200`, а ответ будет содержать сообщение `Migration completed successfully`.

### Шаг 10. Включение нового дата-центра

1. Включи трафик OneAgent.  
   Подробности см. в разделе [Cluster node capabilities](/managed/managed-cluster/configuration/configure-cluster-capabilities "Configure OneAgent data processing and web UI traffic on individual Managed Cluster nodes using the Cluster Management Console or REST API.").
2. Включи резервное копирование в одном из дата-центров. После миграции резервное копирование отключено.  
   Подробности см. в разделе [Backup and restore a cluster](/managed/managed-cluster/operation/back-up-and-restore-a-cluster "Understand the steps and commands required to restore a Dynatrace Managed cluster.").