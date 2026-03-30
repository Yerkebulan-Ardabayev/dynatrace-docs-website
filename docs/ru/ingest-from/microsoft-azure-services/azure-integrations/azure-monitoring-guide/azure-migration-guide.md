---
title: Миграция с классических сервисов Azure (ранее «встроенных») на облачные сервисы
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide
scraped: 2026-03-06T21:33:24.151283
---

* 15 минут чтения

На странице обзора Azure вы можете получить доступ к классическим сервисам Dynatrace и облачным сервисам для мониторинга Azure. Оба типа сервисов используют одни и те же ресурсы Azure. Однако классические сервисы используют предопределённый набор метрик, поэтому настройка отслеживаемых метрик или определение уже отслеживаемых не поддерживается.

## Классические сервисы против облачных сервисов

Как уже упоминалось, классические сервисы и облачные сервисы используют одни и те же ресурсы Azure. Однако облачные сервисы поддерживают более широкий спектр параметров конфигурации, таких как новые метрики и настраиваемые отслеживаемые метрики. Чтобы предоставить вам больше возможностей настройки, мы начали следующее:

* Добавление дополнительных сервисов в раздел **Облачные сервисы**, чтобы вы могли настраивать, какие метрики и измерения хотите отслеживать.
* Добавление дополнительных метрик для облачных сервисов; теперь они не только настраиваемые, но и позволяют отслеживать значительно больше, чем раньше.
* Замена классических сервисов облачными с расширенными параметрами конфигурации для метрик и измерений.

