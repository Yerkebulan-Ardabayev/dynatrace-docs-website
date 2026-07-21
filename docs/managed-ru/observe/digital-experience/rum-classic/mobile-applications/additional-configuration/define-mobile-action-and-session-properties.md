---
title: Определение свойств пользовательских действий и пользовательских сессий для мобильных приложений в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/define-mobile-action-and-session-properties
---

# Определение свойств пользовательских действий и пользовательских сессий для мобильных приложений в RUM Classic

# Определение свойств пользовательских действий и пользовательских сессий для мобильных приложений в RUM Classic

* Практическое руководство
* Чтение 2 мин
* Опубликовано 27 января 2022 г.

Dynatrace собирает много информации о производительности ваших приложений. Эту информацию можно обогатить ценными метаданными, а затем преобразовать метаданные в свойства пользовательских действий и пользовательских сессий.

Свойства действий и сессий, это пары ключ-значение метаданных, которые можно фильтровать во всех представлениях анализа Dynatrace. Эти свойства пригодятся, когда нужно создавать мощные запросы, сегментации или агрегации по собранным метаданным. Эти свойства можно использовать на страницах **User sessions** и **User sessions query**. Подробнее о том, как использовать эти свойства, смотрите в разделе [Использование свойств пользовательских действий и пользовательских сессий для мобильных приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/analyze-and-use/action-and-session-properties-mobile "User action and session properties, which are metadata key-value pairs, provide added visibility and deeper analysis of your end users' experience. Using these properties for your applications, you can filter user sessions, add calculated metrics, create charts, and more.").

