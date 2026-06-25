---
title: Мониторинг Azure Stream Analytics
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-stream-analytics
scraped: 2026-05-12T11:26:04.543764
---

# Мониторинг Azure Stream Analytics

# Мониторинг Azure Stream Analytics

* Практическое руководство
* Чтение: 2 мин
* Опубликовано 23 сентября 2020 г.

Dynatrace получает метрики из Azure Metrics API для Azure Stream Analytics. Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать метрики по различным измерениям и создавать пользовательские графики, которые можно закрепить на ваших дашбордах.

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

![Stream](https://dt-cdn.net/images/2021-03-12-11-39-16-1056-7bb7a37cb2.png)

Stream

## Доступные метрики

| Имя | Измерения | Описание | Единица измерения | Рекомендуется |
| --- | --- | --- | --- | --- |
| AMLCalloutFailedRequests | Неудачные запросы функций | Logical name, Partition ID | Количество | Применимо |
| AMLCalloutInputEvents | События функций | Logical name, Partition ID | Количество |  |
| AMLCalloutRequests | Запросы функций | Logical name, Partition ID | Количество | Применимо |
| ConversionErrors | Ошибки преобразования данных | Logical name, Partition ID | Количество | Применимо |
| DeserializationError | Ошибки десериализации входных данных | Logical name, Partition ID | Количество | Применимо |
| DroppedOrAdjustedEvents | События, поступившие не по порядку | Logical name, Partition ID | Количество | Применимо |
| EarlyInputEvents | Преждевременные входные события | Logical name, Partition ID | Количество | Применимо |
| Errors | Ошибки среды выполнения | Logical name, Partition ID | Количество | Применимо |
| InputEventBytes | Байты входных событий | Logical name, Partition ID | Байт |  |
| InputEvents | Входные события | Logical name, Partition ID | Количество | Применимо |
| InputEventsSourcesBacklogged | Входные события в бэклоге | Logical name, Partition ID | Количество | Применимо |
| InputEventsSourcesPerSecond | Получено источников входных данных | Logical name, Partition ID | В секунду | Применимо |
| LateInputEvents | Опоздавшие входные события | Logical name, Partition ID | Количество | Применимо |
| OutputEvents | Выходные события | Logical name, Partition ID | Количество | Применимо |
| OutputWatermarkDelaySeconds | Задержка водяного знака | Logical name, Partition ID | Секунда | Применимо |
| ResourceUtilization | Процент использования ресурсов | Logical name, Partition ID | Процент | Применимо |