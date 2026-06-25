---
title: Управление подпиской и лицензией (DPS до апреля 2023 года)
source: https://docs.dynatrace.com/managed/license/subscription-and-license/subscription-and-license-dps
scraped: 2026-05-12T11:09:07.428723
---

# Управление подпиской и лицензией (DPS до апреля 2023 года)

# Управление подпиской и лицензией (DPS до апреля 2023 года)

* Explanation
* 2-min read
* Published Feb 01, 2022

Данная документация действительна для лицензий Dynatrace Platform Subscription, подписанных до 26 апреля 2023 года.
Для информации о всех остальных лицензиях Dynatrace Platform Subscription см. [Лицензирование Dynatrace](/managed/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.").

Эта страница предоставляется исключительно в информационных целях.
К любому использованию продуктов или услуг Dynatrace применяются условия бесплатной пробной версии Dynatrace и/или вашей лицензии Dynatrace.

Модель подписки на платформу Dynatrace (DPS) упрощает потребление мониторинга на платформе Dynatrace, основывая всё потребление функций мониторинга Dynatrace на стандартной единице валюты: единице DPS.
Этот подход консолидирует потребление всех единиц мониторинга Dynatrace (хост-единицы, единицы Davis data units, единицы DEM, единицы мейнфрейма и единицы Application Security) в единицу потребления.

## Dynatrace Platform Subscription (DPS)

### Dynatrace Managed

Развёртывание Dynatrace Managed может включать несколько кластеров, каждый со своей лицензией, определяющей доступные продукты.
Возможности продуктов могут включать:

* хост-единицы
* хост-единицы-часы
* Digital Experience Monitoring
* единицы Davis data units
* единицы Application Security

Размер хоста для целей лицензирования определяется объёмом ОЗУ, предоставляемым хостом.
Подробнее см. в [Мониторинг приложений и инфраструктуры (хост-единицы)](/managed/license/monitoring-consumption-classic/application-and-infrastructure-monitoring "Understand how Dynatrace application and infrastructure monitoring consumption is calculated based on host units.").

Хост-единица-час представляет потребление хост-единицы за период времени. Одна единица-час соответствует одной единице за один час.
Хост с 16 GB ОЗУ (одна единица), работающий полный день, потребляет 24 хост-единицы-часа.
Модель Dynatrace Platform Subscription основана на тех же единицах мониторинга, которые используются во всех возможностях Dynatrace.

Объём Dynatrace Platform Subscription определяется суммой годовых лицензионных обязательств.
Эти обязательства по подписке, в совокупности называемые годовым коммитом, назначаются вашему аккаунту и могут быть использованы в течение года подписки.
Прошлое потребление архивируется в начале каждого нового года подписки, и полный объём годового коммита сбрасывается.
Обратите внимание, что неиспользованная часть годового коммита не переносится на новый год подписки.

## Как потребляются единицы DPS

Каждый час Dynatrace собирает все статистические данные использования из ваших сред, рассчитывает потребление и применяет стоимость единиц мониторинга, определённую для вашей подписки.
Суммарное потребление затем вычитается из годового коммита DPS. Остаток — доступный объём на оставшуюся часть года подписки.

## Отслеживание потребления

Просматривать потребление лицензии можно в:

* Account Management — см. [Обзор подписки (Dynatrace Platform Subscription до 2023 года)](/managed/manage/account-management/license-subscription/subscription-overview-dps-la "View your Dynatrace Platform Subscription budget summary and cost analysis.").
* Account Management API — см. [API Dynatrace Platform Subscription](/managed/dynatrace-api/account-management-api/dynatrace-platform-subscription-api "Query the data about your Dynatrace Platform Subscription via the Account Management API.").

Доступная информация включает:

* Использование аккаунта: сводка о том, какая часть годового коммита была использована.
* Использование по средам: разбивка использования годового коммита по средам и возможностям.
* Детали использования: исторический график и таблица использования по средам и возможностям.