---
title: Изменение конфигурации Dynatrace Android Gradle plugin с учётом структуры проекта
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-multi-module-projects
scraped: 2026-05-12T11:32:42.920563
---

# Изменение конфигурации Dynatrace Android Gradle plugin с учётом структуры проекта

# Изменение конфигурации Dynatrace Android Gradle plugin с учётом структуры проекта

* How-to guide
* 6-min read
* Updated on Mar 30, 2026

Dynatrace Android Gradle plugin сканирует все дочерние проекты и настраивает процесс авто-инструментирования для ваших модулей приложения. Другие модули plugin не затрагивает, поэтому в некоторых случаях может потребоваться скорректировать процесс инструментирования, например при использовании Android library modules.

На этой странице описывается поведение Dynatrace Android Gradle plugin и дополнительные шаги настройки, необходимые для определённых типов модулей и архитектур.

## Проекты с модулями библиотек

Все Android/Java-библиотеки, а также все сторонние библиотеки автоматически инструментируются нашим plugin'ом, если они входят в ваш Android application project. Дополнительная настройка не требуется, так как plugin имеет доступ ко всем зависимостям Gradle вашего Android application project.

Если вы хотите обогатить данные о мобильном пользовательском опыте, генерируемые вашими Android library modules, добавьте OneAgent SDK вручную как зависимость Gradle. Используйте одинаковую версию OneAgent SDK и Dynatrace Android Gradle plugin, и задайте зависимость OneAgent SDK через Dynatrace Android Gradle plugin.

Если у вас многомодульный проект и вы хотите использовать OneAgent SDK в каждом модуле библиотеки, используйте следующий фрагмент кода.

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

Для более тонкой настройки можно использовать другие функции Gradle. Например, следующий фрагмент Gradle использует имя модуля для определения того, нужно ли добавлять OneAgent SDK в конкретный Android library module.

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

## Проекты с функциональными модулями

