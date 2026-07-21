---
title: Понимание и измерение потребления для Third-Party Synthetic API Integration (DPS)
source: https://docs.dynatrace.com/managed/license/capabilities/real-user-synthetic-monitoring/third-party-api
---

# Понимание и измерение потребления для Third-Party Synthetic API Integration (DPS)

# Понимание и измерение потребления для Third-Party Synthetic API Integration (DPS)

* Пояснение
* Чтение 5 мин
* Обновлено 11 мая 2026 г.

Third-Party Synthetic API Integration позволяет загружать результаты synthetic-тестов от внешних провайдеров мониторинга в Dynatrace.
Это централизует данные о доступности и производительности из нескольких synthetic-инструментов, объединяет алертинг и позволяет анализировать результаты внешних synthetic-тестов наряду со всеми остальными данными observability в Dynatrace.

На этой странице объясняется, как рассчитывается и учитывается потребление, что помогает прогнозировать, отслеживать и контролировать использование.

## Как рассчитывается потребление

Потребление измеряется в **third-party synthetic results** с использованием позиции прайс-листа **Third-Party Synthetic API Integration**.
Каждый раз, когда результат внешнего тестового запуска отправляется в Dynatrace через API, Dynatrace засчитывает один third-party synthetic result.

### Ключевые термины

Third-party synthetic result
:   Third-party synthetic result, это результат одного выполнения теста, отправленный в Dynatrace внешним synthetic-вендором.
    Показатель основан на общем количестве результатов, загруженных через [Third-Party Synthetic API](/managed/dynatrace-api/environment-api/synthetic/third-party-synthetic "Push third-party synthetic data to Dynatrace via API."), и считается один раз за каждый загруженный результат, независимо от конфигурации, успеха/неудачи, локации или частоты.

### Правила подсчёта и исключения

* Каждый загруженный результат считается за одну единицу, независимо от того:

  + какой вендор произвёл результат;
  + какого типа был тест;
  + завершился тест успехом или неудачей;
  + как часто или где выполнялся тест.
* Если тестовый запуск никогда не отправляет данные в Dynatrace, этот запуск не учитывается в потреблении.
* Примеры результатов включают:

  + проверки uptime;
  + выполнения тестов API;
  + результаты multi-step synthetic-тестов;
  + периодические проверки доступности от внешних инструментов.

## Оценка стоимости

Можно оценить месячную стоимость, рассчитав общее количество загруженных third-party synthetic results и умножив это значение на прайс-лист $0.001 за один third-party synthetic result.

### Формула потребления

```
(# of results sent per test)



× (# of executions per hour)



× (# of tests)



× (# of hours)



= Total consumed results
```

### Пример

У клиента есть:

* 20 внешних synthetic-тестов.
* Каждый тест выполняется каждые пять минут (12 раз в час).
* Каждый запуск отправляет один результат.
* Тесты выполняются в течение 30 дней.

Расчёт:

```
1 result per test



x 12 executions per hour



x 20 tests



x 24 hours



x 30 days



= 172,800 synthetic results
```

Умножив на удельную стоимость $0.001 за результат, общая стоимость synthetic-тестов за этот месяц в примере составляет **$172.80**.

## Отслеживание потребления

Dynatrace предоставляет различные возможности, помогающие понять и проанализировать потребление возможностей DPS вашей организацией.

### Данные через Account Management

Лицензионные менеджеры могут просматривать использование и затраты в Account Management.
Перейти в [**Account Management**﻿](https://myaccount.dynatrace.com/) > **Subscription** > **Overview** > **Cost and usage details** > **Usage summary** и выбрать возможность **Third-Party Synthetic API Ingestion**.

Подробнее см. в [Overview (Dynatrace Platform Subscription)](/managed/manage/account-management/license-subscription/subscription-overview-dps "View your Dynatrace Platform Subscription (DPS) budget summary and cost analysis.").

![Diagram - Example usage for Real User Monitoring visible in Account Management](https://dt-cdn.net/images/rum-usage-overview-account-management-2910-7a5d37e705.png)

Диаграмма, пример использования для Real User Monitoring, отображаемый в Account Management

### Данные через billing usage events

Billing usage events (BUE, `billing_usage_event`), это системные события, которые Dynatrace отправляет в пространство данных `dt.system.events`.
Можно использовать DQL для запроса BUE и анализа использования и стоимости для возможностей Real User Monitoring без повторного применения правил биллинга или логики подсчёта сессий.

BUE представляют уже рассчитанное, оплачиваемое использование для возможностей DPS (а не какую-либо конфигурацию или потенциальное использование) и согласованы с тем, что отображается в Account Management и в счетах.
Поэтому они являются рекомендуемым источником данных для понимания соответствующего потребления.

Billing usage events содержат:

* какая возможность DPS была потреблена;
* объём использования, учитываемый при биллинге;
* временное окно, к которому относится использование;
* контекст сущности, к которой относится использование (например, приложение).

#### Запрос billing usage events через DQL

Billing usage events можно использовать как авторитетный источник при построении представлений распределения затрат, анализа использования или прозрачности затрат.

Например, агрегировать по приложению, чтобы понять, какие приложения вносят наибольший вклад в использование и затраты.

Ниже приведены примеры запросов DQL для различных сценариев использования.
Эти запросы можно использовать как есть или изменить под свои нужды.

1. Общее использование во времени

   ```
   fetch dt.system.events



   | filter event.kind == "BILLING_USAGE_EVENT" and event.type == "Third-Party Synthetic API Integration"



   | dedup event.id



   | summarize totalUsage = sum(billed_sessions), by:{bin(timestamp, 1d)}
   ```

### Данные через API

Можно запрашивать данные через [Environment API – Grail Query﻿](https://developer.dynatrace.com/develop/platform-services/services/grail-service/#grail-query-api).
Примеры запросов DQL приведены в [Query billing usage events with DQL](#rum-dql-query).

## Часто задаваемые вопросы

Учитываются ли в потреблении неудачные результаты third-party тестов?

Да.
Каждый загруженный результат учитывается один раз, независимо от того, завершился он успехом или неудачей.

Взимает ли Dynatrace плату за каждый шаг в multi-step внешнем тесте?

Нет.
Dynatrace взимает плату только за загрузку результатов выполнения теста.
Поэтому не имеет значения, сколько шагов выполнил внешний вендор для получения результата.

Что если third-party тест выполняется, но не отправляет результат в Dynatrace?

В потреблении учитываются только загруженные результаты.
Пропущенные или неотправленные запуски не влияют на использование.

Можно ли контролировать, сколько результатов вендор отправляет в Dynatrace?

Многие внешние вендоры позволяют настраивать частоту тестов или условную отправку отчётов.
Эти настройки напрямую влияют на потребление.

## Похожие темы

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.")
* [Лицензия Dynatrace](/managed/license "Dynatrace Platform Subscription, capability rate cards, hybrid licensing, and previous license models.")
* [Обзор Real User и Synthetic Monitoring (DPS)](/managed/license/capabilities/real-user-synthetic-monitoring "Learn how Dynatrace Real User and Synthetic Monitoring consumption is calculated using the Dynatrace Platform Subscription model.")
* [Цены Dynatrace﻿](https://www.dynatrace.com/pricing/)