---
title: Azure SQL Servers (built-in)
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-servers-builtin
scraped: 2026-05-12T11:26:54.560141
---

# Azure SQL Servers (built-in)

# Azure SQL Servers (built-in)

* Практическое руководство
* Чтение: 1 мин
* Обновлено 15 ноября 2023 г.

Информацию о различиях между классическими и другими сервисами см. в разделе [Миграция с классических (ранее «built-in») сервисов Azure на облачные сервисы](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide "Миграция классических сервисов Azure на их новые версии.").

Dynatrace получает метрики из Azure Metrics API для **Azure SQL (SQL Servers, SQL Databases, SQL elastic pools)**. Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать метрики по различным измерениям и создавать пользовательские графики, которые можно закрепить на ваших дашбордах.

## Предварительные требования

* Environment ActiveGate
* Чтобы отключить мониторинг встроенных сервисов, требуется Environment ActiveGate версии 1.245+ и Dynatrace версии 1.247+.

Этот сервис отслеживает SQL Servers, SQL-базы данных (только пользовательского типа) и SQL elastic pools.

Уже отслеживаемые ресурсы можно найти на странице обзора Azure, раздел **Databases components**.

Для мониторинга ресурсов hyperscale/data warehouse или Managed-развёртываний проверьте SQL Database Hyperscale/SQL Data Warehouse/SQL Managed Instance и страницу обзора Azure, раздел **Cloud services**.

## Включение мониторинга

О том, как включить мониторинг сервиса, см. в разделе [Включение мониторинга сервиса](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Включение мониторинга Azure в Dynatrace.").

## Просмотр метрик сервиса

Метрики сервисов Azure можно просматривать в вашем окружении Dynatrace на странице подписки Azure или на собственном дашборде.

Значения в таблице зависят от выбранного временного интервала. Подробнее см. в разделе [Устранение неполадок со сравнением временных интервалов при настройке мониторинга Azure)](https://dt-url.net/7j438f0).

### Просмотр метрик на странице учётной записи Azure

Чтобы получить доступ к метрикам на странице учётной записи Azure

1. Перейдите в **Azure**.
2. Выберите подписку Azure.
3. Выберите сервис, метрики которого нужно проверить. Метрики выбранного сервиса отображаются под инфографикой в разделе сервиса, как в примере ниже.

   ![Azure service metrics](https://dt-cdn.net/images/azure-service-1109-9488bfa5e4.png)

   Azure service metrics

### Просмотр метрик на дашборде

Вы можете создать собственный дашборд для просмотра метрик сервисов Azure. О том, как создавать дашборды, см. в разделе [Создание и редактирование дашбордов Dynatrace](/managed/analyze-explore-automate/dashboards-classic/dashboards/create-dashboards "Узнайте, как создавать и редактировать дашборды Dynatrace.").

## Доступные метрики

### SQL Databases

| Ключ метрики | Имя | Единица измерения | Агрегации | Потребление мониторинга |
| --- | --- | --- | --- | --- |
| builtin:cloud.azure.sqlDatabase.connections.blockedByFirewall | Blocked by firewall | Количество | autovalue | DDUs |
| builtin:cloud.azure.sqlDatabase.connections.failed | Failed connections | Количество | autovalue | DDUs |
| builtin:cloud.azure.sqlDatabase.connections.successful | Successful connections | Количество | autovalue | DDUs |
| builtin:cloud.azure.sqlDatabase.dtu.limit.count | DTU limit | Количество | autoavgmaxmin | DDUs |
| builtin:cloud.azure.sqlDatabase.dtu.limit.used | DTU used | Количество | autoavgmaxmin | DDUs |
| builtin:cloud.azure.sqlDatabase.dtu.consumptionPerc | DTU percentage | Процент (%) | autoavgmaxmin | DDUs |
| builtin:cloud.azure.sqlDatabase.io.dataRead | Data I/O percentage | Процент (%) | autoavgmaxmin | DDUs |
| builtin:cloud.azure.sqlDatabase.io.logWrite | Log I/O percentage | Процент (%) | autoavgmaxmin | DDUs |
| builtin:cloud.azure.sqlDatabase.storage.percent | Database size percentage | Процент (%) | autoavgmaxmin | DDUs |
| builtin:cloud.azure.sqlDatabase.storage.totalBytes | Total database size | Байт | autoavgmaxmin | DDUs |
| builtin:cloud.azure.sqlDatabase.storage.xtpPercent | In-Memory OLTP storage percent | Процент (%) | autoavgmaxmin | DDUs |
| builtin:cloud.azure.sqlDatabase.cpuPercent | CPU percentage | Процент (%) | autoavgmaxmin | DDUs |
| builtin:cloud.azure.sqlDatabase.deadlocks | Deadlocks | Количество | autovalue | DDUs |
| builtin:cloud.azure.sqlDatabase.sessions | Sessions percentage | Процент (%) | autoavgmaxmin | DDUs |
| builtin:cloud.azure.sqlDatabase.workers | Workers percentage | Процент (%) | autoavgmaxmin | DDUs |

### SQL elastic pools

| Ключ метрики | Имя | Единица измерения | Агрегации | Потребление мониторинга |
| --- | --- | --- | --- | --- |
| builtin:cloud.azure.sqlElasticPool.dtu.storage.limitBytes | Storage limit | Байт | autoavgmaxmin | DDUs |
| builtin:cloud.azure.sqlElasticPool.dtu.storage.percent | Database size percentage | Процент (%) | autoavgmaxmin | DDUs |
| builtin:cloud.azure.sqlElasticPool.dtu.storage.usedBytes | Storage used | Байт | autoavgmaxmin | DDUs |
| builtin:cloud.azure.sqlElasticPool.dtu.storage.xtpPercent | In-memory OLTP storage percent | Процент (%) | autoavgmaxmin | DDUs |
| builtin:cloud.azure.sqlElasticPool.dtu.consumption | DTU percentage | Процент (%) | autoavgmaxmin | DDUs |
| builtin:cloud.azure.sqlElasticPool.edtu.limit | eDTU limit | Количество | autoavgmaxmin | DDUs |
| builtin:cloud.azure.sqlElasticPool.edtu.used | eDTU used | Количество | autoavgmaxmin | DDUs |
| builtin:cloud.azure.sqlElasticPool.io.dataRead | Data I/O percentage | Процент (%) | autoavgmaxmin | DDUs |
| builtin:cloud.azure.sqlElasticPool.io.logWrite | Log I/O percentage | Процент (%) | autoavgmaxmin | DDUs |
| builtin:cloud.azure.sqlElasticPool.cpuPercent | CPU percentage | Процент (%) | autoavgmaxmin | DDUs |
| builtin:cloud.azure.sqlElasticPool.sessions | Sessions percentage | Процент (%) | autoavgmaxmin | DDUs |
| builtin:cloud.azure.sqlElasticPool.workers | Workers percentage | Процент (%) | autoavgmaxmin | DDUs |