---
title: OneAgent для функций автоматической инструментации iOS в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features
---

# OneAgent для функций автоматической инструментации iOS в RUM Classic

# OneAgent для функций автоматической инструментации iOS в RUM Classic

* Разъяснение
* Чтение: 4 мин
* Обновлено 03 февраля 2026 г.

Автоматическая инструментация с помощью OneAgent для iOS происходит во время выполнения. Полученное приложение инструментируется до уровней, настроенных в [файле `Info.plist`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Файл Info.plist хранит идентификационные и конфигурационные ключи приложения. Используй его для точной настройки конфигурации инструментации.") приложения.

Следующие функции инструментируются автоматически при [настройке OneAgent](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios "Настрой мониторинг пользовательского опыта для iOS-приложений в Dynatrace.") для проекта. Эти функции включены по умолчанию, но их можно отключить или настроить, добавив [конфигурационные ключи](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys "С помощью конфигурационных ключей можно точно настроить автоматическую инструментацию iOS-приложений.") в файл `Info.plist` приложения.

Используй автоматическую инструментацию вместе с [ручной инструментацией](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios "Обогати мониторинг пользовательского опыта мобильных приложений с помощью OneAgent SDK для iOS.") для сбора дополнительных данных. Например, может понадобиться вручную инструментировать определённые действия, сообщать значения или помечать конкретных пользователей.

## Автоматический запуск OneAgent

OneAgent для iOS автоматически инициализируется во время загрузки библиотеки, то есть в момент, когда бинарный файл библиотеки OneAgent загружается в мобильное приложение при его запуске. Это происходит до вызова `applicationWillFinishLaunching`, где OneAgent можно запустить вручную.

Установи [конфигурационный ключ `DTXAutoStart`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#general "С помощью конфигурационных ключей можно точно настроить автоматическую инструментацию iOS-приложений.") в значение `false`, чтобы отключить автоматический запуск OneAgent. В этом случае потребуется [запустить OneAgent вручную](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#start-oneagent "Обогати мониторинг пользовательского опыта мобильных приложений с помощью OneAgent SDK для iOS.").

## Мониторинг жизненного цикла

OneAgent собирает данные по следующим событиям.

* `AppStart` (событие запуска приложения)

  + Автоматический запуск OneAgent: измеряет промежуток времени от момента запуска OneAgent до вызова метода [`application(_:didFinishLaunchingWithOptions:)`﻿](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application).
  + Ручной запуск OneAgent: измеряет промежуток времени от момента вызова [API ручного запуска OneAgent](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#start-oneagent "Обогати мониторинг пользовательского опыта мобильных приложений с помощью OneAgent SDK для iOS.") до вызова метода `application(_:didFinishLaunchingWithOptions:)`. Если API ручного запуска вызывается после `application(_:didFinishLaunchingWithOptions:)`, событие `AppStart` не генерируется.
* `Display`: измеряет промежуток времени от загрузки представления (view) до его появления на экране. Временные метки вызовов `viewDidLoad`, `viewWillAppear` и `viewDidAppear` классов `ViewController` отображаются в анализе водопада пользовательского действия и помечаются как **событие жизненного цикла (Lifecycle event)**.
* `Redisplay`: измеряет промежуток времени от загрузки представления (view) до его повторного появления на экране. Временные метки вызовов `viewWillAppear` и `viewDidAppear` классов `ViewController` отображаются в анализе водопада пользовательского действия и помечаются как **событие жизненного цикла (Lifecycle event)**.

Установи [конфигурационный ключ `DTXInstrumentLifecycleMonitoring`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#lifecycle-monitoring "С помощью конфигурационных ключей можно точно настроить автоматическую инструментацию iOS-приложений.") в значение `false`, чтобы отключить автоматический мониторинг жизненного цикла. Также посмотри другие ключи в разделе [**Мониторинг жизненного цикла**](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#lifecycle-monitoring "С помощью конфигурационных ключей можно точно настроить автоматическую инструментацию iOS-приложений.") для дополнительных параметров конфигурации.

Чтобы узнать, какие события жизненного цикла сообщаются для SwiftUI, см. [Инструментация элементов управления SwiftUI | Мониторинг жизненного цикла](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls#lifecycle "Используй инструментатор SwiftUI Dynatrace для мониторинга приложений на SwiftUI.").

## Отчёты о сбоях

OneAgent перехватывает все необработанные исключения и отправляет [отчёт о сбое](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#crash "Узнай о пользовательских событиях и событиях ошибок, а также о типах таких событий, фиксируемых Dynatrace.") на сервер. Отчёт о сбое включает время возникновения и полную трассировку стека исключения.

Данные о сбое отправляются только тогда, когда пользователь снова открывает мобильное приложение (то есть при следующем запуске приложения). Однако, если пользователь не открывает приложение в течение 10 минут, отчёт о сбое удаляется. Это связано с тем, что Dynatrace не отправляет отчёты о сбоях старше 10 минут (поскольку такие отчёты уже нельзя сопоставить в кластере Dynatrace).

Установи [конфигурационный ключ `DTXCrashReportingEnabled`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#privacy-and-security "С помощью конфигурационных ключей можно точно настроить автоматическую инструментацию iOS-приложений.") в значение `false`, чтобы отключить отчёты о сбоях.

## Мониторинг веб-запросов

OneAgent автоматически инструментирует и помечает веб-запросы. Для отслеживания веб-запросов OneAgent добавляет к веб-запросу HTTP-заголовок `x-dynatrace` с уникальным значением. Это необходимо для сопоставления данных мониторинга на стороне сервера с соответствующим мобильным веб-запросом.

Установи [конфигурационный ключ `DTXInstrumentWebRequestTiming`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#web-requests "С помощью конфигурационных ключей можно точно настроить автоматическую инструментацию iOS-приложений.") в значение `false`, чтобы отключить мониторинг веб-запросов. Также посмотри другие ключи в разделе [**Веб-запросы**](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#web-requests "С помощью конфигурационных ключей можно точно настроить автоматическую инструментацию iOS-приложений.") для настройки времени и тегирования веб-запросов.

Чтобы узнать, как инструментировать веб-запросы вручную, см. [Измерение веб-запросов](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#measure-web-requests "Обогати мониторинг пользовательского опыта мобильных приложений с помощью OneAgent SDK для iOS.").

## Мониторинг веб-запросов для запросов, передаваемых в `WKWebView`

OneAgent автоматически инструментирует и помечает веб-запросы, передаваемые в `WKWebView`.

Обрати внимание, что OneAgent не отслеживает запросы, выполняемые внутри `WKWebView`. Такие запросы обрабатываются [RUM JavaScript](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/customize-rum "Узнай, как настроить Real User Monitoring Classic с помощью API JavaScript."), если правильно настроен [мониторинг гибридных приложений](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-hybrid-app "Узнай, как инструментировать различные типы гибридных и кроссплатформенных мобильных приложений.") с Dynatrace.

Установи [конфигурационный ключ `DTXInstrumentWebViewTiming`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#hybrid "С помощью конфигурационных ключей можно точно настроить автоматическую инструментацию iOS-приложений.") в значение `false`, чтобы отключить автоматическое измерение времени и тегирование запросов, передаваемых в `WKWebView`.

## Определение пользовательского действия

OneAgent обнаруживает действия пользователя, такие как нажатия кнопок, действия в представлениях и другие взаимодействия с элементами управления интерфейсом, и засекает их время. OneAgent создаёт пользовательские действия на основе UI-компонентов, которые их инициируют, и автоматически объединяет данные о пользовательских действиях с другими данными мониторинга, например с информацией о веб-запросах и сбоях. OneAgent продлевает время жизни пользовательских действий, чтобы корректно агрегировать их с другими событиями, которые выполняются в фоновом потоке или сразу после пользовательского действия.

Чтобы отключить автоматическое создание пользовательских действий, установи значение [ключа конфигурации `DTXInstrumentAutoUserAction`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#user-actions "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") в `false`. Также проверь другие ключи конфигурации в разделе [**User actions**](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#user-actions "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") для управления обнаружением пользовательских действий.

С помощью OneAgent для iOS также можно выполнять следующие действия, связанные с пользовательскими действиями.

* [Создание пользовательских действий](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#create-custom-user-action "Enrich mobile user experience monitoring using OneAgent SDK for iOS.")
* [Отмена пользовательских и автоматически сгенерированных действий](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#cancel-action "Enrich mobile user experience monitoring using OneAgent SDK for iOS.")
* [Использование пользовательских названий элементов управления](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#custom-control-names "Enrich mobile user experience monitoring using OneAgent SDK for iOS.")
* [Изменение автоматически сгенерированных действий](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#modify-auto-actions "Enrich mobile user experience monitoring using OneAgent SDK for iOS.")
* [Маскирование пользовательских действий](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#mask-user-actions "Enrich mobile user experience monitoring using OneAgent SDK for iOS.")

Чтобы узнать, как OneAgent формирует названия пользовательских действий, см. раздел [Формирование названий пользовательских действий](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#user-action-naming "Enrich mobile user experience monitoring using OneAgent SDK for iOS.").

## Обнаружение яростных нажатий (rage tap)

Когда мобильное приложение медленно реагирует или возникает проблема с пользовательским интерфейсом, пользователи могут многократно нажимать на экран или на затронутый элемент управления. OneAgent распознаёт такое поведение как [rage tap](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#rage-event "Learn about user and error events and the types of user and error events captured by Dynatrace.").

Чтобы прекратить обнаружение яростных нажатий, установи значение [ключа конфигурации `DTXDetectRageTaps`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#user-actions "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") в `false`.

## Мониторинг местоположения

🔴 Отключено по умолчанию

OneAgent может фиксировать местоположение конечных пользователей приложения и отправлять зафиксированное местоположение на сервер в виде метрики. Для защиты приватности пользователей OneAgent фиксирует GPS-координаты с точностью до двух знаков после запятой (точность ~1 км).

Чтобы включить фиксацию местоположения, установи значение [ключа конфигурации `DTXInstrumentGPSLocation`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#privacy-and-security "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") в `true`.