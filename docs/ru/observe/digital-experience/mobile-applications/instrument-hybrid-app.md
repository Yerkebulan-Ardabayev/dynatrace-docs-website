---
title: Instrument hybrid apps
source: https://www.dynatrace.com/docs/observe/digital-experience/mobile-applications/instrument-hybrid-app
scraped: 2026-03-04T21:32:53.595693
---

# Инструментирование гибридных приложений

# Инструментирование гибридных приложений

* Classic
* How-to guide
* 4-min read
* Published Aug 10, 2021

С помощью Dynatrace вы можете настроить Real User Monitoring для различных типов гибридных и кросс-платформенных мобильных приложений.

Вы можете инструментировать ваше мобильное приложение с помощью одного из наших плагинов. Однако если вы используете гибридную платформу, которая не поддерживает наши плагины, или ваши требования запрещают использование сторонних плагинов, выполните следующие шаги для инструментирования вашего гибридного приложения.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Создание гибридного приложения в Dynatrace**](instrument-hybrid-app.md#create-app-in-ui "Learn how you can instrument various types of hybrid and cross-platform mobile apps.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Настройка OneAgent и его конфигурации**](instrument-hybrid-app.md#set-up-oneagent "Learn how you can instrument various types of hybrid and cross-platform mobile apps.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Вставка RUM JavaScript в HTML-файлы гибридного приложения**](instrument-hybrid-app.md#add-rum-js "Learn how you can instrument various types of hybrid and cross-platform mobile apps.")

Для гибридных приложений нативная часть мониторится через OneAgent for Mobile, а браузерная часть наблюдается с помощью Dynatrace RUM JavaScript.

Для гибридных приложений пользовательская сессия тарифицируется только один раз. Подробности см. в разделе [Digital Experience Monitoring (DEM units)](../../../license/monitoring-consumption-classic/digital-experience-monitoring-units.md "Understand how Dynatrace Digital Experience Monitoring consumption is calculated based on DEM units.").

Также обратите внимание, что одна "гибридная" сессия может отображаться в Dynatrace как две отдельные сессии: одна как веб-сессия, а другая как мобильная сессия.

## Шаг 1 Создание гибридного приложения в Dynatrace

Первый шаг -- создание гибридного приложения, состоящего из двух частей:

* **Мобильное приложение** получает данные мониторинга от нативной части гибридного приложения. Действия пользователя и сбои мобильного приложения отправляются в это приложение.
* **Веб-приложение** захватывает данные из браузерной части гибридного приложения. Действия пользователя из веб-представлений отправляются в это веб-приложение.

Чтобы создать приложение в Dynatrace

1. В Dynatrace перейдите в **Mobile**.
2. Нажмите **Create mobile app**.
3. Введите имя для вашего приложения и нажмите **Create mobile app**. Откроется страница настроек приложения.
4. В настройках приложения выберите **Instrumentation wizard** > **Cordova**.
5. Следуйте шагам, описанным в мастере. Не забудьте выбрать **Monitor the web view** для создания веб-приложения.

   ![Monitor web view via Cordova wizard](https://dt-cdn.net/images/monitor-web-view-cordova-wizard-2440-449be51ccc.png)

   Если инструментируемое приложение не является [приложением Cordova](cross-platform-frameworks/apache-cordova.md "Set up Dynatrace to monitor hybrid mobile apps with the Cordova plugin."), пропустите шаги, связанные с плагином Cordova.

## Шаг 2 Настройка OneAgent и его конфигурации

Используйте OneAgent for Mobile для инструментирования нативной части вашего гибридного приложения. Мобильное приложение, которое вы создали на шаге 1, предоставляет мастера инструментирования для нативной части вашего приложения.

Android

iOS

Для автоматического инструментирования вашего Android-проекта используйте [плагин Dynatrace Android Gradle](instrument-android-app/instrumentation-via-plugin.md "Learn how the Dynatrace Android Gradle plugin can auto-instrument your Android application project.").

После этого [настройте конфигурацию по умолчанию](instrument-android-app/instrumentation-via-plugin/adjust-oneagent-configuration.md#hybrid-apps "Learn how to configure the Dynatrace Android Gradle plugin to modify the OneAgent SDK configuration."), чтобы OneAgent мог передавать cookies в WebView и домены, указанные в файле сборки верхнего уровня вашего приложения.

Ниже приведён пример конфигурации для домена `easytravel.com`:

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

Для мониторинга вашего iOS-приложения необходимо инструментировать [OneAgent for iOS](instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios.md "Set up user experience monitoring for iOS apps within Dynatrace.").

После этого используйте [ключи конфигурации `DTXHybridApplication`, `DTXSetCookiesForDomain` и `DTXSetSecureCookiesForDomain`](instrument-ios-app/customization/ios-configuration-keys.md#hybrid "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps."), чтобы OneAgent мог передавать cookies в `WKWebView` и домены, указанные в файле [`Info.plist`](instrument-ios-app/instrumentation/info-plist-file.md "Info.plist file stores your app identification and configuration keys. Use it to fine-tune the instrumentation configuration.") вашего приложения.

Ниже приведён пример конфигурации для домена `easytravel.com`:

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

Когда ключ конфигурации `DTXHybridApplication` установлен в `true`, Apple Pay не работает на веб-страницах, загруженных в `WKWebView`.

Для защиты безопасности транзакций в `WKWebView` Apple [запрещает использование Apple Pay с API инъекции скриптов](https://developer.apple.com/documentation/safari-release-notes/safari-13-release-notes#Payment-Request-API), такими как `WKUserScript` или `evaluateJavaScript`. Dynatrace использует `evaluateJavascript` для передачи корреляционных данных из нативного слоя в `WKWebView`, и этот процесс отключает Apple Pay.

В качестве обходного решения установите ключ конфигурации `DTXHybridApplication` [configuration key](instrument-ios-app/customization/ios-configuration-keys.md "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") в `false`, чтобы прекратить инъекцию скрипта из OneAgent. Однако это также удалит корреляцию мобильных и веб-сессий для вашего гибридного приложения. Соответствующие мобильные и веб-сессии не будут объединены, что приведёт к тарификации двух сессий вместо одной.

Важно добавить необходимые домены в файл сборки верхнего уровня (Android) или [файл `Info.plist`](instrument-ios-app/instrumentation/info-plist-file.md "Info.plist file stores your app identification and configuration keys. Use it to fine-tune the instrumentation configuration.") (iOS), чтобы Dynatrace мог идентифицировать мобильные и веб-сессии в вашем приложении и объединять эти сессии в одну "гибридную" сессию.

## Шаг 3 Вставка RUM JavaScript в HTML-источники

Для захвата действий пользователя в веб-части вашего гибридного приложения используйте RUM JavaScript. Вам необходимо вручную вставить JavaScript-код или тег в ваши HTML-источники. Подробности см. в разделе [Настройка безагентного Real User Monitoring](../web-applications/initial-setup/set-up-agentless-real-user-monitoring.md "Set up agentless monitoring for your web applications."). Обратите внимание, что RUM JavaScript доступен в [нескольких форматах](../web-applications/initial-setup/snippet-formats.md "Select a format for the RUM JavaScript snippet that best fits your specific use case").

После добавления RUM JavaScript в HTML-файлы действия пользователя из веб-представлений вашего гибридного приложения отправляются в веб-приложение, которое вы создали на шаге 1.

Если вы уже инструментировали веб-часть вашего гибридного приложения, вам не нужно вручную добавлять RUM JavaScript в HTML-источники вашего приложения.

## Связанные темы

* [Инструментирование мобильных приложений с помощью плагина Dynatrace Cordova](cross-platform-frameworks/apache-cordova.md "Set up Dynatrace to monitor hybrid mobile apps with the Cordova plugin.")
* [Инструментирование мобильных приложений с помощью плагина Dynatrace Flutter](cross-platform-frameworks/flutter.md "Learn how to auto-instrument your Flutter applications with OneAgent.")
* [Инструментирование мобильных приложений с помощью плагина Dynatrace React Native](cross-platform-frameworks/react-native.md "Auto-instrument your React Native applications with OneAgent.")
* [Инструментирование мобильных приложений с помощью пакета Dynatrace Xamarin NuGet](cross-platform-frameworks/xamarin-nuget.md "Monitor Xamarin apps with Dynatrace OneAgent.")
