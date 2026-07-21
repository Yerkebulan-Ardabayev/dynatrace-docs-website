---
title: Определение свойств пользовательского действия и пользовательской сессии для пользовательских приложений в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/custom-applications/additional-configuration/define-custom-action-and-session-properties
---

# Определение свойств пользовательского действия и пользовательской сессии для пользовательских приложений в RUM Classic

# Определение свойств пользовательского действия и пользовательской сессии для пользовательских приложений в RUM Classic

* Практическое руководство
* 1 минута на чтение
* Опубликовано 27 января 2022 г.

Dynatrace собирает много информации о производительности приложений. Эту информацию можно обогатить ценными метаданными, а затем преобразовать метаданные в свойства пользовательского действия и пользовательской сессии.

Свойства действия и сессии, это пары «ключ, значение» метаданных, которые можно фильтровать во всех представлениях анализа Dynatrace. Эти свойства пригодятся, когда нужно создавать сложные запросы, сегментации или агрегации по собранным метаданным. Эти свойства можно использовать на страницах **User sessions** и **User sessions query**. Подробнее о том, как использовать эти свойства, см. [Использование свойств пользовательского действия и пользовательской сессии для пользовательских приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/custom-applications/analyze-and-use/action-and-session-properties-custom "User action and session properties, which are metadata key-value pairs, provide added visibility and deeper analysis of your end users' experience. Using these properties for your applications, you can filter user sessions, add calculated metrics, create charts, and more.").

