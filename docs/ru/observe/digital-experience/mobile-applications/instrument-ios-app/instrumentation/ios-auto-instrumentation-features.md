---
title: OneAgent for iOS auto-instrumentation features
source: https://www.dynatrace.com/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features
scraped: 2026-03-06T21:34:10.008934
---

# Функции автоинструментирования OneAgent для iOS

# Функции автоинструментирования OneAgent для iOS

* Classic
* Описание
* Время чтения: 4 мин
* Обновлено 3 февраля 2026 г.

Автоинструментирование с помощью OneAgent для iOS происходит во время выполнения. Результирующее приложение инструментируется до уровней, настроенных в файле [`Info.plist`](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Файл Info.plist хранит идентификацию вашего приложения и ключи конфигурации. Используйте его для тонкой настройки конфигурации инструментирования.") приложения.

Следующие функции автоматически инструментируются при [настройке OneAgent](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios "Настройте мониторинг пользовательского опыта для iOS-приложений в Dynatrace.") для вашего проекта. Эти функции включены по умолчанию, но вы можете отключить или настроить их, добавив [ключи конфигурации](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys "С помощью ключей конфигурации вы можете выполнить тонкую настройку автоинструментирования ваших iOS-приложений.") в файл `Info.plist` вашего приложения.

Используйте автоинструментирование в сочетании с [ручным инструментированием](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios "Расширьте мониторинг мобильного пользовательского опыта с помощью OneAgent SDK для iOS.") для захвата дополнительных данных. Например, вы можете захотеть вручную инструментировать определённые действия, передавать значения или помечать конкретных пользователей.

## Автоматический запуск OneAgent

OneAgent для iOS инициализируется автоматически при загрузке библиотеки — это момент, когда бинарный файл библиотеки OneAgent загружается в мобильное приложение при запуске приложения. Это происходит до `applicationWillFinishLaunching`, где OneAgent может быть запущен вручную.

Установите [ключ конфигурации `DTXAutoStart`](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#general "С помощью ключей конфигурации вы можете выполнить тонкую настройку автоинструментирования ваших iOS-приложений.") в значение `false`, чтобы отключить автоматический запуск OneAgent. В этом случае вам потребуется [запустить OneAgent вручную](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#start-oneagent "Расширьте мониторинг мобильного пользовательского опыта с помощью OneAgent SDK для iOS.").

## Мониторинг жизненного цикла

OneAgent собирает данные о следующих событиях.

* `AppStart` (событие запуска приложения)

  + Автоматический запуск OneAgent: измеряет временной интервал от момента запуска OneAgent до вызова метода [`application(_:didFinishLaunchingWithOptions:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application).
  + Ручной запуск OneAgent: измеряет временной интервал от вызова [API ручного запуска OneAgent](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#start-oneagent "Расширьте мониторинг мобильного пользовательского опыта с помощью OneAgent SDK для iOS.") до вызова метода `application(_:didFinishLaunchingWithOptions:)`. Если API ручного запуска вызывается после `application(_:didFinishLaunchingWithOptions:)`, событие `AppStart` не генерируется.
* `Display`: измеряет временной интервал от загрузки представления до его появления на экране. Метки времени вызовов `viewDidLoad`, `viewWillAppear` и `viewDidAppear` классов `ViewController` отображаются в каскадном анализе действий пользователя и помечаются как **Событие жизненного цикла**.
* `Redisplay`: измеряет временной интервал от загрузки представления до его повторного появления на экране. Метки времени вызовов `viewWillAppear` и `viewDidAppear` классов `ViewController` отображаются в каскадном анализе действий пользователя и помечаются как **Событие жизненного цикла**.

Установите [ключ конфигурации `DTXInstrumentLifecycleMonitoring`](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#lifecycle-monitoring "С помощью ключей конфигурации вы можете выполнить тонкую настройку автоинструментирования ваших iOS-приложений.") в значение `false`, чтобы отключить автоматический мониторинг жизненного цикла. Также ознакомьтесь с другими ключами в разделе [**Мониторинг жизненного цикла**](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#lifecycle-monitoring "С помощью ключей конфигурации вы можете выполнить тонкую настройку автоинструментирования ваших iOS-приложений.") для дополнительных возможностей конфигурации.

Чтобы узнать, какие события жизненного цикла отправляются для SwiftUI, см. [Инструментирование элементов управления SwiftUI | Мониторинг жизненного цикла](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls#lifecycle "Используйте инструментатор Dynatrace SwiftUI для мониторинга ваших SwiftUI-приложений.").

## Отчёты о сбоях

OneAgent перехватывает все необработанные исключения и отправляет отчёт о [сбое](/docs/observe/digital-experience/rum-concepts/user-and-error-events#crash "Узнайте о пользовательских событиях и событиях ошибок, а также о типах пользовательских событий и событий ошибок, захватываемых Dynatrace.") на сервер. Отчёт о сбое включает время возникновения и полную трассировку стека исключения.

Данные о сбое отправляются только при повторном открытии мобильного приложения пользователем (то есть при следующем запуске приложения). Однако если пользователь не откроет приложение в течение 10 минут, отчёт о сбое удаляется. Это связано с тем, что Dynatrace не отправляет отчёты о сбоях старше 10 минут (так как такие отчёты больше не могут быть скоррелированы на кластере Dynatrace).

Установите [ключ конфигурации `DTXCrashReportingEnabled`](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#privacy-and-security "С помощью ключей конфигурации вы можете выполнить тонкую настройку автоинструментирования ваших iOS-приложений.") в значение `false`, чтобы отключить отчёты о сбоях.

## Мониторинг веб-запросов

OneAgent автоматически инструментирует и помечает ваши веб-запросы. Для отслеживания веб-запросов OneAgent добавляет HTTP-заголовок `x-dynatrace` с уникальным значением к веб-запросу. Это необходимо для корреляции данных мониторинга на стороне сервера с соответствующим мобильным веб-запросом.

Установите [ключ конфигурации `DTXInstrumentWebRequestTiming`](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#web-requests "С помощью ключей конфигурации вы можете выполнить тонкую настройку автоинструментирования ваших iOS-приложений.") в значение `false`, чтобы отключить мониторинг веб-запросов. Также ознакомьтесь с другими ключами в разделе [**Веб-запросы**](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#web-requests "С помощью ключей конфигурации вы можете выполнить тонкую настройку автоинструментирования ваших iOS-приложений.") для настройки хронометража и маркировки веб-запросов.

Чтобы узнать, как вручную инструментировать веб-запросы, см. [Измерение веб-запросов](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#measure-web-requests "Расширьте мониторинг мобильного пользовательского опыта с помощью OneAgent SDK для iOS.").

## Мониторинг веб-запросов, передаваемых в `WKWebView`

OneAgent автоматически инструментирует и помечает веб-запросы, передаваемые в `WKWebView`.

Обратите внимание, что OneAgent не мониторит запросы, выполняемые внутри `WKWebView`. Такие запросы обрабатываются [RUM JavaScript](/docs/observe/digital-experience/web-applications/additional-configuration/customize-rum "Узнайте, как настроить мониторинг реальных пользователей с помощью JavaScript API."), если вы правильно настроили [мониторинг гибридного приложения](/docs/observe/digital-experience/mobile-applications/instrument-hybrid-app "Узнайте, как инструментировать различные типы гибридных и кроссплатформенных мобильных приложений.") с Dynatrace.

Установите [ключ конфигурации `DTXInstrumentWebViewTiming`](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#hybrid "С помощью ключей конфигурации вы можете выполнить тонкую настройку автоинструментирования ваших iOS-приложений.") в значение `false`, чтобы отключить автоматический хронометраж и маркировку веб-запросов, передаваемых в `WKWebView`.

## Обнаружение действий пользователя

OneAgent обнаруживает и измеряет действия пользователя, такие как нажатия кнопок, действия с представлениями и другие взаимодействия с элементами интерфейса. OneAgent создаёт действия пользователя на основе компонентов интерфейса, которые инициируют эти действия, и автоматически объединяет данные о действиях пользователя с другими данными мониторинга, такими как информация о веб-запросах и сбоях. OneAgent продлевает время жизни действий пользователя для правильной агрегации с другими событиями, выполняемыми в фоновом потоке или сразу после действия пользователя.

Установите [ключ конфигурации `DTXInstrumentAutoUserAction`](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#user-actions "С помощью ключей конфигурации вы можете выполнить тонкую настройку автоинструментирования ваших iOS-приложений.") в значение `false`, чтобы отключить автоматическое создание действий пользователя. Также ознакомьтесь с другими ключами конфигурации в разделе [**Действия пользователя**](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#user-actions "С помощью ключей конфигурации вы можете выполнить тонкую настройку автоинструментирования ваших iOS-приложений.") для управления обнаружением действий пользователя.

С помощью OneAgent для iOS вы также можете выполнять следующие действия, связанные с действиями пользователя.

* [Создание пользовательских действий](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#create-custom-user-action "Расширьте мониторинг мобильного пользовательского опыта с помощью OneAgent SDK для iOS.")
* [Отмена пользовательских и автоматически сгенерированных действий](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#cancel-action "Расширьте мониторинг мобильного пользовательского опыта с помощью OneAgent SDK для iOS.")
* [Использование пользовательских заголовков элементов управления](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#custom-control-names "Расширьте мониторинг мобильного пользовательского опыта с помощью OneAgent SDK для iOS.")
* [Изменение автоматически сгенерированных действий](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#modify-auto-actions "Расширьте мониторинг мобильного пользовательского опыта с помощью OneAgent SDK для iOS.")
* [Маскирование действий пользователя](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#mask-user-actions "Расширьте мониторинг мобильного пользовательского опыта с помощью OneAgent SDK для iOS.")

Чтобы узнать, как OneAgent формирует имена действий пользователя, см. [Именование действий пользователя](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#user-action-naming "Расширьте мониторинг мобильного пользовательского опыта с помощью OneAgent SDK для iOS.").

## Обнаружение яростных нажатий

Когда ваше мобильное приложение не реагирует быстро или возникает проблема с пользовательским интерфейсом, пользователи могут многократно нажимать на экран или затронутый элемент управления. OneAgent обнаруживает такое поведение как [яростное нажатие](/docs/observe/digital-experience/rum-concepts/user-and-error-events#rage-event "Узнайте о пользовательских событиях и событиях ошибок, а также о типах пользовательских событий и событий ошибок, захватываемых Dynatrace.").

Установите [ключ конфигурации `DTXDetectRageTaps`](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#user-actions "С помощью ключей конфигурации вы можете выполнить тонкую настройку автоинструментирования ваших iOS-приложений.") в значение `false`, чтобы прекратить обнаружение яростных нажатий.

## Мониторинг местоположения

Отключено по умолчанию

OneAgent может захватывать местоположение конечных пользователей вашего приложения и отправлять захваченное местоположение в качестве метрики на сервер. Для защиты конфиденциальности ваших пользователей OneAgent захватывает GPS-координаты с точностью до двух десятичных знаков (точность ~1 км).

Установите [ключ конфигурации `DTXInstrumentGPSLocation`](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#privacy-and-security "С помощью ключей конфигурации вы можете выполнить тонкую настройку автоинструментирования ваших iOS-приложений.") в значение `true`, чтобы включить захват местоположения.
