---
title: Мониторинг Azure Application Insights
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-application-insights
scraped: 2026-03-04T21:35:49.902914
---

# Мониторинг Azure Application Insights

# Мониторинг Azure Application Insights

* Последняя версия Dynatrace
* Практическое руководство
* Чтение: 4 мин
* Опубликовано 22 сент. 2020

Dynatrace получает метрики из Azure Metrics API для Azure Application Insights. Вы можете просматривать метрики для каждого экземпляра сервиса, разделять метрики по нескольким измерениям и создавать пользовательские графики, которые можно закрепить на дашбордах.

## Предварительные требования

* Dynatrace версии 1.203+
* Environment ActiveGate версии 1.198+

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

![Insights](https://dt-cdn.net/images/2021-03-12-11-44-29-1661-92088ffd2d.png)

## Доступные метрики

| Название | Описание | Измерения | Единица измерения | Рекомендуется |
| --- | --- | --- | --- | --- |
| requests/duration | Время между получением HTTP-запроса и завершением отправки ответа | Request performance, Result code, Is traffic synthetic, Cloud role instance, Successful request, Cloud role name | MilliSecond | Применимо |
| requests/count | Количество завершённых HTTP-запросов | Request performance, Result code, Is traffic synthetic, Cloud role instance, Successful request, Cloud role name | Count | Применимо |
| requests/failed | Количество неудачных HTTP-запросов | Request performance, Result code, Is traffic synthetic, Cloud role instance, Cloud role name | Count | Применимо |
| availabilityResults/availabilityPercentage | Процент успешно завершённых тестов доступности | Test name, Run location, | Percent | Применимо |
| availabilityResults/count | Количество тестов доступности | Test name, Run location, Test result | Count |  |
| availabilityResults/duration | Длительность теста доступности | Test name, Run location, Test result | MilliSecond |  |
| browserTimings/networkDuration | Время между запросом пользователя и сетевым подключением |  | MilliSecond | Применимо |
| browserTimings/processingDuration | Время между получением последнего байта документа и загрузкой DOM |  | MilliSecond | Применимо |
| browserTimings/receiveDuration | Время получения ответа |  | MilliSecond | Применимо |
| browserTimings/sendDuration | Время отправки запроса |  | MilliSecond | Применимо |
| browserTimings/totalDuration | Время загрузки страницы в браузере |  | MilliSecond |  |
| dependencies/count | Количество вызовов зависимостей | Dependency type, Dependency performance, Successful call, Target of a dependency call, Result code, Is traffic synthetic, Cloud role instance, Cloud role name | Count | Применимо |
| dependencies/duration | Длительность вызова зависимости | Dependency type, Dependency performance, Successful call, Target of a dependency call, Result code, Is traffic synthetic, Cloud role instance, Cloud role name | MilliSecond |  |
| dependencies/failed | Количество неудачных вызовов зависимостей | Dependency type, Dependency performance, Target of a dependency call, Result code, Is traffic synthetic, Cloud role instance, Cloud role name | Count | Применимо |
| pageViews/count | Количество просмотров страниц | Is traffic synthetic, Cloud role name, | Count | Применимо |
| pageViews/duration | Время загрузки просмотра страницы | Is traffic synthetic, Cloud role name | MilliSecond |  |
| performanceCounters/requestExecutionTime | Время выполнения HTTP-запроса | Cloud role instance | MilliSecond |  |
| performanceCounters/requestsInQueue | HTTP-запросы в очереди приложения | Cloud role instance | Count |  |
| performanceCounters/requestsPerSecond | Частота HTTP-запросов | Cloud role instance | PerSecond | Применимо |
| performanceCounters/exceptionsPerSecond | Частота исключений | Cloud role instance | PerSecond |  |
| performanceCounters/processIOBytesPerSecond | Скорость ввода-вывода процесса | Cloud role instance | BytePerSecond | Применимо |
| performanceCounters/processCpuPercentage | Процессорное время | Cloud role instance | Percent | Применимо |
| performanceCounters/processorCpuPercentage |  | Cloud role instance | Percent | Применимо |
| performanceCounters/memoryAvailableBytes | Доступная память | Cloud role instance | Byte | Применимо |
| performanceCounters/processPrivateBytes | Приватные байты процесса | Cloud role instance | Byte |  |
| requests/rate | Частота серверных запросов | Request performance, Result code, Is traffic synthetic, Cloud role instance, Successful request, Cloud role name | PerSecond | Применимо |
| exceptions/count | Количество исключений | Cloud role name, Cloud role instance, Device type | Count |  |
| exceptions/browser | Исключения браузера | Cloud role name | Count | Применимо |
| exceptions/server | Серверные исключения | Cloud role name, Cloud role instance | Count | Применимо |
| traces/count | Количество трассировок | Severity level, Is traffic synthetic, Cloud role name, Cloud role instance | Count |  |

## Ограничения

Одновременное использование расширения Azure App Service вместе с Azure Application Insights не поддерживается.
