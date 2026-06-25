---
title: Миграция с классических (ранее «встроенных») сервисов Azure на облачные сервисы
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide
scraped: 2026-05-12T11:26:11.179951
---

# Миграция с классических (ранее «встроенных») сервисов Azure на облачные сервисы

# Миграция с классических (ранее «встроенных») сервисов Azure на облачные сервисы

* Практическое руководство
* Чтение: 15 мин
* Обновлено 27 июня 2024 г.

На странице обзора Azure доступны классические сервисы Dynatrace и облачные сервисы для мониторинга Azure. Оба типа сервисов используют одни и те же ресурсы Azure. Однако классические сервисы применяют предопределённый набор метрик, поэтому настройка отслеживаемых метрик и определение уже отслеживаемых не поддерживаются.

## Классические сервисы и облачные сервисы

Как упоминалось выше, классические сервисы и облачные сервисы используют одни и те же ресурсы Azure. Однако облачные сервисы поддерживают более широкий спектр параметров конфигурации: новые метрики и настраиваемые отслеживаемые метрики. Для расширения возможностей настройки предпринят ряд шагов:

* Добавление новых сервисов в раздел **Cloud services** для настройки отслеживаемых метрик и измерений.
* Добавление новых метрик для облачных сервисов: они не только настраиваемые, но и охватывают значительно больше данных, чем прежде.
* Замена классических сервисов облачными с расширенными параметрами конфигурации метрик и измерений.

