---
title: Мониторинг Azure Storage Sync
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-sync
scraped: 2026-05-12T11:27:26.156313
---

# Мониторинг Azure Storage Sync

# Мониторинг Azure Storage Sync

* Практическое руководство
* Чтение: 2 мин
* Опубликовано 23 сентября 2020 г.

Dynatrace получает метрики из Azure Metrics API для Azure Storage Sync. Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать метрики по различным измерениям и создавать пользовательские графики, которые можно закрепить на ваших дашбордах.

## Предварительные условия

* Dynatrace версии 1.203+
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

![Stor sync](https://dt-cdn.net/images/2021-03-12-11-36-41-1570-b719e71510.png)

Stor sync

## Доступные метрики

| Имя | Описание | Измерения | Единица измерения | Рекомендуется |
| --- | --- | --- | --- | --- |
| ServerSyncSessionResult | Регистрирует значение `1` каждый раз, когда серверная конечная точка успешно завершает сессию синхронизации с облачной конечной точкой | Sync group name, Server endpoint name, Sync direction | Количество | Применимо |
| StorageSyncSyncSessionAppliedFilesCount | Количество синхронизированных файлов | Sync group name, Server endpoint name, Sync direction | Количество | Применимо |
| StorageSyncSyncSessionPerItemErrorsCount | Количество файлов, которые не удалось синхронизировать | Sync group name, Server endpoint name, Sync direction | Количество | Применимо |
| StorageSyncBatchTransferredFileBytes | Общий размер файлов, переданных за сессии синхронизации | Sync group name, Server endpoint name, Sync direction | Байт | Применимо |
| StorageSyncServerHeartbeat | Регистрирует значение `1` каждый раз, когда зарегистрированный сервер успешно записывает heartbeat в облачную конечную точку | Server name | Количество | Применимо |
| StorageSyncRecallIOTotalSizeBytes | Общий размер данных, отозванных сервером | Server name | Байт |  |
| StorageSyncRecalledTotalNetworkBytes | Размер отозванных данных | Sync group name, Server name | Байт |  |
| StorageSyncRecallThroughputBytesPerSecond | Пропускная способность отзыва данных | Sync group name, Server name | Байт в секунду |  |
| StorageSyncRecalledNetworkBytesByApplication | Размер данных, отозванных приложением | Sync group name, Server name, Application name | Байт |  |