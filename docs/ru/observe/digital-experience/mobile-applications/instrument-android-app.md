---
title: Инструментирование Android-приложений
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

Чтобы использовать Dynatrace для вашего Android-приложения, ознакомьтесь с [руководством по началу работы](instrument-android-app/get-started-with-android-monitoring.md "Узнайте, какие шаги необходимо выполнить для инструментирования вашего Android-приложения для мониторинга с помощью Dynatrace."), в котором представлен обзор необходимых шагов.

Вы также можете изучить наше новое [демонстрационное мобильное приложение](https://dt-url.net/rs0229z), чтобы понять, как работает инструментирование с помощью Dynatrace. Это демонстрационное приложение показывает основные возможности, предоставляемые [Dynatrace Android Gradle Plugin](instrument-android-app/instrumentation-via-plugin.md "Узнайте, как Dynatrace Android Gradle Plugin может автоматически инструментировать ваш проект Android-приложения.") и [OneAgent SDK для Android](instrument-android-app/instrumentation-via-oneagent-sdk.md "Узнайте, что такое OneAgent SDK для Android.").

[Автоматическое инструментирование Jetpack Compose](instrument-android-app/instrumentation-via-plugin/monitoring-capabilities.md#compose-instrumentation "Настройте Dynatrace Android Gradle Plugin для изменения возможностей мониторинга OneAgent.") включено по умолчанию начиная с Dynatrace Android Gradle Plugin версии 8.271.

Автоматическое инструментирование Jetpack Compose для [Session Replay](../session-replay.md "Узнайте, как использовать Session Replay для лучшего понимания и устранения ошибок, с которыми сталкиваются ваши клиенты.") включено по умолчанию начиная с Dynatrace Android Gradle Plugin версии 8.325.

### [Dynatrace Android Gradle Plugin](instrument-android-app/instrumentation-via-plugin.md "Узнайте, как Dynatrace Android Gradle Plugin может автоматически инструментировать ваш проект Android-приложения.")

* [Инструментирование приложения с помощью Dynatrace Android Gradle Plugin](instrument-android-app/instrumentation-via-plugin/instrumentation-via-plugin.md "Выполните шаги этого раздела перед началом инструментирования вашего приложения с помощью Dynatrace Android Gradle Plugin.")
* [Настройка возможностей мониторинга Dynatrace Android Gradle Plugin](instrument-android-app/instrumentation-via-plugin/monitoring-capabilities.md "Настройте Dynatrace Android Gradle Plugin для изменения возможностей мониторинга OneAgent.")
* [Настройка Dynatrace Android Gradle Plugin для процессов инструментирования](instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation.md "Узнайте, как настроить Dynatrace Android Gradle Plugin для изменения процесса автоматического инструментирования.")
* [Настройка конфигурации OneAgent через Dynatrace Android Gradle Plugin](instrument-android-app/instrumentation-via-plugin/adjust-oneagent-configuration.md "Узнайте, как настроить Dynatrace Android Gradle Plugin для изменения конфигурации OneAgent SDK.")
* [Изменение конфигурации Dynatrace Android Gradle Plugin на основе структуры проекта](instrument-android-app/instrumentation-via-plugin/configure-multi-module-projects.md "Используйте Dynatrace Android Gradle Plugin для менее распространённых архитектур проектов.")
* [Устранение неполадок Dynatrace Android Gradle Plugin](instrument-android-app/instrumentation-via-plugin/faqs.md "Узнайте о проблемах, которые могут возникнуть при использовании Dynatrace Android Gradle Plugin.")

### [OneAgent SDK для Android](instrument-android-app/instrumentation-via-oneagent-sdk.md "Узнайте, что такое OneAgent SDK для Android.")

* [Инструментирование с помощью OneAgent SDK для Android](instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android.md "Узнайте, как обогатить мониторинг пользовательского опыта в Android с помощью OneAgent SDK.")
* [Настройка связи с OneAgent SDK для Android](instrument-android-app/instrumentation-via-oneagent-sdk/adjust-oneagent-communication.md "Настройте связь с OneAgent для передачи данных о пользовательском опыте в Dynatrace.")
* [Ручное инструментирование приложения с помощью OneAgent SDK для Android](instrument-android-app/instrumentation-via-oneagent-sdk/manual-instrumentation.md "Используйте OneAgent SDK для Android для ручного инструментирования вашего Android-приложения.")

### Конфиденциальность данных

[Настройка параметров конфиденциальности данных для мобильных приложений](additional-configuration/configure-rum-privacy-mobile.md "Используйте настройки конфиденциальности Dynatrace для обеспечения соответствия ваших мобильных приложений нормативным требованиям по защите данных вашего региона.")

[Руководство по безопасности данных для Android](../../../manage/data-privacy-and-security/data-privacy/user-privacy-for-android.md "Информация о типах данных, которые собирает OneAgent для Android. Вы можете использовать эту страницу при заполнении формы Data safety в Google Play Console.")

### Устранение неполадок

[Мобильные приложения: проблемы с мобильным RUM](https://dt-url.net/82038db)

[Мобильные приложения: общие проблемы с Dynatrace Android Gradle Plugin](https://dt-url.net/b9238e6)

[Мобильные приложения: проблемы сборки с Dynatrace Android Gradle Plugin](https://dt-url.net/wd438of)

Начиная с [Dynatrace Android Gradle Plugin версии 8.261+](instrument-android-app/instrumentation-via-plugin.md "Узнайте, как Dynatrace Android Gradle Plugin может автоматически инструментировать ваш проект Android-приложения.") поддержка Java 8 прекращена, так как для последней версии Android Gradle Plugin API требуется Java 11.

## Связанные темы

* [Настройка Session Replay для Android](../session-replay/session-replay-android.md "Настройте Session Replay для ваших Android-приложений, чтобы узнать, какие действия выполняют ваши пользователи.")
* [Инструментирование мобильных приложений с помощью пакета Dynatrace Xamarin NuGet](cross-platform-frameworks/xamarin-nuget.md "Мониторинг приложений Xamarin с помощью Dynatrace OneAgent.")
