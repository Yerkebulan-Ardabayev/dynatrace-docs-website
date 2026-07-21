---
title: Настройка плагина Dynatrace Android Gradle для процессов инструментации в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation
---

# Настройка плагина Dynatrace Android Gradle для процессов инструментации в RUM Classic

# Настройка плагина Dynatrace Android Gradle для процессов инструментации в RUM Classic

* Практическое руководство
* 11 минут чтения
* Обновлено 26 марта 2026 г.

Следующие параметры конфигурации позволяют настроить процесс инструментации плагина Dynatrace Android Gradle.

## Конфигурации для конкретных вариантов

Плагин позволяет задать несколько конфигураций для конкретных вариантов, при этом каждую такую конфигурацию можно применить к нескольким [вариантам сборки Android﻿](https://dt-url.net/android-build-variants). Нужно указать конфигурацию для каждого варианта. Если плагин не может найти конфигурацию для определённого варианта сборки Android, он отменяет сборку и выдаёт ошибку. Эту функцию защиты можно отключить с помощью свойства [`strictMode`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.DynatraceExtension.html#com.dynatrace.tools.android.dsl.DynatraceExtension:strictMode).

Связь определяется регулярным выражением, указанным в свойстве [`variantFilter`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.VariantConfiguration.html#com.dynatrace.tools.android.dsl.VariantConfiguration:variantFilter), и именем варианта сборки Android. Регулярное выражение чувствительно к регистру, и если продуктовый флейвор не задан, тип сборки в имени варианта пишется строчными буквами. Если нескольким конфигурациям для конкретных вариантов соответствует один и тот же вариант, выбирается и применяется первая конфигурация.

Следующий пример показывает, как задать конфигурацию для конкретного варианта в блоке `dynatrace`:

Groovy

Kotlin

```
dynatrace {



configurations {



dev {



// build type name is upper case because a product flavor is used



variantFilter "Debug"



// other variant-specific properties



}



demo {



// the first product flavor name is always lower case



variantFilter "demo"



// other variant-specific properties



}



prod {



// build type name is upper case because a product flavor is used



variantFilter "Release"



// other variant-specific properties



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("dev") {



// build type name is upper case because a product flavor is used



variantFilter("Debug")



// other variant-specific properties



}



create("demo") {



// the first product flavor name is always lower case



variantFilter("demo")



// other variant-specific properties



}



create("prod") {



// build type name is upper case because a product flavor is used



variantFilter("Release")



// other variant-specific properties



}



}



}
```

Например, есть приложение с двумя продуктовыми флейворами, `demo` и `paid`, и двумя типами сборки по умолчанию, `debug` и `release`. Плагин можно использовать для указания конфигурации для конкретного варианта для всех debug-вариантов сборки, `demoDebug` и `paidDebug`, и ещё двух конфигураций для конкретных вариантов для двух вариантов, `demoRelease` и `paidRelease`.

Связь между конфигурациями плагина для конкретных вариантов и вариантами сборки Android можно вывести с помощью задачи `printVariantAffiliation`. Например, следующий пример показывает вывод консоли для приведённого выше примера:

```
> Task :app:printVariantAffiliation



Variant 'demoDebug' will use configuration 'dev'



Variant 'demoRelease' will use configuration 'demo'



Variant 'paidDebug' will use configuration 'dev'



Variant 'paidRelease' will use configuration 'prod'
```

### Разделение данных мониторинга для разработки и продакшена

Если нежелательно засорять данные мониторинга продакшена данными мониторинга из `debug`-сборок, нужно отделить данные разработки от данных мониторинга продакшена.

Для этого нужно создать два мобильных приложения в Dynatrace. Нужно сгенерировать две конфигурации для конкретных вариантов и использовать предоставленные значения `applicationId` и `beaconUrl` со страницы `Instrumentation`.

Groovy

Kotlin

```
dynatrace {



configurations {



debug {



variantFilter "[dD]ebug"



autoStart {



applicationId '<DebugApplicationID>'



beaconUrl '<ProvidedBeaconURL>'



}



}



prod {



variantFilter "[rR]elease"



autoStart {



applicationId '<ProductionApplicationID>'



beaconUrl '<ProvidedBeaconURL>'



}



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("debug") {



variantFilter("[dD]ebug")



autoStart {



applicationId("<DebugApplicationID>")



beaconUrl("<ProvidedBeaconURL>")



}



}



create("prod") {



variantFilter("[rR]elease")



autoStart {



applicationId("<ProductionApplicationID>")



beaconUrl("<ProvidedBeaconURL>")



}



}



}



}
```

Если мониторинг `debug`-сборок не нужен, нужно отключить конфигурацию для конкретного варианта, отвечающую за `debug`-сборки.

Groovy

Kotlin

```
dynatrace {



configurations {



debug {



variantFilter "[dD]ebug"



enabled false



}



prod {



variantFilter "[rR]elease"



autoStart {



applicationId '<ProductionApplicationID>'



beaconUrl '<ProvidedBeaconURL>'



}



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("debug") {



variantFilter("[dD]ebug")



enabled(false)



}



create("prod") {



variantFilter("[rR]elease")



autoStart {



applicationId("<ProductionApplicationID>")



beaconUrl("<ProvidedBeaconURL>")



}



}



}



}
```

## Отключение автоинструментации

Автоинструментацию можно отключить для всех вариантов или для конкретного варианта.

### Отключение для всех вариантов

Чтобы отключить автоинструментацию для всех вариантов, нужно деактивировать плагин с помощью свойства [`pluginEnabled`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.DynatraceExtension.html#com.dynatrace.tools.android.dsl.DynatraceExtension:pluginEnabled). Плагин по-прежнему добавляет OneAgent SDK как Gradle-зависимость, чтобы компилятор мог скомпилировать файлы исходного кода, инструментированные вручную.

При этой настройке шаг верификации плагина отключается. Также отключается функция автозапуска, и мониторинг приложения прекращается. Если запустить агент вручную, приложение будет мониториться, но OneAgent сможет фиксировать только данные о мобильном пользовательском опыте, инструментированные вручную вызовами OneAgent SDK.

Автоинструментацию можно отключить для всех вариантов или для конкретного варианта.

Groovy

Kotlin

```
dynatrace {



pluginEnabled false



configurations {



dev {



// variant-specific properties



}



prod {



// variant-specific properties



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



pluginEnabled(false)



configurations {



create("dev") {



// variant-specific properties



}



create("prod") {



// variant-specific properties



}



}



}
```

### Отключение одного варианта

Если нужно отключить автоинструментацию для конкретного варианта, следует явно отключить конфигурацию для этого варианта с помощью свойства [`enabled`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.VariantConfiguration.html#com.dynatrace.tools.android.dsl.VariantConfiguration:enabled). Следующий пример показывает, как отключить все `debug`-типы сборки (варианты `demoDebug` и `paidDebug`):

Groovy

Kotlin

```
dynatrace {



configurations {



dev {



enabled false



variantFilter "Debug"



}



prod {



// variant-specific properties



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("dev") {



enabled(false)



variantFilter("Debug")



}



create("prod") {



// variant-specific properties



}



}



}
```

Пропуск автоинструментации при отсутствии конфигурации для конкретного варианта

Можно отключить свойство `strictMode` и задать конфигурацию для конкретного варианта только для того варианта, который нужно инструментировать. Плагин не инструментирует варианты сборки Android, если ни одна конфигурация для конкретного варианта не соответствует данному варианту сборки Android.

Если не отключить свойство `strictMode`, плагин отменяет сборку и выдаёт ошибку.
Такой подход не рекомендуется, поскольку функция строгого режима должна защищать от сборки вариантов без конфигурации для конкретного варианта. Автоинструментацию следует отключать через свойство `enabled` конфигурации для конкретного варианта.

Groovy

Kotlin

```
dynatrace {



strictMode false



configurations {



prod {



variantFilter "Release"



// other variant-specific properties



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



strictMode(false)



configurations {



create("prod") {



variantFilter("Release")



// other variant-specific properties



}



}



}
```

## Автоматический запуск OneAgent

Чтобы получить корректные параметры запуска, перейди в **Instrumentation wizard** в Dynatrace.

1. Перейди в **Mobile**.
2. Выбери мобильное приложение, которое нужно настроить.
3. Выбери **More** (**…**) > **Edit** в правом верхнем углу плитки с названием приложения.
4. В настройках приложения выбери **Instrumentation wizard**.
5. Выбери **Android**, затем перейди на вкладку **Groovy (build.gradle)** или **Kotlin (build.gradle.kts)**.
6. Используй заранее сконфигурированный сниппет (см. шаг **Apply the Dynatrace plugin and add the plugin configuration**), который уже заполнен значениями конфигурации из твоего мобильного приложения.

Все свойства запуска OneAgent, связанные со стартом, являются частью [AutoStart DSL﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.StartOptions.html) и должны настраиваться через [блок `autoStart`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.VariantConfiguration.html#com.dynatrace.tools.android.dsl.VariantConfiguration:autoStart(org.gradle.api.Action)):

Groovy

Kotlin

```
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

Функция автоматического запуска OneAgent запускает OneAgent в методе `Application.onCreate`. Если приложение поддерживает Direct Boot, функцию автоматического запуска OneAgent нужно деактивировать. Также стоит прочитать [Adjust communication with OneAgent SDK for Android in RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/adjust-oneagent-communication "Configure communication with OneAgent to report the user experience data to Dynatrace."), чтобы убедиться, что OneAgent способен передавать данные в кластер.

### Деактивация автоматического запуска OneAgent

Автоматический запуск OneAgent можно отключить через свойство [`enabled`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.StartOptions.html#com.dynatrace.tools.android.dsl.StartOptions:enabled). Указывать свойства `applicationId` и `beaconUrl` нельзя, поскольку эти значения должны использоваться в вызове ручного запуска.

Groovy

Kotlin

```
dynatrace {



configurations {



sampleConfig {



autoStart.enabled false



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("sampleConfig") {



autoStart.enabled(false)



}



}



}
```

Рекомендуется добавить вызов запуска в метод `Application.onCreate`. Подробнее см. [OneAgent SDK for Android > Start OneAgent](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#start-oneagent "Learn how to enrich mobile user experience monitoring in Android using OneAgent SDK.").

`autoStart.enabled` запускает OneAgent автоматически один раз для приложения. OneAgent нельзя запустить повторно в том же приложении, чтобы указать другие `appId` и `beaconUrl`, множественная одновременная инициализация не поддерживается.

Дополнительные изменения конфигурации, заданные через `DynatraceConfigurationBuilder`, переопределяют значения конфигурации, заданные через DSL плагина Dynatrace Android Gradle.

## Исключение определённых классов и методов

По умолчанию плагин Dynatrace Android Gradle инструментирует все пакеты. Если нужно исключить определённые классы, есть два варианта:

* Исключить список пакетов, классов и методов
* Использовать пользовательский фильтр исключений

### Исключение списка пакетов, классов и методов через свойства `packages`, `classes` и `methods`

Groovy

Kotlin

```
dynatrace {



configurations {



sampleConfig {



exclude {



packages "com.mypackage", "com.another.example"



classes "com.example.MyClass"



methods "com.example.ExampleClass.exampleMethod", "com.example.ExampleClass\$InnerClass.anotherMethod"



}



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("sampleConfig") {



exclude {



packages("com.mypackage", "com.another.example")



classes("com.example.MyClass")



methods("com.example.ExampleClass.exampleMethod", "com.example.ExampleClass\$InnerClass.anotherMethod")



}



}



}



}
```

Эти свойства содержат несколько дополнительных возможностей:

* `packages` автоматически исключает подпакеты
* `classes` автоматически исключает внутренние классы
* `methods` автоматически исключает все методы с одинаковым именем (независимо от сигнатуры метода)

Экранируй символ `$` для внутренних классов, как показано в примере выше.

### Использование пользовательского фильтра исключений

Этот вариант позволяет задать более гранулярную логику исключений через дополнительные правила фильтра. В фильтре можно задать [регулярное выражение﻿](https://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html) для `className`, `methodName` и `methodDescription`.

* Для свойства `className` используется полностью квалифицированное имя.
* Имя класса совпадает, когда заданное выражение находится где-либо в имени класса
* Имя метода совпадает, когда заданное выражение находится где-либо в имени метода
* [Описание метода﻿](https://docs.oracle.com/javase/specs/jvms/se8/html/jvms-4.html#jvms-4.3.3) совпадает, когда заданное выражение находится где-либо в описании метода

Groovy

Kotlin

```
dynatrace {



configurations {



sampleConfig {



exclude {



// exclude all inner classes



filter {



className "\$"



}



// exclude all methods that fulfill this requirements



filter {



// the class is part of the "com.example" package



className "^com\\.example\\."



// the method name contain the phrase "webrequest" (uppercase notation is ignored for two letters)



methodName "[wW]eb[rR]equest"



// where the last parameter is a String and where the return value is void



methodDescription "Ljava/lang/String;\\)V"



}



}



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("sampleConfig") {



exclude {



// exclude all inner classes



filter {



className("\$")



}



// exclude all methods that fulfill this requirements



filter {



// the class is part of the "com.example" package



className("^com\\.example\\.")



// the method name contain the phrase "webrequest" (uppercase notation is ignored for two letters)



methodName("[wW]eb[rR]equest")



// where the last parameter is a String and where the return value is void



methodDescription("Ljava/lang/String;\\)V")



}



}



}



}



}
```

## Настройка инструментирования тестовых сценариев

Плагин выполняет шаг автоинструментирования только при сборке приложения. Поэтому поведение [локальных модульных тестов﻿](https://developer.android.com/training/testing/unit-testing/local-unit-tests) и [инструментированных модульных тестов﻿](https://developer.android.com/training/testing/unit-testing/instrumented-unit-tests) отличается.

### Локальные модульные тесты

Локальные модульные тесты используют инструментированные классы из папки исходного кода, но неинструментированные библиотеки. На модульные тесты это не должно влиять, поскольку плагин преимущественно инструментирует классы, специфичные для Android, а вызовы методов игнорируются, когда OneAgent не запущен. Это также справедливо для вызовов методов OneAgent SDK.

### Локальные модульные тесты с Robolectric

[Robolectric﻿](https://robolectric.org/) позволяет симулировать Android в локальных модульных тестах. Robolectric использует инструментированные классы из папки исходного кода, но неинструментированные библиотеки.

Если [автоматический запуск OneAgent отключён](#disable-auto-startup) и OneAgent запущен вручную в классе `Application`, OneAgent работает и отслеживает тестовые сценарии Robolectric. В этом случае настройку конфигурации нужно скорректировать, либо [разделив данные мониторинга разработки и продакшена](#separate-development-and-prod-data), либо [используя другой тип сборки для модульных тестов](#use-diff-build-type-unit-tests).

### Инструментированные модульные тесты

Для запуска инструментированных модульных тестов на устройстве или эмуляторе сборка Android генерирует два APK-файла:

* APK-файл приложения, которое нужно протестировать. Плагин является частью этого процесса сборки и автоматически инструментирует этот APK-файл.
* Тестовый APK-файл, содержащий класс для тестирования другого APK. Плагин также является частью этого процесса сборки, но не инструментирует автоматически эти тестовые APK.

Поскольку APK инструментирован, отслеживается каждый инструментированный модульный тест. В этом случае настройку конфигурации нужно скорректировать, либо [разделив данные мониторинга разработки и продакшена](#separate-development-and-prod-data), либо [используя другой тип сборки для модульных тестов](#use-diff-build-type-unit-tests).

### Использование другого типа сборки для модульных тестов

Для настройки индивидуального поведения инструментации при модульном тестировании нужно с помощью плагина создать новый build type для модульных тестов.

Groovy

Kotlin

```
android {



buildTypes {



// build type used for unit tests in the CI



CI {



initWith debug



applicationIdSuffix ".debugTesting"



}



}



}
```

```
android {



buildTypes {



// build type used for unit tests in the CI



create("CI") {



initWith(getByName("debug"))



applicationIdSuffix = ".debugTesting"



}



}



}
```

Например, чтобы отслеживать сборки `debug`, которые используют разработчики, и при этом не отслеживать выполнение модульных тестов в CI, нужно использовать следующую конфигурацию:

Groovy

Kotlin

```
dynatrace {



configurations {



developer {



variantFilter "[dD]ebug"



autoStart {



applicationId '<DebugApplicationID>'



beaconUrl '<ProvidedBeaconURL>'



}



}



ciTesting {



// deactivate instrumentation for CI tests



variantFilter "CI"



enabled false



}



prod {



variantFilter "[rR]elease"



autoStart {



applicationId '<ProductionApplicationID>'



beaconUrl '<ProvidedBeaconURL>'



}



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("developer") {



variantFilter("[dD]ebug")



autoStart {



applicationId("<ProductionApplicationID>")



beaconUrl("<ProvidedBeaconURL>")



}



}



create("ciTesting") {



// deactivate instrumentation for CI tests



variantFilter("CI")



enabled(false)



}



create("prod") {



variantFilter("[rR]elease")



autoStart {



applicationId("<DebugApplicationID>")



beaconUrl("<ProvidedBeaconURL>")



}



}



}



}
```

При выполнении модульных тестов с вариантом `debug` они отслеживаются, потому что инструментация деактивирована только для варианта `CI`.