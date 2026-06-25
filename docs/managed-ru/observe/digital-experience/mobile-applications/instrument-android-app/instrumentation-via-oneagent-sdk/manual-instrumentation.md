---
title: Ручное инструментирование приложения с помощью OneAgent SDK for Android
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/manual-instrumentation
scraped: 2026-05-12T11:33:22.882949
---

# Ручное инструментирование приложения с помощью OneAgent SDK for Android

# Ручное инструментирование приложения с помощью OneAgent SDK for Android

* How-to guide
* 2-min read
* Updated on Jan 10, 2024

Если вы не можете использовать [Dynatrace Android Gradle plugin](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin "Узнайте, как Dynatrace Android Gradle plugin может автоматически инструментировать ваш Android-проект.") из-за технических ограничений, воспользуйтесь автономным ручным инструментированием с помощью OneAgent SDK for Android.

Выполните следующие шаги для ручного инструментирования приложения с помощью OneAgent SDK for Android.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Убедитесь, что репозиторий Maven Central объявлен.**](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/manual-instrumentation#step-declare-maven-central "Используйте OneAgent SDK for Android для ручного инструментирования Android-приложения.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Подключите библиотеку OneAgent как зависимость к вашему проекту.**](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/manual-instrumentation#step-include-OneAgent-library "Используйте OneAgent SDK for Android для ручного инструментирования Android-приложения.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Запустите OneAgent вручную.**](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/manual-instrumentation#step-start-one-agent "Используйте OneAgent SDK for Android для ручного инструментирования Android-приложения.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Шаг 4")

**Собирайте дополнительные данные через OneAgent SDK for Android.**](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/manual-instrumentation#step-capture-additional-data "Используйте OneAgent SDK for Android для ручного инструментирования Android-приложения.")

При автономном ручном инструментировании ничего не выполняется автоматически. Убедитесь, что каждая важная часть приложения инструментирована вручную. В противном случае OneAgent не сможет осуществлять мониторинг приложения и отправлять данные в Dynatrace.

1. Убедитесь, что репозиторий Maven Central объявлен.

   OneAgent for Android размещён на [Maven Central](https://central.sonatype.com/artifact/com.dynatrace.agent/agent-android). В файле настроек Gradle убедитесь, что `mavenCentral()` добавлен в блоки `repositories` раздела `dependencyResolutionManagement`. Ознакомьтесь с [официальной документацией Android](https://dt-url.net/gradle-settings-file), чтобы понять, как должен выглядеть файл настроек Gradle.

   Проекты с предыдущим шаблоном Android: убедитесь, что репозиторий Maven Central объявлен.

   Возможно, вам потребуется добавить `mavenCentral()` во все блоки `repositories` в [корневом файле сборки](https://dt-url.net/top-level-build-file).
2. Подключите библиотеку OneAgent как зависимость к вашему проекту.

   При использовании Gradle в качестве инструмента автоматизации сборки добавьте библиотеку OneAgent как зависимость `implementation` или `api` в один или несколько модулей. Способ интеграции зависит от частей приложения, которые нужно инструментировать, и архитектуры проекта Android.

   Используйте версию `8.+`, чтобы Gradle мог автоматически обновлять библиотеку OneAgent при выходе новой минорной версии. При выходе новой мажорной версии Dynatrace обновляйтесь вручную — новая мажорная версия может содержать изменения, нарушающие совместимость, поэтому обычно требуются ручные корректировки.

   **Однмодульный Android-проект**

   Добавьте библиотеку OneAgent как зависимость `implementation` в модуль приложения Android.

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

   **Многомодульные Android-проекты с функциональными модулями**

   Добавьте библиотеку OneAgent как зависимость `api` в базовый модуль (модуль приложения Android). Если у вас есть внутренние модули Android-библиотек, которые необходимо инструментировать, добавьте библиотеку OneAgent как зависимость `implementation` в эти внутренние модули.
3. Запустите OneAgent вручную.

   Используйте API-метод [`Dynatrace.startup(Application, Configuration)`](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/Dynatrace.html#startup(android.app.Application,com.dynatrace.android.agent.conf.Configuration)) и запустите OneAgent вручную в методе [`Application.onCreate`](https://developer.android.com/reference/android/app/Application#onCreate()).

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

   Если вам нужно запустить OneAgent на более позднем этапе, используйте API-метод [`Dynatrace.startup(Activity, Configuration)`](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/Dynatrace.html#startup(android.app.Activity,com.dynatrace.android.agent.conf.Configuration)). Передайте активный объект `Activity` в качестве параметра, чтобы OneAgent мог немедленно начать его мониторинг.

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

   Чтобы получить правильные ключи идентификации приложения (`applicationId` и `beaconUrl`), воспользуйтесь [мастером инструментирования мобильных приложений](/managed/observe/digital-experience/mobile-applications/instrument-android-app/get-started-with-android-monitoring#instrumentation-wizard "Узнайте, какие шаги необходимо выполнить для инструментирования Android-приложения для мониторинга с Dynatrace.") для вашего приложения.

   OneAgent можно запустить только один раз на приложение. OneAgent не поддерживает несколько одновременных инициализаций в одном запущенном приложении. Параметры `appId` и `beaconUrl` не являются механизмом для отправки данных в два разных окружения Dynatrace из одного приложения.

   Если ваше приложение поддерживает Direct Boot, никогда не вызывайте API-метод `Dynatrace.startup` из компонента, поддерживающего Direct Boot. Также проверьте раздел [Настройка взаимодействия с OneAgent SDK for Android](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/adjust-oneagent-communication "Настройте коммуникацию с OneAgent для отправки данных о пользовательском опыте в Dynatrace."), чтобы убедиться в возможности передачи данных OneAgent в Dynatrace.
4. Собирайте дополнительные данные через [OneAgent SDK for Android](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android "Узнайте, как расширить мониторинг пользовательского опыта на Android с помощью OneAgent SDK.").

   Например, вы можете создавать пользовательские действия, фиксировать ошибки, тегировать конкретных пользователей и многое другое.