![public-cloud-services-section-infographic](https://dt-cdn.net/images/public-cloud-services-section-infographic-950-ccb7323d99.png)

public-cloud-services-section-infographic

При использовании классических сервисов рекомендуется выполнить миграцию на облачные сервисы, чтобы воспользоваться расширенными возможностями настройки.

## Влияние миграции

Хотя классические и облачные сервисы отслеживают одни и те же ресурсы Azure со стороны Dynatrace, они мониторятся как два разных объекта.

* У них разные идентификаторы объектов и ключи метрик.
* Данные для каждого типа объектов Dynatrace собираются и хранятся отдельно.
* ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Предупреждение") Критическое изменение: необходимо адаптировать конфигурацию дашбордов, оповещений и зон управления на основе идентификатора объекта или [ключей метрик с типом отслеживаемого сервиса](#metrics).

На данный момент можно выбрать классический или облачный сервис для сохранения исторических данных. При этом необходимо учитывать следующее:

* Исторические данные хранятся на классических сервисах. При обратном переключении в данных мониторинга будут пробелы за период, когда ресурсы отслеживались через облачный сервис.
* Нельзя включить оба варианта одновременно. Хотя на стороне Dynatrace они являются двумя разными сервисами, устаревшая и новая версии отслеживают один и тот же ресурс Azure. При одновременном включении двух версий оплата будет взиматься дважды за опрос одних и тех же данных.
* При включении новой версии классическая отключается автоматически, и наоборот.
* Между объектами, содержащими исторические и новые данные, нет прямой связи.
* Журналы из [Azure log forwarder](/managed/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure "Использование log forwarding Azure для приёма журналов Azure.") по-прежнему привязаны к историческим данным и объектам.

Для мониторинга облачных сервисов необходимо настроить [Environment ActiveGate](https://dt-url.net/sc0396g).

## Изменения в пользовательском интерфейсе

Страница обзора Azure изменяется после настройки новой версии сервиса.

Рассмотрим пример с **Azure Storage Account**.

* Если настроен устаревший сервис **Azure Storage Accounts**, раздел **Storage accounts** на странице обзора Azure выглядит следующим образом.

![azure-public-cloud-vct-dev1-storage](https://dt-cdn.net/images/azure-public-cloud-vct-dev1-storage-1449-46980fd72d.png)

azure-public-cloud-vct-dev1-storage

* Выберите **Cloud services**, чтобы открыть новые страницы обзора сервисов.

![azure-public-cloud-vct-dev1-services](https://dt-cdn.net/images/azure-public-cloud-vct-dev1-services-1112-707a41c03e.png)

azure-public-cloud-vct-dev1-services

* После настройки сервисов **Azure Storage Account**, **Azure Storage Blob**, **Azure Storage File**, **Azure Storage Queue** и **Azure Storage Table** раздел **Storage accounts** на странице обзора Azure выглядит следующим образом.

![azure-public-cloud-vct-dev1-storage](https://dt-cdn.net/images/azure-public-cloud-vct-dev1-storage-1452-a16425bb86.png)

azure-public-cloud-vct-dev1-storage

* Кроме того, метрики для облачных сервисов можно настраивать через пользовательский интерфейс.

![azure-settings-manage-services](https://dt-cdn.net/images/azure-settings-manage-services-1297-d00845930c.png)

azure-settings-manage-services

![azure-settings-storage-blob-services](https://dt-cdn.net/images/azure-settings-storage-blob-services-1311-5b78cf0ab1.png)

azure-settings-storage-blob-services

## Облачные сервисы и соответствующие им классические сервисы

| Новый облачный сервис | Старый классический сервис |
| --- | --- |
| [Azure API Management Service](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-api-management-service "Мониторинг Azure API Management Service и просмотр доступных метрик.") | [Azure API Management services (classic)](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-api-management-services-builtin "Мониторинг Azure API Management Services и просмотр доступных метрик.") Устарело |
| [Azure Application Gateway](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-application-gateway "Мониторинг Azure Application Gateway и просмотр доступных метрик.") | [Azure Application Gateway (classic)](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-app-gateways-builtin "Мониторинг Azure Application Gateways и просмотр доступных метрик.") |
| [Azure Basic Load Balancer](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-basic-load-balancer "Мониторинг Azure Basic Load Balancer и просмотр доступных метрик.") | [Azure Load Balancer (classic)](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-load-balancers-builtin "Мониторинг Azure Load Balancers и просмотр доступных метрик.") |
| [Azure Gateway Load Balancer](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-gateway-load-balancer "Мониторинг Azure Gateway Load Balancer и просмотр доступных метрик.") | [Azure Load Balancer (classic)](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-load-balancers-builtin "Мониторинг Azure Load Balancers и просмотр доступных метрик.") |
| [Azure Standard Load Balancer](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-standard-load-balancer "Мониторинг Azure Standard Load Balancer и просмотр доступных метрик.") | [Azure Load Balancer (classic)](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-load-balancers-builtin "Мониторинг Azure Load Balancers и просмотр доступных метрик.") |
| [Azure Cache for Redis](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-cache-for-redis "Мониторинг Azure Cache for Redis и просмотр доступных метрик.") | [Azure Redis (classic)](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-redis-cache-builtin "Мониторинг Azure Redis Cache и просмотр доступных метрик.") |
| [Azure Cosmos DB Account (GlobalDocumentDB)](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-cosmos-db-account-globaldocumentdb "Мониторинг Azure Cosmos DB Account (GlobalDocumentDB) и просмотр доступных метрик.") | [Azure Cosmos DB (classic)](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-cosmos-db-builtin "Мониторинг Azure Cosmos DB и просмотр доступных метрик.") |
| [Azure Cosmos DB Account (MongoDB)](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-cosmos-db-account-mongodb "Мониторинг Azure Cosmos DB Account (MongoDB) и просмотр доступных метрик.") | [Azure Cosmos DB (classic)](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-cosmos-db-builtin "Мониторинг Azure Cosmos DB и просмотр доступных метрик.") |
| [Azure IoT Hub](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-iot-hub "Мониторинг Azure IoT Hub и просмотр доступных метрик.") | [Azure IoT Hubs (classic)](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-iot-hub-builtin "Мониторинг Azure IoT Hub и просмотр доступных метрик.") |
| [Azure SQL Server](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-server "Мониторинг Azure SQL Server и просмотр доступных метрик.") | [Azure SQL (classic)](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-servers-builtin "Мониторинг Azure SQL Servers и просмотр доступных метрик.") |
| [Azure SQL Database (DTU)](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-database-dtu "Мониторинг Azure SQL Database (DTU) и просмотр доступных метрик.") | [Azure SQL (classic)](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-servers-builtin "Мониторинг Azure SQL Servers и просмотр доступных метрик.") |
| [Azure SQL Database (vCore)](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-database-vcore "Мониторинг Azure SQL Database (vCore) и просмотр доступных метрик.") | [Azure SQL (classic)](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-servers-builtin "Мониторинг Azure SQL Servers и просмотр доступных метрик.") |
| [Azure SQL elastic pool (DTU)](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-elastic-pool-dtu "Мониторинг Azure SQL elastic pool (DTU) и просмотр доступных метрик.") | [Azure SQL (classic)](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-servers-builtin "Мониторинг Azure SQL Servers и просмотр доступных метрик.") |
| [Azure SQL elastic pool (vCore)](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-elastic-pool-vcore "Мониторинг Azure SQL elastic pool (vCore) и просмотр доступных метрик.") | [Azure SQL (classic)](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-servers-builtin "Мониторинг Azure SQL Servers и просмотр доступных метрик.") |
| [Azure Storage Account](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account "Мониторинг Azure Storage Account и просмотр доступных метрик.") | [Azure Storage accounts (classic)](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account-builtin "Мониторинг Azure Storage Accounts и просмотр доступных метрик.") |
| [Azure Storage Blob Services](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account "Мониторинг Azure Storage Account и просмотр доступных метрик.") | [Azure Storage accounts (classic)](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account-builtin "Мониторинг Azure Storage Accounts и просмотр доступных метрик.") |
| [Azure Storage File Services](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account "Мониторинг Azure Storage Account и просмотр доступных метрик.") | [Azure Storage accounts (classic)](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account-builtin "Мониторинг Azure Storage Accounts и просмотр доступных метрик.") |
| [Azure Storage Queue Services](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account "Мониторинг Azure Storage Account и просмотр доступных метрик.") | [Azure Storage accounts (classic)](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account-builtin "Мониторинг Azure Storage Accounts и просмотр доступных метрик.") |
| [Azure Storage Table Services](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account "Мониторинг Azure Storage Account и просмотр доступных метрик.") | [Azure Storage accounts (classic)](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account-builtin "Мониторинг Azure Storage Accounts и просмотр доступных метрик.") |

## Миграция метрик

Ниже приведены таблицы с метриками классических сервисов и соответствующими им метриками облачных сервисов. Пустые ячейки означают отсутствие идентичной метрики.

### Azure API Management Service

| Название метрики классического сервиса | Ключ метрики классического сервиса | Название метрики облачного сервиса | Ключ метрики облачного сервиса |
| --- | --- | --- | --- |
| Failed requests | builtin:cloud.azure.apiMgmt.requests.failed | Requests | ext:cloud.azure.microsoft\_apimanagement.service.requests:filter(or(eq("Gateway response code", "400"), eq("Gateway response code category", "5xx"))) |
| Other requests | builtin:cloud.azure.apiMgmt.requests.other | Requests | ext:cloud.azure.microsoft\_apimanagement.service.requests:filter(and(ne("Gateway response code category", "1xx"), ne("Gateway response code category", "2xx"), ne("Gateway response code", "300"), ne("Gateway response code", "301"), ne("Gateway response code", "304"), ne("Gateway response code", "307"), ne("Gateway response code", "400"), ne("Gateway response code", "401"), ne("Gateway response code", "403"), ne("Gateway response code", "429"), ne("Gateway response code category", "5xx"))) |
| Successful requests | builtin:cloud.azure.apiMgmt.requests.successful | Requests | ext:cloud.azure.microsoft\_apimanagement.service.requests:filter(or(eq("Gateway response code category", "1xx"), eq("Gateway response code category", "2xx"), eq("Gateway response code", "300"), eq("Gateway response code", "301"), eq("Gateway response code", "304"), eq("Gateway response code", "307"))) |
| Total requests | builtin:cloud.azure.apiMgmt.requests.total | Requests | ext:cloud.azure.microsoft\_apimanagement.service.requests |
| Unauthorized requests | builtin:cloud.azure.apiMgmt.requests.unauth | Requests | ext:cloud.azure.microsoft\_apimanagement.service.requests:filter(or(eq("Gateway response code", "401"), eq("Gateway response code", "403"), eq("Gateway response code", "429"))) |
| Capacity | builtin:cloud.azure.apiMgmt.capacity | Capacity | ext:cloud.azure.microsoft\_apimanagement.service.capacity |
| Duration | builtin:cloud.azure.apiMgmt.duration | Overall duration of gateway requests | ext:cloud.azure.microsoft\_apimanagement.service.duration |

### Azure Application Gateway

| Название метрики классического сервиса | Ключ метрики классического сервиса | Название метрики облачного сервиса | Ключ метрики облачного сервиса |
| --- | --- | --- | --- |
| Healthy host count | builtin:cloud.azure.appGateway.backend.settings.pool.host.healthy | Healthy host count | ext:cloud.azure.microsoft\_network.applicationgateways.healthyhostcount |
| Unhealthy host count | builtin:cloud.azure.appGateway.backend.settings.pool.host.unhealthy | Unhealthy host count | ext:cloud.azure.microsoft\_network.applicationgateways.unhealthyhostcount |
| Requests failed | builtin:cloud.azure.appGateway.backend.settings.traffic.requests.failed | Failed requests | ext:cloud.azure.microsoft\_network.applicationgateways.failedrequests |
| Requests total | builtin:cloud.azure.appGateway.backend.settings.traffic.requests.total | Total requests | ext:cloud.azure.microsoft\_network.applicationgateways.totalrequests |
| Response status | builtin:cloud.azure.appGateway.http.status.response | Response status | ext:cloud.azure.microsoft\_network.applicationgateways.responsestatus |
| Current connections count | builtin:cloud.azure.appGateway.network.connections.count | Current connections | ext:cloud.azure.microsoft\_network.applicationgateways.currentconnections |
| Network throughput | builtin:cloud.azure.appGateway.network.throughput | Throughput | ext:cloud.azure.microsoft\_network.applicationgateways.throughput |

### Azure Load Balancers

| Название метрики классического сервиса | Ключ метрики классического сервиса | Название метрики облачного сервиса | Ключ метрики облачного сервиса |
| --- | --- | --- | --- |
| Load balancer DIP TCP availability | builtin:cloud.azure.loadbalancer.availability.dipTcp | Health probe status | ext:cloud.azure.microsoft\_network.loadbalancers.dipavailability:filter(eq("ProtocolType", "Tcp")) / 100 |
| Load balancer DIP UDP availability | builtin:cloud.azure.loadbalancer.availability.dipUdp | Health probe status | ext:cloud.azure.microsoft\_network.loadbalancers.dipavailability:filter(eq("ProtocolType", "Udp")) / 100 |
| Load Balancer VIP availability | builtin:cloud.azure.loadbalancer.availability.vip | Data path availability | ext:cloud.azure.microsoft\_network.loadbalancers.vipavailability / 100 |
| SNAT connections successful | builtin:cloud.azure.loadbalancer.snatConnection.est | SNAT connection count | ext:cloud.azure.microsoft\_network.loadbalancers.snatconnectioncount:filter(eq("ConnectionState" ,"Successful")) |
| SNAT connections pending | builtin:cloud.azure.loadbalancer.snatConnection.pending | SNAT connection count | ext:cloud.azure.microsoft\_network.loadbalancers.snatconnectioncount:filter(eq("ConnectionState" ,"Pending")) |
| SNAT connections failed | builtin:cloud.azure.loadbalancer.snatConnection.rej | SNAT connection count | ext:cloud.azure.microsoft\_network.loadbalancers.snatconnectioncount:filter(eq("ConnectionState" ,"Failed")) |
| Bytes received | builtin:cloud.azure.loadbalancer.traffic.byteIn | Byte count | ext:cloud.azure.microsoft\_network.loadbalancers.bytecount:filter(eq("Direction", "In")) |
| Bytes sent | builtin:cloud.azure.loadbalancer.traffic.byteOut | Byte count | ext:cloud.azure.microsoft\_network.loadbalancers.bytecount:filter(eq("Direction", "Out")) |
| Packets received | builtin:cloud.azure.loadbalancer.traffic.packetIn | Packet count | ext:cloud.azure.microsoft\_network.loadbalancers.packetcount:filter(eq("Direction", "In")) |
| Packets sent | builtin:cloud.azure.loadbalancer.traffic.packetOut | Packet count | ext:cloud.azure.microsoft\_network.loadbalancers.packetcount:filter(eq("Direction", "Out")) |
| SYN packets received | builtin:cloud.azure.loadbalancer.traffic.packetSynIn | SYN count | ext:cloud.azure.microsoft\_network.loadbalancers.syncount:filter(eq("Direction", "In")) |
| SYN packets sent | builtin:cloud.azure.loadbalancer.traffic.packetSynOut | SYN count | ext:cloud.azure.microsoft\_network.loadbalancers.syncount:filter(eq("Direction", "Out")) |

### Azure Cache for Redis

| Название метрики классического сервиса | Ключ метрики классического сервиса | Название метрики облачного сервиса | Ключ метрики облачного сервиса |
| --- | --- | --- | --- |
| Cache hits | builtin:cloud.azure.redis.cache.hits | Cache hits | ext:cloud.azure.microsoft\_cache.redis.cachehits |
| Cache misses | builtin:cloud.azure.redis.cache.misses | Cache misses | ext:cloud.azure.microsoft\_cache.redis.cachemisses |
| Read bytes/s | builtin:cloud.azure.redis.cache.read | Cache read | ext:cloud.azure.microsoft\_cache.redis.cacheread |
| Write bytes/s | builtin:cloud.azure.redis.cache.write | Cache write | ext:cloud.azure.microsoft\_cache.redis.cachewrite |
| Get commands | builtin:cloud.azure.redis.commands.get | Gets | ext:cloud.azure.microsoft\_cache.redis.getcommands |
| Set commands | builtin:cloud.azure.redis.commands.set | Sets | ext:cloud.azure.microsoft\_cache.redis.setcommands |
| Total no. of processed commands | builtin:cloud.azure.redis.commands.total | Total operations | ext:cloud.azure.microsoft\_cache.redis.totalcommandsprocessed |
| No. of evicted keys | builtin:cloud.azure.redis.keys.evicted | Evicted keys | ext:cloud.azure.microsoft\_cache.redis.evictedkeys |
| No. of expired keys | builtin:cloud.azure.redis.keys.expired | Expired keys | ext:cloud.azure.microsoft\_cache.redis.expiredkeys |
| Total no. of keys | builtin:cloud.azure.redis.keys.total | Total keys | ext:cloud.azure.microsoft\_cache.redis.totalkeys |
| Used memory | builtin:cloud.azure.redis.memory.used | Used memory | ext:cloud.azure.microsoft\_cache.redis.usedmemory |
| Used memory RSS | builtin:cloud.azure.redis.memory.usedRss | Used memory RSS | ext:cloud.azure.microsoft\_cache.redis.usedmemoryrss |
| Connected clients | builtin:cloud.azure.redis.connected | Connected clients | ext:cloud.azure.microsoft\_cache.redis.connectedclients |
| Server load | builtin:cloud.azure.redis.load | Server load | ext:cloud.azure.microsoft\_cache.redis.serverload |
| Processor time | builtin:cloud.azure.redis.processorTime | CPU | ext:cloud.azure.microsoft\_cache.redis.percentprocessortime |

### Azure Cosmos Database

| Название метрики классического сервиса | Ключ метрики классического сервиса | Название метрики облачного сервиса | Ключ метрики облачного сервиса |
| --- | --- | --- | --- |
| Available Storage | builtin:cloud.azure.cosmos.availableStorage | - | - |
| Data Usage | builtin:cloud.azure.cosmos.dataUsage | Data usage | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.datausage |
| Document Count | builtin:cloud.azure.cosmos.documentCount | Document count | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.documentcount |
| Document Quota | builtin:cloud.azure.cosmos.documentQuota | Document quota | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.documentquota |
| Index Usage | builtin:cloud.azure.cosmos.indexUsage | Index usage | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.indexusage |
| Metadata Requests | builtin:cloud.azure.cosmos.metadataRequests | Metadata requests | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.metadatarequests |
| Normalized request units consumption | builtin:cloud.azure.cosmos.normalizedRUConsumption | Normalized ru consumption | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.normalizedruconsumption |
| Provisioned Throughput | builtin:cloud.azure.cosmos.provisionedThroughput | Provisioned throughput | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.provisionedthroughput |
| Replication Latency | builtin:cloud.azure.cosmos.replicationLatency | P99 replication latency | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.replicationlatency |
| Total number of request units | builtin:cloud.azure.cosmos.requestUnits | Total request units | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.totalrequestunits |
| Total number of requests | builtin:cloud.azure.cosmos.requests | Total requests | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.totalrequests |
| Service Availability | builtin:cloud.azure.cosmos.serviceAvailability | Service availability | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.serviceavailability |

### Azure IoT Hub

| Название метрики классического сервиса | Ключ метрики классического сервиса | Название метрики облачного сервиса | Ключ метрики облачного сервиса |
| --- | --- | --- | --- |
| Commands abandoned | builtin:cloud.azure.iotHub.command.abandoned | C2D messages abandoned | ext:cloud.azure.microsoft\_devices.iothubs.c2d\_commands\_egress\_abandon\_success |
| Commands completed | builtin:cloud.azure.iotHub.command.completed | C2D message deliveries completed | ext:cloud.azure.microsoft\_devices.iothubs.c2d\_commands\_egress\_complete\_success |
| Commands rejected | builtin:cloud.azure.iotHub.command.rejected | C2D messages rejected | ext:cloud.azure.microsoft\_devices.iothubs.c2d\_commands\_egress\_reject\_success |
| Connected devices | builtin:cloud.azure.iotHub.device.connected | Connected devices | ext:cloud.azure.microsoft\_devices.iothubs.connecteddevicecount |
| Number of throttling errors | builtin:cloud.azure.iotHub.device.dailyThroughputThrottling | Number of throttling errors | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_telemetry\_ingress\_sendthrottle |
| Total device data usage | builtin:cloud.azure.iotHub.device.dataUsage | Total device data usage Total device data usage (preview) | ext:cloud.azure.microsoft\_devices.iothubs.devicedatausage ext:cloud.azure.microsoft\_devices.iothubs.devicedatausagev2 |
| Total devices | builtin:cloud.azure.iotHub.device.registered | Total devices | ext:cloud.azure.microsoft\_devices.iothubs.totaldevicecount |
| Messages delivered to the built-in endpoint (messages/events) | builtin:cloud.azure.iotHub.eventHub.builtInEventHub.messages.delivered | Routing - messages delivered to messages/events | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_egress\_builtin\_events |
| Message latency for the built-in endpoint (messages/events) | builtin:cloud.azure.iotHub.eventHub.builtInEventHub.averageLatencyMs | Routing - message latency for messages/events | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_latency\_builtin\_events |
| Messages delivered to Event Hub endpoints | builtin:cloud.azure.iotHub.eventHub.messages.delivered | Routing - messages delivered to event hub | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_egress\_eventhubs |
| Message latency for event hub endpoints | builtin:cloud.azure.iotHub.eventHub.averageLatencyMs | Routing - message latency for event hub | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_latency\_eventhubs |
| Dropped messages | builtin:cloud.azure.iotHub.messages.dropped | Routing - telemetry messages dropped | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_telemetry\_egress\_dropped |
| Invalid messages | builtin:cloud.azure.iotHub.messages.invalidForAllEndpoints | Routing - telemetry messages incompatible | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_telemetry\_egress\_invalid |
| Orphaned messages | builtin:cloud.azure.iotHub.messages.orphaned | Routing - telemetry messages orphaned | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_telemetry\_egress\_orphaned |
| Telemetry message send attempts | builtin:cloud.azure.iotHub.messages.sendAttempts | Telemetry message send attempts | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_telemetry\_ingress\_allprotocol |
| Telemetry messages sent | builtin:cloud.azure.iotHub.messages.sent | Telemetry messages sent | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_telemetry\_ingress\_success |
| Messages matching fallback condition | builtin:cloud.azure.iotHub.messages.sentToFallback | Routing - messages delivered to fallback | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_telemetry\_egress\_fallback |
| Message latency for service bus queue endpoints | builtin:cloud.azure.iotHub.serviceBus.queues.averageLatencyMs | Routing - message latency for service bus queue | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_latency\_servicebusqueues |
| Messages delivered to service bus queue endpoints | builtin:cloud.azure.iotHub.serviceBus.queues.messagesDelivered | Routing - messages delivered to service bus queue | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_egress\_servicebusqueues |
| Message latency for service bus topic endpoints | builtin:cloud.azure.iotHub.serviceBus.topics.averageLatencyMs | Routing - message latency for service bus topic | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_latency\_servicebustopics |
| Messages delivered to service bus topic endpoints | builtin:cloud.azure.iotHub.serviceBus.topics.messagesDelivered | Routing - messages delivered to service bus topic | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_egress\_servicebustopics |
| Message latency for storage endpoints | builtin:cloud.azure.iotHub.storageEndpoints.avgLatencyMs | Routing - message latency for storage | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_latency\_storage |
| Blobs written to storage | builtin:cloud.azure.iotHub.storageEndpoints.blobsWritten | Routing - blobs delivered to storage | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_egress\_storage\_blobs |
| Data written to storage | builtin:cloud.azure.iotHub.storageEndpoints.bytesWritten | Routing - data delivered to storage | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_egress\_storage\_bytes |
| Messages delivered to storage endpoints | builtin:cloud.azure.iotHub.storageEndpoints.messageDelivered | Routing - messages delivered to storage | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_egress\_storage |

### Azure SQL Server

#### Azure SQL Databases

| Название метрики классического сервиса | Ключ метрики классического сервиса | Название метрики облачного сервиса | Метрика облачного сервиса |
| --- | --- | --- | --- |
| Blocked by firewall | builtin:cloud.azure.sqlDatabase.connections.blockedByFirewall | Blocked by firewall | ext:cloud.azure.microsoft\_sql.servers.databases.blocked\_by\_firewall |
| Failed connections | builtin:cloud.azure.sqlDatabase.connections.failed | Failed connections - system errors Failed connections - user errors | ext:cloud.azure.microsoft\_sql.servers.databases.connection\_failed ext:cloud.azure.microsoft\_sql.servers.databases.connection\_failed\_user\_error |
| Successful connections | builtin:cloud.azure.sqlDatabase.connections.successful | Successful connections | ext:cloud.azure.microsoft\_sql.servers.databases.connection\_successful |
| DTU limit | builtin:cloud.azure.sqlDatabase.dtu.limit.count | DTU limit | ext:cloud.azure.microsoft\_sql.servers.databases.dtu\_limit |
| DTU used | builtin:cloud.azure.sqlDatabase.dtu.limit.used | DTU used | ext:cloud.azure.microsoft\_sql.servers.databases.dtu\_used |
| DTU percentage | builtin:cloud.azure.sqlDatabase.dtu.consumptionPerc | DTU percentage | ext:cloud.azure.microsoft\_sql.servers.databases.dtu\_consumption\_percent |
| Data I/O percentage | builtin:cloud.azure.sqlDatabase.io.dataRead | Data IO percentage | ext:cloud.azure.microsoft\_sql.servers.databases.physical\_data\_read\_percent |
| Log I/O percentage | builtin:cloud.azure.sqlDatabase.io.logWrite | Log IO percentage | ext:cloud.azure.microsoft\_sql.servers.databases.log\_write\_percent |
| Database size percentage | builtin:cloud.azure.sqlDatabase.storage.percent | Data space used percent | ext:cloud.azure.microsoft\_sql.servers.databases.storage\_percent |
| Total database size | builtin:cloud.azure.sqlDatabase.storage.totalBytes | Data space used | ext:cloud.azure.microsoft\_sql.servers.databases.storage |
| In-Memory OLTP storage percent | builtin:cloud.azure.sqlDatabase.storage.xtpPercent | ext:cloud.azure.microsoft\_sql.servers.databases.xtp\_storage\_percent | ext:cloud.azure.microsoft\_sql.servers.databases.xtp\_storage\_percent |
| CPU percentage | builtin:cloud.azure.sqlDatabase.cpuPercent | CPU percentage | ext:cloud.azure.microsoft\_sql.servers.databases.cpu\_percent |
| Deadlocks | builtin:cloud.azure.sqlDatabase.deadlocks | Deadlocks | ext:cloud.azure.microsoft\_sql.servers.databases.deadlock |
| Sessions percentage | builtin:cloud.azure.sqlDatabase.sessions | Sessions percentage | ext:cloud.azure.microsoft\_sql.servers.databases.sessions\_percent |
| Workers percentage | builtin:cloud.azure.sqlDatabase.workers | Workers percentage | ext:cloud.azure.microsoft\_sql.servers.databases.workers\_percent |

#### Azure SQL Database elastic pools

| Название метрики классического сервиса | Ключ метрики классического сервиса | Название метрики облачного сервиса | Ключ метрики облачного сервиса |
| --- | --- | --- | --- |
| Storage limit | builtin:cloud.azure.sqlElasticPool.dtu.storage.limitBytes | Data max size | ext:cloud.azure.microsoft\_sql.servers.elasticpools.storage\_limit |
| Database size percentage | builtin:cloud.azure.sqlElasticPool.dtu.storage.percent | Data space used percent | ext:cloud.azure.microsoft\_sql.servers.elasticpools.storage\_percent |
| Storage used | builtin:cloud.azure.sqlElasticPool.dtu.storage.usedBytes | Data space used | ext:cloud.azure.microsoft\_sql.servers.elasticpools.storage\_used |
| In-memory OLTP storage percent | builtin:cloud.azure.sqlElasticPool.dtu.storage.xtpPercent | In - memory OLTP storage percent | ext:cloud.azure.microsoft\_sql.servers.elasticpools.xtp\_storage\_percent |
| DTU percentage | builtin:cloud.azure.sqlElasticPool.dtu.consumption | DTU percentage | ext:cloud.azure.microsoft\_sql.servers.elasticpools.dtu\_consumption\_percent |
| eDTU limit | builtin:cloud.azure.sqlElasticPool.edtu.limit | EDTU limit | ext:cloud.azure.microsoft\_sql.servers.elasticpools.edtu\_limit |
| eDTU used | builtin:cloud.azure.sqlElasticPool.edtu.used | EDTU used | ext:cloud.azure.microsoft\_sql.servers.elasticpools.edtu\_used |
| Data I/O percentage | builtin:cloud.azure.sqlElasticPool.io.dataRead | Data IO percentage | ext:cloud.azure.microsoft\_sql.servers.elasticpools.physical\_data\_read\_percent |
| Log I/O percentage | builtin:cloud.azure.sqlElasticPool.io.logWrite | Log IO percentage | ext:cloud.azure.microsoft\_sql.servers.elasticpools.log\_write\_percent |
| CPU percentage | builtin:cloud.azure.sqlElasticPool.cpuPercent | CPU percentage | ext:cloud.azure.microsoft\_sql.servers.elasticpools.cpu\_percent |
| Sessions percentage | builtin:cloud.azure.sqlElasticPool.sessions | Sessions percentage | ext:cloud.azure.microsoft\_sql.servers.elasticpools.sessions\_percent |
| Workers percentage | builtin:cloud.azure.sqlElasticPool.workers | Workers percentage | ext:cloud.azure.microsoft\_sql.servers.elasticpools.workers\_percent |

### Azure Storage Account

| Название метрики классического сервиса | Ключ метрики классического сервиса | Название метрики облачного сервиса | Ключ метрики облачного сервиса |
| --- | --- | --- | --- |
| Transactions count | builtin:cloud.azure.storage.blob.transactions | Transactions | ext:cloud.azure.microsoft\_storage.storageaccounts.blobservices.transactions |
| E2E success latency | builtin:cloud.azure.storage.blob.transactions.network.latency.success.e2e | Success E2E latency | ext:cloud.azure.microsoft\_storage.storageaccounts.blobservices.transactions |
| Server success latency | builtin:cloud.azure.storage.blob.transactions.network.latency.success.server | Success server latency | ext:cloud.azure.microsoft\_storage.storageaccounts.blobservices.successserverlatency |
| Egress bytes | builtin:cloud.azure.storage.blob.transactions.network.egress | Egress | ext:cloud.azure.microsoft\_storage.storageaccounts.blobservices.egress |
| Ingress bytes | builtin:cloud.azure.storage.blob.transactions.network.ingress | Ingress | ext:cloud.azure.microsoft\_storage.storageaccounts.blobservices.ingress |
| Blob capacity | builtin:cloud.azure.storage.blob.capacity | Blob capacity | ext:cloud.azure.microsoft\_storage.storageaccounts.blobservices.blobcapacity |
| Blob container count | builtin:cloud.azure.storage.blob.containers | Blob container count | ext:cloud.azure.microsoft\_storage.storageaccounts.blobservices.containercount |
| Blob count | builtin:cloud.azure.storage.blob.entities | Blob count | ext:cloud.azure.microsoft\_storage.storageaccounts.blobservices.blobcount |
| Transactions count | builtin:cloud.azure.storage.file.transactions | Transactions | ext:cloud.azure.microsoft\_storage.storageaccounts.fileservices.transactions |
| E2E success latency | builtin:cloud.azure.storage.file.transactions.network.latency.success.e2e | Success E2E latency | ext:cloud.azure.microsoft\_storage.storageaccounts.fileservices.successe2elatency |
| Server success latency | builtin:cloud.azure.storage.file.transactions.network.latency.success.server | Success server latency | ext:cloud.azure.microsoft\_storage.storageaccounts.fileservices.successserverlatency |
| Egress bytes | builtin:cloud.azure.storage.file.transactions.network.egress | Egress | ext:cloud.azure.microsoft\_storage.storageaccounts.fileservices.egress |
| Ingress bytes | builtin:cloud.azure.storage.file.transactions.network.ingress | Ingress | ext:cloud.azure.microsoft\_storage.storageaccounts.fileservices.ingress |
| File capacity | builtin:cloud.azure.storage.file.capacity | File capacity | ext:cloud.azure.microsoft\_storage.storageaccounts.fileservices.filecapacity |
| File share count | builtin:cloud.azure.storage.file.containers | File share count | ext:cloud.azure.microsoft\_storage.storageaccounts.fileservices.filesharecount |
| File count | builtin:cloud.azure.storage.file.entities | File count | ext:cloud.azure.microsoft\_storage.storageaccounts.fileservices.filecount |
| Transactions count | builtin:cloud.azure.storage.queue.transactions | Transactions | ext:cloud.azure.microsoft\_storage.storageaccounts.queueservices.transactions |
| E2E success latency | builtin:cloud.azure.storage.queue.transactions.network.latency.success.e2e | Success E2E latency | ext:cloud.azure.microsoft\_storage.storageaccounts.queueservices.successe2elatency |
| Server success latency | builtin:cloud.azure.storage.queue.transactions.network.latency.success.server | Success server latency | ext:cloud.azure.microsoft\_storage.storageaccounts.queueservices.successserverlatency |
| Egress bytes | builtin:cloud.azure.storage.queue.transactions.network.egress | Egress | ext:cloud.azure.microsoft\_storage.storageaccounts.queueservices.egress |
| Ingress bytes | builtin:cloud.azure.storage.queue.transactions.network.ingress | Ingress | ext:cloud.azure.microsoft\_storage.storageaccounts.queueservices.ingress |
| Queue capacity | builtin:cloud.azure.storage.queue.capacity | Queue capacity | ext:cloud.azure.microsoft\_storage.storageaccounts.queueservices.queuecapacity |
| Queue count | builtin:cloud.azure.storage.queue.containers | Queue count | ext:cloud.azure.microsoft\_storage.storageaccounts.queueservices.queuecount |
| Queue message count | builtin:cloud.azure.storage.queue.entities | Queue message count | ext:cloud.azure.microsoft\_storage.storageaccounts.queueservices.queuemessagecount |
| Transactions count | builtin:cloud.azure.storage.table.transactions | Transactions | ext:cloud.azure.microsoft\_storage.storageaccounts.tableservices.transactions |
| Server success latency | builtin:cloud.azure.storage.table.transactions.network.latency.success.server | Success server latency | ext:cloud.azure.microsoft\_storage.storageaccounts.tableservices.successserverlatency |
| E2E success latency | builtin:cloud.azure.storage.table.transactions.network.latency.success.server.e2e | Success E2E latency | ext:cloud.azure.microsoft\_storage.storageaccounts.tableservices.successe2elatency |
| Egress bytes | builtin:cloud.azure.storage.table.transactions.network.egress | Egress | ext:cloud.azure.microsoft\_storage.storageaccounts.tableservices.egress |
| Ingress bytes | builtin:cloud.azure.storage.table.transactions.network.ingress | Ingress | ext:cloud.azure.microsoft\_storage.storageaccounts.tableservices.ingress |
| Table capacity | builtin:cloud.azure.storage.table.capacity | Table capacity | ext:cloud.azure.microsoft\_storage.storageaccounts.tableservices.tablecapacity |
| Table count | builtin:cloud.azure.storage.table.containers | Table count | ext:cloud.azure.microsoft\_storage.storageaccounts.tableservices.tablecount |
| Table entity count | builtin:cloud.azure.storage.table.entities | Table entity count | ext:cloud.azure.microsoft\_storage.storageaccounts.tableservices.tableentitycount |