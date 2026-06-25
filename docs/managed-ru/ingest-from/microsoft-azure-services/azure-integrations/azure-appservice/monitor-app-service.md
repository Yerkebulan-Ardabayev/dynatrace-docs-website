---
title: Мониторинг метрик Azure App Service Plan
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/monitor-app-service
scraped: 2026-05-12T11:25:55.744220
---

# Мониторинг метрик Azure App Service Plan

# Мониторинг метрик Azure App Service Plan

* Практическое руководство
* Чтение: 2 мин
* Опубликовано 23 сентября 2020 г.

Dynatrace получает метрики из Azure Metrics API для **Azure App Service Plan**, используемого вашим развёрнутым App Service. Можно просматривать метрики для каждого экземпляра сервиса, разбивать метрики по нескольким измерениям и создавать пользовательские диаграммы, которые можно закрепить на дашбордах.

## Предварительные требования

* Dynatrace версии 1.203+
* Environment ActiveGate версии 1.195+

## Включение мониторинга

О том, как включить мониторинг сервиса, см. в разделе [Включение мониторинга сервиса](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Включение мониторинга Azure в Dynatrace.").

## Просмотр метрик сервиса

Метрики сервиса можно просматривать в окружении Dynatrace на странице обзора пользовательского устройства (**custom device overview page**) или на странице **Dashboards**.

### Просмотр метрик на странице обзора пользовательского устройства

Чтобы открыть страницу обзора пользовательского устройства

1. Откройте **Technologies & Processes**.
2. Отфильтруйте по имени сервиса и выберите нужную группу пользовательских устройств.
3. После выбора группы пользовательских устройств откроется **custom device group overview page**.
4. На странице **custom device group overview page** перечислены все экземпляры (пользовательские устройства), входящие в группу. Выберите экземпляр, чтобы открыть **custom device overview page**.

### Просмотр метрик на дашборде

Если для сервиса предусмотрен преднастроенный дашборд, на странице **Dashboards** появится преднастроенный дашборд для соответствующего сервиса со всеми рекомендованными метриками. Нужный дашборд можно найти, отфильтровав по **Preset**, а затем по **Name**.

Для существующих отслеживаемых сервисов может потребоваться повторно сохранить учётные данные, чтобы преднастроенный дашборд появился на странице **Dashboards**. Для повторного сохранения учётных данных откройте **Settings** > **Cloud and virtualization** > **Azure**, выберите нужный экземпляр Azure и нажмите **Save**.

Напрямую вносить изменения в преднастроенный дашборд нельзя, но можно клонировать его и редактировать. Чтобы клонировать дашборд, откройте меню (**…**) и выберите **Clone**.
Чтобы убрать дашборд из списка, его можно скрыть. Для этого откройте меню (**…**) и выберите **Hide**.

Скрытие дашборда не затрагивает других пользователей.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

Clone hide azure

![App service plan](https://dt-cdn.net/images/dashboard-87-873-b330e8b901.png)

App service plan

## Доступные метрики

| Имя | Описание | Измерения | Единица | Рекомендовано |
| --- | --- | --- | --- | --- |
| BytesReceived | Входящие данные | Instance | Byte | ✔️ |
| BytesSent | Исходящие данные | Instance | Byte | ✔️ |
| CpuPercentage | Загрузка CPU | Instance | Percent | ✔️ |
| DiskQueueLength | Длина очереди диска | Instance | Count | ✔️ |
| HttpQueueLength | Длина очереди HTTP | Instance | Count | ✔️ |
| MemoryPercentage | Использование памяти | Instance | Percent | ✔️ |
| SocketInboundAll | Все входящие сокеты |  | Count |  |
| SocketLoopback | Петлевые сокеты | Instance | Count |  |
| SocketOutboundAll | Все исходящие сокеты |  | Count |  |
| SocketOutboundEstablished | Установленные исходящие сокеты | Instance | Count |  |
| SocketOutboundTimeWait | Исходящие сокеты в состоянии ожидания | Instance | Count |  |
| TcpCloseWait | TCP ожидание закрытия | Instance | Count |  |
| TcpClosing | TCP закрытие | Instance | Count |  |
| TcpEstablished | TCP соединения установлены | Instance | Count |  |
| TcpFinWait1 | TCP fin wait 1 | Instance | Count |  |
| TcpFinWait2 | TCP fin wait 2 | Instance | Count |  |
| TcpLastAck | TCP last ack | Instance | Count |  |
| TcpSynReceived | TCP syn received | Instance | Count |  |
| TcpSynSent | TCP syn sent | Instance | Count |  |
| TcpTimeWait | TCP time wait | Instance | Count |  |