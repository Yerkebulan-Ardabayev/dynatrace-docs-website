---
title: Where to view your costs
source: https://docs.dynatrace.com/managed/manage-your-costs/view/where-to-look
---

# Where to view your costs

# Where to view your costs

* Пояснение
* 6 минут на чтение
* Обновлено 26 мая 2026 г.

Dynatrace предоставляет доступ к одним и тем же данным о затратах и использовании через несколько интерфейсов. Выбор зависит от задачи:

* Account Management: главная точка входа для итоговых сумм по подписке, разбивок по функциональности и окружениям, отчётов по биллингу, а также API, которые предоставляют доступ к этим же данным программно.
* DQL: если нужен детальный анализ, DQL используется для запросов к событиям биллинга.

## Обзор

Dynatrace фиксирует каждую запись об измеренном использовании в Grail в виде события биллинга. Account Management представляет эти данные в виде готовых сводок, разбивок и отчётов. Те же данные можно запрашивать напрямую через DQL, а также экспортировать для интеграции с финансовыми системами.

## Сценарии использования

* Проверка текущего потребления по подписке относительно годового обязательства.
* Сравнение затрат по окружениям, функциональности или периодам времени.
* Построение произвольного запроса DQL для вопроса о затратах, на который Account Management не отвечает.

* Выгрузка данных биллинга в Excel, Power BI или другой финансовый инструмент.

## Account Management

Account Management предоставляет почасовую отчётность по использованию DPS, ежедневные обновления текущего бюджета и детализированное представление, позволяющее сравнивать затраты по периодам времени, окружениям и функциональности.

### Обзоры затрат

Обзор потребления по Dynatrace Platform Subscription доступен в **Account Management** > **Subscription**.

![Экран Account Management Budget Summary для моделей лицензирования Dynatrace Platform Subscription.](https://dt-cdn.net/images/account-management-dps-budget-summary-1826-6227bdd871.png)

Экран Account Management Budget Summary для моделей лицензирования Dynatrace Platform Subscription.

* **Budget summary**: сводка общих затрат за период подписки и прогноз с разбивкой по окружениям.
* **Cost and usage breakdown**: детальная разбивка затрат и использования за последние 30 дней, включая потребление по функциональности и по окружениям.
* **Cost and usage analysis**: гибкое детализированное представление, в котором можно сравнивать периоды времени, фильтровать по окружению или функциональности и выявлять драйверы затрат и тренды.

Подробный обзор интерфейса приведён в разделе [Overview (Dynatrace Platform Subscription)](/managed/manage/account-management/license-subscription/subscription-overview-dps "View your Dynatrace Platform Subscription (DPS) budget summary and cost analysis.").

Затраты рассчитываются ежедневно в 02:00:00 UTC на основании доступности локальных (on-premise) кластеров и активного соединения с Dynatrace.
Когда кластеры недоступны, это приводит к позднему поступлению данных об использовании для расчёта затрат и задерживает уведомления о бюджете.
Когда кластер становится доступен и данные об использовании загружаются в Dynatrace, затраты рассчитываются в ходе следующего интервала в 02:00:00 UTC и обрабатываются несколько часов спустя.
Это может повлиять на своевременность уведомлений о бюджете.

### Отчёт по биллингу

Отчёт по биллингу содержит сведения о начисленных затратах по дате учёта (booking date).
Это представление позволяет определить, какие затраты на мониторинг Dynatrace были признаны и учтены в тот или иной день.

Отчёты по биллингу доступны в **Account Management** > **Subscription** > **Billing report**.

Подробнее см. в разделе [Billing report](/managed/manage-your-costs/view/billing-report "View your billing to see details about accrued costs per booking date. Use this view to determine which Dynatrace monitoring costs were recognized and booked on which day.").

### API для интеграции данных о затратах

Каждая точка данных об использовании и затратах, отображаемая в Account Management, также доступна через API Dynatrace.
Это значит, что данные о потреблении можно экспортировать, передавать между командами и интегрировать в любой инструмент, уже используемый в организации: от финансовых систем до собственных дашбордов. Типичные сценарии использования:

* Предоставление видимости затрат владельцам бюджета и финансовым командам.
* Передача данных о потреблении в корпоративные инструменты.
* Автоматизация отчётов и оповещений по бюджету.
* Интеграция с внутренними системами распределения затрат или chargeback.

Все доступные эндпоинты также можно изучить непосредственно в **API Explorer** в Account Management или в [документации API Account Management](/managed/dynatrace-api/account-management-api "Explore endpoints of the Account Management API.").

## Похожие темы

* [Account Management](/managed/manage/account-management "Manage your Dynatrace license, accounts, platform adoption, and environment health.")
* [Недоступно в Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.")
* [Цены Dynatrace﻿](https://www.dynatrace.com/pricing/)
* [Billing report](/managed/manage-your-costs/view/billing-report "View your billing to see details about accrued costs per booking date. Use this view to determine which Dynatrace monitoring costs were recognized and booked on which day.")