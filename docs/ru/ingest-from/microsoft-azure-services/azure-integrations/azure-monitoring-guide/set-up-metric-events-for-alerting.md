---
title: Set up metric events for alerting
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/set-up-metric-events-for-alerting
scraped: 2026-03-04T21:34:17.030619
---

# Настройка событий метрик для оповещений

# Настройка событий метрик для оповещений

* Latest Dynatrace
* Руководство
* Чтение: 10 мин
* Опубликовано 8 января 2021

После [настройки интеграции Azure Monitor](../azure-monitoring-guide.md "Настройте и сконфигурируйте мониторинг Azure в Dynatrace.") вы можете начать настройку и конфигурацию событий метрик для оповещений.

Для настройки событий метрик для оповещений перейдите в **Settings** > **Cloud and virtualization** > **Azure** > **Metric events for alerting** > **Manage alerting rules**. На странице **Metric events for alerting** вы можете создавать, включать/отключать и настраивать рекомендуемые правила оповещений.
Обзор всех рекомендуемых правил оповещений для всех облачных сервисов приведён в списке ниже.

### Предопределённые правила оповещений по облачным сервисам

| Название | Правила оповещений |
| --- | --- |
| Azure Spring Apps | Использование CPU системы Azure Spring Apps (статический порог: выше 95%), использование CPU процесса Azure Spring Apps (статический порог: выше 95%). |
| Azure Blockchain Service | Процент использования CPU Azure Blockchain Service (статический порог: выше 95%), процент использования памяти Azure Blockchain Service (статический порог: выше 95%). |
| Azure Cache for Redis | Процент использования памяти Azure Redis (статический порог: выше 95%), процент использования CPU Azure Redis (статический порог: выше 95%) |
| Azure Redis (built-in) | Процент использования CPU Azure Redis (built-in) (статический порог: выше 95%) |
| Azure Virtual Machine (classic) | Процент CPU Azure Virtual Machine (classic) (статический порог: выше 95%). |
| Azure Storage Account (classic) | Доступность Azure Storage Account (classic) (статический порог: ниже 95%). |
| Azure Storage Blob Services (classic) | Доступность Azure Storage (classic) Blob Services (статический порог: ниже 95%). |
| Azure Storage File Services (classic) | Доступность Azure Storage (classic) File Services (статический порог: ниже 95%). |
| Azure Storage Queue Services (classic) | Доступность Azure Storage (classic) Queue Services (статический порог: ниже 95%). |
| Azure Storage Table Services (classic) | Доступность Azure Storage (classic) Table Services (статический порог: ниже 95%). |
| Azure Data Factory v2 | Использование CPU среды выполнения интеграции Azure Data Factory (статический порог: выше 95%). |
| Azure DB for MariaDB | Процент CPU Azure DB for MariaDB (статический порог: выше 95%), процент памяти Azure DB for MariaDB (статический порог: выше 95%), процент IO Azure DB for MariaDB (статический порог: выше 95%), процент хранения логов сервера Azure DB for MariaDB (статический порог: выше 95%), процент хранилища Azure DB for MariaDB (статический порог: выше 95%). |
| Azure DB for MySQL | Процент CPU Azure DB for MySQL (статический порог: выше 95%), процент памяти Azure DB for MySQL (статический порог: выше 95%), процент IO Azure DB for MySQL (статический порог: выше 95%), процент хранения логов сервера Azure DB for MySQL (статический порог: выше 95%), процент хранилища Azure DB for MySQL (статический порог: выше 95%). |
| Azure DB for PostgreSQL - Flexible Server | Процент CPU Azure DB for PostgreSQL (Flexible) (статический порог: выше 95%), процент памяти Azure DB for PostgreSQL (Flexible) (статический порог: выше 95%), процент хранилища Azure DB for PostgreSQL (Flexible) (статический порог: выше 95%) |
| Azure DB for PostgreSQL - Server | Процент CPU Azure DB for PostgreSQL (статический порог: выше 95%), процент памяти Azure DB for PostgreSQL (статический порог: выше 95%), процент IO Azure DB for PostgreSQL (статический порог: выше 95%), процент хранения логов сервера Azure DB for PostgreSQL (статический порог: выше 95%), процент хранилища Azure DB for PostgreSQL (статический порог: выше 95%). |
| Azure DB for PostgreSQL - Hyperscale | Процент CPU Azure DB for PostgreSQL (статический порог: выше 95%), процент памяти Azure DB for PostgreSQL (статический порог: выше 95%), процент хранилища Azure DB for PostgreSQL (статический порог: выше 95%). |
| Azure Event Hubs Cluster | Использование CPU Azure Event Hubs (статический порог: выше 95%), доступная память Azure Event Hubs (статический порог: ниже 5%). |
| Azure Application Insights | Доступность Azure Application Insights (статический порог: ниже 95%), CPU процесса Azure Application Insights (статический порог: выше 95%), время процессора Azure Application Insights (статический порог: выше 95%). |
| Azure Key Vault | Доступность Azure Key Vault (статический порог: ниже 95%), насыщение Azure Key Vault (статический порог: выше 95%). |
| Azure Data Explorer Cluster | Использование кэша кластера Azure Data Explorer (статический порог: выше 95%), использование загрузки кластера Azure Data Explorer (статический порог: выше 95%), CPU кластера Azure Data Explorer (статический порог: выше 95%), использование экспорта кластера Azure Data Explorer (статический порог: выше 95%). |
| Azure Integration Service Environment | Процент сбоев выполнения Azure ISE (статический порог: выше 5%), использование процессора рабочего потока Azure ISE (статический порог: выше 95%), использование памяти рабочего потока Azure ISE (статический порог: выше 95%). |
| Azure Logic Apps | Процент сбоев выполнения Azure Logic Apps (статический порог: выше 5%). |
| Azure Machine Learning Workspace | Использование CPU Azure Machine Learning (статический порог: выше 95%), использование GPU Azure Machine Learning (статический порог: выше 95%), процент использования квоты Azure Machine Learning (статический порог: выше 95%). |
| Azure Maps Account | Доступность Azure Maps Account (статический порог: ниже 95%). |
| Azure Application Gateway (built-in) | Нездоровые хосты Azure Application Gateway (built-in) (статический порог: выше 0), неудачные запросы Azure Application Gateway (built-in) (авто-адаптивный базовый уровень) |
| Azure Application Gateway | Количество нездоровых хостов Azure Application Gateway (статический порог: выше 0), неудачные запросы Azure Application Gateway (авто-адаптивный базовый уровень) |
| Azure Firewall | Состояние здоровья Azure Firewall (статический порог: ниже 95%), использование портов SNAT Azure Firewall (статический порог: выше 95%). |
| Azure ExpressRoute Circuit | Доступность BGP Azure ExpressRoute Circuit (статический порог: ниже 95%), доступность ARP Azure ExpressRoute Circuit (статический порог: ниже 95%). |
| Azure Front Door | Процент здоровья бэкенда Azure Front Door (статический порог: ниже 95%). |
| Azure Connection Monitors | Процент неудачных проб Azure NetworkWatchers (статический порог: выше 5%). |
| Azure Connection Monitors Preview | Процент неудачных проб Azure NetworkWatchers (статический порог: выше 5%), процент неудачных проверок Azure NetworkWatchers (статический порог: выше 5%). |
| Azure Public IP Address | Доступность маршрута данных Azure Public IP Address (статический порог: ниже 95%). |
| Azure Power BI Embedded | Перегрузка памяти Azure Power BI embedded (наборы данных) (статический порог: выше 95%). |
| Azure Search Service | Ограниченные поисковые запросы Azure Search Service (статический порог: выше 5%). |
| Azure Mesh Application | Использование CPU Azure Mesh Application (статический порог: выше 95%), использование памяти Azure Mesh Application (статический порог: выше 95%). |
| Azure SignalR | Ошибки пользователей Azure SignalR (статический порог: выше 5%), системные ошибки Azure SignalR (статический порог: выше 5%). |
| Azure SQL (built-in) | Процент использования CPU Azure SQL Database (built-in) (статический порог: выше 95%), использованное пространство данных Azure SQL Database (built-in) (статический порог: выше 95%) |
| Azure SQL Managed Instance | Использование CPU Azure SQL Managed Instance (статический порог: выше 95%). |
| Azure SQL Data Warehouse (legacy) | Процент использования CPU Azure SQL Data Warehouse (статический порог: выше 95%), процент памяти Azure SQL Data Warehouse (статический порог: выше 95%), процент Data IO Azure SQL Data Warehouse (статический порог: выше 95%), процент DWU Azure SQL Data Warehouse (статический порог: выше 95%). |
| Azure SQL Database (DTU) | Процент использования CPU Azure SQL Database (статический порог: выше 95%), использованное пространство данных Azure SQL Database (статический порог: выше 95%) |
| Azure SQL Database - Hyperscale | Процент использования CPU Azure SQL Hyperscale Database (статический порог: выше 95%), процент ядер серверного процесса Azure SQL Hyperscale (статический порог: выше 95%), процент памяти серверного процесса Azure SQL Hyperscale (статический порог: выше 95%), процент сессий Azure SQL Hyperscale Database (статический порог: выше 95%), процент Data IO Azure SQL Hyperscale Database (статический порог: выше 95%), процент Log IO Azure SQL Hyperscale Database (статический порог: выше 95%), процент хранилища In-memory OLTP Azure SQL Hyperscale Database (статический порог: выше 95%), процент рабочих потоков Azure SQL Hyperscale Database (статический порог: выше 95%). |
| Azure SQL Database (vCore) | Процент использования CPU Azure SQL Database (статический порог: выше 95%), использованное пространство данных Azure SQL Database (статический порог: выше 95%) |
| Azure Stream Analytics Job | Использование ресурсов задания Azure Stream Analytics (статический порог: выше 95%). |
| Azure SQL Pool | Процент использования DWU Azure Analytics Services (статический порог: выше 95%), процент использования локальной tempdb Azure Analytics Services (статический порог: выше 95%), процент использования памяти Azure Analytics Services (статический порог: выше 95%), процент распределения рабочей нагрузки по системе Azure Analytics Services (статический порог: выше 95%), процент распределения рабочей нагрузки по максимальным ресурсам Azure Analytics Services (статический порог: выше 95%). |
| Azure App Service Environment v2 | Процент CPU Azure App Service Environment (статический порог: выше 95%), процент памяти Azure App Service Environment (статический порог: выше 95%) |
| Azure App Service Plan | Процент CPU Azure App Service (статический порог: выше 95%), процент памяти Azure App Service (статический порог: выше 95%). |
| Azure API Management Service | Ёмкость Api Management (статический порог: выше 95%) |
| Azure Storage Blob Services | Доступность Azure Storage Blob Services (статический порог: ниже 95%) |
| Azure Storage File Services | Доступность Azure Storage File Services (статический порог: ниже 95%) |
| Azure Storage Queue Services | Доступность Azure Storage Queue Services (статический порог: ниже 95%) |
| Azure Storage Table Services | Доступность Azure Storage Table Services (статический порог: ниже 95%) |
| Azure Storage Account | Доступность Azure Storage Account (статический порог: ниже 95%) |

