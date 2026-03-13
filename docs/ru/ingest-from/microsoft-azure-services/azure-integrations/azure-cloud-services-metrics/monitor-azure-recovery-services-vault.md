---
title: Azure Recovery Services Vault
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-recovery-services-vault
scraped: 2026-03-04T21:31:42.502593
---

# Azure Recovery Services Vault

# Azure Recovery Services Vault

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Mar 07, 2024

Dynatrace версии 1.281+ Environment ActiveGate версии 1.195+

Dynatrace получает метрики из Azure Metrics API для Azure Recovery Services Vault. Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать метрики по нескольким измерениям и создавать пользовательские графики, которые можно закрепить на своих дашбордах.

## Включение мониторинга

Сведения о включении мониторинга сервисов см. в разделе [Включение мониторинга сервисов](../azure-monitoring-guide/azure-enable-service-monitoring.md "Enable Azure monitoring in Dynatrace.").

## Просмотр метрик сервиса

Метрики сервиса в вашей среде Dynatrace можно просматривать на **странице обзора пользовательского устройства** или на странице **Dashboards**.

### Просмотр метрик на странице обзора пользовательского устройства

Чтобы перейти на страницу обзора пользовательского устройства:

1. Перейдите в ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Отфильтруйте по имени сервиса и выберите соответствующую группу пользовательских устройств.
3. После выбора группы пользовательских устройств вы перейдёте на **страницу обзора группы пользовательских устройств**.
4. На **странице обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), входящие в группу. Выберите экземпляр для перехода на **страницу обзора пользовательского устройства**.

### Просмотр метрик на дашборде

Если для сервиса существует предустановленный дашборд, он появится на вашей странице **Dashboards** и будет содержать все рекомендованные метрики для соответствующего сервиса. Для поиска конкретных дашбордов можно использовать фильтры **Preset** и **Name**.

Для уже отслеживаемых сервисов может потребоваться повторно сохранить учётные данные, чтобы предустановленный дашборд появился на странице **Dashboards**. Для повторного сохранения учётных данных перейдите в **Settings** > **Cloud and virtualization** > **Azure**, выберите нужный экземпляр Azure и нажмите **Save**.

Вносить изменения в предустановленный дашборд напрямую нельзя, но его можно клонировать и редактировать. Чтобы клонировать дашборд, откройте меню просмотра (**...**) и выберите **Clone**.
Чтобы удалить дашборд из списка, его можно скрыть. Для скрытия дашборда откройте меню просмотра (**...**) и выберите **Hide**.

Скрытие дашборда не влияет на других пользователей.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

## Доступные метрики

| Название | Описание | Измерения | Единица | Рекомендовано |
| --- | --- | --- | --- | --- |
| BackupHealthEvent |  | Backup instance ID, Backup instance name, Datasource ID, Datasource type, Health status | Count | Applicable |
| RestoreHealthEvent |  | Backup instance ID, Backup instance name, Datasource ID, Datasource type, Health status | Count | Applicable |
