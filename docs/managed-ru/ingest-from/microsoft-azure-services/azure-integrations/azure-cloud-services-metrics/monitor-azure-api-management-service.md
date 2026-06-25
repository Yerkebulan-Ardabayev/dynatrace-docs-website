---
title: Мониторинг Azure API Management Service
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-api-management-service
scraped: 2026-05-12T11:26:46.067821
---

# Мониторинг Azure API Management Service

# Мониторинг Azure API Management Service

* Практическое руководство
* Чтение: 2 мин
* Обновлено 15 ноября 2023 г.

Информацию о различиях между классическими службами и другими службами см. в разделе [Миграция с классических служб Azure (ранее «встроенных») на облачные службы](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide "Перенос классических служб Azure на их новые версии.").

Dynatrace получает метрики из Azure Metrics API для Azure API Management Service. Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать метрики по различным измерениям и создавать пользовательские графики, которые можно закрепить на ваших дашбордах.

## Предварительные условия

* Dynatrace версии 1.199+
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

## Доступные метрики

Этот сервис отслеживает часть Azure API Management (Microsoft.ApiManagement/service). Пока этот сервис настроен, вы не можете включить сервис Azure Application Service (built-in) (устаревший).

| Имя | Описание | Измерения | Единица измерения | Рекомендуется |
| --- | --- | --- | --- | --- |
| Overall duration of gateway requests | Общая длительность запросов шлюза в миллисекундах | Location, Hostname | Миллисекунда |  |
| Duration of backend requests | Длительность запросов к бэкенду в миллисекундах | Location, Hostname | Миллисекунда |  |
| Capacity | Метрика использования для сервиса ApiManagement. Примечание: для SKU, отличных от Premium, агрегация 'Max' покажет значение 0. | Location | Процент | Применимо |
| Total event hub events | Количество событий, отправленных в EventHub | Location | Количество | Применимо |
| Successful event hub events | Количество успешных событий EventHub | Location | Количество | Применимо |
| Failed event hub events | Количество неудачных событий EventHub | Location | Количество | Применимо |
| Rejected event hub events | Количество отклонённых событий EventHub (неверная конфигурация или отсутствие авторизации) | Location | Количество |  |
| Throttled event hub events | Количество событий EventHub, подвергнутых регулированию | Location | Количество |  |
| Timed out event hub events | Количество событий EventHub с истёкшим временем ожидания | Location | Количество |  |
| Dropped event hub events | Количество событий, пропущенных из-за достижения лимита размера очереди | Location | Количество |  |
| Size of event hub events | Общий размер событий EventHub в байтах | Location | Байт |  |
| Requests | Метрики запросов шлюза с несколькими измерениями | Location, Hostname, Last error reason, Backend response code, Gateway response code, Backend response code category, Gateway response code category | Количество | Применимо |
| Network connectivity status of resources (preview) | Статус сетевой связности зависимых типов ресурсов со стороны сервиса API Management | Location, Resource type | Количество |  |
| Web socket messages (preview) | Количество сообщений WebSocket по выбранному источнику и назначению | Location, Source, Destination | Количество |  |
| Web socket connection attempts (preview) | Количество попыток подключения WebSocket по выбранному источнику и назначению | Location, Source, Destination, State | Количество |  |