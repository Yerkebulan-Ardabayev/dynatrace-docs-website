---
title: Включение отладочного логирования для плагина Gradle Dynatrace Android или OneAgent SDK в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/debug-logging-oneagent
---

# Включение отладочного логирования для плагина Gradle Dynatrace Android или OneAgent SDK в RUM Classic

# Включение отладочного логирования для плагина Gradle Dynatrace Android или OneAgent SDK в RUM Classic

* Практическое руководство
* Чтение 2 мин
* Обновлено 05 марта 2026 г.

Включение отладочного логирования для плагина Gradle Dynatrace Android или OneAgent SDK.

Не включай отладочное логирование для production-приложений.

Флаги отладки нужно использовать явно для целей отладки, а не для production. Убирай эти флаги при сборке приложения для PlayStore или production, так как дополнительное логирование может замедлить работу мобильного приложения или записать конфиденциальную информацию в логи устройства.

## Включение режима отладочного логирования

Отладочные логи можно включить через плагин Gradle Dynatrace Android или OneAgent SDK для Android.

### Плагин Gradle Dynatrace Android

Включи отладочное логирование через свойство [`agentLogging`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.DebugOptions.html#com.dynatrace.tools.android.dsl.DebugOptions:agentLogging).

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

Включи отладочное логирование с помощью метода [`ConfigurationBuilder.withDebugLogging(boolean)`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/conf/ConfigurationBuilder.html#withDebugLogging(boolean)).

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

## Получение логов с устройства

OneAgent для Android использует стандартный фреймворк логирования Android. Для просмотра сообщений лога можно использовать окно [**Logcat**﻿](https://developer.android.com/studio/debug/am-logcat.html) в Android Studio или [инструмент командной строки logcat﻿](https://developer.android.com/studio/command-line/logcat.html).

Чтобы получить логи Android через окно **Logcat** в Android Studio

1. Подключи устройство к компьютеру или запусти эмулятор.

   Обрати внимание, что устройство должно быть [настроено для разработки﻿](https://developer.android.com/studio/run/device.html#setting-up).
2. В Android Studio выбери **View** > **Tool Windows** > **Logcat**, затем выбери устройство.
3. Создай фильтр.

   Новый Logcat

   Предыдущий Logcat

   Следуй шагам ниже, если включён [новый инструмент Logcat﻿](https://developer.android.com/studio/releases#logcat) в Android Studio Dolphin, или если используется Android Studio Electric Eel.

   * Введи `tag~:^dtx|^caa` в поле фильтра.
   * Если формат отображения был изменён, переключись на стандартный вариант **Standard View**.

     ![Новое окно Logcat](https://dt-cdn.net/images/logcat-window-1479-0ae2bb9420.png)

     Новое окно Logcat

   Следуй шагам ниже, если используется предыдущая версия Logcat.

   * Введи имя фильтра, например, **Dynatrace OneAgent**, в поле **Filter Name**.
   * Введи регулярное выражение `^dtx|^caa` в поле **Log tag**.

     ![Предыдущая версия окна Logcat](https://dt-cdn.net/images/oldlogcat-520-f4d55b692e.png)

     Предыдущая версия окна Logcat
4. Запусти инструментированное приложение с использованием отладочных флагов.
5. Скопируй строки лога и вставь их в текстовый файл.