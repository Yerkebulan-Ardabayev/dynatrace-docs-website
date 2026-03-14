---
title: Метрики самомониторинга
source: https://www.dynatrace.com/docs/analyze-explore-automate/metrics-classic/self-monitoring-metrics
scraped: 2026-03-05T21:37:18.643612
---

# Метрики самомониторинга


* Classic
* Чтение: 4 мин
* Опубликовано 03 дек. 2021

Dynatrace предлагает специальную категорию метрик самомониторинга для обеспечения наблюдаемости за работой и состоянием компонентов и функций Dynatrace. Эти метрики доступны в каждой среде Dynatrace Managed и SaaS и могут быть идентифицированы по префиксу `dsfm:`.

Чтобы просмотреть текущие метрики самомониторинга:

1. Перейдите в **Metrics**.
2. Отфильтруйте таблицу по `dsfm:`.
3. Раскройте любую строку для просмотра деталей метрики.

Приведённые ниже примеры показывают, как вы можете использовать эти метрики самомониторинга для получения информации о работе и состоянии вашего Dynatrace ActiveGate и среды Dynatrace с течением времени.

## Информация о среде

В этом примере мы используем метрики самомониторинга для получения информации о работе и состоянии среды Dynatrace с течением времени.

1. Перейдите в **Data Explorer**.
2. Проверьте перечисленные ниже метрики.

Для просмотра данных самомониторинга используйте следующие метрики:

* `dsfm:cluster.oneagent.agent_modules` (количество отслеживаемых хостов)
  Пример запроса в Data Explorer:

  ```
  dsfm:cluster.oneagent.agent_modules:filter(and(eq("dt.oneagent.agent_type",os))):merge("dt.entity.apm_tenant","dt.tenant.uuid"):avg:splitBy():sum:auto:sort(value(max,descending)):limit(10)
  ```
* `dsfm:cluster.oneagent.agent_modules` (количество отслеживаемых модулей кода)
  Пример запроса в Data Explorer:

  ```
  dsfm:cluster.oneagent.agent_modules:filter(not(or(eq("dt.oneagent.agent_type",os),eq("dt.oneagent.agent_type",log_analytics),eq("dt.oneagent.agent_type",remote_plugin)))):merge("dt.entity.apm_tenant","dt.tenant.uuid"):avg:splitBy():sum:auto:limit(10)
  ```
* `dsfm:server.service_calls.received` (количество полученных вызовов сервисов)
  Пример запроса в Data Explorer:

  ```
  dsfm:server.service_calls.received:default(0):splitBy():sum:rate(1m)
  ```
* `dsfm:server.spans.received` (количество полученных спанов)
  Пример запроса в Data Explorer:

  ```
  dsfm:server.spans.received:default(0):splitBy():sum:rate(1m)
  ```
* `dsfm:server.rum.user_session_count` (количество пользовательских сессий)
  Пример запроса в Data Explorer:

  ```
  dsfm:server.rum.user_session_count:default(0):splitBy():sum:rate(1m)
  ```
* `dsfm:server.rum.action_count` (количество действий пользователей)
  Пример запроса в Data Explorer:

  ```
  dsfm:server.rum.action_count:default(0):splitBy():sum:rate(1m)
  ```

### Пример дашборда с информацией о среде

Вы можете создать дашборд Dynatrace для быстрого и целенаправленного доступа к данным самомониторинга. Создайте плитки, выбрав метрики самомониторинга в Data Explorer, настроив визуализацию для каждой из них и закрепив их на ваших дашбордах. Подробнее см. в разделе [Dashboards Classic](../../../analyze-explore-automate/dashboards-classic.md "Узнайте, как создавать, управлять и использовать Dynatrace Dashboards Classic.").

На следующем снимке экрана показан дашборд, использующий приведённые выше метрики для мониторинга работы среды Dynatrace с течением времени.

* Стабильное количество отслеживаемых хостов и модулей, полученных вызовов сервисов, а также пользовательских сессий/действий в минуту вместе указывают на здоровую среду Dynatrace.
* Значительное падение этих метрик может указывать на проблему; в этом случае следует обратиться к специалисту Dynatrace через онлайн-чат для определения причины.

![Пример страницы дашборда с метриками самомониторинга.](https://dt-cdn.net/images/3dashboard-1107-58988f1958.png)

## Информация о мониторинге логов и событий

В этом примере мы используем метрики самомониторинга для получения информации о работе [Log Monitoring Classic](../../../analyze-explore-automate/log-monitoring.md "Узнайте, как включить Log Monitoring, какие сведения может предоставить Log Monitoring, и многое другое.") с течением времени.

1. Перейдите в **Data Explorer**.
2. Проверьте перечисленные ниже метрики.

Для просмотра данных самомониторинга используйте следующие метрики:

* `dsfm:server.log_and_events_monitoring.events_rejected_count` (количество отклонённых событий журнала из-за лимита приёма)
  Эту метрику можно использовать для проверки того, были ли отклонены какие-либо события журнала из-за лимита приёма в минуту за заданный период. Если метрика часто превышает `0`, это может указывать на необходимость увеличения лимитов для данного тенанта.
  Пример запроса в Data Explorer:

  ```
  dsfm:server.log_and_events_monitoring.events_rejected_count:splitBy():sum:auto:sort(value(sum,descending)):rate(1m)
  ```
* `dsfm:server.log_and_events_monitoring.events_incoming_count` (количество входящих событий журнала)
  Эту метрику можно использовать для проверки количества входящих событий журнала на сервере за заданный период. Она может включать дубликаты из-за повторных передач. Эта метрика содержит дополнительные измерения: `event.sender` для идентификации источника входящего события журнала и `event.type` для идентификации типа входящего события журнала.
  Пример запроса в Data Explorer:

  ```
  dsfm:server.log_and_events_monitoring.events_incoming_count:splitBy():sum:auto:sort(value(sum,descending)):rate(1m)
  ```

## Информация об ActiveGate

В этом примере мы используем метрики самомониторинга для получения информации о работе ActiveGate.

1. Перейдите в **Metrics**.
2. Отфильтруйте таблицу по `dsfm:active_gate`.
3. Проверьте метрики использования CPU JVM и памяти кучи ActiveGate, которые являются хорошим первым индикатором состояния и загрузки ActiveGate:

   * **ActiveGate - JVM - CPU Usage**
   * **ActiveGate - JVM - Heap Memory Used**
   * **ActiveGate - JVM - Heap Memory Available**

На следующих снимках экрана показаны использование памяти JVM и использование CPU JVM одного ActiveGate в кластере.

![Пример страницы Data Explorer с метрикой самомониторинга.](https://dt-cdn.net/images/1explorer-f-1565-6576341d6c.png)

Обратите внимание, что использование и доступность памяти с течением времени не указывают на какое-либо аномальное использование, но загрузка CPU показывает интересный пик.

![Пример страницы Data Explorer с графиком метрики самомониторинга.](https://dt-cdn.net/images/2explorer-f-1565-80ae3f684e.png)

Дальнейшее расследование показывает, что этот пик был вызван увеличением числа OneAgent, отправляющих данные через этот ActiveGate, что стало результатом выполнения теста в данном кластере.
