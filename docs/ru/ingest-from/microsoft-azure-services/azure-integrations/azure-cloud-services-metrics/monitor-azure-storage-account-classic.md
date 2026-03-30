---
title: Мониторинг Azure Storage Account Classic (Blob, File, Queue, Table)
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account-classic
scraped: 2026-03-03T21:26:08.787453
---

* Актуальная версия Dynatrace

Dynatrace собирает метрики для множества предварительно выбранных пространств имён, включая Azure Storage Account Classic. Вы можете просматривать метрики для каждого экземпляра сервиса, разделять метрики по различным измерениям и создавать пользовательские диаграммы, которые можно закрепить на дашбордах.

## Предварительные требования

* Dynatrace версии 1.196+
* Environment ActiveGate версии 1.195+

Этот сервис мониторит часть Storage Account Classic (`Microsoft.ClassicStorage/storageAccounts`). Вы можете найти уже отслеживаемые ресурсы на обзорной странице Azure в разделе **Cloud services** или использовать предустановленный дашборд.

Для мониторинга ресурсов типа `Microsoft.Storage/storageAccounts` (включая Storage, StorageV2 и BlobStorage) ознакомьтесь со Storage Accounts и разделом **Storage accounts** на обзорной странице Azure.

## Включение мониторинга

Чтобы узнать, как включить мониторинг сервиса, см. Включение мониторинга сервиса.

## Просмотр метрик сервиса

Вы можете просматривать метрики сервиса в среде Dynatrace на **странице обзора пользовательского устройства** или на странице **Dashboards**.

### Просмотр метрик на странице обзора пользовательского устройства

Для доступа к странице обзора пользовательского устройства

1. Перейдите в ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Отфильтруйте по имени сервиса и выберите соответствующую группу пользовательских устройств.
3. После выбора группы пользовательских устройств вы окажетесь на **странице обзора группы пользовательских устройств**.
4. **Страница обзора группы пользовательских устройств** содержит список всех экземпляров (пользовательских устройств), принадлежащих группе. Выберите экземпляр для просмотра **страницы обзора пользовательского устройства**.

### Просмотр метрик на дашборде

Если у сервиса есть предустановленный дашборд, вы получите предустановленный дашборд для соответствующего сервиса со всеми рекомендуемыми метриками на странице **Dashboards**. Вы можете искать конкретные дашборды, фильтруя по **Preset**, а затем по **Name**.

Для существующих отслеживаемых сервисов может потребоваться повторное сохранение учётных данных, чтобы предустановленный дашборд появился на странице **Dashboards**. Чтобы повторно сохранить учётные данные, перейдите в **Settings** > **Cloud and virtualization** > **Azure**, выберите нужный экземпляр Azure, затем выберите **Save**.

Вы не можете вносить изменения в предустановленный дашборд напрямую, но можете клонировать и отредактировать его. Чтобы клонировать дашборд, откройте меню (**…**) и выберите **Clone**.
Чтобы удалить дашборд из списка, вы можете скрыть его. Чтобы скрыть дашборд, откройте меню (**…**) и выберите **Hide**.

Скрытие дашборда не влияет на других пользователей.

