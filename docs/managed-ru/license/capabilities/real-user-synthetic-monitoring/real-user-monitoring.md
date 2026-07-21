---
title: Понимание и управление потреблением для Real User Monitoring (DPS)
source: https://docs.dynatrace.com/managed/license/capabilities/real-user-synthetic-monitoring/real-user-monitoring
---

# Понимание и управление потреблением для Real User Monitoring (DPS)

# Понимание и управление потреблением для Real User Monitoring (DPS)

* Пояснение
* 5 минут на чтение
* Обновлено 26 июня 2026 г.

Real User Monitoring (RUM) даёт полную видимость того, как конечные пользователи взаимодействуют с каждой цифровой транзакцией в веб-приложениях, мобильных и single-page приложениях.

На этой странице описано, как рассчитывается потребление RUM и как можно управлять расходами на RUM в Dynatrace.

## Как рассчитывается потребление

Единица измерения потребления RUM, это **сессии**, плюс количество **свойств сессии**, зафиксированных в рамках этих сессий.

Это измеряется с помощью:

* Позиции прайс-листа **Real User Monitoring**, если session replay не включён.
* Позиции прайс-листа **Real User Monitoring with Session Replay**, если session replay включён.
* Позиции прайс-листа **Real User Monitoring Property**, которая применяется отдельно.

### Ключевые термины

Пользовательская сессия
:   Пользовательская сессия (или просто «сессия») представляет собой одно посещение приложения одним пользователем.
    Пользовательская сессия обобщает действия пользователя и технические события, происходящие в течение этого посещения.
    Одна пользовательская сессия может охватывать несколько приложений, как веб, так и мобильных компонентов.

    Подробнее см. [Пользовательские сессии в RUM Classic](/managed/observe/digital-experience/rum-classic/rum-concepts/user-session "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.").

Приложение
:   Приложение (или просто «app»), это логическая сущность, определяемая клиентом в Dynatrace, используемая для мониторинга части или всего клиентского приложения.
    Dynatrace фиксирует пользовательские сессии для веб, мобильных и пользовательских приложений.
    У него есть интерфейс для конечного пользователя, и оно получает трафик реальных пользователей.

    Подробнее см. [Приложения в RUM Classic](/managed/observe/digital-experience/rum-classic/rum-concepts/applications "Learn about monitored applications in Real User Monitoring Classic and the different application types supported by Dynatrace.").

Свойство сессии
:   Свойство сессии, это метаданные, предоставляющие информацию о производительности приложения, которые Dynatrace собирает в рамках конкретной сессии RUM.

    Подробнее см. [Определение свойств пользовательского действия и пользовательской сессии для пользовательских приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/custom-applications/additional-configuration/define-custom-action-and-session-properties "Send metadata to Dynatrace and define action and session properties for your monitored custom applications.").

### Правила подсчёта и исключения

