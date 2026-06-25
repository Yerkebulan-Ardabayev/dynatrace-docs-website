#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""L4-IF.42 - RU build that CLOSES azure-cloud-services-metrics 106/106.

Covers the 15 "irregular" leaf files left after L4-IF.41 + the directory hub:
  * 10 builtin/classic leaves (table: Metric key | Name | Unit | Aggregations |
    Monitoring consumption) - a different layout from the std metric tables.
  * storage-account (6-col: Display name | Name | Description | Dimensions |
    Unit | Recommended, 5 sub-tables).
  * application-insights, relay (std 5-col Name | Description | Dimensions |
    Unit | Recommended).
  * netapp-files (two 4-col tables Name | Description | Unit | Recommended).
  * hdinsight (OneAgent install step-cards + code fence + std 5-col table).
  * azure-cloud-services-metrics.md HUB (nav-grids of Azure product names +
    a ~140-row entity-type table).

Chain: imports L4-IF.41 (-> 40 -> 38 -> 37). Inherits DESC/UNIT/REC/HEADER/
DATE/PROSE/EXACT_LINE/PASS_EN; this batch adds its own on top.

CANON decisions for this batch (no prior translation existed; abridged
all-metrics/built-in-metrics reference pages are NOT a valid precedent):
  * Generic header-driven table handler. A column is translated only when its
    ENGLISH header name is Description / Unit / Recommended* / "Tag monitoring
    and filtering". Every identifier column stays EN byte-identical:
    Metric key, Name, Display name, Dimensions, Aggregations,
    Monitoring consumption, Service, Cloud type, Dynatrace entity type.
    This matches the directory's 91 shipped files (Name = EN findability label,
    Description/Unit/Recommended translated) and L4-IF.34 GCP canon.
  * builtin "Name" values ("Failed requests", "Capacity", ...) stay EN: they
    are the metric display labels shown in the English Metrics browser
    (findability), exactly like the GCP "Name" column (L4-IF.34). The builtin
    tables therefore translate only the header + Unit column.
  * Hub nav-grids ([Azure X](url) ...) stay EN byte-identical: a catalog of
    Azure product/service names (Azure product-name-EN canon). Only the hub
    prose, section headings, entity-table "Tag monitoring and filtering" column
    + headers are translated. FLAGGED for the user.
  * Header labels: Metric key -> Ключ метрики (310x corpus), Aggregations ->
    Агрегации (13x), Monitoring consumption -> Потребление мониторинга (11x),
    Display name -> Отображаемое имя (124x). Name/Description/Dimensions/Unit/
    Recommended inherited from e37.
  * Storage terminology mirrors the shipped storage-account-classic sibling
    (egress->исходящие данные, ingress->входящие, storage service->сервис
    хранилища, the specified API operation->указанная операция API,
    end-to-end latency->сквозная задержка, snapshot->моментальный снимок,
    storage account->аккаунт хранилища, file share->файловый ресурс).
  * workers -> рабочие процессы (L4-IF.40 shipped canon).
  * Pure product-name titles (built-in leaves, storage-account) stay EN whole
    (recovery-vault canon L4-IF.41). "monitoring" titles -> "Мониторинг X".
    Standalone "(deprecated)" tag in a title -> "(устарело)" (GCP title canon).
  No em-dash (CLAUDE.md §0). RU written wb/LF/no-trailing-nl (formatter-safe).
