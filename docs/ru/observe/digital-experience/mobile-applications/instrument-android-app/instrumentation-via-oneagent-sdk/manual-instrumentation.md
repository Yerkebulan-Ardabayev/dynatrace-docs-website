---
title: Инструментирование приложения вручную с помощью OneAgent SDK для Android
source: https://www.dynatrace.com/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/manual-instrumentation
scraped: 2026-03-05T21:32:03.786138
---

# Ручная инструментация приложения с помощью OneAgent SDK для Android


Если вы не можете использовать [плагин Dynatrace Android Gradle](../instrumentation-via-plugin.md "Узнайте, как плагин Dynatrace Android Gradle может автоматически инструментировать ваш проект Android-приложения.") из-за определённых технических ограничений, выберите автономную ручную инструментацию с помощью OneAgent SDK для Android.

Выполните приведённые ниже шаги для ручной инструментации вашего приложения с помощью OneAgent SDK для Android.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Убедитесь, что репозиторий Maven Central объявлен.**](manual-instrumentation.md#step-declare-maven-central "Используйте OneAgent SDK для Android для ручной инструментации вашего Android-приложения.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Добавьте библиотеку OneAgent как зависимость в ваш проект.**](manual-instrumentation.md#step-include-OneAgent-library "Используйте OneAgent SDK для Android для ручной инструментации вашего Android-приложения.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Запустите OneAgent вручную.**](manual-instrumentation.md#step-start-one-agent "Используйте OneAgent SDK для Android для ручной инструментации вашего Android-приложения.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Захватите дополнительные данные с помощью OneAgent SDK для Android.**](manual-instrumentation.md#step-capture-additional-data "Используйте OneAgent SDK для Android для ручной инструментации вашего Android-приложения.")

При использовании автономной ручной инструментации ничего не выполняется автоматически. Убедитесь, что каждая важная часть вашего приложения инструментирована вручную. В противном случае OneAgent не сможет отслеживать ваше приложение и отправлять данные мониторинга в Dynatrace.

1. Убедитесь, что репозиторий Maven Central объявлен.

   OneAgent для Android размещён на [Maven Central](https://central.sonatype.com/artifact/com.dynatrace.agent/agent-android). В файле настроек Gradle убедитесь, что `mavenCentral()` добавлен в блоки `repositories` в разделе `dependencyResolutionManagement`. Ознакомьтесь с [официальной документацией Android](https://dt-url.net/gradle-settings-file), чтобы узнать, как должен выглядеть файл настроек Gradle.

   Проекты с предыдущим шаблоном Android: убедитесь, что репозиторий Maven Central объявлен.

   Возможно, вам потребуется добавить `mavenCentral()` во все блоки `repositories` в [файле сборки верхнего уровня](https://dt-url.net/top-level-build-file).
2. Добавьте библиотеку OneAgent как зависимость в ваш проект.

   При использовании Gradle в качестве инструмента автоматизации сборки добавьте библиотеку OneAgent как зависимость `implementation` или `api` в один или несколько модулей. Интеграция зависит от частей, которые вы хотите инструментировать, и архитектуры проекта, используемой для вашего проекта Android.

   Используйте версию `8.+`, чтобы Gradle мог автоматически обновлять библиотеку OneAgent при выходе новой минорной версии. Когда Dynatrace выпускает новую мажорную версию, обновите её вручную -- новая мажорная версия может содержать критические изменения, поэтому обычно требуются ручные корректировки.

   **Одномодульный проект Android**

   Добавьте библиотеку OneAgent как зависимость `implementation` в ваш модуль Android-приложения.

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

   **Многомодульные проекты Android с функциональными модулями**

   Добавьте библиотеку OneAgent как зависимость `api` в ваш базовый модуль (модуль Android-приложения). Если вы используете внутренние модули библиотек Android, которые необходимо инструментировать, добавьте библиотеку OneAgent как зависимость `implementation` в эти внутренние модули библиотек Android.
3. Запустите OneAgent вручную.

   Используйте метод API [`Dynatrace.startup(Application, Configuration)`](https://www.dynatrace.com/support/doc/javadoc/oneagent/android/agent/com/dynatrace/android/agent/Dynatrace.html#startup(android.app.Application,com.dynatrace.android.agent.conf.Configuration)) и запустите OneAgent вручную в методе [`Application.onCreate`](https://developer.android.com/reference/android/app/Application#onCreate()).

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

   Если вам нужно запустить OneAgent на более позднем этапе, используйте метод API [`Dynatrace.startup(Activity, Configuration)`](https://www.dynatrace.com/support/doc/javadoc/oneagent/android/agent/com/dynatrace/android/agent/Dynatrace.html#startup(android.app.Activity,com.dynatrace.android.agent.conf.Configuration)). Предоставьте активный `Activity` в качестве параметра, чтобы OneAgent мог немедленно начать его мониторинг.

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

   Чтобы получить правильные ключи идентификации приложения (`applicationId` и `beaconUrl`), откройте [мастер мобильной инструментации](../get-started-with-android-monitoring.md#instrumentation-wizard "Узнайте, какие шаги необходимо выполнить для инструментации вашего Android-приложения для мониторинга с помощью Dynatrace.") для вашего приложения.

   Если ваше приложение поддерживает Direct Boot, никогда не вызывайте метод API `Dynatrace.startup` из компонента, поддерживающего Direct Boot. Также ознакомьтесь с разделом [Настройка связи с OneAgent SDK для Android](adjust-oneagent-communication.md "Настройте связь с OneAgent для отправки данных о пользовательском опыте в Dynatrace."), чтобы убедиться, что OneAgent может передавать данные в Dynatrace.
4. Захватите дополнительные данные с помощью [OneAgent SDK для Android](oneagent-sdk-for-android.md "Узнайте, как расширить мониторинг мобильного пользовательского опыта на Android с помощью OneAgent SDK.").

   Например, вы можете создавать пользовательские действия, сообщать об ошибках, отмечать конкретных пользователей и многое другое.
