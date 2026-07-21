---
title: Изменение конфигурации плагина Dynatrace Android Gradle в зависимости от структуры проекта в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-multi-module-projects
---

# Изменение конфигурации плагина Dynatrace Android Gradle в зависимости от структуры проекта в RUM Classic

# Изменение конфигурации плагина Dynatrace Android Gradle в зависимости от структуры проекта в RUM Classic

* Практическое руководство
* Время чтения: 6 мин
* Обновлено 30 марта 2026 г.

Плагин Dynatrace Android Gradle сканирует все подпроекты и настраивает процесс автоматической инструментации для модулей приложения. На остальные модули плагин не влияет, поэтому в некоторых случаях процесс инструментации нужно скорректировать, например для модулей библиотек Android.

На этой странице описано поведение плагина Dynatrace Android Gradle и дополнительные шаги настройки, требуемые для определённых типов модулей и архитектур.

## Проекты с модулями библиотек

Все библиотеки Android/Java, а также все сторонние библиотеки автоматически инструментируются плагином, если они входят в состав проекта приложения Android. Дополнительная настройка не требуется, поскольку плагин имеет доступ ко всем зависимостям Gradle проекта приложения Android.

Чтобы обогатить данные о пользовательском опыте на мобильных устройствах, генерируемые модулями библиотек Android, добавь OneAgent SDK вручную как зависимость Gradle. Используй одну и ту же версию OneAgent SDK и плагина Dynatrace Android Gradle, а зависимость OneAgent SDK укажи через плагин Dynatrace Android Gradle.

Если проект содержит несколько модулей и OneAgent SDK нужен в каждом модуле библиотеки, используй следующий фрагмент кода.

Groovy

Kotlin

```
subprojects {



pluginManager.withPlugin("com.android.library") {



dependencies {



implementation com.dynatrace.tools.android.DynatracePlugin.agentDependency()



}



}



}
```

```
subprojects {



pluginManager.withPlugin("com.android.library") {



dependencies {



"implementation"(com.dynatrace.tools.android.DynatracePlugin.agentDependency())



}



}



}
```

Также можно использовать другие возможности Gradle, чтобы точнее настроить это поведение. Например, следующий фрагмент Gradle использует имя модуля, чтобы определить, нужно ли добавлять OneAgent SDK в конкретный модуль библиотеки Android.

Groovy

Kotlin

```
subprojects { project ->



pluginManager.withPlugin("com.android.library") {



if(project.name == 'firstLibrary' || project.name == 'secondLibrary') {



dependencies {



implementation com.dynatrace.tools.android.DynatracePlugin.agentDependency()



}



}



}



}
```

```
subprojects {



pluginManager.withPlugin("com.android.library") {



if(project.name == "firstLibrary" || project.name == "secondLibrary") {



dependencies {



"implementation"(com.dynatrace.tools.android.DynatracePlugin.agentDependency())



}



}



}



}
```

## Проекты с модулями функций

