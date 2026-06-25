---
title: Azure Storage Account (Blob, File, Queue, Table)
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account
scraped: 2026-05-12T11:25:26.738137
---

# Azure Storage Account (Blob, File, Queue, Table)

# Azure Storage Account (Blob, File, Queue, Table)

* Практическое руководство
* Чтение: 11 мин
* Обновлено 5 декабря 2023 г.

Информацию о различиях между классическими и другими сервисами см. в разделе [Миграция с классических (ранее «built-in») сервисов Azure на облачные сервисы](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide "Миграция классических сервисов Azure на их новые версии.").

Dynatrace получает метрики для нескольких предварительно выбранных пространств имён, включая Azure Storage Account. Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать их по нескольким измерениям и создавать пользовательские диаграммы, которые можно закрепить на дашбордах.

## Предварительные требования

* Dynatrace версии 1.196+
* Environment ActiveGate версии 1.195+

Этот сервис отслеживает часть Storage Account (`Microsoft.Storage/storageAccounts`).

Пока этот сервис настроен, вы **не можете** включить сервис Azure Storage accounts (built-in).

Для мониторинга ресурсов типа `Microsoft.ClassicStorage/storageAccounts` отметьте **Storage Account Classic** и раздел **Cloud services** на странице обзора Azure

## Включение мониторинга

