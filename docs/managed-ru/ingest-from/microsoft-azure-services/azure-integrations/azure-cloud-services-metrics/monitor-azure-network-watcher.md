---
title: Мониторинг Azure Network Watcher (Connection Monitor, Connection Monitor Preview)
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-network-watcher
scraped: 2026-05-12T11:26:50.888745
---

# Мониторинг Azure Network Watcher (Connection Monitor, Connection Monitor Preview)

# Мониторинг Azure Network Watcher (Connection Monitor, Connection Monitor Preview)

* Практическое руководство
* Чтение: 2 мин
* Опубликовано 23 сентября 2020 г.

Dynatrace получает метрики из Azure Metrics API для Azure Network Watcher (Connection Monitor, Connection Monitor Preview). Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать метрики по различным измерениям и создавать пользовательские графики, которые можно закрепить на ваших дашбордах.

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

![Conn monitor](https://dt-cdn.net/images/cm-dashboard-1-3137-226998a645.png)

Conn monitor

![Conn monitor preview](https://dt-cdn.net/images/cm-dashboard-1414-d3238a9386.png)

Conn monitor preview

## Доступные метрики

**Connection Monitor**

| Имя | Описание | Единица измерения | Рекомендуется |
| --- | --- | --- | --- |
| AverageRoundtripMs | Среднее сетевое время кругового пути (мс) для проб мониторинга связности, отправляемых между источником и назначением | Миллисекунда | Применимо |
| ProbesFailedPercent | Процент неудавшихся проб мониторинга связности | Процент | Применимо |

**Connection Monitor Preview**

| Имя | Описание | Единица измерения | Измерения | Рекомендуется |
| --- | --- | --- | --- | --- |
| AverageRoundtripMs | Среднее сетевое время кругового пути (RTT) для проб мониторинга связности, отправляемых между источником и назначением | Миллисекунда |  |  |
| ChecksFailedPercent | Процент неудавшихся проверок для теста | Процент | Source address, Source endpoint name, Source resource ID, Destination address, Destination endpoint name, Destination resource ID, Destination port, Test group name, Test configuration name | Применимо |
| ProbesFailedPercent | Процент неудавшихся проб мониторинга связности | Процент |  |  |
| RoundTripTimeMs | Время кругового пути (RTT) для проверок, отправляемых между источником и назначением | Миллисекунда | Source address, Source endpoint name, Source resource ID, Destination address, Destination endpoint name, Destination resource ID, Destination port, Test group name, Test configuration name | Применимо |