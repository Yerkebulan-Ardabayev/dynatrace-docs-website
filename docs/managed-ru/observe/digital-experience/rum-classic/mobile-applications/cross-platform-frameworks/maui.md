---
title: Инструментирование мобильных приложений с пакетом NuGet Dynatrace .NET MAUI в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/maui
---

# Инструментирование мобильных приложений с пакетом NuGet Dynatrace .NET MAUI в RUM Classic

# Инструментирование мобильных приложений с пакетом NuGet Dynatrace .NET MAUI в RUM Classic

* Практическое руководство
* 10 минут на чтение
* Обновлено 22 июня 2026 г.

Dynatrace версии 1.265+

Пакет NuGet Dynatrace .NET MAUI помогает автоматически инструментировать мобильное приложение .NET MAUI с помощью OneAgent для Android и iOS, а также предоставляет API для [ручного инструментирования](#usage-mobile-agent).

Пакет NuGet Dynatrace .NET MAUI доступен для Android и iOS. Использовать пакет для macOS и Windows нельзя.

## Поддерживаемые функции

#### Автоматическое инструментирование

* Действия пользователя
* События жизненного цикла
* Веб-запросы
* Сбои

#### Ручное инструментирование

* Пользовательские действия
* Веб-запросы
* Значения
* События
* Ошибки
* Сбои
* Тегирование пользователей

## Требования

* **Для Android:** Android версии 6.0+ (API 23+)
* **Для iOS:** iOS версии 15+

## Настройка пакета

Чтобы настроить пакет NuGet Dynatrace .NET MAUI для мобильного приложения, нужно выполнить следующие шаги.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Установить пакет NuGet Dynatrace .NET MAUI**](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/maui#install-package "Мониторинг приложений .NET MAUI с помощью Dynatrace OneAgent.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Создать приложение и получить конфигурационный файл**](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/maui#installation-dynatrace "Мониторинг приложений .NET MAUI с помощью Dynatrace OneAgent.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Добавить конфигурационный файл в проект**](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/maui#configure-app "Мониторинг приложений .NET MAUI с помощью Dynatrace OneAgent.")[![Шаг 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Шаг 4")

**Добавить метод запуска OneAgent**](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/maui#start-method "Мониторинг приложений .NET MAUI с помощью Dynatrace OneAgent.")[![Шаг 5 опционально](https://dt-cdn.net/images/dotted-step-5-52040ae237.svg "Шаг 5 опционально")

**Включить автоматическое инструментирование веб-запросов**](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/maui#http-client "Мониторинг приложений .NET MAUI с помощью Dynatrace OneAgent.")

### Шаг 1 Установить пакет NuGet

Добавить пакет NuGet Dynatrace .NET MAUI в приложение.

1. В Visual Studio щёлкнуть правой кнопкой мыши по решению мобильного приложения и выбрать **Manage NuGet packages**.
2. Найти [**Dynatrace.OneAgent.MAUI** на nuget.org﻿](https://www.nuget.org/packages/Dynatrace.OneAgent.MAUI) и выбрать **Add Package**.
3. Отметить флажки всех проектов, в которые нужно добавить пакет NuGet. Нужно убедиться, что пакет добавляется в нативные проекты, поскольку целевые файлы внутри пакета взаимодействуют со сборкой.
4. Выбрать **OK**.

### Шаг 2 Создать приложение и получить конфигурационный файл

Создать новое мобильное приложение в Dynatrace и скачать конфигурационный файл.

1. В Dynatrace перейти в **Mobile**.
2. Выбрать **Create mobile app**.
3. Ввести имя приложения и выбрать **Create mobile app**. Откроется страница настроек приложения.
4. На странице настроек приложения выбрать **Instrumentation wizard** > **.NET MAUI**.
5. На шаге 2 выбрать **Download dynatrace.config.json**, чтобы получить конфигурационный файл.

### Шаг 3 Добавить конфигурационный файл в проект

Добавить [файл `dynatrace.config.json`](#config-file), скачанный на предыдущем шаге, в проект. Это можно сделать любым из следующих способов, перечисленных в порядке от наиболее к наименее рекомендуемому.

* Добавить файл `dynatrace.config.json` в произвольное расположение. Указать произвольное расположение через [свойство `DynatraceConfigurationFile`](#config-file).
* Добавить файл `dynatrace.config.json` в:

  + директорию `Platforms/Android/Assets` проекта (Android). Если директории `Assets` не существует, создать её внутри директории `Platforms/Android`.
  + директорию `Platforms/iOS/Resources` проекта (iOS). Если директории `Resources` не существует, создать её внутри директории `Platforms/iOS`.
* Добавить файл `dynatrace.config.json` в корневую директорию проекта. MSBuild автоматически устанавливает корневую директорию через свойство `ProjectDir`.

При миграции проекта Xamarin на проект .NET и переходе на пакет NuGet Dynatrace .NET MAUI нужно добавить файл `dynatrace.config.json` в произвольное расположение или в корневую директорию проекта.

### Шаг 4 Добавить метод запуска OneAgent

Метод запуска необходим для запуска OneAgent.

Android

iOS

```
using Dynatrace.MAUI;



Agent.Instance.Start();
```

```
using Dynatrace.MAUI;



Agent.Instance.Start();
```

### Шаг 5 опционально Включить автоматическое инструментирование веб-запросов Опционально

Опционально можно использовать следующий метод, чтобы включить автоматическое инструментирование веб-запросов. `HttpMessageHandler`, используемый `HttpClient`, берёт на себя ручное инструментирование веб-запросов.

```
using Dynatrace.MAUI;



var httpHandler = Agent.Instance.GetHttpMessageHandler();



var httpClient = new HttpClient(httpHandler);
```

Кроме того, можно использовать собственный HTTP-обработчик:

```
using Dynatrace.MAUI;



var defaultHttpHandler = new HttpClientHandler();



var httpHandler = Agent.Instance.GetHttpMessageHandler(defaultHttpHandler);



var httpClient = new HttpClient(httpHandler);
```

## Ручное инструментирование

В разделах ниже описано, как запустить OneAgent вручную, создать пользовательские действия, инструментировать веб-запросы и передавать значения, события и сбои.

### Запуск OneAgent

Можно использовать ручной запуск с построителем конфигурации (Android) или словарём конфигурации (iOS).

1. Изменить [файл `dynatrace.config.json`](#config-file), чтобы отключить автозапуск OneAgent.

   Android

   iOS

   ```
   {



   "android": {



   "autoStart": {



   "enabled": false



   }



   }



   }
   ```

   ```
   {



   "ios": {



   "DTXAutoStart": false



   }



   }
   ```

   Не добавлять в конфигурационный файл дополнительные свойства. Если это сделать, сборка завершится с исключением.
2. Запустить OneAgent вручную и передать необходимые свойства.

   Android

   iOS

   ```
   using Dynatrace.MAUI;



   Agent.Instance.Start(new ConfigurationBuilder("<insertBeaconURL>","<insertApplicationID>").BuildConfiguration());
   ```

   ```
   using Dynatrace.MAUI;



   Agent.Instance.Start(new ConfigurationBuilder("<insertBeaconURL>","<insertApplicationID>").BuildConfiguration());
   ```

### Создание пользовательских действий

Можно создавать пользовательские действия и дополнять их дополнительной информацией, например значениями, событиями и ошибками.

Вызвать `EnterAction`, чтобы начать пользовательское действие, и `LeaveAction`, чтобы закрыть его. Тайминг измеряется автоматически.

```
using Dynatrace.MAUI;



IRootAction myAction = Agent.Instance.EnterAction("Tap on Confirm");



//Perform the action and whatever else is needed.



myAction.LeaveAction();
```

Для мобильного пользовательского действия или автоматически сгенерированного мобильного действия пользователя максимальная длина имени составляет 250 символов.

Информацию об именовании действий пользователя см. по следующим ссылкам: [Android](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#user-action-naming "Настройка плагина Dynatrace Android Gradle для регулирования возможностей мониторинга OneAgent.") и [iOS](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#user-action-naming "Обогащение мониторинга пользовательского опыта на мобильных устройствах с помощью OneAgent SDK для iOS.").

Если для приложения включён [режим согласия пользователя (opt-in)](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Использование настроек конфиденциальности, предоставляемых Dynatrace, для обеспечения соответствия мобильных приложений требованиям законодательства о защите данных региона."), это может повлиять на тегирование пользователей и передачу пользовательских событий, действий пользователя, значений и ошибок. Точные типы данных, не передаваемые в Dynatrace, зависят от уровня сбора данных, установленного конкретным пользователем. Подробнее см. [Уровни сбора данных](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Использование настроек конфиденциальности, предоставляемых Dynatrace, для обеспечения соответствия мобильных приложений требованиям законодательства о защите данных региона.").

### Создание дочерних действий

Помимо создания самостоятельных пользовательских действий, можно также создавать [дочерние действия](/managed/observe/digital-experience/rum-classic/rum-concepts/user-actions#child-actions "Learn what user actions are and how they help you understand what users do with your application.").

Дочерние действия похожи на родительские пользовательские действия. Когда родительское действие закрывается, все дочерние действия этого родительского действия закрываются автоматически.

```
using Dynatrace.MAUI;



IRootAction myAction = Agent.Instance.EnterAction("Tap on Confirm");



IAction mySubAction = myAction.EnterAction("Tap on Confirm again");



//Perform the action and whatever else is needed.



mySubAction.LeaveAction();



myAction.LeaveAction();
```

Для мобильного пользовательского действия или автоматически сгенерированного мобильного пользовательского действия максимальная длина имени составляет 250 символов.

Ограничения на количество дочерних действий, прикреплённых к пользовательскому действию, нет. Однако стоит учитывать, что уровень вложенности дочерних действий только один: нельзя создать дочернее действие для другого дочернего действия (дочерние действия не могут иметь собственных дочерних действий). Также см. [Структура пользовательской сессии для отдельного пользователя](/managed/observe/digital-experience/rum-classic/rum-concepts/user-session#session-structure-dep-on-app-type "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.").

Дочерние действия не отображаются на [странице сведений о пользовательской сессии](/managed/observe/digital-experience/rum-classic/session-segmentation/user-sessions#session-details-page "Learn about user session segmentation and filtering attributes."), но их можно посмотреть на [странице waterfall-анализа](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/waterfall-analysis "Learn how to analyze all user action monitoring data through waterfall analysis.") для пользовательского действия, к которому эти дочерние действия прикреплены.

### Отмена пользовательских действий

Если нужно отменить уже созданное, но ещё не закрытое пользовательское действие, нужно вызвать `Cancel`. Отмена действия отбрасывает все связанные с ним данные: все переданные значения, события и ошибки отбрасываются, все дочерние действия отменяются.

```
using Dynatrace.MAUI;



IRootAction myAction = Agent.Instance.EnterAction("Tap on Confirm");



// Action is canceled



myAction.Cancel();
```

Закрытое действие отменить нельзя, поэтому вызов `Cancel` после `LeaveAction` для одного и того же действия невозможен. То же самое касается закрытия отменённого действия: нельзя вызвать `LeaveAction` после использования `Cancel` для одного и того же действия.

### Инструментирование веб-запросов

Для инструментирования веб-запросов нужно использовать следующий фрагмент кода:

```
using Dynatrace.MAUI;



// Create an action



IRootAction webAction = Agent.Instance.EnterAction(actionName: "WebRequest Action");



// Generate a new unique tag associated with the web request action



string requestTag = webAction.GetRequestTag(url);



string requestTagHeader = webAction.GetRequestTagHeader();



// Place the Dynatrace HTTP header on your web request



httpClient.DefaultRequestHeaders.Add(requestTagHeader, requestTag);



// Generate a WebRequestTiming object based on the unique tag



IWebRequestTiming timing = Agent.Instance.GetWebRequestTiming(requestTag, url);



// Start web request timing before the HTTP request is sent



timing.StartWebRequestTiming();



try



{



var response = await httpClient.GetAsync(url);



// Stop web request timing when the HTTP response is received and the response body is obtained



timing.StopWebRequestTiming(url, (int)response.StatusCode, response.ReasonPhrase);



}



catch (HttpRequestException exception)



{



// Stop web request timing when a connection exception occurs



timing.StopWebRequestTiming(url, -1, exception.ToString());



}



finally



{



// Leave an action



webAction.LeaveAction();



}
```

### Передача значения

Метод `reportValue` позволяет передавать пары «ключ-значение» метаданных, которые впоследствии можно посмотреть в веб-интерфейсе Dynatrace и преобразовать в [свойства пользовательского действия и пользовательской сессии](/managed/observe/digital-experience/rum-classic/mobile-applications/analyze-and-use/action-and-session-properties-mobile "User action and session properties, which are metadata key-value pairs, provide added visibility and deeper analysis of your end users' experience. Using these properties for your applications, you can filter user sessions, add calculated metrics, create charts, and more."). Переданные значения должны быть частью пользовательского действия.

Можно передавать значения следующих типов данных:

* `int`
* `double`
* `string`

```
ReportValue(valueName: string, value: int);



ReportValue(valueName: string, value: double);



ReportValue(valueName: string, value: string);
```

Например, чтобы передать значение типа `string` в рамках действия `Tap on Confirm`, нужно использовать следующий код:

```
using Dynatrace.MAUI;



IRootAction myAction = Agent.Instance.EnterAction("Tap on Confirm");



myAction.ReportValue("Customer type", "Gold");



myAction.LeaveAction();
```

Чтобы посмотреть переданные значения в веб-интерфейсе Dynatrace, нужно перейти к сведениям о пользовательском действии, которое должно содержать эти метаданные, и прокрутить вниз до раздела **Reported values**.

![Страница сведений о пользовательском действии с переданными значениями SDK](https://dt-cdn.net/images/user-action-details-with-reported-values-2048-b44e8bca3e.png)

Страница сведений о пользовательском действии с переданными значениями SDK

Чтобы добавить свойства действия и сессии на основе переданных значений и затем использовать эти свойства для создания сложных запросов, сегментаций и агрегаций, см. [Определение свойств пользовательского действия и пользовательской сессии для мобильных приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/define-mobile-action-and-session-properties "Send metadata to Dynatrace and define action and session properties for your monitored mobile applications.").

Если для приложения включён [режим согласия пользователя (opt-in)](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region."), это может повлиять на тегирование пользователей и передачу пользовательских событий, действий, значений и ошибок. Конкретные типы данных, которые не передаются в Dynatrace, зависят от уровня сбора данных, установленного конкретным пользователем. Подробности см. в разделе [Уровни сбора данных](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.").

### Передача события

Для любого открытого действия можно передать событие. Используется следующий вызов API:

```
ReportEvent(eventName: string);
```

Если для приложения включён [режим согласия пользователя (opt-in)](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region."), это может повлиять на тегирование пользователей и передачу пользовательских событий, действий, значений и ошибок. Конкретные типы данных, которые не передаются в Dynatrace, зависят от уровня сбора данных, установленного конкретным пользователем. Подробности см. в разделе [Уровни сбора данных](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.").

### Передача ошибки

Чтобы передать [ошибку](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#error "Learn about user and error events and the types of user and error events captured by Dynatrace."), нужно использовать метод `ReportError`.

```
ReportError(errorName: string, errorCode: number);
```

Если для приложения включён [режим согласия пользователя (opt-in)](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region."), это может повлиять на тегирование пользователей и передачу пользовательских событий, действий, значений и ошибок. Конкретные типы данных, которые не передаются в Dynatrace, зависят от уровня сбора данных, установленного конкретным пользователем. Подробности см. в разделе [Уровни сбора данных](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.").

### Передача трассировки стека ошибки

Чтобы передать трассировку стека ошибки, нужно использовать следующий вызов API:

```
using Dynatrace.MAUI;



Agent.Instance.ReportErrorStacktrace("Error_Class", "Error_Value", "Error_Reason", "Error_Stacktrace");
```

### Передача сбоя

Чтобы сообщить о [сбое](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#crash "Узнайте о событиях пользователей и ошибках, а также о типах пользовательских событий и событий ошибок, фиксируемых Dynatrace."), используй следующий вызов API.

```
using Dynatrace.MAUI;



Agent.Instance.ReportCrash("CrashWithoutException", "Crash_Reason", "Crash_Stacktrace");
```

Также можно использовать объект исключения:

```
using Dynatrace.MAUI;



Agent.Instance.ReportCrashWithException("CrashWithExceptionObj", exception);
```

Момент отправки данных о сбое в Dynatrace зависит от операционной системы мобильного приложения.

* **Android**

  Как правило, данные о сбое отправляются сразу после сбоя, поэтому пользователю не нужно перезапускать приложение. Однако в некоторых случаях приложение нужно открыть заново в течение 10 минут, чтобы отчёт о сбое был отправлен. Учти, что Dynatrace не отправляет отчёты о сбоях старше 10 минут (такие отчёты уже нельзя сопоставить на кластере Dynatrace).
* **iOS**

  Данные о сбое отправляются только когда пользователь открывает мобильное приложение заново (то есть при следующем запуске приложения). Однако, если пользователь не открывает приложение в течение 10 минут, отчёт о сбое удаляется. Это связано с тем, что Dynatrace не отправляет отчёты о сбоях старше 10 минут (такие отчёты уже нельзя сопоставить на кластере Dynatrace).

Сообщение о сбое принудительно завершает пользовательскую сессию. Любые последующие действия включаются в новую пользовательскую сессию.

Только для Android При использовании автоматического сообщения о сбоях Visual Studio может перехватить исключение раньше OneAgent. Если заметно, что Dynatrace не сообщает о сбоях в твою среду, убедись, что [не используется опция отладки в Visual Studio](#debugger-turn-off). В противном случае отладчик перехватывает сбой, и в среду Dynatrace ничего не передаётся.

### Тегирование конкретных пользователей

Можно присвоить каждому пользователю мобильного приложения уникальное имя пользователя. Это позволяет искать и фильтровать сессии конкретных пользователей и анализировать поведение отдельного пользователя во времени. Подробнее см. [Тегирование пользователей](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#user-tagging "Узнайте о событиях пользователей и ошибках, а также о типах пользовательских событий и событий ошибок, фиксируемых Dynatrace.").

Выполни следующий вызов API, чтобы присвоить текущей сессии определённое имя:

```
using Dynatrace.MAUI;



Agent.Instance.IdentifyUser("John Smith");
```

OneAgent для Android версии 237+ OneAgent для iOS версии 235+ Сессии, разделённые из-за тайм-аута простоя или длительности, тегируются автоматически заново.

Когда OneAgent завершает тегированную сессию из-за достижения установленного лимита длительности сессии или из-за неактивности пользователя, следующая сессия тегируется автоматически. Повторно предоставлять информацию идентификации пользователя не нужно.

Однако учти, что OneAgent не тегирует заново следующую сессию в следующих случаях:

* Когда тегированная пользовательская сессия явно завершается через [`endVisit`](#end-session)
* Когда пользователь или мобильная операционная система закрывает или принудительно останавливает приложение
* Когда OneAgent завершает текущую пользовательскую сессию и создаёт новую сессию после изменения настроек приватности

См. [Пользовательские сессии > Завершение сессии](/managed/observe/digital-experience/rum-classic/rum-concepts/user-session#user-session-end--mobile-apps "Узнай, как определяется пользовательская сессия, когда она начинается и заканчивается, как рассчитывается её длительность, и многое другое."), чтобы узнать, когда OneAgent завершает мобильную пользовательскую сессию.

Если для приложения включён [режим согласия пользователя (opt-in)](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Используй настройки приватности, которые предоставляет Dynatrace, чтобы обеспечить соответствие твоих мобильных приложений нормам защиты данных твоего региона."), это может повлиять на тегирование пользователей и на сообщение о пользовательских событиях, действиях, значениях и ошибках. Конкретные типы данных, не передаваемые в Dynatrace, зависят от уровня сбора данных, установленного конкретным пользователем. Подробнее см. [Уровни сбора данных](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Используй настройки приватности, которые предоставляет Dynatrace, чтобы обеспечить соответствие твоих мобильных приложений нормам защиты данных твоего региона.").

### Завершение сессии

Можно принудительно завершить сессию через вызов API. Это также закрывает все открытые действия и начинает новую сессию.

```
using Dynatrace.MAUI;



Agent.Instance.EndVisit();
```

### Настройка приватности данных (режим opt-in)

В режиме согласия пользователя (opt-in) каждый пользователь приложения может задать свои предпочтения приватности данных и решить, хочет ли он делиться своей информацией. Когда режим opt-in включён, нужно запросить у каждого пользователя разрешение на сбор его данных, а затем сохранить его предпочтения приватности данных. Подробнее см. [Режим согласия пользователя (opt-in)](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Используй настройки приватности, которые предоставляет Dynatrace, чтобы обеспечить соответствие твоих мобильных приложений нормам защиты данных твоего региона.").

#### Включение режима согласия пользователя (opt-in)

Чтобы активировать режим согласия пользователя (opt-in), установи свойство `userOptIn` (Android) или [ключ конфигурации `DTXUserOptIn`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#privacy-and-security "С помощью ключей конфигурации можно точно настроить авто-инструментацию твоих iOS-приложений.") (iOS) в значение `true` в [файле `dynatrace.config.json`](#config-file).

#### Получение предпочтений приватности данных пользователя

Можно получить предпочтения приватности данных конкретного пользователя.

Чтобы получить текущую конфигурацию `UserPrivacyOptions`, используй следующий вызов API:

```
using Dynatrace.MAUI;



// Get the UserPrivacyOptions object



UserPrivacyOptions currentOptions = Agent.Instance.GetUserPrivacyOptions();



// Get the individual settings for DataCollectionLevel and crash reporting



bool crashOptedIn = Agent.Instance.GetUserPrivacyOptions().CrashReportingOptedIn;



DataCollectionLevel dataCollectionLevel = Agent.Instance.GetUserPrivacyOptions().DataCollectionLevel;
```

#### Изменение предпочтений приватности данных пользователя

Можно скорректировать предпочтения приватности данных на основании решения конкретного пользователя.

Чтобы задать новые опции для объекта `UserPrivacyOptions`, используй следующий код:

```
using Dynatrace.MAUI;



// Creating a new UserPrivacyOptions object requires setting the two parameters of DataCollectionLevel and crash reporting



UserPrivacyOptions options = new UserPrivacyOptions(DataCollectionLevel.Performance, false);



// Update the options with the setter



// Set a data collection level (user allowed you to capture performance and personal data)



options.DataCollectionLevel = DataCollectionLevel.UserBehavior;



// Allow crash reporting (user allowed you to collect information on crashes)



options.CrashReportingOptedIn = true;



// Get the values of the configuration with the getter



options.DataCollectionLevel;



options.CrashReportingOptedIn;



// Get the UserPrivacyOptions object



UserPrivacyOptions currentOptions = Agent.Instance.GetUserPrivacyOptions();
```

Чтобы применить новую конфигурацию `UserPrivacyOptions`, используй следующий код:

```
using Dynatrace.MAUI;



UserPrivacyOptions options = new UserPrivacyOptions(DataCollectionLevel.UserBehavior, true);



Agent.Instance.ApplyUserPrivacyOptions(options);
```

Возможные значения для [уровня сбора данных](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Используй настройки приватности, которые предоставляет Dynatrace, чтобы обеспечить соответствие твоих мобильных приложений нормам защиты данных твоего региона.") следующие:

* `Off`
* `Performance`
* `UserBehavior`

### Сообщение о GPS-местоположении

Можно сообщить широту и долготу.

```
SetGPSLocation(latitude: double, longitude: double);
```

## Накладные расходы инструментации

При использовании авто-инструментации через наш плагин, вот несколько примеров различий в размере до и после инструментации для релизных сборок.

| Операционная система | Шаблон приложения | Версия | Размер до | Размер после | Разница |
| --- | --- | --- | --- | --- | --- |
| Android | Новое приложение по умолчанию | net8.0-android | 31.8 MB | 32.4 MB | 0.6 MB |
| iOS | Новое приложение по умолчанию | net8.0-ios | 421 MB | 426.2 MB | 5.2 MB |

## Файл конфигурации

Файл конфигурации `dynatrace.config.json` содержит идентификатор приложения, beacon URL и некоторые другие настройки.

* Этот файл можно [скачать из Dynatrace](#installation-dynatrace) или создать вручную.
* Если не добавить файл конфигурации хотя бы со свойствами beacon URL и идентификатора приложения, сборка завершится ошибкой. В качестве альтернативы можно использовать [ручной запуск](#start-agent) с конфигуратором (Android) или словарём конфигурации (iOS).
* При использовании определённой конфигурации сборки, например `Debug`, `Release` или пользовательской конфигурации, пакет ищет в каталоге `Assets` (Android) или `Resources` (iOS) файл конфигурации с именем `dynatrace<Configuration>.config.json`. Например, при использовании конфигурации сборки `Debug` пакет ищет файл с именем `dynatraceDebug.config.json`.
* Чтобы задать собственный путь к файлу конфигурации, укажи его через свойство `DynatraceConfigurationFile`.

  Создай `Directory.Build.props` в каталоге проекта Android/iOS (или общем каталоге проекта):

  ```
  <Project>



  <PropertyGroup>



  <DynatraceConfigurationFile>CUSTOM_PATH/dynatrace.config.json</DynatraceConfigurationFile>



  </PropertyGroup>



  </Project>
  ```

Таким образом, порядок использования конфигурации следующий:

1. Пользовательский путь к конфигурации через свойство `DynatraceConfigurationFile`
2. Файл конкретной конфигурации, например `dynatrace<Configuration>.config.json`
3. Имя по умолчанию `dynatrace.config.json`

Ниже приведена структура файла `dynatrace.config.json` для Android и iOS.

Android

iOS

```
{



"android": {



"autoStart": {



"applicationId": "<insertApplicationID>",



"beaconUrl": "<insertBeaconURL>"



},



"userOptIn": true,



"agentBehavior": {



"startupLoadBalancing": true



}



}



}
```

```
{



"ios": {



"DTXApplicationId": "<insertApplicationID>",



"DTXBeaconUrl": "<insertBeaconURL>",



"DTXUserOptIn": true,



"DTXStartupLoadBalancing": true



}



}
```

Никогда не использовать нотацию через точку для файла конфигурации. Всегда писать в полном стиле со скобками.

## Включение отладочных логов OneAgent

Если инструментирование прошло успешно и приложение запускается, но данные в среде Dynatrace не отображаются, скорее всего нужно копнуть глубже, чтобы выяснить, почему OneAgentы не отправляют данные. Открыть тикет в поддержку, это хорошая идея, но сначала лучше собрать логи.

Android

iOS

Обнови [файл `dynatrace.config.json`](#config-file), чтобы включить отладочные логи OneAgent.

```
{



"android": {



"autoStart": {



"applicationId": "<insertApplicationID>",



"beaconUrl": "<insertBeaconURL>"



},



"userOptIn": true,



"debug": {



"agentLogging": true



}



}



}
```

Добавь следующий фрагмент конфигурации в [файл `dynatrace.config.json`](#config-file):

```
{



"ios": {



"DTXApplicationId": "<insertApplicationID>",



"DTXBeaconUrl": "<insertBeaconURL>",



"DTXUserOptIn": true,



"DTXLogLevel": "ALL"



}



}
```

## Включение отладочных логов сборки для Android

Только Android

Если инструментирование Android завершается ошибкой, скорее всего, нужно открыть тикет в поддержку и предоставить отладочные логи сборки. Чтобы предоставить эти логи, нужно задать свойство `DynatraceInstrumentationLogging` и изменить уровень логирования сборки на `Diagnostic`.

1. Задай свойство `DynatraceInstrumentationLogging`. Выбери один из следующих способов, чтобы это сделать:

   * Создай `Directory.Build.props` в каталоге проекта Android:

   ```
   <Project>



   <PropertyGroup>



   <DynatraceInstrumentationLogging>true</DynatraceInstrumentationLogging>



   </PropertyGroup>



   </Project>
   ```

   * Добавь свойство `DynatraceInstrumentationLogging` в файл `.csproj` своего проекта. Вставь его в одну из существующих групп `PropertyGroup`, в зависимости от конфигурации, которую ты выполняешь.
2. Измени уровень детализации вывода сборки на `Diagnostic`. Подробности см. в документации Microsoft о том, как [изменить объём информации, включаемой в лог сборки﻿](https://docs.microsoft.com/en-us/visualstudio/ide/how-to-view-save-and-configure-build-log-files?view=vs-2019#to-change-the-amount-of-information-included-in-the-build-log).
3. Пересобери проект.
4. Приложи логи сборки к тикету в поддержку, чтобы можно было дополнительно проанализировать проблему.

## Устранение неполадок

Если проблему не удаётся решить, см. [Мобильные приложения: проблемы с NuGet-пакетом Dynatrace .NET MAUI﻿](https://dt-url.net/sy038sw) в сообществе Dynatrace.

## Похожие темы

* [Инструментирование Android-приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app "Learn how to instrument mobile application monitoring on Android, how to customize instrumentation and more.")
* [Инструментирование iOS-приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app "Instrument mobile application monitoring for iOS apps, customize the auto-instrumentation, and capture additional data via manual instrumentation.")