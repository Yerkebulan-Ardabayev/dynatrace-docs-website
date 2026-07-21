---
title: View your previous DPS periods via subscription history
source: https://docs.dynatrace.com/managed/manage-your-costs/reference/subscription-history
---

# View your previous DPS periods via subscription history

# View your previous DPS periods via subscription history

* Explanation
* 4-min read
* Updated on Jul 16, 2025

Страница **Subscription history** показывает истёкшие, активные и ожидающие подписки и лицензии Dynatrace.
Можно посмотреть детали всех подписок Dynatrace, которые были активны за последние три года.

## Overview

Subscription history позволяет просматривать потребление за предыдущие периоды подписки DPS после продления, когда live overview переключается на новый период. Исторические данные охватывают разбивку по стоимости, использованию и capability за любой прошлый период, в течение которого аккаунт был активен.

## Use cases

* Сравнить фактическое потребление на конец периода с обязательствами прошлого года.
* Получить историческую разбивку по capability для бюджетирования или переговоров по продлению.
* Проверить, как менялось распределение затрат между периодами.

## Requirements

Для просмотра subscription history нужно:

* Активная Dynatrace Platform Subscription, подписанная после 26 апреля 2023 года.
* Учётная запись пользователя Dynatrace с одним или обоими из следующих [прав Account Management](/managed/manage/identity-access-management/permission-management/account-management-permissions "Права Dynatrace, необходимые для доступа к Account Management"):

  + **View account**
  + **View and manage account and billing information**

## View subscription history

Чтобы посмотреть **Subscription history**

1. Перейти в [**Account Management**﻿](https://myaccount.dynatrace.com/).
2. Выбрать **Subscription** > **History**.

Эта страница даёт удобный доступ к деталям использования Dynatrace и затратам, связанным с каждой подпиской и лицензией.

![Account Management: Subscription history](https://dt-cdn.net/images/history-list-1600-dcce197542.png)

Account Management: Subscription history

## View details

Чтобы отобразить детали подписки, нужно найти нужную подписку и выбрать **View details**.
Откроется окно **History** с информацией о **Budget summary** и **Cost and usage details**.

* **Budget summary** показывает:

  + Общий использованный бюджет в процентах от годового бюджета.
  + Прогноз бюджета: фактические затраты, прогнозируемые затраты и годовой бюджет.
* Детали по затратам и использованию представлены на двух вкладках.

  + Вкладка **Cost summary** показывает фактические затраты (в локальной валюте) на основе потребления за период подписки.
  + Вкладка **Usage summary** показывает использование environment согласно единице измерения capability.

Детали по затратам и использованию доступны для всех environment и capability, предоставленных в рамках подписки.
Можно детализировать данные, сфокусировавшись на отдельных environment и capability.

## FAQ

### Моя Dynatrace Platform Subscription началась до 26 апреля 2023 года. Есть ли у меня доступ к subscription history?

Страница **Subscription history** доступна для

* Клиентов с Dynatrace Platform Subscription, которая началась 26 апреля 2023 года или позже.
* Клиентов, перешедших с классической лицензии Dynatrace на лицензию Dynatrace Platform Subscription (DPS), могут просматривать свои подписки.
  Также будут отображаться все предыдущие лицензии DPS и лицензии на основе квот.

### Могу ли я увидеть историю своей лицензии Dynatrace Managed?

Портал Account Management предоставляет обзор всех прошлых, активных и ожидающих подписок, включая предыдущие лицензии на основе квот.

## Related topics

* [License Dynatrace](/managed/license "Dynatrace Platform Subscription, карточки тарифов capability, гибридное лицензирование и предыдущие модели лицензирования.")
* [Account Management](/managed/manage/account-management "Управление лицензией Dynatrace, аккаунтами, внедрением платформы и состоянием environment.")
* [Where to view your costs](/managed/manage-your-costs/view/where-to-look "Просмотр потребления и затрат Dynatrace в Account Management, прямые запросы к событиям биллинга через DQL или обращение к Dynatrace Intelligence на естественном языке.")
* [Billing report](/managed/manage-your-costs/view/billing-report "Просмотр биллинга для детального анализа накопленных затрат по дате бронирования. Используйте это представление, чтобы определить, какие затраты на мониторинг Dynatrace были признаны и учтены в какой день.")