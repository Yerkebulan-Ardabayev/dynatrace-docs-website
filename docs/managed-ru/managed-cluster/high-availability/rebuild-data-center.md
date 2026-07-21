---
title: Восстановление дата-центра
source: https://docs.dynatrace.com/managed/managed-cluster/high-availability/rebuild-data-center
---

# Восстановление дата-центра

# Восстановление дата-центра

* Практическое руководство
* 10 минут на чтение
* Обновлено 07 июля 2026 г.

Чтобы восстановить утраченный дата-центр (DC) в развёртывании Premium High Availability, выполни шаги ниже. Процедура выполняет миграцию и репликацию компонентов Dynatrace Managed, чтобы они могли реплицировать данные между двумя дата-центрами.

В процедуре используются следующие термины:

* **Source-DC**: работоспособный дата-центр, содержащий Managed Cluster.
* **Target-DC**: утраченный дата-центр, назначенный для восстановления.
* **seed node**: узел в **Source-DC**, который выполняет задачи установки и распространяет конфигурацию.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Сбор информации**](/managed/managed-cluster/high-availability/rebuild-data-center#gather-information "Узнай, как восстановить утраченный дата-центр в развёртывании Dynatrace Managed Premium High Availability и восстановить репликацию между обоими дата-центрами.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Настройка переменных и проверка пользовательских настроек**](/managed/managed-cluster/high-availability/rebuild-data-center#set-variables "Узнай, как восстановить утраченный дата-центр в развёртывании Dynatrace Managed Premium High Availability и восстановить репликацию между обоими дата-центрами.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Остановка недоступного дата-центра**](/managed/managed-cluster/high-availability/rebuild-data-center#terminate-unavailable-dc "Узнай, как восстановить утраченный дата-центр в развёртывании Dynatrace Managed Premium High Availability и восстановить репликацию между обоими дата-центрами.")[![Шаг 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Шаг 4")

**Удаление узлов**](/managed/managed-cluster/high-availability/rebuild-data-center#remove-nodes "Узнай, как восстановить утраченный дата-центр в развёртывании Dynatrace Managed Premium High Availability и восстановить репликацию между обоими дата-центрами.")[![Шаг 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Шаг 5")

**Удаление утраченного дата-центра из конфигурации**](/managed/managed-cluster/high-availability/rebuild-data-center#remove-lost-dc "Узнай, как восстановить утраченный дата-центр в развёртывании Dynatrace Managed Premium High Availability и восстановить репликацию между обоими дата-центрами.")[![Шаг 6](https://dt-cdn.net/images/step-6-f906c6c957.svg "Шаг 6")

**Распространение установщика**](/managed/managed-cluster/high-availability/rebuild-data-center#distribute-installer "Узнай, как восстановить утраченный дата-центр в развёртывании Dynatrace Managed Premium High Availability и восстановить репликацию между обоими дата-центрами.")[![Шаг 7](https://dt-cdn.net/images/step-7-35139ef2d6.svg "Шаг 7")

**Подготовка данных Managed Cluster к репликации**](/managed/managed-cluster/high-availability/rebuild-data-center#prepare-cluster-data "Узнай, как восстановить утраченный дата-центр в развёртывании Dynatrace Managed Premium High Availability и восстановить репликацию между обоими дата-центрами.")[![Шаг 8](https://dt-cdn.net/images/step-8-72c2162189.svg "Шаг 8")

**Создание топологии дата-центра**](/managed/managed-cluster/high-availability/rebuild-data-center#create-topology "Узнай, как восстановить утраченный дата-центр в развёртывании Dynatrace Managed Premium High Availability и восстановить репликацию между обоими дата-центрами.")[![Шаг 9](https://dt-cdn.net/images/step-9-caa5a7bd32.svg "Шаг 9")

**Открытие правил файрвола**](/managed/managed-cluster/high-availability/rebuild-data-center#open-firewall-rules "Узнай, как восстановить утраченный дата-центр в развёртывании Dynatrace Managed Premium High Availability и восстановить репликацию между обоими дата-центрами.")[![Шаг 10](https://dt-cdn.net/images/step-10-f1909063b2.svg "Шаг 10")

**Установка узлов второго дата-центра**](/managed/managed-cluster/high-availability/rebuild-data-center#install-nodes "Узнай, как восстановить утраченный дата-центр в развёртывании Dynatrace Managed Premium High Availability и восстановить репликацию между обоими дата-центрами.")[![Шаг 11](https://dt-cdn.net/images/number-step-gray-11-5cb9304947.svg "Шаг 11")

**Миграция Cassandra**](/managed/managed-cluster/high-availability/rebuild-data-center#migrate-cassandra "Узнай, как восстановить утраченный дата-центр в развёртывании Dynatrace Managed Premium High Availability и восстановить репликацию между обоими дата-центрами.")[![Шаг 12](https://dt-cdn.net/images/number-step-gray-12-0eaef2f87b.svg "Шаг 12")

**Миграция Elasticsearch**](/managed/managed-cluster/high-availability/rebuild-data-center#migrate-elastic "Узнай, как восстановить утраченный дата-центр в развёртывании Dynatrace Managed Premium High Availability и восстановить репликацию между обоими дата-центрами.")[![Шаг 13](https://dt-cdn.net/images/number-step-gray-13-51a01d2a99.svg "Шаг 13")

**Миграция сервера**](/managed/managed-cluster/high-availability/rebuild-data-center#migrate-server "Узнай, как восстановить утраченный дата-центр в развёртывании Dynatrace Managed Premium High Availability и восстановить репликацию между обоими дата-центрами.")[![Шаг 14](https://dt-cdn.net/images/number-step-gray-14-75a70c82df.svg "Шаг 14")

**Восстановление трафика и резервного копирования**](/managed/managed-cluster/high-availability/rebuild-data-center#restore-traffic-backup "Узнай, как восстановить утраченный дата-центр в развёртывании Dynatrace Managed Premium High Availability и восстановить репликацию между обоими дата-центрами.")

Коды возврата API

На шагах 3–14 используются вызовы Cluster API Dynatrace. Каждый вызов возвращает HTTP-код. Переходи к следующему шагу только когда возвращённый код равен `200`. Ожидай следующие коды возврата:

`200`: переходи к следующему шагу. Текущий шаг выполнен успешно.  
`207`: запрос всё ещё обрабатывается. Повтори шаг через несколько минут.  
`40x`: пересмотри путь запроса и аргументы и повтори запрос.  
`5xx`: обратись в службу поддержки.

## Шаг 1 Сбор информации

Команды используют следующие переменные в вызовах Cluster API. Собери следующую информацию:

* `<seed-node-ip>`: IP-адрес **seed node** из **Source-DC**.  
  Используй любой узел, работающий в существующем дата-центре, который может выполнять задачи установки и распространять конфигурацию.
* `<nodes-ips>`: список IPv4-адресов новых узлов в **Target-DC**.  
  Пример: `"176.16.0.5", "176.16.0.6", "176.16.0.7"`
* `<api-token>`: действительный токен Cluster API. Токен требует область действия ServiceProviderAPI.  
  Его можно сгенерировать в Cluster Management Console (CMC). См. [Аутентификация Cluster API](/managed/dynatrace-api/cluster-api/cluster-api-authentication "Как пройти аутентификацию для использования Cluster API Dynatrace.").
* `<dynatrace-directory>`: каталог, в котором Dynatrace Managed работает на seed node.  
  Каталог установки Dynatrace Managed по умолчанию: `/opt/dynatrace-managed`.
* `<datacenter-1>`: имя **Source-DC** должно совпадать с именем **Cassandra DC**.  
  Имя Cassandra DC по умолчанию: `datacenter1`.

  Получение имени DC

  Чтобы получить имя DC, перед началом миграции выполни на **seed node** следующую команду:

  ```
  sudo <dynatrace-directory>/utils/cassandra-nodetool.sh status
  ```

  В ответе содержится имя **Source-DC**. В примере показан DC с именем `datacenter1`:

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
* `<datacenter-2>`: имя **Target-DC** должно остаться неизменным. Пример: `dc-us-east-2`.

Имя утраченного дата-центра

При восстановлении **Target-DC** используй то же имя, что и у утраченного дата-центра.

## Шаг 2 Настройка переменных и проверка пользовательских настроек

Установи следующие переменные окружения на **seed node** в **Source-DC** и на каждом узле в **Target-DC**:

```
SEED_IP=<seed-ip>



DT_DIR=<dynatrace-directory>



NODES_IPS=echo '[<nodes-ips]'



API_TOKEN=<api-token>



SDC_NAME=<datacenter-1>



TDC_NAME=<datacenter-2>
```

Например:

```
SEED_IP=10.176.37.201



DT_DIR=/opt/dynatrace-managed



NODES_IPS=echo '["10.176.37.218", "10.176.37.227", "10.176.37.120"]'



API_TOKEN=R_SZOpV4RTOmjr9fFmK4x



SDC_NAME=datacenter1



TDC_NAME=dc-us-east-2
```

Если кластер Cassandra или Elasticsearch использует `custom.settings` для включения rack-awareness, обратись к продуктовому эксперту Dynatrace через онлайн-чат. Продуктовый эксперт Dynatrace должен применить эти пользовательские настройки до того, как приступать к восстановлению **Target-DC**.

Чтобы проверить наличие пользовательских настроек, выполни на **seed node** следующую команду:

```
ls $DT_DIR/installer/custom.settings
```

Если файл `custom.settings` существует, значит Managed Cluster использует пользовательские настройки.

## Шаг 3 Остановка недоступного дата-центра

Останови все необходимые сервисы Dynatrace Managed в рекомендованном порядке. См. [Запуск, остановка или перезапуск узла](/managed/managed-cluster/operation/start-stop-restart-node "Как правильно завершать работу и перезапускать узлы Dynatrace Managed с помощью параметров командной строки.").

## Шаг 4 Удаление узлов

1. Перейди в **CMC**.
2. Для каждого узла в недоступном дата-центре перейди на страницу **Node details** и удали узел.

Подробнее о других способах удаления узла см. [Удаление узла Managed Cluster](/managed/managed-cluster/operation/remove-a-cluster-node "Как удалить новый узел кластера с помощью командной строки или Cluster Management Console.").

## Шаг 5 Удаление утраченного дата-центра из конфигурации

Выполните следующий вызов Cluster API только на **исходном узле (seed node)**:

```
curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/lostDatacenterCleanUp?Api-Token=$API_TOKEN -H  "accept: application/json" -H  "Content-Type: application/json"
```

Если код состояния не `200` и ответ не содержит рекомендаций по дальнейшим действиям, обратитесь к эксперту по продуктам Dynatrace через онлайн-чат.

## Шаг 6. Распространение установщика

На этом шаге нужно скопировать установщик узла на каждый узел в **Target-DC**.

1. Войдите в CMC.
2. Перейдите в **Home**, на страницу статуса развёртывания Dynatrace Managed.
3. Откройте **Add new cluster node**.
4. Скопируйте только строку команды `wget` из **Run this command on the target host**. Команду в **Run this installer script with root rights** игнорируйте и не запускайте скрипт установщика.
5. Вставьте и запустите только строку команды `wget` в окне терминала.

## Шаг 7. Подготовка данных Managed Cluster к репликации

На этом шаге нужно подготовить индексы данных к репликации.

### Подготовка данных Managed Cluster

Выполните следующий вызов Cluster API только на **исходном узле (seed node)**:

```
curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/clusterReplicationPreparation?Api-Token=$API_TOKEN
```

Если код состояния не `200` и ответ не содержит рекомендаций по дальнейшим действиям, обратитесь к эксперту по продуктам Dynatrace через онлайн-чат.

### Проверка статуса подготовки Managed Cluster

Выполните следующий вызов Cluster API только на **исходном узле (seed node)**:

```
curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/clusterReplicationPreparation?Api-Token=$API_TOKEN -H  "accept: application/json"
```

Если код состояния этого вызова не `200`, повторите попытку через несколько минут.

## Шаг 8. Создание топологии дата-центров

На этом шаге нужно создать конфигурацию, определяющую, какие узлы принадлежат каждому дата-центру.

Выполните следующий вызов Cluster API только на **исходном узле (seed node)**:

```
curl -ikS -X POST -d "{\"newDatacenterName\" : \"$TDC_NAME\", \"nodesIp\" :$NODES_IPS}" https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/datacenterTopology?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

Если код состояния не `200` и ответ не содержит рекомендаций по дальнейшим действиям, обратитесь к эксперту по продуктам Dynatrace через онлайн-чат.

## Шаг 9. Открытие правил файрвола

На этом шаге нужно добавить правила файрвола, открывающие порты для трафика от узлов **Target-DC**.

### Открытие портов

Чтобы открыть порты для трафика от новых узлов **Target-DC**, выполните следующий вызов Cluster API только на **исходном узле (seed node)**:

```
curl --noproxy '*' -ikS -X POST -d "$NODES_IPS" https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/clusterNodes/currentDc?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

При успешном выполнении код состояния будет `200`, а тело ответа будет содержать идентификатор запроса. Используйте этот идентификатор для проверки статуса правил файрвола.

Если код состояния не `200` и ответ не содержит рекомендаций по дальнейшим действиям, обратитесь к эксперту по продуктам Dynatrace через онлайн-чат.

### Проверка правил файрвола

Установите переменную окружения с идентификатором запроса только на **исходном узле (seed node)**. Используйте идентификатор запроса из ответа предыдущего вызова API.

```
REQ_ID=<topology-configuration-request-id>
```

Чтобы проверить статус правил файрвола, выполните следующий вызов Cluster API только на **исходном узле (seed node)**:

```
curl -ikS https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/clusterNodes/currentDc/$REQ_ID?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

Если код состояния этого вызова не `200`, повторите попытку через несколько минут.

## Шаг 10. Установка узлов второго дата-центра

На этом шаге нужно установить узлы Managed Cluster на всех хостах в **Target-DC**. Затем проверить работу службы Nodekeeper, чтобы убедиться, что все узлы успешно установлены в **Target-DC**.

### Установка узлов в целевом дата-центре

Выполните следующую команду на каждом узле в **Target-DC**. Следуйте подсказкам для типовой установки узла.

```
sudo /bin/sh ./managed-installer.sh --install-new-dc --premium-ha on --datacenter $TDC_NAME --seed-auth $API_TOKEN
```

Установка узла занимает примерно 3–5 минут. Ожидаемый вывод:

```
Installation in new data center completed successfully after 2 minutes 51 seconds.
```

### Проверка Nodekeeper в целевом дата-центре

Когда установка всех узлов в **Target-DC** завершится, выполните следующий вызов Cluster API только на **исходном узле (seed node)**:

```
curl -ikS https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/nodekeeper/healthCheck?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

Если код состояния не `200`, повторите попытку через несколько минут.

## Шаг 11. Миграция Cassandra

На этом шаге нужно перенастроить Cassandra в **Source-DC** и **Target-DC** для репликации между дата-центрами. Затем запустить синхронизацию данных, перестроить данные Cassandra и проверить состояние Cassandra.

Миграция Cassandra может занять от минут до часов в зависимости от размера хранилища метрик.

1. ### Запуск миграции

   Чтобы начать миграцию Cassandra в дата-центр **Target-DC**, выполните следующий вызов Cluster API только на **исходном узле (seed node)**:

   ```
   curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/newDc?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
   ```

   При успешном выполнении код состояния будет `200`, а тело ответа будет содержать идентификатор запроса. Используйте этот идентификатор для проверки статуса миграции. Установите переменную окружения с идентификатором запроса только на **исходном узле (seed node)**.

   ```
   REQ_ID=<migration-new-datacenter-request-id>
   ```

   Если код состояния не `200` и ответ не содержит рекомендаций по дальнейшим действиям, обратитесь к эксперту по продуктам Dynatrace через онлайн-чат.

   ### Проверка статуса миграции

   Чтобы проверить статус миграции, выполните следующий вызов Cluster API только на **исходном узле (seed node)**:

   ```
   curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/newDc/$REQ_ID?Api-Token=$API_TOKEN -H  "accept: application/json" -H  "Content-Type: application/json"
   ```

   Если код состояния не `200`, повторите попытку через несколько минут.
2. ### Перестроение данных Cassandra

   В зависимости от размера базы данных Cassandra это может занять несколько часов.

   #### Перестроение данных

   Чтобы перестроить данные Cassandra в дата-центре **Target-DC**, выполните следующий вызов Cluster API только на **исходном узле (seed node)**:

   ```
   curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/rebuild?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
   ```

   При успешном выполнении код состояния будет `200`. Если код состояния не `200` и ответ не содержит рекомендаций по дальнейшим действиям, обратитесь к эксперту по продуктам Dynatrace через онлайн-чат.

   #### Проверка статуса перестроения данных

   Чтобы проверить статус перестроения данных, выполните следующий вызов Cluster API только на **исходном узле (seed node)**:

   ```
   curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/rebuild?Api-Token=$API_TOKEN -H  "accept: application/json" -H  "Content-Type: application/json"
   ```

   Если код состояния не `200`, повторите попытку примерно через 15 минут. Процесс перестроения может занять несколько часов.

   Если в ответе флаг ошибки установлен в true, обратитесь к эксперту по продуктам Dynatrace через онлайн-чат.

## Шаг 12. Миграция Elasticsearch

На этом шаге нужно перенести Elasticsearch в дата-центр **Target-DC**. Затем проверить конфигурацию и миграцию данных. Миграция Elasticsearch может занять от минут до часов в зависимости от объёма хранилища Elasticsearch.

### Миграция Elasticsearch в целевой дата-центр

Запустите Elasticsearch. Выполните следующую команду на каждом узле в **Target-DC** по очереди:

```
sudo $DT_DIR/launcher/elasticsearch.sh start
```

Чтобы начать миграцию Elasticsearch в дата-центр **Target-DC**, выполните следующий вызов Cluster API только на **исходном узле (seed node)**:

```
curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/restore/elasticsearch/recover?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

При успешном выполнении код состояния будет `200`.

### Проверка прогресса и статуса

Чтобы проверить статус миграции Elasticsearch, выполните следующий вызов Cluster API только на **исходном узле (seed node)**:

```
curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/restore/elasticsearch/recover?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

Если код состояния не `200`, повторите попытку через несколько минут.

### Проверка миграции данных

Чтобы проверить миграцию данных Elasticsearch, выполните следующий вызов Cluster API только на **исходном узле (seed node)**:

```
curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/elasticsearch/indexMigrationStatus?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

Если код состояния не `200`, повторите попытку через несколько минут.

## Шаг 13. Миграция сервера

На этом шаге нужно перенести сервер, обновить токены авторизации для подключения OneAgent и запустить NGINX в дата-центре **Target-DC**. Также нужно обновить установщики в **Source-DC** для добавления узлов.

### Миграция сервера

Запустите Managed Cluster в **Target-DC**, выполнив следующий вызов Cluster API только на **исходном узле (seed node)**:

```
curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/restore/server/recovery?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

При успешном выполнении код состояния будет `200`, а тело ответа будет содержать идентификатор запроса. Используйте этот идентификатор для проверки готовности Managed Cluster. Установите переменную окружения с идентификатором запроса только на **исходном узле (seed node)**.

```
REQ_ID=<migration-server-request-id>
```

Если код состояния не `200` и ответ не содержит рекомендаций по дальнейшим действиям, обратитесь к эксперту по продуктам Dynatrace через онлайн-чат.

### Проверка готовности Managed Cluster

Чтобы проверить готовность Managed Cluster, выполнить следующий вызов Cluster API только на **seed-узле**:

```
curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/restore/server/recovery/$REQ_ID?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

Если код статуса не `200`, повторить попытку через несколько минут.

## Шаг 14. Восстановление трафика и резервного копирования

1. Восстановить трафик OneAgent.
   Подробности см. в разделе [Cluster node capabilities](/managed/managed-cluster/configuration/configure-cluster-capabilities "Configure OneAgent data processing and web UI traffic on individual Managed Cluster nodes using the Cluster Management Console or REST API.").
2. Включить резервное копирование в одном из дата-центров. Миграция отключает резервное копирование.
   Подробности см. в разделе [Back up and restore a Managed Cluster](/managed/managed-cluster/operation/back-up-and-restore-a-cluster "Understand the steps and commands required to restore a Dynatrace Managed cluster.").