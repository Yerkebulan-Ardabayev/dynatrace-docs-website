#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""L4-IF.37 — RU build for 12 Azure database/data/analytics metric files.

Column-aware engine: each table's header row is read to map column name ->
index, so files with mixed table shapes (Description|Dimensions|Unit vs
Description|Unit|Dimensions, e.g. event-grid/synapse) are handled safely.
Name + Dimensions cells stay EN (Azure Metrics API identifiers); only
Description / Unit / Recommended cells + header labels are translated.

Boilerplate (View service metrics, steps, clone/hide) is byte-identical to the
shipped monitor-azure-ai-* family (_build_azure_ai.py) and reused verbatim.
Canon: L4-IF.34/35 metric-leaf, L85 (match subdirectory siblings), L96
(Необязательный/Обязательный n/a here), migration-note RU pulled from shipped
azure corpus. No em-dash (CLAUDE.md §0).
"""

import os

EN_DIR = "docs/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics"
RU_DIR = "docs/managed-ru/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics"

BATCH = [
    "monitor-azure-sql-database-dtu.md",
    "monitor-azure-sql-database-vcore.md",
    "monitor-azure-sql-elastic-pool-dtu.md",
    "monitor-azure-sql-elastic-pool-vcore.md",
    "monitor-azure-sql-data-warehouse.md",
    "monitor-azure-synapse-analytics.md",
    "monitor-azure-cosmos-db-account-mongodb.md",
    "monitor-azure-cosmos-db-account-globaldocumentdb.md",
    "monitor-azure-data-factory.md",
    "monitor-azure-data-lake-analytics.md",
    "monitor-azure-data-explorer-cluster.md",
    "monitor-azure-machine-learning.md",
]

# ---- per-file EN title (== title: + both H1) -> RU title ----
TITLE_MAP = {
    "monitor-azure-sql-database-dtu.md": (
        "Azure SQL Database (DTU) monitoring",
        "Мониторинг Azure SQL Database (DTU)",
    ),
    "monitor-azure-sql-database-vcore.md": (
        "Azure SQL Database (vCore) monitoring",
        "Мониторинг Azure SQL Database (vCore)",
    ),
    "monitor-azure-sql-elastic-pool-dtu.md": (
        "Azure SQL elastic pool (DTU) monitoring",
        "Мониторинг Azure SQL elastic pool (DTU)",
    ),
    "monitor-azure-sql-elastic-pool-vcore.md": (
        "Azure SQL elastic pool (vCore) monitoring",
        "Мониторинг Azure SQL elastic pool (vCore)",
    ),
    "monitor-azure-sql-data-warehouse.md": (
        "Azure SQL Data Warehouse (legacy)",
        "Azure SQL Data Warehouse (устаревшее)",
    ),
    "monitor-azure-synapse-analytics.md": (
        "Azure Synapse Analytics (Synapse Workspace, Apache Spark pool, SQL pool) monitoring",
        "Мониторинг Azure Synapse Analytics (Synapse Workspace, Apache Spark pool, SQL pool)",
    ),
    "monitor-azure-cosmos-db-account-mongodb.md": (
        "Azure Cosmos DB Account (MongoDB) monitoring",
        "Мониторинг Azure Cosmos DB Account (MongoDB)",
    ),
    "monitor-azure-cosmos-db-account-globaldocumentdb.md": (
        "Azure Cosmos DB Account (GlobalDocumentDB) monitoring",
        "Мониторинг Azure Cosmos DB Account (GlobalDocumentDB)",
    ),
    "monitor-azure-data-factory.md": (
        "Azure Data Factory (V1, V2) monitoring",
        "Мониторинг Azure Data Factory (V1, V2)",
    ),
    "monitor-azure-data-lake-analytics.md": (
        "Azure Data Lake Analytics monitoring",
        "Мониторинг Azure Data Lake Analytics",
    ),
    "monitor-azure-data-explorer-cluster.md": (
        "Azure Data Explorer monitoring",
        "Мониторинг Azure Data Explorer",
    ),
    "monitor-azure-machine-learning.md": (
        "Azure Machine Learning monitoring",
        "Мониторинг Azure Machine Learning",
    ),
}

DATE_MAP = {
    "* Updated on Nov 15, 2023": "* Обновлено 15 ноября 2023",
    "* Published Jul 27, 2020": "* Опубликовано 27 июля 2020 г.",
    "* Published Aug 19, 2020": "* Опубликовано 19 августа 2020 г.",
    "* Published Aug 12, 2021": "* Опубликовано 12 августа 2021 г.",
    "* Published Sep 22, 2020": "* Опубликовано 22 сентября 2020 г.",
    "* Published Sep 23, 2020": "* Опубликовано 23 сентября 2020 г.",
}

# ---- line-level substring replacements (applied to NON-table lines only) ----
PROSE = [
    ("* How-to guide", "* Практическое руководство"),
    ("* 1-min read", "* Чтение: 1 мин"),
    ("* 3-min read", "* Чтение: 3 мин"),
    ("* 4-min read", "* Чтение: 4 мин"),
    ("* 5-min read", "* Чтение: 5 мин"),
    ("* 9-min read", "* Чтение: 9 мин"),
    ("## Prerequisites", "## Предварительные условия"),
    ("Dynatrace version ", "Dynatrace версии "),
    ("Environment ActiveGate version ", "Environment ActiveGate версии "),
    # intro: ML variant first (more specific), then standard prefix, then suffix
    (
        "Dynatrace ingests metrics for multiple preselected namespaces, including ",
        "Dynatrace получает метрики для нескольких предварительно выбранных пространств имён, включая ",
    ),
    (
        "Dynatrace ingests metrics from Azure Metrics API for ",
        "Dynatrace получает метрики из Azure Metrics API для ",
    ),
    (
        ". You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.",
        ". Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать метрики по различным измерениям и создавать пользовательские графики, которые можно закрепить на ваших дашбордах.",
    ),
    # migration note (shipped azure-corpus canon)
    (
        "For information about differences between classic services and other services, see [Migrate from Azure classic (formerly 'built-in') services to cloud services](",
        "Информацию о различиях между классическими службами и другими службами см. в разделе [Миграция с классических служб Azure (ранее «встроенных») на облачные службы](",
    ),
    (
        "Migrate Azure classic services to their new versions.",
        "Перенос классических служб Azure на их новые версии.",
    ),
    # enable monitoring
    ("## Enable monitoring", "## Включение мониторинга"),
    (
        "To learn how to enable service monitoring, see [Enable service monitoring](",
        "Чтобы узнать, как включить мониторинг сервиса, см. [Включение мониторинга сервиса](",
    ),
    (
        "Enable Azure monitoring in Dynatrace.",
        "Включение мониторинга Azure в Dynatrace.",
    ),
    # view service metrics boilerplate (byte-identical to AI family)
    ("## View service metrics", "## Просмотр метрик сервиса"),
    (
        "You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.",
        "Вы можете просматривать метрики сервиса в вашей среде Dynatrace на **странице обзора пользовательского устройства** или на странице **Dashboards**.",
    ),
    (
        "### View metrics on the custom device overview page",
        "### Просмотр метрик на странице обзора пользовательского устройства",
    ),
    (
        "To access the custom device overview page",
        "Чтобы перейти на страницу обзора пользовательского устройства:",
    ),
    (
        "1. Go to **Technologies & Processes**.",
        "1. Перейдите в **Technologies & Processes**.",
    ),
    (
        "2. Filter by service name and select the relevant custom device group.",
        "2. Отфильтруйте по имени сервиса и выберите соответствующую группу пользовательских устройств.",
    ),
    (
        "3. Once you select the custom device group, you're on the **custom device group overview page**.",
        "3. После выбора группы пользовательских устройств вы окажетесь на **странице обзора группы пользовательских устройств**.",
    ),
    (
        "4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.",
        "4. На **странице обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), принадлежащие группе. Выберите экземпляр для просмотра **страницы обзора пользовательского устройства**.",
    ),
    ("### View metrics on your dashboard", "### Просмотр метрик на дашборде"),
    (
        "If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.",
        "Если для сервиса предусмотрен предустановленный дашборд, он появится на вашей странице **Dashboards** с набором всех рекомендуемых метрик. Искать конкретные дашборды можно с помощью фильтрации по **Preset**, а затем по **Name**.",
    ),
    (
        "For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.",
        "Для уже отслеживаемых сервисов может потребоваться повторно сохранить учётные данные, чтобы предустановленный дашборд отобразился на странице **Dashboards**. Для повторного сохранения учётных данных перейдите в **Settings** > **Cloud and virtualization** > **Azure**, выберите нужный экземпляр Azure, затем нажмите **Save**.",
    ),
    (
        "You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (",
        "Вы не можете вносить изменения непосредственно в предустановленный дашборд, но можете клонировать его и редактировать. Чтобы клонировать дашборд, откройте меню обзора (",
    ),
    (") and select **Clone**.", ") и выберите **Clone**."),
    (
        "To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (",
        "Чтобы убрать дашборд из списка, его можно скрыть. Чтобы скрыть дашборд, откройте меню обзора (",
    ),
    (") and select **Hide**.", ") и выберите **Hide**."),
    (
        "Hiding a dashboard doesn't affect other users.",
        "Скрытие дашборда не затрагивает других пользователей.",
    ),
    ("## Available metrics", "## Доступные метрики"),
    # ---- per-file special prose ----
    (
        "This service monitors a part of Azure Cosmos DB Account (Microsoft.DocumentDB/databaseAccounts). While you have this service configured, you can't have Azure Cosmos Database (built-in) service turned on.",
        "Этот сервис отслеживает часть Azure Cosmos DB Account (Microsoft.DocumentDB/databaseAccounts). Пока этот сервис настроен, вы не можете включить сервис Azure Cosmos Database (built-in).",
    ),
    (
        "This service monitors a part of Azure SQL (Microsoft.Sql/servers/databases). While you have this service configured, you can't have Azure Sql Servers (built-in) service turned on.",
        "Этот сервис отслеживает часть Azure SQL (Microsoft.Sql/servers/databases). Пока этот сервис настроен, вы не можете включить сервис Azure Sql Servers (built-in).",
    ),
    (
        "This service monitors a part of Azure SQL (Microsoft.Sql/servers/elasticpools). While you have this service configured, you can't have Azure Sql Servers (built-in) service turned on.",
        "Этот сервис отслеживает часть Azure SQL (Microsoft.Sql/servers/elasticpools). Пока этот сервис настроен, вы не можете включить сервис Azure Sql Servers (built-in).",
    ),
    (
        "The Azure SQL Data Warehouse overview page gives you a comprehensive view of how many jobs and tasks were completed over a period of time. You can also track nodes in different states, such as running, idle, or offline.",
        "Страница обзора Azure SQL Data Warehouse даёт полное представление о том, сколько заданий и задач было выполнено за период времени. Вы также можете отслеживать узлы в различных состояниях, таких как работающие, простаивающие или отключённые.",
    ),
    (
        "This service monitors the data warehouse type of SQL Databases. You can find the already monitored resources on the Azure overview page in the **Cloud services** section.",
        "Этот сервис отслеживает тип SQL-баз данных, представляющий хранилище данных. Уже отслеживаемые ресурсы можно найти на странице обзора Azure в разделе **Cloud services**.",
    ),
    (
        "To monitor the SQL Databases user kind, check Azure SQL Servers and the **Databases components** sections on the Azure overview page.",
        "Для мониторинга пользовательского типа SQL-баз данных проверьте Azure SQL Servers и разделы **Databases components** на странице обзора Azure.",
    ),
]

HEADER_LABEL = {
    "Name": "Имя",
    "Description": "Описание",
    "Dimensions": "Измерения",
    "Unit": "Единица измерения",
    "Recommended": "Рекомендуется",
}

UNIT_MAP = {
    "Count": "Количество",
    "Percent": "Процент",
    "Byte": "Байт",
    "Bytes": "Байты",
    "MilliSecond": "Миллисекунда",
    "MilliSeconds": "Миллисекунды",
    "Second": "Секунда",
    "Seconds": "Секунды",
    "GigaByte": "Гигабайт",
    "MegaByte": "Мегабайт",
    "BytePerSecond": "Байт в секунду",
    "BytesPerSecond": "Байт в секунду",
    "PerSecond": "В секунду",
    "": "",
}

REC_MAP = {"Applicable": "Применимо", "": ""}

# malformed scraper row (sql-data-warehouse): description sits in Name column,
# dimension under Description, unit under Dimensions. Whole-line override mirrors
# the broken EN structure (line-parity) while translating description + unit.
WHOLE_LINE = {
    "| The percentage allocation of resources relative to the effective cap resource percent per workload group. This metric provides the effective utilization of the workload group. | Is user defined, Workload group. | Percent |  |  |": "| Процентное распределение ресурсов относительно эффективного предельного процента ресурсов для каждой группы рабочей нагрузки. Эта метрика отражает фактическую утилизацию группы рабочей нагрузки. | Is user defined, Workload group. | Процент |  |  |",
}

# ---- metric Description cell translations (EN exact -> RU). Name + Dimensions EN. ----
DESC_MAP = {
    "Account Created": "Создание учётной записи",
    "Account Deleted": "Удаление учётной записи",
    "Account Diagnostic Settings Updated": "Обновление настроек диагностики учётной записи",
    "Account Keys Updated": "Обновление ключей учётной записи",
    "Account Network Settings Updated": "Обновление сетевых настроек учётной записи",
    "Account Replication Settings Updated": "Обновление настроек репликации учётной записи",
    "Account requests availability at one hour, day or month granularity": "Доступность запросов к учётной записи с детализацией по часу, дню или месяцу",
    "Active Apache Spark applications": "Активные приложения Apache Spark",
    "Active queries. Using this metric unfiltered and unsplit displays all active queries running on the system.": "Активные запросы. Использование этой метрики без фильтрации и разбиения отображает все активные запросы, выполняемые в системе.",
    "Allocated data storage. Not applicable to data warehouses.": "Выделенное хранилище данных. Неприменимо к хранилищам данных.",
    "App CPU billed. Applies to serverless databases.": "Тарифицируемое использование ЦП приложения. Применимо к бессерверным базам данных.",
    "App CPU percentage. Applies to serverless databases.": "Процент использования ЦП приложения. Применимо к бессерверным базам данных.",
    "App memory percentage. Applies to serverless databases.": "Процент использования памяти приложения. Применимо к бессерверным базам данных.",
    "Autoscale Max Throughput": "Максимальная пропускная способность автомасштабирования",
    "Average CPU usage across dedicated gateway instances": "Среднее использование ЦП по экземплярам выделенного шлюза",
    "Average CPU usage across materialized view builder instances, which are used for populating data in materialized views": "Среднее использование ЦП по экземплярам построителя материализованных представлений, которые используются для заполнения данных в материализованных представлениях",
    "Average Maximum CPU usage across dedicated gateway instances": "Среднее максимальное использование ЦП по экземплярам выделенного шлюза",
    "Average Maximum CPU usage across materialized view builder instances, which are used for populating data in materialized views": "Среднее максимальное использование ЦП по экземплярам построителя материализованных представлений, которые используются для заполнения данных в материализованных представлениях",
    "Average memory usage across dedicated gateway instances, which is used for both routing requests and caching data": "Среднее использование памяти по экземплярам выделенного шлюза, которая используется как для маршрутизации запросов, так и для кэширования данных",
    "Average memory usage across materialized view builder instances, which are used for populating data in materialized views": "Среднее использование памяти по экземплярам построителя материализованных представлений, которые используются для заполнения данных в материализованных представлениях",
    "AzureTable Table Created": "Создание таблицы AzureTable",
    "AzureTable Table Deleted": "Удаление таблицы AzureTable",
    "AzureTable Table Throughput Updated": "Обновление пропускной способности таблицы AzureTable",
    "AzureTable Table Updated": "Обновление таблицы AzureTable",
    "Blocked by Firewall": "Заблокировано брандмауэром",
    "CPU limit. Applies to vCore-based databases.": "Лимит ЦП. Применимо к базам данных на основе vCore.",
    "CPU limit. Applies to vCore-based elastic pools.": "Лимит ЦП. Применимо к эластичным пулам на основе vCore.",
    "CPU percentage": "Процент использования ЦП",
    "CPU usage across dedicated gateway instances": "Использование ЦП по экземплярам выделенного шлюза",
    "CPU usage as a percentage of the SQL DB process. Applies to elastic pools. (This metric is equivalent to sql\\_instance\\_cpu\\_percent, and will be removed in the future.)": "Использование ЦП в процентах от процесса SQL DB. Применимо к эластичным пулам. (Эта метрика эквивалентна sql\\_instance\\_cpu\\_percent и будет удалена в будущем.)",
    "CPU usage as a percentage of the SQL DB process. Not applicable to data warehouses. (This metric is equivalent to sql\\_instance\\_cpu\\_percent, and will be removed in the future.)": "Использование ЦП в процентах от процесса SQL DB. Неприменимо к хранилищам данных. (Эта метрика эквивалентна sql\\_instance\\_cpu\\_percent и будет удалена в будущем.)",
    "CPU used. Applies to vCore-based databases.": "Использовано ЦП. Применимо к базам данных на основе vCore.",
    "CPU used. Applies to vCore-based elastic pools.": "Использовано ЦП. Применимо к эластичным пулам на основе vCore.",
    "Cancelled pipeline runs metrics": "Метрики отменённых запусков конвейеров",
    "Cassandra Connector Average ReplicationLatency": "Средняя задержка репликации коннектора Cassandra",
    "Cassandra Connector Replication Health Status": "Состояние работоспособности репликации коннектора Cassandra",
    "Cassandra Keyspace Created": "Создание пространства ключей Cassandra",
    "Cassandra Keyspace Deleted": "Удаление пространства ключей Cassandra",
    "Cassandra Keyspace Throughput Updated": "Обновление пропускной способности пространства ключей Cassandra",
    "Cassandra Keyspace Updated": "Обновление пространства ключей Cassandra",
    "Cassandra Table Created": "Создание таблицы Cassandra",
    "Cassandra Table Deleted": "Удаление таблицы Cassandra",
    "Cassandra Table Throughput Updated": "Обновление пропускной способности таблицы Cassandra",
    "Cassandra Table Updated": "Обновление таблицы Cassandra",
    "Count of cancelled jobs": "Количество отменённых заданий",
    "Count of failed jobs": "Количество заданий с ошибкой",
    "Count of metadata requests. Cosmos DB maintains system metadata collection for each account, that allows you to enumerate collections, databases, etc, and their configurations, free of charge.": "Количество запросов метаданных. Cosmos DB поддерживает коллекцию системных метаданных для каждой учётной записи, что позволяет бесплатно перечислять коллекции, базы данных и т. д., а также их конфигурации.",
    "Count of successful jobs": "Количество успешных заданий",
    "Cumulative count of requests queued after the maximum concurrency limit was reached.": "Накопительное количество запросов, поставленных в очередь после достижения максимального предела параллелизма.",
    "Cumulative differential backup storage size. Applies to vCore-based databases. Not applicable to Hyperscale databases.": "Накопительный размер хранилища разностных резервных копий. Применимо к базам данных на основе vCore. Неприменимо к базам данных Hyperscale.",
    "Cumulative full backup storage size. Applies to vCore-based databases. Not applicable to Hyperscale databases.": "Накопительный размер хранилища полных резервных копий. Применимо к базам данных на основе vCore. Неприменимо к базам данных Hyperscale.",
    "Cumulative log backup storage size. Applies to vCore-based and Hyperscale databases.": "Накопительный размер хранилища резервных копий журналов. Применимо к базам данных на основе vCore и Hyperscale.",
    "DTU Limit. Applies to DTU-based databases.": "Лимит DTU. Применимо к базам данных на основе DTU.",
    "DTU Percentage. Applies to DTU-based databases.": "Процент DTU. Применимо к базам данных на основе DTU.",
    "DTU Percentage. Applies to DTU-based elastic pools.": "Процент DTU. Применимо к эластичным пулам на основе DTU.",
    "DTU used. Applies to DTU-based databases.": "Использовано DTU. Применимо к базам данных на основе DTU.",
    "DWU limit \\* DWU percentage": "Лимит DWU \\* процент DWU",
    "Data IO percentage": "Процент ввода-вывода данных",
    "Data max size. Not applicable to hyperscale": "Максимальный размер данных. Неприменимо к hyperscale",
    "Data space allocated percent. Not applicable to hyperscale": "Процент выделенного пространства для данных. Неприменимо к hyperscale",
    "Data space allocated. Not applicable to hyperscale": "Выделенное пространство для данных. Неприменимо к hyperscale",
    "Data space used percent. Not applicable to data warehouses or hyperscale databases.": "Процент использованного пространства для данных. Неприменимо к хранилищам данных или базам данных hyperscale.",
    "Data space used percent. Not applicable to hyperscale": "Процент использованного пространства для данных. Неприменимо к hyperscale",
    "Data space used. Not applicable to data warehouses.": "Использованное пространство для данных. Неприменимо к хранилищам данных.",
    "Data space used. Not applicable to hyperscale": "Использованное пространство для данных. Неприменимо к hyperscale",
    "Deadlocks. Not applicable to data warehouses.": "Взаимоблокировки. Неприменимо к хранилищам данных.",
    "Ended Apache Spark applications": "Завершённые приложения Apache Spark",
    "Failed Connections": "Неудачные подключения",
    "Failed Connections : User Errors": "Неудачные подключения: ошибки пользователя",
    "Failed pipeline runs metrics": "Метрики запусков конвейеров с ошибкой",
    "Gremlin Database Created": "Создание базы данных Gremlin",
    "Gremlin Database Deleted": "Удаление базы данных Gremlin",
    "Gremlin Database Throughput Updated": "Обновление пропускной способности базы данных Gremlin",
    "Gremlin Database Updated": "Обновление базы данных Gremlin",
    "Gremlin Graph Created": "Создание графа Gremlin",
    "Gremlin Graph Deleted": "Удаление графа Gremlin",
    "Gremlin Graph Throughput Updated": "Обновление пропускной способности графа Gremlin",
    "Gremlin Graph Updated": "Обновление графа Gremlin",
    "In-Memory OLTP storage percent. Not applicable to data warehouses.": "Процент хранилища In-Memory OLTP. Неприменимо к хранилищам данных.",
    "In-Memory OLTP storage percent. Not applicable to hyperscale": "Процент хранилища In-Memory OLTP. Неприменимо к hyperscale",
    "Indicates whether continuous export succeeded or failed": "Указывает, завершился ли непрерывный экспорт успешно или с ошибкой",
    "Integration runtime CPU utilization": "Загрузка ЦП среды выполнения интеграции",
    "Integration runtime available memory": "Доступная память среды выполнения интеграции",
    "Integration runtime available node count": "Количество доступных узлов среды выполнения интеграции",
    "Integration runtime queue duration": "Длительность очереди среды выполнения интеграции",
    "Integration runtime queue length": "Длина очереди среды выполнения интеграции",
    "Ledger digests that failed to be uploaded.": "Дайджесты реестра, которые не удалось отправить.",
    "Ledger digests that were successfully uploaded.": "Дайджесты реестра, которые были успешно отправлены.",
    "Log IO percentage": "Процент ввода-вывода журнала",
    "Log IO percentage. Not applicable to data warehouses.": "Процент ввода-вывода журнала. Неприменимо к хранилищам данных.",
    "Max RU consumption percentage per minute": "Максимальный процент потребления RU в минуту",
    "Maximum allowed entities count": "Максимально допустимое количество сущностей",
    "Maximum allowed factory size (GB unit)": "Максимально допустимый размер фабрики (в ГБ)",
    "Maximum time difference in minutes between data in source container and data propagated to materialized view": "Максимальная разница во времени (в минутах) между данными в исходном контейнере и данными, перенесёнными в материализованное представление",
    "Measures how well workloads are utilizing the adaptive cache. Use this metric with the cache hit percentage metric to determine whether to scale for additional capacity or rerun workloads to hydrate the cache.": "Измеряет, насколько эффективно рабочие нагрузки используют адаптивный кэш. Используйте эту метрику вместе с метрикой процента попаданий в кэш, чтобы определить, нужно ли масштабировать дополнительную ёмкость или перезапустить рабочие нагрузки для наполнения кэша.",
    "Measures how well workloads are utilizing the adaptive cache. Use this metric with the cache used percentage metric to determine whether to scale for additional capacity or rerun workloads to hydrate the cache.": "Измеряет, насколько эффективно рабочие нагрузки используют адаптивный кэш. Используйте эту метрику вместе с метрикой процента использования кэша, чтобы определить, нужно ли масштабировать дополнительную ёмкость или перезапустить рабочие нагрузки для наполнения кэша.",
    "Memory allocated (in GB)": "Выделенная память (в ГБ)",
    "Memory usage across dedicated gateway instances": "Использование памяти по экземплярам выделенного шлюза",
    "Memory usage as a percentage of the SQL DB process. Applies to elastic pools. (This metric is equivalent to sql\\_instance\\_memory\\_percent, and will be removed in the future.)": "Использование памяти в процентах от процесса SQL DB. Применимо к эластичным пулам. (Эта метрика эквивалентна sql\\_instance\\_memory\\_percent и будет удалена в будущем.)",
    "Memory usage as a percentage of the SQL DB process. Not applicable to data warehouses. (This metric is equivalent to sql\\_instance\\_memory\\_percent, and will be removed in the future.)": "Использование памяти в процентах от процесса SQL DB. Неприменимо к хранилищам данных. (Эта метрика эквивалентна sql\\_instance\\_memory\\_percent и будет удалена в будущем.)",
    "Mongo Collection Created": "Создание коллекции Mongo",
    "Mongo Collection Deleted": "Удаление коллекции Mongo",
    "Mongo Collection Throughput Updated": "Обновление пропускной способности коллекции Mongo",
    "Mongo Collection Updated": "Обновление коллекции Mongo",
    "Mongo Database Created": "Создание базы данных Mongo",
    "Mongo Database Deleted": "Удаление базы данных Mongo",
    "Mongo Database Throughput Updated": "Обновление пропускной способности базы данных Mongo",
    "Mongo Database Updated": "Обновление базы данных Mongo",
    "Mongo Request Units Consumed": "Потреблено единиц запросов Mongo",
    "Number of Cassandra connections that were closed, reported at a 1 minute granularity": "Количество закрытых подключений Cassandra, регистрируется с детализацией в 1 минуту",
    "Number of Cassandra requests made": "Количество выполненных запросов Cassandra",
    "Number of Gremlin requests made": "Количество выполненных запросов Gremlin",
    "Number of Mongo Requests Made": "Количество выполненных запросов Mongo",
    "Number of SQL requests": "Количество запросов SQL",
    "Number of active cores.": "Количество активных ядер.",
    "Number of active nodes. These are the nodes which are actively running a job.": "Количество активных узлов. Это узлы, которые активно выполняют задание.",
    "Number of active sessions": "Количество активных сессий",
    "Number of active sessions. Not applicable to Synapse DW Analytics.": "Количество активных сессий. Неприменимо к Synapse DW Analytics.",
    "Number of idle cores.": "Количество простаивающих ядер.",
    "Number of idle nodes. Idle nodes are the nodes which are not running any jobs but can accept new job if available.": "Количество простаивающих узлов. Простаивающие узлы не выполняют заданий, но могут принять новое задание при его наличии.",
    "Number of items evicted from the integrated cache due to TTL expiration": "Количество элементов, вытесненных из интегрированного кэша из-за истечения TTL",
    "Number of leaving cores": "Количество высвобождаемых ядер",
    "Number of leaving nodes. Leaving nodes are the nodes which just finished processing a job and will go to Idle state.": "Количество высвобождаемых узлов. Высвобождаемые узлы только что завершили обработку задания и перейдут в состояние простоя.",
    "Number of model deployments started in this workspace.": "Количество развёртываний модели, запущенных в этой рабочей области.",
    "Number of model deployments that failed in this workspace.": "Количество развёртываний модели, завершившихся с ошибкой в этой рабочей области.",
    "Number of model deployments that succeeded in this workspace.": "Количество развёртываний модели, успешно завершённых в этой рабочей области.",
    "Number of model registrations that failed in this workspace.": "Количество регистраций модели, завершившихся с ошибкой в этой рабочей области.",
    "Number of model registrations that succeeded in this workspace.": "Количество регистраций модели, успешно завершённых в этой рабочей области.",
    "Number of point reads that used the integrated cache divided by number of point reads routed through the dedicated gateway with eventual consistency": "Количество точечных чтений, использовавших интегрированный кэш, делённое на количество точечных чтений, направленных через выделенный шлюз с итоговой согласованностью",
    "Number of preempted cores": "Количество вытесненных ядер",
    "Number of preempted nodes. These nodes are the low priority nodes which are taken away from the available node pool.": "Количество вытесненных узлов. Это узлы с низким приоритетом, которые изымаются из доступного пула узлов.",
    "Number of queries evicted from the integrated cache due to TTL expiration": "Количество запросов, вытесненных из интегрированного кэша из-за истечения TTL",
    "Number of queries that used the integrated cache divided by number of queries routed through the dedicated gateway with eventual consistency": "Количество запросов, использовавших интегрированный кэш, делённое на количество запросов, направленных через выделенный шлюз с итоговой согласованностью",
    "Number of requests made": "Количество выполненных запросов",
    "Number of run errors in this workspace. Count is updated whenever run encounters an error.": "Количество ошибок запусков в этой рабочей области. Счётчик обновляется каждый раз, когда запуск сталкивается с ошибкой.",
    "Number of run warnings in this workspace. Count is updated whenever a run encounters a warning.": "Количество предупреждений запусков в этой рабочей области. Счётчик обновляется каждый раз, когда запуск сталкивается с предупреждением.",
    "Number of runs cancelled for this workspace. Count is updated when a run is successfully cancelled.": "Количество запусков, отменённых для этой рабочей области. Счётчик обновляется, когда запуск успешно отменён.",
    "Number of runs completed successfully for this workspace. Count is updated when a run has completed and output has been collected.": "Количество запусков, успешно завершённых для этой рабочей области. Счётчик обновляется, когда запуск завершён и выходные данные собраны.",
    "Number of runs entered finalizing state for this workspace. Count is updated when a run has completed but output collection still in progress.": "Количество запусков, перешедших в состояние финализации для этой рабочей области. Счётчик обновляется, когда запуск завершён, но сбор выходных данных ещё продолжается.",
    "Number of runs failed for this workspace. Count is updated when a run fails.": "Количество запусков, завершившихся с ошибкой для этой рабочей области. Счётчик обновляется, когда запуск завершается с ошибкой.",
    "Number of runs in Not Started state for this workspace. Count is updated when a request is received to create a run but run information has not yet been populated.": "Количество запусков в состоянии «Не запущен» для этой рабочей области. Счётчик обновляется, когда получен запрос на создание запуска, но информация о запуске ещё не заполнена.",
    "Number of runs not responding for this workspace. Count is updated when a run enters Not Responding state.": "Количество не отвечающих запусков для этой рабочей области. Счётчик обновляется, когда запуск переходит в состояние «Не отвечает».",
    "Number of runs running for this workspace. Count is updated when a run starts running on required resources.": "Количество выполняющихся запусков для этой рабочей области. Счётчик обновляется, когда запуск начинает выполняться на необходимых ресурсах.",
    "Number of runs started for this workspace. Count is updated after request to create run and run info, such as the Run Id, has been populated.": "Количество запущенных запусков для этой рабочей области. Счётчик обновляется после того, как запрос на создание запуска и сведения о запуске, такие как Run Id, заполнены.",
    "Number of runs that are preparing for this workspace. Count is updated when a run enters Preparing state while the run environment is being prepared.": "Количество запусков в состоянии подготовки для этой рабочей области. Счётчик обновляется, когда запуск переходит в состояние Preparing во время подготовки среды запуска.",
    "Number of runs that are provisioning for this workspace. Count is updated when a run is waiting on compute target creation or provisioning.": "Количество запусков, ожидающих выделения ресурсов, для этой рабочей области. Счётчик обновляется, когда запуск ожидает создания или подготовки целевого вычислительного ресурса.",
    "Number of runs that are queued for this workspace. Count is updated when a run is queued in compute target. Can occur when waiting for required compute nodes to be ready.": "Количество запусков в очереди для этой рабочей области. Счётчик обновляется, когда запуск ставится в очередь на целевом вычислительном ресурсе. Может возникать при ожидании готовности необходимых вычислительных узлов.",
    "Number of runs where cancel was requested for this workspace. Count is updated when cancellation request has been received for a run.": "Количество запусков, для которых была запрошена отмена, в этой рабочей области. Счётчик обновляется, когда получен запрос на отмену запуска.",
    "Number of total cores.": "Общее количество ядер.",
    "Number of total nodes. This total includes some of Active Nodes, Idle Nodes, Unusable Nodes, Preempted Nodes, Leaving Nodes.": "Общее количество узлов. В это число входят активные узлы, простаивающие узлы, непригодные узлы, вытесненные узлы и высвобождаемые узлы.",
    "Number of unusable cores.": "Количество непригодных ядер.",
    "Number of unusable nodes. Unusable nodes are not functional due to some unresolvable issue. Azure will recycle these nodes.": "Количество непригодных узлов. Непригодные узлы не функционируют из-за неустранимой проблемы. Azure утилизирует такие узлы.",
    "P99 Replication Latency across source and target regions for geo-enabled account": "Задержка репликации P99 между исходным и целевым регионами для учётной записи с поддержкой геораспределения",
    "Percent of quota utilized.": "Процент использованной квоты.",
    "Percentage of memory utilization on a CPU node. Utilization is reported at one minute intervals.": "Процент использования памяти на узле ЦП. Загрузка регистрируется с интервалом в одну минуту.",
    "Percentage of memory utilization on a GPU node. Utilization is reported at one-minute intervals.": "Процент использования памяти на узле GPU. Загрузка регистрируется с интервалом в одну минуту.",
    "Physical Partition Size in bytes": "Размер физического раздела в байтах",
    "Physical Partition Throughput": "Пропускная способность физического раздела",
    "Progress of jobs": "Прогресс выполнения заданий",
    "Provisioned Throughput": "Подготовленная пропускная способность",
    "Queries for the workload group that have timed out.": "Запросы для группы рабочей нагрузки, время ожидания которых истекло.",
    "RUs consumed for Cassandra requests made": "Потреблено RU для выполненных запросов Cassandra",
    "Region Added": "Добавление региона",
    "Region Failed Over": "Переключение региона при отказе",
    "Region Offlined": "Перевод региона в автономный режим",
    "Region Onlined": "Перевод региона в оперативный режим",
    "Region Removed": "Удаление региона",
    "Request Units consumed for Gremlin requests made": "Потреблено единиц запросов для выполненных запросов Gremlin",
    "Request Units consumed with CapacityType": "Потреблено единиц запросов с учётом CapacityType",
    "Requests at the dedicated gateway": "Запросы к выделенному шлюзу",
    "SQL Request Units consumed": "Потреблено единиц запросов SQL",
    "Sanity check, indicating how the cluster responds to queries": "Проверка работоспособности, показывающая, как кластер отвечает на запросы",
    "Server Side Latency": "Задержка на стороне сервера",
    "Server Side Latency in Direct Connection Mode": "Задержка на стороне сервера в режиме прямого подключения",
    "Server Side Latency in Gateway Connection Mode": "Задержка на стороне сервера в режиме подключения через шлюз",
    "Sessions percentage": "Процент сессий",
    "Sessions percentage. Not applicable to data warehouses.": "Процент сессий. Неприменимо к хранилищам данных.",
    "Size of the entries evicted from the integrated cache": "Размер записей, вытесненных из интегрированного кэша",
    "Space used in tempdb data files in kilobytes.": "Объём, используемый в файлах данных tempdb, в килобайтах.",
    "Space used in tempdb data files in kilobytes. Not applicable to data warehouses.": "Объём, используемый в файлах данных tempdb, в килобайтах. Неприменимо к хранилищам данных.",
    "Space used in tempdb transaction log file in kilobytes.": "Объём, используемый в файле журнала транзакций tempdb, в килобайтах.",
    "Space used in tempdb transaction log file in kilobytes. Not applicable to data warehouses.": "Объём, используемый в файле журнала транзакций tempdb, в килобайтах. Неприменимо к хранилищам данных.",
    "Space used percentage in tempdb transaction log file": "Процент используемого объёма в файле журнала транзакций tempdb",
    "Space used percentage in tempdb transaction log file. Not applicable to data warehouses.": "Процент используемого объёма в файле журнала транзакций tempdb. Неприменимо к хранилищам данных.",
    "Sql Container Created": "Создание контейнера SQL",
    "Sql Container Deleted": "Удаление контейнера SQL",
    "Sql Container Throughput Updated": "Обновление пропускной способности контейнера SQL",
    "Sql Container Updated": "Обновление контейнера SQL",
    "Sql Database Created": "Создание базы данных SQL",
    "Sql Database Deleted": "Удаление базы данных SQL",
    "Sql Database Throughput Updated": "Обновление пропускной способности базы данных SQL",
    "Sql Database Updated": "Обновление базы данных SQL",
    "Succeeded pipeline runs metrics": "Метрики успешных запусков конвейеров",
    "Successful Connections": "Успешные подключения",
    "The CPU utilization level": "Уровень загрузки ЦП",
    "The Data Warehouse Unit, which is the service-level objective of the data warehouse.": "Единица хранилища данных (DWU), которая является целевым уровнем обслуживания хранилища данных.",
    "The active queries within the workload group": "Активные запросы в пределах группы рабочей нагрузки",
    "The active queries within the workload group. Using this metric unfiltered and unsplit displays all active queries running on the system.": "Активные запросы в пределах группы рабочей нагрузки. Использование этой метрики без фильтрации и разбиения отображает все активные запросы, выполняемые в системе.",
    "The amount of data processed by queries": "Объём данных, обработанных запросами",
    "The cumulative number of requests queued after the max concurrency limit was reached": "Накопительное количество запросов, поставленных в очередь после достижения максимального предела параллелизма",
    "The duration of the aggregation phase in the ingestion flow": "Длительность фазы агрегации в потоке приёма данных",
    "The effective cap resource percent for the workload group": "Эффективный предельный процент ресурсов для группы рабочей нагрузки",
    "The effective cap resource percent for the workload group. If there are other workload groups with the effective min resource percent higher than `0`, the effective cap resource percent is lowered proportionally.": "Эффективный предельный процент ресурсов для группы рабочей нагрузки. Если есть другие группы рабочей нагрузки с эффективным минимальным процентом ресурсов выше `0`, эффективный предельный процент ресурсов пропорционально снижается.",
    "The effective minimum resource percentage setting allowed, considering the service level and the workload group settings": "Допустимая эффективная настройка минимального процента ресурсов с учётом уровня обслуживания и настроек группы рабочей нагрузки",
    "The effective minimum resource percentage setting allowed, considering the service level and the workload group settings.": "Допустимая эффективная настройка минимального процента ресурсов с учётом уровня обслуживания и настроек группы рабочей нагрузки.",
    "The export utilization": "Утилизация экспорта",
    "The ingestion time from the source (for example, if message is in EventHub) to the cluster in seconds": "Время приёма данных от источника (например, если сообщение находится в EventHub) до кластера, в секундах",
    "The lateness (in minutes) reported by the continuous export jobs in the cluster": "Запаздывание (в минутах), регистрируемое заданиями непрерывного экспорта в кластере",
    "The local tempdb utilization across all compute nodes. Values are emitted every five minutes.": "Утилизация локального tempdb по всем вычислительным узлам. Значения публикуются каждые пять минут.",
    "The maximum value when compared between CPU percentage and Data IO percentage.": "Максимальное значение при сравнении процента использования ЦП и процента ввода-вывода данных.",
    "The memory utilization across all nodes in the SQL pool": "Использование памяти по всем узлам в пуле SQL",
    "The number of batches aggregated for ingestion": "Количество пакетов, агрегированных для приёма данных",
    "The number of connections blocked by firewall rules": "Количество подключений, заблокированных правилами брандмауэра",
    "The number of data sources in an aggregated batch for ingestion": "Количество источников данных в агрегированном пакете для приёма данных",
    "The number of events processed by the cluster when ingesting from Event/IoT Hub": "Количество событий, обработанных кластером при приёме данных из Event/IoT Hub",
    "The number of failed connections to the data warehouse from the database application.": "Количество неудачных подключений к хранилищу данных от приложения базы данных.",
    "The number of ingestion operations": "Количество операций приёма данных",
    "The number of login attempts that succeeded or failed": "Количество попыток входа, завершившихся успешно или с ошибкой",
    "The number of logins to the data warehouse from the database application that the firewall blocks.": "Количество заблокированных брандмауэром входов в хранилище данных от приложения базы данных.",
    "The number of orchestration activities that succeeded, failed, or were cancelled": "Количество действий оркестрации, которые завершились успешно, с ошибкой или были отменены",
    "The number of orchestration pipeline runs that succeeded, failed, or were cancelled": "Количество запусков конвейеров оркестрации, которые завершились успешно, с ошибкой или были отменены",
    "The number of orchestration triggers that succeeded, failed, or were cancelled": "Количество триггеров оркестрации, которые сработали успешно, с ошибкой или были отменены",
    "The number of pending continuous export jobs ready for execution": "Количество ожидающих заданий непрерывного экспорта, готовых к выполнению",
    "The number of queries that succeeded, failed, or were cancelled": "Количество запросов, которые завершились успешно, с ошибкой или были отменены",
    "The number of records exported, fired for every storage artifact written during the export operation": "Количество экспортированных записей, регистрируется для каждого артефакта хранилища, записанного во время операции экспорта",
    "The number of successful connections to the data from the database application.": "Количество успешных подключений к данным от приложения базы данных.",
    "The number of total logins to the SQL pool": "Общее количество входов в пул SQL",
    "The overall volume of ingested data to the cluster (in MB)": "Общий объём данных, принятых в кластер (в МБ)",
    "The percentage allocation of resources relative to the effective cap resource percent per workload group": "Процентное распределение ресурсов относительно эффективного предельного процента ресурсов для каждой группы рабочей нагрузки",
    "The percentage allocation of resources relative to the entire system": "Процентное распределение ресурсов относительно всей системы",
    "The percentage allocation of resources relative to the entire system.": "Процентное распределение ресурсов относительно всей системы.",
    "The percentage of CPU that all nodes utilize for the data warehouse.": "Процент ЦП, используемый всеми узлами для хранилища данных.",
    "The percentage of IO that all nodes utilize for the data warehouse.": "Процент ввода-вывода, используемый всеми узлами для хранилища данных.",
    "The percentage of memory of the SQL Server utilized across all nodes for the data warehouse.": "Процент памяти SQL Server, используемый по всем узлам для хранилища данных.",
    "The percentage of the local tempdb that all compute nodes utilize.": "Процент локального tempdb, используемый всеми вычислительными узлами.",
    "The queries duration in seconds": "Длительность запросов в секундах",
    "The queries for the workload group that have timed out": "Запросы для группы рабочей нагрузки, время ожидания которых истекло",
    "The ratio of used ingestion slots in the cluster": "Доля использованных слотов приёма данных в кластере",
    "The service-level objective of the SQL pool": "Целевой уровень обслуживания пула SQL",
    "The streaming ingest data rate (MB per second)": "Скорость потокового приёма данных (МБ в секунду)",
    "The streaming ingest duration in milliseconds": "Длительность потокового приёма данных в миллисекундах",
    "The streaming ingest request rate (requests per second)": "Частота запросов потокового приёма данных (запросов в секунду)",
    "The streaming ingest result": "Результат потокового приёма данных",
    "The sum of all bytes in the local SSD cache across all nodes.": "Сумма всех байтов в локальном SSD-кэше по всем узлам.",
    "The sum of all columnstore segments hits in the local SSD cache.": "Сумма всех попаданий сегментов columnstore в локальный SSD-кэш.",
    "The total instance count": "Общее количество экземпляров",
    "The total number of SSIS IR starts that failed within a minute window": "Общее количество запусков SSIS IR, завершившихся с ошибкой за минутный интервал",
    "The total number of SSIS IR starts that succeeded within a minute window": "Общее количество запусков SSIS IR, завершившихся успешно за минутный интервал",
    "The total number of SSIS IR starts that were cancelled within a minute window": "Общее количество запусков SSIS IR, отменённых за минутный интервал",
    "The total number of SSIS IR stops that succeeded within a minute window": "Общее количество остановок SSIS IR, завершившихся успешно за минутный интервал",
    "The total number of SSIS IR stops that were stuck within a minute window": "Общее количество остановок SSIS IR, зависших за минутный интервал",
    "The total number of SSIS package executions that failed within a minute window": "Общее количество выполнений пакетов SSIS, завершившихся с ошибкой за минутный интервал",
    "The total number of SSIS package executions that succeeded within a minute window": "Общее количество выполнений пакетов SSIS, завершившихся успешно за минутный интервал",
    "The total number of SSIS package executions that were cancelled within a minute window": "Общее количество выполнений пакетов SSIS, отменённых за минутный интервал",
    "The total number of activity runs that failed within a minute window": "Общее количество запусков действий, завершившихся с ошибкой за минутный интервал",
    "The total number of activity runs that succeeded within a minute window": "Общее количество запусков действий, завершившихся успешно за минутный интервал",
    "The total number of activity runs that were cancelled within a minute window": "Общее количество запусков действий, отменённых за минутный интервал",
    "The total number of concurrent queries": "Общее количество параллельных запросов",
    "The total number of data extents": "Общее количество экстентов данных",
    "The total number of runs that failed within a minute window": "Общее количество запусков, завершившихся с ошибкой за минутный интервал",
    "The total number of runs that succeeded within a minute window": "Общее количество запусков, завершившихся успешно за минутный интервал",
    "The total number of throttled commands": "Общее количество команд, подвергнутых регулированию",
    "The total number of throttled queries": "Общее количество запросов, подвергнутых регулированию",
    "The total number of trigger runs that failed within a minute window": "Общее количество запусков триггеров, завершившихся с ошибкой за минутный интервал",
    "The total number of trigger runs that succeeded within a minute window": "Общее количество запусков триггеров, завершившихся успешно за минутный интервал",
    "The total number of trigger runs that were cancelled within a minute window": "Общее количество запусков триггеров, отменённых за минутный интервал",
    "The uncompressed, expected data size in an aggregated batch for ingestion": "Несжатый ожидаемый размер данных в агрегированном пакете для приёма данных",
    "The usage across the SQL pool, measured by DWU limit \\* DWU percentage.": "Использование по пулу SQL, измеряемое как лимит DWU \\* процент DWU.",
    "The usage across the SQL pool, measured by taking the maximum between CPU percentage and Data IO percentage": "Использование по пулу SQL, измеряемое как максимум из процента использования ЦП и процента ввода-вывода данных",
    "The utilization level in the cluster scope": "Уровень утилизации в области кластера",
    "Total AU time for cancelled jobs": "Общее время AU для отменённых заданий",
    "Total AU time for failed jobs": "Общее время AU для заданий с ошибкой",
    "Total AU time for successful jobs": "Общее время AU для успешных заданий",
    "Total data usage reported at 5 minutes granularity": "Общее использование данных, регистрируется с детализацией в 5 минут",
    "Total document count reported at 5 minutes, 1 hour and 1 day granularity": "Общее количество документов, регистрируется с детализацией в 5 минут, 1 час и 1 день",
    "Total entities count": "Общее количество сущностей",
    "Total factory size (GB unit)": "Общий размер фабрики (в ГБ)",
    "Total index usage reported at 5 minutes granularity": "Общее использование индекса, регистрируется с детализацией в 5 минут",
    "Total storage quota reported at 5 minutes granularity": "Общая квота хранилища, регистрируется с детализацией в 5 минут",
    "V cores allocated": "Выделено виртуальных ядер",
    "Workers percentage": "Процент рабочих процессов",
    "Workers percentage. Not applicable to data warehouses.": "Процент рабочих процессов. Неприменимо к хранилищам данных.",
    "eDTU limit. Applies to DTU-based elastic pools.": "Лимит eDTU. Применимо к эластичным пулам на основе DTU.",
    "eDTU used. Applies to DTU-based elastic pools.": "Использовано eDTU. Применимо к эластичным пулам на основе DTU.",
}

warnings = []


def is_sep(cells):
    return all(set(c) <= set("-: ") for c in cells)


def tr_table_line(line, colmap, fname):
    """Translate one table body row given the table's column map."""
    if line in WHOLE_LINE:
        return WHOLE_LINE[line]
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    out = []
    for i, cell in enumerate(cells):
        col = colmap[i] if i < len(colmap) else None
        if col == "Description":
            if cell and cell not in DESC_MAP:
                warnings.append("%s: untranslated DESC -> %r" % (fname, cell))
            out.append(DESC_MAP.get(cell, cell))
        elif col == "Unit":
            if cell not in UNIT_MAP:
                warnings.append("%s: unmapped UNIT -> %r" % (fname, cell))
            out.append(UNIT_MAP.get(cell, cell))
        elif col and col.startswith("Recommended"):
            if cell not in REC_MAP:
                warnings.append("%s: unmapped REC -> %r" % (fname, cell))
            out.append(REC_MAP.get(cell, cell))
        else:  # Name, Dimensions, unknown -> keep EN
            out.append(cell)
    return "| " + " | ".join(out) + " |"


