---
title: Azure Storage Accounts (built-in)
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account-builtin
scraped: 2026-05-12T11:26:23.886002
---

# Azure Storage Accounts (built-in)

# Azure Storage Accounts (built-in)

* Практическое руководство
* Чтение: 1 мин
* Обновлено 15 ноября 2023 г.

Информацию о различиях между классическими и другими сервисами см. в разделе [Миграция с классических (ранее «built-in») сервисов Azure на облачные сервисы](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide "Миграция классических сервисов Azure на их новые версии.").

Dynatrace получает метрики из Azure Metrics API для **Azure Storage Accounts**. Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать метрики по различным измерениям и создавать пользовательские графики, которые можно закрепить на ваших дашбордах.

## Предварительные требования

* Environment ActiveGate
* Чтобы отключить мониторинг встроенных сервисов, требуется Environment ActiveGate версии 1.245+ и Dynatrace версии 1.247+.

Этот сервис отслеживает Storage Accounts (`Microsoft.Storage/storageAccounts`). Уже отслеживаемые ресурсы можно найти на странице обзора Azure в разделе **Storage accounts**.

Поддерживаются типы сервисов Storage, StorageV2 и BlobStorage. Для мониторинга ресурсов типа `Microsoft.ClassicStorage/storageAccounts` отметьте **Storage Account Classic** и раздел **Cloud services** на странице обзора Azure.

Этот сервис отслеживает те же ресурсы Azure, что и Azure Storage Account и Azure Storage Blob/File/Queue Services из раздела **Cloud services**. Для более гибкой настройки мониторинга перейдите на последние. Историческую (built-in) и новые версии нельзя включить одновременно.

## Включение мониторинга

