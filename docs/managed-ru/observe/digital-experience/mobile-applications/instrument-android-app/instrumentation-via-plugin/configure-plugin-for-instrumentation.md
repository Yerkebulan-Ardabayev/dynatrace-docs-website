---
title: Настройка Dynatrace Android Gradle plugin для процессов инструментирования
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation
scraped: 2026-05-12T11:32:49.093220
---

# Настройка Dynatrace Android Gradle plugin для процессов инструментирования

# Настройка Dynatrace Android Gradle plugin для процессов инструментирования

* How-to guide
* 11-min read
* Updated on Mar 26, 2026

Следующие параметры конфигурации позволяют настроить процесс инструментирования Dynatrace Android Gradle plugin.

## Конфигурации, специфичные для вариантов

Plugin позволяет задавать несколько конфигураций, специфичных для вариантов, где каждая такая конфигурация может применяться к нескольким [вариантам сборки Android](https://dt-url.net/android-build-variants). Необходимо предоставить конфигурацию, специфичную для варианта, для каждого варианта. Если plugin не может найти конфигурацию для определённого варианта сборки Android, он отменяет сборку и генерирует ошибку. Эту функцию защиты можно отключить с помощью свойства [`strictMode`](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.DynatraceExtension.html#com.dynatrace.tools.android.dsl.DynatraceExtension:strictMode).

Соответствие определяется регулярным выражением, заданным в свойстве [`variantFilter`](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.VariantConfiguration.html#com.dynatrace.tools.android.dsl.VariantConfiguration:variantFilter), и именем варианта сборки Android. Регулярное выражение чувствительно к регистру; если флейвор продукта не определён, тип сборки в имени варианта указывается в нижнем регистре. Если несколько конфигураций соответствуют одному и тому же варианту, выбирается и применяется первая из них.

Следующий пример показывает, как задать конфигурацию, специфичную для варианта, в блоке `dynatrace`:

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

### Разделение данных мониторинга для разработки и промышленной среды

Если вы не хотите смешивать данные мониторинга из сборок `debug` с данными промышленного мониторинга, разделите их. Для этого создайте два мобильных приложения в Dynatrace, сгенерируйте две конфигурации, специфичные для вариантов, и используйте предоставленные значения `applicationId` и `beaconUrl` со страницы **Instrumentation**.

### Отключение авто-инструментирования

Вы можете отключить авто-инструментирование для всех вариантов или для конкретного варианта.

Отключение авто-инструментирования для всех вариантов выполняется с помощью свойства [`pluginEnabled`](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.DynatraceExtension.html#com.dynatrace.tools.android.dsl.DynatraceExtension:pluginEnabled). При этом plugin по-прежнему добавляет OneAgent SDK как зависимость Gradle, чтобы компилятор мог компилировать вручную инструментированные файлы.

При этой настройке шаг верификации plugin'а деактивируется. Также деактивируется функция автозапуска, и приложение перестаёт отслеживаться. Если вы запустите агент вручную, приложение будет отслеживаться, но OneAgent сможет захватывать только данные мобильного пользовательского опыта, инструментированные ручными вызовами OneAgent SDK.

## Автоматический запуск OneAgent

Чтобы получить правильные параметры запуска, перейдите в **Instrumentation wizard** в Dynatrace.

1. Перейдите в **Mobile**.
2. Выберите мобильное приложение, которое нужно настроить.
3. В правом верхнем углу плитки с именем приложения нажмите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Instrumentation wizard**.
5. Выберите **Android**, затем перейдите на вкладку **Groovy (build.gradle)** или **Kotlin (build.gradle.kts)**.
6. Используйте предварительно настроенный фрагмент (см. шаг **Apply the Dynatrace plugin and add the plugin configuration**), уже заполненный значениями конфигурации из вашего мобильного приложения.

Все свойства, связанные с запуском OneAgent, являются частью [AutoStart DSL](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.StartOptions.html) и должны настраиваться через [блок `autoStart`](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.VariantConfiguration.html#com.dynatrace.tools.android.dsl.VariantConfiguration:autoStart(org.gradle.api.Action)):

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

Функция автоматического запуска OneAgent запускает OneAgent в методе `Application.onCreate`. Если ваше приложение поддерживает Direct Boot, необходимо отключить функцию автоматического запуска OneAgent. Также прочитайте раздел [Настройка взаимодействия с OneAgent SDK for Android](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/adjust-oneagent-communication "Настройте коммуникацию с OneAgent для отправки данных о пользовательском опыте в Dynatrace."), чтобы убедиться в возможности передачи данных OneAgent в кластер.

### Отключение автоматического запуска OneAgent

Отключить автоматический запуск OneAgent можно с помощью свойства [`enabled`](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.StartOptions.html#com.dynatrace.tools.android.dsl.StartOptions:enabled). Указывать свойства `applicationId` и `beaconUrl` нельзя, так как эти значения должны использоваться в вызове ручного запуска.

## Исключение определённых классов и методов

По умолчанию Dynatrace Android Gradle plugin инструментирует все пакеты. Для исключения определённых классов предусмотрено два варианта:

* Исключить список пакетов, классов и методов
* Использовать пользовательский фильтр исключений

### Исключение пакетов, классов и методов через свойства `packages`, `classes` и `methods`

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

Эти свойства имеют следующие дополнительные возможности:

* `packages` автоматически исключает дочерние пакеты
* `classes` автоматически исключает внутренние классы
* `methods` автоматически исключает все методы с одинаковым именем (независимо от сигнатуры метода)

Экранируйте символ `$` для внутренних классов, как показано в приведённом выше примере.

### Использование пользовательского фильтра исключений

Эта опция позволяет задать более гранулированную логику исключения через дополнительные правила фильтрации. В фильтре можно определить [регулярное выражение](https://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html) для `className`, `methodName` и `methodDescription`.

## Настройка инструментирования тестовых случаев

Plugin выполняет шаг авто-инструментирования только при сборке приложения. Поэтому поведение [локальных модульных тестов](https://developer.android.com/training/testing/unit-testing/local-unit-tests) и [инструментированных модульных тестов](https://developer.android.com/training/testing/unit-testing/instrumented-unit-tests) различается.

### Локальные модульные тесты

Локальные модульные тесты используют инструментированные классы из папки исходников, но неинструментированные библиотеки. Влияние на модульные тесты должно быть минимальным, поскольку plugin в основном инструментирует классы, специфичные для Android, а вызовы методов игнорируются, когда OneAgent не запущен.

### Инструментированные модульные тесты

Для запуска инструментированных модульных тестов на устройстве или эмуляторе сборка Android генерирует два APK-файла:

* APK-файл тестируемого приложения. Plugin участвует в этом процессе сборки и автоматически инструментирует APK-файл.
* Тестовый APK-файл, содержащий класс для тестирования другого APK. Plugin также участвует в этом процессе сборки, но не инструментирует тестовые APK.

Поскольку APK инструментирован, каждый инструментированный модульный тест отслеживается. В этом случае следует скорректировать конфигурацию: разделить данные мониторинга для разработки и промышленной среды или использовать отдельный тип сборки для модульных тестов.