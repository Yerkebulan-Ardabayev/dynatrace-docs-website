---
title: Мониторинг Azure ExpressRoute Circuit
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-expressroute-circuit
scraped: 2026-03-03T21:32:31.882413
---

* Latest Dynatrace
* How-to guide
* 1-min read

Dynatrace принимает метрики для нескольких предварительно выбранных пространств имён, включая Azure ExpressRoute Circuit. Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать метрики по нескольким измерениям и создавать пользовательские диаграммы, которые можно закрепить на дашбордах.

## Предварительные условия

* Dynatrace версии 1.200+
* Environment ActiveGate версии 1.195+

## Включение мониторинга

Сведения о включении мониторинга сервиса см. в разделе [Enable service monitoring](../azure-monitoring-guide/azure-enable-service-monitoring.md "Enable Azure monitoring in Dynatrace.").

## Просмотр метрик сервиса

Метрики сервиса можно просматривать в вашей среде Dynatrace либо на **странице обзора пользовательского устройства**, либо на странице **Dashboards**.

### Просмотр метрик на странице обзора пользовательского устройства

Чтобы перейти на страницу обзора пользовательского устройства:

1. Перейдите в ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Отфильтруйте по имени сервиса и выберите соответствующую группу пользовательских устройств.
3. После выбора группы пользовательских устройств вы окажетесь на **странице обзора группы пользовательских устройств**.
4. На **странице обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), входящие в группу. Выберите экземпляр для просмотра **страницы обзора пользовательского устройства**.

### Просмотр метрик на дашборде

Если для сервиса предусмотрен предустановленный дашборд, на странице **Dashboards** появится предустановленный дашборд для соответствующего сервиса, содержащий все рекомендуемые метрики. Найти нужные дашборды можно с помощью фильтрации по **Preset**, а затем по **Name**.

Для уже отслеживаемых сервисов, возможно, потребуется повторно сохранить учётные данные, чтобы предустановленный дашборд появился на странице **Dashboards**. Для повторного сохранения учётных данных перейдите в **Settings** > **Cloud and virtualization** > **Azure**, выберите нужный экземпляр Azure, затем нажмите **Save**.

Вносить изменения непосредственно в предустановленный дашборд невозможно, но его можно клонировать и редактировать. Чтобы клонировать дашборд, откройте меню просмотра (**...**) и выберите **Clone**.
Чтобы удалить дашборд из списка, можно скрыть его. Для этого откройте меню просмотра (**...**) и выберите **Hide**.

Скрытие дашборда не влияет на других пользователей.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Express dash](https://dt-cdn.net/images/dashboard-36-1699-420811ae56.png)

## Доступные метрики

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| ArpAvailability | ARP availability from MSEE towards all peers | PeeringType, Peer | Percent | Applicable |
| BgpAvailability | BGP availability from MSEE towards all peers | PeeringType, Peer | Percent | Applicable |
| BitsInPerSecond | Bits ingressing Azure per second | PeeringType | PerSecond | Applicable |
| BitsOutPerSecond | Bits egressing Azure per second | PeeringType | PerSecond | Applicable |
| QosDropBitsInPerSecond | Ingress bits of data dropped per second |  | PerSecond | Applicable |
| QosDropBitsOutPerSecond | Egress bits of data dropped per second |  | PerSecond | Applicable |
