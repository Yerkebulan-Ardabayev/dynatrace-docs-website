---
title: Фильтрация данных мониторинга через атрибуты запроса
source: https://www.dynatrace.com/docs/observe/application-observability/services/request-attributes/filter-monitoring-data-via-request-attributes
scraped: 2026-03-06T21:23:07.407482
---

# Фильтрация данных мониторинга с помощью атрибутов запроса


* Последняя версия Dynatrace
* Чтение займёт 2 минуты
* Обновлено 28 июля 2023 г.

После определения атрибутов запроса они отображаются в связанном анализе сервиса и указываются в виде меток для соответствующих запросов.

![Request attributes](https://dt-cdn.net/images/request-attribute-filter-1446-3c51f44605.png)

* Чтобы отфильтровать весь вид страницы только по тем запросам, которые содержат определённый атрибут, выберите атрибут запроса из списка **Request attribute**.
* Чтобы проверить значения атрибута запроса, разверните его строку.

  Выбрав значение, вы можете отфильтровать страницу по запросам, содержащим указанное значение для выбранного атрибута запроса.
* Применённый фильтр по атрибуту запроса или значению атрибута запроса сохраняется в дальнейших опциях анализа, таких как [**Service flow**](../../services-classic/service-flow.md "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment.") и [**Multidimensional analysis**](../../multidimensional-analysis.md "Configure a multidimensional analysis view and save it as a calculated metric.").

  Пример

  Чтобы отфильтровать запросы **BookingService** по значению атрибута запроса, выберите **Request attributes** > **Booking** и укажите значение **checkCreditCard**. Результаты отражают текущие настройки фильтра и показывают те же метрики, что и таблица запросов.

  ![Request attributes' list](https://dt-cdn.net/images/request-attribute-filter-1-1439-2762e66325.png)

  + **Median response time** — это медианное время ответа всех запросов, содержащих данный атрибут запроса.
  + **Total time consumption** — это сумма времён ответа всех запросов за выбранный период времени, имеющих выбранный атрибут запроса.
  + Также можно просматривать соответствующие метрики пропускной способности.

  Нажмите **Create analysis view**, чтобы визуализировать пользовательское представление многомерного анализа, отфильтрованное по выбранному значению атрибута запроса.

  ![Multidimensional analysis filtered by request attribute value](https://dt-cdn.net/images/request-attribute-filter-2-1423-91835f8d9f.png)
* Для фильтрации [пользовательских графиков](../../../../analyze-explore-automate/dashboards-classic/dashboards-upgrade.md "Upgrade your Dynatrace custom charts to Data Explorer visualizations now.") по атрибуту запроса или значению атрибута запроса создайте [пользовательскую метрику](../calculated-service-metric.md "Learn how to create a calculated metric based on web requests.") на основе этих условий.

  Без пользовательской метрики, если атрибут запроса обнаружен для сервиса, на пользовательских графиках отображаются все точки данных для метрики сервиса.

## Связанные темы

* [Захват атрибутов запроса на основе данных веб-запроса](capture-request-attributes-based-on-web-request-data.md "Create request attributes based on web request data.")
* [Захват атрибутов запроса на основе аргументов методов](capture-request-attributes-based-on-method-arguments.md "Learn how to create request attributes based on Java, .NET, or PHP method arguments and how to use them on the serviceâs overview page. Also find out how you can aggregate the captured values of request attributes as well as how you can access objects, in case the value to be captured is a complex object.")