## Добавление сервиса в мониторинг

Количество рекомендуемых правил оповещений зависит от количества отслеживаемых облачных сервисов.
Чтобы добавить рекомендуемые правила оповещений для нового облачного сервиса, сначала нужно добавить новый сервис в мониторинг.

Чтобы добавить сервис в мониторинг,

1. Перейдите в **Settings**.
2. В разделе **Cloud and virtualization** выберите **Azure**.
3. На странице обзора Azure выберите **Edit** для нужного экземпляра Azure.
4. Перейдите в **Services** и выберите **Add service**, выберите нужное имя сервиса из списка и выберите **Add service**.
5. Выберите **Save changes**.

![Add azure service](https://dt-cdn.net/images/configuration-of-supporting-service-add-service-1690-2482af29eb.png)

Не все облачные сервисы имеют собственные предопределённые правила оповещений.

## Создание и включение правил оповещений

Не применимо к новым средам Dynatrace, созданным после 26 января 2026 года.

Чтобы включить рекомендуемые правила оповещений, сначала нужно их создать. Вы можете создать правила оповещений и автоматически включить их, или (если вы снимете флажок **Automatically enable created rules**) создать их и включить вручную после возможных изменений конфигурации.

![Create alerting rules](https://dt-cdn.net/images/2020-11-30-11-56-33-1079-923b3ef77f.png)

Например, вы можете создать и автоматически включить первую группу оповещений. Когда вы начинаете мониторинг новых сервисов, вы можете создать оповещения для этих новых сервисов без автоматического включения (потому что сначала хотите их настроить).

## Настройка правил оповещений

Не применимо к новым средам Dynatrace, созданным после 26 января 2026 года.

Способ редактирования правил зависит от того, выбрали ли вы автоматическое включение оповещений.

* Если вы выбрали автоматическое включение оповещений при их создании, перейдите в **Adjust recommended alerting rules**, разверните **Enabled recommended alerting rules** и выберите любое правило. Это перенаправит вас в **Edit custom event for alerting**, где вы можете изменить правила конфигурации для конкретного сервиса.

![Conf alerts 2](https://dt-cdn.net/images/2020-12-01-15-40-01-1011-3206a4bdc7.png)

* Если вы не выбрали автоматическое включение оповещений при их создании, перейдите в **Enable recommended alerting rules**, разверните **Disabled recommended alerting rules** и выберите любое из отключённых правил. Это перенаправит вас на ту же страницу **Edit custom event for alerting**.

![Enable rules](https://dt-cdn.net/images/2020-12-02-08-08-59-1076-1e07d04c6d.png)

## Отключение правил оповещений

Не применимо к новым средам Dynatrace, созданным после 26 января 2026 года.

Вы можете отключить все правила оповещений или отключить или удалить их выборочно.

![Custom alerts](https://dt-cdn.net/images/2020-12-01-14-08-02-1106-a6cabbaddc.png)

* Чтобы отключить все правила оповещений, перейдите в **Adjust recommended alerting rules** и выберите **Disable all enabled recommended alerting rules**.
* Чтобы отключить или удалить правила оповещений выборочно, перейдите в **Adjust recommended alerting rules** и выберите **Metric events**. На странице **Metric events** вы можете отключить оповещение, выключив его в столбце **On/Off**, или удалить его, выбрав `x` в столбце **Delete**.

![Custom events](https://dt-cdn.net/images/2020-11-30-12-57-44-1098-1e38daa33f.png)

Если вы отключите какие-либо или все правила оповещений, вы всегда можете включить их снова.

![Enable rules](https://dt-cdn.net/images/2020-11-30-19-21-05-1110-6b33994c7a.png)

## Связанные темы

* [Интеграции Microsoft Azure](../../azure-integrations.md "Настройте глубокий мониторинг кода Dynatrace в Azure с помощью OneAgent или OpenTelemetry.")