---
title: Настройка гибридных приложений в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-hybrid-app
---

# Настройка гибридных приложений в RUM Classic

# Настройка гибридных приложений в RUM Classic

* Практическое руководство
* 4 минуты чтения
* Опубликовано 10 авг. 2021 г.

С Dynatrace можно настроить Real User Monitoring для различных типов гибридных и кроссплатформенных мобильных приложений.

Мобильное приложение можно настроить с помощью одного из плагинов. Однако если используется гибридная платформа, для которой плагины не поддерживаются, или требования не допускают сторонних плагинов, нужно выполнить шаги ниже для настройки гибридного приложения.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Создание гибридного приложения в Dynatrace**](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-hybrid-app#create-app-in-ui "Узнайте, как настроить мониторинг различных типов гибридных и кроссплатформенных мобильных приложений.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Настройка OneAgent и корректировка его конфигурации**](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-hybrid-app#set-up-oneagent "Узнайте, как настроить мониторинг различных типов гибридных и кроссплатформенных мобильных приложений.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Вставка RUM JavaScript в HTML-файлы гибридного приложения**](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-hybrid-app#add-rum-js "Узнайте, как настроить мониторинг различных типов гибридных и кроссплатформенных мобильных приложений.")

Для гибридных приложений нативная часть отслеживается через OneAgent для мобильных приложений, а браузерная часть отслеживается с помощью Dynatrace RUM JavaScript.

Для гибридных приложений сессия пользователя тарифицируется только один раз. Подробнее см. [Digital Experience Monitoring (единицы DEM)](/managed/license/classic-licensing/digital-experience-monitoring-units "Узнайте, как рассчитывается потребление Digital Experience Monitoring Dynatrace на основе единиц DEM.").

Также стоит учитывать, что одна «гибридная» сессия может отображаться в Dynatrace как две отдельные сессии: одна как веб-сессия, другая как мобильная сессия.

## Совместимость агентов

OneAgent для мобильных приложений и RUM JavaScript совместимы друг с другом, если только хотя бы один из них не достиг окончания поддержки (EoS). Чтобы проверить статус поддержки версий, см. [Плановое окончание жизненного цикла неподдерживаемых версий OneAgent](/managed/whats-new/technology/end-of-life-announcements#scheduled-eol-for-unsupported-oneagent-versions "Информация о технологиях, функциях или интеграциях, для которых запланировано окончание жизненного цикла (EOL) в Dynatrace, включая предстоящие и недавно завершившиеся.").

Если версии OneAgent для мобильных приложений и RUM JavaScript находятся в пределах поддерживаемых жизненных циклов, дополнительная проверка совместимости не требуется. Оптимальный подход, поддерживать обе версии обновлёнными до последних. Единственное исключение, когда документация Dynatrace явно указывает на конфликт между конкретными версиями OneAgent для мобильных приложений и RUM JavaScript. В этом случае нужно обратиться к документации за инструкциями по устранению конфликта.

### Требования к совместимости для конкретных функций

Некоторым функциям для корректной работы требуется минимальная версия OneAgent для мобильных приложений или RUM JavaScript. Если используется функция с зависимостью от версии, нужно убедиться, что и OneAgent для мобильных приложений, и RUM JavaScript соответствуют этим минимальным требованиям, даже если обе версии находятся в пределах поддерживаемых жизненных циклов.

Примеры известных требований к версиям для конкретных функций:

* Для использования [функции конфигурации только для iOS﻿](https://www.npmjs.com/package/@dynatrace/cordova-plugin#ios-only-configuration) с плагином Cordova Dynatrace требуется RUM JavaScript версии 1.327 или выше. Помимо минимальной версии, нужно добавить соответствующее свойство в файл `dynatrace.config.js`. Подробности о необходимой конфигурации см. в [документации плагина Cordova﻿](https://www.npmjs.com/package/@dynatrace/cordova-plugin#ios-only-configuration).

## Шаг 1. Создание гибридного приложения в Dynatrace

Первый шаг, создание гибридного приложения, которое состоит из двух частей:

* **Мобильное приложение** получает данные мониторинга из нативной части гибридного приложения. Действия пользователя и сбои из мобильного приложения передаются в это приложение.
* **Веб-приложение** собирает данные из браузерной части гибридного приложения. Действия пользователя из веб-представлений передаются в это веб-приложение.

Для создания приложения в Dynatrace

1. В Dynatrace перейти в раздел **Mobile**.
2. Выбрать **Create mobile app**.
3. Ввести имя приложения и выбрать **Create mobile app**. Откроется страница настроек приложения.
4. На странице настроек приложения выбрать **Instrumentation wizard** > **Cordova**.
5. Выполнить шаги, описанные в мастере настройки. Не забыть выбрать **Monitor the web view** для создания веб-приложения.

   ![Мониторинг веб-представления через мастер Cordova](https://dt-cdn.net/images/monitor-web-view-cordova-wizard-2440-449be51ccc.png)

   Мониторинг веб-представления через мастер Cordova

   Если настраиваемое приложение не является [приложением Cordova](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/apache-cordova "Настройка Dynatrace для мониторинга гибридных мобильных приложений с помощью плагина Cordova."), шаги, связанные с плагином Cordova, нужно пропустить.

## Шаг 2. Настройка OneAgent и корректировка его конфигурации

Для настройки нативной части гибридного приложения используется OneAgent для мобильных приложений. Мобильное приложение, созданное на шаге 1, предлагает мастера настройки для нативной части приложения.

Android

iOS

Для автоматической настройки Android-проекта используется [плагин Android Gradle Dynatrace](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin "Узнайте, как плагин Android Gradle Dynatrace может автоматически настроить мониторинг проекта Android-приложения.").

После этого нужно [скорректировать конфигурацию по умолчанию](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/adjust-oneagent-configuration#hybrid-apps "Узнайте, как настроить плагин Android Gradle Dynatrace для изменения конфигурации SDK OneAgent."), чтобы разрешить OneAgent передавать cookie в WebView и домены, указанные в файле сборки верхнего уровня приложения.

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

Для мониторинга iOS-приложения нужно настроить [OneAgent для iOS](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios "Настройка мониторинга пользовательского опыта для iOS-приложений в Dynatrace.").

После этого нужно использовать [ключи конфигурации `DTXHybridApplication`, `DTXSetCookiesForDomain` и `DTXSetSecureCookiesForDomain`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#hybrid "С помощью ключей конфигурации можно точно настроить автоматическую настройку мониторинга iOS-приложений."), чтобы разрешить OneAgent передавать cookie в `WKWebView` и домены, указанные в файле [`Info.plist`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Файл Info.plist хранит идентификацию приложения и ключи конфигурации. Используйте его для точной настройки конфигурации мониторинга.") приложения.

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

Когда ключ конфигурации `DTXHybridApplication` установлен в `true`, Apple Pay не работает на веб-страницах, загруженных в `WKWebView`.

Для защиты безопасности транзакций в `WKWebView` компания Apple [запрещает использование Apple Pay с API по внедрению скриптов﻿](https://developer.apple.com/documentation/safari-release-notes/safari-13-release-notes#Payment-Request-API), такими как `WKUserScript` или `evaluateJavaScript`. Dynatrace использует `evaluateJavascript` для передачи данных корреляции из нативного слоя в `WKWebView`, и этот процесс отключает Apple Pay.

В качестве обходного решения нужно установить [ключ конфигурации](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys "С помощью ключей конфигурации можно точно настроить автоматическую настройку мониторинга iOS-приложений.") `DTXHybridApplication` в `false`, чтобы остановить внедрение скрипта от OneAgent. Однако это также уберёт корреляцию мобильной и веб-сессий гибридного приложения. Соответствующие мобильная и веб-сессии не будут объединены, что приводит к тарификации двух сессий вместо одной.

Важно добавить необходимые домены в файл сборки верхнего уровня (Android) или в файл [`Info.plist`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Файл Info.plist хранит идентификацию приложения и ключи конфигурации. Используйте его для точной настройки конфигурации мониторинга.") (iOS), чтобы Dynatrace мог идентифицировать мобильные и веб-сессии в приложении и объединять эти сессии в одну «гибридную» сессию.

## Шаг 3. Вставка RUM JavaScript в HTML-источники

Чтобы фиксировать действия пользователя в веб-части гибридного приложения, используется RUM JavaScript. Код или тег JavaScript нужно вручную вставить в HTML-исходники. Дополнительная информация: [Set up agentless Real User Monitoring Classic](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications."). RUM JavaScript доступен в [нескольких форматах](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/snippet-formats "Select a format for the RUM JavaScript snippet that best fits your specific use case").

После добавления RUM JavaScript в HTML-файлы действия пользователя из веб-представлений гибридного приложения передаются в веб-приложение, созданное на шаге 1.

Если веб-часть гибридного приложения уже инструментирована, вручную добавлять RUM JavaScript в HTML-исходники приложения не нужно.

## Related topics

* [Instrument mobile apps with Dynatrace Cordova plugin in RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/apache-cordova "Set up Dynatrace to monitor hybrid mobile apps with the Cordova plugin.")
* [Instrument mobile apps with Dynatrace Flutter plugin in RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/flutter "Learn how to auto-instrument your Flutter applications with OneAgent.")
* [Instrument mobile apps with Dynatrace React Native plugin in RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/react-native "Auto-instrument your React Native applications with OneAgent.")
* [Instrument mobile apps with Dynatrace Xamarin NuGet package in RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/xamarin-nuget "Monitor Xamarin apps with Dynatrace OneAgent.")
* [Instrument mobile apps with Dynatrace .NET MAUI NuGet package in RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/maui "Monitor .NET MAUI applications with Dynatrace OneAgent.")