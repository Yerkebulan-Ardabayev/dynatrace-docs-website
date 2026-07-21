---
title: Обзор (подписка на платформу Dynatrace)
source: https://docs.dynatrace.com/managed/manage/account-management/license-subscription/subscription-overview-dps
---

# Обзор (подписка на платформу Dynatrace)

# Обзор (подписка на платформу Dynatrace)

* Пояснение
* 3 мин чтения
* Опубликовано 24 нояб. 2025 г.

Раздел **Overview** в Account Management предоставляет три ключевых анализа подписки DPS.

* Budget summary: сводка по общим затратам за период подписки и прогноз, с разбивкой по environment'ам.
* Cost and usage breakdown: подробная разбивка затрат и потребления за последние 30 дней.
* Cost and usage analysis: детализированное представление с гибкими фильтрами для просмотра и сравнения затрат и потребления.

Эта информация доступна в **Account Management** > **Subscription** > **Overview**.

Все данные о бюджете и затратах также доступны через [Dynatrace Platform Subscription API](/managed/dynatrace-api/account-management-api/dynatrace-platform-subscription-api "Query the data about your Dynatrace Platform Subscription via the Account Management API.").

Если вместо этого отображается **Account Management** > **License**, обратитесь к [документации по классической лицензии Dynatrace](/managed/manage/account-management/license-subscription/license-overview-classic "View your Dynatrace classic licensing usage and details.").

## Budget summary

Раздел **Budget summary** отображает сведения о годовых затратах и прогнозе, с разбивкой затрат по environment'ам.

