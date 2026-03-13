---
title: Extract metrics from spans and distributed traces
source: https://www.dynatrace.com/docs/platform/openpipeline/use-cases/tutorial-extract-metrics-from-spans
scraped: 2026-03-06T21:15:57.758999
---

# Извлечение метрик из спанов и распределённых трассировок

# Извлечение метрик из спанов и распределённых трассировок

* Latest Dynatrace
* Руководство
* Время чтения: 5 мин
* Опубликовано 23 декабря 2025 г.

Это руководство показывает, как извлекать метрики непосредственно из спанов и распределённых трассировок через OpenPipeline, который обеспечивает гибкую обработку, обогащение и маршрутизацию в масштабе. Новые метрики могут быть рассчитаны и получены на основе любых данных, доступных в захваченной распределённой трассировке, а также могут быть разделены по нескольким измерениям, например, по рабочей нагрузке Kubernetes или атрибуту запроса.

## Для кого предназначено

Эта статья предназначена для пользователей приложений, создающих долгосрочные метрики для дашбордов из трассировок.

## Что вы узнаете

Как настроить OpenPipeline для извлечения метрики из захваченного спана на пяти примерах, которые можно адаптировать к вашим сервисам.

## Перед началом работы

Необходимые знания

* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "Как использовать Dynatrace Query Language.")
* [Обработка в OpenPipeline](/docs/platform/openpipeline/concepts/processing "Узнайте основные концепции обработки Dynatrace OpenPipeline.")

Предварительные требования

