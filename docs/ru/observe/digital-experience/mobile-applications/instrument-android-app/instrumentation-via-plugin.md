---
title: Dynatrace Android Gradle plugin
source: https://www.dynatrace.com/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin
scraped: 2026-03-05T21:26:36.781022
---

* 6 мин. чтения

Вы можете использовать Dynatrace Android Gradle plugin только для Android-проектов, которые используют [Android Gradle plugin](https://developer.android.com/studio/build/index.html) для сборки приложения. Dynatrace Android Gradle plugin следует применять к [файлу сборки верхнего уровня](https://dt-url.net/top-level-build-file) (`build.gradle` или `build.gradle.kts`), который расположен в корневой директории проекта. Такой подход позволяет плагину правильно настроить дочерние проекты Android и интегрировать процесс автоинструментирования в процесс сборки Android.

Dynatrace Android Gradle plugin размещён на [Maven Central](https://central.sonatype.com/artifact/com.dynatrace.tools.android/gradle-plugin/overview), а техническая документация доступна в виде [DSL reference](https://www.dynatrace.com/support/doc/javadoc/oneagent/android/gradle-plugin/dsl/).

Через несколько месяцев мы прекратим устанавливать cookies для доменов с файловой схемой для гибридных приложений. Подробности и необходимые действия см. в разделе [Отключение cookies для файловых доменов](instrumentation-via-plugin/adjust-oneagent-configuration.md#file-domain-cookies "Узнайте, как настроить Dynatrace Android Gradle plugin для изменения конфигурации OneAgent SDK.").

[Автоинструментирование Jetpack Compose](instrumentation-via-plugin/monitoring-capabilities.md#compose-instrumentation "Настройка Dynatrace Android Gradle plugin для настройки возможностей мониторинга OneAgent.") включено по умолчанию начиная с версии Dynatrace Android Gradle plugin 8.271.

## Требования

* Gradle версии 7.0.2+
* Android Gradle plugin версии 7.0+
* JVM: Java 11+

## Инструментирование

Dynatrace Android Gradle plugin использует инструментирование байт-кода для инструментирования вашего приложения. Он может инструментировать исходные файлы всех дочерних проектов и сторонних библиотек. С точки зрения производительности инструментирование байт-кода выполняется быстро и оказывает минимальное влияние на время сборки. Благодаря поддержке инкрементальных сборок и кэша сборки инструментирование приложений практически незаметно.

### Возможности, связанные с инструментированием

* Java и Kotlin: Dynatrace Android Gradle plugin поддерживает инструментирование классов Java и Kotlin. Он также поддерживает другие языки JVM.
* Обфускация и оптимизация: процесс автоинструментирования завершается до выполнения задачи Gradle [R8](https://android-developers.googleblog.com/2018/11/r8-new-code-shrinker-from-google-is.html). Если вы используете другой инструмент обфускации, убедитесь, что задача обфускации выполняется после процесса автоинструментирования.

  OneAgent для Android и его транзитивные зависимости предоставляют правила ProGuard, разработанные для R8. Если вы используете сторонние инструменты обфускации, вы несёте ответственность за то, чтобы эти инструменты были настроены для соблюдения необходимых правил keep. Несоблюдение этого требования может привести к ошибкам во время выполнения из-за неправильно обфусцированных классов.

  Если вы используете функции Android Gradle Plugin, такие как [`ignoreFrom`](https://android-developers.googleblog.com/2025/11/configure-and-troubleshoot-r8-keep-rules.html), для фильтрации правил keep из зависимостей, учтите, что это может повлиять на функциональность OneAgent.
* Безопасность и инструменты укрепления APK: инструментирование байт-кода происходит до обфускации и до того, как [Android Dexer (D8)](https://developer.android.com/studio/command-line/d8) преобразует байт-код `.class` в байт-код `.dex`, который может быть выполнен в Android Runtime. Поэтому плагин обеспечивает максимальную совместимость с другими инструментами безопасности и укрепления APK, которые вычисляют контрольные суммы для DEX-кода, такими как DexGuard и Arxan.

### Ограничения, связанные с инструментированием

Android Gradle plugin инструментирует только `AndroidManifest.xml` и другие файлы `.class`. Он не инструментирует следующие компоненты:

* Нативный код, например код, написанный с помощью [NDK](https://developer.android.com/ndk)
* Веб-компоненты, такие как файлы `.html` и `.js`
* Файлы ресурсов, такие как файлы макетов `.xml`

### Совместимость с другими инструментами мониторинга

Могут возникнуть проблемы совместимости с другими плагинами мониторинга производительности, особенно когда эти плагины инструментируют OneAgent для Android. Мы рекомендуем использовать только один плагин мониторинга производительности или убедиться путём ручного тестирования, что выбранные вами плагины совместимы.

## Сборка

### Возможности, связанные со сборкой

Dynatrace Android Gradle plugin поддерживает возможности, специфичные для сборки Gradle, включая следующие:

* Ускорение инкрементальных сборок за счёт изменения только классов и библиотек, что сокращает время инструментирования.
* [Кэш сборки](https://docs.gradle.org/current/userguide/build_cache.html) для сокращения времени сборки за счёт повторного использования результатов, полученных другими сборками.
* Dynatrace Android Gradle plugin версии 8.257+ [Кэш конфигурации](https://docs.gradle.org/current/userguide/configuration_cache.html) для сокращения времени сборки за счёт повторного использования кэшированного результата фазы конфигурации.
* [Apply Changes](https://developer.android.com/studio/run#apply-changes) для отправки изменений кода и ресурсов в работающее приложение без перезапуска. Перезапуск приложения требуется только при изменении конфигурации плагина или OneAgent.
* Процессы сборки для [Android App Bundles](https://developer.android.com/guide/app-bundle) и APK.
* [Сборка нескольких APK](https://developer.android.com/studio/build/configure-apk-splits#build-apks) через блок `splits`, чтобы шаг инструментирования выполнялся только один раз.
* Поддержка [Kotlin DSL](https://docs.gradle.org/current/userguide/kotlin_dsl.html) в файлах `build.gradle.kts`.

### Ограничения, связанные со сборкой

* **Библиотечные проекты Android**: Dynatrace Android Gradle plugin автоматически инструментирует только проекты приложений Android. Он не поддерживает автоинструментирование отдельных библиотечных проектов Android. Наш плагин автоматически инструментирует внутренние библиотеки, если вы добавляете их как зависимость в ваш проект приложения Android.
* **Свойство `excludes` Android Gradle plugin**: С помощью свойства [`excludes`](https://developer.android.com/reference/tools/gradle-api/7.4/com/android/build/api/variant/Instrumentation#excludes()) Android Gradle plugin вы можете отключить инструментирование для определённых классов. Это свойство аналогично свойству [`exclude`](instrumentation-via-plugin/configure-plugin-for-instrumentation.md#exclude-classes-and-methods "Узнайте, как настроить Dynatrace Android Gradle plugin для управления процессом автоинструментирования.") Dynatrace Android Gradle plugin. Однако при использовании свойства Dynatrace наш плагин по-прежнему инструментирует некоторые очень важные классы для обеспечения корректности инструментирования. При использовании свойства Android `excludes` все указанные классы не инструментируются, что может негативно повлиять на инструментирование.

## Конфигурация

Android Gradle plugin предоставляет широкий спектр параметров конфигурации для настройки сборки вашего Android-приложения и отслеживаемых данных мобильного пользовательского опыта.

Фрагмент Gradle со страницы **Instrumentation** и фрагменты Gradle из документации содержат примеры имён для конфигурации, специфичной для вариантов, например `sampleConfig`. Чтобы лучше понять это, ознакомьтесь с тем, как используются [конфигурации, специфичные для вариантов](instrumentation-via-plugin/configure-plugin-for-instrumentation.md#variant-specific-configs "Узнайте, как настроить Dynatrace Android Gradle plugin для управления процессом автоинструментирования.").

### Настройка возможностей мониторинга

Следующие параметры можно использовать для настройки возможностей мониторинга OneAgent SDK для Android и тонкой настройки процесса автоинструментирования.

* [Мониторинг действий пользователя](instrumentation-via-plugin/monitoring-capabilities.md#user-action-monitoring "Настройка Dynatrace Android Gradle plugin для настройки возможностей мониторинга OneAgent.")
* [Мониторинг действий пользователя для Jetpack Compose](instrumentation-via-plugin/monitoring-capabilities.md#compose-instrumentation "Настройка Dynatrace Android Gradle plugin для настройки возможностей мониторинга OneAgent.")
* [Мониторинг веб-запросов](instrumentation-via-plugin/monitoring-capabilities.md#web-request-monitoring "Настройка Dynatrace Android Gradle plugin для настройки возможностей мониторинга OneAgent.")
* [Мониторинг жизненного цикла](instrumentation-via-plugin/monitoring-capabilities.md#lifecycle-monitoring "Настройка Dynatrace Android Gradle plugin для настройки возможностей мониторинга OneAgent.")
* [Отчёты о сбоях](instrumentation-via-plugin/monitoring-capabilities.md#crash-reporting "Настройка Dynatrace Android Gradle plugin для настройки возможностей мониторинга OneAgent.")
* [Обнаружение яростных нажатий](instrumentation-via-plugin/monitoring-capabilities.md#rage-tap-detection "Настройка Dynatrace Android Gradle plugin для настройки возможностей мониторинга OneAgent.")
* [Мониторинг местоположения](instrumentation-via-plugin/monitoring-capabilities.md#location-monitoring "Настройка Dynatrace Android Gradle plugin для настройки возможностей мониторинга OneAgent.")

### Настройка процессов инструментирования

Плагин также предоставляет дополнительные параметры конфигурации для настройки процесса инструментирования:

* [Конфигурации, специфичные для вариантов](instrumentation-via-plugin/configure-plugin-for-instrumentation.md#variant-specific-configs "Узнайте, как настроить Dynatrace Android Gradle plugin для управления процессом автоинструментирования.")
* [Деактивация автоинструментирования](instrumentation-via-plugin/configure-plugin-for-instrumentation.md#deactivate-auto-instrumentation "Узнайте, как настроить Dynatrace Android Gradle plugin для управления процессом автоинструментирования.")
* [Автоматический запуск OneAgent](instrumentation-via-plugin/configure-plugin-for-instrumentation.md#auto-startup "Узнайте, как настроить Dynatrace Android Gradle plugin для управления процессом автоинструментирования.")
* [Исключение определённых классов и методов](instrumentation-via-plugin/configure-plugin-for-instrumentation.md#exclude-certain-classes-and-methods "Узнайте, как настроить Dynatrace Android Gradle plugin для управления процессом автоинструментирования.")
* [Настройка инструментирования тестовых случаев](instrumentation-via-plugin/configure-plugin-for-instrumentation.md#adjust-test-case-instrumentation "Узнайте, как настроить Dynatrace Android Gradle plugin для управления процессом автоинструментирования.")

### Настройка конфигурации OneAgent

Следующие параметры конфигурации можно использовать для настройки конфигурации OneAgent по умолчанию:

* [Конфиденциальность данных](instrumentation-via-plugin/adjust-oneagent-configuration.md#data-privacy "Узнайте, как настроить Dynatrace Android Gradle plugin для изменения конфигурации OneAgent SDK.")
* [Гибридные приложения, использующие RUM JavaScript внутри `WebView`](instrumentation-via-plugin/adjust-oneagent-configuration.md#hybrid-apps "Узнайте, как настроить Dynatrace Android Gradle plugin для изменения конфигурации OneAgent SDK.")
* [Настройка поведения OneAgent](instrumentation-via-plugin/adjust-oneagent-configuration.md#adjust-oneagent-behavior "Узнайте, как настроить Dynatrace Android Gradle plugin для изменения конфигурации OneAgent SDK.")

Эти параметры особенно полезны при использовании совместно с автоматическим запуском OneAgent. Их также можно использовать для настройки конфигурации OneAgent при ручном запуске, но будьте осторожны, так как настройки могут быть легко переопределены с помощью `ConfigurationBuilder`.

### Настройка конфигурации Dynatrace Android Gradle plugin на основе структуры проекта

Наш плагин сканирует все дочерние проекты и настраивает процесс автоинструментирования для ваших модулей приложений. Другие модули не затрагиваются плагином. В этом случае вам может потребоваться настроить процесс инструментирования для Android-проекта с:

* [Библиотечными модулями](instrumentation-via-plugin/configure-multi-module-projects.md#library-modules "Использование Dynatrace Android Gradle plugin для менее типичных архитектур проектов.")
* [Модулями функций](instrumentation-via-plugin/configure-multi-module-projects.md#feature-modules "Использование Dynatrace Android Gradle plugin для менее типичных архитектур проектов.")
* [Несколькими модулями приложений](instrumentation-via-plugin/configure-multi-module-projects.md#multiple-application-modules "Использование Dynatrace Android Gradle plugin для менее типичных архитектур проектов.")
* [Несколькими модулями приложений и модулями функций](instrumentation-via-plugin/configure-multi-module-projects.md#application-and-feature-modules "Использование Dynatrace Android Gradle plugin для менее типичных архитектур проектов.")
* [Одним файлом сборки](instrumentation-via-plugin/configure-multi-module-projects.md#one-build-file "Использование Dynatrace Android Gradle plugin для менее типичных архитектур проектов.")
