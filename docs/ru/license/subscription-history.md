---
title: Просмотр предыдущих периодов DPS через историю подписок
source: https://www.dynatrace.com/docs/license/subscription-history
scraped: 2026-03-06T21:32:43.549341
---

* Latest Dynatrace
* Tutorial
* 4-min read

Страница **Subscription history** содержит список ваших истёкших, активных и ожидающих подписок и лицензий Dynatrace.
Вы можете просматривать сведения обо всех подписках Dynatrace, которые были активны в течение последних трёх лет.

## Требования

Для просмотра истории подписок необходимо:

* Активная подписка Dynatrace Platform Subscription, заключённая после 26 апреля 2023 года.
* Учётная запись пользователя Dynatrace с одним или обоими из следующих [разрешений управления аккаунтом](../manage/identity-access-management/permission-management/account-management-permissions.md "Dynatrace permissions required to access Account Management"):

  + **View account**
  + **View and manage account and billing information**

## Просмотр истории подписок

Для просмотра **Subscription history**:

1. Перейдите в [**Account Management**](https://myaccount.dynatrace.com/).
2. Выберите **Subscription** > **History**.

Эта страница предоставляет удобный доступ к сведениям об использовании Dynatrace и расходах, связанных с каждой подпиской и лицензией.

Информация о стоимости для подписок POC (обозначаются типом `DPS:POC`) предоставляется исключительно в информационных целях.
Эти расходы фактически не взимаются, поскольку POC являются бесплатными согласно условиям вашей лицензии POC.

Дополнительную информацию о POC см. в разделе [Proof of Concept for existing DPS subscriptions](proof-of-concept.md "Use Account Management tools to view consumption during your DPS Proof of Concept period.").

![Account Management: Subscription history](https://dt-cdn.net/images/history-list-1600-dcce197542.png)

## Просмотр деталей

Чтобы отобразить сведения о подписке, найдите нужную подписку и выберите **View details**.
Откроется окно **History** с информацией о **Budget summary** и **Cost and usage details**.

* В разделе **Budget summary** отображается:

  + Общий израсходованный бюджет в процентах от годового бюджета.
  + Прогноз бюджета: фактические расходы, прогнозируемые расходы и годовой бюджет.
* Сведения о стоимости и использовании представлены на двух вкладках.

  + Вкладка **Cost summary** отображает фактические расходы (в местной валюте) на основе потребления за период подписки.
  + Вкладка **Usage summary** показывает использование среды в соответствии с единицей измерения возможности.

Сведения о стоимости и использовании доступны для всех сред и возможностей, предоставляемых в рамках подписки.
Вы можете детализировать данные до отдельных сред и возможностей.

## Часто задаваемые вопросы

### Моя подписка Dynatrace Platform Subscription началась до 26 апреля 2023 года. Могу ли я получить доступ к истории подписок?

Страница **Subscription history** доступна для:

* Клиентов с подпиской Dynatrace Platform Subscription, начавшейся 26 апреля 2023 года или позднее.
* Клиентов, перешедших с классической лицензии Dynatrace на лицензию Dynatrace Platform Subscription (DPS): они могут просматривать свои подписки.
  Все предыдущие лицензии DPS и квотные лицензии также будут отображаться.

### Почему я не вижу сведения о часах использования хостовых единиц, пользовательских сессиях или пользовательских метриках и журналах для подписки Dynatrace SaaS?

Отображаются только контракты с функциями Host Unit, DEM и DDU. Если вы были лицензированы с использованием более старых функциональных возможностей, подробные сведения не отображаются.

## Связанные темы

* [License Dynatrace](../license.md "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")
