---
title: Обзор (DPS для гибридной модели)
source: https://docs.dynatrace.com/managed/manage/account-management/license-subscription/subscription-overview-dps-hybrid
---

# Обзор (DPS для гибридной модели)

# Обзор (DPS для гибридной модели)

* Пояснение
* 3 минуты чтения
* Опубликовано 24 нояб. 2025 г.
* Предварительная версия

Эта страница предназначена именно для клиентов с настройкой DPS для гибридной модели, см. [DPS для гибридной модели](/managed/license/dps-for-hybrid "DPS for Hybrid lets you share one subscription across multiple accounts.").

Если лицензия DPS не используется совместно с другими аккаунтами, описание раздела **Обзор** приведено в [Подписка (DPS)](/managed/manage/account-management/license-subscription/subscription-overview-dps "View your Dynatrace Platform Subscription (DPS) budget summary and cost analysis.").

Доступ к обзору подписки

При создании новой настройки DPS для гибридной модели по умолчанию все администраторы всех связанных аккаунтов получают доступ к разделу **Subscription overview** для соответствующей подписки DPS.
Это означает, что доступ есть у пользователей с правами «View account» (`account-viewer`) или «View and manage account and billing information» (`account-company-info`) хотя бы на одном из аккаунтов Dynatrace, потребляющих ресурсы подписки DPS.

Если администраторы определённого аккаунта не должны иметь доступ к разделу **Subscription overview**, для настройки прав доступа нужно обратиться в Dynatrace.

Раздел обзора подписки в Account Management предоставляет ключевую аналитику по подписке DPS для гибридной модели.
В нём можно увидеть общую информацию о лицензии, а также детализацию на уровне аккаунта.

Чтобы просмотреть эту информацию, нужно перейти в **Account Management** > **Subscription** > **Subscription Overview**.

## Уровень лицензии

При первом открытии страницы **Subscription** > **Subscription Overview** отображается информация о лицензии DPS.

* **Dynatrace Platform Subscription**: общая информация о лицензии DPS.
* **Cost distribution - Accounts**: суммарная стоимость на текущий момент по всем аккаунтам в рамках настройки DPS для гибридной модели, с разбивкой на уровне аккаунта.
* **Cost Trend**: динамика изменения затрат каждого аккаунта во времени.

Чтобы увидеть потребление по всем аккаунтам, привязанным к лицензии, нужно убедиться, что в выпадающем меню в правом верхнем углу выбрано значение **All accounts**.
Для детализации и просмотра затрат на уровне аккаунта нужно открыть выпадающее меню и выбрать соответствующее имя аккаунта.

![Subscription overview for DPS for Hybrid license view in Account Management](https://dt-cdn.net/images/account-management-hybrid-subscription-overview-5760-3bc4d3f40f.png)

Обзор подписки для представления лицензии DPS для гибридной модели в Account Management

### Панель Dynatrace Platform Subscription

Панель **Dynatrace Platform Subscription** даёт обзор лицензии DPS, к которой привязаны все аккаунты.
Сюда входят:

* Годовая сумма обязательства.
* Годовой период обязательства.
* Оставшиеся дни.
  Отсчитываются от текущего дня до последнего полного дня годового периода обязательства (включительно).

Дополнительная информация о лицензиях доступна при выборе:

* **History**, для просмотра всех лицензий, связанных с аккаунтами, включая активные и истёкшие лицензии.
* **Pricing**, для просмотра сведений о ценах на единицы возможностей (capability unit).

### Cost distribution - Accounts

Панель **Cost distribution - Accounts** показывает вклад каждого отдельного аккаунта в общее потребление лицензии.

* Круговая диаграмма слева показывает, какую долю в общих затратах на текущий момент внёс каждый аккаунт.
* Столбчатые диаграммы справа показывают затраты каждого аккаунта как долю от общего обязательства по лицензии.

### Cost Trend

Панель **Cost Trend** показывает динамику изменения затрат каждого аккаунта во времени.
Аккаунты отображаются друг над другом (stacked), поэтому также видно суммарное потребление по всем аккаунтам.

## Уровень аккаунта

Чтобы просмотреть потребление лицензии на уровне аккаунта, нужно выбрать выпадающее меню в правом верхнем углу.
(По умолчанию там указано **All accounts**.)
При выборе меню оно разворачивается, и отображается список всех аккаунтов, связанных с лицензией DPS.
Нужно выбрать аккаунт, который требуется просмотреть.

Представление на уровне аккаунта предоставляет следующую информацию:

* **Dynatrace Platform Subscription**: как и в представлении на уровне лицензии, здесь приводится общая информация о лицензии DPS.
* **Cost distribution**: суммарная стоимость на текущий момент для аккаунта.
* **Cost Forecast**: динамика изменения затрат аккаунта во времени, включая прогноз будущих затрат.
* **Events**: все применимые прогнозные события, связанные с аккаунтом.

![Account overview for DPS for Hybrid subscription license view in Account Management](https://dt-cdn.net/images/account-management-hybrid-account-overview-5760-ac81f83d69.png)

Обзор аккаунта для представления лицензии подписки DPS для гибридной модели в Account Management

### Панель Dynatrace Platform Subscription

Панель **Dynatrace Platform Subscription** даёт обзор лицензии DPS, к которой привязан данный аккаунт.
Это та же информация, что показана в обзоре подписки, см. [Панель Dynatrace Platform Subscription](#subscription-overview-dps-pane).

### Cost distribution

Панель **Cost distribution** даёт представление о потреблении аккаунтом различных возможностей тарифного справочника (rate-card) Dynatrace.

Нужно выбрать **View details**, чтобы увидеть страницу **Cost and usage details**, см. [Cost and usage](/managed/manage/account-management/license-subscription/subscription-overview-dps#dps-cost-and-usage "View your Dynatrace Platform Subscription (DPS) budget summary and cost analysis.").

### Cost Forecast

Панель **Cost Forecast** показывает накопленные затраты нарастающим итогом.
Данные отображаются с начала периода подписки и включают прогноз затрат до конца периода.
При наведении на график отображаются фактические и прогнозные затраты.

Account Management использует продвинутые модели прогнозирования для предсказания будущих затрат.
Такие прогнозы доступны только для аккаунтов, по которым накоплено 15 или более дней данных о затратах.

Прогнозные данные носят исключительно оценочный характер.
Они не гарантируют будущих затрат.

### Events

Панель **Events** показывает прогнозируемый рост потребления по требованию (on-demand), в процентах и в стоимости, который ожидается к концу годового периода обязательства.
Если прогнозируется, что потребление превысит годовое обязательство, панель показывает конкретную дату, на которую прогнозируемое потребление превышает годовое обязательство.

## Связанные темы

* [Подписка (DPS) или лицензия (классическая лицензия)](/managed/manage/account-management/license-subscription "View your Dynatrace license information, including budgets, cost analysis, and historical usage, for all license models.")
* [Лицензия Dynatrace](/managed/license "Dynatrace Platform Subscription, capability rate cards, hybrid licensing, and previous license models.")
* [Цены Dynatrace﻿](https://www.dynatrace.com/pricing/)