---
title: Определение свойств пользовательских действий и сессий для мобильных приложений
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/additional-configuration/define-mobile-action-and-session-properties
scraped: 2026-05-12T11:33:09.937045
---

# Определение свойств пользовательских действий и сессий для мобильных приложений

# Определение свойств пользовательских действий и сессий для мобильных приложений

* How-to guide
* 2-min read
* Published Jan 27, 2022

Dynatrace собирает большой объём информации о производительности ваших приложений. Вы можете дополнить эту информацию ценными метаданными, а затем преобразовать их в свойства пользовательских действий и сессий.

Свойства действий и сессий — это пары ключ-значение метаданных, по которым можно фильтровать данные в представлениях анализа Dynatrace. Эти свойства удобны, когда требуется создавать мощные запросы, сегментации или агрегации захваченных метаданных. Вы можете использовать их на страницах **User sessions** и **User sessions query**. Для более глубокого понимания применения этих свойств см. раздел [Использование свойств пользовательских действий и сессий для мобильных приложений](/managed/observe/digital-experience/mobile-applications/analyze-and-use/action-and-session-properties-mobile "Свойства пользовательских действий и сессий — пары ключ-значение метаданных, обеспечивающие дополнительную видимость и более глубокий анализ опыта конечных пользователей. Используя эти свойства, вы можете фильтровать сессии, добавлять вычисленные метрики, создавать графики и многое другое.").