* Если посещение пользователя охватывает несколько приложений, Dynatrace засчитывает одну сессию для каждого приложения, с которым взаимодействовал пользователь.
* Если посещение пользователя длится дольше одного часа в рамках конкретного приложения, Dynatrace засчитывает дополнительную сессию за каждый начавшийся час.
  Полные сведения о том, когда пользовательские сессии RUM начинаются и заканчиваются, см. в [Тайминги пользовательской сессии](/managed/observe/digital-experience/rum-classic/rum-concepts/user-session#user-session-timings "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.").
* Посещение пользователя, связанное с гибридным мобильным приложением, которое по техническим причинам включает веб-приложение и мобильное приложение, считается одной пользовательской сессией.
* Пользовательские сессии, включающие только одно пользовательское действие (например, загрузку страницы или переход, вызывающий веб-запросы), считаются отказами (bounced).
  Они не учитываются в потреблении RUM.
* Приложения с менее чем 2 пользовательскими действиями в час не генерируют потребление пользовательских сессий.
* RUM включает до 20 свойств сессии для каждого приложения без дополнительной оплаты.
  Дополнительные свойства сессии (сверх включённых 20) выставляются по тарифам **Real User Monitoring Property** за каждую сессию, в которой это свойство присутствует.

  **Примечание**: при миграции существующего приложения RUM Classic на Latest Dynatrace предусмотрена защита от двойного выставления счетов, оплата взимается только за максимальное количество свойств, настроенных либо в RUM Classic, либо в Latest Dynatrace.

### Пример расчёта

Например, пользователь посещает розничный сайт для совершения покупки.

Пользователь:

1. Просматривает онлайн-каталог товаров и добавляет некоторые позиции в корзину.
   Это занимает 75 минут.
2. Просматривает товары в корзине покупок.
   Это занимает 3 минуты.
3. Оформляет заказ и покупает товары.
   Это занимает 7 минут.

Поскольку сессии выставляются по счёту в расчёте на приложение за час, всего потребляется четыре сессии, см. рисунок ниже.

![DIAGRAM - Real User Monitoring consumption example](https://dt-cdn.net/images/rum-consumption-calculation-example-corrected-7112-aae60e7915.png)

DIAGRAM - пример потребления Real User Monitoring

## Оценка стоимости

Следующий пример демонстрирует, как рассчитывается стоимость для сессий RUM.

Для простоты в этом примере предполагается, что…

* Расчёты основаны на следующих ценах прайс-листа (которые могут отличаться от цен вашего прайс-листа):

  + Real User Monitoring: $0,00225 за сессию.
  + Real User Monitoring with Session Replay: $0,0045 за сессию.
  + Real User Monitoring Property: $0,0001 за свойство за сессию.
  + Все цены указаны в USD.
* Один месяц эквивалентен 30 дням.
* Отслеживаемая сущность, это одно веб-приложение.

  + Сущность отслеживается 24 часа в сутки.
  + Все посещения пользователей длились менее одного часа.
  + Уровни трафика составляют 5000 сессий в час (эквивалент 3 600 000 сессий в месяц).

### Пример стоимости 1: Real User Monitoring

Если включить **Real User Monitoring** по цене прайс-листа, ежемесячные затраты составят:

* 3 600 000 сессий × $0,00225 = **$8100 в месяц**

### Пример стоимости 2: Real User Monitoring with Session Replay

Если включить **Real User Monitoring**, и для 20% (720 000) от общего числа сессий включён **Real User Monitoring Session Replay**, ежемесячные затраты составят:

* Real User Monitoring: 2 880 000 x $0,00225 = $6480 в месяц
* Real User Monitoring with Session Replay: 720 000 x $0,0045 = $3240 в месяц
* $6480 + $3240 = **$9720 в месяц**

### Пример стоимости 3: Real User Monitoring Property

Если определить 30 свойств сессии, ежемесячные затраты составят:

* 30 всего свойств – 20 включённых свойств = 10 оплачиваемых свойств на сессию
* 10 оплачиваемых свойств × 3 600 000 сессий = 36 000 000
* 36 000 000 × $0,0001 = **$3600 в месяц**

## Отслеживание потребления

Dynatrace предоставляет различные варианты, помогающие понять и проанализировать потребление возможностей RUM вашей организацией.

### Аналитика через Account Management

Менеджеры лицензий могут просматривать использование и затраты в Account Management.

Перейти в **Account Management** > **Subscription** > **Overview** > **Cost and usage details** > **Usage summary** и выбрать соответствующую категорию: **Real User Monitoring**, **Real User Monitoring with Session Replay** или **Real User Monitoring Property**.

Подробнее об интерфейсе обзора подписки см. в [Overview (Dynatrace Platform Subscription)](/managed/manage/account-management/license-subscription/subscription-overview-dps "View your Dynatrace Platform Subscription (DPS) budget summary and cost analysis.").

![Diagram - Example usage for Real User Monitoring visible in Account Management](https://dt-cdn.net/images/rum-usage-overview-account-management-2910-7a5d37e705.png)

Diagram - пример использования Real User Monitoring, отображаемого в Account Management

### Аналитика через события использования для выставления счетов

Billing usage events (BUE, `billing_usage_event`), это системные события, отправляемые Dynatrace в пространство данных `dt.system.events`.
Можно использовать DQL для запросов BUE и анализа использования и стоимости для возможностей Real User Monitoring без повторного применения правил биллинга или логики подсчёта сессий.

BUE представляют уже рассчитанное, оплачиваемое использование для возможностей DPS (не какую-либо конфигурацию или потенциальное использование) и соответствуют тому, что отображается в Account Management и в счетах.
Поэтому они рекомендуются как источник данных для понимания потребления, связанного с RUM.

Billing usage events содержат:

* Какая возможность DPS была использована.
* Объём использования, учитываемый в биллинге.
* Временной интервал, к которому относится использование.
* Контекст сущности, к которой относится использование (например, приложение).

#### Billing usage events для возможностей RUM

В таблице ниже описаны billing usage events для трёх возможностей RUM.

| Возможность | `usageAmount` | Правила подсчёта |
| --- | --- | --- |
| Real User Monitoring | Сессии, которые оплачиваются по тарифу Real User Monitoring, для данного приложения и временного интервала. | Все правила подсчёта уже применены (для каждого приложения, для каждого часа, отказные сессии исключены). |
| Real User Monitoring с Session Replay | Сессии, которые оплачиваются по тарифу Real User Monitoring с Session Replay, для данного приложения и временного интервала. | Только сессии, для которых был включён Session Replay. |
| Real User Monitoring Property | Оплачиваемые вхождения свойств по сессиям. | Учитываются только свойства сверх включённых 20 на приложение, и только когда они присутствуют в сессии. |

#### Запрос billing usage events с помощью DQL

Billing usage events можно использовать как достоверный источник при построении представлений распределения затрат, анализа использования или прозрачности стоимости:

* Фильтровать billing usage events по возможности, чтобы различать использование Real User Monitoring, использование Real User Monitoring с Session Replay и использование Real User Monitoring Property.
* Агрегировать по приложению, чтобы понять, какие приложения больше всего вносят вклад в использование и стоимость.

Ниже приведены примеры запросов DQL для различных сценариев использования.
Эти запросы можно использовать как есть или изменить их под свои нужды.

* Общее использование Real User Monitoring во времени

  ```
  fetch dt.system.events



  | filter event.kind == "BILLING_USAGE_EVENT" and event.type == "Real User Monitoring"



  | dedup event.id



  | summarize totalUsage = sum(billed_sessions), by:{bin(timestamp, 1d)}
  ```
* Общее использование по возможности (все приложения)

  ```
  fetch dt.system.events



  | filter event.kind == "BILLING_USAGE_EVENT"



  | filter event.type == "Real User Monitoring" or



  event.type == "Real User Monitoring with Session Replay" or



  event.type == "Real User Monitoring Property"



  | fieldsAdd



  web_or_mobile = coalesce(dt.entity.application, dt.entity.device_application),



  platform = if(isNotNull(dt.entity.application), "Web", else: "Mobile")



  | dedup event.id



  | summarize



  RUM = sum(billed_sessions),



  Replay = sum(billed_replay_sessions),



  Property = sum(billed_property_sessions),



  by:{platform, web_or_mobile, event.type}
  ```
* Общее использование по возможности для одного приложения

  ```
  fetch dt.system.events



  | filter event.kind == "BILLING_USAGE_EVENT"



  | filter event.type == "Real User Monitoring" or



  event.type == "Real User Monitoring with Session Replay" or



  event.type == "Real User Monitoring Property"



  | fieldsAdd



  web_or_mobile = coalesce(dt.entity.application, dt.entity.device_application),



  platform = if(isNotNull(dt.entity.application), "Web", else: "Mobile")



  | filter web_or_mobile == "APPLICATION-DC92E74A7A844E6E"



  | dedup event.id



  | summarize



  RUM = sum(billed_sessions),



  Replay = sum(billed_replay_sessions),



  Property = sum(billed_property_sessions),



  by:{platform, web_or_mobile}
  ```
* Использование Real User Monitoring по приложению

  ```
  fetch dt.system.events



  | filter event.kind == "BILLING_USAGE_EVENT" and event.type == "Real User Monitoring"



  | fieldsAdd



  web_or_mobile = coalesce(dt.entity.application, dt.entity.device_application),



  platform = if(isNotNull(dt.entity.application), "Web", else: "Mobile")



  | dedup event.id



  | summarize totalUsage = sum(billed_sessions), by:{platform, web_or_mobile}



  | sort totalUsage desc
  ```
* Использование Real User Monitoring с Session Replay по приложению

  ```
  fetch dt.system.events



  | filter event.kind == "BILLING_USAGE_EVENT" and event.type == "Real User Monitoring with Session Replay"



  | fieldsAdd



  web_or_mobile = coalesce(dt.entity.application, dt.entity.device_application),



  platform = if(isNotNull(dt.entity.application), "Web", else: "Mobile")



  | dedup event.id



  | summarize totalUsage = sum(billed_replay_sessions), by:{platform, web_or_mobile}



  | sort totalUsage desc
  ```
* Использование Real User Monitoring Property по приложению

  ```
  fetch dt.system.events



  | filter event.kind == "BILLING_USAGE_EVENT" and event.type == "Real User Monitoring Property"



  | fieldsAdd



  web_or_mobile = coalesce(dt.entity.application, dt.entity.device_application),



  platform = if(isNotNull(dt.entity.application), "Web", else: "Mobile")



  | dedup event.id



  | summarize totalUsage = sum(billed_property_sessions), by:{platform, web_or_mobile}



  | sort totalUsage desc
  ```

### Insights через API

Можно запрашивать insights через [Environment API – Grail Query﻿](https://developer.dynatrace.com/develop/platform-services/services/grail-service/#grail-query-api).
Примеры запросов DQL приведены в разделе [Запрос billing usage events с помощью DQL](#rum-dql-query).

## Часто задаваемые вопросы

Учитываются ли отказные сессии в потреблении RUM?

Нет.
Сессии, включающие только одно действие пользователя (например, загрузку страницы без дальнейшего взаимодействия), считаются отказными.
Отказные сессии отфильтровываются и не учитываются в потреблении RUM.

Как Dynatrace подсчитывает сессии, когда посещение охватывает несколько приложений?

Если пользователь взаимодействует более чем с одним приложением в ходе своего посещения (например, как с веб-приложением, так и с мобильным компонентом), каждое приложение учитывается как одна сессия.

Исключение: взаимодействие с гибридным мобильным приложением, охватывающим как мобильные, так и веб-технологии, учитывается как одна сессия.

Когда применяются дополнительные платежи за сессии RUM для свойств?

Каждое приложение включает до 20 свойств без дополнительной платы.
Каждое свойство сверх этих 20 оплачивается один раз за каждую сессию, в которой это свойство присутствует.

Увеличивает ли включение Session Replay потребление?

Да.
Сессии с включённым Session Replay оплачиваются согласно позиции **Real User Monitoring с Session Replay** в тарифной карте.

Что происходит, если сессия длится дольше одного часа?

Dynatrace учитывает дополнительную сессию каждый раз, когда начинается новый час активности.
Например, посещение одного и того же приложения продолжительностью 2,5 часа учитывается как три сессии.

## Похожие темы

* [Обзор Real User и Synthetic Monitoring (DPS)](/managed/license/capabilities/real-user-synthetic-monitoring "Узнайте, как рассчитывается потребление Real User и Synthetic Monitoring Dynatrace с использованием модели Dynatrace Platform Subscription.")
* [Real User Monitoring Classic](/managed/observe/digital-experience/rum-classic/rum-concepts/rum-overview "Узнайте о Real User Monitoring Classic, ключевых показателях производительности, мониторинге мобильных приложений и других возможностях.")
* [Лицензирование Dynatrace](/managed/license "Dynatrace Platform Subscription, тарифные карты возможностей, гибридное лицензирование и предыдущие модели лицензирования.")
* [Цены Dynatrace﻿](https://www.dynatrace.com/pricing/)