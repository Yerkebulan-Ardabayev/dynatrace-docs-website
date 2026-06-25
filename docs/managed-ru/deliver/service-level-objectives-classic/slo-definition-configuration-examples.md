---
title: Примеры конфигурации определений целей уровня обслуживания
source: https://docs.dynatrace.com/managed/deliver/service-level-objectives-classic/slo-definition-configuration-examples
scraped: 2026-05-12T11:38:27.869025
---

# Example configuration of service-level objective definitions

# Example configuration of service-level objective definitions

* Reference
* 5-min read
* Updated on Sep 14, 2023

Dynatrace предлагает набор готовых SLO для некоторых из основных доменов мониторинга, которые можно настраивать как в мастере SLO, так и в глобальных настройках SLO.  
Для лучшего понимания показателей SLI, необходимых для этих целей уровня обслуживания, изучите приведённые ниже примеры конфигурации.

## Доступность на уровне сервиса

Базовая доступность на уровне сервиса рассчитывается как отношение числа успешных вызовов сервиса (`builtin:service.errors.server.successCount`) к общему числу вызовов (`builtin:service.requestCount.server`).

**Пример**

* Выражение метрики

  ```
  (100)*(builtin:service.errors.server.successCount:splitBy())/(builtin:service.requestCount.server:splitBy())
  ```
* Селектор сущностей

  ```
  type("SERVICE"),entityName("My service")
  ```

## Производительность сервиса

SLO производительности сервиса измеряет процент временных срезов, в течение которых сервис отвечал в пределах «быстрого» порога, где «быстрый» определяется пользовательским условием.

Пример ниже показывает, как определить выражение метрики, которое подсчитывает временные срезы, соответствующие условию «быстрый», и как использовать это выражение для определения SLO в Dynatrace.

**Пример**