* Среда Dynatrace SaaS на базе Grail и AppEngine.
* Подписка Dynatrace Platform Subscription (DPS) с возможностями [Traces powered by Grail (DPS)](/docs/license/capabilities/traces "Узнайте, как рассчитывается потребление Dynatrace Traces powered by Grail в модели Dynatrace Platform Subscription (DPS).").
* Разрешения OpenPipeline: `settings:objects:read` и `settings:objects:write`. Чтобы узнать, как настроить разрешения, см. [Разрешения в Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Узнайте, как назначать разрешения бакетам и таблицам в Grail.").
* [Разрешения Distributed Tracing](/docs/observe/application-observability/distributed-tracing/permissions#user-permissions-for-distributed-tracing "Управление разрешениями для Distributed Tracing powered by Grail.")

## Примеры

### Запросы к рабочей нагрузке с разделением по Pod Kubernetes

Этот пример показывает новый рекомендуемый способ получения [аналитики на уровне экземпляра сервиса](/docs/observe/application-observability/services-classic/analyze-individual-service-instances "Узнайте, как выполнять анализ экземпляров сервиса.") — концепция, которая уходит в прошлое. Извлекайте метрики из спанов и разделяйте по реальным измерениям развёртывания, таким как рабочая нагрузка Kubernetes, pod, хост и др.

Для типичных разделений, таких как пространство имён, кластер или регион облака, используйте готовые [основные поля Grail](/docs/semantic-dictionary/tags/primary-fields), уже доступные в метриках сервисов; новая метрика не требуется.

1. Найдите условие для соответствующих спанов в Notebooks

1. Перейдите в ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** и откройте существующий или новый блокнот.
2. Выберите  > **DQL**.
3. Используйте DQL-запрос для прототипирования фильтров, полей и группировок перед настройкой OpenPipeline. Например, для исследования спанов, представляющих запросы к рабочей нагрузке, можно использовать следующий запрос:

   ```
   fetch spans



   | filter k8s.workload.name == "my-otel-demo-frontend" and span.kind == "server" and isNotNull(endpoint.name)



   | fields k8s.pod.name, dt.entity.service, endpoint.name, duration



   | limit 200
   ```

   Run in Playground

Понимание условий фильтрации

* `span.kind == "server"` оставляет только входящие запросы, обработанные сервисом, и исключает клиентские или внутренние спаны.
* `isNotNull(endpoint.name)` гарантирует, что спан представляет запрос к эндпоинту, который Dynatrace учитывает в правилах обнаружения эндпоинтов, и что это не заглушённый запрос.

2. Создайте пайплайн для извлечения метрик

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **System events** > **Pipelines**.
2. Выберите существующий пайплайн или создайте новый. Для создания нового пайплайна выберите  **Pipeline** и введите имя — например, `TeamA Span metrics from Services`.
3. Для настройки извлечения метрик перейдите в **Metric extraction** >  **Processor** > **Sampling aware counter metric** и определите процессор, указав:

   * Описательное имя — например, `Requests to my-otel-demo-frontend split by Kubernetes pod`
   * Условие совпадения:

     ```
     k8s.workload.name == "my-otel-demo-frontend"
     ```
   * Ключ новой метрики — например, `span.my-otel-demo-frontend.requests_by_pod.count`
   * Измерения метрики:

     1. Выберите **Pre-defined** и выберите `k8s.pod.name` и `k8s.pod.uid` из [предопределённых измерений](/docs/semantic-dictionary/model/dt-system-events#audit-event "Познакомьтесь с моделями Semantic Dictionary, связанными с системными событиями."). Эти измерения идентифицируют pods, на которых работает рабочая нагрузка. Другие измерения также были предварительно выбраны, например `dt.entity.service`.
     2. Выберите **Save**.

Вы успешно создали новый пайплайн для извлечения метрики, содержащей информацию о количестве запросов к рабочей нагрузке `my-otel-demo-frontend`, и, поскольку метрика содержит pod в качестве измерения, вы сможете разделять запросы по pods. Новый пайплайн виден в списке пайплайнов.

3. Направьте спаны в пайплайн

Создайте динамический маршрут, который направляет интересующие вас спаны в пайплайн команды.

* Один спан будет направлен только в один динамический маршрут. Спаны не могут быть направлены в несколько динамических маршрутов, поэтому условия совпадения должны быть точными и взаимоисключающими.
* Динамические маршруты оцениваются сверху вниз; как только условие совпадения оценивается как «true», спан направляется через этот динамический маршрут.

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **System events** > **Dynamic routing**.
2. Для создания нового маршрута выберите  **Dynamic route** и укажите:

   * Описательное имя — например, `Spans for TeamA Cluster1 Namespace2`
   * Условие совпадения:

     ```
     k8s.cluster.name == "Cluster1" and k8s.namespace.name == "Namespace2"
     ```
3. Выберите **Add**.

Вы успешно создали новый маршрут. Все спаны Kubernetes «Cluster1» и «Namespace2» направляются в пайплайн, где извлекается метрика. Новый маршрут виден в списке маршрутов.

4. Запросите метрику

1. Перейдите в ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** и откройте существующий или новый блокнот.
2. Выберите  > **Metrics** > **Select a metric**.
3. Введите и выберите ключ новой метрики (`span.my-otel-demo-frontend.requests_by_pod.count`).
4. Выберите  **Run**.

Вы успешно извлекли метрику для отслеживания запросов к рабочей нагрузке `my-otel-demo-frontend`.

* Вы можете использовать измерение Kubernetes pod для разделения этой метрики.
* Спаны направляются в новый пайплайн; когда спан принадлежит рабочей нагрузке `my-otel-demo-frontend` (условие совпадения процессора), новый пайплайн извлекает метрику, содержащую pod, на котором работает рабочая нагрузка, в дополнение к другим деталям.
* Вы можете запрашивать метрику в ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** или ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, или просматривать её в ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** или ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**.

### Количество успешно проданных книг по сервисам

В этом примере мы описываем создание пайплайна и процессора извлечения метрик. Для подробных шагов следуйте подходу [примера с разделением рабочей нагрузки по Pod Kubernetes](#workload-requests-pod), но адаптируйте запросы фильтрации и маршрутизацию.

Допущения для примера

Количество проданных книг фиксируется как [атрибут запроса](/docs/observe/application-observability/services/request-attributes "Узнайте, что такое атрибуты запросов и как использовать их на всех уровнях представлений анализа сервисов."), например `request_attribute.book_orders_count`. Атрибуты запросов доступны под [`request_attribute.__attribute_name__`](/docs/semantic-dictionary/fields#request-attributes "Познакомьтесь со списком глобальных полей, имеющих определённое семантическое значение в Dynatrace и доступных для различных типов мониторинга.").

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **System events** > **Pipelines**.
2. Выберите существующий пайплайн или создайте новый. Для создания нового пайплайна выберите  **Pipeline** и введите имя — например, `TeamA Span metrics from Services`.
3. Для настройки извлечения метрик перейдите в **Metric extraction** >  **Processor** > **Sampling aware counter metric** и определите процессор, указав:

   * Описательное имя — например, `Number of books successfully sold per service`
   * Условие совпадения:

     ```
     endpoint.name == "POST /book/{id}/checkout" and isNotNull(request_attribute.book_orders_count) and request.is_failed != true
     ```
   * Для типа измерения выберите **Custom**, так как мы не измеряем длительность.
   * Имя поля, из которого извлекается значение (`request_attribute.book_orders_count`).
   * Параметры выборки включены (оставьте как есть), чтобы извлечение метрик учитывало выборку.
   * Ключ новой метрики — например, `span.books.sold.count`.
   * Измерения метрики. Можно использовать предварительно выбранные измерения, так как `dt.entity.service` выбран по умолчанию.
4. Выберите **Save**.

Вы успешно создали новый процессор для извлечения метрики, содержащей информацию о количестве успешно проданных книг, и, поскольку метрика содержит сервис `dt.entity.service` в качестве измерения, вы сможете разделять метрику по сервисам.

### Топ вызовов базы данных по сервисам и группам запросов

В этом примере мы описываем создание пайплайна и процессора извлечения метрик. Для подробных шагов следуйте подходу [примера с разделением рабочей нагрузки по Pod Kubernetes](#workload-requests-pod), но адаптируйте запросы фильтрации и маршрутизацию.

Для этой примерной метрики мы хотим узнать основные операции или команды базы данных, выполняемые нашими сервисами. Например, имя команды MongoDB, ключевое слово SQL, имя команды Redis, вместе с именем целевой базы данных (`db.namespace`).

Мы не создаём метрику для фактического `db.query.text` (например, `SELECT * FROM user_table`), так как это привело бы к метрике с очень высокой кардинальностью.

Чтобы увидеть список фактических запросов, выполняемых вашими сервисами, используйте [анализ производительности запросов к базе данных в приложении Services](/docs/observe/application-observability/services/services-app#database-query-performance-analysis "Обеспечьте централизованный контроль над здоровьем, производительностью и ресурсами сервисов с помощью приложения Services.").

1. Добавьте новый атрибут группы запросов к спанам базы данных

Мы добавим новый атрибут к спанам базы данных, содержащий интересующую нас группу запросов для метрики: `db.operation.name + db.namespace`. Затем мы сможем использовать вновь созданный атрибут на этапе извлечения метрик.

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Spans** > **Pipelines**.
2. Выберите существующий пайплайн или создайте новый. Для создания нового пайплайна выберите  **Pipeline** и введите имя — например, `TeamA Span metrics from Services`.
3. Чтобы добавить новый атрибут к входящим спанам базы данных, перейдите в **Processing** > **+ Processor** > **DQL** и определите процессор, указав:

   * Описательное имя — например, `Construct low cardinality db.query.group`
   * Условие совпадения:

     ```
     isNotNull(db.operation.name) and isNotNull(db.namespace)
     ```
   * Определение DQL-процессора:

     ```
     fieldsAdd db.query.group = concat(db.operation.name, " ", db.namespace)
     ```

Заключение

Вы добавили новый атрибут `db.query.group` к спанам базы данных, который теперь можно использовать для создания метрики.

**До**

```
{



"db.namespace": "books",



"db.operation.name": "SELECT",



"db.query.text": "select b1_0.id,b1_0.author,b1_0.title from books b1_0 where b1_0.title=?"



}
```

**После**

```
{



"db.query.group": "SELECT books",



"db.namespace": "books",



"db.operation.name": "SELECT",



"db.query.text": "select b1_0.id,b1_0.author,b1_0.title from books b1_0 where b1_0.title=?"



}
```

2. Используйте новый атрибут при извлечении метрик

1. Перейдите в **Metric extraction** >  **Processor** > **Sampling aware counter metric** и определите процессор, указав:

   * Описательное имя — например, `Database calls per service and query group`
   * Условие совпадения:

     ```
     isNotNull(db.query.group)
     ```
   * Имя поля, из которого извлекается значение (`request_attribute.book_orders_count`).
   * Параметры выборки включены (оставьте как есть), чтобы извлечение метрик учитывало выборку.
   * Ключ новой метрики — например, `span.service.db_calls_by_group.count`.
   * Измерения метрики. Выберите **Custom** и укажите `db.query.group` в качестве **Field name on record**. Для измерения сервиса `dt.entity.service` выбран по умолчанию.
2. Выберите **Save**.

Вы успешно создали новый процессор для извлечения метрики, содержащей информацию о вызовах базы данных по сервисам и группам запросов.

3. Запросите топ-10 значений

В ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** или ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** используйте [интерфейс Explore для метрик](/docs/analyze-explore-automate/dashboards-and-notebooks/explore-data#explore-metrics "Исследуйте данные с помощью нашего интерфейса point-and-click.") для построения графика `span.service.db_calls_by_group.count`:

* Разделение по `db.query.group` и `dt.entity.service`
* Сортировка по метрике `value.A` в порядке `DESC`
* Используйте [**Limit**](/docs/analyze-explore-automate/dashboards-and-notebooks/explore-data#metric-limit "Исследуйте данные с помощью нашего интерфейса point-and-click.") `10` для отображения топ-10 результатов

![Explore metrics - Топ-10 запросов](https://dt-cdn.net/images/screenshot-2025-12-23-at-18-23-49-2414-9876a1a980.png)

### Время CPU на эндпоинт сервиса

В этом примере мы описываем создание пайплайна и процессора извлечения метрик. Для подробных шагов следуйте подходу [примера с разделением рабочей нагрузки по Pod Kubernetes](#workload-requests-pod), но адаптируйте запросы фильтрации и маршрутизацию.

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Spans** > **Pipelines**.
2. Выберите существующий пайплайн или создайте новый. Для создания нового пайплайна выберите  **Pipeline** и введите имя — например, `TeamA Span metrics from Services`.
3. Для настройки извлечения метрики значения перейдите в **Metric extraction** >  **Processor** > **Sampling aware value metric** и определите процессор, указав:

   * Описательное имя — например, `CPU time per service endpoint`
   * Условие совпадения:

     ```
     request.is_root_span == true
     ```

     Это условие гарантирует, что мы будем захватывать первый спан запроса внутри сервиса. То есть спан, в котором оцениваются правила обнаружения эндпоинтов.
   * Для типа измерения выберите **Custom**, так как мы не измеряем длительность.
   * Имя поля, из которого извлекается значение (`span.timing.cpu`). Этот атрибут отслеживает общее время CPU, затраченное на выполнение спана, включая время CPU дочерних спанов, работающих в том же потоке на том же стеке вызовов.
   * Параметры выборки включены (оставьте как есть), чтобы извлечение метрик учитывало выборку.
   * Ключ новой метрики — например, `span.request.cpu_time`.
   * Измерения метрики:

     1. Выберите **Pre-defined** и выберите `endpoint.name` из [предопределённых измерений](/docs/semantic-dictionary/model/dt-system-events#audit-event "Познакомьтесь с моделями Semantic Dictionary, связанными с системными событиями."). Другие измерения также предварительно выбраны, например `dt.entity.service`.
     2. Выберите **Save**.

Вы успешно создали новый процессор для извлечения метрики, содержащей информацию о времени CPU, затраченном на каждый эндпоинт. Поле CPU-time измеряется в наносекундах.

### Время отклика для исходящих вызовов к paypal.com по сервисам, измеренное вызывающей стороной

Предстоящие возможности

Поддержка извлечения метрик гистограмм появится в ближайшее время.

Позднее в 2026 году Dynatrace предоставит готовые метрики для сторонних вызовов в рамках модернизации [Мониторинга сторонних сервисов](/docs/observe/application-observability/services/service-detection/service-detection-v1/monitor-3rd-party-services "Настройте, как Dynatrace должен отслеживать сторонние сервисы.").

В этом примере мы описываем создание пайплайна и процессора извлечения метрик. Для подробных шагов следуйте подходу [примера с разделением рабочей нагрузки по Pod Kubernetes](#workload-requests-pod), но адаптируйте запросы фильтрации и маршрутизацию.

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Spans** > **Pipelines**.
2. Выберите существующий пайплайн или создайте новый. Для создания нового пайплайна выберите  **Pipeline** и введите имя — например, `TeamA Span metrics from Services`.
3. Для настройки извлечения метрики гистограммы перейдите в **Metric extraction** >  **Processor** > **Sampling aware histogram metric** и определите процессор, указав:

   * Описательное имя — например, `Response time for outbound calls to paypal.com per service, as measured by the caller`.
   * Условие совпадения:

     ```
     span.kind == "client" and matchesValue(server.address, "*.paypal.com")
     ```
   * **Measurement** установлен на **Duration**.
   * Ключ новой метрики — например, `span.outbound_paypal_requests.response_time`.
   * Измерения метрики — можно использовать предварительно выбранные измерения, так как `dt.entity.service` выбран по умолчанию.
4. Выберите **Save**.

Вы успешно создали новый процессор для извлечения метрики, содержащей время отклика для исходящих вызовов к paypal.com, измеренное вызывающей стороной. Также, поскольку метрика содержит вызывающий сервис (`dt.entity.service`) в качестве измерения, вы сможете разделять метрику по сервисам.
