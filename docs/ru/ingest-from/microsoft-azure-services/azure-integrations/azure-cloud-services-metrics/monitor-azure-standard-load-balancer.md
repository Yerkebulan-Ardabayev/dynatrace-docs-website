---
title: Мониторинг Azure Standard Load Balancer
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-standard-load-balancer
scraped: 2026-03-06T21:28:17.913970
---

* 2 мин. чтения

Информацию о различиях между классическими и другими службами Azure см. в разделе Переход с классических служб Azure (ранее — встроенных) на облачные службы.

Dynatrace принимает метрики из Azure Metrics API для Azure Standard Load Balancer. Вы можете просматривать метрики для каждого экземпляра службы, разбивать метрики по нескольким измерениям и создавать пользовательские графики, которые можно закреплять на панелях мониторинга.

## Предварительные требования

* Dynatrace версии 1.199+
* Environment ActiveGate версии 1.195+

## Включение мониторинга

Сведения о включении мониторинга служб см. в разделе Включение мониторинга служб.

## Просмотр метрик службы

Метрики службы можно просматривать в среде Dynatrace либо на **странице обзора пользовательского устройства**, либо на странице **Dashboards**.

### Просмотр метрик на странице обзора пользовательского устройства

Чтобы перейти на страницу обзора пользовательского устройства:

1. Перейдите в ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Отфильтруйте по имени службы и выберите нужную группу пользовательских устройств.
3. После выбора группы вы окажетесь на **странице обзора группы пользовательских устройств**.
4. На **странице обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), принадлежащие группе. Выберите экземпляр, чтобы перейти на **страницу обзора пользовательского устройства**.

### Просмотр метрик на панели мониторинга

Если у службы есть предустановленная панель мониторинга, на вашей странице **Dashboards** появится предустановленная панель для данной службы со всеми рекомендуемыми метриками. Вы можете искать конкретные панели, фильтруя по **Preset**, а затем по **Name**.

Для уже отслеживаемых служб может потребоваться повторное сохранение учётных данных, чтобы предустановленная панель появилась на странице **Dashboards**. Для повторного сохранения учётных данных перейдите в **Settings** > **Cloud and virtualization** > **Azure**, выберите нужный экземпляр Azure, затем нажмите **Save**.

Вносить изменения непосредственно в предустановленную панель нельзя, но её можно клонировать и редактировать. Чтобы клонировать панель, откройте меню просмотра (**...**) и выберите **Clone**.
Чтобы удалить панель из списка, её можно скрыть. Для этого откройте меню просмотра (**...**) и выберите **Hide**.

Скрытие панели не влияет на других пользователей.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

## Доступные метрики

Данная служба отслеживает часть Azure Load Balancer (Microsoft.Network/loadBalancers). При наличии настроенной службы невозможно одновременно включить службу Azure Load Balancers (встроенная).

| Название | Описание | Измерения | Единица | Рекомендуется |
| --- | --- | --- | --- | --- |
| Data path availability | Средняя доступность пути к данным Load Balancer за период времени | Frontend IP address, Frontend port | Count | Применимо |
| Health probe status | Средний статус пробы работоспособности Load Balancer за период времени | Protocol type, Backend port, Frontend IP address, Frontend port, Backend IP address | Count | Применимо |
| Byte count | Общее количество байтов, переданных за период времени | Frontend IP address, Frontend port, Direction | Byte |  |
| Packet count | Общее количество пакетов, переданных за период времени | Frontend IP address, Frontend port, Direction | Count |  |
| SYN count | Общее количество SYN-пакетов, переданных за период времени | Frontend IP address, Frontend port, Direction | Count |  |
| SNAT connection count | Общее количество новых SNAT-соединений, созданных за период времени | Frontend IP address, Backend IP address, Connection state | Count |  |
| Allocated SNAT ports | Общее количество портов SNAT, выделенных за период времени | Frontend IP address, Backend IP address, Protocol type | Count |  |
| Used SNAT ports | Общее количество используемых портов SNAT за период времени | Frontend IP address, Backend IP address, Protocol type | Count |  |
| Health probe status | Статус работоспособности и состояния серверной части Azure Cross-region Load Balancer за период времени | Frontend IP address, Frontend port, Backend IP address, Protocol type, Frontend region, Backend region | Count |  |
