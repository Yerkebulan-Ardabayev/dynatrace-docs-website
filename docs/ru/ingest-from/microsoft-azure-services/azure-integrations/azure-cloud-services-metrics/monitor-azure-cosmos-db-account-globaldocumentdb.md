---
title: Мониторинг Azure Cosmos DB Account (GlobalDocumentDB)
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-cosmos-db-account-globaldocumentdb
scraped: 2026-03-04T21:39:13.305924
---

# Мониторинг Azure Cosmos DB Account (GlobalDocumentDB)


* Latest Dynatrace
* Практическое руководство
* Чтение: 9 мин
* Обновлено 15 ноября 2023 г.

Информацию о различиях между классическими сервисами и другими сервисами см. в разделе [Миграция с классических (ранее «встроенных») сервисов Azure на облачные сервисы](../azure-monitoring-guide/azure-migration-guide.md "Миграция классических сервисов Azure на их новые версии.").

Dynatrace получает метрики из Azure Metrics API для Azure Cosmos DB Account (GlobalDocumentDB). Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать метрики по нескольким измерениям и создавать пользовательские графики, которые можно закрепить на панелях мониторинга.

## Предварительные требования

* Dynatrace версии 1.199+
* Environment ActiveGate версии 1.195+

## Включение мониторинга

Чтобы узнать, как включить мониторинг сервисов, см. [Включение мониторинга сервисов](../azure-monitoring-guide/azure-enable-service-monitoring.md "Включение мониторинга Azure в Dynatrace.").

## Просмотр метрик сервиса

Вы можете просматривать метрики сервиса в среде Dynatrace на **странице обзора пользовательского устройства** или на странице **Панели мониторинга**.

### Просмотр метрик на странице обзора пользовательского устройства

Для доступа к странице обзора пользовательского устройства

1. Перейдите в ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Отфильтруйте по имени сервиса и выберите соответствующую группу пользовательских устройств.
3. После выбора группы пользовательских устройств вы окажетесь на **странице обзора группы пользовательских устройств**.
4. На **странице обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), принадлежащие группе. Выберите экземпляр для просмотра **страницы обзора пользовательского устройства**.

### Просмотр метрик на панели мониторинга

Если для сервиса существует предустановленная панель мониторинга, вы получите предустановленную панель для соответствующего сервиса, содержащую все рекомендуемые метрики, на странице **Панели мониторинга**. Вы можете искать конкретные панели, фильтруя по **Предустановленные**, а затем по **Имя**.

Для существующих отслеживаемых сервисов может потребоваться повторное сохранение учётных данных, чтобы предустановленная панель появилась на странице **Панели мониторинга**. Для повторного сохранения учётных данных перейдите в **Settings** > **Cloud and virtualization** > **Azure**, выберите нужный экземпляр Azure, затем нажмите **Save**.

Вы не можете вносить изменения в предустановленную панель напрямую, но можете клонировать и редактировать её. Чтобы клонировать панель, откройте меню обзора (**...**) и выберите **Clone**.
Чтобы удалить панель из списка, вы можете её скрыть. Для этого откройте меню обзора (**...**) и выберите **Hide**.

Скрытие панели не влияет на других пользователей.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

## Доступные метрики

Этот сервис отслеживает часть Azure Cosmos DB Account (Microsoft.DocumentDB/databaseAccounts). Пока этот сервис настроен, вы не можете включить сервис Azure Cosmos Database (built-in).

