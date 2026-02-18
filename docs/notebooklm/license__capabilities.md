# Документация Dynatrace: license/capabilities
Язык: Русский (RU)
Сгенерировано: 2026-02-18
Файлов в разделе: 2
---

## license/capabilities/log-analytics/dps-log-query.md

---
title: Calculate your consumption of Log Management & Analytics - Query (DPS)
source: https://www.dynatrace.com/docs/license/capabilities/log-analytics/dps-log-query
scraped: 2026-02-06T16:21:01.498046
---

# Рассчитайте потребление Log Management & Analytics — Query (DPS)

# Рассчитайте потребление Log Management & Analytics — Query (DPS)

* Последняя версия Dynatrace
* Объяснение
* 6-минутное чтение
* Обновлено 4 ноября 2025 г.

Журнал — обзор функции запроса

На этой странице описывается, как используется и выставляется счет за возможность управления журналами и аналитикой — Query DPS.
Обзор этой возможности, включая ее основные функции, см. в разделе [Аналитика журналов (DPS)](/docs/license/capabilities/log-analytics "Learn how Dynatrace Log Analytics consumption is calculated using the Dynatrace Platform Subscription model.").

Использование ![Распределенная трассировка](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Распределенной трассировки** и ![Услуги](https://dt-cdn.net/hub/logos/services.png "Services") **Сервисов** включено в состав Dynatrace.
Эти приложения не производят никакого потребления.

## Как рассчитывается потребление: сканируется ГиБ

Запрошенные данные — это объем данных, считанных во время выполнения запроса DQL.
Он рассчитывается на каждый отсканированный гибибайт (отсканированный ГиБ).

Примените следующий расчет, чтобы определить потребление для измерения использования данных по запросу:

`consumption = (number of GiB of uncompressed data read during query execution) Ã (GiB scanned price as per your rate card)`

Потребление запросов основано на ГиБ данных, сканированных для возврата результата.
Наивысшая потенциальная стоимость запроса равна объему журналов в диапазоне поиска запроса, умноженному на цену в вашем прейскуранте.

Grail применяет различные оптимизации для улучшения времени отклика и снижения затрат.
В некоторых случаях эти оптимизации позволяют выявить части данных, которые не имеют отношения к результату запроса — цена за сканирование этих данных снижается на 98 %.

Влияние оптимизации сканирования Grail зависит от атрибутов данных и запросов.
Он может развиваться по мере того, как Dynatrace продолжает совершенствовать интеллект запросов Grail.

## Отслеживайте свое потребление

В этом разделе описаны различные инструменты Dynatrace, которые можно использовать для отслеживания потребления и затрат.

### Отслеживайте свое потребление с помощью показателей

Dynatrace предоставляет встроенную метрику использования, которая поможет вам понять и проанализировать использование вашей организацией Log Management & Analytics — Query.
Чтобы использовать эту метрику, в обозревателе данных введите `DPS` в поле **Поиск**.

Управление журналами и аналитика — запрос
: Ключ: `builtin:billing.log.query.usage`

Размерность: байт

Разрешение: 1 час

Описание: количество байтов, прочитанных во время выполнения запроса DQL, включая выборочные данные.

Пример использования метрики: отслеживание общего количества байтов, сканируемых с ежечасными интервалами.

Вы можете отслеживать общее количество сканированных байт для [Запрос](#query) с часовыми интервалами для любого выбранного периода времени, используя метрику `builtin:billing.log.query.usage`.

В приведенном ниже примере показано использование, агрегированное за 1-часовые интервалы между 04.09.2023 и 11.09.2023 (за последние 7 дней).

![Управление журналами и аналитика — запрос](https://dt-cdn.net/images/image034-806-25e7da895d.png)

### Отслеживайте свое потребление с помощью запросов DQL

Пример использования метрики: отслеживание общего количества просканированных гибибайтов.

Следующий запрос DQL предоставляет обзор общего использования [Запрос](#query) в отсканированных гибибайтах:

```
fetch dt.system.events



| filter event.kind == "BILLING_USAGE_EVENT"



| filter event.type == "Log Management & Analytics - Query"



| dedup event.id



| summarize {



data_read_bytes = sum(billed_bytes)



}, by: {



startHour = bin(timestamp, 1d)



}
```

В приведенном ниже примере показано ежедневное использование запросов, визуализированное в виде линейной диаграммы за последние 30 дней:

![Сохранение с включенными запросами (LMA)](https://dt-cdn.net/images/image-5-screenshot-2024-10-17-at-15-19-09-1243-832a39ebb6.png)

### Отслеживайте свое потребление и расходы в Управлении учетной записью

Вы также можете просмотреть показатели использования в разделе «Управление учетной записью».
Перейдите в раздел [**Управление аккаунтом**ï»¿](https://myaccount.dynatrace.com/) > **Подписка** > **Обзор** > **Сведения о стоимости и использовании** > **Сводка использования** и выберите возможность **Управление журналами и аналитика — Запрос**.

### Отслеживайте потребление и расходы через API

Вы можете запросить метрики через [API среды — API метрик v2](/docs/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.").

## Похожие темы

* [Аналитика журналов (DPS)](/docs/license/capabilities/log-analytics "Learn how Dynatrace Log Analytics consumption is calculated using the Dynatrace Platform Subscription model.")
* [Что такое Dynatrace Grail?](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more.")
* [Язык запросов Dynatrace](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Лицензия Dynatrace](/docs/license "About Dynatrace Platform Subscription (DPS), модель лицензирования для всех возможностей Dynatrace.")
* [Цены на Dynatrace»¿](https://www.dynatrace.com/pricing/)

---

## license/capabilities.md

---
title: Understanding DPS capabilities
source: https://www.dynatrace.com/docs/license/capabilities
scraped: 2026-02-16T21:15:19.175670
---

# Understanding DPS capabilities

# Understanding DPS capabilities

* Latest Dynatrace
* Explanation
* 1-min read
* Updated on Jan 20, 2026

A Dynatrace Platform Subscription (DPS) agreement is typically signed for 1â3 years, with a minimum annual commitment.
Each platform capability has a price point defined in the rate card that's included with your agreement.

Your organization's usage of each Dynatrace capability accrues costs towards your annual commitment as defined in the rate card.
**Account Management** provides daily updates about accrued usage and related costs.
You can access these details anytime via [Account Management](/docs/manage/account-management "Manage your Dynatrace license, subscriptions, and platform adoption and environment health.") or the [Dynatrace Platform Subscription API](/docs/dynatrace-api/account-management-api/dynatrace-platform-subscription-api "Query the data about your Dynatrace Platform Subscription via the Account Management API.").

Once your annual commitment is reached, you can continue to use Dynatrace while incurring on-demand usage.
Dynatrace applies the same rate card for on-demand usage without additional fees or premium pricing.
You receive monthly invoices for on-demand costs until the next annual commitment period begins.

Your [DPS Billing report](/docs/license/billing-reports "View your billing to see details about accrued costs per booking date. Use this view to determine which Dynatrace monitoring costs were recognized and booked on which day.") is available in the Dynatrace web UI at **Subscription** > **Billing report**.
Your billing report provides details about accrued costs per booking date.

[### Application & Infrastructure Observability

Full-Stack Monitoring, Infrastructure Monitoring, Foundation & Discovery, Mainframe Monitoring](/docs/license/capabilities/app-infra-observability "Learn about the different Application & Infrastructure Observability options that are available with a Dynatrace Platform Subscription (DPS) license.")[### Container Observability

Kubernetes Platform Monitoring, Code Monitoring](/docs/license/capabilities/container-monitoring "Learn about the different container monitoring modes that are available with a Dynatrace Platform Subscription (DPS) license.")[### Application Security

Runtime Application Protection (RAP), Runtime Vulnerability Analytics (RVA), Security Posture Management (SPM)](/docs/license/capabilities/application-security "Learn how Dynatrace Application Security monitoring consumption is calculated using the Dynatrace Platform Subscription model.")[### Digital Experience Monitoring

Real User Monitoring (RUM), Real User Monitoring Property, Real User Monitoring with Session Replay, Browser Monitor or Clickpath, HTTP Monitor, Third-Party Synthetic API Integration](/docs/license/capabilities/digital-experience-monitoring "Learn how Dynatrace Digital Experience Monitoring (DEM) consumption is calculated using the Dynatrace Platform Subscription model.")[### Log Analytics

Ingest & Process, Retain, Query](/docs/license/capabilities/log-analytics "Learn how Dynatrace Log Analytics consumption is calculated using the Dynatrace Platform Subscription model.")[### Traces powered by Grail

Ingest & Process, Retain, Query](/docs/license/capabilities/traces "Learn how Dynatrace Traces powered by Grail consumption is calculated using the Dynatrace Platform Subscription (DPS) model.")[### Events powered by Grail

Ingest & Process, Retain, Query](/docs/license/capabilities/events "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.")[### Metrics powered by Grail

Ingest & Process, Retain, Query](/docs/license/capabilities/metrics "Learn how Dynatrace Metrics powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.")[### Automation

Automation](/docs/license/capabilities/automation "Learn how Dynatrace Automation Workflow consumption is calculated using the Dynatrace Platform Subscription model.")[### AppEngine Functions

AppEngine Functions](/docs/license/capabilities/appengine-functions "Learn how AppEngine Function consumption is calculated using the Dynatrace Platform Subscription model.")[### Platform extensions

Custom Metrics Classic, Log Monitoring Classic, Custom Traces Classic, Custom Events Classic, Serverless Functions Classic](/docs/license/capabilities/platform-extensions "Learn how consumption of Dynatrace platform extensions is calculated using the Dynatrace Platform Subscription model.")

---
