---
title: Мониторинг Azure Data Factory (V1, V2)
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-data-factory
scraped: 2026-03-06T21:34:04.551751
---

* Latest Dynatrace

Dynatrace получает метрики из Azure Metrics API для Azure Data Factory (V1, V2). Вы можете просматривать метрики для каждого экземпляра сервиса, разделять метрики по нескольким измерениям и создавать пользовательские графики, которые можно закреплять на ваших панелях мониторинга.

## Предварительные требования

* Dynatrace версии 1.199+
* Environment ActiveGate версии 1.195+

## Включение мониторинга

Чтобы узнать, как включить мониторинг сервиса, см. Включение мониторинга сервиса.

## Просмотр метрик сервиса

Вы можете просмотреть метрики сервиса в вашей среде Dynatrace на **странице обзора пользовательского устройства** или на странице **Dashboards**.

### Просмотр метрик на странице обзора пользовательского устройства

Для доступа к странице обзора пользовательского устройства

1. Перейдите в ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Отфильтруйте по имени сервиса и выберите соответствующую группу пользовательских устройств.
3. После выбора группы пользовательских устройств вы окажетесь на **странице обзора группы пользовательских устройств**.
4. На **странице обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), принадлежащие группе. Выберите экземпляр для просмотра **страницы обзора пользовательского устройства**.

### Просмотр метрик на панели мониторинга

Если у сервиса есть предустановленная панель мониторинга, вы получите предустановленную панель для соответствующего сервиса, содержащую все рекомендованные метрики, на странице **Dashboards**. Вы можете искать конкретные панели, фильтруя по **Preset**, а затем по **Name**.

Для уже мониторируемых сервисов может потребоваться повторно сохранить учётные данные, чтобы предустановленная панель появилась на странице **Dashboards**. Чтобы повторно сохранить учётные данные, перейдите в **Settings** > **Cloud and virtualization** > **Azure**, выберите нужный экземпляр Azure, затем нажмите **Save**.

Вы не можете вносить изменения в предустановленную панель напрямую, но можете клонировать и редактировать её. Чтобы клонировать панель, откройте меню обзора (**...**) и выберите **Clone**.
Чтобы удалить панель из списка панелей, вы можете её скрыть. Чтобы скрыть панель, откройте меню обзора (**...**) и выберите **Hide**.

Скрытие панели не влияет на других пользователей.

![Клонирование и скрытие Azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Data Factory 1](https://dt-cdn.net/images/2021-03-12-10-56-34-1618-f4f03adbc4.png)

![Data Factory 2](https://dt-cdn.net/images/2021-03-12-11-01-37-1813-741106667f.png)

## Доступные метрики

### Azure Data Factory V1

| Имя | Описание | Измерения | Единица измерения | Рекомендуется |
| --- | --- | --- | --- | --- |
| FailedRuns | Общее количество неудачных запусков за минутное окно | pipelineName, activityName | Количество | Применимо |
| SuccessfulRuns | Общее количество успешных запусков за минутное окно | pipelineName, activityName | Количество | Применимо |

### Azure Data Factory V2

| Имя | Описание | Измерения | Единица измерения | Рекомендуется |
| --- | --- | --- | --- | --- |
| ActivityCancelledRuns | Общее количество отменённых запусков действий за минутное окно | ActivityType, PipelineName, FailureType, Name | Количество |  |
| ActivityFailedRuns | Общее количество неудачных запусков действий за минутное окно | ActivityType, PipelineName, FailureType, Name | Количество | Применимо |
| ActivitySucceededRuns | Общее количество успешных запусков действий за минутное окно | ActivityType, PipelineName, FailureType, Name | Количество | Применимо |
| FactorySizeInGbUnits | Общий размер фабрики (в ГБ) |  | Гигабайт |  |
| IntegrationRuntimeAvailableMemory | Доступная память среды выполнения интеграции | IntegrationRuntimeName, NodeName | Байт | Применимо |
| IntegrationRuntimeAvailableNodeNumber | Количество доступных узлов среды выполнения интеграции | IntegrationRuntimeName | Количество |  |
| IntegrationRuntimeAverageTaskPickupDelay | Длительность очереди среды выполнения интеграции | IntegrationRuntimeName | Секунда |  |
| IntegrationRuntimeCpuPercentage | Использование ЦП среды выполнения интеграции | IntegrationRuntimeName, NodeName | Процент | Применимо |
| IntegrationRuntimeQueueLength | Длина очереди среды выполнения интеграции | IntegrationRuntimeName | Количество |  |
| MaxAllowedFactorySizeInGbUnits | Максимально допустимый размер фабрики (в ГБ) |  | Гигабайт |  |
| MaxAllowedResourceCount | Максимально допустимое количество сущностей |  | Количество |  |
| PipelineCancelledRuns | Метрики отменённых запусков конвейера | FailureType, Name | Количество |  |
| PipelineFailedRuns | Метрики неудачных запусков конвейера | FailureType, Name | Количество | Применимо |
| PipelineSucceededRuns | Метрики успешных запусков конвейера | FailureType, Name | Количество | Применимо |
| ResourceCount | Общее количество сущностей |  | Количество |  |
| SSISIntegrationRuntimeStartCancel | Общее количество отменённых запусков SSIS IR за минутное окно | IntegrationRuntimeName | Количество |  |
| SSISIntegrationRuntimeStartFailed | Общее количество неудачных запусков SSIS IR за минутное окно | IntegrationRuntimeName | Количество |  |
| SSISIntegrationRuntimeStartSucceeded | Общее количество успешных запусков SSIS IR за минутное окно | IntegrationRuntimeName | Количество |  |
| SSISIntegrationRuntimeStopStuck | Общее количество зависших остановок SSIS IR за минутное окно | IntegrationRuntimeName | Количество |  |
| SSISIntegrationRuntimeStopSucceeded | Общее количество успешных остановок SSIS IR за минутное окно | IntegrationRuntimeName | Количество |  |
| SSISPackageExecutionCancel | Общее количество отменённых выполнений пакетов SSIS за минутное окно | IntegrationRuntimeName | Количество |  |
| SSISPackageExecutionFailed | Общее количество неудачных выполнений пакетов SSIS за минутное окно | IntegrationRuntimeName | Количество |  |
| SSISPackageExecutionSucceeded | Общее количество успешных выполнений пакетов SSIS за минутное окно | IntegrationRuntimeName | Количество |  |
| TriggerCancelledRuns | Общее количество отменённых запусков триггеров за минутное окно | Name, FailureType | Количество |  |
| TriggerFailedRuns | Общее количество неудачных запусков триггеров за минутное окно | Name, FailureType | Количество | Применимо |
| TriggerSucceededRuns | Общее количество успешных запусков триггеров за минутное окно | Name, FailureType | Количество | Применимо |
