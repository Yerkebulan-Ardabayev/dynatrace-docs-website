---
title: Azure Cosmos DB Account (MongoDB) monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-cosmos-db-account-mongodb
scraped: 2026-03-06T21:28:04.102554
---

# Мониторинг Azure Cosmos DB Account (MongoDB)

# Мониторинг Azure Cosmos DB Account (MongoDB)

* Latest Dynatrace
* How-to guide
* 5-min read
* Updated on Nov 15, 2023

Информацию о различиях между классическими сервисами и другими сервисами см. в разделе [Миграция с классических сервисов Azure (ранее «встроенных») на облачные сервисы](../azure-monitoring-guide/azure-migration-guide.md "Migrate Azure classic services to their new versions.").

Dynatrace получает метрики из Azure Metrics API для Azure Cosmos DB Account (MongoDB). Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать метрики по нескольким измерениям и создавать пользовательские графики, которые можно закреплять на ваших дашбордах.

## Предварительные требования

* Dynatrace версии 1.199+
* Environment ActiveGate версии 1.195+

## Включение мониторинга

Чтобы узнать, как включить мониторинг сервиса, см. [Включение мониторинга сервиса](../azure-monitoring-guide/azure-enable-service-monitoring.md "Enable Azure monitoring in Dynatrace.").

## Просмотр метрик сервиса

Вы можете просматривать метрики сервиса в вашей среде Dynatrace либо на **странице обзора пользовательского устройства**, либо на странице **Dashboards**.

### Просмотр метрик на странице обзора пользовательского устройства

Для доступа к странице обзора пользовательского устройства

1. Перейдите в ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Отфильтруйте по имени сервиса и выберите соответствующую группу пользовательских устройств.
3. После выбора группы пользовательских устройств вы попадёте на **страницу обзора группы пользовательских устройств**.
4. На **странице обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), принадлежащие группе. Выберите экземпляр для просмотра **страницы обзора пользовательского устройства**.

### Просмотр метрик на дашборде

Если для сервиса имеется предустановленный дашборд, вы получите предустановленный дашборд для соответствующего сервиса со всеми рекомендуемыми метриками на странице **Dashboards**. Вы можете искать конкретные дашборды, фильтруя по **Preset**, а затем по **Name**.

Для существующих отслеживаемых сервисов может потребоваться повторное сохранение учётных данных, чтобы предустановленный дашборд появился на странице **Dashboards**. Чтобы повторно сохранить учётные данные, перейдите в **Settings** > **Cloud and virtualization** > **Azure**, выберите нужный экземпляр Azure, а затем нажмите **Save**.

Вы не можете вносить изменения непосредственно в предустановленный дашборд, но вы можете его клонировать и редактировать. Чтобы клонировать дашборд, откройте меню (**...**) и выберите **Clone**.
Чтобы удалить дашборд из списка дашбордов, вы можете скрыть его. Чтобы скрыть дашборд, откройте меню (**...**) и выберите **Hide**.

Скрытие дашборда не влияет на других пользователей.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

## Доступные метрики

Этот сервис отслеживает часть Azure Cosmos DB Account (Microsoft.DocumentDB/databaseAccounts). Пока данный сервис настроен, вы не можете включить сервис Azure Cosmos Database (built-in).

