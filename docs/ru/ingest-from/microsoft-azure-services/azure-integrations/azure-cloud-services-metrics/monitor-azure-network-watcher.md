---
title: Мониторинг Azure Network Watcher (Connection Monitor, Connection Monitor Preview)
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-network-watcher
scraped: 2026-03-06T21:36:28.724701
---

# Мониторинг Azure Network Watcher (Connection Monitor, Connection Monitor Preview)


* Актуальная версия Dynatrace
* Практическое руководство
* Чтение: 2 мин
* Опубликовано 23 сен. 2020 г.

Dynatrace получает метрики из Azure Metrics API для Azure Network Watcher (Connection Monitor, Connection Monitor Preview). Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать метрики по нескольким измерениям и создавать пользовательские графики, которые можно закрепить на дашбордах.

## Предварительные требования

* Dynatrace версии 1.203+
* Environment ActiveGate версии 1.195+

## Включение мониторинга

Чтобы узнать, как включить мониторинг сервиса, см. [Включение мониторинга сервиса](../azure-monitoring-guide/azure-enable-service-monitoring.md "Enable Azure monitoring in Dynatrace.").

## Просмотр метрик сервиса

Метрики сервиса можно просматривать в вашей среде Dynatrace либо на **странице обзора пользовательского устройства**, либо на странице **Дашборды**.

### Просмотр метрик на странице обзора пользовательского устройства

Чтобы перейти на страницу обзора пользовательского устройства

1. Перейдите в ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Отфильтруйте по имени сервиса и выберите соответствующую группу пользовательских устройств.
3. После выбора группы пользовательских устройств вы окажетесь на **странице обзора группы пользовательских устройств**.
4. На **странице обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), принадлежащие группе. Выберите экземпляр для перехода на **страницу обзора пользовательского устройства**.

### Просмотр метрик на дашборде

Если для сервиса предусмотрен преднастроенный дашборд, вы получите его для соответствующего сервиса со всеми рекомендуемыми метриками на странице **Дашборды**. Вы можете искать конкретные дашборды, фильтруя по **Preset**, а затем по **Name**.

Для существующих отслеживаемых сервисов, возможно, потребуется повторно сохранить учётные данные, чтобы преднастроенный дашборд появился на странице **Дашборды**. Для повторного сохранения учётных данных перейдите в **Settings** > **Cloud and virtualization** > **Azure**, выберите нужный экземпляр Azure, затем нажмите **Save**.

Вносить изменения в преднастроенный дашборд напрямую нельзя, однако его можно клонировать и редактировать. Чтобы клонировать дашборд, откройте меню просмотра (**â¦**) и выберите **Clone**.
Чтобы убрать дашборд из списка дашбордов, его можно скрыть. Для этого откройте меню просмотра (**â¦**) и выберите **Hide**.

Скрытие дашборда не влияет на других пользователей.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Conn monitor](https://dt-cdn.net/images/cm-dashboard-1-3137-226998a645.png)

![Conn monitor preview](https://dt-cdn.net/images/cm-dashboard-1414-d3238a9386.png)

## Доступные метрики

**Connection Monitor**

| Название | Описание | Единица | Рекомендуется |
| --- | --- | --- | --- |
| AverageRoundtripMs | Среднее время сетевого кругового обхода (мс) для зондов мониторинга подключений, отправленных между источником и назначением | MilliSecond | Применимо |
| ProbesFailedPercent | Процент неудавшихся зондов мониторинга подключений | Percent | Применимо |

**Connection Monitor Preview**

| Название | Описание | Единица | Измерения | Рекомендуется |
| --- | --- | --- | --- | --- |
| AverageRoundtripMs | Среднее сетевое RTT для зондов мониторинга подключений, отправленных между источником и назначением | MilliSecond |  |  |
| ChecksFailedPercent | Процент неудавшихся проверок для теста | Percent | Source address, Source endpoint name, Source resource ID, Destination address, Destination endpoint name, Destination resource ID, Destination port, Test group name, Test configuration name | Применимо |
| ProbesFailedPercent | Процент неудавшихся зондов мониторинга подключений | Percent |  |  |
| RoundTripTimeMs | RTT для проверок, отправленных между источником и назначением | MilliSecond | Source address, Source endpoint name, Source resource ID, Destination address, Destination endpoint name, Destination resource ID, Destination port, Test group name, Test configuration name | Применимо |
