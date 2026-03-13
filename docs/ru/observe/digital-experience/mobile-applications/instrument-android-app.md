---
title: Instrument Android apps
source: https://www.dynatrace.com/docs/observe/digital-experience/mobile-applications/instrument-android-app
scraped: 2026-03-05T21:26:31.388242
---

# Инструментирование Android-приложений

# Инструментирование Android-приложений

* Classic
* Обзор
* Чтение: 2 мин
* Обновлено 7 октября 2025

Процесс мониторинга пользовательского опыта нативных мобильных приложений отличается от мониторинга браузерных веб-приложений. Это связано с тем, что мониторинг мобильных приложений включает компиляцию, упаковку и доставку библиотеки мониторинга вместе с пакетом вашего мобильного приложения.

Чтобы использовать Dynatrace для вашего Android-приложения, ознакомьтесь с [руководством по началу работы](/docs/observe/digital-experience/mobile-applications/instrument-android-app/get-started-with-android-monitoring "Узнайте, какие шаги необходимо выполнить для инструментирования вашего Android-приложения для мониторинга с помощью Dynatrace."), в котором представлен обзор необходимых шагов.

Вы также можете изучить наше новое [демонстрационное мобильное приложение](https://dt-url.net/rs0229z), чтобы понять, как работает инструментирование с помощью Dynatrace. Это демонстрационное приложение показывает основные возможности, предоставляемые [Dynatrace Android Gradle Plugin](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin "Узнайте, как Dynatrace Android Gradle Plugin может автоматически инструментировать ваш проект Android-приложения.") и [OneAgent SDK для Android](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk "Узнайте, что такое OneAgent SDK для Android.").

[Автоматическое инструментирование Jetpack Compose](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#compose-instrumentation "Настройте Dynatrace Android Gradle Plugin для изменения возможностей мониторинга OneAgent.") включено по умолчанию начиная с Dynatrace Android Gradle Plugin версии 8.271.

Автоматическое инструментирование Jetpack Compose для [Session Replay](/docs/observe/digital-experience/session-replay "Узнайте, как использовать Session Replay для лучшего понимания и устранения ошибок, с которыми сталкиваются ваши клиенты.") включено по умолчанию начиная с Dynatrace Android Gradle Plugin версии 8.325.

### [Dynatrace Android Gradle Plugin](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin "Узнайте, как Dynatrace Android Gradle Plugin может автоматически инструментировать ваш проект Android-приложения.")

* [Инструментирование приложения с помощью Dynatrace Android Gradle Plugin](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/instrumentation-via-plugin "Выполните шаги этого раздела перед началом инструментирования вашего приложения с помощью Dynatrace Android Gradle Plugin.")
* [Настройка возможностей мониторинга Dynatrace Android Gradle Plugin](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities "Настройте Dynatrace Android Gradle Plugin для изменения возможностей мониторинга OneAgent.")
* [Настройка Dynatrace Android Gradle Plugin для процессов инструментирования](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation "Узнайте, как настроить Dynatrace Android Gradle Plugin для изменения процесса автоматического инструментирования.")
* [Настройка конфигурации OneAgent через Dynatrace Android Gradle Plugin](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/adjust-oneagent-configuration "Узнайте, как настроить Dynatrace Android Gradle Plugin для изменения конфигурации OneAgent SDK.")
* [Изменение конфигурации Dynatrace Android Gradle Plugin на основе структуры проекта](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-multi-module-projects "Используйте Dynatrace Android Gradle Plugin для менее распространённых архитектур проектов.")
* [Устранение неполадок Dynatrace Android Gradle Plugin](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/faqs "Узнайте о проблемах, которые могут возникнуть при использовании Dynatrace Android Gradle Plugin.")

### [OneAgent SDK для Android](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk "Узнайте, что такое OneAgent SDK для Android.")

* [Инструментирование с помощью OneAgent SDK для Android](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android "Узнайте, как обогатить мониторинг пользовательского опыта в Android с помощью OneAgent SDK.")
* [Настройка связи с OneAgent SDK для Android](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/adjust-oneagent-communication "Настройте связь с OneAgent для передачи данных о пользовательском опыте в Dynatrace.")
* [Ручное инструментирование приложения с помощью OneAgent SDK для Android](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/manual-instrumentation "Используйте OneAgent SDK для Android для ручного инструментирования вашего Android-приложения.")

### Конфиденциальность данных

[Настройка параметров конфиденциальности данных для мобильных приложений](/docs/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile "Используйте настройки конфиденциальности Dynatrace для обеспечения соответствия ваших мобильных приложений нормативным требованиям по защите данных вашего региона.")

[Руководство по безопасности данных для Android](/docs/manage/data-privacy-and-security/data-privacy/user-privacy-for-android "Информация о типах данных, которые собирает OneAgent для Android. Вы можете использовать эту страницу при заполнении формы Data safety в Google Play Console.")

### Устранение неполадок

[Мобильные приложения: проблемы с мобильным RUM](https://dt-url.net/82038db)

[Мобильные приложения: общие проблемы с Dynatrace Android Gradle Plugin](https://dt-url.net/b9238e6)

[Мобильные приложения: проблемы сборки с Dynatrace Android Gradle Plugin](https://dt-url.net/wd438of)

Начиная с [Dynatrace Android Gradle Plugin версии 8.261+](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin "Узнайте, как Dynatrace Android Gradle Plugin может автоматически инструментировать ваш проект Android-приложения.") поддержка Java 8 прекращена, так как для последней версии Android Gradle Plugin API требуется Java 11.

## Связанные темы

* [Настройка Session Replay для Android](/docs/observe/digital-experience/session-replay/session-replay-android "Настройте Session Replay для ваших Android-приложений, чтобы узнать, какие действия выполняют ваши пользователи.")
* [Инструментирование мобильных приложений с помощью пакета Dynatrace Xamarin NuGet](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/xamarin-nuget "Мониторинг приложений Xamarin с помощью Dynatrace OneAgent.")
