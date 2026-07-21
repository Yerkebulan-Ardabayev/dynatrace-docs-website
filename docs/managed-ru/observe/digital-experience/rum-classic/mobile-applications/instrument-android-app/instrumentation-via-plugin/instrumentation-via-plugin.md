---
title: Инструментирование приложения через плагин Gradle для Dynatrace Android в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/instrumentation-via-plugin
---

# Инструментирование приложения через плагин Gradle для Dynatrace Android в RUM Classic

# Инструментирование приложения через плагин Gradle для Dynatrace Android в RUM Classic

* Практическое руководство
* Чтение за 1 мин
* Обновлено 06 сен. 2023 г.

Если в проекте есть библиотечные модули, feature-модули, несколько модулей приложения или всего один build-файл, сначала нужно проверить соответствующий раздел в [Изменение настройки Dynatrace Android Gradle plugin в зависимости от структуры проекта в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-multi-module-projects "Использование Dynatrace Android Gradle plugin для менее распространённых архитектур проекта."). Шаги, необходимые для настройки Dynatrace Android Gradle plugin, могут немного отличаться для приложений с такими архитектурами.

Чтобы инструментировать Android-приложение с помощью Dynatrace Android Gradle plugin, выполни шаги ниже.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Убедиться, что объявлен репозиторий Maven Central.**](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/instrumentation-via-plugin#step-declare-maven-central "Выполни шаги из этого раздела перед началом инструментирования приложения с помощью Dynatrace Android Gradle plugin.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Добавить плагин в classpath build-скрипта.**](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/instrumentation-via-plugin#step-add-plugin "Выполни шаги из этого раздела перед началом инструментирования приложения с помощью Dynatrace Android Gradle plugin.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Применить плагин и добавить его конфигурационный фрагмент.**](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/instrumentation-via-plugin#step-apply-plugin-and-add-config-snippet "Выполни шаги из этого раздела перед началом инструментирования приложения с помощью Dynatrace Android Gradle plugin.")[![Шаг 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Шаг 4")

**Настроить конфигурацию плагина.**](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/instrumentation-via-plugin#step-customize-plugin-config "Выполни шаги из этого раздела перед началом инструментирования приложения с помощью Dynatrace Android Gradle plugin.")[![Шаг 5 опционально](https://dt-cdn.net/images/dotted-step-5-52040ae237.svg "Шаг 5 опционально")

**Расширить данные о пользовательском опыте на мобильных устройствах с помощью OneAgent SDK для Android.**](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/instrumentation-via-plugin#step-use-oneagent-sdk "Выполни шаги из этого раздела перед началом инструментирования приложения с помощью Dynatrace Android Gradle plugin.")

1. Убедиться, что объявлен репозиторий Maven Central.

   Dynatrace размещён на Maven Central. В файле настроек Gradle нужно проверить, что `mavenCentral()` добавлен в блоки `repositories` внутри `pluginManagement` и `dependencyResolutionManagement`. В [официальной документации Android﻿](https://dt-url.net/gradle-settings-file) можно посмотреть, как должен выглядеть файл настроек Gradle.

   Проекты с предыдущим шаблоном Android: убедиться, что объявлен репозиторий Maven Central.

   Может понадобиться добавить `mavenCentral()` во все блоки `repositories` в [build-файле верхнего уровня﻿](https://dt-url.net/top-level-build-file).

2. Добавить плагин в classpath build-скрипта.

   В [build-файле верхнего уровня﻿](https://dt-url.net/top-level-build-file) нужно добавить блок `buildscript` с блоком `dependencies` внутри и указать classpath плагина Dynatrace Android Gradle plugin (`com.dynatrace.tools.android:gradle-plugin`).

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

   Проекты с предыдущим шаблоном Android: добавить плагин в classpath build-скрипта.

   В build-файле верхнего уровня нужно найти блок `dependencies` внутри блока `buildscript` и добавить classpath плагина Dynatrace Android Gradle plugin (`com.dynatrace.tools.android:gradle-plugin`) после classpath build-скрипта [Android Gradle plugin﻿](https://developer.android.com/studio/build/index.html) (`com.android.tools.build:gradle`).

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

   Проекты с Gradle Plugin DSL: добавить плагин в блок Gradle Plugin DSL.

   В build-файле верхнего уровня нужно найти блок [plugins﻿](https://docs.gradle.org/current/userguide/plugins.html#sec:plugins_block) и добавить id `com.dynatrace.instrumentation` из [Plugin Marker Artifacts﻿](https://docs.gradle.org/current/userguide/plugins.html#sec:plugin_markers) плагина Dynatrace. После блока `plugins` нужно добавить конфигурацию плагина из [мастера инструментирования Android](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/get-started-with-android-monitoring#instrumentation-wizard "Узнай, какие шаги нужно выполнить для инструментирования Android-приложения для мониторинга с помощью Dynatrace.") с правильными значениями `applicationId` и `beaconUrl`.

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

   Пропустить шаг 3. При использовании Gradle Plugin DSL инструкция `apply` не нужна.

   Нужно использовать версию `8.+`, чтобы Gradle мог автоматически обновлять плагин при выходе новой минорной версии. Когда Dynatrace выпускает новую мажорную версию, нужно вручную перейти на новую версию: новая мажорная версия может содержать критические изменения, поэтому обычно требуется ручная корректировка.

3. Применить плагин и добавить его конфигурационный фрагмент.

   Нужно применить Dynatrace Android Gradle plugin с id плагина `com.dynatrace.instrumentation` в build-файле верхнего уровня.

   Затем нужно добавить фрагмент кода из шага 3 (**Применение плагина Dynatrace и добавление конфигурации плагина**) [мастера инструментирования Android](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/get-started-with-android-monitoring#instrumentation-wizard "Узнай, какие шаги нужно выполнить для инструментирования Android-приложения для мониторинга с помощью Dynatrace.") с правильными значениями `applicationId` и `beaconUrl`.

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

   Название конфигурации `sampleConfig` можно изменить на более осмысленное. Также можно определить разные конфигурации для разных [вариантов сборки Android﻿](https://dt-url.net/android-build-variants). Например, можно направлять данные вариантов `debug` и `release` в разные мобильные приложения в Dynatrace, используя [конфигурации для конкретных вариантов](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation#variant-specific-configs "Узнай, как настроить Dynatrace Android Gradle plugin для корректировки процесса автоматического инструментирования.").

4. Настроить конфигурацию плагина.

Фрагмент Gradle, скопированный из мастера инструментирования Android, содержит конфигурацию плагина по умолчанию. Одна и та же конфигурация используется для всех вариантов сборки Android, а наш плагин использует сенсоры по умолчанию и стандартные значения конфигурации OneAgent. По этой причине может понадобиться [настроить конфигурацию](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin#configuration "Learn how the Dynatrace Android Gradle plugin can auto-instrument your Android application project.") плагина Dynatrace Android Gradle.

5. Опционально: улучшить данные о пользовательском опыте на мобильных устройствах с помощью OneAgent SDK для Android.

   С помощью [OneAgent SDK для Android](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android "Learn how to enrich mobile user experience monitoring in Android using OneAgent SDK.") можно обогатить данные о пользовательском опыте на мобильных устройствах. Например, тегирование пользователей или отчёты о произвольных значениях доступны только через OneAgent SDK.