Ниже приведена информация о том, как настроить такие свойства, а также соответствующие примеры настройки. Чтобы использовать свойства действия и сессии, нужно сначала отправить необходимые метаданные в Dynatrace, а затем [добавить свойства в веб-интерфейсе Dynatrace](#add-properties).

## Отправка метаданных в Dynatrace

Прежде чем определять свойства действия и сессии, нужно сначала начать передавать необходимые метаданные в Dynatrace. Сделать это можно двумя способами:

* [Передача пользовательских значений через SDK](#report-value-sdk)
* [Определение атрибутов запроса](#add-request-attribute)

### Передача значения через SDK

Пары «ключ, значение» метаданных можно передавать в исходном коде пользовательского приложения через вызов API. Подробнее см. [Методы API Dynatrace OpenKit | Передача значения](/managed/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-api-methods#report-values "Read how Dynatrace OpenKit can be used from the developer's point of view.").

Чтобы проверить, доходят ли данные, передаваемые в коде приложения, до Dynatrace, перейти к деталям пользовательского действия, которое должно содержать эти данные, и прокрутить вниз до раздела **Reported values**.

![Страница деталей пользовательского действия со значениями, переданными через SDK](https://dt-cdn.net/images/user-action-details-with-reported-values-2048-b44e8bca3e.png)

Страница деталей пользовательского действия со значениями, переданными через SDK

### Определение атрибута запроса

Кроме того, можно добавить необходимые метаданные к запросам на стороне сервера, определить атрибуты запроса, а затем использовать эти атрибуты для создания свойств действия и сессии.

Атрибуты запроса формируются на основе URL веб-запросов, заголовков HTTP-запросов и других метаданных запроса. Эти атрибуты представляют собой пары «ключ, значение», которые можно фильтровать во многих представлениях анализа и распределённой трассировки Dynatrace.

Подробнее см. [Атрибуты запроса](/managed/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.").

## Добавление свойств действия и сессии

После того как значения переданы через код приложения или определены атрибуты запроса, информация, которую собирает Dynatrace, обогащается ценными метаданными. Эти метаданные можно «продвинуть» до свойств действия и сессии в настройках приложения.

Метаданные можно сохранять на разных «уровнях хранения»:

* **User action property**: данные сохраняются в определённом свойстве на уровне пользовательского действия для каждого пользовательского действия, для которого Dynatrace может получить метаданные.
* **User session property**: последнее полученное значение сохраняется в определённом свойстве на уровне сессии.
* **Both options**: данные сохраняются в определённом свойстве как на уровне пользовательского действия, так и на уровне сессии.

Чтобы определить свойство действия или сессии

1. Перейти в **Frontend** и выбрать приложение, которое нужно настроить.
2. Выбрать **More** (**…**) > **Edit**.
3. В настройках приложения выбрать **Session and user action properties** и выбрать **Add property**.
4. Выбрать **Expression type** и, при необходимости, **Data type**.

   * Если метаданные были добавлены к запросам и [определены атрибуты запроса](#add-request-attribute), выбрать **Server-side request attribute**.
   * Если [пользовательские значения были переданы через SDK](#report-value-sdk), выбрать **SDK reported value**.
5. Указать **Name** или **Request attribute name**, **Display name** и **Key**.

   | Опция | Пояснение |
   | --- | --- |
   | Name Request attribute name | Для типа значения, переданного через SDK, это имя переданного значения из кода приложения. Поле **Name** учитывает регистр, поэтому оно должно точно совпадать с записью в коде. Для типа атрибута запроса на стороне сервера это имя атрибута запроса, заданного в **Settings** > **Server-side service monitoring** > **Request attributes**. |
   | Display name | Имя свойства, которое используется в веб-интерфейсе Dynatrace, например на странице деталей сессии или странице деталей пользовательского действия. |
   | Key | Имя свойства, которое используется для идентификации и последующего поиска свойства в [USQL](/managed/observe/digital-experience/rum-classic/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Learn how you can access and query user session data based on keywords, syntax, functions, and more."). |
6. Выбрать как минимум один [тип хранения](#storage-levels): свойство действия, свойство сессии или оба.
7. Для типа хранения свойства сессии выбрать один из типов агрегации.
8. Опционально Чтобы ограничить набор захватываемых значений, включить **Apply cleanup rule** и указать [регулярное выражение](/managed/manage/tags-and-metadata/reference/regular-expressions-in-dynatrace "Learn how to use regular expressions in the context of Dynatrace.").

## Примеры свойств действия и сессии

Ниже приведены примеры нескольких свойств действия и сессии, настроенных для примера веб-приложения easyTravel.

Journey ID

Member status

Total purchase amount

Credit card

![Journey ID](https://dt-cdn.net/images/property-journey-id-2136-1e20f89c85.png)

Journey ID

Свойство **Journey ID**, содержащее значение типа данных `long`, добавляется к каждому пользовательскому действию и пользовательской сессии в приложении easyTravel. Для пользовательской сессии сохраняется значение последнего пользовательского действия.

![Свойство Member status](https://dt-cdn.net/images/property-member-status-2136-1665ea176c.png)

Свойство Member status

Свойство **Member status** фиксирует статус членства в программе лояльности для всей сессии. В этом случае отдельные пользовательские действия не важны, поскольку статус лояльности обычно одинаков для всей сессии.

![Свойство Purchase amount](https://dt-cdn.net/images/property-purchase-amount-2136-8a92eff1b1.png)

Свойство Purchase amount

Свойство **Total purchase amount** представляет общую стоимость всех поездок, забронированных через приложение easyTravel. Обратите внимание, что это свойство сессии на самом деле представляет собой сумму значений `purchase_amount` из нескольких пользовательских действий.

![Свойство Credit card type](https://dt-cdn.net/images/property-credit-card-type-2136-8a271f7d47.png)

Свойство Credit card type

**Credit card type**, это пример того, как атрибут запроса на стороне сервера был «продвинут» до свойств действия и сессии.

## Ограничения

* Можно определить не более 200 свойств на приложение.
* Можно определить не более 20 свойств действия на приложение.
* Свойства действия и сессии типа данных `String` ограничены 100 символами после применения правила очистки.
* На приложение можно бесплатно использовать до 20 свойств. Дополнительные свойства расходуют DEM units.
  См. [DEM units](/managed/license/classic-licensing/digital-experience-monitoring-units#dem-units "Understand how Dynatrace Digital Experience Monitoring consumption is calculated based on DEM units.") (обратить внимание на записи **Session property** и **Action property** в таблице) и [Бесплатный уровень свойств действия и сессии](/managed/license/classic-licensing/digital-experience-monitoring-units#free-action-and-session-properties "Understand how Dynatrace Digital Experience Monitoring consumption is calculated based on DEM units.") для получения дополнительной информации.

## Примечания

* Dynatrace начинает собирать свойства действия и сессии только после того, как эти свойства [определены в настройках приложения](#add-properties).
* Можно проверить, сколько свойств уже используется и сколько ещё можно добавить. Перейти в настройки приложения > **Session and user action properties** и прокрутить вниз до **Property usage quotas**.

## Связанные темы

* [Использование свойств пользовательского действия и пользовательской сессии для пользовательских приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/custom-applications/analyze-and-use/action-and-session-properties-custom "User action and session properties, which are metadata key-value pairs, provide added visibility and deeper analysis of your end users' experience. Using these properties for your applications, you can filter user sessions, add calculated metrics, create charts, and more.")
* [Mastering session and user action properties for enhanced analytics﻿](https://www.youtube.com/watch?v=b8Vj0EoaDeM)