---
title: Instrument iOS apps
source: https://www.dynatrace.com/docs/observe/digital-experience/mobile-applications/instrument-ios-app
scraped: 2026-03-05T21:26:00.148955
---

# Инструментирование iOS-приложений

# Инструментирование iOS-приложений

* Classic
* Обзор
* Чтение: 1 мин
* Обновлено 9 февраля 2026 г.

Процесс мониторинга пользовательского опыта нативных мобильных приложений принципиально отличается от мониторинга браузерных веб-приложений. Это объясняется тем, что мониторинг мобильных приложений предполагает компиляцию, упаковку и поставку библиотеки мониторинга вместе с пакетом вашего мобильного приложения.

Для мониторинга мобильного приложения с помощью Dynatrace необходимо инструментировать OneAgent для iOS, который обеспечивает видимость жизненного цикла активности, действий пользователей, веб-запросов, сбоев и многого другого.

Ознакомьтесь с нашим новым [демонстрационным мобильным приложением](https://dt-url.net/332226v), чтобы понять, как работает инструментирование с Dynatrace. Это образцовое приложение демонстрирует основные функции, предоставляемые OneAgent SDK для iOS.

Информацию о поддерживаемых версиях iOS см. в разделе [Поддержка технологий | Real User Monitoring для мобильных приложений](/docs/ingest-from/technology-support#mobile-rum "Найдите технические сведения о поддержке Dynatrace конкретных платформ и фреймворков разработки.").

### Инструментирование

* [Начало работы с мониторингом iOS](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/get-started-with-ios-monitoring "Узнайте о шагах, необходимых для инструментирования iOS-приложения для мониторинга в Dynatrace.")
* [Настройка OneAgent для iOS-приложений](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios "Настройте мониторинг пользовательского опыта iOS-приложений в Dynatrace.")
* [Инструментирование элементов управления SwiftUI](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls "Используйте инструментатор Dynatrace SwiftUI для мониторинга SwiftUI-приложений.")
* [Функции автоинструментирования OneAgent для iOS](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features "Изучите список функций, доступных после инструментирования приложения с помощью OneAgent.")
* [Файл Info.plist](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Файл Info.plist хранит ключи идентификации и конфигурации приложения. Используйте его для тонкой настройки конфигурации инструментирования.")

### Настройка

* [Расширенная конфигурация OneAgent для iOS](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/configuration-settings "Настройте автоинструментирование iOS-приложений с помощью расширенных параметров.")
* [Ключи конфигурации OneAgent для iOS](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys "С помощью ключей конфигурации можно тонко настроить автоинструментирование iOS-приложений.")
* [OneAgent SDK для iOS](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios "Расширьте возможности мониторинга пользовательского опыта мобильных приложений с помощью OneAgent SDK для iOS.")
* [Отладочное журналирование OneAgent для iOS](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/logging-for-ios "Включите отладочное журналирование для OneAgent.")

### Конфиденциальность данных

[Настройка параметров конфиденциальности данных для мобильных приложений](/docs/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile "Используйте параметры конфиденциальности, предоставляемые Dynatrace, чтобы обеспечить соответствие мобильных приложений нормативным требованиям по защите данных в вашем регионе.")

[Конфиденциальность пользователей для iOS](/docs/manage/data-privacy-and-security/data-privacy/user-privacy-for-ios "Узнайте, какие данные собирает OneAgent при необходимости сообщения о конфиденциальности приложения в Apple.")

Начиная с OneAgent для iOS версии 8.335, Dynatrace прекратила поддержку Xcode 16. Поддерживается только Xcode 26 и выше.

Также обратите внимание, что [рекомендации Apple по публикации в App Store](https://dt-url.net/we038fb) ограничат поддержку приложениями, созданными с использованием минимум Xcode 26, приблизительно в апреле 2026 года.

Начиная с OneAgent для iOS версии 8.323, Dynatrace прекратит поддержку методов интеграции `static builds` и `Carthage`.

Рекомендуется перейти на поддерживаемую альтернативу, например Swift Package Manager, для обеспечения совместимости и получения обновлений.

OneAgent для iOS версии 8.249 является последней версией с поддержкой 32-битной архитектуры.
