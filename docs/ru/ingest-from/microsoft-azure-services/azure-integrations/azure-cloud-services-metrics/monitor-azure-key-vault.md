---
title: Мониторинг Azure Key Vault
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-key-vault
scraped: 2026-03-05T21:40:30.301955
---

# Мониторинг Azure Key Vault


* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jun 25, 2020

Dynatrace принимает метрики из Azure Metrics API для Azure Key Vault. Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать метрики по нескольким измерениям и создавать пользовательские диаграммы, которые можно закрепить на дашбордах.

## Предварительные условия

* Dynatrace версии 1.201+
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

![Key vault](https://dt-cdn.net/images/key-vault-dashboard-1920-537bfb50e1.png)

## Доступные метрики

| Name | Description | Unit | Dimensions | Recommended |
| --- | --- | --- | --- | --- |
| Availability | Vault requests availability | Percent | ActivityType, ActivityName, StatusCode, StatusCodeClass | Applicable |
| ServiceApiHit | Total number of service API hits | Count | ActivityType, ActivityName, StatusCode, StatusCodeClass | Applicable |
| ServiceApiLatency | Overall latency of service API | MilliSecond | ActivityType, ActivityName, StatusCode, StatusCodeClass | Applicable |
| ServiceApiResult | Total number of service API results | Count | ActivityType, ActivityName, StatusCode, StatusCodeClass | Applicable |
| SaturationShoebox | Vault capacity used | Percent | ActivityType, ActivityName, StatusCode, StatusCodeClass | Applicable |
