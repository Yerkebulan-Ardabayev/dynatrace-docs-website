---
title: Dynatrace Android Gradle plugin
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin
scraped: 2026-05-12T11:23:09.966655
---

# Dynatrace Android Gradle plugin

# Dynatrace Android Gradle plugin

* Overview
* 6-min read
* Updated on Mar 05, 2026

Dynatrace Android Gradle plugin можно использовать только для Android-проектов, в которых для сборки приложения применяется [Android Gradle plugin](https://developer.android.com/studio/build/index.html). Dynatrace Android Gradle plugin следует применять к [корневому файлу сборки](https://dt-url.net/top-level-build-file) (либо `build.gradle`, либо `build.gradle.kts`), расположенному в корневом каталоге проекта. Такой подход позволяет plugin'у правильно настраивать дочерние Android-проекты и встраивать процесс авто-инструментирования в процесс сборки Android.

Dynatrace Android Gradle plugin размещён на [Maven Central](https://central.sonatype.com/artifact/com.dynatrace.tools.android/gradle-plugin/overview), техническая документация доступна в [DSL reference](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/).

В ближайшие несколько месяцев будет прекращена установка cookies для доменов файловой схемы в гибридных приложениях. Подробнее и о необходимых действиях см. в разделе [Отключение cookies для файловых доменов](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/adjust-oneagent-configuration#file-domain-cookies "Узнайте, как настроить Dynatrace Android Gradle plugin для изменения конфигурации OneAgent SDK.").

[Авто-инструментирование Jetpack Compose](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#compose-instrumentation "Настройте Dynatrace Android Gradle plugin для регулировки возможностей мониторинга OneAgent.") включено по умолчанию начиная с Dynatrace Android Gradle plugin версии 8.271.

## Требования

* Gradle версии 7.0.2+
* Android Gradle plugin версии 7.0+
* JVM: Java 11+

## Инструментирование

Dynatrace Android Gradle plugin использует инструментирование байткода для инструментирования приложения. Он может инструментировать исходные файлы всех дочерних проектов и сторонних библиотек. С точки зрения производительности инструментирование байткода работает быстро и оказывает минимальное влияние на время сборки. За счёт поддержки инкрементных сборок и кэша сборки инструментирование приложений практически незаметно.

### Особенности инструментирования

* Java и Kotlin: Dynatrace Android Gradle plugin поддерживает инструментирование классов Java и Kotlin, а также других JVM-языков.
* Обфускация и оптимизация: процесс авто-инструментирования завершается до задачи Gradle [R8](https://android-developers.googleblog.com/2018/11/r8-new-code-shrinker-from-google-is.html). При использовании другого инструмента обфускации необходимо убедиться, что задача обфускации выполняется после процесса авто-инструментирования.

  OneAgent for Android и его транзитивные зависимости предоставляют правила ProGuard, разработанные для R8. При использовании сторонних инструментов обфускации вы несёте ответственность за их правильную настройку с учётом требуемых правил сохранения. Несоблюдение этого требования может привести к ошибкам во время выполнения из-за неправильно обфусцированных классов.

  Если вы используете такие функции Android Gradle Plugin, как [`ignoreFrom`](https://android-developers.googleblog.com/2025/11/configure-and-troubleshoot-r8-keep-rules.html), для фильтрации правил сохранения из зависимостей, имейте в виду, что это может повлиять на функциональность OneAgent.
* Инструменты безопасности и усиления APK: инструментирование байткода происходит до обфускации и до того, как [Android Dexer (D8)](https://developer.android.com/studio/command-line/d8) преобразует байткод `.class` в байткод `.dex` для выполнения в Android Runtime. Поэтому plugin обеспечивает максимальную совместимость с другими инструментами, ориентированными на безопасность и усиление APK, которые вычисляют контрольные суммы для DEX-кода, например DexGuard и Arxan.

### Ограничения инструментирования

Android Gradle plugin инструментирует только `AndroidManifest.xml` и другие файлы `.class`. Следующие компоненты не инструментируются:

* Нативный код, например код, написанный с использованием [NDK](https://developer.android.com/ndk)
* Веб-компоненты, такие как файлы `.html` и `.js`
* Файлы ресурсов, например файлы разметки `.xml`

### Совместимость с другими инструментами мониторинга

Возможны проблемы совместимости с другими plugin'ами мониторинга производительности, особенно когда эти plugin'ы инструментируют OneAgent for Android. Рекомендуется либо использовать только один plugin мониторинга производительности, либо путём ручного тестирования убедиться в совместимости выбранных plugin'ов.

## Сборка

### Возможности, связанные со сборкой

Dynatrace Android Gradle plugin поддерживает специфические возможности Gradle, в том числе:

* Более быстрые инкрементные сборки за счёт изменения только классов и библиотек, что сокращает время инструментирования.
* [Кэш сборки](https://docs.gradle.org/current/userguide/build_cache.html) для сокращения времени сборки за счёт повторного использования результатов других сборок.
* Dynatrace Android Gradle plugin версии 8.257+ [Кэш конфигурации](https://docs.gradle.org/current/userguide/configuration_cache.html) для сокращения времени сборки за счёт повторного использования кэшированного результата фазы конфигурации.
* [Apply Changes](https://developer.android.com/studio/run#apply-changes) для применения изменений кода и ресурсов к запущенному приложению без его перезапуска. Перезапуск приложения требуется только при изменении конфигурации plugin'а или OneAgent.
* Процессы сборки для [Android App Bundles](https://developer.android.com/guide/app-bundle) и APK.
* [Множественные APK-сборки](https://developer.android.com/studio/build/configure-apk-splits#build-apks) через блок `splits`, при которых шаг инструментирования выполняется только один раз.
* Поддержка [Kotlin DSL](https://docs.gradle.org/current/userguide/kotlin_dsl.html) в файлах `build.gradle.kts`.

### Ограничения, связанные со сборкой

* **Android library projects**: Dynatrace Android Gradle plugin автоматически инструментирует только Android application projects. Авто-инструментирование автономных Android library projects не поддерживается. Plugin автоматически инструментирует внутренние библиотеки, если они добавлены как зависимость к вашему Android application project.
* **Свойство `excludes` Android Gradle plugin**: с помощью свойства [`excludes`](https://developer.android.com/reference/tools/gradle-api/7.4/com/android/build/api/variant/Instrumentation#excludes()) Android Gradle plugin можно отключить инструментирование для определённых классов. Это свойство аналогично свойству [`exclude`](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation#exclude-classes-and-methods "Узнайте, как настроить Dynatrace Android Gradle plugin для регулировки процесса авто-инструментирования.") Dynatrace Android Gradle plugin. Однако при использовании свойства Dynatrace наш plugin всё равно инструментирует ряд важных классов, чтобы инструментирование всегда оставалось корректным. При использовании свойства `excludes` Android все указанные классы не инструментируются, что может негативно сказаться на результатах инструментирования.

## Конфигурация

Android Gradle plugin предоставляет широкий спектр параметров конфигурации для настройки сборки Android-приложения и отслеживаемых данных о мобильном пользовательском опыте.

Фрагмент Gradle на странице **Instrumentation** и фрагменты Gradle из документации содержат примеры имён для конфигурации, специфичной для вариантов, например `sampleConfig`. Чтобы лучше разобраться в этом, ознакомьтесь с тем, как применяются [конфигурации, специфичные для вариантов](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation#variant-specific-configs "Узнайте, как настроить Dynatrace Android Gradle plugin для регулировки процесса авто-инструментирования.").

### Настройка возможностей мониторинга

Следующие параметры можно использовать для настройки возможностей мониторинга OneAgent SDK for Android и тонкой настройки процесса авто-инструментирования.

* [Мониторинг пользовательских действий](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#user-action-monitoring "Настройте Dynatrace Android Gradle plugin для регулировки возможностей мониторинга OneAgent.")
* [Мониторинг пользовательских действий для Jetpack Compose](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#compose-instrumentation "Настройте Dynatrace Android Gradle plugin для регулировки возможностей мониторинга OneAgent.")
* [Мониторинг веб-запросов](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#web-request-monitoring "Настройте Dynatrace Android Gradle plugin для регулировки возможностей мониторинга OneAgent.")
* [Мониторинг жизненного цикла](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#lifecycle-monitoring "Настройте Dynatrace Android Gradle plugin для регулировки возможностей мониторинга OneAgent.")
* [Фиксация сбоев](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#crash-reporting "Настройте Dynatrace Android Gradle plugin для регулировки возможностей мониторинга OneAgent.")
* [Обнаружение rage tap](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#rage-tap-detection "Настройте Dynatrace Android Gradle plugin для регулировки возможностей мониторинга OneAgent.")
* [Мониторинг местоположения](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#location-monitoring "Настройте Dynatrace Android Gradle plugin для регулировки возможностей мониторинга OneAgent.")

### Настройка процессов инструментирования

Plugin также предоставляет дополнительные параметры конфигурации для настройки процесса инструментирования:

* [Конфигурации, специфичные для вариантов](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation#variant-specific-configs "Узнайте, как настроить Dynatrace Android Gradle plugin для регулировки процесса авто-инструментирования.")
* [Отключение авто-инструментирования](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation#deactivate-auto-instrumentation "Узнайте, как настроить Dynatrace Android Gradle plugin для регулировки процесса авто-инструментирования.")
* [Автоматический запуск OneAgent](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation#auto-startup "Узнайте, как настроить Dynatrace Android Gradle plugin для регулировки процесса авто-инструментирования.")
* [Исключение определённых классов и методов](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation#exclude-certain-classes-and-methods "Узнайте, как настроить Dynatrace Android Gradle plugin для регулировки процесса авто-инструментирования.")
* [Настройка инструментирования тестовых случаев](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation#adjust-test-case-instrumentation "Узнайте, как настроить Dynatrace Android Gradle plugin для регулировки процесса авто-инструментирования.")

### Настройка конфигурации OneAgent

Следующие параметры конфигурации можно использовать для изменения конфигурации OneAgent по умолчанию:

* [Конфиденциальность данных](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/adjust-oneagent-configuration#data-privacy "Узнайте, как настроить Dynatrace Android Gradle plugin для изменения конфигурации OneAgent SDK.")
* [Гибридные приложения, использующие RUM JavaScript внутри `WebView`](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/adjust-oneagent-configuration#hybrid-apps "Узнайте, как настроить Dynatrace Android Gradle plugin для изменения конфигурации OneAgent SDK.")
* [Настройка поведения OneAgent](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/adjust-oneagent-configuration#adjust-oneagent-behavior "Узнайте, как настроить Dynatrace Android Gradle plugin для изменения конфигурации OneAgent SDK.")

Эти параметры особенно полезны при использовании совместно с функцией автоматического запуска OneAgent. Их также можно применять для настройки конфигурации OneAgent при ручном запуске, однако в этом случае следует учитывать, что настройки могут быть легко переопределены через `ConfigurationBuilder`.

### Настройка конфигурации Dynatrace Android Gradle plugin с учётом структуры проекта

Наш plugin сканирует все дочерние проекты и настраивает процесс авто-инструментирования для ваших модулей приложения. Другие модули plugin не затрагивает. В некоторых случаях может потребоваться скорректировать процесс инструментирования для Android-проекта с:

* [Модулями библиотек](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-multi-module-projects#library-modules "Используйте Dynatrace Android Gradle plugin для менее распространённых архитектур проектов.")
* [Функциональными модулями](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-multi-module-projects#feature-modules "Используйте Dynatrace Android Gradle plugin для менее распространённых архитектур проектов.")
* [Несколькими модулями приложения](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-multi-module-projects#multiple-application-modules "Используйте Dynatrace Android Gradle plugin для менее распространённых архитектур проектов.")
* [Несколькими модулями приложения и функциональными модулями](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-multi-module-projects#application-and-feature-modules "Используйте Dynatrace Android Gradle plugin для менее распространённых архитектур проектов.")
* [Одним файлом сборки](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-multi-module-projects#one-build-file "Используйте Dynatrace Android Gradle plugin для менее распространённых архитектур проектов.")