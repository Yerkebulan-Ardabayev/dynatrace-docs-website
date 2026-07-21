---
title: Начало работы с мониторингом iOS в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/get-started-with-ios-monitoring
---

# Начало работы с мониторингом iOS в RUM Classic

# Начало работы с мониторингом iOS в RUM Classic

* Практическое руководство
* Чтение за 1 мин
* Обновлено 19 сентября 2022 г.

Чтобы мониторить мобильное приложение с помощью Dynatrace, сначала нужно создать приложение в Dynatrace, а затем инструментировать само мобильное приложение с помощью OneAgent для iOS.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Создание приложения в Dynatrace**

Создание мобильного приложения в веб-интерфейсе Dynatrace](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios#create-app-in-ui "Настройка мониторинга пользовательского опыта для iOS-приложений в Dynatrace.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Настройка OneAgent**

Инструментирование приложения через CocoaPods, Swift Package Manager или вручную](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios#set-up-oneagent "Настройка мониторинга пользовательского опыта для iOS-приложений в Dynatrace.")[![Шаг 3, опционально](https://dt-cdn.net/images/dotted-step-3-e2082c1921.svg "Шаг 3, опционально")

**Инструментирование элементов управления SwiftUI**

Инструментирование кнопок, степперов, переключателей SwiftUI и других элементов](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls "Использование инструментатора SwiftUI Dynatrace для мониторинга приложений на SwiftUI.")

После инструментирования iOS-приложения с помощью OneAgent может понадобиться донастроить инструментирование под свои задачи:

* Настроить [функции автоматического инструментирования](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features "Список функций, доступных после инструментирования приложения с помощью OneAgent.") через [ключи конфигурации](/managed/observe/digital-experience/rum-classic/mobile-applications/customization/ios-configuration-keys "С помощью ключей конфигурации можно донастроить автоматическое инструментирование iOS-приложений.").
* Собирать дополнительные данные с помощью [ручного инструментирования](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios "Расширение мониторинга пользовательского опыта мобильных приложений с помощью OneAgent SDK для iOS.").
* [Настроить параметры конфиденциальности данных](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile "Использование настроек конфиденциальности, которые предоставляет Dynatrace, чтобы обеспечить соответствие мобильных приложений требованиям законодательства о защите данных вашего региона.") для iOS-приложений, например настроить режим согласия пользователя (opt-in) или маскирование действий пользователя.
* Узнать, [какие данные собирает OneAgent для iOS](/managed/manage/data-privacy-and-security/data-privacy/user-privacy-for-ios "Информация о том, какие данные собирает OneAgent, чтобы заполнить или обновить анкету о конфиденциальности приложения в App Store Connect."), чтобы заполнить или обновить анкету о конфиденциальности данных в App Store Connect.