| Название | Описание | Измерения | Единица | Рекомендовано |
| --- | --- | --- | --- | --- |
| AddRegion | Регион добавлен | Region | Count |  |
| AutoscaleMaxThroughput | Максимальная пропускная способность автомасштабирования | Collection name, Database name | Count | Применимо |
| CreateAccount | Учётная запись создана |  | Count |  |
| DataUsage | Общее использование данных с отчётностью каждые 5 минут | Collection name, Database name, Region | Byte | Применимо |
| DeleteAccount | Учётная запись удалена |  | Count |  |
| DocumentCount | Общее количество документов с отчётностью каждые 5 минут, 1 час и 1 день | Collection name, Database name, Region | Count | Применимо |
| DocumentQuota | Общая квота хранилища с отчётностью каждые 5 минут | Collection name, Database name, Region | Byte | Применимо |
| IndexUsage | Общее использование индекса с отчётностью каждые 5 минут | Collection name, Database name, Region | Byte | Применимо |
| MetadataRequests | Количество запросов метаданных. Cosmos DB поддерживает коллекцию системных метаданных для каждой учётной записи, что позволяет бесплатно перечислять коллекции, базы данных и их конфигурации. | Collection name, Database name, Region, Status code | Count | Применимо |
| MongoCollectionCreate | Коллекция Mongo создана | Collection name, Database name | Count |  |
| MongoCollectionDelete | Коллекция Mongo удалена | Collection name, Database name | Count |  |
| MongoCollectionThroughputUpdate | Пропускная способность коллекции Mongo обновлена | Collection name, Database name | Count |  |
| MongoCollectionUpdate | Коллекция Mongo обновлена | Collection name, Database name | Count |  |
| MongoDBDatabaseCreate | База данных Mongo создана | Database name | Count |  |
| MongoDBDatabaseUpdate | База данных Mongo обновлена | Database name | Count |  |
| MongoDatabaseDelete | База данных Mongo удалена | Database name | Count |  |
| MongoDatabaseThroughputUpdate | Пропускная способность базы данных Mongo обновлена | Database name | Count |  |
| MongoRequestCharge | Потреблённые единицы запросов Mongo | Collection name, Command name, Database name, Error code, Region, Status | Count |  |
| MongoRequests | Количество выполненных запросов Mongo | Collection name, Command name, Database name, Error code, Region, Status | Count |  |
| NormalizedRUConsumption | Максимальный процент потребления RU в минуту | Collection name, Collection rid, Database name, Partition key range ID, Physical partition ID, Region | Percent | Применимо |
| OfflineRegion | Регион переведён в автономный режим | Region, Status code | Count |  |
| OnlineRegion | Регион переведён в режим онлайн | Region, Status code | Count |  |
| PhysicalPartitionSizeInfo | Размер физического раздела в байтах | Collection name, Database name, Physical partition ID, Region, Resource ID | Byte |  |
| PhysicalPartitionThroughputInfo | Пропускная способность физического раздела | Collection name, Database name, Physical partition ID, Region, Resource ID | Count |  |
| ProvisionedThroughput | Подготовленная пропускная способность | Collection name, Database name | Count | Применимо |
| RegionFailover | Выполнена отработка отказа региона |  | Count |  |
| RemoveRegion | Регион удалён | Region | Count |  |
| ReplicationLatency | Задержка репликации P99 между исходным и целевым регионами для учётной записи с поддержкой георепликации | Source region, Target region | MilliSecond |  |
| ServerSideLatency | Задержка на стороне сервера | Collection name, Connection mode, Database name, Operation type, Publicapi type, Region | MilliSecond | Применимо |
| ServerSideLatencyDirect | Задержка на стороне сервера в режиме прямого подключения | Collection name, Database name, Operation type, Publicapi type, Region | MilliSecond |  |
| ServerSideLatencyGateway | Задержка на стороне сервера в режиме подключения через шлюз | Collection name, Database name, Operation type, Publicapi type, Region | MilliSecond |  |
| ServiceAvailability | Доступность запросов учётной записи с гранулярностью 1 час, 1 день или 1 месяц |  | Percent | Применимо |
| TotalRequestUnits | Потреблённые единицы запросов SQL | Capacity type, Collection name, Database name, Operation type, Region, Status, Status code | Count | Применимо |
| TotalRequests | Количество выполненных запросов | Capacity type, Collection name, Database name, Operation type, Region, Status, Status code | Count | Применимо |
| UpdateAccountKeys | Ключи учётной записи обновлены | Key type | Count |  |
| UpdateAccountNetworkSettings | Сетевые настройки учётной записи обновлены |  | Count |  |
| UpdateAccountReplicationSettings | Параметры репликации учётной записи обновлены |  | Count |  |
| UpdateDiagnosticsSettings | Параметры диагностики учётной записи обновлены | Diagnostic settings name, Resource group name | Count |  |