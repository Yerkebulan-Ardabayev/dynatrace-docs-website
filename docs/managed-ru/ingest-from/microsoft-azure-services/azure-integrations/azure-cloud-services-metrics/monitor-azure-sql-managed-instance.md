---
title: Мониторинг Azure SQL Managed Instance
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-managed-instance
---

# Мониторинг Azure SQL Managed Instance

# Мониторинг Azure SQL Managed Instance

* Практическое руководство
* Чтение за 1 минуту
* Опубликовано 02 июля 2020

На странице обзора Azure SQL Managed Instance можно увидеть различные аспекты производительности базы данных, включая использование CPU, количество виртуальных ядер, объём хранилища, отправленные/полученные байты ввода-вывода и многое другое.

## Предварительные требования

* Dynatrace версии 1.196+
* Environment ActiveGate версии 1.195+

## Включение мониторинга

О том, как включить мониторинг сервиса, рассказано в статье [Включение мониторинга сервиса](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Включение мониторинга Azure в Dynatrace.").

Дополнительно, для интеграции с OneAgent, см. [как отслеживается активность базы данных](/managed/observe/infrastructure-observability/database-services-classic/how-database-activity-is-monitored "Узнайте об автоматическом обнаружении и мониторинге сервисов баз данных в окружении приложения.").

## Просмотр метрик сервиса

Метрики сервиса в окружении Dynatrace можно посмотреть либо на **странице обзора custom device**, либо на странице **Dashboards**.

### Просмотр метрик на странице обзора custom device

Чтобы перейти на страницу обзора custom device

1. Перейти в **Technologies & Processes**.
2. Отфильтровать по имени сервиса и выбрать нужную группу custom device.
3. После выбора группы custom device открывается **страница обзора группы custom device**.
4. На **странице обзора группы custom device** перечислены все экземпляры (custom devices), входящие в группу. Выбрать экземпляр, чтобы перейти на **страницу обзора custom device**.

### Просмотр метрик на дашборде

Если для сервиса есть готовый дашборд, на странице **Dashboards** появится готовый дашборд для соответствующего сервиса со всеми рекомендованными метриками. Нужные дашборды можно найти, отфильтровав сначала по **Preset**, а затем по **Name**.

Для уже отслеживаемых сервисов может понадобиться заново сохранить учётные данные, чтобы готовый дашборд появился на странице **Dashboards**. Чтобы заново сохранить учётные данные, перейти в **Settings** > **Cloud and virtualization** > **Azure**, выбрать нужный экземпляр Azure, затем нажать **Save**.

Вносить изменения напрямую в готовый дашборд нельзя, но его можно клонировать и редактировать. Чтобы клонировать дашборд, открыть меню обзора (**…**) и выбрать **Clone**.  
Чтобы убрать дашборд из списка дашбордов, его можно скрыть. Для этого открыть меню обзора (**…**) и выбрать **Hide**.

Скрытие дашборда не влияет на других пользователей.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

Clone hide azure

![SQL dash](https://dt-cdn.net/images/sqlmanagedinstances-1303-b09d61719b.png)

SQL dash

## Доступные метрики

| Название | Описание | Единица измерения | Рекомендуется |
| --- | --- | --- | --- |
| avg\_cpu\_percent | Средний процент использования CPU | Percent | Applicable |
| io\_bytes\_read | Байты ввода-вывода, прочитанные | Bytes | Applicable |
| io\_bytes\_written | Байты ввода-вывода, записанные | Bytes | Applicable |
| io\_requests | Количество запросов ввода-вывода | Count | Applicable |
| reserved\_storage\_mb | Зарезервированный объём хранилища | Count | Applicable |
| storage\_space\_used\_mb | Использованный объём хранилища | Count | Applicable |
| virtual\_core\_count | Количество виртуальных ядер | Count | Applicable |