| Название | Описание | Измерения | Единица | Рекомендуемая |
| --- | --- | --- | --- | --- |
| Region added | Регион добавлен | Region | Count |  |
| Autoscale max throughput | Максимальная пропускная способность автомасштабирования | Collection name, Database name | Count | Применимо |
| Cassandra connection closures | Количество закрытых подключений Cassandra, с гранулярностью в 1 минуту | Closure reason, Region | Count |  |
| Cassandra connector average replication latency | Средняя задержка репликации коннектора Cassandra |  | MilliSecond |  |
| Cassandra connector replication health status | Состояние репликации коннектора Cassandra | Replication in error, Replication not started, Replication in progress | Count |  |
| Cassandra keyspace created | Создано пространство ключей Cassandra | Keyspace name | Count |  |
| Cassandra keyspace deleted | Удалено пространство ключей Cassandra | Keyspace name | Count |  |
| Cassandra keyspace throughput updated | Обновлена пропускная способность пространства ключей Cassandra | Keyspace name | Count |  |
| Cassandra keyspace updated | Обновлено пространство ключей Cassandra | Keyspace name | Count |  |
| Cassandra request charges | Единицы запросов (RU), потреблённые запросами Cassandra | Collection name, Database name, Operation type, Region, Resource type | Count |  |
| Cassandra requests | Количество выполненных запросов Cassandra | Collection name, Database name, Error code, Operation type, Region, Resource type | Count |  |
| Cassandra table created | Создана таблица Cassandra | Table name, Keyspace name | Count |  |
| Cassandra table deleted | Удалена таблица Cassandra | Table name, Keyspace name | Count |  |
| Cassandra table throughput updated | Обновлена пропускная способность таблицы Cassandra | Table name, Keyspace name | Count |  |
| Cassandra table updated | Обновлена таблица Cassandra | Table name, Keyspace name | Count |  |
| Account created | Учётная запись создана |  | Count |  |
| Data usage | Общее использование данных с гранулярностью в 5 минут | Collection name, Database name, Region | Byte | Применимо |
| Dedicated gateway average CPU usage | Среднее использование ЦП на экземплярах выделенного шлюза | Region | Percent |  |
| Dedicated gateway average memory usage | Среднее использование памяти на экземплярах выделенного шлюза, которая используется как для маршрутизации запросов, так и для кэширования данных | Region | Byte |  |
| Dedicated gateway CPU usage | Использование ЦП на экземплярах выделенного шлюза | Region | Percent |  |
| Dedicated gateway maximum CPU usage | Среднее максимальное использование ЦП на экземплярах выделенного шлюза | Region | Percent |  |
| Dedicated gateway memory usage | Использование памяти на экземплярах выделенного шлюза | Region | Byte |  |
| Dedicated gateway requests | Запросы к выделенному шлюзу | Cache exercised, Cache hit, Collection name, Database name, Operation name, Region | Count |  |
| Account deleted | Учётная запись удалена |  | Count |  |
| Document count | Общее количество документов с гранулярностью в 5 минут, 1 час и 1 день | Collection name, Database name, Region | Count | Применимо |
| Document quota | Общая квота хранилища с гранулярностью в 5 минут | Collection name, Database name, Region | Byte | Применимо |
| Gremlin database created | Создана база данных Gremlin | Database name | Count |  |
| Gremlin database deleted | Удалена база данных Gremlin | Database name | Count |  |
| Gremlin database throughput updated | Обновлена пропускная способность базы данных Gremlin | Database name | Count |  |
| Gremlin database updated | Обновлена база данных Gremlin | Database name | Count |  |
| Gremlin graph created | Создан граф Gremlin | Graph name, Database name | Count |  |
| Gremlin graph deleted | Удалён граф Gremlin | Graph name, Database name | Count |  |
| Gremlin graph throughput updated | Обновлена пропускная способность графа Gremlin | Graph name, Database name | Count |  |
| Gremlin graph updated | Обновлён граф Gremlin | Graph name, Database name | Count |  |
| Gremlin request charges | Единицы запросов (RU), потреблённые запросами Gremlin | Collection name, Database name, Region | Count |  |
| Gremlin requests | Количество выполненных запросов Gremlin | Collection name, Database name, Error code, Region | Count |  |
| Index usage | Общее использование индекса с гранулярностью в 5 минут | Collection name, Database name, Region | Byte | Применимо |
| Integrated cache evicted entries size | Размер записей, вытесненных из интегрированного кэша | Region | Byte |  |
| Integrated cache item expiration count | Количество элементов, вытесненных из интегрированного кэша из-за истечения TTL | Region | Count |  |
| Integrated cache item hit rate | Количество точечных чтений, использовавших интегрированный кэш, делённое на количество точечных чтений, маршрутизированных через выделенный шлюз с eventual consistency | Region | Percent |  |
| Integrated cache query expiration count | Количество запросов, вытесненных из интегрированного кэша из-за истечения TTL | Region | Count |  |
| Integrated cache query hit rate | Количество запросов, использовавших интегрированный кэш, делённое на количество запросов, маршрутизированных через выделенный шлюз с eventual consistency | Region | Percent |  |
| Materialized view catchup gap in minutes | Максимальная разница во времени в минутах между данными в исходном контейнере и данными, переданными в материализованное представление | Region, Materialized view name | Count |  |
| Materialized views builder average CPU usage | Среднее использование ЦП на экземплярах построителя материализованных представлений | Region | Percent |  |
| Materialized views builder average memory usage | Среднее использование памяти на экземплярах построителя материализованных представлений | Region | Byte |  |
| Materialized views builder maximum CPU usage | Среднее максимальное использование ЦП на экземплярах построителя материализованных представлений | Region | Percent |  |
| Metadata requests | Количество запросов метаданных. Cosmos DB поддерживает коллекцию системных метаданных для каждой учётной записи, позволяющую перечислять коллекции, базы данных и т.д. и их конфигурации бесплатно. | Collection name, Database name, Region, Status code | Count | Применимо |
| Normalized ru consumption | Максимальный процент потребления RU в минуту | Collection name, Collection rid, Database name, Partition key range ID, Physical partition ID, Region | Percent | Применимо |
| Region offlined | Регион отключён | Region, Status code | Count |  |
| Region onlined | Регион включён | Region, Status code | Count |  |
| Physical partition size | Размер физического раздела в байтах | Collection name, Database name, Resource ID, Physical partition ID, Region | Byte |  |
| Physical partition throughput | Пропускная способность физического раздела | Collection name, Database name, Resource ID, Physical partition ID, Region | Count |  |
| Provisioned throughput | Выделенная пропускная способность | Collection name, Database name | Count | Применимо |
| Region failed over | Переключение региона |  | Count |  |
| Region removed | Регион удалён | Region | Count |  |
| P99 replication latency | Задержка репликации P99 между исходным и целевым регионами для учётной записи с поддержкой георепликации | Source region, Target region | MilliSecond |  |
| Server side latency | Задержка на стороне сервера | Collection name, Connection mode, Database name, Operation type, Publicapi type, Region | MilliSecond | Применимо |
| Server side latency direct | Задержка на стороне сервера в режиме прямого подключения | Collection name, Database name, Operation type, Publicapi type, Region | MilliSecond |  |
| Server side latency gateway | Задержка на стороне сервера в режиме подключения через шлюз | Collection name, Database name, Operation type, Publicapi type, Region | MilliSecond |  |
| Service availability | Доступность запросов учётной записи с гранулярностью в час, день или месяц |  | Percent | Применимо |
| SQL container created | Создан контейнер SQL | Container name, Database name | Count |  |
| SQL container deleted | Удалён контейнер SQL | Container name, Database name | Count |  |
| SQL container throughput updated | Обновлена пропускная способность контейнера SQL | Container name, Database name | Count |  |
| SQL container updated | Обновлён контейнер SQL | Container name, Database name | Count |  |
| SQL database created | Создана база данных SQL | Database name | Count |  |
| SQL database deleted | Удалена база данных SQL | Database name | Count |  |
| SQL database throughput updated | Обновлена пропускная способность базы данных SQL | Database name | Count |  |
| SQL database updated | Обновлена база данных SQL | Database name | Count |  |
| Azure table table created | Создана таблица AzureTable | Table name | Count |  |
| Azure table table deleted | Удалена таблица AzureTable | Table name | Count |  |
| Azure table table throughput updated | Обновлена пропускная способность таблицы AzureTable | Table name | Count |  |
| Azure table table updated | Обновлена таблица AzureTable | Table name | Count |  |
| Total requests | Количество выполненных запросов | Capacity type, Collection name, Database name, Operation type, Region, Status, Status code | Count | Применимо |
| Total requests (preview) | Количество SQL-запросов | Collection name, Database name, Operation type, Region, Status, Status code | Count |  |
| Total request units | Потреблённые единицы запросов SQL | Capacity type, Collection name, Database name, Operation type, Region, Status, Status code | Count | Применимо |
| Total request units (preview) | Единицы запросов, потреблённые с CapacityType | Capacity type, Collection name, Database name, Operation type, Region, Status, Status code | Count |  |
| Account keys updated | Ключи учётной записи обновлены | Key type | Count |  |
| Account network settings updated | Сетевые настройки учётной записи обновлены |  | Count |  |
| Account replication settings updated | Настройки репликации учётной записи обновлены |  | Count |  |
| Account diagnostic settings updated | Диагностические настройки учётной записи обновлены | Diagnostic settings name, Resource group name | Count |  |
