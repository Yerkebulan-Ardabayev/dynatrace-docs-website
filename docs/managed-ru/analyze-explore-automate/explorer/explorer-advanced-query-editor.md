---
title: Редактор запросов в Advanced mode Data Explorer
source: https://docs.dynatrace.com/managed/analyze-explore-automate/explorer/explorer-advanced-query-editor
scraped: 2026-05-12T11:13:08.239485
---

# Редактор запросов в Advanced mode Data Explorer

# Редактор запросов в Advanced mode Data Explorer

* Чтение: 10 мин
* Обновлено 31 октября 2025 г.

Чтобы в полной мере использовать возможности запросов [Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Получение информации о метриках через Metrics v2 API.") в веб-интерфейсе Dynatrace, используйте Data Explorer в **Advanced mode**.

В **Advanced mode** можно:

* Проверять и редактировать запрос, созданный через веб-интерфейс Dynatrace (с отключённым **Advanced mode**).
* Использовать [селекторы метрик](/managed/dynatrace-api/environment-api/metric-v2/metric-selector "Настройка селектора метрик для Metric v2 API.") для применения трансформаций, недоступных иначе. Например, сдвиги по времени.
* Использовать [выражения метрик](/managed/dynatrace-api/environment-api/metric-v2/metric-expressions "Применяйте арифметические операции в запросе точек данных через Metrics API v2.") для создания простых арифметических операций с несколькими различными значениями метрик. Например, `metric A` + `metric B`.
* Работать с [селекторами объектов](/managed/dynatrace-api/environment-api/entity-v2/entity-selector "Настройка селектора объектов для конечных точек Environment API.") для применения более сложных фильтров к метрикам. Например, для фильтрации метрики узла Kubernetes по определённому кластеру Kubernetes.

## Включение Advanced mode

Можно начать с простого запроса через веб-интерфейс, а затем включить **Advanced mode**, чтобы увидеть базовый запрос.

Например, если начать с такого запроса при отключённом **Advanced mode**:

![Data Explorer: Advanced mode: выключен](https://dt-cdn.net/images/advanced-mode-off-1275-ba8224556d.png)

Data Explorer: Advanced mode: выключен

при включении **Advanced mode** вы увидите следующее:

![Data Explorer: Advanced mode: включён](https://dt-cdn.net/images/advanced-mode-on-1274-8db9a65b58.png)

Data Explorer: Advanced mode: включён

Базовый код запроса отображается в том виде, в котором он передаётся в Metrics API v2:

`builtin:host.cpu.usage:splitBy("dt.entity.host"):avg:auto:sort(value(avg,descending)):limit(20)`

## Отключение Advanced mode

Для простых запросов, использующих одну из следующих трансформаций, можно снова отключить Advanced mode:

* **Split by** — измерения метрики (если не добавлены дополнительные измерения через селектор объектов в Advanced mode)
* **Filter** — соединённые через условие ИЛИ
* **Sort**
* **Limit**

Подробное описание отдельных трансформаций см. в разделе [metric selector](/managed/dynatrace-api/environment-api/metric-v2/metric-selector "Настройка селектора метрик для Metric v2 API.").

Отключение Advanced mode возможно только если трансформации, отредактированные в Advanced mode, были добавлены при выключенном Advanced mode.

Например, если изначально применена трансформация сортировки при выключенном Advanced mode, можно изменить порядок сортировки с `ascending` на `descending` при включённом Advanced mode, а затем снова выключить его. Однако после добавления новых частей запроса — например, трансформаций, таких как сдвиг по времени или выражения метрик, недоступных при выключенном Advanced mode — отключить Advanced mode уже нельзя.

## Редактирование запроса

Основные функции редактора запросов одинаковы независимо от состояния **Advanced mode**:

* Чтобы добавить метрику, нажмите **Add metric**, чтобы добавить строку (ещё одну метрику) в запрос.
* Чтобы скопировать метрику, нажмите **More** (**…**) > **Duplicate** в строке.
* Чтобы удалить метрику, нажмите **More** (**…**) > **Delete** в строке.
* Чтобы изменить порядок метрик, выберите метрику и перетащите её на новую позицию. Запустите запрос повторно, чтобы увидеть изменения.

  ![Перетащите метрику для изменения порядка](https://dt-cdn.net/images/data-explorer-drag-metric-69-84144c5cd2.png)

  Перетащите метрику для изменения порядка

  Порядок метрик влияет на следующее:

  + Порядок отображения элементов: метрики запроса отображаются сверху вниз, поэтому последняя располагается поверх остальных
  + Порядок столбцов в табличной визуализации
  + Порядок отображения параметров в панели **Settings**
* Чтобы попробовать запрос, нажмите **Run query**. Текст рядом с кнопкой показывает статус последнего выполнения.

Основное различие — в способе редактирования запроса и количестве доступных возможностей:

* При выключенном **Advanced mode** веб-интерфейс упрощает построение запроса через меню, но возможности запроса ограничены
* При включённом **Advanced mode** возможности запроса значительно больше, но требуется знание синтаксиса

### Добавление метрики

Самый удобный способ выбора метрик — начать с выключенным **Advanced mode**.

1. Установите курсор в строке и начните вводить имя метрики. Появится список совпадений.  
   Например, введите `cpu usage` и выберите `builtin:host.cpu.usage` из списка.

   ![Data Explorer: выбор метрики: ввод и выбор](https://dt-cdn.net/images/metric-selector-metric-type-471-10a8a83a2e.png)

   Data Explorer: выбор метрики: ввод и выбор
2. Можно выбрать часто используемые агрегации, измерения и трансформации:

   * Split by: выберите одно из перечисленных измерений для выбранной метрики
   * Aggregate: выберите `Average`, `Count`, `Maximum`, `Minimum`, `Sum`, `Median`, `Percentile 10th`, `Percentile 75th` или `Percentile 90th`.

   Выбранная агрегация применяется после **Split by**. Например, если выбрать `Percentile 10th` и разделить по `Host` для метрики-измерителя `builtin:host.cpu.idle`, процентиль вычисляется по значениям после разделения по хосту.

   * Sort by: выберите по возрастанию или убыванию
   * Filter by: выберите измерения и атрибуты фильтра
   * Limit: выберите значение ограничения
3. Включите **Advanced mode**.
4. Отредактируйте результаты по необходимости.

   * Копируйте и вставляйте из одной строки в другую
   * Добавляйте, копируйте и удаляйте строки по необходимости

Чтобы добавить метрику в **Advanced mode**

1. Установите курсор в строке и начните вводить ключ метрики. Появится список совпадений.  
   Например, введите `host.cpu` и выберите `builtin:host.cpu.usage` из списка.

   ![Data Explorer: Advanced mode: выбор метрики](https://dt-cdn.net/images/data-explorer-tab-code-metric-select-1240-1f16bbf6d6.png)

   Data Explorer: Advanced mode: выбор метрики
2. Все трансформации нужно добавлять вручную.

### Редактирование метрики

В поле редактирования:

* Введите двоеточие (`:`), чтобы увидеть список доступных добавлений в точке вставки, и выберите из списка.
* Нажмите **Shift-Enter** для принудительного перехода на новую строку. Полезно для читаемости и не влияет на выполнение запроса.
* Выберите метрику или число и нажмите **(** на клавиатуре, чтобы обернуть выделение в скобки.

Подробнее о метриках

* Обзор метрик см. в разделе [Метрики](/managed/analyze-explore-automate/metrics-classic "Узнайте о классических метриках в Dynatrace.").
* Список встроенных метрик см. в разделе [Встроенные метрики](/managed/analyze-explore-automate/metrics-classic/built-in-metrics "Изучите полный список встроенных метрик Dynatrace.").
* Информацию о приёме пользовательских метрик см. в разделе [Расширение наблюдаемости метрик](/managed/ingest-from/extend-dynatrace/extend-metrics "Узнайте, как расширить наблюдаемость метрик в Dynatrace.").
* Используйте [браузер метрик](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Просматривайте метрики с помощью браузера метрик Dynatrace.") для:

  + Проверки подробностей метрики
  + Открытия выбранной метрики в Data Explorer

### Операнды

Операнд — это метрика или число.

* Каждый операнд должен быть заключён в скобки `()`. Можно также использовать скобки для задания приоритета.
* Все метрики с более чем одной точкой данных, участвующие в выражении метрики, должны иметь одинаковое разрешение.
* Любую метрику можно использовать как операнд, включая метрики, изменённые любой [цепочкой трансформаций](/managed/dynatrace-api/environment-api/metric-v2/metric-selector "Настройка селектора метрик для Metric v2 API."), а также применять трансформации к результату выражения.

Полные подробности о написании запросов метрик см.:

* [Metrics API — Metric selector](/managed/dynatrace-api/environment-api/metric-v2/metric-selector "Настройка селектора метрик для Metric v2 API.")
* [Metrics API — Metric expressions](/managed/dynatrace-api/environment-api/metric-v2/metric-expressions "Применяйте арифметические операции в запросе точек данных через Metrics API v2.")
* [Metrics API — Примеры и варианты использования](/managed/dynatrace-api/environment-api/metric-v2/examples "Узнайте, как использовать Dynatrace API на реальных примерах.")

### Выражения

Выражения метрик позволяют применять простые арифметические операции над операндами (метриками или числами).

Например, это выражение вычисляет отношение двух метрик в процентах:  
`((metric1)/(metric2))*(100)`

Основные компоненты для работы:

* Операнд: метрика или число
* Скобки: `()`
* Арифметические операторы: `+`, `-`, `*`, `/`
* Отрицание: `-()`

Арифметические операции используют точки данных кортежей (уникальных комбинаций метрика–измерение–значение измерения) метрик. Идентичные кортежи каждой метрики сопоставляются, затем их точки данных выравниваются. Подробности см. в разделе [Metrics API — Metric expressions](/managed/dynatrace-api/environment-api/metric-v2/metric-expressions#tuples "Применяйте арифметические операции в запросе точек данных через Metrics API v2.").

## Пример: дельта

Узнайте, как:

* Собрать метрику в Advanced mode
* Использовать дельту

В этом примере показано, как преобразовать метрику-измеритель в метрику дельты подсчёта.

1. При включённом **Advanced mode** собираем следующую метрику-измеритель:  
   `builtin:cloud.kubernetes.pod.containerRestarts:splitBy()`  
   путём последовательного выбора параметров из редактора:

   **Select metric:** введите часть ключа метрики, пока не появится нужная.

   ![Data Explorer: пример: Delta: 1](https://dt-cdn.net/images/data-explorer-example-delta-01-1237-d51b884316.png)

   Data Explorer: пример: Delta: 1

   **Select splitBy:** введите двоеточие (`:`) и часть строки поиска для `splitBy`, затем выберите из списка.

   ![Data Explorer: пример: Delta: 2](https://dt-cdn.net/images/data-explorer-example-delta-02-1233-aea8238deb.png)

   Data Explorer: пример: Delta: 2

   **Промежуточное состояние:**

   ![Data Explorer: пример: Delta: 3](https://dt-cdn.net/images/data-explorer-example-delta-03-1232-67882fdf0f.png)

   Data Explorer: пример: Delta: 3

   `builtin:cloud.kubernetes.pod.containerRestarts:splitBy()`
2. Решаем отобразить её как метрику дельты подсчёта.

   **Select avg:** введите двоеточие (`:`) и часть строки поиска для `avg`, затем выберите из списка.

   ![Data Explorer: пример: Delta: 4](https://dt-cdn.net/images/data-explorer-example-delta-04-1233-9cdcedc998.png)

   Data Explorer: пример: Delta: 4

   **Select delta:** введите двоеточие (`:`) и часть строки поиска для `delta`, затем выберите из списка.

   ![Data Explorer: пример: Delta: 5](https://dt-cdn.net/images/data-explorer-example-delta-05-1232-4edc6c1618.png)

   Data Explorer: пример: Delta: 5

   **Финальное состояние:**

   ![Data Explorer: пример: Delta: 6](https://dt-cdn.net/images/data-explorer-example-delta-06-1231-72baaf1ed3.png)

   Data Explorer: пример: Delta: 6

   `builtin:cloud.kubernetes.pod.containerRestarts:splitBy():avg:delta`
3. Выполните запрос.

## Пример: вычисление показателя ошибок

Узнайте, как:

* Объединить две строки в одну с помощью выражения метрики
* Выполнить простое вычисление

В этом примере нужно отобразить показатель ошибок для страницы конверсии. Начнём с этих метрик:

* Action count (`builtin:apps.web.action.count.load.browser`)
* Error count (`builtin:apps.web.action.countOfErrors`)

Но простые счётчики не дают полной картины. На основе счётчиков действий и ошибок хотим вычислить третью метрику — показатель ошибок страницы конверсии. Запрос для третьей метрики разделит счётчик ошибок на счётчик действий с фильтрацией по имени страницы.

Этот запрос можно создать почти без ввода текста.

1. При выключенном **Advanced mode** выберите метрики, агрегации и фильтры.

   ![Пример: вычисление показателя ошибок: Advanced mode выключен](https://dt-cdn.net/images/example-error-rate-adv-mode-off-1274-90a4675f30.png)

   Пример: вычисление показателя ошибок: Advanced mode выключен
2. При включённом **Advanced mode** просмотрите код запроса.

   ![Пример: вычисление показателя ошибок: Advanced mode включён: метрики отдельно](https://dt-cdn.net/images/example-error-rate-adv-mode-on-1273-c3e3141f83.png)

   Пример: вычисление показателя ошибок: Advanced mode включён: метрики отдельно
3. Скопируйте и вставьте содержимое поля редактирования **B** в поле **A**, объединив два запроса с добавлением скобок и знака деления, затем удалите **B**.

   Если **A** — первый операнд:

   ```
   builtin:apps.web.action.countOfErrors:filter(and(or(in("dt.entity.application_method",entitySelector("type(application_method),entityName.equals(~"loading of page /easytravel/home~")"))))):splitBy():sum:auto:sort(value(sum,descending)):limit(20)
   ```

   а **B** — второй операнд:

   ```
   builtin:apps.web.action.count.load.browser:filter(and(or(in("dt.entity.application_method",entitySelector("type(application_method),entityName.equals(~"loading of page /easytravel/home~")"))))):splitBy():sum:auto:sort(value(sum,descending)):limit(20)
   ```

   хотим разделить `(A)/(B)`:

   ```
   ((builtin:apps.web.action.countOfErrors:filter(and(or(in("dt.entity.application_method",entitySelector("type(application_method),entityName.equals(~"loading of page /easytravel/home~")"))))):splitBy():sum:auto:sort(value(sum,descending)):limit(20))



   /



   (builtin:apps.web.action.count.load.browser:filter(and(or(in("dt.entity.application_method",entitySelector("type(application_method),entityName.equals(~"loading of page /easytravel/home~")"))))):splitBy():sum:auto:sort(value(sum,descending)):limit(20))
   ```
4. Результат должен выглядеть примерно так:

   ![Пример: вычисление показателя ошибок: Advanced mode включён: метрики объединены для вычисления](https://dt-cdn.net/images/example-error-rate-adv-mode-on-combined-1274-6cd39af452.png)

   Пример: вычисление показателя ошибок: Advanced mode включён: метрики объединены для вычисления
5. Выполните запрос.

Теперь можно добавить пороговые значения и закрепить запрос на дашборде.

## Пример: сравнение метрики с предыдущим временным диапазоном

Узнайте, как добавить контекст к визуализациям, например линейным графикам, чтобы ответить на вопрос: «Что считается нормальным?»

При просмотре данных на дашбордах линии или отдельные значения сами по себе часто малоинформативны, особенно для новых пользователей, которым может не хватать опыта для быстрой оценки пиков или конкретных значений. Добавление контекста может существенно улучшить интерпретацию данных.

В этом примере изучим, как дублировать метрику и применить трансформацию `:timeshift` для добавления контекста к линейным графикам.
Начнём с `builtin:apps.web.largestContentfulPaint.load.browser` — встроенной метрики [Core Web Vitals](https://web.dev/vitals/#core-web-vitals), которая показывает измерения наибольшей отрисовки контента для всех действий загрузки всех веб-приложений.

Этот запрос можно создать почти без ввода текста.

1. При выключенном **Advanced mode** выберите метрику, разбивки, агрегации и фильтры.
2. Скопируйте метрику, нажав **More** (**…**) > **Duplicate** для этой строки.
3. Включите **Advanced mode**, чтобы просмотреть код запроса.
4. Добавьте **timeshift(-1w)** в конец второго запроса (B).
5. Выполните запрос.

Финальный код запроса для A и B должен выглядеть примерно так (в зависимости от выборов на шаге 1):

**A** без сдвига по времени:

```
builtin:apps.web.largestContentfulPaint.load.browser:splitBy():percentile(75):auto:sort(value(percentile(75),descending)):limit(10)
```

**B** с применённым сдвигом по времени:

```
builtin:apps.web.largestContentfulPaint.load.browser:timeshift(-1w):splitBy():percentile(75):auto:sort(value(percentile(75),descending)):limit(10)
```

## Пример: фильтры связей

Узнайте, как использовать [селектор объектов](/managed/dynatrace-api/environment-api/entity-v2/entity-selector "Настройка селектора объектов для конечных точек Environment API.") и связи для фильтрации метрики по значениям связанного объекта.

В этом примере:

* Начинаем с метрики `builtin:cloud.kubernetes.node.cores`
* Применяем фильтр `in` для узлов Kubernetes типа `dt.entity.kubernetes_node`
* Используем селектор объектов для поиска всех узлов Kubernetes, работающих в заданном кластере Kubernetes

Разберём компоненты селектора объектов:

* `type(KUBERNETES_NODE)` определяет тип искомого объекта.
* `toRelationships.IS_KUBERNETES_CLUSTER_OF_NODE(` определяет связь между узлом (левая часть) и кластером (правая часть). Мы ищем все узлы Kubernetes в заданном кластере: «из объекта, определённого выше (узел Kubernetes), ищем все кластеры Kubernetes этого узла».
* `type(KUBERNETES_CLUSTER),entityId(KUBERNETES_CLUSTER-A943C5CF0A41A684))")))` определяет правую часть связи как кластер Kubernetes с заданным идентификатором объекта.

Финальный запрос выглядит следующим образом:

```
(builtin:cloud.kubernetes.node.cores:avg)



:filter(in("dt.entity.kubernetes_node",



entitySelector("type(KUBERNETES_NODE),toRelationships.IS_KUBERNETES_CLUSTER_OF_NODE(type(KUBERNETES_CLUSTER),entityId(KUBERNETES_CLUSTER-A943C5CF0A41A684))")))
```

## Пример: явная гистограмма

Узнайте, как анализировать метрику с явной гистограммой в Data Explorer с помощью трансформации `histogram` и извлекать из неё `percentiles`.

В этом примере:

* Начинаем с метрики `_cws.otlp.metrics.generic.histogram1.histogram`. Обратите внимание на суффикс `.histogram`.
* Применяем фильтр равенства для кластера Kubernetes по `dt.kubernetes.cluster.id`.
* Используем трансформацию `histogram` для отображения вёдер гистограммы как измерений.

Финальный запрос выглядит следующим образом:

```
_cws.otlp.metrics.generic.histogram1.histogram:filter(eq("dt.kubernetes.cluster.id", "KUBERNETES_CLUSTER-1")):histogram
```

![Трансформация histogram в Data Explorer](https://dt-cdn.net/images/histogram-transformation-1513-2c45d6a28d.png)

Трансформация histogram в Data Explorer

Значение измерения `le` обозначает верхнюю границу (меньше или равно) каждого ведра. В этом примере верхняя граница ведра `55` равна `5`.

Ограничения

* Хранится не более 12 вёдер на точку данных гистограммы.
* Отрицательные границы вёдер не поддерживаются.

### Процентили

Для извлечения процентиля из метрики гистограммы используйте трансформацию `percentile`. Например, медиану можно извлечь с помощью `percentile(50)`.

Финальный запрос выглядит следующим образом:

```
_cws.otlp.metrics.generic.histogram1.histogram:filter(eq("dt.kubernetes.cluster.id", "KUBERNETES_CLUSTER-1")):percentile(50)
```

![Трансформация percentile в Data Explorer](https://dt-cdn.net/images/histogram-percentile-1514-33827a5e8f.png)

Трансформация percentile в Data Explorer