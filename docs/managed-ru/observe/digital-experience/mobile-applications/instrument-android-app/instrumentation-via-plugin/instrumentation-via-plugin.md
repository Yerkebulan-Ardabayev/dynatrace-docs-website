---
title: Инструментирование приложения через Dynatrace Android Gradle plugin
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/instrumentation-via-plugin
scraped: 2026-05-12T11:33:01.629670
---

# Инструментирование приложения через Dynatrace Android Gradle plugin

# Инструментирование приложения через Dynatrace Android Gradle plugin

* How-to guide
* 1-min read
* Updated on Sep 06, 2023

Если ваш проект содержит библиотечные модули, feature-модули, несколько модулей приложения или только один файл сборки, сначала ознакомьтесь с соответствующим разделом в [Изменение конфигурации Dynatrace Android Gradle plugin с учётом структуры проекта](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-multi-module-projects "Используйте Dynatrace Android Gradle plugin для менее распространённых архитектур проектов."). Шаги по настройке Dynatrace Android Gradle plugin могут немного отличаться для приложений с подобными архитектурами.

Выполните следующие шаги для инструментирования Android-приложения с помощью Dynatrace Android Gradle plugin.

1. Убедитесь, что репозиторий Maven Central объявлен.

   Dynatrace размещён в Maven Central. В файле настроек Gradle убедитесь, что `mavenCentral()` добавлен в блоки `repositories` в разделах `pluginManagement` и `dependencyResolutionManagement`. Ознакомьтесь с [официальной документацией Android](https://dt-url.net/gradle-settings-file), чтобы узнать, как должен выглядеть файл настроек Gradle.

   Для проектов с предыдущим шаблоном Android: убедитесь, что репозиторий Maven Central объявлен.

   Возможно, потребуется добавить `mavenCentral()` во все блоки `repositories` в [файле сборки верхнего уровня](https://dt-url.net/top-level-build-file).

2. Добавьте plugin в classpath скрипта сборки.

   В [файле сборки верхнего уровня](https://dt-url.net/top-level-build-file) добавьте блок `buildscript` с блоком `dependencies` внутри и добавьте classpath Dynatrace Android Gradle plugin (`com.dynatrace.tools.android:gradle-plugin`).

   Groovy

   Kotlin

   ```
   // add this entire block



   buildscript {



   dependencies {



   classpath 'com.dynatrace.tools.android:gradle-plugin:8.+'



   }



   }



   // this block already exists



   plugins {



   id 'com.android.application' version '8.1.0' apply false



   id 'com.android.library' version '8.1.0' apply false



   }
   ```

   ```
   // add this entire block



   buildscript {



   dependencies {



   classpath("com.dynatrace.tools.android:gradle-plugin:8.+")



   }



   }



   // this block already exists



   plugins {



   id("com.android.application") version "8.1.0" apply false



   id("com.android.library") version "8.1.0" apply false



   }
   ```

   Для проектов с предыдущим шаблоном Android: добавьте plugin в classpath скрипта сборки.

   В файле сборки верхнего уровня найдите блок `dependencies` внутри блока `buildscript` и добавьте classpath Dynatrace Android Gradle plugin (`com.dynatrace.tools.android:gradle-plugin`) после classpath скрипта сборки [Android Gradle plugin](https://developer.android.com/studio/build/index.html) (`com.android.tools.build:gradle`).

   Groovy

   Kotlin

   ```
   buildscript {



   repositories {



   google()



   mavenCentral() // hosts Dynatrace Android Gradle plugin



   }



   dependencies {



   // build script classpath of Android Gradle plugin



   classpath 'com.android.tools.build:gradle:<version>'



   // build script classpath of Dynatrace Android Gradle plugin; add this line to build.gradle file



   classpath 'com.dynatrace.tools.android:gradle-plugin:8.+'



   }



   }
   ```

   ```
   buildscript {



   repositories {



   google()



   mavenCentral() // hosts Dynatrace Android Gradle plugin



   }



   dependencies {



   // build script classpath of Android Gradle plugin



   classpath("com.android.tools.build:gradle:<version>")



   // build script classpath of Dynatrace Android Gradle plugin; add this line to build.gradle.kts file



   classpath("com.dynatrace.tools.android:gradle-plugin:8.+")



   }



   }
   ```

   Для проектов с Gradle Plugin DSL: добавьте plugin в блок Gradle Plugin DSL.

   В файле сборки верхнего уровня найдите блок [plugins](https://docs.gradle.org/current/userguide/plugins.html#sec:plugins_block) и добавьте id `com.dynatrace.instrumentation` Dynatrace [Plugin Marker Artifacts](https://docs.gradle.org/current/userguide/plugins.html#sec:plugin_markers). После блока `plugins` добавьте конфигурацию plugin'а из [мастера инструментирования Android](/managed/observe/digital-experience/mobile-applications/instrument-android-app/get-started-with-android-monitoring#instrumentation-wizard "Узнайте о шагах, необходимых для инструментирования Android-приложения для мониторинга в Dynatrace."), чтобы получить правильные значения `applicationId` и `beaconUrl`.

   Groovy

   Kotlin

   ```
   plugins {



   id 'com.android.application' version '8.5.0' apply false



   id 'com.dynatrace.instrumentation' version '8.+' apply true



   }



   dynatrace {



   configurations {



   sampleConfig {



   autoStart {



   applicationId = '<YourApplicationID>'



   beaconUrl = '<ProvidedBeaconURL>'



   }



   }



   }



   }
   ```

   ```
   plugins {



   id("com.android.application") version "8.5.0" apply false



   id("com.dynatrace.instrumentation") version "8.+" apply true



   }



   dynatrace {



   configurations {



   create("sampleConfig") {



   autoStart {



   applicationId("<YourApplicationID>")



   beaconUrl("<ProvidedBeaconURL>")



   }



   }



   }



   }
   ```

   Пропустите шаг 3. Оператор `apply` не нужен при использовании Gradle Plugin DSL.

   Используйте версию `8.+`, чтобы Gradle мог автоматически обновлять plugin при выходе новой минорной версии. При выпуске Dynatrace новой мажорной версии обновляйтесь вручную, так как новая мажорная версия может содержать критические изменения, требующие ручных настроек.

3. Примените plugin и добавьте фрагмент конфигурации.

   Примените Dynatrace Android Gradle plugin с ID plugin'а `com.dynatrace.instrumentation` в файле сборки верхнего уровня.

   Затем добавьте фрагмент кода из шага 3 (**Apply the Dynatrace plugin and add the plugin configuration**) [мастера инструментирования Android](/managed/observe/digital-experience/mobile-applications/instrument-android-app/get-started-with-android-monitoring#instrumentation-wizard "Узнайте о шагах, необходимых для инструментирования Android-приложения для мониторинга в Dynatrace."), чтобы получить правильные значения `applicationId` и `beaconUrl`.

   Groovy

   Kotlin

   ```
   apply plugin: 'com.dynatrace.instrumentation'



   dynatrace {



   configurations {



   sampleConfig {



   autoStart {



   applicationId '<YourApplicationID>'



   beaconUrl '<ProvidedBeaconURL>'



   }



   }



   }



   }
   ```

   ```
   apply(plugin = "com.dynatrace.instrumentation")



   configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



   configurations {



   create("sampleConfig") {



   autoStart {



   applicationId("<YourApplicationID>")



   beaconUrl("<ProvidedBeaconURL>")



   }



   }



   }



   }
   ```

   Имя конфигурации `sampleConfig` можно изменить на более понятное. Также можно определить разные конфигурации для разных [вариантов сборки Android](https://dt-url.net/android-build-variants). Например, можно отправлять данные вариантов `debug` и `release` в разные мобильные приложения в Dynatrace, используя [конфигурации, специфичные для вариантов](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation#variant-specific-configs "Узнайте, как настроить Dynatrace Android Gradle plugin для регулировки процесса авто-инструментирования.").

4. Настройте конфигурацию plugin'а.

   Фрагмент Gradle, скопированный из мастера инструментирования Android, содержит конфигурацию plugin'а по умолчанию. Она применяется ко всем вариантам сборки Android, а plugin использует сенсоры и значения конфигурации OneAgent по умолчанию. По этой причине вы можете [настроить конфигурацию](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin#configuration "Узнайте, как Dynatrace Android Gradle plugin может автоматически инструментировать проект Android-приложения.") Dynatrace Android Gradle plugin.

5. Опционально. Расширьте данные мобильного пользовательского опыта с помощью OneAgent SDK for Android.

   С помощью [OneAgent SDK for Android](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android "Узнайте, как расширить мониторинг мобильного пользовательского опыта на Android с помощью OneAgent SDK.") вы можете обогатить данные мобильного пользовательского опыта. Например, тегирование пользователей или отчёты о пользовательских значениях доступны только через OneAgent SDK.