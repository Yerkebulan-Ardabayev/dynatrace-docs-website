---
title: Начало работы с мониторингом iOS
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/get-started-with-ios-monitoring
scraped: 2026-05-12T11:32:52.882328
---

# Начало работы с мониторингом iOS

# Начало работы с мониторингом iOS

* How-to guide
* 1-min read
* Updated on Sep 19, 2022

Для мониторинга мобильного приложения с помощью Dynatrace необходимо сначала создать приложение в Dynatrace, а затем инструментировать само мобильное приложение с помощью OneAgent for iOS.

1. **Создайте приложение в Dynatrace**

   Создайте мобильное приложение в веб-интерфейсе Dynatrace.

2. **Настройте OneAgent**

   Инструментируйте приложение через CocoaPods, Swift Package Manager или вручную.

3. **Опционально. Инструментируйте элементы управления SwiftUI**

   Инструментируйте кнопки SwiftUI, stepper, toggle и другие элементы.

После инструментирования iOS-приложения с помощью OneAgent вы можете дополнительно настроить инструментирование в соответствии с вашими потребностями:

* Настройте [функции авто-инструментирования](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features "Изучите список функций, доступных после инструментирования приложения с помощью OneAgent.") через [конфигурационные ключи](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys "С помощью конфигурационных ключей можно точно настроить авто-инструментирование iOS-приложений.").
* Захватывайте дополнительные данные через [ручное инструментирование](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios "Расширьте мониторинг мобильного пользовательского опыта с помощью OneAgent SDK for iOS.").
* [Настройте параметры конфиденциальности данных](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile "Используйте настройки конфиденциальности Dynatrace для обеспечения соответствия мобильных приложений нормативным требованиям вашего региона.") для iOS-приложений: например, настройте режим opt-in для пользователя или маскировку пользовательских действий.
* Узнайте, [какие данные захватывает OneAgent for iOS](/managed/manage/data-privacy-and-security/data-privacy/user-privacy-for-ios "Узнайте, какие данные собирает OneAgent, когда вам нужно сообщить о конфиденциальности приложения в Apple."), чтобы заполнить или обновить вопросник о конфиденциальности данных в App Store Connect.