Ниже приведена информация о том, как настроить такие свойства, а также соответствующие примеры конфигурации. Чтобы использовать свойства действий и сессий, сначала нужно отправить необходимые метаданные в Dynatrace, а затем [добавить свойства в веб-интерфейсе Dynatrace](#add-properties).

## Отправка метаданных в Dynatrace

Прежде чем определять свойства действий и сессий, сначала нужно начать передачу необходимых метаданных в Dynatrace. Это можно сделать двумя способами:

* [Передать пользовательские значения через SDK](#report-value-sdk)
* [Определить атрибуты запроса](#add-request-attribute)

### Передача значения через SDK

Можно передавать пользовательские значения в исходном коде мобильного приложения через вызов API. Наши нативные SDK и плагины для кроссплатформенных фреймворков предлагают вариант вызова `reportValue` для этого.

[Android](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#report-value) [iOS](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#report-value) [React Native](https://www.npmjs.com/package/@dynatrace/react-native-plugin#report-values) [Flutter](https://pub.dev/packages/dynatrace_flutter_plugin#reportValues) [Xamarin](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/xamarin-nuget#report-values) [![.NET MAUI](https://dt-cdn.net/images/dotnetmaui-aea483621e.svg ".NET MAUI").NET MAUI](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/maui#report-values) 

Чтобы передавать значения для нативной части приложений Cordova, следуйте инструкциям для Android или iOS. Для веб-части используйте [RUM JavaScript API](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/customize-rum "Find out how to customize Real User Monitoring Classic using the JavaScript API.").

Можно передавать значения следующих типов данных:

| Фреймворк | `int` | `long` | `double` | `string` | `date` |
| --- | --- | --- | --- | --- | --- |
| Android | Применимо | Применимо | Применимо | Применимо | Не применимо |
| iOS | Применимо | Не применимо | Применимо | Применимо | Не применимо |
| React Native | Применимо | Не применимо | Применимо | Применимо | Не применимо |
| Flutter | Применимо | Не применимо | Применимо | Применимо | Не применимо |
| Xamarin | Применимо | Не применимо | Применимо | Применимо | Не применимо |
| .NET MAUI | Применимо | Не применимо | Применимо | Применимо | Не применимо |
| Cordova (веб-часть)RUM JavaScript API | Не применимо | Применимо | Применимо | Применимо | Применимо |

Чтобы проверить, доходят ли данные, которые передаются в коде приложения, до Dynatrace, перейдите к деталям пользовательского действия, которое должно содержать эти данные, и прокрутите вниз до раздела **Reported values**.

![Страница деталей пользовательского действия со значениями, переданными через SDK](https://dt-cdn.net/images/user-action-details-with-reported-values-2048-b44e8bca3e.png)

Страница деталей пользовательского действия со значениями, переданными через SDK

### Определение атрибута запроса

Кроме того, можно добавить необходимые метаданные в серверные запросы, определить атрибуты запроса, а затем использовать эти атрибуты для создания свойств действий и сессий.

Атрибуты запроса извлекаются из URL веб-запросов, заголовков HTTP-запросов и других метаданных запроса. Эти атрибуты представляют собой пары ключ-значение, которые можно фильтровать во многих представлениях анализа Dynatrace и распределённой трассировки.

Подробнее смотрите в разделе [Атрибуты запроса](/managed/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.").

## Добавление свойств действий и сессий

После того, как значения переданы через код приложения или определены атрибуты запроса, информация, которую собирает Dynatrace, обогащается ценными метаданными. Эти метаданные можно «продвинуть» до свойств действий и сессий в настройках приложения.

Метаданные можно сохранять на разных «уровнях хранения»:

* **User action property**: данные сохраняются в определённом свойстве на уровне пользовательского действия для каждого пользовательского действия, для которого Dynatrace может получить метаданные.
* **User session property**: последнее собранное значение сохраняется в определённом свойстве на уровне сессии.
* **Both options**: данные сохраняются в определённом свойстве как на уровне пользовательского действия, так и на уровне сессии.

Чтобы определить свойство действия или сессии

1. Перейдите в **Frontend** и выберите приложение, которое нужно настроить.
2. Выберите **More** (**…**) > **Edit**.
3. В настройках приложения выберите **Session and user action properties** и нажмите **Add property**.
4. Выберите **Expression type** и, при необходимости, **Data type**.

   * Если метаданные были добавлены в запросы и [определены атрибуты запроса](#add-request-attribute), выберите **Server-side request attribute**.
   * Если [пользовательские значения были переданы через SDK](#report-value-sdk), выберите **SDK reported value**.
5. Укажите **Name** или **Request attribute name**, **Display name** и **Key**.

   | Параметр | Пояснение |
   | --- | --- |
   | Name Request attribute name | Для типа значения, переданного через SDK, это имя переданного значения из кода приложения. Поле **Name** чувствительно к регистру, поэтому оно должно точно совпадать с записью в коде. Для типа атрибута серверного запроса это имя атрибута запроса, заданного в **Settings** > **Server-side service monitoring** > **Request attributes**. |
   | Display name | Имя свойства, которое используется в веб-интерфейсе Dynatrace, например, на странице деталей сессии или странице деталей пользовательского действия. |
   | Key | Имя свойства, которое используется для идентификации и последующего поиска свойства в [USQL](/managed/observe/digital-experience/rum-classic/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Learn how you can access and query user session data based on keywords, syntax, functions, and more."). |
6. Выберите как минимум один [тип хранения](#storage-levels): свойство пользовательского действия, свойство сессии или оба.
7. Для типа хранения «свойство сессии» выберите один из типов агрегации.
8. Необязательно Чтобы ограничить собираемые значения, включите **Apply cleanup rule** и укажите [регулярное выражение](/managed/manage/tags-and-metadata/reference/regular-expressions-in-dynatrace "Learn how to use regular expressions in the context of Dynatrace.").

## Примеры свойств действий и сессий

Ниже приведены примеры нескольких свойств действий и сессий, которые настроены для нашего демонстрационного веб-приложения easyTravel.

Journey ID

Member status

Total purchase amount

Credit card

![Journey ID](https://dt-cdn.net/images/property-journey-id-2136-1e20f89c85.png)

Journey ID

Свойство **Journey ID**, содержащее значение типа данных `long`, добавляется к каждому пользовательскому действию и пользовательской сессии в приложении easyTravel. Для пользовательской сессии сохраняется значение последнего пользовательского действия.

![Свойство Member status](https://dt-cdn.net/images/property-member-status-2136-1665ea176c.png)

Свойство Member status

Свойство **Member status** отражает статус участия в программе лояльности для всей сессии. В данном случае отдельные пользовательские действия не важны, поскольку статус лояльности обычно одинаков для всей сессии.

![Свойство Purchase amount](https://dt-cdn.net/images/property-purchase-amount-2136-8a92eff1b1.png)

Свойство Purchase amount

Свойство **Total purchase amount** представляет общую стоимость всех поездок, забронированных через приложение easyTravel. Обратите внимание, что это свойство сессии на самом деле представляет собой сумму значений `purchase_amount` из нескольких пользовательских действий.

![Свойство Credit card type](https://dt-cdn.net/images/property-credit-card-type-2136-8a271f7d47.png)

Свойство Credit card type

**Credit card type**, это пример того, как атрибут серверного запроса был «продвинут» до свойств действий и сессий.

## Ограничения

* Максимум можно определить 200 свойств на приложение.
* Максимум можно определить 20 свойств действий на приложение.
* Свойства действий и сессий с типом данных `String` ограничены 100 символами после применения правила очистки.
* Можно использовать до 20 свойств на приложение бесплатно. Дополнительные свойства расходуют DEM units.
  Подробнее см. [DEM units](/managed/license/classic-licensing/digital-experience-monitoring-units#dem-units "Understand how Dynatrace Digital Experience Monitoring consumption is calculated based on DEM units.") (обратить внимание на записи **Session property** и **Action property** в таблице) и [Free tier of action and session properties](/managed/license/classic-licensing/digital-experience-monitoring-units#free-action-and-session-properties "Understand how Dynatrace Digital Experience Monitoring consumption is calculated based on DEM units.").

## Примечания

* Dynatrace начинает захватывать свойства действий и сессий только после того, как эти свойства [определены в настройках приложения](#add-properties).
* Можно проверить, сколько свойств уже используется и сколько ещё можно добавить. Перейти в настройки приложения > **Session and user action properties** и прокрутить вниз до **Property usage quotas**.

## Связанные темы

* [Leverage user action and user session properties for mobile applications in RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/analyze-and-use/action-and-session-properties-mobile "User action and session properties, which are metadata key-value pairs, provide added visibility and deeper analysis of your end users' experience. Using these properties for your applications, you can filter user sessions, add calculated metrics, create charts, and more.")
* [Mastering session and user action properties for enhanced analytics﻿](https://www.youtube.com/watch?v=b8Vj0EoaDeM)