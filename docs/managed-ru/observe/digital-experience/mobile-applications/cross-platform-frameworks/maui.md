---
title: Инструментирование мобильных приложений с помощью пакета Dynatrace .NET MAUI NuGet
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/cross-platform-frameworks/maui
scraped: 2026-05-12T11:23:27.756722
---

# Инструментирование мобильных приложений с помощью пакета Dynatrace .NET MAUI NuGet

# Инструментирование мобильных приложений с помощью пакета Dynatrace .NET MAUI NuGet

* How-to guide
* 10-min read
* Updated on Apr 03, 2026

Dynatrace version 1.265+

Пакет Dynatrace .NET MAUI NuGet помогает автоматически инструментировать мобильное приложение .NET MAUI с помощью OneAgent для Android и iOS, а также предоставляет API для [ручного инструментирования](#usage-mobile-agent).

Пакет Dynatrace .NET MAUI NuGet доступен для Android и iOS. Использовать пакет для macOS и Windows нельзя.

## Поддерживаемые функции

#### Автоматическое инструментирование

* Пользовательские действия
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
* Пользовательская маркировка

## Требования

* **Для Android:** Android версии 5.0+ (API 21+)
* **Для iOS:** iOS версии 12+

## Настройка пакета

Выполните следующие шаги для настройки пакета Dynatrace .NET MAUI NuGet для вашего мобильного приложения.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Установить пакет Dynatrace .NET MAUI NuGet**](/managed/observe/digital-experience/mobile-applications/cross-platform-frameworks/maui#install-package "Мониторинг .NET MAUI приложений с помощью Dynatrace OneAgent.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Создать приложение и получить файл конфигурации**](/managed/observe/digital-experience/mobile-applications/cross-platform-frameworks/maui#installation-dynatrace "Мониторинг .NET MAUI приложений с помощью Dynatrace OneAgent.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Добавить файл конфигурации в проект**](/managed/observe/digital-experience/mobile-applications/cross-platform-frameworks/maui#configure-app "Мониторинг .NET MAUI приложений с помощью Dynatrace OneAgent.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Добавить метод запуска OneAgent**](/managed/observe/digital-experience/mobile-applications/cross-platform-frameworks/maui#start-method "Мониторинг .NET MAUI приложений с помощью Dynatrace OneAgent.")[![Step 5 optional](https://dt-cdn.net/images/dotted-step-5-52040ae237.svg "Step 5 optional")

**Включить автоматическое инструментирование веб-запросов**](/managed/observe/digital-experience/mobile-applications/cross-platform-frameworks/maui#http-client "Мониторинг .NET MAUI приложений с помощью Dynatrace OneAgent.")

### Шаг 1. Установка пакета NuGet

Добавьте пакет Dynatrace .NET MAUI NuGet в ваше приложение.

1. В Visual Studio щёлкните правой кнопкой мыши на решении мобильного приложения и выберите **Manage NuGet packages**.
2. Найдите [**Dynatrace.OneAgent.MAUI** на nuget.org](https://www.nuget.org/packages/Dynatrace.OneAgent.MAUI) и нажмите **Add Package**.
3. Установите флажки у всех проектов, в которые нужно добавить пакет NuGet. Убедитесь, что добавляете пакет в нативные проекты, поскольку целевые файлы пакета взаимодействуют со сборкой.
4. Нажмите **OK**.

### Шаг 2. Создание приложения и получение файла конфигурации

Создайте новое мобильное приложение в Dynatrace и скачайте файл конфигурации.

1. В Dynatrace перейдите в **Mobile**.
2. Нажмите **Create mobile app**.
3. Введите имя приложения и нажмите **Create mobile app**. Откроется страница настроек приложения.
4. В настройках приложения выберите **Instrumentation wizard** > **.NET MAUI**.
5. В шаге 2 нажмите **Download dynatrace.config.json**, чтобы получить файл конфигурации.

### Шаг 3. Добавление файла конфигурации в проект

Добавьте [файл `dynatrace.config.json`](#config-file), скачанный на предыдущем шаге, в проект. Это можно сделать одним из следующих способов (перечислены в порядке от наиболее к наименее рекомендуемому).

* Добавьте файл `dynatrace.config.json` в пользовательское расположение. Укажите его через [свойство `DynatraceConfigurationFile`](#config-file).
* Добавьте файл `dynatrace.config.json` в:

  + директорию `Platforms/Android/Assets` вашего проекта (Android). Если директория `Assets` не существует, создайте её внутри `Platforms/Android`.
  + директорию `Platforms/iOS/Resources` вашего проекта (iOS). Если директория `Resources` не существует, создайте её внутри `Platforms/iOS`.
* Добавьте файл `dynatrace.config.json` в корневую директорию проекта. MSBuild автоматически задаёт корневую директорию через свойство `ProjectDir`.

При миграции проекта Xamarin на .NET и переходе на пакет Dynatrace .NET MAUI NuGet добавьте файл `dynatrace.config.json` в пользовательское расположение или корневую директорию проекта.

### Шаг 4. Добавление метода запуска OneAgent

Метод запуска необходим для старта OneAgent.

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

### Шаг 5 (необязательно). Включение автоматического инструментирования веб-запросов

Вы можете использовать следующий метод для включения автоматического инструментирования веб-запросов. `HttpMessageHandler`, используемый `HttpClient`, берёт на себя ручное инструментирование веб-запросов.

```
using Dynatrace.MAUI;



var httpHandler = Agent.Instance.GetHttpMessageHandler();



var httpClient = new HttpClient(httpHandler);
```

Кроме того, вы можете использовать собственный HTTP-обработчик:

```
using Dynatrace.MAUI;



var defaultHttpHandler = new HttpClientHandler();



var httpHandler = Agent.Instance.GetHttpMessageHandler(defaultHttpHandler);



var httpClient = new HttpClient(httpHandler);
```

## Ручное инструментирование

В разделах ниже описано, как запустить OneAgent вручную, создавать пользовательские действия, инструментировать веб-запросы, передавать значения, события и сбои.

### Запуск OneAgent

Вы можете использовать ручной запуск с построителем конфигурации (Android) или словарём конфигурации (iOS).

1. Измените [файл `dynatrace.config.json`](#config-file), чтобы отключить автозапуск OneAgent.

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

   Не добавляйте дополнительные свойства в файл конфигурации. В противном случае сборка завершится с ошибкой.
2. Запустите OneAgent вручную, передав необходимые свойства.

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

Вы можете создавать пользовательские действия и дополнять их такой информацией, как значения, события и ошибки.

Вызовите `EnterAction` для начала пользовательского действия и `LeaveAction` для его завершения. Время измеряется автоматически.

```
using Dynatrace.MAUI;



IRootAction myAction = Agent.Instance.EnterAction("Tap on Confirm");



//Perform the action and whatever else is needed.



myAction.LeaveAction();
```

Максимальная длина имени мобильного пользовательского действия (созданного вручную или автоматически) — 250 символов.

Информацию об именовании пользовательских действий см. в разделах [Android](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#user-action-naming "Настройте плагин Dynatrace Android Gradle для управления возможностями мониторинга OneAgent.") и [iOS](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#user-action-naming "Расширьте мониторинг мобильного пользовательского опыта с помощью OneAgent SDK для iOS.").

Если для вашего приложения включён [режим согласия пользователя](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Используйте настройки конфиденциальности Dynatrace для обеспечения соответствия мобильных приложений требованиям конфиденциальности данных."), это может повлиять на пользовательскую маркировку и передачу пользовательских событий, действий, значений и ошибок. Типы данных, не передаваемых в Dynatrace, зависят от уровня сбора данных, установленного конкретным пользователем. Подробнее см. в разделе [Уровни сбора данных](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Используйте настройки конфиденциальности Dynatrace для обеспечения соответствия мобильных приложений требованиям конфиденциальности данных.").

### Создание дочерних действий

Помимо самостоятельных пользовательских действий, вы также можете создавать [дочерние действия](/managed/observe/digital-experience/rum-concepts/user-actions#child-actions "Узнайте, что такое пользовательские действия и как они помогают понять, что пользователи делают в вашем приложении.").

Дочерние действия аналогичны родительским пользовательским действиям. При закрытии родительского действия все его дочерние действия закрываются автоматически.

```
using Dynatrace.MAUI;



IRootAction myAction = Agent.Instance.EnterAction("Tap on Confirm");



IAction mySubAction = myAction.EnterAction("Tap on Confirm again");



//Perform the action and whatever else is needed.



mySubAction.LeaveAction();



myAction.LeaveAction();
```

Максимальная длина имени мобильного пользовательского действия (созданного вручную или автоматически) — 250 символов.

Ограничений на количество дочерних действий у пользовательского действия нет. Однако учтите, что допускается только один уровень дочерних действий: нельзя создать дочернее действие для другого дочернего действия. Также см. [Структуру пользовательской сессии для отдельного пользователя](/managed/observe/digital-experience/rum-concepts/user-session#session-structure-dep-on-app-type "Узнайте, как определяется пользовательская сессия, когда она начинается и заканчивается, как рассчитывается её продолжительность и многое другое.").

Дочерние действия не отображаются на [странице сведений о пользовательской сессии](/managed/observe/digital-experience/session-segmentation/new-user-sessions#session-details-page "Узнайте о сегментации пользовательских сессий и атрибутах фильтрации."), но их можно просмотреть на [странице анализа водопада](/managed/observe/digital-experience/web-applications/analyze-and-use/waterfall-analysis "Узнайте, как анализировать все данные мониторинга пользовательских действий с помощью анализа водопада.") для пользовательского действия, к которому они прикреплены.

### Отмена пользовательских действий

Если нужно отменить уже созданное, но ещё не закрытое пользовательское действие, вызовите `Cancel`. При отмене действия все связанные с ним данные удаляются: переданные значения, события и ошибки; все дочерние действия также отменяются.

```
using Dynatrace.MAUI;



IRootAction myAction = Agent.Instance.EnterAction("Tap on Confirm");



// Action is canceled



myAction.Cancel();
```

Нельзя отменить закрытое действие, поэтому вызов `Cancel` после `LeaveAction` для одного и того же действия невозможен. Аналогично нельзя закрыть отменённое действие: вызов `LeaveAction` после `Cancel` для одного и того же действия также невозможен.

### Инструментирование веб-запросов

Используйте следующий фрагмент кода для инструментирования веб-запросов:

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

Метод `reportValue` позволяет передавать пары ключ-значение метаданных, которые можно просматривать в веб-интерфейсе Dynatrace и преобразовывать в [свойства пользовательских действий и сессий](/managed/observe/digital-experience/mobile-applications/analyze-and-use/action-and-session-properties-mobile "Свойства пользовательских действий и сессий — пары ключ-значение метаданных, обеспечивающие дополнительную видимость и анализ опыта конечных пользователей."). Передаваемые значения должны быть частью пользовательского действия.

Поддерживаются следующие типы данных:

* `int`
* `double`
* `string`

```
ReportValue(valueName: string, value: int);



ReportValue(valueName: string, value: double);



ReportValue(valueName: string, value: string);
```

Например, для передачи значения `string` в рамках действия `Tap on Confirm` используйте следующий код:

```
using Dynatrace.MAUI;



IRootAction myAction = Agent.Instance.EnterAction("Tap on Confirm");



myAction.ReportValue("Customer type", "Gold");



myAction.LeaveAction();
```

Чтобы просмотреть переданные значения в веб-интерфейсе Dynatrace, перейдите в сведения о пользовательском действии, которое должно содержать эти метаданные, и прокрутите вниз до раздела **Reported values**.

![User action details page with SDK-reported values](https://dt-cdn.net/images/user-action-details-with-reported-values-2048-b44e8bca3e.png)

User action details page with SDK-reported values

Чтобы добавить свойства действий и сессий на основе переданных значений и использовать их для создания мощных запросов, сегментаций и агрегаций, см. раздел [Определение свойств пользовательских действий и сессий для мобильных приложений](/managed/observe/digital-experience/mobile-applications/additional-configuration/define-mobile-action-and-session-properties "Отправляйте метаданные в Dynatrace и определяйте свойства действий и сессий для отслеживаемых мобильных приложений.").

### Передача события

Для любого открытого действия можно передать событие. Используйте следующий вызов API:

```
ReportEvent(eventName: string);
```

### Передача ошибки

Для передачи [ошибки](/managed/observe/digital-experience/rum-concepts/user-and-error-events#error "Узнайте о событиях пользователей и ошибок, а также о типах событий, захватываемых Dynatrace.") используйте метод `ReportError`.

```
ReportError(errorName: string, errorCode: number);
```

### Передача трассировки стека ошибки

Для передачи трассировки стека ошибки используйте следующий вызов API:

```
using Dynatrace.MAUI;



Agent.Instance.ReportErrorStacktrace("Error_Class", "Error_Value", "Error_Reason", "Error_Stacktrace");
```

### Передача информации о сбое

Для передачи [сбоя](/managed/observe/digital-experience/rum-concepts/user-and-error-events#crash "Узнайте о событиях пользователей и ошибок, а также о типах событий, захватываемых Dynatrace.") используйте следующий вызов API.

```
using Dynatrace.MAUI;



Agent.Instance.ReportCrash("CrashWithoutException", "Crash_Reason", "Crash_Stacktrace");
```

Вы также можете использовать объект исключения:

```
using Dynatrace.MAUI;



Agent.Instance.ReportCrashWithException("CrashWithExceptionObj", exception);
```

Время отправки деталей сбоя в Dynatrace зависит от операционной системы мобильного приложения.

* **Android**

  Как правило, детали сбоя отправляются сразу после его возникновения, и пользователю не нужно перезапускать приложение. Однако в некоторых случаях приложение должно быть открыто повторно в течение 10 минут, чтобы отчёт о сбое был отправлен. Обратите внимание, что Dynatrace не отправляет отчёты о сбоях, которым более 10 минут (такие отчёты больше не могут быть скоррелированы на кластере Dynatrace).
* **iOS**

  Детали сбоя отправляются только при следующем открытии мобильного приложения (то есть при следующем запуске). Однако если пользователь не откроет приложение в течение 10 минут, отчёт о сбое будет удалён. Это связано с тем, что Dynatrace не отправляет отчёты старше 10 минут.

Передача сбоя завершает пользовательскую сессию. Последующие действия включаются в новую пользовательскую сессию.

Только Android: при использовании автоматической отчётности о сбоях Visual Studio может перехватить исключение раньше OneAgent. Если Dynatrace не передаёт сбои в ваше окружение, убедитесь, что [вы не используете режим отладки в Visual Studio](#debugger-turn-off). В противном случае отладчик перехватывает сбой, и в ваше окружение Dynatrace ничего не передаётся.

### Маркировка конкретных пользователей

Вы можете пометить каждого пользователя мобильного приложения уникальным именем пользователя. Это позволяет искать и фильтровать конкретные пользовательские сессии и анализировать поведение отдельных пользователей со временем. Подробнее см. в разделе [Пользовательская маркировка](/managed/observe/digital-experience/rum-concepts/user-and-error-events#user-tagging "Узнайте о событиях пользователей и ошибок, а также о типах событий, захватываемых Dynatrace.").

Выполните следующий вызов API для маркировки текущей сессии конкретным именем:

```
using Dynatrace.MAUI;



Agent.Instance.IdentifyUser("John Smith");
```

OneAgent для Android версии 237+, OneAgent для iOS версии 235+: сессии, разделённые из-за простоя или превышения продолжительности, повторно маркируются автоматически.

Когда OneAgent завершает помеченную сессию по истечении установленного лимита или из-за неактивности пользователя, следующая сессия маркируется автоматически. Повторно указывать данные пользователя не нужно.

Однако OneAgent не выполняет повторную маркировку следующей сессии в следующих случаях:

* Когда вы явно завершаете помеченную пользовательскую сессию через [`endVisit`](#end-session)
* Когда пользователь или мобильная ОС закрывает или принудительно останавливает приложение
* Когда OneAgent завершает текущую пользовательскую сессию и создаёт новую после изменения настроек конфиденциальности

Информацию о том, когда OneAgent завершает мобильную пользовательскую сессию, см. в разделе [Пользовательские сессии > Завершение сессии](/managed/observe/digital-experience/rum-concepts/user-session#user-session-end--mobile-apps "Узнайте, как определяется пользовательская сессия, когда она начинается и заканчивается.").

### Завершение сессии

Вы можете принудительно завершить сессию через вызов API. При этом все открытые действия закрываются и начинается новая сессия.

```
using Dynatrace.MAUI;



Agent.Instance.EndVisit();
```

### Настройка конфиденциальности данных (режим согласия)

В режиме согласия каждый пользователь вашего приложения может настроить свои предпочтения конфиденциальности и решить, хочет ли он делиться информацией. При включённом режиме согласия необходимо запрашивать у каждого пользователя разрешение на захват данных и затем сохранять их предпочтения. Подробнее см. в разделе [Режим согласия пользователя](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Используйте настройки конфиденциальности Dynatrace для обеспечения соответствия мобильных приложений требованиям конфиденциальности данных.").

#### Включение режима согласия пользователя

Чтобы активировать режим согласия, установите свойство `userOptIn` (Android) или [ключ конфигурации `DTXUserOptIn`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#privacy-and-security "С помощью ключей конфигурации можно точно настроить автоматическое инструментирование iOS-приложений.") (iOS) в значение `true` в [файле `dynatrace.config.json`](#config-file).

#### Получение предпочтений конфиденциальности пользователя

Вы можете получать предпочтения конфиденциальности конкретного пользователя.

Чтобы получить текущую конфигурацию `UserPrivacyOptions`, используйте следующий вызов API:

```
using Dynatrace.MAUI;



// Get the UserPrivacyOptions object



UserPrivacyOptions currentOptions = Agent.Instance.GetUserPrivacyOptions();



// Get the individual settings for DataCollectionLevel and crash reporting



bool crashOptedIn = Agent.Instance.GetUserPrivacyOptions().CrashReportingOptedIn;



DataCollectionLevel dataCollectionLevel = Agent.Instance.GetUserPrivacyOptions().DataCollectionLevel;
```

#### Изменение предпочтений конфиденциальности пользователя

Вы можете изменять предпочтения конфиденциальности на основе решения конкретного пользователя.

Чтобы задать новые параметры в объекте `UserPrivacyOptions`, используйте следующий код:

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

Для применения новой конфигурации `UserPrivacyOptions` используйте следующий код:

```
using Dynatrace.MAUI;



UserPrivacyOptions options = new UserPrivacyOptions(DataCollectionLevel.UserBehavior, true);



Agent.Instance.ApplyUserPrivacyOptions(options);
```

Возможные значения [уровня сбора данных](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Используйте настройки конфиденциальности Dynatrace для обеспечения соответствия мобильных приложений требованиям конфиденциальности данных."):

* `Off`
* `Performance`
* `UserBehavior`

### Передача данных GPS

Вы можете передавать широту и долготу.

```
SetGPSLocation(latitude: double, longitude: double);
```

## Накладные расходы инструментирования

При использовании автоматического инструментирования через плагин ниже приведены примеры разницы в размере сборок release до и после инструментирования.

| Операционная система | Шаблон приложения | Версия | Размер до | Размер после | Разница |
| --- | --- | --- | --- | --- | --- |
| Android | Стандартное новое приложение | net8.0-android | 31,8 МБ | 32,4 МБ | 0,6 МБ |
| iOS | Стандартное новое приложение | net8.0-ios | 421 МБ | 426,2 МБ | 5,2 МБ |

## Файл конфигурации

Файл конфигурации `dynatrace.config.json` содержит идентификатор приложения, URL beacon и некоторые другие настройки.

* Вы можете [скачать этот файл из Dynatrace](#installation-dynatrace) или создать его вручную.
* Если не добавить файл конфигурации как минимум со свойствами URL beacon и идентификатора приложения, сборка завершится с ошибкой. Как альтернатива — используйте [ручной запуск](#start-agent) с построителем конфигурации (Android) или словарём конфигурации (iOS).
* При использовании конкретной конфигурации сборки (например, `Debug`, `Release` или пользовательской) наш пакет ищет в директории `Assets` (Android) или `Resources` (iOS) файл конфигурации с именем `dynatrace<Configuration>.config.json`. Например, при использовании конфигурации `Debug` пакет ищет файл `dynatraceDebug.config.json`.
* Если нужно указать пользовательский путь для конфигурации, задайте его через свойство `DynatraceConfigurationFile`.

  Создайте `Directory.Build.props` в директории Android/iOS (или общего) проекта:

  ```
  <Project>



  <PropertyGroup>



  <DynatraceConfigurationFile>CUSTOM_PATH/dynatrace.config.json</DynatraceConfigurationFile>



  </PropertyGroup>



  </Project>
  ```

Итоговый порядок использования конфигурации:

1. Пользовательский путь через свойство `DynatraceConfigurationFile`
2. Файл для конкретной конфигурации, например `dynatrace<Configuration>.config.json`
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

Никогда не используйте точечную нотацию в файле конфигурации. Всегда пишите в полном стиле скобок.

## Включение журналов отладки OneAgent

Если инструментирование прошло успешно и приложение запускается, но данные в окружение Dynatrace не поступают, вероятно, нужно углубиться в анализ причин. Открытие обращения в службу поддержки — хорошая идея, но сначала стоит собрать журналы.

Android

iOS

Обновите [файл `dynatrace.config.json`](#config-file), чтобы включить журналы отладки OneAgent.

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

Добавьте следующий фрагмент конфигурации в [файл `dynatrace.config.json`](#config-file):

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

## Включение журналов отладки сборки для Android

Только Android

Если инструментирование Android завершается с ошибкой, вероятно, потребуется открыть обращение в службу поддержки и предоставить журналы отладки сборки. Для этого нужно задать свойство `DynatraceInstrumentationLogging` и изменить уровень журналирования сборки на `Diagnostic`.

1. Задайте свойство `DynatraceInstrumentationLogging`. Выберите один из следующих способов:

   * Создайте `Directory.Build.props` в директории Android-проекта:

   ```
   <Project>



   <PropertyGroup>



   <DynatraceInstrumentationLogging>true</DynatraceInstrumentationLogging>



   </PropertyGroup>



   </Project>
   ```

   * Добавьте свойство `DynatraceInstrumentationLogging` в файл `.csproj` вашего проекта. Вставьте его в подходящую `PropertyGroup` в зависимости от выполняемой конфигурации.
2. Измените детализацию вывода сборки на `Diagnostic`. Подробнее см. в документации Microsoft о том, как [изменить объём информации в журнале сборки](https://docs.microsoft.com/en-us/visualstudio/ide/how-to-view-save-and-configure-build-log-files?view=vs-2019#to-change-the-amount-of-information-included-in-the-build-log).
3. Пересоберите проект.
4. Прикрепите журналы сборки к обращению в службу поддержки для дальнейшего анализа.

## Устранение неполадок

Если не удаётся решить проблему, обратитесь к разделу [Mobile applications: Issues with Dynatrace .NET MAUI NuGet package](https://dt-url.net/sy038sw) в сообществе Dynatrace.

## Связанные темы

* [Инструментирование Android-приложений](/managed/observe/digital-experience/mobile-applications/instrument-android-app "Узнайте, как инструментировать мониторинг мобильных приложений на Android.")
* [Инструментирование iOS-приложений](/managed/observe/digital-experience/mobile-applications/instrument-ios-app "Инструментируйте мониторинг мобильных приложений для iOS.")