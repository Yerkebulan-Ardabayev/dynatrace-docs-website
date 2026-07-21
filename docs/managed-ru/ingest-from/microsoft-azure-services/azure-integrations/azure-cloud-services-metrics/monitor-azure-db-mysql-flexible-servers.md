---
title: Мониторинг Azure Database for MySQL Flexible Servers
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-db-mysql-flexible-servers
---

# Мониторинг Azure Database for MySQL Flexible Servers

# Мониторинг Azure Database for MySQL Flexible Servers

* Практическое руководство
* 3 минуты на чтение
* Опубликовано 27 августа 2024 г.

С 16 сентября 2024 года Azure Database for MySQL Flexible Servers заменяет [Azure Database for MySQL Single Server](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-db-mysql "Мониторинг Azure DB for MySQL и просмотр доступных метрик.").

Страница обзора Azure Database for MySQL Flexible Servers служит исчерпывающим обзором серверов MySQL и экземпляров баз данных. Здесь можно получить полную видимость и проверить, здорова ли база данных, не работает ли она с пониженной производительностью, и нет ли сбойных соединений.

## Предварительные требования

* Dynatrace версии 1.298+
* Environment ActiveGate версии 1.195+

## Включение мониторинга

Для получения инструкций о том, как включить мониторинг сервисов, см. [Включение мониторинга сервисов](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Включение мониторинга Azure в Dynatrace.").

Дополнительно, для интеграции с OneAgent, см. [как отслеживается активность базы данных](/managed/observe/infrastructure-observability/database-services-classic/how-database-activity-is-monitored "Узнайте про автоматическое обнаружение и мониторинг сервисов баз данных в среде приложения.").

## Просмотр метрик сервиса

Метрики сервиса можно просматривать в среде Dynatrace либо на **странице обзора пользовательского устройства**, либо на странице **Dashboards**.

### Просмотр метрик на странице обзора пользовательского устройства

Чтобы перейти на страницу обзора пользовательского устройства:

1. Перейти в **Technologies & Processes**.
2. Отфильтровать по названию сервиса и выбрать нужную группу пользовательских устройств.
3. После выбора группы пользовательских устройств открывается **страница обзора группы пользовательских устройств**.
4. На **странице обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), входящие в группу. Нужно выбрать экземпляр, чтобы открыть **страницу обзора пользовательского устройства**.

### Просмотр метрик на дашборде

Если для сервиса есть готовый дашборд, на странице **Dashboards** появится готовый дашборд для соответствующего сервиса со всеми рекомендуемыми метриками. Нужные дашборды можно найти, отфильтровав по **Preset**, а затем по **Name**.

Для уже отслеживаемых сервисов может потребоваться заново сохранить учётные данные, чтобы готовый дашборд появился на странице **Dashboards**. Для этого нужно перейти в **Settings** > **Cloud and virtualization** > **Azure**, выбрать нужный экземпляр Azure, а затем нажать **Save**.

Вносить изменения напрямую в готовый дашборд нельзя, но его можно клонировать и редактировать. Чтобы клонировать дашборд, нужно открыть меню обзора (**…**) и выбрать **Clone**.
Чтобы убрать дашборд из списка дашбордов, его можно скрыть. Для этого нужно открыть меню обзора (**…**) и выбрать **Hide**.

Скрытие дашборда не влияет на других пользователей.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

Clone hide azure

## Доступные метрики

| Название | Описание | Единица измерения | Рекомендовано |
| --- | --- | --- | --- |
| aborted\_connections | Прерванные соединения | Count | Применимо |
| active\_connections | Активные соединения | Count | Применимо |
| active\_transactions | Активные транзакции | Count |  |
| backup\_storage\_used | Использовано хранилища резервных копий | Byte |  |
| binlog\_storage\_used | Использовано хранилища binlog | Byte |  |
| cpu\_credits\_consumed | Израсходовано кредитов CPU | Count |  |
| cpu\_credits\_remaining | Осталось кредитов CPU | Count |  |
| Com\_alter\_table | Com alter table | Count |  |
| Com\_create\_db | Com create DB | Count |  |
| Com\_create\_table | Com create table | Count |  |
| Com\_delete | Com delete | Count |  |
| Com\_drop\_db | Com drop DB | Count |  |
| Com\_drop\_table | Com drop table | Count |  |
| Com\_insert | Com insert | Count |  |
| Com\_select | Com select | Count |  |
| Com\_update | Com update | Count |  |
| data\_storage\_used | Использовано хранилища данных | Byte |  |
| HA\_IO\_status | Статус HA IO | Count |  |
| HA\_SQL\_status | Статус HA SQL | Count |  |
| HA\_replication\_lag | Задержка репликации HA | Second |  |
| cpu\_percent | Процент CPU хоста | Percent | Применимо |
| network\_bytes\_ingress | Входящий сетевой трафик хоста | Byte | Применимо |
| network\_bytes\_egress | Исходящий сетевой трафик хоста | Byte | Применимо |
| ibdata1\_storage\_used | Использовано хранилища ibdata1 | Byte |  |
| Innodb\_buffer\_pool\_pages\_data | Innodb buffer pool pages data | Count |  |
| Innodb\_buffer\_pool\_pages\_dirty | Innodb buffer pool pages dirty | Count |  |
| Innodb\_buffer\_pool\_pages\_flushed | Innodb buffer pool pages flushed | Count |  |
| Innodb\_buffer\_pool\_pages\_free | Innodb buffer pool pages free | Count |  |
| Innodb\_buffer\_pool\_reads | Innodb buffer pool reads | Count |  |
| Innodb\_data\_writes | Innodb data writes | Count |  |
| Innodb\_row\_lock\_time | Время блокировки строки Innodb | MilliSecond |  |
| Innodb\_row\_lock\_waits | Ожидания блокировки строки Innodb | Count |  |
| memory\_percent | Процент памяти | Percent | Применимо |
| trx\_rseg\_history\_len | Длина списка истории Mysql | Count |  |
| lock\_deadlocks | Взаимоблокировки Mysql | Count |  |
| lock\_timeouts | Таймауты блокировок Mysql | Count |  |
| Uptime | Время работы Mysql | Second |  |
| others\_storage\_used | Использовано прочего хранилища | Byte |  |
| Queries | Запросы | Count |  |
| Replica\_IO\_Running | Статус Replica IO | Count |  |
| Replica\_SQL\_Running | Статус Replica SQL | Count |  |
| replication\_lag | Задержка репликации в секундах | Second | Применимо |
| serverlog\_storage\_limit | Лимит хранилища журнала сервера | Byte |  |
| serverlog\_storage\_percent | Процент хранилища журнала сервера | Percent | Применимо |
| serverlog\_storage\_usage | Использовано хранилища журнала сервера | Byte |  |
| Slow\_queries | Медленные запросы | Count |  |
| storage\_io\_count | Количество операций IO хранилища | Count |  |
| io\_consumption\_percent | Процент IO хранилища | Percent | Применимо |
| storage\_limit | Лимит хранилища | Byte |  |
| storage\_percent | Процент хранилища | Percent |  |
| storage\_used | Использовано хранилища | Byte |  |
| Threads\_running | Работающие потоки | Count |  |
| total\_connections | Всего соединений | Count |  |