Ниже вы найдёте информацию о настройке таких свойств, а также соответствующие примеры конфигурации. Чтобы использовать свойства действий и сессий, сначала необходимо отправить нужные метаданные в Dynatrace, а затем [добавить свойства в веб-интерфейсе Dynatrace](#add-properties).

## Отправка метаданных в Dynatrace

Прежде чем определять свойства действий и сессий, необходимо начать передачу нужных метаданных в Dynatrace. Это можно сделать двумя способами:

* [Передача пользовательских значений через SDK](#report-value-sdk)
* [Определение атрибутов запросов](#add-request-attribute)

### Передача значений через SDK

Вы можете передавать пользовательские значения в исходном коде мобильного приложения через вызов API. Наши нативные SDK и плагины для кроссплатформенных фреймворков предлагают вариант вызова `reportValue` для этой цели.

[Android](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#report-value) [iOS](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#report-value) [React Native](https://www.npmjs.com/package/@dynatrace/react-native-plugin#report-values) [Flutter](https://pub.dev/packages/dynatrace_flutter_plugin#reportValues) [Xamarin](/managed/observe/digital-experience/mobile-applications/cross-platform-frameworks/xamarin-nuget#report-values) [![.NET MAUI](https://dt-cdn.net/images/dotnetmaui-aea483621e.svg ".NET MAUI").NET MAUI](/managed/observe/digital-experience/mobile-applications/cross-platform-frameworks/maui#report-values) 

Для передачи значений нативной части приложений Cordova следуйте инструкциям для Android или iOS. Для веб-части используйте [RUM JavaScript API](/managed/observe/digital-experience/web-applications/additional-configuration/customize-rum "Узнайте, как настроить Real User Monitoring с помощью JavaScript API.").

Вы можете передавать значения следующих типов данных:

| Фреймворк | `int` | `long` | `double` | `string` | `date` |
| --- | --- | --- | --- | --- | --- |
| Android | Применимо | Применимо | Применимо | Применимо | Не применимо |
| iOS | Применимо | Не применимо | Применимо | Применимо | Не применимо |
| React Native | Применимо | Не применимо | Применимо | Применимо | Не применимо |
| Flutter | Применимо | Не применимо | Применимо | Применимо | Не применимо |
| Xamarin | Применимо | Не применимо | Применимо | Применимо | Не применимо |
| .NET MAUI | Применимо | Не применимо | Применимо | Применимо | Не применимо |
| Cordova (веб-часть) RUM JavaScript API | Не применимо | Применимо | Применимо | Применимо | Применимо |

Чтобы проверить, достигают ли данные, передаваемые в коде приложения, Dynatrace, перейдите в сведения о пользовательском действии, которое должно содержать данные, и прокрутите вниз до раздела **Reported values**.

![User action details page with SDK-reported values](https://dt-cdn.net/images/user-action-details-with-reported-values-2048-b44e8bca3e.png)

User action details page with SDK-reported values

### Определение атрибута запроса

Кроме того, вы можете добавить нужные метаданные к серверным запросам, определить атрибуты запросов и затем использовать их для создания свойств действий и сессий.

Атрибуты запросов извлекаются из URL-адресов веб-запросов, HTTP-заголовков запросов и других метаданных запросов. Эти атрибуты представляют собой пары ключ-значение, по которым можно фильтровать данные во многих представлениях анализа и распределённой трассировки Dynatrace.

Подробнее см. в разделе [Атрибуты запросов](/managed/observe/application-observability/services/request-attributes "Узнайте, что такое атрибуты запросов и как использовать их на всех уровнях представлений анализа сервисов.").

## Добавление свойств действий и сессий

После того как вы передали значения через код приложения или определили атрибуты запросов, информация, захватываемая Dynatrace, обогащается ценными метаданными. Вы можете «повысить» эти метаданные до свойств действий и сессий в настройках приложения.

Метаданные можно сохранять на разных «уровнях хранения»:

* **Свойство пользовательского действия**: данные сохраняются в определённом свойстве на уровне пользовательского действия для каждого действия, из которого Dynatrace может извлечь метаданные.
* **Свойство пользовательской сессии**: последнее захваченное значение сохраняется в определённом свойстве на уровне сессии.
* **Оба варианта**: данные сохраняются в определённом свойстве как на уровне действия, так и на уровне сессии.

Чтобы определить свойство действия или сессии:

1. Перейдите в **Frontend** и выберите приложение, которое нужно настроить.
2. Нажмите **More** (**…**) > **Edit**.
3. В настройках приложения выберите **Session and user action properties** и нажмите **Add property**.
4. Выберите **Expression type** и при необходимости **Data type**.

   * Если вы добавили метаданные к запросам и [определили атрибуты запросов](#add-request-attribute), выберите **Server-side request attribute**.
   * Если вы [передавали пользовательские значения через SDK](#report-value-sdk), выберите **SDK reported value**.
5. Укажите **Name** или **Request attribute name**, **Display name** и **Key**.

   | Параметр | Пояснение |
   | --- | --- |
   | Name / Request attribute name | Для типа значения SDK — это имя передаваемого значения из кода приложения. **Name** учитывает регистр и должно точно совпадать с записью в коде. Для типа атрибута серверного запроса — это имя атрибута запроса, заданного в **Settings** > **Server-side service monitoring** > **Request attributes**. |
   | Display name | Имя свойства, используемое в веб-интерфейсе Dynatrace, например на странице сведений о сессии или пользовательском действии. |
   | Key | Имя свойства для идентификации и последующего поиска в [USQL](/managed/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Узнайте, как получать доступ к данным пользовательских сессий и запрашивать их."). |
6. Выберите хотя бы один [тип хранения](#storage-levels): свойство пользовательского действия, свойство сессии или оба.
7. Для типа хранения свойства сессии выберите один из типов агрегации.
8. Необязательно: чтобы ограничить захватываемые значения, включите **Apply cleanup rule** и укажите [регулярное выражение](/managed/manage/tags-and-metadata/reference/regular-expressions-in-dynatrace "Узнайте, как использовать регулярные выражения в контексте Dynatrace.").

## Примеры свойств действий и сессий

Ниже приведены примеры нескольких свойств действий и сессий, настроенных для нашего образца веб-приложения easyTravel.

Journey ID

Member status

Total purchase amount

Credit card

![Journey ID](https://dt-cdn.net/images/property-journey-id-2136-1e20f89c85.png)

Journey ID

Свойство **Journey ID**, содержащее значение типа `long`, добавляется к каждому пользовательскому действию и сессии в приложении easyTravel. Для пользовательской сессии сохраняется значение последнего пользовательского действия.

![Member status property](https://dt-cdn.net/images/property-member-status-2136-1665ea176c.png)

Member status property

Свойство **Member status** захватывает статус участия в программе лояльности для всей сессии. В данном случае нас не интересуют отдельные действия, так как статус лояльности обычно не меняется в течение сессии.

![Purchase amount property](https://dt-cdn.net/images/property-purchase-amount-2136-8a92eff1b1.png)

Purchase amount property

Свойство **Total purchase amount** представляет общую стоимость всех поездок, забронированных через наше приложение easyTravel. Обратите внимание, что это свойство сессии фактически является суммой значений `purchase_amount` из нескольких пользовательских действий.

![Credit card type property](https://dt-cdn.net/images/property-credit-card-type-2136-8a271f7d47.png)

Credit card type property

**Credit card type** — пример того, как атрибут серверного запроса «повышается» до свойств действия и сессии.

## Ограничения

* Для одного приложения можно определить не более 200 свойств.
* Для одного приложения можно определить не более 20 свойств действий.
* Свойства действий и сессий типа `String` ограничены 100 символами после применения правила очистки.
* Бесплатно можно использовать до 20 свойств на приложение. Дополнительные свойства потребляют единицы DEM.
  Подробнее см. в разделах [DEM units](/managed/license/monitoring-consumption-classic/digital-experience-monitoring-units#dem-units "Узнайте, как рассчитывается потребление Dynatrace Digital Experience Monitoring на основе единиц DEM.") (обратите внимание на записи **Session property** и **Action property** в таблице) и [Бесплатный уровень свойств действий и сессий](/managed/license/monitoring-consumption-classic/digital-experience-monitoring-units#free-action-and-session-properties "Узнайте, как рассчитывается потребление Dynatrace Digital Experience Monitoring на основе единиц DEM.").

## Примечания

* Dynatrace начинает захватывать свойства действий и сессий только после того, как вы [определите эти свойства в настройках приложения](#add-properties).
* Вы можете проверить, сколько свойств уже используется и сколько ещё можно добавить. Перейдите в настройки приложения > **Session and user action properties** и прокрутите вниз до раздела **Property usage quotas**.

## Связанные темы

* [Использование свойств пользовательских действий и сессий для мобильных приложений](/managed/observe/digital-experience/mobile-applications/analyze-and-use/action-and-session-properties-mobile "Свойства пользовательских действий и сессий — пары ключ-значение метаданных, обеспечивающие дополнительную видимость и более глубокий анализ опыта конечных пользователей.")
* [Mastering session and user action properties for enhanced analytics](https://www.youtube.com/watch?v=b8Vj0EoaDeM)