---
title: Azure Stream Analytics monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-stream-analytics
scraped: 2026-03-02T21:32:59.961251
---

# Мониторинг Azure Stream Analytics

# Мониторинг Azure Stream Analytics

* Актуальная версия Dynatrace
* Практическое руководство
* Чтение: 2 мин
* Опубликовано 23 сен. 2020 г.

Dynatrace получает метрики из Azure Metrics API для Azure Stream Analytics. Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать метрики по нескольким измерениям и создавать пользовательские графики, которые можно закрепить на дашбордах.

## Предварительные требования

* Dynatrace версии 1.203+
* Environment ActiveGate версии 1.195+

## Включение мониторинга

Чтобы узнать, как включить мониторинг сервиса, см. [Включение мониторинга сервиса](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## Просмотр метрик сервиса

Метрики сервиса можно просматривать в вашей среде Dynatrace либо на **странице обзора пользовательского устройства**, либо на странице **Дашборды**.

### Просмотр метрик на странице обзора пользовательского устройства

Чтобы перейти на страницу обзора пользовательского устройства:

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

![Stream](https://dt-cdn.net/images/2021-03-12-11-39-16-1056-7bb7a37cb2.png)

## Доступные метрики

| Название | Измерения | Описание | Единица | Рекомендуется |
| --- | --- | --- | --- | --- |
| AMLCalloutFailedRequests | Неудавшиеся запросы функции | Logical name, Partition ID | Count | Применимо |
| AMLCalloutInputEvents | События функции | Logical name, Partition ID | Count |  |
| AMLCalloutRequests | Запросы функции | Logical name, Partition ID | Count | Применимо |
| ConversionErrors | Ошибки преобразования данных | Logical name, Partition ID | Count | Применимо |
| DeserializationError | Ошибки десериализации входных данных | Logical name, Partition ID | Count | Применимо |
| DroppedOrAdjustedEvents | События вне порядка | Logical name, Partition ID | Count | Применимо |
| EarlyInputEvents | Ранние входные события | Logical name, Partition ID | Count | Применимо |
| Errors | Ошибки среды выполнения | Logical name, Partition ID | Count | Применимо |
| InputEventBytes | Байты входных событий | Logical name, Partition ID | Byte |  |
| InputEvents | Входные события | Logical name, Partition ID | Count | Применимо |
| InputEventsSourcesBacklogged | Входные события в очереди | Logical name, Partition ID | Count | Применимо |
| InputEventsSourcesPerSecond | Полученные входные источники | Logical name, Partition ID | PerSecond | Применимо |
| LateInputEvents | Поздние входные события | Logical name, Partition ID | Count | Применимо |
| OutputEvents | Выходные события | Logical name, Partition ID | Count | Применимо |
| OutputWatermarkDelaySeconds | Задержка водяного знака | Logical name, Partition ID | Second | Применимо |
| ResourceUtilization | Процент использования ресурсов | Logical name, Partition ID | Percent | Применимо |
