---
title: Инструментирование гибридных приложений
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/instrument-hybrid-app
scraped: 2026-05-12T11:32:34.210602
---

# Инструментирование гибридных приложений

# Инструментирование гибридных приложений

* How-to guide
* 4-min read
* Published Aug 10, 2021

С помощью Dynatrace можно настроить Real User Monitoring для различных типов гибридных и кроссплатформенных мобильных приложений.

Вы можете инструментировать мобильное приложение с помощью одного из наших плагинов. Однако, если вы используете гибридную платформу, не поддерживающую наши плагины, или ваши требования исключают применение сторонних плагинов, выполните приведённые ниже шаги для инструментирования гибридного приложения.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Создайте гибридное приложение в Dynatrace**](/managed/observe/digital-experience/mobile-applications/instrument-hybrid-app#create-app-in-ui "Узнайте, как инструментировать различные типы гибридных и кроссплатформенных мобильных приложений.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Настройте OneAgent и его конфигурацию**](/managed/observe/digital-experience/mobile-applications/instrument-hybrid-app#set-up-oneagent "Узнайте, как инструментировать различные типы гибридных и кроссплатформенных мобильных приложений.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Вставьте RUM JavaScript в HTML-файлы гибридного приложения**](/managed/observe/digital-experience/mobile-applications/instrument-hybrid-app#add-rum-js "Узнайте, как инструментировать различные типы гибридных и кроссплатформенных мобильных приложений.")

Для гибридных приложений нативная часть отслеживается через OneAgent для мобильных устройств, а браузерная часть — через Dynatrace RUM JavaScript.

Для гибридных приложений пользовательская сессия тарифицируется только один раз. Подробнее см. в разделе [Digital Experience Monitoring (единицы DEM)](/managed/license/monitoring-consumption-classic/digital-experience-monitoring-units "Узнайте, как рассчитывается потребление Dynatrace Digital Experience Monitoring на основе единиц DEM.").

Также обратите внимание, что одна «гибридная» сессия может отображаться в Dynatrace как две отдельных сессии: одна — как веб-сессия, другая — как мобильная сессия.

## Совместимость агентов

OneAgent для мобильных устройств и RUM JavaScript совместимы между собой, если хотя бы один из них не достиг конца поддержки (EoS). Для проверки статуса поддержки версий обратитесь к разделу [Запланированное прекращение поддержки версий OneAgent](/managed/whats-new/technology/end-of-life-announcements#scheduled-eol-for-unsupported-oneagent-versions "Информация о технологиях, функциях или интеграциях, запланированных для прекращения поддержки в Dynatrace, включая предстоящие и недавно выведенные из эксплуатации элементы.").

Если версии OneAgent для мобильных устройств и RUM JavaScript находятся в пределах поддерживаемого жизненного цикла, дополнительная проверка совместимости не требуется. Оптимальный подход — поддерживать обоих в актуальном состоянии. Единственное исключение — когда документация Dynatrace явно указывает на конфликт между конкретными версиями OneAgent для мобильных устройств и RUM JavaScript. В этом случае для устранения конфликта обратитесь к документации.

### Требования к совместимости для конкретных функций

Некоторые функции требуют минимальной версии OneAgent для мобильных устройств или RUM JavaScript для корректной работы. Если вы используете функцию, зависящую от версии, необходимо убедиться, что оба компонента — OneAgent для мобильных устройств и RUM JavaScript — соответствуют минимальным требованиям, даже если оба находятся в пределах поддерживаемого жизненного цикла.

Примеры известных требований к версиям для конкретных функций:

* Для использования [функции конфигурации только для iOS](https://www.npmjs.com/package/@dynatrace/cordova-plugin#ios-only-configuration) с плагином Dynatrace Cordova требуется RUM JavaScript версии 1.327 или выше. Помимо минимальной версии, необходимо добавить соответствующее свойство в файл `dynatrace.config.js`. Сведения о требуемой конфигурации см. в [документации плагина Cordova](https://www.npmjs.com/package/@dynatrace/cordova-plugin#ios-only-configuration).

## Шаг 1 Создание гибридного приложения в Dynatrace

Первый шаг — создание гибридного приложения, состоящего из двух частей:

* **Мобильное приложение** получает данные мониторинга из нативной части гибридного приложения. Пользовательские действия и сбои из мобильного приложения передаются в это приложение.
* **Веб-приложение** собирает данные из браузерной части гибридного приложения. Пользовательские действия из веб-представлений передаются в это веб-приложение.

Чтобы создать приложение в Dynatrace:

1. В Dynatrace перейдите в раздел **Mobile**.
2. Выберите **Create mobile app**.
3. Введите имя приложения и нажмите **Create mobile app**. Откроется страница параметров приложения.
4. В параметрах приложения выберите **Instrumentation wizard** > **Cordova**.
5. Выполните шаги, описанные в мастере. Не забудьте выбрать **Monitor the web view** для создания веб-приложения.

   ![Monitor web view via Cordova wizard](https://dt-cdn.net/images/monitor-web-view-cordova-wizard-2440-449be51ccc.png)

   Мониторинг веб-представления через мастер Cordova

   Если инструментируемое приложение не является [приложением Cordova](/managed/observe/digital-experience/mobile-applications/cross-platform-frameworks/apache-cordova "Настройте Dynatrace для мониторинга гибридных мобильных приложений с помощью плагина Cordova."), пропустите шаги, связанные с плагином Cordova.

## Шаг 2 Настройка OneAgent и его конфигурации

Для инструментирования нативной части гибридного приложения используйте OneAgent для мобильных устройств. Мобильное приложение, созданное на шаге 1, предоставляет мастера инструментирования для нативной части приложения.

Android

iOS

Для автоинструментирования Android-проекта используйте [плагин Dynatrace Android Gradle](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin "Узнайте, как плагин Dynatrace Android Gradle может автоматически инструментировать Android-проект приложения.").

После этого [настройте конфигурацию по умолчанию](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/adjust-oneagent-configuration#hybrid-apps "Узнайте, как настроить плагин Dynatrace Android Gradle для изменения конфигурации OneAgent SDK."), чтобы разрешить OneAgent передавать cookie в WebView и домены, указанные в файле сборки верхнего уровня приложения.

Пример конфигурации для домена `easytravel.com`:

```
dynatrace {



configurations {



sampleConfig {



hybridWebView {



enabled true



domains '.easytravel.com'



}



}



}



}
```

Для мониторинга iOS-приложения необходимо инструментировать [OneAgent для iOS](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios "Настройте мониторинг пользовательского опыта для iOS-приложений в Dynatrace.").

После этого используйте [ключи конфигурации `DTXHybridApplication`, `DTXSetCookiesForDomain` и `DTXSetSecureCookiesForDomain`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#hybrid "С помощью ключей конфигурации можно выполнить тонкую настройку автоинструментирования iOS-приложений."), чтобы разрешить OneAgent передавать cookie в `WKWebView` и домены, указанные в файле [`Info.plist`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Файл Info.plist хранит идентификационные и конфигурационные ключи приложения. Используйте его для точной настройки конфигурации инструментирования.") вашего приложения.

Пример конфигурации для домена `easytravel.com`:

```
<key>DTXHybridApplication</key>



<true/>



<key>DTXSetCookiesForDomain</key>



<array>



<string>.easytravel.com</string>



</array>



<key>DTXSetSecureCookiesForDomain</key>



<array>



<string>.example.com</string>



</array>
```

Apple Pay не работает в WKWebView

Если ключ конфигурации `DTXHybridApplication` установлен в значение `true`, Apple Pay не работает на веб-страницах, загруженных в `WKWebView`.

Для защиты безопасности транзакций в `WKWebView` Apple [запрещает использование Apple Pay с API внедрения скриптов](https://developer.apple.com/documentation/safari-release-notes/safari-13-release-notes#Payment-Request-API), такими как `WKUserScript` или `evaluateJavaScript`. Dynatrace использует `evaluateJavascript` для передачи корреляционных данных из нативного слоя в `WKWebView`, и этот процесс отключает Apple Pay.

В качестве обходного решения установите ключ конфигурации `DTXHybridApplication` в значение `false`, чтобы остановить внедрение скрипта из OneAgent. Однако это также отключит корреляцию мобильных и веб-сессий для гибридного приложения. Соответствующие мобильные и веб-сессии не будут объединены, что приведёт к тарификации двух сессий вместо одной.

Важно добавить необходимые домены в файл сборки верхнего уровня (Android) или в файл [`Info.plist`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Файл Info.plist хранит идентификационные и конфигурационные ключи приложения. Используйте его для точной настройки конфигурации инструментирования.") (iOS), чтобы Dynatrace мог идентифицировать мобильные и веб-сессии в приложении и объединять их в одну «гибридную» сессию.

## Шаг 3 Вставка RUM JavaScript в HTML-источники

Для записи пользовательских действий в браузерной части гибридного приложения используйте RUM JavaScript. Необходимо вручную вставить код или тег JavaScript в HTML-источники. Подробнее см. в разделе [Настройка агентлесс-мониторинга Real User Monitoring](/managed/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Настройте агентлесс-мониторинг для веб-приложений."). Обратите внимание, что RUM JavaScript доступен в [нескольких форматах](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats "Выберите формат фрагмента RUM JavaScript, наиболее подходящий для вашего конкретного случая использования.").

После добавления RUM JavaScript в HTML-файлы пользовательские действия из веб-представлений гибридного приложения будут передаваться в веб-приложение, созданное на шаге 1.

Если вы уже инструментировали браузерную часть гибридного приложения, вручную добавлять RUM JavaScript в HTML-источники приложения не требуется.

## Связанные темы

* [Инструментирование мобильных приложений с помощью плагина Dynatrace Cordova](/managed/observe/digital-experience/mobile-applications/cross-platform-frameworks/apache-cordova "Настройте Dynatrace для мониторинга гибридных мобильных приложений с помощью плагина Cordova.")
* [Инструментирование мобильных приложений с помощью плагина Dynatrace Flutter](/managed/observe/digital-experience/mobile-applications/cross-platform-frameworks/flutter "Узнайте, как автоматически инструментировать Flutter-приложения с помощью OneAgent.")
* [Инструментирование мобильных приложений с помощью плагина Dynatrace React Native](/managed/observe/digital-experience/mobile-applications/cross-platform-frameworks/react-native "Автоматически инструментируйте React Native-приложения с помощью OneAgent.")
* [Инструментирование мобильных приложений с помощью пакета Dynatrace Xamarin NuGet](/managed/observe/digital-experience/mobile-applications/cross-platform-frameworks/xamarin-nuget "Выполняйте мониторинг Xamarin-приложений с помощью Dynatrace OneAgent.")
* [Инструментирование мобильных приложений с помощью пакета Dynatrace .NET MAUI NuGet](/managed/observe/digital-experience/mobile-applications/cross-platform-frameworks/maui "Выполняйте мониторинг .NET MAUI-приложений с помощью Dynatrace OneAgent.")