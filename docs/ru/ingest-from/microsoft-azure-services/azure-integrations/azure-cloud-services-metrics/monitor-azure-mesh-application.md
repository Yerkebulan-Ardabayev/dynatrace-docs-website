---
title: Azure Mesh Application monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-mesh-application
scraped: 2026-03-06T21:29:53.332620
---

# Мониторинг Azure Mesh Application

# Мониторинг Azure Mesh Application

* Последняя версия Dynatrace
* Практическое руководство
* Время чтения: 1 мин
* Опубликовано 10 сент. 2020 г.

Эта служба была выведена из эксплуатации компанией Microsoft. Подробнее см. в [объявлении Microsoft](https://azure.microsoft.com/en-us/updates/azure-service-fabric-mesh-preview-retirement/).

Dynatrace получает метрики из Azure Metrics API для Azure Mesh Application. Вы можете просматривать метрики для каждого экземпляра службы, разбивать метрики по нескольким измерениям и создавать пользовательские графики, которые можно закрепить на панелях мониторинга.

## Предварительные требования

* Dynatrace версии 1.201+
* Среда ActiveGate версии 1.195+

## Включение мониторинга

Чтобы узнать, как включить мониторинг службы, см. раздел [Включение мониторинга службы](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## Просмотр метрик службы

Вы можете просматривать метрики службы в вашей среде Dynatrace либо на **странице обзора пользовательского устройства**, либо на странице **Панели мониторинга**.

### Просмотр метрик на странице обзора пользовательского устройства

Чтобы перейти на страницу обзора пользовательского устройства:

1. Перейдите в ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Отфильтруйте по имени службы и выберите соответствующую группу пользовательских устройств.
3. После выбора группы пользовательских устройств вы перейдёте на **страницу обзора группы пользовательских устройств**.
4. На **странице обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), входящие в группу. Выберите экземпляр для перехода на **страницу обзора пользовательского устройства**.

### Просмотр метрик на панели мониторинга

Если для службы предусмотрена предустановленная панель мониторинга, на странице **Панели мониторинга** появится предустановленная панель для соответствующей службы, содержащая все рекомендуемые метрики. Вы можете искать конкретные панели, фильтруя по **Preset**, а затем по **Name**.

Для уже отслеживаемых служб может потребоваться повторно сохранить учётные данные, чтобы предустановленная панель появилась на странице **Панели мониторинга**. Чтобы повторно сохранить учётные данные, перейдите в **Settings** > **Cloud and virtualization** > **Azure**, выберите нужный экземпляр Azure, затем нажмите **Save**.

Вносить изменения в предустановленную панель мониторинга напрямую нельзя, но её можно клонировать и редактировать. Чтобы клонировать панель, откройте меню обзора (**…**) и выберите **Clone**.
Чтобы убрать панель из списка, её можно скрыть. Для этого откройте меню обзора (**…**) и выберите **Hide**.

Скрытие панели не влияет на других пользователей.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Mesh](https://dt-cdn.net/images/dashboard-63-2674-12efdf4c98.png)

## Доступные метрики

| Название | Описание | Единица | Измерения | Рекомендуется |
| --- | --- | --- | --- | --- |
| AllocatedCpu | Выделенный ЦП согласно шаблону Azure Resource Manager | ApplicationName, ServiceName, CodePackageName, ServiceReplicaName | Count | Применимо |
| AllocatedMemory | Выделенная память согласно шаблону Azure Resource Manager | ApplicationName, ServiceName, CodePackageName, ServiceReplicaName | Byte | Применимо |
| ActualCpu | Использование ЦП | ApplicationName, ServiceName, CodePackageName, ServiceReplicaName | Count | Применимо |
| ActualMemory | Использование памяти | ApplicationName, ServiceName, CodePackageName, ServiceReplicaName | Byte | Применимо |
| CpuUtilization | Процент фактического использования ЦП от выделенного | ApplicationName, ServiceName, CodePackageName, ServiceReplicaName | Percent | Применимо |
| MemoryUtilization | Процент фактического использования памяти от выделенной | ApplicationName, ServiceName, CodePackageName, ServiceReplicaName | Percent | Применимо |