"""

import os
import importlib.util

_spec = importlib.util.spec_from_file_location(
    "e41", os.path.join(os.path.dirname(__file__), "_build_azure_metrics_l4if41.py")
)
e41 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(e41)

LEAF_EN = e41.EN_DIR  # .../azure-cloud-services-metrics
LEAF_RU = e41.RU_DIR
HUB_EN = os.path.join(os.path.dirname(LEAF_EN), "azure-cloud-services-metrics.md")
HUB_RU = os.path.join(os.path.dirname(LEAF_RU), "azure-cloud-services-metrics.md")

# leaf files (bare names under LEAF_EN); hub handled separately
BATCH = [
    "monitor-azure-api-management-services-builtin.md",
    "monitor-azure-app-gateways-builtin.md",
    "monitor-azure-cosmos-db-builtin.md",
    "monitor-azure-event-hub-builtin.md",
    "monitor-azure-iot-hub-builtin.md",
    "monitor-azure-load-balancers-builtin.md",
    "monitor-azure-redis-cache-builtin.md",
    "monitor-azure-service-bus-builtin.md",
    "monitor-azure-sql-servers-builtin.md",
    "monitor-azure-storage-account-builtin.md",
    "monitor-azure-storage-account.md",
    "monitor-azure-application-insights.md",
    "monitor-azure-hdinsight.md",
    "monitor-azure-netapp-files.md",
    "monitor-azure-relay.md",
]

# en_title -> ru_title. Identity entries (pure product names) keep EN whole.
TITLE_MAP = {
    "monitor-azure-api-management-services-builtin.md": (
        "Monitor Azure API Management (built-in) (deprecated)",
        "Мониторинг Azure API Management (built-in) (устарело)",
    ),
    "monitor-azure-app-gateways-builtin.md": (
        "Azure Application Gateways (built-in)",
        "Azure Application Gateways (built-in)",
    ),
    "monitor-azure-cosmos-db-builtin.md": (
        "Azure Cosmos DB (built-in)",
        "Azure Cosmos DB (built-in)",
    ),
    "monitor-azure-event-hub-builtin.md": (
        "Azure Event Hubs (built-in)",
        "Azure Event Hubs (built-in)",
    ),
    "monitor-azure-iot-hub-builtin.md": (
        "Azure IoT Hub (built-in)",
        "Azure IoT Hub (built-in)",
    ),
    "monitor-azure-load-balancers-builtin.md": (
        "Azure Load Balancers (built-in)",
        "Azure Load Balancers (built-in)",
    ),
    "monitor-azure-redis-cache-builtin.md": (
        "Azure Redis Cache (built-in)",
        "Azure Redis Cache (built-in)",
    ),
    "monitor-azure-service-bus-builtin.md": (
        "Azure Service Bus (built-in)",
        "Azure Service Bus (built-in)",
    ),
    "monitor-azure-sql-servers-builtin.md": (
        "Azure SQL Servers (built-in)",
        "Azure SQL Servers (built-in)",
    ),
    "monitor-azure-storage-account-builtin.md": (
        "Azure Storage Accounts (built-in)",
        "Azure Storage Accounts (built-in)",
    ),
    "monitor-azure-storage-account.md": (
        "Azure Storage Account (Blob, File, Queue, Table)",
        "Azure Storage Account (Blob, File, Queue, Table)",
    ),
    "monitor-azure-application-insights.md": (
        "Azure Application Insights monitoring",
        "Мониторинг Azure Application Insights",
    ),
    "monitor-azure-hdinsight.md": (
        "Azure HDInsight monitoring",
        "Мониторинг Azure HDInsight",
    ),
    "monitor-azure-netapp-files.md": (
        "Azure NetApp Files monitoring",
        "Мониторинг Azure NetApp Files",
    ),
    "monitor-azure-relay.md": (
        "Azure Relay monitoring",
        "Мониторинг Azure Relay",
    ),
    HUB_EN: ("All Azure cloud services", "Все облачные сервисы Azure"),
}

# ---- maps (inherit + extend) ----
HEADER_LABEL = dict(e41.HEADER_LABEL)
HEADER_LABEL.update(
    {
        "Metric key": "Ключ метрики",
        "Aggregations": "Агрегации",
        "Monitoring consumption": "Потребление мониторинга",
        "Display name": "Отображаемое имя",
        # hub entity table
        "Service": "Сервис",
        "Cloud type": "Тип облака",
        "Tag monitoring and filtering": "Мониторинг и фильтрация по тегам",
        "Dynatrace entity type": "Тип сущности Dynatrace",
    }
)

UNIT_MAP = dict(e41.UNIT_MAP)
UNIT_MAP.update(
    {
        "Millisecond": UNIT_MAP.get("MilliSecond", "Миллисекунда"),
        "Percent (%)": UNIT_MAP.get("Percent", "Процент") + " (%)",
        "Byte/second": UNIT_MAP.get("BytePerSecond", "Байт в секунду"),
        "Byte/minute": "Байт в минуту",
    }
)

REC_MAP = dict(e41.REC_MAP)
REC_MAP.update({"Not applicable": "Неприменимо"})
# columns whose values are translated via REC_MAP (Applicable / Not applicable)
REC_COLS = {"Tag monitoring and filtering"}

DATE_MAP = dict(e41.DATE_MAP)
DATE_MAP.update(
    {
        "* Updated on Nov 15, 2023": "* Обновлено 15 ноября 2023 г.",
        "* Updated on Dec 05, 2023": "* Обновлено 5 декабря 2023 г.",
        "* Updated on Jan 22, 2026": "* Обновлено 22 января 2026 г.",
        "* Updated on Feb 12, 2024": "* Обновлено 12 февраля 2024 г.",
        "* Published Sep 22, 2020": "* Опубликовано 22 сентября 2020 г.",
        "* Published Jun 25, 2020": "* Опубликовано 25 июня 2020 г.",
        "* Published Jul 27, 2022": "* Опубликовано 27 июля 2022 г.",
        "* Published Jul 26, 2022": "* Опубликовано 26 июля 2022 г.",
        "* Published Aug 19, 2020": "* Опубликовано 19 августа 2020 г.",
    }
)

PROSE = list(e41.PROSE) + [
    ("* 1-min read", "* Чтение: 1 мин"),
    ("* 2-min read", "* Чтение: 2 мин"),
    ("* 4-min read", "* Чтение: 4 мин"),
    ("* 11-min read", "* Чтение: 11 мин"),
    ("* 19-min read", "* Чтение: 19 мин"),
    ("* Overview", "* Обзор"),
]

# ---- metric Description translations (92 new) ----
DESC_MAP = dict(e41.DESC_MAP)
DESC_MAP.update(
    {
        # ---- Storage Account (Blob/File/Queue/Table); short EN source, canon
        #      from shipped storage-account-classic ----
        "The percentage of availability for the storage service or the specified API operation. All unexpected errors result in reduced availability for the storage service or the specified API operation.": "Процент доступности для сервиса хранилища или указанной операции API. Все неожиданные ошибки приводят к снижению доступности для сервиса хранилища или указанной операции API.",
        "The amount of egress data.": "Объём исходящих данных.",
        "The amount of ingress data, in bytes.": "Объём входящих данных в байтах.",
        "The average end-to-end latency of successful requests made to a storage service or the specified API operation, in milliseconds.": "Средняя сквозная задержка успешных запросов к сервису хранилища или указанной операции API в миллисекундах.",
        "The average time used to process a successful request by Azure Storage. This value does not include the network latency specified in SuccessE2ELatency.": "Среднее время обработки успешного запроса в Azure Storage. Это значение не включает сетевую задержку, указанную в SuccessE2ELatency.",
        "The number of requests made to a storage service or the specified API operation. Use ResponseType dimension for the number of different type of response.": "Количество запросов к сервису хранилища или указанной операции API. Используйте измерение ResponseType, чтобы получить количество ответов разных типов.",
        "The amount of storage used by the storage account. For standard storage accounts, it's the sum of capacity used by blob, table, file, and queue. For premium storage accounts and Blob storage accounts, it is the same as BlobCapacity or FileCapacity.": "Объём хранилища, используемого аккаунтом хранилища. Для стандартных аккаунтов хранилища это сумма ёмкости, используемой blob, table, file и queue. Для premium-аккаунтов хранилища и аккаунтов Blob storage оно совпадает с BlobCapacity или FileCapacity.",
        "The amount of storage used by the storage account's Blob service in bytes.": "Объём хранилища, используемого сервисом Blob аккаунта хранилища, в байтах.",
        "The number of containers in the storage account.": "Количество контейнеров в аккаунте хранилища.",
        "The number of blob objects stored in the storage account.": "Количество объектов blob, хранящихся в аккаунте хранилища.",
        "The amount of storage provisioned in the storage account's Blob service in bytes.": "Объём хранилища, выделенного в сервисе Blob аккаунта хранилища, в байтах.",
        "The amount of storage used by Azure Data Lake Storage Gen2 hierarchical index.": "Объём хранилища, используемого иерархическим индексом Azure Data Lake Storage Gen2.",
        "The amount of File storage used by the storage account.": "Объём хранилища File, используемого аккаунтом хранилища.",
        "The number of files in the storage account.": "Количество файлов в аккаунте хранилища.",
        "The upper limit on the amount of storage that can be used by Azure Files Service in bytes.": "Верхний предел объёма хранилища, которое может использовать сервис Azure Files, в байтах.",
        "The number of file shares in the storage account.": "Количество файловых ресурсов в аккаунте хранилища.",
        "The baseline number of provisioned IOPS for the premium file share in the premium files storage account.": "Базовое количество выделенных IOPS для premium-файлового ресурса в premium-аккаунте files storage.",
        "The number of snapshots present on the share in storage account's Files Service.": "Количество моментальных снимков на ресурсе в сервисе Files аккаунта хранилища.",
        "The amount of storage used by the snapshots in storage account's File service in bytes.": "Объём хранилища, используемого моментальными снимками в сервисе File аккаунта хранилища, в байтах.",
        "The amount of Queue storage used by the storage account.": "Объём хранилища Queue, используемого аккаунтом хранилища.",
        "The number of queues in the storage account.": "Количество очередей в аккаунте хранилища.",
        "The number of unexpired queue messages in the storage account.": "Количество неистёкших сообщений очереди в аккаунте хранилища.",
        "The amount of Table storage used by the storage account.": "Объём хранилища Table, используемого аккаунтом хранилища.",
        "The number of tables in the storage account.": "Количество таблиц в аккаунте хранилища.",
        "The number of table entities in the storage account.": "Количество сущностей таблиц в аккаунте хранилища.",
        # ---- Application Insights ----
        "The time between receiving an HTTP request and finishing sending the response": "Время между получением HTTP-запроса и завершением отправки ответа",
        "The count of completed HTTP requests": "Количество завершённых HTTP-запросов",
        "The count of failed HTTP requests": "Количество неуспешных HTTP-запросов",
        "The percentage of successfully completed availability tests": "Процент успешно завершённых тестов доступности",
        "The count of availability tests": "Количество тестов доступности",
        "Availability test duration": "Длительность теста доступности",
        "The time between user request and network connection": "Время между запросом пользователя и сетевым подключением",
        "The time between receiving the last byte of a document until the DOM is loaded": "Время от получения последнего байта документа до загрузки DOM",
        "The receiving response time": "Время получения ответа",
        "The send request time": "Время отправки запроса",
        "The browser page load time": "Время загрузки страницы в браузере",
        "The number of dependency calls": "Количество вызовов зависимостей",
        "The dependency duration": "Длительность вызова зависимости",
        "The number of dependency call failures": "Количество неуспешных вызовов зависимостей",
        "The number of page views": "Количество просмотров страниц",
        "The page view load time": "Время загрузки просмотра страницы",
        "The HTTP request execution time": "Время выполнения HTTP-запроса",
        "The HTTP requests in application queue": "HTTP-запросы в очереди приложения",
        "The HTTP request rate": "Частота HTTP-запросов",
        "The exception rate": "Частота исключений",
        "The process IO rate": "Частота ввода-вывода процесса",
        "The processor time": "Процессорное время",
        "The available memory": "Доступная память",
        "The process private bytes": "Приватные байты процесса",
        "The server request rate": "Частота запросов к серверу",
        "The number of exceptions": "Количество исключений",
        "The browser exceptions": "Исключения в браузере",
        "The server exceptions": "Исключения на сервере",
        "The number of traces": "Количество трассировок",
        # ---- NetApp Files (pools + volumes) ----
        "Provisioned size of the pool": "Выделенный размер пула",
        "Allocated used size of the pool": "Используемый выделенный размер пула",
        "Sum of the logical size of all the volumes belonging to the pool": "Сумма логических размеров всех томов, принадлежащих пулу",
        "Sum of snapshot size of all volumes in this pool": "Сумма размеров моментальных снимков всех томов в этом пуле",
        "The average time for reads from the volume in milliseconds": "Среднее время чтения с тома в миллисекундах",
        "The average time for writes from the volume in milliseconds": "Среднее время записи на том в миллисекундах",
        "Volume backup active state": "Состояние активности резервного копирования тома",
        "Logical bytes backed up": "Логические байты, помещённые в резервную копию",
        "Operation state": "Состояние операции",
        "Bytes transferred for operation": "Байты, переданные для операции",
        "Volume protected state": "Состояние защищённости тома",
        "Read IOPS": "IOPS чтения",
        "Volume allocated size": "Выделенный размер тома",
        "Volume consumed size": "Потреблённый размер тома",
        "Volume snapshot size": "Размер моментального снимка тома",
        "Write IOPS": "IOPS записи",
        "Checks if volume replication status is healthy": "Проверяет, исправен ли статус репликации тома",
        "Volume replication lag time": "Время отставания репликации тома",
        "Volume replication last transfer duration": "Длительность последней передачи репликации тома",
        "Volume replication last transfer size": "Размер последней передачи репликации тома",
        "Volume replication progress": "Прогресс репликации тома",
        "Checks if volume replication is transferring": "Проверяет, идёт ли передача репликации тома",
        "Volume replication total transfer": "Общий объём передачи репликации тома",
        # ---- Relay ----
        "Total active connections for Azure Relay": "Всего активных подключений для Azure Relay",
        "Total active listeners for Azure Relay": "Всего активных слушателей для Azure Relay",
        "Total bytes transferred for Azure Relay": "Всего переданных байтов для Azure Relay",
        "Client error on listener connections for Azure Relay": "Клиентская ошибка на подключениях слушателей для Azure Relay",
        "Server error on listener connections for Azure Relay": "Серверная ошибка на подключениях слушателей для Azure Relay",
        "Successful listener connections for Azure Relay": "Успешные подключения слушателей для Azure Relay",
        "Total listener connections for Azure Relay": "Всего подключений слушателей для Azure Relay",
        "Total listener disconnects for Azure Relay": "Всего отключений слушателей для Azure Relay",
        "Client error on sender connection for Azure Relay": "Клиентская ошибка на подключении отправителя для Azure Relay",
        "Server error on sender connection for Azure Relay": "Серверная ошибка на подключении отправителя для Azure Relay",
        "Successful sender connections for Azure Relay": "Успешные подключения отправителей для Azure Relay",
        "Total sender connections requests for Azure Relay": "Всего запросов на подключение отправителей для Azure Relay",
        "Total sender disconnects for Azure Relay": "Всего отключений отправителей для Azure Relay",
        # ---- HDInsight ----
        "Number of gateway requests by categories (1xx/2xx/3xx/4xx/5xx)": "Количество запросов к шлюзу по категориям (1xx/2xx/3xx/4xx/5xx)",
        "Number of gateway requests": "Количество запросов к шлюзу",
        "Number of active workers": "Количество активных рабочих процессов",
    }
)

# ---- prose / headings / step-cards (content-keyed) ----
EXACT_LINE = dict(e41.EXACT_LINE)
EXACT_LINE.update(
    {
        # shared headings
        "## Prerequisites": "## Предварительные требования",
        "## Enable monitoring": "## Включение мониторинга",
        "## View service metrics": "## Просмотр метрик сервиса",
        "## Available metrics": "## Доступные метрики",
        "## Limitations": "## Ограничения",
        "## Additional notes": "## Дополнительные замечания",
        "### View metrics on the Azure account page": "### Просмотр метрик на странице учётной записи Azure",
        "### View metrics on a dashboard": "### Просмотр метрик на дашборде",
        # builtin migration note (top of every classic page)
        "For information about differences between classic services and other services, see [Migrate from Azure classic (formerly 'built-in') services to cloud services](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide \"Migrate Azure classic services to their new versions.\").": 'Информацию о различиях между классическими и другими сервисами см. в разделе [Миграция с классических (ранее «built-in») сервисов Azure на облачные сервисы](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide "Миграция классических сервисов Azure на их новые версии.").',
        # builtin Enable-monitoring link
        'To learn how to enable service monitoring, see [Enable service monitoring](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").': 'О том, как включить мониторинг сервиса, см. в разделе [Включение мониторинга сервиса](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Включение мониторинга Azure в Dynatrace.").',
        # builtin View-service-metrics prose (Azure account page flow)
        "You can view Azure service metrics in your Dynatrace environment on the Azure subscription page or on your own dashboard.": "Метрики сервисов Azure можно просматривать в вашем окружении Dynatrace на странице подписки Azure или на собственном дашборде.",
        "Values in the table depend upon the selected timeframe. For more details, see [Troubleshoot timeframe comparison for Azure monitoring setup)](https://dt-url.net/7j438f0).": "Значения в таблице зависят от выбранного временного интервала. Подробнее см. в разделе [Устранение неполадок со сравнением временных интервалов при настройке мониторинга Azure)](https://dt-url.net/7j438f0).",
        "To access metrics on the Azure account page": "Чтобы получить доступ к метрикам на странице учётной записи Azure",
        "1. Go to **Azure**.": "1. Перейдите в **Azure**.",
        "2. Choose the Azure subscription.": "2. Выберите подписку Azure.",
        "3. Select the service whose metrics you want to check. Metrics for the selected service are visible under the infographic in the service section, similarly to the example below.": "3. Выберите сервис, метрики которого нужно проверить. Метрики выбранного сервиса отображаются под инфографикой в разделе сервиса, как в примере ниже.",
        'You can create your own dashboard for viewing Azure service metrics. For information on how to create dashboards, see [Create and edit Dynatrace dashboards](/managed/analyze-explore-automate/dashboards-classic/dashboards/create-dashboards "Learn how to create and edit Dynatrace dashboards.").': 'Вы можете создать собственный дашборд для просмотра метрик сервисов Azure. О том, как создавать дашборды, см. в разделе [Создание и редактирование дашбордов Dynatrace](/managed/analyze-explore-automate/dashboards-classic/dashboards/create-dashboards "Узнайте, как создавать и редактировать дашборды Dynatrace.").',
        # ---- builtin Prerequisites bullet ----
        "* To disable monitoring of built-in services, you need Environment ActiveGate version 1.245+ and Dynatrace version 1.247+.": "* Чтобы отключить мониторинг встроенных сервисов, требуется Environment ActiveGate версии 1.245+ и Dynatrace версии 1.247+.",
        # ---- per-file intro sentences (builtin) ----
        "Dynatrace ingests metrics from Azure Metrics API for Azure API Management Services. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.": "Dynatrace получает метрики из Azure Metrics API для Azure API Management Services. Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать их по нескольким измерениям и создавать пользовательские диаграммы, которые можно закрепить на дашбордах.",
        "Dynatrace ingests metrics from Azure Metrics API for Azure Application Gateways. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.": "Dynatrace получает метрики из Azure Metrics API для Azure Application Gateways. Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать их по нескольким измерениям и создавать пользовательские диаграммы, которые можно закрепить на дашбордах.",
        "Dynatrace ingests metrics from Azure Metrics API for Azure Cosmos DB. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.": "Dynatrace получает метрики из Azure Metrics API для Azure Cosmos DB. Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать их по нескольким измерениям и создавать пользовательские диаграммы, которые можно закрепить на дашбордах.",
        "Dynatrace ingests metrics from Azure Metrics API for Azure Event Hubs. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.": "Dynatrace получает метрики из Azure Metrics API для Azure Event Hubs. Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать их по нескольким измерениям и создавать пользовательские диаграммы, которые можно закрепить на дашбордах.",
        "Dynatrace ingests metrics from Azure Metrics API for Azure IoT Hub. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.": "Dynatrace получает метрики из Azure Metrics API для Azure IoT Hub. Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать их по нескольким измерениям и создавать пользовательские диаграммы, которые можно закрепить на дашбордах.",
        "Dynatrace ingests metrics from Azure Metrics API for Azure Load Balancers. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.": "Dynatrace получает метрики из Azure Metrics API для Azure Load Balancers. Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать их по нескольким измерениям и создавать пользовательские диаграммы, которые можно закрепить на дашбордах.",
        "Dynatrace ingests metrics from Azure Metrics API for Azure Redis Cache. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.": "Dynatrace получает метрики из Azure Metrics API для Azure Redis Cache. Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать их по нескольким измерениям и создавать пользовательские диаграммы, которые можно закрепить на дашбордах.",
        "Dynatrace ingests metrics from Azure Metrics API for Azure Service Bus. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.": "Dynatrace получает метрики из Azure Metrics API для Azure Service Bus. Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать их по нескольким измерениям и создавать пользовательские диаграммы, которые можно закрепить на дашбордах.",
        "Dynatrace ingests metrics from Azure Metrics API for Azure SQL Servers. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.": "Dynatrace получает метрики из Azure Metrics API для Azure SQL Servers. Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать их по нескольким измерениям и создавать пользовательские диаграммы, которые можно закрепить на дашбордах.",
        "Dynatrace ingests metrics from Azure Metrics API for Azure Storage Accounts. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.": "Dynatrace получает метрики из Azure Metrics API для Azure Storage Accounts. Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать их по нескольким измерениям и создавать пользовательские диаграммы, которые можно закрепить на дашбордах.",
        "Dynatrace ingests metrics for multiple preselected namespaces, including Azure Storage Account. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.": "Dynatrace получает метрики для нескольких предварительно выбранных пространств имён, включая Azure Storage Account. Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать их по нескольким измерениям и создавать пользовательские диаграммы, которые можно закрепить на дашбордах.",
        # ---- per-file SQL-servers-builtin sub-headings ----
        "### SQL Databases": "### SQL Databases",
        "### SQL elastic pools": "### SQL elastic pools",
        # ---- storage-account body prose ----
        "This service monitors a part of Storage Account (`Microsoft.Storage/storageAccounts`).": "Этот сервис отслеживает часть Storage Account (`Microsoft.Storage/storageAccounts`).",
        "While you have this service configured, you **can't** have Azure Storage accounts (built-in) service turned on.": "Пока этот сервис настроен, вы **не можете** включить сервис Azure Storage accounts (built-in).",
        "To monitor resources of the `Microsoft.ClassicStorage/storageAccounts` type, check **Storage Account Classic** and the **Cloud services** section on the Azure overview page": "Для мониторинга ресурсов типа `Microsoft.ClassicStorage/storageAccounts` отметьте **Storage Account Classic** и раздел **Cloud services** на странице обзора Azure",
        "This service monitors a part of Storage Account (`Microsoft.Storage/storageAccounts`). While you have this service configured, you can't have Azure Storage accounts (built-in) service turned on.": "Этот сервис отслеживает часть Storage Account (`Microsoft.Storage/storageAccounts`). Пока этот сервис настроен, вы не можете включить сервис Azure Storage accounts (built-in).",
        "To monitor resources of the `Microsoft.ClassicStorage/storageAccounts` type, check **Storage Account Classic** and **Cloud services** sections on the Azure overview page.": "Для мониторинга ресурсов типа `Microsoft.ClassicStorage/storageAccounts` отметьте разделы **Storage Account Classic** и **Cloud services** на странице обзора Azure.",
        "**Storage Account**": "**Storage Account**",
        "**Azure Storage Blob Services**": "**Azure Storage Blob Services**",
        "**Azure Storage File Services**": "**Azure Storage File Services**",
        "**Azure Storage Queue Services**": "**Azure Storage Queue Services**",
        "**Azure Storage Table Services**": "**Azure Storage Table Services**",
        "As newly implemented Azure Storage Accounts and Azure Storage accounts (built-in) monitor the same resources (from the `Microsoft.Storage/storageAccounts` group), they can't be switched on simultaneously.": "Поскольку новые Azure Storage Accounts и Azure Storage accounts (built-in) отслеживают одни и те же ресурсы (из группы `Microsoft.Storage/storageAccounts`), их нельзя включить одновременно.",
        "* Enabling the built-in version will disable all of the generic versions.": "* Включение встроенной версии отключит все обычные версии.",
        "* Enabling any of the generic versions will disable the built-in version.": "* Включение любой из обычных версий отключит встроенную версию.",
        # ---- application-insights / relay Limitations ----
        "Running the Azure App Service extension at the same time with Azure Application Insights is not supported.": "Одновременный запуск расширения Azure App Service и Azure Application Insights не поддерживается.",
        "Metrics are only supported for the Hybrid Connections feature in Azure Relay.": "Метрики поддерживаются только для функции Hybrid Connections в Azure Relay.",
        # ---- builtin per-service "This service monitors..." body sentences ----
        "This service monitors both `Microsoft.EventHub/namespaces` and `Microsoft.EventHub/namespaces/eventHubs`.": "Этот сервис отслеживает и `Microsoft.EventHub/namespaces`, и `Microsoft.EventHub/namespaces/eventHubs`.",
        "Only monitored Event Hubs (as opposed to Event Hub Namespaces) are directly presented on the Azure overview page, in the **Event hubs** section. To view metrics for Event Hub Namespace, create a custom dashboard.": "Непосредственно на странице обзора Azure, в разделе **Event hubs**, представлены только отслеживаемые Event Hubs (в отличие от Event Hub Namespaces). Чтобы просмотреть метрики для Event Hub Namespace, создайте пользовательский дашборд.",
        "This service monitors Azure Cache for Redis (`Microsoft.Cache/redis`).": "Этот сервис отслеживает Azure Cache for Redis (`Microsoft.Cache/redis`).",
        "No metrics are available for Basic SKU Load Balancers.": "Для Load Balancers уровня Basic SKU метрики недоступны.",
        "This service monitors SQL Servers, SQL Databases (only containing the user kind) and SQL elastic pools.": "Этот сервис отслеживает SQL Servers, SQL-базы данных (только пользовательского типа) и SQL elastic pools.",
        "You can find the already monitored resources on the Azure overview page, **Databases components** view.": "Уже отслеживаемые ресурсы можно найти на странице обзора Azure, раздел **Databases components**.",
        "To monitor resources of the hyperscale/data warehouse resources, or Managed deployments, check the SQL Database Hyperscale/SQL Data Warehouse/SQL Managed Instance and the Azure overview page, **Cloud services** view.": "Для мониторинга ресурсов hyperscale/data warehouse или Managed-развёртываний проверьте SQL Database Hyperscale/SQL Data Warehouse/SQL Managed Instance и страницу обзора Azure, раздел **Cloud services**.",
        "This service monitors Storage Accounts (`Microsoft.Storage/storageAccounts`). You can find the already monitored resources on the Azure overview page in **Storage accounts** section.": "Этот сервис отслеживает Storage Accounts (`Microsoft.Storage/storageAccounts`). Уже отслеживаемые ресурсы можно найти на странице обзора Azure в разделе **Storage accounts**.",
        "The Storage, StorageV2 and BlobStorage service types are supported. To monitor resources of the `Microsoft.ClassicStorage/storageAccounts` type, check **Storage Account Classic** and the **Cloud services** section on the Azure overview page.": "Поддерживаются типы сервисов Storage, StorageV2 и BlobStorage. Для мониторинга ресурсов типа `Microsoft.ClassicStorage/storageAccounts` отметьте **Storage Account Classic** и раздел **Cloud services** на странице обзора Azure.",
        "This service monitors the same Azure resources as Azure Storage Account and Azure Storage Blob/File/Queue Services from **Cloud services** section. For more customizable monitoring switch to the latter ones. The historical (built-in) and new versions can't be switched on at the same time.": "Этот сервис отслеживает те же ресурсы Azure, что и Azure Storage Account и Azure Storage Blob/File/Queue Services из раздела **Cloud services**. Для более гибкой настройки мониторинга перейдите на последние. Историческую (built-in) и новые версии нельзя включить одновременно.",
        "* `Azure Storage Accounts (built-in)` monitors the same Azure resources as `Azure Storage Account` and `Azure Storage Blob/File/Queue Services` from `Cloud services` section. For more customizable monitoring switch to the latter ones. The built-in and generic versions can't be switched on simultaneously:": "* `Azure Storage Accounts (built-in)` отслеживает те же ресурсы Azure, что и `Azure Storage Account` и `Azure Storage Blob/File/Queue Services` из раздела `Cloud services`. Для более гибкой настройки мониторинга перейдите на последние. Встроенную и обычные версии нельзя включить одновременно:",
        "  + Enabling the built-in version will disable all of the generic versions.": "  + Включение встроенной версии отключит все обычные версии.",
        "  + Enabling any of the generic versions will disable the built-in version.": "  + Включение любой из обычных версий отключит встроенную версию.",
        # ---- hdinsight intro + Install OneAgent step-cards ----
        "On the Azure HDInsights dashboard, you get holistic insights into your Hadoop, Spark, and Kafka resources and can cover all angles of your big data monitoring in one place.": "На дашборде Azure HDInsights вы получаете целостное представление о ресурсах Hadoop, Spark и Kafka и можете охватить мониторинг больших данных со всех сторон в одном месте.",
        "## Install OneAgent Optional": "## Установка OneAgent Необязательно",
        "For additional Hadoop, Spark, and Kafka insights, you can install OneAgent on Azure HDInsight cluster nodes.": "Для получения дополнительных данных мониторинга по Hadoop, Spark и Kafka можно установить OneAgent на узлы кластера Azure HDInsight.",
        "How to install OneAgent on Azure HDInsight cluster (Linux)": "Как установить OneAgent на кластер Azure HDInsight (Linux)",
        "Follow the steps below to install OneAgent on Azure HDInsight cluster (Linux).": "Выполните приведённые ниже шаги, чтобы установить OneAgent на кластер Azure HDInsight (Linux).",
        '[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")': '[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")',
        '**Create an install script**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-hdinsight#step-1 "Monitor Azure HDInsight and view available metrics.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")': '**Создайте скрипт установки**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-hdinsight#step-1 "Мониторинг Azure HDInsight и просмотр доступных метрик.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")',
        '**Create an HDInsight cluster**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-hdinsight#step-2 "Monitor Azure HDInsight and view available metrics.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")': '**Создайте кластер HDInsight**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-hdinsight#step-2 "Мониторинг Azure HDInsight и просмотр доступных метрик.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")',
        '**Restart the processes**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-hdinsight#step-3 "Monitor Azure HDInsight and view available metrics.")': '**Перезапустите процессы**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-hdinsight#step-3 "Мониторинг Azure HDInsight и просмотр доступных метрик.")',
        "### Step 1 Create an install script": "### Шаг 1 Создайте скрипт установки",
        "### Step 2 Create an HDInsight cluster": "### Шаг 2 Создайте кластер HDInsight",
        "### Step 3 Restart the processes": "### Шаг 3 Перезапустите процессы",
        "1. Go to **Deploy Dynatrace**.": "1. Перейдите в **Deploy Dynatrace**.",
        "2. Select **Start installation** > **Linux**.": "2. Выберите **Start installation** > **Linux**.",
        "3. On the **Install Dynatrace OneAgent on your Linux hosts** page, copy the command below **Use this command on the target host** and the command below **And run the installer with root rights** into a plain text document called `installdynatrace.sh`, and save it to your local machine.": "3. На странице **Install Dynatrace OneAgent on your Linux hosts** скопируйте команду под надписью **Use this command on the target host** и команду под надписью **And run the installer with root rights** в текстовый документ с именем `installdynatrace.sh` и сохраните его на локальном компьютере.",
        "**Example of install script**": "**Пример скрипта установки**",
        "3. Go to Microsoft Azure Storage Explorer and upload the Dynatrace installation file `installdynatrace.sh` to an accessible Blob Storage Container.": "3. Откройте Microsoft Azure Storage Explorer и загрузите установочный файл Dynatrace `installdynatrace.sh` в доступный контейнер Blob Storage.",
        "4. Click right on `installdynatrace.sh` and select **Set public access level**. In the pop-up window, set the access level to **Public read access for container and blobs**, and click **Apply**.": "4. Щёлкните правой кнопкой мыши по `installdynatrace.sh` и выберите **Set public access level**. Во всплывающем окне установите уровень доступа **Public read access for container and blobs** и нажмите **Apply**.",
        '5. On the top menu of the Microsoft Azure Storage Explorer window, click on "Copy URL" and save it locally for later access.': '5. В верхнем меню окна Microsoft Azure Storage Explorer нажмите "Copy URL" и сохраните ссылку локально для последующего доступа.',
        "1. Login to Microsoft Azure portal and select **HDInsight clusters** on the left-side menu.": "1. Войдите на портал Microsoft Azure и выберите **HDInsight clusters** в меню слева.",
        "2. Select **Create hdinsight cluster**.": "2. Выберите **Create hdinsight cluster**.",
        "3. Select **Custom** installation.": "3. Выберите установку **Custom**.",
        "4. Follow the creating wizard to configure basic settings, set storage settings, applications and cluster size.": "4. Следуйте мастеру создания, чтобы настроить базовые параметры, параметры хранилища, приложения и размер кластера.",
        "5. In the **Advanced settings** menu, select **Script Actions**.": "5. В меню **Advanced settings** выберите **Script Actions**.",
        "6. Select **Submit new**.": "6. Выберите **Submit new**.",
        "7. In the **Submit script action** menu, enter **Custom** for the script type, choose a name, for instance **Install Dynatrace**, and paste the URL of the script you copied previously in the **Bash script URI** field. If you want to install Dynatrace OneAgent on all the nodes, select all node types (**Head**, **Worker**, **Zookeeper**).": "7. В меню **Submit script action** укажите тип скрипта **Custom**, выберите имя, например **Install Dynatrace**, и вставьте URL скопированного ранее скрипта в поле **Bash script URI**. Если вы хотите установить Dynatrace OneAgent на все узлы, выберите все типы узлов (**Head**, **Worker**, **Zookeeper**).",
        "8. Select **Create** to save the changes and create the HDInsight cluster.": "8. Нажмите **Create**, чтобы сохранить изменения и создать кластер HDInsight.",
        "Once the installation is completed, make sure to restart the processes.": "После завершения установки обязательно перезапустите процессы.",
        "1. Select your newly created cluster on the MicrosoftAzure portal. On the **Overview** menu, click on your cluster URL.": "1. Выберите только что созданный кластер на портале Microsoft Azure. В меню **Overview** нажмите на URL вашего кластера.",
        "2. For each node where you chose to install Dynatrace, go to **Service Actions** and select **Restart All**.": "2. Для каждого узла, где вы выбрали установку Dynatrace, перейдите в **Service Actions** и выберите **Restart All**.",
        "As soon as processes are restarted, Dynatrace will start collecting metrics.": "Как только процессы будут перезапущены, Dynatrace начнёт собирать метрики.",
        "### Set up a management zone": "### Настройка зоны управления",
        'To import a dashboard for Azure HDInsight, you need to [set up a management zone](/managed/manage/identity-access-management/permission-management/management-zones/set-up-management-zones "Create and assign access rights to management zones.") to limit the entities displayed on the dashboard to cluster nodes only and exclude other hosts not relevant to the service.': 'Чтобы импортировать дашборд для Azure HDInsight, необходимо [настроить зону управления](/managed/manage/identity-access-management/permission-management/management-zones/set-up-management-zones "Создание зон управления и назначение прав доступа к ним."), чтобы ограничить отображаемые на дашборде сущности только узлами кластера и исключить другие хосты, не относящиеся к сервису.',
        "When you create a management zone for this dashboard:": "При создании зоны управления для этого дашборда:",
        "1. Create a rule that identifies hosts based on a common property:": "1. Создайте правило, которое определяет хосты по общему свойству:",
        "   * Host name contains the `hdi` string": "   * Имя хоста содержит строку `hdi`",
        "2. Create a rule that identifies custom devices based on a common property:": "2. Создайте правило, которое определяет пользовательские устройства по общему свойству:",
        "   * Custom device group contains the `HDInsight` string.": "   * Группа пользовательских устройств содержит строку `HDInsight`.",
        "3. Create a rule that identifies services based on a common property:": "3. Создайте правило, которое определяет сервисы по общему свойству:",
        'After you create the management zone, assign it to your dashboard (from the dashboard, select **Edit** > **Settings** > **Default management zone**). For more information, see [Dashboard timeframe and management zone](/managed/analyze-explore-automate/dashboards-classic/dashboards/dashboard-timeframe "Learn about Dynatrace dashboard timeframe and management zone settings.").': 'После создания зоны управления назначьте её своему дашборду (на дашборде выберите **Edit** > **Settings** > **Default management zone**). Дополнительную информацию см. в разделе [Временной интервал и зона управления дашборда](/managed/analyze-explore-automate/dashboards-classic/dashboards/dashboard-timeframe "Узнайте о настройках временного интервала и зоны управления дашбордов Dynatrace.").',
        # ---- HUB prose ----
        "Dynatrace can receive Azure Monitor metrics for multiple preselected services.": "Dynatrace может получать метрики Azure Monitor для нескольких предварительно выбранных сервисов.",
        "* You can view graphs per service instance, with a set of dimensions, and create custom graphs that you can pin to your dashboards.": "* Вы можете просматривать графики для каждого экземпляра сервиса с набором измерений и создавать пользовательские графики, которые можно закрепить на дашбордах.",
        "* You can reduce your Azure Monitor costs and throttling by selecting which additional services to monitor.": "* Вы можете снизить затраты на Azure Monitor и регулирование, выбрав, какие дополнительные сервисы отслеживать.",
        '* For non-classic (formerly "non-built-in") services, you can choose which metrics to monitor.': "* Для неклассических (ранее «non-built-in») сервисов вы можете выбрать, какие метрики отслеживать.",
        "## Azure cloud services monitored by default": "## Облачные сервисы Azure, отслеживаемые по умолчанию",
        'As a result of [Azure monitoring integration](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Set up and configure Azure monitoring in Dynatrace."), some services are monitored out-of-the-box.': 'В результате [интеграции мониторинга Azure](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Настройка и конфигурирование мониторинга Azure в Dynatrace.") некоторые сервисы отслеживаются «из коробки».',
        "## Other Azure cloud services": "## Другие облачные сервисы Azure",
        "Apart from cloud services monitored by default, you can also monitor other Azure services that affect the performance of your Azure-hosted applications.": "Помимо облачных сервисов, отслеживаемых по умолчанию, вы также можете отслеживать другие сервисы Azure, влияющие на производительность ваших приложений, размещённых в Azure.",
        "## Cloud services with their respective Dynatrace entity types": "## Облачные сервисы и соответствующие им типы сущностей Dynatrace",
        "Not all cloud services have Dynatrace entities created for them and can have tags imported from the cloud. Expand the table below to see cloud services with their respective Dynatrace entity types and to check if they have tags imported from the cloud provider.": "Не для всех облачных сервисов создаются сущности Dynatrace и не для всех можно импортировать теги из облака. Разверните таблицу ниже, чтобы увидеть облачные сервисы и соответствующие им типы сущностей Dynatrace и проверить, импортируются ли для них теги от облачного провайдера.",
        "### List of Azure services with entities and tags": "### Список сервисов Azure с сущностями и тегами",
        "## Configuration API": "## Configuration API",
        "## Related topics": "## Связанные темы",
        'To list all Azure-supported services on your cluster by the current version, use the [Azure-supported services API](/managed/dynatrace-api/configuration-api/azure-supported-services "Fetch a list of Azure supported services via the Dynatrace API.").': 'Чтобы получить список всех поддерживаемых Azure сервисов на вашем кластере для текущей версии, используйте [API поддерживаемых сервисов Azure](/managed/dynatrace-api/configuration-api/azure-supported-services "Получение списка поддерживаемых Azure сервисов через Dynatrace API.").',
        "## Monitoring consumption": "## Потребление при мониторинге",
        "All cloud services consume DDUs. The amount of DDU consumption per service instance depends on the number of monitored metrics and their dimensions.": "Все облачные сервисы потребляют DDU. Объём потребления DDU на экземпляр сервиса зависит от количества отслеживаемых метрик и их измерений.",
        "* Each metric dimension results in the ingestion of 1 data point": "* Каждое измерение метрики приводит к приёму 1 точки данных",
        "* 1 data point consumes 0.001 DDUs": "* 1 точка данных потребляет 0,001 DDU",
        '* [Monitor Azure services with Azure Monitor metrics](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Set up and configure Azure monitoring in Dynatrace.")': '* [Мониторинг сервисов Azure с помощью метрик Azure Monitor](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Настройка и конфигурирование мониторинга Azure в Dynatrace.")',
    }
)

# image captions / pure-EN tokens that must stay EN (leftover-scan whitelist)
PASS_EN = set(e41.PASS_EN)
PASS_EN.update(
    {
        "Azure service metrics",
        "Clone hide azure",
        "Storage account dashboard",
        "Hdinsights azure",
        "Azure management zone",
        "Netapp",
        "Example",
        # intentional-EN Azure product/feature labels (sub-table group headers,
        # metric-namespace H2) - kept EN like the hub catalog + storage canon
        "**Azure Storage Blob Services**",
        "**Azure Storage File Services**",
        "**Azure Storage Queue Services**",
        "**Azure Storage Table Services**",
        "## Azure NetApp Files - Volumes",
        # MZ rule-condition bullet stays EN whole (canon: "* Service type: `Database`")
        "* Service technology: `Apache Hadoop Distributed File System`",
    }
)

warnings = []


def is_sep(cells):
    return all(set(c) <= set("-: ") for c in cells)


def split_cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def tr_row(cells, colmap, fname):
    out = []
    for i, cell in enumerate(cells):
        col = colmap[i] if i < len(colmap) else None
        if col == "Description":
            if cell and cell not in DESC_MAP:
                warnings.append("%s: untranslated DESC -> %r" % (fname, cell))
            out.append(DESC_MAP.get(cell, cell))
        elif col == "Unit":
            if cell and cell not in UNIT_MAP:
                warnings.append("%s: unmapped UNIT -> %r" % (fname, cell))
            out.append(UNIT_MAP.get(cell, cell))
        elif col and col.startswith("Recommended"):
            if cell and cell not in REC_MAP:
                warnings.append("%s: unmapped REC -> %r" % (fname, cell))
            out.append(REC_MAP.get(cell, cell))
        elif col in REC_COLS:
            if cell and cell not in REC_MAP:
                warnings.append("%s: unmapped TAG -> %r" % (fname, cell))
            out.append(REC_MAP.get(cell, cell))
        elif cell == "Applicable":  # broken/blank-header fallback (L4-IF.40)
            out.append(REC_MAP["Applicable"])
        else:  # Metric key / Name / Display name / Dimensions / Aggregations /
            # Monitoring consumption / Service / Cloud type / entity type -> EN
            out.append(cell)
    return "| " + " | ".join(out) + " |"


def tr_header(cells):
    return "| " + " | ".join(HEADER_LABEL.get(c, c) for c in cells) + " |"


def has_cyr(s):
    return any("Ѐ" <= ch <= "ӿ" for ch in s)


def leftover_scan(fname, ru_text):
    """Flag prose lines that stayed fully EN (>=4 alpha words, no Cyrillic),
    fence-aware, skipping links/cards/captions."""
    in_fence = False
    fmc = 0
    for n, line in enumerate(ru_text.split("\n"), 1):
        if line == "---" and fmc < 2:
            fmc += 1
            continue
        if fmc == 1:
            continue
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        s = line.strip()
        if not s or s.startswith("|") or s.startswith("![") or s.startswith("["):
            continue
        if s in PASS_EN:
            continue
        if has_cyr(s):
            continue
        words = [
            w
            for w in s.replace("*", " ").replace("`", " ").replace(">", " ").split()
            if w.isalpha() and len(w) >= 3
        ]
        if len(words) >= 4:
            warnings.append("%s: EN leftover L%d -> %r" % (fname, n, s[:90]))


def build_one(en_path, ru_path, title_key):
    en = open(en_path, encoding="utf-8").read().replace("\r\n", "\n")
    lines = en.split("\n")
    en_title, ru_title = TITLE_MAP[title_key]
    out_lines = []
    colmap = None
    in_fence = False
    for i, line in enumerate(lines):
        if line.strip().startswith("```"):
            in_fence = not in_fence
            out_lines.append(line)
            colmap = None
            continue
        if in_fence:
            out_lines.append(line)  # code: byte-identical
            continue
        if line.startswith("|"):
            cells = split_cells(line)
            if is_sep(cells):
                out_lines.append(line)
            elif (
                i + 1 < len(lines)
                and lines[i + 1].startswith("|")
                and is_sep(split_cells(lines[i + 1]))
            ):
                colmap = cells  # header row -> map columns by EN name
                out_lines.append(tr_header(cells))
            elif colmap is not None:
                out_lines.append(tr_row(cells, colmap, os.path.basename(en_path)))
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
    os.makedirs(os.path.dirname(ru_path), exist_ok=True)
    with open(ru_path, "wb") as f:
        f.write(result.encode("utf-8"))
    leftover_scan(os.path.basename(en_path), result)
    return en, result


def main():
    jobs = [(os.path.join(LEAF_EN, f), os.path.join(LEAF_RU, f), f) for f in BATCH]
    jobs.append((HUB_EN, HUB_RU, HUB_EN))
    ok = 0
    for en_path, ru_path, key in jobs:
        en, ru = build_one(en_path, ru_path, key)
        en_n, ru_n = en.count("\n"), ru.count("\n")
        name = os.path.basename(en_path)
        status = "OK" if en_n == ru_n else "LINE MISMATCH %d!=%d" % (en_n, ru_n)
        if en_n == ru_n:
            ok += 1
        print("%-18s  %s (%d lines)" % (status, name, ru_n + 1))
    print("\nline-parity OK: %d/%d" % (ok, len(jobs)))
    if warnings:
        print("\n=== WARNINGS (%d) ===" % len(warnings))
        for w in warnings:
            print("  ", w)
    else:
        print("no warnings")


if __name__ == "__main__":
    main()
