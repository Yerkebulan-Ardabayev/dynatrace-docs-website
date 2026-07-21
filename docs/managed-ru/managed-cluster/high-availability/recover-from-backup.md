---
title: Восстановление из резервной копии
source: https://docs.dynatrace.com/managed/managed-cluster/high-availability/recover-from-backup
---

# Восстановление из резервной копии

# Восстановление из резервной копии

* Практическое руководство
* 10 минут чтения
* Обновлено 07 июля 2026

Чтобы восстановить утраченный дата-центр (DC) из резервной копии в развёртывании Premium High Availability, следуй этим шагам.

В процедуре используются следующие термины:

* **Source-DC**, исходный (уцелевший) DC, где расположен Managed Cluster.
* **Target-DC**, целевой (утраченный) DC, назначенный для восстановления.
* **seed node**, любой узел в **Source-DC**, используемый для выполнения задач установки и распространения конфигурации.

Процедура выполняет миграцию и репликацию компонентов Dynatrace Managed по отдельности, чтобы подготовить их к репликации данных между двумя DC.
См. [Компоненты Managed](/managed/managed-cluster/basics/managed-components "Разберись в архитектуре Dynatrace Managed, включая Managed Cluster, Cluster Management Console и Mission Control.").

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Удали Dynatrace Managed на всех работающих узлах**](/managed/managed-cluster/high-availability/recover-from-backup#step-1 "Узнай, как восстановить дата-центр Premium High Availability из резервной копии в многодатацентровом развёртывании Dynatrace Managed после утраты дата-центра.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Восстанови дата-центр из резервной копии**](/managed/managed-cluster/high-availability/recover-from-backup#step-2 "Узнай, как восстановить дата-центр Premium High Availability из резервной копии в многодатацентровом развёртывании Dynatrace Managed после утраты дата-центра.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Удали утраченный дата-центр из конфигурации**](/managed/managed-cluster/high-availability/recover-from-backup#step-3 "Узнай, как восстановить дата-центр Premium High Availability из резервной копии в многодатацентровом развёртывании Dynatrace Managed после утраты дата-центра.")[![Шаг 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Шаг 4")

**Распространи установщик**](/managed/managed-cluster/high-availability/recover-from-backup#step-4 "Узнай, как восстановить дата-центр Premium High Availability из резервной копии в многодатацентровом развёртывании Dynatrace Managed после утраты дата-центра.")[![Шаг 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Шаг 5")

**Подготовь данные кластера к репликации**](/managed/managed-cluster/high-availability/recover-from-backup#step-5 "Узнай, как восстановить дата-центр Premium High Availability из резервной копии в многодатацентровом развёртывании Dynatrace Managed после утраты дата-центра.")[![Шаг 6](https://dt-cdn.net/images/step-6-f906c6c957.svg "Шаг 6")

**Создай топологию дата-центра**](/managed/managed-cluster/high-availability/recover-from-backup#step-6 "Узнай, как восстановить дата-центр Premium High Availability из резервной копии в многодатацентровом развёртывании Dynatrace Managed после утраты дата-центра.")[![Шаг 7](https://dt-cdn.net/images/step-7-35139ef2d6.svg "Шаг 7")

**Открой правила брандмауэра**](/managed/managed-cluster/high-availability/recover-from-backup#step-7 "Узнай, как восстановить дата-центр Premium High Availability из резервной копии в многодатацентровом развёртывании Dynatrace Managed после утраты дата-центра.")[![Шаг 8](https://dt-cdn.net/images/step-8-72c2162189.svg "Шаг 8")

**Установи узлы второго дата-центра**](/managed/managed-cluster/high-availability/recover-from-backup#step-8 "Узнай, как восстановить дата-центр Premium High Availability из резервной копии в многодатацентровом развёртывании Dynatrace Managed после утраты дата-центра.")[![Шаг 9](https://dt-cdn.net/images/step-9-caa5a7bd32.svg "Шаг 9")

**Мигрируй Cassandra**](/managed/managed-cluster/high-availability/recover-from-backup#step-9 "Узнай, как восстановить дата-центр Premium High Availability из резервной копии в многодатацентровом развёртывании Dynatrace Managed после утраты дата-центра.")[![Шаг 10](https://dt-cdn.net/images/step-10-f1909063b2.svg "Шаг 10")

**Мигрируй Elasticsearch**](/managed/managed-cluster/high-availability/recover-from-backup#anchor_pha_migrate_elastic "Узнай, как восстановить дата-центр Premium High Availability из резервной копии в многодатацентровом развёртывании Dynatrace Managed после утраты дата-центра.")[![Шаг 11](https://dt-cdn.net/images/number-step-gray-11-5cb9304947.svg "Шаг 11")

**Мигрируй сервер**](/managed/managed-cluster/high-availability/recover-from-backup#step-11 "Узнай, как восстановить дата-центр Premium High Availability из резервной копии в многодатацентровом развёртывании Dynatrace Managed после утраты дата-центра.")[![Шаг 12](https://dt-cdn.net/images/number-step-gray-12-0eaef2f87b.svg "Шаг 12")

**Включи новый дата-центр**](/managed/managed-cluster/high-availability/recover-from-backup#step-12 "Узнай, как восстановить дата-центр Premium High Availability из резервной копии в многодатацентровом развёртывании Dynatrace Managed после утраты дата-центра.")

## Собери информацию

Собери следующую информацию перед выполнением вызовов API:

* `<seed-node-ip>`, IP-адрес **seed node** из **Source-DC**.  
  Seed node может быть любым узлом, работающим в существующем DC, используемым для выполнения задач установки и распространения конфигурации.
* `<nodes-ips>`, список IPv4-адресов новых узлов в **Target-DC**.  
  Пример: `"176.16.0.5", "176.16.0.6", "176.16.0.7"`
* `<api-token>`, действительный токен Cluster API (требуется область действия ServiceProviderAPI).  
  Его можно сгенерировать в Dynatrace Managed Cluster Management Console (CMC). См. [Cluster API, аутентификация](/managed/dynatrace-api/cluster-api/cluster-api-authentication "Как пройти аутентификацию для использования Dynatrace Cluster API.").
* `<dynatrace-directory>`, каталог, в котором Dynatrace Managed установлен на seed node.  
  Каталог установки Dynatrace Managed по умолчанию: `/opt/dynatrace-managed`
* `<datacenter-1>`, имя **Source-DC** должно совпадать с именем **Cassandra DC**.  
  Имя Cassandra DC по умолчанию: `datacenter1`.

  Получи имя DC.

  Чтобы получить имя DC, выполни эту команду на **seed node** перед началом миграции:

  `sudo <dynatrace-directory>/utils/cassandra-nodetool.sh status`

  В ответ будет получено имя **Source-DC**. Пример для DC с именем `datacenter1`:

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
* `<datacenter-2>`, имя **Target-DC** должно остаться неизменным. Пример: `dc-us-east-2`.

Имя утраченного дата-центра

При восстановлении в **Target-DC** нужно использовать то же имя утраченного DC.

## Задай переменные

Задай следующие переменные окружения на **seed node** в **Source-DC** и на каждом узле в **Target-DC**:

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

## Проверь наличие пользовательских настроек

Если кластер Cassandra или Elasticsearch настроен с `custom.settings`, включающими rack-awareness, обратись к продуктовому эксперту Dynatrace через live chat. Примени пользовательские настройки перед тем, как переходить к установке **Target-DC**.

Чтобы проверить, применены ли пользовательские настройки, выполни на **seed node**:

```
ls $DT_DIR/installer/custom.settings
```

Если файл `custom.settings` существует, значит используются пользовательские настройки.

Коды возврата API

Каждый вызов REST API вернёт HTTP-код. Переходи к следующему шагу только когда возвращённый код `200`. Ожидай следующие коды возврата:

`200`, шаг выполнен успешно. Переходи к следующему шагу.  
`207`, запрос находится в обработке. Повтори через несколько минут.  
`40x`, пересмотри путь запроса и аргументы и повтори запрос.  
`5xx`, обратись в поддержку.

## Шаг 1 Удали Dynatrace Managed на всех работающих узлах

Следуй официальной процедуре удаления узла Managed Cluster с помощью командной строки или CMC. См. [Удаление узла кластера](/managed/managed-cluster/operation/remove-a-cluster-node "Узнай, как удалить новый узел кластера с помощью командной строки или Cluster Management Console.").

## Шаг 2 Восстанови дата-центр из резервной копии

Следуй официальной процедуре восстановления DC из резервной копии. См. [Резервное копирование и восстановление кластера](/managed/managed-cluster/operation/back-up-and-restore-a-cluster#cluster-restore "Разберись в шагах и командах, необходимых для восстановления кластера Dynatrace Managed.").

## Шаг 3 Удали утраченный дата-центр из конфигурации

Выполни следующий вызов cluster API только на **seed node**:

```
curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/lostDatacenterCleanUp?Api-Token=$API_TOKEN -H  "accept: application/json" -H  "Content-Type: application/json"
```

Если код состояния не `200` и ответ не подсказывает дальнейшие шаги, обратись к продуктовому эксперту Dynatrace через live chat.

## Шаг 4 Распространи установщик

1. Войти в CMC.
2. Перейти в раздел **Home**, чтобы открыть страницу состояния развёртывания Dynatrace Managed.
3. Выбрать **Add new cluster node**.
4. Скопировать командную строку `wget` из текстового поля **Run this command on the target host**.

   Не запускать установочный скрипт

   Текстовое поле **Run this installer script with root rights** содержит команду для установочного скрипта. Игнорировать эту команду. Не запускать предложенный скрипт.
5. Вставить и запустить только командную строку `wget` на каждом узле в окне терминала **Target-DC**.

## Шаг 5. Подготовка данных кластера для репликации

### Подготовка данных кластера

Выполнить следующий вызов API кластера только на **seed-узле**:

```
curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/clusterReplicationPreparation?Api-Token=$API_TOKEN
```

Если код состояния не `200` и ответ не предлагает дальнейших шагов, обратиться к эксперту по продукту Dynatrace через живой чат.

### Проверка статуса подготовки кластера

Выполнить следующий вызов API кластера только на **seed-узле**:

```
curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/clusterReplicationPreparation?Api-Token=$API_TOKEN -H  "accept: application/json"
```

Если код состояния этого вызова не `200`, повторить попытку через несколько минут.

## Шаг 6. Создание топологии дата-центра

Выполнить следующий вызов API кластера только на **seed-узле**:

```
curl -ikS -X POST -d "{\"newDatacenterName\" : \"$TDC_NAME\", \"nodesIp\" :$NODES_IPS}" https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/datacenterTopology?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

Если код состояния не `200` и ответ не предлагает дальнейших шагов, обратиться к эксперту по продукту Dynatrace через живой чат.

## Шаг 7. Открытие правил файрвола

### Открытие портов

Чтобы открыть порты для трафика от новых узлов **Target-DC**, выполнить следующий вызов API кластера только на **seed-узле**:

```
curl --noproxy '*' -ikS -X POST -d "$NODES_IPS" https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/clusterNodes/currentDc?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

В случае успеха код состояния будет `200`, а тело ответа будет содержать ID запроса, необходимый для проверки статуса правил файрвола.

Если код состояния не `200` и ответ не предлагает дальнейших шагов, обратиться к эксперту по продукту Dynatrace через живой чат.

### Проверка правил файрвола

Установить переменную окружения ID запроса только на **seed-узле**. ID запроса берётся из ответа предыдущего вызова API.

```
REQ_ID=<topology-configuration-request-id>
```

Чтобы проверить статус правил файрвола, выполнить следующий вызов API кластера только на **seed-узле**:

```
curl -ikS https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/clusterNodes/currentDc/$REQ_ID?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

Если код состояния этого вызова не `200`, повторить попытку через несколько минут.

## Шаг 8. Установка узлов второго дата-центра

### Установка узлов в Target-DC

Выполнить следующую команду на каждом узле в **Target-DC**. Следовать подсказкам установки, поскольку это будет обычная установка узла.

```
sudo /bin/sh ./managed-installer.sh --install-new-dc --premium-ha on --datacenter $TDC_NAME --seed-auth $API_TOKEN
```

Установка занимает от 3 до 5 минут. Ожидаемый результат похож на следующий:

```
Installation in new data center completed successfully after 2 minutes 51 seconds.
```

### Проверка Nodekeeper в Target-DC

Выполнить следующий вызов API кластера только на **seed-узле**, когда установка на всех узлах в **Target-DC** завершится:

```
curl -ikS https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/nodekeeper/healthCheck?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

Если код состояния не `200`, повторить попытку через несколько минут.

## Шаг 9. Миграция Cassandra

Миграция Cassandra может занять от минут до часов в зависимости от размера хранилища метрик.

### Миграция Cassandra

Чтобы начать миграцию Cassandra в **Target-DC**, выполнить следующий вызов API кластера только на **seed-узле**:

```
curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/newDc?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

В случае успеха код состояния будет `200`, а тело ответа будет содержать ID запроса, необходимый для проверки статуса миграции. Установить переменную окружения ID запроса только на **seed-узле**. ID запроса берётся из ответа предыдущего вызова API.

```
REQ_ID=<migration-new-datacenter-request-id>
```

Если код состояния не `200` и ответ не предлагает дальнейших шагов, обратиться к эксперту по продукту Dynatrace через живой чат.

### Проверка статуса миграции

Чтобы проверить статус миграции, выполнить следующий вызов API кластера только на **seed-узле**:

```
curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/newDc/$REQ_ID?Api-Token=$API_TOKEN -H  "accept: application/json" -H  "Content-Type: application/json"
```

Если код состояния не `200`, повторить попытку через несколько минут.

### Восстановление данных Cassandra

Восстановление данных Cassandra и проверка состояния Cassandra для Dynatrace релиза 254 и более ранних.

В зависимости от размера базы данных Cassandra этот процесс может занять несколько часов.

#### Восстановление данных

Чтобы восстановить Cassandra, выполнить следующую команду последовательно на каждом новом узле **Target-DC**. Использовать команду `nohup`, чтобы предотвратить прерывание выполнения скрипта (например, из-за разрыва сессии) во время важных операций.

```
sudo nohup $DT_DIR/utils/cassandra-nodetool.sh rebuild -- $SDC_NAME &
```

#### Проверка прогресса и статуса

Чтобы проверить прогресс и статус, выполнить следующий вызов API кластера только на **seed-узле**:

```
curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/rebuildStatus?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

Если код состояния не `200`, повторить попытку примерно через 15 минут. Следует помнить, что процесс восстановления может занять много времени.

### Проверка состояния Cassandra

Чтобы проверить состояние кластера Cassandra, выполнить `cassandra-nodetool.sh` с параметром `status` только на **seed-узле**:

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

Значение **Load** не должно значительно отличаться между узлами, а **Status** должен быть `UN` на всех узлах.

В зависимости от размера базы данных Cassandra это может занять несколько часов.

### Восстановление данных

Чтобы восстановить данные Cassandra в **Target-DC**, выполнить следующий вызов API кластера только на seed-узле:

```
curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/rebuild?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

В случае успеха код состояния будет `200`. Если код состояния не `200` и ответ не предлагает дальнейших шагов, обратиться к эксперту по продукту Dynatrace через живой чат в своей среде Dynatrace.

### Проверка статуса восстановления данных

Чтобы проверить статус восстановления данных, выполнить следующий вызов API кластера только на **seed-узле**:

```
curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/rebuild?Api-Token=$API_TOKEN -H  "accept: application/json" -H  "Content-Type: application/json"
```

Если код состояния не `200`, повторить попытку примерно через 15 минут. Следует помнить, что процесс восстановления данных может занять много времени.

Если в ответе флаг ошибки установлен в `true`, обратиться к эксперту по продукту Dynatrace через живой чат в своей среде.

## Шаг 10. Миграция Elasticsearch

Миграция Elasticsearch может занять от минут до часов в зависимости от размера хранилища Elasticsearch.

### Миграция Elasticsearch в Target-DC

Запустить Elasticsearch. Выполнить следующую команду последовательно только на каждом узле в **Target-DC**:

```
sudo $DT_DIR/launcher/elasticsearch.sh start
```

Чтобы начать миграцию Elasticsearch в **Target-DC**, выполнить следующий вызов API кластера только на **seed-узле**:

```
curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/restore/elasticsearch/recover?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

В случае успеха код состояния будет `200`.

### Проверка прогресса и статуса

Чтобы проверить статус миграции Elasticsearch, выполнить следующий вызов API кластера только на seed-узле:

```
curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/restore/elasticsearch/recover?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

Если код состояния не `200`, повторить попытку через несколько минут.

### Проверка миграции данных

Чтобы проверить миграцию данных Elasticsearch, выполни следующий кластерный вызов API только на **seed-узле**:

```
curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/elasticsearch/indexMigrationStatus?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

Если код статуса не `200`, попробуй снова через несколько минут.

## Шаг 11 Миграция сервера

### Миграция сервера

Запусти **Managed Cluster** в **Target-DC**, выполнив следующий кластерный вызов API только на **seed-узле**:

```
curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/restore/server/recovery?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

При успешном выполнении код статуса будет `200`, а тело ответа будет содержать ID запроса, который понадобится для проверки готовности кластера. Задай переменную окружения ID запроса только на **seed-узле**. ID запроса берётся из ответа на предыдущий вызов API.

```
REQ_ID=<migration-server-request-id>
```

Если код статуса не `200` и ответ не содержит рекомендаций по дальнейшим действиям, обратись к эксперту по продукту Dynatrace через онлайн-чат.

### Проверка готовности кластера

Чтобы проверить готовность Managed Cluster, выполни следующий кластерный вызов API только на **seed-узле**:

```
curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/restore/server/recovery/$REQ_ID?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

Если код статуса не `200`, попробуй снова через несколько минут.

## Шаг 12 Включение нового дата-центра

1. Включи трафик OneAgent.  
   Подробнее см. [Cluster node capabilities](/managed/managed-cluster/configuration/configure-cluster-capabilities "Configure OneAgent data processing and web UI traffic on individual Managed Cluster nodes using the Cluster Management Console or REST API.").
2. Включи резервное копирование в одном из ДЦ. Миграция отключает резервное копирование.  
   Подробнее см. [Back up and restore a cluster](/managed/managed-cluster/operation/back-up-and-restore-a-cluster "Understand the steps and commands required to restore a Dynatrace Managed cluster.").