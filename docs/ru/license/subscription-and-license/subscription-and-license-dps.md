---
title: Управление подпиской и лицензией (DPS до апреля 2023)
source: https://www.dynatrace.com/docs/license/subscription-and-license/subscription-and-license-dps
scraped: 2026-03-06T21:22:13.621808
---

# Управление подпиской и лицензией (DPS до апреля 2023 г.)


* Последняя версия Dynatrace
* Пояснение
* Время чтения: 2 мин
* Опубликовано 1 февраля 2022 г.

Эта документация актуальна для лицензий Dynatrace Platform Subscription, заключённых до 26 апреля 2023 г.
Информацию обо всех прочих лицензиях Dynatrace Platform Subscription см. в разделе [Лицензирование Dynatrace](../../license.md "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.").

Эта страница предоставляется исключительно в информационных целях.
К любому использованию продуктов или сервисов Dynatrace применяются условия бесплатного пробного предложения Dynatrace и/или вашей лицензии Dynatrace.

Модель подписки на платформу Dynatrace (DPS) упрощает потребление мониторинга на платформе Dynatrace, основывая всё потребление функциональности мониторинга Dynatrace на стандартной единице измерения: единице DPS.
Этот подход объединяет потребление всех единиц мониторинга Dynatrace (хост-единицы, единицы данных Davis, единицы DEM, единицы мейнфреймов и единицы Application security) в единую единицу потребления.

## Dynatrace Platform Subscription (DPS)

В развёртывании Dynatrace SaaS действует одна активная лицензия, определяющая доступные вам продукты.
Возможности продуктов включают:

* хост-единицы[1](#fn-1-1-def)
* хост-единицо-часы[2](#fn-1-2-def)
* Digital Experience Monitoring
* единицы данных Davis
* единицы Application security

1

Размер хоста для целей лицензирования (определяется объёмом ОЗУ, предоставленного хостом).
Подробная информация приведена в разделе [Application and Infrastructure Monitoring (Host Units)](../monitoring-consumption-classic/application-and-infrastructure-monitoring.md "Understand how Dynatrace application and infrastructure monitoring consumption is calculated based on host units.").

2

Отражает потребление хост-единицы за определённый период. Одна единицо-единица соответствует одной единице, потреблённой за один час.
Хост с 16 ГБ ОЗУ (одна единица), работающий в течение полного дня, потребляет 24 хост-единицо-часа.
Модель Dynatrace Platform Subscription основана на тех же единицах мониторинга, которые используются во всех возможностях Dynatrace.

Объём вашей Dynatrace Platform Subscription определяется суммой ежегодных лицензионных обязательств.
Эти обязательства по платформенной подписке, совокупно именуемые вашим ежегодным обязательством (annual commit), назначаются вашей учётной записи и могут быть использованы в течение года подписки.
В начале каждого нового года подписки прошлое потребление архивируется, а полный объём ежегодного обязательства сбрасывается.
Обратите внимание: неиспользованная к концу года подписки часть ежегодного обязательства не переносится на новый год подписки.

## Как расходуются единицы DPS

Каждый час Dynatrace собирает всю статистику использования из ваших сред, рассчитывает потребление и применяет стоимости единиц мониторинга, определённые для вашей подписки.
Общее потребление затем вычитается из вашего ежегодного обязательства DPS. Остаток — это сумма, доступная вам до конца года подписки.

## Отслеживание потребления

Вы можете просматривать потребление лицензии в:

* Account Management — см. [Обзор подписки (Dynatrace Platform Subscription до 2023 г.)](../../manage/account-management/license-subscription/subscription-overview-dps-la.md "View your Dynatrace Platform Subscription budget summary and cost analysis.").
* API управления учётными записями — см. [API Dynatrace Platform Subscription](../../dynatrace-api/account-management-api/dynatrace-platform-subscription-api.md "Query the data about your Dynatrace Platform Subscription via the Account Management API.").

Доступная информация включает:

* Использование по учётной записи: сводка о том, какая часть ежегодного обязательства была использована.
* Использование по средам: разбивка того, как ежегодное обязательство использовалось в ваших средах и по возможностям.
* Детали использования: исторический график и табличное представление использования по средам и возможностям.