Для [Play Feature Delivery﻿](https://developer.android.com/guide/playcore/feature-delivery) приложение должно состоять из базового модуля и одного или нескольких модулей функций. Модули функций можно доставлять условно, загружать по требованию или запускать без установки.

Базовый модуль применяет плагин `com.android.application`, а модули функций, плагин `com.android.dynamic-feature`. При сборке приложения плагин Dynatrace Android Gradle автоматически инструментирует оба плагина, `com.android.application` и `com.android.dynamic-feature`, и для всех модулей используется одна и та же конфигурация.

Если включён [автоматический запуск OneAgent](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation#auto-startup "Узнай, как настроить плагин Dynatrace Android Gradle для корректировки процесса автоматической инструментации."), плагин инструментирует класс `Application` базового модуля. Это гарантирует, что OneAgent всегда работает, даже когда функция [доставляется мгновенно﻿](https://developer.android.com/topic/google-play-instant/overview).

### Мгновенная доставка и ручной запуск OneAgent

При мгновенной доставке пользователи могут взаимодействовать с функциями приложения без установки APK на устройство. Однако их устройствам нужно загрузить как базовый модуль, так и модуль функции с поддержкой мгновенного запуска. Подробнее см. [Google Play Instant﻿](https://developer.android.com/topic/google-play-instant/overview).

Если [автоматический запуск OneAgent отключён](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation#disable-auto-startup "Узнай, как настроить плагин Dynatrace Android Gradle для корректировки процесса автоматической инструментации.") для проекта с модулями функций, [запусти OneAgent вручную](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#start-oneagent "Узнай, как обогатить мониторинг пользовательского опыта на мобильных устройствах в Android с помощью OneAgent SDK.") внутри базового модуля, желательно в классе `Application` базового модуля. Так OneAgent будет готов к использованию, когда потребуется, и получится избежать возможных проблем, вызванных отложенным запуском OneAgent в других классах или внутри модуля функции.

### Инструментация вариантов сборки

Если [настроены варианты сборки﻿](https://dt-url.net/android-build-variants) через product flavors, используй одинаковые имена и измерения product flavor в каждом модуле.

При использовании свойства [`missingDimensionStrategy`﻿](https://developer.android.com/reference/tools/gradle-api/8.1/com/android/build/api/dsl/BaseFlavor#missingDimensionStrategy(kotlin.String,kotlin.String)) плагина Android Gradle убедись, что каждый вариант сборки в каждом модуле связан с правильной конфигурацией для конкретного варианта, скорректировав свойство [`variantFilter`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation#variant-specific-configs "Узнай, как настроить плагин Dynatrace Android Gradle для корректировки процесса автоматической инструментации."). Чтобы посмотреть, какая конфигурация используется для каждого варианта сборки, используй задачу [`printVariantAffiliation`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/javadoc/com/dynatrace/tools/android/PrintVariantAffiliationTask.html).

## Проекты с несколькими модулями приложений

Настройка Dynatrace Android Gradle plugin для проектов с несколькими модулями приложения похожа на настройку проекта, содержащего только один модуль приложения.

Чтобы инструментировать Android-проекты с несколькими модулями приложения, выполни следующие шаги.

1. Убедись, что репозиторий Maven Central объявлен.

   Dynatrace размещён в Maven Central. В файле настроек Gradle проверь, что `mavenCentral()` добавлен в блоки `repositories` внутри `pluginManagement` и `dependencyResolutionManagement`. Загляни в [официальную документацию Android﻿](https://dt-url.net/gradle-settings-file), чтобы посмотреть, как должен выглядеть файл настроек Gradle.

   Проекты с предыдущим шаблоном Android: убедись, что репозиторий Maven Central объявлен.

   Возможно, потребуется добавить `mavenCentral()` во все блоки `repositories` в [файле сборки верхнего уровня﻿](https://dt-url.net/top-level-build-file).

2. Добавь наш плагин в classpath скрипта сборки.

   В [файле сборки верхнего уровня﻿](https://dt-url.net/top-level-build-file) добавь блок `buildscript` с блоком `dependencies` внутри и укажи classpath Dynatrace Android Gradle plugin (`com.dynatrace.tools.android:gradle-plugin`).

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

   Проекты с предыдущим шаблоном Android: добавь наш плагин в classpath скрипта сборки.

   В файле сборки верхнего уровня найди блок `dependencies` внутри блока `buildscript` и добавь classpath Dynatrace Android Gradle plugin (`com.dynatrace.tools.android:gradle-plugin`) после classpath скрипта сборки [Android Gradle plugin﻿](https://developer.android.com/studio/build/index.html) (`com.android.tools.build:gradle`).

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

   Проекты с Gradle Plugin DSL: добавь наш плагин в блок Gradle Plugin DSL.

   В файле сборки верхнего уровня найди блок [plugins﻿](https://docs.gradle.org/current/userguide/plugins.html#sec:plugins_block) и добавь id `com.dynatrace.instrumentation` из Dynatrace [Plugin Marker Artifacts﻿](https://docs.gradle.org/current/userguide/plugins.html#sec:plugin_markers). После блока `plugins` добавь конфигурацию плагина из [мастера инструментирования Android](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/get-started-with-android-monitoring#instrumentation-wizard "Learn the steps you need to perform to instrument your Android app for monitoring with Dynatrace."), чтобы получить корректные значения `applicationId` и `beaconUrl`.

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

   Пропусти шаг 3. Инструкция `apply` не нужна, если используется Gradle Plugin DSL.

   Используй версию `8.+`, чтобы Gradle мог автоматически обновлять наш плагин при выходе новой минорной версии. Когда Dynatrace выпускает новую мажорную версию, обновляйся до неё вручную, новая мажорная версия может содержать breaking changes, поэтому обычно требуются ручные корректировки.
3. Примени наш плагин и добавь фрагмент его конфигурации.

   Примени Dynatrace Android Gradle plugin с id плагина `com.dynatrace.instrumentation.module` в [файле сборки уровня модуля﻿](https://developer.android.com/build#module-level) каждого модуля приложения.

   Затем добавь фрагмент кода из шага 3 (**Apply the Dynatrace plugin and add the plugin configuration**) [мастера инструментирования Android](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/get-started-with-android-monitoring#instrumentation-wizard "Learn the steps you need to perform to instrument your Android app for monitoring with Dynatrace."), чтобы получить корректные значения `applicationId` и `beaconUrl`.

   Groovy

   Kotlin

   ```
   apply plugin: 'com.dynatrace.instrumentation.module'



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
   apply(plugin = "com.dynatrace.instrumentation.module")



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

Название конфигурации `sampleConfig` можно поменять на более осмысленное. Также можно определить разные конфигурации для разных [Android build variants﻿](https://dt-url.net/android-build-variants). Например, можно отправлять данные вариантов `debug` и `release` в разные мобильные приложения в Dynatrace, используя [конфигурации для конкретных вариантов](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation#variant-specific-configs "Learn how to configure the Dynatrace Android Gradle plugin to adjust the auto-instrumentation process.").

4. Настрой конфигурацию плагина.

   Фрагмент Gradle, который ты скопировал из мастера инструментирования Android, содержит конфигурацию плагина по умолчанию. Эта же конфигурация используется для всех Android build variants, и наш плагин использует сенсоры по умолчанию и значения конфигурации OneAgent по умолчанию. По этой причине может понадобиться [скорректировать конфигурацию](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin#configuration "Learn how the Dynatrace Android Gradle plugin can auto-instrument your Android application project.") Dynatrace Android Gradle plugin.

5. Опционально Расширь данные о пользовательском опыте мобильных пользователей с помощью OneAgent SDK для Android.

   С помощью [OneAgent SDK для Android](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android "Learn how to enrich mobile user experience monitoring in Android using OneAgent SDK.") можно обогатить данные о пользовательском опыте мобильных пользователей. Например, тегирование пользователей или отправка пользовательских значений доступны только через OneAgent SDK.

Чтобы настроить инструментирование для конкретного приложения, измени конфигурацию Dynatrace Android Gradle plugin в файле сборки этого приложения. На другие модули приложения это изменение конфигурации не повлияет.

## Проекты с несколькими модулями приложения и feature-модулями

Если Android-проект содержит модули, использующие плагин `com.android.dynamic-feature`, скопируй фрагмент кода из шага 3 инструкции выше в новый файл `.gradle`. Примени полученный файл в модуле приложения и во всех feature-модулях, принадлежащих этому модулю приложения. Чтобы применить файл `.gradle`, используй следующий фрагмент, как описано в [официальной документации Gradle﻿](https://docs.gradle.org/current/userguide/plugins.html#sec:script_plugins).

Groovy

Kotlin

```
apply from: 'other.gradle'
```

```
apply(from = "other.gradle.kts")
```

При таком подходе одна и та же конфигурация используется для всех модулей, принадлежащих одному приложению.

Использовать разные конфигурации для одного и того же feature-модуля, принадлежащего нескольким приложениям, невозможно.

## Проекты с одним файлом сборки

Если проект Android не следует [рекомендуемой архитектуре﻿](https://developer.android.com/studio/build#build-files) и содержит только один файл сборки, то файл сборки верхнего уровня и файл сборки модуля указывают на один и тот же файл сборки.

Чтобы инструментировать проекты Android только с одним файлом сборки, выполните шаги ниже. Там, где в инструкциях упоминается файл сборки верхнего уровня, используйте файл сборки своего проекта.

1. Убедитесь, что репозиторий Maven Central объявлен.

   Dynatrace размещён в Maven Central. В файле настроек Gradle проверьте, что `mavenCentral()` добавлен в блоки `repositories` внутри `pluginManagement` и `dependencyResolutionManagement`. В [официальной документации Android﻿](https://dt-url.net/gradle-settings-file) можно посмотреть, как должен выглядеть файл настроек Gradle.

   Проекты с предыдущим шаблоном Android: убедитесь, что репозиторий Maven Central объявлен.

   Возможно, потребуется добавить `mavenCentral()` во все блоки `repositories` в [файле сборки верхнего уровня﻿](https://dt-url.net/top-level-build-file).

2. Добавьте наш плагин в classpath скрипта сборки.

   В [файле сборки верхнего уровня﻿](https://dt-url.net/top-level-build-file) добавьте блок `buildscript` с блоком `dependencies` внутри и добавьте classpath плагина Android Gradle Dynatrace (`com.dynatrace.tools.android:gradle-plugin`).

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

   Проекты с предыдущим шаблоном Android: добавьте наш плагин в classpath скрипта сборки.

   В файле сборки верхнего уровня найдите блок `dependencies` внутри блока `buildscript` и добавьте classpath плагина Android Gradle Dynatrace (`com.dynatrace.tools.android:gradle-plugin`) после classpath скрипта сборки [Android Gradle plugin﻿](https://developer.android.com/studio/build/index.html) (`com.android.tools.build:gradle`).

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

   Проекты с Gradle Plugin DSL: добавьте наш плагин в блок Gradle Plugin DSL.

   В файле сборки верхнего уровня найдите блок [plugins﻿](https://docs.gradle.org/current/userguide/plugins.html#sec:plugins_block) и добавьте id `com.dynatrace.instrumentation` [Plugin Marker Artifacts﻿](https://docs.gradle.org/current/userguide/plugins.html#sec:plugin_markers) Dynatrace. После блока `plugins` добавьте конфигурацию плагина из [мастера инструментирования Android](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/get-started-with-android-monitoring#instrumentation-wizard "Learn the steps you need to perform to instrument your Android app for monitoring with Dynatrace."), чтобы указать правильные значения `applicationId` и `beaconUrl`.

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

   Пропустите шаг 3. Инструкция `apply` не нужна, если используется Gradle Plugin DSL.

   Используйте версию `8.+`, чтобы Gradle мог автоматически обновлять наш плагин при выходе новой минорной версии. Когда Dynatrace выпускает новую мажорную версию, переходите на неё вручную, новая мажорная версия может содержать breaking changes, поэтому обычно требуются ручные корректировки.
3. Примените наш плагин и добавьте фрагмент его конфигурации.

   Примените плагин Android Gradle Dynatrace с id плагина `com.dynatrace.instrumentation.module` в файле сборки. Убедитесь, что `com.dynatrace.instrumentation.module` применяется после плагина `com.android.application`, но до плагина `com.google.firebase.firebase-perf`, если он тоже используется.

   Затем добавьте фрагмент кода из шага 3 (**Apply the Dynatrace plugin and add the plugin configuration**) [мастера инструментирования Android](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/get-started-with-android-monitoring#instrumentation-wizard "Learn the steps you need to perform to instrument your Android app for monitoring with Dynatrace."), чтобы указать правильные значения `applicationId` и `beaconUrl`.

   Groovy

   Kotlin

   ```
   apply plugin: 'com.android.application'



   ...



   apply plugin: 'com.dynatrace.instrumentation.module'



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
   apply(plugin = "com.android.application")



   ...



   apply(plugin = "com.dynatrace.instrumentation.module")



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

   Название конфигурации `sampleConfig` можно изменить на более осмысленное. Также можно определить разные конфигурации для разных [вариантов сборки Android﻿](https://dt-url.net/android-build-variants). Например, можно передавать варианты `debug` и `release` в разные мобильные приложения Dynatrace, используя [конфигурации для конкретных вариантов](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation#variant-specific-configs "Learn how to configure the Dynatrace Android Gradle plugin to adjust the auto-instrumentation process.").

4. Настройте конфигурацию плагина.

   Фрагмент Gradle, скопированный из мастера инструментирования Android, содержит конфигурацию плагина по умолчанию. Одна и та же конфигурация используется для всех вариантов сборки Android, а наш плагин использует сенсоры по умолчанию и значения конфигурации OneAgent по умолчанию. По этой причине может понадобиться [скорректировать конфигурацию](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin#configuration "Learn how the Dynatrace Android Gradle plugin can auto-instrument your Android application project.") плагина Android Gradle Dynatrace.

5. Опционально. Расширьте данные о пользовательском опыте на мобильных устройствах с помощью OneAgent SDK для Android.

   С помощью [OneAgent SDK для Android](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android "Learn how to enrich mobile user experience monitoring in Android using OneAgent SDK.") можно обогатить данные о пользовательском опыте на мобильных устройствах. Например, теггирование пользователей или отправка пользовательских значений доступны только через OneAgent SDK.