#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""L4-IF.40 — RU build for 14 Azure metric files: DB family (6) + Containers (4) + Storage/Data (4).

Reuses the column-aware engine from L4-IF.37 via the L4-IF.38 wrapper
(_build_azure_metrics_l4if38.py): base DESC_MAP/UNIT_MAP/PROSE/HEADER_LABEL win
for any shared EN string; this batch adds its own strings on top.

New vs L4-IF.38:
  * EXACT_LINE layer — full-line overrides applied BEFORE substring replaces
    (file-specific intros, deprecation notices, management-zone how-to,
    storage-account-classic per-service paragraphs). Removes the partial-match
    risk of pure replace-chains (hyperscale prereq line shares a substring with
    the L4-IF.37 data-warehouse key but differs in the first sentence).
  * Post-build leftover-EN scan with an explicit PASS_EN whitelist
    (image captions, bold product labels, management-zone rule-condition
    bullets — deliberately EN per UI-strings canon).

Canon: Description/Unit/Recommended + header labels translated; Name +
Dimensions stay EN (Azure Metrics API identifiers). Image alt + caption lines
stay EN byte-identical (shipped canon, see monitor-azure-sql-database-dtu).
Com_* counter echo descriptions (Com alter table, ...) stay EN: nothing
translatable (counter prefix + SQL statement tokens). No em-dash (CLAUDE.md §0).
"""

import os
import importlib.util

_spec = importlib.util.spec_from_file_location(
    "e38", os.path.join(os.path.dirname(__file__), "_build_azure_metrics_l4if38.py")
)
e38 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(e38)

EN_DIR = "docs/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics"
RU_DIR = "docs/managed-ru/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics"

BATCH = [
    "monitor-azure-db-mariadb.md",
    "monitor-azure-db-mysql.md",
    "monitor-azure-db-mysql-flexible-servers.md",
    "monitor-azure-db-postgresql.md",
    "monitor-azure-sql-database-hyperscale.md",
    "monitor-azure-sql-managed-instance.md",
    "monitor-azure-container-app.md",
    "monitor-azure-container-apps-environment.md",
    "monitor-azure-container-instances.md",
    "monitor-azure-container-registry.md",
    "monitor-azure-data-lake-storage-gen1.md",
    "monitor-azure-data-share.md",
    "monitor-azure-storage-account-classic.md",
    "monitor-azure-storage-sync.md",
]

TITLE_MAP = {
    "monitor-azure-db-mariadb.md": (
        "Azure Database for MariaDB monitoring",
        "Мониторинг Azure Database for MariaDB",
    ),
    "monitor-azure-db-mysql.md": (
        "Azure Database for MySQL monitoring",
        "Мониторинг Azure Database for MySQL",
    ),
    "monitor-azure-db-mysql-flexible-servers.md": (
        "Azure Database for MySQL Flexible Servers monitoring",
        "Мониторинг Azure Database for MySQL Flexible Servers",
    ),
    "monitor-azure-db-postgresql.md": (
        "Azure Database for PostgreSQL (Single Server, Hyperscale, Flexible Server) monitoring",
        "Мониторинг Azure Database for PostgreSQL (Single Server, Hyperscale, Flexible Server)",
    ),
    "monitor-azure-sql-database-hyperscale.md": (
        "Azure SQL Database Hyperscale monitoring",
        "Мониторинг Azure SQL Database Hyperscale",
    ),
    "monitor-azure-sql-managed-instance.md": (
        "Azure SQL Managed Instance monitoring",
        "Мониторинг Azure SQL Managed Instance",
    ),
    "monitor-azure-container-app.md": (
        "Azure Container App monitoring",
        "Мониторинг Azure Container App",
    ),
    "monitor-azure-container-apps-environment.md": (
        "Azure Container Apps Environment monitoring",
        "Мониторинг Azure Container Apps Environment",
    ),
    "monitor-azure-container-instances.md": (
        "Monitor Azure Container Instances",
        "Мониторинг Azure Container Instances",
    ),
    "monitor-azure-container-registry.md": (
        "Azure Container Registry monitoring",
        "Мониторинг Azure Container Registry",
    ),
    "monitor-azure-data-lake-storage-gen1.md": (
        "Azure Data Lake Storage Gen1 monitoring",
        "Мониторинг Azure Data Lake Storage Gen1",
    ),
    "monitor-azure-data-share.md": (
        "Azure Data Share monitoring",
        "Мониторинг Azure Data Share",
    ),
    "monitor-azure-storage-account-classic.md": (
        "Azure Storage Account Classic (Blob, File, Queue, Table) monitoring",
        "Мониторинг Azure Storage Account Classic (Blob, File, Queue, Table)",
    ),
    "monitor-azure-storage-sync.md": (
        "Azure Storage Sync monitoring",
        "Мониторинг Azure Storage Sync",
    ),
}

DATE_MAP = dict(e38.DATE_MAP)
DATE_MAP.update(
    {
        # canon L4-IF.35: dates with trailing "г."; overrides the e37 entry without it
        "* Updated on Nov 15, 2023": "* Обновлено 15 ноября 2023 г.",
        "* Published Jul 02, 2020": "* Опубликовано 2 июля 2020 г.",
        "* Published Apr 13, 2021": "* Опубликовано 13 апреля 2021 г.",
        "* Published Aug 31, 2023": "* Опубликовано 31 августа 2023 г.",
        "* Published Aug 27, 2024": "* Опубликовано 27 августа 2024 г.",
    }
)

PROSE = list(e38.PROSE) + [
    ("* 6-min read", "* Чтение: 6 мин"),
    ("* 11-min read", "* Чтение: 11 мин"),
]

# ---- full-line overrides (applied first, before any substring replace) ----
MGMT_ZONE_LINK = (
    "[настроить зону управления](/managed/manage/identity-access-management/permission-management/"
    'management-zones/set-up-management-zones "Создание зон управления и назначение прав доступа к ним.")'
)
TIMEFRAME_LINK = (
    "[Временной диапазон и зона управления дашборда](/managed/analyze-explore-automate/dashboards-classic/"
    'dashboards/dashboard-timeframe "Узнайте о параметрах временного диапазона и зоны управления дашборда Dynatrace.")'
)
ONEAGENT_DB_LINE = (
    "Optionally, for OneAgent integration, see [how database activity is monitored]"
    "(/managed/observe/infrastructure-observability/databases/database-services-classic/"
    'how-database-activity-is-monitored "Learn about automatic detection and monitoring '
    'of database services in your application environment.").',
    "При желании для интеграции OneAgent см. [как отслеживается активность баз данных]"
    "(/managed/observe/infrastructure-observability/databases/database-services-classic/"
    'how-database-activity-is-monitored "Узнайте об автоматическом обнаружении и мониторинге '
    'сервисов баз данных в среде вашего приложения.").',
)


def _import_dash(svc):
    return (
        "To import a dashboard for %s, you need to [set up a management zone]"
        "(/managed/manage/identity-access-management/permission-management/management-zones/"
        'set-up-management-zones "Create and assign access rights to management zones.") '
        "to limit the entities displayed on the dashboard to those relevant to this service."
        % svc,
        "Чтобы импортировать дашборд для %s, необходимо %s, которая ограничит сущности, "
        "отображаемые на дашборде, теми, которые относятся к этому сервису."
        % (svc, MGMT_ZONE_LINK),
    )


def _add_condition(token):
    return (
        "2. Add a condition for the database name to contain the `%s` string (case sensitive.)"
        % token,
        "2. Добавьте условие, чтобы имя базы данных содержало строку `%s` (с учётом регистра)."
        % token,
    )


AFTER_CREATE_SELECT = (
    "After you create the management zone, select it from your dashboard "
    "(**Edit** > **Settings** > **Default management zone**). For more information, "
    "see [Dashboard timeframe and management zone](/managed/analyze-explore-automate/"
    'dashboards-classic/dashboards/dashboard-timeframe "Learn about Dynatrace dashboard '
    'timeframe and management zone settings.").',
    "После создания зоны управления выберите её на вашем дашборде "
    "(**Edit** > **Settings** > **Default management zone**). Дополнительную информацию "
    "см. в разделе %s." % TIMEFRAME_LINK,
)
AFTER_CREATE_ASSIGN = (
    "After you create the management zone, assign it to your dashboard (from the dashboard, "
    "select **Edit** > **Settings** > **Default management zone**). For more information, "
    "see [Dashboard timeframe and management zone](/managed/analyze-explore-automate/"
    'dashboards-classic/dashboards/dashboard-timeframe "Learn about Dynatrace dashboard '
    'timeframe and management zone settings.").',
    "После создания зоны управления назначьте её вашему дашборду (на дашборде выберите "
    "**Edit** > **Settings** > **Default management zone**). Дополнительную информацию "
    "см. в разделе %s." % TIMEFRAME_LINK,
)

STORAGE_CLASSIC_PARA_RU = (
    "Этот сервис отслеживает часть Storage Account Classic (Microsoft.ClassicStorage/storageAccounts). "
    "Уже отслеживаемые ресурсы можно найти на странице обзора Azure в разделе `Cloud services` или "
    "использовать предустановленный дашборд. Для мониторинга ресурсов типа Microsoft.Storage/storageAccounts "
    "(включая Storage, StorageV2 и BlobStorage) проверьте Storage Accounts и раздел `Storage accounts` "
    "на странице обзора Azure."
)

EXACT_LINE = dict(
    [
        # shared management-zone block
        (
            "When you create a management zone for this dashboard:",
            "При создании зоны управления для этого дашборда:",
        ),
        (
            "1. Create a rule that identifies services based on a common property:",
            "1. Создайте правило, которое идентифицирует сервисы на основе общего свойства:",
        ),
        ("Example", "Пример"),
        ("### Set up a management zone", "### Настройка зоны управления"),
        (
            "You can see whether a dashboard requires a management zone in the rules setup.",
            "Увидеть, требуется ли для дашборда зона управления, можно в настройке правил.",
        ),
        ONEAGENT_DB_LINE,
        _import_dash("Azure Database for MariaDB"),
        _import_dash("Azure Database for MySQL"),
        _import_dash("Azure Database for PostgreSQL"),
        _add_condition("mariadb"),
        _add_condition("mysql"),
        _add_condition("postgres"),
        AFTER_CREATE_SELECT,
        AFTER_CREATE_ASSIGN,
        # db-mariadb intro
        (
            "On the Azure Database for MariaDB overview page you can see if you’re running out of "
            "CPU or facing a high I/O percentage, so you always know which queries need to be optimized.",
            "На странице обзора Azure Database for MariaDB можно увидеть, не заканчиваются ли ресурсы ЦП "
            "и не наблюдается ли высокий процент ввода-вывода, поэтому вы всегда знаете, какие запросы "
            "необходимо оптимизировать.",
        ),
        # db-mysql deprecation
        ("Deprecation notice", "Уведомление об устаревании"),
        (
            "On 16 September 2024, Azure Database for MySQL will be retired. Azure introduced a new service, "
            "see [Azure Database for MySQL Flexible Servers monitoring](/managed/ingest-from/"
            "microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/"
            'monitor-azure-db-mysql-flexible-servers "Monitor Azure DB for Database for MySQL Flexible '
            'Servers and view available metrics.").',
            "16 сентября 2024 г. сервис Azure Database for MySQL будет выведен из эксплуатации. "
            "Azure представил новый сервис, см. [Мониторинг Azure Database for MySQL Flexible Servers]"
            "(/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/"
            'monitor-azure-db-mysql-flexible-servers "Мониторинг Azure DB for Database for MySQL Flexible '
            'Servers и просмотр доступных метрик.").',
        ),
        (
            "The Azure Database for MySQL overview page serves as a comprehensive overview of your MySQL "
            "servers and database instances. From here you can gain full visibility and check if your "
            "database is healthy, under-performing, or if there are any failed connections.",
            "Страница обзора Azure Database for MySQL служит комплексным обзором ваших серверов MySQL и "
            "экземпляров баз данных. Здесь вы можете получить полную видимость и проверить, работоспособна "
            "ли ваша база данных, снижена ли её производительность и есть ли неудачные подключения.",
        ),
        # db-mysql-flexible-servers
        (
            "From 16 September 2024, Azure Database for MySQL Flexible Servers replaces "
            "[Azure Database for MySQL Single Server](/managed/ingest-from/microsoft-azure-services/"
            'azure-integrations/azure-cloud-services-metrics/monitor-azure-db-mysql "Monitor Azure DB '
            'for MySQL and view available metrics.").',
            "С 16 сентября 2024 г. Azure Database for MySQL Flexible Servers заменяет "
            "[Azure Database for MySQL Single Server](/managed/ingest-from/microsoft-azure-services/"
            'azure-integrations/azure-cloud-services-metrics/monitor-azure-db-mysql "Мониторинг Azure DB '
            'for MySQL и просмотр доступных метрик.").',
        ),
        (
            "The Azure Database for MySQL Flexible Servers overview page serves as a comprehensive overview "
            "of your MySQL servers and database instances. From here you can gain full visibility and check "
            "if your database is healthy, under-performing, or if there are any failed connections.",
            "Страница обзора Azure Database for MySQL Flexible Servers служит комплексным обзором ваших "
            "серверов MySQL и экземпляров баз данных. Здесь вы можете получить полную видимость и проверить, "
            "работоспособна ли ваша база данных, снижена ли её производительность и есть ли неудачные "
            "подключения.",
        ),
        # db-postgresql intro
        (
            "On the Azure Database for PostgreSQL (Single Server, Hyperscale, Flexible Server) overview "
            "pages you get insights into various aspects of database performance, including CPU and memory "
            "usage, active connections, storage space, and much more.",
            "На страницах обзора Azure Database for PostgreSQL (Single Server, Hyperscale, Flexible Server) "
            "вы получаете представление о различных аспектах производительности базы данных, включая "
            "использование ЦП и памяти, активные подключения, пространство хранилища и многое другое.",
        ),
        # sql-database-hyperscale prereq note (first sentence differs from L4-IF.37 data-warehouse key)
        (
            "This service monitors the hyperscale type of SQL Databases. You can find the already monitored "
            "resources on the Azure overview page in the **Cloud services** section or use a dashboard "
            "preset. To monitor the SQL Databases user kind, check Azure SQL Servers and the "
            "**Databases components** sections on the Azure overview page.",
            "Этот сервис отслеживает тип SQL-баз данных Hyperscale. Уже отслеживаемые ресурсы можно найти "
            "на странице обзора Azure в разделе **Cloud services** или использовать предустановленный "
            "дашборд. Для мониторинга пользовательского типа SQL-баз данных проверьте Azure SQL Servers и "
            "разделы **Databases components** на странице обзора Azure.",
        ),
        # sql-managed-instance intro
        (
            "On the Azure SQL Managed Instance overview page you get insights into various aspects of "
            "database performance, including CPU usage, virtual core count, storage space, IO bytes "
            "sent/received, and much more.",
            "На странице обзора Azure SQL Managed Instance вы получаете представление о различных аспектах "
            "производительности базы данных, включая использование ЦП, количество виртуальных ядер, "
            "пространство хранилища, отправленные/полученные байты ввода-вывода и многое другое.",
        ),
        # storage-account-classic top notes
        (
            "This service monitors a part of Storage Account Classic (`Microsoft.ClassicStorage/storageAccounts`). "
            "You can find the already monitored resources on the Azure overview page in the **Cloud services** "
            "section or use a dashboard preset.",
            "Этот сервис отслеживает часть Storage Account Classic (`Microsoft.ClassicStorage/storageAccounts`). "
            "Уже отслеживаемые ресурсы можно найти на странице обзора Azure в разделе **Cloud services** или "
            "использовать предустановленный дашборд.",
        ),
        (
            "To monitor resources of the `Microsoft.Storage/storageAccounts` (including Storage, StorageV2 "
            "and BlobStorage) type, check Storage Accounts and the **Storage accounts** section on the "
            "Azure overview page.",
            "Для мониторинга ресурсов типа `Microsoft.Storage/storageAccounts` (включая Storage, StorageV2 "
            "и BlobStorage) проверьте Storage Accounts и раздел **Storage accounts** на странице обзора Azure.",
        ),
        # storage-account-classic per-service paragraphs (3 EN variants, same meaning -> same RU)
        (
            "This service monitors a part of Storage Account Classic (Microsoft.ClassicStorage/storageAccounts). "
            "You can find the already monitored resources on the Azure overview page in the `Cloud services` "
            "section or use a dashboard preset. To monitor resources of the Microsoft.Storage/storageAccounts "
            "type (including Storage, StorageV2 and BlobStorage), check Storage Accounts and the "
            "`Storage accounts` section on the Azure overview page.",
            STORAGE_CLASSIC_PARA_RU,
        ),
        (
            "This service monitors a part of Storage Account Classic (Microsoft.ClassicStorage/storageAccounts). "
            "You can find the already monitored resources in Azure overview page in `Cloud services` section "
            "or use a dashboard preset. To monitor resources of the Microsoft.Storage/storageAccounts type "
            "(including Storage, StorageV2 and BlobStorage), check Storage Accounts and the `Storage accounts` "
            "section on the Azure overview page.",
            STORAGE_CLASSIC_PARA_RU,
        ),
        (
            "This service monitors a part of Storage Account Classic (Microsoft.ClassicStorage/storageAccounts). "
            "You can find the already monitored resources in Azure overview page in `Cloud services` section "
            "or use a dashboard preset. To monitor resources of type Microsoft.Storage/storageAccounts "
            "(including Storage, StorageV2 and BlobStorage), check Storage Accounts and Azure overview "
            "section `Storage accounts`.",
            STORAGE_CLASSIC_PARA_RU,
        ),
    ]
)

# ---- deliberately-EN pass-through lines (whitelist for the leftover scan) ----
PASS_EN = {
    # postgresql sub-table H3 headings: pure product names (EN canon + anchor fidelity, L4-IF.33)
    "### Azure Database for PostgreSQL (Single Server)",
    "### Azure Database for PostgreSQL Hyperscale",
    "### Azure Database for PostgreSQL - Flexible Server",
    # image captions (shipped canon: stay EN byte-identical)
    "Clone hide azure",
    "Mariadb dash",
    "Mysql dash",
    "Postgres dash",
    "Hyper",
    "Hyperscale",
    "SQL dash",
    "Cont inst",
    "Container reg",
    "Datalake stor",
    "Data share",
    "Storage Account Classic",
    "Stor sync",
    "Azure management zone",
    # bold sub-service labels (product names)
    "**Storage Account (Classic)**",
    "**Azure Storage Blob Services (Classic)**",
    "**Azure Storage File Services (Classic)**",
    "**Azure Storage Queue Services (Classic)**",
    "**Azure Storage Table Services (Classic)**",
    # management-zone rule conditions (UI field names + UI values)
    "* Service type: `Database`",
    "* Technology: `MariaDB`",
    "* Service topology: `Opaque service`",
    "* Service type equals `Database`",
    "* Service topology equals `Opaque service`",
}

HEADER_LABEL = dict(e38.HEADER_LABEL)
REC_MAP = dict(e38.REC_MAP)
UNIT_MAP = dict(e38.UNIT_MAP)

# ---- batch Description cells (EN exact -> RU); base maps win for shared strings ----
NEW_DESC = {
    # --- db-mariadb / db-mysql (short name-echo descriptions) ---
    "Active connections": "Активные подключения",
    "Backup storage used": "Использованное хранилище резервных копий",
    "CPU percent": "Процент использования ЦП",
    "Failed connections": "Неудачные подключения",
    "IO percent": "Процент ввода-вывода",
    "Memory percent": "Процент использования памяти",
    "Network In across active connections": "Входящий сетевой трафик по активным подключениям",
    "Network Out across active connections": "Исходящий сетевой трафик по активным подключениям",
    "Replication lag in seconds": "Задержка репликации в секундах",
    "Server log storage limit": "Лимит хранилища журналов сервера",
    "Server log storage percent": "Процент использования хранилища журналов сервера",
    "Server log storage used": "Использованное хранилище журналов сервера",
    "Storage limit": "Лимит хранилища",
    "Storage percent": "Процент использования хранилища",
    "Storage used": "Использованное хранилище",
    # --- db-mysql-flexible-servers ---
    "Aborted connections": "Прерванные подключения",
    "Active transactions": "Активные транзакции",
    "Binlog storage used": "Использованное хранилище binlog",
    "CPU credits consumed": "Израсходованные кредиты ЦП",
    "CPU credits remaining": "Оставшиеся кредиты ЦП",
    # Com_* MySQL counter echoes: counter prefix + SQL statement tokens, nothing translatable
    "Com alter table": "Com alter table",
    "Com create DB": "Com create DB",
    "Com create table": "Com create table",
    "Com delete": "Com delete",
    "Com drop DB": "Com drop DB",
    "Com drop table": "Com drop table",
    "Com insert": "Com insert",
    "Com select": "Com select",
    "Com update": "Com update",
    "Data storage used": "Использованное хранилище данных",
    "Ha IO status": "Статус ввода-вывода Ha",
    "Ha SQL status": "Статус SQL Ha",
    "Ha replication lag": "Задержка репликации Ha",
    "Host CPU percent": "Процент использования ЦП хоста",
    "Host network in": "Входящий сетевой трафик хоста",
    "Host network out": "Исходящий сетевой трафик хоста",
    "Ibdata1 storage used": "Использованное хранилище Ibdata1",
    "Innodb buffer pool pages data": "Страницы данных буферного пула Innodb",
    "Innodb buffer pool pages dirty": "Грязные страницы буферного пула Innodb",
    "Innodb buffer pool pages flushed": "Сброшенные страницы буферного пула Innodb",
    "Innodb buffer pool pages free": "Свободные страницы буферного пула Innodb",
    "Innodb buffer pool reads": "Чтения буферного пула Innodb",
    "Innodb data writes": "Записи данных Innodb",
    "Innodb row lock time": "Время блокировки строк Innodb",
    "Innodb row lock waits": "Ожидания блокировки строк Innodb",
    "Mysql history list length": "Длина списка истории Mysql",
    "Mysql lock deadlocks": "Взаимоблокировки Mysql",
    "Mysql lock timeouts": "Тайм-ауты блокировок Mysql",
    "Mysql uptime": "Время работы Mysql",
    "Others storage used": "Использованное прочее хранилище",
    "Queries": "Запросы",
    "Replica IO status": "Статус ввода-вывода реплики",
    "Replica SQL status": "Статус SQL реплики",
    "Serverlog storage limit": "Лимит хранилища журналов сервера",
    "Serverlog storage percent": "Процент использования хранилища журналов сервера",
    "Serverlog storage used": "Использованное хранилище журналов сервера",
    "Slow queries": "Медленные запросы",
    "Storage IO count": "Количество операций ввода-вывода хранилища",
    "Storage IO percent": "Процент ввода-вывода хранилища",
    "Threads running": "Работающие потоки",
    "Total connections": "Всего подключений",
    # --- db-postgresql (Single Server table: full sentences) ---
    "The number of active connections to the server": "Количество активных подключений к серверу",
    "The amount of backup storage used. This metric represents the sum of storage consumed by all the full database backups, differential backups, and log backups retained based on the backup retention period set for the server.": "Объём использованного хранилища резервных копий. Эта метрика представляет сумму хранилища, потребляемого всеми полными резервными копиями базы данных, разностными резервными копиями и резервными копиями журналов, сохраняемыми в соответствии с периодом хранения резервных копий, заданным для сервера.",
    "The percentage of CPU in use": "Процент используемого ЦП",
    "The number of established connections that failed": "Количество установленных подключений, которые завершились сбоем",
    "The percentage of IO in use": "Процент используемого ввода-вывода",
    "Lag in bytes of the most lagging replica": "Отставание в байтах наиболее отстающей реплики",
    "The percentage of memory in use": "Процент используемой памяти",
    "Network in across active connections": "Входящий сетевой трафик по активным подключениям",
    "Network out across active connections": "Исходящий сетевой трафик по активным подключениям",
    "The time since the last replayed transaction. This metric is available for replica servers only.": "Время с момента последней воспроизведённой транзакции. Эта метрика доступна только для серверов-реплик.",
    "The maximum server log storage for this server": "Максимальное хранилище журналов сервера для этого сервера",
    "The percentage of server log storage used out of the server's maximum server log storage": "Процент использованного хранилища журналов сервера от максимального хранилища журналов сервера",
    "The amount of server log storage in use": "Объём используемого хранилища журналов сервера",
    "The maximum storage for this server": "Максимальное хранилище для этого сервера",
    "The percentage of storage used out of the server's maximum": "Процент использованного хранилища от максимума сервера",
    "The amount of storage in use. The storage used by the service may include the database files, transaction logs, and the server logs.": "Объём используемого хранилища. Хранилище, используемое сервисом, может включать файлы базы данных, журналы транзакций и журналы сервера.",
    "The number of requests that your application is sending to the storage disks in one second": "Количество запросов, которые ваше приложение отправляет дискам хранилища за одну секунду",
    # --- db-postgresql (Flexible Server table) ---
    "Number of connections to your server.": "Количество подключений к вашему серверу.",
    "Amount of backup storage used. This metric represents the sum of storage consumed by all the full database backups, differential backups, and log backups retained based on the backup retention period set for the server. The frequency of the backups is service managed. For geo-redundant storage, backup storage usage is twice that of the locally redundant storage.": "Объём использованного хранилища резервных копий. Эта метрика представляет сумму хранилища, потребляемого всеми полными резервными копиями базы данных, разностными резервными копиями и резервными копиями журналов, сохраняемыми в соответствии с периодом хранения резервных копий, заданным для сервера. Частота резервного копирования управляется сервисом. Для геоизбыточного хранилища использование хранилища резервных копий вдвое больше, чем для локально избыточного хранилища.",
    "Failed connections.": "Неудачные подключения.",
    "Succeeded connections.": "Успешные подключения.",
    "Number of credits used by the flexible server. Applicable to Burstable tier.": "Количество кредитов, использованных гибким сервером. Применимо к уровню Burstable.",
    "Number of credits available to burst. Applicable to Burstable tier.": "Количество кредитов, доступных для всплесков. Применимо к уровню Burstable.",
    "Percentage of CPU in use.": "Процент используемого ЦП.",
    "Number of outstanding I/O operations to the data disk.": "Количество ожидающих операций ввода-вывода к диску данных.",
    "Number of I/O operations to disk per second.": "Количество операций ввода-вывода к диску в секунду.",
    "Maximum transaction ID in use.": "Максимальный используемый идентификатор транзакции.",
    "Percentage of memory in use.": "Процент используемой памяти.",
    "Amount of incoming network traffic.": "Объём входящего сетевого трафика.",
    "Amount of outgoing network traffic.": "Объём исходящего сетевого трафика.",
    "Number of data disk I/O read operations per second.": "Количество операций чтения ввода-вывода диска данных в секунду.",
    "Bytes read per second from disk.": "Байты, читаемые с диска в секунду.",
    "Amount of storage space available.": "Объём доступного пространства хранилища.",
    "Percent of storage space used. The storage used by the service may include the database files, transaction logs, and the server logs.": "Процент использованного пространства хранилища. Хранилище, используемое сервисом, может включать файлы базы данных, журналы транзакций и журналы сервера.",
    "The storage used by the service may include the database files, transaction logs, and the server logs.": "Хранилище, используемое сервисом, может включать файлы базы данных, журналы транзакций и журналы сервера.",
    "Amount of storage space used by the transaction logs.": "Объём пространства хранилища, используемого журналами транзакций.",
    "Number of data disk I/O write operations per second.": "Количество операций записи ввода-вывода диска данных в секунду.",
    "Bytes written per second to disk.": "Байты, записываемые на диск в секунду.",
    # --- sql-database-hyperscale (name-echo; shipped dtu canon where same words) ---
    "Data space allocated": "Выделенное хранилище данных",
    "Base blob storage size": "Размер хранилища базовых BLOB-объектов",
    "Blocked by firewall": "Заблокировано брандмауэром",
    "Successful connections": "Успешные подключения",
    "CPU limit": "Лимит ЦП",
    "CPU used": "Использовано ЦП",
    "Deadlocks": "Взаимоблокировки",
    "Log backup storage size": "Размер хранилища резервных копий журналов",
    "Snapshot backup storage size": "Размер хранилища резервных копий моментальных снимков",
    "SQL server process core percent": "Процент использования ядер процесса SQL Server",
    "SQL server process memory percent": "Процент использования памяти процесса SQL Server",
    "Tempdb data file size kb": "Размер файла данных tempdb в КБ",
    "Tempdb log file size kb": "Размер файла журнала tempdb в КБ",
    "Tempdb percent log used": "Процент используемого журнала tempdb",
    "In-memory OLTP storage percent": "Процент хранилища In-Memory OLTP",
    # --- sql-managed-instance ---
    "Average CPU percentage": "Средний процент использования ЦП",
    "IO bytes read": "Прочитано байтов ввода-вывода",
    "IO bytes written": "Записано байтов ввода-вывода",
    "IO requests count": "Количество запросов ввода-вывода",
    "Storage space reserved": "Зарезервированное пространство хранилища",
    "Storage space used": "Использованное пространство хранилища",
    "Virtual core count": "Количество виртуальных ядер",
    # --- container-app ---
    "Number of reserved cores for container app revisions": "Количество зарезервированных ядер для ревизий контейнерного приложения",
    "Number of replicas count of container app": "Количество реплик контейнерного приложения",
    "Requests processed": "Обработанные запросы",
    "Restart count of container app replicas": "Количество перезапусков реплик контейнерного приложения",
    "Network received bytes": "Получено байтов по сети",
    "Number of total reserved cores for the container app": "Общее количество зарезервированных ядер для контейнерного приложения",
    "Network transmitted bytes": "Передано байтов по сети",
    "CPU consumed by the container app, in nano cores. 1,000,000,000 nano cores = 1 core": "ЦП, потребляемый контейнерным приложением, в наноядрах. 1 000 000 000 наноядер = 1 ядро",
    "Container App working set memory used in bytes.": "Используемая память рабочего набора Container App в байтах.",
    # --- container-apps-environment ---
    "The cores quota limit of managed environment": "Лимит квоты ядер управляемой среды",
    "The cores quota utilization of managed environment": "Использование квоты ядер управляемой среды",
    # --- container-instances ---
    "CPU usage on all cores in millicores": "Использование ЦП на всех ядрах в миллиядрах",
    "Total memory usage in byte": "Общее использование памяти в байтах",
    "The network bytes received per second": "Байты, получаемые по сети в секунду",
    "The network bytes transmitted per second": "Байты, передаваемые по сети в секунду",
    # --- container-registry ---
    "AgentPool CPU time in seconds": "Время ЦП AgentPool в секундах",
    "Run duration in milliseconds": "Длительность запуска в миллисекундах",
    "Number of successful image pulls": "Количество успешных извлечений образов",
    "Number of successful image pushes": "Количество успешных отправок образов",
    "Number of image pulls in total": "Общее количество извлечений образов",
    "Number of image pushes in total": "Общее количество отправок образов",
    # --- data-lake-storage-gen1 ---
    "Total amount of data stored in the account": "Общий объём данных, хранящихся в аккаунте",
    "Count of data read requests to the account": "Количество запросов на чтение данных к аккаунту",
    "Total amount of data read from the account": "Общий объём данных, прочитанных из аккаунта",
    "Count of data write requests to the account": "Количество запросов на запись данных к аккаунту",
    # EN source quirk "written from the account" (direction slip); RU renders the metric meaning
    "Total amount of data written from the account": "Общий объём данных, записанных в аккаунт",
    # --- storage-account-classic ---
    "The percentage of availability for the storage service or the specified API operation. Availability is calculated by taking the TotalBillableRequests value and dividing it by the number of applicable requests, including those that produced unexpected errors. All unexpected errors result in reduced availability for the storage service or the specified API operation.": "Процент доступности для сервиса хранилища или указанной операции API. Доступность рассчитывается путём деления значения TotalBillableRequests на количество применимых запросов, включая те, которые привели к неожиданным ошибкам. Все неожиданные ошибки приводят к снижению доступности для сервиса хранилища или указанной операции API.",
    "The amount of egress data, in bytes. This number includes egress from an external client into Azure Storage as well as egress within Azure. As a result, this number does not reflect billable egress.": "Объём исходящих данных в байтах. Это число включает исходящий трафик от внешнего клиента в Azure Storage, а также исходящий трафик внутри Azure. Поэтому это число не отражает оплачиваемый исходящий трафик.",
    "The amount of ingress data, in bytes. This number includes ingress from an external client into Azure Storage as well as ingress within Azure.": "Объём входящих данных в байтах. Это число включает входящий трафик от внешнего клиента в Azure Storage, а также входящий трафик внутри Azure.",
    "The end-to-end latency of successful requests made to a storage service or the specified API operation, in milliseconds. This value includes the required processing time within Azure Storage to read the request, send the response, and receive acknowledgment of the response.": "Сквозная задержка успешных запросов к сервису хранилища или указанной операции API в миллисекундах. Это значение включает необходимое время обработки внутри Azure Storage для чтения запроса, отправки ответа и получения подтверждения ответа.",
    "The latency used by Azure Storage to process a successful request, in milliseconds. This value does not include the network latency specified in SuccessE2ELatency.": "Задержка, используемая Azure Storage для обработки успешного запроса, в миллисекундах. Это значение не включает сетевую задержку, указанную в SuccessE2ELatency.",
    "The number of requests made to a storage service or the specified API operation. This number includes successful and failed requests, as well as requests which produced errors. Use ResponseType dimension for the number of different type of response.": "Количество запросов к сервису хранилища или указанной операции API. Это число включает успешные и неудачные запросы, а также запросы, которые привели к ошибкам. Используйте измерение ResponseType для получения количества ответов разных типов.",
    "Account used capacity.": "Использованная ёмкость аккаунта.",
    "The amount of storage used by the storage account’s Blob service in bytes.": "Объём хранилища, используемого сервисом Blob аккаунта хранилища, в байтах.",
    "The number of Blob in the storage account’s Blob service.": "Количество Blob в сервисе Blob аккаунта хранилища.",
    "The number of containers in the storage account’s Blob service.": "Количество контейнеров в сервисе Blob аккаунта хранилища.",
    "The amount of storage used by ADLS Gen2 (Hierarchical) Index in bytes.": "Объём хранилища, используемого индексом ADLS Gen2 (Hierarchical), в байтах.",
    "The amount of storage used by the storage account’s File service in bytes.": "Объём хранилища, используемого сервисом File аккаунта хранилища, в байтах.",
    "The number of file in the storage account’s File service.": "Количество файлов в сервисе File аккаунта хранилища.",
    "The number of file shares in the storage account’s File service.": "Количество файловых ресурсов в сервисе File аккаунта хранилища.",
    "The upper limit on the amount of storage that can be used by Azure Files Service in bytes.": "Верхний предел объёма хранилища, которое может использовать сервис Azure Files, в байтах.",
    "The number of snapshots present on the share in storage account’s Files Service.": "Количество моментальных снимков на файловом ресурсе в сервисе Files аккаунта хранилища.",
    "The amount of storage used by the snapshots in storage account’s File service in bytes.": "Объём хранилища, используемого моментальными снимками в сервисе File аккаунта хранилища, в байтах.",
    "The amount of storage used by the storage account’s Queue service in bytes.": "Объём хранилища, используемого сервисом Queue аккаунта хранилища, в байтах.",
    "The number of queue in the storage account’s Queue service.": "Количество очередей в сервисе Queue аккаунта хранилища.",
    "The approximate number of queue messages in the storage account’s Queue service.": "Приблизительное количество сообщений очереди в сервисе Queue аккаунта хранилища.",
    "The number of requests made to a storage service or the specified API operation. This number includes successful and failed requests, as well as requests which produced errors.": "Количество запросов к сервису хранилища или указанной операции API. Это число включает успешные и неудачные запросы, а также запросы, которые привели к ошибкам.",
    "The amount of storage used by the storage account’s Table service in bytes.": "Объём хранилища, используемого сервисом Table аккаунта хранилища, в байтах.",
    "The number of table in the storage account’s Table service.": "Количество таблиц в сервисе Table аккаунта хранилища.",
    "The number of table entities in the storage account’s Table service.": "Количество сущностей таблиц в сервисе Table аккаунта хранилища.",
    # --- storage-sync ---
    "Logs a value of `1` each time the server endpoint successfully completes a sync session with the cloud endpoint": "Регистрирует значение `1` каждый раз, когда серверная конечная точка успешно завершает сессию синхронизации с облачной конечной точкой",
    "The number of files synced": "Количество синхронизированных файлов",
    "The number of files that failed to sync": "Количество файлов, которые не удалось синхронизировать",
    "The total file size transferred for sync sessions": "Общий размер файлов, переданных за сессии синхронизации",
    "Logs a value of `1` each time the registered server successfully records a heartbeat with the cloud endpoint": "Регистрирует значение `1` каждый раз, когда зарегистрированный сервер успешно записывает heartbeat в облачную конечную точку",
    "The total size of data recalled by the server": "Общий размер данных, отозванных сервером",
    "The size of data recalled": "Размер отозванных данных",
    "The size of data recall throughput": "Пропускная способность отзыва данных",
    "The size of data recalled by application": "Размер данных, отозванных приложением",
}

DESC_MAP = dict(e38.DESC_MAP)
for k, v in NEW_DESC.items():
    DESC_MAP.setdefault(k, v)

warnings = []


def is_sep(cells):
    return all(set(c) <= set("-: ") for c in cells)


def tr_table_line(line, colmap, fname):
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
        elif cell == "Applicable":
            # container-registry: broken EN header puts Recommended values into
            # an unnamed column; translate the unambiguous value anyway
            out.append(REC_MAP[cell])
        else:  # Name, Dimensions, unknown -> keep EN
            out.append(cell)
    return "| " + " | ".join(out) + " |"


def tr_header(line):
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    out = [HEADER_LABEL.get(c, c) for c in cells]
    return "| " + " | ".join(out) + " |", cells


def has_cyr(s):
    return any("Ѐ" <= ch <= "ӿ" for ch in s)


def leftover_scan(fname, ru_text):
    """Warn on prose lines that stayed fully EN and are not whitelisted."""
    fmc = 0
    for n, line in enumerate(ru_text.split("\n"), 1):
        if line == "---" and fmc < 2:
            fmc += 1
            continue
        if fmc == 1:
            continue
        s = line.strip()
        if not s or s.startswith("|") or s.startswith("!["):
            continue
        if s in PASS_EN:
            continue
        if has_cyr(s):
            continue
        words = [
            w
            for w in s.replace("*", " ").replace("`", " ").split()
            if w.isalpha() and len(w) >= 3
        ]
        if len(words) >= 3:
            warnings.append("%s: EN leftover L%d -> %r" % (fname, n, s[:100]))


def build_one(fname):
    en = (
        open(os.path.join(EN_DIR, fname), encoding="utf-8").read().replace("\r\n", "\n")
    )
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
                out_lines.append(line)
            continue
        colmap = None
        if line in EXACT_LINE:
            out_lines.append(EXACT_LINE[line])
            continue
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
    with open(out_path, "wb") as f:
        f.write(result.encode("utf-8"))
    leftover_scan(fname, result)
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
