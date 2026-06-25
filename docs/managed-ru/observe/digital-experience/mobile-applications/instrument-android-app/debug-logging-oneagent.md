---
title: Включение отладочного журналирования для Dynatrace Android Gradle plugin или OneAgent SDK
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/instrument-android-app/debug-logging-oneagent
scraped: 2026-05-12T12:05:48.090151
---

# Включение отладочного журналирования для Dynatrace Android Gradle plugin или OneAgent SDK

# Включение отладочного журналирования для Dynatrace Android Gradle plugin или OneAgent SDK

* How-to guide
* 2-min read
* Updated on Mar 05, 2026

Активируйте отладочное журналирование для Dynatrace Android Gradle plugin или OneAgent SDK.

Не включайте отладочное журналирование в промышленных приложениях.

Используйте отладочные флаги исключительно для целей отладки, но не в промышленной среде. Удалите эти флаги при сборке приложения для PlayStore или промышленной версии, так как дополнительное журналирование может замедлить мобильное приложение или записывать конфиденциальную информацию в журналы устройства.

## Активация режима отладочного журналирования

Активировать отладочные журналы можно через Dynatrace Android Gradle plugin или OneAgent SDK for Android.

### Dynatrace Android Gradle plugin

Включите отладочное журналирование через свойство [`agentLogging`](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.DebugOptions.html#com.dynatrace.tools.android.dsl.DebugOptions:agentLogging).

Groovy

Kotlin

```
dynatrace {



configurations {



sampleConfig {



debug {



agentLogging true



}



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("sampleConfig") {



debug {



agentLogging(true)



}



}



}



}
```

### OneAgent SDK

Включите отладочное журналирование с помощью метода [`ConfigurationBuilder.withDebugLogging(boolean)`](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/conf/ConfigurationBuilder.html#withDebugLogging(boolean)).

Java

Kotlin

```
Dynatrace.startup(this, new DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withDebugLogging(true)



.buildConfiguration());
```

```
Dynatrace.startup(this, DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withDebugLogging(true)



.buildConfiguration())
```

## Получение журналов с устройства

OneAgent for Android использует стандартный фреймворк журналирования Android. Для просмотра сообщений журнала вы можете использовать [окно **Logcat**](https://developer.android.com/studio/debug/am-logcat.html) в Android Studio или [утилиту logcat для командной строки](https://developer.android.com/studio/command-line/logcat.html).

Чтобы получить журналы Android через окно **Logcat** в Android Studio:

1. Подключите устройство к компьютеру или запустите эмулятор.

   Убедитесь, что устройство [настроено для разработки](https://developer.android.com/studio/run/device.html#setting-up).
2. В Android Studio выберите **View** > **Tool Windows** > **Logcat**, затем выберите ваше устройство.
3. Создайте фильтр.

   New Logcat

   Previous Logcat

   Выполните следующие действия, если вы включили [новый инструмент Logcat](https://developer.android.com/studio/releases#logcat) в Android Studio Dolphin или используете Android Studio Electric Eel.

   * В поле фильтра введите `tag~:^dtx|^caa`.
   * Если вы изменили параметр форматирования, переключитесь на параметр по умолчанию **Standard View**.

     ![Новое окно Logcat](https://dt-cdn.net/images/logcat-window-1479-0ae2bb9420.png)

     Новое окно Logcat

   Выполните следующие действия, если вы используете предыдущую версию Logcat.

   * В поле **Filter Name** введите имя фильтра, например **Dynatrace OneAgent**.
   * В поле **Log tag** введите регулярное выражение `^dtx|^caa`.

     ![Предыдущая версия окна Logcat](https://dt-cdn.net/images/oldlogcat-520-f4d55b692e.png)

     Предыдущая версия окна Logcat
4. Запустите инструментированное приложение с использованием отладочных флагов.
5. Скопируйте строки журнала и вставьте их в текстовый файл.