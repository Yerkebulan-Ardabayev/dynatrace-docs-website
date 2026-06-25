---
title: Инструментирование iOS-приложений
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/instrument-ios-app
scraped: 2026-05-12T11:23:34.406656
---

# Инструментирование iOS-приложений

# Инструментирование iOS-приложений

* Overview
* 1-min read
* Updated on Mar 31, 2026

Процесс мониторинга пользовательского опыта нативных мобильных приложений принципиально отличается от мониторинга браузерных веб-приложений. Это связано с тем, что мониторинг мобильных приложений включает компиляцию, упаковку и доставку библиотеки мониторинга вместе с пакетом мобильного приложения.

Для мониторинга мобильного приложения с помощью Dynatrace необходимо инструментировать OneAgent для iOS, который обеспечивает видимость жизненного цикла активности, пользовательских действий, веб-запросов, сбоев и многого другого.

Ознакомьтесь с нашим [демонстрационным мобильным приложением](https://dt-url.net/332226v), чтобы получить представление о том, как работает инструментирование с помощью Dynatrace. Это образцовое приложение демонстрирует основные функции, предоставляемые OneAgent SDK для iOS.

Поддерживаемые версии iOS можно найти в разделе [Поддержка технологий | Real User Monitoring мобильных приложений](/managed/ingest-from/technology-support#mobile-rum "Ознакомьтесь с техническими сведениями о поддержке Dynatrace конкретных платформ и фреймворков разработки.").

### Инструментирование

* [Начало работы с мониторингом iOS](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/get-started-with-ios-monitoring "Изучите шаги, необходимые для инструментирования iOS-приложения в целях мониторинга с помощью Dynatrace.")
* [Настройка OneAgent для iOS-приложений](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios "Настройте мониторинг пользовательского опыта для iOS-приложений в Dynatrace.")
* [Инструментирование элементов управления SwiftUI](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls "Используйте инструментор Dynatrace SwiftUI для мониторинга приложений SwiftUI.")
* [Функции автоинструментирования OneAgent для iOS](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features "Ознакомьтесь со списком функций, доступных после инструментирования приложения с помощью OneAgent.")
* [Файл Info.plist](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Файл Info.plist хранит идентификационные и конфигурационные ключи приложения. Используйте его для точной настройки конфигурации инструментирования.")

### Настройка

* [Расширенная настройка OneAgent для iOS](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/configuration-settings "Настройте автоинструментирование для iOS-приложений с помощью расширенных параметров.")
* [Ключи конфигурации OneAgent для iOS](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys "С помощью ключей конфигурации можно выполнить тонкую настройку автоинструментирования iOS-приложений.")
* [OneAgent SDK для iOS](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios "Расширьте мониторинг мобильного пользовательского опыта с помощью OneAgent SDK для iOS.")
* [Журналирование отладки OneAgent для iOS](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/logging-for-ios "Включите журналирование отладки для OneAgent.")

### Конфиденциальность данных

[Настройка параметров конфиденциальности данных для мобильных приложений](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile "Используйте параметры конфиденциальности Dynatrace, чтобы обеспечить соответствие мобильных приложений требованиям законодательства о защите данных в вашем регионе.")

[Конфиденциальность пользователей для iOS](/managed/manage/data-privacy-and-security/data-privacy/user-privacy-for-ios "Узнайте, какие данные собирает OneAgent, когда требуется сообщить Apple о конфиденциальности приложения.")

Начиная с OneAgent для iOS версии 8.335 поддержка Xcode 16 прекращена. Поддерживается только Xcode 26 и выше.

Также обратите внимание, что [требования Apple к отправке приложений в App Store](https://dt-url.net/we038fb) ограничат поддержку приложениями, собранными минимум на Xcode 26, приблизительно в апреле 2026 года.

Начиная с OneAgent для iOS версии 8.343 поддержка iOS 12, iOS 13 и iOS 14 будет прекращена. Новая минимальная поддерживаемая версия — iOS 15. Версия 8.341 является последней версией OneAgent для iOS, поддерживающей iOS 12–14.

Начиная с OneAgent для iOS версии 8.323 поддержка `static builds` и `Carthage` как методов интеграции будет прекращена.

Рекомендуется перейти на поддерживаемую альтернативу, например Swift Package Manager, для обеспечения дальнейшей совместимости и получения обновлений.

OneAgent для iOS версии 8.249 является последней версией, поддерживающей 32-битную архитектуру.