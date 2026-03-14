---
title: Мониторинг Azure Synapse Analytics (Synapse Workspace, Apache Spark pool, SQL pool)
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-synapse-analytics
scraped: 2026-03-06T21:26:29.714702
---

# Мониторинг Azure Synapse Analytics (Synapse Workspace, Apache Spark pool, SQL pool)

# Мониторинг Azure Synapse Analytics (Synapse Workspace, Apache Spark pool, SQL pool)

* Последняя версия Dynatrace
* Практическое руководство
* Чтение: 4 мин
* Опубликовано 23 сент. 2020

Dynatrace получает метрики из Azure Metrics API для Azure Analytics (Synapse Workspace, Apache Spark pool, SQL pool). Вы можете просматривать метрики для каждого экземпляра сервиса, разделять метрики по нескольким измерениям и создавать пользовательские графики, которые можно закрепить на дашбордах.

## Предварительные требования

* Dynatrace версии 1.203+
* Environment ActiveGate версии 1.195+

## Включение мониторинга

Чтобы узнать, как включить мониторинг сервиса, см. [Включение мониторинга сервиса](../azure-monitoring-guide/azure-enable-service-monitoring.md "Включение мониторинга Azure в Dynatrace.").

## Просмотр метрик сервиса

Вы можете просматривать метрики сервиса в вашей среде Dynatrace на **странице обзора пользовательского устройства** или на странице **Дашборды**.

### Просмотр метрик на странице обзора пользовательского устройства

Чтобы перейти на страницу обзора пользовательского устройства

1. Перейдите в ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Отфильтруйте по имени сервиса и выберите соответствующую группу пользовательских устройств.
3. После выбора группы пользовательских устройств вы окажетесь на **странице обзора группы пользовательских устройств**.
4. На **странице обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), принадлежащие группе. Выберите экземпляр для просмотра **страницы обзора пользовательского устройства**.

### Просмотр метрик на дашборде

Если для сервиса имеется предустановленный дашборд, вы получите предустановленный дашборд для соответствующего сервиса со всеми рекомендуемыми метриками на странице **Дашборды**. Вы можете искать конкретные дашборды, фильтруя по **Предустановленный**, а затем по **Имени**.

Для существующих отслеживаемых сервисов может потребоваться повторное сохранение учётных данных, чтобы предустановленный дашборд появился на странице **Дашборды**. Чтобы повторно сохранить учётные данные, перейдите в **Settings** > **Cloud and virtualization** > **Azure**, выберите нужный экземпляр Azure и нажмите **Save**.

Вы не можете вносить изменения в предустановленный дашборд напрямую, но можете клонировать и редактировать его. Чтобы клонировать дашборд, откройте меню (**...**) и выберите **Clone**.
Чтобы удалить дашборд из списка дашбордов, вы можете скрыть его. Чтобы скрыть дашборд, откройте меню (**...**) и выберите **Hide**.

Скрытие дашборда не влияет на других пользователей.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Synapse workspace](https://dt-cdn.net/images/dashboard-86-1365-48045e63d7.png)

## Доступные метрики

**Synapse Workspace**

| Название | Описание | Измерения | Единица измерения | Рекомендуется |
| --- | --- | --- | --- | --- |
| IntegrationActivityRunsEnded | Количество операций оркестрации, которые завершились успешно, с ошибкой или были отменены | Result, Failure type, Activity, Activity type, Pipeline | Count | Применимо |
| IntegrationPipelineRunsEnded | Количество запусков конвейеров оркестрации, которые завершились успешно, с ошибкой или были отменены | Result, Failure type, Pipeline | Count | Применимо |
| IntegrationTriggerRunsEnded | Количество триггеров оркестрации, которые завершились успешно, с ошибкой или были отменены | Result, Failure type, Trigger | Count | Применимо |
| BuiltinSqlPoolLoginAttempts | Количество попыток входа, завершившихся успешно или с ошибкой | Result, Failure type | Count |  |
| BuiltinSqlPoolRequestsEnded | Количество запросов, которые завершились успешно, с ошибкой или были отменены | Result, Failure type | Count | Применимо |
| BuiltinSqlPoolDataProcessedBytes | Объём данных, обработанных запросами |  | Byte | Применимо |

**Apache Spark pool**

| Название | Описание | Измерения | Единица измерения | Рекомендуется |
| --- | --- | --- | --- | --- |
| BigDataPoolApplicationsActive | Активные приложения Apache Spark | Job state | Count | Применимо |
| BigDataPoolApplicationsEnded | Завершённые приложения Apache Spark | Job result, Job type | Count | Применимо |
| BigDataPoolAllocatedMemory | Выделенная память (в ГБ) | Submitter ID | Count | Применимо |
| BigDataPoolAllocatedCores | Выделенные виртуальные ядра | Submitter ID | Count | Применимо |

**SQL pool**

| Название | Описание | Единица измерения | Измерения | Рекомендуется |
| --- | --- | --- | --- | --- |
| AdaptiveCacheHitPercent | Показывает, насколько эффективно рабочие нагрузки используют адаптивный кеш. Используйте эту метрику совместно с метрикой процента попаданий в кеш, чтобы определить, нужно ли масштабировать дополнительные мощности или перезапустить рабочие нагрузки для заполнения кеша. | Percent |  | Применимо |
| AdaptiveCacheUsedPercent | Показывает, насколько эффективно рабочие нагрузки используют адаптивный кеш. Используйте эту метрику совместно с метрикой процента использования кеша, чтобы определить, нужно ли масштабировать дополнительные мощности или перезапустить рабочие нагрузки для заполнения кеша. | Percent |  | Применимо |
| Connections | Общее количество подключений к SQL pool | Count | Result | Применимо |
| ConnectionsBlockedByFirewall | Количество подключений, заблокированных правилами файрвола | Count |  |  |
| DWULimit | Целевой уровень обслуживания SQL pool | Count |  | Применимо |
| DWUUsed | Использование ресурсов SQL pool, рассчитанное как DWU limit * DWU percentage | Count |  | Применимо |
| DWUUsedPercent | Использование ресурсов SQL pool, рассчитанное как максимум между процентом CPU и процентом ввода-вывода данных | Percent |  | Применимо |
| LocalTempDBUsedPercent | Использование локальной tempdb на всех вычислительных узлах. Значения передаются каждые пять минут. | Percent |  | Применимо |
| MemoryUsedPercent | Использование памяти на всех узлах SQL pool | Percent |  | Применимо |
| WLGActiveQueries | Активные запросы в группе рабочей нагрузки | Count | Is user defined, Workload group | Применимо |
| WLGActiveQueriesTimeouts | Запросы группы рабочей нагрузки, для которых истекло время ожидания | Count | Is user defined, Workload group | Применимо |
| WLGAllocationByMaxResourcePercent | Процент выделения ресурсов относительно эффективного предельного процента ресурсов на группу рабочей нагрузки | Percent | Is user defined, Workload group |  |
| WLGAllocationBySystemPercent | Процент выделения ресурсов относительно всей системы | Percent | Is user defined, Workload group |  |
| WLGEffectiveCapResourcePercent | Эффективный предельный процент ресурсов для группы рабочей нагрузки | Percent | Is user defined, Workload group |  |
| WLGQueuedQueries | Общее количество запросов, поставленных в очередь после достижения предела максимальной параллельности | Count | Is user defined, Workload group |  |
| wlg\_effective\_min\_resource\_percent | Эффективный минимальный процент ресурсов с учётом уровня обслуживания и настроек группы рабочей нагрузки | Percent | Is user defined, Workload group |  |
