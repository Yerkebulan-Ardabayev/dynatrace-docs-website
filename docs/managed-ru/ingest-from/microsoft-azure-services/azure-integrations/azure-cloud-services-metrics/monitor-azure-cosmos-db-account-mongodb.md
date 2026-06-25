---
title: Мониторинг Azure Cosmos DB Account (MongoDB)
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-cosmos-db-account-mongodb
scraped: 2026-05-12T11:26:56.971345
---

# Мониторинг Azure Cosmos DB Account (MongoDB)

# Мониторинг Azure Cosmos DB Account (MongoDB)

* Практическое руководство
* Чтение: 5 мин
* Обновлено 15 ноября 2023 г.

Информацию о различиях между классическими службами и другими службами см. в разделе [Миграция с классических служб Azure (ранее «встроенных») на облачные службы](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide "Перенос классических служб Azure на их новые версии.").

Dynatrace получает метрики из Azure Metrics API для Azure Cosmos DB Account (MongoDB). Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать метрики по различным измерениям и создавать пользовательские графики, которые можно закрепить на ваших дашбордах.

## Предварительные условия

* Dynatrace версии 1.199+
* Environment ActiveGate версии 1.195+

## Включение мониторинга

Чтобы узнать, как включить мониторинг сервиса, см. [Включение мониторинга сервиса](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Включение мониторинга Azure в Dynatrace.").

## Просмотр метрик сервиса

Вы можете просматривать метрики сервиса в вашей среде Dynatrace на **странице обзора пользовательского устройства** или на странице **Dashboards**.

### Просмотр метрик на странице обзора пользовательского устройства

Чтобы перейти на страницу обзора пользовательского устройства:

1. Перейдите в **Technologies & Processes**.
2. Отфильтруйте по имени сервиса и выберите соответствующую группу пользовательских устройств.
3. После выбора группы пользовательских устройств вы окажетесь на **странице обзора группы пользовательских устройств**.
4. На **странице обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), принадлежащие группе. Выберите экземпляр для просмотра **страницы обзора пользовательского устройства**.

### Просмотр метрик на дашборде

Если для сервиса предусмотрен предустановленный дашборд, он появится на вашей странице **Dashboards** с набором всех рекомендуемых метрик. Искать конкретные дашборды можно с помощью фильтрации по **Preset**, а затем по **Name**.

Для уже отслеживаемых сервисов может потребоваться повторно сохранить учётные данные, чтобы предустановленный дашборд отобразился на странице **Dashboards**. Для повторного сохранения учётных данных перейдите в **Settings** > **Cloud and virtualization** > **Azure**, выберите нужный экземпляр Azure, затем нажмите **Save**.

Вы не можете вносить изменения непосредственно в предустановленный дашборд, но можете клонировать его и редактировать. Чтобы клонировать дашборд, откройте меню обзора (**…**) и выберите **Clone**.  
Чтобы убрать дашборд из списка, его можно скрыть. Чтобы скрыть дашборд, откройте меню обзора (**…**) и выберите **Hide**.

Скрытие дашборда не затрагивает других пользователей.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

Clone hide azure

## Доступные метрики

Этот сервис отслеживает часть Azure Cosmos DB Account (Microsoft.DocumentDB/databaseAccounts). Пока этот сервис настроен, вы не можете включить сервис Azure Cosmos Database (built-in).

