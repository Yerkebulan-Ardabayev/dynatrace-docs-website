---
title: Классические (ранее «встроенные») метрики Azure
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/default-azure-metrics
scraped: 2026-03-06T21:31:33.010747
---

# Классические (ранее «встроенные») метрики Azure

# Классические (ранее «встроенные») метрики Azure

* Последняя версия Dynatrace
* Справочник
* Чтение: 1 мин
* Обновлено 29 янв. 2024

Информацию о различиях между классическими сервисами и другими сервисами см. в разделе [Миграция с классических (ранее «встроенных») сервисов Azure на облачные сервисы](azure-migration-guide.md "Миграция классических сервисов Azure на новые версии.").

В таблице ниже перечислены все метрики Azure, которые Dynatrace собирает по умолчанию при включении мониторинга [Microsoft Azure](../azure-monitoring-guide.md "Настройка и конфигурация мониторинга Azure в Dynatrace.").

Все остальные метрики, собираемые Dynatrace для настраиваемых сервисов Azure, см. на страницах [облачных сервисов](../azure-cloud-services-metrics.md "Мониторинг сервисов Azure с помощью Dynatrace и просмотр доступных метрик.").

| Ключ метрики | Название | Единица измерения | Агрегации |
| --- | --- | --- | --- |
| builtin:cloud.azure.apiMgmt.requests.failed | Неуспешные запросы | Count | autoavgcountmaxminsum |
| builtin:cloud.azure.apiMgmt.requests.other | Прочие запросы | Count | autoavgcountmaxminsum |
| builtin:cloud.azure.apiMgmt.requests.successful | Успешные запросы | Count | autoavgcountmaxminsum |
| builtin:cloud.azure.apiMgmt.requests.total | Всего запросов | Count | autoavgcountmaxminsum |
| builtin:cloud.azure.apiMgmt.requests.unauth | Неавторизованные запросы | Count | autoavgcountmaxminsum |
| builtin:cloud.azure.apiMgmt.capacity | Ёмкость | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.apiMgmt.duration | Длительность | Millisecond | autoavgmaxmin |
| builtin:cloud.azure.appGateway.backend.settings.pool.host.healthy | Количество работоспособных хостов | Count | autoavgmaxmin |
| builtin:cloud.azure.appGateway.backend.settings.pool.host.unhealthy | Количество неработоспособных хостов | Count | autoavgmaxmin |
| builtin:cloud.azure.appGateway.backend.settings.traffic.requests.failed | Неуспешные запросы | Count | autovalue |
| builtin:cloud.azure.appGateway.backend.settings.traffic.requests.total | Всего запросов | Count | autovalue |
| builtin:cloud.azure.appGateway.http.status.response | Статус ответа | Count | autovalue |
| builtin:cloud.azure.appGateway.network.connections.count | Текущее количество соединений | Count | autoavgmaxmin |
| builtin:cloud.azure.appGateway.network.throughput | Пропускная способность сети | Byte/second | autoavgmaxmin |
| builtin:cloud.azure.appService.applicationQueue.requests | Запросы в очереди приложения | Count | autoavgmaxmin |
| builtin:cloud.azure.appService.functions.applicationQueue.requests | Запросы в очереди приложения | Count | autoavgmaxmin |
| builtin:cloud.azure.appService.functions.execution.count | Количество выполнений функции | Count | autovalue |
| builtin:cloud.azure.appService.functions.execution.unitsCount | Количество единиц выполнения функции | Count | autovalue |
| builtin:cloud.azure.appService.functions.http.status.http5xx | HTTP 5xx | Count | autovalue |
| builtin:cloud.azure.appService.functions.io.operations.other | Прочие операции ввода-вывода/с | Per second | autoavgmaxmin |
| builtin:cloud.azure.appService.functions.io.operations.read | Операции чтения ввода-вывода/с | Per second | autoavgmaxmin |
| builtin:cloud.azure.appService.functions.io.operations.write | Операции записи ввода-вывода/с | Per second | autoavgmaxmin |
| builtin:cloud.azure.appService.functions.io.other | Прочие байты ввода-вывода/с | Byte/second | autoavgmaxmin |
| builtin:cloud.azure.appService.functions.io.read | Чтение ввода-вывода байт/с | Byte/second | autoavgmaxmin |
| builtin:cloud.azure.appService.functions.io.write | Запись ввода-вывода байт/с | Byte/second | autoavgmaxmin |
| builtin:cloud.azure.appService.functions.traffic.bytesReceived | Полученные байты | Byte | autovalue |
| builtin:cloud.azure.appService.functions.traffic.bytesSent | Отправленные байты | Byte | autovalue |
| builtin:cloud.azure.appService.http.status.http2xx | HTTP 2xx | Count | autovalue |
| builtin:cloud.azure.appService.http.status.http403 | HTTP 403 | Count | autovalue |
| builtin:cloud.azure.appService.http.status.http5xx | HTTP 5xx | Count | autovalue |
| builtin:cloud.azure.appService.io.operations.other | Прочие операции ввода-вывода/с | Per second | autoavgmaxmin |
| builtin:cloud.azure.appService.io.operations.read | Операции чтения ввода-вывода/с | Per second | autoavgmaxmin |
| builtin:cloud.azure.appService.io.operations.write | Операции записи ввода-вывода/с | Per second | autoavgmaxmin |
| builtin:cloud.azure.appService.io.other | Прочие байты ввода-вывода/с | Byte/second | autoavgmaxmin |
| builtin:cloud.azure.appService.io.read | Чтение ввода-вывода байт/с | Byte/second | autoavgmaxmin |
| builtin:cloud.azure.appService.io.write | Запись ввода-вывода байт/с | Byte/second | autoavgmaxmin |
| builtin:cloud.azure.appService.response.avg | Среднее время ответа | Second | autoavgmaxmin |
| builtin:cloud.azure.appService.traffic.bytesReceived | Полученные байты | Byte | autovalue |
| builtin:cloud.azure.appService.traffic.bytesSent | Отправленные байты | Byte | autovalue |
| builtin:cloud.azure.appService.traffic.requests | Количество запросов | Count | autovalue |
| builtin:cloud.azure.cosmos.availableStorage | Доступное хранилище | Byte | autoavgmaxmin |
| builtin:cloud.azure.cosmos.dataUsage | Использование данных | Byte | autoavgmaxmin |
| builtin:cloud.azure.cosmos.documentCount | Количество документов | Count | autoavgmaxmin |
| builtin:cloud.azure.cosmos.documentQuota | Квота документов | Byte | autoavgmaxmin |
| builtin:cloud.azure.cosmos.indexUsage | Использование индекса | Byte | autoavgmaxmin |
| builtin:cloud.azure.cosmos.metadataRequests | Запросы метаданных | Count | autoavgmaxmin |
| builtin:cloud.azure.cosmos.normalizedRUConsumption | Нормализованное потребление единиц запросов | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.cosmos.provisionedThroughput | Предоставленная пропускная способность | Count | autoavgmaxmin |
| builtin:cloud.azure.cosmos.replicationLatency | Задержка репликации | Millisecond | autoavgmaxmin |
| builtin:cloud.azure.cosmos.requestUnits | Общее количество единиц запросов | Count | autoavgmaxmin |
| builtin:cloud.azure.cosmos.requests | Общее количество запросов | Count | autoavgmaxmin |
| builtin:cloud.azure.cosmos.serviceAvailability | Доступность сервиса | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.eventHub.capture.backlog | Бэклог захвата | Count | autovalue |
| builtin:cloud.azure.eventHub.capture.bytes | Захваченные байты | Byte | autovalue |
| builtin:cloud.azure.eventHub.capture.msg | Захваченные сообщения | Count | autovalue |
| builtin:cloud.azure.eventHub.errors.quotaExceeded | Ошибки превышения квоты | Count | autovalue |
| builtin:cloud.azure.eventHub.errors.server | Серверные ошибки | Count | autovalue |
| builtin:cloud.azure.eventHub.errors.user | Пользовательские ошибки | Count | autovalue |
| builtin:cloud.azure.eventHub.requests.incoming | Входящие запросы | Count | autovalue |
| builtin:cloud.azure.eventHub.requests.successful | Успешные запросы | Count | autovalue |
| builtin:cloud.azure.eventHub.requests.throttled | Ограниченные запросы | Count | autovalue |
| builtin:cloud.azure.eventHub.traffic.bytesIn | Входящие байты | Byte/minute | autovalue |
| builtin:cloud.azure.eventHub.traffic.bytesOut | Исходящие байты | Byte | autovalue |
| builtin:cloud.azure.eventHub.traffic.msgIn | Входящие сообщения | Count | autovalue |
| builtin:cloud.azure.eventHub.traffic.msgOut | Исходящие сообщения | Count | autovalue |
| builtin:cloud.azure.eventHubNamespace.connections.active | Активные соединения | Count | autoavgmaxmin |
| builtin:cloud.azure.eventHubNamespace.connections.closed | Закрытые соединения | Count | autoavgmaxmin |
| builtin:cloud.azure.eventHubNamespace.connections.opened | Открытые соединения | Count | autoavgmaxmin |
| builtin:cloud.azure.iotHub.command.abandoned | Оставленные команды | Count | autovalue |
| builtin:cloud.azure.iotHub.command.completed | Выполненные команды | Count | autovalue |
| builtin:cloud.azure.iotHub.command.rejected | Отклонённые команды | Count | autovalue |
| builtin:cloud.azure.iotHub.device.connected | Подключённые устройства | Count | autoavgmaxmin |
| builtin:cloud.azure.iotHub.device.dailyThroughputThrottling | Количество ошибок ограничения | Count | autovalue |
| builtin:cloud.azure.iotHub.device.dataUsage | Общее использование данных устройствами | Byte | autoavgmaxmin |
| builtin:cloud.azure.iotHub.device.registered | Всего устройств | Count | autoavgmaxmin |
| builtin:cloud.azure.iotHub.eventHub.builtInEventHub.messages.delivered | Сообщения, доставленные во встроенную конечную точку (messages/events) | Count | autovalue |
| builtin:cloud.azure.iotHub.eventHub.builtInEventHub.averageLatencyMs | Задержка сообщений для встроенной конечной точки (messages/events) | Millisecond | autoavgmaxmin |
| builtin:cloud.azure.iotHub.eventHub.messages.delivered | Сообщения, доставленные в конечные точки Event Hub | Count | autovalue |
| builtin:cloud.azure.iotHub.eventHub.averageLatencyMs | Задержка сообщений для конечных точек Event Hub | Millisecond | autoavgmaxmin |
| builtin:cloud.azure.iotHub.messages.dropped | Удалённые сообщения | Count | autovalue |
| builtin:cloud.azure.iotHub.messages.invalidForAllEndpoints | Недопустимые сообщения | Count | autovalue |
| builtin:cloud.azure.iotHub.messages.orphaned | Осиротевшие сообщения | Count | autovalue |
| builtin:cloud.azure.iotHub.messages.sendAttempts | Попытки отправки телеметрических сообщений | Count | autovalue |
| builtin:cloud.azure.iotHub.messages.sent | Отправленные телеметрические сообщения | Count | autovalue |
| builtin:cloud.azure.iotHub.messages.sentToFallback | Сообщения, соответствующие резервному условию | Count | autovalue |
| builtin:cloud.azure.iotHub.serviceBus.queues.averageLatencyMs | Задержка сообщений для конечных точек очередей Service Bus | Millisecond | autoavgmaxmin |
| builtin:cloud.azure.iotHub.serviceBus.queues.messagesDelivered | Сообщения, доставленные в конечные точки очередей Service Bus | Count | autovalue |
| builtin:cloud.azure.iotHub.serviceBus.topics.averageLatencyMs | Задержка сообщений для конечных точек топиков Service Bus | Millisecond | autoavgmaxmin |
| builtin:cloud.azure.iotHub.serviceBus.topics.messagesDelivered | Сообщения, доставленные в конечные точки топиков Service Bus | Count | autovalue |
| builtin:cloud.azure.iotHub.storageEndpoints.avgLatencyMs | Задержка сообщений для конечных точек хранилища | Millisecond | autoavgmaxmin |
| builtin:cloud.azure.iotHub.storageEndpoints.blobsWritten | Blob-объекты, записанные в хранилище | Count | autovalue |
| builtin:cloud.azure.iotHub.storageEndpoints.bytesWritten | Данные, записанные в хранилище | Byte | autoavgmaxmin |
| builtin:cloud.azure.iotHub.storageEndpoints.messageDelivered | Сообщения, доставленные в конечные точки хранилища | Count | autovalue |
| builtin:cloud.azure.loadbalancer.availability.dipTcp | Доступность DIP TCP балансировщика нагрузки | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.loadbalancer.availability.dipUdp | Доступность DIP UDP балансировщика нагрузки | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.loadbalancer.availability.vip | Доступность VIP балансировщика нагрузки | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.loadbalancer.snatConnection.est | Успешные SNAT-соединения | Count | autovalue |
| builtin:cloud.azure.loadbalancer.snatConnection.pending | Ожидающие SNAT-соединения | Count | autovalue |
| builtin:cloud.azure.loadbalancer.snatConnection.rej | Неуспешные SNAT-соединения | Count | autovalue |
| builtin:cloud.azure.loadbalancer.traffic.byteIn | Полученные байты | Byte | autovalue |
| builtin:cloud.azure.loadbalancer.traffic.byteOut | Отправленные байты | Byte | autovalue |
| builtin:cloud.azure.loadbalancer.traffic.packetIn | Полученные пакеты | Count | autovalue |
| builtin:cloud.azure.loadbalancer.traffic.packetOut | Отправленные пакеты | Count | autovalue |
| builtin:cloud.azure.loadbalancer.traffic.packetSynIn | Полученные SYN-пакеты | Count | autovalue |
| builtin:cloud.azure.loadbalancer.traffic.packetSynOut | Отправленные SYN-пакеты | Count | autovalue |
| builtin:cloud.azure.redis.cache.hits | Попадания в кэш | Count | autovalue |
| builtin:cloud.azure.redis.cache.misses | Промахи кэша | Count | autovalue |
| builtin:cloud.azure.redis.cache.read | Чтение байт/с | Byte/second | autoavgmaxmin |
| builtin:cloud.azure.redis.cache.write | Запись байт/с | Byte/second | autoavgmaxmin |
| builtin:cloud.azure.redis.commands.get | Команды Get | Count | autovalue |
| builtin:cloud.azure.redis.commands.set | Команды Set | Count | autovalue |
| builtin:cloud.azure.redis.commands.total | Общее количество обработанных команд | Count | autovalue |
| builtin:cloud.azure.redis.keys.evicted | Количество вытесненных ключей | Count | autovalue |
| builtin:cloud.azure.redis.keys.expired | Количество истёкших ключей | Count | autovalue |
| builtin:cloud.azure.redis.keys.total | Общее количество ключей | Count | autoavgmaxmin |
| builtin:cloud.azure.redis.memory.used | Используемая память | Byte | autoavgmaxmin |
| builtin:cloud.azure.redis.memory.usedRss | Используемая память RSS | Byte | autoavgmaxmin |
| builtin:cloud.azure.redis.connected | Подключённые клиенты | Count | autoavgmaxmin |
| builtin:cloud.azure.redis.load | Нагрузка на сервер | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.redis.processorTime | Процессорное время | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.region.vms.initializing | Количество запускающихся ВМ в регионе | Count | autoavgmaxmin |
| builtin:cloud.azure.region.vms.running | Количество активных ВМ в регионе | Count | autoavgmaxmin |
| builtin:cloud.azure.region.vms.stopped | Количество остановленных ВМ в регионе | Count | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.namespace.connections.active | Всего активных соединений | Count | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.namespace.errors.server | Серверные ошибки | Count | autovalue |
| builtin:cloud.azure.serviceBus.namespace.errors.user | Пользовательские ошибки | Count | autovalue |
| builtin:cloud.azure.serviceBus.namespace.messages.count | Количество сообщений | Count | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.namespace.messages.countActive | Количество активных сообщений | Count | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.namespace.messages.countDeadLettered | Количество сообщений dead-letter | Count | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.namespace.messages.countScheduled | Количество запланированных сообщений | Count | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.namespace.messages.incoming | Входящие сообщения | Count | autovalue |
| builtin:cloud.azure.serviceBus.namespace.messages.outgoing | Исходящие сообщения | Count | autovalue |
| builtin:cloud.azure.serviceBus.namespace.requests.incoming | Входящие запросы | Count | autovalue |
| builtin:cloud.azure.serviceBus.namespace.requests.successful | Всего успешных запросов | Count | autovalue |
| builtin:cloud.azure.serviceBus.namespace.requests.throttled | Ограниченные запросы | Count | autovalue |
| builtin:cloud.azure.serviceBus.namespace.cpu | Метрика использования CPU пространства имён Service Bus Premium | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.namespace.memory | Метрика использования памяти пространства имён Service Bus Premium | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.namespace.size | Размер Service Bus | Byte | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.queue.errors.server | Серверные ошибки | Count | autovalue |
| builtin:cloud.azure.serviceBus.queue.errors.user | Пользовательские ошибки | Count | autovalue |
| builtin:cloud.azure.serviceBus.queue.messages.count | Количество сообщений в очереди | Count | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.queue.messages.countActive | Количество активных сообщений в очереди | Count | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.queue.messages.countDeadLettered | Количество сообщений dead-letter в очереди | Count | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.queue.messages.countScheduled | Количество запланированных сообщений в очереди | Count | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.queue.messages.incoming | Входящие сообщения | Count | autovalue |
| builtin:cloud.azure.serviceBus.queue.messages.outgoing | Исходящие сообщения | Count | autovalue |
| builtin:cloud.azure.serviceBus.queue.requests.incoming | Входящие запросы | Count | autovalue |
| builtin:cloud.azure.serviceBus.queue.requests.successful | Всего успешных запросов | Count | autovalue |
| builtin:cloud.azure.serviceBus.queue.requests.throttled | Ограниченные запросы | Count | autovalue |
| builtin:cloud.azure.serviceBus.queue.size | Размер очереди | Byte | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.topic.errors.server | Серверные ошибки | Count | autovalue |
| builtin:cloud.azure.serviceBus.topic.errors.user | Пользовательские ошибки | Count | autovalue |
| builtin:cloud.azure.serviceBus.topic.messages.count | Количество сообщений в топике | Count | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.topic.messages.countActive | Количество активных сообщений в топике | Count | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.topic.messages.countDeadLettered | Количество сообщений dead-letter в топике | Count | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.topic.messages.countScheduled | Количество запланированных сообщений в топике | Count | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.topic.messages.incoming | Входящие сообщения | Count | autovalue |
| builtin:cloud.azure.serviceBus.topic.messages.outgoing | Исходящие сообщения | Count | autovalue |
| builtin:cloud.azure.serviceBus.topic.requests.incoming | Входящие запросы | Count | autovalue |
| builtin:cloud.azure.serviceBus.topic.requests.successful | Всего успешных запросов | Count | autovalue |
| builtin:cloud.azure.serviceBus.topic.requests.throttled | Ограниченные запросы | Count | autovalue |
| builtin:cloud.azure.serviceBus.topic.size | Размер топика | Byte | autoavgmaxmin |
| builtin:cloud.azure.sqlDatabase.connections.blockedByFirewall | Заблокировано межсетевым экраном | Count | autovalue |
| builtin:cloud.azure.sqlDatabase.connections.failed | Неуспешные подключения | Count | autovalue |
| builtin:cloud.azure.sqlDatabase.connections.successful | Успешные подключения | Count | autovalue |
| builtin:cloud.azure.sqlDatabase.dtu.limit.count | Лимит DTU | Count | autoavgmaxmin |
| builtin:cloud.azure.sqlDatabase.dtu.limit.used | Использовано DTU | Count | autoavgmaxmin |
| builtin:cloud.azure.sqlDatabase.dtu.consumptionPerc | Процент DTU | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlDatabase.io.dataRead | Процент ввода-вывода данных | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlDatabase.io.logWrite | Процент ввода-вывода журнала | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlDatabase.storage.percent | Процент размера базы данных | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlDatabase.storage.totalBytes | Общий размер базы данных | Byte | autoavgmaxmin |
| builtin:cloud.azure.sqlDatabase.storage.xtpPercent | Процент хранилища In-Memory OLTP | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlDatabase.cpuPercent | Процент CPU | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlDatabase.deadlocks | Взаимоблокировки | Count | autovalue |
| builtin:cloud.azure.sqlDatabase.sessions | Процент сессий | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlDatabase.workers | Процент рабочих процессов | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlElasticPool.dtu.storage.limitBytes | Лимит хранилища | Byte | autoavgmaxmin |
| builtin:cloud.azure.sqlElasticPool.dtu.storage.percent | Процент размера базы данных | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlElasticPool.dtu.storage.usedBytes | Использовано хранилища | Byte | autoavgmaxmin |
| builtin:cloud.azure.sqlElasticPool.dtu.storage.xtpPercent | Процент хранилища In-Memory OLTP | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlElasticPool.dtu.consumption | Процент DTU | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlElasticPool.edtu.limit | Лимит eDTU | Count | autoavgmaxmin |
| builtin:cloud.azure.sqlElasticPool.edtu.used | Использовано eDTU | Count | autoavgmaxmin |
| builtin:cloud.azure.sqlElasticPool.io.dataRead | Процент ввода-вывода данных | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlElasticPool.io.logWrite | Процент ввода-вывода журнала | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlElasticPool.cpuPercent | Процент CPU | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlElasticPool.sessions | Процент сессий | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlElasticPool.workers | Процент рабочих процессов | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.vm.disk.read | Байты чтения диска | Byte | autovalue |
| builtin:cloud.azure.vm.disk.readOps | Операции чтения диска в секунду | Per second | autoavgmaxmin |
| builtin:cloud.azure.vm.disk.write | Байты записи диска | Byte | autovalue |
| builtin:cloud.azure.vm.disk.writeOps | Операции записи диска в секунду | Per second | autoavgmaxmin |
| builtin:cloud.azure.vm.network.bytesIn | Входящие байты сети | Byte | autovalue |
| builtin:cloud.azure.vm.network.bytesOut | Исходящие байты сети | Byte | autovalue |
| builtin:cloud.azure.vm.cpuUsage | Процент CPU | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.vmScaleSet.disk.read | Байты чтения диска | Byte | autovalue |
| builtin:cloud.azure.vmScaleSet.disk.readOps | Операции чтения диска в секунду | Per second | autoavgmaxmin |
| builtin:cloud.azure.vmScaleSet.disk.write | Байты записи диска | Byte | autovalue |
| builtin:cloud.azure.vmScaleSet.disk.writeOps | Операции записи диска в секунду | Per second | autoavgmaxmin |
| builtin:cloud.azure.vmScaleSet.network.bytesIn | Входящие байты сети | Byte | autovalue |
| builtin:cloud.azure.vmScaleSet.network.bytesOut | Исходящие байты сети | Byte | autovalue |
| builtin:cloud.azure.vmScaleSet.vms.initializing | Количество запускающихся ВМ в масштабируемом наборе | Count | autoavgmaxmin |
| builtin:cloud.azure.vmScaleSet.vms.running | Количество активных ВМ в масштабируемом наборе | Count | autoavgmaxmin |
| builtin:cloud.azure.vmScaleSet.vms.stopped | Количество остановленных ВМ в масштабируемом наборе | Count | autoavgmaxmin |
| builtin:cloud.azure.vmScaleSet.cpuUsage | Процент CPU | Percent (%) | autoavgmaxmin |
