---
title: Понимание и измерение потребления для HTTP Monitor (DPS)
source: https://docs.dynatrace.com/managed/license/capabilities/real-user-synthetic-monitoring/http-monitor
---

# Понимание и измерение потребления для HTTP Monitor (DPS)

# Понимание и измерение потребления для HTTP Monitor (DPS)

* Пояснение
* 5 мин на чтение
* Обновлено 11 мая 2026 г.

С помощью HTTP Monitor можно проверять доступность, производительность и корректность работы сайтов и API эндпоинтов.

На этой странице объясняется, как рассчитывается потребление и как можно оценивать, управлять и оптимизировать использование в Dynatrace.

## Как рассчитывается потребление

Потребление HTTP Monitor измеряется в **synthetic requests** с использованием элемента тарифной карты **HTTP Monitor**.
Один synthetic request расходуется при каждом запуске монитора для каждого выполненного HTTP(S)-запроса, в каждой локации.

### Ключевые термины

Synthetic request
:   Synthetic request, это единичный HTTP(S)-запрос, выполненный HTTP Monitor.
    Каждый запрос учитывается как один synthetic request.

    Это не зависит от HTTP-метода, от того, происходит ли запрос из публичной или приватной локации, а также от того, используются ли аутентификация, сертификаты, пользовательские заголовки или скрипты.

### Правила подсчёта и исключения

* Synthetic request расходуется, как только запрос выполнен.
* Если запрос HTTP Monitor завершается с ошибкой во время выполнения, он всё равно учитывается.
* Запросы учитываются один раз за выполнение в каждой локации.
  Не важно, является ли локация мониторинга публичной или приватной.
* Запросы учитываются независимо от HTTP-метода и от того, используются ли аутентификация, клиентские сертификаты, пользовательские заголовки или скрипты.
* Следующие запросы не учитываются в потреблении HTTP monitor:

  + Запросы, пропущенные из-за скриптов или логики, выполняемых перед запуском.
  + Запросы, которые не были выполнены, потому что предыдущий запрос завершился с ошибкой.
  + Запросы, которые не были выполнены, потому что монитор отключён.

## Оценка стоимости

Оценить ежемесячную стоимость можно, рассчитав общее количество synthetic results и умножив это значение на прайс-лист по цене $0.001 за synthetic result.

### Формула расчёта потребления

```
(# of synthetic requests in the monitor)



× (# of executions per hour)



× (# of locations)



× (# of hours)



= Total consumed results
```

### Пример

У клиента есть:

* 3 HTTP-запроса.
* Они выполняются каждые 10 минут (6 раз в час).
* Каждый запрос выполняется из четырёх локаций.
* Тесты выполняются в течение 30 дней.

Расчёт:

```
3 requests per execution



x  6 executions per hour



x  4 locations



x 24 hours



x 30 days



= 51,840 synthetic requests
```

Умножив на стоимость единицы $0.001 за результат, получаем общую стоимость synthetic-тестов за этот месяц в примере: **$51.84**.

## Отслеживание потребления

В этом разделе описываются различные инструменты Dynatrace, которые можно использовать для отслеживания потребления и затрат.

## Управление потреблением

Dynatrace предоставляет различные варианты, которые помогают понимать и анализировать потребление возможностей DPS в организации.

### Аналитика через Account Management

Менеджеры лицензий могут просматривать использование и затраты в Account Management.
Перейти в [**Account Management**﻿](https://myaccount.dynatrace.com/) > **Subscription** > **Overview** > **Cost and usage details** > **Usage summary** и выбрать возможность **HTTP Monitor**.

Подробнее см. [Overview (Dynatrace Platform Subscription)](/managed/manage/account-management/license-subscription/subscription-overview-dps "View your Dynatrace Platform Subscription (DPS) budget summary and cost analysis.").

![Диаграмма - пример использования для Real User Monitoring, видимый в Account Management](https://dt-cdn.net/images/rum-usage-overview-account-management-2910-7a5d37e705.png)

Диаграмма - пример использования для Real User Monitoring, видимый в Account Management

### Аналитика через billing usage events

Billing usage events (BUEs, `billing_usage_event`), это системные события, отправляемые Dynatrace в пространство данных `dt.system.events`.
С помощью DQL можно запрашивать BUE и анализировать использование и стоимость для возможностей Real User Monitoring без повторного применения правил биллинга или логики подсчёта сессий.

BUE представляют собой уже рассчитанное, подлежащее оплате использование для возможностей DPS (а не какую-либо конфигурацию или потенциальное использование) и соответствуют тому, что отображается в Account Management и в счетах.
Поэтому это рекомендуемый источник данных для понимания соответствующего потребления.

Billing usage events содержат:

* Какая возможность DPS была использована.
* Объём использования, учитываемый при биллинге.
* Временное окно, к которому относится использование.
* Контекст сущности, к которой относится использование (например, приложение).

#### Запрос billing usage events с помощью DQL

Billing usage events можно использовать как авторитетный источник при построении представлений распределения затрат, анализа использования или прозрачности затрат.

Например, агрегировать по приложению, чтобы понять, какие приложения больше всего влияют на использование и затраты.

Ниже приведены примеры запросов DQL для различных сценариев использования.
Эти запросы можно использовать как есть или изменять под свои нужды.

1. Общее использование во времени

   ```
   fetch dt.system.events



   | filter event.kind == "BILLING_USAGE_EVENT" and event.type == "HTTP Monitor"



   | dedup event.id



   | summarize totalUsage = sum(billed_sessions), by:{bin(timestamp, 1d)}
   ```
2. Использование HTTP-сессий по приложению (за последние семь дней)

   ```
   fetch dt.system.events, from: -7d



   | filter event.kind == "BILLING_USAGE_EVENT"



   | filter event.type == "HTTP Monitor"



   | dedup event.id



   | summarize total_sessions = sum(billed_http_request_count), by: {dt.entity.http_check}



   | fieldsAdd app_name = entityName(dt.entity.http_check)



   | sort total_sessions desc



   | limit 20
   ```

### Аналитика через API

Аналитику можно запрашивать через [Environment API – Grail Query﻿](https://developer.dynatrace.com/develop/platform-services/services/grail-service/#grail-query-api).
Примеры запросов DQL приведены в разделе [Запрос billing usage events с помощью DQL](#rum-dql-query).

## Часто задаваемые вопросы

Расходуют ли неудачные запросы synthetic requests?

Да.
Запрос учитывается, как только начинает выполняться.
Пропущенные из-за сбоя запросы не учитываются.

Увеличивают ли пользовательская аутентификация, заголовки или сертификаты потребление?

Нет.
Учитываются только выполненные HTTP-запросы.

Как учитываются редиректы?

Если следование за редиректами включено, каждый редирект, это дополнительный synthetic request.
Если отключено, учитывается только исходный запрос.

Расходуют ли запросы ручные (on-demand) выполнения?

Да.
Ручные выполнения расходуют synthetic requests так же, как и запланированные.

## Похожие темы

* [Обзор Real User и Synthetic Monitoring (DPS)](/managed/license/capabilities/real-user-synthetic-monitoring "Learn how Dynatrace Real User and Synthetic Monitoring consumption is calculated using the Dynatrace Platform Subscription model.")
* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.")
* [Лицензирование Dynatrace](/managed/license "Dynatrace Platform Subscription, capability rate cards, hybrid licensing, and previous license models.")
* [Цены Dynatrace﻿](https://www.dynatrace.com/pricing/)