---
title: Инструментирование Android-приложений в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app
---

# Инструментирование Android-приложений в RUM Classic

# Инструментирование Android-приложений в RUM Classic

* Обзор
* 2 мин на чтение
* Обновлено 10 июня 2026 г.

Процесс мониторинга пользовательского опыта нативных мобильных приложений отличается от мониторинга веб-приложений на основе браузера. Причина в том, что мониторинг мобильных приложений подразумевает компиляцию, упаковку и поставку библиотеки мониторинга вместе с пакетом собственного мобильного приложения.

Чтобы задействовать Dynatrace для Android-приложения, ознакомься с [руководством по началу работы](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/get-started-with-android-monitoring "Learn the steps you need to perform to instrument your Android app for monitoring with Dynatrace."), где описан обзор необходимых шагов.

[Автоинструментирование Jetpack Compose](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#compose-instrumentation "Configure the Dynatrace Android Gradle plugin to adjust the monitoring capabilities of OneAgent.") включено по умолчанию начиная с версии 8.271 плагина Dynatrace Android Gradle.

Автоинструментирование Jetpack Compose для [Session Replay](/managed/observe/digital-experience/session-replay "Learn how you can use Session Replay to better understand and troubleshoot errors experienced by your customers.") включено по умолчанию начиная с версии 8.325 плагина Dynatrace Android Gradle.

### [Плагин Dynatrace Android Gradle](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin "Learn how the Dynatrace Android Gradle plugin can auto-instrument your Android application project.")

* [Инструментирование приложения через плагин Dynatrace Android Gradle в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/instrumentation-via-plugin "Perform the steps in this topic before you begin instrumenting your app with the Dynatrace Android Gradle plugin.")
* [Настройка возможностей мониторинга плагина Dynatrace Android Gradle в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities "Configure the Dynatrace Android Gradle plugin to adjust the monitoring capabilities of OneAgent.")
* [Настройка плагина Dynatrace Android Gradle для процессов инструментирования в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation "Learn how to configure the Dynatrace Android Gradle plugin to adjust the auto-instrumentation process.")
* [Настройка конфигурации OneAgent через плагин Dynatrace Android Gradle в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/adjust-oneagent-configuration "Learn how to configure the Dynatrace Android Gradle plugin to modify the OneAgent SDK configuration.")
* [Изменение конфигурации плагина Dynatrace Android Gradle в зависимости от структуры проекта в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-multi-module-projects "Use the Dynatrace Android Gradle plugin for less common project architectures.")
* [Устранение неполадок плагина Dynatrace Android Gradle в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/faqs "Learn about the problems that might occur while using the Dynatrace Android Gradle plugin.")

### [OneAgent SDK для Android](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk "Learn what OneAgent SDK for Android is.")

* [Инструментирование через OneAgent SDK для Android в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android "Learn how to enrich mobile user experience monitoring in Android using OneAgent SDK.")
* [Настройка взаимодействия с OneAgent SDK для Android в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/adjust-oneagent-communication "Configure communication with OneAgent to report the user experience data to Dynatrace.")
* [Ручное инструментирование приложения с помощью OneAgent SDK для Android в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/manual-instrumentation "Use OneAgent SDK for Android to manually instrument your Android application.")

### Конфиденциальность данных

[Настройка параметров конфиденциальности данных для мобильных приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.")

[Рекомендации по безопасности данных для Android](/managed/manage/data-privacy-and-security/data-privacy/user-privacy-for-android "Information on types of data that OneAgent for Android collects. You can use this page when filling out the Data safety form in Google Play Console.")

### Устранение неполадок

[Мобильные приложения: проблемы с мобильным RUM﻿](https://dt-url.net/82038db)

[Мобильные приложения: общие проблемы с плагином Dynatrace Android Gradle﻿](https://dt-url.net/b9238e6)

[Мобильные приложения: проблемы сборки с плагином Dynatrace Android Gradle﻿](https://dt-url.net/wd438of)

## Связанные темы

* [Настройка Session Replay Classic для Android](/managed/observe/digital-experience/session-replay/session-replay-android "Set up Session Replay Classic for your Android apps to learn which actions your users perform.")
* [Инструментирование мобильных приложений с помощью пакета Dynatrace Xamarin NuGet в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/xamarin-nuget "Monitor Xamarin apps with Dynatrace OneAgent.")