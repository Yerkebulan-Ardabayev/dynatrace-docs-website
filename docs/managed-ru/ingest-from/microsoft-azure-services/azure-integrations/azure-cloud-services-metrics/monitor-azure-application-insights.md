---
title: Мониторинг Azure Application Insights
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-application-insights
scraped: 2026-05-12T11:25:23.790956
---

# Мониторинг Azure Application Insights

# Мониторинг Azure Application Insights

* Практическое руководство
* Чтение: 4 мин
* Опубликовано 22 сентября 2020 г.

Dynatrace получает метрики из Azure Metrics API для Azure Application Insights. Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать метрики по различным измерениям и создавать пользовательские графики, которые можно закрепить на ваших дашбордах.

## Предварительные требования

* Dynatrace версии 1.203+
* Environment ActiveGate версии 1.198+

## Включение мониторинга

О том, как включить мониторинг сервиса, см. в разделе [Включение мониторинга сервиса](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Включение мониторинга Azure в Dynatrace.").

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

![Insights](https://dt-cdn.net/images/2021-03-12-11-44-29-1661-92088ffd2d.png)

Insights

## Доступные метрики

| Имя | Описание | Измерения | Единица измерения | Рекомендуется |
| --- | --- | --- | --- | --- |
| requests/duration | Время между получением HTTP-запроса и завершением отправки ответа | Request performance, Result code, Is traffic synthetic, Cloud role instance, Successful request, Cloud role name | Миллисекунда | Применимо |
| requests/count | Количество завершённых HTTP-запросов | Request performance, Result code, Is traffic synthetic, Cloud role instance, Successful request, Cloud role name | Количество | Применимо |
| requests/failed | Количество неуспешных HTTP-запросов | Request performance, Result code, Is traffic synthetic, Cloud role instance, Cloud role name | Количество | Применимо |
| availabilityResults/availabilityPercentage | Процент успешно завершённых тестов доступности | Test name, Run location, | Процент | Применимо |
| availabilityResults/count | Количество тестов доступности | Test name, Run location, Test result | Количество |  |
| availabilityResults/duration | Длительность теста доступности | Test name, Run location, Test result | Миллисекунда |  |
| browserTimings/networkDuration | Время между запросом пользователя и сетевым подключением |  | Миллисекунда | Применимо |
| browserTimings/processingDuration | Время от получения последнего байта документа до загрузки DOM |  | Миллисекунда | Применимо |
| browserTimings/receiveDuration | Время получения ответа |  | Миллисекунда | Применимо |
| browserTimings/sendDuration | Время отправки запроса |  | Миллисекунда | Применимо |
| browserTimings/totalDuration | Время загрузки страницы в браузере |  | Миллисекунда |  |
| dependencies/count | Количество вызовов зависимостей | Dependency type, Dependency performance, Successful call, Target of a dependency call, Result code, Is traffic synthetic, Cloud role instance, Cloud role name | Количество | Применимо |
| dependencies/duration | Длительность вызова зависимости | Dependency type, Dependency performance, Successful call, Target of a dependency call, Result code, Is traffic synthetic, Cloud role instance, Cloud role name | Миллисекунда |  |
| dependencies/failed | Количество неуспешных вызовов зависимостей | Dependency type, Dependency performance, Target of a dependency call, Result code, Is traffic synthetic, Cloud role instance, Cloud role name | Количество | Применимо |
| pageViews/count | Количество просмотров страниц | Is traffic synthetic, Cloud role name, | Количество | Применимо |
| pageViews/duration | Время загрузки просмотра страницы | Is traffic synthetic, Cloud role name | Миллисекунда |  |
| performanceCounters/requestExecutionTime | Время выполнения HTTP-запроса | Cloud role instance | Миллисекунда |  |
| performanceCounters/requestsInQueue | HTTP-запросы в очереди приложения | Cloud role instance | Количество |  |
| performanceCounters/requestsPerSecond | Частота HTTP-запросов | Cloud role instance | В секунду | Применимо |
| performanceCounters/exceptionsPerSecond | Частота исключений | Cloud role instance | В секунду |  |
| performanceCounters/processIOBytesPerSecond | Частота ввода-вывода процесса | Cloud role instance | Байт в секунду | Применимо |
| performanceCounters/processCpuPercentage | Процессорное время | Cloud role instance | Процент | Применимо |
| performanceCounters/processorCpuPercentage |  | Cloud role instance | Процент | Применимо |
| performanceCounters/memoryAvailableBytes | Доступная память | Cloud role instance | Байт | Применимо |
| performanceCounters/processPrivateBytes | Приватные байты процесса | Cloud role instance | Байт |  |
| requests/rate | Частота запросов к серверу | Request performance, Result code, Is traffic synthetic, Cloud role instance, Successful request, Cloud role name | В секунду | Применимо |
| exceptions/count | Количество исключений | Cloud role name, Cloud role instance, Device type | Количество |  |
| exceptions/browser | Исключения в браузере | Cloud role name | Количество | Применимо |
| exceptions/server | Исключения на сервере | Cloud role name, Cloud role instance | Количество | Применимо |
| traces/count | Количество трассировок | Severity level, Is traffic synthetic, Cloud role name, Cloud role instance | Количество |  |

## Ограничения

Одновременный запуск расширения Azure App Service и Azure Application Insights не поддерживается.