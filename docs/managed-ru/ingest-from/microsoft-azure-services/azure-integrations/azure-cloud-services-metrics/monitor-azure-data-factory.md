---
title: Мониторинг Azure Data Factory (V1, V2)
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-data-factory
scraped: 2026-05-12T11:27:22.613528
---

# Мониторинг Azure Data Factory (V1, V2)

# Мониторинг Azure Data Factory (V1, V2)

* Практическое руководство
* Чтение: 3 мин
* Опубликовано 27 июля 2020 г.

Dynatrace получает метрики из Azure Metrics API для Azure Data Factory (V1, V2). Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать метрики по различным измерениям и создавать пользовательские графики, которые можно закрепить на ваших дашбордах.

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

![Data fact 1](https://dt-cdn.net/images/2021-03-12-10-56-34-1618-f4f03adbc4.png)

Data fact 1

![Data fact 2](https://dt-cdn.net/images/2021-03-12-11-01-37-1813-741106667f.png)

Data fact 2

## Доступные метрики

### Azure Data Factory V1

| Имя | Описание | Измерения | Единица измерения | Рекомендуется |
| --- | --- | --- | --- | --- |
| FailedRuns | Общее количество запусков, завершившихся с ошибкой за минутный интервал | pipelineName, activityName | Количество | Применимо |
| SuccessfulRuns | Общее количество запусков, завершившихся успешно за минутный интервал | pipelineName, activityName | Количество | Применимо |

### Azure Data Factory V2

| Имя | Описание | Измерения | Единица измерения | Рекомендуется |
| --- | --- | --- | --- | --- |
| ActivityCancelledRuns | Общее количество запусков действий, отменённых за минутный интервал | ActivityType, PipelineName, FailureType, Name | Количество |  |
| ActivityFailedRuns | Общее количество запусков действий, завершившихся с ошибкой за минутный интервал | ActivityType, PipelineName, FailureType, Name | Количество | Применимо |
| ActivitySucceededRuns | Общее количество запусков действий, завершившихся успешно за минутный интервал | ActivityType, PipelineName, FailureType, Name | Количество | Применимо |
| FactorySizeInGbUnits | Общий размер фабрики (в ГБ) |  | Гигабайт |  |
| IntegrationRuntimeAvailableMemory | Доступная память среды выполнения интеграции | IntegrationRuntimeName, NodeName | Байт | Применимо |
| IntegrationRuntimeAvailableNodeNumber | Количество доступных узлов среды выполнения интеграции | IntegrationRuntimeName | Количество |  |
| IntegrationRuntimeAverageTaskPickupDelay | Длительность очереди среды выполнения интеграции | IntegrationRuntimeName | Секунда |  |
| IntegrationRuntimeCpuPercentage | Загрузка ЦП среды выполнения интеграции | IntegrationRuntimeName, NodeName | Процент | Применимо |
| IntegrationRuntimeQueueLength | Длина очереди среды выполнения интеграции | IntegrationRuntimeName | Количество |  |
| MaxAllowedFactorySizeInGbUnits | Максимально допустимый размер фабрики (в ГБ) |  | Гигабайт |  |
| MaxAllowedResourceCount | Максимально допустимое количество сущностей |  | Количество |  |
| PipelineCancelledRuns | Метрики отменённых запусков конвейеров | FailureType, Name | Количество |  |
| PipelineFailedRuns | Метрики запусков конвейеров с ошибкой | FailureType, Name | Количество | Применимо |
| PipelineSucceededRuns | Метрики успешных запусков конвейеров | FailureType, Name | Количество | Применимо |
| ResourceCount | Общее количество сущностей |  | Количество |  |
| SSISIntegrationRuntimeStartCancel | Общее количество запусков SSIS IR, отменённых за минутный интервал | IntegrationRuntimeName | Количество |  |
| SSISIntegrationRuntimeStartFailed | Общее количество запусков SSIS IR, завершившихся с ошибкой за минутный интервал | IntegrationRuntimeName | Количество |  |
| SSISIntegrationRuntimeStartSucceeded | Общее количество запусков SSIS IR, завершившихся успешно за минутный интервал | IntegrationRuntimeName | Количество |  |
| SSISIntegrationRuntimeStopStuck | Общее количество остановок SSIS IR, зависших за минутный интервал | IntegrationRuntimeName | Количество |  |
| SSISIntegrationRuntimeStopSucceeded | Общее количество остановок SSIS IR, завершившихся успешно за минутный интервал | IntegrationRuntimeName | Количество |  |
| SSISPackageExecutionCancel | Общее количество выполнений пакетов SSIS, отменённых за минутный интервал | IntegrationRuntimeName | Количество |  |
| SSISPackageExecutionFailed | Общее количество выполнений пакетов SSIS, завершившихся с ошибкой за минутный интервал | IntegrationRuntimeName | Количество |  |
| SSISPackageExecutionSucceeded | Общее количество выполнений пакетов SSIS, завершившихся успешно за минутный интервал | IntegrationRuntimeName | Количество |  |
| TriggerCancelledRuns | Общее количество запусков триггеров, отменённых за минутный интервал | Name, FailureType | Количество |  |
| TriggerFailedRuns | Общее количество запусков триггеров, завершившихся с ошибкой за минутный интервал | Name, FailureType | Количество | Применимо |
| TriggerSucceededRuns | Общее количество запусков триггеров, завершившихся успешно за минутный интервал | Name, FailureType | Количество | Применимо |