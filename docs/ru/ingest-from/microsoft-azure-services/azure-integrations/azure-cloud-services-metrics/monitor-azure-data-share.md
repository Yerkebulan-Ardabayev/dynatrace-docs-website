---
title: Мониторинг Azure Data Share
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-data-share
scraped: 2026-03-02T21:28:14.296102
---

# Azure Data Share monitoring


* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jun 25, 2020

Dynatrace принимает метрики из Azure Metrics API для Azure Data Share. Вы можете просматривать метрики для каждого экземпляра службы, разбивать метрики по нескольким измерениям и создавать пользовательские графики, которые можно закрепить на своих дашбордах.

## Предварительные требования

* Dynatrace версии 1.203+
* Environment ActiveGate версии 1.195+

## Включение мониторинга

Чтобы узнать, как включить мониторинг службы, см. раздел [Enable service monitoring](../azure-monitoring-guide/azure-enable-service-monitoring.md "Enable Azure monitoring in Dynatrace.").

## Просмотр метрик службы

Вы можете просматривать метрики службы в вашей среде Dynatrace либо на **странице обзора пользовательского устройства**, либо на странице **Dashboards**.

### Просмотр метрик на странице обзора пользовательского устройства

Чтобы перейти на страницу обзора пользовательского устройства:

1. Перейдите в ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Отфильтруйте по названию службы и выберите соответствующую группу пользовательских устройств.
3. После выбора группы пользовательских устройств вы окажетесь на **странице обзора группы пользовательских устройств**.
4. На **странице обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), принадлежащие группе. Выберите экземпляр для перехода на **страницу обзора пользовательского устройства**.

### Просмотр метрик на дашборде

Если для службы предусмотрен готовый дашборд, на вашей странице **Dashboards** появится готовый дашборд для соответствующей службы, содержащий все рекомендованные метрики. Искать конкретные дашборды можно с помощью фильтрации по **Preset**, а затем по **Name**.

Для уже отслеживаемых служб может потребоваться повторное сохранение учётных данных, чтобы готовый дашборд появился на странице **Dashboards**. Чтобы повторно сохранить учётные данные, перейдите в **Settings** > **Cloud and virtualization** > **Azure**, выберите нужный экземпляр Azure, затем нажмите **Save**.

Вносить изменения в готовый дашборд напрямую нельзя, но его можно клонировать и редактировать. Чтобы клонировать дашборд, откройте меню просмотра (**...**) и выберите **Clone**.
Чтобы удалить дашборд из списка дашбордов, его можно скрыть. Чтобы скрыть дашборд, откройте меню просмотра (**...**) и выберите **Hide**.

Скрытие дашборда не влияет на других пользователей.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Data share](https://dt-cdn.net/images/dashboard-80-1920-72f664b28a.png)

## Доступные метрики

| Название | Измерения | Единица измерения | Рекомендуется |
| --- | --- | --- | --- |
| FailedShareSubscriptionSynchronizations |  | Count | Applicable |
| FailedShareSynchronizations |  | Count | Applicable |
| ShareCount | ShareName | Count | Applicable |
| ShareSubscriptionCount |  | Count | Applicable |
| SucceededShareSubscriptionSynchronizations |  | Count | Applicable |
| SucceededShareSynchronizations |  | Count | Applicable |
