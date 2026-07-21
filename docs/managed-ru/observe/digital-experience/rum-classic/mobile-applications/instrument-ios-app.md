---
title: Инструментирование iOS-приложений в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app
---

# Инструментирование iOS-приложений в RUM Classic

# Инструментирование iOS-приложений в RUM Classic

* Обзор
* Чтение: 1 минута
* Обновлено 10 июля 2026 г.

Мониторинг пользовательского опыта нативных мобильных приложений принципиально отличается от мониторинга веб-приложений на основе браузера. Причина в том, что мониторинг мобильных приложений подразумевает компиляцию, упаковку и поставку библиотеки мониторинга вместе с пакетом самого мобильного приложения.

Чтобы отслеживать мобильное приложение с помощью Dynatrace, нужно инструментировать OneAgent для iOS, который предоставляет видимость жизненного цикла activity, действий пользователя, веб-запросов, сбоев и прочего.

Список поддерживаемых версий iOS доступен на странице [Поддержка технологий | Mobile app Real User Monitoring](/managed/ingest-from/technology-support#mobile-rum "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

### Инструментирование

* [Начало работы с мониторингом iOS в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/get-started-with-ios-monitoring "Learn the steps you need to perform to instrument your iOS app for monitoring with Dynatrace.")
* [Настройка OneAgent для iOS-приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios "Set up user experience monitoring for iOS apps within Dynatrace.")
* [Инструментирование элементов SwiftUI в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls "Use the Dynatrace SwiftUI instrumentor to monitor your SwiftUI apps.")
* [Функции автоинструментирования OneAgent для iOS в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features "Explore the list of features that are available after you instrument your application with OneAgent.")
* [Файл Info.plist в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Info.plist file stores your app identification and configuration keys. Use it to fine-tune the instrumentation configuration.")

### Настройка

* [Расширенная конфигурация OneAgent для iOS в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/configuration-settings "Configure auto-instrumentation for iOS apps using advanced settings.")
* [Ключи конфигурации OneAgent для iOS в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.")
* [OneAgent SDK для iOS в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios "Enrich mobile user experience monitoring using OneAgent SDK for iOS.")
* [Отладочное логирование OneAgent для iOS в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/logging-for-ios "Turn on debug logging for OneAgent.")

### Конфиденциальность данных

[Настройка параметров конфиденциальности данных для мобильных приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.")

[Конфиденциальность пользователей для iOS](/managed/manage/data-privacy-and-security/data-privacy/user-privacy-for-ios "Learn about what kind of data OneAgent collects when you need to report your app privacy to Apple.")

Начиная с версии OneAgent для iOS 8.335, Dynatrace прекратил поддержку Xcode 16. Поддерживается только Xcode 26+.

Также учитывайте, что [правила публикации Apple App Store﻿](https://dt-url.net/we038fb) ограничат поддержку приложениями, собранными как минимум с Xcode 26, примерно в апреле 2026 года.

Начиная с версии OneAgent для iOS 8.343, Dynatrace прекратил поддержку iOS 12, iOS 13 и iOS 14. Минимальная поддерживаемая версия, iOS 15. Версия 8.341, последняя версия OneAgent для iOS с поддержкой iOS 12–14.