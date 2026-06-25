---
title: Интеграция Dynatrace и JMeter
source: https://docs.dynatrace.com/managed/deliver/test-automation/dynatrace-and-jmeter-integration
scraped: 2026-05-12T11:38:32.539787
---

# Dynatrace and JMeter integration

# Dynatrace and JMeter integration

* Published Apr 12, 2018

При выполнении нагрузочного теста в Apache JMeter каждый имитируемый HTTP-запрос можно тегировать в JMeter дополнительными HTTP-заголовками, содержащими информацию о тестовой транзакции (например, имя скрипта, имя шага теста и ID виртуального пользователя). Dynatrace может анализировать входящие HTTP-заголовки, извлекать такую контекстную информацию из значений заголовков и «тегировать» захваченные запросы. Наличие тега на запросе позволяет анализировать запросы с конкретными тегами. Например, можно проанализировать все запросы, поступившие из скрипта `Scenario1` и шага теста `Put Item into Cart`.

Для интеграции Dynatrace с JMeter:

1. В JMeter используйте [HTTP Header Manager](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Header_Manager) для добавления пользовательских HTTP-заголовков запросов. Для передачи контекстной информации можно использовать любые пользовательские HTTP-заголовки. В данном примере используется заголовок `x-dynatrace-test` со значением `LSN=Scenario1;TSN=Put Item into Cart;`. Подробнее о рекомендуемых парах ключ/значение см. в разделе [Интеграция Dynatrace с инструментами нагрузочного тестирования](/managed/deliver/test-automation "Learn how you can integrate Dynatrace into your load testing process.").

![JMeter Http Header manager](https://dt-cdn.net/images/jmeter-httpheadermanager-1382-6305950980.png)

HTTP Header Manager в JMeter

2. В Dynatrace настройте правила извлечения для пользовательских HTTP-заголовков через **Settings** > **Server-side service monitoring** > **Request attributes**.
3. Выберите **HTTP request header** в качестве **Request attribute source** и введите имя вашего пользовательского HTTP-заголовка в поле **Parameter name**. Также можно настроить извлечение данных из конкатенированной строки (например, `LSN=Scenario1;TSN=Put Item into Cart;`), как показано ниже.

![Request attributes](https://dt-cdn.net/images/jmeter-definerequestattribute-1095-ce93ef5c26.png)

Атрибуты запроса

4. Запустите нагрузочный тест из JMeter. Запросы и распределённые трассировки будут тегированы в Dynatrace настроенными атрибутами запросов для целевой диагностики и анализа.

## Дополнительное чтение

* [Как интегрировать Dynatrace в процесс нагрузочного тестирования?](/managed/deliver/test-automation "Learn how you can integrate Dynatrace into your load testing process.")
* [Blog: Load testing redefined: From KPI reporting to AI-supported performance engineering](https://www.dynatrace.com/news/blog/load-testing-redefined-a-guide-from-kpi-reporting-to-ai-supported-performance-engineering/)

## Связанные темы

* [Интеграция Dynatrace с инструментами нагрузочного тестирования](/managed/deliver/test-automation "Learn how you can integrate Dynatrace into your load testing process.")
* [Захват атрибутов запроса на основе данных веб-запроса](/managed/observe/application-observability/services/request-attributes/capture-request-attributes-based-on-web-request-data "Create request attributes based on web request data.")
* [Фильтрация данных мониторинга через атрибуты запроса](/managed/observe/application-observability/services/request-attributes/filter-monitoring-data-via-request-attributes "Use request attributes to filter your monitoring data and narrow down service analysis scope.")