def tr_header(line):
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    out = [HEADER_LABEL.get(c, c) for c in cells]
    return "| " + " | ".join(out) + " |", cells


def build_one(fname):
    en = open(os.path.join(EN_DIR, fname), encoding="utf-8").read()
    en_title, ru_title = TITLE_MAP[fname]
    out_lines = []
    colmap = None
    for line in en.split("\n"):
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if is_sep(cells):
                out_lines.append(line)
            elif cells and cells[0] == "Name":
                tline, colmap = tr_header(line)
                out_lines.append(tline)
            elif colmap is not None:
                out_lines.append(tr_table_line(line, colmap, fname))
            else:
                out_lines.append(line)  # stray table line w/o header
        else:
            colmap = None
            s = line
            if en_title != ru_title:
                s = s.replace(en_title, ru_title)
            for k, v in DATE_MAP.items():
                s = s.replace(k, v)
            for k, v in PROSE:
                s = s.replace(k, v)
            out_lines.append(s)
    result = "\n".join(out_lines)
    out_path = os.path.join(RU_DIR, fname)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    open(out_path, "w", encoding="utf-8", newline="").write(result)
    return en, result


def main():
    ok = 0
    for fname in BATCH:
        en, ru = build_one(fname)
        en_n, ru_n = en.count("\n"), ru.count("\n")
        status = "OK" if en_n == ru_n else "LINE MISMATCH %d!=%d" % (en_n, ru_n)
        if en_n == ru_n:
            ok += 1
        print("%-22s  %s  (%d lines)" % (status, fname, ru_n + 1))
    print("\nline-parity OK: %d/%d" % (ok, len(BATCH)))
    if warnings:
        print("\n=== WARNINGS (%d) ===" % len(warnings))
        for w in warnings:
            print("  ", w)
    else:
        print("no warnings")


if __name__ == "__main__":
    main()