![Экран Account Management Budget Summary для моделей лицензирования Dynatrace Platform Subscription.](https://dt-cdn.net/images/account-management-dps-budget-summary-1826-6227bdd871.png)

Экран Account Management Budget Summary для моделей лицензирования Dynatrace Platform Subscription.

* Общая информация о подписке включает:

  + **Annual commitment period**: текущий период подписки.
    (При многолетней подписке отображается только текущий период подписки.)
  + **Annual commitment amount**: обязательный бюджет на текущий период подписки, в валюте, указанной в соглашении о подписке.
  + **Days remaining**: сколько дней осталось до конца текущего периода подписки.
* Кольцевая диаграмма **Total used budget** показывает срез процента от годовой обязательной суммы, который уже израсходован, а также фактическую сумму и накопленное потребление.
  При наведении на диаграмму отображается точная разбивка по каждому environment'у.
  (Обрати внимание: на диаграмме перечислены только первые четыре environment'а, все остальные сгруппированы в **Other**).
* Линейная диаграмма **Budget forecast** показывает накопленные фактические затраты.
  Данные отображаются с начала периода подписки и включают прогноз затрат до конца периода.
  При наведении на диаграмму отображаются фактические и прогнозные затраты.

  Account Management использует продвинутые модели прогнозирования для предсказания будущих затрат.
  Такие прогнозы доступны только для аккаунтов с данными о затратах за 15 и более дней.

  Прогнозные данные являются лишь оценкой.
  Они не гарантируют будущие затраты.
* **Forecast events**: прогнозируемый рост потребления on-demand (в процентах и в затратах), который, по прогнозу, будет достигнут к концу периода годового обязательства.
  Если прогнозируется, что потребление превысит годовое обязательство, панель показывает конкретную дату, на которую прогнозируемое потребление превышает годовое обязательство.
* **Environment**: сведения о затратах для каждого environment'а.

  + **Annual budget-to-date cost**: накопленные затраты для данного environment'а, измеренные с начала периода обязательства.
  + **Last 0–30 days cost** и **Last 0–30 days change**: накопленные затраты и процентное изменение по environment'у за последние 30 дней.
    Поскольку потребление environment'а может колебаться в течение периода обязательства, эти столбцы помогают определить environment'ы, которые в данный момент несут наибольшие затраты.
* Чтобы посмотреть разбивку затрат для environment'а по capability, выбери **Actions** > **View details**.

## Cost and usage

Панель **Cost and usage** предоставляет подробный анализ затрат и потребления, связанных с подпиской, за последние 30 дней.
Для просмотра этой информации выбери либо **Cost summary** (для затрат), либо **Usage summary** (для потребления).

### Cost summary

Вкладка **Cost Summary** отображает затраты, понесённые за предыдущие 30 дней, по всем environment'ам и capability.

![Экран Account Management Cost Summary для моделей лицензирования Dynatrace Platform Subscription.](https://dt-cdn.net/images/account-management-dps-cost-summary-1818-cdf2edb006.png)

Экран Account Management Cost Summary для моделей лицензирования Dynatrace Platform Subscription.

Столбчатая диаграмма вверху показывает затраты, связанные с environment'ом, во времени.

* Наведи курсор на значение на диаграмме, чтобы увидеть разбивку затрат по environment'ам.
* Выбери название environment'а, чтобы показать/скрыть его на диаграмме.
* Чтобы отфильтровать данные о затратах по конкретным environment'ам или capability, используй фильтры **All environments** и **All capabilities**, отображаемые над диаграммой.
  (Обрати внимание: по отдельности отображаются только первые четыре environment'а, ранжированные по затратам от наибольших к наименьшим.
  Все остальные environment'ы сгруппированы в **Other**.)

Табличные данные под диаграммой показывают разбивку затрат на уровне capability.

* **Annual budget-to-date cost**, это накопленные затраты для данного environment'а, измеренные с начала периода обязательства.
* **Last 0–30 days cost** и **Last 0–30 days change** показывают накопленные затраты и процентное изменение по environment'у за предыдущие 30 дней.
  Поскольку потребление environment'а может колебаться в течение периода обязательства, эти столбцы помогают определить environment'ы, которые в данный момент несут наибольшие затраты.
* Чтобы посмотреть разбивку затрат для capability, выбери **Actions** > **View details**.

### Usage summary

Вкладка **Usage summary** отображает диаграмму, показывающую потребление, понесённое отдельными capability, за предыдущие 30 дней.

![Экран Account Management Usage Summary для моделей лицензирования Dynatrace Platform Subscription.](https://dt-cdn.net/images/account-management-dps-usage-summary-1822-4917e05426.png)

Экран Account Management Usage Summary для моделей лицензирования Dynatrace Platform Subscription.

* Общее потребление для каждой capability отображается в единице измерения этой capability.
* Используй фильтр над диаграммой, чтобы посмотреть потребление для разных environment'ов и capability.

## Capability cost and usage analysis

Страница **Capability cost and usage analysis** позволяет просматривать затраты и потребление подписки рядом друг с другом и предоставляет дополнительные фильтры по временному диапазону.

![Экран Account Management Capability Cost and Usage для моделей лицензирования Dynatrace Platform Subscription.](https://dt-cdn.net/images/account-management-dps-capability-cost-and-usage-2-1843-ab841d53ae.png)

Экран Account Management Capability Cost and Usage для моделей лицензирования Dynatrace Platform Subscription.

* Диаграмма **Environment cost** отображает ежедневные затраты в валютной единице, настроенной для подписки.
  Диаграмма **Environment usage** отображает ежедневное потребление в единице измерения этой capability.
* Используй фильтр, чтобы изменить временной диапазон.
  По умолчанию диаграмма отображает данные за предыдущие 30 дней.
* Таблица отображает общие затраты и общее потребление на основе выбранных фильтров.

## Environment cost and usage analysis

Страница **Environment cost and usage analysis** позволяет просматривать затраты и потребление по capability для конкретного environment'а.

![Экран Account Management Environment Cost and Usage для моделей лицензирования Dynatrace Platform Subscription.](https://dt-cdn.net/images/account-management-dps-environment-cost-and-usage-1852-042963b02d.png)

Экран Account Management Environment Cost and Usage для моделей лицензирования Dynatrace Platform Subscription.

Чтобы посмотреть анализ затрат и потребления environment'а для любого environment'а, выбери **Actions** > **View details**.
Эта страница является вариантом страницы **Capability cost and usage analysis**, отображающей накопленные затраты и потребление по capability.

Выбери capability из фильтра над диаграммой, чтобы посмотреть потребление за выбранный временной диапазон.

## Похожие темы

* [Subscription (DPS) or License (classic license)](/managed/manage/account-management/license-subscription "View your Dynatrace license information, including budgets, cost analysis, and historical usage, for all license models.")
* [License Dynatrace](/managed/license "Dynatrace Platform Subscription, capability rate cards, hybrid licensing, and previous license models.")
* [Dynatrace pricing﻿](https://www.dynatrace.com/pricing/)