![Клонирование и скрытие Azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Storage Account Classic](https://dt-cdn.net/images/storageaccountnew-2908-6a758a1c35.png)

## Доступные метрики

**Storage Account (Classic)**

| Название | Описание | Единица | Измерения | Рекомендуется |
| --- | --- | --- | --- | --- |
| Availability | Процент доступности сервиса хранения или указанной операции API. Доступность рассчитывается путём деления значения TotalBillableRequests на количество применимых запросов, включая те, которые привели к непредвиденным ошибкам. Все непредвиденные ошибки приводят к снижению доступности сервиса хранения или указанной операции API. | Percent | Authentication, GeoType, ApiName | Applicable |
| Egress | Объём исходящих данных в байтах. Это число включает исходящий трафик от внешнего клиента в Azure Storage, а также исходящий трафик внутри Azure. Поэтому это число не отражает тарифицируемый исходящий трафик. | Byte | Authentication, GeoType, ApiName | Applicable |
| Ingress | Объём входящих данных в байтах. Это число включает входящий трафик от внешнего клиента в Azure Storage, а также входящий трафик внутри Azure. | Byte | Authentication, GeoType, ApiName | Applicable |
| SuccessE2ELatency | Сквозная задержка успешных запросов к сервису хранения или указанной операции API в миллисекундах. Это значение включает необходимое время обработки в Azure Storage для чтения запроса, отправки ответа и получения подтверждения ответа. | MilliSecond | Authentication, GeoType, ApiName | Applicable |
| SuccessServerLatency | Задержка обработки успешного запроса в Azure Storage в миллисекундах. Это значение не включает сетевую задержку, указанную в SuccessE2ELatency. | MilliSecond | Authentication, GeoType, ApiName |  |
| Transactions | Количество запросов к сервису хранения или указанной операции API. Это число включает успешные и неудачные запросы, а также запросы, вызвавшие ошибки. Используйте измерение ResponseType для подсчёта различных типов ответов. | Count | Authentication, GeoType, ResponseType, ApiName | Applicable |
| UsedCapacity | Используемая ёмкость учётной записи. | Byte |  | Applicable |

**Azure Storage Blob Services (Classic)**

Этот сервис мониторит часть Storage Account Classic (Microsoft.ClassicStorage/storageAccounts). Вы можете найти уже отслеживаемые ресурсы на обзорной странице Azure в разделе `Cloud services` или использовать предустановленный дашборд. Для мониторинга ресурсов типа Microsoft.Storage/storageAccounts (включая Storage, StorageV2 и BlobStorage) ознакомьтесь со Storage Accounts и разделом `Storage accounts` на обзорной странице Azure.

| Название | Описание | Единица | Измерения | Рекомендуется |
| --- | --- | --- | --- | --- |
| Availability | Процент доступности сервиса хранения или указанной операции API. Доступность рассчитывается путём деления значения TotalBillableRequests на количество применимых запросов, включая те, которые привели к непредвиденным ошибкам. Все непредвиденные ошибки приводят к снижению доступности сервиса хранения или указанной операции API. | Percent | Authentication, GeoType, ApiName | Applicable |
| BlobCapacity | Объём хранилища, используемый сервисом Blob учётной записи хранения, в байтах. | Byte | BlobType | Applicable |
| BlobCount | Количество объектов Blob в сервисе Blob учётной записи хранения. | Count | BlobType | Applicable |
| ContainerCount | Количество контейнеров в сервисе Blob учётной записи хранения. | Count |  | Applicable |
| Egress | Объём исходящих данных в байтах. Это число включает исходящий трафик от внешнего клиента в Azure Storage, а также исходящий трафик внутри Azure. Поэтому это число не отражает тарифицируемый исходящий трафик. | Byte | Authentication, GeoType, ApiName | Applicable |
| IndexCapacity | Объём хранилища, используемый индексом ADLS Gen2 (иерархический), в байтах. | Byte |  |  |
| Ingress | Объём входящих данных в байтах. Это число включает входящий трафик от внешнего клиента в Azure Storage, а также входящий трафик внутри Azure. | Byte | Authentication, GeoType, ApiName | Applicable |
| SuccessE2ELatency | Сквозная задержка успешных запросов к сервису хранения или указанной операции API в миллисекундах. Это значение включает необходимое время обработки в Azure Storage для чтения запроса, отправки ответа и получения подтверждения ответа. | MilliSecond | Authentication, GeoType, ApiName | Applicable |
| SuccessServerLatency | Задержка обработки успешного запроса в Azure Storage в миллисекундах. Это значение не включает сетевую задержку, указанную в SuccessE2ELatency. | MilliSecond | Authentication, GeoType, ApiName |  |
| Transactions | Количество запросов к сервису хранения или указанной операции API. Это число включает успешные и неудачные запросы, а также запросы, вызвавшие ошибки. Используйте измерение ResponseType для подсчёта различных типов ответов. | Count | Authentication, GeoType, ResponseType, ApiName | Applicable |

**Azure Storage File Services (Classic)**

Этот сервис мониторит часть Storage Account Classic (Microsoft.ClassicStorage/storageAccounts). Вы можете найти уже отслеживаемые ресурсы на обзорной странице Azure в разделе `Cloud services` или использовать предустановленный дашборд. Для мониторинга ресурсов типа Microsoft.Storage/storageAccounts (включая Storage, StorageV2 и BlobStorage) ознакомьтесь со Storage Accounts и разделом `Storage accounts` на обзорной странице Azure.

| Название | Описание | Единица | Измерения | Рекомендуется |
| --- | --- | --- | --- | --- |
| Availability | Процент доступности сервиса хранения или указанной операции API. Доступность рассчитывается путём деления значения TotalBillableRequests на количество применимых запросов, включая те, которые привели к непредвиденным ошибкам. Все непредвиденные ошибки приводят к снижению доступности сервиса хранения или указанной операции API. | Percent | Authentication, FileShare, GeoType, ApiName | Applicable |
| Egress | Объём исходящих данных в байтах. Это число включает исходящий трафик от внешнего клиента в Azure Storage, а также исходящий трафик внутри Azure. Поэтому это число не отражает тарифицируемый исходящий трафик. | Byte | Authentication, FileShare, GeoType, ApiName | Applicable |
| FileCapacity | Объём хранилища, используемый сервисом File учётной записи хранения, в байтах. | Byte | FileShare | Applicable |
| FileCount | Количество файлов в сервисе File учётной записи хранения. | Count | FileShare | Applicable |
| FileShareCount | Количество файловых ресурсов общего доступа в сервисе File учётной записи хранения. | Count |  | Applicable |
| FileShareQuota | Верхний предел объёма хранилища, который может быть использован сервисом Azure Files, в байтах. | Byte | FileShare | Applicable |
| FileShareSnapshotCount | Количество моментальных снимков, присутствующих в общем ресурсе сервиса Files учётной записи хранения. | Count | FileShare |  |
| FileShareSnapshotSize | Объём хранилища, используемый моментальными снимками в сервисе File учётной записи хранения, в байтах. | Byte | FileShare |  |
| Ingress | Объём входящих данных в байтах. Это число включает входящий трафик от внешнего клиента в Azure Storage, а также входящий трафик внутри Azure. | Byte | Authentication, FileShare, GeoType, ApiName | Applicable |
| SuccessE2ELatency | Сквозная задержка успешных запросов к сервису хранения или указанной операции API в миллисекундах. Это значение включает необходимое время обработки в Azure Storage для чтения запроса, отправки ответа и получения подтверждения ответа. | MilliSecond | Authentication, FileShare, GeoType, ApiName | Applicable |
| SuccessServerLatency | Задержка обработки успешного запроса в Azure Storage в миллисекундах. Это значение не включает сетевую задержку, указанную в SuccessE2ELatency. | MilliSecond | Authentication, FileShare, GeoType, ApiName |  |
| Transactions | Количество запросов к сервису хранения или указанной операции API. Это число включает успешные и неудачные запросы, а также запросы, вызвавшие ошибки. Используйте измерение ResponseType для подсчёта различных типов ответов. | Count | Authentication, FileShare, GeoType, ResponseType, ApiName | Applicable |

**Azure Storage Queue Services (Classic)**

Этот сервис мониторит часть Storage Account Classic (Microsoft.ClassicStorage/storageAccounts). Вы можете найти уже отслеживаемые ресурсы на обзорной странице Azure в разделе `Cloud services` или использовать предустановленный дашборд. Для мониторинга ресурсов типа Microsoft.Storage/storageAccounts (включая Storage, StorageV2 и BlobStorage) ознакомьтесь со Storage Accounts и разделом `Storage accounts` на обзорной странице Azure.

| Название | Описание | Единица | Измерения | Рекомендуется |
| --- | --- | --- | --- | --- |
| Availability | Процент доступности сервиса хранения или указанной операции API. Доступность рассчитывается путём деления значения TotalBillableRequests на количество применимых запросов, включая те, которые привели к непредвиденным ошибкам. Все непредвиденные ошибки приводят к снижению доступности сервиса хранения или указанной операции API. | Percent | Authentication, GeoType, ApiName | Applicable |
| Egress | Объём исходящих данных в байтах. Это число включает исходящий трафик от внешнего клиента в Azure Storage, а также исходящий трафик внутри Azure. Поэтому это число не отражает тарифицируемый исходящий трафик. | Byte | Authentication, GeoType, ApiName | Applicable |
| Ingress | Объём входящих данных в байтах. Это число включает входящий трафик от внешнего клиента в Azure Storage, а также входящий трафик внутри Azure. | Byte | Authentication, GeoType, ApiName | Applicable |
| QueueCapacity | Объём хранилища, используемый сервисом Queue учётной записи хранения, в байтах. | Byte |  | Applicable |
| QueueCount | Количество очередей в сервисе Queue учётной записи хранения. | Count |  | Applicable |
| QueueMessageCount | Приблизительное количество сообщений очереди в сервисе Queue учётной записи хранения. | Count |  | Applicable |
| SuccessE2ELatency | Сквозная задержка успешных запросов к сервису хранения или указанной операции API в миллисекундах. Это значение включает необходимое время обработки в Azure Storage для чтения запроса, отправки ответа и получения подтверждения ответа. | MilliSecond | Authentication, GeoType, ApiName | Applicable |
| SuccessServerLatency | Задержка обработки успешного запроса в Azure Storage в миллисекундах. Это значение не включает сетевую задержку, указанную в SuccessE2ELatency. | MilliSecond | Authentication, GeoType, ApiName |  |
| Transactions | Количество запросов к сервису хранения или указанной операции API. Это число включает успешные и неудачные запросы, а также запросы, вызвавшие ошибки. | Count | Authentication, GeoType, ResponseType, ApiName | Applicable |

**Azure Storage Table Services (Classic)**

Этот сервис мониторит часть Storage Account Classic (Microsoft.ClassicStorage/storageAccounts). Вы можете найти уже отслеживаемые ресурсы на обзорной странице Azure в разделе `Cloud services` или использовать предустановленный дашборд. Для мониторинга ресурсов типа Microsoft.Storage/storageAccounts (включая Storage, StorageV2 и BlobStorage) ознакомьтесь со Storage Accounts и разделом `Storage accounts` на обзорной странице Azure.

| Название | Описание | Единица | Измерения | Рекомендуется |
| --- | --- | --- | --- | --- |
| Availability | Процент доступности сервиса хранения или указанной операции API. Доступность рассчитывается путём деления значения TotalBillableRequests на количество применимых запросов, включая те, которые привели к непредвиденным ошибкам. Все непредвиденные ошибки приводят к снижению доступности сервиса хранения или указанной операции API. | Percent | Authentication, GeoType, ApiName | Applicable |
| Egress | Объём исходящих данных в байтах. Это число включает исходящий трафик от внешнего клиента в Azure Storage, а также исходящий трафик внутри Azure. Поэтому это число не отражает тарифицируемый исходящий трафик. | Byte | Authentication, GeoType, ApiName | Applicable |
| Ingress | Объём входящих данных в байтах. Это число включает входящий трафик от внешнего клиента в Azure Storage, а также входящий трафик внутри Azure. | Byte | Authentication, GeoType, ApiName | Applicable |
| SuccessE2ELatency | Сквозная задержка успешных запросов к сервису хранения или указанной операции API в миллисекундах. Это значение включает необходимое время обработки в Azure Storage для чтения запроса, отправки ответа и получения подтверждения ответа. | MilliSecond | Authentication, GeoType, ApiName | Applicable |
| SuccessServerLatency | Задержка обработки успешного запроса в Azure Storage в миллисекундах. Это значение не включает сетевую задержку, указанную в SuccessE2ELatency. | MilliSecond | Authentication, GeoType, ApiName |  |
| TableCapacity | Объём хранилища, используемый сервисом Table учётной записи хранения, в байтах. | Byte |  | Applicable |
| TableCount | Количество таблиц в сервисе Table учётной записи хранения. | Count |  | Applicable |
| TableEntityCount | Количество сущностей таблиц в сервисе Table учётной записи хранения. | Count |  | Applicable |
| Transactions | Количество запросов к сервису хранения или указанной операции API. Это число включает успешные и неудачные запросы, а также запросы, вызвавшие ошибки. Используйте измерение ResponseType для подсчёта различных типов ответов. | Count | Authentication, GeoType, ResponseType, ApiName | Applicable |
