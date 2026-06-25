---
title: Мониторинг Azure Cosmos DB Account (GlobalDocumentDB)
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-cosmos-db-account-globaldocumentdb
scraped: 2026-05-12T11:27:09.454764
---

# Мониторинг Azure Cosmos DB Account (GlobalDocumentDB)

# Мониторинг Azure Cosmos DB Account (GlobalDocumentDB)

* Практическое руководство
* Чтение: 9 мин
* Обновлено 15 ноября 2023 г.

Информацию о различиях между классическими службами и другими службами см. в разделе [Миграция с классических служб Azure (ранее «встроенных») на облачные службы](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide "Перенос классических служб Azure на их новые версии.").

Dynatrace получает метрики из Azure Metrics API для Azure Cosmos DB Account (GlobalDocumentDB). Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать метрики по различным измерениям и создавать пользовательские графики, которые можно закрепить на ваших дашбордах.

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
| Region added | Добавление региона | Region | Количество |  |
| Autoscale max throughput | Максимальная пропускная способность автомасштабирования | Collection name, Database name | Количество | Применимо |
| Cassandra connection closures | Количество закрытых подключений Cassandra, регистрируется с детализацией в 1 минуту | Closure reason, Region | Количество |  |
| Cassandra connector average replication latency | Средняя задержка репликации коннектора Cassandra |  | Миллисекунда |  |
| Cassandra connector replication health status | Состояние работоспособности репликации коннектора Cassandra | Replication in error, Replication not started, Replication in progress | Количество |  |
| Cassandra keyspace created | Создание пространства ключей Cassandra | Keyspace name | Количество |  |
| Cassandra keyspace deleted | Удаление пространства ключей Cassandra | Keyspace name | Количество |  |
| Cassandra keyspace throughput updated | Обновление пропускной способности пространства ключей Cassandra | Keyspace name | Количество |  |
| Cassandra keyspace updated | Обновление пространства ключей Cassandra | Keyspace name | Количество |  |
| Cassandra request charges | Потреблено RU для выполненных запросов Cassandra | Collection name, Database name, Operation type, Region, Resource type | Количество |  |
| Cassandra requests | Количество выполненных запросов Cassandra | Collection name, Database name, Error code, Operation type, Region, Resource type | Количество |  |
| Cassandra table created | Создание таблицы Cassandra | Table name, Keyspace name | Количество |  |
| Cassandra table deleted | Удаление таблицы Cassandra | Table name, Keyspace name | Количество |  |
| Cassandra table throughput updated | Обновление пропускной способности таблицы Cassandra | Table name, Keyspace name | Количество |  |
| Cassandra table updated | Обновление таблицы Cassandra | Table name, Keyspace name | Количество |  |
| Account created | Создание учётной записи |  | Количество |  |
| Data usage | Общее использование данных, регистрируется с детализацией в 5 минут | Collection name, Database name, Region | Байт | Применимо |
| Dedicated gateway average CPU usage | Среднее использование ЦП по экземплярам выделенного шлюза | Region | Процент |  |
| Dedicated gateway average memory usage | Среднее использование памяти по экземплярам выделенного шлюза, которая используется как для маршрутизации запросов, так и для кэширования данных | Region | Байт |  |
| Dedicated gateway CPU usage | Использование ЦП по экземплярам выделенного шлюза | Region | Процент |  |
| Dedicated gateway maximum CPU usage | Среднее максимальное использование ЦП по экземплярам выделенного шлюза | Region | Процент |  |
| Dedicated gateway memory usage | Использование памяти по экземплярам выделенного шлюза | Region | Байт |  |
| Dedicated gateway requests | Запросы к выделенному шлюзу | Cache exercised, Cache hit, Collection name, Database name, Operation name, Region | Количество |  |
| Account deleted | Удаление учётной записи |  | Количество |  |
| Document count | Общее количество документов, регистрируется с детализацией в 5 минут, 1 час и 1 день | Collection name, Database name, Region | Количество | Применимо |
| Document quota | Общая квота хранилища, регистрируется с детализацией в 5 минут | Collection name, Database name, Region | Байт | Применимо |
| Gremlin database created | Создание базы данных Gremlin | Database name | Количество |  |
| Gremlin database deleted | Удаление базы данных Gremlin | Database name | Количество |  |
| Gremlin database throughput updated | Обновление пропускной способности базы данных Gremlin | Database name | Количество |  |
| Gremlin database updated | Обновление базы данных Gremlin | Database name | Количество |  |
| Gremlin graph created | Создание графа Gremlin | Graph name, Database name | Количество |  |
| Gremlin graph deleted | Удаление графа Gremlin | Graph name, Database name | Количество |  |
| Gremlin graph throughput updated | Обновление пропускной способности графа Gremlin | Graph name, Database name | Количество |  |
| Gremlin graph updated | Обновление графа Gremlin | Graph name, Database name | Количество |  |
| Gremlin request charges | Потреблено единиц запросов для выполненных запросов Gremlin | Collection name, Database name, Region | Количество |  |
| Gremlin requests | Количество выполненных запросов Gremlin | Collection name, Database name, Error code, Region | Количество |  |
| Index usage | Общее использование индекса, регистрируется с детализацией в 5 минут | Collection name, Database name, Region | Байт | Применимо |
| Integrated cache evicted entries size | Размер записей, вытесненных из интегрированного кэша | Region | Байт |  |
| Integrated cache item expiration count | Количество элементов, вытесненных из интегрированного кэша из-за истечения TTL | Region | Количество |  |
| Integrated cache item hit rate | Количество точечных чтений, использовавших интегрированный кэш, делённое на количество точечных чтений, направленных через выделенный шлюз с итоговой согласованностью | Region | Процент |  |
| Integrated cache query expiration count | Количество запросов, вытесненных из интегрированного кэша из-за истечения TTL | Region | Количество |  |
| Integrated cache query hit rate | Количество запросов, использовавших интегрированный кэш, делённое на количество запросов, направленных через выделенный шлюз с итоговой согласованностью | Region | Процент |  |
| Materialized view catchup gap in minutes | Максимальная разница во времени (в минутах) между данными в исходном контейнере и данными, перенесёнными в материализованное представление | Region, Materialized view name | Количество |  |
| Materialized views builder average CPU usage | Среднее использование ЦП по экземплярам построителя материализованных представлений, которые используются для заполнения данных в материализованных представлениях | Region | Процент |  |
| Materialized views builder average memory usage | Среднее использование памяти по экземплярам построителя материализованных представлений, которые используются для заполнения данных в материализованных представлениях | Region | Байт |  |
| Materialized views builder maximum CPU usage | Среднее максимальное использование ЦП по экземплярам построителя материализованных представлений, которые используются для заполнения данных в материализованных представлениях | Region | Процент |  |
| Metadata requests | Количество запросов метаданных. Cosmos DB поддерживает коллекцию системных метаданных для каждой учётной записи, что позволяет бесплатно перечислять коллекции, базы данных и т. д., а также их конфигурации. | Collection name, Database name, Region, Status code | Количество | Применимо |
| Normalized ru consumption | Максимальный процент потребления RU в минуту | Collection name, Collection rid, Database name, Partition key range ID, Physical partition ID, Region | Процент | Применимо |
| Region offlined | Перевод региона в автономный режим | Region, Status code | Количество |  |
| Region onlined | Перевод региона в оперативный режим | Region, Status code | Количество |  |
| Physical partition size | Размер физического раздела в байтах | Collection name, Database name, Resource ID, Physical partition ID, Region | Байт |  |
| Physical partition throughput | Пропускная способность физического раздела | Collection name, Database name, Resource ID, Physical partition ID, Region | Количество |  |
| Provisioned throughput | Подготовленная пропускная способность | Collection name, Database name | Количество | Применимо |
| Region failed over | Переключение региона при отказе |  | Количество |  |
| Region removed | Удаление региона | Region | Количество |  |
| P99 replication latency | Задержка репликации P99 между исходным и целевым регионами для учётной записи с поддержкой геораспределения | Source region, Target region | Миллисекунда |  |
| Server side latency | Задержка на стороне сервера | Collection name, Connection mode, Database name, Operation type, Publicapi type, Region | Миллисекунда | Применимо |
| Server side latency direct | Задержка на стороне сервера в режиме прямого подключения | Collection name, Database name, Operation type, Publicapi type, Region | Миллисекунда |  |
| Server side latency gateway | Задержка на стороне сервера в режиме подключения через шлюз | Collection name, Database name, Operation type, Publicapi type, Region | Миллисекунда |  |
| Service availability | Доступность запросов к учётной записи с детализацией по часу, дню или месяцу |  | Процент | Применимо |
| SQL container created | Создание контейнера SQL | Container name, Database name | Количество |  |
| SQL container deleted | Удаление контейнера SQL | Container name, Database name | Количество |  |
| SQL container throughput updated | Обновление пропускной способности контейнера SQL | Container name, Database name | Количество |  |
| SQL container updated | Обновление контейнера SQL | Container name, Database name | Количество |  |
| SQL database created | Создание базы данных SQL | Database name | Количество |  |
| SQL database deleted | Удаление базы данных SQL | Database name | Количество |  |
| SQL database throughput updated | Обновление пропускной способности базы данных SQL | Database name | Количество |  |
| SQL database updated | Обновление базы данных SQL | Database name | Количество |  |
| Azure table table created | Создание таблицы AzureTable | Table name | Количество |  |
| Azure table table deleted | Удаление таблицы AzureTable | Table name | Количество |  |
| Azure table table throughput updated | Обновление пропускной способности таблицы AzureTable | Table name | Количество |  |
| Azure table table updated | Обновление таблицы AzureTable | Table name | Количество |  |
| Total requests | Количество выполненных запросов | Capacity type, Collection name, Database name, Operation type, Region, Status, Status code | Количество | Применимо |
| Total requests (preview) | Количество запросов SQL | Collection name, Database name, Operation type, Region, Status, Status code | Количество |  |
| Total request units | Потреблено единиц запросов SQL | Capacity type, Collection name, Database name, Operation type, Region, Status, Status code | Количество | Применимо |
| Total request units (preview) | Потреблено единиц запросов с учётом CapacityType | Capacity type, Collection name, Database name, Operation type, Region, Status, Status code | Количество |  |
| Account keys updated | Обновление ключей учётной записи | Key type | Количество |  |
| Account network settings updated | Обновление сетевых настроек учётной записи |  | Количество |  |
| Account replication settings updated | Обновление настроек репликации учётной записи |  | Количество |  |
| Account diagnostic settings updated | Обновление настроек диагностики учётной записи | Diagnostic settings name, Resource group name | Количество |  |