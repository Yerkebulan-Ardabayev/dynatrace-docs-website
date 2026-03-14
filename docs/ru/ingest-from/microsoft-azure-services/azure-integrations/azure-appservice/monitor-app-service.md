---
title: Мониторинг метрик Azure App Service Plan
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/monitor-app-service
scraped: 2026-03-06T21:36:16.915907
---

# Мониторинг метрик Azure App Service Plan

# Мониторинг метрик Azure App Service Plan

* Последняя версия Dynatrace
* Практическое руководство
* 2 минуты чтения
* Опубликовано 23 сентября 2020 г.

Dynatrace получает метрики из Azure Metrics API для **Azure App Service Plan**, используемого вашим развёрнутым App Service. Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать метрики по нескольким измерениям и создавать пользовательские графики, которые можно закрепить на информационных панелях.

## Предварительные условия

* Dynatrace версии 1.203+
* ActiveGate для среды версии 1.195+

## Включение мониторинга

Чтобы узнать, как включить мониторинг сервисов, см. раздел [Enable service monitoring](../azure-monitoring-guide/azure-enable-service-monitoring.md "Enable Azure monitoring in Dynatrace.").

## Просмотр метрик сервиса

Метрики сервиса можно просматривать в среде Dynatrace на странице **обзора пользовательского устройства** или на странице **Dashboards**.

### Просмотр метрик на странице обзора пользовательского устройства

Чтобы перейти на страницу обзора пользовательского устройства:

1. Перейдите в раздел ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Отфильтруйте по имени сервиса и выберите нужную группу пользовательских устройств.
3. После выбора группы пользовательских устройств откроется **страница обзора группы пользовательских устройств**.
4. На **странице обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), относящиеся к группе. Выберите экземпляр для просмотра **страницы обзора пользовательского устройства**.

### Просмотр метрик на информационной панели

Если для сервиса предусмотрена стандартная информационная панель, она появится на вашей странице **Dashboards** и будет содержать все рекомендуемые метрики для соответствующего сервиса. Можно искать конкретные панели, применяя фильтр по **Preset**, а затем по **Name**.

Для уже отслеживаемых сервисов может потребоваться повторное сохранение учётных данных, чтобы стандартная информационная панель появилась на странице **Dashboards**. Чтобы повторно сохранить учётные данные, перейдите в **Settings** > **Cloud and virtualization** > **Azure**, выберите нужный экземпляр Azure, затем нажмите **Save**.

Вносить изменения непосредственно в стандартную информационную панель нельзя, но её можно клонировать и редактировать. Чтобы клонировать панель, откройте меню обзора (**...**) и выберите **Clone**.
Чтобы удалить панель из списка, её можно скрыть. Для этого откройте меню обзора (**...**) и выберите **Hide**.

Скрытие панели не влияет на других пользователей.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![App service plan](https://dt-cdn.net/images/dashboard-87-873-b330e8b901.png)

## Доступные метрики

| Название | Описание | Измерения | Единица | Рекомендуется |
| --- | --- | --- | --- | --- |
| BytesReceived | Входящие данные | Instance | Байт | ✔️ |
| BytesSent | Исходящие данные | Instance | Байт | ✔️ |
| CpuPercentage | Процент использования CPU | Instance | Процент | ✔️ |
| DiskQueueLength | Длина очереди диска | Instance | Количество | ✔️ |
| HttpQueueLength | Длина очереди HTTP | Instance | Количество | ✔️ |
| MemoryPercentage | Процент использования памяти | Instance | Процент | ✔️ |
| SocketInboundAll | Все входящие сокеты |  | Количество |  |
| SocketLoopback | Петлевые сокеты | Instance | Количество |  |
| SocketOutboundAll | Все исходящие сокеты |  | Количество |  |
| SocketOutboundEstablished | Установленные исходящие сокеты | Instance | Количество |  |
| SocketOutboundTimeWait | Исходящие сокеты в ожидании | Instance | Количество |  |
| TcpCloseWait | TCP close wait | Instance | Количество |  |
| TcpClosing | TCP closing | Instance | Количество |  |
| TcpEstablished | TCP established | Instance | Количество |  |
| TcpFinWait1 | TCP fin wait 1 | Instance | Количество |  |
| TcpFinWait2 | TCP fin wait 2 | Instance | Количество |  |
| TcpLastAck | TCP last ack | Instance | Количество |  |
| TcpSynReceived | TCP syn received | Instance | Количество |  |
| TcpSynSent | TCP syn sent | Instance | Количество |  |
| TcpTimeWait | TCP time wait | Instance | Количество |  |
