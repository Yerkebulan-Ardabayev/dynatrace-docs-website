---
title: Azure Front Door (classic) monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-front-door
scraped: 2026-03-06T21:27:23.128258
---

# Мониторинг Azure Front Door (classic)

# Мониторинг Azure Front Door (classic)

* Latest Dynatrace
* Руководство
* 2 мин. чтения
* Обновлено 27 сен. 2023 г.

Страница обзора Azure Front Door (classic) предоставляет сведения о количестве обслуженных клиентских запросов, задержке и эффективности вашей маршрутизации.

## Предварительные требования

* Dynatrace версии 1.196+
* Environment ActiveGate версии 1.195+

Этот сервис отслеживает предыдущую (классическую) версию [Azure Front Door](https://dt-url.net/rz0390g).

Сведения о последней версии сервиса Microsoft [Azure Front Door Standard и Premium](https://learn.microsoft.com/en-us/azure/frontdoor/front-door-overview) (`Front Door and CDN profile`) см. в разделе [Мониторинг Azure Front Door Standard/Premium и профилей CDN](monitor-azure-front-door-cdn-profiles.md "Мониторинг Azure Front Door Standard/Premium и профилей CDN и просмотр доступных метрик.").

## Включение мониторинга

Сведения о включении мониторинга сервиса см. в разделе [Включение мониторинга сервиса](../azure-monitoring-guide/azure-enable-service-monitoring.md "Включите мониторинг Azure в Dynatrace.").

## Просмотр метрик сервиса

Метрики сервиса можно просматривать в вашей среде Dynatrace на **странице обзора пользовательского устройства** или на странице **Dashboards**.

### Просмотр метрик на странице обзора пользовательского устройства

Чтобы перейти на страницу обзора пользовательского устройства

1. Перейдите в ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Отфильтруйте по имени сервиса и выберите соответствующую группу пользовательских устройств.
3. После выбора группы пользовательских устройств вы окажетесь на **странице обзора группы пользовательских устройств**.
4. На **странице обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), входящие в группу. Выберите экземпляр, чтобы перейти на **страницу обзора пользовательского устройства**.

### Просмотр метрик на дашборде

Если для сервиса предусмотрен готовый дашборд, он появится на странице **Dashboards** с рекомендуемыми метриками. Поиск конкретных дашбордов можно выполнять с помощью фильтра **Preset**, а затем по **Name**.

Для существующих отслеживаемых сервисов может потребоваться повторное сохранение учётных данных, чтобы готовый дашборд появился на странице **Dashboards**. Для повторного сохранения учётных данных перейдите в **Settings** > **Cloud and virtualization** > **Azure**, выберите нужный экземпляр Azure, а затем выберите **Save**.

Вносить изменения в готовый дашборд напрямую нельзя, но его можно клонировать и редактировать. Чтобы клонировать дашборд, откройте меню обзора (**...**) и выберите **Clone**.
Чтобы удалить дашборд из списка, его можно скрыть. Для этого откройте меню обзора (**...**) и выберите **Hide**.

Скрытие дашборда не влияет на других пользователей.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Frontdoor dash](https://dt-cdn.net/images/frontdoor-1600-ab764051bd.png)

## Доступные метрики

| Имя | Описание | Единица | Рекомендуется |
| --- | --- | --- | --- |
| BackendHealthPercentage | Процент успешных проверок работоспособности от HTTP/S-прокси к бэкендам | Percent | Applicable |
| BackendRequestCount | Количество запросов, отправленных HTTP/S-прокси к бэкендам | Count | Applicable |
| BackendRequestLatency | Время от отправки запроса HTTP/S-прокси к бэкенду до получения последнего байта ответа от бэкенда HTTP/S-прокси | MilliSeconds | Applicable |
| BillableResponseSize | Количество оплачиваемых байт (минимум 2 КБ на запрос), отправленных в виде ответов от HTTP/S-прокси клиентам | Bytes |  |
| RequestCount | Количество клиентских запросов, обслуженных HTTP/S-прокси | Count | Applicable |
| RequestSize | Количество байт, отправленных в виде запросов от клиентов к HTTP/S-прокси | Bytes | Applicable |
| ResponseSize | Количество байт, отправленных в виде ответов от HTTP/S-прокси клиентам | Bytes | Applicable |
| TotalLatency | Время от получения клиентского запроса HTTP/S-прокси до подтверждения клиентом последнего байта ответа от HTTP/S-прокси | MilliSeconds | Applicable |
| WebApplicationFirewallRequestCount | Количество клиентских запросов, обработанных Web Application Firewall | Count | Applicable |
