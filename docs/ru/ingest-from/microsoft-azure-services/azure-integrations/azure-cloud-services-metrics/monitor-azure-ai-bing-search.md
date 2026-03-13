---
title: Azure AI - Bing Search monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-bing-search
scraped: 2026-03-06T21:34:46.561297
---

# Мониторинг Azure AI - Bing Search

# Мониторинг Azure AI - Bing Search

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Sep 22, 2020

Dynatrace получает метрики из Azure Metrics API для Bing Search. Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать метрики по нескольким измерениям и создавать пользовательские графики, которые можно закреплять на дашбордах.

## Предварительные требования

* Dynatrace версии 1.203+
* Environment ActiveGate версии 1.195+

## Включение мониторинга

Чтобы узнать, как включить мониторинг сервиса, см. [Включение мониторинга сервиса](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Включение мониторинга Azure в Dynatrace.").

## Просмотр метрик сервиса

Метрики сервиса можно просматривать в вашей среде Dynatrace либо на **странице обзора пользовательского устройства**, либо на странице **Дашборды**.

### Просмотр метрик на странице обзора пользовательского устройства

Чтобы открыть страницу обзора пользовательского устройства

1. Перейдите в ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Отфильтруйте по имени сервиса и выберите соответствующую группу пользовательских устройств.
3. После выбора группы пользовательских устройств вы окажетесь на **странице обзора группы пользовательских устройств**.
4. На **странице обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), входящие в группу. Выберите экземпляр для просмотра **страницы обзора пользовательского устройства**.

### Просмотр метрик на дашборде

Если для сервиса существует преднастроенный дашборд, вы получите преднастроенный дашборд для соответствующего сервиса со всеми рекомендуемыми метриками на странице **Дашборды**. Вы можете искать конкретные дашборды, фильтруя по **Preset**, а затем по **Name**.

Для уже отслеживаемых сервисов может потребоваться повторно сохранить учётные данные, чтобы преднастроенный дашборд появился на странице **Дашборды**. Чтобы повторно сохранить учётные данные, перейдите в **Settings** > **Cloud and virtualization** > **Azure**, выберите нужный экземпляр Azure и нажмите **Save**.

Вносить изменения в преднастроенный дашборд напрямую нельзя, но его можно клонировать и редактировать. Чтобы клонировать дашборд, откройте меню просмотра (**â¦**) и выберите **Clone**.
Чтобы удалить дашборд из списка дашбордов, его можно скрыть. Для этого откройте меню просмотра (**â¦**) и выберите **Hide**.

Скрытие дашборда не влияет на других пользователей.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Cognitive services](https://dt-cdn.net/images/dashboard-79-1423-6e181ef360.png)

## Доступные метрики

| Название | Описание | Измерения | Единица | Рекомендуется |
| --- | --- | --- | --- | --- |
| BlockedCalls | Количество вызовов, превысивших ограничение скорости или квоты | ApiName, OperationName, Region | Count | Applicable |
| ClientErrors | Количество вызовов с ошибкой на стороне клиента (код ответа HTTP `4xx`) | ApiName, OperationName, Region | Count | Applicable |
| DataIn | Размер входящих данных в байтах | ApiName, OperationName, Region | Byte | Applicable |
| DataOut | Размер исходящих данных в байтах | ApiName, OperationName, Region | Byte | Applicable |
| Latency | Задержка в миллисекундах | ApiName, OperationName, Region | MilliSecond | Applicable |
| ServerErrors | Количество вызовов с внутренней ошибкой сервиса (код ответа HTTP `5xx`) | ApiName, OperationName, Region | Count | Applicable |
| SuccessfulCalls | Количество успешных вызовов | ApiName, OperationName, Region | Count | Applicable |
| TotalCalls | Общее количество вызовов | ApiName, OperationName, Region | Count |  |
| TotalErrors | Общее количество вызовов с ответом об ошибке (код ответа HTTP `4xx` или `5xx`) | ApiName, OperationName, Region | Count | Applicable |