![public-cloud-services-section-infographic](https://dt-cdn.net/images/public-cloud-services-section-infographic-950-ccb7323d99.png)

Если вы используете классические сервисы, мы рекомендуем мигрировать на облачные сервисы, чтобы воспользоваться расширенным набором настраиваемых параметров конфигурации.

## Влияние миграции

Несмотря на то что классические и облачные сервисы отслеживают одни и те же ресурсы Azure на стороне Dynatrace, они отслеживаются как две разные сущности.

* У них разные идентификаторы сущностей и ключи метрик.
* Данные для каждого типа сущности Dynatrace собираются и хранятся отдельно.
* ![Предупреждение](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Предупреждение") Критическое изменение. Вам необходимо адаптировать конфигурацию дашбордов, оповещений и Management Zone на основе идентификатора сущности или [ключей метрик с типом отслеживаемого сервиса](#metrics).

У вас есть возможность выбрать классический или облачный сервис для сохранения исторических данных на данный момент. Однако следует учитывать следующее:

* Исторические данные хранятся в классических сервисах. Если вы переключитесь обратно, в отслеживаемых данных будут пробелы за период, когда ресурсы отслеживались через облачный сервис.
* Вы не можете включить оба варианта одновременно. Несмотря на то что на стороне Dynatrace это два разных сервиса, устаревшая и новая версии отслеживают один и тот же ресурс Azure. Если бы обе версии были включены одновременно, вам пришлось бы платить двойную цену за опрос одних и тех же данных дважды.
* При включении новой версии классическая версия отключается автоматически, и наоборот.
* Прямой связи между сущностями, содержащими исторические и новые данные, нет.
* Логи от инструмента перенаправления логов Azure по-прежнему связаны с историческими данными и сущностями.

Для мониторинга облачных сервисов необходимо настроить [Environment ActiveGate](https://dt-url.net/sc0396g).

## Изменения в пользовательском интерфейсе

Страница обзора Azure изменяется после настройки новой версии сервиса.

Например, рассмотрим **Учётную запись хранения Azure**.

* Если настроен устаревший сервис **Учётные записи хранения Azure**, раздел **Учётные записи хранения** на обзорной странице Azure выглядит следующим образом.

![azure-public-cloud-vct-dev1-storage](https://dt-cdn.net/images/azure-public-cloud-vct-dev1-storage-1449-46980fd72d.png)

* Выберите **Облачные сервисы**, чтобы найти новые обзорные страницы сервисов.

![azure-public-cloud-vct-dev1-services](https://dt-cdn.net/images/azure-public-cloud-vct-dev1-services-1112-707a41c03e.png)

* После настройки сервисов **Учётная запись хранения Azure**, **BLOB-объекты хранилища Azure**, **Файлы хранилища Azure**, **Очереди хранилища Azure** и **Таблицы хранилища Azure** раздел **Учётные записи хранения** на обзорной странице Azure выглядит следующим образом.

![azure-public-cloud-vct-dev1-storage](https://dt-cdn.net/images/azure-public-cloud-vct-dev1-storage-1452-a16425bb86.png)

* Кроме того, вы можете настраивать метрики для облачных сервисов через пользовательский интерфейс.

![azure-settings-manage-services](https://dt-cdn.net/images/azure-settings-manage-services-1297-d00845930c.png)

![azure-settings-storage-blob-services](https://dt-cdn.net/images/azure-settings-storage-blob-services-1311-5b78cf0ab1.png)

## Облачные сервисы и соответствующие им классические сервисы

| Новый облачный сервис | Старый классический сервис |
| --- | --- |
| Служба управления API Azure | Службы управления API Azure (классические) Устаревший |
| Шлюз приложений Azure | Шлюз приложений Azure (классический) |
| Базовый балансировщик нагрузки Azure | Балансировщик нагрузки Azure (классический) |
| Шлюзовой балансировщик нагрузки Azure | Балансировщик нагрузки Azure (классический) |
| Стандартный балансировщик нагрузки Azure | Балансировщик нагрузки Azure (классический) |
| Кэш Azure для Redis | Azure Redis (классический) |
| Учётная запись Azure Cosmos DB (GlobalDocumentDB) и просмотр доступных метрик.") | Azure Cosmos DB (классическая) |
| Учётная запись Azure Cosmos DB (MongoDB) и просмотр доступных метрик.") | Azure Cosmos DB (классическая) |
| Azure IoT Hub | Azure IoT Hubs (классические) |
| SQL Server Azure | SQL Azure (классический) |
| База данных SQL Azure (DTU) и просмотр доступных метрик.") | SQL Azure (классический) |
| База данных SQL Azure (vCore) и просмотр доступных метрик.") | SQL Azure (классический) |
| Эластичный пул SQL Azure (DTU) и просмотр доступных метрик.") | SQL Azure (классический) |
| Эластичный пул SQL Azure (vCore) и просмотр доступных метрик.") | SQL Azure (классический) |
| Учётная запись хранения Azure | Учётные записи хранения Azure (классические) |
| Служба BLOB-объектов хранилища Azure | Учётные записи хранения Azure (классические) |
| Файловая служба хранилища Azure | Учётные записи хранения Azure (классические) |
| Служба очередей хранилища Azure | Учётные записи хранения Azure (классические) |
| Служба таблиц хранилища Azure | Учётные записи хранения Azure (классические) |

## Миграция метрик

Ниже представлены таблицы с метриками классических сервисов и соответствующими им метриками облачных сервисов. Пустые ячейки указывают на отсутствие идентичной соответствующей метрики.

### Служба управления API Azure

| Название метрики классического сервиса | Ключ метрики классического сервиса | Название метрики облачного сервиса | Ключ метрики облачного сервиса |
| --- | --- | --- | --- |
| Неудачные запросы | builtin:cloud.azure.apiMgmt.requests.failed | Запросы | ext:cloud.azure.microsoft\_apimanagement.service.requests:filter(or(eq("Gateway response code", "400"), eq("Gateway response code category", "5xx"))) |
| Прочие запросы | builtin:cloud.azure.apiMgmt.requests.other | Запросы | ext:cloud.azure.microsoft\_apimanagement.service.requests:filter(and(ne("Gateway response code category", "1xx"), ne("Gateway response code category", "2xx"), ne("Gateway response code", "300"), ne("Gateway response code", "301"), ne("Gateway response code", "304"), ne("Gateway response code", "307"), ne("Gateway response code", "400"), ne("Gateway response code", "401"), ne("Gateway response code", "403"), ne("Gateway response code", "429"), ne("Gateway response code category", "5xx"))) |
| Успешные запросы | builtin:cloud.azure.apiMgmt.requests.successful | Запросы | ext:cloud.azure.microsoft\_apimanagement.service.requests:filter(or(eq("Gateway response code category", "1xx"), eq("Gateway response code category", "2xx"), eq("Gateway response code", "300"), eq("Gateway response code", "301"), eq("Gateway response code", "304"), eq("Gateway response code", "307"))) |
| Всего запросов | builtin:cloud.azure.apiMgmt.requests.total | Запросы | ext:cloud.azure.microsoft\_apimanagement.service.requests |
| Несанкционированные запросы | builtin:cloud.azure.apiMgmt.requests.unauth | Запросы | ext:cloud.azure.microsoft\_apimanagement.service.requests:filter(or(eq("Gateway response code", "401"), eq("Gateway response code", "403"), eq("Gateway response code", "429"))) |
| Ёмкость | builtin:cloud.azure.apiMgmt.capacity | Ёмкость | ext:cloud.azure.microsoft\_apimanagement.service.capacity |
| Длительность | builtin:cloud.azure.apiMgmt.duration | Общая длительность запросов шлюза | ext:cloud.azure.microsoft\_apimanagement.service.duration |

### Шлюз приложений Azure

| Название метрики классического сервиса | Ключ метрики классического сервиса | Название метрики облачного сервиса | Ключ метрики облачного сервиса |
| --- | --- | --- | --- |
| Количество работоспособных узлов | builtin:cloud.azure.appGateway.backend.settings.pool.host.healthy | Количество работоспособных узлов | ext:cloud.azure.microsoft\_network.applicationgateways.healthyhostcount |
| Количество неработоспособных узлов | builtin:cloud.azure.appGateway.backend.settings.pool.host.unhealthy | Количество неработоспособных узлов | ext:cloud.azure.microsoft\_network.applicationgateways.unhealthyhostcount |
| Неудачные запросы | builtin:cloud.azure.appGateway.backend.settings.traffic.requests.failed | Неудачные запросы | ext:cloud.azure.microsoft\_network.applicationgateways.failedrequests |
| Всего запросов | builtin:cloud.azure.appGateway.backend.settings.traffic.requests.total | Всего запросов | ext:cloud.azure.microsoft\_network.applicationgateways.totalrequests |
| Статус ответа | builtin:cloud.azure.appGateway.http.status.response | Статус ответа | ext:cloud.azure.microsoft\_network.applicationgateways.responsestatus |
| Количество текущих соединений | builtin:cloud.azure.appGateway.network.connections.count | Текущие соединения | ext:cloud.azure.microsoft\_network.applicationgateways.currentconnections |
| Пропускная способность сети | builtin:cloud.azure.appGateway.network.throughput | Пропускная способность | ext:cloud.azure.microsoft\_network.applicationgateways.throughput |

### Балансировщики нагрузки Azure

| Название метрики классического сервиса | Ключ метрики классического сервиса | Название метрики облачного сервиса | Ключ метрики облачного сервиса |
| --- | --- | --- | --- |
| Доступность TCP для DIP балансировщика нагрузки | builtin:cloud.azure.loadbalancer.availability.dipTcp | Статус проверки работоспособности | ext:cloud.azure.microsoft\_network.loadbalancers.dipavailability:filter(eq("ProtocolType", "Tcp")) / 100 |
| Доступность UDP для DIP балансировщика нагрузки | builtin:cloud.azure.loadbalancer.availability.dipUdp | Статус проверки работоспособности | ext:cloud.azure.microsoft\_network.loadbalancers.dipavailability:filter(eq("ProtocolType", "Udp")) / 100 |
| Доступность VIP балансировщика нагрузки | builtin:cloud.azure.loadbalancer.availability.vip | Доступность пути данных | ext:cloud.azure.microsoft\_network.loadbalancers.vipavailability / 100 |
| Успешные соединения SNAT | builtin:cloud.azure.loadbalancer.snatConnection.est | Количество соединений SNAT | ext:cloud.azure.microsoft\_network.loadbalancers.snatconnectioncount:filter(eq("ConnectionState" ,"Successful")) |
| Ожидающие соединения SNAT | builtin:cloud.azure.loadbalancer.snatConnection.pending | Количество соединений SNAT | ext:cloud.azure.microsoft\_network.loadbalancers.snatconnectioncount:filter(eq("ConnectionState" ,"Pending")) |
| Неудачные соединения SNAT | builtin:cloud.azure.loadbalancer.snatConnection.rej | Количество соединений SNAT | ext:cloud.azure.microsoft\_network.loadbalancers.snatconnectioncount:filter(eq("ConnectionState" ,"Failed")) |
| Полученные байты | builtin:cloud.azure.loadbalancer.traffic.byteIn | Количество байт | ext:cloud.azure.microsoft\_network.loadbalancers.bytecount:filter(eq("Direction", "In")) |
| Отправленные байты | builtin:cloud.azure.loadbalancer.traffic.byteOut | Количество байт | ext:cloud.azure.microsoft\_network.loadbalancers.bytecount:filter(eq("Direction", "Out")) |
| Полученные пакеты | builtin:cloud.azure.loadbalancer.traffic.packetIn | Количество пакетов | ext:cloud.azure.microsoft\_network.loadbalancers.packetcount:filter(eq("Direction", "In")) |
| Отправленные пакеты | builtin:cloud.azure.loadbalancer.traffic.packetOut | Количество пакетов | ext:cloud.azure.microsoft\_network.loadbalancers.packetcount:filter(eq("Direction", "Out")) |
| Полученные пакеты SYN | builtin:cloud.azure.loadbalancer.traffic.packetSynIn | Количество SYN | ext:cloud.azure.microsoft\_network.loadbalancers.syncount:filter(eq("Direction", "In")) |
| Отправленные пакеты SYN | builtin:cloud.azure.loadbalancer.traffic.packetSynOut | Количество SYN | ext:cloud.azure.microsoft\_network.loadbalancers.syncount:filter(eq("Direction", "Out")) |

### Кэш Azure для Redis

| Название метрики классического сервиса | Ключ метрики классического сервиса | Название метрики облачного сервиса | Ключ метрики облачного сервиса |
| --- | --- | --- | --- |
| Попадания в кэш | builtin:cloud.azure.redis.cache.hits | Попадания в кэш | ext:cloud.azure.microsoft\_cache.redis.cachehits |
| Промахи кэша | builtin:cloud.azure.redis.cache.misses | Промахи кэша | ext:cloud.azure.microsoft\_cache.redis.cachemisses |
| Чтение байт/с | builtin:cloud.azure.redis.cache.read | Чтение из кэша | ext:cloud.azure.microsoft\_cache.redis.cacheread |
| Запись байт/с | builtin:cloud.azure.redis.cache.write | Запись в кэш | ext:cloud.azure.microsoft\_cache.redis.cachewrite |
| Команды get | builtin:cloud.azure.redis.commands.get | Gets | ext:cloud.azure.microsoft\_cache.redis.getcommands |
| Команды set | builtin:cloud.azure.redis.commands.set | Sets | ext:cloud.azure.microsoft\_cache.redis.setcommands |
| Общее количество обработанных команд | builtin:cloud.azure.redis.commands.total | Всего операций | ext:cloud.azure.microsoft\_cache.redis.totalcommandsprocessed |
| Количество вытесненных ключей | builtin:cloud.azure.redis.keys.evicted | Вытесненные ключи | ext:cloud.azure.microsoft\_cache.redis.evictedkeys |
| Количество истёкших ключей | builtin:cloud.azure.redis.keys.expired | Истёкшие ключи | ext:cloud.azure.microsoft\_cache.redis.expiredkeys |
| Общее количество ключей | builtin:cloud.azure.redis.keys.total | Всего ключей | ext:cloud.azure.microsoft\_cache.redis.totalkeys |
| Используемая память | builtin:cloud.azure.redis.memory.used | Используемая память | ext:cloud.azure.microsoft\_cache.redis.usedmemory |
| Используемая память RSS | builtin:cloud.azure.redis.memory.usedRss | Используемая память RSS | ext:cloud.azure.microsoft\_cache.redis.usedmemoryrss |
| Подключённые клиенты | builtin:cloud.azure.redis.connected | Подключённые клиенты | ext:cloud.azure.microsoft\_cache.redis.connectedclients |
| Нагрузка на сервер | builtin:cloud.azure.redis.load | Нагрузка на сервер | ext:cloud.azure.microsoft\_cache.redis.serverload |
| Время процессора | builtin:cloud.azure.redis.processorTime | CPU | ext:cloud.azure.microsoft\_cache.redis.percentprocessortime |

### Azure Cosmos Database

| Название метрики классического сервиса | Ключ метрики классического сервиса | Название метрики облачного сервиса | Ключ метрики облачного сервиса |
| --- | --- | --- | --- |
| Доступное хранилище | builtin:cloud.azure.cosmos.availableStorage | - | - |
| Использование данных | builtin:cloud.azure.cosmos.dataUsage | Использование данных | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.datausage |
| Количество документов | builtin:cloud.azure.cosmos.documentCount | Количество документов | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.documentcount |
| Квота документов | builtin:cloud.azure.cosmos.documentQuota | Квота документов | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.documentquota |
| Использование индекса | builtin:cloud.azure.cosmos.indexUsage | Использование индекса | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.indexusage |
| Запросы метаданных | builtin:cloud.azure.cosmos.metadataRequests | Запросы метаданных | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.metadatarequests |
| Нормализованное потребление единиц запроса | builtin:cloud.azure.cosmos.normalizedRUConsumption | Нормализованное потребление RU | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.normalizedruconsumption |
| Подготовленная пропускная способность | builtin:cloud.azure.cosmos.provisionedThroughput | Подготовленная пропускная способность | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.provisionedthroughput |
| Задержка репликации | builtin:cloud.azure.cosmos.replicationLatency | Задержка репликации P99 | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.replicationlatency |
| Общее количество единиц запроса | builtin:cloud.azure.cosmos.requestUnits | Всего единиц запроса | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.totalrequestunits |
| Общее количество запросов | builtin:cloud.azure.cosmos.requests | Всего запросов | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.totalrequests |
| Доступность сервиса | builtin:cloud.azure.cosmos.serviceAvailability | Доступность сервиса | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.serviceavailability |

### Azure IoT Hub

| Название метрики классического сервиса | Ключ метрики классического сервиса | Название метрики облачного сервиса | Ключ метрики облачного сервиса |
| --- | --- | --- | --- |
| Отклонённые команды | builtin:cloud.azure.iotHub.command.abandoned | Отклонённые сообщения C2D | ext:cloud.azure.microsoft\_devices.iothubs.c2d\_commands\_egress\_abandon\_success |
| Выполненные команды | builtin:cloud.azure.iotHub.command.completed | Доставка сообщений C2D завершена | ext:cloud.azure.microsoft\_devices.iothubs.c2d\_commands\_egress\_complete\_success |
| Отклонённые команды | builtin:cloud.azure.iotHub.command.rejected | Отклонённые сообщения C2D | ext:cloud.azure.microsoft\_devices.iothubs.c2d\_commands\_egress\_reject\_success |
| Подключённые устройства | builtin:cloud.azure.iotHub.device.connected | Подключённые устройства | ext:cloud.azure.microsoft\_devices.iothubs.connecteddevicecount |
| Количество ошибок регулирования | builtin:cloud.azure.iotHub.device.dailyThroughputThrottling | Количество ошибок регулирования | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_telemetry\_ingress\_sendthrottle |
| Общее использование данных устройствами | builtin:cloud.azure.iotHub.device.dataUsage | Общее использование данных устройствами / Общее использование данных устройствами (предварительная версия) | ext:cloud.azure.microsoft\_devices.iothubs.devicedatausage ext:cloud.azure.microsoft\_devices.iothubs.devicedatausagev2 |
| Всего устройств | builtin:cloud.azure.iotHub.device.registered | Всего устройств | ext:cloud.azure.microsoft\_devices.iothubs.totaldevicecount |
| Сообщения, доставленные во встроенную конечную точку (сообщения/события) | builtin:cloud.azure.iotHub.eventHub.builtInEventHub.messages.delivered | Маршрутизация — сообщения, доставленные в messages/events | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_egress\_builtin\_events |
| Задержка сообщений для встроенной конечной точки (сообщения/события) | builtin:cloud.azure.iotHub.eventHub.builtInEventHub.averageLatencyMs | Маршрутизация — задержка сообщений для messages/events | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_latency\_builtin\_events |
| Сообщения, доставленные в конечные точки концентратора событий | builtin:cloud.azure.iotHub.eventHub.messages.delivered | Маршрутизация — сообщения, доставленные в концентратор событий | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_egress\_eventhubs |
| Задержка сообщений для конечных точек концентратора событий | builtin:cloud.azure.iotHub.eventHub.averageLatencyMs | Маршрутизация — задержка сообщений для концентратора событий | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_latency\_eventhubs |
| Отброшенные сообщения | builtin:cloud.azure.iotHub.messages.dropped | Маршрутизация — отброшенные телеметрические сообщения | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_telemetry\_egress\_dropped |
| Недопустимые сообщения | builtin:cloud.azure.iotHub.messages.invalidForAllEndpoints | Маршрутизация — несовместимые телеметрические сообщения | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_telemetry\_egress\_invalid |
| Потерянные сообщения | builtin:cloud.azure.iotHub.messages.orphaned | Маршрутизация — потерянные телеметрические сообщения | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_telemetry\_egress\_orphaned |
| Попытки отправки телеметрических сообщений | builtin:cloud.azure.iotHub.messages.sendAttempts | Попытки отправки телеметрических сообщений | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_telemetry\_ingress\_allprotocol |
| Отправленные телеметрические сообщения | builtin:cloud.azure.iotHub.messages.sent | Отправленные телеметрические сообщения | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_telemetry\_ingress\_success |
| Сообщения, соответствующие условию резервного маршрута | builtin:cloud.azure.iotHub.messages.sentToFallback | Маршрутизация — сообщения, доставленные в резервный маршрут | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_telemetry\_egress\_fallback |
| Задержка сообщений для конечных точек очереди служебной шины | builtin:cloud.azure.iotHub.serviceBus.queues.averageLatencyMs | Маршрутизация — задержка сообщений для очереди служебной шины | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_latency\_servicebusqueues |
| Сообщения, доставленные в конечные точки очереди служебной шины | builtin:cloud.azure.iotHub.serviceBus.queues.messagesDelivered | Маршрутизация — сообщения, доставленные в очередь служебной шины | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_egress\_servicebusqueues |
| Задержка сообщений для конечных точек темы служебной шины | builtin:cloud.azure.iotHub.serviceBus.topics.averageLatencyMs | Маршрутизация — задержка сообщений для темы служебной шины | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_latency\_servicebustopics |
| Сообщения, доставленные в конечные точки темы служебной шины | builtin:cloud.azure.iotHub.serviceBus.topics.messagesDelivered | Маршрутизация — сообщения, доставленные в тему служебной шины | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_egress\_servicebustopics |
| Задержка сообщений для конечных точек хранилища | builtin:cloud.azure.iotHub.storageEndpoints.avgLatencyMs | Маршрутизация — задержка сообщений для хранилища | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_latency\_storage |
| Записанные в хранилище BLOB-объекты | builtin:cloud.azure.iotHub.storageEndpoints.blobsWritten | Маршрутизация — BLOB-объекты, доставленные в хранилище | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_egress\_storage\_blobs |
| Данные, записанные в хранилище | builtin:cloud.azure.iotHub.storageEndpoints.bytesWritten | Маршрутизация — данные, доставленные в хранилище | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_egress\_storage\_bytes |
| Сообщения, доставленные в конечные точки хранилища | builtin:cloud.azure.iotHub.storageEndpoints.messageDelivered | Маршрутизация — сообщения, доставленные в хранилище | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_egress\_storage |

### SQL Server Azure

#### Базы данных SQL Azure

| Название метрики классического сервиса | Ключ метрики классического сервиса | Название метрики облачного сервиса | Метрика облачного сервиса |
| --- | --- | --- | --- |
| Заблокировано брандмауэром | builtin:cloud.azure.sqlDatabase.connections.blockedByFirewall | Заблокировано брандмауэром | ext:cloud.azure.microsoft\_sql.servers.databases.blocked\_by\_firewall |
| Неудачные соединения | builtin:cloud.azure.sqlDatabase.connections.failed | Неудачные соединения — системные ошибки / Неудачные соединения — ошибки пользователя | ext:cloud.azure.microsoft\_sql.servers.databases.connection\_failed ext:cloud.azure.microsoft\_sql.servers.databases.connection\_failed\_user\_error |
| Успешные соединения | builtin:cloud.azure.sqlDatabase.connections.successful | Успешные соединения | ext:cloud.azure.microsoft\_sql.servers.databases.connection\_successful |
| Лимит DTU | builtin:cloud.azure.sqlDatabase.dtu.limit.count | Лимит DTU | ext:cloud.azure.microsoft\_sql.servers.databases.dtu\_limit |
| Использовано DTU | builtin:cloud.azure.sqlDatabase.dtu.limit.used | Использовано DTU | ext:cloud.azure.microsoft\_sql.servers.databases.dtu\_used |
| Процент DTU | builtin:cloud.azure.sqlDatabase.dtu.consumptionPerc | Процент DTU | ext:cloud.azure.microsoft\_sql.servers.databases.dtu\_consumption\_percent |
| Процент ввода/вывода данных | builtin:cloud.azure.sqlDatabase.io.dataRead | Процент ввода/вывода данных | ext:cloud.azure.microsoft\_sql.servers.databases.physical\_data\_read\_percent |
| Процент ввода/вывода журнала | builtin:cloud.azure.sqlDatabase.io.logWrite | Процент ввода/вывода журнала | ext:cloud.azure.microsoft\_sql.servers.databases.log\_write\_percent |
| Процент размера базы данных | builtin:cloud.azure.sqlDatabase.storage.percent | Процент используемого пространства данных | ext:cloud.azure.microsoft\_sql.servers.databases.storage\_percent |
| Общий размер базы данных | builtin:cloud.azure.sqlDatabase.storage.totalBytes | Используемое пространство данных | ext:cloud.azure.microsoft\_sql.servers.databases.storage |
| Процент использования In-Memory OLTP | builtin:cloud.azure.sqlDatabase.storage.xtpPercent | ext:cloud.azure.microsoft\_sql.servers.databases.xtp\_storage\_percent | ext:cloud.azure.microsoft\_sql.servers.databases.xtp\_storage\_percent |
| Процент использования CPU | builtin:cloud.azure.sqlDatabase.cpuPercent | Процент использования CPU | ext:cloud.azure.microsoft\_sql.servers.databases.cpu\_percent |
| Взаимные блокировки | builtin:cloud.azure.sqlDatabase.deadlocks | Взаимные блокировки | ext:cloud.azure.microsoft\_sql.servers.databases.deadlock |
| Процент сессий | builtin:cloud.azure.sqlDatabase.sessions | Процент сессий | ext:cloud.azure.microsoft\_sql.servers.databases.sessions\_percent |
| Процент рабочих процессов | builtin:cloud.azure.sqlDatabase.workers | Процент рабочих процессов | ext:cloud.azure.microsoft\_sql.servers.databases.workers\_percent |

#### Эластичные пулы баз данных SQL Azure

| Название метрики классического сервиса | Ключ метрики классического сервиса | Название метрики облачного сервиса | Ключ метрики облачного сервиса |
| --- | --- | --- | --- |
| Лимит хранилища | builtin:cloud.azure.sqlElasticPool.dtu.storage.limitBytes | Максимальный размер данных | ext:cloud.azure.microsoft\_sql.servers.elasticpools.storage\_limit |
| Процент размера базы данных | builtin:cloud.azure.sqlElasticPool.dtu.storage.percent | Процент используемого пространства данных | ext:cloud.azure.microsoft\_sql.servers.elasticpools.storage\_percent |
| Используемое хранилище | builtin:cloud.azure.sqlElasticPool.dtu.storage.usedBytes | Используемое пространство данных | ext:cloud.azure.microsoft\_sql.servers.elasticpools.storage\_used |
| Процент использования In-Memory OLTP | builtin:cloud.azure.sqlElasticPool.dtu.storage.xtpPercent | Процент использования In-Memory OLTP | ext:cloud.azure.microsoft\_sql.servers.elasticpools.xtp\_storage\_percent |
| Процент DTU | builtin:cloud.azure.sqlElasticPool.dtu.consumption | Процент DTU | ext:cloud.azure.microsoft\_sql.servers.elasticpools.dtu\_consumption\_percent |
| Лимит eDTU | builtin:cloud.azure.sqlElasticPool.edtu.limit | Лимит EDTU | ext:cloud.azure.microsoft\_sql.servers.elasticpools.edtu\_limit |
| Использовано eDTU | builtin:cloud.azure.sqlElasticPool.edtu.used | Использовано EDTU | ext:cloud.azure.microsoft\_sql.servers.elasticpools.edtu\_used |
| Процент ввода/вывода данных | builtin:cloud.azure.sqlElasticPool.io.dataRead | Процент ввода/вывода данных | ext:cloud.azure.microsoft\_sql.servers.elasticpools.physical\_data\_read\_percent |
| Процент ввода/вывода журнала | builtin:cloud.azure.sqlElasticPool.io.logWrite | Процент ввода/вывода журнала | ext:cloud.azure.microsoft\_sql.servers.elasticpools.log\_write\_percent |
| Процент использования CPU | builtin:cloud.azure.sqlElasticPool.cpuPercent | Процент использования CPU | ext:cloud.azure.microsoft\_sql.servers.elasticpools.cpu\_percent |
| Процент сессий | builtin:cloud.azure.sqlElasticPool.sessions | Процент сессий | ext:cloud.azure.microsoft\_sql.servers.elasticpools.sessions\_percent |
| Процент рабочих процессов | builtin:cloud.azure.sqlElasticPool.workers | Процент рабочих процессов | ext:cloud.azure.microsoft\_sql.servers.elasticpools.workers\_percent |

### Учётная запись хранения Azure

| Название метрики классического сервиса | Ключ метрики классического сервиса | Название метрики облачного сервиса | Ключ метрики облачного сервиса |
| --- | --- | --- | --- |
| Количество транзакций | builtin:cloud.azure.storage.blob.transactions | Транзакции | ext:cloud.azure.microsoft\_storage.storageaccounts.blobservices.transactions |
| Сквозная задержка успешных запросов (E2E) | builtin:cloud.azure.storage.blob.transactions.network.latency.success.e2e | Задержка E2E для успешных запросов | ext:cloud.azure.microsoft\_storage.storageaccounts.blobservices.transactions |
| Задержка успешных запросов на сервере | builtin:cloud.azure.storage.blob.transactions.network.latency.success.server | Задержка сервера для успешных запросов | ext:cloud.azure.microsoft\_storage.storageaccounts.blobservices.successserverlatency |
| Исходящие байты | builtin:cloud.azure.storage.blob.transactions.network.egress | Исходящий трафик | ext:cloud.azure.microsoft\_storage.storageaccounts.blobservices.egress |
| Входящие байты | builtin:cloud.azure.storage.blob.transactions.network.ingress | Входящий трафик | ext:cloud.azure.microsoft\_storage.storageaccounts.blobservices.ingress |
| Ёмкость BLOB-объектов | builtin:cloud.azure.storage.blob.capacity | Ёмкость BLOB-объектов | ext:cloud.azure.microsoft\_storage.storageaccounts.blobservices.blobcapacity |
| Количество контейнеров BLOB-объектов | builtin:cloud.azure.storage.blob.containers | Количество контейнеров BLOB-объектов | ext:cloud.azure.microsoft\_storage.storageaccounts.blobservices.containercount |
| Количество BLOB-объектов | builtin:cloud.azure.storage.blob.entities | Количество BLOB-объектов | ext:cloud.azure.microsoft\_storage.storageaccounts.blobservices.blobcount |
| Количество транзакций | builtin:cloud.azure.storage.file.transactions | Транзакции | ext:cloud.azure.microsoft\_storage.storageaccounts.fileservices.transactions |
| Сквозная задержка успешных запросов (E2E) | builtin:cloud.azure.storage.file.transactions.network.latency.success.e2e | Задержка E2E для успешных запросов | ext:cloud.azure.microsoft\_storage.storageaccounts.fileservices.successe2elatency |
| Задержка успешных запросов на сервере | builtin:cloud.azure.storage.file.transactions.network.latency.success.server | Задержка сервера для успешных запросов | ext:cloud.azure.microsoft\_storage.storageaccounts.fileservices.successserverlatency |
| Исходящие байты | builtin:cloud.azure.storage.file.transactions.network.egress | Исходящий трафик | ext:cloud.azure.microsoft\_storage.storageaccounts.fileservices.egress |
| Входящие байты | builtin:cloud.azure.storage.file.transactions.network.ingress | Входящий трафик | ext:cloud.azure.microsoft\_storage.storageaccounts.fileservices.ingress |
| Ёмкость файлового хранилища | builtin:cloud.azure.storage.file.capacity | Ёмкость файлового хранилища | ext:cloud.azure.microsoft\_storage.storageaccounts.fileservices.filecapacity |
| Количество файловых ресурсов | builtin:cloud.azure.storage.file.containers | Количество файловых ресурсов | ext:cloud.azure.microsoft\_storage.storageaccounts.fileservices.filesharecount |
| Количество файлов | builtin:cloud.azure.storage.file.entities | Количество файлов | ext:cloud.azure.microsoft\_storage.storageaccounts.fileservices.filecount |
| Количество транзакций | builtin:cloud.azure.storage.queue.transactions | Транзакции | ext:cloud.azure.microsoft\_storage.storageaccounts.queueservices.transactions |
| Сквозная задержка успешных запросов (E2E) | builtin:cloud.azure.storage.queue.transactions.network.latency.success.e2e | Задержка E2E для успешных запросов | ext:cloud.azure.microsoft\_storage.storageaccounts.queueservices.successe2elatency |
| Задержка успешных запросов на сервере | builtin:cloud.azure.storage.queue.transactions.network.latency.success.server | Задержка сервера для успешных запросов | ext:cloud.azure.microsoft\_storage.storageaccounts.queueservices.successserverlatency |
| Исходящие байты | builtin:cloud.azure.storage.queue.transactions.network.egress | Исходящий трафик | ext:cloud.azure.microsoft\_storage.storageaccounts.queueservices.egress |
| Входящие байты | builtin:cloud.azure.storage.queue.transactions.network.ingress | Входящий трафик | ext:cloud.azure.microsoft\_storage.storageaccounts.queueservices.ingress |
| Ёмкость очереди | builtin:cloud.azure.storage.queue.capacity | Ёмкость очереди | ext:cloud.azure.microsoft\_storage.storageaccounts.queueservices.queuecapacity |
| Количество очередей | builtin:cloud.azure.storage.queue.containers | Количество очередей | ext:cloud.azure.microsoft\_storage.storageaccounts.queueservices.queuecount |
| Количество сообщений в очереди | builtin:cloud.azure.storage.queue.entities | Количество сообщений в очереди | ext:cloud.azure.microsoft\_storage.storageaccounts.queueservices.queuemessagecount |
| Количество транзакций | builtin:cloud.azure.storage.table.transactions | Транзакции | ext:cloud.azure.microsoft\_storage.storageaccounts.tableservices.transactions |
| Задержка успешных запросов на сервере | builtin:cloud.azure.storage.table.transactions.network.latency.success.server | Задержка сервера для успешных запросов | ext:cloud.azure.microsoft\_storage.storageaccounts.tableservices.successserverlatency |
| Сквозная задержка успешных запросов (E2E) | builtin:cloud.azure.storage.table.transactions.network.latency.success.server.e2e | Задержка E2E для успешных запросов | ext:cloud.azure.microsoft\_storage.storageaccounts.tableservices.successe2elatency |
| Исходящие байты | builtin:cloud.azure.storage.table.transactions.network.egress | Исходящий трафик | ext:cloud.azure.microsoft\_storage.storageaccounts.tableservices.egress |
| Входящие байты | builtin:cloud.azure.storage.table.transactions.network.ingress | Входящий трафик | ext:cloud.azure.microsoft\_storage.storageaccounts.tableservices.ingress |
| Ёмкость таблиц | builtin:cloud.azure.storage.table.capacity | Ёмкость таблиц | ext:cloud.azure.microsoft\_storage.storageaccounts.tableservices.tablecapacity |
| Количество таблиц | builtin:cloud.azure.storage.table.containers | Количество таблиц | ext:cloud.azure.microsoft\_storage.storageaccounts.tableservices.tablecount |
| Количество сущностей таблиц | builtin:cloud.azure.storage.table.entities | Количество сущностей таблиц | ext:cloud.azure.microsoft\_storage.storageaccounts.tableservices.tableentitycount |
