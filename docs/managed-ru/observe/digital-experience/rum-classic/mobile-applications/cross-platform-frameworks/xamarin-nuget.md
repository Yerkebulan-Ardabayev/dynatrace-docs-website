---
title: Инструментирование мобильных приложений с помощью NuGet-пакета Dynatrace Xamarin в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/xamarin-nuget
---

# Инструментирование мобильных приложений с помощью NuGet-пакета Dynatrace Xamarin в RUM Classic

# Инструментирование мобильных приложений с помощью NuGet-пакета Dynatrace Xamarin в RUM Classic

* Практическое руководство
* 12 минут на чтение
* Обновлено 22 июня 2026 г.

NuGet-пакет Dynatrace Xamarin помогает автоматически инструментировать приложение Xamarin с помощью OneAgent для Android и iOS, а также предоставляет API для [ручного инструментирования](#usage-mobile-agent). Пакет совместим с проектами `Xamarin.iOS`, `Xamarin.Android` и `Xamarin.Forms`.

Устаревание и окончание поддержки NuGet-пакета Dynatrace Xamarin

1 мая 2024 года [Microsoft прекратит поддержку всех SDK Xamarin﻿](https://dotnet.microsoft.com/en-us/platform/support/policy/xamarin#microsoft-support). По этой причине в мае 2024 года прекращается поддержка NuGet-пакета Dynatrace Xamarin, он переходит в статус устаревшего. Мы сообщим, начиная с какой версии пакета будут исправляться только ошибки и устраняться важные проблемы безопасности.

Кроме того, в соответствии с [политикой поддержки Dynatrace﻿](https://www.dynatrace.com/company/trust-center/support-policy/), поддержка NuGet-пакета Dynatrace Xamarin будет прекращена в мае 2025 года.

Рекомендуется [перевести проекты Xamarin на .NET﻿](https://learn.microsoft.com/en-gb/dotnet/maui/migration) и использовать [NuGet-пакет Dynatrace .NET MAUI](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/maui "Мониторинг приложений .NET MAUI с помощью Dynatrace OneAgent.") вместо устаревшего NuGet-пакета Xamarin.

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

* **Для Android:**

  + Android версии 6.0+ (API 23+)
  + SDK Xamarin.Android версии 10.1.x+
* **Для iOS:** iOS версии 15+
* **Для Xamarin.Forms:** .NET Standard версии 2.0+

## Настройка пакета

Для настройки NuGet-пакета Dynatrace Xamarin в приложении Xamarin нужно выполнить следующие шаги.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Установка NuGet-пакета Dynatrace Xamarin**](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/xamarin-nuget#install-package "Мониторинг приложений Xamarin с помощью Dynatrace OneAgent.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Создание приложения и получение файла конфигурации**](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/xamarin-nuget#installation-dynatrace "Мониторинг приложений Xamarin с помощью Dynatrace OneAgent.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Добавление файла конфигурации в проект**](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/xamarin-nuget#configure-app "Мониторинг приложений Xamarin с помощью Dynatrace OneAgent.")[![Шаг 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Шаг 4")

**Добавление метода запуска OneAgent**](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/xamarin-nuget#start-method "Мониторинг приложений Xamarin с помощью Dynatrace OneAgent.")[![Шаг 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Шаг 5")

Только для Xamarin.Forms

**Настройка Xamarin.Forms DependencyService**](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/xamarin-nuget#usage-forms "Мониторинг приложений Xamarin с помощью Dynatrace OneAgent.")[![Шаг 6 необязательный](https://dt-cdn.net/images/dotted-step-6-fbd29ea893.svg "Шаг 6 необязательный")

**Включение автоматического инструментирования веб-запросов**](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/xamarin-nuget#http-client "Мониторинг приложений Xamarin с помощью Dynatrace OneAgent.")

### Шаг 1 Установка NuGet-пакета

Добавить NuGet-пакет Dynatrace Xamarin во все нужные проекты.

1. В Visual Studio щёлкнуть правой кнопкой мыши по основному проекту приложения и выбрать **Manage NuGet packages**.
2. Найти [**Dynatrace.OneAgent.Xamarin** на nuget.org﻿](https://www.nuget.org/packages/Dynatrace.OneAgent.Xamarin) и выбрать **Add Package**.
3. Отметить флажками все проекты, в которые нужно добавить NuGet-пакет.
4. Выбрать **OK**.

### Шаг 2 Создание приложения и получение файла конфигурации

Создать новое мобильное приложение в Dynatrace и скачать файл конфигурации.

1. В Dynatrace перейти в **Mobile**.
2. Выбрать **Create mobile app**.
3. Ввести имя приложения и выбрать **Create mobile app**. Откроется страница настроек приложения.
4. На странице настроек приложения выбрать **Instrumentation wizard** > **Xamarin**.
5. На шаге 2 выбрать **Download dynatrace.config.json**, чтобы скачать файл конфигурации.

### Шаг 3 Добавление файла конфигурации в проект

Добавить в проект [файл `dynatrace.config.json`](#config-file), скачанный на предыдущем шаге.

Android

iOS

Добавить файл `dynatrace.config.json` в каталог `Assets` проекта Android.

Добавить файл `dynatrace.config.json` в каталог `Resources` проекта iOS.

Перед каждой сборкой пакет автоматически создаёт новый файл `Dynatrace.plist` на основе параметров, заданных в файле конфигурации.

### Шаг 4 Добавление метода запуска OneAgent

Для запуска OneAgent требуется метод запуска.

Android

iOS

```
using Dynatrace.Xamarin;



Agent.Instance.Start();
```

```
using Dynatrace.Xamarin;



Agent.Instance.Start();
```

### Шаг 5 Настройка `DependencyService` Xamarin.Forms

Только для Xamarin.Forms

Эта инструкция предназначена для версий Xamarin.Forms 4.7.0+, использующих `RegisterSingleton`. Для более ранних версий Xamarin.Forms см. [инструкцию ниже](#xamarin-forms-4-6).

Зарегистрировать интерфейс при запуске в нативной части приложения Xamarin.Forms, вставив следующий код сразу после `Forms.Init()`.

Пример ниже приведён для приложения Android Forms:

```
using Dynatrace.Xamarin;



Xamarin.Essentials.Platform.Init(this, savedInstanceState);



global::Xamarin.Forms.Forms.Init(this, savedInstanceState);



Xamarin.Forms.DependencyService.RegisterSingleton<IDynatrace>(Agent.Instance);



LoadApplication(new App());
```

Следующий код в приложении Xamarin.Forms открывает доступ к OneAgent:

```
using Dynatrace.Xamarin;



IDynatrace dynatrace = DependencyService.Get<IDynatrace>();
```

При автоматическом инструментировании необходимо также применить NuGet-пакет Dynatrace Xamarin к нативным частям приложения.

Xamarin.Forms 4.6.0 и более ранние версии

Если использовать `DependencyService.RegisterSingleton` нельзя, поскольку версия Xamarin.Forms 4.6.0 или более ранняя, есть обходной путь. Следующий фрагмент кода показывает, как это работает для Xamarin.Forms и Android, но его несложно применить и для iOS.

Файл `App.xaml.cs` в части Xamarin.Forms:

```
public partial class App : Application



{



static readonly Dictionary<Type, Func<object, object>> factories = new Dictionary<Type, Func<object, object>>();



public App()



{



InitializeComponent();



DependencyResolver.ResolveUsing((type, args) => factories.ContainsKey(type) ? factories[type].Invoke(args) : null);



IDynatrace Dynatrace = DependencyService.Resolve<IDynatrace>();



Dynatrace.Start(null);



}



public static void Register(Type type, Func<object, object> factory)



{



factories[type] = factory;



}



...



}
```

Часть Android, в которой нужно вызвать `RegisterSingleton`, должна выглядеть так:

```
public class MainActivity : global::Xamarin.Forms.Platform.Android.FormsAppCompatActivity



{



protected override void OnCreate(Bundle savedInstanceState)



{



...



Xamarin.Essentials.Platform.Init(this, savedInstanceState);



global::Xamarin.Forms.Forms.Init(this, savedInstanceState);



App.Register(typeof(IDynatrace), (o) => Agent.Instance);



LoadApplication(new App());



}



...



}
```

### Шаг 6 необязательный Включение автоматического инструментирования веб-запросов Необязательно

При желании можно использовать следующий метод, чтобы включить автоматическое инструментирование веб-запросов. `HttpMessageHandler`, используемый `HttpClient`, берёт на себя ручное инструментирование веб-запросов.

```
using Dynatrace.Xamarin;



var httpHandler = Agent.Instance.GetHttpMessageHandler();



var httpClient = new HttpClient(httpHandler);
```

Кроме того, можно использовать и собственный HTTP-обработчик:

```
using Dynatrace.Xamarin;



var defaultHttpHandler = new HttpClientHandler();



var httpHandler = Agent.Instance.GetHttpMessageHandler(defaultHttpHandler);



var httpClient = new HttpClient(httpHandler);
```

## Ручное инструментирование

В разделах ниже описано, как запустить OneAgent вручную, создавать пользовательские действия, инструментировать веб-запросы, а также отправлять значения, события и сбои.

### Запуск OneAgent

Можно использовать ручной запуск с конфигуратором (Android) или словарём конфигурации (iOS).

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

   Не добавляй дополнительные свойства в файл конфигурации. Если это сделать, сборка завершится с исключением.
2. Запустить OneAgent вручную и передать необходимые свойства.

   Android

   iOS

   ```
   using Dynatrace.Xamarin;



   Agent.Instance.Start(new ConfigurationBuilder("<insertBeaconURL>","<insertApplicationID>") .BuildConfiguration());
   ```

   ```
   using Dynatrace.Xamarin;



   var configDict = new Dictionary<string, object>();



   configDict.Add("DTXApplicationID", "<insertApplicationID>");



   configDict.Add("DTXBeaconURL", "<insertBeaconURL");



   Agent.Instance.Start(configDict);
   ```

### Создание пользовательских действий (custom actions)

Можно создавать пользовательские действия и дополнять их информацией, такой как значения, события и ошибки.

Вызови `EnterAction`, чтобы начать пользовательское действие, и `LeaveAction`, чтобы закрыть его. Время измеряется автоматически.

```
using Dynatrace.Xamarin;



var myAction = Agent.Instance.EnterAction("Tap on Confirm");



//Perform the action and whatever else is needed.



myAction.LeaveAction();
```

Для мобильного пользовательского действия или автоматически сгенерированного мобильного действия пользователя максимальная длина имени составляет 250 символов.

Информацию об именовании действий пользователя смотри по ссылкам: [Android](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#user-action-naming "Configure the Dynatrace Android Gradle plugin to adjust the monitoring capabilities of OneAgent.") и [iOS](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#user-action-naming "Enrich mobile user experience monitoring using OneAgent SDK for iOS.").

Если для приложения включён [режим согласия пользователя (opt-in)](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region."), это может повлиять на тегирование пользователей и отчётность по пользовательским событиям, действиям пользователя, значениям и ошибкам. Точные типы данных, которые не передаются в Dynatrace, зависят от уровня сбора данных, установленного конкретным пользователем. Подробности смотри в разделе [Уровни сбора данных](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.").

### Создание дочерних действий

Помимо создания самостоятельных пользовательских действий, можно также создавать [дочерние действия](/managed/observe/digital-experience/rum-classic/rum-concepts/user-actions#child-actions "Learn what user actions are and how they help you understand what users do with your application.").

Дочерние действия похожи на родительские пользовательские действия. Когда родительское действие закрывается, все его дочерние действия закрываются автоматически.

```
using Dynatrace.Xamarin;



var myAction = Agent.Instance.EnterAction("Tap on Confirm");



var mySubAction = myAction.EnterAction("Tap on Confirm again");



//Perform the action and whatever else is needed.



mySubAction.LeaveAction();



myAction.LeaveAction();
```

Для мобильного пользовательского действия или автоматически сгенерированного мобильного действия пользователя максимальная длина имени составляет 250 символов.

Ограничения на количество дочерних действий, прикреплённых к пользовательскому действию, нет. Однако учти, что доступен только один уровень дочерних действий: нельзя создать дочернее действие для другого дочернего действия (у дочерних действий не может быть собственных дочерних действий). Также смотри [Структура пользовательской сессии для отдельного пользователя](/managed/observe/digital-experience/rum-classic/rum-concepts/user-session#session-structure-dep-on-app-type "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.").

Дочерние действия не отображаются на [странице сведений о пользовательской сессии](/managed/observe/digital-experience/rum-classic/session-segmentation/user-sessions#session-details-page "Learn about user session segmentation and filtering attributes."), но их можно посмотреть на [странице waterfall-анализа](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/waterfall-analysis "Learn how to analyze all user action monitoring data through waterfall analysis.") для пользовательского действия, к которому прикреплены эти дочерние действия.

### Отмена пользовательских действий

Если нужно отменить уже созданное, но ещё не закрытое пользовательское действие, вызови `Cancel`. Отмена действия приводит к удалению всех связанных с ним данных: все отправленные значения, события и ошибки отбрасываются, все дочерние действия отменяются.

```
using Dynatrace.Xamarin;



var myAction = Agent.Instance.EnterAction("Tap on Confirm");



// Action is canceled



myAction.Cancel();
```

Закрытое действие отменить нельзя, поэтому вызов `Cancel` после `LeaveAction` для того же действия невозможен. То же самое касается закрытия отменённого действия: нельзя вызвать `LeaveAction` после использования `Cancel` для того же действия.

### Инструментирование веб-запросов

Используй следующий фрагмент кода для инструментирования веб-запросов:

```
using Dynatrace.Xamarin;



// Create an action



var webAction = Agent.Instance.EnterAction(actionName: "WebRequest Action");



// Generate a new unique tag associated with the web request action



string requestTag = webAction.GetRequestTag(url);



string requestTagHeader = webAction.GetRequestTagHeader();



// Place the Dynatrace HTTP header on your web request



httpClient.DefaultRequestHeaders.Add(requestTagHeader, requestTag);



// Generate a WebRequestTiming object based on the unique tag



WebRequestTiming timing = (WebRequestTiming)Agent.Instance.GetWebRequestTiming(requestTag, url);



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

### Отправка значения

Метод `reportValue` позволяет отправлять пары «ключ-значение» метаданных, которые впоследствии можно посмотреть в веб-интерфейсе Dynatrace и преобразовать в [свойства пользовательского действия и пользовательской сессии](/managed/observe/digital-experience/rum-classic/mobile-applications/analyze-and-use/action-and-session-properties-mobile "User action and session properties, which are metadata key-value pairs, provide added visibility and deeper analysis of your end users' experience. Using these properties for your applications, you can filter user sessions, add calculated metrics, create charts, and more."). Отправляемые значения должны быть частью пользовательского действия.

Можно отправлять значения следующих типов данных:

* `int`
* `double`
* `string`

```
ReportValue(valueName: string, value: int);



ReportValue(valueName: string, value: double);



ReportValue(valueName: string, value: string);
```

Например, чтобы отправить значение типа `string` в рамках действия `Tap on Confirm`, используй следующий код:

```
using Dynatrace.Xamarin;



var myAction = Agent.Instance.EnterAction("Tap on Confirm");



myAction.ReportValue("Customer type", "Gold");



myAction.LeaveAction();
```

Чтобы посмотреть отправленные значения в веб-интерфейсе Dynatrace, перейди к сведениям о пользовательском действии, которое должно содержать эти метаданные, и прокрути вниз до раздела **Reported values**.

![Страница сведений о пользовательском действии со значениями, отправленными SDK](https://dt-cdn.net/images/user-action-details-with-reported-values-2048-b44e8bca3e.png)

Страница сведений о пользовательском действии со значениями, отправленными SDK

Чтобы добавить свойства действия и сессии на основе отправленных значений, а затем использовать эти свойства для создания сложных запросов, сегментаций и агрегаций, смотри [Определение свойств пользовательского действия и пользовательской сессии для мобильных приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/define-mobile-action-and-session-properties "Send metadata to Dynatrace and define action and session properties for your monitored mobile applications.").

Если для приложения включён [режим согласия пользователя (opt-in)](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region."), это может повлиять на тегирование пользователей и отчётность по пользовательским событиям, действиям пользователя, значениям и ошибкам. Точные типы данных, которые не передаются в Dynatrace, зависят от уровня сбора данных, установленного конкретным пользователем. Подробности смотри в разделе [Уровни сбора данных](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.").

### Отправка события

Для любого открытого действия можно сообщить о событии. Используется следующий вызов API:

```
ReportEvent(eventName: string);
```

Если для приложения включен [режим согласия пользователя](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region."), это может повлиять на тегирование пользователей и отправку пользовательских событий, действий пользователя, значений и ошибок. Конкретные типы данных, которые не отправляются в Dynatrace, зависят от уровня сбора данных, установленного конкретным пользователем. Подробности приведены в разделе [Уровни сбора данных](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.").

### Отправка сообщения об ошибке

Чтобы отправить сообщение об [ошибке](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#error "Learn about user and error events and the types of user and error events captured by Dynatrace."), используется метод `ReportError`.

```
ReportError(errorName: string, errorCode: number);
```

Если для приложения включен [режим согласия пользователя](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region."), это может повлиять на тегирование пользователей и отправку пользовательских событий, действий пользователя, значений и ошибок. Конкретные типы данных, которые не отправляются в Dynatrace, зависят от уровня сбора данных, установленного конкретным пользователем. Подробности приведены в разделе [Уровни сбора данных](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.").

### Отправка трассировки стека ошибки

Чтобы отправить трассировку стека ошибки, используется следующий вызов API:

```
using Dynatrace.Xamarin;



Agent.Instance.ReportErrorStacktrace("Error_Class", "Error_Value", "Error_Reason", "Error_Stacktrace");
```

### Отправка сообщения о сбое

Чтобы отправить сообщение о [сбое](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#crash "Learn about user and error events and the types of user and error events captured by Dynatrace."), используется следующий вызов API.

```
using Dynatrace.Xamarin;



Agent.Instance.ReportCrash("CrashWithoutException", "Crash_Reason", "Crash_Stacktrace");
```

Также можно использовать объект исключения:

```
using Dynatrace.Xamarin;



Agent.Instance.ReportCrashWithException("CrashWithExceptionObj", exception);
```

Момент, когда сведения о сбое отправляются в Dynatrace, зависит от операционной системы мобильного приложения.

* **Android**

  Как правило, сведения о сбое отправляются сразу после сбоя, поэтому пользователю не нужно перезапускать приложение. Однако в некоторых случаях приложение нужно открыть заново в течение 10 минут, чтобы отчет о сбое был отправлен. Обрати внимание, что Dynatrace не отправляет отчеты о сбоях старше 10 минут (такие отчеты уже не могут быть сопоставлены на кластере Dynatrace).
* **iOS**

  Сведения о сбое отправляются только тогда, когда пользователь открывает мобильное приложение заново (то есть при следующем запуске приложения). Однако если пользователь не открывает приложение в течение 10 минут, отчет о сбое удаляется. Это связано с тем, что Dynatrace не отправляет отчеты о сбоях старше 10 минут (такие отчеты уже не могут быть сопоставлены на кластере Dynatrace).

Отправка сообщения о сбое принудительно завершает пользовательский сеанс. Любые последующие действия включаются в новый пользовательский сеанс.

Только для Android При использовании автоматической отправки сообщений о сбоях Visual Studio может перехватить исключение раньше OneAgent. Если заметно, что Dynatrace не отправляет сообщения о сбоях в среду, убедись, что [не используется опция отладки в Visual Studio](#debugger-turn-off). В противном случае отладчик перехватывает сбой, и ничего не отправляется в среду Dynatrace.

### Тегирование конкретных пользователей

Каждого пользователя приложения можно пометить уникальным именем пользователя. Это позволяет искать и фильтровать сеансы конкретных пользователей и анализировать поведение отдельного пользователя во времени. Подробнее см. [Тегирование пользователей](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#user-tagging "Learn about user and error events and the types of user and error events captured by Dynatrace.").

Чтобы пометить текущий сеанс определенным именем, выполни следующий вызов API:

```
using Dynatrace.Xamarin;



Agent.Instance.IdentifyUser("John Smith");
```

OneAgent для Android версии 237+ OneAgent для iOS версии 235+ Сеансы, разделенные из-за таймаута бездействия или длительности, автоматически перетегируются.

Когда OneAgent завершает помеченный сеанс из-за достижения установленного предела длительности сеанса или из-за неактивности пользователя, последующий сеанс автоматически перетегируется. Повторно указывать сведения об идентификации пользователя не нужно.

Однако обрати внимание, что OneAgent не перетегирует последующий сеанс в следующих случаях:

* Когда помеченный пользовательский сеанс явно завершается через [`endVisit`](#end-session)
* Когда пользователь или мобильная операционная система закрывает или принудительно останавливает приложение
* Когда OneAgent завершает текущий пользовательский сеанс и создает новый сеанс после изменения настроек конфиденциальности

См. [Пользовательские сеансы > Завершение сеанса](/managed/observe/digital-experience/rum-classic/rum-concepts/user-session#user-session-end--mobile-apps "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more."), чтобы узнать, когда OneAgent завершает мобильный пользовательский сеанс.

Если для приложения включен [режим согласия пользователя](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region."), это может повлиять на тегирование пользователей и отправку пользовательских событий, действий пользователя, значений и ошибок. Конкретные типы данных, которые не отправляются в Dynatrace, зависят от уровня сбора данных, установленного конкретным пользователем. Подробности приведены в разделе [Уровни сбора данных](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.").

### Завершение сеанса

Можно принудительно завершить сеанс через вызов API. Это также закрывает все открытые действия и запускает новый сеанс.

```
using Dynatrace.Xamarin;



Agent.Instance.EndVisit();
```

### Настройка конфиденциальности данных (режим согласия)

С режимом user opt-in каждый пользователь приложения может задать свои настройки приватности данных и решить, хочет ли он делиться своей информацией. Если режим opt-in включён, нужно запросить у каждого пользователя разрешение на сбор его данных, а затем сохранить его настройки приватности. Подробнее см. в разделе [User opt-in mode](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.").

#### Включение режима user opt-in

Чтобы активировать режим user opt-in, установите свойство `userOptIn` (Android) или [ключ конфигурации `DTXUserOptIn`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#privacy-and-security "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") (iOS) в значение `true` в [файле `dynatrace.config.json`](#config-file).

#### Получение настроек приватности данных пользователя

Можно получить настройки приватности данных конкретного пользователя.

Чтобы получить текущую конфигурацию `UserPrivacyOptions`, используйте следующий вызов API:

```
using Dynatrace.Xamarin;



// Get the UserPrivacyOptions object



UserPrivacyOptions currentOptions = Agent.Instance.GetUserPrivacyOptions();



// Get the individual settings for DataCollectionLevel and crash reporting



bool crashOptedIn = Agent.Instance.GetUserPrivacyOptions().CrashReportingOptedIn;



DataCollectionLevel dataCollectionLevel = Agent.Instance.GetUserPrivacyOptions().DataCollectionLevel;
```

#### Изменение настроек приватности данных пользователя

Можно скорректировать настройки приватности данных на основе решения конкретного пользователя.

Чтобы задать новые настройки в объекте `UserPrivacyOptions`, используйте следующий код:

```
using Dynatrace.Xamarin;



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

Чтобы применить новую конфигурацию `UserPrivacyOptions`, используйте этот код:

```
using Dynatrace.Xamarin;



UserPrivacyOptions options = new UserPrivacyOptions(DataCollectionLevel.UserBehavior, true);



Agent.Instance.ApplyUserPrivacyOptions(options);
```

Возможные значения для [уровня сбора данных](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.") следующие:

* `Off`
* `Performance`
* `UserBehavior`

### Передача GPS-координат

Можно передавать широту и долготу.

```
SetGPSLocation(latitude: double, longitude: double);
```

## Файл конфигурации

Файл конфигурации `dynatrace.config.json` содержит ID приложения, beacon URL и некоторые другие настройки.

* Этот файл можно [скачать из Dynatrace](#installation-dynatrace) или создать вручную.
* Если не добавить файл конфигурации хотя бы со свойствами beacon URL и ID приложения, сборка завершится с ошибкой. Как вариант, можно использовать [ручной запуск](#start-agent) с построителем конфигурации (Android) или словарём конфигурации (iOS).
* При использовании определённой конфигурации сборки, например `Debug`, `Release` или пользовательской конфигурации, наш пакет ищет в директории `Assets` (Android) или `Resources` (iOS) файл конфигурации с именем `dynatrace<Configuration>.config.json`. Например, при использовании конфигурации сборки `Debug` пакет ищет файл с именем `dynatraceDebug.config.json`.
* Если нужно задать пользовательский путь для конфигурации, установите его через свойство `DynatraceConfigurationFile`.

  Создайте `Directory.Build.props` в директории проекта Android/iOS (или общей директории проекта):

  ```
  <Project>



  <PropertyGroup>



  <DynatraceConfigurationFile>CUSTOM_PATH/dynatrace.config.json</DynatraceConfigurationFile>



  </PropertyGroup>



  </Project>
  ```

В итоге получается следующий порядок, в котором будет использоваться конфигурация:

1. Пользовательский путь к конфигурации через свойство `DynatraceConfigurationFile`
2. Файл, специфичный для конфигурации, например `dynatrace<Configuration>.config.json`
3. Имя по умолчанию `dynatrace.config.json`

Далее приведена структура файла `dynatrace.config.json` для Android и iOS.

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

Никогда не используйте точечную нотацию для файла конфигурации. Всегда пишите в полном стиле со скобками.

## Включение отладочных логов OneAgent

Если инструментация прошла успешно и приложение запускается, но данные в вашей среде Dynatrace не отображаются, вероятно, нужно копнуть глубже, чтобы выяснить, почему OneAgentы не отправляют данные. Открыть тикет в службу поддержки, это хорошая идея, но сначала лучше собрать логи.

Android

iOS

Обновите [файл `dynatrace.config.json`](#config-file), чтобы включить отладочные логи OneAgent.

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

## Включение отладочных логов сборки для Android

Только для Android

Если инструментация Android завершилась неудачно, скорее всего, нужно открыть тикет в службу поддержки и предоставить отладочные логи сборки. Чтобы предоставить эти логи, нужно установить свойство `DynatraceInstrumentationLogging` и изменить уровень логирования сборки на `Diagnostic`.

1. Установите свойство `DynatraceInstrumentationLogging`. Выберите один из следующих вариантов, чтобы это сделать:

   * Создайте `Directory.Build.props` в директории проекта Android:

   ```
   <Project>



   <PropertyGroup>



   <DynatraceInstrumentationLogging>true</DynatraceInstrumentationLogging>



   </PropertyGroup>



   </Project>
   ```

   * Добавьте свойство `DynatraceInstrumentationLogging` в файл `.csproj` вашего проекта. Вставьте его в существующую `PropertyGroup`, в зависимости от конфигурации, которую вы выполняете.
2. Измените подробность вывода сборки на `Diagnostic`. Подробнее см. документацию Microsoft о том, как [изменить объём информации, включаемой в лог сборки﻿](https://docs.microsoft.com/en-us/visualstudio/ide/how-to-view-save-and-configure-build-log-files?view=vs-2019#to-change-the-amount-of-information-included-in-the-build-log).
3. Пересоберите проект.
4. Приложите логи сборки к тикету в службу поддержки, чтобы мы могли дополнительно проанализировать проблему.

## Решение проблем

Если проблему не удаётся решить, ознакомьтесь со статьёй [Mobile applications: Issues with Dynatrace Xamarin NuGet package﻿](https://dt-url.net/xn638zc) в сообществе Dynatrace.

## Смежные темы

* [Инструментирование Android-приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app "Learn how to instrument mobile application monitoring on Android, how to customize instrumentation and more.")
* [Инструментирование iOS-приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app "Instrument mobile application monitoring for iOS apps, customize the auto-instrumentation, and capture additional data via manual instrumentation.")