---
title: Мониторинг Azure Public IP Address
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-public-ip-addresses
scraped: 2026-03-04T21:30:09.923259
---

# Azure Public IP Address monitoring


* Latest Dynatrace
* How-to guide
* 2-min read

Dynatrace принимает метрики из Azure Metrics API для Azure Public IP Address. Можно просматривать метрики для каждого экземпляра сервиса, разбивать метрики по нескольким измерениям и создавать пользовательские графики для закрепления на дашбордах.

## Предварительные требования

* Dynatrace версии 1.199+
* Environment ActiveGate версии 1.195+

## Включение мониторинга

Сведения о включении мониторинга сервиса см. в разделе Enable service monitoring.

## Просмотр метрик сервиса

Метрики сервиса можно просматривать в среде Dynatrace на **странице обзора пользовательского устройства** или на странице **Dashboards**.

### Просмотр метрик на странице обзора пользовательского устройства

Чтобы перейти на страницу обзора пользовательского устройства

1. Перейдите в ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Отфильтруйте по имени сервиса и выберите нужную группу пользовательских устройств.
3. После выбора группы пользовательских устройств откроется **страница обзора группы пользовательских устройств**.
4. На **странице обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), принадлежащие группе. Выберите экземпляр для просмотра **страницы обзора пользовательского устройства**.

### Просмотр метрик на дашборде

Если для сервиса имеется предустановленный дашборд, на странице **Dashboards** появится предустановленный дашборд соответствующего сервиса со всеми рекомендуемыми метриками. Можно искать конкретные дашборды, фильтруя по **Preset**, а затем по **Name**.

Для уже отслеживаемых сервисов может потребоваться повторное сохранение учётных данных, чтобы предустановленный дашборд появился на странице **Dashboards**. Чтобы повторно сохранить учётные данные, перейдите в **Settings** > **Cloud and virtualization** > **Azure**, выберите нужный экземпляр Azure, затем нажмите **Save**.

Нельзя вносить изменения непосредственно в предустановленный дашборд, но его можно клонировать и редактировать. Чтобы клонировать дашборд, откройте меню (**...**) и выберите **Clone**.
Чтобы удалить дашборд из списка, его можно скрыть. Чтобы скрыть дашборд, откройте меню (**...**) и выберите **Hide**.

Скрытие дашборда не влияет на других пользователей.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![IP-dash](https://dt-cdn.net/images/dashboard-21-1352-94948a295c.png)

## Доступные метрики

| Имя | Описание | Единица | Рекомендовано |
| --- | --- | --- | --- |
| ByteCount | Общее количество байт, переданных за период времени | Byte, Port, Direction | Применимо |
| BytesDroppedDDoS | Входящие байты, сброшенные при DDoS | BytePerSecond |  |
| BytesForwardedDDoS | Входящие байты, перенаправленные при DDoS | BytePerSecond |  |
| BytesInDDoS | Входящие байты при DDoS | BytePerSecond |  |
| DDoSTriggerSYNPackets | Входящие SYN-пакеты для активации защиты от DDoS | PerSecond |  |
| DDoSTriggerTCPPackets | Входящие TCP-пакеты для активации защиты от DDoS | PerSecond |  |
| DDoSTriggerUDPPackets | Входящие UDP-пакеты для активации защиты от DDoS | PerSecond |  |
| IfUnderDDoSAttack | Находится ли под DDoS-атакой | Count |  |
| PacketCount | Общее количество пакетов, переданных за период времени | Count, Port, Direction | Применимо |
| PacketsDroppedDDoS | Входящие пакеты, сброшенные при DDoS | PerSecond |  |
| PacketsForwardedDDoS | Входящие пакеты, перенаправленные при DDoS | PerSecond |  |
| PacketsInDDoS | Входящие пакеты при DDoS | PerSecond |  |
| SynCount | Общее количество SYN-пакетов, переданных за период времени | Count, Port, Direction | Применимо |
| TCPBytesDroppedDDoS | Входящие TCP-байты, сброшенные при DDoS | BytePerSecond |  |
| TCPBytesForwardedDDoS | Входящие TCP-байты, перенаправленные при DDoS | BytePerSecond |  |
| TCPBytesInDDoS | Входящие TCP-байты при DDoS | BytePerSecond |  |
| TCPPacketsDroppedDDoS | Входящие TCP-пакеты, сброшенные при DDoS | PerSecond |  |
| TCPPacketsForwardedDDoS | Входящие TCP-пакеты, перенаправленные при DDoS | PerSecond |  |
| TCPPacketsInDDoS | Входящие TCP-пакеты при DDoS | PerSecond |  |
| UDPBytesDroppedDDoS | Входящие UDP-байты, сброшенные при DDoS | BytePerSecond |  |
| UDPBytesForwardedDDoS | Входящие UDP-байты, перенаправленные при DDoS | BytePerSecond |  |
| UDPBytesInDDoS | Входящие UDP-байты при DDoS | BytePerSecond |  |
| UDPPacketsDroppedDDoS | Входящие UDP-пакеты, сброшенные при DDoS | PerSecond |  |
| UDPPacketsForwardedDDoS | Входящие UDP-пакеты, перенаправленные при DDoS | PerSecond |  |
| UDPPacketsInDDoS | Входящие UDP-пакеты при DDoS | PerSecond |  |
| VipAvailability | Средняя доступность IP-адреса за период времени | Percent, Port | Применимо |
