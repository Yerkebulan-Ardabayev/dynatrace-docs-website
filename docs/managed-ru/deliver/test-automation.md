---
title: Интеграция Dynatrace с инструментами нагрузочного тестирования
source: https://docs.dynatrace.com/managed/deliver/test-automation
scraped: 2026-05-12T11:09:55.715582
---

# Dynatrace and load testing tools integration

# Dynatrace and load testing tools integration

* Published Jun 14, 2018

Интегрируя Dynatrace в существующий процесс нагрузочного тестирования, вы можете раньше прекращать сборку при выявлении проблем в вашем пайплайне поставки.

![Load Testing process](https://dt-cdn.net/images/dynatrace-loadtesting-process-1785-bf9e8cf86f.png)

Процесс нагрузочного тестирования

## Доступные интеграции

Dynatrace предлагает несколько готовых интеграций с фреймворками автоматизации тестирования.

Автоматизация тестирования предполагает использование специального ПО (отдельного от тестируемого) для управления выполнением тестов и сравнения фактических результатов с ожидаемыми. Автоматизация тестирования позволяет автоматизировать некоторые повторяющиеся задачи в уже налаженном процессе формального тестирования или выполнять дополнительное тестирование, которое было бы сложно сделать вручную. Автоматизация тестирования важна для непрерывной поставки и непрерывного тестирования.

[JMeter](/managed/deliver/test-automation/dynatrace-and-jmeter-integration) [LoadRunner](/managed/deliver/test-automation/dynatrace-and-loadrunner-integration) [Neotys](/managed/deliver/test-automation/neotys-integration)

## Тегирование тестовых запросов и отправка пользовательских событий

### Тегирование тестов с помощью HTTP-заголовков

При выполнении нагрузочного теста из вашего инструмента нагрузочного тестирования ([JMeter](/managed/deliver/test-automation/dynatrace-and-jmeter-integration "Learn how you can add custom HTTP headers in JMeter to tag distributed traces and requests in Dynatrace for targeted diagnostics and analysis of your load tests."), [Neotys](https://www.neotys.com/resources/whitepaper/dynatrace-integration-neoload), LoadRunner и др.) каждый имитируемый HTTP-запрос можно тегировать дополнительными HTTP-заголовками, содержащими информацию о тестовой транзакции (например, имя скрипта, имя шага теста и ID виртуального пользователя). Dynatrace может анализировать входящие HTTP-заголовки, извлекать такую контекстную информацию из значений заголовков и тегировать захваченные запросы с помощью [атрибутов запроса](/managed/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views."). Атрибуты запроса позволяют [фильтровать данные мониторинга по определённым тегам](/managed/observe/application-observability/services/request-attributes/filter-monitoring-data-via-request-attributes "Use request attributes to filter your monitoring data and narrow down service analysis scope.").

![Load Testing HTTP header](https://dt-cdn.net/images/dynatrace-loadtesting-httptagging-1186-cfea1a2702.png)

HTTP-заголовок нагрузочного теста

Для передачи контекстной информации можно использовать любые (или несколько) HTTP-заголовков или HTTP-параметров. [Правила извлечения](/managed/observe/application-observability/services/request-attributes/capture-request-attributes-based-on-web-request-data "Create request attributes based on web request data.") можно настроить через **Settings** > **Server-side service monitoring** > **Request attributes**.

В следующих примерах используется заголовок `x-dynatrace-test` со следующим набором пар ключ/значение:

|  |  |
| --- | --- |
| VU | ID **V**иртуального **п**ользователя (**V**irtual **U**ser), отправившего запрос. |
| SI | **S**ource **I**D — идентифицирует продукт, инициировавший запрос (JMeter, LoadRunner, Neotys и др.). |
| TSN | **T**est **S**tep **N**ame — логический шаг теста в скрипте нагрузочного тестирования (например, `Login` или `Add to cart`). |
| LSN | **L**oad **S**cript **N**ame — имя скрипта нагрузочного тестирования. Группирует набор тестовых шагов, составляющих многошаговую транзакцию (например, онлайн-покупку). |
| LTN | **L**oad **T**est **N**ame — уникально идентифицирует выполнение теста (например, `6h Load Test — June 25`). |
| PC | **P**age **C**ontext — предоставляет информацию о документе, загруженном на текущей обрабатываемой странице. |

### Отправка пользовательских событий

При выполнении нагрузочного теста можно отправлять дополнительную контекстную информацию в Dynatrace с помощью [API пользовательских событий](/managed/dynatrace-api/environment-api/events-v1#api-events-post-event "Find out what you can do with the Dynatrace Events API."). Пользовательская аннотация затем появляется в разделе **Events** на всех страницах обзора сущностей, определённых в вызове API (см. пример ниже).

![Loadtesting event custom annotation](https://dt-cdn.net/images/dynatrace-loadtesting-annotation-1100-a9baf541e3.png)

Пользовательская аннотация события нагрузочного теста

События нагрузочного теста также отображаются на страницах связанных сервисов (см. пример ниже).

![Loadtest custom annotation in chart](https://dt-cdn.net/images/dynatrace-loadtesting-annotation-chart-1399-df488eb91d.png)

Пользовательская аннотация нагрузочного теста на графике

### Отправка метрик нагрузочного тестирования в Dynatrace

Также можно отправлять конкретные метрики из инструмента нагрузочного тестирования (пропускная способность, нагрузка пользователей и т.д.) в Dynatrace через [API пользовательских метрик](/managed/dynatrace-api/environment-api/metric-v1/custom-metrics "Manage custom metrics via the Timeseries v1 API.").

Для JMeter доступен новый [open-source плагин](https://github.com/dynatrace-oss/jmeter-dynatrace-plugin), который можно использовать для отправки метрик непосредственно в Dynatrace через Metrics API.

## Сравнение и анализ

Существует несколько способов анализа данных. Подход должен быть основан на типе анализа производительности (например, сбои, узкие места по ресурсам и производительности или проблемы масштабируемости). Ниже приведён обзор некоторых полезных подходов для анализа нагрузочных тестов. Разумеется, можно использовать любую функцию анализа и диагностики Dynatrace.

### Фильтрация

* Через [атрибуты запроса](/managed/observe/application-observability/services/request-attributes/filter-monitoring-data-via-request-attributes "Use request attributes to filter your monitoring data and narrow down service analysis scope.")  
  После тегирования запросов соответствующими HTTP-заголовками можно использовать определённые атрибуты запроса для фильтрации данных мониторинга.
* Через [правила именования запросов](/managed/observe/application-observability/services/service-detection/service-detection-v1/set-up-request-naming "Adjust request naming and define the operations your services offer.")  
  Можно определить правило именования веб-запросов на основе атрибутов запроса для удобного доступа к данным мониторинга нагрузочных тестов. Например, можно определить правило именования по имени шага теста (например, `TSN` в примере ниже).

  Пример правила именования TSN

  ![Loadtesting request naming rule](https://dt-cdn.net/images/dynatrace-loadtesting-requestnamingrule-918-45c07d7d67.png)

  Правило именования запросов нагрузочного теста

  В результате это правило создаёт отдельный отслеживаемый запрос для каждого шага теста. Поскольку правила именования запросов создают отдельные запросы к сервису, каждый запрос независимо базируется и контролируется на предмет аномалий производительности.
* Через [ключевые запросы](/managed/observe/application-observability/services-classic/monitor-key-requests "Discover how to closely monitor requests that are critical to your business.")  
  Если запросы помечены как ключевые, они будут отдельно доступны через конечную точку [Metrics API v1](/managed/dynatrace-api/environment-api/metric-v1 "Retrieve metric information via Timeseries v1 API.") Dynatrace.

  ![Load test requests](https://dt-cdn.net/images/dynatrace-loadtesting-loadtestrequests-1504-f5f6bc2ccd.png)

  Запросы нагрузочного теста

### Многомерный анализ

Данные, захваченные через атрибуты запроса, можно использовать для построения собственного [многомерного анализа](/managed/observe/application-observability/multidimensional-analysis "Configure a multidimensional analysis view and save it as a calculated metric."). **Представления многомерного анализа** полезны для мониторинга эволюции нагрузочных тестов с течением времени.

### Сравнение

* [Представление Compare](https://www.dynatrace.com/news/blog/compare-service-request-performance-behavior-time/) позволяет сравнивать критические метрики запросов к сервисам (время ответа, сбои, CPU и нагрузка) между двумя нагрузочными тестами.

  ![Load testing compare](https://dt-cdn.net/images/dynatrace-loadtesting-compare-2217-2d06c0115c.png)

  Сравнение нагрузочных тестов
* [Представления анализа времени ответа и анализа сбоев](/managed/observe/application-observability/services-classic/response-time-distribution-and-outlier-analysis "Gain insights into the distribution of response times across all requests, including those that are either unusually high or unusually low.") можно использовать для детального понимания изменений производительности.

  ![Load testing response time analysis](https://dt-cdn.net/images/dynatrace-loadtesting-responsetimeanalysis-1509-089136b54b.png)

  Анализ времени ответа нагрузочного теста

### Диагностика

Инструмент диагностики [top web requests](https://www.dynatrace.com/news/blog/analyze-the-top-web-requests-across-all-your-services/) можно использовать для анализа наиболее частых веб-запросов ко всем сервисам. Используйте определённые атрибуты запроса для фильтрации запросов нагрузочного теста.

## Представление результатов

[Metrics API v1](/managed/dynatrace-api/environment-api/metric-v1 "Retrieve metric information via Timeseries v1 API.") позволяет получать данные по конкретным сущностям (процессам, сервисам, методам сервисов и т.д.) и передавать их в инструменты, определяющие момент остановки пайплайна сборки.

[Problem API](/managed/dynatrace-api/environment-api/problems "Find out what the Dynatrace Problems v1 API offers.") предоставляет метрики и сведения о проблемах, обнаруженных Dynatrace в ходе нагрузочных тестов.

## Дополнительные соображения

### Окна технического обслуживания

Если нагрузочный тест выполняется в производственном окружении и нежелательно негативное влияние на общие базовые линии сервисов и приложений, перед проведением тестирования рекомендуется определить [окна технического обслуживания](/managed/analyze-explore-automate/notifications-and-alerting/maintenance-windows "Understand when to use a maintenance window. Read about the supported maintenance window types."). Использование окон технического обслуживания во время нагрузочного тестирования гарантирует, что всплески нагрузки, увеличенное время ответа или повышенная частота ошибок не будут негативно влиять на общее базирование.

В качестве альтернативы, если у вас есть выделенное окружение для нагрузочного тестирования и вы хотите использовать [обнаружение проблем](/managed/observe/infrastructure-observability/hosts/configuration/anomaly-detection "Configure host anomaly detection, including problem and event thresholds.") во время тестов, не следует использовать окна технического обслуживания во время выполнения нагрузочного теста.

## Связанные темы

* [[Blog] Load testing redefined: From KPI reporting to AI-supported performance engineering](https://www.dynatrace.com/news/blog/load-testing-redefined-a-guide-from-kpi-reporting-to-ai-supported-performance-engineering)
* [[Blog] Unbreakable DevOps Pipeline: Shift-Left, Shift-Right & Self-Healing](https://www.dynatrace.com/news/blog/unbreakable-devops-pipeline-shift-left-shift-right-self-healing)