| Имя | Описание | Измерения | Единица измерения | Рекомендуется |
| --- | --- | --- | --- | --- |
| AddRegion | Добавление региона | Region | Количество |  |
| AutoscaleMaxThroughput | Максимальная пропускная способность автомасштабирования | Collection name, Database name | Количество | Применимо |
| CreateAccount | Создание учётной записи |  | Количество |  |
| DataUsage | Общее использование данных, регистрируется с детализацией в 5 минут | Collection name, Database name, Region | Байт | Применимо |
| DeleteAccount | Удаление учётной записи |  | Количество |  |
| DocumentCount | Общее количество документов, регистрируется с детализацией в 5 минут, 1 час и 1 день | Collection name, Database name, Region | Количество | Применимо |
| DocumentQuota | Общая квота хранилища, регистрируется с детализацией в 5 минут | Collection name, Database name, Region | Байт | Применимо |
| IndexUsage | Общее использование индекса, регистрируется с детализацией в 5 минут | Collection name, Database name, Region | Байт | Применимо |
| MetadataRequests | Количество запросов метаданных. Cosmos DB поддерживает коллекцию системных метаданных для каждой учётной записи, что позволяет бесплатно перечислять коллекции, базы данных и т. д., а также их конфигурации. | Collection name, Database name, Region, Status code | Количество | Применимо |
| MongoCollectionCreate | Создание коллекции Mongo | Collection name, Database name | Количество |  |
| MongoCollectionDelete | Удаление коллекции Mongo | Collection name, Database name | Количество |  |
| MongoCollectionThroughputUpdate | Обновление пропускной способности коллекции Mongo | Collection name, Database name | Количество |  |
| MongoCollectionUpdate | Обновление коллекции Mongo | Collection name, Database name | Количество |  |
| MongoDBDatabaseCreate | Создание базы данных Mongo | Database name | Количество |  |
| MongoDBDatabaseUpdate | Обновление базы данных Mongo | Database name | Количество |  |
| MongoDatabaseDelete | Удаление базы данных Mongo | Database name | Количество |  |
| MongoDatabaseThroughputUpdate | Обновление пропускной способности базы данных Mongo | Database name | Количество |  |
| MongoRequestCharge | Потреблено единиц запросов Mongo | Collection name, Command name, Database name, Error code, Region, Status | Количество |  |
| MongoRequests | Количество выполненных запросов Mongo | Collection name, Command name, Database name, Error code, Region, Status | Количество |  |
| NormalizedRUConsumption | Максимальный процент потребления RU в минуту | Collection name, Collection rid, Database name, Partition key range ID, Physical partition ID, Region | Процент | Применимо |
| OfflineRegion | Перевод региона в автономный режим | Region, Status code | Количество |  |
| OnlineRegion | Перевод региона в оперативный режим | Region, Status code | Количество |  |
| PhysicalPartitionSizeInfo | Размер физического раздела в байтах | Collection name, Database name, Physical partition ID, Region, Resource ID | Байт |  |
| PhysicalPartitionThroughputInfo | Пропускная способность физического раздела | Collection name, Database name, Physical partition ID, Region, Resource ID | Количество |  |
| ProvisionedThroughput | Подготовленная пропускная способность | Collection name, Database name | Количество | Применимо |
| RegionFailover | Переключение региона при отказе |  | Количество |  |
| RemoveRegion | Удаление региона | Region | Количество |  |
| ReplicationLatency | Задержка репликации P99 между исходным и целевым регионами для учётной записи с поддержкой геораспределения | Source region, Target region | Миллисекунда |  |
| ServerSideLatency | Задержка на стороне сервера | Collection name, Connection mode, Database name, Operation type, Publicapi type, Region | Миллисекунда | Применимо |
| ServerSideLatencyDirect | Задержка на стороне сервера в режиме прямого подключения | Collection name, Database name, Operation type, Publicapi type, Region | Миллисекунда |  |
| ServerSideLatencyGateway | Задержка на стороне сервера в режиме подключения через шлюз | Collection name, Database name, Operation type, Publicapi type, Region | Миллисекунда |  |
| ServiceAvailability | Доступность запросов к учётной записи с детализацией по часу, дню или месяцу |  | Процент | Применимо |
| TotalRequestUnits | Потреблено единиц запросов SQL | Capacity type, Collection name, Database name, Operation type, Region, Status, Status code | Количество | Применимо |
| TotalRequests | Количество выполненных запросов | Capacity type, Collection name, Database name, Operation type, Region, Status, Status code | Количество | Применимо |
| UpdateAccountKeys | Обновление ключей учётной записи | Key type | Количество |  |
| UpdateAccountNetworkSettings | Обновление сетевых настроек учётной записи |  | Количество |  |
| UpdateAccountReplicationSettings | Обновление настроек репликации учётной записи |  | Количество |  |
| UpdateDiagnosticsSettings | Обновление настроек диагностики учётной записи | Diagnostic settings name, Resource group name | Количество |  |