* Выражение метрики:

  ```
  ((builtin:service.response.time:avg:partition("latency",value("good",lt(10000))):splitBy():count:default(0))/(builtin:service.response.time:avg:splitBy():count)*(100)):default(100,always)
  ```

  С использованием следующих преобразований выражение метрики возвращает значения со временем ответа ниже заданного порога.

  | Преобразование | Область | Информация |
  | --- | --- | --- |
  | [Aggregation](/managed/dynatrace-api/environment-api/metric-v2/metric-selector#aggregation "Configure the metric selector for the Metric v2 API.") | Агрегирует значения, отличные от `null`, и игнорирует остальные. | В зависимости от варианта использования можно применять несколько агрегаций, например `avg` (для агрегирования значений) и `percentile (90)` (для удаления выбросов). |
  | [Partition](/managed/dynatrace-api/environment-api/metric-v2/metric-selector#partition "Configure the metric selector for the Metric v2 API.") | Разделяет отдельные точки данных метрики на определённое число временных срезов по временному диапазону на основе значения `good` измерения метрики `latency`. | Для повышения точности SLO уменьшите продолжительность временного среза, задав более короткий временной диапазон. |
  | [Partition](/managed/dynatrace-api/environment-api/metric-v2/metric-selector#partition "Configure the metric selector for the Metric v2 API.") | Условие `lt()` изменяет единицу метрики для порогового значения задержки ответа на микросекунды. | Требуемая единица метрики для SLO производительности сервиса — микросекунды. |
  | [Default](/managed/dynatrace-api/environment-api/metric-v2/metric-selector#default "Configure the metric selector for the Metric v2 API.") | Заменяет значения `null` в данных на указанное значение (`0`). |  |

Использование пользовательски вычисляемой метрики в качестве числителя повышает точность SLO производительности. Рекомендуется использовать параметр заглушённых запросов при совместном использовании вычисляемых метрик сервисов со встроенными метриками, так как встроенная метрика применяет его по умолчанию.

## Доступность метода сервиса

Доступность метода сервиса рассчитывается как отношение числа успешных вызовов ключевых запросов (`builtin:service.keyRequest.errors.server.successCount`) к общему числу вызовов ключевых запросов (`builtin:service.keyRequest.count.server`). Использует фильтр SLO `type("SERVICE_METHOD")`.

Пример конфигурации с фильтром для `YOUR_METHOD_OF_INTEREST`

* `<YOUR custom success metrics/filter service, endpoint, availability, and latency>` / `builtin:service.keyRequest.count.server:filter(eq("dt.entity.service\_method","SERVICE\_METHOD-XXX"))`

Этот пример показывает, как определить пользовательскую метрику сервиса, подсчитывающую быстрые вызовы сервиса, и как определить SLO на основе этой метрики в Dynatrace.

1. Перейдите на страницу любого вашего сервиса, изучите его типичную производительность в миллисекундах, затем перейдите на страницу многомерного анализа.

   ![Validation](https://dt-cdn.net/images/example-service-custom-1-1667-5951521a24.png)

   Валидация
2. На странице многомерного анализа выберите **Request count metric** и определите условие для одного из свойств вызова сервиса. В этом примере определяется условие по времени ответа: оно должно быть меньше 1300 миллисекунд, чтобы засчитываться как быстрый вызов для выбранного сервиса.

   ![Multidim analysis](https://dt-cdn.net/images/example-service-custom-2-1667-9b11e40270.png)

   Многомерный анализ
3. После определения условия нажмите **Create metric**. Задайте собственный уникальный идентификатор метрики для использования этой метрики при построении графиков, оповещениях и в SLO.  
   Например, новая метрика `fastcreditcardrequests` получает уникальный ID `calc:service:fastcreditcardrequests`.

   ![Multidim analysis 2](https://dt-cdn.net/images/example-service-custom-3-1663-8b2a76bf1c.png)

   Многомерный анализ 2
4. Можно построить сравнительный график общего числа запросов к сервису и быстрых запросов.

   Проверьте фильтр селектора сущностей на выбранном сервисе (`CreditCardValidation`), иначе будет получено общее количество запросов для всех сервисов.

   Пример селектора сущностей: `type("SERVICE"),entityName("CreditCardValidation")`
5. Результат — итоговый статус SLO, отображаемый в списке SLO.

   ![Perform result](https://dt-cdn.net/images/example-service-8-1618-00d321b833.png)

   Результат производительности

## Пользовательский опыт

Dynatrace предлагает экспертизу в области измерения реального пользовательского опыта при предоставлении сервисов. Метрики Dynatrace, такие как [Apdex (Application Performance Index)](/managed/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance.") или [Оценка пользовательского опыта](/managed/observe/digital-experience/rum-concepts/scores-and-ratings/user-experience-score "User experience score is a metric used to categorize user sessions as Frustrating, Tolerable, or Satisfying."), можно использовать в рамках определения SLO.

Apdex определяет стандарт производительности для разделения пользователей приложения на три группы: **SATISFIED**, **TOLERATING** и **FRUSTRATED**.

Например, в качестве цели SLO для вашего приложения можно указать, что 90% всех пользователей должны находиться в категории **SATISFIED**.

![Mobile app](https://dt-cdn.net/images/mobile-app-1319-9714a225f6.png)

Мобильное приложение

Этот SLO рассчитывается как отношение числа пользователей в категории **SATISFIED** (`builtin:apps.web.actionCount.category:filter(eq(Apdex category,SATISFIED)):splitBy()`) к общему числу пользователей веб- или мобильного приложения (`builtin:apps.web.actionCount.category:splitBy()`).

**Пример**

* Выражение метрики

  ```
  (100)*(builtin:apps.web.actionCount.category:filter(eq("Apdex category",SATISFIED)):splitBy())/(builtin:apps.web.actionCount.category:splitBy())
  ```
* Селектор сущностей

  ```
  type("APPLICATION"),entityName("My application")
  ```

## Доля пользователей мобильного приложения без сбоев

Одной из важнейших метрик для измерения доступности и надёжности вашего мобильного приложения (iOS и Android) является `Crash free user rate` (доля пользователей без сбоев). Используемая встроенная метрика — `builtin:apps.other.crashFreeUsersRate.os`. Эта метрика измеряет процент пользователей, открывающих и использующих мобильное приложение без возникновения сбоев.

**Пример**

* Выражение метрики

  ```
  (builtin:apps.other.crashFreeUsersRate.os:splitBy())
  ```
* Селектор сущностей

  ```
  type("MOBILE_APPLICATION"),entityName("My mobile app")
  ```

## Доступность синтетических мониторов

SLO доступности синтетических мониторов представляет процент времени, в течение которого синтетический тест находился в доступном состоянии, или, в качестве альтернативы, процент успешных тестов от общего числа выполненных.

Для определения цели синтетического монитора на основе времени используется встроенная метрика `builtin:synthetic.browser.availability.location.total`.

Для определения доступности на основе времени, исключающей периоды технического обслуживания, используется встроенная метрика `builtin:synthetic.browser.availability.location.totalWoMaintenanceWindow`.

**Пример**

* Выражение метрики

  ```
  (builtin:synthetic.browser.availability.location.total:splitBy())
  ```
* Селектор сущностей

  ```
  type("SYNTHETIC_TEST"),entityName("My synth test")
  ```

## Дополнительные ресурсы

Для получения дополнительной информации о SLO изучите руководство Dynatrace University [Getting started with SLOs in Dynatrace](https://dt-url.net/3h03row).