---
title: Azure Cognitive Services - Ink Recognizer monitoring (deprecated)
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-cognitive-services-ink-recognizer
scraped: 2026-03-04T21:39:33.010885
---

# Мониторинг Azure Cognitive Services - Ink Recognizer (устаревший)

# Мониторинг Azure Cognitive Services - Ink Recognizer (устаревший)

* Latest Dynatrace
* Практическое руководство
* Чтение: 1 мин
* Опубликовано 22 сент. 2020 г.

Dynatrace получает метрики из Azure Metrics API для Ink Recognizer. Вы можете просматривать метрики для каждого экземпляра службы, разбивать метрики по нескольким измерениям и создавать пользовательские графики, которые можно закрепить на ваших дашбордах.

## Предварительные требования

* Dynatrace версии 1.203+
* Environment ActiveGate версии 1.195+

## Включение мониторинга

Чтобы узнать, как включить мониторинг службы, см. [Включение мониторинга службы](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## Просмотр метрик службы

Метрики службы можно просматривать в вашей среде Dynatrace либо на **странице обзора пользовательского устройства**, либо на странице **Дашборды**.

### Просмотр метрик на странице обзора пользовательского устройства

Чтобы перейти на страницу обзора пользовательского устройства:

1. Перейдите в ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Отфильтруйте по имени службы и выберите соответствующую группу пользовательских устройств.
3. После выбора группы пользовательских устройств вы окажетесь на **странице обзора группы пользовательских устройств**.
4. На **странице обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), входящие в группу. Выберите экземпляр для просмотра **страницы обзора пользовательского устройства**.

### Просмотр метрик на дашборде

Если для службы предусмотрен предустановленный дашборд, на вашей странице **Дашборды** появится предустановленный дашборд для соответствующей службы, содержащий все рекомендуемые метрики. Вы можете искать конкретные дашборды, фильтруя по **Preset**, а затем по **Name**.

Для уже отслеживаемых служб может потребоваться повторно сохранить учётные данные, чтобы предустановленный дашборд появился на странице **Дашборды**. Чтобы повторно сохранить учётные данные, перейдите в **Settings** > **Cloud and virtualization** > **Azure**, выберите нужный экземпляр Azure, затем нажмите **Save**.

Вносить изменения в предустановленный дашборд напрямую нельзя, но его можно клонировать и редактировать. Чтобы клонировать дашборд, откройте меню просмотра (**…**) и выберите **Clone**.
Чтобы удалить дашборд из списка, его можно скрыть. Для этого откройте меню просмотра (**…**) и выберите **Hide**.

Скрытие дашборда не влияет на других пользователей.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Cognitive services](https://dt-cdn.net/images/dashboard-79-1423-6e181ef360.png)

## Доступные метрики

| Название | Описание | Измерения | Единица | Рекомендуется |
| --- | --- | --- | --- | --- |
| BlockedCalls | Количество вызовов, превысивших ограничение по частоте или квоте | ApiName, OperationName, Region | Count | Применимо |
| ClientErrors | Количество вызовов с ошибкой на стороне клиента (код ответа HTTP `4xx`) | ApiName, OperationName, Region | Count | Применимо |
| DataIn | Размер входящих данных в байтах | ApiName, OperationName, Region | Byte | Применимо |
| DataOut | Размер исходящих данных в байтах | ApiName, OperationName, Region | Byte | Применимо |
| Latency | Задержка в миллисекундах | ApiName, OperationName, Region | MilliSecond | Применимо |
| ServerErrors | Количество вызовов с внутренней ошибкой службы (код ответа HTTP `5xx`) | ApiName, OperationName, Region | Count | Применимо |
| SuccessfulCalls | Количество успешных вызовов | ApiName, OperationName, Region | Count | Применимо |
| TotalCalls | Общее количество вызовов | ApiName, OperationName, Region | Count |  |
| TotalErrors | Общее количество вызовов с ответом об ошибке (код ответа HTTP `4xx` или `5xx`) | ApiName, OperationName, Region | Count | Применимо |
