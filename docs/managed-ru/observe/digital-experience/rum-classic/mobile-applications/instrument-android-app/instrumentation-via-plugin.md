---
title: Плагин Dynatrace Android Gradle в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin
---

# Плагин Dynatrace Android Gradle в RUM Classic

# Плагин Dynatrace Android Gradle в RUM Classic

* Обзор
* 6 минут на чтение
* Обновлено 22 июня 2026 г.

Плагин Dynatrace Android Gradle можно использовать только для Android-проектов, в которых для сборки приложения применяется [Android Gradle plugin﻿](https://developer.android.com/studio/build/index.html). Плагин Dynatrace Android Gradle нужно применять к [файлу сборки верхнего уровня﻿](https://dt-url.net/top-level-build-file) (`build.gradle` или `build.gradle.kts`), который находится в корневом каталоге проекта. Такой подход позволяет плагину правильно настроить подпроекты Android и встроить процесс автоматической инструментации в процесс сборки Android.

Плагин Dynatrace Android Gradle размещён на [Maven Central﻿](https://central.sonatype.com/artifact/com.dynatrace.tools.android/gradle-plugin/overview), техническая документация доступна в виде [справочника DSL﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/).

Через пару месяцев прекратится установка cookie для доменов схемы file в гибридных приложениях. Подробнее и о необходимых действиях см. [Disable cookies for file domains](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/adjust-oneagent-configuration#file-domain-cookies "Learn how to configure the Dynatrace Android Gradle plugin to modify the OneAgent SDK configuration.").

[Автоматическая инструментация Jetpack Compose](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#compose-instrumentation "Configure the Dynatrace Android Gradle plugin to adjust the monitoring capabilities of OneAgent.") включена по умолчанию начиная с версии 8.271 плагина Dynatrace Android Gradle.

## Требования

* Gradle версии 8.0+
* Android Gradle plugin версии 8.1.1+
* JVM: Java 17+

## Инструментация

Плагин Dynatrace Android Gradle использует инструментацию байт-кода для инструментации приложения. Он может инструментировать исходные файлы всех подпроектов и сторонних библиотек. С точки зрения производительности инструментация байт-кода выполняется быстро и слабо влияет на время сборки. Благодаря поддержке инкрементальных сборок и кэша сборки инструментация приложений проходит практически незаметно.

### Особенности инструментации

* Java и Kotlin: плагин Dynatrace Android Gradle поддерживает инструментацию классов Java и Kotlin. Также поддерживаются другие языки JVM.
* Обфускация и оптимизация: процесс автоматической инструментации завершается до выполнения Gradle-задачи [R8﻿](https://android-developers.googleblog.com/2018/11/r8-new-code-shrinker-from-google-is.html). При использовании другого инструмента обфускации нужно убедиться, что задача обфускации выполняется после процесса автоматической инструментации.

  OneAgent для Android и его транзитивные зависимости предоставляют правила ProGuard, рассчитанные на R8. При использовании сторонних инструментов обфускации ответственность за то, что эти инструменты настроены с учётом необходимых правил сохранения (keep rules), лежит на пользователе. Несоблюдение этого требования может привести к ошибкам времени выполнения из-за некорректно обфусцированных классов.

  При использовании функций Android Gradle Plugin, таких как [`ignoreFrom`﻿](https://android-developers.googleblog.com/2025/11/configure-and-troubleshoot-r8-keep-rules.html), для исключения правил сохранения из зависимостей, нужно учитывать, что это может повлиять на работу OneAgent.
* Средства защиты и усиления защиты APK: инструментация байт-кода происходит до обфускации и до того, как [Android Dexer (D8)﻿](https://developer.android.com/studio/command-line/d8) преобразует байт-код `.class` в байт-код `.dex`, который может выполняться в Android Runtime. Поэтому плагин обеспечивает максимальную совместимость с другими инструментами, ориентированными на безопасность и усиление защиты APK, которые вычисляют контрольные суммы для DEX-кода, такими как DexGuard и Arxan.

### Ограничения инструментации

Плагин Android Gradle инструментирует только `AndroidManifest.xml` и другие файлы `.class`. Он не инструментирует следующие компоненты:

* Нативный код, например код, написанный с использованием [NDK﻿](https://developer.android.com/ndk)
* Веб-компоненты, например файлы `.html` и `.js`
* Файлы ресурсов, например файлы разметки `.xml`

### Совместимость с другими инструментами мониторинга

Возможны проблемы совместимости с другими плагинами мониторинга производительности, особенно если эти плагины инструментируют OneAgent для Android. Рекомендуется либо использовать только один плагин мониторинга производительности, либо путём ручного тестирования убедиться, что выбранные плагины совместимы друг с другом.

## Сборка

### Особенности сборки

Плагин Dynatrace Android Gradle поддерживает специфичные для сборки Gradle возможности, включая следующие:

* Более быстрые инкрементальные сборки за счёт изменения только классов и библиотек, что сокращает время инструментации.
* [Кэш сборки﻿](https://docs.gradle.org/current/userguide/build_cache.html) для сокращения времени сборки за счёт повторного использования результатов, полученных при других сборках.
* Плагин Dynatrace Android Gradle версии 8.257+ [Кэш конфигурации﻿](https://docs.gradle.org/current/userguide/configuration_cache.html) для сокращения времени сборки за счёт повторного использования кэшированного результата фазы конфигурации.
* [Apply Changes﻿](https://developer.android.com/studio/run#apply-changes) для передачи изменений кода и ресурсов в запущенное приложение без необходимости его перезапуска. Перезапуск приложения требуется только при изменении конфигурации плагина или OneAgent.
* Процессы сборки для [Android App Bundles﻿](https://developer.android.com/guide/app-bundle) и APK.
* [Сборка нескольких APK﻿](https://developer.android.com/studio/build/configure-apk-splits#build-apks) через блок `splits`, при этом шаг инструментации выполняется только один раз.
* Поддержка [Kotlin DSL﻿](https://docs.gradle.org/current/userguide/kotlin_dsl.html) в файлах `build.gradle.kts`.

### Ограничения сборки

* **Проекты Android-библиотек**: плагин Dynatrace Android Gradle автоматически инструментирует только проекты Android-приложений. Автоматическая инструментация отдельных (stand-alone) проектов Android-библиотек не поддерживается. Наш плагин автоматически инструментирует внутренние библиотеки, если добавить их в качестве зависимости в проект Android-приложения.
* **Свойство `excludes` плагина Android Gradle**: с помощью свойства [`excludes`﻿](https://developer.android.com/reference/tools/gradle-api/7.4/com/android/build/api/variant/Instrumentation#excludes()) плагина Android Gradle можно отключить инструментацию для отдельных классов. Это свойство похоже на свойство [`exclude`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation#exclude-classes-and-methods "Learn how to configure the Dynatrace Android Gradle plugin to adjust the auto-instrumentation process.") плагина Dynatrace Android Gradle. Однако при использовании свойства Dynatrace наш плагин всё равно инструментирует некоторые особенно важные классы, чтобы инструментация всегда оставалась корректной. При использовании свойства Android `excludes` все указанные классы не инструментируются, что может негативно повлиять на инструментацию.

## Конфигурация

Плагин Android Gradle предоставляет широкий набор параметров конфигурации для настройки сборки Android-приложения и данных о мониторинге пользовательского опыта на мобильных устройствах.

Фрагмент Gradle со страницы **Instrumentation** и фрагменты Gradle из документации содержат примеры имён для конфигураций, специфичных для варианта сборки, например `sampleConfig`. Подробнее о том, как используются [конфигурации для конкретных вариантов сборки](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation#variant-specific-configs "Learn how to configure the Dynatrace Android Gradle plugin to adjust the auto-instrumentation process."), см. по ссылке.

### Настройка возможностей мониторинга

Следующие параметры позволяют настроить OneAgent SDK для возможностей мониторинга Android и точнее настроить процесс автоматического инструментирования.

* [Мониторинг действий пользователя](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#user-action-monitoring "Настройка плагина Dynatrace Android Gradle для регулировки возможностей мониторинга OneAgent.")
* [Мониторинг действий пользователя для Jetpack Compose](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#compose-instrumentation "Настройка плагина Dynatrace Android Gradle для регулировки возможностей мониторинга OneAgent.")
* [Мониторинг веб-запросов](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#web-request-monitoring "Настройка плагина Dynatrace Android Gradle для регулировки возможностей мониторинга OneAgent.")
* [Мониторинг жизненного цикла](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#lifecycle-monitoring "Настройка плагина Dynatrace Android Gradle для регулировки возможностей мониторинга OneAgent.")
* [Отчёты о сбоях](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#crash-reporting "Настройка плагина Dynatrace Android Gradle для регулировки возможностей мониторинга OneAgent.")
* [Обнаружение раздражённых нажатий (rage tap)](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#rage-tap-detection "Настройка плагина Dynatrace Android Gradle для регулировки возможностей мониторинга OneAgent.")
* [Мониторинг местоположения](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#location-monitoring "Настройка плагина Dynatrace Android Gradle для регулировки возможностей мониторинга OneAgent.")

### Настройка процессов инструментирования

Плагин также предоставляет дополнительные параметры настройки для управления процессом инструментирования:

* [Конфигурации для конкретных вариантов](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation#variant-specific-configs "Как настроить плагин Dynatrace Android Gradle для регулировки процесса автоматического инструментирования.")
* [Отключение автоматического инструментирования](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation#deactivate-auto-instrumentation "Как настроить плагин Dynatrace Android Gradle для регулировки процесса автоматического инструментирования.")
* [Автоматический запуск OneAgent](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation#auto-startup "Как настроить плагин Dynatrace Android Gradle для регулировки процесса автоматического инструментирования.")
* [Исключение определённых классов и методов](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation#exclude-certain-classes-and-methods "Как настроить плагин Dynatrace Android Gradle для регулировки процесса автоматического инструментирования.")
* [Настройка инструментирования тестовых случаев](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation#adjust-test-case-instrumentation "Как настроить плагин Dynatrace Android Gradle для регулировки процесса автоматического инструментирования.")

### Настройка конфигурации OneAgent

Следующие параметры настройки можно использовать для изменения конфигурации OneAgent по умолчанию:

* [Конфиденциальность данных](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/adjust-oneagent-configuration#data-privacy "Как настроить плагин Dynatrace Android Gradle для изменения конфигурации OneAgent SDK.")
* [Гибридные приложения, использующие RUM JavaScript внутри `WebView`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/adjust-oneagent-configuration#hybrid-apps "Как настроить плагин Dynatrace Android Gradle для изменения конфигурации OneAgent SDK.")
* [Настройка поведения OneAgent](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/adjust-oneagent-configuration#adjust-oneagent-behavior "Как настроить плагин Dynatrace Android Gradle для изменения конфигурации OneAgent SDK.")

Эти параметры особенно полезны в сочетании с автоматическим запуском OneAgent. Их также можно использовать для настройки конфигурации OneAgent при ручном запуске, но в этом случае нужно действовать осторожно, поскольку настройки легко переопределяются через `ConfigurationBuilder`.

### Настройка конфигурации плагина Dynatrace Android Gradle с учётом структуры проекта

Плагин сканирует все подпроекты и настраивает процесс автоматического инструментирования для модулей приложения. На остальные модули плагин не влияет. В связи с этим может понадобиться скорректировать процесс инструментирования для Android-проекта со следующими компонентами:

* [Библиотечные модули](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-multi-module-projects#library-modules "Использование плагина Dynatrace Android Gradle для менее распространённых архитектур проекта.")
* [Feature-модули](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-multi-module-projects#feature-modules "Использование плагина Dynatrace Android Gradle для менее распространённых архитектур проекта.")
* [Несколько модулей приложения](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-multi-module-projects#multiple-application-modules "Использование плагина Dynatrace Android Gradle для менее распространённых архитектур проекта.")
* [Несколько модулей приложения и feature-модулей](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-multi-module-projects#application-and-feature-modules "Использование плагина Dynatrace Android Gradle для менее распространённых архитектур проекта.")
* [Один файл сборки](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-multi-module-projects#one-build-file "Использование плагина Dynatrace Android Gradle для менее распространённых архитектур проекта.")