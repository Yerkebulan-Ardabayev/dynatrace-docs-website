---
title: Управление подписками и лицензиями (DPS до апреля 2023)
source: https://docs.dynatrace.com/managed/license/classic-licensing/subscription-and-license-dps
---

# Управление подписками и лицензиями (DPS до апреля 2023)

# Управление подписками и лицензиями (DPS до апреля 2023)

* Пояснение
* 2 мин на чтение
* Опубликовано 01 февраля 2022

Эта документация актуальна для лицензий Dynatrace Platform Subscription, подписанных до 26 апреля 2023 года.
Информацию обо всех остальных лицензиях Dynatrace Platform Subscription смотри в разделе [Лицензия Dynatrace](/managed/license "Dynatrace Platform Subscription, карточки тарифов возможностей, гибридное лицензирование и предыдущие модели лицензирования.").

Эта страница предоставлена исключительно в информационных целях.
К любому использованию продуктов или сервисов Dynatrace применяются условия бесплатной пробной версии Dynatrace и (или) условия лицензии Dynatrace.

Модель Dynatrace platform subscription (DPS) упрощает потребление мониторинга на платформе Dynatrace, приводя всё потребление функциональности мониторинга Dynatrace к единой валютной единице: unit DPS.
Такой подход объединяет потребление всех единиц мониторинга Dynatrace (host units, Davis data units, DEM units, Mainframe units и Application security units) в единую единицу потребления.

## Dynatrace Platform Subscription (DPS)

### Dynatrace Managed

Развёртывание Dynatrace Managed может включать несколько кластеров, каждый со своей лицензией, и каждая лицензия определяет продукты, которые можно использовать.
Возможности продуктов могут включать

* host units[1](#fn-1-1-def)
* host unit hours[2](#fn-1-2-def)
* Digital Experience Monitoring
* Davis data units
* Application security units

1

Размер хоста для целей лицензирования (на основе объёма RAM, предоставляемого хостом).
Подробнее смотри в разделе [Application and Infrastructure Monitoring (Host Units)](/managed/license/classic-licensing/application-and-infrastructure-monitoring "Как рассчитывается потребление мониторинга приложений и инфраструктуры Dynatrace на основе host units.").

2

Отражает потребление host unit за период времени. Один unit hour равен одному unit, потреблённому за один час.
Хост с 16 ГБ RAM (один unit), работающий полные сутки, потребляет 24 host unit hours.
Модель Dynatrace Platform Subscription основана на тех же единицах мониторинга, что используются во всех возможностях Dynatrace.

Объём Dynatrace Platform Subscription определяется размером годовых лицензионных обязательств.
Эти обязательства platform subscription, совокупно называемые годовым коммитом, привязаны к аккаунту и могут использоваться в течение года подписки.
Прошлое потребление архивируется в начале каждого нового года подписки, и полный объём годового коммита сбрасывается.
Обрати внимание: часть годового коммита, не использованная к концу года подписки, не переносится на новый год подписки.

## Как расходуются unit DPS

Каждый час Dynatrace собирает всю статистику использования из окружений, рассчитывает потребление и применяет стоимость единиц мониторинга, определённую для подписки.
Затем общее потребление вычитается из годового коммита DPS. Оставшийся баланс, это объём, доступный на оставшуюся часть года подписки.

## Отслеживание потребления

Потребление лицензии можно посмотреть в:

* Account Management, см. [Обзор подписки (Dynatrace Platform Subscription до 2023)](/managed/manage/account-management/license-subscription/subscription-overview-dps-la "Обзор бюджета и анализ стоимости Dynatrace Platform Subscription.").
* API Account Management, см. [API Dynatrace Platform Subscription](/managed/dynatrace-api/account-management-api/dynatrace-platform-subscription-api "Запрос данных о Dynatrace Platform Subscription через API Account Management.").

Информация включает:

* Account usage: сводку по тому, какая часть годового коммита уже использована.
* Потребление Environment: разбивку использования годового коммита по окружениям и возможностям.
* Usage details: исторический график и табличное представление использования по окружениям и возможностям.