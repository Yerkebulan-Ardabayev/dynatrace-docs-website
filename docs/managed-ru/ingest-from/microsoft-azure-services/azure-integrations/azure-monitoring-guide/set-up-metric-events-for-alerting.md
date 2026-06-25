---
title: Настройка метрических событий для оповещений
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/set-up-metric-events-for-alerting
scraped: 2026-05-12T11:38:13.418779
---

# Настройка метрических событий для оповещений

# Настройка метрических событий для оповещений

* Практическое руководство
* Чтение: 10 мин
* Опубликовано 8 января 2021 г.

После [настройки интеграции с Azure Monitor](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Настройка и конфигурирование мониторинга Azure в Dynatrace.") можно приступить к настройке и конфигурированию метрических событий для оповещений.

Чтобы настроить метрические события для оповещений, откройте **Settings** > **Cloud and virtualization** > **Azure** > **Metric events for alerting** > **Manage alerting rules**. На странице **Metric events for alerting** можно создавать, включать/отключать и настраивать рекомендуемые правила оповещений.
Обзор всех рекомендуемых правил оповещений для всех облачных сервисов см. в списке ниже.

### Предопределённые правила оповещений по облачному сервису

| Название | Правила оповещений |
| --- | --- |
| Azure Spring Apps | Azure Spring Apps system CPU usage (static threshold: above 95%), Azure Spring Apps process CPU usage (static threshold: above 95%). |
| Azure Blockchain Service | Azure Blockchain Service CPU usage percentage (static threshold: above 95%), Azure Blockchain Service memory usage percentage (static threshold: above 95%). |
| Azure Cache for Redis | Azure Redis memory usage % (Static threshold: above 95 %), Azure Redis CPU usage % (Static threshold: above 95 %) |
| Azure Redis (built-in) | Azure Redis CPU usage % (built-in) (Static threshold: above 95 %) |
| Azure Virtual Machine (classic) | Azure Virtual Machine (classic) percentage CPU (static threshold: above 95%). |
| Azure Storage Account (classic) | Azure Storage Account (classic) availability (static threshold: below 95%). |
| Azure Storage Blob Services (classic) | Azure Storage (classic) Blob Services availability (static threshold: below 95%). |
| Azure Storage File Services (classic) | Azure Storage (classic) File Services availability (static threshold: below 95%). |
| Azure Storage Queue Services (classic) | Azure Storage (classic) Queue Services availability (static threshold: below 95%). |
| Azure Storage Table Services (classic) | Azure Storage (classic) Table Services availability (static threshold: below 95%). |
| Azure Data Factory v2 | Azure Data Factory integration runtime CPU utilization (static threshold: above 95%). |
| Azure DB for MariaDB | Azure DB for MariaDB CPU percent (static threshold: above 95%), Azure DB for MariaDB memory percent (static threshold: above 95%), Azure DB for MariaDB IO percent (static threshold: above 95%), Azure DB for MariaDB server log storage percent (static threshold: above 95%), Azure DB for MariaDB storage percent (static threshold: above 95%). |
| Azure DB for MySQL | Azure DB for MySQL CPU percent (static threshold: above 95%), Azure DB for MySQL memory percent (static threshold: above 95%), Azure DB for MySQL IO percent (static threshold: above 95%), Azure DB for MySQL server log storage percent (static threshold: above 95%), Azure DB for MySQL storage percent (static threshold: above 95%). |
| Azure DB for PostgreSQL - Flexible Server | Azure DB for PostgreSQL (Flexible) CPU percent (Static threshold: above 95 %), Azure DB for PostgreSQL (Flexible) memory percent (Static threshold: above 95 %), Azure DB for PostgreSQL (Flexible) storage percent (Static threshold: above 95 %) |
| Azure DB for PostgreSQL - Server | Azure DB for PostgreSQL CPU percent (static threshold: above 95%), Azure DB for PostgreSQL memory percent (static threshold: above 95%), Azure DB for PostgreSQL IO percent (static threshold: above 95%), Azure DB for PostgreSQL server log storage percent (static threshold: above 95%), Azure DB for PostgreSQL storage percent (static threshold: above 95%). |
| Azure DB for PostgreSQL - Hyperscale | Azure DB for PostgreSQL CPU percent (static threshold: above 95%), Azure DB for PostgreSQL memory percent (static threshold: above 95%), Azure DB for PostgreSQL storage percent (static threshold: above 95%). |
| Azure Event Hubs Cluster | Azure Event Hubs CPU usage (static threshold: above 95%), Azure Event Hubs available memory (static threshold: below 5%). |
| Azure Application Insights | Azure Application Insights availability (static threshold: below 95%), Azure Application Insights process CPU (static threshold: above 95%), Azure Application Insights processor time (static threshold: above 95%). |
| Azure Key Vault | Azure Key Vault availability (static threshold: below 95%), Azure Key Vault saturation (static threshold: above 95%). |
| Azure Data Explorer Cluster | Azure Data Explorer Cluster cache utilization (static threshold: above 95%), Azure Data Explorer Cluster ingestion utilization (static threshold: above 95%), Azure Data Explorer Cluster CPU (static threshold: above 95%), Azure Data Explorer Cluster Export utilization (static threshold: above 95%). |
| Azure Integration Service Environment | Azure ISE run failure percentage (static threshold: above 5%), Azure ISE workflow processor usage (static threshold: above 95%), Azure ISE workflow memory usage (static threshold: above 95%). |
| Azure Logic Apps | Azure Logic Apps run failure percentage (static threshold: above 5%). |
| Azure Machine Learning Workspace | Azure Machine Learning CPU utilization (static threshold: above 95%), Azure Machine Learning GPU utilization (static threshold: above 95%), Azure Machine Learning quota utilization percentage (static threshold: above 95%). |
| Azure Maps Account | Azure Maps Account availability (static threshold: below 95%). |
| Azure Application Gateway (built-in) | Azure Application Gateway unhealthy hosts (built-in) (Static threshold: above 0 ), Azure Application Gateway failed requests (built-in) (Auto-adaptive baseline) |
| Azure Application Gateway | Azure Application Gateway unhealthy hosts count (Static threshold: above 0 ), Azure Application Gateway failed requests (Auto-adaptive baseline) |
| Azure Firewall | Azure Firewall health state (static threshold: below 95%), Azure Firewall SNAT port utilization (static threshold: above 95%). |
| Azure ExpressRoute Circuit | Azure ExpressRoute Circuit BGP availability (static threshold: below 95%), Azure ExpressRoute Circuit ARP availability (static threshold: below 95%). |
| Azure Front Door | Azure Front Door backend health percentage (static threshold: below 95%). |
| Azure Connection Monitors | Azure NetworkWatchers probes failed percent (static threshold: above 5%). |
| Azure Connection Monitors Preview | Azure NetworkWatchers probes failed percent (static threshold: above 5%), Azure NetworkWatchers checks failed percent (static threshold: above 5%). |
| Azure Public IP Address | Azure Public IP Address data path availability (static threshold: below 95%). |
| Azure Power BI Embedded | Azure Power BI embedded memory thrashing (datasets) (static threshold: above 95%). |
| Azure Search Service | Azure Search Service throttled search queries (static threshold: above 5%). |
| Azure Mesh Application | Azure Mesh Application CPU utilization (static threshold: above 95%), Azure Mesh Application memory utilization (static threshold: above 95%). |
| Azure SignalR | Azure SignalR user errors (static threshold: above 5%), Azure SignalR system errors (static threshold: above 5%). |
| Azure SQL (built-in) | Azure SQL Database CPU usage % (built-in) (Static threshold: above 95 %), Azure SQL Database used data space (built-in) (Static threshold: above 95 %) |
| Azure SQL Managed Instance | Azure SQL Managed Instance CPU usage (static threshold: above 95%). |
| Azure SQL Data Warehouse (legacy) | Azure SQL Data Warehouse CPU usage percentage (static threshold: above 95%), Azure SQL Data Warehouse memory percentage (static threshold: above 95%), Azure SQL Data Warehouse Data IO percentage (static threshold: above 95%), Azure SQL Data Warehouse DWU percentage (static threshold: above 95%). |
| Azure SQL Database (DTU) | Azure SQL Database CPU usage % (Static threshold: above 95 %), Azure SQL Database used data space (Static threshold: above 95 %) |
| Azure SQL Database - Hyperscale | Azure SQL Hyperscale Database CPU usage percentage (static threshold: above 95%), Azure SQL Hyperscale server process core percent (static threshold: above 95%), Azure SQL Hyperscale server process memory percent (static threshold: above 95%), Azure SQL Hyperscale Database Sessions percentage (static threshold: above 95%), Azure SQL Hyperscale Database Data IO percentage (static threshold: above 95%), Azure SQL Hyperscale Database Log IO percentage (static threshold: above 95%), Azure SQL Hyperscale Database In - memory OLTP storage percent (static threshold: above 95%), Azure SQL Hyperscale Database Workers percentage (static threshold: above 95%). |
| Azure SQL Database (vCore) | Azure SQL Database CPU usage % (Static threshold: above 95 %), Azure SQL Database used data space (Static threshold: above 95 %) |
| Azure Stream Analytics Job | Azure Stream Analytics job resource utilization (static threshold: above 95%). |
| Azure SQL Pool | Azure Analytics Services DWU used percentage (static threshold: above 95%), Azure Analytics Services Local tempdb used percentage (static threshold: above 95%), Azure Analytics Services memory used percentage (static threshold: above 95%), Azure Analytics Services workload group allocation by system percent (static threshold: above 95%), Azure Analytics Services workload group allocation by max resource percent (static threshold: above 95%). |
| Azure App Service Environment v2 | Azure App Service Environment CPU percentage (static threshold: above 95%), Azure App Service Environment memory percentage (static threshold: above 95%) |
| Azure App Service Plan | Azure App Service CPU percentage (static threshold: above 95%), Azure App Service memory percentage (static threshold: above 95%). |
| Azure API Management Service | Api Management capacity (Static threshold: above 95 %) |
| Azure Storage Blob Services | Azure Storage Blob Services availability (Static threshold: below 95%) |
| Azure Storage File Services | Azure Storage File Services availability (Static threshold: below 95%) |
| Azure Storage Queue Services | Azure Storage Queue Services availability (Static threshold: below 95%) |
| Azure Storage Table Services | Azure Storage Table Services availability (Static threshold: below 95%) |
| Azure Storage Account | Azure Storage Account availability (Static threshold: below 95 %) |

## Добавление сервиса в мониторинг

Количество рекомендуемых правил оповещений зависит от количества отслеживаемых облачных сервисов.
Чтобы добавить рекомендуемые правила оповещений для нового облачного сервиса, нужно сначала добавить этот сервис в мониторинг.

Чтобы добавить сервис в мониторинг,

1. Откройте **Settings**.
2. В разделе **Cloud and virtualization** выберите **Azure**.
3. На странице обзора Azure выберите **Edit** для нужного экземпляра Azure.
4. Откройте **Services**, выберите **Add service**, выберите нужное имя сервиса из списка и нажмите **Add service**.
5. Нажмите **Save changes**.

![Add azure service](https://dt-cdn.net/images/configuration-of-supporting-service-add-service-1690-2482af29eb.png)

Add azure service

Не все облачные сервисы имеют собственные предопределённые правила оповещений.

## Создание и включение правил оповещений

Не применяется к новым средам Dynatrace, созданным после 26 января 2026 г.

Чтобы включить рекомендуемые правила оповещений, сначала нужно их создать. Можно создать правила оповещений и автоматически включить их, или (если снять флажок **Automatically enable created rules**) создать их и включить вручную после возможных изменений конфигурации.

![Create alerting rules](https://dt-cdn.net/images/2020-11-30-11-56-33-1079-923b3ef77f.png)

Create alerting rules

Например, можно создать и автоматически включить первый набор оповещений. При начале мониторинга новых сервисов можно создать оповещения для этих сервисов без автоматического включения (чтобы сначала настроить их).

## Настройка правил оповещений

Не применяется к новым средам Dynatrace, созданным после 26 января 2026 г.

Способ редактирования правил зависит от того, было ли выбрано автоматическое включение оповещений.

* Если при создании оповещений было выбрано автоматическое включение, откройте **Adjust recommended alerting rules**, разверните **Enabled recommended alerting rules** и выберите любое правило. Откроется страница **Edit custom event for alerting**, где можно изменить правила конфигурации для данного сервиса.

![Conf alerts 2](https://dt-cdn.net/images/2020-12-01-15-40-01-1011-3206a4bdc7.png)

Conf alerts 2

* Если при создании оповещений автоматическое включение не было выбрано, откройте **Enable recommended alerting rules**, разверните **Disabled recommended alerting rules** и выберите любое из отключённых правил. Откроется та же страница **Edit custom event for alerting**.

![Enable rules](https://dt-cdn.net/images/2020-12-02-08-08-59-1076-1e07d04c6d.png)

Enable rules

## Отключение правил оповещений

Не применяется к новым средам Dynatrace, созданным после 26 января 2026 г.

Можно отключить все правила оповещений или отключить/удалить их выборочно.

![Custom alerts](https://dt-cdn.net/images/2020-12-01-14-08-02-1106-a6cabbaddc.png)

Custom alerts

* Чтобы отключить все правила оповещений, откройте **Adjust recommended alerting rules** и выберите **Disable all enabled recommended alerting rules**.
* Чтобы отключить или удалить правила оповещений выборочно, откройте **Adjust recommended alerting rules** и выберите **Metric events**. На странице **Metric events** можно отключить оповещение, переключив его в столбце **On/Off**, или удалить, нажав `x` в столбце **Delete**.

![Custom events](https://dt-cdn.net/images/2020-11-30-12-57-44-1098-1e38daa33f.png)

Custom events

Если отключить часть или все правила оповещений, их всегда можно включить снова.

![Enable rules](https://dt-cdn.net/images/2020-11-30-19-21-05-1110-6b33994c7a.png)

Enable rules

## Связанные темы

* [Интеграции с Microsoft Azure](/managed/ingest-from/microsoft-azure-services/azure-integrations "Настройка глубокого мониторинга кода Dynatrace в Azure с помощью OneAgent или OpenTelemetry.")