О том, как включить мониторинг сервиса, см. в разделе [Включение мониторинга сервиса](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Включение мониторинга Azure в Dynatrace.").

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

![Storage account dashboard](https://dt-cdn.net/images/storage-accounts-dashboard-1489-114f1e2260.png)

Storage account dashboard

## Доступные метрики

Этот сервис отслеживает часть Storage Account (`Microsoft.Storage/storageAccounts`). Пока этот сервис настроен, вы не можете включить сервис Azure Storage accounts (built-in).

Для мониторинга ресурсов типа `Microsoft.ClassicStorage/storageAccounts` отметьте разделы **Storage Account Classic** и **Cloud services** на странице обзора Azure.

**Storage Account**

| Отображаемое имя | Имя | Описание | Измерения | Единица измерения | Рекомендуется |
| --- | --- | --- | --- | --- | --- |
| Availability | Availability | Процент доступности для сервиса хранилища или указанной операции API. Все неожиданные ошибки приводят к снижению доступности для сервиса хранилища или указанной операции API. | API name, Authentication, Geo type | Процент |  |
| Egress | Egress | Объём исходящих данных. | API name, Authentication, Geo type | Байт |  |
| Ingress | Ingress | Объём входящих данных в байтах. | API name, Authentication, Geo type | Байт |  |
| Success E2E latency | SuccessE2ELatency | Средняя сквозная задержка успешных запросов к сервису хранилища или указанной операции API в миллисекундах. | API name, Authentication, Geo type | Миллисекунда |  |
| Success server latency | SuccessServerLatency | Среднее время обработки успешного запроса в Azure Storage. Это значение не включает сетевую задержку, указанную в SuccessE2ELatency. | API name, Authentication, Geo type | Миллисекунда |  |
| Transactions | Transactions | Количество запросов к сервису хранилища или указанной операции API. Используйте измерение ResponseType, чтобы получить количество ответов разных типов. | API name, Authentication, Geo type, Response type, Transaction type | Количество | Применимо |
| Used capacity | UsedCapacity | Объём хранилища, используемого аккаунтом хранилища. Для стандартных аккаунтов хранилища это сумма ёмкости, используемой blob, table, file и queue. Для premium-аккаунтов хранилища и аккаунтов Blob storage оно совпадает с BlobCapacity или FileCapacity. |  | Байт | Применимо |

**Azure Storage Blob Services**

Этот сервис отслеживает часть Storage Account (`Microsoft.Storage/storageAccounts`). Пока этот сервис настроен, вы не можете включить сервис Azure Storage accounts (built-in).

Для мониторинга ресурсов типа `Microsoft.ClassicStorage/storageAccounts` отметьте разделы **Storage Account Classic** и **Cloud services** на странице обзора Azure.

| Отображаемое имя | Имя | Описание | Измерения | Единица измерения | Рекомендуется |
| --- | --- | --- | --- | --- | --- |
| Availability | Availability | Процент доступности для сервиса хранилища или указанной операции API. Все неожиданные ошибки приводят к снижению доступности для сервиса хранилища или указанной операции API. | API name, Authentication, Geo type | Процент |  |
| Blob capacity | BlobCapacity | Объём хранилища, используемого сервисом Blob аккаунта хранилища, в байтах. | Blob tier, Blob type | Байт | Применимо |
| Blob container count | ContainerCount | Количество контейнеров в аккаунте хранилища. |  | Количество |  |
| Blob count | BlobCount | Количество объектов blob, хранящихся в аккаунте хранилища. | Blob tier, Blob type | Количество |  |
| Blob provisioned size | BlobProvisionedSize | Объём хранилища, выделенного в сервисе Blob аккаунта хранилища, в байтах. | Blob tier, Blob type | Байт |  |
| Egress | Egress | Объём исходящих данных. | API name, Authentication, Geo type | Байт |  |
| Index capacity | IndexCapacity | Объём хранилища, используемого иерархическим индексом Azure Data Lake Storage Gen2. |  | Байт |  |
| Ingress | Ingress | Объём входящих данных в байтах. | API name, Authentication, Geo type | Байт |  |
| Success E2E latency | SuccessE2ELatency | Средняя сквозная задержка успешных запросов к сервису хранилища или указанной операции API в миллисекундах. | API name, Authentication, Geo type | Миллисекунда |  |
| Success server latency | SuccessServerLatency | Среднее время обработки успешного запроса в Azure Storage. Это значение не включает сетевую задержку, указанную в SuccessE2ELatency. | API name, Authentication, Geo type | Миллисекунда |  |
| Transactions | Transactions | Количество запросов к сервису хранилища или указанной операции API. Используйте измерение ResponseType, чтобы получить количество ответов разных типов. | API name, Authentication, Geo type, Response type, Transaction type | Количество | Применимо |

**Azure Storage File Services**

Этот сервис отслеживает часть Storage Account (`Microsoft.Storage/storageAccounts`). Пока этот сервис настроен, вы не можете включить сервис Azure Storage accounts (built-in).

Для мониторинга ресурсов типа `Microsoft.ClassicStorage/storageAccounts` отметьте разделы **Storage Account Classic** и **Cloud services** на странице обзора Azure.

| Отображаемое имя | Имя | Описание | Измерения | Единица измерения | Рекомендуется |
| --- | --- | --- | --- | --- | --- |
| Availability | Availability | Процент доступности для сервиса хранилища или указанной операции API. Все неожиданные ошибки приводят к снижению доступности для сервиса хранилища или указанной операции API. | API name, Authentication, File share, Geo type | Процент |  |
| Egress | Egress | Объём исходящих данных. | API name, Authentication, File share, Geo type | Байт |  |
| File capacity | FileCapacity | Объём хранилища File, используемого аккаунтом хранилища. | File share, Tier | Байт | Применимо |
| File count | FileCount | Количество файлов в аккаунте хранилища. | File share, Tier | Количество |  |
| File share capacity quota | FileShareCapacityQuota | Верхний предел объёма хранилища, которое может использовать сервис Azure Files, в байтах. | File share | Байт |  |
| File share count | FileShareCount | Количество файловых ресурсов в аккаунте хранилища. |  | Количество |  |
| File share provisioned IOPS | FileShareProvisionedIOPS | Базовое количество выделенных IOPS для premium-файлового ресурса в premium-аккаунте files storage. | File share | В секунду |  |
| File share snapshot count | FileShareSnapshotCount | Количество моментальных снимков на ресурсе в сервисе Files аккаунта хранилища. | File share | Количество |  |
| File share snapshot size | FileShareSnapshotSize | Объём хранилища, используемого моментальными снимками в сервисе File аккаунта хранилища, в байтах. | File share | Байт |  |
| Ingress | Ingress | Объём входящих данных в байтах. | API name, Authentication, File share, Geo type | Байт |  |
| Success E2E latency | SuccessE2ELatency | Средняя сквозная задержка успешных запросов к сервису хранилища или указанной операции API в миллисекундах. | API name, Authentication, File share, Geo type | Миллисекунда |  |
| Success server latency | SuccessServerLatency | Среднее время обработки успешного запроса в Azure Storage. Это значение не включает сетевую задержку, указанную в SuccessE2ELatency. | API name, Authentication, File share, Geo type | Миллисекунда |  |
| Transactions | Transactions | Количество запросов к сервису хранилища или указанной операции API. Используйте измерение ResponseType, чтобы получить количество ответов разных типов. | API name, Authentication, File share, Geo type, Response type, Transaction type | Количество | Применимо |

**Azure Storage Queue Services**

Этот сервис отслеживает часть Storage Account (`Microsoft.Storage/storageAccounts`). Пока этот сервис настроен, вы не можете включить сервис Azure Storage accounts (built-in).

Для мониторинга ресурсов типа `Microsoft.ClassicStorage/storageAccounts` отметьте разделы **Storage Account Classic** и **Cloud services** на странице обзора Azure.

| Отображаемое имя | Имя | Описание | Измерения | Единица измерения | Рекомендуется |
| --- | --- | --- | --- | --- | --- |
| Availability | Availability | Процент доступности для сервиса хранилища или указанной операции API. Все неожиданные ошибки приводят к снижению доступности для сервиса хранилища или указанной операции API. | API name, Authentication, Geo type | Процент |  |
| Egress | Egress | Объём исходящих данных. | API name, Authentication, Geo type | Байт |  |
| Ingress | Ingress | Объём входящих данных в байтах. | API name, Authentication, Geo type | Байт |  |
| Queue capacity | QueueCapacity | Объём хранилища Queue, используемого аккаунтом хранилища. |  | Байт | Применимо |
| Queue count | QueueCount | Количество очередей в аккаунте хранилища. |  | Количество |  |
| Queue message count | QueueMessageCount | Количество неистёкших сообщений очереди в аккаунте хранилища. |  | Количество |  |
| Success E2E latency | SuccessE2ELatency | Средняя сквозная задержка успешных запросов к сервису хранилища или указанной операции API в миллисекундах. | API name, Authentication, Geo type | Миллисекунда |  |
| Success server latency | SuccessServerLatency | Среднее время обработки успешного запроса в Azure Storage. Это значение не включает сетевую задержку, указанную в SuccessE2ELatency. | API name, Authentication, Geo type | Миллисекунда |  |
| Transactions | Transactions | Количество запросов к сервису хранилища или указанной операции API. Используйте измерение ResponseType, чтобы получить количество ответов разных типов. | API name, Authentication, Geo type, Response type, Transaction type | Количество | Применимо |

**Azure Storage Table Services**

Этот сервис отслеживает часть Storage Account (`Microsoft.Storage/storageAccounts`). Пока этот сервис настроен, вы не можете включить сервис Azure Storage accounts (built-in).

Для мониторинга ресурсов типа `Microsoft.ClassicStorage/storageAccounts` отметьте разделы **Storage Account Classic** и **Cloud services** на странице обзора Azure.

| Отображаемое имя | Имя | Описание | Измерения | Единица измерения | Рекомендуется |
| --- | --- | --- | --- | --- | --- |
| Availability | Availability | Процент доступности для сервиса хранилища или указанной операции API. Все неожиданные ошибки приводят к снижению доступности для сервиса хранилища или указанной операции API. | API name, Authentication, Geo type | Процент |  |
| Egress | Egress | Объём исходящих данных. | API name, Authentication, Geo type | Байт |  |
| Ingress | Ingress | Объём входящих данных в байтах. | API name, Authentication, Geo type | Байт |  |
| Success E2E latency | SuccessE2ELatency | Средняя сквозная задержка успешных запросов к сервису хранилища или указанной операции API в миллисекундах. | API name, Authentication, Geo type | Миллисекунда |  |
| Success server latency | SuccessServerLatency | Среднее время обработки успешного запроса в Azure Storage. Это значение не включает сетевую задержку, указанную в SuccessE2ELatency. | API name, Authentication, Geo type | Миллисекунда |  |
| Table capacity | TableCapacity | Объём хранилища Table, используемого аккаунтом хранилища. |  | Байт | Применимо |
| Table count | TableCount | Количество таблиц в аккаунте хранилища. |  | Количество |  |
| Table entity count | TableEntityCount | Количество сущностей таблиц в аккаунте хранилища. |  | Количество |  |
| Transactions | Transactions | Количество запросов к сервису хранилища или указанной операции API. Используйте измерение ResponseType, чтобы получить количество ответов разных типов. | API name, Authentication, Geo type, Response type, Transaction type | Количество | Применимо |

## Дополнительные замечания

Поскольку новые Azure Storage Accounts и Azure Storage accounts (built-in) отслеживают одни и те же ресурсы (из группы `Microsoft.Storage/storageAccounts`), их нельзя включить одновременно.

* Включение встроенной версии отключит все обычные версии.
* Включение любой из обычных версий отключит встроенную версию.