Для [Play Feature Delivery](https://developer.android.com/guide/playcore/feature-delivery) приложение должно состоять из базового модуля и одного или нескольких функциональных модулей. Функциональные модули могут поставляться условно, загружаться по запросу или запускаться без установки.

Базовый модуль применяет plugin `com.android.application`, а функциональные модули — plugin `com.android.dynamic-feature`. При сборке приложения Dynatrace Android Gradle plugin автоматически инструментирует оба plugin'а — `com.android.application` и `com.android.dynamic-feature`, при этом для всех модулей используется одна и та же конфигурация.

При включённом [автоматическом запуске OneAgent](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation#auto-startup "Узнайте, как настроить Dynatrace Android Gradle plugin для регулировки процесса авто-инструментирования.") наш plugin инструментирует класс `Application` базового модуля. Это гарантирует постоянную работу OneAgent, даже когда функция [поставляется мгновенно](https://developer.android.com/topic/google-play-instant/overview).

### Мгновенная поставка и ручной запуск OneAgent

При мгновенной поставке пользователи могут взаимодействовать с функциями приложения без установки APK на свои устройства. Однако устройства должны загрузить как базовый модуль, так и функциональный модуль с поддержкой мгновенного запуска. Подробнее см. в разделе [Google Play Instant](https://developer.android.com/topic/google-play-instant/overview).

Если вы [отключили автоматический запуск OneAgent](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation#disable-auto-startup "Узнайте, как настроить Dynatrace Android Gradle plugin для регулировки процесса авто-инструментирования.") для проекта с функциональными модулями, [запустите OneAgent вручную](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#start-oneagent "Узнайте, как расширить мониторинг пользовательского опыта на Android с помощью OneAgent SDK.") в базовом модуле, предпочтительно в классе `Application` базового модуля. Это обеспечит готовность OneAgent к работе при необходимости и позволит избежать потенциальных проблем, вызванных поздним запуском OneAgent в других классах или в функциональном модуле.

### Инструментирование вариантов сборки

Если вы [настроили варианты сборки](https://dt-url.net/android-build-variants) через флейворы продукта, используйте одинаковые имена флейворов и измерений в каждом модуле.

При использовании свойства [`missingDimensionStrategy`](https://developer.android.com/reference/tools/gradle-api/8.1/com/android/build/api/dsl/BaseFlavor#missingDimensionStrategy(kotlin.String,kotlin.String)) Android Gradle plugin убедитесь, что каждый вариант сборки в каждом модуле связан с правильной конфигурацией, специфичной для варианта, скорректировав свойство [`variantFilter`](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation#variant-specific-configs "Узнайте, как настроить Dynatrace Android Gradle plugin для регулировки процесса авто-инструментирования."). Для просмотра того, какая конфигурация используется для каждого варианта сборки, воспользуйтесь задачей [`printVariantAffiliation`](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/javadoc/com/dynatrace/tools/android/PrintVariantAffiliationTask.html).

## Проекты с несколькими модулями приложения

Настройка Dynatrace Android Gradle plugin для проектов с несколькими модулями приложения аналогична настройке проекта с одним модулем приложения.

Выполните следующие шаги для инструментирования Android-проектов с несколькими модулями приложения.

1. Убедитесь, что репозиторий Maven Central объявлен.

   Dynatrace размещён на Maven Central. В файле настроек Gradle убедитесь, что `mavenCentral()` добавлен в блоки `repositories` разделов `pluginManagement` и `dependencyResolutionManagement`. Ознакомьтесь с [официальной документацией Android](https://dt-url.net/gradle-settings-file), чтобы понять, как должен выглядеть файл настроек Gradle.

   Проекты с предыдущим шаблоном Android: убедитесь, что репозиторий Maven Central объявлен.

   Возможно, вам потребуется добавить `mavenCentral()` во все блоки `repositories` в [корневом файле сборки](https://dt-url.net/top-level-build-file).

2. Добавьте наш plugin в classpath скрипта сборки.

   В [корневом файле сборки](https://dt-url.net/top-level-build-file) добавьте блок `buildscript` с блоком `dependencies` внутри и добавьте classpath Dynatrace Android Gradle plugin (`com.dynatrace.tools.android:gradle-plugin`).

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

3. Примените наш plugin и добавьте фрагмент его конфигурации.

   Примените Dynatrace Android Gradle plugin с идентификатором plugin'а `com.dynatrace.instrumentation.module` в [файле сборки на уровне модуля](https://developer.android.com/build#module-level) каждого модуля приложения.

   Затем добавьте фрагмент кода из шага 3 (**Apply the Dynatrace plugin and add the plugin configuration**) [мастера инструментирования Android](/managed/observe/digital-experience/mobile-applications/instrument-android-app/get-started-with-android-monitoring#instrumentation-wizard "Узнайте, какие шаги необходимо выполнить для инструментирования Android-приложения для мониторинга с Dynatrace."), чтобы использовать правильные значения `applicationId` и `beaconUrl`.

4. Настройте конфигурацию plugin'а.

   Фрагмент Gradle, скопированный из мастера инструментирования Android, содержит конфигурацию plugin'а по умолчанию. Для всех вариантов сборки Android используется одна и та же конфигурация, при этом наш plugin применяет сенсоры по умолчанию и значения конфигурации OneAgent по умолчанию. По этой причине вы можете захотеть [настроить конфигурацию](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin#configuration "Узнайте, как Dynatrace Android Gradle plugin может автоматически инструментировать ваш Android-проект.") Dynatrace Android Gradle plugin.

5. Необязательно: расширьте данные о мобильном пользовательском опыте с помощью OneAgent SDK for Android.

   С помощью [OneAgent SDK for Android](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android "Узнайте, как расширить мониторинг пользовательского опыта на Android с помощью OneAgent SDK.") вы можете обогатить данные о мобильном пользовательском опыте. Например, тегирование пользователей или фиксация пользовательских значений доступны только через OneAgent SDK.

Чтобы настроить инструментирование для конкретного приложения, измените конфигурацию Dynatrace Android Gradle plugin в файле сборки этого приложения. Другие модули приложения не будут затронуты этим изменением конфигурации.

## Проекты с несколькими модулями приложения и функциональными модулями

Если ваш Android-проект содержит модули, использующие plugin `com.android.dynamic-feature`, скопируйте фрагмент кода из шага 3 инструкций выше в новый файл `.gradle`. Примените сгенерированный файл в модуле приложения и всех функциональных модулях, принадлежащих этому модулю приложения. Для применения файла `.gradle` используйте следующий фрагмент, как описано в [официальной документации Gradle](https://docs.gradle.org/current/userguide/plugins.html#sec:script_plugins).

Groovy

Kotlin

```
apply from: 'other.gradle'
```

```
apply(from = "other.gradle.kts")
```

При таком подходе одна и та же конфигурация используется для всех модулей, принадлежащих одному приложению.

Невозможно использовать разные конфигурации для одного и того же функционального модуля, принадлежащего нескольким приложениям.

## Проекты с одним файлом сборки

Если ваш Android-проект не следует [рекомендуемой архитектуре](https://developer.android.com/studio/build#build-files) и имеет только один файл сборки, корневой файл сборки и файл сборки на уровне модуля ссылаются на один и тот же файл.

Выполните следующие шаги для инструментирования Android-проектов с одним файлом сборки. Используйте файл сборки вашего проекта там, где в инструкциях упоминается корневой файл сборки.

1. Убедитесь, что репозиторий Maven Central объявлен.
2. Добавьте наш plugin в classpath скрипта сборки.
3. Примените наш plugin и добавьте фрагмент его конфигурации.

   Примените Dynatrace Android Gradle plugin с идентификатором plugin'а `com.dynatrace.instrumentation.module` в файле сборки. Убедитесь, что `com.dynatrace.instrumentation.module` применяется после plugin'а `com.android.application`, но до plugin'а `com.google.firebase.firebase-perf`, если он также используется.

4. Настройте конфигурацию plugin'а.

5. Необязательно: расширьте данные о мобильном пользовательском опыте с помощью OneAgent SDK for Android.