---
title: Ручное инструментирование приложения с помощью OneAgent SDK для Android в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/manual-instrumentation
---

# Ручное инструментирование приложения с помощью OneAgent SDK для Android в RUM Classic

# Ручное инструментирование приложения с помощью OneAgent SDK для Android в RUM Classic

* Практическое руководство
* Чтение 2 мин
* Обновлено 10 января 2024 г.

Если использовать [плагин Dynatrace Android Gradle](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin "Узнайте, как плагин Dynatrace Android Gradle может автоматически инструментировать проект вашего Android-приложения.") нельзя из-за определённых технических ограничений, стоит выбрать самостоятельное ручное инструментирование с помощью OneAgent SDK для Android.

Выполните шаги ниже, чтобы вручную инструментировать приложение с помощью OneAgent SDK для Android.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Убедитесь, что репозиторий Maven Central объявлен.**](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/manual-instrumentation#step-declare-maven-central "Используйте OneAgent SDK для Android, чтобы вручную инструментировать своё Android-приложение.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Добавьте библиотеку OneAgent как зависимость в проект.**](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/manual-instrumentation#step-include-OneAgent-library "Используйте OneAgent SDK для Android, чтобы вручную инструментировать своё Android-приложение.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Запустите OneAgent вручную.**](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/manual-instrumentation#step-start-one-agent "Используйте OneAgent SDK для Android, чтобы вручную инструментировать своё Android-приложение.")[![Шаг 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Шаг 4")

**Собирайте дополнительные данные с помощью OneAgent SDK для Android.**](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/manual-instrumentation#step-capture-additional-data "Используйте OneAgent SDK для Android, чтобы вручную инструментировать своё Android-приложение.")

При самостоятельном ручном инструментировании ничего не выполняется автоматически. Нужно убедиться, что каждая важная часть приложения инструментирована вручную. Иначе OneAgent не сможет отслеживать приложение и отправлять данные мониторинга в Dynatrace.

1. Убедитесь, что репозиторий Maven Central объявлен.

   OneAgent для Android размещён на [Maven Central﻿](https://central.sonatype.com/artifact/com.dynatrace.agent/agent-android). В файле настроек Gradle проверьте, что `mavenCentral()` добавлен в блоки `repositories` под `dependencyResolutionManagement`. В [официальной документации Android﻿](https://dt-url.net/gradle-settings-file) можно посмотреть, как должен выглядеть файл настроек Gradle.

   Проекты с предыдущим шаблоном Android: убедитесь, что репозиторий Maven Central объявлен.

   Возможно, потребуется добавить `mavenCentral()` во все блоки `repositories` в [файле сборки верхнего уровня﻿](https://dt-url.net/top-level-build-file).
2. Добавьте библиотеку OneAgent как зависимость в проект.

   При использовании Gradle в качестве инструмента автоматизации сборки добавьте библиотеку OneAgent как зависимость `implementation` или `api` в один или несколько модулей. Интеграция зависит от того, какие части нужно инструментировать, и от архитектуры проекта, используемой для Android-проекта.

   Используйте версию `8.+`, чтобы Gradle мог автоматически обновлять библиотеку OneAgent при выходе новой минорной версии. Когда Dynatrace выпускает новую основную версию, обновляйтесь до неё вручную: новая основная версия может содержать критичные изменения, поэтому обычно требуется ручная доработка.

   **Однмодульный Android-проект**

   Добавьте библиотеку OneAgent как зависимость `implementation` в модуль вашего Android-приложения.

   Groovy

   Kotlin

   ```
   dependencies {



   implementation 'com.dynatrace.agent:agent-android:8.+'



   }
   ```

   ```
   dependencies {



   implementation("com.dynatrace.agent:agent-android:8.+")



   }
   ```

   **Многомодульные Android-проекты с feature-модулями**

   Добавьте библиотеку OneAgent как зависимость `api` в базовый модуль (модуль Android-приложения). Если используются внутренние модули библиотек Android, которые нужно инструментировать, добавьте библиотеку OneAgent как зависимость `implementation` в эти внутренние модули библиотек Android.
3. Запустите OneAgent вручную.

   Используйте API-метод [`Dynatrace.startup(Application, Configuration)`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/Dynatrace.html#startup(android.app.Application,com.dynatrace.android.agent.conf.Configuration)) и запустите OneAgent вручную в методе [`Application.onCreate`﻿](https://developer.android.com/reference/android/app/Application#onCreate()).

   Java

   Kotlin

   ```
   public class YourApplication extends Application {



   @Override



   public void onCreate() {



   super.onCreate();



   // provide the application context as parameter



   Dynatrace.startup(this, new DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconUrl>")



   ... // additional configuration



   .buildConfiguration());



   }



   }
   ```

   ```
   class YourApplication : Application() {



   override fun onCreate() {



   super.onCreate()



   // provide the application context as parameter



   Dynatrace.startup(this, DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconUrl>")



   ... // additional configuration



   .buildConfiguration())



   }



   }
   ```

   Если нужно запустить OneAgent на более позднем этапе, используйте API-метод [`Dynatrace.startup(Activity, Configuration)`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/Dynatrace.html#startup(android.app.Activity,com.dynatrace.android.agent.conf.Configuration)). Передайте активную `Activity` в качестве параметра, чтобы OneAgent мог сразу начать её мониторинг.

   Java

   Kotlin

   ```
   Dynatrace.startup(yourActiveActivity, new DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconUrl>")



   ... // additional configuration



   .buildConfiguration());
   ```

   ```
   Dynatrace.startup(yourActiveActivity, DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconUrl>")



   ... // additional configuration



   .buildConfiguration())
   ```

   Чтобы получить правильные ключи идентификации приложения (`applicationId` и `beaconUrl`), перейдите в [мастер инструментирования мобильных приложений](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/get-started-with-android-monitoring#instrumentation-wizard "Узнайте, какие шаги нужно выполнить, чтобы инструментировать своё Android-приложение для мониторинга с Dynatrace.") для вашего приложения.

   OneAgent можно запустить только один раз для приложения. OneAgent не поддерживает несколько одновременных инициализаций в одном запущенном приложении. Параметры `appId` и `beaconUrl` не являются механизмом для отправки данных в две разные среды Dynatrace из одного приложения.

   Если приложение поддерживает Direct Boot, никогда не вызывайте API-метод `Dynatrace.startup` из компонента, поддерживающего Direct Boot. Также проверьте [Настройка взаимодействия с OneAgent SDK для Android в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/adjust-oneagent-communication "Настройте взаимодействие с OneAgent для передачи данных о пользовательском опыте в Dynatrace."), чтобы убедиться, что OneAgent может передавать данные в Dynatrace.
4. Собирайте дополнительные данные с помощью [OneAgent SDK для Android](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android "Узнайте, как обогатить мониторинг пользовательского опыта в Android с помощью OneAgent SDK.").

   Например, можно создавать пользовательские действия, сообщать об ошибках, помечать конкретных пользователей и многое другое.