О том, как включить мониторинг сервиса, см. в разделе [Включение мониторинга сервиса](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Включение мониторинга Azure в Dynatrace.").

## Просмотр метрик сервиса

Метрики сервисов Azure можно просматривать в вашем окружении Dynatrace на странице подписки Azure или на собственном дашборде.

Значения в таблице зависят от выбранного временного интервала. Подробнее см. в разделе [Устранение неполадок со сравнением временных интервалов при настройке мониторинга Azure)](https://dt-url.net/7j438f0).

### Просмотр метрик на странице учётной записи Azure

Чтобы получить доступ к метрикам на странице учётной записи Azure

1. Перейдите в **Azure**.
2. Выберите подписку Azure.
3. Выберите сервис, метрики которого нужно проверить. Метрики выбранного сервиса отображаются под инфографикой в разделе сервиса, как в примере ниже.

   ![Azure service metrics](https://dt-cdn.net/images/azure-service-1109-9488bfa5e4.png)

   Azure service metrics

### Просмотр метрик на дашборде

Вы можете создать собственный дашборд для просмотра метрик сервисов Azure. О том, как создавать дашборды, см. в разделе [Создание и редактирование дашбордов Dynatrace](/managed/analyze-explore-automate/dashboards-classic/dashboards/create-dashboards "Узнайте, как создавать и редактировать дашборды Dynatrace.").

## Доступные метрики

| Ключ метрики | Имя | Единица измерения | Агрегации | Потребление мониторинга |
| --- | --- | --- | --- | --- |
| builtin:cloud.azure.storage.blob.transactions | Transactions count | Количество | autovalue | DDUs |
| builtin:cloud.azure.storage.blob.transactions.network.latency.success.e2e | E2E success latency | Миллисекунда | autoavgmaxmin | DDUs |
| builtin:cloud.azure.storage.blob.transactions.network.latency.success.server | Server success latency | Миллисекунда | autoavgmaxmin | DDUs |
| builtin:cloud.azure.storage.blob.transactions.network.egress | Egress bytes | Байт | autovalue | DDUs |
| builtin:cloud.azure.storage.blob.transactions.network.ingress | Ingress bytes | Байт | autovalue | DDUs |
| builtin:cloud.azure.storage.blob.capacity | Blob capacity | Байт | autoavgcountmaxminsum | DDUs |
| builtin:cloud.azure.storage.blob.containers | Blob container count | Количество | autoavgcountmaxminsum | DDUs |
| builtin:cloud.azure.storage.blob.entities | Blob count | Количество | autoavgcountmaxminsum | DDUs |
| builtin:cloud.azure.storage.file.transactions | Transactions count | Количество | autovalue | DDUs |
| builtin:cloud.azure.storage.file.transactions.network.latency.success.e2e | E2E success latency | Миллисекунда | autoavgmaxmin | DDUs |
| builtin:cloud.azure.storage.file.transactions.network.latency.success.server | Server success latency | Миллисекунда | autoavgmaxmin | DDUs |
| builtin:cloud.azure.storage.file.transactions.network.egress | Egress bytes | Байт | autovalue | DDUs |
| builtin:cloud.azure.storage.file.transactions.network.ingress | Ingress bytes | Байт | autovalue | DDUs |
| builtin:cloud.azure.storage.file.capacity | File capacity | Байт | autoavgcountmaxminsum | DDUs |
| builtin:cloud.azure.storage.file.containers | File share count | Количество | autoavgcountmaxminsum | DDUs |
| builtin:cloud.azure.storage.file.entities | File count | Количество | autoavgcountmaxminsum | DDUs |
| builtin:cloud.azure.storage.queue.transactions | Transactions count | Количество | autovalue | DDUs |
| builtin:cloud.azure.storage.queue.transactions.network.latency.success.e2e | E2E success latency | Миллисекунда | autoavgmaxmin | DDUs |
| builtin:cloud.azure.storage.queue.transactions.network.latency.success.server | Server success latency | Миллисекунда | autoavgmaxmin | DDUs |
| builtin:cloud.azure.storage.queue.transactions.network.egress | Egress bytes | Байт | autovalue | DDUs |
| builtin:cloud.azure.storage.queue.transactions.network.ingress | Ingress bytes | Байт | autovalue | DDUs |
| builtin:cloud.azure.storage.queue.capacity | Queue capacity | Байт | autoavgcountmaxminsum | DDUs |
| builtin:cloud.azure.storage.queue.containers | Queue count | Количество | autoavgcountmaxminsum | DDUs |
| builtin:cloud.azure.storage.queue.entities | Queue message count | Количество | autoavgcountmaxminsum | DDUs |
| builtin:cloud.azure.storage.table.transactions | Transactions count | Количество | autovalue | DDUs |
| builtin:cloud.azure.storage.table.transactions.network.latency.success.server | Server success latency | Миллисекунда | autoavgmaxmin | DDUs |
| builtin:cloud.azure.storage.table.transactions.network.latency.success.server.e2e | E2E success latency | Миллисекунда | autoavgmaxmin | DDUs |
| builtin:cloud.azure.storage.table.transactions.network.egress | Egress bytes | Байт | autovalue | DDUs |
| builtin:cloud.azure.storage.table.transactions.network.ingress | Ingress bytes | Байт | autovalue | DDUs |
| builtin:cloud.azure.storage.table.capacity | Table capacity | Байт | autoavgcountmaxminsum | DDUs |
| builtin:cloud.azure.storage.table.containers | Table count | Количество | autoavgcountmaxminsum | DDUs |
| builtin:cloud.azure.storage.table.entities | Table entity count | Количество | autoavgcountmaxminsum | DDUs |

## Дополнительные замечания

* `Azure Storage Accounts (built-in)` отслеживает те же ресурсы Azure, что и `Azure Storage Account` и `Azure Storage Blob/File/Queue Services` из раздела `Cloud services`. Для более гибкой настройки мониторинга перейдите на последние. Встроенную и обычные версии нельзя включить одновременно:

  + Включение встроенной версии отключит все обычные версии.
  + Включение любой из обычных версий отключит встроенную версию.