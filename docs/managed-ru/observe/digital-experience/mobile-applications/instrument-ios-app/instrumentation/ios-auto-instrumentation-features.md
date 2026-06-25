---
title: Функции авто-инструментирования OneAgent for iOS
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features
scraped: 2026-05-12T11:32:51.030038
---

# Функции авто-инструментирования OneAgent for iOS

# Функции авто-инструментирования OneAgent for iOS

* Explanation
* 4-min read
* Updated on Feb 03, 2026

Авто-инструментирование с помощью OneAgent for iOS происходит во время выполнения. Результирующее приложение инструментируется до уровней, настроенных в файле [`Info.plist`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Файл Info.plist хранит ключи идентификации и конфигурации приложения. Используйте его для точной настройки конфигурации инструментирования.") приложения.

Следующие функции инструментируются автоматически при [настройке OneAgent](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios "Настройте мониторинг пользовательского опыта для iOS-приложений в Dynatrace.") для проекта. Эти функции включены по умолчанию, но их можно отключить или настроить, добавив [конфигурационные ключи](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys "С помощью конфигурационных ключей можно точно настроить авто-инструментирование iOS-приложений.") в файл `Info.plist` приложения.

Используйте авто-инструментирование совместно с [ручным инструментированием](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios "Расширьте мониторинг мобильного пользовательского опыта с помощью OneAgent SDK for iOS.") для захвата дополнительных данных. Например, вы можете вручную инструментировать определённые действия, сообщать о значениях или тегировать конкретных пользователей.

## Автоматический запуск OneAgent

OneAgent for iOS инициализируется автоматически при загрузке библиотеки, то есть когда двоичный файл библиотеки OneAgent загружается в мобильное приложение при его запуске. Это происходит до вызова `applicationWillFinishLaunching`, где OneAgent можно запустить вручную.

Установите [конфигурационный ключ `DTXAutoStart`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#general "С помощью конфигурационных ключей можно точно настроить авто-инструментирование iOS-приложений.") в значение `false`, чтобы отключить автоматический запуск OneAgent. В этом случае потребуется [запустить OneAgent вручную](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#start-oneagent "Расширьте мониторинг мобильного пользовательского опыта с помощью OneAgent SDK for iOS.").

## Мониторинг жизненного цикла

OneAgent собирает данные о следующих событиях.

* `AppStart` (событие запуска приложения)

  + Автоматический запуск OneAgent: измеряет промежуток времени от запуска OneAgent до вызова метода [`application(_:didFinishLaunchingWithOptions:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application).
  + Ручной запуск OneAgent: измеряет промежуток времени от вызова [API ручного запуска OneAgent](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#start-oneagent "Расширьте мониторинг мобильного пользовательского опыта с помощью OneAgent SDK for iOS.") до вызова метода `application(_:didFinishLaunchingWithOptions:)`. Если API ручного запуска вызывается после `application(_:didFinishLaunchingWithOptions:)`, событие `AppStart` не генерируется.
* `Display`: измеряет промежуток времени от загрузки представления до его появления на экране. Временные метки вызовов `viewDidLoad`, `viewWillAppear` и `viewDidAppear` классов `ViewController` отображаются в waterfall-анализе пользовательских действий и помечаются как **Lifecycle event**.
* `Redisplay`: измеряет промежуток времени от загрузки представления до его повторного появления на экране. Временные метки вызовов `viewWillAppear` и `viewDidAppear` классов `ViewController` отображаются в waterfall-анализе пользовательских действий и помечаются как **Lifecycle event**.

Установите [конфигурационный ключ `DTXInstrumentLifecycleMonitoring`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#lifecycle-monitoring "С помощью конфигурационных ключей можно точно настроить авто-инструментирование iOS-приложений.") в значение `false`, чтобы отключить автоматический мониторинг жизненного цикла. Дополнительные параметры настройки см. в других ключах раздела [**Lifecycle monitoring**](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#lifecycle-monitoring "С помощью конфигурационных ключей можно точно настроить авто-инструментирование iOS-приложений.").

Чтобы узнать, какие события жизненного цикла сообщаются для SwiftUI, см. [Инструментирование элементов управления SwiftUI | Мониторинг жизненного цикла](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls#lifecycle "Используйте Dynatrace SwiftUI instrumentor для мониторинга SwiftUI-приложений.").

## Отчёты о сбоях

OneAgent захватывает все необработанные исключения и отправляет отчёт о [сбое](/managed/observe/digital-experience/rum-concepts/user-and-error-events#crash "Узнайте о событиях пользователей и ошибках, а также о типах событий, захватываемых Dynatrace.") на сервер. Отчёт о сбое содержит время возникновения и полную трассировку стека исключения.

Сведения о сбое отправляются только после повторного открытия пользователем мобильного приложения (то есть при следующем запуске). Однако если пользователь не открывает приложение в течение 10 минут, отчёт о сбое удаляется. Это объясняется тем, что Dynatrace не отправляет отчёты о сбоях старше 10 минут (такие отчёты больше не могут быть скоррелированы в кластере Dynatrace).

Установите [конфигурационный ключ `DTXCrashReportingEnabled`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#privacy-and-security "С помощью конфигурационных ключей можно точно настроить авто-инструментирование iOS-приложений.") в значение `false`, чтобы отключить отчёты о сбоях.

## Мониторинг веб-запросов

OneAgent автоматически инструментирует и тегирует веб-запросы. Для отслеживания веб-запросов OneAgent добавляет HTTP-заголовок `x-dynatrace` с уникальным значением к веб-запросу. Это необходимо для корреляции данных мониторинга на стороне сервера с соответствующим мобильным веб-запросом.

Установите [конфигурационный ключ `DTXInstrumentWebRequestTiming`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#web-requests "С помощью конфигурационных ключей можно точно настроить авто-инструментирование iOS-приложений.") в значение `false`, чтобы отключить мониторинг веб-запросов. Дополнительные ключи для настройки тайминга и тегирования веб-запросов см. в разделе [**Web requests**](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#web-requests "С помощью конфигурационных ключей можно точно настроить авто-инструментирование iOS-приложений.").

Чтобы узнать, как вручную инструментировать веб-запросы, см. [Измерение веб-запросов](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#measure-web-requests "Расширьте мониторинг мобильного пользовательского опыта с помощью OneAgent SDK for iOS.").

## Мониторинг веб-запросов для запросов, передаваемых в `WKWebView`

OneAgent автоматически инструментирует и тегирует веб-запросы, передаваемые в `WKWebView`.

Обратите внимание, что OneAgent не отслеживает запросы, инициированные внутри `WKWebView`. Такие запросы обрабатываются [RUM JavaScript](/managed/observe/digital-experience/web-applications/additional-configuration/customize-rum "Узнайте, как настроить Real User Monitoring с помощью JavaScript API."), если вы правильно настроили [мониторинг гибридных приложений](/managed/observe/digital-experience/mobile-applications/instrument-hybrid-app "Узнайте, как инструментировать различные типы гибридных и кроссплатформенных мобильных приложений.") в Dynatrace.

Установите [конфигурационный ключ `DTXInstrumentWebViewTiming`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#hybrid "С помощью конфигурационных ключей можно точно настроить авто-инструментирование iOS-приложений.") в значение `false`, чтобы отключить автоматический тайминг и тегирование веб-запросов для запросов, передаваемых в `WKWebView`.

## Обнаружение пользовательских действий

OneAgent обнаруживает и отсчитывает время пользовательских действий, таких как нажатие кнопок, действия с представлениями и другие взаимодействия с элементами управления UI. OneAgent создаёт пользовательские действия на основе компонентов UI, которые инициируют эти действия, и автоматически объединяет данные пользовательских действий с другими данными мониторинга, например с информацией о веб-запросах и сбоях. OneAgent продлевает время жизни пользовательских действий, чтобы правильно агрегировать их с другими событиями, выполняемыми в фоновом потоке или сразу после пользовательского действия.

Установите [конфигурационный ключ `DTXInstrumentAutoUserAction`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#user-actions "С помощью конфигурационных ключей можно точно настроить авто-инструментирование iOS-приложений.") в значение `false`, чтобы отключить автоматическое создание пользовательских действий. Дополнительные ключи для управления обнаружением пользовательских действий см. в разделе [**User actions**](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#user-actions "С помощью конфигурационных ключей можно точно настроить авто-инструментирование iOS-приложений.").

С помощью OneAgent for iOS также можно выполнять следующие действия, связанные с пользовательскими действиями:

* [Создавать пользовательские действия](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#create-custom-user-action "Расширьте мониторинг мобильного пользовательского опыта с помощью OneAgent SDK for iOS.")
* [Отменять пользовательские и автоматически создаваемые действия](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#cancel-action "Расширьте мониторинг мобильного пользовательского опыта с помощью OneAgent SDK for iOS.")
* [Использовать пользовательские названия элементов управления](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#custom-control-names "Расширьте мониторинг мобильного пользовательского опыта с помощью OneAgent SDK for iOS.")
* [Изменять автоматически создаваемые действия](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#modify-auto-actions "Расширьте мониторинг мобильного пользовательского опыта с помощью OneAgent SDK for iOS.")
* [Маскировать пользовательские действия](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#mask-user-actions "Расширьте мониторинг мобильного пользовательского опыта с помощью OneAgent SDK for iOS.")

Чтобы узнать, как OneAgent формирует имена пользовательских действий, см. [Именование пользовательских действий](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#user-action-naming "Расширьте мониторинг мобильного пользовательского опыта с помощью OneAgent SDK for iOS.").

## Обнаружение rage tap

Когда мобильное приложение не реагирует быстро или в интерфейсе есть проблемы, пользователи могут неоднократно нажимать на экран или затронутый элемент управления UI. OneAgent обнаруживает такое поведение как [rage tap](/managed/observe/digital-experience/rum-concepts/user-and-error-events#rage-event "Узнайте о событиях пользователей и ошибках, а также о типах событий, захватываемых Dynatrace.").

Установите [конфигурационный ключ `DTXDetectRageTaps`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#user-actions "С помощью конфигурационных ключей можно точно настроить авто-инструментирование iOS-приложений.") в значение `false`, чтобы прекратить обнаружение rage tap.

## Мониторинг местоположения

Отключён по умолчанию

OneAgent может захватывать местоположение пользователей вашего приложения и отправлять его в виде метрики на сервер. Для защиты конфиденциальности пользователей OneAgent захватывает GPS-координаты с точностью до двух десятичных знаков (точность около 1 км).

Установите [конфигурационный ключ `DTXInstrumentGPSLocation`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#privacy-and-security "С помощью конфигурационных ключей можно точно настроить авто-инструментирование iOS-приложений.") в значение `true`, чтобы включить захват местоположения.