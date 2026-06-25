---
title: Метрики самомониторинга
source: https://docs.dynatrace.com/managed/analyze-explore-automate/metrics-classic/self-monitoring-metrics
scraped: 2026-05-12T11:06:50.936314
---

# Метрики самомониторинга

# Метрики самомониторинга

* Чтение: 4 мин
* Опубликовано 3 декабря 2021 г.

Dynatrace предлагает специальную категорию метрик самомониторинга, обеспечивающую наблюдаемость за работой и состоянием компонентов и функций Dynatrace. Эти метрики доступны в каждом окружении Dynatrace Managed и SaaS и определяются по префиксу метрик `dsfm:`.

Чтобы просмотреть реализованные на данный момент метрики самомониторинга

1. Перейдите в **Metrics**.
2. Отфильтруйте таблицу по `dsfm:`.
3. Разверните любую строку, чтобы просмотреть сведения о метрике.

Приведённые ниже примеры показывают, как использовать эти метрики самомониторинга для анализа работы и состояния вашего Dynatrace ActiveGate и окружения Dynatrace во времени.

## Аналитика окружения

В этом примере мы используем метрики самомониторинга для анализа работы и состояния окружения Dynatrace во времени.

1. Перейдите в **Data Explorer**.
2. Проверьте перечисленные ниже метрики.

Для просмотра данных самомониторинга используйте следующие метрики:

* `dsfm:cluster.oneagent.agent_modules` (число отслеживаемых хостов)  
  Пример запроса Data Explorer:

  ```
  dsfm:cluster.oneagent.agent_modules:filter(and(eq("dt.oneagent.agent_type",os))):merge("dt.entity.apm_tenant","dt.tenant.uuid"):avg:splitBy():sum:auto:sort(value(max,descending)):limit(10)
  ```
* `dsfm:cluster.oneagent.agent_modules` (число отслеживаемых кодовых модулей)  
  Пример запроса Data Explorer:

  ```
  dsfm:cluster.oneagent.agent_modules:filter(not(or(eq("dt.oneagent.agent_type",os),eq("dt.oneagent.agent_type",log_analytics),eq("dt.oneagent.agent_type",remote_plugin)))):merge("dt.entity.apm_tenant","dt.tenant.uuid"):avg:splitBy():sum:auto:limit(10)
  ```
* `dsfm:server.service_calls.received` (число полученных вызовов сервисов)  
  Пример запроса Data Explorer:

  ```
  dsfm:server.service_calls.received:default(0):splitBy():sum:rate(1m)
  ```
* `dsfm:server.spans.received` (число полученных спанов)  
  Пример запроса Data Explorer:

  ```
  dsfm:server.spans.received:default(0):splitBy():sum:rate(1m)
  ```
* `dsfm:server.rum.user_session_count` (число пользовательских сессий)  
  Пример запроса Data Explorer:

  ```
  dsfm:server.rum.user_session_count:default(0):splitBy():sum:rate(1m)
  ```
* `dsfm:server.rum.action_count` (число действий пользователей)  
  Пример запроса Data Explorer:

  ```
  dsfm:server.rum.action_count:default(0):splitBy():sum:rate(1m)
  ```

### Пример дашборда с аналитикой окружения

Вы можете создать дашборд Dynatrace для быстрого целевого доступа к данным самомониторинга. Создайте плитки, выбрав метрики самомониторинга в Data Explorer, настроив для каждой визуализацию и закрепив их на дашбордах. Подробнее см. в разделе [Дашборды](/managed/analyze-explore-automate/dashboards-classic "Узнайте, как создавать, использовать дашборды Dynatrace Dashboards Classic и управлять ими.").

На следующем снимке экрана показан дашборд, который использует приведённые выше метрики для мониторинга работы окружения Dynatrace во времени.

* Стабильное число отслеживаемых хостов и модулей, полученных вызовов сервисов и пользовательских сессий/действий в минуту в совокупности указывает на исправное окружение Dynatrace.
* Значительное падение этих метрик может указывать на проблему. В этом случае обратитесь к эксперту по продукту Dynatrace через онлайн-чат, чтобы определить первопричину.

![Example of dashboard page with self-monitoring metrics.](https://dt-cdn.net/images/3dashboard-1107-58988f1958.png)

Пример страницы дашборда с метриками самомониторинга.

## Аналитика мониторинга логов и событий

В этом примере мы используем метрики самомониторинга для анализа работы [мониторинга логов](/managed/analyze-explore-automate/log-monitoring "Узнайте, как включить мониторинг логов, какую аналитику он предоставляет, и многое другое.") во времени.

1. Перейдите в **Data Explorer**.
2. Проверьте перечисленные ниже метрики.

Для просмотра данных самомониторинга используйте следующие метрики:

* `dsfm:server.log_and_events_monitoring.events_rejected_count` (число событий логов, отклонённых из-за лимита приёма)  
  Эта метрика позволяет проверить, были ли отклонены события логов из-за лимита приёма в минуту за заданный период. Если метрика часто превышает `0`, это может означать, что для данного тенанта стоит увеличить лимиты.  
  Пример запроса Data Explorer:

  ```
  dsfm:server.log_and_events_monitoring.events_rejected_count:splitBy():sum:auto:sort(value(sum,descending)):rate(1m)
  ```
* `dsfm:server.log_and_events_monitoring.events_incoming_count` (число входящих событий логов)  
  Эта метрика позволяет проверить, сколько событий логов поступает на сервер за заданный период. В неё могут попадать дубликаты из-за повторных передач. Метрика содержит дополнительные измерения: `event.sender` для определения источника входящего события лога и `event.type` для определения типа входящего события лога.  
  Пример запроса Data Explorer:

  ```
  dsfm:server.log_and_events_monitoring.events_incoming_count:splitBy():sum:auto:sort(value(sum,descending)):rate(1m)
  ```

## Аналитика ActiveGate

В этом примере мы используем метрики самомониторинга для анализа работы ActiveGate.

1. Перейдите в **Metrics**.
2. Отфильтруйте таблицу по `dsfm:active_gate`.
3. Проверьте метрики использования CPU и heap-памяти JVM ActiveGate, которые служат хорошим первым индикатором состояния и загрузки ActiveGate:

   * **ActiveGate - JVM - CPU Usage**
   * **ActiveGate - JVM - Heap Memory Used**
   * **ActiveGate - JVM - Heap Memory Available**

На следующих снимках экрана показаны использование памяти JVM и использование CPU JVM одного ActiveGate в кластере.

![Example of Data Explorer page with self-monitoring metric.](https://dt-cdn.net/images/1explorer-f-1565-6576341d6c.png)

Пример страницы Data Explorer с метрикой самомониторинга.

Обратите внимание, что использование и доступность памяти во времени не указывают на аномальную загрузку, однако использование CPU показывает интересный пик.

![Example of Data Explorer page with self-monitoring metric graph.](https://dt-cdn.net/images/2explorer-f-1565-80ae3f684e.png)

Пример страницы Data Explorer с графиком метрики самомониторинга.

Дальнейшее исследование показывает, что этот пик был вызван увеличением числа OneAgent, передающих данные через этот ActiveGate, что стало результатом выполнения теста на этом кластере.