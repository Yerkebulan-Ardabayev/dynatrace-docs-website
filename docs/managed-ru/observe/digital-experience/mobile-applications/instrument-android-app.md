---
title: Инструментирование Android-приложений
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/instrument-android-app
scraped: 2026-05-12T11:23:33.151912
---

# Инструментирование Android-приложений

# Инструментирование Android-приложений

* Overview
* 2-min read
* Updated on Oct 07, 2025

Процесс мониторинга пользовательского опыта нативных мобильных приложений принципиально отличается от мониторинга браузерных веб-приложений. Это связано с тем, что мониторинг мобильных приложений включает компиляцию, упаковку и доставку библиотеки мониторинга вместе с пакетом мобильного приложения.

Для использования Dynatrace в Android-приложении ознакомьтесь с [руководством по началу работы](/managed/observe/digital-experience/mobile-applications/instrument-android-app/get-started-with-android-monitoring "Изучите шаги, необходимые для инструментирования Android-приложения в целях мониторинга с помощью Dynatrace.") — оно содержит обзор необходимых шагов.

Также можно ознакомиться с нашим [демонстрационным мобильным приложением](https://dt-url.net/rs0229z), чтобы получить представление о том, как работает инструментирование с помощью Dynatrace. Это образцовое приложение демонстрирует основные функции, предоставляемые [плагином Dynatrace Android Gradle](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin "Узнайте, как плагин Dynatrace Android Gradle может автоматически инструментировать Android-проект приложения.") и [OneAgent SDK для Android](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk "Узнайте, что такое OneAgent SDK для Android.").

[Автоинструментирование Jetpack Compose](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#compose-instrumentation "Настройте плагин Dynatrace Android Gradle для изменения возможностей мониторинга OneAgent.") включено по умолчанию начиная с версии плагина Dynatrace Android Gradle 8.271.

Автоинструментирование Jetpack Compose для [Session Replay](/managed/observe/digital-experience/session-replay "Узнайте, как использовать Session Replay для лучшего понимания ошибок, с которыми сталкиваются ваши клиенты, и их устранения.") включено по умолчанию начиная с версии плагина Dynatrace Android Gradle 8.325.

### [Плагин Dynatrace Android Gradle](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin "Узнайте, как плагин Dynatrace Android Gradle может автоматически инструментировать Android-проект приложения.")

* [Инструментирование приложения через плагин Dynatrace Android Gradle](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/instrumentation-via-plugin "Выполните шаги, описанные в этом разделе, прежде чем начинать инструментирование приложения с помощью плагина Dynatrace Android Gradle.")
* [Настройка возможностей мониторинга плагина Dynatrace Android Gradle](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities "Настройте плагин Dynatrace Android Gradle для изменения возможностей мониторинга OneAgent.")
* [Настройка плагина Dynatrace Android Gradle для процессов инструментирования](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation "Узнайте, как настроить плагин Dynatrace Android Gradle для изменения процесса автоинструментирования.")
* [Настройка конфигурации OneAgent через плагин Dynatrace Android Gradle](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/adjust-oneagent-configuration "Узнайте, как настроить плагин Dynatrace Android Gradle для изменения конфигурации OneAgent SDK.")
* [Изменение конфигурации плагина Dynatrace Android Gradle в зависимости от структуры проекта](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-multi-module-projects "Используйте плагин Dynatrace Android Gradle для нестандартных архитектур проекта.")
* [Устранение неполадок плагина Dynatrace Android Gradle](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/faqs "Узнайте о проблемах, которые могут возникнуть при использовании плагина Dynatrace Android Gradle.")

### [OneAgent SDK для Android](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk "Узнайте, что такое OneAgent SDK для Android.")

* [Инструментирование через OneAgent SDK для Android](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android "Узнайте, как расширить мониторинг мобильного пользовательского опыта на Android с помощью OneAgent SDK.")
* [Настройка взаимодействия с OneAgent SDK для Android](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/adjust-oneagent-communication "Настройте взаимодействие с OneAgent для передачи данных о пользовательском опыте в Dynatrace.")
* [Ручное инструментирование приложения с помощью OneAgent SDK для Android](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/manual-instrumentation "Используйте OneAgent SDK для Android для ручного инструментирования Android-приложения.")

### Конфиденциальность данных

[Настройка параметров конфиденциальности данных для мобильных приложений](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile "Используйте параметры конфиденциальности Dynatrace, чтобы обеспечить соответствие мобильных приложений требованиям законодательства о защите данных в вашем регионе.")

[Руководство по безопасности данных для Android](/managed/manage/data-privacy-and-security/data-privacy/user-privacy-for-android "Информация о типах данных, которые OneAgent для Android собирает. Эта страница пригодится при заполнении формы о безопасности данных в Google Play Console.")

### Устранение неполадок

[Mobile applications: Issues with mobile RUM](https://dt-url.net/82038db)

[Mobile applications: General issues with Dynatrace Android Gradle plugin](https://dt-url.net/b9238e6)

[Mobile applications: Build issues with Dynatrace Android Gradle plugin](https://dt-url.net/wd438of)

Начиная с версии плагина [Dynatrace Android Gradle 8.261+](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin "Узнайте, как плагин Dynatrace Android Gradle может автоматически инструментировать Android-проект приложения.") Java 8 больше не поддерживается, так как для последней версии Android Gradle plugin API требуется Java 11.

## Связанные темы

* [Настройка Session Replay для Android](/managed/observe/digital-experience/session-replay/session-replay-android "Настройте Session Replay для Android-приложений, чтобы узнать, какие действия выполняют пользователи.")
* [Инструментирование мобильных приложений с помощью пакета Dynatrace Xamarin NuGet](/managed/observe/digital-experience/mobile-applications/cross-platform-frameworks/xamarin-nuget "Выполняйте мониторинг Xamarin-приложений с помощью Dynatrace OneAgent.")